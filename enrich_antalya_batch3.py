import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Antalya Turkey", f"{place_name} Antalya", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:60000@36.8841,30.7056"
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

# BATCH 15: Son Ek Yerler - Daha Fazla Plaj & Koylar
batch_15 = [
    {"name": "Adrasan Koyu", "name_en": "Adrasan Bay", "area": "Kumluca", "category": "Plaj", "tags": ["koy", "sakin", "doğal"], "distanceFromCenter": 100.0, "lat": 36.3750, "lng": 30.4600, "price": "free", "rating": 4.7, "description": "Sakin ve doğal koy, kalabalıktan uzak.", "description_en": "Calm and natural bay, away from crowds.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Olimpos'a yakın, birlikte gezin.", "tips_en": "Close to Olympos, visit together."},
    {"name": "Sülüklü Göl", "name_en": "Suluklu Lake", "area": "Döşemealtı", "category": "Doğa", "tags": ["göl", "yürüyüş", "doğa"], "distanceFromCenter": 35.0, "lat": 37.0400, "lng": 30.4800, "price": "free", "rating": 4.5, "description": "Dağ gölü etrafında yürüyüş parkuru.", "description_en": "Hiking trail around mountain lake.", "bestTime": "İlkbahar", "bestTime_en": "Spring", "tips": "Yürüyüş ayakkabısı şart.", "tips_en": "Hiking shoes required."},
    {"name": "Bey Dağları Sahil Milli Parkı", "name_en": "Bey Mountains Coastal National Park", "area": "Kemer", "category": "Doğa", "tags": ["milli park", "doğa", "yürüyüş"], "distanceFromCenter": 60.0, "lat": 36.5500, "lng": 30.4500, "price": "low", "rating": 4.7, "description": "Deniz ve dağın buluştuğu milli park.", "description_en": "National park where sea meets mountains.", "bestTime": "İlkbahar", "bestTime_en": "Spring", "tips": "Phaselis buraya dahil.", "tips_en": "Phaselis is included."},
    {"name": "Ölüdeniz Plajı", "name_en": "Oludeniz Beach", "area": "Fethiye", "category": "Plaj", "tags": ["lagün", "mavi", "ikonik"], "distanceFromCenter": 220.0, "lat": 36.5500, "lng": 29.1150, "price": "low", "rating": 4.9, "description": "Türkiye'nin en ünlü mavi lagünü.", "description_en": "Turkey's most famous blue lagoon.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Sabah erken gidin.", "tips_en": "Go early morning."},
    {"name": "Butterfly Valley (Kelebekler Vadisi)", "name_en": "Butterfly Valley", "area": "Fethiye", "category": "Doğa", "tags": ["vadi", "kelebek", "doğa"], "distanceFromCenter": 230.0, "lat": 36.5270, "lng": 29.1100, "price": "medium", "rating": 4.7, "description": "Tekneyle ulaşılan gizli vadi ve plaj.", "description_en": "Hidden valley and beach reached by boat.", "bestTime": "Yaz", "bestTime_en": "Summer", "tips": "Kamp yapılabilir.", "tips_en": "Camping available."},
    {"name": "Saklikent Kanyonu", "name_en": "Saklikent Canyon", "area": "Fethiye", "category": "Doğa", "tags": ["kanyon", "yürüyüş", "su"], "distanceFromCenter": 200.0, "lat": 36.4600, "lng": 29.4000, "price": "low", "rating": 4.6, "description": "Türkiye'nin en uzun ve en derin kanyonu.", "description_en": "Turkey's longest and deepest canyon.", "bestTime": "Yaz", "bestTime_en": "Summer", "tips": "Su ayakkabısı şart.", "tips_en": "Water shoes required."}
]

# BATCH 16: Oteller & Konaklama Bölgeleri
batch_16 = [
    {"name": "Lara Beach Oteller Bölgesi", "name_en": "Lara Beach Hotels Zone", "area": "Lara", "category": "Manzara", "tags": ["otel", "lüks", "sahil"], "distanceFromCenter": 12.0, "lat": 36.8400, "lng": 30.8600, "price": "high", "rating": 4.5, "description": "Lüks all-inclusive otellerin bulunduğu sahil şeridi.", "description_en": "Coastal strip with luxury all-inclusive hotels.", "bestTime": "Yaz", "bestTime_en": "Summer", "tips": "Otel plajları genellikle ücretsiz.", "tips_en": "Hotel beaches usually free."},
    {"name": "Belek Golf Sahası", "name_en": "Belek Golf Course", "area": "Belek", "category": "Deneyim", "tags": ["golf", "spor", "lüks"], "distanceFromCenter": 35.0, "lat": 36.8500, "lng": 31.0500, "price": "high", "rating": 4.7, "description": "Dünya standartlarında golf sahaları.", "description_en": "World-class golf courses.", "bestTime": "İlkbahar", "bestTime_en": "Spring", "tips": "Golf turizmi için Türkiye'nin en iyi bölgesi.", "tips_en": "Turkey's best region for golf tourism."},
    {"name": "Side Sahil Yürüyüşü", "name_en": "Side Beach Promenade", "area": "Manavgat", "category": "Deneyim", "tags": ["yürüyüş", "sahil", "gece"], "distanceFromCenter": 75.0, "lat": 36.7700, "lng": 31.3880, "price": "free", "rating": 4.5, "description": "Antik şehir boyunca sahil yürüyüş yolu.", "description_en": "Beachfront walking path along ancient city.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Akşam yürüyüşü mükemmel.", "tips_en": "Evening walk is perfect."}
]

