#!/usr/bin/env python3
"""
Antalya şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve antalya.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyCMEuzJpyZtG-LPG-8DFiNrSn2-KfKrQp0"

# Antalya'nın temel mekanları - Gezimanya & Biz Evde Yokuz
ANTALYA_PLACES = [
    # Tarihi & Kaleiçi
    {"name": "Kaleiçi", "search": "Kaleici Antalya Old Town", "category": "Deneyim", "area": "Merkez"},
    {"name": "Hadrian Kapısı (Üç Kapılar)", "search": "Hadrian's Gate", "category": "Tarihi", "area": "Kaleiçi"},
    {"name": "Yivli Minare", "search": "Yivliminare Mosque", "category": "Tarihi", "area": "Kaleiçi"},
    {"name": "Hıdırlık Kulesi", "search": "Hidirlik Tower", "category": "Tarihi", "area": "Kaleiçi"},
    {"name": "Kesik Minare (Korkut Camii)", "search": "Kesik Minare Cami", "category": "Tarihi", "area": "Kaleiçi"},
    {"name": "Antalya Arkeoloji Müzesi", "search": "Antalya Museum", "category": "Müze", "area": "Konyaaltı"},
    
    # Antik Kentler (Yakın Çevre)
    {"name": "Aspendos Antik Tiyatrosu", "search": "Aspendos Ancient Theatre", "category": "Tarihi", "area": "Serik"},
    {"name": "Perge Antik Kenti", "search": "Perge Ancient City", "category": "Tarihi", "area": "Aksu"},
    {"name": "Termessos Antik Kenti", "search": "Termessos Ancient City", "category": "Tarihi", "area": "Döşemealtı"},
    {"name": "Phaselis Antik Kenti", "search": "Phaselis Ancient City", "category": "Tarihi", "area": "Kemer"},
    {"name": "Olimpos Antik Kenti", "search": "Olympos Ancient City", "category": "Tarihi", "area": "Kumluca"},
    {"name": "Yanartaş (Chimaera)", "search": "Yanartas Chimaera", "category": "Doğa", "area": "Çıralı"},
    
    # Doğa & Şelaleler
    {"name": "Düden Şelalesi (Aşağı)", "search": "Lower Duden Waterfalls", "category": "Manzara", "area": "Lara"},
    {"name": "Düden Şelalesi (Yukarı)", "search": "Upper Duden Waterfalls", "category": "Park", "area": "Kepez"},
    {"name": "Kurşunlu Şelalesi", "search": "Kursunlu Waterfall Nature Park", "category": "Park", "area": "Aksu"},
    {"name": "Manavgat Şelalesi", "search": "Manavgat Waterfall", "category": "Manzara", "area": "Manavgat"},
    {"name": "Köprülü Kanyon", "search": "Koprulu Canyon National Park", "category": "Doğa", "area": "Manavgat"},
    {"name": "Konyaaltı Plajı", "search": "Konyaalti Beach", "category": "Manzara", "area": "Konyaaltı"},
    {"name": "Lara Plajı", "search": "Lara Beach", "category": "Manzara", "area": "Lara"},
    {"name": "Kaputaş Plajı", "search": "Kaputas Beach", "category": "Manzara", "area": "Kaş"},
    
    # Yeme-İçme
    {"name": "7 Mehmet", "search": "7 Mehmet Restaurant", "category": "Restoran", "area": "Konyaaltı"},
    {"name": "Seraser Fine Dining", "search": "Seraser Fine Dining Restaurant", "category": "Restoran", "area": "Kaleiçi"},
    {"name": "Vanilla", "search": "Vanilla Antalya", "category": "Restoran", "area": "Kaleiçi"},
    {"name": "Pio Gastro Bar & Bistro", "search": "Pio Gastro Bar & Bistro", "category": "Restoran", "area": "Kaleiçi"},
    {"name": "Börekçi Tevfik", "search": "Borekci Tevfik", "category": "Restoran", "area": "Merkez"},
    {"name": "Paçacı Şemsi", "search": "Pacaci Semsi", "category": "Restoran", "area": "Merkez"},
    {"name": "The Castle Cafe & Bistro", "search": "The Castle Cafe & Bistro Antalya", "category": "Cafe", "area": "Kaleiçi"},
    {"name": "Land of Legends", "search": "The Land of Legends Theme Park", "category": "Deneyim", "area": "Belek"},
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
        "Müze": f"{name}, Antalya'nın binlerce yıllık tarihine ışık tutan, dünyanın en önemli müzelerinden biri. {area} bölgesinde yer alıyor.",
        "Tarihi": f"{name}, antik çağlardan günümüze ulaşan büyüleyici bir yapı. {area} bölgesindeki bu mekan, tarih meraklıları için bir cennet.",
        "Manzara": f"{name}, Akdeniz'in mavisiyle Torosların yeşilini buluşturan eşsiz bir nokta. {area} bölgesindeki bu manzara nefes kesici.",
        "Deneyim": f"{name}, Antalya'da mutlaka yaşanması gereken özel bir an sunuyor. {area}'da bulunan bu aktivite tatilinize renk katacak.",
        "Park": f"{name}, şelaleleri ve doğasıyla serinlemek için mükemmel bir kaçış noktası. {area} bölgesindeki bu park, huzur verici.",
        "Doğa": f"{name}, Antalya'nın doğal güzelliklerini keşfetmek için harika bir durak. {area} bölgesinde yer alıyor.",
        "Restoran": f"{name}, Akdeniz mutfağının ve yerel lezzetlerin (piyaz, şiş köfte) tadına bakabileceğiniz kaliteli bir mekan. {area} bölgesinde.",
        "Cafe": f"{name}, tarihi atmosferde veya deniz manzarası eşliğinde kahve içmek için ideal. {area}'da yer alıyor.",
    }
    return descriptions.get(category, f"{name}, Antalya'nın incisi, keşfedilmeyi bekliyor.")

def main():
    print("🇹🇷 Antalya şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(ANTALYA_PLACES, 1):
        print(f"\n[{i}/{len(ANTALYA_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 36.8841)
        lng = geometry.get("lng", 30.7056)
        
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
            "tags": [place["area"].lower(), "antalya", "türkiye", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "high" if place["category"] == "Restoran" and "Fine Dining" in place["name"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Yazın" if place["category"] == "Manzara" else "İlkbahar",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Yazın çok sıcak olabilir, şapka ve güneş kremi şart.",
            "description_en": f"{place['name']} is a highlight of Antalya in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Antalya",
        "country": "Türkiye",
        "description": "Turkuaz sahilin başkenti. Tarihi Kaleiçi, büyüleyici falezler, antik tiyatrolar ve lüks tatil köyleriyle Akdeniz'in incisi.",
        "heroImage": "",
        "coordinates": {
            "lat": 36.8841,
            "lng": 30.7056
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Kaleiçi" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/antalya.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Antalya verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
