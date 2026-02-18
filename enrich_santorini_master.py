import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Santorini Greece", f"{place_name} Santorini", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:30000@36.4618,25.3753"
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

# BATCH 1: Oia & Fira Ek Yerler
batch_1 = [
    {"name": "Oia Mavi Kubbeler", "name_en": "Oia Blue Domes", "area": "Oia", "category": "Manzara", "tags": ["kubbe", "kilise", "ikonik"], "lat": 36.4615, "lng": 25.3735, "price": "free", "rating": 4.9, "description": "Santorini'nin en ikonik manzarası - mavi kubbeli kiliseler.", "description_en": "Santorini's most iconic view - blue domed churches.", "bestTime": "Sabah", "tips": "Kalabalıktan kaçmak için sabah erken gidin.", "tips_en": "Go early morning to avoid crowds."},
    {"name": "Fira Merkez", "name_en": "Fira Town Center", "area": "Fira", "category": "Deneyim", "tags": ["merkez", "alışveriş", "yeme"], "lat": 36.4165, "lng": 25.4315, "price": "free", "rating": 4.6, "description": "Ada'nın başkenti, kafeler, restoranlar ve butiklerle dolu.", "description_en": "Capital of the island, full of cafes, restaurants and boutiques.", "bestTime": "Akşam", "tips": "Gün batımı için kaldera kenarındaki kafelere gidin.", "tips_en": "Go to caldera-edge cafes for sunset."},
    {"name": "Firostefani", "name_en": "Firostefani", "area": "Firostefani", "category": "Manzara", "tags": ["köy", "sakin", "manzara"], "lat": 36.4262, "lng": 25.4275, "price": "free", "rating": 4.7, "description": "Fira'nın tacı, sakin ve romantik köy.", "description_en": "Crown of Fira, quiet and romantic village.", "bestTime": "Gün batımı", "tips": "Ünlü Mavi Kubbe Kilisesi burada.", "tips_en": "Famous Blue Dome Church is here."},
    {"name": "Caldera Yürüyüş Yolu", "name_en": "Caldera Walking Path", "area": "Fira", "category": "Yürüyüş", "tags": ["yürüyüş", "manzara", "kaldera"], "lat": 36.4300, "lng": 25.4200, "price": "free", "rating": 4.8, "description": "Fira'dan Oia'ya uzanan muhteşem 10 km'lik yürüyüş parkuru.", "description_en": "Stunning 10km walking trail from Fira to Oia.", "bestTime": "Sabah", "tips": "Bol su alın, gölge az.", "tips_en": "Bring plenty of water, little shade."}
]

# BATCH 2: Köyler
batch_2 = [
    {"name": "Megalochori", "name_en": "Megalochori", "area": "Güney", "category": "Tarihi", "tags": ["köy", "otantik", "şarap"], "lat": 36.3853, "lng": 25.4353, "price": "free", "rating": 4.5, "description": "Geleneksel köy, şarap mahzenleri ve Kiklad mimarisi.", "description_en": "Traditional village, wine cellars and Cycladic architecture.", "bestTime": "Gündüz", "tips": "Boutari şaraplığını ziyaret edin.", "tips_en": "Visit Boutari winery."},
    {"name": "Emporio", "name_en": "Emporio", "area": "Güney", "category": "Tarihi", "tags": ["köy", "kale", "ortaçağ"], "lat": 36.3678, "lng": 25.4567, "price": "free", "rating": 4.4, "description": "Ortaçağ köyü, labirent sokaklar ve Goulas kalesi.", "description_en": "Medieval village, labyrinth streets and Goulas castle.", "bestTime": "Gündüz", "tips": "Fotoğraf için en otantik köy.", "tips_en": "Most authentic village for photos."},
    {"name": "Akrotiri Köyü", "name_en": "Akrotiri Village", "area": "Güney", "category": "Tarihi", "tags": ["köy", "kale", "sakin"], "lat": 36.3515, "lng": 25.4100, "price": "free", "rating": 4.3, "description": "Venedik kale kalıntıları ve sakin atmosfer.", "description_en": "Venetian castle ruins and calm atmosphere.", "bestTime": "Gündüz", "tips": "Red Beach'e yakın, birlikte gezin.", "tips_en": "Close to Red Beach, visit together."},
    {"name": "Vlihada Beach", "name_en": "Vlihada Beach", "area": "Güney", "category": "Plaj", "tags": ["plaj", "ay", "doğal"], "lat": 36.3433, "lng": 25.4217, "price": "free", "rating": 4.6, "description": "Ay yüzeyi hissi veren beyaz pomza kayalıkları.", "description_en": "White pumice cliffs giving moon-like feeling.", "bestTime": "Öğleden sonra", "tips": "Doğal güneşlenme imkanı.", "tips_en": "Natural sunbathing opportunity."}
]

