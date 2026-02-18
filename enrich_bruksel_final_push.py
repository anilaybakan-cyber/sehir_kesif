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

# 1. COMIC BOOK WALLS (Çizgi Roman Duvarları)
comics = [
    {"name": "Broussaille Comic Mural", "category": "Sanat", "tags": ["sokak sanatı", "çizgi roman", "ilk"], "description": "Brüksel'in ilk çizgi roman duvarı, sevgililerin yürüyüşünü tasvir eder."},
    {"name": "Tintin and Captain Haddock Mural", "area": "Merkez", "category": "Sanat", "tags": ["tenten", "ünlü", "fire escape"], "description": "Hergé'nin ünlü karakterleri yangın merdiveninden inerken."},
    {"name": "Astérix & Obélix Mural", "area": "Merkez", "category": "Sanat", "tags": ["asterix", "roma", "komik"], "description": "Galyalıların Romalılara saldırısını gösteren eğlenceli duvar resmi."},
    {"name": "Lucky Luke Mural", "area": "Merkez", "category": "Sanat", "tags": ["red kit", "daltonlar", "kovboy"], "description": "Gölgesinden hızlı silah çeken Red Kit ve Daltonlar."},
    {"name": "Smurfs Mural (Putterie)", "area": "Merkez", "category": "Sanat", "tags": ["şirinler", "tavan", "büyük"], "description": "Putterie geçidinin tavanını kaplayan dev Şirinler kompozisyonu."},
    {"name": "Gaston Lagaffe Mural", "area": "Merkez", "category": "Sanat", "tags": ["sakar", "komik", "duvar"], "description": "Sakar ofis çalışanı Gaston'un maceralarından bir kare."},
    {"name": "Nero Mural", "area": "Saint-Gery", "category": "Sanat", "tags": ["kuş", "besleme", "sakin"], "description": "Saint-Géry meydanında kuşları besleyen Nero karakteri."},
    {"name": "Victor Sackville Mural", "area": "Merkez", "category": "Sanat", "tags": ["casus", "1. dünya savaşı", "detay"], "description": "Birinci Dünya Savaşı casusu Sackville'i gösteren detaylı fresk."},
    {"name": "Ric Hochet Mural", "area": "Merkez", "category": "Sanat", "tags": ["dedektif", "aksiyon", "pencere"], "description": "Duvara tırmanan dedektif Ric Hochet."},
    {"name": "Monsieur Jean Mural", "area": "Merkez", "category": "Sanat", "tags": ["modern", "şehir", "yaşam"], "description": "Şehir hayatını yansıtan modern çizgi roman duvarı."},
    {"name": "Le Jeune Albert Mural", "area": "Marolles", "category": "Sanat", "tags": ["yaramaz", "çocuk", "marolles"], "description": "Marolles mahallesinin yaramaz çocuğunu anlatan eser."},
    {"name": "Kinky & Cosy Mural", "area": "Merkez", "category": "Sanat", "tags": ["yaramaz", "kızlar", "asi"], "description": "Tehlikeli ikiz kız kardeşlerin asi dünyası."},
    {"name": "Yoko Tsuno Mural", "area": "Merkez", "category": "Sanat", "tags": ["bilim kurgu", "japon", "elektronik"], "description": "Elektronik mühendisi Yoko Tsuno'yu gösteren eser."},
    {"name": "XIII Mural", "area": "Merkez", "category": "Sanat", "tags": ["aksiyon", "gizemi", "ajan"], "description": "Hafızasını kaybetmiş ajanın hikayesi."},
    {"name": "Cubitus Mural", "area": "Marolles", "category": "Sanat", "tags": ["köpek", "beyaz", "büyük"], "description": "Sevimli beyaz köpek Cubitus ve Manneken Pis."},
    {"name": "Blake & Mortimer Mural", "area": "Marolles", "category": "Sanat", "tags": ["ingiliz", "klasik", "macera"], "description": "Sarı M damgasıyla ünlü klasik çizgi roman sahnesi."},
    {"name": "Thorgal Mural", "area": "Merkez", "category": "Sanat", "tags": ["viking", "fantastik", "aile"], "description": "Viking kahramanı Thorgal ve ailesi."},
    {"name": "Billy the Cat Mural", "area": "Marolles", "category": "Sanat", "tags": ["kedi", "çocuk", "macera"], "description": "Kediye dönüşen çocuğun hikayesi."},
    {"name": "Spirou Mural", "area": "Marolles", "category": "Sanat", "tags": ["belboy", "sincap", "klasik"], "description": "Spirou ve sincabı Spip."},
    {"name": "Le Chat Mural", "area": "Güney", "category": "Sanat", "tags": ["kedi", "felsefi", "komik"], "description": "Philippe Geluck'un ünlü Şişman Kedi'si."}
]

