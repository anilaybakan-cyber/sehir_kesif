#!/usr/bin/env python3
"""
Kopenhag (Copenhagen) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve kopenhag.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Kopenhag'ın temel mekanları - Oitheblog & Araştırma
KOPENHAG_PLACES = [
    # İkonik & Tarihi
    {"name": "Nyhavn", "search": "Nyhavn Copenhagen", "category": "Manzara", "area": "Indre By"},
    {"name": "Tivoli Bahçeleri", "search": "Tivoli Gardens Copenhagen", "category": "Deneyim", "area": "Vesterbro"},
    {"name": "Küçük Deniz Kızı", "search": "The Little Mermaid Copenhagen", "category": "Manzara", "area": "Langelinie"},
    {"name": "Amalienborg Sarayı", "search": "Amalienborg Palace", "category": "Tarihi", "area": "Frederiksstaden"},
    {"name": "Rosenborg Kalesi", "search": "Rosenborg Castle", "category": "Tarihi", "area": "Indre By"},
    {"name": "Christiansborg Sarayı", "search": "Christiansborg Palace", "category": "Tarihi", "area": "Slotsholmen"},
    {"name": "Yuvarlak Kule (Rundetaarn)", "search": "The Round Tower Copenhagen", "category": "Manzara", "area": "Indre By"},
    {"name": "Mermer Kilise", "search": "The Marble Church Copenhagen", "category": "Tarihi", "area": "Frederiksstaden"},
    {"name": "Kastellet", "search": "Kastellet Copenhagen", "category": "Tarihi", "area": "Langelinie"},
    
    # Müzeler & Sanat
    {"name": "Ny Carlsberg Glyptotek", "search": "Ny Carlsberg Glyptotek", "category": "Müze", "area": "Vesterbro"},
    {"name": "Designmuseum Danmark", "search": "Designmuseum Danmark", "category": "Müze", "area": "Frederiksstaden"},
    {"name": "Louisiana Modern Sanat Müzesi", "search": "Louisiana Museum of Modern Art", "category": "Müze", "area": "Humlebæk (Yakın)"},
    {"name": "Danimarka Ulusal Müzesi", "search": "National Museum of Denmark", "category": "Müze", "area": "Indre By"},
    
    # Deneyim & Mahalleler
    {"name": "Freetown Christiania", "search": "Freetown Christiania", "category": "Deneyim", "area": "Christianshavn"},
    {"name": "Strøget", "search": "Stroget Copenhagen", "category": "Alışveriş", "area": "Indre By"},
    {"name": "Superkilen Parkı", "search": "Superkilen Park", "category": "Park", "area": "Nørrebro"},
    {"name": "CopenHill", "search": "CopenHill", "category": "Deneyim", "area": "Amager"},
    {"name": "Botanical Garden", "search": "Botanical Garden Copenhagen", "category": "Park", "area": "Indre By"},
    {"name": "Torvehallerne", "search": "TorvehallerneKBH", "category": "Alışveriş", "area": "Nørreport"},
    {"name": "Reffen Street Food", "search": "Reffen Copenhagen Street Food", "category": "Restoran", "area": "Refshaleøen"},
    
    # Yeme-İçme & Kafeler
    {"name": "The Coffee Collective", "search": "The Coffee Collective Jægersborggade", "category": "Cafe", "area": "Nørrebro"},
    {"name": "Democratic Coffee", "search": "Democratic Coffee Copenhagen", "category": "Cafe", "area": "Indre By"},
    {"name": "Atelier September", "search": "Atelier September Copenhagen", "category": "Cafe", "area": "Indre By"},
    {"name": "Andersen Bakery", "search": "Andersen Bakery Copenhagen", "category": "Cafe", "area": "Islands Brygge"},
    {"name": "Hart Bageri", "search": "Hart Bageri Copenhagen", "category": "Cafe", "area": "Frederiksberg"},
    {"name": "Gasoline Grill", "search": "Gasoline Grill Copenhagen", "category": "Restoran", "area": "Indre By"},
    {"name": "Hija de Sanchez", "search": "Hija de Sanchez Torvehallerne", "category": "Restoran", "area": "Nørreport"},
    {"name": "WarPigs", "search": "WarPigs Brewpub Copenhagen", "category": "Restoran", "area": "Kødbyen"},
    {"name": "Geranium", "search": "Geranium Copenhagen", "category": "Restoran", "area": "Østerbro"},
    {"name": "Noma", "search": "Noma Copenhagen", "category": "Restoran", "area": "Refshaleøen"},
    
    # Alışveriş
    {"name": "Hay House", "search": "Hay House Copenhagen", "category": "Alışveriş", "area": "Indre By"},
    {"name": "Illums Bolighus", "search": "Illums Bolighus", "category": "Alışveriş", "area": "Indre By"},
    {"name": "Magasin du Nord", "search": "Magasin du Nord Copenhagen", "category": "Alışveriş", "area": "Kongens Nytorv"},
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
        "Müze": f"{name}, Danimarka tasarımını ve sanatını keşfetmek için harika bir yer. {area} bölgesindeki bu müze, ziyaretçilerine ilham verici bir deneyim sunuyor.",
        "Tarihi": f"{name}, Kopenhag'ın kraliyet geçmişine tanıklık eden ikonik bir yapı. {area} içinde yer alan bu mekan, mimarisiyle büyülüyor.",
        "Manzara": f"{name}, şehrin kanallarını ve renkli evlerini izlemek için en iyi noktalardan. {area} bölgesindeki bu konum, klasik Kopenhag manzarası sunuyor.",
        "Deneyim": f"{name}, şehrin özgür ruhunu ve 'hygge' atmosferini hissetmek için mutlaka gidilmeli. {area}'da bulunan bu nokta, farklı bir yaşam tarzını yansıtıyor.",
        "Park": f"{name}, şehir merkezinde doğayla buluşmak ve dinlenmek için mükemmel bir alan. {area} bölgesindeki bu park, yerel halkın da favorisi.",
        "Restoran": f"{name}, Yeni İskandinav mutfağının lezzetli örneklerini sunan popüler bir mekan. {area} bölgesindeki bu restoran, taze ve yerel malzemeler kullanıyor.",
        "Cafe": f"{name}, harika kahveler ve Danimarka hamur işleri (wienerbrød) için ideal bir durak. {area}'da yer alan bu kafe, minimalist tasarımıyla dikkat çekiyor.",
        "Alışveriş": f"{name}, İskandinav tasarımı ürünler ve moda için şık bir adres. {area}'da bulunan bu mekan, kaliteli alışveriş deneyimi sunuyor.",
    }
    return descriptions.get(category, f"{name}, Kopenhag'da keşfedilmeyi bekleyen özel bir nokta.")

def main():
    print("🇩🇰 Kopenhag şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(KOPENHAG_PLACES, 1):
        print(f"\n[{i}/{len(KOPENHAG_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 55.6761)
        lng = geometry.get("lng", 12.5683)
        
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
            "tags": [place["area"].lower(), "kopenhag", "danimarka", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "high" if place["category"] in ["Restoran", "Alışveriş"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Müze", "Tarihi"] else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Bisiklet kiralayarak şehri keşfetmek en iyi yöntemdir.",
            "description_en": f"{place['name']} is a highlight of Copenhagen in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Kopenhag",
        "country": "Danimarka",
        "description": "Bisikletleri, kanalları, renkli evleri ve 'Hygge' felsefesiyle dünyanın en mutlu şehirlerinden biri. Modern tasarım, Michelin yıldızlı restoranlar ve özgür Christiania.",
        "heroImage": "",
        "coordinates": {
            "lat": 55.6761,
            "lng": 12.5683
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Nyhavn" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/kopenhag.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Kopenhag verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
