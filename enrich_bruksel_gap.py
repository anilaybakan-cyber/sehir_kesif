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

# BATCH 7: LAST PUSH (Kalan Çizgi Roman Duvarları ve Diğerleri)
extra_comics = [
    {"name": "Quick & Flupke Mural", "category": "Sanat", "tags": ["yaramaz", "polis", "komik"], "description": "Tenten'in yaratıcısından iki haylaz çocuğun maceraları."},
    {"name": "Odilon Verjus Mural", "category": "Sanat", "tags": ["rahip", "misyoner", "macera"], "description": "Maceracı rahip Odilon Verjus ve yardımcısı."},
    {"name": "Blondin & Cirage Mural", "category": "Sanat", "tags": ["arkadaş", "klasik", "macera"], "description": "Jijé'nin ünlü ikilisi."},
    {"name": "Passe-Moi L'Ciel Mural", "category": "Sanat", "tags": ["cennet", "komik", "melek"], "description": "Aziz Petrus ve cennetin kapısındaki komik olaylar."},
    {"name": "La Patrouille des Castors Mural", "category": "Sanat", "tags": ["izci", "macera", "takım"], "description": "İzci grubunun maceraları."},
    {"name": "Jojo Mural", "category": "Sanat", "tags": ["çocuk", "duygusal", "sakin"], "description": "André Geerts'in sevimli karakteri Jojo."},
    {"name": "Le Roi des Mouches Mural", "category": "Sanat", "tags": ["alternatif", "modern", "inek"], "description": "Sıradışı ve modern bir çizgi roman karakteri."},
    {"name": "Lincoln Mural", "category": "Sanat", "tags": ["kovboy", "huysuz", "komik"], "description": "Huysuz kovboy Lincoln."},
    {"name": "Koko Bill Mural", "category": "Sanat", "tags": ["kuş", "komik", "renkli"], "description": "Komik kuş Koko Bill."},
    {"name": "Froud & Stouf Mural", "category": "Sanat", "tags": ["köpek", "felsefe", "mavi"], "description": "İki mavi köpeğin felsefi sohbetleri."},
    {"name": "Gile Jourdan Mural", "category": "Sanat", "tags": ["dedektif", "klasik", "araba"], "description": "Özel dedektif Gil Jourdan."},
    {"name": "Natacha Mural", "category": "Sanat", "tags": ["hostes", "macera", "ikonik"], "description": "Maceracı hostes Natacha."},
    {"name": "Martine Mural", "category": "Sanat", "tags": ["çocuk", "klasik", "kitap"], "description": "Çocuk kitaplarının ünlü kahramanı Martine (Ayşegül)."},
    {"name": "Spike and Suzy Mural (Bob et Bobette)", "category": "Sanat", "tags": ["aile", "macera", "ünlü"], "description": "Willy Vandersteen'in ünlü kahramanları."},
    {"name": "Cubitus Mural 2", "category": "Sanat", "tags": ["köpek", "büyük", "komik"], "description": "Cubitus'un bir başka duvar resmi."}
]