# BATCH 3: Ek Şaraphaneler & Gastronomi
batch_3 = [
    {"name": "Boutari Winery", "name_en": "Boutari Winery", "area": "Megalochori", "category": "Deneyim", "tags": ["şarap", "tadım", "tur"], "lat": 36.3850, "lng": 25.4350, "price": "medium", "rating": 4.6, "description": "Yunanistan'ın en ünlü şarap üreticilerinden biri.", "description_en": "One of Greece's most famous wine producers.", "bestTime": "İkindi", "tips": "Tadım turuna katılın.", "tips_en": "Join a tasting tour."},
    {"name": "Sigalas Winery", "name_en": "Sigalas Winery", "area": "Oia", "category": "Deneyim", "tags": ["şarap", "organik", "butik"], "lat": 36.4600, "lng": 25.3650, "price": "medium", "rating": 4.7, "description": "Organik üzümlerden butik şaraplar.", "description_en": "Boutique wines from organic grapes.", "bestTime": "Gün batımı", "tips": "Assyrtiko şarabını kesinlikle deneyin.", "tips_en": "Definitely try Assyrtiko wine."},
    {"name": "Tomatakia (Domates Köftesi)", "name_en": "Tomatakia Shop", "area": "Fira", "category": "Sokak Lezzeti", "tags": ["yerel", "köfte", "domates"], "lat": 36.4175, "lng": 25.4305, "price": "low", "rating": 4.5, "description": "Santorini'nin meşhur domates köftesi.", "description_en": "Santorini's famous tomato fritters.", "bestTime": "Öğle", "tips": "Her yerde deneyin ama yerel tavernalar en iyisi.", "tips_en": "Try everywhere but local taverns are best."},
    {"name": "Fava Restaurant", "name_en": "Fava Restaurant", "area": "Fira", "category": "Restoran", "tags": ["yerel", "geleneksel", "fava"], "lat": 36.4170, "lng": 25.4310, "price": "medium", "rating": 4.5, "description": "Santorini'nin ünlü fava yemeği burada en iyi.", "description_en": "Santorini's famous fava dish is best here.", "bestTime": "Akşam", "tips": "Fava ezme ve caper salatası deneyin.", "tips_en": "Try fava puree and caper salad."}
]

