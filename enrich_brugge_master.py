import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Bruges Belgium", f"{place_name} Brugge", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:5000@51.2093,3.2247"
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

# BATCH 1: Meydanlar & Tarihi Yapılar (Ek)
batch_1 = [
    {"name": "Jan van Eyckplein", "name_en": "Jan van Eyck Square", "area": "Merkez", "category": "Meydan", "tags": ["meydan", "heykeltıraş", "tarihi"], "lat": 51.2115, "lng": 3.2260, "price": "free", "rating": 4.6, "description": "Ünlü ressam Jan van Eyck'in heykelinin bulunduğu tarihi meydan.", "description_en": "Historic square featuring the statue of famous painter Jan van Eyck.", "bestTime": "Gündüz", "tips": "Eski gümrük binasını inceleyin.", "tips_en": "Check out the old customs house."},
    {"name": "Sint-Janshospitaal", "name_en": "St John's Hospital", "area": "Merkez", "category": "Müze", "tags": ["hastane", "memling", "tarihi"], "lat": 51.2045, "lng": 3.2240, "price": "medium", "rating": 4.7, "description": "Avrupa'nın en eski hastanelerinden biri, şimdi Memling müzesi.", "description_en": "One of Europe's oldest hospitals, now Memling museum.", "bestTime": "Gündüz", "tips": "Eski eczane bölümü çok ilginç.", "tips_en": "Old pharmacy section is very interesting."},
    {"name": "Bonifacius Bridge", "name_en": "Bonifacius Bridge", "area": "Merkez", "category": "Manzara", "tags": ["köprü", "romantik", "fotoğraf"], "lat": 51.2048, "lng": 3.2255, "price": "free", "rating": 4.9, "description": "Brugge'ün en romantik ve fotojenik köprüsü.", "description_en": "Bruges' most romantic and photogenic bridge.", "bestTime": "Sabah", "tips": "Kanal turu teknelerini buradan izleyin.", "tips_en": "Watch canal tour boats from here."},
    {"name": "Jeruzalemkerk", "name_en": "Jerusalem Chapel", "area": "St. Anna", "category": "Tarihi", "tags": ["kilise", "özel", "gotik"], "lat": 51.2135, "lng": 3.2325, "price": "low", "rating": 4.5, "description": "Adornes ailesi tarafından yaptırılan özel şapel.", "description_en": "Private chapel built by the Adornes family.", "bestTime": "Gündüz", "tips": "Kafatası sunağı ilginç bir detay.", "tips_en": "Skull altar is an interesting detail."},
    {"name": "Gentpoort", "name_en": "Gate of Ghent", "area": "Ring", "category": "Tarihi", "tags": ["kapı", "sur", "ortaçağ"], "lat": 51.2010, "lng": 3.2350, "price": "low", "rating": 4.4, "description": "Şehrin kalan dört ortaçağ kapısından biri.", "description_en": "One of the remaining four medieval gates of the city.", "bestTime": "Gündüz", "tips": "Kuleye çıkıp kanalı izleyebilirsiniz.", "tips_en": "You can climb the tower and watch the canal."}
]

# BATCH 2: Müzeler & İlginç Yerler
batch_2 = [
    {"name": "Torture Museum Oude Steen", "name_en": "Torture Museum", "area": "Merkez", "category": "Müze", "tags": ["işkence", "tarih", "karanlık"], "lat": 51.2080, "lng": 3.2270, "price": "medium", "rating": 4.2, "description": "Eski bir hapishanede işkence aletleri sergisi.", "description_en": "Exhibition of torture instruments in an old prison.", "bestTime": "Gündüz", "tips": "Çocuklar için biraz ürkütücü olabilir.", "tips_en": "Might be a bit scary for children."},
    {"name": "Lumina Domestica", "name_en": "Lamp Museum", "area": "Wijnzakstraat", "category": "Müze", "tags": ["lamba", "ışık", "koleksiyon"], "lat": 51.2095, "lng": 3.2250, "price": "medium", "rating": 4.3, "description": "Dünyanın en büyük lamba koleksiyonlarından biri.", "description_en": "One of the world's largest lamp collections.", "bestTime": "Gündüz", "tips": "Choco-Story ile aynı binada.", "tips_en": "In the same building as Choco-Story."},
    {"name": "Gruuthusemuseum", "name_en": "Gruuthusemuseum", "area": "Merkez", "category": "Müze", "tags": ["saray", "tarih", "lüks"], "lat": 51.2050, "lng": 3.2250, "price": "medium", "rating": 4.6, "description": "Brugge lordlarının lüks yaşamını sergileyen saray.", "description_en": "Palace showcasing the luxurious life of Bruges lords.", "bestTime": "Gündüz", "tips": "Özel şapelden kiliseyi görebilirsiniz.", "tips_en": "You can see the church from the private chapel."},
    {"name": "Godshuizen", "name_en": "Almshouses", "area": "Çeşitli", "category": "Tarihi", "tags": ["evler", "beyaz", "bahçe"], "lat": 51.2030, "lng": 3.2200, "price": "free", "rating": 4.7, "description": "Yaşlılar için yapılmış tarihi beyaz evler ve huzurlu bahçeleri.", "description_en": "Historic white houses built for the elderly and their peaceful gardens.", "bestTime": "Gündüz", "tips": "Sessiz olun, insanlar hala yaşıyor.", "tips_en": "Be quiet, people still live there."}
]

