"""
Faz 2 — Description doğrulama (Gemini 2.5 Flash).

Her mekanın mevcut Türkçe açıklamasının, GERÇEKTEN adı geçen mekanı anlatıp
anlatmadığını Gemini'nin dünya bilgisiyle kontrol eder. Tamamen dışarıdan
herhangi bir ücretli API kullanmaz — .env'deki GEMINI_API_KEY'i kullanır.

Özellikler:
  • 50'lik batch'ler ile verimli kullanım (~296 request / 14.7k mekan)
  • Resumable: sonuçlar her batch sonunda cache'e yazılır, yarıda kesilirse
    kaldığı yerden devam eder
  • Sadece temiz JSON bekler, Gemini çıktısı çöp olursa batch tekrar denenir
  • Rate-limit korumalı (default 10 RPM)

Kullanım:
  python3 tools/data_audit/verify_with_gemini.py                  # hepsini tara
  python3 tools/data_audit/verify_with_gemini.py --city madrid    # sadece madrid
  python3 tools/data_audit/verify_with_gemini.py --limit 100      # ilk 100

Çıktılar:
  tools/data_audit/gemini_verdicts.json   {pid: {verdict, reason, suggest_tr, ...}}
  tools/data_audit/report_v2.html         tüm mismatch'leri listeleyen görsel rapor
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CITIES_DIR = ROOT / "assets" / "cities"
ENV_FILE = ROOT / ".env"
OUT_DIR = ROOT / "tools" / "data_audit"
CACHE_PATH = OUT_DIR / "gemini_verdicts.json"
REPORT_HTML = OUT_DIR / "report_v2.html"

GEMINI_MODEL = "gemini-2.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

DEFAULT_BATCH = 10          # istek başına mekan sayısı (küçültüldü, daha az parse hatası için)
DEFAULT_RPM = 15            # rate limit (dakikada istek) - optimum (30'da timeout başladı)
MIN_GAP = 60.0 / DEFAULT_RPM

# ---------------------------------------------------------------------------

def load_api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("GEMINI_API_KEY"):
                _, _, v = line.partition("=")
                return v.strip().strip("\"'")
    sys.exit("❌ GEMINI_API_KEY bulunamadı (.env veya ortam değişkeni)")


def load_all_places(city_filter: str | None = None) -> list[dict]:
    out: list[dict] = []
    for f in sorted(CITIES_DIR.glob("*.json")):
        if city_filter and f.stem != city_filter:
            continue
        try:
            raw = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"⚠️  {f.name}: {e}", file=sys.stderr)
            continue
        places = raw if isinstance(raw, list) else raw.get("highlights", [])
        for p in places:
            if not isinstance(p, dict):
                continue
            pid = p.get("id") or ""
            name = (p.get("name") or "").strip()
            desc = (p.get("description") or "").strip()
            if not pid or not name or len(desc) < 20:
                continue
            out.append({
                "city": f.stem,
                "id": pid,
                "name": name,
                "category": (p.get("category") or "").strip(),
                "area": (p.get("area") or "").strip(),
                "description": desc,
                "description_en": (p.get("description_en") or "").strip(),
            })
    return out


def load_cache() -> dict[str, dict]:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(cache: dict) -> None:
    tmp = CACHE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(CACHE_PATH)


# ---------------------------------------------------------------------------
# Gemini çağrısı
# ---------------------------------------------------------------------------

PROMPT_TEMPLATE = """Sen bir veri kalite denetçisisin. Aşağıda seyahat uygulamasından mekanlar var.
Her mekan için, verilen TÜRKÇE AÇIKLAMANIN bu isimli mekanı gerçekten anlatıp
anlatmadığını kontrol et. Mekanın bulunduğu şehri de dikkate al.

Aşağıdaki kategorilerden biriyle verdict ver:
  "ok"         Açıklama bu mekanı tutarlı bir şekilde anlatıyor.
  "mismatch"   Açıklama açıkça BAŞKA bir mekanı anlatıyor (ör. başka bir şehir,
               başka tür bir yapı, tamamen farklı bir varlık). Bu en önemli
               yakalamak istediğimiz durum.
  "wrong_city" Açıklama doğru türde ama yanlış şehirden bahsediyor.
  "uncertain"  Bu mekanı yeterince tanımıyorum, emin olamam.

SADECE geçerli JSON döndür, başka bir şey yazma. Şema:
[
  {{"id":"<place_id>", "verdict":"ok|mismatch|wrong_city|uncertain", "reason":"<max 20 kelime TR>"}}
]

