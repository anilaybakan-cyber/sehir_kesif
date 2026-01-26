import json
import requests
import time
import urllib.parse
import os

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

# BATCH 1: KİLİSELER VE TARİHİ YAPILAR
batch_1 = [
    {"name": "Cathedral of St. Michael and St. Gudula", "area": "Merkez", "category": "Tarih", "tags": ["katedral", "gotik", "vitray"], "description": "Brüksel'in en önemli katedrali, kraliyet düğünlerine ev sahipliği yapar.", "lat": 50.8478, "lng": 4.3601},
    {"name": "Basilica of the Sacred Heart", "area": "Koekelberg", "category": "Tarih", "tags": ["bazilika", "art deco", "manzara"], "description": "Dünyanın en büyük Art Deco binası, tepesinde panoramik şehir manzarası var.", "lat": 50.8667, "lng": 4.3167},
    {"name": "Notre Dame du Sablon", "area": "Sablon", "category": "Tarih", "tags": ["kilise", "gotik", "sablon"], "description": "Sablon meydanında, muhteşem vitraylara sahip geç Gotik kilise.", "lat": 50.8400, "lng": 4.3560},
    {"name": "Coudenberg Palace", "area": "Royale", "category": "Tarih", "tags": ["yeraltı", "saray", "arkeoloji"], "description": "Günümüz şehrinin altında kalmış eski imparatorluk sarayının kalıntıları.", "lat": 50.8431, "lng": 4.3598},
    {"name": "Church of Saint-Jacques-sur-Coudenberg", "area": "Royale", "category": "Tarih", "tags": ["kilise", "kraliyet", "neoklasik"], "description": "Kraliyet Meydanı'nda yer alan etkileyici neoklasik kilise.", "lat": 50.8423, "lng": 4.3606},
    {"name": "Eglise Sainte-Catherine", "area": "Sainte-Catherine", "category": "Tarih", "tags": ["kilise", "meydan", "tarihi"], "description": "Eski balık pazarı bölgesinin merkezinde yer alan tarihi kilise.", "lat": 50.8520, "lng": 4.3480},
    {"name": "Halle Gate", "area": "Saint-Gilles", "category": "Müze", "tags": ["kale", "ortaçağ", "savunma"], "description": "Brüksel'in ortaçağ surlarından günümüze kalan tek şehir kapısı.", "lat": 50.8333, "lng": 4.3444},
    {"name": "Egmont Palace", "area": "Sablon", "category": "Tarih", "tags": ["saray", "park", "diplomasi"], "description": "Dışişleri Bakanlığı tarafından kullanılan tarihi saray ve halka açık parkı.", "lat": 50.8390, "lng": 4.3570}
]

# BATCH 2: DAHA FAZLA MÜZE (Niş Müzeler)
batch_2 = [
    {"name": "Museum of the City of Brussels", "area": "Grand Place", "category": "Müze", "tags": ["şehir", "tarih", "kralın evi"], "description": "Grand Place'daki Kralın Evi binasında, şehrin tarihini anlatan müze.", "lat": 50.8468, "lng": 4.3524},
    {"name": "GardeRobe MannekenPis", "area": "Merkez", "category": "Müze", "tags": ["kostüm", "manneken pis", "eğlenceli"], "description": "İşeyen Çocuk heykelinin giydiği yüzlerce kostümün sergilendiği müze.", "lat": 50.8450, "lng": 4.3500},
    {"name": "Jewish Museum of Belgium", "area": "Sablon", "category": "Müze", "tags": ["yahudi", "kültür", "tarih"], "description": "Belçika'daki Yahudi toplumunun tarihini ve kültürünü anlatan müze.", "lat": 50.8410, "lng": 4.3540},
    {"name": "Choco-Story Brussels", "area": "Merkez", "category": "Müze", "tags": ["çikolata", "tadım", "yapım"], "description": "Çikolatanın tarihini öğrenip tadım yapabileceğiniz interaktif müze.", "lat": 50.8460, "lng": 4.3510},
    {"name": "Belgian Beer World", "area": "Bourse", "category": "Müze", "tags": ["bira", "borsa", "deneyim"], "description": "Eski Borsa binasında (La Bourse) yeni açılan interaktif bira müzesi.", "lat": 50.8480, "lng": 4.3500},
    {"name": "Sewer Museum", "area": "Anderlecht", "category": "Müze", "tags": ["kanalizasyon", "yeraltı", "ilginç"], "description": "Şehrin altındaki kanalizasyon sistemini gezebileceğiniz sıra dışı müze.", "lat": 50.8350, "lng": 4.3400},
    {"name": "Design Museum Brussels", "area": "Heysel", "category": "Müze", "tags": ["tasarım", "plastik", "modern"], "description": "Atomium'un yanında, modern tasarım ve plastik sanatına odaklanan müze.", "lat": 50.8950, "lng": 4.3400},
    {"name": "Fashion & Lace Museum", "area": "Merkez", "category": "Müze", "tags": ["moda", "dantel", "tekstil"], "description": "Brüksel danteli ve moda tarihine adanmış şık müze.", "lat": 50.8465, "lng": 4.3515},
    {"name": "Royal Military Museum", "area": "Cinquantenaire", "category": "Müze", "tags": ["askeri", "uçak", "tank"], "description": "Savaş uçakları ve tankların sergilendiği devasa askeri tarih müzesi.", "lat": 50.8420, "lng": 4.3920}
]

