import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Zermatt Switzerland", f"{place_name} Zermatt", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:20000@46.0207,7.7491"
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

# BATCH 1: Matterhorn & Seyir Noktaları
batch_1 = [
    {"name": "Matterhorn", "name_en": "Matterhorn", "area": "Zermatt", "category": "Manzara", "tags": ["dağ", "ikonik", "alpler"], "lat": 45.9766, "lng": 7.6586, "price": "free", "rating": 5.0, "description": "Dünyanın en ünlü dağ siluetidir. 4.478 metre yüksekliğinde İsviçre-İtalya sınırında Toblerone'un amblemi.", "description_en": "World's most famous mountain silhouette. 4,478m at Swiss-Italian border, Toblerone's emblem.", "bestTime": "Gün doğumu", "tips": "En iyi fotoğraf için Riffelsee'ye çıkın.", "tips_en": "Go to Riffelsee for best photo."},
    {"name": "Matterhorn Glacier Paradise", "name_en": "Matterhorn Glacier Paradise", "area": "Klein Matterhorn", "category": "Manzara", "tags": ["buzul", "teleferik", "panorama"], "lat": 45.9377, "lng": 7.7287, "price": "high", "rating": 4.9, "description": "Avrupa'nın teleferikle ulaşılabilen en yüksek noktası, 3.883 metre.", "description_en": "Europe's highest cable car station at 3,883m.", "bestTime": "Öğle", "tips": "Buz sarayı ve buzul kayağı yapabilirsiniz.", "tips_en": "Ice palace and glacier skiing available."},
    {"name": "Gornergrat", "name_en": "Gornergrat", "area": "Zermatt", "category": "Manzara", "tags": ["tren", "panorama", "observatoryum"], "lat": 45.9833, "lng": 7.7853, "price": "high", "rating": 4.9, "description": "Dişli tren ile ulaşılan 3.089 metre yükseklikteki seyir terası.", "description_en": "Viewing terrace at 3,089m reached by cogwheel train.", "bestTime": "Gün doğumu", "tips": "Gün doğumu turu kaçırılmamalı.", "tips_en": "Sunrise tour is a must."},
    {"name": "Riffelsee", "name_en": "Riffelsee Lake", "area": "Gornergrat", "category": "Manzara", "tags": ["göl", "yansıma", "matterhorn"], "lat": 45.9891, "lng": 7.7656, "price": "free", "rating": 4.9, "description": "Matterhorn'un suya yansıdığı efsanevi göl.", "description_en": "Legendary lake where Matterhorn reflects in water.", "bestTime": "Sabah erken", "tips": "Durgun su için sabah erken gidin.", "tips_en": "Go early morning for still water."},
    {"name": "Rothorn Paradise", "name_en": "Rothorn Paradise", "area": "Zermatt", "category": "Manzara", "tags": ["teleferik", "manzara", "yürüyüş"], "lat": 46.0250, "lng": 7.7156, "price": "high", "rating": 4.7, "description": "3.103 metre yükseklikte panoramik manzara noktası.", "description_en": "Panoramic viewpoint at 3,103m.", "bestTime": "Gündüz", "tips": "5 Göl yürüyüşü buradan başlar.", "tips_en": "5 Lakes hike starts from here."},
    {"name": "Sunnegga", "name_en": "Sunnegga", "area": "Zermatt", "category": "Manzara", "tags": ["füniküler", "göl", "aile"], "lat": 46.0089, "lng": 7.7658, "price": "medium", "rating": 4.6, "description": "Aile dostu bölge, yüzme gölü ve Matterhorn manzarası.", "description_en": "Family-friendly area, swimming lake and Matterhorn view.", "bestTime": "İkindi", "tips": "Leisee gölünde yüzebilirsiniz.", "tips_en": "You can swim in Leisee lake."}
]

