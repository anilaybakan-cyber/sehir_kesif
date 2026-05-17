from dotenv import load_dotenv
load_dotenv()
import os
#!/usr/bin/env python3
"""
Kapadokya şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve kapadokya.json oluşturur.
"""

import json
import requests
import time

from typing import Optional

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Kapadokya'nın temel mekanları - araştırmadan derlendi
KAPADOKYA_PLACES = [
    # Tarihi & Müzeler
    {"name": "Göreme Açık Hava Müzesi", "search": "Goreme Open Air Museum Cappadocia", "category": "Müze", "area": "Göreme"},
    {"name": "Derinkuyu Yeraltı Şehri", "search": "Derinkuyu Underground City", "category": "Müze", "area": "Derinkuyu"},
    {"name": "Kaymaklı Yeraltı Şehri", "search": "Kaymakli Underground City", "category": "Müze", "area": "Kaymaklı"},
    {"name": "Özkonak Yeraltı Şehri", "search": "Ozkonak Underground City", "category": "Müze", "area": "Özkonak"},
    {"name": "Zelve Açık Hava Müzesi", "search": "Zelve Open Air Museum Cappadocia", "category": "Müze", "area": "Zelve"},
    {"name": "Hacı Bektaş Veli Müzesi", "search": "Haci Bektas Veli Museum", "category": "Müze", "area": "Hacıbektaş"},
    {"name": "Avanos Güray Müze", "search": "Guray Museum Avanos", "category": "Müze", "area": "Avanos"},
    
    # Tarihi Yapılar
    {"name": "Uçhisar Kalesi", "search": "Uchisar Castle Cappadocia", "category": "Tarihi", "area": "Uçhisar"},
    {"name": "Ortahisar Kalesi", "search": "Ortahisar Castle Cappadocia", "category": "Tarihi", "area": "Ortahisar"},
    {"name": "Nevşehir Kalesi", "search": "Nevsehir Castle", "category": "Tarihi", "area": "Nevşehir"},
    {"name": "Paşabağ Peribacaları", "search": "Pasabag Fairy Chimneys", "category": "Tarihi", "area": "Göreme"},
    {"name": "Devrent Vadisi", "search": "Devrent Valley Cappadocia Imagination Valley", "category": "Tarihi", "area": "Göreme"},
    
    # Manzara Noktaları
    {"name": "Aşk Vadisi", "search": "Love Valley Cappadocia", "category": "Manzara", "area": "Göreme"},
    {"name": "Güvercinlik Vadisi", "search": "Pigeon Valley Cappadocia", "category": "Manzara", "area": "Uçhisar"},
    {"name": "Kızılçukur Vadisi", "search": "Red Valley Kizilcukur Cappadocia", "category": "Manzara", "area": "Göreme"},
    {"name": "Meskendir Vadisi", "search": "Meskendir Valley Cappadocia", "category": "Manzara", "area": "Göreme"},
    {"name": "Ihlara Vadisi", "search": "Ihlara Valley Cappadocia", "category": "Manzara", "area": "Ihlara"},
    {"name": "Sunset Point Göreme", "search": "Sunset Point Goreme Cappadocia", "category": "Manzara", "area": "Göreme"},
    {"name": "Esentepe Seyir Terası", "search": "Esentepe Viewpoint Goreme", "category": "Manzara", "area": "Göreme"},
    
    # Deneyimler
    {"name": "Kapadokya Balon Turu", "search": "Cappadocia Hot Air Balloon", "category": "Deneyim", "area": "Göreme"},
    {"name": "ATV Safari Turu", "search": "ATV Safari Tour Cappadocia", "category": "Deneyim", "area": "Göreme"},
    {"name": "At Binme Turu", "search": "Horse Riding Cappadocia", "category": "Deneyim", "area": "Göreme"},
    {"name": "Çömlek Atölyesi", "search": "Pottery Workshop Avanos", "category": "Deneyim", "area": "Avanos"},
    {"name": "Şarap Tadımı", "search": "Wine Tasting Cappadocia", "category": "Deneyim", "area": "Ürgüp"},
    {"name": "Türk Gecesi", "search": "Turkish Night Show Cappadocia", "category": "Deneyim", "area": "Göreme"},
    
    # Parklar
    {"name": "Göreme Milli Parkı", "search": "Goreme National Park", "category": "Park", "area": "Göreme"},
    {"name": "Soğanlı Vadisi", "search": "Soganli Valley Cappadocia", "category": "Park", "area": "Soğanlı"},
    
    # Restoranlar
    {"name": "Topdeck Cave Restaurant", "search": "Topdeck Cave Restaurant Goreme", "category": "Restoran", "area": "Göreme"},
    {"name": "Old Greek House", "search": "Old Greek House Restaurant Mustafapasa", "category": "Restoran", "area": "Mustafapaşa"},
    {"name": "Seki Restaurant", "search": "Seki Restaurant Urgup", "category": "Restoran", "area": "Ürgüp"},
    {"name": "Dibek Restaurant", "search": "Dibek Restaurant Goreme", "category": "Restoran", "area": "Göreme"},
    {"name": "Lil'a Restaurant", "search": "Lila Restaurant Cappadocia", "category": "Restoran", "area": "Ürgüp"},
    {"name": "Elai Restaurant", "search": "Elai Restaurant Cappadocia", "category": "Restoran", "area": "Ürgüp"},
    {"name": "Ziggy's Shoppe", "search": "Ziggys Shoppe Urgup", "category": "Restoran", "area": "Ürgüp"},
    {"name": "Pumpkin Goreme", "search": "Pumpkin Restaurant Goreme", "category": "Restoran", "area": "Göreme"},
    {"name": "Cappadocian Cuisine", "search": "Cappadocian Cuisine Restaurant", "category": "Restoran", "area": "Göreme"},
    {"name": "Kebapzade", "search": "Kebapzade Urgup", "category": "Restoran", "area": "Ürgüp"},
    
    # Kafeler
    {"name": "Cafe Safak", "search": "Cafe Safak Goreme Sunrise Point", "category": "Cafe", "area": "Göreme"},
    {"name": "Kale Cafe", "search": "Kale Cafe Uchisar Castle", "category": "Cafe", "area": "Uçhisar"},
    {"name": "My Mother's Cafe", "search": "My Mothers Cafe Goreme", "category": "Cafe", "area": "Göreme"},
    {"name": "Coffee House Goreme", "search": "Coffee House Goreme Cappadocia", "category": "Cafe", "area": "Göreme"},
    {"name": "Orient Cafe", "search": "Orient Cafe Goreme", "category": "Cafe", "area": "Göreme"},
    {"name": "Sedef Cafe", "search": "Sedef Cafe Uchisar", "category": "Cafe", "area": "Uçhisar"},
    
    # Barlar
    {"name": "Fat Boys Bar", "search": "Fat Boys Bar Goreme", "category": "Bar", "area": "Göreme"},
    {"name": "Flintstones Bar", "search": "Flintstones Bar Goreme", "category": "Bar", "area": "Göreme"},
    {"name": "Red Red Wine House", "search": "Red Red Wine House Goreme", "category": "Bar", "area": "Göreme"},
    
    # Alışveriş
    {"name": "Avanos Çömlekçiler Çarşısı", "search": "Avanos Pottery Market", "category": "Alışveriş", "area": "Avanos"},
    {"name": "Göreme Merkez Çarşı", "search": "Goreme Market Bazaar", "category": "Alışveriş", "area": "Göreme"},
    {"name": "Ürgüp Halı Mağazaları", "search": "Urgup Carpet Shops", "category": "Alışveriş", "area": "Ürgüp"},
    {"name": "Sultan Carpets", "search": "Sultan Carpets Cappadocia", "category": "Alışveriş", "area": "Göreme"},
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
        "Müze": f"{name}, Kapadokya'nın eşsiz tarihi dokusunu yansıtan önemli bir müze. {area} bölgesinde yer alan bu mekan, bölgenin zengin kültürel mirasını keşfetmek isteyenler için mutlaka görülmeli.",
        "Tarihi": f"{name}, Kapadokya'nın binlerce yıllık tarihine tanıklık eden muhteşem bir yapı. {area}'da yer alan bu tarihi mekan, peri bacaları ve volkanik oluşumların büyüleyici atmosferini sunuyor.",
        "Manzara": f"{name}, Kapadokya'nın en etkileyici manzara noktalarından biri. {area} bölgesinde bulunan bu nokta, gün doğumu ve gün batımında unutulmaz fotoğraf kareleri sunuyor.",
        "Deneyim": f"{name}, Kapadokya'da yaşanması gereken eşsiz deneyimlerden biri. {area}'da sunulan bu aktivite, bölgenin büyüleyici atmosferini farklı bir perspektiften keşfetmenizi sağlıyor.",
        "Park": f"{name}, Kapadokya'nın doğal güzelliklerini keşfetmek için ideal bir nokta. {area} bölgesindeki bu alan, yürüyüş ve doğa fotoğrafçılığı için mükemmel.",
        "Restoran": f"{name}, Kapadokya'nın lezzet duraklarından biri. {area} bölgesindeki bu mekan, yerel mutfağın seçkin örnekleriyle damak zevkinize hitap ediyor.",
        "Cafe": f"{name}, Kapadokya'nın atmosferik kafelerinden biri. {area}'da bulunan bu mekan, peri bacaları manzarasında kahve keyfi sunuyor.",
        "Bar": f"{name}, Kapadokya'nın gece hayatının renkli noktalarından biri. {area}'daki bu mekan, yerel şaraplar ve canlı atmosferiyle keyifli bir akşam vaat ediyor.",
        "Alışveriş": f"{name}, Kapadokya'nın en otantik alışveriş noktalarından biri. {area}'da yer alan bu mekan, el yapımı seramikler, halılar ve yerel ürünlerle dolu.",
    }
    return descriptions.get(category, f"{name}, Kapadokya'nın keşfedilmeye değer noktalarından biri.")

