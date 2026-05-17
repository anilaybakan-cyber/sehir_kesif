from dotenv import load_dotenv
load_dotenv()
import os
#!/usr/bin/env python3
"""
Fes (Fas) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve fes.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Fes'in temel mekanları - Az Gezen & Araştırma
FES_PLACES = [
    # Tarihi & Müzeler (Medina)
    {"name": "Fes el-Bali", "search": "Fes el-Bali Medina", "category": "Tarihi", "area": "Medina"},
    {"name": "Chouara Tabakhaneleri", "search": "Chouara Tannery Fes", "category": "Deneyim", "area": "Medina"},
    {"name": "Bou Inania Medresesi", "search": "Bou Inania Madrasa Fes", "category": "Tarihi", "area": "Medina"},
    {"name": "Al-Attarine Medresesi", "search": "Al-Attarine Madrasa", "category": "Tarihi", "area": "Medina"},
    {"name": "Bab Boujloud (Mavi Kapı)", "search": "Bab Boujloud Blue Gate", "category": "Tarihi", "area": "Medina Girişi"},
    {"name": "Al-Qarawiyyin Üniversitesi", "search": "University of al-Qarawiyyin", "category": "Tarihi", "area": "Medina"},
    {"name": "Zaouia Moulay Idriss II", "search": "Zaouia of Moulay Idriss II", "category": "Tarihi", "area": "Medina"},
    {"name": "Nejjarine Ahşap Sanatları Müzesi", "search": "Nejjarine Museum of Wooden Arts & Crafts", "category": "Müze", "area": "Medina"},
    {"name": "Dar Batha Müzesi", "search": "Dar Batha Museum", "category": "Müze", "area": "Medina"},
    {"name": "Marinid Mezarları", "search": "Marinid Tombs Fes", "category": "Manzara", "area": "Tepe"},
    {"name": "Borj Nord", "search": "Borj Nord Arms Museum", "category": "Müze", "area": "Tepe"},
    {"name": "Kraliyet Sarayı (Dar al-Makhzen)", "search": "Royal Palace of Fez", "category": "Tarihi", "area": "Fes el-Jdid"},
    {"name": "Mellah (Yahudi Mahallesi)", "search": "Mellah Fes", "category": "Tarihi", "area": "Fes el-Jdid"},
    {"name": "Ibn Danan Sinagogu", "search": "Ibn Danan Synagogue", "category": "Tarihi", "area": "Mellah"},
    
    # Parklar & Bahçeler
    {"name": "Jnan Sbil Bahçeleri", "search": "Jnan Sbil Gardens", "category": "Park", "area": "Fes el-Jdid"},
    
    # Deneyimler & Alışveriş
    {"name": "Seffarine Meydanı", "search": "Place Seffarine Fes", "category": "Alışveriş", "area": "Medina"},
    {"name": "Kına Çarşısı (Souk el-Henna)", "search": "Souk el Henna Fes", "category": "Alışveriş", "area": "Medina"},
    {"name": "Glaoui Sarayı", "search": "Palais Glaoui Fes", "category": "Tarihi", "area": "Medina"},
    {"name": "Rainbow Street Art", "search": "Rainbow Street Art Fes", "category": "Manzara", "area": "Medina"},
    {"name": "Art Naji (Seramik)", "search": "Art Naji Potterie Fes", "category": "Alışveriş", "area": "Medina Dışı"},
    
    # Restoranlar & Kafeler
    {"name": "Café Clock", "search": "Cafe Clock Fes", "category": "Cafe", "area": "Medina"},
    {"name": "The Ruined Garden", "search": "The Ruined Garden Fes", "category": "Restoran", "area": "Medina"},
    {"name": "Nur Restaurant", "search": "Nur Restaurant Fes", "category": "Restoran", "area": "Medina"},
    {"name": "Dar Roumana", "search": "Dar Roumana Restaurant", "category": "Restoran", "area": "Medina"},
    {"name": "Fez Café", "search": "Fez Cafe at Le Jardin des Biehn", "category": "Restoran", "area": "Medina"},
    {"name": "Nagham Cafe", "search": "Nagham Cafe Fes", "category": "Restoran", "area": "Bab Boujloud"},
    {"name": "Cinema Cafe", "search": "Cinema Cafe Fes", "category": "Cafe", "area": "Medina"},
    {"name": "Made in M", "search": "Made in M Fes", "category": "Cafe", "area": "Medina"},
    {"name": "Restaurant Dar Hatim", "search": "Restaurant Dar Hatim", "category": "Restoran", "area": "Medina"},
    {"name": "Palais De Fès Dar Tazi", "search": "Palais De Fes Dar Tazi", "category": "Restoran", "area": "Medina"},

    # Oteller (Riad Deneyimi için)
    {"name": "Riad Fes", "search": "Riad Fes - Relais & Châteaux", "category": "Deneyim", "area": "Medina"},
    {"name": "Karawan Riad", "search": "Karawan Riad Fes", "category": "Deneyim", "area": "Medina"},
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
        "Müze": f"{name}, Fes'in köklü tarihini ve sanatını keşfetmek için harika bir yer. {area} bölgesindeki bu müze, Fas kültürünün derinliklerine inmenizi sağlıyor.",
        "Tarihi": f"{name}, dünyanın en eski orta çağ şehirlerinden biri olan Fes'in en önemli yapılarından. {area} içinde yer alan bu mekan, İslam mimarisinin şaheserlerinden.",
        "Manzara": f"{name}, Fes'in o meşhur labirent sokaklarını ve teraslarını izlemek için en iyi noktalardan. {area} bölgesindeki bu konum, özellikle gün batımında büyüleyici.",
        "Deneyim": f"{name}, Fes'in mistik atmosferini hissetmek için mutlaka yaşanması gereken bir deneyim. {area}'da bulunan bu nokta, renkleri ve kokularıyla sizi başka bir zamana götürüyor.",
        "Park": f"{name}, Medina'nın karmaşasından kaçıp nefes almak için yeşil bir vaha. {area} bölgesindeki bu bahçe, huzurlu yürüyüşler için ideal.",
        "Restoran": f"{name}, Fas mutfağının en özel lezzetlerini (tajin, kuskus) tadabileceğiniz otantik bir mekan. {area} bölgesindeki bu restoran, geleneksel dekorasyonuyla da büyülüyor.",
        "Cafe": f"{name}, nane çayı içip soluklanmak için keyifli bir durak. {area}'da yer alan bu kafe, genellikle harika bir çatı manzarasına sahip.",
        "Alışveriş": f"{name}, deri ürünleri, seramikler ve baharatlar için renkli bir pazar. {area}'da bulunan bu mekan, pazarlık yapmanın ve yerel zanaatkarları izlemenin adresi.",
    }
    return descriptions.get(category, f"{name}, Fes'te keşfedilmeyi bekleyen büyüleyici bir nokta.")

def main():
    print("🇲🇦 Fes şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(FES_PLACES, 1):
        print(f"\n[{i}/{len(FES_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 34.0181)
        lng = geometry.get("lng", -5.0078)
        
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
            "tags": [place["area"].lower(), "fes", "fas", place["category"].lower()],
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
            "tips": "Medina'da kaybolmak gezinin bir parçasıdır, tadını çıkarın!",
            "description_en": f"{place['name']} is a highlight of Fes in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Fes",
        "country": "Fas",
        "description": "Dünyanın en büyük trafiğe kapalı şehir merkezi Medina'sı, deri tabakhaneleri ve labirent sokaklarıyla orta çağdan kalma bir zaman kapsülü. Fas'ın ruhani ve kültürel başkenti.",
        "heroImage": "",
        "coordinates": {
            "lat": 34.0181,
            "lng": -5.0078
        },
        "highlights": highlights
    }
    
    # Hero image - Chouara veya Bab Boujloud
    for h in highlights:
        if "Chouara" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/fes.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Fes verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
