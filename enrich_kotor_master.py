import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Kotor Montenegro", f"{place_name} Montenegro", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:30000@42.4247,18.7712"
            r = requests.get(url)
            data = r.json()
            if data['status'] == 'OK' and data['candidates']:
                if 'photos' in data['candidates'][0]:
                    ref = data['candidates'][0]['photos'][0]['photo_reference']
                    print(f"  ✓ {place_name}")
                    return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={ref}&key={API_KEY}"
        except:
            continue
    print(f"  ✗ {place_name}")
    return None

# BATCH 1: Perast & Adalar
batch_1 = [
    {"name": "Perast", "name_en": "Perast", "area": "Kotor Bay", "category": "Tarihi", "tags": ["unesco", "kasaba", "barok"], "lat": 42.4867, "lng": 18.6978, "price": "free", "rating": 4.8, "description": "UNESCO Dünya Mirası listesindeki Barok kasaba. Venedik dönemi sarayları ve 17 kilise.", "description_en": "UNESCO World Heritage Baroque town with Venetian palaces and 17 churches.", "bestTime": "Gündüz", "tips": "Kotor'dan 20 dakika araçla. Botla adalara geçin.", "tips_en": "20 minutes from Kotor by car. Take boats to islands."},
    {"name": "Our Lady of the Rocks", "name_en": "Our Lady of the Rocks", "area": "Perast", "category": "Tarihi", "tags": ["ada", "kilise", "efsane"], "lat": 42.4872, "lng": 18.6875, "price": "medium", "rating": 4.9, "description": "Yapay ada üzerinde 15. yüzyıl kilisesi. Denizcilerin taşlarla oluşturduğu efsanevi ada.", "description_en": "15th century church on artificial island. Legendary island created by sailors with stones.", "bestTime": "Sabah", "tips": "Perast'tan 5 dakikalık bot turu. Müze içinde.", "tips_en": "5-minute boat ride from Perast. Museum inside."},
    {"name": "St. George Island", "name_en": "St. George Island", "area": "Perast", "category": "Manzara", "tags": ["ada", "manastır", "gizemli"], "lat": 42.4875, "lng": 18.6886, "price": "free", "rating": 4.7, "description": "Benediktin manastırı olan doğal ada. Ziyarete kapalı ama yakından izlenebilir.", "description_en": "Natural island with Benedictine monastery. Closed to visits but can be viewed closely.", "bestTime": "Gündüz", "tips": "Our Lady of the Rocks'a giderken yanından geçilir.", "tips_en": "Passed by when going to Our Lady of the Rocks."},
    {"name": "Perast Müzesi", "name_en": "Perast Museum", "area": "Perast", "category": "Müze", "tags": ["tarih", "denizcilik", "barok"], "lat": 42.4865, "lng": 18.6980, "price": "low", "rating": 4.5, "description": "Bujovic Sarayı'nda kurulu, Perast'ın denizcilik tarihini anlatan müze.", "description_en": "Museum in Bujovic Palace displaying Perast's maritime history.", "bestTime": "Gündüz", "tips": "Perast'ın en güzel Barok binası.", "tips_en": "Perast's most beautiful Baroque building."}
]

# BATCH 2: Lovcen Milli Parkı
batch_2 = [
    {"name": "Lovcen Milli Parkı", "name_en": "Lovcen National Park", "area": "Dağlar", "category": "Doğa", "tags": ["milli park", "dağ", "doğa"], "lat": 42.3967, "lng": 18.8422, "price": "low", "rating": 4.8, "description": "Karadağ'ın kutsal dağı. 1.749 metre yükseklikte muhteşem manzaralar.", "description_en": "Montenegro's sacred mountain with stunning views at 1,749 meters.", "bestTime": "Gündüz", "tips": "Kotor'dan 1.5 saat. 25 viraj yolda.", "tips_en": "1.5 hours from Kotor. 25 hairpin turns on the road."},
    {"name": "Njegos Mozolesi", "name_en": "Njegos Mausoleum", "area": "Lovcen", "category": "Tarihi", "tags": ["mozole", "anıt", "panorama"], "lat": 42.3997, "lng": 18.8436, "price": "medium", "rating": 4.9, "description": "Karadağ'ın en büyük şairinin anıt mezarı. 461 basamak tırmanarak ulaşılır.", "description_en": "Mausoleum of Montenegro's greatest poet. Reached by climbing 461 steps.", "bestTime": "Açık hava", "tips": "Balkanlardaki en yüksek mozole.", "tips_en": "Highest mausoleum in the Balkans."},
    {"name": "Ivanova Korita", "name_en": "Ivanova Korita", "area": "Lovcen", "category": "Deneyim", "tags": ["piknik", "doğa", "restoran"], "distanceFromCenter": 25.0, "lat": 42.4000, "lng": 18.8300, "price": "low", "rating": 4.4, "description": "Milli park içinde piknik alanı ve geleneksel restoran.", "description_en": "Picnic area and traditional restaurant in national park.", "bestTime": "Öğle", "tips": "Yerel Njeguški pršut ve peynir deneyin.", "tips_en": "Try local Njeguški ham and cheese."}
]

