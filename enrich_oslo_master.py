import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Oslo Norway", f"{place_name} Oslo", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:10000@59.9139,10.7522"
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

# BATCH 1: Modern Mimari & Fiyort
batch_1 = [
    {"name": "Oslo Opera House", "name_en": "Oslo Opera House", "area": "Bjørvika", "category": "Manzara", "tags": ["mimari", "beyaz", "çatı"], "lat": 59.9075, "lng": 10.7531, "price": "free", "rating": 4.8, "description": "Buzuldan esinlenilmiş, çatısında yürüyebileceğiniz modern mimari harikası.", "description_en": "Modern architectural wonder inspired by glaciers, where you can walk on the roof.", "bestTime": "Gün batımı", "tips": "Çatısına kadar yürüyüp fiyort manzarasını izleyin.", "tips_en": "Walk up to the roof and watch the fjord view."},
    {"name": "Vigeland Park", "name_en": "Vigeland Sculpture Park", "area": "Majorstuen", "category": "Park", "tags": ["heykel", "açıkhava", "gustav vigeland"], "lat": 59.9270, "lng": 10.7008, "price": "free", "rating": 4.7, "description": "Dünyanın en büyük heykel parkı. İnsan yaşamının döngüsünü anlatan 200'den fazla heykel.", "description_en": "World's largest sculpture park. More than 200 sculptures depicting the cycle of human life.", "bestTime": "Sabah", "tips": "'Sinirli Çocuk' (Sinnataggen) heykelini bulun.", "tips_en": "Find the 'Angry Boy' (Sinnataggen) sculpture."},
    {"name": "Munch Museum", "name_en": "Munch Museum", "area": "Bjørvika", "category": "Müze", "tags": ["sanat", "edvard munch", "çığlık"], "lat": 59.9055, "lng": 10.7550, "price": "medium", "rating": 4.5, "description": "Edvard Munch'un 'Çığlık' tablosu dahil devasa koleksiyonuna ev sahipliği yapan dikey müze.", "description_en": "Vertical museum hosting Edvard Munch's vast collection including 'The Scream'.", "bestTime": "Gündüz", "tips": "En üst kattaki bardan Oslo manzarası harikadır.", "tips_en": "Oslo view from the top floor bar is wonderful."},
    {"name": "Akershus Fortress", "name_en": "Akershus Fortress", "area": "Sentrum", "category": "Tarihi", "tags": ["kale", "manzara", "tarihi"], "lat": 59.9090, "lng": 10.7370, "price": "free", "rating": 4.6, "description": "Limanı koruyan ortaçağ kalesi. Yemyeşil alanları ve tarihi dokusuyla huzurlu bir kaçış.", "description_en": "Medieval fortress protecting the harbor. Peaceful escape with lush green areas and historic texture.", "bestTime": "Öğle", "tips": "Disney'in Frozen filmindeki Arendelle kalesine ilham vermiştir.", "tips_en": "It inspired the Arendelle castle in Disney's Frozen movie."},
    {"name": "Holmenkollen Ski Museum", "name_en": "Ski Jump", "area": "Holmenkollen", "category": "Manzara", "tags": ["kayak", "panaroma", "spor"], "lat": 59.9640, "lng": 10.6675, "price": "medium", "rating": 4.7, "description": "Şehrin tepesinde, panoramik Oslo manzarası sunan dev kayakla atlama kulesi.", "description_en": "Giant ski jumping tower atop the city offering panoramic Oslo views.", "bestTime": "Gündüz", "tips": "Kuleye asansörle çıkabilirsiniz, manzara nefes kesici.", "tips_en": "You can take the elevator to the tower, view is breathtaking."}
]

# BATCH 2: Gizli Köşeler & Yerel Yaşam
batch_2 = [
    {"name": "Damstredet", "name_en": "Damstredet", "area": "St. Hanshaugen", "category": "Tarihi", "tags": ["ahşap ev", "renkli", "nostalji"], "lat": 59.9215, "lng": 10.7483, "price": "free", "rating": 4.6, "description": "18. ve 19. yüzyıldan kalma renkli ahşap evlerle dolu masalsı sokak.", "description_en": "Fairytale street filled with colorful wooden houses from 18th and 19th centuries.", "bestTime": "Gündüz", "tips": "Fotoğraf çekmek için şehrin en şirin sokağıdır.", "tips_en": "It is the cutest street in the city for taking photos."},
    {"name": "Akerselva River Walk", "name_en": "Akerselva Walk", "area": "Grünerløkka", "category": "Doğa", "tags": ["nehir", "yürüyüş", "şelale"], "lat": 59.9280, "lng": 10.7560, "price": "free", "rating": 4.8, "description": "Şehrin ortasında şelaleler ve eski fabrikalar arasından geçen yeşil yürüyüş rotası.", "description_en": "Green walking route passing through waterfalls and old factories in the middle of the city.", "bestTime": "Sabah", "tips": "Mølla şelalesini mutlaka görün.", "tips_en": "Must see the Mølla waterfall."},
    {"name": "Emanuel Vigeland Museum", "name_en": "Emanuel Vigeland Museum", "area": "Slemdal", "category": "Müze", "tags": ["gizemli", "karanlık", "akustik"], "lat": 59.9400, "lng": 10.6900, "price": "medium", "rating": 4.7, "description": "Loş ışıklı, fresklerle kaplı ve inanılmaz bir akustiğe sahip gizli bir mozole-müze.", "description_en": "Hidden mausoleum-museum, dimly lit, covered in frescoes and with incredible acoustics.", "bestTime": "Pazar", "tips": "Sadece pazar günleri açıktır, önceden kontrol edin.", "tips_en": "Only open on Sundays, check beforehand."},
    {"name": "Ekebergparken", "name_en": "Ekeberg Sculpture Park", "area": "Ekeberg", "category": "Park", "tags": ["sanat", "orman", "manzara"], "lat": 59.8970, "lng": 10.7725, "price": "free", "rating": 4.6, "description": "Orman içine gizlenmiş modern heykeller (Dali, Rodin) ve harika bir şehir manzarası.", "description_en": "Modern sculptures (Dali, Rodin) hidden in the forest and a great city view.", "bestTime": "Gün batımı", "tips": "'Munch Spot' (Çığlık tablosunun arka planı) buradadır.", "tips_en": "'Munch Spot' (background of The Scream) is here."},
    {"name": "Telthusbakken", "name_en": "Telthusbakken", "area": "Gamle Aker", "category": "Tarihi", "tags": ["romantik", "bahçe", "yokuş"], "lat": 59.9230, "lng": 10.7500, "price": "free", "rating": 4.5, "description": "Damstredet'in yakınında, topluluk bahçelerine bakan bir başka şirin ahşap evler sokağı.", "description_en": "Another cute wooden houses street near Damstredet overlooking community gardens.", "bestTime": "Akşamüzeri", "tips": "Yokuş aşağı yürürken bahçeleri izleyin.", "tips_en": "Watch the gardens while walking downhill."}
]