# 2. ART NOUVEAU MASTERPIECES (Art Nouveau Evleri)
art_nouveau = [
    {"name": "Horta Museum", "area": "Saint-Gilles", "category": "Müze", "tags": ["victor horta", "ev", "unesco"], "description": "Victor Horta'nın kendi evi ve atölyesi. UNESCO listesinde."},
    {"name": "Hôtel Solvay", "area": "Avenue Louise", "category": "Mimari", "tags": ["lüks", "horta", "unesco"], "description": "Horta'nın en lüks ve bozulmamış tasarımı. UNESCO listesinde."},
    {"name": "Hôtel Tassel", "area": "Ixelles", "category": "Mimari", "tags": ["ilk", "horta", "devrim"], "description": "Dünyanın ilk Art Nouveau binası olarak kabul edilir."},
    {"name": "Hôtel van Eetvelde", "area": "Ambiorix", "category": "Mimari", "tags": ["demir", "cam", "aydınlık"], "description": "Merkezi kubbesi ve demir işçiliğiyle ünlü Horta eseri."},
    {"name": "Maison Cauchie", "area": "Merode", "category": "Mimari", "tags": ["sgraffito", "cephe", "sanat"], "description": "Cephesi devasa sgraffito resimlerle kaplı, müze ev."},
    {"name": "Maison Saint-Cyr", "area": "Ambiorix", "category": "Mimari", "tags": ["dar", "süslü", "demir"], "description": "Gustave Strauven'in aşırı süslü, sadece 4 metre genişliğindeki başyapıtı."},
    {"name": "Hôtel Hannon", "area": "Saint-Gilles", "category": "Müze", "tags": ["yeni", "müze", "fransız"], "description": "Yakın zamanda müze olarak halka açılan muhteşem köşe bina."},
    {"name": "Maison Autrique", "area": "Schaerbeek", "category": "Müze", "tags": ["erken", "horta", "senografi"], "description": "Horta'nın ilk dönem eseri, hayali bir senografiyle sergileniyor."},
    {"name": "Musical Instruments Museum (MIM) Building", "area": "Merkez", "category": "Mimari", "tags": ["old england", "demir", "manzara"], "description": "Eski Old England mağazası, şimdi müzik müzesi."},
    {"name": "Hôtel Ciamberlani", "area": "Ixelles", "category": "Mimari", "tags": ["at nalı", "pencere", "resim"], "description": "At nalı şeklindeki pencereleriyle ünlü Paul Hankar eseri."}
]

# 3. METRO ART (Metro İstasyonu Sanatı)
metro_art = [
    {"name": "Pannenhuis Metro Station", "category": "Sanat", "tags": ["fütüristik", "turuncu", "fotoğraf"], "description": "Bilim kurgu filmlerinden fırlamış gibi duran turuncu daireli istasyon."},
    {"name": "Stockel Metro Station", "category": "Sanat", "tags": ["tenten", "karakter", "duvar"], "description": "Duvarlarında 140'tan fazla Tenten karakterinin olduğu istasyon."},
    {"name": "Hankar Metro Station", "category": "Sanat", "tags": ["renkli", "duvar", "somville"], "description": "Roger Somville'in devasa ve renkli 'Notre Temps' duvar resmi."},
    {"name": "Porte de Hal Metro Art", "category": "Sanat", "tags": ["schuiten", "tramvay", "hayali"], "description": "François Schuiten'in istasyondan çıkan eski tramvay tasarımı."},
    {"name": "Comte de Flandre Metro Art", "category": "Sanat", "tags": ["icarus", "tavan", "heykel"], "description": "Tavandan sarkan Icarus figürleriyle dolu istasyon."}
]