# BATCH 3: Yeme & İçme
batch_3 = [
    {"name": "De Garre", "name_en": "De Garre", "area": "Merkez", "category": "Bar", "tags": ["bira", "gizli", "yerel"], "lat": 51.2083, "lng": 3.2242, "price": "medium", "rating": 4.8, "description": "Dar bir sokakta gizlenmiş, kendi birasını üreten efsanevi bar.", "description_en": "Legendary bar hidden in a narrow alley, brewing its own beer.", "bestTime": "Akşam", "tips": "Garre birası (11%) sadece burada var, yanında peynirle gelir.", "tips_en": "Garre beer (11%) is only available here, comes with cheese."},
    {"name": "'t Brugs Beertje", "name_en": "'t Brugs Beertje", "area": "Merkez", "category": "Bar", "tags": ["bira", "pub", "çeşit"], "lat": 51.2060, "lng": 3.2210, "price": "medium", "rating": 4.7, "description": "300'den fazla Belçika birası sunan kült bir mekan.", "description_en": "Cult venue offering over 300 Belgian beers.", "bestTime": "Gece", "tips": "Personelden tavsiye isteyin, menü ansiklopedi gibi.", "tips_en": "Ask staff for advice, menu is like an encyclopedia."},
    {"name": "Otto Waffle Atelier", "name_en": "Otto Waffle Atelier", "area": "Merkez", "category": "Kafe", "tags": ["waffle", "yulaf", "farklı"], "lat": 51.2040, "lng": 3.2230, "price": "medium", "rating": 4.6, "description": "Dantel şeklinde özel yulaf waffle'ları.", "description_en": "Special oat waffles in lace shape.", "bestTime": "Öğle", "tips": "Klasik waffle'dan daha hafif ve çıtır.", "tips_en": "Lighter and crispier than classic waffle."},
    {"name": "The Chocolate Line", "name_en": "The Chocolate Line", "area": "Merkez", "category": "Alışveriş", "tags": ["çikolata", "gurme", "deneysel"], "lat": 51.2065, "lng": 3.2220, "price": "high", "rating": 4.7, "description": "Dominique Persoone'un çılgın ve ödüllü çikolataları.", "description_en": "Dominique Persoone's crazy and award-winning chocolates.", "bestTime": "Gündüz", "tips": "Wasabi veya soğanlı çikolata deneyin.", "tips_en": "Try wasabi or onion chocolate."},
    {"name": "Frituur De Halve Maan", "name_en": "Frituur De Halve Maan", "area": "Beguinage", "category": "Sokak Lezzeti", "tags": ["patates", "kızartma", "hızlı"], "lat": 51.2020, "lng": 3.2245, "price": "low", "rating": 4.5, "description": "Bira fabrikasının yanında harika Belçika patatesi.", "description_en": "Great Belgian fries next to the brewery.", "bestTime": "Öğle", "tips": "Mayonezli sosla isteyin.", "tips_en": "Ask with mayonnaise sauce."}
]

# BATCH 4: Parklar & Diğer
batch_4 = [
    {"name": "Koningin Astridpark", "name_en": "Queen Astrid Park", "area": "Merkez", "category": "Park", "tags": ["park", "sakin", "yerel"], "lat": 51.2060, "lng": 3.2300, "price": "free", "rating": 4.6, "description": "Turistlerden uzak, göletli ve sakin bir park.", "description_en": "Quiet park with a pond, away from tourists.", "bestTime": "Gündüz", "tips": "'In Bruges' filminin meşhur sahnesi burada çekildi.", "tips_en": "Famous scene from 'In Bruges' movie was shot here."},
    {"name": "Sint-Janshuismolen", "name_en": "Sint-Janshuis Mill", "area": "Kruisvest", "category": "Tarihi", "tags": ["yel değirmeni", "müze", "manzara"], "lat": 51.2160, "lng": 3.2380, "price": "low", "rating": 4.6, "description": "Hala un öğüten ve içine girilebilen tarihi yel değirmeni.", "description_en": "Historic windmill that still grinds flour and can be entered.", "bestTime": "Gündüz", "tips": "Rüzgarlı günlerde kanatların dönüşünü izleyin.", "tips_en": "Watch the blades turn on windy days."},
    {"name": "Concertgebouw", "name_en": "Concert Hall", "area": "'t Zand", "category": "Sanat", "tags": ["konser", "modern", "mimari"], "lat": 51.2035, "lng": 3.2180, "price": "variable", "rating": 4.5, "description": "Modern mimarisiyle dikkat çeken konser ve etkinlik salonu.", "description_en": "Concert and event hall notable for its modern architecture.", "bestTime": "Akşam", "tips": "Çatı katından şehir manzarası güzel.", "tips_en": "City view from the roof is nice."},
    {"name": "'t Zand", "name_en": "'t Zand Square", "area": "Merkez", "category": "Meydan", "tags": ["meydan", "büyük", "fıskiye"], "lat": 51.2040, "lng": 3.2190, "price": "free", "rating": 4.4, "description": "Şehrin en büyük meydanı, altında otopark var.", "description_en": "City's largest square, with parking underneath.", "bestTime": "Cumartesi", "tips": "Cumartesi günleri kurulan pazarı kaçırmayın.", "tips_en": "Don't miss the market held on Saturdays."},
    {"name": "Bourgogne des Flandres Brewery", "name_en": "Bourgogne des Flandres", "area": "Merkez", "category": "Deneyim", "tags": ["bira", "fabrika", "kanal"], "lat": 51.2075, "lng": 3.2260, "price": "medium", "rating": 4.6, "description": "Kanal kenarında romantik bira fabrikası.", "description_en": "Romantic brewery by the canal.", "bestTime": "İkindi", "tips": "Terasta kanal manzarası eşliğinde bira için.", "tips_en": "Drink beer on the terrace with canal view."}
]

def enrich():
    filepath = 'assets/cities/brugge.json'
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('(', '').replace(')', '').replace('.', '')
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