MEKANLAR:
{places_json}
"""


def call_gemini(api_key: str, prompt: str, timeout: int = 120) -> str:
    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.1,
            "responseMimeType": "application/json",
            "maxOutputTokens": 8192,
        },
    }
    req = urllib.request.Request(
        f"{API_URL}?key={api_key}",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        raise RuntimeError(f"Gemini response malformed: {json.dumps(data)[:500]}")


def parse_verdicts(text: str) -> list[dict]:
    text = text.strip()
    # Bazen ```json ... ``` fence'i ile döner
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.S)
    obj = json.loads(text)
    if not isinstance(obj, list):
        raise ValueError("expected JSON array")
    return obj


# ---------------------------------------------------------------------------
# Ana akış
# ---------------------------------------------------------------------------

def run(city_filter: str | None, limit: int | None, batch_size: int) -> None:
    api_key = load_api_key()
    places = load_all_places(city_filter)
    print(f"📦 {len(places)} mekan bulundu")

    cache = load_cache()
    pending = [p for p in places if p["id"] not in cache]
    print(f"🧠 Cache'te {len(cache)} var, {len(pending)} yeni kayıt sorulacak")

    if limit is not None:
        pending = pending[:limit]
        print(f"   --limit ile {len(pending)} kayıtla sınırlandı")

    if not pending:
        print("✅ Yapılacak bir şey yok, cache güncel")
        generate_report(places, cache)
        return

    total_batches = (len(pending) + batch_size - 1) // batch_size
    last_call = 0.0
    errors = 0

    for bi in range(total_batches):
        batch = pending[bi * batch_size:(bi + 1) * batch_size]
        # Rate limit
        gap = time.time() - last_call
        if gap < MIN_GAP:
            time.sleep(MIN_GAP - gap)

        # Gemini'ye gönderilecek kısa veri
        compact = [
            {
                "id": p["id"],
                "name": p["name"],
                "city": p["city"],
                "category": p["category"],
                "description_tr": p["description"][:400],
            }
            for p in batch
        ]
        prompt = PROMPT_TEMPLATE.format(places_json=json.dumps(compact, ensure_ascii=False))

        last_call = time.time()
        try:
            resp_text = call_gemini(api_key, prompt)
            verdicts = parse_verdicts(resp_text)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore")
            print(f"\n❌ HTTP {e.code}: {body[:200]}")
            if e.code == 429:
                print("   → rate limit, 60sn bekliyorum")
                time.sleep(60)
                continue
            errors += 1
            if errors > 5:
                sys.exit("Çok hata, duruyorum")
            continue
        except Exception as e:  # noqa: BLE001
            print(f"\n⚠️  Batch {bi+1} hata: {e}; retry (max 3)")
            errors += 1
            if errors > 3:
                print("❌ Çok hata, batch atlanıyor")
                errors = 0
                continue
            time.sleep(2)
            bi -= 1  # Retry same batch
            continue

        # Eşleştir
        by_id = {v.get("id"): v for v in verdicts if isinstance(v, dict)}
        for p in batch:
            v = by_id.get(p["id"])
            if v:
                cache[p["id"]] = {
                    "verdict": v.get("verdict", "uncertain"),
                    "reason": v.get("reason", "")[:200],
                    "name": p["name"],
                    "city": p["city"],
                    "category": p["category"],
                }
            else:
                cache[p["id"]] = {"verdict": "uncertain", "reason": "no response", "name": p["name"], "city": p["city"], "category": p["category"]}

        save_cache(cache)

        # İlerleme
        mm = sum(1 for v in cache.values() if v["verdict"] == "mismatch")
        wc = sum(1 for v in cache.values() if v["verdict"] == "wrong_city")
        unc = sum(1 for v in cache.values() if v["verdict"] == "uncertain")
        done = len(cache)
        print(f"  [{bi+1}/{total_batches}] batch={len(batch)} | toplam={done} | mismatch={mm} | wrong_city={wc} | uncertain={unc}")

    generate_report(places, cache)
    print(f"\n✅ Rapor: {REPORT_HTML}")


# ---------------------------------------------------------------------------
# Rapor
# ---------------------------------------------------------------------------

import html as _html


def generate_report(places: list[dict], cache: dict) -> None:
    by_id = {p["id"]: p for p in places}

    # En önemli durumlar önce
    rank = {"mismatch": 0, "wrong_city": 1, "uncertain": 2, "ok": 3}
    items = [
        (cache[pid], by_id[pid])
        for pid in cache
        if pid in by_id and cache[pid]["verdict"] in ("mismatch", "wrong_city")
    ]
    items.sort(key=lambda x: (rank.get(x[0]["verdict"], 9), x[1]["city"]))

    total = len(cache)
    counts = {
        "mismatch": sum(1 for v in cache.values() if v["verdict"] == "mismatch"),
        "wrong_city": sum(1 for v in cache.values() if v["verdict"] == "wrong_city"),
        "uncertain": sum(1 for v in cache.values() if v["verdict"] == "uncertain"),
        "ok": sum(1 for v in cache.values() if v["verdict"] == "ok"),
    }

    rows = []
    for v, p in items:
        color = "#dc2626" if v["verdict"] == "mismatch" else "#d97706"
        rows.append(f"""
