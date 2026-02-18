#!/usr/bin/env python3
"""
Belgrad (Belgrade) şehir JSON dosyası oluşturucu.
Google Places API kullanarak mekanları çeker ve belgrad.json oluşturur.
"""

import json
import requests
import time
from typing import Optional

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Belgrad'ın temel mekanları - araştırmadan derlendi
BELGRAD_PLACES = [
    # Tarihi & Müzeler
    {"name": "Belgrad Kalesi (Kalemegdan)", "search": "Belgrade Fortress Kalemegdan", "category": "Tarihi", "area": "Stari Grad"},
    {"name": "Aziz Sava Katedrali", "search": "Temple of Saint Sava Belgrade", "category": "Tarihi", "area": "Vracar"},
    {"name": "Nikola Tesla Müzesi", "search": "Nikola Tesla Museum Belgrade", "category": "Müze", "area": "Vracar"},
    {"name": "Sırbistan Ulusal Müzesi", "search": "National Museum of Serbia", "category": "Müze", "area": "Republic Square"},
    {"name": "Yugoslavya Tarihi Müzesi", "search": "Museum of Yugoslavia Belgrade", "category": "Müze", "area": "Dedinje"},
    {"name": "Çiçek Evi (Tito'nun Mezarı)", "search": "House of Flowers Belgrade", "category": "Tarihi", "area": "Dedinje"},
    {"name": "Ružica Kilisesi", "search": "Ruzica Church Belgrade", "category": "Tarihi", "area": "Kalemegdan"},
    {"name": "Çağdaş Sanat Müzesi", "search": "Museum of Contemporary Art Belgrade", "category": "Müze", "area": "Ušće"},
    {"name": "Prenses Ljubica Konağı", "search": "Princess Ljubica's Residence", "category": "Tarihi", "area": "Kosančićev Venac"},
    {"name": "Etnografya Müzesi", "search": "Ethnographic Museum Belgrade", "category": "Müze", "area": "Stari Grad"},
    
    # Meydanlar & Caddeler
    {"name": "Cumhuriyet Meydanı", "search": "Republic Square Belgrade", "category": "Manzara", "area": "Stari Grad"},
    {"name": "Knez Mihailova Caddesi", "search": "Knez Mihailova Street", "category": "Alışveriş", "area": "Stari Grad"},
    {"name": "Skadarlija", "search": "Skadarlija Belgrade", "category": "Deneyim", "area": "Stari Grad"},
    {"name": "Terazije", "search": "Terazije Belgrade", "category": "Manzara", "area": "Stari Grad"},
    {"name": "Slavija Meydanı", "search": "Slavija Square Belgrade", "category": "Manzara", "area": "Vracar"},
    {"name": "Beton Hala", "search": "Beton Hala Belgrade", "category": "Deneyim", "area": "Savamala"},
    
    # Parklar & Manzara
    {"name": "Ada Ciganlija", "search": "Ada Ciganlija Belgrade", "category": "Park", "area": "Çukarica"},
    {"name": "Taşmeydan Parkı", "search": "Tasmajdan Park Belgrade", "category": "Park", "area": "Palilula"},
    {"name": "Zemun Sahili", "search": "Zemun Quay Belgrade", "category": "Manzara", "area": "Zemun"},
    {"name": "Gardoş Kulesi", "search": "Gardos Tower Zemun", "category": "Manzara", "area": "Zemun"},
    {"name": "Avala Kulesi", "search": "Avala Tower Belgrade", "category": "Manzara", "area": "Avala"},
    {"name": "Topçuder", "search": "Topcider Park Belgrade", "category": "Park", "area": "Savski Venac"},
    
    # Restoranlar
    {"name": "Tri Sesira", "search": "Tri Sesira Skadarlija", "category": "Restoran", "area": "Skadarlija"},
    {"name": "Dva Jelena", "search": "Dva Jelena Skadarlija", "category": "Restoran", "area": "Skadarlija"},
    {"name": "Lorenzo & Kakalamba", "search": "Lorenzo & Kakalamba Belgrade", "category": "Restoran", "area": "Palilula"},
    {"name": "Manufaktura", "search": "Manufaktura Belgrade", "category": "Restoran", "area": "Stari Grad"},
    {"name": "Ambar", "search": "Ambar Belgrade", "category": "Restoran", "area": "Beton Hala"},
    {"name": "Toro Latin GastroBar", "search": "Toro Latin GastroBar Belgrade", "category": "Restoran", "area": "Beton Hala"},
    {"name": "Mala Fabrika Ukusa", "search": "Mala Fabrika Ukusa Belgrade", "category": "Restoran", "area": "Vracar"},
    {"name": "Frans", "search": "Frans Restaurant Belgrade", "category": "Restoran", "area": "Vracar"},
    {"name": "Walter Sarajevski Cevap", "search": "Walter Sarajevski Cevap Belgrade", "category": "Restoran", "area": "Stari Grad"},
    {"name": "Pizza Bar", "search": "Pizza Bar Belgrade", "category": "Restoran", "area": "Novi Beograd"},
    
    # Kafeler & Tatlıcılar
    {"name": "Hotel Moskva Café", "search": "Hotel Moskva Cafe Belgrade", "category": "Cafe", "area": "Terazije"},
    {"name": "Kafeterija Magazin 1907", "search": "Kafeterija Magazin 1907 Belgrade", "category": "Cafe", "area": "Stari Grad"},
    {"name": "Aviator Coffee Explorer", "search": "Aviator Coffee Explorer Belgrade", "category": "Cafe", "area": "Vracar"},
    {"name": "Przionica D59B", "search": "Przionica D59B Belgrade", "category": "Cafe", "area": "Dorcol"},
    {"name": "Smokvica", "search": "Smokvica Belgrade", "category": "Cafe", "area": "Vracar"},
    {"name": "Crna Ovca", "search": "Crna Ovca Ice Cream Belgrade", "category": "Cafe", "area": "Stari Grad"},
    {"name": "Ferdinand Knedle", "search": "Ferdinand Knedle Belgrade", "category": "Cafe", "area": "Stari Grad"},
    
    # Barlar & Gece Hayatı
    {"name": "Samo Pivo", "search": "Samo Pivo Belgrade", "category": "Bar", "area": "Stari Grad"},
    {"name": "Jazz Bašta", "search": "Jazz Basta Belgrade", "category": "Bar", "area": "Savamala"},
    {"name": "Druid Bar", "search": "Druid Bar Belgrade", "category": "Bar", "area": "Stari Grad"},
    {"name": "Cantina de Frida", "search": "Cantina de Frida Belgrade", "category": "Restoran", "area": "Beton Hala"},
    {"name": "Boho Bar", "search": "Boho Bar Kalemegdan", "category": "Bar", "area": "Kalemegdan"},
    
    # Alışveriş
    {"name": "Ušće Shopping Center", "search": "Usce Shopping Center Belgrade", "category": "Alışveriş", "area": "Novi Beograd"},
    {"name": "Galerija Belgrade", "search": "Galerija Belgrade Shopping Mall", "category": "Alışveriş", "area": "Belgrade Waterfront"},
    {"name": "Rajićeva Shopping Center", "search": "Rajiceva Shopping Center", "category": "Alışveriş", "area": "Stari Grad"},
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
        "Müze": f"{name}, Belgrad'ın zengin tarihini ve kültürünü keşfetmek için harika bir durak. {area} bölgesindeki bu müze, ziyaretçilerine unutulmaz bir deneyim sunuyor.",
        "Tarihi": f"{name}, şehrin en önemli tarihi simgelerinden biri. {area}'da yer alan bu yapı, Belgrad'ın çok katmanlı geçmişine tanıklık ediyor.",
        "Manzara": f"{name}, şehri tepeden izlemek ve harika fotoğraflar çekmek için mükemmel bir nokta. {area} bölgesindeki bu konum, özellikle gün batımında büyüleyici.",
        "Deneyim": f"{name}, Belgrad'ın enerjisini hissetmek için mutlaka uğranması gereken bir yer. {area}'da bulunan bu nokta, yerel yaşamın kalbinin attığı yerlerden.",
        "Park": f"{name}, şehir karmaşasından uzaklaşıp doğayla buluşmak için ideal. {area} bölgesindeki bu park, yürüyüş, spor ve piknik için tercih ediliyor.",
        "Restoran": f"{name}, Sırp mutfağının lezzetli örneklerini tadabileceğiniz popüler bir mekan. {area} bölgesindeki bu restoran, hem atmosferi hem de yemekleriyle öne çıkıyor.",
        "Cafe": f"{name}, kahve keyfi yapmak ve dinlenmek için şık bir durak. {area}'da yer alan bu kafe, şehrin modern ve geleneksel yüzünü bir arada sunuyor.",
        "Bar": f"{name}, Belgrad'ın ünlü gece hayatını deneyimlemek için harika bir seçenek. {area}'daki bu mekan, keyifli müzikleri ve içecekleriyle dikkat çekiyor.",
        "Alışveriş": f"{name}, alışveriş yapmak ve keyifli vakit geçirmek için şehrin en popüler noktalarından biri. {area}'da bulunan bu mekan, birçok markayı bir arada sunuyor.",
    }
    return descriptions.get(category, f"{name}, Belgrad'da keşfedilmeyi bekleyen özel bir nokta.")

