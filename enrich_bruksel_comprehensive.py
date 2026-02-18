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

# BATCH 1: Müzeler ve Sanat
batch_1 = [
    {"name": "Comic Art Museum", "name_en": "Belgian Comic Strip Center", "area": "Merkez", "category": "Müze", "tags": ["çizgi roman", "tenten", "şirinler"], "lat": 50.8509, "lng": 4.3601, "price": "medium", "rating": 4.5, "description": "Victor Horta tasarımlı binada, Tenten ve Şirinler'in dünyasına yolculuk.", "description_en": "Journey into the world of Tintin and Smurfs in a building designed by Victor Horta.", "bestTime": "Gündüz", "tips": "Müze dükkanından çizgi roman alabilirsiniz.", "tips_en": "You can buy comic books from the museum shop."},
    {"name": "Musical Instruments Museum", "name_en": "MIM", "area": "Mont des Arts", "category": "Müze", "tags": ["müzik", "art nouveau", "manzara"], "lat": 50.8428, "lng": 4.3587, "price": "medium", "rating": 4.7, "description": "Art Nouveau binasında, kulaklıklarla enstrümanların sesini dinleyebileceğiniz müze.", "description_en": "Museum in Art Nouveau building where you can listen to instruments via headphones.", "bestTime": "Gündüz", "tips": "En üst kattaki terasın manzarası harikadır.", "tips_en": "View from the top floor terrace is wonderful."},
    {"name": "Train World", "name_en": "Train World", "area": "Schaerbeek", "category": "Müze", "tags": ["tren", "lokomotif", "tarih"], "lat": 50.8785, "lng": 4.3790, "price": "medium", "rating": 4.8, "description": "Tarihi lokomotiflerin sergilendiği, Avrupa'nın en iyi tren müzelerinden biri.", "description_en": "One of Europe's best train museums displaying historic locomotives.", "bestTime": "Gündüz", "tips": "Schaerbeek istasyonunda yer alır.", "tips_en": "Located at Schaerbeek station."},
    {"name": "Autoworld", "name_en": "Autoworld", "area": "Cinquantenaire", "category": "Müze", "tags": ["araba", "klasik", "koleksiyon"], "lat": 50.8398, "lng": 4.3932, "price": "medium", "rating": 4.6, "description": "Cinquantenaire Parkı'nda, yüzlerce klasik otomobilin sergilendiği müze.", "description_en": "Museum in Cinquantenaire Park displaying hundreds of classic cars.", "bestTime": "Gündüz", "tips": "Ferrari sergisi varsa kaçırmayın.", "tips_en": "Don't miss the Ferrari exhibition if available."},
    {"name": "House of European History", "name_en": "House of European History", "area": "Leopold Park", "category": "Müze", "tags": ["avrupa", "tarih", "ücretsiz"], "lat": 50.8390, "lng": 4.3780, "price": "free", "rating": 4.7, "description": "Avrupa tarihini interaktif ve tarafsız bir şekilde anlatan etkileyici müze.", "description_en": "Impressive museum explaining European history interactively and impartially.", "bestTime": "Gündüz", "tips": "Giriş ücretsizdir.", "tips_en": "Entrance is free."},
    {"name": "Natural Sciences Museum", "name_en": "Museum of Natural Sciences", "area": "Leopold Park", "category": "Müze", "tags": ["dinozor", "doğa", "bilim"], "lat": 50.8370, "lng": 4.3760, "price": "medium", "rating": 4.7, "description": "Avrupa'nın en büyük dinozor galerisine sahip doğa tarihi müzesi.", "description_en": "Natural history museum with Europe's largest dinosaur gallery.", "bestTime": "Gündüz", "tips": "Iguanodon iskeletleri çok meşhurdur.", "tips_en": "Iguanodon skeletons are very famous."}
]

