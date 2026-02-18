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

# BATCH 1: MÜZELER VE KÜLTÜR (DEV LİSTE)
batch_1 = [
    {"name": "Munch Museum (MUNCH)", "area": "Bjørvika", "category": "Müze", "tags": ["sanat", "edvard munch", "çığlık"], "description": "Edvard Munch'a adanmış, dünyanın en büyük tek sanatçı müzelerinden biri.", "lat": 59.9050, "lng": 10.7550},
    {"name": "Vigeland Museum", "area": "Frogner", "category": "Müze", "tags": ["heykel", "sanat", "atölye"], "description": "Gustav Vigeland'ın stüdyosu ve yaşam alanı, heykellerin yapım sürecini gösterir.", "lat": 59.9230, "lng": 10.7000},
    {"name": "Akershus Fortress", "area": "Sentrum", "category": "Tarih", "tags": ["kale", "manzara", "tarihi"], "description": "Limanı koruyan ortaçağ kalesi ve şatosu. Harika fiyort manzarası.", "lat": 59.9070, "lng": 10.7370},
    {"name": "Norway Resistance Museum", "area": "Akershus Fortress", "category": "Müze", "tags": ["savaş", "tarih", "direniş"], "description": "II. Dünya Savaşı'ndaki Norveç direnişinin hikayesini anlatan müze.", "lat": 59.9080, "lng": 10.7360},
    {"name": "Holmenkollen Ski Museum", "area": "Holmenkollen", "category": "Müze", "tags": ["kayak", "manzara", "kule"], "description": "Dünyanın en eski kayak müzesi ve muhteşem manzaralı atlama kulesi.", "lat": 59.9640, "lng": 10.6670},
    {"name": "Ibsen Museum", "area": "Sentrum", "category": "Müze", "tags": ["edebiyat", "ev", "tarih"], "description": "Ünlü yazar Henrik Ibsen'in son yıllarını geçirdiği ev ve müze.", "lat": 59.9140, "lng": 10.7290},
    {"name": "Natural History Museum", "area": "Tøyen", "category": "Müze", "tags": ["doğa", "dinozor", "botanik"], "description": "Botanik bahçesi içinde yer alan, jeoloji ve zooloji sergileri olan müze.", "lat": 59.9190, "lng": 10.7700},
    {"name": "Historical Museum", "area": "Sentrum", "category": "Müze", "tags": ["viking", "tarih", "arkeoloji"], "description": "Viking çağından eserler ve Norveç'in kültürel tarihi.", "lat": 59.9160, "lng": 10.7350},
    {"name": "Oslo City Museum", "area": "Frogner", "category": "Müze", "tags": ["şehir", "tarih", "kültür"], "description": "Vigeland Parkı'nın köşesinde, Oslo'nun 1000 yıllık tarihini anlatan müze.", "lat": 59.9240, "lng": 10.7020},
    {"name": "Paradox Museum Oslo", "area": "Sentrum", "category": "Müze", "tags": ["illüzyon", "eğlence", "fotoğraf"], "description": "Optik illüzyonlar ve paradokslarla dolu eğlenceli deneyim müzesi.", "lat": 59.9120, "lng": 10.7420}
]

# BATCH 2: KİLİSELER VE İNANÇ
batch_2 = [
    {"name": "Oslo Cathedral (Domkirke)", "area": "Sentrum", "category": "Tarih", "tags": ["katedral", "barok", "vitray"], "description": "Şehrin ana kilisesi, vitrayları ve tavan süslemeleriyle ünlüdür.", "lat": 59.9125, "lng": 10.7480},
    {"name": "Old Aker Church (Gamle Aker Kirke)", "area": "St. Hanshaugen", "category": "Tarih", "tags": ["en eski", "taş", "ortaçağ"], "description": "Oslo'nun en eski binası, 1100'lerden kalma taş kilise.", "lat": 59.9235, "lng": 10.7450},
    {"name": "Trinity Church (Trefoldighetskirken)", "area": "Hammersborg", "category": "Tarih", "tags": ["kırmızı", "büyük", "akustik"], "description": "Devasa kubbesi ve kırmızı tuğlalarıyla dikkat çeken güzel bir kilise.", "lat": 59.9170, "lng": 10.7450},
    {"name": "Frogner Church", "area": "Frogner", "category": "Tarih", "tags": ["konum", "mimari", "sakin"], "description": "Frogner bölgesinin zarif mimariye sahip mahalle kilisesi.", "lat": 59.9190, "lng": 10.7090},
    {"name": "St. Olav's Cathedral", "area": "Sentrum", "category": "Tarih", "tags": ["katolik", "neo-gotik", "tarihi"], "description": "Oslo'nun ana Katolik katedrali, neo-gotik tarzda.", "lat": 59.9180, "lng": 10.7430},
    {"name": "Kulturkirken Jakob", "area": "Grünerløkka", "category": "Kültür", "tags": ["konser", "etkinlik", "dönüşüm"], "description": "Eski bir kilise, şimdi konserler ve tiyatrolar için kullanılan bir kültür merkezi.", "lat": 59.9185, "lng": 10.7540}
]