# BATCH 3: PARKLAR VE YEŞİL ALANLAR (DETAYLI)
batch_3 = [
    {"name": "Josaphat Park", "area": "Schaerbeek", "category": "Park", "tags": ["romantik", "heykel", "gölet"], "description": "İngiliz bahçesi tarzında, heykellerle dolu, yerlilerin sevdiği romantik park.", "lat": 50.8650, "lng": 4.3850},
    {"name": "Egmont Park", "area": "Sablon", "category": "Park", "tags": ["gizli", "şehir içi", "sakin"], "description": "Alışveriş caddelerinin arkasında saklı, Peter Pan heykeli olan huzurlu bahçe.", "lat": 50.8380, "lng": 4.3560},
    {"name": "Meise Botanical Garden", "area": "Meise", "category": "Doğa", "tags": ["botanik", "dev", "kale"], "description": "Şehrin biraz kuzeyinde, dünyanın en büyük botanik bahçelerinden biri.", "lat": 50.9300, "lng": 4.3300},
    {"name": "Forest Park (Parc de Forest)", "area": "Forest", "category": "Park", "tags": ["manzara", "piknik", "gün batımı"], "description": "Şehri tepeden gören, gün batımını izlemek için harika bir park.", "lat": 50.8250, "lng": 4.3400},
    {"name": "Duden Park", "area": "Forest", "category": "Park", "tags": ["orman", "doğa", "yürüyüş"], "description": "Forest Park'ın devamında, daha vahşi ve ormanlık bir yeşil alan.", "lat": 50.8200, "lng": 4.3350},
    {"name": "Jardin du Mont des Arts", "area": "Mont des Arts", "category": "Park", "tags": ["bahçe", "manzara", "merkez"], "description": "Müzeler tepesindeki geometrik düzenlenmiş, en iyi fotoğraf noktalarından biri.", "lat": 50.8435, "lng": 4.3565},
    {"name": "Square Ambiorix", "area": "European Quarter", "category": "Park", "tags": ["art nouveau", "meydan", "sakin"], "description": "Etrafı muhteşem Art Nouveau evlerle çevrili şık bir meydan parkı.", "lat": 50.8470, "lng": 4.3800},
    {"name": "Abbaye de la Cambre gardens", "area": "Ixelles", "category": "Park", "tags": ["manastır", "bahçe", "tarihi"], "description": "Eski bir manastırın büyüleyici Fransız tarzı bahçeleri.", "lat": 50.8180, "lng": 4.3730}
]

