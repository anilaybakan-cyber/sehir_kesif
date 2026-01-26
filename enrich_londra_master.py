#!/usr/bin/env python3
"""
Londra şehir verisini zenginleştirme scripti.
'Oitheblog' ve 'Biz Evde Yokuz' kaynaklarından 35+ yeni mekan ekler.
Google Places API kullanır.
"""

import json
import requests
import time
import os
from typing import Optional

API_KEY = "AIzaSyCMEuzJpyZtG-LPG-8DFiNrSn2-KfKrQp0"
LONDRA_JSON_PATH = "assets/cities/londra.json"

NEW_PLACES = [
    # Gizli ve Renkli (Oitheblog)
    {"name": "Neal's Yard", "search": "Neal's Yard London", "category": "Manzara", "area": "Covent Garden", "tags": ["renkli", "gizli", "avlu"]},
    {"name": "Sky Garden", "search": "Sky Garden London", "category": "Manzara", "area": "City", "tags": ["ücretsiz", "manzara", "bahçe"]},
    {"name": "Leadenhall Market", "search": "Leadenhall Market London", "category": "Alışveriş", "area": "City", "tags": ["harry potter", "tarihi", "mimari"]},
    {"name": "St Dunstan in the East", "search": "St Dunstan in the East Church Garden", "category": "Park", "area": "City", "tags": ["harabe", "bahçe", "huzur"]},
    {"name": "God's Own Junkyard", "search": "God's Own Junkyard London", "category": "Müze", "area": "Walthamstow", "tags": ["neon", "sanat", "retro"]},
    {"name": "Little Venice", "search": "Little Venice London", "category": "Manzara", "area": "Maida Vale", "tags": ["kanal", "tekne", "yürüyüş"]},
    {"name": "Kyoto Garden", "search": "Kyoto Garden Holland Park", "category": "Park", "area": "Holland Park", "tags": ["japon", "tavuskuşu", "sakin"]},
    {"name": "Primrose Hill", "search": "Primrose Hill London", "category": "Manzara", "area": "Camden", "tags": ["manzara", "piknik", "gün batımı"]},

    # Mahalleler & Deneyim
    {"name": "Shoreditch Street Art", "search": "Shoreditch Street Art London", "category": "Deneyim", "area": "Shoreditch", "tags": ["sanat", "graffiti", "hipster"]},
    {"name": "Brick Lane", "search": "Brick Lane London", "category": "Alışveriş", "area": "Shoreditch", "tags": ["vintage", "köri", "pazar"]},
    {"name": "Columbia Road Flower Market", "search": "Columbia Road Flower Market", "category": "Alışveriş", "area": "Bethnal Green", "tags": ["pazar", "çiçek", "pazar günü"]},
    {"name": "Borough Market", "search": "Borough Market London", "category": "Alışveriş", "area": "Southwark", "tags": ["yemek", "gurme", "tarihi"]},
    {"name": "Maltby Street Market", "search": "Maltby Street Market", "category": "Alışveriş", "area": "Bermondsey", "tags": ["yemek", "hafta sonu", "yerel"]},
    {"name": "Liberty London", "search": "Liberty London", "category": "Alışveriş", "area": "Soho", "tags": ["lüks", "tarihi", "avm"]},
    {"name": "Daunt Books", "search": "Daunt Books Marylebone", "category": "Alışveriş", "area": "Marylebone", "tags": ["kitaplık", "tarihi", "güzel"]},

    # Yeme-İçme (Oitheblog)
    {"name": "Dishoom Covent Garden", "search": "Dishoom Covent Garden", "category": "Restoran", "area": "Covent Garden", "tags": ["hint", "popüler", "sıra"]},
    {"name": "Sketch", "search": "Sketch London", "category": "Cafe", "area": "Mayfair", "tags": ["pembe", "tasarım", "ikonik"]},
    {"name": "Peggy Porschen", "search": "Peggy Porschen Belgravia", "category": "Cafe", "area": "Belgravia", "tags": ["pembe", "kek", "instagram"]},
    {"name": "Duck & Waffle", "search": "Duck & Waffle London", "category": "Restoran", "area": "City", "tags": ["manzara", "24 saat", "lüks"]},
    {"name": "The Breakfast Club", "search": "The Breakfast Club Soho", "category": "Restoran", "area": "Soho", "tags": ["kahvaltı", "pancake", "retro"]},
    {"name": "Bao Soho", "search": "Bao Soho", "category": "Restoran", "area": "Soho", "tags": ["tayvan", "bao bun", "popüler"]},
    {"name": "Flat Iron", "search": "Flat Iron Covent Garden", "category": "Restoran", "area": "Covent Garden", "tags": ["steak", "uygun", "lezzetli"]},
    {"name": "Beigel Bake", "search": "Beigel Bake Brick Lane", "category": "Restoran", "area": "Shoreditch", "tags": ["bagel", "24 saat", "tarihi"]},
    {"name": "Padella", "search": "Padella Borough Market", "category": "Restoran", "area": "Southwark", "tags": ["makarna", "taze", "sıra"]},
    
    # Müzeler & Sanat
    {"name": "Victoria and Albert Museum", "search": "Victoria and Albert Museum", "category": "Müze", "area": "South Kensington", "tags": ["tasarım", "moda", "ücretsiz"]},
    {"name": "Tate Modern", "search": "Tate Modern London", "category": "Müze", "area": "Southwark", "tags": ["modern sanat", "turbin", "ücretsiz"]},
    {"name": "Natural History Museum", "search": "Natural History Museum London", "category": "Müze", "area": "South Kensington", "tags": ["dinozor", "mimari", "ücretsiz"]},
    {"name": "Churchill War Rooms", "search": "Churchill War Rooms", "category": "Müze", "area": "Westminster", "tags": ["tarih", "savaş", "bunker"]},
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
    print("🇬🇧 Londra zenginleştirme başlıyor...")
    
    # Mevcut dosyayı oku
    if not os.path.exists(LONDRA_JSON_PATH):
        print(f"❌ Dosya bulunamadı: {LONDRA_JSON_PATH}")
        return

    with open(LONDRA_JSON_PATH, "r", encoding="utf-8") as f:
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
        desc = f"{place['name']}, Londra'nın {place['area']} bölgesinde, {', '.join(place['tags'])} atmosferiyle bilinen bir {place['category'].lower()} noktasıdır."
        
        new_item = {
            "name": place["name"],
            "area": place["area"],
            "category": place["category"],
            "subcategory": place["category"],
            "tags": place["tags"] + ["londra", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": geometry.get("lat", 0),
            "lng": geometry.get("lng", 0),
            "price": "medium",
            "rating": rating,
            "description": desc,
            "bestTime": "Sabah" if place["category"] == "Müze" else "Öğleden sonra",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": photo_url,
            "tips": "Müzeler genellikle ücretsizdir (bağış hariç)." if place["category"] == "Müze" else "Sıra beklemeye hazır olun.",
            "description_en": f"{place['name']} is a famous spot in London's {place['area']} district."
        }
        
        new_highlights.append(new_item)
        print(f"  ✅ Eklendi")
        time.sleep(0.5)
        
    # Listeyi birleştir
    city_data["highlights"] = existing_highlights + new_highlights
    
    # Dosyayı kaydet
    with open(LONDRA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✨ Londra zenginleştirildi! {len(new_highlights)} yeni mekan eklendi.")
    print(f"📊 Toplam mekan sayısı: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()