def main():
    print("🇷🇸 Belgrad şehir verisi oluşturuluyor...")
    
    highlights = []
    
    for i, place in enumerate(BELGRAD_PLACES, 1):
        print(f"\n[{i}/{len(BELGRAD_PLACES)}] {place['name']} işleniyor...")
        
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
        lat = geometry.get("lat", 44.7866)
        lng = geometry.get("lng", 20.4489)
        
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
            "tags": [place["area"].lower(), "belgrad", place["category"].lower()],
            "distanceFromCenter": 0,
            "lat": lat,
            "lng": lng,
            "price": "low" if place["category"] in ["Park", "Manzara", "Tarihi"] else "medium",
            "rating": rating or 4.5,
            "description": description,
            "bestTime": "Sabah" if place["category"] in ["Müze", "Tarihi"] else "Akşam",
            "bestFor": ["herkes"],
            "source": "google",
            "imageUrl": get_photo_url(photo_ref) if photo_ref else "",
            "tips": "Tuna ve Sava nehirlerinin birleştiği yerde gün batımını izleyin!",
            "description_en": f"{place['name']} is a highlight of Belgrade in the {place['area']} area."
        }
        
        highlights.append(highlight)
        print(f"  ✅ Eklendi (rating: {rating})")
        
        time.sleep(0.3)  # Rate limiting
    
    # JSON oluştur
    city_data = {
        "city": "Belgrad",
        "country": "Sırbistan",
        "description": "Tuna ve Sava nehirlerinin buluştuğu, Avrupa'nın en eski şehirlerinden biri. Hareketli gece hayatı, zengin tarihi ve lezzetli Balkan mutfağıyla vizesiz cennet.",
        "heroImage": "",
        "coordinates": {
            "lat": 44.7866,
            "lng": 20.4489
        },
        "highlights": highlights
    }
    
    # Hero image - Kalemegdan veya Aziz Sava
    for h in highlights:
        if "Kalemegdan" in h["name"] and h.get("imageUrl"):
            city_data["heroImage"] = h["imageUrl"]
            break
            
    if not city_data["heroImage"] and highlights:
         city_data["heroImage"] = highlights[0].get("imageUrl", "")

    # Dosyaya yaz
    output_path = "assets/cities/belgrad.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Belgrad verisi oluşturuldu!")
    print(f"📁 Dosya: {output_path}")
    print(f"📊 Toplam mekan: {len(highlights)}")

if __name__ == "__main__":
    main()