# BATCH 4: KAFELER VE KAHVE DÜKKANLARI
batch_4 = [
    {"name": "MOK Coffee Dansaert", "area": "Dansaert", "category": "Kafe", "tags": ["kahve", "modern", "brunch"], "description": "Şehrin en iyi 3. dalga kahvecilerinden biri, minimalist dekor.", "lat": 50.8520, "lng": 4.3460},
    {"name": "OR Coffee", "area": "Merkez", "category": "Kafe", "tags": ["kavurma", "merkez", "ders"], "description": "Kendi çekirdeklerini kavuran, öğrenciler ve çalışanlar için popüler mekan.", "lat": 50.8480, "lng": 4.3500},
    {"name": "Belga & Co", "area": "Ixelles", "category": "Kafe", "tags": ["kahve", "bahçe", "sakin"], "description": "Arka bahçesiyle ünlü, huzurlu bir kahve dükkanı.", "lat": 50.8250, "lng": 4.3600},
    {"name": "Kafei", "area": "Sablon", "category": "Kafe", "tags": ["asya", "fluffy pancake", "brunch"], "description": "Japon usulü kabarık pankekleriyle (fluffy pancakes) ünlü kafe.", "lat": 50.8400, "lng": 4.3500},
    {"name": "Corica Coffee Shop", "area": "Merkez", "category": "Kafe", "tags": ["çeşit", "tarihi", "hızlı"], "description": "Dünyanın her yerinden kahve çekirdeği bulabileceğiniz klasik bir dükkan.", "lat": 50.8485, "lng": 4.3520},
    {"name": "La Fabrique en Ville", "area": "Egmont Park", "category": "Kafe", "tags": ["brunch", "park", "şık"], "description": "Egmont Park'ın içinde, hafta sonu brunch'ları için mükemmel bir mekan.", "lat": 50.8385, "lng": 4.3565},
    {"name": "Buddy Buddy", "area": "Toison d'Or", "category": "Kafe", "tags": ["vegan", "fıstık ezmesi", "özel"], "description": "Özel fıstık ezmeli kahveleriyle ünlü pembe dekorlu mekan.", "lat": 50.8350, "lng": 4.3590},
    {"name": "Frank", "area": "Merkez", "category": "Kafe", "tags": ["kahvaltı", "organik", "modern"], "description": "Muntpunt kütüphanesi karşısında, kaliteli kahvaltı ve kahve.", "lat": 50.8490, "lng": 4.3540},
    {"name": "Café Capitale", "area": "Merkez", "category": "Kafe", "tags": ["yerel", "kavurma", "tatlı"], "description": "Merkezde kendi kavurdukları kahveleri sunan samimi kafe.", "lat": 50.8460, "lng": 4.3480},
    {"name": "Jat' Café", "area": "Saint-Gilles", "category": "Kafe", "tags": ["rahat", "bagel", "çalışma"], "description": "Rahat koltukları ve bagel sandviçleriyle bilinen geniş kafe.", "lat": 50.8340, "lng": 4.3580}
]

# BATCH 5: RESTORANLAR VE YEMEK
batch_5 = [
    {"name": "Fin de Siècle", "area": "Sainte-Catherine", "category": "Restoran", "tags": ["klasik", "belçika", "sıra"], "description": "Rezervasyon alınmayan, her zaman dolu, en otantik Belçika yemekleri.", "lat": 50.8490, "lng": 4.3470},
    {"name": "Fritland", "area": "Bourse", "category": "Sokak Lezzeti", "tags": ["patates", "mitraillette", "ikonik"], "description": "Şehrin en ünlü patates kızartmacısı. 'Mitraillette' (sandviç) deneyin.", "lat": 50.8480, "lng": 4.3490},
    {"name": "Maison Antoine", "area": "Jourdan", "category": "Sokak Lezzeti", "tags": ["patates", "efsane", "meydan"], "description": "Brüksel'in en iyi patatesçisi olarak bilinir, Jourdan meydanında.", "lat": 50.8370, "lng": 4.3810},
    {"name": "Nona Pizza", "area": "Sainte-Catherine", "category": "Restoran", "tags": ["pizza", "napoli", "popüler"], "description": "Belçika malzemeleriyle yapılan Napoli tarzı harika pizzalar.", "lat": 50.8500, "lng": 4.3480},
    {"name": "Le Pré Salé", "area": "Sainte-Catherine", "category": "Restoran", "tags": ["midye", "eski", "otantik"], "description": "Eski bir kasap dükkanı, şimdi midye ve et yemekleri sunuyor.", "lat": 50.8510, "lng": 4.3470},
    {"name": "Amadeus", "area": "Sainte-Catherine", "category": "Restoran", "tags": ["kaburga", "sınırsız", "kitap"], "description": "Sınırsız kaburga (all-you-can-eat ribs) konseptiyle ünlü mekan.", "lat": 50.8500, "lng": 4.3500},
    {"name": "Ballekes", "area": "Saint-Gilles", "category": "Restoran", "tags": ["köfte", "sos", "yerel"], "description": "Geleneksel Belçika köftelerini modern soslarla sunan yer.", "lat": 50.8300, "lng": 4.3550},
    {"name": "Makisu", "area": "Bailli", "category": "Restoran", "tags": ["sushi", "hızlı", "popüler"], "description": "Brüksel'in en sevilen, uygun fiyatlı ve yaratıcı sushi zinciri.", "lat": 50.8280, "lng": 4.3620},
    {"name": "Manhattn's Burgers", "area": "Merkez", "category": "Restoran", "tags": ["burger", "new york", "kaliteli"], "description": "New York tarzı, yüksek kaliteli burgerler yapan popüler zincir.", "lat": 50.8500, "lng": 4.3530},
    {"name": "Gaston", "area": "Sainte-Catherine", "category": "Kafe", "tags": ["dondurma", "artisan", "yaz"], "description": "Şehrin en iyi dondurmacılarından biri.", "lat": 50.8515, "lng": 4.3475},
    {"name": "Wolf Sharing Food Market", "area": "Merkez", "category": "Restoran", "tags": ["yemek pazarı", "çeşit", "canlı"], "description": "Eski bir banka binasında, birçok dünya mutfağını barındıran yemek alanı.", "lat": 50.8500, "lng": 4.3550}
]

