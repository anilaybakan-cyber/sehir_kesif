import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Hallstatt Austria", f"{place_name} Hallstatt", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:10000@47.5622,13.6493"
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

# BATCH 1: Hallstatt Klasikleri
batch_1 = [
    {"name": "Skywalk Hallstatt", "name_en": "Skywalk Hallstatt", "area": "Salzberg", "category": "Manzara", "tags": ["panorama", "unesco", "yüksek"], "lat": 47.5630, "lng": 13.6400, "price": "free", "rating": 4.8, "description": "Köyün ve gölün kuşbakışı manzarasını sunan, uçurumun kenarındaki platform.", "description_en": "Platform on the edge of the cliff offering a bird's eye view of the village and lake.", "bestTime": "Sabah", "tips": "Öğleden sonra güneş karşıdan gelir, fotoğraf için sabah ideal.", "tips_en": "Sun is opposite in the afternoon, morning is ideal for photos."},
    {"name": "Salzwelten Hallstatt", "name_en": "Hallstatt Salt Mine", "area": "Salzberg", "category": "Müze", "tags": ["maden", "kaydırak", "tarih"], "lat": 47.5650, "lng": 13.6380, "price": "high", "rating": 4.7, "description": "Dünyanın en eski tuz madeni. Yeraltı kaydıraklarıyla eğlenceli bir tur.", "description_en": "World's oldest salt mine. Fun tour with underground slides.", "bestTime": "Gündüz", "tips": "İçerisi soğuktur, kalın giyinin.", "tips_en": "It is cold inside, dress warmly."},
    {"name": "Hallstatt Postcard Viewpoint", "name_en": "Classic Viewpoint", "area": "Kuzey", "category": "Manzara", "tags": ["ikonik", "fotoğraf", "göl"], "lat": 47.5645, "lng": 13.6499, "price": "free", "rating": 4.9, "description": "Hallstatt'ın o meşhur kartpostal fotoğrafının çekildiği nokta.", "description_en": "The spot where that famous postcard photo of Hallstatt is taken.", "bestTime": "Sabah", "tips": "Çok kalabalıktır, erken gidin ve sessiz olun.", "tips_en": "Very crowded, go early and be quiet."},
    {"name": "Marktplatz Hallstatt", "name_en": "Market Square", "area": "Merkez", "category": "Meydan", "tags": ["tarihi", "renkli", "çeşme"], "lat": 47.5620, "lng": 13.6490, "price": "free", "rating": 4.6, "description": "Çiçeklerle süslü evlerle çevrili, tarihi pazar meydanı.", "description_en": "Historic market square surrounded by flower-adorned houses.", "bestTime": "Gündüz", "tips": "Noel zamanı burada kurulan pazar çok güzeldir.", "tips_en": "The market set up here at Christmas is beautiful."},
    {"name": "Beinhaus", "name_en": "Bone House", "area": "Mezarlık", "category": "Tarihi", "tags": ["kemik", "ilginç", "gelenek"], "lat": 47.5635, "lng": 13.6495, "price": "low", "rating": 4.5, "description": "Boyalı kafataslarının sergilendiği, 12. yüzyıldan kalma kemik evi.", "description_en": "12th-century bone house exhibiting painted skulls.", "bestTime": "Gündüz", "tips": "Saygılı olunması gereken, ilginç bir kültürel miras.", "tips_en": "An interesting cultural heritage that requires respect."}
]