# BATCH 2: Parklar ve Yeşil Alanlar
batch_2 = [
    {"name": "Parc du Cinquantenaire", "name_en": "Cinquantenaire Park", "area": "European Quarter", "category": "Park", "tags": ["zafer takı", "piknik", "müzeler"], "lat": 50.8410, "lng": 4.3900, "price": "free", "rating": 4.7, "description": "Devasa zafer takı ve müzelerle çevrili, şehrin en görkemli parkı.", "description_en": "City's most magnificent park surrounded by a giant triumphal arch and museums.", "bestTime": "Öğle", "tips": "Zafer takının üzerine çıkıp manzarayı izleyin.", "tips_en": "Climb up the triumphal arch and watch the view."},
    {"name": "Bois de la Cambre", "name_en": "Cambre Woods", "area": "Ixelles", "category": "Park", "tags": ["orman", "göl", "bisiklet"], "lat": 50.8100, "lng": 4.3750, "price": "free", "rating": 4.8, "description": "Şehrin akciğeri sayılan, göletli ve ormanlık devasa park.", "description_en": "Massive park with pond and woods, considered the city's lungs.", "bestTime": "Hafta sonu", "tips": "Ortadaki adada yer alan Chalet Robinson'a kayıkla geçin.", "tips_en": "Take a boat to Chalet Robinson on the central island."},
    {"name": "Parc Leopold", "name_en": "Leopold Park", "area": "European Quarter", "category": "Park", "tags": ["gölet", "sakin", "ab"], "lat": 50.8385, "lng": 4.3795, "price": "free", "rating": 4.6, "description": "Avrupa Parlamentosu'nun gölgesinde, huzurlu ve göletli bir park.", "description_en": "Peaceful park with a pond in the shadow of the European Parliament.", "bestTime": "Öğle", "tips": "Öğle yemeği molası veren AB çalışanlarını görebilirsiniz.", "tips_en": "You can see EU employees taking lunch breaks."},
    {"name": "Tenbosch Park", "name_en": "Tenbosch Park", "area": "Ixelles", "category": "Park", "tags": ["botanik", "gizli", "oyun"], "lat": 50.8245, "lng": 4.3645, "price": "free", "rating": 4.7, "description": "Nadir ağaçlar ve bitkilerle dolu, botanik bahçesi tadında gizli bir park.", "description_en": "Hidden park like a botanical garden filled with rare trees and plants.", "bestTime": "Gündüz", "tips": "Çocuklar için oyun alanları çok güzeldir.", "tips_en": "Playgrounds for kids are very nice."},
    {"name": "Royal Greenhouses of Laeken", "name_en": "Laeken Greenhouses", "area": "Laeken", "category": "Park", "tags": ["sera", "kraliyet", "nadir"], "lat": 50.8870, "lng": 4.3600, "price": "medium", "rating": 4.9, "description": "Sadece baharda 3 hafta açılan, Art Nouveau tarzı muhteşem kraliyet seraları.", "description_en": "Magnificent Art Nouveau royal greenhouses open only for 3 weeks in spring.", "bestTime": "Bahar", "tips": "Açık olduğu dönemi mutlaka kontrol edin, biletler hemen tükenir.", "tips_en": "Ideally check the open period, tickets sell out immediately."}
]

