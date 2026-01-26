#!/usr/bin/env python3
"""
Saraybosna (Sarajevo) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve saraybosna.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyCMEuzJpyZtG-LPG-8DFiNrSn2-KfKrQp0"

# Saraybosna'nın temel mekanları - Gezipgördüm & Araştırma
SARAYBOSNA_PLACES = [
    # Tarihi & Başçarşı
    {"name": "Başçarşı", "search": "Bascarsija Sarajevo", "category": "Deneyim", "area": "Merkez"},
    {"name": "Sebil (Sebilj Brunnen)", "search": "Sebilj Fountain", "category": "Tarihi", "area": "Başçarşı"},
    {"name": "Gazi Hüsrev Bey Camii", "search": "Gazi Husrev-beg Mosque", "category": "Tarihi", "area": "Başçarşı"},
    {"name": "Latin Köprüsü", "search": "Latin Bridge Sarajevo", "category": "Tarihi", "area": "Merkez"},
    {"name": "Saraybosna Katedrali", "search": "Sacred Heart Cathedral Sarajevo", "category": "Tarihi", "area": "Ferhadiye"},
    {"name": "Vijećnica (Belediye Binası)", "search": "Sarajevo City Hall", "category": "Tarihi", "area": "Merkez"},
    {"name": "Sarı Tabya (Yellow Bastion)", "search": "Yellow Bastion Sarajevo", "category": "Manzara", "area": "Vratnik"},
    
    # Savaş Tarihi & Müzeler
    {"name": "Umut Tüneli (Tunnel of Hope)", "search": "Sarajevo War Tunnel", "category": "Müze", "area": "Havalimanı Yanı"},
    {"name": "Galerija 11/07/95", "search": "Gallery 11/07/95", "category": "Müze", "area": "Merkez"},
    {"name": "Saraybosna Müzesi 1878-1918", "search": "Museum of Sarajevo 1878-1918", "category": "Müze", "area": "Latin Köprüsü"},
    {"name": "Svrzo'nun Evi", "search": "Svrzo's House", "category": "Müze", "area": "Merkez"},
    
    # Doğa & Parklar
    {"name": "Vrelo Bosne", "search": "Vrelo Bosne", "category": "Park", "area": "Ilidža"},
    {"name": "Trebević Dağı (Teleferik)", "search": "Sarajevo Cable Car", "category": "Manzara", "area": "Trebević"},
    {"name": "Sunnyland Sarajevo", "search": "Sunnyland Sarajevo", "category": "Deneyim", "area": "Trebević"},
    
    # Yeme-İçme (Börek & Cevapi)
    {"name": "Cevabdzinica Zeljo", "search": "Cevabdzinica Zeljo", "category": "Restoran", "area": "Başçarşı"},
    {"name": "Cevabdzinica Petica Ferhatovic", "search": "Cevabdzinica Petica Ferhatovic", "category": "Restoran", "area": "Başçarşı"},
    {"name": "Buregdzinica Sac", "search": "Buregdzinica Sac", "category": "Restoran", "area": "Başçarşı"},
    {"name": "Buregdzinica Bosna", "search": "Buregdzinica Bosna", "category": "Restoran", "area": "Başçarşı"},
    {"name": "Inat Kuca", "search": "Inat Kuca", "category": "Restoran", "area": "Miljacka"},
    {"name": "Dveri", "search": "Dveri Sarajevo", "category": "Restoran", "area": "Başçarşı"},
    {"name": "Cajdzinica Dzirlo", "search": "Teahouse Dzirlo", "category": "Cafe", "area": "Kovaci"},
    {"name": "Ministry of Cejh", "search": "Ministry of Cejh", "category": "Cafe", "area": "Kovaci"},
    {"name": "Zlatna Ribica", "search": "Zlatna Ribica", "category": "Bar", "area": "Merkez"},
    
    # Alışveriş
    {"name": "Bakırcılar Çarşısı (Kazandziluk)", "search": "Kazandziluk Street", "category": "Alışveriş", "area": "Başçarşı"},
    {"name": "Bezistan (Kapalı Çarşı)", "search": "Gazi Husrev-beg's Bezistan", "category": "Alışveriş", "area": "Başçarşı"},
    {"name": "Sarajevo City Center", "search": "Sarajevo City Center", "category": "Alışveriş", "area": "Marijin Dvor"},
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
        "Müze": f"{name}, Saraybosna'nın hüzünlü ve etkileyici tarihine tanıklık eden önemli bir durak. {area} bölgesindeki bu müze, ziyaretçilerine unutulmaz bir deneyim sunuyor.",
        "Tarihi": f"{name}, şehrin Doğu ve Batı sentezini yansıtan simge yapılardan biri. {area} içinde yer alan bu mekan, Osmanlı ve Avusturya-Macaristan izlerini taşıyor.",
        "Manzara": f"{name}, Saraybosna'nın panoramik manzarasını izlemek için en güzel noktalardan. {area} bölgesindeki bu konum, özellikle gün batımında harika.",
        "Deneyim": f"{name}, Başçarşı'nın ruhunu ve canlılığını hissetmek için mutlaka uğranması gereken bir yer. {area}'da bulunan bu nokta, şehrin kalbinin attığı yer.",
        "Park": f"{name}, doğanın içinde huzur bulmak ve nehir kenarında yürümek için mükemmel bir kaçış. {area} bölgesindeki bu park, yerel halkın favorisi.",
        "Restoran": f"{name}, Boşnak mutfağının efsanevi lezzetlerini (Cevapi, Boşnak Böreği) tadabileceğiniz otantik bir mekan. {area} bölgesindeki bu restoran çok popüler.",
        "Cafe": f"{name}, Türk kahvesi veya bitki çayı eşliğinde keyifli bir mola. {area}'da yer alan bu kafe, samimi atmosferiyle biliniyor.",
        "Alışveriş": f"{name}, el işi bakır ürünler ve hediyelik eşyalar için tarihi bir çarşı. {area}'da bulunan bu mekan, zanaatkarları izleme fırsatı sunuyor.",
    }
    return descriptions.get(category, f"{name}, Saraybosna'da keşfedilmeyi bekleyen özel bir yer.")

def main():
    print("🇧🇦 Saraybosna şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(SARAYBOSNA_PLACES, 1):
        print(f"\n[{i}/{len(SARAYBOSNA_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 43.8563)
        lng = geometry.get("lng", 18.4131)
        
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
            "tags": [place["area"].lower(), "saraybosna", "bosna", place["category"].lower()],
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
            "tips": "Boşnak kahvesini şekersiz içmeyi deneyin, yanında lokum gelir.",
            "description_en": f"{place['name']} is a highlight of Sarajevo in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Saraybosna",
        "country": "Bosna Hersek",
        "description": "Doğu'nun Batı ile buluştuğu yer. Osmanlı mirası Başçarşı, Avusturya mimarisi, hüzünlü savaş tarihi ve misafirperver halkıyla Balkanların kalbi.",
        "heroImage": "",
        "coordinates": {
            "lat": 43.8563,
            "lng": 18.4131
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Sebil" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/saraybosna.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Saraybosna verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