def main():
    print("🏔️ Kapadokya şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(KAPADOKYA_PLACES, 1):
        print(f"\n[{i}/{len(KAPADOKYA_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 38.6431)
        lng = geometry.get("lng", 34.8289)
        
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
            "tags": [place["area"].lower(), "kapadokya", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Manzara", "Müze"] else "Öğleden sonra",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Kapadokya'nın büyüleyici atmosferinin tadını çıkarın!",
            "description_en": f"{place['name']} is one of Cappadocia's must-visit destinations in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Kapadokya",
        "country": "Türkiye",
        "description": "Peri bacaları, yeraltı şehirleri ve sıcak hava balonlarıyla dünyaca ünlü UNESCO Dünya Mirası. Göreme, Ürgüp ve Uçhisar'ın büyüleyici manzaralarıyla eşsiz bir deneyim.",
        "heroImage": "",  # İlk fotoğraftan alınacak
        "coordinates": {
            "lat": 38.6431,
            "lng": 34.8289
        },
        "highlights": highlights
    }
    
    # Hero image'ı ilk manzara noktasından al
    for h in highlights:
        if h.get("imageUrl") and h.get("category") == "Manzara":
            city_data["heroImage"] = h["imageUrl"]
            break
    
    # Dosyaya yaz
    output_path = "assets/cities/kapadokya.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Kapadokya verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
