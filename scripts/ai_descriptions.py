#!/usr/bin/env python3
"""
Jenerik description'ları AI ile gerçek mekan-spesifik metinlerle değiştirir.

Akış:
  1. Google Place Details → gerçek review, rating, editorial, types verisi
  2. Gemini 2.5 Flash → gerçek veriden 15-20 kelimelik doğal TR+EN description üretir
     (strict prompt: sadece verilen veriden yararlan, uydurma yok)
  3. JSON'lara uygula

Kullanım:
  export GOOGLE_PLACES_KEY="..."
  export GEMINI_KEY="..."
  python3 scripts/ai_descriptions.py --limit 5              # test
  python3 scripts/ai_descriptions.py --city bari --fix      # tek şehir
  python3 scripts/ai_descriptions.py --fix                  # hepsi
"""

import json
import os
import sys
import argparse
import time
import requests
from pathlib import Path
from collections import Counter

PLACES_KEY = os.environ.get("GOOGLE_PLACES_KEY", "")
GEMINI_KEY = os.environ.get("GEMINI_KEY", "")
CITIES_DIR = Path(__file__).parent.parent / "assets" / "cities"

PLACES_URL = "https://maps.googleapis.com/maps/api/place/details/json"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

GENERIC_PATTERNS = [
    'en sevilen noktalarından biri olan bu mekan',
    'kentinde gurme lezzetler arayan',
    'lezzet kaçış rotası',
    'Antik dokularla',
    'mistik bir atmosfer sunan',
    'kentin kültürel kimliğini tanımlayan',
    'Geleneksel tarifleri modern bir dokunuşla harmanlayan',
    'gastronomisinin en seçkin temsilcilerinden',
    'damak çıtasını yükselten',
    'şehrin imza duraklarından',
    'yerel dokuyu hissetmek',
    'sosyal gezginler için',
    'otantik lezzetleri modern bir sunumla birleştirerek',
]


def is_generic(desc: str) -> bool:
    if not desc:
        return True
    return any(p in desc for p in GENERIC_PATTERNS)


def get_place_details(place_id: str, lang: str = "en") -> dict | None:
    """Google Place Details - tüm değerli alanları çek."""
    params = {
        "place_id": place_id,
        "key": PLACES_KEY,
        "language": lang,
        "fields": "name,editorial_summary,types,rating,user_ratings_total,reviews,formatted_address,price_level",
    }
    try:
        r = requests.get(PLACES_URL, params=params, timeout=15)
        data = r.json()
        if data.get("status") != "OK":
            return {"_error": data.get("status"), "_msg": data.get("error_message", "")}
        return data.get("result", {})
    except Exception as e:
        return {"_error": "EXCEPTION", "_msg": str(e)}


def build_ai_prompt(place_name: str, city: str, details_tr: dict, details_en: dict) -> str:
    """Strict prompt - sadece verilen verilerden yararlan, uydurma yasak."""
    
    # TR ve EN'den en zengin veriyi birleştir
    editorial_tr = (details_tr.get("editorial_summary") or {}).get("overview", "")
    editorial_en = (details_en.get("editorial_summary") or {}).get("overview", "")
    types = details_en.get("types", [])
    rating = details_en.get("rating")
    rcount = details_en.get("user_ratings_total", 0)
    price_level = details_en.get("price_level")
    
    # En iyi 5 yorum (uzun ve yüksek puanlı)
    reviews = details_en.get("reviews") or []
    review_excerpts = []
    for r in sorted(reviews, key=lambda x: (x.get("rating", 0), len(x.get("text", ""))), reverse=True)[:5]:
        txt = (r.get("text") or "").strip().replace("\n", " ")
        if len(txt) > 20:
            review_excerpts.append(f'- [{r.get("rating")}★] {txt[:400]}')
    
    reviews_block = "\n".join(review_excerpts) if review_excerpts else "(yok)"
    
    prompt = f"""Sen bir seyahat rehberisin. Aşağıdaki GERÇEK Google Maps verilerinden yola çıkarak, bu mekan için kısa bir açıklama yazacaksın.

MEKAN: {place_name}
ŞEHİR: {city}
TİPLER: {', '.join(types[:5]) if types else '(yok)'}
RATING: {rating}/5 ({rcount} kullanıcı)
FİYAT SEVİYESİ: {price_level if price_level is not None else '(yok)'}

GOOGLE EDITORIAL (TR): {editorial_tr or '(yok)'}
GOOGLE EDITORIAL (EN): {editorial_en or '(yok)'}

GERÇEK KULLANICI YORUMLARI:
{reviews_block}

KURALLAR (çok önemli):
1. Verilen verilerde OLMAYAN hiçbir şey yazma (kurucu, tarih, mimari detay, menü, kapasite, vs.).
2. 15-20 kelime arası, tek cümle veya iki kısa cümle.
3. KESİNLİKLE puan, yıldız veya yorum sayısından (örn: "4.5 yıldızlı", "1000 yorum alan") bahsetme. Yalnızca atmosfere, menüye ve deneyime odaklan.
4. Mekanın ADINI tekrar etme (zaten başlıkta gösterilir), onun yerine "burada", "mekan" gibi ifadeler kullan.
5. Reklamvari, abartılı ("harika", "muhteşem") sıfatlardan kaçın. Somut, betimleyici ol.
6. Eğer veri çok yetersizse (editorial yok + 2'den az review) → yanıt olarak SADECE "INSUFFICIENT_DATA" yaz.

ÇIKTI FORMATI (kesinlikle bu JSON formatında dön, başka hiçbir şey yazma):
{{"tr": "Türkçe açıklama buraya", "en": "English description here"}}

Eğer veri yetersizse:
{{"tr": "INSUFFICIENT_DATA", "en": "INSUFFICIENT_DATA"}}"""
    
    return prompt


