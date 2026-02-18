import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Bologna Italy", f"{place_name} Bologna", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:15000@44.4942,11.3464"
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

# BATCH 1: Ana Meydanlar & Tarihi Yapılar
batch_1 = [
    {"name": "Piazza Maggiore", "name_en": "Piazza Maggiore", "area": "Merkez", "category": "Meydan", "tags": ["meydan", "merkez", "tarihi"], "lat": 44.4938, "lng": 11.3428, "price": "free", "rating": 4.8, "description": "Bologna'nın kalbi, Orta Çağ mimarisiyle çevrili ana meydan.", "description_en": "Heart of Bologna, main square surrounded by medieval architecture.", "bestTime": "Akşam", "tips": "Sokak müzisyenlerini dinleyin.", "tips_en": "Listen to street musicians."},
    {"name": "Basilica di San Petronio", "name_en": "Basilica di San Petronio", "area": "Piazza Maggiore", "category": "Tarihi", "tags": ["bazilika", "gotik", "kilise"], "lat": 44.4937, "lng": 11.3432, "price": "free", "rating": 4.7, "description": "Dünyanın 10. büyük kilisesi, yarım kalmış cephesiyle ünlü.", "description_en": "World's 10th largest church, famous for unfinished facade.", "bestTime": "Gündüz", "tips": "İçerideki güneş meridyeni dikkat çekici.", "tips_en": "Solar meridian inside is remarkable."},
    {"name": "Fontana del Nettuno", "name_en": "Neptune Fountain", "area": "Piazza Nettuno", "category": "Tarihi", "tags": ["çeşme", "rönesans", "simge"], "lat": 44.4941, "lng": 11.3425, "price": "free", "rating": 4.6, "description": "Giambologna'nın 1567 yapımı Neptün heykeli.", "description_en": "Giambologna's 1567 Neptune statue.", "bestTime": "Gündüz", "tips": "Şehrin sembolü, fotoğraf için ideal.", "tips_en": "City symbol, ideal for photos."},
    {"name": "Le Due Torri (Asinelli & Garisenda)", "name_en": "The Two Towers", "area": "Merkez", "category": "Manzara", "tags": ["kule", "ortaçağ", "panorama"], "lat": 44.4944, "lng": 11.3473, "price": "medium", "rating": 4.9, "description": "Bologna'nın ikonik ikiz kuleleri, Asinelli 97 metre.", "description_en": "Bologna's iconic twin towers, Asinelli is 97m.", "bestTime": "Gün batımı", "tips": "498 basamak, muhteşem manzara.", "tips_en": "498 steps, amazing view."},
    {"name": "Basilica di Santo Stefano", "name_en": "Basilica di Santo Stefano", "area": "Santo Stefano", "category": "Tarihi", "tags": ["kilise", "yedi kilise", "bizans"], "lat": 44.4909, "lng": 11.3497, "price": "free", "rating": 4.8, "description": "Yedi Kilise kompleksi, Bologna'nın en eski yapısı.", "description_en": "Seven Churches complex, Bologna's oldest structure.", "bestTime": "Sabah", "tips": "Sessiz avlu çok huzurlu.", "tips_en": "Quiet courtyard is very peaceful."}
]

# BATCH 2: Müzeler & Kültür
batch_2 = [
    {"name": "Palazzo dell'Archiginnasio", "name_en": "Archiginnasio Palace", "area": "Merkez", "category": "Müze", "tags": ["üniversite", "anatomi", "kütüphane"], "lat": 44.4929, "lng": 11.3438, "price": "low", "rating": 4.7, "description": "Eski üniversite binası, tarihi anatomi tiyatrosu.", "description_en": "Old university building, historic anatomy theater.", "bestTime": "Gündüz", "tips": "Anatomi odası mutlaka görülmeli.", "tips_en": "Anatomy room is a must-see."},
    {"name": "Pinacoteca Nazionale", "name_en": "National Art Gallery", "area": "Merkez", "category": "Müze", "tags": ["sanat", "resim", "rönesans"], "lat": 44.4960, "lng": 11.3520, "price": "medium", "rating": 4.5, "description": "Bologna okulu tablolarının en iyi koleksiyonu.", "description_en": "Best collection of Bolognese school paintings.", "bestTime": "Gündüz", "tips": "Rafael, Carracci eserleri mevcut.", "tips_en": "Works by Raphael, Carracci available."},
    {"name": "Museo Civico Archeologico", "name_en": "Archaeological Museum", "area": "Merkez", "category": "Müze", "tags": ["arkeoloji", "etrüsk", "mısır"], "lat": 44.4937, "lng": 11.3422, "price": "medium", "rating": 4.4, "description": "Etrüsk ve Mısır koleksiyonlarıyla zengin müze.", "description_en": "Museum rich with Etruscan and Egyptian collections.", "bestTime": "Gündüz", "tips": "Etrüsk bölümü çok ilginç.", "tips_en": "Etruscan section is very interesting."},
    {"name": "Museo della Storia di Bologna", "name_en": "Bologna History Museum", "area": "Merkez", "category": "Müze", "tags": ["tarih", "interaktif", "şehir"], "lat": 44.4945, "lng": 11.3400, "price": "medium", "rating": 4.5, "description": "Bologna tarihini anlatan interaktif müze.", "description_en": "Interactive museum telling Bologna's history.", "bestTime": "Gündüz", "tips": "Multimedya sunumları çok iyi.", "tips_en": "Multimedia presentations are excellent."}
]