# BATCH 2: Yürüyüş Rotaları
batch_2 = [
    {"name": "5-Seenweg (Beş Göl Yürüyüşü)", "name_en": "Five Lakes Hike", "area": "Rothorn", "category": "Yürüyüş", "tags": ["yürüyüş", "göl", "manzara"], "lat": 46.0200, "lng": 7.7200, "price": "medium", "rating": 4.9, "description": "Beş muhteşem göl boyunca 9 km'lik orta zorlukta parkur.", "description_en": "Medium difficulty 9km trail along five stunning lakes.", "bestTime": "Yaz", "tips": "Fluhalp'ta öğle yemeği molası verin.", "tips_en": "Stop at Fluhalp for lunch."},
    {"name": "Höhenweg Europaweg", "name_en": "Europaweg Trail", "area": "Zermatt-Grächen", "category": "Yürüyüş", "tags": ["yürüyüş", "köprü", "macera"], "lat": 46.1000, "lng": 7.8000, "price": "free", "rating": 4.8, "description": "Charles Kuonen asma köprüsünü içeren epik 2 günlük rota.", "description_en": "Epic 2-day route including Charles Kuonen suspension bridge.", "bestTime": "Yaz", "tips": "En az 2 gün ayırın.", "tips_en": "Plan at least 2 days."},
    {"name": "Charles Kuonen Asma Köprüsü", "name_en": "Charles Kuonen Bridge", "area": "Randa", "category": "Manzara", "tags": ["köprü", "dünya rekoru", "macera"], "lat": 46.1050, "lng": 7.7950, "price": "free", "rating": 4.8, "description": "Dünyanın en uzun yaya asma köprüsü, 494 metre.", "description_en": "World's longest pedestrian suspension bridge, 494m.", "bestTime": "Gündüz", "tips": "Yükseklik korkusu olanlar için zorlayıcı.", "tips_en": "Challenging for those with height fear."},
    {"name": "Matterhorn Trail", "name_en": "Matterhorn Trail", "area": "Schwarzsee", "category": "Yürüyüş", "tags": ["yürüyüş", "matterhorn", "yakın"], "lat": 45.9860, "lng": 7.7050, "price": "free", "rating": 4.7, "description": "Matterhorn'a en yakın yürüyüş, Schwarzsee'den başlar.", "description_en": "Closest hike to Matterhorn, starts from Schwarzsee.", "bestTime": "Yaz", "tips": "Dönüşte Hörnlihütte'de kahve için durun.", "tips_en": "Stop at Hörnlihütte for coffee on return."}
]

# BATCH 3: Müzeler & Kültür
batch_3 = [
    {"name": "Matterhorn Müzesi (Zermatlantis)", "name_en": "Matterhorn Museum", "area": "Merkez", "category": "Müze", "tags": ["müze", "tarih", "dağcılık"], "lat": 46.0217, "lng": 7.7478, "price": "medium", "rating": 4.6, "description": "Matterhorn'un ilk tırmanışını ve Zermatt tarihini anlatan yeraltı müzesi.", "description_en": "Underground museum telling first Matterhorn ascent and Zermatt history.", "bestTime": "Gündüz", "tips": "Yağmurlu günler için ideal.", "tips_en": "Ideal for rainy days."},
    {"name": "St. Mauritius Kilisesi", "name_en": "St. Mauritius Church", "area": "Merkez", "category": "Tarihi", "tags": ["kilise", "matterhorn", "manzara"], "lat": 46.0210, "lng": 7.7485, "price": "free", "rating": 4.4, "description": "Matterhorn manzarasıyla ünlü köy kilisesi.", "description_en": "Village church famous for Matterhorn view.", "bestTime": "Sabah", "tips": "Mezarlıkta dağcı anıtları var.", "tips_en": "Mountaineer memorials in cemetery."},
    {"name": "Hinterdorf (Eski Köy)", "name_en": "Hinterdorf Old Village", "area": "Merkez", "category": "Tarihi", "tags": ["eski köy", "ahşap", "geleneksel"], "lat": 46.0205, "lng": 7.7505, "price": "free", "rating": 4.5, "description": "16-17. yüzyıldan kalma otantik ahşap evler.", "description_en": "Authentic wooden houses from 16-17th century.", "bestTime": "Gündüz", "tips": "Fotoğraf için en güzel tarihi bölge.", "tips_en": "Most beautiful historic area for photos."}
]