# BATCH 8: MORE SPECIALTY SHOPS & SPOTS
shops_spots = [
    {"name": "Maison Dandoy - Grand Place", "category": "Tatlı", "tags": ["bisküvi", "speculoos", "tarihi"], "description": "Brüksel'in en ünlü ve tarihi bisküvi üreticisi."},
    {"name": "Pierre Marcolini - Sablon", "category": "Tatlı", "tags": ["çikolata", "lüks", "ödüllü"], "description": "Dünyanın en iyi çikolatacılarından biri."},
    {"name": "Neuhaus - Galerie de la Reine", "category": "Tatlı", "tags": ["çikolata", "pralin", "ilk"], "description": "Pralinin mucidi, orijinal mağaza."},
    {"name": "Mary Chocolatier", "category": "Tatlı", "tags": ["kraliyet", "çikolata", "zarif"], "description": "Belçika Kraliyet Ailesi'nin tedarikçisi."},
    {"name": "Elisabeth Chocolatier", "category": "Tatlı", "tags": ["mereng", "çikolata", "hediyelik"], "description": "Dev merengleri ve kaliteli çikolatalarıyla ünlü."},
    {"name": "Le Comptoir de Mathilde", "category": "Alışveriş", "tags": ["gurme", "çikolata", "sos"], "description": "Fransız ve Belçika gurme ürünleri."},
    {"name": "Dille & Kamille", "category": "Alışveriş", "tags": ["ev", "mutfak", "doğal"], "description": "Doğal malzemelerden mutfak ve ev gereçleri."},
    {"name": "Pêle-Mêle Ixelles", "category": "Alışveriş", "tags": ["kitap", "ikinci el", "ucuz"], "description": "Devasa ikinci el kitapçı."},
    {"name": "Filigranes", "category": "Alışveriş", "tags": ["kitap", "kafe", "etkinlik"], "description": "Brüksel'in en büyük ve en canlı kitapçısı, içinde kafe var."},
    {"name": "Tropismes", "category": "Alışveriş", "tags": ["kitap", "pasaj", "güzel"], "description": "Galeries Royales'de, dünyanın en güzel kitapçılarından biri."},
    {"name": "Caméléon", "category": "Alışveriş", "tags": ["outlet", "giyim", "büyük"], "description": "Devasa marka outlet mağazası."},
    {"name": "Woluwe Shopping Center", "category": "Alışveriş", "tags": ["avm", "modern", "çeşit"], "description": "Şehrin en büyük alışveriş merkezlerinden biri."},
    {"name": "Rob The Gourmets' Market", "category": "Alışveriş", "tags": ["gurme", "lüks", "yiyecek"], "description": "Lüks gıda ürünleri ve şaraplar için bir cennet."},
    {"name": "Place Jourdan Market", "category": "Pazar", "tags": ["yemek", "pazar", "yerel"], "description": "Pazar günleri kurulan canlı bir pazar."},
    {"name": "Marché du Midi", "category": "Pazar", "tags": ["dev", "ucuz", "çiçek"], "description": "Avrupa'nın en büyük açık hava pazarlarından biri (Pazar günleri)."}
]

# BATCH 9: MORE PARKS & STATUES
extra_nature = [
    {"name": "Parc Leopold", "category": "Park", "tags": ["gölet", "ab", "tarihi"], "description": "Avrupa Parlamentosu'nun arkasında, sakin ve tarihi bir park."},
    {"name": "Parc de Wolvendael", "category": "Park", "tags": ["tepe", "manzara", "ağaç"], "description": "Uccle bölgesinde, inişli çıkışlı büyük bir park."},
    {"name": "Bois de la Cambre", "category": "Doğa", "tags": ["orman", "göl", "bisiklet"], "description": "Şehrin akciğeri, hafta sonları trafiğe kapanan dev orman parkı."},
    {"name": "Rouge-Cloître", "category": "Doğa", "tags": ["manastır", "orman", "sanat"], "description": "Sonian Ormanı'nın kenarında, eski manastır ve sanat merkezi."},
    {"name": "Park Pierre Paulus", "category": "Park", "tags": ["gizli", "ördek", "sakin"], "description": "Saint-Gilles'de küçük ama çok şirin bir park."},
    {"name": "Statue of Brabant", "category": "Simge", "tags": ["heykel", "park", "bronz"], "description": "Cinquantenaire Parkı'ndaki heybetli heykel."},
    {"name": "Monument to the Dynasty", "category": "Simge", "tags": ["anıt", "kraliyet", "laeken"], "description": "Laeken Parkı'ndaki neo-gotik anıt."}
]

def enrich_gap():
    filepath = 'assets/cities/bruksel.json'
    all_new = extra_comics + shops_spots + extra_nature
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('é', 'e').replace('à', 'a').replace('.', '').replace('ç', 'c').replace('&', 'and')
        place['price'] = place.get('price', 'medium')
        place['rating'] = 4.4
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
    print(f"\n✅ Added {len(places_to_add)} new places to Brüksel. GAP CLOSED!")

if __name__ == "__main__":
    enrich_gap()