# BATCH 6: GİZLİ MÜCEVHERLER VE AKTİVİTELER
batch_6 = [
    {"name": "Passage du Nord", "area": "Merkez", "category": "Alışveriş", "tags": ["pasaj", "tarihi", "mimari"], "description": "Daha az bilinen ama çok zarif bir 19. yüzyıl alışveriş pasajı.", "lat": 50.8520, "lng": 4.3530},
    {"name": "Galeries Royales Saint-Hubert", "area": "Merkez", "category": "Alışveriş", "tags": ["pasaj", "lüks", "çikolata"], "description": "Avrupa'nın en eski ve en şık alışveriş merkezlerinden biri.", "lat": 50.8470, "lng": 4.3540},
    {"name": "Statue of Everard t'Serclaes", "area": "Grand Place", "category": "Simge", "tags": ["heykel", "şans", "dokunma"], "description": "Grand Place'ın köşesinde, dokunanın Brüksel'e tekrar geleceğine inanılan heykel.", "lat": 50.8465, "lng": 4.3520},
    {"name": "Mont des Arts Carillon", "area": "Mont des Arts", "category": "Simge", "tags": ["saat", "müzik", "figür"], "description": "Her saat başı figürlerin hareket ettiği ve müzik çalan büyük duvar saati.", "lat": 50.8430, "lng": 4.3560},
    {"name": "Black Tower (Tour Noire)", "area": "Sainte-Catherine", "category": "Tarih", "tags": ["kule", "surlar", "gizemli"], "description": "Modern bir otelin arkasına gizlenmiş, ortaçağ surlarından kalan kule.", "lat": 50.8510, "lng": 4.3490},
    {"name": "Old City Wall", "area": "Merkez", "category": "Tarih", "tags": ["duvar", "ortaçağ", "kalıntı"], "description": "Şehrin ilk surlarından kalan, binaların arasına sıkışmış parçalar.", "lat": 50.8450, "lng": 4.3450},
    {"name": "Place Poelaert", "area": "Marolles", "category": "Manzara", "tags": ["bakış", "gün batımı", "asansör"], "description": "Adalet Sarayı'nın önünde, şehri tepeden gören devasa meydan.", "lat": 50.8380, "lng": 4.3520},
    {"name": "Elevator to the Marolles", "area": "Marolles", "category": "Ulaşım", "tags": ["asansör", "cam", "ücretsiz"], "description": "Place Poelaert ile Marolles mahallesini birbirine bağlayan ücretsiz cam asansör.", "lat": 50.8385, "lng": 4.3525}
]

def enrich_massive():
    filepath = 'assets/cities/bruksel.json'
    all_new = batch_1 + batch_2 + batch_3 + batch_4 + batch_5 + batch_6
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('é', 'e').replace('à', 'a').replace('.', '').replace('ç', 'c')
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
    print(f"\n✅ Added {len(places_to_add)} new places to Brüksel.")

if __name__ == "__main__":
    enrich_massive()