# BATCH 4: Restoranlar & Kafeler
batch_4 = [
    {"name": "Chez Vrony", "name_en": "Chez Vrony", "area": "Findeln", "category": "Restoran", "tags": ["dağ restoran", "manzara", "gurme"], "lat": 46.0050, "lng": 7.7600, "price": "high", "rating": 4.8, "description": "Matterhorn manzaralı dağ restoranı, gurme mutfak.", "description_en": "Mountain restaurant with Matterhorn view, gourmet cuisine.", "bestTime": "Öğle", "tips": "Rösti kesinlikle deneyin.", "tips_en": "Definitely try their Rösti."},
    {"name": "Zum See", "name_en": "Zum See", "area": "Zum See", "category": "Restoran", "tags": ["dağ restoran", "romantik", "tarihi"], "lat": 45.9900, "lng": 7.7400, "price": "high", "rating": 4.7, "description": "1855'ten kalma tarihi dağ restoranı.", "description_en": "Historic mountain restaurant from 1855.", "bestTime": "Öğle", "tips": "Yürüyüş ile ulaşılır, muhteşem atmosfer.", "tips_en": "Reached by hiking, amazing atmosphere."},
    {"name": "Findlerhof", "name_en": "Findlerhof", "area": "Findeln", "category": "Restoran", "tags": ["dağ restoran", "yerel", "otantik"], "lat": 46.0055, "lng": 7.7610, "price": "medium", "rating": 4.6, "description": "Otantik İsviçre dağ mutfağı.", "description_en": "Authentic Swiss mountain cuisine.", "bestTime": "Öğle", "tips": "Käseschnitte deneyin.", "tips_en": "Try Käseschnitte."},
    {"name": "Whymper Stube", "name_en": "Whymper Stube", "area": "Merkez", "category": "Restoran", "tags": ["fondu", "raclette", "geleneksel"], "lat": 46.0212, "lng": 7.7475, "price": "high", "rating": 4.7, "description": "İlk Matterhorn fatihi Edward Whymper adını taşıyan fondu restoranı.", "description_en": "Fondue restaurant named after first Matterhorn conqueror.", "bestTime": "Akşam", "tips": "Peynir fondusu için en iyi adres.", "tips_en": "Best address for cheese fondue."},
    {"name": "Elsie's Bar", "name_en": "Elsie's Bar", "area": "Merkez", "category": "Bar", "tags": ["bar", "efsane", "istiridye"], "lat": 46.0218, "lng": 7.7485, "price": "high", "rating": 4.5, "description": "Zermatt'ın efsanevi barı, istiridye ve şampanya.", "description_en": "Zermatt's legendary bar, oysters and champagne.", "bestTime": "Akşam", "tips": "Kayak sonrası klasik buluşma noktası.", "tips_en": "Classic meeting point after skiing."},
    {"name": "Brown Cow Pub", "name_en": "Brown Cow Pub", "area": "Merkez", "category": "Bar", "tags": ["pub", "canlı müzik", "gece"], "lat": 46.0215, "lng": 7.7480, "price": "medium", "rating": 4.3, "description": "Canlı müzik ve aprés-ski atmosferi.", "description_en": "Live music and après-ski atmosphere.", "bestTime": "Gece", "tips": "Gece hayatı için en popüler nokta.", "tips_en": "Most popular spot for nightlife."}
]

