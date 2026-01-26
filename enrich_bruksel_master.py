import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Brussels Belgium", f"{place_name} Brussels", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:10000@50.8476,4.3572"
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

# BATCH 1: İkonik Merkez & Tarih
batch_1 = [
    {"name": "Grand Place", "name_en": "Grand Place", "area": "Merkez", "category": "Meydan", "tags": ["unesco", "tarihi", "altın"], "lat": 50.8467, "lng": 4.3524, "price": "free", "rating": 4.9, "description": "Dünyanın en güzel meydanlarından biri; altın süslemeli lonca evleriyle çevrili.", "description_en": "One of the world's most beautiful squares; surrounded by gold-decorated guild houses.", "bestTime": "Gündüz", "tips": "Her iki yılda bir ağustos ayında çiçek halısı seriliyor.", "tips_en": "Flower carpet is laid every two years in August."},
    {"name": "Manneken Pis", "name_en": "Manneken Pis", "area": "Merkez", "category": "Heykel", "tags": ["ikonik", "küçük", "eğlenceli"], "lat": 50.8449, "lng": 4.3500, "price": "free", "rating": 4.3, "description": "Şehrin en ünlü simgesi, işeyen çocuk heykeli. Beklediğinizden küçük olabilir!", "description_en": "The city's most famous symbol, the peeing boy statue. Might be smaller than you expect!", "bestTime": "Gündüz", "tips": "Özel günlerde farklı kostümler giydiriliyor.", "tips_en": "Dressed in different costumes on special days."},
    {"name": "Atomium", "name_en": "Atomium", "area": "Heysel", "category": "Müze", "tags": ["bilim", "manzara", "modern"], "lat": 50.8949, "lng": 4.3414, "price": "high", "rating": 4.6, "description": "1958 Fuarı için yapılan devasa atom modeli. En üst küreden manzara müthiş.", "description_en": "Giant atom model built for 1958 Fair. View from the top sphere is amazing.", "bestTime": "Sabah", "tips": "Biletinizi online alın, sıra çok oluyor.", "tips_en": "Buy tickets online, lines are long."},
    {"name": "Royal Palace of Brussels", "name_en": "Royal Palace", "area": "Kraliyet Parkı", "category": "Saray", "tags": ["kraliyet", "lüks", "yaz"], "lat": 50.8415, "lng": 4.3630, "price": "free", "rating": 4.7, "description": "Belçika Krallığı'nın resmi sarayı. Sadece yaz aylarında ziyarete açık.", "description_en": "Official palace of the Belgian Monarchy. Open to visitors only in summer.", "bestTime": "Gündüz", "tips": "Giriş ücretsizdir ama rezervasyon gerekebilir.", "tips_en": "Entry is free but reservation might be needed."},
    {"name": "Mont des Arts", "name_en": "Mount of the Arts", "area": "Merkez", "category": "Manzara", "tags": ["bahçe", "gün batımı", "fotoğraf"], "lat": 50.8435, "lng": 4.3565, "price": "free", "rating": 4.8, "description": "Brüksel'in en iyi şehir manzarası ve gün batımı noktası.", "description_en": "Best city view and sunset spot in Brussels.", "bestTime": "Gün batımı", "tips": "Müzisyenler genellikle burada çalar, atmosfer harikadır.", "tips_en": "Musicians often play here, atmosphere is great."}
]

# BATCH 2: Sanat, Müze & Gizli Köşeler
batch_2 = [
    {"name": "Magritte Museum", "name_en": "Magritte Museum", "area": "Kraliyet Parkı", "category": "Müze", "tags": ["sanat", "sürrealizm", "magritte"], "lat": 50.8427, "lng": 4.3582, "price": "medium", "rating": 4.7, "description": "René Magritte'in sürrealist eserlerinin sergilendiği etkileyici müze.", "description_en": "Impressive museum exhibiting René Magritte's surrealist works.", "bestTime": "Öğle", "tips": "Sesli rehber almanızı öneririm, tabloları anlamak için önemli.", "tips_en": "I recommend getting an audio guide, essential to understand the paintings."},
    {"name": "Galeries Royales Saint-Hubert", "name_en": "Royal Gallery", "area": "Merkez", "category": "Alışveriş", "tags": ["pasaj", "çikolata", "ləks"], "lat": 50.8466, "lng": 4.3556, "price": "free", "rating": 4.6, "description": "Avrupa'nın en eski alışveriş pasajlarından biri, çikolata kokusuyla dolu.", "description_en": "One of Europe's oldest shopping arcades, filled with the smell of chocolate.", "bestTime": "Akşam", "tips": "Sadece yürümek bile keyifli, vitrinler sanat eseri gibi.", "tips_en": "Just walking is enjoyable, windows are like art pieces."},
    {"name": "Jeanneke Pis", "name_en": "Jeanneke Pis", "area": "Impasse de la Fidélité", "category": "Heykel", "tags": ["komik", "gizli", "meydan okuma"], "lat": 50.8485, "lng": 4.3540, "price": "free", "rating": 4.0, "description": "Manneken Pis'in daha az bilinen kız kardeşi. Bir çıkmaz sokakta saklı.", "description_en": "Manneken Pis's lesser-known sister. Hidden in a dead-end alley.", "bestTime": "Gündüz", "tips": "Delirium Café'nin hemen karşısındaki çıkmaz sokakta.", "tips_en": "In the dead-end alley right across Delirium Café."},
    {"name": "Horta Museum", "name_en": "Horta Museum", "area": "Saint-Gilles", "category": "Müze", "tags": ["art nouveau", "mimari", "tasarım"], "lat": 50.8240, "lng": 4.3550, "price": "medium", "rating": 4.7, "description": "Art Nouveau mimarisinin babası Victor Horta'nın evi ve atölyesi.", "description_en": "House and studio of Victor Horta, father of Art Nouveau architecture.", "bestTime": "Öğle", "tips": "Sınırlı kapasite nedeniyle önceden bilet alın.", "tips_en": "Buy tickets in advance due to limited capacity."},
    {"name": "St. Michael and St. Gudula Cathedral", "name_en": "Brussels Cathedral", "area": "Merkez", "category": "Tarihi", "tags": ["katedral", "gotik", "vitray"], "lat": 50.8479, "lng": 4.3601, "price": "free", "rating": 4.7, "description": "Victor Hugo'nun 'gotik sanatın en saf örneği' dediği görkemli katedral.", "description_en": "Magnificent cathedral called 'purest example of Gothic art' by Victor Hugo.", "bestTime": "Sabah", "tips": "Pazar ayinlerinde koro müziği dinleyebilirsiniz.", "tips_en": "You can listen to choir music during Sunday mass."}
]

