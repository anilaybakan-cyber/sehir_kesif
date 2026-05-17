"""
Faz 1 — Heuristik kategori-isim denetimi (sadeleştirilmiş).

Sadece yüksek precision kurallar:
  H1  (name-prefix)   İsim "Bar / Café / Restaurante / Museo / Palacio / Parque"
                      gibi bir tip kelimesiyle BAŞLIYOR ama kategori uyumsuz.
                      Ör. "Bar Menuda History" + kategori=Tarihi → flag.
  H2  (name-keyword)  İsmin herhangi bir yerinde güçlü bir tip kelimesi var ama
                      kategori uyumsuz (ör. "X Museum of Y" + kategori=Kafe).

Atılan kurallar (çok gürültülü bulundu):
  H3 (description başka mekandan bahsediyor) — çevre referansları meşru.
  H4 (aynı description tekrar ediyor)           — zaten 0 vaka.
  H5 (description ismi geçmiyor)                 — normal yazım tarzı.
  H6 (TR/EN özel isim uyuşmazlığı)                 — çeviri farkı.

Description'ın MEKANLA ilgili olup olmadığını heuristikle tespit etmek imkansız
(ör. Menuda "Barı"nın Kraliyet Sarayını anlatan metni). Bunun için Google Places
/ Gemini ile harici doğrulama gerek → Faz 2.

Çıktılar:
  tools/data_audit/report.json
  tools/data_audit/report.html
"""

from __future__ import annotations

import glob
import html
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Yol sabitleri
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]
CITIES_DIR = ROOT / "assets" / "cities"
OUT_DIR = ROOT / "tools" / "data_audit"
OUT_JSON = OUT_DIR / "report.json"
OUT_HTML = OUT_DIR / "report.html"

# ---------------------------------------------------------------------------
# Kategori setleri
# ---------------------------------------------------------------------------
FOOD_CATS = {"Yeme-İçme", "Kafe", "Bar", "Restoran"}
CULTURE_CATS = {"Müze", "Tarihi", "Saray", "Kültür"}
NATURE_CATS = {"Park", "Doğa", "Göl", "Manzara"}
BEACH_CATS = {"Plaj"}
SQUARE_CATS = {"Meydan"}

# İsim başındaki tip kelimeleri → zorunlu kategori havuzu
NAME_PREFIX_RULES: list[tuple[re.Pattern, set[str], str]] = [
    # İspanyolca yeme-içme
    (re.compile(r"^\s*(bar|cafetería|cafeteria|café|cafe|restaurante|pastelería|pasteleria|bodega|cervecería|cerveceria|taberna|mesón|meson|asador|churrería|churreria|heladería|heladeria|chocolatería|chocolateria|vermutería|vermuteria|coctelería|cocteleria|tapería|taperia|vinoteca|gastrobar)\b", re.I), FOOD_CATS, "İsim 'yeme-içme' kelimesiyle başlıyor"),
    # İtalyanca yeme-içme
    (re.compile(r"^\s*(ristorante|trattoria|osteria|pizzeria|gelateria|caffè|caffe|pasticceria|enoteca|paninoteca|focacceria|tavola)\b", re.I), FOOD_CATS, "İsim 'yeme-içme' kelimesiyle başlıyor"),
    # İngilizce / genel
    (re.compile(r"^\s*(pub|pizzeria|brasserie|bistro|bistrot|brewery|tavern|taproom|cocktail\s+bar|wine\s+bar|coffee\s+shop|coffee\s+house|roastery|bakery|ice\s+cream|winery)\b", re.I), FOOD_CATS, "İsim 'yeme-içme' kelimesiyle başlıyor"),
]

# İsim İÇİNDE geçerse güçlü sinyal
NAME_KEYWORD_RULES: list[tuple[re.Pattern, set[str], str]] = [
    (re.compile(r"\b(museo|museum|müze|musée|pinacoteca|galería|galeria)\b", re.I), CULTURE_CATS | {"Müze"}, "Ad 'müze' içeriyor"),
    (re.compile(r"\b(catedral|cathedral|basílica|basilica|iglesia|chiesa|duomo|katedral|kilise|cami|camii|mosque|mezquita|sinagoga|synagogue)\b", re.I), CULTURE_CATS, "Ad 'dini yapı' içeriyor"),
    (re.compile(r"\b(palacio|palace|palazzo|saray|palais)\b", re.I), CULTURE_CATS | {"Saray"}, "Ad 'saray' içeriyor"),
    (re.compile(r"\b(parque|parc|park|jardín|jardin|jardines|giardini|giardino|garden|bahçe|bahce)\b", re.I), NATURE_CATS | {"Park"}, "Ad 'park/bahçe' içeriyor"),
    (re.compile(r"\b(playa|plage|beach|plaj|spiaggia)\b", re.I), BEACH_CATS, "Ad 'plaj' içeriyor"),
    (re.compile(r"\b(plaza|piazza|meydan[ıi]?|square|place)\b", re.I), SQUARE_CATS | CULTURE_CATS, "Ad 'meydan' içeriyor"),
    (re.compile(r"\b(mercado|market|pazar|mercato|marché|marche)\b", re.I), {"Alışveriş", "Deneyim"} | FOOD_CATS, "Ad 'pazar/market' içeriyor"),
    (re.compile(r"\b(bar|café|cafe|caffè|caffe|coffee|kahve|kafe)\b", re.I), FOOD_CATS, "Ad yeme-içme anahtar kelimesi içeriyor"),
]

