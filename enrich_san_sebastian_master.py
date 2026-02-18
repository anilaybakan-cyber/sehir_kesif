import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} San Sebastian Spain", f"{place_name} Donostia", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:10000@43.3183,-1.9812"
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

# BATCH 1: Çevre Kasabalar (Bask Kıyıları)
batch_1 = [
    {"name": "Hondarribia", "name_en": "Hondarribia", "area": "Çevre", "category": "Kasaba", "tags": ["kasaba", "renkli", "bask"], "lat": 43.3600, "lng": -1.7900, "price": "free", "rating": 4.8, "description": "Rengarenk balkonlu Bask evleri ve muhteşem yemekleriyle ünlü sınır kasabası.", "description_en": "Border town famous for its colorful balconied Basque houses and magnificent food.", "bestTime": "Gündüz", "tips": "Fransa'ya (Hendaye) tekneyle geçebilirsiniz.", "tips_en": "You can cross to France (Hendaye) by boat."},
    {"name": "Pasai Donibane", "name_en": "Pasajes San Juan", "area": "Çevre", "category": "Kasaba", "tags": ["kasaba", "tarihi", "liman"], "lat": 43.3200, "lng": -1.9200, "price": "free", "rating": 4.7, "description": "Victor Hugo'nun hayran kaldığı, tek caddeli pitoresk balıkçı köyü.", "description_en": "Picturesque fishing village with a single street, admired by Victor Hugo.", "bestTime": "Öğle", "tips": "Meydanda deniz ürünleri yiyin.", "tips_en": "Eat seafood in the square."},
    {"name": "Getaria", "name_en": "Getaria", "area": "Çevre", "category": "Kasaba", "tags": ["kasaba", "balenciaga", "ızgara"], "lat": 43.3000, "lng": -2.2000, "price": "free", "rating": 4.7, "description": "Balenciaga'nın doğum yeri ve ızgara balıklarıyla ünlü kasaba.", "description_en": "Town famous for grilled fish and birthplace of Balenciaga.", "bestTime": "Öğle", "tips": "Balenciaga Müzesi'ni ziyaret edin.", "tips_en": "Visit the Balenciaga Museum."},
    {"name": "Zarautz", "name_en": "Zarautz", "area": "Çevre", "category": "Plaj", "tags": ["plaj", "sörf", "uzun"], "lat": 43.2800, "lng": -2.1700, "price": "free", "rating": 4.6, "description": "Bask Bölgesi'nin en uzun plajı ve sörf merkezi.", "description_en": "Longest beach in the Basque Country and surf center.", "bestTime": "Yaz", "tips": "Karlos Arguiñano'nun restoranı burada.", "tips_en": "Karlos Arguiñano's restaurant is here."}
]

# BATCH 2: Efsanevi Pintxos Barlar (Rota Tamamlayıcı)
batch_2 = [
    {"name": "Borda Berri", "name_en": "Borda Berri", "area": "Old Town", "category": "Restoran", "tags": ["pintxos", "risotto", "yanağı"], "lat": 43.3230, "lng": -1.9840, "price": "medium", "rating": 4.8, "description": "İdiyazabal peynirli risotto ve dana yanağı efsanedir.", "description_en": "Idiazabal cheese risotto and beef cheek are legendary.", "bestTime": "Akşam", "tips": "Sadece nakit geçerli olabilir.", "tips_en": "Only cash might be accepted."},
    {"name": "La Cuchara de San Telmo", "name_en": "La Cuchara de San Telmo", "area": "Old Town", "category": "Restoran", "tags": ["sıcak", "gurme", "foie"], "lat": 43.3240, "lng": -1.9835, "price": "medium", "rating": 4.7, "description": "Tezgahta ürün yok, her şey sipariş üzerine sıcak yapılıyor. Foie gras müthiş.", "description_en": "No products on the counter, everything is made hot to order. Foie gras is amazing.", "bestTime": "Akşam", "tips": "Erken gidin, çok kalabalık oluyor.", "tips_en": "Go early, it gets very crowded."},
    {"name": "Goiz Argi", "name_en": "Goiz Argi", "area": "Old Town", "category": "Restoran", "tags": ["karides", "brochette", "sos"], "lat": 43.3235, "lng": -1.9845, "price": "medium", "rating": 4.6, "description": "'Brocheta de gambas' (karides şiş) buranın imzası.", "description_en": "'Brocheta de gambas' (shrimp skewer) is their signature.", "bestTime": "Öğle", "tips": "Sosu ekmeğe banmayı unutmayın.", "tips_en": "Don't forget to dip bread in the sauce."},
    {"name": "Bar Zeruko", "name_en": "Bar Zeruko", "area": "Old Town", "category": "Restoran", "tags": ["modern", "deneyim", "duman"], "lat": 43.3230, "lng": -1.9835, "price": "high", "rating": 4.5, "description": "Modern ve deneysel pintxoslar, görsel şölen.", "description_en": "Modern and experimental pintxos, a visual feast.", "bestTime": "Akşam", "tips": "'La Hoguera' (Kendi pişirdiğin morina) deneyin.", "tips_en": "Try 'La Hoguera' (Cook your own cod)."}
]

