#!/usr/bin/env python3
"""
Budapeşte şehir verisini zenginleştirme scripti.
'Gezipgördüm' kaynaklarından 20+ yeni mekan ekler.
"""

import json
import requests
import time
import os
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"
BUDAPESTE_JSON_PATH = "assets/cities/budapeste.json"

NEW_PLACES = [
    # Tarihi & Manzara
    {"name": "Parlamento Binası", "search": "Hungarian Parliament Building", "category": "Tarihi", "area": "Pest", "tags": ["simgesel", "gotik", "nehir"]},
    {"name": "Buda Kalesi", "search": "Buda Castle", "category": "Tarihi", "area": "Buda", "tags": ["kale", "manzara", "müze"]},
    {"name": "Balıkçı Tabyası (Fisherman's Bastion)", "search": "Fisherman's Bastion Budapest", "category": "Manzara", "area": "Buda", "tags": ["fotoğraf", "tarihi", "masalsı"]},
    {"name": "Matthias Kilisesi", "search": "Matthias Church Budapest", "category": "Tarihi", "area": "Buda", "tags": ["kilise", "renkli çatı", "gotik"]},
    {"name": "Zincirli Köprü (Chain Bridge)", "search": "Szechenyi Chain Bridge", "category": "Manzara", "area": "Tuna", "tags": ["köprü", "ışıklar", "ikonik"]},
    {"name": "Aziz Stephen Bazilikası", "search": "St. Stephen's Basilica", "category": "Tarihi", "area": "Pest", "tags": ["kilise", "kubbeye çıkış", "heybetli"]},
    {"name": "Kahramanlar Meydanı", "search": "Heroes' Square Budapest", "category": "Tarihi", "area": "Pest", "tags": ["meydan", "heykel", "tarih"]},
    {"name": "Gellert Tepesi", "search": "Gellert Hill", "category": "Manzara", "area": "Buda", "tags": ["manzara", "özgürlük anıtı", "tırmanış"]},

    # Termaller & Deneyim (Gezipgördüm)
    {"name": "Széchenyi Termal Hamamı", "search": "Szechenyi Thermal Bath", "category": "Deneyim", "area": "City Park", "tags": ["hamam", "parti", "sıcak su"]},
    {"name": "Gellert Hamamı", "search": "Gellert Thermal Bath", "category": "Deneyim", "area": "Buda", "tags": ["mimari", "lüks", "tarihi"]},
    {"name": "Margaret Adası", "search": "Margaret Island Budapest", "category": "Park", "area": "Tuna", "tags": ["park", "yürüyüş", "fıskiye"]},
    {"name": "Şehir Parkı (Városliget)", "search": "City Park Budapest", "category": "Park", "area": "Pest", "tags": ["buz pateni", "kale", "yeşil"]},
    {"name": "Ayakkabılar Anıtı", "search": "Shoes on the Danube Bank", "category": "Tarihi", "area": "Pest", "tags": ["anıt", "duygusal", "nehir"]},

    # Ruin Barlar & Yeme-İçme
    {"name": "Szimpla Kert", "search": "Szimpla Kert", "category": "Bar", "area": "Jewish Quarter", "tags": ["ruin bar", "orijinal", "kaotik"]},
    {"name": "New York Café", "search": "New York Cafe Budapest", "category": "Cafe", "area": "Pest", "tags": ["dünyanın en güzel kafesi", "lüks", "tarihi"]},
    {"name": "Mazel Tov", "search": "Mazel Tov Budapest", "category": "Restoran", "area": "Jewish Quarter", "tags": ["ortadoğu", "ferah", "popüler"]},
    {"name": "Karavan Street Food", "search": "Karavan Street Food Budapest", "category": "Restoran", "area": "Jewish Quarter", "tags": ["sokak lezzeti", "bahçe", "çeşit"]},
    {"name": "Instant-Fogas", "search": "Instant-Fogas Complex", "category": "Bar", "area": "Pest", "tags": ["dev kulüp", "parti", "labirent"]},
    {"name": "Ruszwurm", "search": "Ruszwurm Confectionery", "category": "Cafe", "area": "Buda", "tags": ["pasta", "en eski", "kremalı pasta"]},
    {"name": "For Sale Pub", "search": "For Sale Pub Budapest", "category": "Restoran", "area": "Pest", "tags": ["yer fıstığı", "notlar", "orijinal"]},
    
    # Müzeler
    {"name": "Macaristan Ulusal Müzesi", "search": "Hungarian National Museum", "category": "Müze", "area": "Pest", "tags": ["tarih", "kültür", "bina"]},
    {"name": "Terror Háza (Terör Evi)", "search": "House of Terror Budapest", "category": "Müze", "area": "Pest", "tags": ["tarih", "gizli polis", "etkileyici"]},
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
    print("🇭🇺 Budapeşte zenginleştirme başlıyor...")
    
    if not os.path.exists(BUDAPESTE_JSON_PATH):
        print(f"❌ Dosya bulunamadı: {BUDAPESTE_JSON_PATH} - Oluşturulmaya çalışılıyor...")
        city_data = {
            "city": "Budapeşte", 
            "country": "Macaristan", 
            "description": "Tuna'nın incisi. Termal hamamlar, Ruin barlar ve görkemli mimari.",
            "heroImage": "",
            "coordinates": {"lat": 47.4979, "lng": 19.0402},
            "highlights": []
        }
    else:
        with open(BUDAPESTE_JSON_PATH, "r", encoding="utf-8") as f:
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
            
        geometry = search_result.get("geometry", {}).get("location", {})
        rating = search_result.get("rating", 4.5)
        photos = search_result.get("photos", [])
        photo_url = get_photo_url(photos[0]["photo_reference"]) if photos else ""
        
        desc = f"{place['name']}, Budapeşte'nin {place['area']} bölgesinde, {', '.join(place['tags'])} özellikleriyle öne çıkan bir {place['category'].lower()} noktasıdır."
        
        new_item = {
            "name": place["name"],
            "area": place["area"],
            "category": place["category"],
            "subcategory": place["category"],
            "tags": place["tags"] + ["budapeşte", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": geometry.get("lat", 0),
            "lng": geometry.get("lng", 0),
            "price": "low" if place["category"] == "Bar" else "medium",
            "rating": rating,
            "description": desc,
            "bestTime": "Akşam" if place["category"] == "Bar" else "Gündüz",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": photo_url,
            "tips": "Szimpla Kert'e pazar günü giderseniz pazar kuruluyor!",
            "description_en": f"{place['name']} is a cool spot in Budapest's {place['area']}."
        }
        
        new_highlights.append(new_item)
        print(f"  ✅ Eklendi")
        time.sleep(0.5)
        
    city_data["highlights"] = existing_highlights + new_highlights
    
    if not city_data.get("heroImage") and new_highlights:
        for h in new_highlights:
             if "Parlamento" in h["name"] and h.get("imageUrl"):
                city_data["heroImage"] = h["imageUrl"]
                break
    
    with open(BUDAPESTE_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✨ Budapeşte zenginleştirildi! {len(new_highlights)} yeni mekan eklendi.")
    print(f"📊 Toplam mekan sayısı: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()
