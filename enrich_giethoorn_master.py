import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Giethoorn Netherlands", f"{place_name} Giethoorn", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:10000@52.7397,6.0772"
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

# BATCH 1: Çevre Köyler (Sakin Alternatifler)
batch_1 = [
    {"name": "Dwarsgracht", "name_en": "Dwarsgracht", "area": "Çevre", "category": "Köy", "tags": ["köy", "sakin", "kanal"], "lat": 52.7200, "lng": 6.0600, "price": "free", "rating": 4.8, "description": "Giethoorn'un kalabalığından uzakta, aynı güzellikte ama çok daha sakin bir köy.", "description_en": "Away from Giethoorn crowds, equally beautiful but much quieter village.", "bestTime": "Gündüz", "tips": "Bisikletle veya tekneyle ulaşım çok keyifli.", "tips_en": "Very pleasant to reach by bike or boat."},
    {"name": "Kalenberg", "name_en": "Kalenberg", "area": "Weerribben", "category": "Köy", "tags": ["köy", "doğa", "saz"], "lat": 52.7800, "lng": 5.9500, "price": "free", "rating": 4.7, "description": "Milli parkın kalbinde, sazlıkların arasında gizlenmiş büyüleyici bir köy.", "description_en": "Charming village hidden among reeds in the heart of the national park.", "bestTime": "Gündüz", "tips": "Kano kiralayıp sazlıkların arasında kaybolun.", "tips_en": "Rent a canoe and get lost among the reeds."},
    {"name": "Wanneperveen", "name_en": "Wanneperveen", "area": "Çevre", "category": "Köy", "tags": ["köy", "göl", "tarım"], "lat": 52.7000, "lng": 6.1300, "price": "free", "rating": 4.6, "description": "Uzun ve şerit şeklindeki tarihi turba köyü.", "description_en": "Long, ribbon-shaped historic peat village.", "bestTime": "Gündüz", "tips": "Koyun peyniri yapan çiftlikleri ziyaret edin.", "tips_en": "Visit farms making sheep cheese."},
    {"name": "Blokzijl", "name_en": "Blokzijl", "area": "Çevre", "category": "Liman", "tags": ["liman", "tarihi", "deniz"], "lat": 52.7300, "lng": 5.9600, "price": "free", "rating": 4.7, "description": "Eski bir Zuiderzee liman kasabası, tarihi kilit havuzuyla ünlü.", "description_en": "Old Zuiderzee harbor town, famous for its historic lock basin.", "bestTime": "Öğle", "tips": "Liman kenarında Michelin yıldızlı 'Kaatje bij de Sluis' var.", "tips_en": "There is Michelin starred 'Kaatje bij de Sluis' by the harbor."}
]

# BATCH 2: Aktiviteler & Doğa
batch_2 = [
    {"name": "E-Chopper Rental", "name_en": "E-Chopper Rental", "area": "Giethoorn", "category": "Deneyim", "tags": ["scooter", "elektrikli", "eğlence"], "lat": 52.7420, "lng": 6.0850, "price": "medium", "rating": 4.6, "description": "Kasabayı ve milli parkı sessiz elektrikli chopper motorlarla keşfedin.", "description_en": "Explore the town and national park with silent electric choppers.", "bestTime": "Gündüz", "tips": "Ehliyet gereklidir, önceden kontrol edin.", "tips_en": "Driving license required, check beforehand."},
    {"name": "Weerribben-Wieden Kano Rotaları", "name_en": "Canoe Routes", "area": "Milli Park", "category": "Deneyim", "tags": ["kano", "spor", "doğa"], "lat": 52.7500, "lng": 6.0900, "price": "medium", "rating": 4.8, "description": "Avrupa'nın en güzel kano rotalarından bazıları burada.", "description_en": "Some of Europe's most beautiful canoe routes are here.", "bestTime": "Sabah", "tips": "Renkli okları takip ederek rotada kalın.", "tips_en": "Stay on route by following colored arrows."},
    {"name": "Uitkijktoren Woldberg", "name_en": "Woldberg Watchtower", "area": "Steenwijk", "category": "Manzara", "tags": ["kule", "panaroma", "orman"], "lat": 52.7700, "lng": 6.1000, "price": "free", "rating": 4.5, "description": "24 metre yüksekliğinde, bölgeye hakim modern gözetleme kulesi.", "description_en": "24m high modern watchtower dominating the region.", "bestTime": "Gündüz", "tips": "Açık havada Giethoorn kanallarını görebilirsiniz.", "tips_en": "You can see Giethoorn canals on a clear day."}
]

# BATCH 3: Restoranlar
batch_3 = [
    {"name": "De Rietstulp", "name_en": "De Rietstulp", "area": "Merkez", "category": "Restoran", "tags": ["yerel", "saz çatı", "inek"], "lat": 52.7400, "lng": 6.0800, "price": "medium", "rating": 4.4, "description": "Geleneksel çiftlik atmosferinde yemek deneyimi.", "description_en": "Dining experience in traditional farm atmosphere.", "bestTime": "Akşam", "tips": "Yerel 'Gieters' spesiyalitelerini sorun.", "tips_en": "Ask for local 'Gieters' specialties."},
    {"name": "Ristorante Fratelli", "name_en": "Fratelli", "area": "Merkez", "category": "Restoran", "tags": ["italyan", "kanal", "romantik"], "lat": 52.7380, "lng": 6.0790, "price": "medium", "rating": 4.5, "description": "Kanal kenarında kaliteli İtalyan mutfağı.", "description_en": "Quality Italian cuisine by the canal.", "bestTime": "Akşam", "tips": "Tiramisu çok başarılı.", "tips_en": "Tiramisu is very successful."},
    {"name": "Kaatje bij de Sluis", "name_en": "Kaatje bij de Sluis", "area": "Blokzijl", "category": "Restoran", "tags": ["michelin", "gurme", "deniz"], "lat": 52.7305, "lng": 5.9605, "price": "high", "rating": 4.7, "description": "Tarihi kilit havuzunun yanında Michelin yıldızlı restoran.", "description_en": "Michelin starred restaurant next to historic lock basin.", "bestTime": "Öğle", "tips": "Rezervasyon şart.", "tips_en": "Reservation required."},
    {"name": "Canal Grande", "name_en": "Canal Grande", "area": "Merkez", "category": "Restoran", "tags": ["ızgara", "teras", "merkez"], "lat": 52.7390, "lng": 6.0810, "price": "medium", "rating": 4.3, "description": "Geniş terasıyla kanal manzaralı ızgara yemekleri.", "description_en": "Grilled dishes with canal view from large terrace.", "bestTime": "Öğle", "tips": "Kalabalık gruplar için uygundur.", "tips_en": "Suitable for large groups."}
]

def enrich():
    filepath = 'assets/cities/giethoorn.json'
    all_new = batch_1 + batch_2 + batch_3
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('(', '').replace(')', '').replace('ë', 'e')
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
