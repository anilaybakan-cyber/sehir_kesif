#!/usr/bin/env python3
"""
Roma şehir verisini zenginleştirme scripti.
'Biz Evde Yokuz' ve 'Oitheblog' kaynaklarından 40+ yeni mekan ekler.
Google Places API kullanır.
"""

import json
import requests
import time
import os
from typing import Optional

API_KEY = "AIzaSyCMEuzJpyZtG-LPG-8DFiNrSn2-KfKrQp0"
ROMA_JSON_PATH = "assets/cities/roma.json"

NEW_PLACES = [
    # Meydanlar & Manzara (Biz Evde Yokuz)
    {"name": "Giardino degli Aranci", "search": "Orange Garden Rome", "category": "Park", "area": "Aventine", "tags": ["manzara", "portakal", "gün batımı"]},
    {"name": "Piazza del Popolo", "search": "Piazza del Popolo Rome", "category": "Manzara", "area": "Centro Storico", "tags": ["meydan", "obelisk", "tarihi"]},
    {"name": "Campo de' Fiori", "search": "Campo de' Fiori Rome", "category": "Alışveriş", "area": "Centro Storico", "tags": ["pazar", "çiçek", "tarihi"]},
    {"name": "Pincio Tepesi", "search": "Pincian Hill Rome", "category": "Manzara", "area": "Villa Borghese", "tags": ["manzara", "gün batımı", "romantik"]},
    {"name": "Janiculum (Gianicolo)", "search": "Janiculum Hill Rome", "category": "Manzara", "area": "Trastevere", "tags": ["manzara", "top atışı", "sessiz"]},
    {"name": "Knights of Malta Keyhole", "search": "Knights of Malta Keyhole Rome", "category": "Deneyim", "area": "Aventine", "tags": ["gizli", "manzara", "anahtar deliği"]},
    {"name": "Piazza della Rotonda", "search": "Piazza della Rotonda Rome", "category": "Manzara", "area": "Pantheon", "tags": ["meydan", "pantheon", "çeşme"]},
    
    # Tarihi & Müzeler
    {"name": "Galleria Borghese", "search": "Galleria Borghese Rome", "category": "Müze", "area": "Villa Borghese", "tags": ["bernin", "sanat", "heykel"]},
    {"name": "Castel Sant'Angelo", "search": "Castel Sant'Angelo Rome", "category": "Tarihi", "area": "Borgo", "tags": ["kale", "manzara", "tarihi"]},
    {"name": "Terme di Caracalla", "search": "Baths of Caracalla Rome", "category": "Tarihi", "area": "San Saba", "tags": ["hamam", "antik", "harabe"]},
    {"name": "Mercati di Traiano", "search": "Trajan's Market Rome", "category": "Tarihi", "area": "Monti", "tags": ["antik", "çarşı", "tarihi"]},
    {"name": "Bocca della Verità", "search": "Mouth of Truth Rome", "category": "Tarihi", "area": "Ripa", "tags": ["efsane", "rölyef", "turistik"]},
    {"name": "Basilica di Santa Maria Maggiore", "search": "Basilica di Santa Maria Maggiore Rome", "category": "Tarihi", "area": "Esquilino", "tags": ["kilise", "mozaik", "hac"]},
    {"name": "San Luigi dei Francesi", "search": "San Luigi dei Francesi Rome", "category": "Tarihi", "area": "Navona", "tags": ["caravaggio", "sanat", "kilise"]},

    # Yeme-İçme (Oitheblog & Biz Evde Yokuz)
    {"name": "Tonnarello", "search": "Tonnarello Rome", "category": "Restoran", "area": "Trastevere", "tags": ["makarna", "popüler", "sıra"]},
    {"name": "Da Enzo al 29", "search": "Da Enzo al 29 Rome", "category": "Restoran", "area": "Trastevere", "tags": ["carbonara", "yerel", "rezervasyon"]},
    {"name": "Cantina e Cucina", "search": "Cantina e Cucina Rome", "category": "Restoran", "area": "Navona", "tags": ["modern", "kokteyl", "makarna"]},
    {"name": "Giolitti", "search": "Giolitti Rome", "category": "Cafe", "area": "Pantheon", "tags": ["dondurma", "tarihi", "çeşit"]},
    {"name": "Frigidarium", "search": "Gelateria Frigidarium Rome", "category": "Cafe", "area": "Navona", "tags": ["dondurma", "sos", "lezzetli"]},
    {"name": "Pompi", "search": "Pompi Tiramisu Rome", "category": "Cafe", "area": "Spanish Steps", "tags": ["tiramisu", "tatlı", "paket"]},
    {"name": "Sant'Eustachio Il Caffè", "search": "Sant'Eustachio Il Caffe Rome", "category": "Cafe", "area": "Pantheon", "tags": ["kahve", "tarihi", "espresso"]},
    {"name": "Roscioli Salumeria", "search": "Roscioli Salumeria con Cucina Rome", "category": "Restoran", "area": "Campo de' Fiori", "tags": ["şarküteri", "carbonara", "gurme"]},
    {"name": "Bonci Pizzarium", "search": "Bonci Pizzarium Rome", "category": "Restoran", "area": "Vatikan", "tags": ["pizza", "dilim", "meşhur"]},
    {"name": "All'Antico Vinaio Roma", "search": "All'Antico Vinaio Rome Pantheon", "category": "Restoran", "area": "Pantheon", "tags": ["sandviç", "sokak lezzeti", "popüler"]},

    # Mahalleler & Deneyimler
    {"name": "Trastevere", "search": "Trastevere Rome", "category": "Deneyim", "area": "Trastevere", "tags": ["sokak", "gece hayatı", "otantik"]},
    {"name": "Monti", "search": "Rione Monti Rome", "category": "Deneyim", "area": "Monti", "tags": ["vintage", "sanat", "butik"]},
    {"name": "Via del Corso", "search": "Via del Corso Rome", "category": "Alışveriş", "area": "Centro Storico", "tags": ["alışveriş", "cadde", "kalabalık"]},
    {"name": "Via Condotti", "search": "Via dei Condotti Rome", "category": "Alışveriş", "area": "Spanish Steps", "tags": ["lüks", "moda", "marka"]},
    {"name": "Quartiere Coppedè", "search": "Quartiere Coppede Rome", "category": "Deneyim", "area": "Trieste", "tags": ["mimari", "masalsı", "sessiz"]},
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
    print("🇮🇹 Roma zenginleştirme başlıyor...")
    
    # Mevcut dosyayı oku
    if not os.path.exists(ROMA_JSON_PATH):
        print(f"❌ Dosya bulunamadı: {ROMA_JSON_PATH}")
        return

    with open(ROMA_JSON_PATH, "r", encoding="utf-8") as f:
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
        desc = f"{place['name']}, Roma'nın {place['area']} bölgesinde, {', '.join(place['tags'])} özellikleriyle ünlü bir {place['category'].lower()} noktasıdır."
        
        new_item = {
            "name": place["name"],
            "area": place["area"],
            "category": place["category"],
            "subcategory": place["category"],
            "tags": place["tags"] + ["roma", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": geometry.get("lat", 0),
            "lng": geometry.get("lng", 0),
            "price": "medium",
            "rating": rating,
            "description": desc,
            "bestTime": "Sabah" if place["category"] == "Müze" else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": photo_url,
            "tips": "Rezervasyon şart!" if place["category"] == "Restoran" else "Rahat ayakkabı giyin.",
            "description_en": f"{place['name']} is a famous spot in Rome's {place['area']} district."
        }
        
        new_highlights.append(new_item)
        print(f"  ✅ Eklendi")
        time.sleep(0.5)
        
    # Listeyi birleştir
    city_data["highlights"] = existing_highlights + new_highlights
    
    # Dosyayı kaydet
    with open(ROMA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✨ Roma zenginleştirildi! {len(new_highlights)} yeni mekan eklendi.")
    print(f"📊 Toplam mekan sayısı: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()
