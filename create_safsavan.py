from dotenv import load_dotenv
load_dotenv()
import os
#!/usr/bin/env python3
"""
Şafşavan (Chefchaouen) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve safsavan.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Şafşavan'ın temel mekanları - Az Gezen & Araştırma
SAFSAVAN_PLACES = [
    # Mavi Şehir & Tarihi
    {"name": "Medina (Eski Şehir)", "search": "Medina Chefchaouen", "category": "Deneyim", "area": "Medina"},
    {"name": "Uta el-Hammam Meydanı", "search": "Plaza Uta el-Hammam", "category": "Manzara", "area": "Merkez"},
    {"name": "Kasbah Müzesi", "search": "Kasbah Museum Chefchaouen", "category": "Müze", "area": "Merkez"},
    {"name": "İspanyol Camii", "search": "Spanish Mosque Chefchaouen", "category": "Manzara", "area": "Tepe"},
    {"name": "Büyük Camii (Grand Mosque)", "search": "Grand Mosque Chefchaouen", "category": "Tarihi", "area": "Merkez"},
    {"name": "Bab el-Ain", "search": "Bab el-Ain Chefchaouen", "category": "Tarihi", "area": "Giriş Kapısı"},
    
    # Doğa & Manzara
    {"name": "Ras el-Maa Şelalesi", "search": "Ras el-Maa Waterfall", "category": "Park", "area": "Nehir Kenarı"},
    {"name": "Akchour Şelaleleri", "search": "Cascades d'Akchour", "category": "Park", "area": "Akchour (Yakın)"},
    {"name": "Tanrı'nın Köprüsü (God's Bridge)", "search": "God's Bridge Akchour", "category": "Manzara", "area": "Akchour (Yakın)"},
    {"name": "Jebel el-Kelaa", "search": "Jebel el-Kelaa", "category": "Manzara", "area": "Tepe"},
    
    # Fotoğraf Noktaları
    {"name": "Callejon El Asri", "search": "Callejon El Asri Chefchaouen", "category": "Manzara", "area": "Medina"},
    {"name": "Mavi Sokaklar", "search": "Blue Streets Chefchaouen", "category": "Deneyim", "area": "Medina"},
    {"name": "Tuilerie de Chefchaouen", "search": "Tuilerie de Chefchaouen", "category": "Manzara", "area": "Medina Dışı"},
    
    # Yeme-İçme
    {"name": "Restaurant Bab Ssour", "search": "Restaurant Bab Ssour Chefchaouen", "category": "Restoran", "area": "Medina"},
    {"name": "Casa Aladdin", "search": "Casa Aladdin Chefchaouen", "category": "Restoran", "area": "Meydan"},
    {"name": "Cafe Clock Chefchaouen", "search": "Cafe Clock Chefchaouen", "category": "Cafe", "area": "Medina"},
    {"name": "Restaurant Tissemlal", "search": "Restaurant Tissemlal Casa Hassan", "category": "Restoran", "area": "Medina"},
    {"name": "Sofia", "search": "Restaurant Sofia Chefchaouen", "category": "Restoran", "area": "Medina"},
    {"name": "Pizzeria Mandala", "search": "Pizzeria Mandala Chefchaouen", "category": "Restoran", "area": "Medina"},
    {"name": "Bilmos", "search": "Restaurant Bilmos Chefchaouen", "category": "Restoran", "area": "Medina"},
    {"name": "Lala Mesouda", "search": "Lala Mesouda Chefchaouen", "category": "Restoran", "area": "Medina"},
    
    # Alışveriş
    {"name": "Hatillo Artisan", "search": "Hatillo Artisan Chefchaouen", "category": "Alışveriş", "area": "Medina"},
    {"name": "La Botica de la Abuela Aladdin", "search": "La Botica de la Abuela Aladdin", "category": "Alışveriş", "area": "Medina"},
    {"name": "Dar El Moualim", "search": "Dar El Moualim Chefchaouen", "category": "Alışveriş", "area": "Medina"},
    
    # Konaklama (Riad)
    {"name": "Lina Ryad & Spa", "search": "Lina Ryad & Spa Chefchaouen", "category": "Deneyim", "area": "Medina"},
    {"name": "Dar Echchaouen", "search": "Dar Echchaouen Maison d'Hotes", "category": "Deneyim", "area": "Tepe"},
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
        "Müze": f"{name}, Şafşavan'ın tarihini ve yerel kültürünü sergileyen önemli bir yapı. {area} bölgesindeki bu müze, şehrin geçmişine ışık tutuyor.",
        "Tarihi": f"{name}, Mavi Şehir'in simge yapılarından biri. {area} içinde yer alan bu tarihi mekan, eşsiz mimarisiyle dikkat çekiyor.",
        "Manzara": f"{name}, Şafşavan'ın o büyülü mavi manzarasını izlemek için mükemmel bir nokta. {area} bölgesindeki bu konum, özellikle gün batımında nefes kesici.",
        "Deneyim": f"{name}, maviye boyanmış sokakların büyüsünü hissetmek için harika bir yer. {area}'da bulunan bu nokta, fotoğraf tutkunları için bir cennet.",
        "Park": f"{name}, doğanın içinde serinlemek ve dinlenmek için ideal bir kaçış noktası. {area} bölgesindeki bu alan, şelaleleri ve yeşillikleriyle ünlü.",
        "Restoran": f"{name}, Fas mutfağının en lezzetli örneklerini sunan samimi bir mekan. {area} bölgesindeki bu restoran, hem manzarası hem de yemekleriyle öne çıkıyor.",
        "Cafe": f"{name}, nane çayı eşliğinde dinlenmek için keyifli bir durak. {area}'da yer alan bu kafe, şehrin sakin ritmini yakalamak için ideal.",
        "Alışveriş": f"{name}, el dokuması kilimler, sabunlar ve yerel el sanatları için harika bir dükkan. {area}'da bulunan bu mekan, otantik hediyelikler sunuyor.",
    }
    return descriptions.get(category, f"{name}, Şafşavan'da keşfedilmeyi bekleyen masalsı bir yer.")

def main():
    print("🇲🇦 Şafşavan şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(SAFSAVAN_PLACES, 1):
        print(f"\n[{i}/{len(SAFSAVAN_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 35.1688)
        lng = geometry.get("lng", -5.2684)
        
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
            "tags": [place["area"].lower(), "şafşavan", "mavi şehir", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "low" if place["category"] in ["Tarihi", "Manzara"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] == "Manzara" else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Mavi sokaklarda fotoğraf çekerken yerel halkın mahremiyetine saygı gösterin.",
            "description_en": f"{place['name']} is a highlight of Chefchaouen in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Şafşavan",
        "country": "Fas",
        "description": "Rif Dağları'nın eteklerinde, rüya gibi maviye boyanmış sokaklarıyla ünlü 'Mavi İnci'. Fotoğrafçılar için bir cennet, sakin ve huzurlu bir kaçış.",
        "heroImage": "",
        "coordinates": {
            "lat": 35.1688,
            "lng": -5.2684
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Medina" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/safsavan.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Şafşavan verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
