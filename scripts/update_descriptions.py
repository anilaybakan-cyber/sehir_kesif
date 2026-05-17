#!/usr/bin/env python3
"""
Jenerik description'ları Google Places API ile gerçek mekan-spesifik
metinlerle değiştirir.

Kullanım:
  export GOOGLE_PLACES_KEY="YOUR_KEY"
  python3 scripts/update_descriptions.py              # dry-run (rapor)
  python3 scripts/update_descriptions.py --fix        # uygula
  python3 scripts/update_descriptions.py --fix --city bari  # tek şehir
  python3 scripts/update_descriptions.py --limit 10   # sadece 10 mekan test et

Strateji:
  1. editorial_summary.overview varsa (TR+EN) → kullan (en kaliteli)
  2. types + reviews'tan kısa, mekan-spesifik tanım üret
  3. Hiçbir veri yoksa → atla, eski metni bırak

API: Google Places Place Details
Maliyet: ~$17/1000 call. 319 mekan x 2 dil = 638 call ≈ $11
"""

import json
import os
import sys
import argparse
import time
import requests
from pathlib import Path
from collections import Counter

API_KEY = os.environ.get("GOOGLE_PLACES_KEY", "")
CITIES_DIR = Path(__file__).parent.parent / "assets" / "cities"
DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

# Jenerik metni tespit etmek için kalıplar
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


def get_place_details(place_id: str, lang: str = "tr") -> dict | None:
    """Google Place Details çek. None=hata."""
    params = {
        "place_id": place_id,
        "key": API_KEY,
        "language": lang,
        "fields": "name,editorial_summary,types,rating,user_ratings_total,reviews,formatted_address",
    }
    try:
        r = requests.get(DETAILS_URL, params=params, timeout=15)
        data = r.json()
        if data.get("status") != "OK":
            return {"_error": data.get("status"), "_msg": data.get("error_message", "")}
        return data.get("result", {})
    except Exception as e:
        return {"_error": "EXCEPTION", "_msg": str(e)}


# Kategori-bazlı insan-okur kısa tanımlar (types → şehirde X)
TYPE_TR = {
    "movie_theater": "sinema",
    "cinema": "sinema",
    "restaurant": "restoran",
    "cafe": "kafe",
    "bar": "bar",
    "night_club": "gece kulübü",
    "museum": "müze",
    "art_gallery": "sanat galerisi",
    "tourist_attraction": "popüler turistik nokta",
    "park": "park",
    "church": "kilise",
    "mosque": "cami",
    "synagogue": "sinagog",
    "hindu_temple": "tapınak",
    "place_of_worship": "ibadethane",
    "shopping_mall": "alışveriş merkezi",
    "store": "mağaza",
    "lodging": "konaklama tesisi",
    "spa": "spa",
    "amusement_park": "lunapark",
    "zoo": "hayvanat bahçesi",
    "aquarium": "akvaryum",
    "stadium": "stadyum",
    "library": "kütüphane",
    "book_store": "kitapçı",
    "bakery": "fırın",
    "meal_takeaway": "yemek noktası",
}
TYPE_EN = {
    "movie_theater": "cinema",
    "cinema": "cinema",
    "restaurant": "restaurant",
    "cafe": "cafe",
    "bar": "bar",
    "night_club": "nightclub",
    "museum": "museum",
    "art_gallery": "art gallery",
    "tourist_attraction": "popular tourist attraction",
    "park": "park",
    "church": "church",
    "mosque": "mosque",
    "shopping_mall": "shopping mall",
    "store": "shop",
    "lodging": "accommodation",
    "spa": "spa",
    "amusement_park": "amusement park",
    "zoo": "zoo",
    "aquarium": "aquarium",
    "stadium": "stadium",
    "library": "library",
    "book_store": "bookshop",
    "bakery": "bakery",
}


def humanize_type(types: list, lang: str) -> str:
    """types listesinden insan okur kategori döndür."""
    table = TYPE_TR if lang == "tr" else TYPE_EN
    for t in types:
        if t in table:
            return table[t]
    # Generic fallback
    return "popüler bir nokta" if lang == "tr" else "popular spot"


def review_excerpt(reviews: list, lang: str) -> str:
    """En yüksek puanlı 1 yorumdan kısa, anlamlı bir cümle çıkar."""
    if not reviews:
        return ""
    # En yüksek rating'li ve en uzun review'u tercih et
    sorted_r = sorted(reviews, key=lambda r: (r.get("rating", 0), len(r.get("text", ""))), reverse=True)
    for r in sorted_r:
        text = (r.get("text") or "").strip()
        if len(text) < 30:
            continue
        # İlk cümle veya 150 char
        first_dot = text.find(".")
        if 30 < first_dot < 200:
            return text[:first_dot].strip() + "."
        return text[:150].strip() + "..."
    return ""