# BATCH 5: Aktiviteler
batch_5 = [
    {"name": "Kayak & Snowboard", "name_en": "Skiing & Snowboarding", "area": "Zermatt Ski Area", "category": "Deneyim", "tags": ["kayak", "kış", "spor"], "lat": 46.0000, "lng": 7.7500, "price": "high", "rating": 4.9, "description": "360 km pist, yıl boyunca kayak imkanı.", "description_en": "360km slopes, year-round skiing.", "bestTime": "Kış", "tips": "Peak Pass alarak daha uygun fiyata kayak yapın.", "tips_en": "Get Peak Pass for cheaper skiing."},
    {"name": "Igloo Village Zermatt", "name_en": "Igloo Village Zermatt", "area": "Rotenboden", "category": "Deneyim", "tags": ["igloo", "konaklama", "benzersiz"], "lat": 45.9850, "lng": 7.7750, "price": "high", "rating": 4.7, "description": "Buzdan yapılmış otel, kış masalı deneyimi.", "description_en": "Ice hotel, winter fairy tale experience.", "bestTime": "Kış", "tips": "Fondu dahil gece konaklama.", "tips_en": "Overnight with fondue included."},
    {"name": "Gorner Gorge", "name_en": "Gorner Gorge", "area": "Zermatt", "category": "Doğa", "tags": ["boğaz", "su", "doğa"], "lat": 46.0150, "lng": 7.7400, "price": "low", "rating": 4.5, "description": "Buzul suları tarafından oyulmuş muhteşem boğaz.", "description_en": "Magnificent gorge carved by glacier waters.", "bestTime": "Yaz", "tips": "Ahşap köprülerden geçiş.", "tips_en": "Passage through wooden bridges."},
    {"name": "Helicopter Tour", "name_en": "Helicopter Tour", "area": "Zermatt", "category": "Deneyim", "tags": ["helikopter", "panorama", "lüks"], "lat": 46.0200, "lng": 7.7500, "price": "high", "rating": 4.9, "description": "Matterhorn çevresinde helikopter turu.", "description_en": "Helicopter tour around Matterhorn.", "bestTime": "Açık hava", "tips": "4 kişilik grup indirimi mevcut.", "tips_en": "Group discount for 4 people."}
]

# BATCH 6: Alışveriş
batch_6 = [
    {"name": "Bahnhofstrasse", "name_en": "Bahnhofstrasse", "area": "Merkez", "category": "Alışveriş", "tags": ["cadde", "alışveriş", "yeme"], "lat": 46.0207, "lng": 7.7480, "price": "variable", "rating": 4.4, "description": "Ana cadde, dükkanlar ve restoranlar.", "description_en": "Main street, shops and restaurants.", "bestTime": "Akşam", "tips": "Elektrikli taksiler geçiyor, dikkat!", "tips_en": "Electric taxis passing, watch out!"},
    {"name": "Zermatt Spor Dükkanları", "name_en": "Zermatt Sports Shops", "area": "Merkez", "category": "Alışveriş", "tags": ["spor", "kayak", "kıyafet"], "lat": 46.0210, "lng": 7.7475, "price": "high", "rating": 4.3, "description": "Kayak ve outdoor ekipman kiralama/satış.", "description_en": "Ski and outdoor equipment rental/sales.", "bestTime": "Gündüz", "tips": "Kiralama için önceden rezervasyon.", "tips_en": "Book rental in advance."},
    {"name": "Zermatt Souvenirs", "name_en": "Zermatt Souvenirs", "area": "Merkez", "category": "Alışveriş", "tags": ["hediyelik", "çikolata", "saat"], "lat": 46.0208, "lng": 7.7482, "price": "variable", "rating": 4.2, "description": "İsviçre çikolatası, saatler ve hediyelikler.", "description_en": "Swiss chocolate, watches and souvenirs.", "bestTime": "Gündüz", "tips": "Lindt & Toblerone en popüler.", "tips_en": "Lindt & Toblerone most popular."}
]

def enrich():
    filepath = 'assets/cities/zermatt.json'
    all_new = batch_1 + batch_2 + batch_3 + batch_4 + batch_5 + batch_6
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('(', '').replace(')', '').replace('ü', 'u').replace('ö', 'o').replace('ä', 'a')
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
