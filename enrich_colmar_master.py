import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Colmar France", f"{place_name} Alsace", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:10000@48.0794,7.3585"
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

# BATCH 1: Çevredeki Köyler (Alsace'ın İncileri)
batch_1 = [
    {"name": "Eguisheim", "name_en": "Eguisheim Village", "area": "Çevre", "category": "Köy", "tags": ["köy", "çiçek", "şarap"], "lat": 48.0440, "lng": 7.3070, "price": "free", "rating": 4.9, "description": "Fransa'nın en güzel köyü seçilen, daire şeklindeki sokaklarıyla masalsı köy.", "description_en": "Fairytale village with circular streets, voted France's most beautiful village.", "bestTime": "Gündüz", "tips": "Colmar'a sadece 7 km, bisikletle bile gidilebilir.", "tips_en": "Only 7 km from Colmar, accessible even by bike."},
    {"name": "Riquewihr", "name_en": "Riquewihr", "area": "Çevre", "category": "Köy", "tags": ["köy", "tarihi", "surlar"], "lat": 48.1660, "lng": 7.2970, "price": "free", "rating": 4.8, "description": "Bağların arasında zamanın durduğu, surlarla çevrili Ortaçağ köyü.", "description_en": "Walled medieval village surrounded by vineyards where time stands still.", "bestTime": "Gündüz", "tips": "Noel dükkanı 'Féerie de Noël' yıl boyu açık.", "tips_en": "Christmas shop 'Féerie de Noël' is open year-round."},
    {"name": "Kaysersberg", "name_en": "Kaysersberg", "area": "Çevre", "category": "Köy", "tags": ["köy", "kale", "nehir"], "lat": 48.1380, "lng": 7.2640, "price": "free", "rating": 4.8, "description": "Weiss nehri kıyısında, tepesinde kalesi olan büyüleyici kasaba.", "description_en": "Charming town on the Weiss river with a castle on top.", "bestTime": "Gündüz", "tips": "Köprüden kale manzarası muhteşem.", "tips_en": "View of the castle from the bridge is magnificent."},
    {"name": "Ribeauvillé", "name_en": "Ribeauville", "area": "Çevre", "category": "Köy", "tags": ["köy", "üç kale", "festival"], "lat": 48.1950, "lng": 7.3190, "price": "free", "rating": 4.7, "description": "Tepesinde üç kale harabesi bulunan tarihi şarap rotası köyü.", "description_en": "Historic wine route village with three castle ruins on top.", "bestTime": "Gündüz", "tips": "Pfifferdaj (Fiddlers' Festival) eylül ayında.", "tips_en": "Pfifferdaj (Fiddlers' Festival) is in September."}
]

# BATCH 2: Colmar İçi Ekstra Yerler
batch_2 = [
    {"name": "Grand Rue", "name_en": "Main Street", "area": "Merkez", "category": "Alışveriş", "tags": ["cadde", "tarihi", "yürüyüş"], "lat": 48.0770, "lng": 7.3575, "price": "free", "rating": 4.6, "description": "Colmar'ın ana caddesi, tarihi binalar ve dükkanlarla dolu.", "description_en": "Colmar's main street, full of historic buildings and shops.", "bestTime": "Gündüz", "tips": "Noel zamanı süslemeler büyüleyici.", "tips_en": "Christmas decorations are fascinating."},
    {"name": "Parc du Champ de Mars", "name_en": "Field of Mars Park", "area": "Merkez", "category": "Park", "tags": ["park", "piknik", "heykeller"], "lat": 48.0730, "lng": 7.3520, "price": "free", "rating": 4.5, "description": "Şehrin en büyük yeşil alanı, dinlenmek için ideal.", "description_en": "City's largest green space, ideal for relaxing.", "bestTime": "İkindi", "tips": "Atlıkarınca çocuklar için harika.", "tips_en": "Carousel is great for kids."},
    {"name": "Place des Dominicains", "name_en": "Dominicans Square", "area": "Merkez", "category": "Meydan", "tags": ["meydan", "kilise", "pazar"], "lat": 48.0785, "lng": 7.3575, "price": "free", "rating": 4.6, "description": "Dominikan Kilisesi'nin önündeki zarif meydan.", "description_en": "Elegant square in front of the Dominican Church.", "bestTime": "Akşam", "tips": "Noel pazarının en güzel kurulduğu yerlerden biri.", "tips_en": "One of the best places for Christmas market."},
    {"name": "Ancienne Douane (Koïfhus)", "name_en": "Old Customs House", "area": "Merkez", "category": "Tarihi", "tags": ["bina", "çatı", "gümrük"], "lat": 48.0755, "lng": 7.3585, "price": "free", "rating": 4.7, "description": "Renkli kiremitli çatısıyla ünlü eski gümrük binası.", "description_en": "Old customs house famous for its colorful tiled roof.", "bestTime": "Gündüz", "tips": "İç avlusu fotoğraf için çok güzel.", "tips_en": "Inner courtyard is very nice for photos."}
]