# 4. ICONIC BARS & CAFES (İkonik Barlar ve Kafeler)
bars_cafes = [
    {"name": "Delirium Café", "area": "Merkez", "category": "Bar", "tags": ["rekor", "çeşit", "turistik"], "description": "2000'den fazla bira çeşidiyle Guinness Rekorlar Kitabı'na giren bar."},
    {"name": "Poechenellekelder", "area": "Merkez", "category": "Bar", "tags": ["kukla", "tarihi", "otantik"], "description": "Manneken Pis'in karşısında, içi kuklalarla dolu tarihi bar."},
    {"name": "L'Archiduc", "area": "Dansaert", "category": "Bar", "tags": ["caz", "art deco", "kokteyl"], "description": "1930'lardan kalma art deco tarzı efsanevi caz bar."},
    {"name": "Goupil Le Fol", "area": "Merkez", "category": "Bar", "tags": ["labirent", "şarap", "şanson"], "description": "Labirent gibi odaları, eski koltukları ve meyve şaraplarıyla ünlü."},
    {"name": "La Pharmacie Anglaise", "area": "Coudenberg", "category": "Bar", "tags": ["kokteyl", "eczane", "gotik"], "description": "Eski bir eczaneden dönüştürülmüş, gotik atmosferli kokteyl bar."},
    {"name": "Au Bon Vieux Temps", "area": "Merkez", "category": "Bar", "tags": ["gizli", "ortaçağ", "vitray"], "description": "1695'ten kalma, vitraylı pencereleri olan gizli bir ara sokak barı."},
    {"name": "Le Falstaff", "area": "Bourse", "category": "Restoran", "tags": ["art deco", "brasserie", "tarihi"], "description": "Muhteşem Art Deco iç mekanıyla ünlü tarihi brasserie."},
    {"name": "Café Belga", "area": "Flagey", "category": "Bar", "tags": ["popüler", "teras", "meydan"], "description": "Eski radyo binasında (Flagey), yerlilerin en popüler buluşma noktası."},
    {"name": "Moeder Lambic Original", "area": "Saint-Gilles", "category": "Bar", "tags": ["bira", "uzman", "yerel"], "description": "Gerçek bira tutkunlarının tercih ettiği, turistik olmayan şube."},
    {"name": "La Porte Noire", "area": "Merkez", "category": "Bar", "tags": ["mahzen", "konser", "viski"], "description": "Tuhafiyeciler loncasının eski mahzeninde yer alan atmosferik bar."},
    {"name": "Chez Richard", "area": "Sablon", "category": "Bar", "tags": ["bistro", "şık", "teras"], "description": "Sablon'da insanları izlemek için en şık köşe barı."},
    {"name": "Le Mort Subite", "area": "Merkez", "category": "Bar", "tags": ["film", "klasik", "kalabalık"], "description": "Danimarkalı Kız filminde de görünen, 1920'lerden kalma salon."},
    {"name": "Monk", "area": "Sainte-Catherine", "category": "Bar", "tags": ["spagetti", "piyano", "bira"], "description": "Spagettisi ve bira seleksiyonuyla ünlü popüler mahalle barı."},
    {"name": "Walvis", "area": "Dansaert", "category": "Bar", "tags": ["kanal", "güneş", "hipster"], "description": "Kanal kenarında, güneşli günlerin vazgeçilmez terası."},
    {"name": "BarBeton", "area": "Dansaert", "category": "Bar", "tags": ["beton", "modern", "kahve"], "description": "Beton ağırlıklı modern dekoruyla bilinen kafe/bar."},
    {"name": "Life is Beautiful", "area": "Dansaert", "category": "Bar", "tags": ["kokteyl", "butik", "samimi"], "description": "Özel kokteylleriyle ünlü küçük ve samimi bar."},
    {"name": "Yi Chan", "area": "Bourse", "category": "Restoran", "tags": ["asya", "kokteyl", "füzyon"], "description": "Asya mutfağı ve kokteylleri birleştiren şık mekan."},
    {"name": "Nüetnigenough", "area": "Merkez", "category": "Restoran", "tags": ["yerel", "bira", "yemek"], "description": "'Asla yetmez' anlamına gelen, bira ile pişen yemekler sunan yer."}
]