# BATCH 3: Gizli Güzellikler & Manzara
batch_3 = [
    {"name": "Finestrella (Venedik Penceresi)", "name_en": "Finestrella (Little Venice)", "area": "Via Piella", "category": "Manzara", "tags": ["kanal", "gizli", "fotoğraf"], "lat": 44.4980, "lng": 11.3400, "price": "free", "rating": 4.7, "description": "Bologna'nın gizli kanallarını gösteren küçük pencere.", "description_en": "Small window showing Bologna's hidden canals.", "bestTime": "Gündüz", "tips": "Via Piella'da arayın, kolay kaçırılır.", "tips_en": "Look for it on Via Piella, easy to miss."},
    {"name": "Santuario di San Luca", "name_en": "Sanctuary of San Luca", "area": "Colle della Guardia", "category": "Tarihi", "tags": ["bazilika", "tepe", "revak"], "lat": 44.4789, "lng": 11.2997, "price": "free", "rating": 4.9, "description": "666 revaklı dünyanın en uzun üstü kapalı yürüyüş yoluyla ulaşılan bazilika.", "description_en": "Basilica reached by world's longest covered walkway with 666 arcades.", "bestTime": "Gün batımı", "tips": "Şehir panoraması muhteşem.", "tips_en": "City panorama is magnificent."},
    {"name": "Portico di San Luca", "name_en": "Portico di San Luca", "area": "Colle della Guardia", "category": "Yürüyüş", "tags": ["revak", "yürüyüş", "unesco"], "lat": 44.4850, "lng": 11.3100, "price": "free", "rating": 4.8, "description": "3.8 km uzunluğunda UNESCO listesindeki revaklı yol.", "description_en": "3.8km UNESCO-listed porticoed walkway.", "bestTime": "Sabah", "tips": "Yaklaşık 1 saat yürüyüş.", "tips_en": "About 1 hour walk."},
    {"name": "Giardini Margherita", "name_en": "Margherita Gardens", "area": "Güney", "category": "Park", "tags": ["park", "yeşil", "piknik"], "lat": 44.4833, "lng": 11.3533, "price": "free", "rating": 4.5, "description": "Bologna'nın en büyük parkı, yerellerle dolu.", "description_en": "Bologna's largest park, full of locals.", "bestTime": "İkindi", "tips": "Hafta sonu piknik için ideal.", "tips_en": "Ideal for weekend picnic."}
]