# BATCH 3: Yeme & İçme (Norveç Mutfağı)
batch_3 = [
    {"name": "Vippa Oslo", "name_en": "Vippa Street Food", "area": "Vippetangen", "category": "Sokak Lezzeti", "tags": ["fiyort", "sokak lezzeti", "canlı"], "lat": 59.9020, "lng": 10.7410, "price": "medium", "rating": 4.6, "description": "Deniz kenarında eski bir depoda kurulmuş, çok çeşitli sokak lezzetleri pazarı.", "description_en": "Street food market with great variety set in an old warehouse by the sea.", "bestTime": "Öğle", "tips": "Deniz kenarındaki masalarda oturup fiyort havası alın.", "tips_en": "Sit at tables by the sea and enjoy the fjord air."},
    {"name": "Mathallen Oslo", "name_en": "Mathallen Food Hall", "area": "Grünerløkka", "category": "Restoran", "tags": ["gurme", "pazar", "çeşit"], "lat": 59.9220, "lng": 10.7520, "price": "medium", "rating": 4.5, "description": "Norveç ve dünya mutfağından gurme ürünler sunan kapalı pazar yeri.", "description_en": "Indoor market hall offering gourmet products from Norwegian and world cuisine.", "bestTime": "Öğle", "tips": "Fiskeriet'te balık çorbası için.", "tips_en": "Drink fish soup at Fiskeriet."},
    {"name": "Restaurant Schrøder", "name_en": "Restaurant Schrøder", "area": "St. Hanshaugen", "category": "Restoran", "tags": ["geleneksel", "köfte", "nostalji"], "lat": 59.9260, "lng": 10.7400, "price": "medium", "rating": 4.4, "description": "Harry Hole romanlarının müdavimi olduğu, geleneksel Norveç yemekleri yapan tarihi restoran.", "description_en": "Historic restaurant serving traditional Norwegian food, frequented by Harry Hole novels.", "bestTime": "Akşam", "tips": "'Kjøttkaker' (Norveç köftesi) denemelisiniz.", "tips_en": "You must try 'Kjøttkaker' (Norwegian meatballs)."},
    {"name": "Tim Wendelboe", "name_en": "Tim Wendelboe", "area": "Grünerløkka", "category": "Kafe", "tags": ["kahve", "dünya çapında", "mikro"], "lat": 59.9235, "lng": 10.7580, "price": "medium", "rating": 4.8, "description": "Dünyanın en iyi kahvecilerinden biri olarak gösterilen, kendi kavurduğu kahveleri sunan mekan.", "description_en": "Place showing as one of the best coffee shops in the world, serving its own roasted coffee.", "bestTime": "Sabah", "tips": "Sadece kahve odaklıdır, yiyecek çeşidi azdır.", "tips_en": "Focused only on coffee, food variety is low."},
    {"name": "Engebret Café", "name_en": "Engebret Café", "area": "Sentrum", "category": "Restoran", "tags": ["en eski", "tarihi", "lüks"], "lat": 59.9080, "lng": 10.7400, "price": "high", "rating": 4.5, "description": "1857'den beri açık olan Oslo'nun en eski restoranı. Ibsen ve Munch'un müdavimi olduğu yer.", "description_en": "Oslo's oldest restaurant open since 1857. Place where Ibsen and Munch were regulars.", "bestTime": "Akşam", "tips": "Klasik 'Smørbrød' (açık sandviç) öğle yemeği için idealdir.", "tips_en": "Classic 'Smørbrød' (open sandwich) is ideal for lunch."}
]

def enrich():
    filepath = 'assets/cities/oslo.json'
    all_new = batch_1 + batch_2 + batch_3
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if 'highlights' not in data: data['highlights'] = []
    except:
        data = {"city": "Oslo", "country": "Norway", "coordinates": {"lat": 59.9139, "lng": 10.7522}, "highlights": []}

    print(f"Loaded {len(data['highlights'])} places.")
    existing_names = {p['name'].lower() for p in data['highlights']}
    places_to_add = []
    
    for place in all_new:
        if place['name'].lower() in existing_names:
            print(f"Skip: {place['name']}")
            continue
        print(f"Processing: {place['name']}")
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('ø', 'o').replace('å', 'a')
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        place['distanceFromCenter'] = place.get('distanceFromCenter', 0.5)
        places_to_add.append(place)
        time.sleep(0.3)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places to Oslo.")

if __name__ == "__main__":
    enrich()
