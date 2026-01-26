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

# BATCH 7: HIKING CABINS & NATURE (Orman Kulübeleri ve Doğa)
cabins = [
    {"name": "Ullevålseter", "category": "Yeme İçme", "tags": ["ormaniçi", "waffle", "popüler"], "description": "Nordmarka ormanının kalbinde, yürüyüşçülerin uğrak noktası olan kafe."},
    {"name": "Skjennungstua", "category": "Yeme İçme", "tags": ["manzara", "kulübe", "tatlı"], "description": "Tepede yer alan ve harika manzarası olan popüler bir orman kulübesi."},
    {"name": "Frognerseteren", "category": "Restoran", "tags": ["tarihi", "elmalı kek", "manzara"], "description": "Şehre tepeden bakan, geleneksel Norveç mimarisi ve elmalı kekiyle ünlü yer."},
    {"name": "Rustadsaga", "category": "Yeme İçme", "tags": ["Nøklevann", "kulübe", "göl"], "description": "Nøklevann gölü kıyısında, sıcak çikolatasıyla meşhur durak."},
    {"name": "Mariholtet Sportsstue", "category": "Yeme İçme", "tags": ["doğa", "bisiklet", "mola"], "description": "Østmarka ormanının derinliklerinde,sporcuların mola yeri."},
    {"name": "Kikutstua", "category": "Konaklama", "tags": ["uzak", "kayak", "efsane"], "description": "Kışın kayakçıların, yazın bisikletçilerin ana hedefi olan büyük kulübe."},
    {"name": "Kobberhaughytta", "category": "Konaklama", "tags": ["manzara", "turist derneği", "modern"], "description": "DNT'ye ait, modern ve manzaralı dağ evi."},
    {"name": "Lilloseter", "category": "Yeme İçme", "tags": ["kuzey", "sakin", "orman"], "description": "Lillomarka ormanında sakin bir dinlenme noktası."},
    {"name": "Sandbakken Sportsstue", "category": "Yeme İçme", "tags": ["doğu", "tarihi", "waffle"], "description": "Østmarka'nın doğusunda tarihi bir spor kulübesi."},
    {"name": "Vangen Skistue", "category": "Yeme İçme", "tags": ["çiftlik", "hayvanlar", "aile"], "description": "Çiftlik hayvanlarının da olduğu, aileler için ideal bir yer."}
]

# BATCH 8: MORE STATUES & LANDMARKS
extra_statues = [
    {"name": "Oslo Opera House Roof", "category": "Manzara", "tags": ["mermer", "yürüyüş", "ikonik"], "description": "Opera binasının çatısında yürümek Oslo'nun olmazsa olmazı."},
    {"name": "Old Aker Church Cemetery", "category": "Tarih", "tags": ["mezarlık", "ünlüler", "tarihi"], "description": "Munch ve Ibsen gibi ünlülerin mezarlarının olduğu tarihi mezarlık (Vår Frelsers)."},
    {"name": "Botanisering (The Sprout)", "category": "Sanat", "tags": ["heykel", "botanik", "bronz"], "description": "Botanik bahçesindeki ilginç filiz heykeli."},
    {"name": "Peer Gynt Sculpture Park", "category": "Sanat", "tags": ["ibsen", "park", "tiyatro"], "description": "Løren bölgesinde, Ibsen'in Peer Gynt oyunundan sahnelerin olduğu park."},
    {"name": "Oslo Lions (Stortinget)", "category": "Simge", "tags": ["aslan", "parlamento", "taş"], "description": "Parlamento binasının önündeki ikonik taş aslanlar."},
    {"name": "Abel Monument", "category": "Simge", "tags": ["matematik", "ünlü", "saray"], "description": "Saray parkında, ünlü matematikçi Niels Henrik Abel'in anıtı."},
    {"name": "Wergeland Statue", "category": "Simge", "tags": ["şair", "milli", "tarih"], "description": "Norveç'in milli şairi Henrik Wergeland'ın heykeli."},
    {"name": "Holberg Statue", "category": "Simge", "tags": ["tiyatro", "yazar", "ulusal"], "description": "Ulusal Tiyatro'nun önündeki Ludvig Holberg heykeli."},
    {"name": "The Glove (Hansk)", "category": "Simge", "tags": ["eldiven", "kuruluş", "efsane"], "description": "Kral Christian IV'ün şehri kurduğu yeri işaret eden eldiven heykeli (Christiania Torv)."}
]

# BATCH 9: MORE SHOPS & LOCAL SPOTS
extra_shops = [
    {"name": "Fons", "category": "Alışveriş", "tags": ["vintage", "seçkin", "moda"], "description": "Özenle seçilmiş vintage parçalar."},
    {"name": "Robot", "category": "Alışveriş", "tags": ["retro", "plak", "giyim"], "description": "Hem kıyafet hem plak satan kült dükkan."},
    {"name": "Lush Dive", "category": "Alışveriş", "tags": ["kırtasiye", "tasarım", "defter"], "description": "Nitelikli kırtasiye ve tasarım ürünleri."},
    {"name": "Heaven Scent", "category": "Alışveriş", "tags": ["kozmetik", "niş", "parfüm"], "description": "Niş parfümler ve kozmetik ürünleri."},
    {"name": "Dapper", "category": "Alışveriş", "tags": ["erkek", "berber", "bisiklet"], "description": "Erkek giyim, berber ve bisiklet dükkanı bir arada."},
    {"name": "Chillout Travel Store", "category": "Alışveriş", "tags": ["seyahat", "kitap", "kafe"], "description": "Seyahat temalı kitapçı ve ekipman mağazası."},
    {"name": "Røtter St. Hanshaugen", "category": "Alışveriş", "tags": ["organik", "market", "sağlık"], "description": "En iyi organik ve doğal ürünler marketi."},
    {"name": "Gutta på Haugen", "category": "Alışveriş", "tags": ["şarküteri", "gurme", "peynir"], "description": "Lüks şarküteri ve gurme ürünler."},
    {"name": "Fiskeriet Shop", "category": "Alışveriş", "tags": ["balık", "taze", "deniz"], "description": "En taze deniz ürünlerini alabileceğiniz balıkçı."},
    {"name": "Strøget", "category": "Gece Hayatı", "tags": ["pasaj", "bar", "gizli"], "description": "Birçok barın olduğu, üzeri açık gizli pasaj."}
]

def enrich_gap():
    filepath = 'assets/cities/oslo.json'
    all_new = cabins + extra_statues + extra_shops
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('ø', 'o').replace('å', 'a').replace('.', '').replace('æ', 'ae').replace('(', '').replace(')', '')
        place['price'] = place.get('price', 'medium')
        place['rating'] = 4.5
        place['bestTime'] = 'Gündüz'
        place['tips'] = 'Ziyaret öncesi saatleri kontrol edin.'
        
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        place['distanceFromCenter'] = place.get('distanceFromCenter', 1.0)
        places_to_add.append(place)
        time.sleep(0.2)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places to Oslo. GAP CLOSED!")

if __name__ == "__main__":
    enrich_gap()