# BATCH 3: Gastronomi (Midyeler, Waffle & Çikolata)
batch_3 = [
    {"name": "Chez Léon", "name_en": "Chez Léon", "area": "Merkez", "category": "Restoran", "tags": ["midye", "popüler", "klasik"], "lat": 50.8482, "lng": 4.3539, "price": "medium", "rating": 4.4, "description": "'Moules-Frites' (Midye-Patates) denince akla gelen ilk, klasikleşmiş mekan.", "description_en": "First classic place that comes to mind for 'Moules-Frites'.", "bestTime": "Akşam", "tips": "Turistik olsa da servis hızlı ve lezzet standarttır.", "tips_en": "Although touristy, service is fast and taste is standard."},
    {"name": "Fritland", "name_en": "Fritland", "area": "Bourse", "category": "Sokak Lezzeti", "tags": ["patates", "mitraillette", "efsane"], "lat": 50.8480, "lng": 4.3490, "price": "low", "rating": 4.5, "description": "Brüksel'in en iyi patates kızartmacısı. Mitraillette sandviçi efsane.", "description_en": "Best fries place in Brussels. Mitraillette sandwich is legendary.", "bestTime": "Gece", "tips": "Sıra her zaman vardır ama çabuk ilerler.", "tips_en": "There is always a line but it moves fast."},
    {"name": "Maison Dandoy - Grand Place", "name_en": "Dandoy Tea Room", "area": "Grand Place", "category": "Kafe", "tags": ["waffle", "speculoos", "tarihi"], "lat": 50.8468, "lng": 4.3526, "price": "high", "rating": 4.4, "description": "Gerçek Brüksel Waffle'ı yemek için en doğru, tarihi adres.", "description_en": "The right, historic address to eat real Brussels Waffle.", "bestTime": "Öğle", "tips": "Speculooslu waffle'ı deneyin.", "tips_en": "Try the Speculoos waffle."},
    {"name": "Delirium Café", "name_en": "Delirium Café", "area": "Merkez", "category": "Bar", "tags": ["bira", "rekor", "çeşit"], "lat": 50.8484, "lng": 4.3538, "price": "medium", "rating": 4.6, "description": "Guinness rekorlar kitabına giren bira çeşidiyle ünlü ikonik bar.", "description_en": "Iconic bar famous for its beer variety entered in Guinness Book of Records.", "bestTime": "Gece", "tips": "Pembe fil logolu bardağı hatıra olarak alabilirsiniz.", "tips_en": "You can buy the glass with pink elephant logo as souvenir."},
    {"name": "Fin de Siècle", "name_en": "Fin de Siècle", "area": "Dansaert", "category": "Restoran", "tags": ["otantik", "karbonat", "yerel"], "lat": 50.8490, "lng": 4.3470, "price": "medium", "rating": 4.6, "description": "Menüsü kara tahtada yazılı, rezervasyonsuz çalışan, en otantik Belçika restoranı.", "description_en": "Most authentic Belgian restaurant with menu on blackboard, no reservations.", "bestTime": "Akşam", "tips": "'Carbonnade Flamande' (biralı et yahnisi) burada yenmeli.", "tips_en": "'Carbonnade Flamande' should be eaten here."},
    {"name": "Pierre Marcolini", "name_en": "Pierre Marcolini", "area": "Sablon", "category": "Alışveriş", "tags": ["çikolata", "lüks", "gurme"], "lat": 50.8405, "lng": 4.3560, "price": "high", "rating": 4.8, "description": "Çikolatanın haute-couture'ü. Makaronları ve pralinleri sanat eseri gibi.", "description_en": "Haute-couture of chocolate. Macarons and pralines are like art pieces.", "bestTime": "Gündüz", "tips": "Şampanyalı trüf çikolatası efsane.", "tips_en": "Champagne truffle chocolate is legendary."}
]

def enrich():
    filepath = 'assets/cities/bruksel.json'
    all_new = batch_1 + batch_2 + batch_3
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if 'highlights' not in data: data['highlights'] = []
    except:
        data = {"city": "Brüksel", "country": "Belgium", "coordinates": {"lat": 50.8476, "lng": 4.3572}, "highlights": []}

    print(f"Loaded {len(data['highlights'])} places.")
    existing_names = {p['name'].lower() for p in data['highlights']}
    places_to_add = []
    
    for place in all_new:
        if place['name'].lower() in existing_names:
            print(f"Skip: {place['name']}")
            continue
        print(f"Processing: {place['name']}")
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('é', 'e').replace('ü', 'u')
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        place['distanceFromCenter'] = place.get('distanceFromCenter', 0.5)
        places_to_add.append(place)
        time.sleep(0.3)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places to Brüksel.")

if __name__ == "__main__":
    enrich()