def build_description(details: dict, place_name: str, city: str, lang: str) -> tuple[str | None, str]:
    """Place details'den kaliteli bir description üret.
    Returns: (description, quality) — quality: 'editorial' | 'fallback' | 'none'
    """
    if not details or details.get("_error"):
        return None, "none"
    
    # 1. Editorial summary varsa VE istediğimiz dilde ise kullan (en iyi)
    es_obj = details.get("editorial_summary") or {}
    es_text = es_obj.get("overview", "").strip()
    es_lang = es_obj.get("language", "")
    if es_text and len(es_text) > 20 and es_lang == lang:
        return es_text, "editorial"
    
    # 2. Types + reviews ile inşa et
    types = details.get("types", [])
    rating = details.get("rating")
    rcount = details.get("user_ratings_total", 0)
    type_label = humanize_type(types, lang)
    review = review_excerpt(details.get("reviews", []), lang)
    
    if lang == "tr":
        parts = []
        s1 = f"{place_name}, {city}'de yer alan bir {type_label}."
        parts.append(s1)
        if rating and rcount > 10:
            parts.append(f"Google'da {rating}/5 puanla {rcount:,} kullanıcı tarafından değerlendirildi.")
        if review:
            parts.append(f"Ziyaretçi yorumu: \"{review}\"")
        if len(parts) < 2:
            return None, "none"
        return " ".join(parts), "fallback"
    else:
        parts = []
        s1 = f"{place_name} is a {type_label} in {city}."
        parts.append(s1)
        if rating and rcount > 10:
            parts.append(f"Rated {rating}/5 by {rcount:,} users on Google.")
        if review:
            parts.append(f"Visitor note: \"{review}\"")
        if len(parts) < 2:
            return None, "none"
        return " ".join(parts), "fallback"


def collect_targets(only_city: str | None = None, limit: int = 0) -> list:
    """Jenerik description'a sahip ve geçerli Place ID'si olan mekanları topla."""
    targets = []
    files = sorted(CITIES_DIR.glob("*.json"))
    for f in files:
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
    ap.add_argument("--fix", action="store_true", help="JSON'lara yaz")
    ap.add_argument("--city", help="Sadece bu şehri işle")
    ap.add_argument("--limit", type=int, default=0, help="Max mekan sayısı (test için)")
    args = ap.parse_args()
    
    if not API_KEY:
        print("HATA: GOOGLE_PLACES_KEY env değişkeni set edilmemiş.")
        print("  export GOOGLE_PLACES_KEY=\"YOUR_KEY\"")
        sys.exit(1)
    
    targets = collect_targets(args.city, args.limit)
    print(f"Hedef: {len(targets)} jenerik mekan\n")
    
    if not targets:
        print("Yapacak iş yok!")
        return
    
    # Dosya bazlı toplu güncelleme için cache
    file_cache = {}  # path -> data
    
    stats = Counter()
    for i, t in enumerate(targets, 1):
        prefix = f"[{i}/{len(targets)}]"
        # TR ve EN paralel çek
        tr = get_place_details(t["place_id"], "tr")
        en = get_place_details(t["place_id"], "en")
        
        if tr and tr.get("_error"):
            print(f"{prefix} HATA {t['name'][:40]}: {tr['_error']} {tr.get('_msg','')[:60]}")
            stats["error"] += 1
            if "REQUEST_DENIED" in tr.get("_error", ""):
                print("API key sorunu - duruyorum.")
                break
            continue
        
        new_tr, q_tr = build_description(tr, t["name"], t["city"], "tr")
        new_en, q_en = build_description(en, t["name"], t["city"], "en")
        
        if not new_tr and not new_en:
            print(f"{prefix} ATLA {t['name'][:40]}: yetersiz veri")
            stats["skip"] += 1
            continue
        
        quality = f"TR:{q_tr.upper()[:3]} EN:{q_en.upper()[:3]}"
        stats[f"tr_{q_tr}"] += 1
        stats[f"en_{q_en}"] += 1
        
        print(f"{prefix} OK {t['name'][:40]:<40} [{quality}]")
        if not args.fix:
            print(f"     TR: {(new_tr or '')[:130]}")
            if new_en:
                print(f"     EN: {new_en[:130]}")
            print()
        
        if args.fix:
            # Cache'den oku/yaz
            if t["file"] not in file_cache:
                file_cache[t["file"]] = json.load(open(t["file"]))
            data = file_cache[t["file"]]
            hl = data if t["is_list"] else data["highlights"]
            h = hl[t["idx"]]
            if new_tr:
                h["description"] = new_tr
            if new_en:
                h["description_en"] = new_en
        
        time.sleep(0.05)  # Rate limit nazikliği
    
    if args.fix:
        # Tüm dosyaları kaydet
        for path, data in file_cache.items():
            with open(path, "w", encoding="utf-8") as fp:
                json.dump(data, fp, ensure_ascii=False, indent=2)
        print(f"\nGuncellendi: {len(file_cache)} dosya")
    
    print(f"\n=== ISTATISTIK ===")
    for k, v in stats.most_common():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
