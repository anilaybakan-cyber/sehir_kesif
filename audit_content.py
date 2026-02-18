#!/usr/bin/env python3
"""
Tüm şehir içeriğini tarayan ve kalite kontrolü yapan script.
- Mekan sayısı
- Fake isimler
- Fotoğraf durumu
"""

import json
import os
from pathlib import Path
from collections import Counter

CITIES_DIR = Path("assets/cities")

FAKE_TERMS = ["london spot", "spot", "temp", "test", "place", "unknown"]

def analyze_city(json_path: Path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    city_name = json_path.stem.upper()
    highlights = data.get("highlights", [])
    count = len(highlights)
    
    fake_names = []
    missing_photos = 0
    unsplash_photos = 0
    generic_photos = 0 # Örn: benim hatamla yayılanlar
    
    for h in highlights:
        name = h.get("name", "").lower()
        img = h.get("imageUrl", "")
        
        # Fake isim kontrolü
        if any(term in name for term in FAKE_TERMS) and not "spotlight" in name:
             # London Spot gibi bariz olanları listele, ama "Spotlight Club" gibi gerçekleri eleme
             if "spot" in name and not any(c.isdigit() for c in name): 
                 pass # Sadece "spot" geçmesi yetmez, rakam da olsun genelde
             elif "spot " in name:
                 fake_names.append(h.get("name"))
        
        # Fotoğraf kontrolü
        if not img:
            missing_photos += 1
        elif "unsplash" in img.lower():
            unsplash_photos += 1
        elif "lombardia.info" in img: # Benim hatam diğer şehirlere sıçradı mı?
            generic_photos += 1
            
    return {
        "city": city_name,
        "count": count,
        "fakes": fake_names,
        "missing_img": missing_photos,
        "unsplash": unsplash_photos,
        "generic": generic_photos
    }

def main():
    print("="*80)
    print(f"{'ŞEHİR':<15} {'SAYI':<10} {'FAKE':<30} {'FOTO SORUNU':<15}")
    print("="*80)
    
    total_places = 0
    cities_under_100 = []
    
    for json_path in sorted(list(CITIES_DIR.glob("*.json"))):
        res = analyze_city(json_path)
        total_places += res["count"]
        
        fake_str = f"{len(res['fakes'])} ({', '.join(res['fakes'][:2])}...)" if res['fakes'] else "0"
        photo_issues = res['missing_img'] + res['unsplash'] + res['generic']
        photo_str = f"{photo_issues}" 
        
        if photo_issues > 0:
            photo_str += f" (M:{res['missing_img']} U:{res['unsplash']} G:{res['generic']})"
            
        print(f"{res['city']:<15} {res['count']:<10} {fake_str:<30} {photo_str:<15}")
        
        if res["count"] < 80:
            cities_under_100.append(res['city'])
            
    print("="*80)
    print(f"TOPLAM MEKAN: {total_places}")
    print(f"ZENGİNLEŞTİRİLMESİ GEREKENLER (<80): {', '.join(cities_under_100)}")

if __name__ == "__main__":
    main()
