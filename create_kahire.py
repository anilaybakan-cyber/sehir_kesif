#!/usr/bin/env python3
"""
Kahire (Cairo) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve kahire.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Kahire'nin temel mekanları - Az Gezen & Araştırma
KAHIRE_PLACES = [
    # Tarihi & Müzeler
    {"name": "Giza Piramitleri", "search": "Giza Necropolis", "category": "Tarihi", "area": "Giza"},
    {"name": "Büyük Giza Sfenksi", "search": "Great Sphinx of Giza", "category": "Tarihi", "area": "Giza"},
    {"name": "Mısır Müzesi (Tahrir)", "search": "The Egyptian Museum Cairo", "category": "Müze", "area": "Tahrir"},
    {"name": "Büyük Mısır Müzesi (GEM)", "search": "Grand Egyptian Museum", "category": "Müze", "area": "Giza"},
    {"name": "Mısır Medeniyeti Ulusal Müzesi", "search": "National Museum of Egyptian Civilization", "category": "Müze", "area": "Fustat"},
    {"name": "Kahire Kalesi (Selahaddin Eyyubi)", "search": "Cairo Citadel", "category": "Tarihi", "area": "Old Cairo"},
    {"name": "Mehmet Ali Paşa Camii", "search": "Mosque of Muhammad Ali", "category": "Tarihi", "area": "Citadel"},
    {"name": "Han el-Halili Çarşısı", "search": "Khan el-Khalili", "category": "Alışveriş", "area": "Islamic Cairo"},
    {"name": "El-Ezher Camii", "search": "Al-Azhar Mosque", "category": "Tarihi", "area": "Islamic Cairo"},
    {"name": "Sultan Hasan Camii", "search": "Mosque-Madrassa of Sultan Hassan", "category": "Tarihi", "area": "Old Cairo"},
    {"name": "İbn Tolun Camii", "search": "Mosque of Ibn Tulun", "category": "Tarihi", "area": "Old Cairo"},
    {"name": "Kahire Kulesi", "search": "Cairo Tower", "category": "Manzara", "area": "Gezira"},
    
    # Kıpti Kahire (Coptic Cairo)
    {"name": "Asılı Kilise (Hanging Church)", "search": "The Hanging Church Cairo", "category": "Tarihi", "area": "Coptic Cairo"},
    {"name": "Kıpti Müzesi", "search": "Coptic Museum Cairo", "category": "Müze", "area": "Coptic Cairo"},
    {"name": "Ben Ezra Sinagogu", "search": "Ben Ezra Synagogue", "category": "Tarihi", "area": "Coptic Cairo"},
    
    # Parklar & Nil
    {"name": "El-Ezher Parkı", "search": "Al-Azhar Park", "category": "Park", "area": "Islamic Cairo"},
    {"name": "Nil Gezisi (Felucca)", "search": "Nile River Felucca Cairo", "category": "Deneyim", "area": "Nil Nehri"},
    {"name": "Akvaryum Mağarası Bahçesi", "search": "Aquarium Grotto Garden", "category": "Park", "area": "Zamalek"},
    
    # Restoranlar & Kafeler
    {"name": "Naguib Mahfouz Cafe", "search": "Naguib Mahfouz Cafe", "category": "Cafe", "area": "Han el-Halili"},
    {"name": "Abou El Sid", "search": "Abou El Sid Zamalek", "category": "Restoran", "area": "Zamalek"},
    {"name": "Koshary Abou Tarek", "search": "Koshary Abou Tarek", "category": "Restoran", "area": "Downtown"},
    {"name": "Felfela", "search": "Felfela Restaurant", "category": "Restoran", "area": "Downtown"},
    {"name": "El Fishawy", "search": "El Fishawy Cafe", "category": "Cafe", "area": "Han el-Halili"},
    {"name": "Zööba", "search": "Zooba Zamalek", "category": "Restoran", "area": "Zamalek"},
    {"name": "Sequoia", "search": "Sequoia Cairo", "category": "Restoran", "area": "Zamalek"},
    {"name": "Crimson Bar & Grill", "search": "Crimson Bar & Grill Cairo", "category": "Restoran", "area": "Zamalek"},
    {"name": "Cairo Jazz Club", "search": "Cairo Jazz Club", "category": "Bar", "area": "Agouza"},
    
    # Alışveriş & Deneyim
    {"name": "Citystars Heliopolis", "search": "Citystars Heliopolis", "category": "Alışveriş", "area": "Heliopolis"},
    {"name": "Mall of Egypt", "search": "Mall of Egypt", "category": "Alışveriş", "area": "6th of October"},
    {"name": "Garbage City (Manastır)", "search": "Monastery of Saint Simon the Tanner", "category": "Deneyim", "area": "Mokattam"},
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
        "Müze": f"{name}, Antik Mısır'ın hazinelerini keşfetmek için dünyaca ünlü bir durak. {area} bölgesindeki bu müze, binlerce yıllık tarihe ev sahipliği yapıyor.",
        "Tarihi": f"{name}, Kahire'nin simge yapılarından biri. {area} bölgesinde yer alan bu anıt, İslam ve Mısır tarihinin en önemli örneklerinden.",
        "Manzara": f"{name}, şehri ve Nil Nehri'ni tepeden izlemek için harika bir nokta. {area} bölgesindeki bu konum, özellikle gün batımında büyüleyici.",
        "Deneyim": f"{name}, Kahire'nin kaosunu ve enerjisini hissetmek için mutlaka yaşanması gereken bir yer. {area}'da bulunan bu nokta, unutulmaz anılar vaat ediyor.",
        "Park": f"{name}, şehrin tozundan ve gürültüsünden kaçmak için yeşil bir vaha. {area} bölgesindeki bu park, muhteşem manzaralar sunuyor.",
        "Restoran": f"{name}, Mısır mutfağının (koshary, falafel) en iyi örneklerini tadabileceğiniz bir mekan. {area} bölgesindeki bu restoran, yerel lezzetleriyle ünlü.",
        "Cafe": f"{name}, nargile ve çay eşliğinde dinlenmek için tarihi bir mekan. {area}'da yer alan bu kafe, Nobel ödüllü yazarların uğrak noktasıydı.",
        "Alışveriş": f"{name}, baharatlar, lambalar ve hediyelik eşyalarla dolu büyüleyici bir çarşı. {area}'da bulunan bu mekan, pazarlık sanatını konuşturmak için ideal.",
        "Bar": f"{name}, Kahire gece hayatının nabzını tutan popüler bir mekan. {area}'daki bu nokta, canlı müzik ve eğlence sunuyor.",
    }
    return descriptions.get(category, f"{name}, Kahire'de keşfedilmeyi bekleyen gizemli bir yer.")

def main():
    print("🇪🇬 Kahire şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(KAHIRE_PLACES, 1):
        print(f"\n[{i}/{len(KAHIRE_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 30.0444)
        lng = geometry.get("lng", 31.2357)
        
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
            "tags": [place["area"].lower(), "kahire", "mısır", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "low" if place["category"] in ["Tarihi", "Manzara"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Müze", "Tarihi"] else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Piramitlerde satıcılara karşı dikkatli olun, 'hayır' demeyi öğrenin.",
            "description_en": f"{place['name']} is a highlight of Cairo in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Kahire",
        "country": "Mısır",
        "description": "Piramitlerin gölgesinde, bin minareli şehir. Antik tarih, İslami mimari, Nil Nehri'nin bereketi ve hiç uyumayan bir metropolün kaosu.",
        "heroImage": "",
        "coordinates": {
            "lat": 30.0444,
            "lng": 31.2357
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Piramit" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/kahire.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Kahire verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
