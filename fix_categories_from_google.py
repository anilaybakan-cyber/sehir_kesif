from dotenv import load_dotenv
load_dotenv()
import os
#!/usr/bin/env python3
"""
Tüm mekanlardaki kategorileri Google Places API'den gelen 'types' verisine göre düzeltir.
Google'ın resmi sınıflandırmasını kullanarak yanlış etiketlemeleri giderir.
"""

import json
import requests
import time
import sys
from pathlib import Path

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
CITIES_DIR = Path("assets/cities")

# Google Place Types -> Uygulama Kategorisi Eşleştirmesi
# Öncelik sırasına göre: İlk eşleşen kategori atanır
TYPE_TO_CATEGORY = {
    # Müze & Sanat
    "museum": "Müze",
    "art_gallery": "Müze",
    
    # Tarihi Yapılar
    "castle": "Tarihi",
    "church": "Tarihi",
    "place_of_worship": "Tarihi",
    "hindu_temple": "Tarihi",
    "mosque": "Tarihi",
    "synagogue": "Tarihi",
    "city_hall": "Tarihi",
    "embassy": "Tarihi",
    "courthouse": "Tarihi",
    
    # Parklar & Doğa
    "park": "Park",
    "zoo": "Park",
    "aquarium": "Akvaryum",
    "amusement_park": "Eğlence",
    "botanical_garden": "Park",
    
    # Yeme İçme
    "restaurant": "Restoran",
    "meal_delivery": "Restoran",
    "meal_takeaway": "Restoran",
    "cafe": "Kafe",
    "bakery": "Kafe",
    "bar": "Bar",
    "night_club": "Bar",
    
    # Alışveriş
    "shopping_mall": "Alışveriş",
    "department_store": "Alışveriş",
    "clothing_store": "Alışveriş",
    "jewelry_store": "Alışveriş",
    
    # Manzara & Gözlem
    "tourist_attraction": "Gezilecek Yer",
    "point_of_interest": "Gezilecek Yer",
    
    # Ulaşım (Genelde atlanır ama bazı turistik tren istasyonları var)
    "train_station": "Tarihi",
    "transit_station": "Gezilecek Yer",
    
    # Konaklama (Genelde eklenmez ama bazı tarihi oteller var)
    "lodging": "Otel",
    
    # Spor
    "stadium": "Spor",
    "gym": "Spor",
    
    # Sağlık (Turistik değil, atlanmalı ama spa'lar var)
    "spa": "Deneyim",
    
    # Eğitim (Turistik değil ama bazı üniversite kampüsleri)
    "university": "Gezilecek Yer",
    "library": "Kültür",
}

def get_place_types(place_name: str, city_name: str) -> list:
    """Google Places API ile bir mekanın types bilgisini çeker."""
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": f"{place_name} {city_name}",
        "inputtype": "textquery",
        "fields": "types,name",
        "key": API_KEY
    }
    try:
        res = requests.get(url, params=params)
        data = res.json()
        if data.get("status") == "OK" and data.get("candidates"):
            return data["candidates"][0].get("types", [])
    except Exception as e:
        print(f"    ❌ API Hatası: {e}")
    return []

def determine_category(types: list) -> str:
    """Google types listesinden en uygun kategoriyi belirler.
    Öncelik: Spesifik tipler (museum, church) önce, genel tipler (tourist_attraction) sonra."""
    
    # Öncelik sırası: Spesifik -> Genel
    priority_order = [
        # Yüksek öncelik (spesifik)
        "museum", "art_gallery", "castle", "church", "mosque", "synagogue", 
        "hindu_temple", "place_of_worship", "stadium", "zoo", "aquarium",
        "amusement_park", "park", "botanical_garden", "spa",
        "restaurant", "cafe", "bakery", "bar", "night_club",
        "shopping_mall", "department_store", "library", "university",
        # Düşük öncelik (genel)
        "tourist_attraction", "point_of_interest", "establishment"
    ]
    
    for priority_type in priority_order:
        if priority_type in types:
            if priority_type in TYPE_TO_CATEGORY:
                return TYPE_TO_CATEGORY[priority_type]
    
    return None  # Eşleşme yoksa mevcut kategoriyi koru

def fix_city(json_path: Path):
    city_key = json_path.stem
    print(f"\n🔧 ŞEHİR: {city_key.upper()}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    city_name = data.get("city") or city_key.capitalize()
    highlights = data.get("highlights", [])
    fixed_count = 0
    
    for place in highlights:
        name = place.get("name", "")
        current_cat = place.get("category", "")
        
        # Google'dan types çek
        types = get_place_types(name, city_name)
        
        if not types:
            continue
            
        # Yeni kategori belirle
        new_cat = determine_category(types)
        
        if new_cat and new_cat != current_cat:
            print(f"  🔄 '{name}': {current_cat} -> {new_cat} (Google: {types[:3]})")
            place["category"] = new_cat
            fixed_count += 1
            
        time.sleep(0.1)  # Rate limiting
        
    if fixed_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    print(f"  ✅ {fixed_count} kategori düzeltildi.")
    return fixed_count

def main():
    print("🌍 GOOGLE-BASED KATEGORİ DÜZELTME BAŞLADI")
    
    if len(sys.argv) > 1:
        # Tek şehir modu
        city = sys.argv[1].lower()
        path = CITIES_DIR / f"{city}.json"
        if path.exists():
            fix_city(path)
        else:
            print(f"Dosya bulunamadı: {path}")
    else:
        # Tüm şehirler
        total = 0
        for p in sorted(CITIES_DIR.glob("*.json")):
            total += fix_city(p)
        print(f"\n🎉 TOPLAM {total} KATEGORİ DÜZELTİLDİ.")

if __name__ == "__main__":
    main()