# BATCH 3: PARKLAR VE REKREASYON
batch_3 = [
    {"name": "St. Hanshaugen Park", "area": "St. Hanshaugen", "category": "Park", "tags": ["manzara", "piknik", "popüler"], "description": "Şehir manzarası sunan, tepelik ve geniş bir park. Yazın çok popüler.", "lat": 59.9270, "lng": 10.7400},
    {"name": "Ekebergparken", "area": "Ekeberg", "category": "Park", "tags": ["heykel", "manzara", "orman"], "description": "Fiyort manzaralı tepede, modern heykellerle dolu ormanlık park.", "lat": 59.8970, "lng": 10.7600},
    {"name": "Tøyen Park", "area": "Tøyen", "category": "Park", "tags": ["festival", "yeşil", "havuz"], "description": "Munch Müzesi'ne (eski yeri) yakın, Øya Festivali'nin yapıldığı park.", "lat": 59.9160, "lng": 10.7750},
    {"name": "Sofienberg Park", "area": "Grünerløkka", "category": "Park", "tags": ["sosyal", "barbekü", "genç"], "description": "Grünerløkka'nın kalbinde, gençlerin buluşma ve piknik noktası.", "lat": 59.9220, "lng": 10.7620},
    {"name": "Akerselva River Walk", "area": "Çeşitli", "category": "Doğa", "tags": ["nehir", "yürüyüş", "şelale"], "description": "Şehri boydan boya geçen nehir kenarındaki popüler yürüyüş yolu.", "lat": 59.9280, "lng": 10.7550},
    {"name": "Birkelunden", "area": "Grünerløkka", "category": "Park", "tags": ["pazar", "bit pazarı", "meydan"], "description": "Pazar günleri bit pazarı kurulan tarihi park/meydan.", "lat": 59.9260, "lng": 10.7600},
    {"name": "Tjuvholmen Sculpture Park", "area": "Tjuvholmen", "category": "Sanat", "tags": ["heykel", "deniz", "modern"], "description": "Astrup Fearnley Müzesi'nin yanında, deniz kenarında küçük heykel parkı.", "lat": 59.9065, "lng": 10.7210}
]

# BATCH 4: KAFELER VE FIRINLAR
batch_4 = [
    {"name": "Tim Wendelboe", "area": "Grünerløkka", "category": "Kafe", "tags": ["kahve", "efsane", "tadım"], "description": "Dünyanın en iyi kahvecilerinden biri. Sadece kahve odaklı, oturma alanı az.", "lat": 59.9260, "lng": 10.7580},
    {"name": "Java Espressobar", "area": "St. Hanshaugen", "category": "Kafe", "tags": ["klasik", "kalite", "mahalle"], "description": "1990'lardan beri hizmet veren, çok sevilen bir espresso bar.", "lat": 59.9230, "lng": 10.7380},
    {"name": "Farine", "area": "Kampen", "category": "Kafe", "tags": ["ekşi maya", "kakule", "şirin"], "description": "Kampen bölgesinde, kakuleli çörekleri (cardamom bun) meşhur fırın.", "lat": 59.9120, "lng": 10.7800},
    {"name": "Ille Brød", "area": "Løkka", "category": "Fırın", "tags": ["ekmek", "organik", "ekşi maya"], "description": "Sadece ekşi mayalı ürünler yapan ödüllü fırın.", "lat": 59.9180, "lng": 10.7650},
    {"name": "Godt Brød Grünerløkka", "area": "Grünerløkka", "category": "Kafe", "tags": ["organik", "fırın", "geniş"], "description": "Organik unlu mamuller ve sandviçler sunan popüler zincir.", "lat": 59.9230, "lng": 10.7570},
    {"name": "Talor & Jørgen", "area": "Sentrum", "category": "Kafe", "tags": ["donut", "kahve", "renkli"], "description": "Taze donutları ve kendi kavurdukları kahveleriyle ünlü.", "lat": 59.9110, "lng": 10.7550},
    {"name": "Kiosk!", "area": "Galgeberg", "category": "Kafe", "tags": ["benzinlik", "ilginç", "küçük"], "description": "Eski bir benzin istasyonundan dönüştürülmüş şirin bir kahve büfesi.", "lat": 59.9090, "lng": 10.7850},
    {"name": "Mendels Oslo", "area": "Sentrum", "category": "Tatlı", "tags": ["pastane", "fransız", "sanat"], "description": "Fransız usulü sanat eseri gibi tatlılar ve kruvasanlar.", "lat": 59.9130, "lng": 10.7420}
]