# BATCH 2: Doğa ve Çevre (Dachstein & Obertraun)
batch_2 = [
    {"name": "5 Fingers", "name_en": "5 Fingers", "area": "Dachstein", "category": "Manzara", "tags": ["adrenalin", "alp", "buzul"], "lat": 47.5300, "lng": 13.6900, "price": "free", "rating": 4.9, "description": "400 metre boşluğa uzanan, el şeklindeki 5 parmaklı seyir terası.", "description_en": "Hand-shaped 5-finger viewing terrace extending over 400 meters of void.", "bestTime": "Gündüz", "tips": "Teleferikle (Dachstein Krippenstein) çıkılır.", "tips_en": "Reached by cable car (Dachstein Krippenstein)."},
    {"name": "Dachstein Giant Ice Cave", "name_en": "Giant Ice Cave", "area": "Dachstein", "category": "Mağara", "tags": ["buz", "doğa", "soğuk"], "lat": 47.5350, "lng": 13.7000, "price": "high", "rating": 4.7, "description": "Devasa buz kütleleri ve donmuş şelalelerle dolu büyüleyici mağara.", "description_en": "Fascinating cave full of huge ice masses and frozen waterfalls.", "bestTime": "Gündüz", "tips": "Yazın bile sıcaklık eksilerdedir, mont şart.", "tips_en": "Temperature is below zero even in summer, coat is a must."},
    {"name": "Waldbachstrub Waterfall", "name_en": "Waldbachstrub Waterfall", "area": "Echern", "category": "Doğa", "tags": ["şelale", "yürüyüş", "orman"], "lat": 47.5500, "lng": 13.6300, "price": "free", "rating": 4.6, "description": "Echern Vadisi'nde, orman içinde gürül gürül akan şelale.", "description_en": "Roaring waterfall in the forest in Echern Valley.", "bestTime": "Gündüz", "tips": "Romantik Ressamlar Yolu (Malerweg) üzerinden gidin.", "tips_en": "Go via the Romantic Painters' Path (Malerweg)."},
    {"name": "Lake Hallstatt Boat Rental", "name_en": "Boat Rental", "area": "Göl", "category": "Aktivite", "tags": ["tekne", "kuğu", "elektrikli"], "lat": 47.5610, "lng": 13.6480, "price": "medium", "rating": 4.5, "description": "Elektrikli teknelerle gölde sessiz bir tur.", "description_en": "Silent tour on the lake with electric boats.", "bestTime": "Gün batımı", "tips": "Kuğu şeklindeki pedallı botlar popülerdir.", "tips_en": "Swan-shaped pedal boats are popular."}
]

# BATCH 3: Yeme & İçme
batch_3 = [
    {"name": "Seewirt Zauner", "name_en": "Seewirt Zauner", "area": "Merkez", "category": "Restoran", "tags": ["balık", "yerel", "tarihi"], "lat": 47.5625, "lng": 13.6492, "price": "medium", "rating": 4.6, "description": "Gölden taze tutulan 'Reinanke' balığı burada yenir.", "description_en": "Freshly caught 'Reinanke' fish from the lake is eaten here.", "bestTime": "Akşam", "tips": "Izgara Reinanke balığını mutlaka deneyin.", "tips_en": "Must try the grilled Reinanke fish."},
    {"name": "Brauhaus", "name_en": "Brauhaus", "area": "Merkez", "category": "Restoran", "tags": ["bira", "schnitzel", "bahçe"], "lat": 47.5615, "lng": 13.6485, "price": "medium", "rating": 4.4, "description": "Göl kenarında, asırlık kestane ağaçları altında yemek.", "description_en": "Dining under centuries-old chestnut trees by the lake.", "bestTime": "Öğle", "tips": "Porsiyonlar büyüktür.", "tips_en": "Portions are large."},
    {"name": "Café Derbl", "name_en": "Café Derbl", "area": "Marktplatz", "category": "Kafe", "tags": ["tatlı", "kahve", "meydan"], "lat": 47.5621, "lng": 13.6491, "price": "medium", "rating": 4.3, "description": "Meydanı izleyerek kahve ve apfelstrudel keyfi.", "description_en": "Enjoying coffee and apfelstrudel while watching the square.", "bestTime": "Öğle", "tips": "Ev yapımı dondurmaları güzeldir.", "tips_en": "Their homemade ice creams are good."}
]

def enrich():
    filepath = 'assets/cities/hallstatt.json'
    all_new = batch_1 + batch_2 + batch_3
    
    # Load existing data (likely empty)
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            # Eğer highlights anahtarı yoksa veya boşsa başlat
            if 'highlights' not in data:
                data['highlights'] = []
    except (FileNotFoundError, json.JSONDecodeError):
        # Dosya yoksa veya bozuksa temel yapıyı oluştur
        data = {
          "city": "Hallstatt",
          "country": "Austria",
          "coordinates": { "lat": 47.5622, "lng": 13.6493 },
          "highlights": []
        }

    print(f"Loaded {len(data['highlights'])} places.")
    
    existing_names = {p['name'].lower() for p in data['highlights']}
    places_to_add = []
    
    for place in all_new:
        if place['name'].lower() in existing_names:
            print(f"Skip: {place['name']}")
            continue
        print(f"Processing: {place['name']}")
        
        # ID oluşturma
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('ä', 'a').replace('ö', 'o').replace('ü', 'u')
        
        # Fotoğraf çekme
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        
        # Eksik alanları tamamlama
        place['distanceFromCenter'] = place.get('distanceFromCenter', 0.5)
        
        places_to_add.append(place)
        time.sleep(0.3)
    
    data['highlights'].extend(places_to_add)
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places. Total: {len(data['highlights'])}")

if __name__ == "__main__":
    enrich()
