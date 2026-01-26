#!/usr/bin/env python3
"""
Londra için eksik kalan ~50 mekanı tamamlayan script.
Google Places API kullanarak fotoğraf ve detayları çeker.
"""

import json
import requests
import time
from pathlib import Path

# Google Places API Key
API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"
CITY_FILE = Path("assets/cities/londra.json")

# Eklenecek Son Parti Mekanlar
NEW_PLACES = [
    {"name": "Spitalfields Market", "category": "Pazar", "desc": "Doğu Londra'nın kalbinde, moda, sanat ve yiyecek tezgahlarıyla dolu canlı pazar."},
    {"name": "Brick Lane", "category": "Semt", "desc": "Vintage mağazaları, sokak sanatı ve ünlü köri restoranlarıyla dolu renkli cadde."},
    {"name": "Holland Park", "category": "Park", "desc": "Zengin bitki örtüsü, tavus kuşları ve Kyoto Bahçesi ile ünlü huzurlu park."},
    {"name": "Science Museum", "category": "Müze", "desc": "Bilim ve teknolojinin tarihine ışık tutan, interaktif sergilerle dolu müze."},
    {"name": "Churchill War Rooms", "category": "Müze", "desc": "Winston Churchill'in İkinci Dünya Savaşı'nı yönettiği yer altı sığınağı."},
    {"name": "The National Gallery", "category": "Sanat Galerisi", "desc": "Da Vinci, Van Gogh ve Rembrandt gibi ustaların eserlerine ev sahipliği yapan galeri."},
    {"name": "Twickenham Stadium", "category": "Spor", "desc": "Rugby'nin evi olarak bilinen, dünyanın en büyük rugby stadyumu."},
    {"name": "Wembley Stadium", "category": "Spor", "desc": "İngiliz futbolunun kalbi, devasa kemeriyle ünlü ikonik stadyum."},
    {"name": "Hampton Court Palace", "category": "Tarihi", "desc": "Kral VIII. Henry'nin görkemli sarayı ve ünlü labirenti."},
    {"name": "Royal Botanic Gardens, Kew", "category": "Botanik Bahçe", "desc": "UNESCO Dünya Mirası listesinde yer alan, dünyanın en ünlü botanik bahçesi."}
]

def get_place_details(place_name):
    """Google Places API'den fotoğraf, lokasyon ve rating al."""
    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": f"{place_name} London",
        "inputtype": "textquery",
        "fields": "place_id,photos,geometry,rating,user_ratings_total,formatted_address",
        "key": API_KEY
    }
    
    try:
        resp = requests.get(search_url, params=params)
        data = resp.json()
        
        if data.get("status") == "OK" and data.get("candidates"):
            candidate = data["candidates"][0]
            
            result = {
                "lat": candidate["geometry"]["location"]["lat"],
                "lng": candidate["geometry"]["location"]["lng"],
                "rating": candidate.get("rating", 4.5),
                "reviewCount": candidate.get("user_ratings_total", 100),
                "address": candidate.get("formatted_address", "London, UK")
            }
            
            if "photos" in candidate:
                photo_ref = candidate["photos"][0]["photo_reference"]
                result["imageUrl"] = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={photo_ref}&key={API_KEY}"
            else:
                result["imageUrl"] = "" # Fotoğraf yoksa boş bırak
                
            return result
    except Exception as e:
        print(f"  ❌ Hata ({place_name}): {e}")
        
    return None

def main():
    print(f"🚀 Londra zenginleştirme başlatılıyor... ({len(NEW_PLACES)} mekan)")
    
    with open(CITY_FILE, 'r', encoding='utf-8') as f:
        city_data = json.load(f)
        
    existing_names = {p["name"].lower() for p in city_data["highlights"]}
    added_count = 0
    
    for place in NEW_PLACES:
        if place["name"].lower() in existing_names:
            print(f"  ⚠️ Zaten var: {place['name']}")
            continue
            
        print(f"  🔍 İşleniyor: {place['name']}...")
        details = get_place_details(place["name"])
        
        if details:
            new_place = {
                "id": f"lon_{int(time.time())}_{added_count}",
                "name": place["name"],
                "description": place["desc"],
                "category": place["category"],
                "imageUrl": details["imageUrl"],
                "lat": details["lat"],
                "lng": details["lng"],
                "rating": details["rating"],
                "address": details["address"],
                "expense": "€€", # Varsayılan
                "distanceFromCenter": 0.0 # Sonra hesaplanacak veya dinamik
            }
            city_data["highlights"].append(new_place)
            added_count += 1
            print(f"  ✅ Eklendi: {place['name']}")
            time.sleep(0.5) # Rate limiting
        else:
            print(f"  ❌ Detaylar alınamadı: {place['name']}")
            
    # Kaydet
    with open(CITY_FILE, 'w', encoding='utf-8') as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n💾 Toplam {added_count} yeni mekan eklendi. Yeni toplam: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()
