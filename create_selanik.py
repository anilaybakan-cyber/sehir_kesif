#!/usr/bin/env python3
"""
Selanik (Thessaloniki) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve selanik.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Selanik'in temel mekanları - araştırmadan derlendi
SELANIK_PLACES = [
    # Tarihi & Müzeler
    {"name": "Atatürk Evi Müzesi", "search": "Ataturk Museum Thessaloniki", "category": "Müze", "area": "Apostolou Pavlou"},
    {"name": "Beyaz Kule", "search": "White Tower of Thessaloniki", "category": "Tarihi", "area": "Sahil"},
    {"name": "Arkeoloji Müzesi", "search": "Archaeological Museum of Thessaloniki", "category": "Müze", "area": "Merkez"},
    {"name": "Bizans Kültürü Müzesi", "search": "Museum of Byzantine Culture Thessaloniki", "category": "Müze", "area": "Merkez"},
    {"name": "Rotonda", "search": "Rotunda of Galerius Thessaloniki", "category": "Tarihi", "area": "Kamara"},
    {"name": "Galerius Kemeri", "search": "Arch of Galerius Thessaloniki", "category": "Tarihi", "area": "Kamara"},
    {"name": "Ayasofya Kilisesi", "search": "Hagia Sophia Thessaloniki", "category": "Tarihi", "area": "Merkez"},
    {"name": "Agios Dimitrios Kilisesi", "search": "Church of Saint Demetrius Thessaloniki", "category": "Tarihi", "area": "Merkez"},
    {"name": "Yedi Kule (Heptapyrgion)", "search": "Heptapyrgion of Thessaloniki", "category": "Tarihi", "area": "Ano Poli"},
    {"name": "Trigoniou Kulesi", "search": "Trigoniou Tower Thessaloniki", "category": "Manzara", "area": "Ano Poli"},
    {"name": "Roman Forum", "search": "Roman Forum of Thessaloniki", "category": "Tarihi", "area": "Merkez"},
    {"name": "Yahudi Müzesi", "search": "Jewish Museum of Thessaloniki", "category": "Müze", "area": "Merkez"},
    {"name": "Makedonya Mücadele Müzesi", "search": "Museum of the Macedonian Struggle", "category": "Müze", "area": "Sahil"},
    
    # Meydanlar & Caddeler
    {"name": "Aristoteles Meydanı", "search": "Aristotelous Square Thessaloniki", "category": "Manzara", "area": "Merkez"},
    {"name": "Nikis Caddesi", "search": "Leoforos Nikis Thessaloniki", "category": "Manzara", "area": "Sahil"},
    {"name": "Tsimiski Caddesi", "search": "Tsimiski Street Thessaloniki", "category": "Alışveriş", "area": "Merkez"},
    {"name": "Egnatia Caddesi", "search": "Egnatia Street Thessaloniki", "category": "Alışveriş", "area": "Merkez"},
    
    # Mahalleler & Deneyimler
    {"name": "Ladadika", "search": "Ladadika District Thessaloniki", "category": "Deneyim", "area": "Ladadika"},
    {"name": "Ano Poli", "search": "Ano Poli Thessaloniki", "category": "Deneyim", "area": "Ano Poli"},
    {"name": "Kapani Çarşısı", "search": "Kapani Market Thessaloniki", "category": "Alışveriş", "area": "Merkez"},
    {"name": "Modiano Çarşısı", "search": "Modiano Market Thessaloniki", "category": "Deneyim", "area": "Merkez"},
    {"name": "Yeni Sahil Yolu", "search": "Nea Paralia Thessaloniki", "category": "Park", "area": "Sahil"},
    {"name": "Şemsiyeler", "search": "The Umbrellas by Zongolopoulos Thessaloniki", "category": "Manzara", "area": "Sahil"},
    
    # Restoranlar
    {"name": "Full tou Meze", "search": "Full tou Meze Thessaloniki", "category": "Restoran", "area": "Ladadika"},
    {"name": "Ouzou Melathron", "search": "Ouzou Melathron Thessaloniki", "category": "Restoran", "area": "Ladadika"},
    {"name": "Sebriko", "search": "Sebriko Thessaloniki", "category": "Restoran", "area": "Batı Duvarları"},
    {"name": "Mourga", "search": "Mourga Thessaloniki", "category": "Restoran", "area": "Merkez"},
    {"name": "Extravaganza", "search": "Extravaganza Thessaloniki", "category": "Restoran", "area": "Merkez"},
    {"name": "The Rouga", "search": "The Rouga Thessaloniki", "category": "Restoran", "area": "Merkez"},
    {"name": "Dia Xeiros & Saliaras", "search": "Dia Xeiros & Saliaras Thessaloniki", "category": "Restoran", "area": "Merkez"},
    {"name": "Ergon Agora", "search": "Ergon Agora Thessaloniki", "category": "Restoran", "area": "Merkez"},
    {"name": "Kitchen Bar", "search": "Kitchen Bar Thessaloniki", "category": "Restoran", "area": "Liman"},
    {"name": "Palati", "search": "Palati Restaurant Thessaloniki", "category": "Restoran", "area": "Ladadika"},
    
    # Kafeler & Tatlıcılar
    {"name": "Terkenlis", "search": "Terkenlis Aristotelous Thessaloniki", "category": "Cafe", "area": "Merkez"},
    {"name": "Ble", "search": "Ble Bakery Thessaloniki", "category": "Cafe", "area": "Merkez"},
    {"name": "Elenidis", "search": "Trigona Elenidis Thessaloniki", "category": "Cafe", "area": "Sahil"},
    {"name": "Ypsilon", "search": "Ypsilon Thessaloniki", "category": "Cafe", "area": "Valaoritou"},
    {"name": "Tabya", "search": "Tabya Thessaloniki", "category": "Cafe", "area": "Merkez"},
    {"name": "Skyline Bar", "search": "Skyline Bar Thessaloniki OTE Tower", "category": "Cafe", "area": "Fuaye"},
    {"name": "Little Big House", "search": "Little Big House Cafe Thessaloniki", "category": "Cafe", "area": "Ano Poli"},
    
    # Barlar & Gece Hayatı
    {"name": "Vogatsikou 3", "search": "Vogatsikou 3 Thessaloniki", "category": "Bar", "area": "Sahil"},
    {"name": "Gorilla", "search": "Gorilla Bar Thessaloniki", "category": "Bar", "area": "Ladadika"},
    {"name": "The Hoppy Pub", "search": "The Hoppy Pub Thessaloniki", "category": "Bar", "area": "Beyaz Kule"},
    {"name": "Pulp Bar", "search": "Pulp Bar Thessaloniki", "category": "Bar", "area": "Merkez"},
    {"name": "La Doze", "search": "La Doze Bar Thessaloniki", "category": "Bar", "area": "Valaoritou"},
    
    # Alışveriş
    {"name": "One Salonica Outlet", "search": "One Salonica Outlet Mall", "category": "Alışveriş", "area": "Batı"},
    {"name": "Mediterranean Cosmos", "search": "Mediterranean Cosmos Thessaloniki", "category": "Alışveriş", "area": "Havalimanı Yolu"},
    {"name": "Attica", "search": "Attica Department Store Thessaloniki", "category": "Alışveriş", "area": "Tsimiski"},
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
        "Müze": f"{name}, Selanik'in zengin tarihine ışık tutan önemli bir kültür durağı. {area} bölgesinde yer alan bu müze, şehrin çok katmanlı geçmişini keşfetmek isteyenler için ideal.",
        "Tarihi": f"{name}, Selanik'in en önemli tarihi simgelerinden biri. {area}'da bulunan bu yapı, Roma, Bizans ve Osmanlı dönemlerinden izler taşıyor.",
        "Manzara": f"{name}, şehri ve körfezi izlemek için harika bir nokta. {area} bölgesindeki bu konum, özellikle gün batımında eşsiz manzaralar sunuyor.",
        "Deneyim": f"{name}, Selanik'in canlı atmosferini hissetmek için mükemmel bir yer. {area}'da bulunan bu nokta, yerel yaşamın ritmini yakalamak isteyenler için.",
        "Park": f"{name}, şehir içinde nefes almak ve dinlenmek için yeşil bir vaha. {area} bölgesindeki bu park, yürüyüş ve gevşeme için tercih ediliyor.",
        "Restoran": f"{name}, Selanik'in ünlü gastronomi sahnesinin başarılı örneklerinden. {area} bölgesindeki bu mekan, taze deniz ürünleri ve meze çeşitleriyle öne çıkıyor.",
        "Cafe": f"{name}, kahve molası ve tatlı kaçamağı için popüler bir durak. {area}'da yer alan bu kafe, şehrin ünlü frappe kültürünü deneyimlemek için ideal.",
        "Bar": f"{name}, Selanik gece hayatının nabzını tutan mekanlardan biri. {area}'daki bu bar, kokteylleri ve müziğiyle keyifli bir akşam vaat ediyor.",
        "Alışveriş": f"{name}, alışveriş tutkunları için çeşitli seçenekler sunuyor. {area}'da bulunan bu mekan, hem yerel markaları hem de dünyaca ünlü mağazaları barındırıyor.",
    }
    return descriptions.get(category, f"{name}, Selanik'te keşfedilmeyi bekleyen özel bir nokta.")

def main():
    print("🏛️ Selanik şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(SELANIK_PLACES, 1):
        print(f"\n[{i}/{len(SELANIK_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 40.6401)
        lng = geometry.get("lng", 22.9444)
        
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
            "tags": [place["area"].lower(), "selanik", place["category"].lower()],
            "distanceFromCenter": 0, # Şehir merkezine göre hesaplanabilir ama şimdilik 0
            "lat": lat,
            "lng": lng,
            "price": "low" if place["category"] in ["Tarihi", "Manzara"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Müze", "Tarihi"] else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Selanik'in keyfini çıkarın! 'Frappe' içmeyi unutmayın.",
            "description_en": f"{place['name']} is a must-visit spot in Thessaloniki's {place['area']} district."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Selanik",
        "country": "Yunanistan",
        "description": "Atatürk'ün doğum yeri, tarih ve kültür dolu liman şehri. Beyaz Kule, Ladadika'nın canlı tavernoları ve zengin mutfağıyla Ege'nin incisi.",
        "heroImage": "",  # İlk fotoğraftan alınacak
        "coordinates": {
            "lat": 40.6401,
            "lng": 22.9444
        },
        "highlights": highlights
    }
    
    # Hero image'ı Beyaz Kule veya Aristoteles Meydanı'ndan al
    for h in highlights:
        if h["name"] == "Beyaz Kule" and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
    
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/selanik.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Selanik verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
