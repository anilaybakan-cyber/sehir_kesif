#!/usr/bin/env python3
"""
Stockholm şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve stockholm.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Stockholm'ün temel mekanları - Oitheblog & Araştırma
STOCKHOLM_PLACES = [
    # Tarihi & Müzeler
    {"name": "Gamla Stan", "search": "Gamla Stan Stockholm", "category": "Deneyim", "area": "Gamla Stan"},
    {"name": "Vasa Müzesi", "search": "Vasa Museum", "category": "Müze", "area": "Djurgården"},
    {"name": "Skansen Açık Hava Müzesi", "search": "Skansen", "category": "Müze", "area": "Djurgården"},
    {"name": "Stockholm Sarayı", "search": "The Royal Palace Stockholm", "category": "Tarihi", "area": "Gamla Stan"},
    {"name": "Stortorget", "search": "Stortorget Stockholm", "category": "Manzara", "area": "Gamla Stan"},
    {"name": "Stockholm Belediye Binası", "search": "Stockholm City Hall", "category": "Tarihi", "area": "Kungsholmen"},
    {"name": "Abba The Museum", "search": "ABBA The Museum", "category": "Müze", "area": "Djurgården"},
    {"name": "Fotografiska", "search": "Fotografiska Stockholm", "category": "Müze", "area": "Södermalm"},
    {"name": "Nobel Ödülü Müzesi", "search": "Nobel Prize Museum", "category": "Müze", "area": "Gamla Stan"},
    {"name": "Drottningholm Sarayı", "search": "Drottningholm Palace", "category": "Tarihi", "area": "Drottningholm"},
    {"name": "Nordiska Müzesi", "search": "Nordiska Museet", "category": "Müze", "area": "Djurgården"},
    
    # Metro Sanatı (Dünyanın en uzun sanat galerisi)
    {"name": "T-Centralen Metro", "search": "T-Centralen Metro Station Art", "category": "Sanat", "area": "City"},
    {"name": "Solna Centrum Metro", "search": "Solna Centrum Metro Station Art", "category": "Sanat", "area": "Solna"},
    {"name": "Kungsträdgården Metro", "search": "Kungstradgarden Metro Station Art", "category": "Sanat", "area": "City"},
    {"name": "Stadion Metro", "search": "Stadion Metro Station Art", "category": "Sanat", "area": "Östermalm"},
    
    # Parklar & Manzara
    {"name": "Monteliusvägen", "search": "Monteliusvagen", "category": "Manzara", "area": "Södermalm"},
    {"name": "Skinnarviksberget", "search": "Skinnarviksberget", "category": "Manzara", "area": "Södermalm"},
    {"name": "Djurgården", "search": "Royal Djurgarden", "category": "Park", "area": "Djurgården"},
    {"name": "SkyView", "search": "SkyView Stockholm", "category": "Manzara", "area": "Johanneshov"},
    
    # Yeme-İçme (Fika & Köfte)
    {"name": "Meatballs for the People", "search": "Meatballs for the People", "category": "Restoran", "area": "Södermalm"},
    {"name": "Vete-Katten", "search": "Vete-Katten Stockholm", "category": "Cafe", "area": "City"},
    {"name": "Chokladkoppen", "search": "Chokladkoppen", "category": "Cafe", "area": "Gamla Stan"},
    {"name": "Fabrique", "search": "Fabrique Stenugnsbageri Stockholm", "category": "Cafe", "area": "Södermalm"},
    {"name": "Rosendals Trädgård", "search": "Rosendals Tradgard", "category": "Cafe", "area": "Djurgården"},
    {"name": "Pelikan", "search": "Restaurant Pelikan Stockholm", "category": "Restoran", "area": "Södermalm"},
    {"name": "Hermans", "search": "Hermans Vegetarian Restaurant", "category": "Restoran", "area": "Södermalm"},
    {"name": "Urban Deli", "search": "Urban Deli Nytorget", "category": "Restoran", "area": "Södermalm"},
    {"name": "Tak", "search": "Tak Stockholm", "category": "Bar", "area": "City"},

    # Alışveriş & Mahalleler
    {"name": "SoFo (South of Folkungagatan)", "search": "SoFo Södermalm", "category": "Alışveriş", "area": "Södermalm"},
    {"name": "Östermalms Saluhall", "search": "Ostermalms Saluhall", "category": "Alışveriş", "area": "Östermalm"},
    {"name": "Drottninggatan", "search": "Drottninggatan Stockholm", "category": "Alışveriş", "area": "City"},
    {"name": "Svenskt Tenn", "search": "Svenskt Tenn", "category": "Alışveriş", "area": "Östermalm"},
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
        "Müze": f"{name}, Stockholm'ün zengin kültürünü ve tarihini yansıtan önemli bir durak. {area} bölgesindeki bu müze, ziyaretçilerine benzersiz bir deneyim sunuyor.",
        "Tarihi": f"{name}, İsveç tarihinin en önemli simgelerinden biri. {area} bölgesinde yer alan bu yapı, mimarisiyle büyülüyor.",
        "Manzara": f"{name}, Stockholm'ün adalarını ve sularını tepeden izlemek için harika bir nokta. {area} bölgesindeki bu konum, özellikle gün batımında çok popüler.",
        "Deneyim": f"{name}, Stockholm'ün modern ve geleneksel yüzünü bir arada görebileceğiniz bir yer. {area}'da bulunan bu nokta, şehrin ruhunu yansıtıyor.",
        "Park": f"{name}, şehrin içinde doğayla baş başa kalmak için yeşil bir kaçış noktası. {area} bölgesindeki bu park, piknik ve yürüyüş için ideal.",
        "Restoran": f"{name}, İsveç mutfağının (özellikle köfte) en lezzetli örneklerini sunan bir mekan. {area} bölgesindeki bu restoran, sıcak atmosferiyle biliniyor.",
        "Cafe": f"{name}, 'Fika' kültürü için mükemmel bir durak. {area}'da yer alan bu kafe, tarçınlı çörekleri ve kahvesiyle meşhur.",
        "Alışveriş": f"{name}, İskandinav tasarımı ve vintage ürünler için popüler bir adres. {area}'da bulunan bu mekan, alışveriş tutkunlarını cezbediyor.",
        "Sanat": f"{name}, Stockholm metrosunun 'dünyanın en uzun sanat galerisi' unvanını hak ettiğini kanıtlayan bir istasyon. {area} bölgesinde yer alıyor.",
    }
    return descriptions.get(category, f"{name}, Stockholm'de keşfedilmeyi bekleyen harika bir yer.")

def main():
    print("🇸🇪 Stockholm şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(STOCKHOLM_PLACES, 1):
        print(f"\n[{i}/{len(STOCKHOLM_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 59.3293)
        lng = geometry.get("lng", 18.0686)
        
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
            "tags": [place["area"].lower(), "stockholm", "isveç", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "high" if place["category"] in ["Restoran", "Alışveriş"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Müze", "Tarihi"] else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Müzeler için 'Stockholm Pass' almayı düşünebilirsiniz.",
            "description_en": f"{place['name']} is a highlight of Stockholm in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Stockholm",
        "country": "İsveç",
        "description": "14 ada üzerine kurulu, köprülerle birbirine bağlı 'Kuzeyin Venediği'. Gamla Stan'ın tarihi sokakları, modern tasarım, ABBA Müzesi ve Fika kültürü.",
        "heroImage": "",
        "coordinates": {
            "lat": 59.3293,
            "lng": 18.0686
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Gamla Stan" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/stockholm.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Stockholm verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