# BATCH 3: Tatlı Krizleri (Çikolata & Waffle)
batch_3 = [
    {"name": "Neuhaus Chocolates - Galerie de la Reine", "name_en": "Neuhaus", "area": "Merkez", "category": "Alışveriş", "tags": ["çikolata", "pralin", "ilk"], "lat": 50.8470, "lng": 4.3550, "price": "high", "rating": 4.7, "description": "Pralinin mucidi. Pasaj içindeki bu mağaza tarihi atmosferiyle büyüleyici.", "description_en": "Inventor of praline. This shop inside the arcade is fascinating with its historic atmosphere.", "bestTime": "Gündüz", "tips": "Caprice ve Tentation çeşitlerini deneyin.", "tips_en": "Try Caprice and Tentation varieties."},
    {"name": "Mary Chocolatier", "name_en": "Mary", "area": "Royale", "category": "Alışveriş", "tags": ["çikolata", "kraliyet", "zarif"], "lat": 50.8475, "lng": 4.3630, "price": "high", "rating": 4.8, "description": "Belçika Kraliyet Ailesi'nin tedarikçisi. Kutuları sanat eseri gibidir.", "description_en": "Supplier of Belgian Royal Family. Boxes are like art pieces.", "bestTime": "Gündüz", "tips": "Hediye için en şık seçenektir.", "tips_en": "Most stylish option for gifts."},
    {"name": "Aux Merveilleux de Fred", "name_en": "Aux Merveilleux de Fred", "area": "Merkez", "category": "Tatlı", "tags": ["mereng", "hafif", "bulut"], "lat": 50.8480, "lng": 4.3530, "price": "medium", "rating": 4.8, "description": "Bulut gibi hafif mereng (bezbe) tatlılarıyla ünlü pastane.", "description_en": "Patisserie famous for cloud-light meringue sweets.", "bestTime": "Gündüz", "tips": "Altı çeşit mini merengden oluşan kutudan alın.", "tips_en": "Get the box with six types of mini meringues."},
    {"name": "Frederic Blondeel", "name_en": "Frederic Blondeel", "area": "Koekelberg", "category": "Kafe", "tags": ["çikolata", "kavurma", "sıcak çikolata"], "lat": 50.8650, "lng": 4.3350, "price": "medium", "rating": 4.8, "description": "Çekirdekten çikolataya (bean-to-bar) üretim yapan nadir şeflerden.", "description_en": "One of the rare chefs producing bean-to-bar chocolate.", "bestTime": "Öğle", "tips": "Sıcak çikolatası ödüllüdür.", "tips_en": "His hot chocolate is award-winning."},
    {"name": "Laurent Gerbaud Chocolatier", "name_en": "Laurent Gerbaud", "area": "Merkez", "category": "Alışveriş", "tags": ["çikolata", "meyveli", "modern"], "lat": 50.8440, "lng": 4.3570, "price": "high", "rating": 4.7, "description": "Şeker yerine meyve ve baharatların doğal tadını kullanan modern çikolatacı.", "description_en": "Modern chocolatier using natural taste of fruits and spices instead of sugar.", "bestTime": "Gündüz", "tips": "Cumartesi günleri atölye çalışmaları yapılır.", "tips_en": "Workshops are held on Saturdays."}
]

# BATCH 4: Restoranlar ve Barlar
batch_4 = [
    {"name": "Noordzee - Mer du Nord", "name_en": "Noordzee", "area": "Sainte-Catherine", "category": "Sokak Lezzeti", "tags": ["balık", "ayaküstü", "taze"], "lat": 50.8505, "lng": 4.3485, "price": "medium", "rating": 4.7, "description": "Ayaküstü taze deniz ürünleri, balık çorbası ve şarap keyfi.", "description_en": "Standing fresh seafood, fish soup and wine enjoyment.", "bestTime": "Öğle", "tips": "Kibbeling (kızarmış balık) ve karides kroket favori.", "tips_en": "Kibbeling (fried fish) and shrimp croquettes are favorites."},
    {"name": "Moeder Lambic Fontainas", "name_en": "Moeder Lambic", "area": "Fontainas", "category": "Bar", "tags": ["bira", "yerel", "uzman"], "lat": 50.8450, "lng": 4.3450, "price": "medium", "rating": 4.6, "description": "Gerçek bira tutkunlarının buluşma noktası. Muslukta onlarca çeşit var.", "description_en": "Meeting point for true beer enthusiasts. Dozens of varieties on tap.", "bestTime": "Gece", "tips": "Garsonlardan tadım önerisi isteyin, çok bilgililer.", "tips_en": "Ask waiters for tasting suggestions, they are very knowledgeable."},
    {"name": "À La Mort Subite", "name_en": "A La Mort Subite", "area": "Merkez", "category": "Bar", "tags": ["tarihi", "bira", "nostalji"], "lat": 50.8490, "lng": 4.3575, "price": "medium", "rating": 4.5, "description": "1910'dan kalma dekoruyla zamanın durduğu tarihi brasserie.", "description_en": "Historic brasserie where time stands still with 1910 decor.", "bestTime": "Öğle", "tips": "Kendi biraları olan 'Mort Subite' (Ani Ölüm) içilir.", "tips_en": "Drink their own beer 'Mort Subite' (Sudden Death)."},
    {"name": "Peck 47", "name_en": "Peck 47", "area": "Merkez", "category": "Kafe", "tags": ["brunch", "yumurta", "popüler"], "lat": 50.8485, "lng": 4.3500, "price": "medium", "rating": 4.6, "description": "Brüksel'in en popüler brunch mekanı. Poşe yumurtaları efsane.", "description_en": "Brussels' most popular brunch place. Poached eggs are legendary.", "bestTime": "Sabah", "tips": "Erken gidin, rezervasyon almıyorlar.", "tips_en": "Go early, they don't take reservations."},
    {"name": "Le Cirio", "name_en": "Le Cirio", "area": "Bourse", "category": "Restoran", "tags": ["brasserie", "tarihi", "art nouveau"], "lat": 50.8482, "lng": 4.3510, "price": "medium", "rating": 4.4, "description": "1886'dan beri açık, Art Nouveau tarzda görkemli bir brasserie.", "description_en": "Magnificent Art Nouveau brasserie open since 1886.", "bestTime": "Akşam", "tips": "'Half-en-half' kokteylini deneyin.", "tips_en": "Try the 'Half-en-half' cocktail."}
]

