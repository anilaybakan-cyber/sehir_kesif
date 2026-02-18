#!/usr/bin/env python3
"""
Midilli (Lesbos) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve midilli.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Midilli'nin temel mekanları - Biz Evde Yokuz
MIDILLI_PLACES = [
    # Köyler & Tarihi
    {"name": "Molyvos (Mithymna)", "search": "Molyvos Village Lesvos", "category": "Deneyim", "area": "Kuzey"},
    {"name": "Molyvos Kalesi", "search": "Molyvos Castle", "category": "Tarihi", "area": "Molyvos"},
    {"name": "Midilli Kalesi (Mytilene Castle)", "search": "Castle of Mytilene", "category": "Tarihi", "area": "Merkez"},
    {"name": "Petra", "search": "Petra Lesvos", "category": "Deneyim", "area": "Kuzey"},
    {"name": "Panagia Glykofilousa Kilisesi", "search": "Panagia Glykofilousa Petra", "category": "Tarihi", "area": "Petra"},
    {"name": "Vatoussa", "search": "Vatoussa Village Lesvos", "category": "Deneyim", "area": "Batı"},
    {"name": "Agiasos", "search": "Agiasos Village Lesvos", "category": "Deneyim", "area": "Dağlık"},
    {"name": "Sigri", "search": "Sigri Lesvos", "category": "Manzara", "area": "Batı"},
    
    # Doğa & Plajlar
    {"name": "Taşlaşmış Orman (Petrified Forest)", "search": "Petrified Forest of Lesvos", "category": "Müze", "area": "Sigri"},
    {"name": "Eressos Plajı", "search": "Skala Eressos Beach", "category": "Manzara", "area": "Eressos"},
    {"name": "Vatera Plajı", "search": "Vatera Beach Lesvos", "category": "Manzara", "area": "Güney"},
    {"name": "Tarti Plajı", "search": "Tarti Beach Lesvos", "category": "Manzara", "area": "Gera"},
    {"name": "Midilli Termalleri", "search": "Hot Springs of Eftalou", "category": "Deneyim", "area": "Eftalou"},
    
    # Yeme-İçme (Ouzo & Deniz Ürünü)
    {"name": "Kadınlar Kooperatifi (Petra)", "search": "Petra Women's Cooperative", "category": "Restoran", "area": "Petra"},
    {"name": "Vafios Taverna", "search": "Vafios Taverna Molyvos", "category": "Restoran", "area": "Molyvos Yakını"},
    {"name": "Ouzadiko Baboukos", "search": "Ouzadiko Baboukos Mytilene", "category": "Restoran", "area": "Merkez"},
    {"name": "Ermis Ouzeri", "search": "Ermis Ouzeri Mytilene", "category": "Restoran", "area": "Merkez"},
    {"name": "Tsalikis", "search": "Tsalikis Taverna Lesvos", "category": "Restoran", "area": "Loutra"},
    {"name": "Gorgona", "search": "Gorgona Restaurant Skala Sykaminas", "category": "Restoran", "area": "Skala Sykaminas"},
    {"name": "Be Happy", "search": "Be Happy Waffles Molyvos", "category": "Cafe", "area": "Molyvos"},
    {"name": "Parasol Beach Bar", "search": "Parasol Beach Bar Eressos", "category": "Bar", "area": "Eressos"},
    
    # Müzeler & Kültür
    {"name": "Barbayanni Uzo Müzesi", "search": "Barbayanni Ouzo Museum", "category": "Müze", "area": "Plomari"},
    {"name": "Midilli Arkeoloji Müzesi", "search": "Archaeological Museum of Mytilene", "category": "Müze", "area": "Merkez"},
    {"name": "Theophilos Müzesi", "search": "Theophilos Museum", "category": "Müze", "area": "Varia"},
    {"name": "Plomari", "search": "Plomari Lesvos", "category": "Deneyim", "area": "Güney"},
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
        "Müze": f"{name}, Midilli'nin tarihini ve kültürünü (özellikle Uzo yapımını) keşfetmek için harika bir durak. {area} bölgesindeki bu müze çok ilginç.",
        "Tarihi": f"{name}, adanın zengin geçmişine tanıklık eden heybetli bir yapı. {area} bölgesinde yer alan bu kale, Ege Denizi'ne hakim bir konumda.",
        "Manzara": f"{name}, Midilli'nin doğal güzelliklerini ve turkuaz sularını gözler önüne seriyor. {area} bölgesindeki bu nokta, gün batımı için ideal.",
        "Deneyim": f"{name}, adanın en şirin ve otantik köylerinden biri. {area}'da bulunan bu yer, taş evleri ve dar sokaklarıyla büyülüyor.",
        "Park": f"{name}, doğa harikası bir alan. {area} bölgesindeki bu yer, jeolojik önemiyle UNESCO koruması altında.",
        "Restoran": f"{name}, taze deniz ürünleri ve meşhur mezeleriyle gerçek bir Yunan taverna deneyimi sunuyor. {area} bölgesindeki bu restoran çok popüler.",
        "Cafe": f"{name}, deniz kenarında serinlemek veya güzel bir tatlı yemek için keyifli bir mola. {area}'da yer alıyor.",
    }
    return descriptions.get(category, f"{name}, Midilli'de keşfedilmeyi bekleyen harika bir yer.")

def main():
    print("🇬🇷 Midilli şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(MIDILLI_PLACES, 1):
        print(f"\n[{i}/{len(MIDILLI_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 39.1044)
        lng = geometry.get("lng", 26.5557)
        
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
            "tags": [place["area"].lower(), "midilli", "yunanistan", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "low" if place["category"] == "Restoran" else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Yazın",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Kapıda vize uygulamasıyla kolayca gidebilirsiniz.",
            "description_en": f"{place['name']} is a highlight of Lesbos in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Midilli",
        "country": "Yunanistan",
        "description": "Zeytin ağaçları, Uzo fabrikaları, şirin balıkçı köyleri ve orta çağ kaleleriyle Ege'nin en büyük ve en otantik adalarından biri.",
        "heroImage": "",
        "coordinates": {
            "lat": 39.1044,
            "lng": 26.5557
        },
        "highlights": highlights
    }
    
    # Hero image
    for h in highlights:
        if "Molyvos" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/midilli.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Midilli verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