# BATCH 3: Restoranlar & Gastronomi
batch_3 = [
    {"name": "Sézanne", "name_en": "Sezanne", "area": "Merkez", "category": "Restoran", "tags": ["bistrot", "taze", "yerel"], "lat": 48.0760, "lng": 7.3560, "price": "medium", "rating": 4.7, "description": "Market tarzı bistro, taze ve günlük değişen menü.", "description_en": "Market-style bistro, fresh and daily changing menu.", "bestTime": "Öğle", "tips": "Yer bulmak zordur, erken gidin.", "tips_en": "Hard to find a seat, go early."},
    {"name": "Fortwenger", "name_en": "Fortwenger Gingerbread", "area": "Merkez", "category": "Alışveriş", "tags": ["zencefil", "kurabiye", "hediyelik"], "lat": 48.0775, "lng": 7.3580, "price": "medium", "rating": 4.8, "description": "Alsace'ın meşhur zencefilli kurabiyelerinin (Pain d'épices) adresi.", "description_en": "Address for Alsace's famous gingerbread (Pain d'épices).", "bestTime": "Gündüz", "tips": "Farklı şekillerdeki kurabiyeler harika hediye.", "tips_en": "Cookies in different shapes are great gifts."},
    {"name": "Vins d'Alsace Robert Karcher", "name_en": "Robert Karcher Wines", "area": "Merkez", "category": "Deneyim", "tags": ["şarap", "tadım", "mahzen"], "lat": 48.0765, "lng": 7.3555, "price": "medium", "rating": 4.8, "description": "Eski şehir merkezinde, 1602'den kalma binada şarap tadımı.", "description_en": "Wine tasting in a 1602 building in old town center.", "bestTime": "İkindi", "tips": "Gewurztraminer şarabını mutlaka deneyin.", "tips_en": "Must try Gewurztraminer wine."},
    {"name": "Caveau Saint-Pierre", "name_en": "Caveau Saint-Pierre", "area": "Petite Venise", "category": "Restoran", "tags": ["romantik", "kanal", "geleneksel"], "lat": 48.0740, "lng": 7.3590, "price": "medium", "rating": 4.5, "description": "Kanal kenarında, yarı ahşap bir evde romantik yemek.", "description_en": "Romantic dinner in a half-timbered house by the canal.", "bestTime": "Akşam", "tips": "Tarte Flambée (Flammekueche) çok iyi.", "tips_en": "Tarte Flambée (Flammekueche) is very good."},
     {"name": "Jadis et Gourmande", "name_en": "Jadis et Gourmande", "area": "Merkez", "category": "Kafe", "tags": ["çay", "oyuncak", "kahvaltı"], "lat": 48.0770, "lng": 7.3570, "price": "medium", "rating": 4.6, "description": "Oyuncak ayılarla dolu masalsı bir çay salonu.", "description_en": "Fairytale tea room full of teddy bears.", "bestTime": "Sabah", "tips": "Sıcak çikolatası çok yoğun ve lezzetli.", "tips_en": "Hot chocolate is very thick and delicious."}
]

def enrich():
    filepath = 'assets/cities/colmar.json'
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('(', '').replace(')', '').replace('é', 'e').replace('à', 'a')
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