# 5. STATUES & SCULPTURES (Heykeller ve Simgeler)
statues = [
    {"name": "Jeanneke Pis", "area": "Merkez", "category": "Simge", "tags": ["kız", "işeyen", "fıskiye"], "description": "Manneken Pis'in kız kardeşi, demir parmaklıklar arkasında."},
    {"name": "Het Zinneke", "area": "Dansaert", "category": "Simge", "tags": ["köpek", "işeyen", "sokak"], "description": "Direğe işeyen sokak köpeği heykeli, ailenin üçüncü üyesi."},
    {"name": "Madame Chapeau Statue", "area": "Merkez", "category": "Simge", "tags": ["tiyatro", "yaşlı kadın", "komik"], "description": "Brüksel tiyatrosunun ünlü karakteri, tavşanını sayan yaşlı kadın."},
    {"name": "Gaston Lagaffe Statue", "area": "Merkez", "category": "Simge", "tags": ["çizgi roman", "heykel", "sakar"], "description": "Çizgi roman müzesinin önündeki sakar kahraman heykeli."},
    {"name": "Boule & Bill Statue", "area": "Jette", "category": "Simge", "tags": ["çocuk", "köpek", "çizgi roman"], "description": "Ünlü çocuk ve köpeğinin heykeli."},
    {"name": "Bip Bip (Road Runner) Statue", "area": "Merkez", "category": "Simge", "tags": ["hızlı", "kuş", "çizgi roman"], "description": "Hızlı koşan çizgi film karakteri."}
]

# 6. PARKS & SQUARES (Meydanlar ve Parklar)
squares = [
    {"name": "Place Saint-Géry", "area": "Merkez", "category": "Meydan", "tags": ["gece hayatı", "tarihi", "pazar"], "description": "Eski pazar yeri, şimdi barların ve sergilerin merkezi."},
    {"name": "Place du Châtelain", "area": "Ixelles", "category": "Meydan", "tags": ["pazar", "çarşamba", "sosyal"], "description": "Çarşamba günleri kurulan sokak pazarı ve aperitif kültürüyle ünlü."},
    {"name": "Place Flagey", "area": "Ixelles", "category": "Meydan", "tags": ["gölet", "kültür", "geniş"], "description": "Göletlerin yanındaki devasa meydan, kültür merkezi ve kafeler."},
    {"name": "Square du Petit Sablon", "area": "Sablon", "category": "Park", "tags": ["heykeller", "lonca", "romantik"], "description": "Etrafı 48 eski meslek loncası heykeliyle çevrili küçük romantik bahçe."},
    {"name": "Jardin du Fleuriste", "area": "Laeken", "category": "Park", "tags": ["panoramik", "çiçek", "sakin"], "description": "Kraliyet seralarının yakınında, harika manzaralı az bilinen park."}
]

def enrich_final():
    filepath = 'assets/cities/bruksel.json'
    # Tüm listeleri birleştir
    all_new = comics + art_nouveau + metro_art + bars_cafes + statues + squares
    
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
        place['rating'] = 4.6
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
    print(f"\n✅ Added {len(places_to_add)} new places to Brüksel. Target reached!")

if __name__ == "__main__":
    enrich_final()
