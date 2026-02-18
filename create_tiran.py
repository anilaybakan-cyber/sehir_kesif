#!/usr/bin/env python3
"""
Tiran (Tirana) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve tiran.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Tiran'ın temel mekanları
TIRAN_PLACES = [
    # Tarihi & Müzeler
    {"name": "İskender Bey Meydanı", "search": "Skanderbeg Square Tirana", "category": "Manzara", "area": "Merkez"},
    {"name": "Bunk'Art 1", "search": "Bunk'Art 1 Tirana", "category": "Müze", "area": "Dajti Yolu"},
    {"name": "Bunk'Art 2", "search": "Bunk'Art 2 Tirana", "category": "Müze", "area": "Merkez"},
    {"name": "Tiran Piramidi", "search": "Pyramid of Tirana", "category": "Tarihi", "area": "Merkez"},
    {"name": "Ethem Bey Camii", "search": "Et'hem Bej Mosque Tirana", "category": "Tarihi", "area": "Merkez"},
    {"name": "Ulusal Tarih Müzesi", "search": "National History Museum Tirana", "category": "Müze", "area": "Merkez"},
    {"name": "Yapraklar Evi (House of Leaves)", "search": "House of Leaves Museum Tirana", "category": "Müze", "area": "Merkez"},
    {"name": "Diriliş Katedrali", "search": "Resurrection of Christ Orthodox Cathedral Tirana", "category": "Tarihi", "area": "Merkez"},
    {"name": "Tanners' Bridge", "search": "Tanners' Bridge Tirana", "category": "Tarihi", "area": "Lanë Nehri"},
    {"name": "Kruja Kalesi", "search": "Kruje Castle", "category": "Tarihi", "area": "Kruja (Yakın)"},
    
    # Parklar & Manzara
    {"name": "Dajti Dağı (Teleferik)", "search": "Dajti Ekspres Cable Car", "category": "Manzara", "area": "Dajti"},
    {"name": "Tiran Büyük Parkı", "search": "Grand Park of Tirana", "category": "Park", "area": "Yapay Göl"},
    {"name": "Rinia Parkı", "search": "Rinia Park Tirana", "category": "Park", "area": "Merkez"},
    {"name": "Bulut (Reja)", "search": "Reja - The Cloud Pavillion", "category": "Sanat", "area": "Merkez"},
    
    # Deneyimler & Mahalleler
    {"name": "Blloku", "search": "Blloku Tirana", "category": "Deneyim", "area": "Blloku"},
    {"name": "Pazari i Ri (Yeni Pazar)", "search": "Pazari i Ri Tirana", "category": "Alışveriş", "area": "Pazar"},
    {"name": "Toptani Shopping Center", "search": "Toptani Shopping Center", "category": "Alışveriş", "area": "Merkez"},
    {"name": "Tiran Kalesi (Justinian)", "search": "Castle of Tirana", "category": "Deneyim", "area": "Pedonalja"},
    
    # Restoranlar
    {"name": "Mullixhiu", "search": "Mullixhiu Tirana", "category": "Restoran", "area": "Büyük Park"},
    {"name": "Oda", "search": "Oda Restaurant Tirana", "category": "Restoran", "area": "Pazar Yanı"},
    {"name": "Era Blloku", "search": "Era Blloku Tirana", "category": "Restoran", "area": "Blloku"},
    {"name": "Artigiano", "search": "Artigiano at Vila Tirana", "category": "Restoran", "area": "Papa Gjon Pali II"},
    {"name": "Padam Boutique Hotel & Restaurant", "search": "Padam Tirana", "category": "Restoran", "area": "Blloku"},
    {"name": "Salt", "search": "Salt Restaurant Tirana", "category": "Restoran", "area": "Blloku"},
    {"name": "Ballkoni Dajtit", "search": "Ballkoni Dajtit Restaurant", "category": "Restoran", "area": "Dajti Dağı"},
    {"name": "Ceren Ismet Shehu", "search": "Ceren Ismet Shehu Surrel", "category": "Restoran", "area": "Surrel"},
    
    # Kafeler & Barlar
    {"name": "Komiteti Kafe Müze", "search": "Komiteti Kafe Muzeum Tirana", "category": "Cafe", "area": "Merkez"},
    {"name": "Radio Bar", "search": "Radio Bar Tirana", "category": "Bar", "area": "Blloku"},
    {"name": "Colonial Cocktails Academy", "search": "Colonial Cocktails Academy Tirana", "category": "Bar", "area": "Blloku"},
    {"name": "Nouvelle Vague", "search": "Nouvelle Vague Tirana", "category": "Bar", "area": "Blloku"},
    {"name": "Mulliri i Vjeter", "search": "Mulliri i Vjeter Tirana", "category": "Cafe", "area": "Zincir"},
    {"name": "Mon Cheri", "search": "Mon Cheri Coffee Shop Tirana", "category": "Cafe", "area": "Zincir"},
    {"name": "Sophie Caffe", "search": "Sophie Caffe Tirana", "category": "Cafe", "area": "Zincir"},
    
    # Alışveriş
    {"name": "TEG (Tirana East Gate)", "search": "Tirana East Gate Mall", "category": "Alışveriş", "area": "Banliyö"},
    {"name": "Ring Center", "search": "Ring Center Tirana", "category": "Alışveriş", "area": "Zogu i Zi"},
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
        "Müze": f"{name}, Arnavutluk'un yakın tarihine ve komünist geçmişine ışık tutan etkileyici bir müze. {area} bölgesindeki bu mekan, ziyaretçilerine sarsıcı bir deneyim sunuyor.",
        "Tarihi": f"{name}, Tiran'ın en ikonik yapılarından biri. {area}'da yer alan bu tarihi mekan, şehrin dönüşümüne tanıklık ediyor.",
        "Manzara": f"{name}, Tiran'ı kuşbakışı izlemek için harika bir nokta. {area} bölgesindeki bu konum, temiz havası ve panoramik manzarasıyla ünlü.",
        "Deneyim": f"{name}, Tiran'ın modern yüzünü ve canlı atmosferini yansıtıyor. {area}'da bulunan bu nokta, renkli binaları ve enerjisiyle dikkat çekiyor.",
        "Park": f"{name}, şehrin ortasında yeşil bir kaçış noktası. {area} bölgesindeki bu park, yürüyüş, koşu ve dinlenmek için Tiranlıların favorisi.",
        "Restoran": f"{name}, Arnavut mutfağının en seçkin lezzetlerini sunan popüler bir restoran. {area} bölgesindeki bu mekan, \"farm-to-table\" konseptiyle öne çıkıyor.",
        "Cafe": f"{name}, Tiran'ın ünlü kahve kültürünü deneyimlemek için ideal. {area}'da yer alan bu kafe, şık dekorasyonu ve kaliteli kahveleriyle biliniyor.",
        "Bar": f"{name}, Tiran gece hayatının kalbinin attığı yer. {area}'daki bu mekan, yaratıcı kokteylleri ve canlı atmosferiyle keyifli bir akşam vaat ediyor.",
        "Alışveriş": f"{name}, alışveriş tutkunları için çeşitli seçenekler sunan bir merkez. {area}'da bulunan bu mekan, hem yerel hem de uluslararası markaları barındırıyor.",
    }
    return descriptions.get(category, f"{name}, Tiran'da keşfedilmeyi bekleyen renkli bir nokta.")

def main():
    print("🇦🇱 Tiran şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(TIRAN_PLACES, 1):
        print(f"\n[{i}/{len(TIRAN_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 41.3275)
        lng = geometry.get("lng", 19.8187)
        
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
            "tags": [place["area"].lower(), "tiran", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "low" if place["category"] in ["Park", "Manzara"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Müze", "Tarihi", "Manzara"] else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Blloku bölgesinde akşam yürüyüşü yapmayı unutmayın!",
            "description_en": f"{place['name']} is a highlight of Tirana in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Tiran",
        "country": "Arnavutluk",
        "description": "Renkli binaları, canlı kafe kültürü ve komünist geçmişin izlerini taşıyan bunkerleriyle hızla değişen dinamik bir başkent. Blloku'nun enerjisi ve Dajti Dağı'nın manzarası.",
        "heroImage": "",
        "coordinates": {
            "lat": 41.3275,
            "lng": 19.8187
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "İskender Bey" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/tiran.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Tiran verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