# BATCH 3: Manzara ve Kültür
batch_3 = [
    {"name": "Paseo Nuevo", "name_en": "New Promenade", "area": "Urgull", "category": "Manzara", "tags": ["yürüyüş", "dalga", "deniz"], "lat": 43.3280, "lng": -1.9900, "price": "free", "rating": 4.8, "description": "Urull Dağı'nın etrafını dolaşan, dalgaların patladığı muhteşem yürüyüş yolu.", "description_en": "Magnificent walkway around Mount Urgull where waves crash.", "bestTime": "Gün batımı", "tips": "Fırtınalı havalarda dikkatli olun, ıslanabilirsiniz.", "tips_en": "Be careful in stormy weather, you might get wet."},
    {"name": "Mercado de la Bretxa", "name_en": "La Bretxa Market", "area": "Old Town", "category": "Alışveriş", "tags": ["pazar", "taze", "yerel"], "lat": 43.3225, "lng": -1.9820, "price": "medium", "rating": 4.5, "description": "Şehrin en iyi şeflerinin alışveriş yaptığı tarihi pazar yeri.", "description_en": "Historic market where the city's best chefs shop.", "bestTime": "Sabah", "tips": "Vakumlanmış jambon ve peynir alabilirsiniz.", "tips_en": "You can buy vacuum-packed ham and cheese."},
    {"name": "Eureka! Zientzia Museoa", "name_en": "Eureka! Science Museum", "area": "Miramon", "category": "Müze", "tags": ["bilim", "çocuk", "interaktif"], "lat": 43.2950, "lng": -1.9700, "price": "medium", "rating": 4.6, "description": "Çocuklar ve meraklılar için interaktif bilim müzesi ve planetaryum.", "description_en": "Interactive science museum and planetarium for kids and enthusiasts.", "bestTime": "Gündüz", "tips": "Yağmurlu günler için harika bir aktivite.", "tips_en": "Great activity for rainy days."},
    {"name": "Monte Ulia", "name_en": "Mount Ulia", "area": "Gros", "category": "Manzara", "tags": ["doğa", "yürüyüş", "bakir"], "lat": 43.3300, "lng": -1.9600, "price": "free", "rating": 4.7, "description": "Daha az turistik, yerlilerin tercih ettiği doğa yürüyüşü rotası.", "description_en": "Less touristy nature hiking route preferred by locals.", "bestTime": "Gündüz", "tips": "Pasai Donibane'ye kadar yürüyebilirsiniz (muhteşem rota).", "tips_en": "You can walk to Pasai Donibane (magnificent route)."}
]

# BATCH 4: Aktiviteler
batch_4 = [
    {"name": "Kursaal Bridge", "name_en": "Zurriola Bridge", "area": "Merkez", "category": "Manzara", "tags": ["köprü", "ışık", "modern"], "lat": 43.3250, "lng": -1.9780, "price": "free", "rating": 4.4, "description": "Nehir ile denizin buluştuğu noktadaki ikonik köprü.", "description_en": "Iconic bridge where river meets sea.", "bestTime": "Gece", "tips": "Kursaal binasının ışıklarıyla güzel görünür.", "tips_en": "Looks beautiful with Kursaal building lights."},
    {"name": "Cider House Experience", "name_en": "Sidreria", "area": "Astigarraga", "category": "Deneyim", "tags": ["sidra", "biftek", "geleneksel"], "lat": 43.2800, "lng": -1.9500, "price": "medium", "rating": 4.8, "description": "Geleneksel 'Sidreria' deneyimi: dev fıçılardan elma şarabı ve biftek menüsü.", "description_en": "Traditional 'Sidreria' experience: cider from giant barrels and steak menu.", "bestTime": "Akşam", "tips": "'Txotx!' denildiğinde bardağınızı fıçıya götürün.", "tips_en": "Take your glass to the barrel when they shout 'Txotx!'."},
    {"name": "Cristina Enea Park", "name_en": "Cristina Enea Park", "area": "Egia", "category": "Park", "tags": ["park", "sakin", "tavuskuşu"], "lat": 43.3150, "lng": -1.9750, "price": "free", "rating": 4.6, "description": "Şehrin ortasında tavuskuşlarının dolaştığı huzurlu bir vaha.", "description_en": "Peaceful oasis in the city center where peacocks roam.", "bestTime": "Gündüz", "tips": "Göl kenarındaki banklarda dinlenin.", "tips_en": "Relax on benches by the lake."}
]

def enrich():
    filepath = 'assets/cities/san_sebastian.json'
    all_new = batch_1 + batch_2 + batch_3 + batch_4
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('ñ', 'n').replace('á', 'a')
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
