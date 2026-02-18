#!/usr/bin/env python3
"""
İstanbul şehir verisini zenginleştirme scripti.
'Küçük Dünya' ve 'Biz Evde Yokuz' kaynaklarından 25+ yeni mekan ekler.
Google Places API kullanır.
"""

import json
import requests
import time
import os
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"
ISTANBUL_JSON_PATH = "assets/cities/istanbul.json"

NEW_PLACES = [
    # Fener & Balat (Küçük Dünya)
    {"name": "Fener Rum Patrikhanesi", "search": "Ecumenical Patriarchate of Constantinople", "category": "Tarihi", "area": "Fener", "tags": ["tarihi", "dini", "mimari"]},
    {"name": "Balat Renkli Evler", "search": "Balat Colorful Houses", "category": "Manzara", "area": "Balat", "tags": ["instagram", "fotoğraf", "sokak"]},
    {"name": "Agora Meyhanesi", "search": "Agora Meyhanesi 1890", "category": "Restoran", "area": "Balat", "tags": ["meyhane", "tarihi", "meze"]},
    {"name": "Sveti Stefan Kilisesi (Demir Kilise)", "search": "Bulgarian St. Stephen Church", "category": "Tarihi", "area": "Balat", "tags": ["kilise", "tarihi", "mimari"]},
    {"name": "Mabeyin Restaurant", "search": "Mabeyin Restaurant", "category": "Restoran", "area": "Kısıklı", "tags": ["kebap", "yöresel", "şık"]},
    {"name": "Çıfıtçı Çarşısı", "search": "Leblebiciler Sokak Balat", "category": "Alışveriş", "area": "Balat", "tags": ["antikacı", "sokak", "nostalji"]},
    
    # Boğaz Köyleri & Anadolu Yakası
    {"name": "Kuzguncuk Bostanı", "search": "Kuzguncuk Bostani", "category": "Park", "area": "Kuzguncuk", "tags": ["yeşil", "mahalle", "sakin"]},
    {"name": "Mihrimah Sultan Camii (Üsküdar)", "search": "Mihrimah Sultan Mosque Uskudar", "category": "Tarihi", "area": "Üsküdar", "tags": ["mimar sinan", "boğaz", "tarihi"]},
    {"name": "Sait Halim Paşa Yalısı", "search": "Sait Halim Pasa Yalisi", "category": "Tarihi", "area": "Yeniköy", "tags": ["yalı", "lüks", "düğün"]},
    {"name": "Hidiv Kasrı", "search": "Khedive's Pavilion", "category": "Park", "area": "Beykoz", "tags": ["koru", "yürüyüş", "manzara"]},
    {"name": "Anadolu Kavağı", "search": "Anadolu Kavagi", "category": "Deneyim", "area": "Beykoz", "tags": ["balıkçı", "manzara", "kale"]},
    {"name": "Yoros Kulesi", "search": "Yoros Castle", "category": "Tarihi", "area": "Anadolu Kavağı", "tags": ["kale", "manzara", "bizans"]},
    
    # Sanat & Modern (Biz Evde Yokuz)
    {"name": "Arter", "search": "Arter Museum Istanbul", "category": "Müze", "area": "Dolapdere", "tags": ["çağdaş sanat", "sergi", "yeni"]},
    {"name": "Pera Müzesi", "search": "Pera Museum", "category": "Müze", "area": "Beyoğlu", "tags": ["sanat", "kaplumbağa terbiyecisi", "tarihi"]},
    {"name": "Salt Galata", "search": "Salt Galata", "category": "Müze", "area": "Karaköy", "tags": ["kütüphane", "mimari", "banka"]},
    {"name": "Museum of Illusions", "search": "Museum of Illusions Istanbul", "category": "Müze", "area": "Beyoğlu", "tags": ["eğlence", "çocuk", "fotoğraf"]},
    
    # Restoran & Cafe
    {"name": "Vefa Bozacısı", "search": "Vefa Bozacisi", "category": "Deneyim", "area": "Vefa", "tags": ["tarihi", "boza", "kış"]},
    {"name": "Hafız Mustafa 1864 (Sultanahmet)", "search": "Hafiz Mustafa 1864 Sultanahmet", "category": "Cafe", "area": "Sultanahmet", "tags": ["tatlı", "baklava", "tarihi"]},
    {"name": "Baylan Pastanesi", "search": "Baylan Kadikoy", "category": "Cafe", "area": "Kadıköy", "tags": ["kup griye", "tarihi", "klasik"]},
    {"name": "Çiya Sofrası", "search": "Ciya Sofrasi", "category": "Restoran", "area": "Kadıköy", "tags": ["yöresel", "anadolu", "meşhur"]},
    {"name": "Zübeyir Ocakbaşı", "search": "Zubeyir Ocakbasi", "category": "Restoran", "area": "Beyoğlu", "tags": ["kebap", "ocakbaşı", "popüler"]},
    {"name": "Mikla Restaurant", "search": "Mikla Restaurant", "category": "Restoran", "area": "Beyoğlu", "tags": ["fine dining", "manzara", "modern"]},
    
     # Gizli Rotalar
    {"name": "Büyük Valide Han", "search": "Buyuk Valide Han", "category": "Manzara", "area": "Eminönü", "tags": ["çatı", "manzara", "tarihi"]},
    {"name": "Otağtepe Fatih Korusu", "search": "Otagtepe Fatih Korusu", "category": "Manzara", "area": "Kavacık", "tags": ["boğaz", "köprü", "fotoğraf"]},
    {"name": "Pierre Loti Tepesi", "search": "Pierre Loti Hill", "category": "Manzara", "area": "Eyüp", "tags": ["haliç", "kahve", "tarihi"]},
]