# BATCH 3: Adriyatik Kıyısı
batch_3 = [
    {"name": "Budva Old Town", "name_en": "Budva Old Town", "area": "Budva", "category": "Tarihi", "tags": ["eski şehir", "plaj", "gece hayatı"], "lat": 42.2889, "lng": 18.8378, "price": "free", "rating": 4.6, "description": "2.500 yıllık tarihi şehir. Plajlar, barlar ve gece hayatı.", "description_en": "2,500-year-old historic town. Beaches, bars and nightlife.", "bestTime": "Akşam", "tips": "Kotor'dan 30 dakika. Gece hayatı için en iyi yer.", "tips_en": "30 minutes from Kotor. Best place for nightlife."},
    {"name": "Sveti Stefan", "name_en": "Sveti Stefan", "area": "Budva", "category": "Manzara", "tags": ["ada", "lüks", "ikonik"], "lat": 42.2556, "lng": 18.8911, "price": "free", "rating": 4.8, "description": "Dünyaca ünlü ada-otel. Karadağ'ın en ikonik manzarası.", "description_en": "World-famous island-hotel. Montenegro's most iconic view.", "bestTime": "Gün batımı", "tips": "Adaya giriş sadece otel misafirleri için. Karşı plajdan fotoğraf çekin.", "tips_en": "Entry only for hotel guests. Take photos from opposite beach."},
    {"name": "Jaz Beach", "name_en": "Jaz Beach", "area": "Budva", "category": "Plaj", "tags": ["plaj", "festival", "geniş"], "lat": 42.2972, "lng": 18.8000, "price": "low", "rating": 4.5, "description": "1.2 km uzunluğunda popüler plaj. Yaz festivalleri.", "description_en": "Popular 1.2 km beach. Summer festivals.", "bestTime": "Yaz", "tips": "Sea Dance festivali için bilet alın.", "tips_en": "Get tickets for Sea Dance festival."},
    {"name": "Mogren Beach", "name_en": "Mogren Beach", "area": "Budva", "category": "Plaj", "tags": ["plaj", "mağara", "küçük"], "lat": 42.2897, "lng": 18.8317, "price": "low", "rating": 4.6, "description": "Budva kalesi yanında gizli koy. Kayalıklar ve berrak su.", "description_en": "Hidden cove by Budva fortress. Rocks and crystal clear water.", "bestTime": "Sabah", "tips": "Erken gidin, küçük plaj çabuk doluyor.", "tips_en": "Go early, small beach fills quickly."}
]

# BATCH 4: Kotor Eski Şehir Ek Yerler
batch_4 = [
    {"name": "Saat Kulesi (Clock Tower)", "name_en": "Clock Tower", "area": "Old Town", "category": "Tarihi", "tags": ["kule", "meydan", "simge"], "lat": 42.4246, "lng": 18.7713, "price": "free", "rating": 4.5, "description": "17. yüzyılda inşa edilen şehrin simgesi. Silah Meydanı'nda.", "description_en": "City symbol built in 17th century. In Arms Square.", "bestTime": "Gündüz", "tips": "Altındaki utanç taşını fark edin.", "tips_en": "Notice the shame stone underneath."},
    {"name": "Pima Sarayı", "name_en": "Pima Palace", "area": "Old Town", "category": "Tarihi", "tags": ["saray", "barok", "mimari"], "lat": 42.4248, "lng": 18.7718, "price": "free", "rating": 4.4, "description": "Venedik dönemi Barok sarayı. Cephe kabartmaları dikkat çekici.", "description_en": "Venetian Baroque palace. Notable facade reliefs.", "bestTime": "Gündüz", "tips": "Fotoğraf için en güzel Barok cephe.", "tips_en": "Best Baroque facade for photos."},
    {"name": "Karampana Meydanı", "name_en": "Karampana Square", "area": "Old Town", "category": "Manzara", "tags": ["meydan", "gizli", "sakin"], "lat": 42.4240, "lng": 18.7708, "price": "free", "rating": 4.3, "description": "Turistlerin kaçırdığı gizli meydan. Sakin atmosfer.", "description_en": "Hidden square missed by tourists. Calm atmosphere.", "bestTime": "İkindi", "tips": "Eski şehrin en sakin köşesi.", "tips_en": "Quietest corner of old town."},
    {"name": "Napoleon Tiyatrosu", "name_en": "Napoleon Theatre", "area": "Old Town", "category": "Tarihi", "tags": ["tiyatro", "napoleon", "tarihi"], "lat": 42.4252, "lng": 18.7720, "price": "low", "rating": 4.2, "description": "Fransız işgali döneminden kalma küçük tiyatro.", "description_en": "Small theatre from French occupation period.", "bestTime": "Akşam", "tips": "Bazen canlı performanslar var.", "tips_en": "Sometimes live performances."}
]