<tr>
  <td class="city">{_html.escape(p['city'])}</td>
  <td>
    <div class="name">{_html.escape(p['name'])}</div>
    <div class="meta"><span class="cat">{_html.escape(p['category'])}</span> · {_html.escape(p['area'])}</div>
    <div class="desc">{_html.escape(p['description'][:400])}</div>
  </td>
  <td><span class="verdict" style="background:{color}">{v['verdict']}</span>
      <div class="why">{_html.escape(v.get('reason',''))}</div>
  </td>
  <td><a href="https://www.google.com/maps/place/?q=place_id:{_html.escape(p['id'])}" target="_blank">maps</a></td>
</tr>""")

    REPORT_HTML.write_text(f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><title>Faz 2 — description doğrulama</title>
<style>
body{{font:14px -apple-system,system-ui,sans-serif;margin:0;padding:24px;background:#f8fafc;color:#0f172a}}
h1{{margin:0 0 8px}}
.summary{{display:flex;gap:16px;margin-bottom:24px;flex-wrap:wrap}}
.stat{{background:#fff;padding:14px 18px;border-radius:10px;border:1px solid #e2e8f0}}
.stat h3{{margin:0 0 4px;font-size:11px;color:#64748b;text-transform:uppercase;letter-spacing:.05em}}
.stat .n{{font-size:28px;font-weight:700}}
table{{width:100%;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden;border:1px solid #e2e8f0}}
th,td{{padding:10px 12px;border-bottom:1px solid #f1f5f9;text-align:left;vertical-align:top;font-size:13px}}
th{{background:#f1f5f9;font-weight:600;font-size:12px;text-transform:uppercase;color:#475569}}
.city{{font-weight:600;white-space:nowrap;color:#334155}}
.name{{font-weight:600;font-size:14px}}
.meta{{color:#64748b;font-size:12px;margin:3px 0 6px}}
.cat{{display:inline-block;background:#ede9fe;color:#6d28d9;padding:1px 8px;border-radius:4px;font-size:11px}}
.desc{{font-size:12px;color:#475569;margin-top:4px;line-height:1.5}}
.verdict{{display:inline-block;color:#fff;padding:2px 10px;border-radius:4px;font-size:11px;font-weight:700;text-transform:uppercase}}
.why{{font-size:12px;color:#475569;margin-top:6px}}
a{{color:#2563eb;text-decoration:none}}
</style></head><body>
<h1>Description doğrulama raporu (Faz 2)</h1>
<p style="color:#475569;margin:0 0 20px">Toplam {total} mekan Gemini ile doğrulandı. Sadece sorunlu olanlar aşağıda.</p>
<div class="summary">
  <div class="stat"><h3>mismatch</h3><div class="n" style="color:#dc2626">{counts['mismatch']}</div></div>
  <div class="stat"><h3>wrong city</h3><div class="n" style="color:#d97706">{counts['wrong_city']}</div></div>
  <div class="stat"><h3>uncertain</h3><div class="n" style="color:#6b7280">{counts['uncertain']}</div></div>
  <div class="stat"><h3>ok</h3><div class="n" style="color:#16a34a">{counts['ok']}</div></div>
</div>
<table><thead><tr><th>şehir</th><th>mekan</th><th>verdict</th><th></th></tr></thead>
<tbody>
{''.join(rows)}
</tbody></table>
</body></html>""", encoding="utf-8")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--city", help="sadece belirli şehir")
    ap.add_argument("--limit", type=int, help="ilk N kayıtla sınırla (test için)")
    ap.add_argument("--batch", type=int, default=DEFAULT_BATCH, help=f"request başına mekan (default {DEFAULT_BATCH})")
    args = ap.parse_args()
    run(args.city, args.limit, args.batch)