# ---------------------------------------------------------------------------
# Yardımcılar
# ---------------------------------------------------------------------------

_NORMALIZE_MAP = str.maketrans({
    "ı": "i", "İ": "i", "ğ": "g", "Ğ": "g", "ş": "s", "Ş": "s",
    "ç": "c", "Ç": "c", "ö": "o", "Ö": "o", "ü": "u", "Ü": "u",
    "á": "a", "à": "a", "â": "a", "ä": "a",
    "é": "e", "è": "e", "ê": "e", "ë": "e",
    "í": "i", "ì": "i", "î": "i", "ï": "i",
    "ó": "o", "ò": "o", "ô": "o", "õ": "o",
    "ú": "u", "ù": "u", "û": "u",
    "ñ": "n", "ý": "y",
})


def norm(s: str) -> str:
    """Lower + aksan/diakritik çöz + fazla boşlukları kaldır."""
    if not s:
        return ""
    return re.sub(r"\s+", " ", s.translate(_NORMALIZE_MAP).lower()).strip()


STOPWORDS = {
    # TR
    "ve", "ile", "bir", "bu", "da", "de", "en", "için", "çok", "o", "ki",
    # ES
    "el", "la", "los", "las", "de", "del", "y", "en", "un", "una",
    # IT
    "il", "lo", "gli", "le", "di", "da", "dei", "delle", "e",
    # EN
    "the", "and", "of", "to", "a", "an", "in", "at", "on", "for", "with",
    # Kategori kelimeleri (token olarak description'da olsa bile bilgi yok)
    "bar", "cafe", "café", "caffe", "caffè", "coffee", "restaurant", "restaurante",
    "ristorante", "museum", "museo", "müze", "park", "parque", "palace", "palacio",
    "plaza", "piazza", "church", "iglesia", "cathedral", "catedral", "basilica",
    "basílica", "market", "mercado", "beach", "playa",
}


def tokens(s: str, min_len: int = 4) -> list[str]:
    """İsimden anlamlı token'lar çıkar."""
    ns = norm(s)
    return [t for t in re.findall(r"[a-z0-9]+", ns) if len(t) >= min_len and t not in STOPWORDS]


def distinctive_tokens(name: str) -> list[str]:
    """
    İsimdeki ayırt edici token'lar. Örn. "Bar Menuda History" → ['menuda','history'].
    Kısa veya jenerik sözcükler elenir.
    """
    ts = tokens(name, min_len=4)
    # Roma rakamları vs. çok kısa — zaten min_len=4 elemiş olur
    return ts[:6]


def build_city_name_index(places: list[dict]) -> list[tuple[str, str]]:
    """Her place için (normalized_name, id) listesi. Cross-talk için kullanılır."""
    idx = []
    for p in places:
        nm = (p.get("name") or "").strip()
        if not nm:
            continue
        # Tip kelimesini baştan at (Bar/Café/Restaurante vs) — "Menuda History" kalsın
        stripped = re.sub(
            r"^\s*(bar|café|cafe|cafetería|cafeteria|restaurante|ristorante|trattoria|osteria|pizzeria|pastelería|pasteleria|pasticceria|gelateria|heladería|heladeria|taberna|mesón|meson|asador|churrería|churreria|bodega|cervecería|cerveceria|enoteca|vinoteca|caffè|caffe|museo|museum|müze|palacio|palace|palazzo|saray|parque|parc|park|jardín|jardin|plaza|piazza|meydanı|meydani|catedral|cathedral|basílica|basilica|iglesia|chiesa|el|la|los|las|il|lo|gli|le|the)\s+",
            "", nm, flags=re.I,
        )
        idx.append((norm(stripped), p.get("id") or nm))
    return idx