# BATCH 5: RESTORANLAR VE YEMEK
batch_5 = [
    {"name": "Mathallen Oslo", "area": "Vulkan", "category": "Yemek", "tags": ["market", "çeşit", "gurme"], "description": "Birçok farklı restoran ve dükkanın olduğu kapalı yemek pazarı.", "lat": 59.9220, "lng": 10.7520},
    {"name": "Vippa Oslo", "area": "Vippetangen", "category": "Yemek", "tags": ["sokak lezzeti", "deniz", "manzara"], "description": "Fiyort kenarında, konteynerlardan oluşan sokak lezzetleri pazarı.", "lat": 59.9020, "lng": 10.7400},
    {"name": "Syverkiosken", "area": "Friedensborg", "category": "Sokak Lezzeti", "tags": ["sosisli", "tarihi", "efsane"], "description": "Oslo'nun son kalan geleneksel sosisli (pølse) büfesi. Özel hardalıyla meşhur.", "lat": 59.9240, "lng": 10.7500},
    {"name": "Haralds Vaffel", "area": "Grünerløkka", "category": "Tatlı", "tags": ["waffle", "norveç", "kahverengi peynir"], "description": "Geleneksel Norveç waffle'ı ve kahverengi peynir (brunost) denemek için en iyi yer.", "lat": 59.9230, "lng": 10.7580},
    {"name": "Hrimnir Ramen", "area": "Vulkan", "category": "Restoran", "tags": ["ramen", "fermente", "modern"], "description": "İskandinav malzemeleriyle yapılan şehrin en iyi ramenlerinden biri.", "lat": 59.9230, "lng": 10.7510},
    {"name": "Fiskeriet", "area": "Sentrum", "category": "Restoran", "tags": ["balık", "fish&chips", "taze"], "description": "Balıkçı dükkanı ve restoran. Fish & Chips'i çok popüler.", "lat": 59.9145, "lng": 10.7490},
    {"name": "Døgnvill Burger Vulkan", "area": "Vulkan", "category": "Restoran", "tags": ["burger", "kaliteli", "süt"], "description": "Yüksek kaliteli etler ve harika milkshake'ler sunan burgerci.", "lat": 59.9225, "lng": 10.7515},
    {"name": "Izakaya", "area": "St. Olavs Plass", "category": "Restoran", "tags": ["japon", "saklı", "otantik"], "description": "Japon bar kültürünü yansıtan, küçük tabaklar sunan gizli bir mekan.", "lat": 59.9180, "lng": 10.7380},
    {"name": "Koie Ramen", "area": "Sentrum", "category": "Restoran", "tags": ["ramen", "hızlı", "lezzetli"], "description": "Gerçek Japon rameni sunan popüler ve samimi bir mekan.", "lat": 59.9150, "lng": 10.7520}
]

# BATCH 6: AKTİVİTELER VE DENEYİMLER
batch_6 = [
    {"name": "Sauna at Langkaia (SALT)", "area": "Bjørvika", "category": "Aktivite", "tags": ["sauna", "kültür", "deniz"], "description": "Dev piramit konstrüksiyonlar içinde sauna ve sanat merkezi.", "lat": 59.9060, "lng": 10.7450},
    {"name": "Oslo Camping", "area": "Sentrum", "category": "Eğlence", "tags": ["minigolf", "bar", "kamp"], "description": "İçeride mini golf oynayabileceğiniz, kamp temalı eğlenceli bar.", "lat": 59.9150, "lng": 10.7500},
    {"name": "Deichman Bjørvika", "area": "Bjørvika", "category": "Kültür", "tags": ["kütüphane", "modern", "mimari"], "description": "Sadece kitap değil, sinema ve atölyeler de sunan ödüllü modern kütüphane.", "lat": 59.9070, "lng": 10.7520},
    {"name": "Botanical Garden Greenhouses", "area": "Tøyen", "category": "Doğa", "tags": ["sera", "bitki", "tropik"], "description": "Victoria Evi ve Palmiye Evi seralarında tropik bitkileri keşfedin.", "lat": 59.9180, "lng": 10.7710},
    {"name": "Ingierstrand Beach", "area": "Fjord", "category": "Doğa", "tags": ["plaj", "yüzme", "dalış"], "description": "İkonik dalış kulesi olan, 1930'lardan kalma popüler plaj.", "lat": 59.8150, "lng": 10.7500}
]

def enrich_massive():
    filepath = 'assets/cities/oslo.json'
    all_new = batch_1 + batch_2 + batch_3 + batch_4 + batch_5 + batch_6
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('ø', 'o').replace('å', 'a').replace('.', '').replace('æ', 'ae')
        place['price'] = place.get('price', 'medium')
        place['rating'] = 4.6
        place['bestTime'] = 'Gündüz/Akşam'
        place['tips'] = 'Google Haritalar\'dan güncel saatlere bakın.'
        
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        place['distanceFromCenter'] = place.get('distanceFromCenter', 1.0)
        places_to_add.append(place)
        time.sleep(0.2)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places to Oslo.")

if __name__ == "__main__":
    enrich_massive()