# BATCH 4: Yeme-İçme
batch_4 = [
    {"name": "Quadrilatero (Eski Pazar)", "name_en": "Quadrilatero Market", "area": "Merkez", "category": "Alışveriş", "tags": ["pazar", "yiyecek", "ortaçağ"], "lat": 44.4950, "lng": 11.3450, "price": "variable", "rating": 4.7, "description": "Ortaçağ'dan kalma dar sokaklarda gıda pazarı.", "description_en": "Food market in narrow medieval streets.", "bestTime": "Sabah", "tips": "Sabah erken en canlı zaman.", "tips_en": "Early morning is liveliest."},
    {"name": "Osteria dell'Orsa", "name_en": "Osteria dell'Orsa", "area": "Üniversite", "category": "Restoran", "tags": ["osteria", "öğrenci", "ekonomik"], "lat": 44.4965, "lng": 11.3480, "price": "low", "rating": 4.6, "description": "Öğrenci favorisi, otantik Bolognese mutfağı.", "description_en": "Student favorite, authentic Bolognese cuisine.", "bestTime": "Öğle", "tips": "Tagliatelle al ragù kesinlikle deneyin.", "tips_en": "Definitely try tagliatelle al ragù."},
    {"name": "Trattoria Anna Maria", "name_en": "Trattoria Anna Maria", "area": "Merkez", "category": "Restoran", "tags": ["trattoria", "geleneksel", "tortellini"], "lat": 44.4960, "lng": 11.3420, "price": "medium", "rating": 4.8, "description": "Efsanevi tortellini servisi, duvarlar ünlülerin fotoğraflarıyla dolu.", "description_en": "Legendary tortellini service, walls full of celebrity photos.", "bestTime": "Akşam", "tips": "Kesinlikle rezervasyon yapın.", "tips_en": "Definitely make reservation."},
    {"name": "Mercato di Mezzo", "name_en": "Mercato di Mezzo", "area": "Quadrilatero", "category": "Sokak Lezzeti", "tags": ["pazar", "gıda salonu", "yeme"], "lat": 44.4948, "lng": 11.3455, "price": "medium", "rating": 4.5, "description": "Ortaçağ binasında modern yiyecek salonu.", "description_en": "Modern food hall in medieval building.", "bestTime": "Öğle", "tips": "Her stanttan bir şey deneyin.", "tips_en": "Try something from every stall."},
    {"name": "Sfoglia Rina", "name_en": "Sfoglia Rina", "area": "Merkez", "category": "Restoran", "tags": ["pasta", "taze", "geleneksel"], "lat": 44.4942, "lng": 11.3445, "price": "medium", "rating": 4.6, "description": "Günlük taze el yapımı makarna.", "description_en": "Daily fresh handmade pasta.", "bestTime": "Öğle", "tips": "Makarna yapımını izleyebilirsiniz.", "tips_en": "You can watch pasta being made."},
    {"name": "Cremeria Funivia", "name_en": "Cremeria Funivia", "area": "San Luca", "category": "Tatlı", "tags": ["gelato", "dondurma", "yerel"], "lat": 44.4870, "lng": 11.3280, "price": "low", "rating": 4.7, "description": "San Luca yürüyüşünden sonra mükemmel gelato.", "description_en": "Perfect gelato after San Luca walk.", "bestTime": "İkindi", "tips": "Pistacchio en popüler.", "tips_en": "Pistachio is most popular."}
]

# BATCH 5: Bar & Kafeler
batch_5 = [
    {"name": "Caffè Terzi", "name_en": "Caffè Terzi", "area": "Merkez", "category": "Kafe", "tags": ["kahve", "espresso", "butik"], "lat": 44.4940, "lng": 11.3460, "price": "medium", "rating": 4.7, "description": "Bologna'nın en iyi espressosu.", "description_en": "Bologna's best espresso.", "bestTime": "Sabah", "tips": "Özel kahve çekirdeği satıyorlar.", "tips_en": "They sell specialty coffee beans."},
    {"name": "Le Stanze", "name_en": "Le Stanze", "area": "Merkez", "category": "Bar", "tags": ["bar", "fresk", "atmosfer"], "lat": 44.4920, "lng": 11.3500, "price": "medium", "rating": 4.5, "description": "15. yüzyıl freskli şapelde kokteyl barı.", "description_en": "Cocktail bar in 15th century chapel with frescoes.", "bestTime": "Akşam", "tips": "Muhteşem atmosfer, aperitivo harika.", "tips_en": "Amazing atmosphere, aperitivo is great."},
    {"name": "Camera a Sud", "name_en": "Camera a Sud", "area": "Merkez", "category": "Bar", "tags": ["bar", "kokteyl", "hipster"], "lat": 44.4955, "lng": 11.3470, "price": "medium", "rating": 4.4, "description": "Bohemian atmosferli kokteyl barı.", "description_en": "Cocktail bar with bohemian atmosphere.", "bestTime": "Gece", "tips": "DJ geceleri çok eğlenceli.", "tips_en": "DJ nights are very fun."}
]

def enrich():
    filepath = 'assets/cities/bologna.json'
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('(', '').replace(')', '').replace('&', 'and')
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
