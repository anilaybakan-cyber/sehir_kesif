from dotenv import load_dotenv
load_dotenv()
import os
#!/usr/bin/env python3
"""
Strazburg (Strasbourg) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve strazburg.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Strazburg'un temel mekanları - Oitheblog
STRAZBURG_PLACES = [
    # Petite France & Tarihi
    {"name": "Petite France", "search": "Petite France Strasbourg", "category": "Manzara", "area": "Grande Île"},
    {"name": "Strazburg Katedrali", "search": "Cathedrale Notre Dame de Strasbourg", "category": "Tarihi", "area": "Merkez"},
    {"name": "Maison Kammerzell", "search": "Maison Kammerzell", "category": "Tarihi", "area": "Katedral Yanı"},
    {"name": "Ponts Couverts (Kapalı Köprüler)", "search": "Ponts Couverts Strasbourg", "category": "Manzara", "area": "Petite France"},
    {"name": "Barrage Vauban", "search": "Barrage Vauban", "category": "Manzara", "area": "Petite France"},
    {"name": "Place Kléber", "search": "Place Kleber Strasbourg", "category": "Alışveriş", "area": "Merkez"},
    {"name": "Place Gutenberg", "search": "Place Gutenberg Strasbourg", "category": "Tarihi", "area": "Merkez"},
    {"name": "Rohan Sarayı", "search": "Palais Rohan Strasbourg", "category": "Müze", "area": "Merkez"},

    # Avrupa Kurumları & Parklar
    {"name": "Avrupa Parlamentosu", "search": "European Parliament Strasbourg", "category": "Tarihi", "area": "Quartier Européen"},
    {"name": "Parc de l'Orangerie", "search": "Parc de l'Orangerie", "category": "Park", "area": "Orangerie"},
    {"name": "Alsace Müzesi", "search": "Musee Alsacien", "category": "Müze", "area": "Krutenau"},

    # Yeme-İçme (Alsace Mutfağı)
    {"name": "Maison des Tanneurs", "search": "Maison des Tanneurs", "category": "Restoran", "area": "Petite France"},
    {"name": "Au Pont Saint-Martin", "search": "Au Pont Saint Martin Strasbourg", "category": "Restoran", "area": "Petite France"},
    {"name": "Le Clou", "search": "Winstub Le Clou", "category": "Restoran", "area": "Merkez"},
    {"name": "Chez Yvonne", "search": "Chez Yvonne Strasbourg", "category": "Restoran", "area": "Merkez"},
    {"name": "Café Bretelles", "search": "Cafe Bretelles Petite France", "category": "Cafe", "area": "Petite France"},
    {"name": "Christian", "search": "Christian Patisserie Strasbourg", "category": "Cafe", "area": "Merkez"},
    
    # Noel Pazarı (Sezonluk ama önemli)
    {"name": "Christkindelsmärik", "search": "Place Broglie Christmas Market", "category": "Deneyim", "area": "Place Broglie"},
]

def get_photo_url(photo_reference: str) -> str:
    """Google Places photo URL oluşturur."""
    return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={photo_reference}&key={API_KEY}"

def search_place(query: str) -> Optional[dict]:
    """Google Places Text Search ile mekan arar."""
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": API_KEY,
        "language": "tr"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if data.get("results"):
            return data["results"][0]
    except Exception as e:
        print(f"  ⚠️ Search error: {e}")
    return None

def get_place_details(place_id: str) -> Optional[dict]:
    """Google Places Details ile detaylı bilgi alır."""
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "key": API_KEY,
        "language": "tr",
        "fields": "name,rating,user_ratings_total,geometry,photos,formatted_address,editorial_summary,types"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        return data.get("result")
    except Exception as e:
        print(f"  ⚠️ Details error: {e}")
    return None

def generate_description(name: str, category: str, area: str) -> str:
    """Kategori bazlı açıklama oluşturur."""
    descriptions = {
        "Müze": f"{name}, Alsace kültürünü ve tarihini yansıtan önemli bir mekan. {area} bölgesindeki bu müze, ziyaretçilerine zengin bir içerik sunuyor.",
        "Tarihi": f"{name}, Strazburg'un ikonik yapılarından biri. {area} içinde yer alan bu tarihi mekan, eşsiz mimarisiyle dikkat çekiyor.",
        "Manzara": f"{name}, şehrin kanallarını ve orta çağ evlerini izlemek için mükemmel bir nokta. {area} bölgesindeki bu konum, masalsı bir atmosfer sunuyor.",
        "Restoran": f"{name}, Alsace mutfağının (Lahmacun benzeri Tarte Flambée, Choucroute) en iyi örneklerini tadabileceğiniz yerel bir restoran (Winstub). {area} bölgesinde.",
        "Cafe": f"{name}, harika bir kahve veya tatlı molası için ideal. {area}'da yer alan bu kafe, şık ve samimi.",
        "Park": f"{name}, şehrin içinde leylekleri görebileceğiniz ve dinlenebileceğiniz yeşil bir alan. {area} bölgesindeki bu park çok popüler.",
    }
    return descriptions.get(category, f"{name}, Strazburg'da keşfedilmeyi bekleyen büyüleyici bir yer.")

def main():
    print("🇫🇷 Strazburg şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(STRAZBURG_PLACES, 1):
        print(f"\n[{i}/{len(STRAZBURG_PLACES)}] {place['name']} işleniyor...")
        
        # Google'da ara
        search_result = search_place(place["search"])
        if not search_result:
            print(f"  ❌ Bulunamadı, atlanıyor...")
            continue
        
        place_id = search_result.get("place_id")
        
        # Detayları al
        details = get_place_details(place_id) if place_id else None
        
        # Koordinatlar
        geometry = search_result.get("geometry", {}).get("location", {})
        lat = geometry.get("lat", 48.5734)
        lng = geometry.get("lng", 7.7521)
        
        # Rating
        rating = search_result.get("rating") or details.get("rating") if details else None
        
        # Fotoğraf
        photo_ref = None
        photos = search_result.get("photos") or (details.get("photos") if details else None)
        if photos:
            photo_ref = photos[0].get("photo_reference")
        
        # Editorial summary varsa kullan
        description = None
        if details and details.get("editorial_summary"):
            description = details["editorial_summary"].get("overview")
        
        if not description:
            description = generate_description(place["name"], place["category"], place["area"])
        
        highlight = {
            "name": place["name"],
            "area": place["area"],
            "category": place["category"],
            "subcategory": place["category"],
            "tags": [place["area"].lower(), "strazburg", "fransa", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Her zaman",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Noel zamanı giderseniz erken rezervasyon şart.",
            "description_en": f"{place['name']} is a highlight of Strasbourg in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Strazburg",
        "country": "Fransa",
        "description": "Fransa ve Almanya'nın mükemmel karışımı. Petite France'ın kanalları, ahşap evleri, görkemli katedrali ve dünyanın en ünlü Noel pazarlarından biri.",
        "heroImage": "",
        "coordinates": {
            "lat": 48.5734,
            "lng": 7.7521
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Petite France" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/strazburg.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Strazburg verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
