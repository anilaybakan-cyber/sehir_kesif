#!/usr/bin/env python3
"""
Edinburgh şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve edinburgh.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Edinburgh'un temel mekanları
EDINBURGH_PLACES = [
    # Tarihi & Müzeler
    {"name": "Edinburgh Kalesi", "search": "Edinburgh Castle", "category": "Tarihi", "area": "Old Town"},
    {"name": "Holyrood Sarayı", "search": "Palace of Holyroodhouse", "category": "Tarihi", "area": "Canongate"},
    {"name": "İskoçya Ulusal Müzesi", "search": "National Museum of Scotland", "category": "Müze", "area": "Old Town"},
    {"name": "St Giles Katedrali", "search": "St Giles' Cathedral", "category": "Tarihi", "area": "Royal Mile"},
    {"name": "Scott Anıtı", "search": "Scott Monument", "category": "Tarihi", "area": "Princes Street Gardens"},
    {"name": "The Real Mary King's Close", "search": "The Real Mary King's Close", "category": "Tarihi", "area": "Royal Mile"},
    {"name": "İskoçya Ulusal Galerisi", "search": "Scottish National Gallery", "category": "Müze", "area": "The Mound"},
    {"name": "Camera Obscura", "search": "Camera Obscura & World of Illusions", "category": "Müze", "area": "Royal Mile"},
    {"name": "Writers' Museum", "search": "The Writers' Museum Edinburgh", "category": "Müze", "area": "Royal Mile"},
    {"name": "Surgeons' Hall Museums", "search": "Surgeons' Hall Museums", "category": "Müze", "area": "South Bridge"},
    
    # Manzara & Parklar
    {"name": "Arthur's Seat", "search": "Arthur's Seat Edinburgh", "category": "Manzara", "area": "Holyrood Park"},
    {"name": "Calton Hill", "search": "Calton Hill Edinburgh", "category": "Manzara", "area": "Calton"},
    {"name": "Princes Street Bahçeleri", "search": "Princes Street Gardens", "category": "Park", "area": "City Centre"},
    {"name": "Royal Botanic Garden", "search": "Royal Botanic Garden Edinburgh", "category": "Park", "area": "Inverleith"},
    {"name": "Dean Village", "search": "Dean Village Edinburgh", "category": "Manzara", "area": "Dean"},
    {"name": "Water of Leith", "search": "Water of Leith Walkway", "category": "Park", "area": "Leith"},
    
    # Deneyimler & Caddeler
    {"name": "Royal Mile", "search": "Royal Mile Edinburgh", "category": "Deneyim", "area": "Old Town"},
    {"name": "Victoria Street", "search": "Victoria Street Edinburgh", "category": "Alışveriş", "area": "Old Town"},
    {"name": "Grassmarket", "search": "Grassmarket Edinburgh", "category": "Deneyim", "area": "Old Town"},
    {"name": "Leith Limanı", "search": "Shore of Leith", "category": "Deneyim", "area": "Leith"},
    {"name": "Royal Yacht Britannia", "search": "The Royal Yacht Britannia", "category": "Deneyim", "area": "Leith"},
    {"name": "Greyfriars Kirkyard", "search": "Greyfriars Kirkyard", "category": "Tarihi", "area": "Candlemaker Row"},
    {"name": "Edinburgh Dungeon", "search": "The Edinburgh Dungeon", "category": "Deneyim", "area": "Market Street"},
    {"name": "Scotch Whisky Experience", "search": "The Scotch Whisky Experience", "category": "Deneyim", "area": "Royal Mile"},
    
    # Restoranlar
    {"name": "The Witchery by the Castle", "search": "The Witchery by the Castle", "category": "Restoran", "area": "Royal Mile"},
    {"name": "Dishoom Edinburgh", "search": "Dishoom Edinburgh", "category": "Restoran", "area": "St Andrew Square"},
    {"name": "The Kitchin", "search": "The Kitchin Edinburgh", "category": "Restoran", "area": "Leith"},
    {"name": "Makars Gourmet Mash Bar", "search": "Makars Gourmet Mash Bar Edinburgh", "category": "Restoran", "area": "Mound"},
    {"name": "Oink", "search": "Oink Victoria Street Edinburgh", "category": "Restoran", "area": "Victoria Street"},
    {"name": "Howies", "search": "Howies Victoria Street", "category": "Restoran", "area": "Victoria Street"},
    {"name": "Timberyard", "search": "Timberyard Edinburgh", "category": "Restoran", "area": "Lady Lawson St"},
    {"name": "Aizle", "search": "Aizle Edinburgh", "category": "Restoran", "area": "Charlotte Square"},
    {"name": "Angels with Bagpipes", "search": "Angels with Bagpipes", "category": "Restoran", "area": "Royal Mile"},
    
    # Kafeler ve Publar
    {"name": "The Elephant House", "search": "The Elephant House Edinburgh", "category": "Cafe", "area": "George IV Bridge"},
    {"name": "The Milkman", "search": "The Milkman Edinburgh", "category": "Cafe", "area": "Cockburn Street"},
    {"name": "Cairngorm Coffee", "search": "Cairngorm Coffee Edinburgh", "category": "Cafe", "area": "Melville Place"},
    {"name": "World's End", "search": "The World's End Edinburgh", "category": "Bar", "area": "Royal Mile"},
    {"name": "The Last Drop", "search": "The Last Drop Edinburgh", "category": "Bar", "area": "Grassmarket"},
    {"name": "Panda & Sons", "search": "Panda & Sons Edinburgh", "category": "Bar", "area": "Queen Street"},
    {"name": "Sandy Bell's", "search": "Sandy Bell's Edinburgh", "category": "Bar", "area": "Forrest Road"},
    {"name": "The Dome", "search": "The Dome Edinburgh", "category": "Bar", "area": "George Street"},
    
    # Alışveriş
    {"name": "Jenners", "search": "Jenners Edinburgh", "category": "Alışveriş", "area": "Princes Street"},
    {"name": "Waverley Mall", "search": "Waverley Mall Edinburgh", "category": "Alışveriş", "area": "Waverley"},
    {"name": "Multrees Walk", "search": "Multrees Walk Edinburgh", "category": "Alışveriş", "area": "St Andrew Square"},
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
        "Müze": f"{name}, Edinburgh'un kültürel mirasını keşfetmek için harika bir durak. {area} bölgesindeki bu müze, İskoç tarihini ve sanatını yakından tanımanızı sağlıyor.",
        "Tarihi": f"{name}, şehrin en ikonik tarihi yapılarından biri. {area}'da yer alan bu mekan, gotik mimarisi ve büyüleyici atmosferiyle sizi Orta Çağ'a götürecek.",
        "Manzara": f"{name}, Edinburgh'un silüetini izlemek için en iyi noktalardan. {area} bölgesindeki bu konum, özellikle gün batımında nefes kesici manzaralar sunuyor.",
        "Deneyim": f"{name}, Edinburgh ruhunu hissetmek için mutlaka görülmeli. {area}'da bulunan bu nokta, Harry Potter dünyasından izler taşıyan sokakları ve canlı atmosferiyle ünlü.",
        "Park": f"{name}, şehir merkezinde doğayla buluşmak için ideal bir kaçış noktası. {area} bölgesindeki bu park, piknik yapmak ve dinlenmek için mükemmel.",
        "Restoran": f"{name}, İskoç mutfağının modern yorumlarını tadabileceğiniz şık bir mekan. {area} bölgesindeki bu restoran, yerel malzemelerle hazırlanan lezzetli menüsüyle dikkat çekiyor.",
        "Cafe": f"{name}, Edinburgh'un edebi atmosferini soluyabileceğiniz sıcak bir kafe. {area}'da yer alan bu mekan, JK Rowling gibi yazarların ilham aldığı yerlerden biri.",
        "Bar": f"{name}, geleneksel İskoç pub kültürünü deneyimlemek için harika bir seçenek. {area}'daki bu mekan, geniş viski koleksiyonu ve canlı halk müziğiyle keyifli bir akşam vaat ediyor.",
        "Alışveriş": f"{name}, alışveriş meraklıları için şehrin kalbinde bir merkez. {area}'da bulunan bu mekan, İskoç yünü (kaşmir, tartan) ve hediyelik eşya için ideal.",
    }
    return descriptions.get(category, f"{name}, Edinburgh'da keşfedilmeyi bekleyen büyüleyici bir yer.")

def main():
    print("🏰 Edinburgh şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(EDINBURGH_PLACES, 1):
        print(f"\n[{i}/{len(EDINBURGH_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 55.9533)
        lng = geometry.get("lng", -3.1883)
        
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
            "tags": [place["area"].lower(), "edinburgh", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "low" if place["category"] in ["Park", "Manzara"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Müze", "Tarihi"] else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Yağmurluk almayı unutmayın, hava çok değişken olabilir!",
            "description_en": f"{place['name']} is a highlight of Edinburgh in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Edinburgh",
        "country": "İskoçya",
        "description": "Tarihi kaleleri, Arnavut kaldırımlı sokakları ve edebi mirasıyla büyüleyici bir başkent. Harry Potter'ın doğduğu, festivallerin ve viskinin şehri.",
        "heroImage": "",
        "coordinates": {
            "lat": 55.9533,
            "lng": -3.1883
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if h["name"] == "Edinburgh Kalesi" and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/edinburgh.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Edinburgh verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
