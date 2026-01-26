#!/usr/bin/env python3
"""
Kotor şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve kotor.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Kotor'un temel mekanları
KOTOR_PLACES = [
    # Tarihi & Müzeler
    {"name": "Kotor Kalesi (San Giovanni)", "search": "Kotor Fortress Saint John", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Aziz Tryphon Katedrali", "search": "Saint Tryphon Cathedral Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Denizcilik Müzesi", "search": "Maritime Museum Kotor", "category": "Müze", "area": "Eski Şehir"},
    {"name": "Kotor Kedileri Müzesi", "search": "Cats Museum Kotor", "category": "Müze", "area": "Eski Şehir"},
    {"name": "Saat Kulesi", "search": "Clock Tower Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Aziz Nikola Kilisesi", "search": "Saint Nicholas Church Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Aziz Luke Kilisesi", "search": "Saint Luke Church Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Pima Sarayı", "search": "Pima Palace Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Drago Sarayı", "search": "Drago Palace Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Grgurina Sarayı", "search": "Grgurina Palace Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Kampana Kulesi", "search": "Kampana Tower Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Gurdic Kapısı", "search": "Gurdic Gate Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Deniz Kapısı (Ana Kapı)", "search": "Sea Gate Kotor", "category": "Tarihi", "area": "Eski Şehir"},
    
    # Yakın Çevre & Manzara
    {"name": "Perast", "search": "Perast Montenegro", "category": "Deneyim", "area": "Kotor Körfezi"},
    {"name": "Kayaların Leydisi (Our Lady of the Rocks)", "search": "Our Lady of the Rocks Perast", "category": "Tarihi", "area": "Perast"},
    {"name": "Lovcen Milli Parkı", "search": "Lovcen National Park", "category": "Park", "area": "Lovcen"},
    {"name": "Blue Grotto (Mavi Mağara)", "search": "Blue Grotto Montenegro", "category": "Deneyim", "area": "Lustica"},
    {"name": "Kotor Serpentine Yolu", "search": "Kotor Serpentine Road", "category": "Manzara", "area": "Lovcen Yolu"},
    {"name": "Şehir Surları", "search": "Kotor City Walls", "category": "Manzara", "area": "Eski Şehir"},
    
    # Restoranlar
    {"name": "Galion", "search": "Galion Restaurant Kotor", "category": "Restoran", "area": "Körfez"},
    {"name": "Konoba Scala Santa", "search": "Konoba Scala Santa Kotor", "category": "Restoran", "area": "Eski Şehir"},
    {"name": "Konoba Trpeza", "search": "Konoba Trpeza Kotor", "category": "Restoran", "area": "Eski Şehir"},
    {"name": "Bastion", "search": "Bastion Restaurant Kotor", "category": "Restoran", "area": "Eski Şehir"},
    {"name": "Cesarica", "search": "Cesarica Restaurant Kotor", "category": "Restoran", "area": "Eski Şehir"},
    {"name": "Konoba Portun", "search": "Konoba Portun Dobrota", "category": "Restoran", "area": "Dobrota"},
    {"name": "Stari Mlini", "search": "Stari Mlini Restaurant Ljuta", "category": "Restoran", "area": "Ljuta"},
    {"name": "Verige 65", "search": "Verige 65 Restaurant", "category": "Restoran", "area": "Perast Yakını"},
    {"name": "Ladovina Kitchen & Wine Bar", "search": "Ladovina Kitchen & Wine Bar Kotor", "category": "Restoran", "area": "Kotor"},
    {"name": "Tanjga Family Restaurant", "search": "Tanjga Family Restaurant Kotor", "category": "Restoran", "area": "Kotor"},
    
    # Kafeler & Barlar
    {"name": "O'Clock Coffee", "search": "O'Clock Coffee Kotor", "category": "Cafe", "area": "Eski Şehir"},
    {"name": "Forza Cafe", "search": "Forza Cafe Kotor", "category": "Cafe", "area": "Eski Şehir"},
    {"name": "Old Town Pub", "search": "Old Town Pub Kotor", "category": "Bar", "area": "Eski Şehir"},
    {"name": "Letrika Caffe Bar", "search": "Letrika Caffe Bar Kotor", "category": "Bar", "area": "Eski Şehir"},
    {"name": "Bokun Wine Bar", "search": "Bokun Wine Bar Kotor", "category": "Bar", "area": "Eski Şehir"},
    {"name": "Jazz Club Evergreen", "search": "Jazz Club Evergreen Kotor", "category": "Bar", "area": "Eski Şehir"},
    {"name": "Pirate Bar", "search": "Pirate Bar Perast", "category": "Bar", "area": "Perast"},
    
    # Alışveriş & Pazar
    {"name": "Kotor Semt Pazarı", "search": "Kotor Farmers Market", "category": "Alışveriş", "area": "Surlar Dışı"},
    {"name": "Kamelija AVM", "search": "Shopping Centre Kamelija Kotor", "category": "Alışveriş", "area": "Dobrota"},
    {"name": "Cats of Kotor Shop", "search": "Cats of Kotor Souvenir Shop", "category": "Alışveriş", "area": "Eski Şehir"},
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
        "Müze": f"{name}, Kotor'un denizcilik geçmişini ve zengin kültürünü keşfetmek için harika bir yer. {area} bölgesindeki bu müze, ziyaretçilerine nostaljik bir yolculuk sunuyor.",
        "Tarihi": f"{name}, UNESCO Dünya Mirası Kotor'un en önemli tarihi yapılarından biri. {area}'da yer alan bu mekan, Venedik mimarisinin izlerini taşıyor.",
        "Manzara": f"{name}, Kotor Körfezi'nin nefes kesen manzarasını izlemek için en iyi noktalardan. {area} bölgesindeki bu konum, özellikle fotoğraf tutkunları için ideal.",
        "Deneyim": f"{name}, Kotor'un büyüsünü hissetmek için mutlaka yaşanması gereken bir deneyim. {area}'da bulunan bu nokta, körfezin sakinliğini ve güzelliğini sunuyor.",
        "Park": f"{name}, Karadağ'ın vahşi doğasını keşfetmek için muhteşem bir milli park. {area} bölgesindeki bu alan, eşsiz manzaralar ve yürüyüş rotaları sunuyor.",
        "Restoran": f"{name}, Adriyatik mutfağının en taze deniz ürünlerini tadabileceğiniz şık bir mekan. {area} bölgesindeki bu restoran, deniz manzarası eşliğinde unutulmaz bir yemek vaat ediyor.",
        "Cafe": f"{name}, tarihi sokaklarda kahve molası vermek için keyifli bir durak. {area}'da yer alan bu kafe, Kotor'un sakin ritmini yakalamak için ideal.",
        "Bar": f"{name}, Kotor gecelerinin tadını çıkarmak için popüler bir mekan. {area}'daki bu bar, taş binaların arasında keyifli bir atmosfer sunuyor.",
        "Alışveriş": f"{name}, yerel ürünler ve hediyelik eşyalar için renkli bir pazar. {area}'da bulunan bu mekan, taze meyve-sebze ve el yapımı ürünlerle dolu.",
    }
    return descriptions.get(category, f"{name}, Kotor'da keşfedilmeyi bekleyen büyüleyici bir nokta.")

def main():
    print("🇲🇪 Kotor şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(KOTOR_PLACES, 1):
        print(f"\n[{i}/{len(KOTOR_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 42.4247)
        lng = geometry.get("lng", 18.7712)
        
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
            "tags": [place["area"].lower(), "kotor", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "low" if place["category"] in ["Manzara", "Tarihi"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Müze", "Tarihi", "Manzara"] else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Kalede gün batımı manzarasını kaçırmayın, ama merdivenlere hazırlıklı olun!",
            "description_en": f"{place['name']} is a highlight of Kotor in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Kotor",
        "country": "Karadağ",
        "description": "Adriyatik'in fiyord benzeri körfezinde gizlenmiş UNESCO Dünya Mirası. Venedik mimarisi, dar sokaklar, kediler ve muhteşem dağ manzaraları.",
        "heroImage": "",
        "coordinates": {
            "lat": 42.4247,
            "lng": 18.7712
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Kotor Kalesi" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/kotor.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Kotor verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
