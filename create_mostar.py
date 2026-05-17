from dotenv import load_dotenv
load_dotenv()
import os
#!/usr/bin/env python3
"""
Mostar şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve mostar.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Mostar'ın temel mekanları - Gezipgördüm & Araştırma
MOSTAR_PLACES = [
    # Tarihi & Stari Most
    {"name": "Mostar Köprüsü (Stari Most)", "search": "Stari Most Mostar", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Eski Çarşı (Kujundziluk)", "search": "Old Bridge Area of the Old City of Mostar", "category": "Alışveriş", "area": "Eski Şehir"},
    {"name": "Koski Mehmed Paşa Camii", "search": "Koski Mehmed Pasha Mosque", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Karagöz Bey Camii", "search": "Karadjoz Bey Mosque", "category": "Tarihi", "area": "Merkez"},
    {"name": "Eğri Köprü (Kriva Cuprija)", "search": "Crooked Bridge Mostar", "category": "Tarihi", "area": "Eski Şehir"},
    {"name": "Muslibegovic Evi", "search": "Muslibegovic House", "category": "Müze", "area": "Merkez"},
    {"name": "Biscelica Evi", "search": "Biscevic House", "category": "Müze", "area": "Merkez"},
    {"name": "Kajtaz Evi", "search": "Kajtaz House", "category": "Müze", "area": "Merkez"},
    
    # Manzara & Doğa
    {"name": "Barış Kulesi (Çan Kulesi)", "search": "Peace Bell Tower Mostar", "category": "Manzara", "area": "Merkez"},
    {"name": "Hum Tepesi (Haç)", "search": "Millennium Cross Mostar", "category": "Manzara", "area": "Hum Dağı"},
    {"name": "Partizan Mezarlığı", "search": "Partisan Memorial Cemetery Mostar", "category": "Tarihi", "area": "Batı Mostar"},
    {"name": "Fortica Park (Skywalk)", "search": "Fortica Park Mostar", "category": "Manzara", "area": "Fortica"},
    
    # Blagaj (Yakın Çevre)
    {"name": "Blagaj Tekkesi (Dervish House)", "search": "Dervish House Blagaj", "category": "Tarihi", "area": "Blagaj"},
    {"name": "Buna Nehri Kaynağı (Vrelo Bune)", "search": "Vrelo Bune", "category": "Manzara", "area": "Blagaj"},
    {"name": "Stjepan Grad (Blagaj Kalesi)", "search": "Fortress of Stjepan Grad", "category": "Tarihi", "area": "Blagaj"},
    
    # Yeme-İçme
    {"name": "Sadrvan", "search": "Saurvan Restaurant Mostar", "category": "Restoran", "area": "Eski Şehir"},
    {"name": "Hindin Han", "search": "National Restaurant Hindin Han", "category": "Restoran", "area": "Eski Şehir"},
    {"name": "Tima-Irma", "search": "Cevabdzinica Tima Irma", "category": "Restoran", "area": "Eski Şehir"},
    {"name": "Urban Grill", "search": "Urban Grill Mostar", "category": "Restoran", "area": "Eski Şehir"},
    {"name": "Restoran Lagero", "search": "Restoran Lagero", "category": "Restoran", "area": "Eski Şehir"},
    {"name": "Café de Alma", "search": "Cafe de Alma Mostar", "category": "Cafe", "area": "Eski Şehir"},
    {"name": "Black Dog Pub", "search": "Black Dog Pub Mostar", "category": "Bar", "area": "Eski Şehir"},
    {"name": "Restoran Vrelo", "search": "Restoran Vrelo Blagaj", "category": "Restoran", "area": "Blagaj"},
    
    # Alışveriş & Deneyim
    {"name": "Mostar Köprüsü Atlayışları", "search": "Mostar Bridge Diving", "category": "Deneyim", "area": "Stari Most"},
    {"name": "War Photo Exhibition", "search": "War Photo Exhibition Mostar", "category": "Müze", "area": "Eski Şehir"},
    {"name": "Museum of War and Genocide Victims", "search": "Museum of War and Genocide Victims", "category": "Müze", "area": "Merkez"},
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
        "Müze": f"{name}, Mostar'ın tarihini ve kültürel mirasını yansıtan önemli bir mekan. {area} bölgesindeki bu müze, ziyaretçilerine derin bir içgörü sunuyor.",
        "Tarihi": f"{name}, Mostar'ın simge yapılarından biri. {area} içinde yer alan bu tarihi mekan, Osmanlı mimarisinin zarafetini taşıyor.",
        "Manzara": f"{name}, Neretva Nehri'nin ve şehrin taş evlerinin muhteşem manzarasını sunuyor. {area} bölgesindeki bu nokta, fotoğrafçılar için ideal.",
        "Deneyim": f"{name}, Mostar'ın ruhunu hissetmek için harika bir fırsat. {area}'da bulunan bu aktivite, seyahatinize renk katacak.",
        "Park": f"{name}, doğayla iç içe olmak ve serinlemek için güzel bir alan. {area} bölgesindeki bu park, huzurlu bir mola yeri.",
        "Restoran": f"{name}, nehir kenarında keyifli bir yemek deneyimi sunuyor. {area} bölgesindeki bu restoran, hem manzarası hem de yerel lezzetleriyle ünlü.",
        "Cafe": f"{name}, Türk kahvesi geleneğini sürdüren otantik bir mekan. {area}'da yer alan bu kafe, dinlenmek için birebir.",
        "Alışveriş": f"{name}, el yapımı hediyelikler ve yerel ürünler bulabileceğiniz renkli bir çarşı. {area}'da bulunan bu mekan, eski zamanları anımsatıyor.",
    }
    return descriptions.get(category, f"{name}, Mostar'da görülmesi gereken etkileyici bir yer.")

def main():
    print("🇧🇦 Mostar şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(MOSTAR_PLACES, 1):
        print(f"\n[{i}/{len(MOSTAR_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 43.3438)
        lng = geometry.get("lng", 17.8078)
        
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
            "tags": [place["area"].lower(), "mostar", "bosna", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "low" if place["category"] in ["Restoran", "Cafe"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Müze", "Tarihi"] else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Köprüden atlayanları izlemek için nehir kenarına inin.",
            "description_en": f"{place['name']} is a highlight of Mostar in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Mostar",
        "country": "Bosna Hersek",
        "description": "Neretva Nehri'nin zümrüt suları üzerinde yükselen ikonik Stari Most köprüsüyle ünlü. Tarihi taş evleri, Osmanlı çarşısı ve Blagaj Tekkesi ile masalsı bir şehir.",
        "heroImage": "",
        "coordinates": {
            "lat": 43.3438,
            "lng": 17.8078
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Mostar Köprüsü" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/mostar.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Mostar verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
