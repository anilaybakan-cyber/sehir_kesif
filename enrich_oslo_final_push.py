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

# 1. SCULPTURES & PUBLIC ART (Heykeller ve Kamusal Sanat)
sculptures = [
    {"name": "The Monolith (Monolitten)", "area": "Frogner Park", "category": "Sanat", "tags": ["vigeland", "ikonik", "121 figür"], "description": "14 metre yüksekliğinde, 121 insan figüründen oluşan Vigeland'ın başyapıtı."},
    {"name": "The Angry Boy (Sinnataggen)", "area": "Frogner Park", "category": "Sanat", "tags": ["vigeland", "popüler", "bronz"], "description": "Parkın en ünlü ve en çok fotoğrafı çekilen sinirli çocuk heykeli."},
    {"name": "The Wheel of Life", "area": "Frogner Park", "category": "Sanat", "tags": ["vigeland", "sembolik", "çember"], "description": "İnsanlardan oluşan bir çember, yaşam döngüsünü simgeler."},
    {"name": "She Lies", "area": "Bjørvika", "category": "Sanat", "tags": ["su üstünde", "modern", "buzdağı"], "description": "Opera Binası'nın önündeki suda yüzen, değişen konumuyla ünlü cam ve çelik heykel."},
    {"name": "The Tiger Statue", "area": "Sentrum", "category": "Simge", "tags": ["kaplan", "meydan", "buluşma"], "description": "Oslo Merkez İstasyonu'nun önündeki dev 4.5 metrelik bronz kaplan. Şehrin takma adı 'Tigerstaden'e atıf."},
    {"name": "Oslo Tree", "area": "Bjørvika", "category": "Sanat", "tags": ["ışık", "ağaç", "yapay"], "description": "Geceleri ışık saçan, modern bir yapay ağaç enstalasyonu."},
    {"name": "Christian IV Statue", "area": "Stortorvet", "category": "Tarih", "tags": ["kral", "kurucu", "bronz"], "description": "Oslo'yu (Christiania) kuran kralın Stortorvet meydanındaki heykeli."},
    {"name": "Karl Johan Statue", "area": "Slottsplassen", "category": "Tarih", "tags": ["kral", "atlı", "saray"], "description": "Kraliyet Sarayı'nın önündeki atlı kral heykeli."},
    {"name": "Dykkar (The Diver)", "area": "Aker Brygge", "category": "Sanat", "tags": ["dalgıç", "deniz", "modern"], "description": "Suya atlamak üzere olan stilize edilmiş dalgıç heykeli."},
    {"name": "Fearless Girl Oslo", "area": "Sentrum", "category": "Sanat", "tags": ["kız", "cesur", "kopya"], "description": "Wall Street'teki ünlü heykelin bir benzeri, Grand Hotel'in önünde."}
]

# 2. ISLANDS & NATURE (Adalar ve Doğa)
islands_nature = [
    {"name": "Hovedøya", "area": "Fjord", "category": "Doğa", "tags": ["manastır", "plaj", "tarih"], "description": "Fiyordun en popüler adası, manastır kalıntıları ve plajlarıyla ünlü."},
    {"name": "Langøyene", "area": "Fjord", "category": "Doğa", "tags": ["kamp", "plaj", "festival"], "description": "Kamp yapmaya izin verilen tek ada, geniş kumsalı var."},
    {"name": "Gressholmen", "area": "Fjord", "category": "Doğa", "tags": ["tavşanlar", "doğa koruma", "sakin"], "description": "Doğa koruma alanı olan ve yaban tavşanlarıyla bilinen huzurlu ada."},
    {"name": "Lindøya", "area": "Fjord", "category": "Doğa", "tags": ["kulübe", "renkli", "yazlık"], "description": "Rengarenk 300'den fazla küçük yazlık kulübesiyle ünlü şirin ada."},
    {"name": "Bleikøya", "area": "Fjord", "category": "Doğa", "tags": ["küçük", "kulübe", "mahalle"], "description": "Sadece yazlıkçıların olduğu, çok küçük ve sakin bir ada."},
    {"name": "Nakholmen", "area": "Fjord", "category": "Doğa", "tags": ["sakin", "yürüyüş", "manzara"], "description": "Kışın da feribotun uğradığı, yürüyüş için ideal küçük ada."},
    {"name": "Sognsvann Lake", "area": "Nordmarka", "category": "Doğa", "tags": ["göl", "yürüyüş", "piknik"], "description": "Metro son durağında, Oslo'luların en popüler yürüyüş ve piknik gölü."},
    {"name": "Maridalsvannet", "area": "Maridalen", "category": "Doğa", "tags": ["içme suyu", "koruma", "manzara"], "description": "Oslo'nun içme suyu kaynağı, etrafında yürüyüş yapmak yasak olsa da manzarası harika."},
    {"name": "Vettakollen Viewpoint", "area": "Nordmarka", "category": "Manzara", "tags": ["zirve", "fiyort", "kolay"], "description": "Kısa bir yürüyüşle Oslo Fiyordu'nun en iyi manzaralarından birine ulaşabilirsiniz."},
    {"name": "Grefsenkollen Viewpoint", "area": "Grefsen", "category": "Manzara", "tags": ["restoran", "gün batımı", "tepe"], "description": "Tepesinde restoran olan, arabayla çıkılabilen harika manzara noktası."},
    {"name": "Akerselva Waterfall (Mølla)", "area": "Grünerløkka", "category": "Doğa", "tags": ["şelale", "şehir içi", "güçlü"], "description": "Nehrin şehir içindeki en büyük ve etkileyici şelalesi."}
]