def get_photo_url(photo_reference: str) -> str:
    return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={photo_reference}&key={API_KEY}"

def search_place(query: str) -> Optional[dict]:
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": query, "key": API_KEY, "language": "tr"}
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if data.get("results"):
            return data["results"][0]
    except Exception as e:
        print(f"  ⚠️ Search error for {query}: {e}")
    return None

def main():
    print("🇹🇷 İstanbul zenginleştirme başlıyor...")
    
    # Mevcut dosyayı oku
    if not os.path.exists(ISTANBUL_JSON_PATH):
        print(f"❌ Dosya bulunamadı: {ISTANBUL_JSON_PATH}")
        return

    with open(ISTANBUL_JSON_PATH, "r", encoding="utf-8") as f:
        city_data = json.load(f)
    
    existing_highlights = city_data.get("highlights", [])
    existing_names = {h["name"].lower() for h in existing_highlights}
    
    new_highlights = []
    
    for i, place in enumerate(NEW_PLACES, 1):
        if place["name"].lower() in existing_names:
            print(f"⏩ {place['name']} zaten var, atlanıyor.")
            continue
            
        print(f"\n[{i}/{len(NEW_PLACES)}] {place['name']} işleniyor...")
        
        search_result = search_place(place["search"])
        if not search_result:
            print(f"  ❌ Bulunamadı: {place['name']}")
            continue
            
        # Verileri çek
        geometry = search_result.get("geometry", {}).get("location", {})
        rating = search_result.get("rating", 4.5)
        photos = search_result.get("photos", [])
        photo_url = get_photo_url(photos[0]["photo_reference"]) if photos else ""
        
        # Açıklama
        desc = f"{place['name']}, İstanbul'un {place['area']} semtinde, {', '.join(place['tags'])} atmosferiyle dikkat çeken özel bir mekandır."
        
        new_item = {
            "name": place["name"],
            "area": place["area"],
            "category": place["category"],
            "subcategory": place["category"],
            "tags": place["tags"] + ["istanbul", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": geometry.get("lat", 0),
            "lng": geometry.get("lng", 0),
            "price": "medium",
            "rating": rating,
            "description": desc,
            "bestTime": "Öğleden sonra",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": photo_url,
            "tips": "Hafta sonu kalabalık olabilir.",
            "description_en": f"{place['name']} is a unique spot in Istanbul's {place['area']} district."
        }
        
        new_highlights.append(new_item)
        print(f"  ✅ Eklendi")
        time.sleep(0.5)
        
    # Listeyi birleştir
    city_data["highlights"] = existing_highlights + new_highlights
    
    # Dosyayı kaydet
    with open(ISTANBUL_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✨ İstanbul zenginleştirildi! {len(new_highlights)} yeni mekan eklendi.")
    print(f"📊 Toplam mekan sayısı: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()
