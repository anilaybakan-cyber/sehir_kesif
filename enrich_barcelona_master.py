#!/usr/bin/env python3
"""
Barcelona şehir verisini zenginleştirme scripti.
'Pegasus Blog' ve 'Biz Evde Yokuz' kaynaklarından 30+ yeni mekan ekler.
Google Places API kullanır.
"""

import json
import requests
import time
import os
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"
BARCELONA_JSON_PATH = "assets/cities/barcelona.json"

NEW_PLACES = [
    # Gizli Gaudi ve Mimari
    {"name": "Casa Vicens", "search": "Casa Vicens Gaudí", "category": "Müze", "area": "Gràcia", "tags": ["gaudi", "ilk eser", "renkli"]},
    {"name": "Palau Güell", "search": "Palau Guell Barcelona", "category": "Tarihi", "area": "El Raval", "tags": ["gaudi", "saray", "karanlık"]},
    {"name": "Hospital de Sant Pau", "search": "Recinte Modernista de Sant Pau", "category": "Tarihi", "area": "Eixample", "tags": ["modernizm", "mimari", "renkli"]},
    {"name": "Bunkers del Carmel", "search": "Bunkers del Carmel Barcelona", "category": "Manzara", "area": "Horta", "tags": ["panoramik", "gün batımı", "ücretsiz"]},
    {"name": "Casa de les Punxes", "search": "Casa de les Punxes", "category": "Tarihi", "area": "Eixample", "tags": ["modernizm", "kale", "sivri"]},
    
    # Yerel Pazarlar & Deneyim
    {"name": "Mercat de Sant Antoni", "search": "Mercat de Sant Antoni", "category": "Alışveriş", "area": "Sant Antoni", "tags": ["pazar", "yerel", "mimari"]},
    {"name": "El Born Centre de Cultura", "search": "El Born Centre de Cultura i Memoria", "category": "Müze", "area": "El Born", "tags": ["kazı", "tarihi", "kültür"]},
    {"name": "Parc del Laberint d'Horta", "search": "Parc del Laberint d'Horta", "category": "Park", "area": "Horta", "tags": ["labirent", "bahçe", "film"]},
    {"name": "Poble Espanyol", "search": "Poble Espanyol Barcelona", "category": "Müze", "area": "Montjuïc", "tags": ["mimari", "köy", "sanat"]},
    {"name": "Telefèric de Montjuïc", "search": "Teleferic de Montjuic", "category": "Manzara", "area": "Montjuïc", "tags": ["teleferik", "manzara", "kale"]},

    # Yeme-İçme (Tapas & Barlar)
    {"name": "El Xampanyet", "search": "El Xampanyet Barcelona", "category": "Restoran", "area": "El Born", "tags": ["tapas", "cava", "klasik"]},
    {"name": "Bar Cañete", "search": "Bar Canete Barcelona", "category": "Restoran", "area": "El Raval", "tags": ["tapas", "canlı", "rezervasyon"]},
    {"name": "Cervecería Catalana", "search": "Cerveceria Catalana Barcelona", "category": "Restoran", "area": "Eixample", "tags": ["tapas", "popüler", "bira"]},
    {"name": "La Xampanyeria", "search": "La Xampanyeria Can Paixano", "category": "Restoran", "area": "Barceloneta", "tags": ["cava", "ucuz", "ayakta"]},
    {"name": "Disfrutar", "search": "Disfrutar Barcelona", "category": "Restoran", "area": "Eixample", "tags": ["michelin", "modern", "deneyim"]},
    {"name": "Paradiso", "search": "Paradiso Barcelona", "category": "Bar", "area": "El Born", "tags": ["speakeasy", "kokteyl", "gizli"]},
    {"name": "Dr. Stravinsky", "search": "Dr. Stravinsky Barcelona", "category": "Bar", "area": "El Born", "tags": ["kokteyl", "lab", "ödüllü"]},
    {"name": "Satan's Coffee Corner", "search": "Satan's Coffee Corner", "category": "Cafe", "area": "Gothic Quarter", "tags": ["kahve", "hip", "sakin"]},
    {"name": "Nomad Coffee Lab", "search": "Nomad Coffee Lab & Shop", "category": "Cafe", "area": "El Born", "tags": ["kahve", "kavurma", "uzman"]},
    {"name": "Churreria Laietana", "search": "Xurreria Laietana", "category": "Cafe", "area": "Gothic Quarter", "tags": ["churros", "sıcak çikolata", "klasik"]},

    # Müzeler & Sanat
    {"name": "Museu Nacional d'Art de Catalunya", "search": "MNAC Barcelona", "category": "Müze", "area": "Montjuïc", "tags": ["sanat", "manzara", "saray"]},
    {"name": "Fundació Joan Miró", "search": "Fundacio Joan Miro Barcelona", "category": "Müze", "area": "Montjuïc", "tags": ["modern sanat", "miro", "mimari"]},
    {"name": "CosmoCaixa", "search": "CosmoCaixa Barcelona", "category": "Müze", "area": "Tibidabo", "tags": ["bilim", "orkide", "interaktif"]},
    {"name": "Museu Picasso", "search": "Museu Picasso Barcelona", "category": "Müze", "area": "El Born", "tags": ["picasso", "sanat", "tarihi"]},
    {"name": "MOCO Museum Barcelona", "search": "Moco Museum Barcelona", "category": "Müze", "area": "El Born", "tags": ["modern sanat", "banksy", "yeni"]},
    
    # Plaj & Doğa
    {"name": "Barceloneta Plajı", "search": "Barceloneta Beach", "category": "Manzara", "area": "Barceloneta", "tags": ["plaj", "deniz", "kalabalık"]},
    {"name": "Bogatell Plajı", "search": "Bogatell Beach", "category": "Manzara", "area": "Poblenou", "tags": ["plaj", "sakin", "spor"]},
    {"name": "Parc de la Ciutadella", "search": "Parc de la Ciutadella", "category": "Park", "area": "El Born", "tags": ["tekne", "çeşme", "piknik"]},
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
    print("🇪🇸 Barcelona zenginleştirme başlıyor...")
    
    # Mevcut dosyayı oku
    if not os.path.exists(BARCELONA_JSON_PATH):
        print(f"❌ Dosya bulunamadı: {BARCELONA_JSON_PATH}")
        # Dosya yoksa bile create scripti ile oluşturulmuş olabilir, kontrol et
        # Barcelona daha önce ekli değilse hata verebilir ama Aşama 2 mevcut şehirler olduğu için var sayıyoruz.
        return

    with open(BARCELONA_JSON_PATH, "r", encoding="utf-8") as f:
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
        desc = f"{place['name']}, Barcelona'nın {place['area']} bölgesinde, {', '.join(place['tags'])} atmosferiyle öne çıkan bir {place['category'].lower()} noktasıdır."
        
        new_item = {
            "name": place["name"],
            "area": place["area"],
            "category": place["category"],
            "subcategory": place["category"],
            "tags": place["tags"] + ["barcelona", place["category"].lower()],
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
            "tips": "Yerliler gibi geç saatte yiyin!" if place["category"] == "Restoran" else "Online bilet alın.",
            "description_en": f"{place['name']} is a cool spot in Barcelona's {place['area']}."
        }
        
        new_highlights.append(new_item)
        print(f"  ✅ Eklendi")
        time.sleep(0.5)
        
    # Listeyi birleştir
    city_data["highlights"] = existing_highlights + new_highlights
    
    # Dosyayı kaydet
    with open(BARCELONA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✨ Barcelona zenginleştirildi! {len(new_highlights)} yeni mekan eklendi.")
    print(f"📊 Toplam mekan sayısı: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()