# BATCH 5: Gizli Rotalar
batch_5 = [
    {"name": "Zinneke Pis", "name_en": "Zinneke Pis", "area": "Dansaert", "category": "Heykel", "tags": ["köpek", "işeyen", "gizli"], "lat": 50.8488, "lng": 4.3455, "price": "free", "rating": 4.2, "description": "İşeyen çocuk ve kızdan sonra ailenin üçüncü üyesi: direğe işeyen köpek.", "description_en": "Third member of the family after peeing boy and girl: dog peeing on a pole.", "bestTime": "Gündüz", "tips": "Sokak köşesinde olduğu için gözden kaçabilir.", "tips_en": "Can be missed as it is on a street corner."},
    {"name": "Place du Grand Sablon", "name_en": "Grand Sablon Square", "area": "Sablon", "category": "Meydan", "tags": ["antika", "şık", "çikolata"], "lat": 50.8410, "lng": 4.3550, "price": "free", "rating": 4.7, "description": "Antikacılar ve lüks çikolatacılarla çevrili şık meydan.", "description_en": "Stylish square surrounded by antique shops and luxury chocolatiers.", "bestTime": "Hafta sonu", "tips": "Hafta sonları antika pazarı kurulur.", "tips_en": "Antique market is set up on weekends."},
    {"name": "Place Sainte-Catherine", "name_en": "St. Catherine Square", "area": "Sainte-Catherine", "category": "Meydan", "tags": ["balık", "kilise", "canlı"], "lat": 50.8510, "lng": 4.3480, "price": "free", "rating": 4.6, "description": "Eski liman bölgesi, şimdi balık restoranları ve kafelerle dolu.", "description_en": "Old port area, now filled with fish restaurants and cafes.", "bestTime": "Akşam", "tips": "Noel zamanı buradaki pazar çok güzel olur.", "tips_en": "Market here is very nice at Christmas."},
    {"name": "Marolles Flea Market", "name_en": "Jeu de Balle Flea Market", "area": "Marolles", "category": "Alışveriş", "tags": ["bit pazarı", "vintage", "yerel"], "lat": 50.8365, "lng": 4.3455, "price": "free", "rating": 4.5, "description": "Place du Jeu de Balle'de her gün kurulan ünlü bit pazarı.", "description_en": "Famous flea market set up every day at Place du Jeu de Balle.", "bestTime": "Sabah", "tips": "Erken saatte gidip hazine avına çıkın.", "tips_en": "Go early and go treasure hunting."},
    {"name": "Tintin Comic Mural", "name_en": "Tintin Mural", "area": "Merkez", "category": "Sanat", "tags": ["sokak sanatı", "tenten", "haddock"], "lat": 50.8455, "lng": 4.3505, "price": "free", "rating": 4.6, "description": "Tenten ve Kaptan Haddock'u yangın merdiveninden inerken gösteren ikonik duvar resmi.", "description_en": "Iconic mural showing Tintin and Captain Haddock descending the fire escape.", "bestTime": "Gündüz", "tips": "Stoofstraat (Rue de l'Etuve) üzerindedir.", "tips_en": "Located on Stoofstraat (Rue de l'Etuve)."}
]

def enrich_comprehensive():
    filepath = 'assets/cities/bruksel.json'
    all_new = batch_1 + batch_2 + batch_3 + batch_4 + batch_5
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('é', 'e').replace('à', 'a').replace('.', '')
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        place['distanceFromCenter'] = place.get('distanceFromCenter', 1.0)
        places_to_add.append(place)
        time.sleep(0.3)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places to Brüksel.")

if __name__ == "__main__":
    enrich_comprehensive()