# BATCH 5: Ek Restoranlar & Kafeler
batch_5 = [
    {"name": "Restoran Stari Mlini", "name_en": "Old Mills Restaurant", "area": "Ljuta", "category": "Restoran", "tags": ["geleneksel", "nehir", "doğa"], "lat": 42.4450, "lng": 18.7350, "price": "medium", "rating": 4.8, "description": "Nehir kenarında tarihi değirmende yemek. Taze alabalık.", "description_en": "Dining in historic mill by river. Fresh trout.", "bestTime": "Öğle", "tips": "Kotor'dan 15 dakika. Kesinlikle rezervasyon yapın.", "tips_en": "15 minutes from Kotor. Definitely make reservation."},
    {"name": "Conte Nautilus", "name_en": "Conte Nautilus", "area": "Perast", "category": "Restoran", "tags": ["deniz ürünleri", "lüks", "manzara"], "lat": 42.4868, "lng": 18.6975, "price": "high", "rating": 4.7, "description": "Perast'ın en iyi restoranı. Körfez manzarası eşliğinde deniz ürünleri.", "description_en": "Best restaurant in Perast. Seafood with bay view.", "bestTime": "Gün batımı", "tips": "Gün batımı için teras masası alın.", "tips_en": "Get terrace table for sunset."},
    {"name": "Restoran Catovica Mlini", "name_en": "Catovica Mlini", "area": "Morinj", "category": "Restoran", "tags": ["değirmen", "doğal", "romantik"], "lat": 42.4850, "lng": 18.6500, "price": "high", "rating": 4.8, "description": "300 yıllık değirmende, şelale manzaralı romantik restoran.", "description_en": "Romantic restaurant in 300-year-old mill with waterfall view.", "bestTime": "Akşam", "tips": "Karadağ'ın en romantik restoranlarından.", "tips_en": "One of Montenegro's most romantic restaurants."},
    {"name": "Ladovina", "name_en": "Ladovina", "area": "Old Town", "category": "Restoran", "tags": ["yerel", "şarap", "mezeler"], "lat": 42.4245, "lng": 18.7710, "price": "medium", "rating": 4.5, "description": "Karadağ şarapları ve geleneksel mezeler.", "description_en": "Montenegrin wines and traditional appetizers.", "bestTime": "Akşam", "tips": "Vranac şarabını deneyin.", "tips_en": "Try Vranac wine."},
    {"name": "City Pub", "name_en": "City Pub", "area": "Old Town", "category": "Bar", "tags": ["bar", "canlı müzik", "yerel"], "lat": 42.4250, "lng": 18.7715, "price": "medium", "rating": 4.3, "description": "Yerel halkın buluşma noktası. Canlı müzik geceleri.", "description_en": "Local meeting point. Live music nights.", "bestTime": "Gece", "tips": "Hafta sonu canlı müzik var.", "tips_en": "Live music on weekends."},
    {"name": "Maximus", "name_en": "Maximus", "area": "Old Town", "category": "Bar", "tags": ["bar", "kokteyl", "teras"], "lat": 42.4255, "lng": 18.7720, "price": "medium", "rating": 4.4, "description": "Sur manzaralı kokteyl barı.", "description_en": "Cocktail bar with wall view.", "bestTime": "Gün batımı", "tips": "Aperol Spritz için en iyi adres.", "tips_en": "Best address for Aperol Spritz."}
]

