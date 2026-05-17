#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()
"""
Berlin şehir verisini zenginleştirme scripti.
'Oitheblog' ve 'Biz Evde Yokuz' kaynaklarından 30+ yeni mekan ekler.
"""

import json
import requests
import time
import os
from typing import Optional

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
BERLIN_JSON_PATH = "assets/cities/berlin.json"

NEW_PLACES = [
    # Tarihi & Duvar
    {"name": "East Side Gallery", "search": "East Side Gallery Berlin", "category": "Müze", "area": "Friedrichshain", "tags": ["duvar", "sanat", "tarihi"]},
    {"name": "Berlin Duvarı Anıtı", "search": "Berlin Wall Memorial Bernauer Strasse", "category": "Tarihi", "area": "Mitte", "tags": ["duvar", "açık hava", "duygusal"]},
    {"name": "Topography of Terror", "search": "Topography of Terror", "category": "Müze", "area": "Kreuzberg", "tags": ["tarih", "savaş", "ücretsiz"]},
    {"name": "Checkpoint Charlie", "search": "Checkpoint Charlie", "category": "Tarihi", "area": "Mitte", "tags": ["sınır", "turistik", "fotoğraf"]},
    {"name": "Yahudi Müzesi (Jewish Museum)", "search": "Jewish Museum Berlin", "category": "Müze", "area": "Kreuzberg", "tags": ["mimari", "tarih", "etkileyici"]},
    {"name": "Bebelplatz", "search": "Bebelplatz Berlin", "category": "Tarihi", "area": "Mitte", "tags": ["kitap yakma", "meydan", "tarihi"]},

    # Alternatif & Kreuzberg (Oitheblog)
    {"name": "Kreuzberg", "search": "Kreuzberg Berlin", "category": "Deneyim", "area": "Kreuzberg", "tags": ["sokak sanatı", "genç", "hipster"]},
    {"name": "Markthalle Neun", "search": "Markthalle Neun", "category": "Alışveriş", "area": "Kreuzberg", "tags": ["sokak lezzeti", "perşembe", "pazar"]},
    {"name": "Viktoriapark", "search": "Viktoriapark Berlin", "category": "Park", "area": "Kreuzberg", "tags": ["şelale", "manzara", "bira"]},
    {"name": "Admiralbrücke", "search": "Admiralbrücke Berlin", "category": "Deneyim", "area": "Kreuzberg", "tags": ["köprü", "gün batımı", "sosyal"]},
    {"name": "SO36", "search": "SO36 Berlin", "category": "Deneyim", "area": "Kreuzberg", "tags": ["kulüp", "tarihi", "punk"]},
    {"name": "Urban Spree", "search": "Urban Spree", "category": "Sanat", "area": "Friedrichshain", "tags": ["sanat", "bahçe", "alternatif"]},
    {"name": "RAW-Gelände", "search": "RAW-Gelaende Berlin", "category": "Deneyim", "area": "Friedrichshain", "tags": ["graffiti", "sanat", "gece hayatı"]},
    {"name": "Mauerpark", "search": "Mauerpark", "category": "Park", "area": "Prenzlauer Berg", "tags": ["karaoke", "bit pazarı", "pazar günü"]},
    {"name": "Teufelsberg", "search": "Teufelsberg Spy Station", "category": "Manzara", "area": "Grunewald", "tags": ["terk edilmiş", "casus", "sanat"]},

    # Yeme-İçme (Mustafa's vb.)
    {"name": "Mustafa's Gemüse Kebap", "search": "Mustafa's Gemuse Kebap", "category": "Restoran", "area": "Kreuzberg", "tags": ["kebap", "meşhur", "sıra"]},
    {"name": "Curry 36", "search": "Curry 36 Mehringdamm", "category": "Restoran", "area": "Kreuzberg", "tags": ["currywurst", "klasik", "hızlı"]},
    {"name": "Burgermeister Schlesisches Tor", "search": "Burgermeister Schlesisches Tor", "category": "Restoran", "area": "Kreuzberg", "tags": ["burger", "tuvalet", "kült"]},
    {"name": "The Barn", "search": "THE BARN Cafe Kranzler", "category": "Cafe", "area": "Mitte", "tags": ["kahve", "nitelikli", "modern"]},
    {"name": "Five Elephant", "search": "Five Elephant Kreuzberg", "category": "Cafe", "area": "Kreuzberg", "tags": ["cheesecake", "kahve", "roastery"]},
    {"name": "Father Carpenter", "search": "Father Carpenter Berlin", "category": "Cafe", "area": "Mitte", "tags": ["kahvaltı", "avlu", "şık"]},
    {"name": "Prater Biergarten", "search": "Prater Beer Garden", "category": "Restoran", "area": "Prenzlauer Berg", "tags": ["bira bahçesi", "yaz", "tarihi"]},
    {"name": "Klunkerkranich", "search": "Klunkerkranich", "category": "Bar", "area": "Neukölln", "tags": ["çatı", "gün batımı", "alternatif"]},
    
    # Müzeler
    {"name": "Pergamon Müzesi", "search": "Pergamon Museum", "category": "Müze", "area": "Müzeler Adası", "tags": ["antik", "babil", "tarih"]},
    {"name": "Neues Museum", "search": "Neues Museum Berlin", "category": "Müze", "area": "Müzeler Adası", "tags": ["nefertiti", "mısır", "tarih"]},
    {"name": "DDR Müzesi", "search": "DDR Museum", "category": "Müze", "area": "Mitte", "tags": ["doğu almanya", "interaktif", "yaşam"]},
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
    print("🇩🇪 Berlin zenginleştirme başlıyor...")
    
    if not os.path.exists(BERLIN_JSON_PATH):
        print(f"❌ Dosya bulunamadı: {BERLIN_JSON_PATH} - Oluşturulmaya çalışılıyor...")
        # Basit bir taslak oluştur
        city_data = {
            "city": "Berlin", 
            "country": "Almanya", 
            "description": "Özgürlüğün ve tarihin başkenti.",
            "heroImage": "",
            "coordinates": {"lat": 52.5200, "lng": 13.4050},
            "highlights": []
        }
    else:
        with open(BERLIN_JSON_PATH, "r", encoding="utf-8") as f:
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
        
        desc = f"{place['name']}, Berlin'in {place['area']} bölgesinde, {', '.join(place['tags'])} özellikleriyle bilinen bir {place['category'].lower()} noktasıdır."
        
        new_item = {
            "name": place["name"],
            "area": place["area"],
            "category": place["category"],
            "subcategory": place["category"],
            "tags": place["tags"] + ["berlin", place["category"].lower()],
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
            "tips": "Nakit taşımanız iyi olur, Berlin'de kart her yerde geçmeyebilir.",
            "description_en": f"{place['name']} is a cool spot in Berlin's {place['area']}."
        }
        
        new_highlights.append(new_item)
        print(f"  ✅ Eklendi")
        time.sleep(0.5)
        
    city_data["highlights"] = existing_highlights + new_highlights
    
    # Hero image yoksa ekle
    if not city_data.get("heroImage") and new_highlights:
        for h in new_highlights:
             if "East Side" in h["name"] and h.get("imageUrl"):
                city_data["heroImage"] = h["imageUrl"]
                break
    
    with open(BERLIN_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✨ Berlin zenginleştirildi! {len(new_highlights)} yeni mekan eklendi.")
    print(f"📊 Toplam mekan sayısı: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()