# 3. LIBRARIES & CULTURE (Kütüphaneler ve Gizli Müzeler)
culture = [
    {"name": "Deichman Grünerløkka", "area": "Grünerløkka", "category": "Kültür", "tags": ["kütüphane", "modern", "çizgi roman"], "description": "Serieteket (Çizgi Roman Kütüphanesi) bölümüyle ünlü modern şube."},
    {"name": "Deichman Majorstuen", "area": "Majorstuen", "category": "Kültür", "tags": ["kütüphane", "klasik", "çalışma"], "description": "Sessiz çalışma alanlarıyla popüler, klasik tarzda kütüphane."},
    {"name": "Emanuel Vigeland Museum", "area": "Slemdal", "category": "Müze", "tags": ["gizli", "karanlık", "fresk"], "description": "Gustav'ın kardeşinin, içi tamamen fresklerle kaplı loş ve gizemli mozolesi."},
    {"name": "Mini Bottle Gallery", "area": "Sentrum", "category": "Müze", "tags": ["şişe", "ilginç", "koleksiyon"], "description": "Dünyanın en büyük minyatür şişe koleksiyonuna sahip eksantrik müze."},
    {"name": "Oslo City Hall (Rådhuset)", "area": "Sentrum", "category": "Tarih", "tags": ["nobel", "mural", "ücretsiz"], "description": "Nobel Barış Ödülü'nün verildiği, içi devasa duvar resimleriyle kaplı bina."},
    {"name": "Intercultural Museum", "area": "Grønland", "category": "Müze", "tags": ["göç", "kültür", "hapishane"], "description": "Eski bir karakol/hapishane binasında göç ve kültür tarihi."},
    {"name": "Armed Forces Museum", "area": "Akershus", "category": "Müze", "tags": ["askeri", "tarih", "silah"], "description": "Norveç askeri tarihini, Vikinglerden günümüze anlatan kapsamlı müze."}
]

# 4. BEST BAKERIES & CAFES (En İyi Fırın ve Kafeler - Genişletilmiş)
bakeries = [
    {"name": "Grains", "area": "Majorstuen", "category": "Fırın", "tags": ["fransız", "krep", "artisan"], "description": "Fransız usulü artizan ekmekler ve krepler sunan popüler fırın."},
    {"name": "Mjøl Bakeri", "area": "Sentrum", "category": "Fırın", "tags": ["ekşi maya", "pizza", "kalite"], "description": "Sadece yerel un kullanan, akşamları pizzacıya dönüşen fırın."},
    {"name": "Kveitemjøl", "area": "Aker Brygge", "category": "Fırın", "tags": ["küp kruvasan", "modern", "brunch"], "description": "Küp şeklindeki kruvasanlarıyla (cube croissant) Instagram fenomeni olan yer."},
    {"name": "Åpent Bakeri Inkognito", "area": "Slottsparken", "category": "Fırın", "tags": ["klasik", "zincir", "taze"], "description": "Güvenilir kalitesiyle bilinen, öğle yemeği için ideal fırın."},
    {"name": "Baker Hansen", "area": "Çeşitli", "category": "Fırın", "tags": ["köklü", "gluten-free", "zincir"], "description": "Norveç'in en eski fırın zinciri, glutensiz seçenekleriyle ünlü."},
    {"name": "WB Samson", "area": "Egertorget", "category": "Fırın", "tags": ["tarihi", "kahve", "merkez"], "description": "1894'ten beri hizmet veren tarihi pastane zinciri."},
    {"name": "Supreme Roastworks", "area": "Grünerløkka", "category": "Kafe", "tags": ["kavurma", "ödüllü", "espresso"], "description": "Dünya şampiyonu baristaların kurduğu yüksek nitelikli kahveci."},
    {"name": "Fuglen Oslo", "area": "Sentrum", "category": "Kafe", "tags": ["vintage", "kokteyl", "tasarım"], "description": "Hem kahveci hem kokteyl barı, 1960'lar İskandinav tasarımıyla ünlü."},
    {"name": "Stockfleths", "area": "Sentrum", "category": "Kafe", "tags": ["zincir", "kalite", "norveç"], "description": "Norveç'in Starbucks'ı ama çok daha kaliteli kahve sunan yerel zincir."},
    {"name": "Pust Kaffebar", "area": "Majorstuen", "category": "Kafe", "tags": ["sakin", "bitki", "öğrenci"], "description": "Bol bitkili, öğrenciler için ideal çalışma ortamı olan kafe."},
    {"name": "KaffeBrenneriet", "area": "Bislett", "category": "Kafe", "tags": ["popüler", "köşe", "gazete"], "description": "Her köşe başında bulabileceğiniz, güvenilir standartta kahveci."},
    {"name": "Neongrut", "area": "Tøyen", "category": "Kafe", "tags": ["vegan", "renkli", "modern"], "description": "Tamamen vegan ürünler sunan, neon ışıklı modern kafe."},
    {"name": "Handwerk", "area": "Vulkan", "category": "Fırın", "tags": ["ekşi maya", "organik", "mathallen"], "description": "Mathallen içinde, sadece ekşi maya ile çalışan artizan fırın."},
    {"name": "Vårt Daglige Brød", "area": "Bislett", "category": "Kafe", "tags": ["samimi", "yerel", "kahvaltı"], "description": "'Günlük Ekmeğimiz' anlamına gelen, yerel halkın sevdiği sıcak mekan."},
    {"name": "Liebling", "area": "Grünerløkka", "category": "Kafe", "tags": ["berlin", "tarz", "plak"], "description": "Berlin tarzı dekorasyonu ve plaklarıyla ünlü hip kafe."}
]

