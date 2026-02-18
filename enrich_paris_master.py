#!/usr/bin/env python3
"""
Paris şehir verisini zenginleştirme scripti.
'Biz Evde Yokuz', 'Oitheblog' ve diğer kaynaklardan toplanan 30+ yeni mekanı ekler.
Google Places API kullanarak fotoğraf ve rating çeker.
Mevcut paris.json dosyasını günceller.
"""

import json
import requests
import time
import os
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"
PARIS_JSON_PATH = "assets/cities/paris.json"

# Paris için yeni eklenecek mekanlar - Araştırma kaynaklı
NEW_PLACES = [
    # Gizli Hazineler (Biz Evde Yokuz & Oitheblog)
    {"name": "Passage des Panoramas", "search": "Passage des Panoramas Paris", "category": "Deneyim", "area": "2. Bölge", "tags": ["pasaj", "tarihi", "fotoğraf"]},
    {"name": "Galerie Vivienne", "search": "Galerie Vivienne Paris", "category": "Deneyim", "area": "2. Bölge", "tags": ["pasaj", "lüks", "tarihi"]},
    {"name": "Rue Crémieux", "search": "Rue Crémieux Paris", "category": "Manzara", "area": "12. Bölge", "tags": ["renkli evler", "instagram", "sokak"]},
    {"name": "Petit Palais", "search": "Petit Palais Paris", "category": "Müze", "area": "8. Bölge", "tags": ["sanat", "ücretsiz", "mimari"]},
    {"name": "Musée de la Vie Romantique", "search": "Museum of Romantic Life Paris", "category": "Müze", "area": "Montmartre", "tags": ["romantik", "bahçe", "gizli"]},
    {"name": "Coulée Verte René-Dumont", "search": "Coulee Verte Rene-Dumont Paris", "category": "Park", "area": "12. Bölge", "tags": ["yürüyüş yolu", "yeşil", "sessiz"]},
    {"name": "La Grande Mosquée de Paris", "search": "Grande Mosquee de Paris", "category": "Deneyim", "area": "5. Bölge", "tags": ["mimari", "çay bahçesi", "huzur"]},
    {"name": "Musée de l'Orangerie", "search": "Musee de l'Orangerie Paris", "category": "Müze", "area": "Tuileries", "tags": ["monet", "nilüferler", "sanat"]},
    {"name": "Fondation Louis Vuitton", "search": "Fondation Louis Vuitton Paris", "category": "Müze", "area": "Bois de Boulogne", "tags": ["modern sanat", "mimari", "lüks"]},
    {"name": "Atelier des Lumières", "search": "Atelier des Lumieres Paris", "category": "Sanat", "area": "11. Bölge", "tags": ["dijital sanat", "sergi", "deneyim"]},
    
    # Yeme-İçme (Oitheblog & Biz Evde Yokuz)
    {"name": "Le Train Bleu", "search": "Le Train Bleu Restaurant Paris", "category": "Restoran", "area": "Gare de Lyon", "tags": ["tarihi", "lüks", "ambiyans"]},
    {"name": "Angelina Paris", "search": "Angelina Paris Rivoli", "category": "Cafe", "area": "Rivoli", "tags": ["sıcak çikolata", "tatlı", "klasik"]},
    {"name": "Café de Flore", "search": "Cafe de Flore Paris", "category": "Cafe", "area": "Saint-Germain", "tags": ["ikonik", "edebiyat", "kahve"]},
    {"name": "Les Deux Magots", "search": "Les Deux Magots Paris", "category": "Cafe", "area": "Saint-Germain", "tags": ["tarihi", "teras", "ikonik"]},
    {"name": "Holybelly 5", "search": "Holybelly 5 Paris", "category": "Cafe", "area": "10. Bölge", "tags": ["kahvaltı", "pancake", "popüler"]},
    {"name": "Pink Mamma", "search": "Pink Mamma Paris", "category": "Restoran", "area": "Pigalle", "tags": ["italyan", "instagram", "lezzetli"]},
    {"name": "Ober Mamma", "search": "Ober Mamma Paris", "category": "Restoran", "area": "Oberkampf", "tags": ["italyan", "canlı", "kokteyl"]},
    {"name": "L'As du Fallafel", "search": "L'As du Fallafel Paris", "category": "Restoran", "area": "Le Marais", "tags": ["falafel", "sokak lezzeti", "meşhur"]},
    {"name": "Bontemps Pâtisserie", "search": "Bontemps Patisserie Paris", "category": "Cafe", "area": "Le Marais", "tags": ["tatlı", "bahçe", "şık"]},
    {"name": "Du Pain et des Idées", "search": "Du Pain et des Idees Paris", "category": "Cafe", "area": "10. Bölge", "tags": ["fırın", "kruvasan", "tarihi"]},
    
    # Alışveriş & Mahalleler
    {"name": "Merci", "search": "Merci Concept Store Paris", "category": "Alışveriş", "area": "Le Marais", "tags": ["konsept", "tasarım", "moda"]},
    {"name": "Shakespeare and Company", "search": "Shakespeare and Company Paris", "category": "Alışveriş", "area": "Latin Mahallesi", "tags": ["kitapçı", "tarihi", "ingilizce"]},
    {"name": "Le Bon Marché", "search": "Le Bon Marche Rive Gauche", "category": "Alışveriş", "area": "Saint-Germain", "tags": ["avm", "lüks", "gurme"]},
    {"name": "Samaritaine", "search": "Samaritaine Paris", "category": "Alışveriş", "area": "Pont Neuf", "tags": ["mimari", "alışveriş", "manzara"]},
    {"name": "Canal Saint-Martin", "search": "Canal Saint-Martin Paris", "category": "Deneyim", "area": "10. Bölge", "tags": ["kanal", "piknik", "amelie"]},
    {"name": "Place des Vosges", "search": "Place des Vosges Paris", "category": "Park", "area": "Le Marais", "tags": ["meydan", "tarihi", "simetrik"]},
    {"name": "Jardin du Luxembourg", "search": "Jardin du Luxembourg Paris", "category": "Park", "area": "6. Bölge", "tags": ["bahçe", "saray", "dinlenme"]},
    {"name": "Buttes-Chaumont Parkı", "search": "Parc des Buttes-Chaumont Paris", "category": "Park", "area": "19. Bölge", "tags": ["manzara", "tepe", "yerel"]},
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
    print("🇫🇷 Paris zenginleştirme başlıyor...")
    
    # Mevcut dosyayı oku
    if not os.path.exists(PARIS_JSON_PATH):
        print(f"❌ Dosya bulunamadı: {PARIS_JSON_PATH}")
        return

    with open(PARIS_JSON_PATH, "r", encoding="utf-8") as f:
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
        
        # Açıklama (Basit bir şablon, detaylar API'den gelmiyor genelde)
        desc = f"{place['name']}, Paris'in {place['area']} bölgesinde bulunan popüler bir {place['category'].lower()} noktasıdır. {', '.join(place['tags'])} özellikleri ile öne çıkar."
        
        new_item = {
            "name": place["name"],
            "area": place["area"],
            "category": place["category"],
            "subcategory": place["category"],
            "tags": place["tags"] + ["paris", place["category"].lower()],
            "distanceFromCenter": 0, # Otomatik hesaplanmalı normalde
            "lat": geometry.get("lat", 0),
            "lng": geometry.get("lng", 0),
            "price": "medium",
            "rating": rating,
            "description": desc,
            "bestTime": "Öğleden sonra",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": photo_url,
            "tips": "Rezervasyon yapmayı unutmayın." if place["category"] == "Restoran" else "Erken gitmekte fayda var.",
            "description_en": f"{place['name']} is a popular spot in Paris located in {place['area']}."
        }
        
        new_highlights.append(new_item)
        print(f"  ✅ Eklendi")
        time.sleep(0.5)
        
    # Listeyi birleştir
    city_data["highlights"] = existing_highlights + new_highlights
    
    # Dosyayı kaydet
    with open(PARIS_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✨ İşlem tamamlandı! {len(new_highlights)} yeni mekan eklendi.")
    print(f"📊 Toplam mekan sayısı: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()
