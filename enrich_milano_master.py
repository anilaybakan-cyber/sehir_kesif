#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()
"""
Milano şehir verisini zenginleştirme scripti.
'Az Gezen' ve 'Oitheblog' kaynaklarından 25+ yeni mekan ekler.
"""

import json
import requests
import time
import os
from typing import Optional

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
MILANO_JSON_PATH = "assets/cities/milano.json"

NEW_PLACES = [
    # Tarihi & Mimari
    {"name": "Duomo Terası", "search": "Duomo di Milano Terraces", "category": "Manzara", "area": "Centro Storico", "tags": ["gotik", "manzara", "heykel"]},
    {"name": "Galleria Vittorio Emanuele II", "search": "Galleria Vittorio Emanuele II", "category": "Alışveriş", "area": "Centro Storico", "tags": ["lüks", "alışveriş", "boğa mozaiği"]},
    {"name": "Sforzesco Şatosu", "search": "Sforzesco Castle", "category": "Tarihi", "area": "Parco Sempione", "tags": ["kale", "müze", "michelangelo"]},
    {"name": "Santa Maria delle Grazie", "search": "Santa Maria delle Grazie Milano", "category": "Tarihi", "area": "Magenta", "tags": ["da vinci", "son akşam yemeği", "unesco"]},
    {"name": "La Scala Operası", "search": "Teatro alla Scala", "category": "Sanat", "area": "Centro Storico", "tags": ["opera", "müzik", "sahne"]},
    
    # Modern & Tasarım (Az Gezen)
    {"name": "Bosco Verticale", "search": "Bosco Verticale Milano", "category": "Manzara", "area": "Porta Nuova", "tags": ["mimari", "yeşil", "dikey orman"]},
    {"name": "Fondazione Prada", "search": "Fondazione Prada Milano", "category": "Müze", "area": "Porta Romana", "tags": ["modern sanat", "wes anderson", "bar luce"]},
    {"name": "CityLife Shopping District", "search": "CityLife Shopping District", "category": "Alışveriş", "area": "Tre Torri", "tags": ["modern", "avm", "gökdelen"]},
    {"name": "Piazza Gae Aulenti", "search": "Piazza Gae Aulenti", "category": "Manzara", "area": "Porta Nuova", "tags": ["modern", "havuz", "fotoğraf"]},

    # Mahalleler & Deneyim (Oitheblog)
    {"name": "Navigli", "search": "Navigli Milano", "category": "Deneyim", "area": "Navigli", "tags": ["kanal", "aperitivo", "gece hayatı"]},
    {"name": "Brera Sanat Bölgesi", "search": "Brera District Milan", "category": "Deneyim", "area": "Brera", "tags": ["galeri", "romantik", "sokak"]},
    {"name": "Via Montenapoleone", "search": "Via Montenapoleone Milano", "category": "Alışveriş", "area": "Quadrilatero della Moda", "tags": ["moda", "lüks", "vitrin"]},
    {"name": "Parco Sempione", "search": "Parco Sempione Milano", "category": "Park", "area": "Sempione", "tags": ["yeşil", "piknik", "arco della pace"]},
    {"name": "San Siro Stadyumu", "search": "San Siro Stadium", "category": "Deneyim", "area": "San Siro", "tags": ["futbol", "müze", "maç"]},

    # Yeme-İçme & Aperitivo
    {"name": "Bar Luce", "search": "Bar Luce Milano", "category": "Cafe", "area": "Fondazione Prada", "tags": ["wes anderson", "retro", "tasarım"]},
    {"name": "Princi", "search": "Princi Bakery Milan", "category": "Cafe", "area": "Brera", "tags": ["fırın", "pizza", "şık"]},
    {"name": "Luini", "search": "Luini Panzerotti", "category": "Restoran", "area": "Duomo", "tags": ["panzerotti", "sokak lezzeti", "sıra"]},
    {"name": "Spontini", "search": "Pizzeria Spontini Duomo", "category": "Restoran", "area": "Duomo", "tags": ["pizza", "dilim", "kalın hamur"]},
    {"name": "Camparino in Galleria", "search": "Camparino in Galleria", "category": "Bar", "area": "Duomo", "tags": ["campari", "tarihi", "aperitivo"]},
    {"name": "Pasticceria Marchesi", "search": "Pasticceria Marchesi 1824", "category": "Cafe", "area": "Galleria", "tags": ["pastane", "tarihi", "şık"]},
    {"name": "Langosteria", "search": "Langosteria Milano", "category": "Restoran", "area": "Navigli", "tags": ["deniz ürünü", "şık", "akşam yemeği"]},
    {"name": "Dry Milano", "search": "Dry Milano Solferino", "category": "Bar", "area": "Brera", "tags": ["kokteyl", "pizza", "modern"]},

    # Müzeler
    {"name": "Pinacoteca di Brera", "search": "Pinacoteca di Brera", "category": "Müze", "area": "Brera", "tags": ["sanat", "resim", "klasik"]},
    {"name": "Museo del Novecento", "search": "Museo del Novecento", "category": "Müze", "area": "Duomo", "tags": ["20. yüzyıl", "sanat", "manzara"]},
    {"name": "Leonardo3 Museum", "search": "Leonardo3 Museum", "category": "Müze", "area": "Galleria", "tags": ["da vinci", "icat", "interaktif"]},
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
    print("🇮🇹 Milano zenginleştirme başlıyor...")
    
    if not os.path.exists(MILANO_JSON_PATH):
        print(f"❌ Dosya bulunamadı: {MILANO_JSON_PATH} - Oluşturulmaya çalışılıyor...")
        city_data = {
            "city": "Milano", 
            "country": "İtalya", 
            "description": "Moda, tasarım ve finansın başkenti. Tarihi Duomo ile modern gökdelenlerin buluştuğu yer.",
            "heroImage": "",
            "coordinates": {"lat": 45.4642, "lng": 9.1900},
            "highlights": []
        }
    else:
        with open(MILANO_JSON_PATH, "r", encoding="utf-8") as f:
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
        
        desc = f"{place['name']}, Milano'nın {place['area']} bölgesinde, {', '.join(place['tags'])} atmosferiyle öne çıkan bir {place['category'].lower()} noktasıdır."
        
        new_item = {
            "name": place["name"],
            "area": place["area"],
            "category": place["category"],
            "subcategory": place["category"],
            "tags": place["tags"] + ["milano", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": geometry.get("lat", 0),
            "lng": geometry.get("lng", 0),
            "price": "high" if place["category"] in ["Alışveriş", "Restoran"] else "medium",
            "rating": rating,
            "description": desc,
            "bestTime": "Akşam" if place["category"] == "Deneyim" else "Öğleden sonra",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": photo_url,
            "tips": "Aperitivo saatini (18:00-20:00) kaçırmayın!",
            "description_en": f"{place['name']} is a stylish spot in Milan's {place['area']}."
        }
        
        new_highlights.append(new_item)
        print(f"  ✅ Eklendi")
        time.sleep(0.5)
        
    city_data["highlights"] = existing_highlights + new_highlights
    
    if not city_data.get("heroImage") and new_highlights:
        for h in new_highlights:
             if "Duomo" in h["name"] and h.get("imageUrl"):
                city_data["heroImage"] = h["imageUrl"]
                break
    
    with open(MILANO_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✨ Milano zenginleştirildi! {len(new_highlights)} yeni mekan eklendi.")
    print(f"📊 Toplam mekan sayısı: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()