# BATCH 6: Aktiviteler & Deneyimler
batch_6 = [
    {"name": "Kayak Turu", "name_en": "Kayak Tour", "area": "Kotor Bay", "category": "Deneyim", "tags": ["kayak", "macera", "su"], "lat": 42.4260, "lng": 18.7700, "price": "medium", "rating": 4.7, "description": "Körfezde kayakla mağaralara ve gizli koylara ulaşın.", "description_en": "Reach caves and hidden coves by kayaking in the bay.", "bestTime": "Sabah", "tips": "Güneş kremi ve su geçirmez çanta şart.", "tips_en": "Sunscreen and waterproof bag essential."},
    {"name": "Dalış (Diving)", "name_en": "Scuba Diving", "area": "Kotor Bay", "category": "Deneyim", "tags": ["dalış", "deniz", "macera"], "lat": 42.4200, "lng": 18.7650, "price": "high", "rating": 4.6, "description": "Batık gemiler ve su altı mağaraları keşfedin.", "description_en": "Explore sunken ships and underwater caves.", "bestTime": "Yaz", "tips": "Sertifikalı ve sertifikasız seçenekler var.", "tips_en": "Certified and uncertified options available."},
    {"name": "Paragliding", "name_en": "Paragliding", "area": "Budva", "category": "Deneyim", "tags": ["paraşüt", "adrenalin", "manzara"], "lat": 42.2900, "lng": 18.8400, "price": "high", "rating": 4.8, "description": "Adriyatik üzerinde yamaç paraşütü deneyimi.", "description_en": "Paragliding experience over the Adriatic.", "bestTime": "Güneşli", "tips": "Budva yakınlarından kalkış.", "tips_en": "Take off near Budva."},
    {"name": "Bisiklet Turu", "name_en": "Bike Tour", "area": "Kotor Bay", "category": "Deneyim", "tags": ["bisiklet", "doğa", "tur"], "lat": 42.4300, "lng": 18.7600, "price": "medium", "rating": 4.5, "description": "Körfez çevresinde bisiklet turu.", "description_en": "Bike tour around the bay.", "bestTime": "Sabah", "tips": "Perast'a kadar güzel parkur.", "tips_en": "Nice route up to Perast."},
    {"name": "Jeep Safari", "name_en": "Jeep Safari", "area": "Lovcen", "category": "Deneyim", "tags": ["safari", "dağ", "macera"], "lat": 42.4000, "lng": 18.8000, "price": "high", "rating": 4.6, "description": "4x4 ile dağ köylerini ve manzara noktalarını keşfedin.", "description_en": "Explore mountain villages and viewpoints in 4x4.", "bestTime": "Gündüz", "tips": "Yarım günlük veya tam günlük turlar.", "tips_en": "Half-day or full-day tours."}
]

# BATCH 7: Manzara Noktaları
batch_7 = [
    {"name": "Kotor Serpantine Viewpoint", "name_en": "Kotor Serpentine Viewpoint", "area": "Lovcen Road", "category": "Manzara", "tags": ["manzara", "fotoğraf", "viraj"], "lat": 42.4100, "lng": 18.8100, "price": "free", "rating": 4.9, "description": "Lovcen yolundaki 25 virajdan birinde körfez manzarası.", "description_en": "Bay view from one of 25 hairpin turns on Lovcen road.", "bestTime": "Gün batımı", "tips": "4. virajda park alanı var.", "tips_en": "Parking area at 4th hairpin turn."},
    {"name": "Krstac Viewpoint", "name_en": "Krstac Viewpoint", "area": "Lovcen", "category": "Manzara", "tags": ["manzara", "panorama", "dağ"], "lat": 42.4050, "lng": 18.8200, "price": "free", "rating": 4.7, "description": "Lovcen'e giderken muhteşem panoramik manzara noktası.", "description_en": "Magnificent panoramic viewpoint on the way to Lovcen.", "bestTime": "Öğleden sonra", "tips": "Burada yerel ürünler satılır.", "tips_en": "Local products sold here."},
    {"name": "Dobrota Promenade", "name_en": "Dobrota Promenade", "area": "Dobrota", "category": "Manzara", "tags": ["yürüyüş", "sahil", "sakin"], "lat": 42.4400, "lng": 18.7600, "price": "free", "rating": 4.4, "description": "Kotor'un hemen dışında sakin sahil yürüyüşü.", "description_en": "Quiet seaside walk just outside Kotor.", "bestTime": "Sabah", "tips": "Kahvaltı sonrası yürüyüş için ideal.", "tips_en": "Ideal for post-breakfast walk."}
]

def enrich():
    filepath = 'assets/cities/kotor.json'
    all_new = batch_1 + batch_2 + batch_3 + batch_4 + batch_5 + batch_6 + batch_7
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    print(f"Loaded {len(data['highlights'])} places.")
    
    existing_names = {p['name'].lower() for p in data['highlights']}
    places_to_add = []
    
    for place in all_new:
        if place['name'].lower() in existing_names:
            print(f"Skip: {place['name']}")
            continue
        print(f"Processing: {place['name']}")
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('(', '').replace(')', '')
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        place['distanceFromCenter'] = place.get('distanceFromCenter', 1.0)
        places_to_add.append(place)
        time.sleep(0.3)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places. Total: {len(data['highlights'])}")

if __name__ == "__main__":
    enrich()