# ---------------------------------------------------------------------------
# Audit ana akışı
# ---------------------------------------------------------------------------

def audit_city(city_file: Path) -> list[dict]:
    raw = json.loads(city_file.read_text(encoding="utf-8"))
    places = raw if isinstance(raw, list) else raw.get("highlights", [])
    if not isinstance(places, list):
        return []

    city_key = city_file.stem
    name_idx = build_city_name_index(places)

    # H4: description → kaç farklı mekanda kullanılıyor
    desc_counter: Counter[str] = Counter()
    for p in places:
        d = (p.get("description") or "").strip()
        if len(d) > 40:
            desc_counter[d] += 1

    findings: list[dict] = []

    for p in places:
        if not isinstance(p, dict):
            continue
        name = (p.get("name") or "").strip()
        cat = (p.get("category") or "").strip()
        desc_tr = (p.get("description") or "").strip()
        desc_en = (p.get("description_en") or "").strip()
        pid = p.get("id") or ""

        flags: list[dict] = []

        # H1 — İsim yeme-içme/müze/saray/park gibi bir tip kelimesiyle BAŞLIYOR
        #      ama kategori uyumsuz. Çok yüksek precision.
        hit_h1 = False
        for pat, req_cats, why in NAME_PREFIX_RULES:
            if pat.search(name) and cat not in req_cats:
                flags.append({
                    "rule": "H1",
                    "severity": "high",
                    "why": why,
                    "suggest_category_in": sorted(req_cats),
                })
                hit_h1 = True
                break

        # H2 — Ad İÇİNDE güçlü bir tip kelimesi var ama kategori uyumsuz
        if not hit_h1:
            for pat, req_cats, why in NAME_KEYWORD_RULES:
                if pat.search(name) and cat not in req_cats:
                    flags.append({
                        "rule": "H2",
                        "severity": "medium",
                        "why": why,
                        "suggest_category_in": sorted(req_cats),
                    })
                    break

        if flags:
            findings.append({
                "city": city_key,
                "id": pid,
                "name": name,
                "category": cat,
                "area": p.get("area") or "",
                "description": desc_tr,
                "description_en": desc_en,
                "imageUrl": p.get("imageUrl") or "",
                "flags": flags,
            })

    return findings


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(CITIES_DIR.glob("*.json"))
    all_findings: list[dict] = []
    per_city: dict[str, int] = {}

    for f in files:
        try:
            found = audit_city(f)
        except Exception as e:  # noqa: BLE001
            print(f"⚠️  {f.name}: {e}", file=sys.stderr)
            continue
        if found:
            per_city[f.stem] = len(found)
            all_findings.extend(found)

    rule_counter: Counter[str] = Counter()
    sev_counter: Counter[str] = Counter()
    for it in all_findings:
        for fl in it["flags"]:
            rule_counter[fl["rule"]] += 1
            sev_counter[fl["severity"]] += 1

    OUT_JSON.write_text(
        json.dumps(
            {
                "summary": {
                    "total_findings": len(all_findings),
                    "per_rule": dict(rule_counter),
                    "per_severity": dict(sev_counter),
                    "per_city": dict(sorted(per_city.items(), key=lambda x: -x[1])),
                },
                "findings": all_findings,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    _write_html(all_findings, per_city, rule_counter, sev_counter)

    print(f"✅ {len(all_findings)} şüpheli kayıt bulundu")
    print("   Kural dağılımı:", dict(rule_counter))
    print("   Önem dağılımı: ", dict(sev_counter))
    print(f"   En kirli 10 şehir: {list(sorted(per_city.items(), key=lambda x: -x[1])[:10])}")
    print(f"\n📄 Rapor:")
    print(f"   {OUT_JSON.relative_to(ROOT)}")
    print(f"   {OUT_HTML.relative_to(ROOT)}  ← tarayıcıda aç")


# ---------------------------------------------------------------------------
# HTML rapor
# ---------------------------------------------------------------------------

_RULE_LABEL = {
    "H1": "Ad tip kelimesiyle BAŞLIYOR ama kategori uyumsuz",
    "H2": "Ad içinde tip kelimesi var, kategori uyumsuz",
}


def _sev_color(sev: str) -> str:
    return {"high": "#dc2626", "medium": "#d97706", "low": "#6b7280"}.get(sev, "#6b7280")


def _write_html(findings: list[dict], per_city: dict, rules: Counter, sevs: Counter) -> None:
    rows = []
    # En şüphelileri tepeye koy
    sev_rank = {"high": 0, "medium": 1, "low": 2}
    findings_sorted = sorted(
        findings,
        key=lambda x: (min(sev_rank.get(f["severity"], 3) for f in x["flags"]), x["city"]),
    )

    for it in findings_sorted:
        flag_html = "".join(
            f'<div class="flag" style="border-left-color:{_sev_color(f["severity"])}">'
            f'<span class="rule">{f["rule"]}</span> '
            f'<span class="why">{html.escape(f["why"])}</span>'
            + (
                f'<div class="suggest">önerilen kategori: <b>{" / ".join(f["suggest_category_in"])}</b></div>'
                if f.get("suggest_category_in")
                else ""
            )
            + "</div>"
            for f in it["flags"]
        )

        rows.append(f"""
<tr>
  <td class="city">{html.escape(it['city'])}</td>
  <td>
    <div class="name">{html.escape(it['name'])}</div>
    <div class="meta"><span class="cat">{html.escape(it['category'])}</span> · {html.escape(it['area'])}</div>
    <div class="desc tr">TR: {html.escape(it['description'][:280])}</div>
    <div class="desc en">EN: {html.escape(it['description_en'][:280])}</div>
  </td>
  <td>{flag_html}</td>
  <td><a href="https://www.google.com/maps/place/?q=place_id:{html.escape(it['id'])}" target="_blank">maps</a></td>
</tr>""")

    summary_rows = "\n".join(
        f"<tr><td>{k}</td><td>{_RULE_LABEL.get(k, k)}</td><td>{v}</td></tr>"
        for k, v in rules.most_common()
    )
    sev_rows = "\n".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in sevs.most_common())
    city_rows = "\n".join(
        f"<tr><td>{k}</td><td>{v}</td></tr>"
        for k, v in sorted(per_city.items(), key=lambda x: -x[1])
    )

    OUT_HTML.write_text(f"""<!doctype html>
<html lang="tr">
<head><meta charset="utf-8"><title>Veri kalite raporu</title>
<style>
body{{font:14px -apple-system,system-ui,sans-serif;margin:0;padding:24px;background:#f8fafc;color:#0f172a}}
h1{{margin:0 0 8px}}
.summary{{display:flex;gap:24px;margin-bottom:24px;flex-wrap:wrap}}
.card{{background:#fff;padding:14px 18px;border-radius:10px;border:1px solid #e2e8f0;min-width:240px}}
.card h3{{margin:0 0 8px;font-size:13px;color:#64748b;text-transform:uppercase;letter-spacing:.05em}}
table{{width:100%;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden;border:1px solid #e2e8f0}}
th,td{{padding:10px 12px;border-bottom:1px solid #f1f5f9;text-align:left;vertical-align:top;font-size:13px}}
th{{background:#f1f5f9;font-weight:600;font-size:12px;text-transform:uppercase;color:#475569}}
tr:last-child td{{border-bottom:none}}
.city{{font-weight:600;white-space:nowrap;color:#334155}}
.name{{font-weight:600;font-size:14px}}
.meta{{color:#64748b;font-size:12px;margin:3px 0 6px}}
.cat{{display:inline-block;background:#ede9fe;color:#6d28d9;padding:1px 8px;border-radius:4px;font-size:11px;margin-right:6px}}
.desc{{font-size:12px;color:#475569;margin-top:2px;line-height:1.45}}
.desc.en{{color:#94a3b8}}
.flag{{border-left:3px solid #d1d5db;padding:4px 10px;margin-bottom:4px;background:#f9fafb;border-radius:3px}}
.rule{{display:inline-block;background:#1e293b;color:#fff;padding:1px 6px;border-radius:3px;font-size:11px;font-weight:700;margin-right:6px}}
.why{{font-size:12px}}
.suggest{{font-size:11px;color:#6d28d9;margin-top:2px}}
a{{color:#2563eb;text-decoration:none}}
details{{margin-top:12px}}
</style></head>
<body>
<h1>Veri kalite raporu</h1>
<p style="color:#475569;margin:0 0 20px">{len(findings)} şüpheli kayıt · Faz 1 heuristik taraması · sadece açık işaretler</p>

<div class="summary">
  <div class="card"><h3>Kural dağılımı</h3><table>{summary_rows}</table></div>
  <div class="card"><h3>Önem</h3><table>{sev_rows}</table></div>
  <div class="card"><h3>Şehirler</h3><details><summary>göster</summary><table>{city_rows}</table></details></div>
</div>

<table>
<thead><tr><th>şehir</th><th>mekan</th><th>işaretler</th><th></th></tr></thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
</body></html>""", encoding="utf-8")


if __name__ == "__main__":
    main()