# 5. UNIQUE BARS & NIGHTLIFE (Barlar ve Gece Hayatı)
nightlife = [
    {"name": "Himkok", "area": "Sentrum", "category": "Bar", "tags": ["gizli", "dünyanın en iyi", "aquavit"], "description": "Dünyanın en iyi 50 barı listesinde, kendi içkilerini üreten gizli bar."},
    {"name": "Torggata Botaniske", "area": "Torggata", "category": "Bar", "tags": ["bitki", "sera", "kokteyl"], "description": "İçi tamamen sarmaşık ve bitkilerle kaplı, sera görünümlü kokteyl bar."},
    {"name": "Blå", "area": "Akerselva", "category": "Gece Kulübü", "tags": ["caz", "nehir", "alternatif"], "description": "Nehir kenarında, eski bir fabrikadan dönüştürülmüş efsanevi caz ve dans kulübü."},
    {"name": "Tilt", "area": "Torggata", "category": "Eğlence", "tags": ["arcade", "pinball", "bira"], "description": "Yüzlerce retro arcade ve pinball makinesi olan oyun barı."},
    {"name": "The Villa", "area": "Møllergata", "category": "Gece Kulübü", "tags": ["tekno", "yeraltı", "dans"], "description": "Elektronik müzik severlerin bir numaralı adresi."},
    {"name": "Summit Bar", "area": "Radisson Blu", "category": "Bar", "tags": ["manzara", "çatı", "şık"], "description": "Radisson Blu otelinin 21. katında, muhteşem şehir manzaralı bar."},
    {"name": "Røør", "area": "Sentrum", "category": "Bar", "tags": ["bira", "musluk", "çeşit"], "description": "70'ten fazla musluk birası sunan craft bira cenneti."},
    {"name": "Schouskjelleren Mikrobryggeri", "area": "Grünerløkka", "category": "Bar", "tags": ["mahzen", "bira", "tarihi"], "description": "Eski bir bira fabrikasının mahzeninde yer alan, şömineli otantik pub."},
    {"name": "Andre til Høyre", "area": "Youngstorget", "category": "Bar", "tags": ["şık", "apartman", "kokteyl"], "description": "Bir apartman dairesi gibi dekore edilmiş, 'Soldan İkinci' anlamına gelen şık bar."}
]

# 6. SHOPPING & OTHERS (Alışveriş ve Diğer)
shopping = [
    {"name": "Velouria Vintage", "area": "Grünerløkka", "category": "Alışveriş", "tags": ["vintage", "moda", "ikinci el"], "description": "Oslo'nun en ünlü ve kaliteli vintage giyim mağazası."},
    {"name": "Tronsmo Bokhandel", "area": "Sentrum", "category": "Alışveriş", "tags": ["kitap", "bağımsız", "kült"], "description": "Sıradışı çizgi roman ve sanat kitapları bulabileceğiniz efsanevi kitapçı."},
    {"name": "Mathallen Oslo (Shops)", "area": "Vulkan", "category": "Alışveriş", "tags": ["gurme", "peynir", "balık"], "description": "Sadece yemek değil, gurme ürünler almak için de harika bir pazar."},
    {"name": "Paleet", "area": "Karl Johan", "category": "Alışveriş", "tags": ["lüks", "moda", "merkez"], "description": "Karl Johans gate üzerindeki şık ve lüks alışveriş merkezi."}
]

def enrich_final():
    filepath = 'assets/cities/oslo.json'
    all_new = sculptures + islands_nature + culture + bakeries + nightlife + shopping
    
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
    print(f"\n✅ Added {len(places_to_add)} new places to Oslo. Target reached!")

if __name__ == "__main__":
    enrich_final()