# BATCH 4: Ek Aktiviteler
batch_4 = [
    {"name": "Eşek Turu", "name_en": "Donkey Ride", "area": "Fira", "category": "Deneyim", "tags": ["eşek", "geleneksel", "liman"], "lat": 36.4160, "lng": 25.4280, "price": "medium", "rating": 4.2, "description": "Fira limanından şehre geleneksel eşek yolculuğu.", "description_en": "Traditional donkey ride from Fira port to town.", "bestTime": "Sabah", "tips": "Hayvanlara iyi davranılması için seçici olun.", "tips_en": "Be selective for good animal treatment."},
    {"name": "Teleferik Fira", "name_en": "Fira Cable Car", "area": "Fira", "category": "Deneyim", "tags": ["teleferik", "manzara", "liman"], "lat": 36.4155, "lng": 25.4270, "price": "low", "rating": 4.6, "description": "Cruise limanından Fira'ya teleferik.", "description_en": "Cable car from cruise port to Fira.", "bestTime": "Gündüz", "tips": "Cruise gemilerinden önce gidin, sıra çok uzuyor.", "tips_en": "Go before cruise ships, lines get very long."},
    {"name": "Scuba Diving Santorini", "name_en": "Scuba Diving Santorini", "area": "Çeşitli", "category": "Deneyim", "tags": ["dalış", "sualtı", "volkanik"], "lat": 36.4000, "lng": 25.4500, "price": "high", "rating": 4.7, "description": "Volkanik oluşumlar arasında tüplü dalış.", "description_en": "Scuba diving among volcanic formations.", "bestTime": "Yaz", "tips": "Deneyimli dalıcılar için özel noktalar.", "tips_en": "Special spots for experienced divers."},
    {"name": "Jet Ski Tour", "name_en": "Jet Ski Tour", "area": "Perissa", "category": "Deneyim", "tags": ["jet ski", "macera", "deniz"], "lat": 36.3550, "lng": 25.4780, "price": "high", "rating": 4.5, "description": "Kaldera ve ada çevresinde jet ski turu.", "description_en": "Jet ski tour around caldera and island.", "bestTime": "Öğle", "tips": "Önceden rezervasyon yapın.", "tips_en": "Book in advance."}
]

# BATCH 5: Alışveriş & Kafeler
batch_5 = [
    {"name": "Oia Hediyelik Dükkanları", "name_en": "Oia Gift Shops", "area": "Oia", "category": "Alışveriş", "tags": ["hediyelik", "sanat", "el işi"], "lat": 36.4618, "lng": 25.3750, "price": "variable", "rating": 4.4, "description": "El yapımı mücevher, seramik ve sanat eserleri.", "description_en": "Handmade jewelry, ceramics and artwork.", "bestTime": "Gündüz", "tips": "Pazarlık yapmayı deneyin.", "tips_en": "Try to bargain."},
    {"name": "Kira Thira Jazz Bar", "name_en": "Kira Thira Jazz Bar", "area": "Fira", "category": "Bar", "tags": ["jazz", "bar", "gece"], "lat": 36.4165, "lng": 25.4310, "price": "medium", "rating": 4.6, "description": "Ada'nın en eski ve en iyi jazz barı.", "description_en": "Island's oldest and best jazz bar.", "bestTime": "Gece", "tips": "Canlı müzik için hafta sonu gelin.", "tips_en": "Come weekends for live music."},
    {"name": "Mama Thira", "name_en": "Mama Thira", "area": "Fira", "category": "Kafe", "tags": ["kafe", "brunch", "görünüm"], "lat": 36.4170, "lng": 25.4300, "price": "medium", "rating": 4.5, "description": "Kaldera manzaralı kahvaltı ve brunch.", "description_en": "Breakfast and brunch with caldera view.", "bestTime": "Sabah", "tips": "Erken rezervasyon yapın.", "tips_en": "Book early."},
    {"name": "Palia Kameni Cocktail Bar", "name_en": "Palia Kameni Cocktail Bar", "area": "Fira", "category": "Bar", "tags": ["kokteyl", "manzara", "akşam"], "lat": 36.4168, "lng": 25.4295, "price": "high", "rating": 4.7, "description": "Kaldera kenarında premium kokteyller.", "description_en": "Premium cocktails at caldera edge.", "bestTime": "Gün batımı", "tips": "Gün batımı saatlerinde çok kalabalık.", "tips_en": "Very crowded at sunset hours."}
]

def enrich():
    filepath = 'assets/cities/santorini.json'
    all_new = batch_1 + batch_2 + batch_3 + batch_4 + batch_5
    
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