def call_gemini(prompt: str) -> dict | None:
    """Gemini çağrısı, JSON parse edilmiş cevap döner."""
    try:
        r = requests.post(
            f"{GEMINI_URL}?key={GEMINI_KEY}",
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.3,  # Düşük = tutucu, uydurma az
                    "maxOutputTokens": 800,
                    "responseMimeType": "application/json",
                    "thinkingConfig": {"thinkingBudget": 0},  # 2.5-flash hızlı mod
                },
            },
            timeout=30,
        )
        data = r.json()
        if "candidates" not in data:
            return {"_error": str(data)[:200]}
        text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
        # JSON parse
        try:
            return json.loads(text)
        except:
            # Gemini bazen ```json ``` sarabiliyor
            if "```" in text:
                text = text.split("```")[1].lstrip("json").strip()
                return json.loads(text)
            return {"_error": f"parse: {text[:200]}"}
    except Exception as e:
        return {"_error": f"exc: {e}"}


def collect_targets(only_city: str | None = None, limit: int = 0) -> list:
    targets = []
    for f in sorted(CITIES_DIR.glob("*.json")):
        if only_city and only_city.lower() not in f.stem.lower():
            continue
        try:
            d = json.load(open(f))
        except:
            continue
        is_list = isinstance(d, list)
        hl = d if is_list else d.get("highlights", [])
        city_name = "" if is_list else d.get("city", "")
        for idx, h in enumerate(hl):
            desc = h.get("description", "")
            pid = h.get("id", "")
            if is_generic(desc) and pid.startswith("ChIJ"):
                targets.append({
                    "file": f,
                    "is_list": is_list,
                    "idx": idx,
                    "city": city_name or f.stem,
                    "place_id": pid,
                    "name": h.get("name", ""),
                })
                if limit and len(targets) >= limit:
                    return targets
    return targets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--city", help="Sadece bu şehri")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    
    if not PLACES_KEY or not GEMINI_KEY:
        print("HATA: GOOGLE_PLACES_KEY ve GEMINI_KEY env değişkenleri gerekli")
        sys.exit(1)
    
    targets = collect_targets(args.city, args.limit)
    print(f"Hedef: {len(targets)} mekan\n")
    if not targets:
        return
    
    file_cache = {}
    stats = Counter()
    
    for i, t in enumerate(targets, 1):
        prefix = f"[{i}/{len(targets)}]"
        name_short = t["name"][:40]
        
        # 1. Place Details çek (TR + EN)
        details_tr = get_place_details(t["place_id"], "tr")
        details_en = get_place_details(t["place_id"], "en")
        
        if details_tr and details_tr.get("_error"):
            err = details_tr["_error"]
            print(f"{prefix} HATA(Places) {name_short}: {err}")
            stats["places_error"] += 1
            if "REQUEST_DENIED" in err:
                print("Places API key hatası - duruyorum.")
                break
            continue
        
        # 2. Gemini'ye gönder
        prompt = build_ai_prompt(t["name"], t["city"], details_tr, details_en)
        result = call_gemini(prompt)
        
        if not result or result.get("_error"):
            err = (result or {}).get("_error", "?")
            print(f"{prefix} HATA(AI) {name_short}: {err[:80]}")
            stats["ai_error"] += 1
            continue
        
        tr = result.get("tr", "").strip()
        en = result.get("en", "").strip()
        
        if tr == "INSUFFICIENT_DATA" or en == "INSUFFICIENT_DATA":
            print(f"{prefix} ATLA {name_short}: yetersiz veri")
            stats["skip"] += 1
            continue
        
        if not tr or not en:
            print(f"{prefix} ATLA {name_short}: eksik çıktı")
            stats["skip"] += 1
            continue
        
        stats["ok"] += 1
        print(f"{prefix} OK  {name_short:<40} ({t['city']})")
        if not args.fix:
            print(f"     TR: {tr}")
            print(f"     EN: {en}\n")
        
        if args.fix:
            if t["file"] not in file_cache:
                file_cache[t["file"]] = json.load(open(t["file"]))
            data = file_cache[t["file"]]
            hl = data if t["is_list"] else data["highlights"]
            hl[t["idx"]]["description"] = tr
            hl[t["idx"]]["description_en"] = en
        
        # Rate limit: Gemini Free = 15 RPM
        time.sleep(4.5)
    
    if args.fix:
        for path, data in file_cache.items():
            with open(path, "w", encoding="utf-8") as fp:
                json.dump(data, fp, ensure_ascii=False, indent=2)
        print(f"\n{len(file_cache)} dosya guncellendi.")
    
    print(f"\n=== OZET ===")
    for k, v in stats.most_common():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