# BATCH 17: Ek Kafeler & Tatlıcılar
batch_17 = [
    {"name": "Dondurma Dükkanı", "name_en": "Ice Cream Shop", "area": "Kaleiçi", "category": "Tatlı", "tags": ["dondurma", "tatlı", "gösteri"], "distanceFromCenter": 0.2, "lat": 36.8850, "lng": 30.7060, "price": "low", "rating": 4.4, "description": "Maraş dondurması ve gösterili sunum.", "description_en": "Maras ice cream with performative serving.", "bestTime": "İkindi", "bestTime_en": "Afternoon", "tips": "Fıstıklı dondurma en iyisi.", "tips_en": "Pistachio ice cream is best."},
    {"name": "Künefe Evi", "name_en": "Kunefe House", "area": "Kaleiçi", "category": "Tatlı", "tags": ["künefe", "tatlı", "geleneksel"], "distanceFromCenter": 0.2, "lat": 36.8855, "lng": 30.7065, "price": "low", "rating": 4.6, "description": "Geleneksel Antep künefesi.", "description_en": "Traditional Antep kunefe.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Sıcak sıcak yiyin.", "tips_en": "Eat while hot."},
    {"name": "Cafe Terra", "name_en": "Cafe Terra", "area": "Kaleiçi", "category": "Kafe", "tags": ["kafe", "teras", "manzara"], "distanceFromCenter": 0.2, "lat": 36.8830, "lng": 30.7045, "price": "medium", "rating": 4.5, "description": "Deniz manzaralı teras kafe.", "description_en": "Terrace cafe with sea view.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "Gün batımı için erken gidin.", "tips_en": "Go early for sunset."},
    {"name": "Portakal Çiçeği Kahvesi", "name_en": "Orange Blossom Coffee", "area": "Kaleiçi", "category": "Kafe", "tags": ["türk kahvesi", "geleneksel", "fal"], "distanceFromCenter": 0.2, "lat": 36.8845, "lng": 30.7055, "price": "low", "rating": 4.5, "description": "Portakal çiçeği aromalı Türk kahvesi.", "description_en": "Turkish coffee with orange blossom aroma.", "bestTime": "İkindi", "bestTime_en": "Afternoon", "tips": "Kahve falı baktırın.", "tips_en": "Get coffee fortune reading."}
]

# BATCH 18: Ek Tarihi Yerler
batch_18 = [
    {"name": "Letoon Antik Kenti", "name_en": "Letoon Ancient City", "area": "Kaş", "category": "Tarihi", "tags": ["antik", "likya", "unesco"], "distanceFromCenter": 210.0, "lat": 36.3320, "lng": 29.3150, "price": "low", "rating": 4.5, "description": "UNESCO listesinde Likya kutsal alanı.", "description_en": "UNESCO-listed Lycian sanctuary.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Xanthos ile birlikte gezin.", "tips_en": "Visit with Xanthos."},
    {"name": "Patara Antik Kenti", "name_en": "Patara Ancient City", "area": "Kaş", "category": "Tarihi", "tags": ["antik", "likya", "parlamento"], "distanceFromCenter": 200.0, "lat": 36.2720, "lng": 29.3000, "price": "low", "rating": 4.7, "description": "Dünyanın ilk parlamentosunun bulunduğu antik kent.", "description_en": "Ancient city with world's first parliament.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Plaj biletine dahil.", "tips_en": "Included in beach ticket."},
    {"name": "Arykanda Antik Kenti", "name_en": "Arykanda Ancient City", "area": "Kumluca", "category": "Tarihi", "tags": ["antik", "dağ", "tiyatro"], "distanceFromCenter": 120.0, "lat": 36.4850, "lng": 30.0650, "price": "low", "rating": 4.6, "description": "Dağ yamacına kurulu iyi korunmuş antik kent.", "description_en": "Well-preserved ancient city on mountainside.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Daha az turist, daha sessiz.", "tips_en": "Fewer tourists, quieter."},
    {"name": "Limyra Antik Kenti", "name_en": "Limyra Ancient City", "area": "Kumluca", "category": "Tarihi", "tags": ["antik", "likya", "kaya mezar"], "distanceFromCenter": 110.0, "lat": 36.3580, "lng": 30.1800, "price": "free", "rating": 4.4, "description": "Likya kaya mezarları ve tiyatro kalıntıları.", "description_en": "Lycian rock tombs and theater remains.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Ücretsiz giriş.", "tips_en": "Free entry."},
    {"name": "Selge Antik Kenti", "name_en": "Selge Ancient City", "area": "Manavgat", "category": "Tarihi", "tags": ["antik", "dağ", "izole"], "distanceFromCenter": 100.0, "lat": 37.2400, "lng": 31.1300, "price": "free", "rating": 4.5, "description": "Dağlarda gizli, zorlu ulaşımla antik kent.", "description_en": "Hidden ancient city in mountains with challenging access.", "bestTime": "İlkbahar", "bestTime_en": "Spring", "tips": "4x4 araç önerilir.", "tips_en": "4x4 vehicle recommended."}
]

def enrich():
    filepath = 'assets/cities/antalya.json'
    all_new = batch_15 + batch_16 + batch_17 + batch_18
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace('ç', 'c').replace('ğ', 'g').replace('ı', 'i').replace('ö', 'o').replace('ş', 's').replace('ü', 'u').replace('(', '').replace(')', '').replace('&', 'and')
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        places_to_add.append(place)
        time.sleep(0.3)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places. Total: {len(data['highlights'])}")

if __name__ == "__main__":
    enrich()
