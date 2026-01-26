import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Heidelberg Germany", f"{place_name} Heidelberg", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:20000@49.4093,8.6943"
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

# BATCH 8: Ek Restoranlar & Kafeler
batch_8 = [
    {"name": "Goldener Hecht", "name_en": "Golden Pike", "area": "Altstadt", "category": "Restoran", "tags": ["balık", "geleneksel", "nehir"], "distanceFromCenter": 0.3, "lat": 49.4115, "lng": 8.7080, "price": "medium", "rating": 4.4, "description": "Neckar kenarında taze balık ve geleneksel Alman mutfağı.", "description_en": "Fresh fish and traditional German cuisine by the Neckar.", "bestTime": "Akşam", "tips": "Teras manzarası harika.", "tips_en": "Terrace view is great."},
    {"name": "Kulturbrauerei", "name_en": "Culture Brewery", "area": "Bergheim", "category": "Restoran", "tags": ["bira", "restoran", "bahçe"], "distanceFromCenter": 0.8, "lat": 49.4065, "lng": 8.6920, "price": "medium", "rating": 4.5, "description": "Kendi birasını yapan, geniş bira bahçesiyle oğlak popüler mekan.", "description_en": "Popular spot with own brewery and large beer garden.", "bestTime": "Akşam", "tips": "Yaz aylarında bira bahçesi ideal.", "tips_en": "Beer garden perfect in summer."},
    {"name": "Wirtshaus Zum Nepomuk", "name_en": "Nepomuk Inn", "area": "Altstadt", "category": "Restoran", "tags": ["geleneksel", "yöresel", "köfte"], "distanceFromCenter": 0.2, "lat": 49.4095, "lng": 8.7100, "price": "medium", "rating": 4.3, "description": "Otantik Palatinate mutfağı ve bölge şarapları.", "description_en": "Authentic Palatinate cuisine and regional wines.", "bestTime": "Akşam", "tips": "Saumagen'i (yerel spesiyalite) deneyin.", "tips_en": "Try Saumagen (local specialty)."},
    {"name": "Weinstube Schnitzelbank", "name_en": "Schnitzelbank Wine Bar", "area": "Altstadt", "category": "Restoran", "tags": ["şarap", "schnitzel", "romantik"], "distanceFromCenter": 0.2, "lat": 49.4088, "lng": 8.7082, "price": "medium", "rating": 4.5, "description": "Bölge şarapları eşliğinde schnitzel ve yöresel lezzetler.", "description_en": "Schnitzel and regional dishes with local wines.", "bestTime": "Akşam", "tips": "Şarap seçenekleri çok iyi.", "tips_en": "Wine selection is excellent."},
    {"name": "Sakura Sushi", "name_en": "Sakura Sushi", "area": "Altstadt", "category": "Restoran", "tags": ["japon", "sushi", "modern"], "distanceFromCenter": 0.2, "lat": 49.4090, "lng": 8.7065, "price": "medium", "rating": 4.4, "description": "Kaliteli Japon mutfağı ve sushi.", "description_en": "Quality Japanese cuisine and sushi.", "bestTime": "Akşam", "tips": "Öğle menüsü uygun fiyatlı.", "tips_en": "Lunch menu is affordable."},
    {"name": "Palmbrau Gasse", "name_en": "Palmbrau Alley", "area": "Altstadt", "category": "Restoran", "tags": ["bira", "geleneksel", "yerel"], "distanceFromCenter": 0.15, "lat": 49.4100, "lng": 8.7095, "price": "low", "rating": 4.3, "description": "Yerel bira ve uygun fiyatlı Alman yemekleri.", "description_en": "Local beer and affordable German food.", "bestTime": "Akşam", "tips": "Öğrenci dostu fiyatlar.", "tips_en": "Student-friendly prices."}
]

# BATCH 9: Ek Kafeler & Pastaneler
batch_9 = [
    {"name": "Cafe Gundel", "name_en": "Cafe Gundel", "area": "Altstadt", "category": "Kafe", "tags": ["kahve", "pasta", "kahvaltı"], "distanceFromCenter": 0.2, "lat": 49.4098, "lng": 8.7055, "price": "medium", "rating": 4.5, "description": "Kaliteli kahve ve taze hamur işleri. Kahvaltı menüsü çok iyi.", "description_en": "Quality coffee and fresh pastries. Great breakfast menu.", "bestTime": "Sabah", "tips": "Hafta sonu brunch için erken gelin.", "tips_en": "Come early for weekend brunch."},
    {"name": "Gelato Go", "name_en": "Gelato Go", "area": "Altstadt", "category": "Tatlı", "tags": ["dondurma", "gelato", "italyan"], "distanceFromCenter": 0.1, "lat": 49.4095, "lng": 8.7070, "price": "low", "rating": 4.6, "description": "El yapımı İtalyan gelato, taze meyveli çeşitler.", "description_en": "Handmade Italian gelato, fresh fruit flavors.", "bestTime": "İkindi", "tips": "Pistacchio lezzeti harika.", "tips_en": "Pistachio flavor is amazing."},
    {"name": "Cafe Frisch", "name_en": "Cafe Frisch", "area": "Altstadt", "category": "Kafe", "tags": ["modern", "kahve", "vejetaryen"], "distanceFromCenter": 0.3, "lat": 49.4085, "lng": 8.7060, "price": "medium", "rating": 4.4, "description": "Modern kafe, özel kahve çeşitleri ve vejetaryen seçenekler.", "description_en": "Modern cafe, specialty coffee and vegetarian options.", "bestTime": "Gündüz", "tips": "Vegan seçenekleri mevcut.", "tips_en": "Vegan options available."},
    {"name": "Tee Kontor", "name_en": "Tea Counter", "area": "Altstadt", "category": "Kafe", "tags": ["çay", "sakin", "organik"], "distanceFromCenter": 0.2, "lat": 49.4102, "lng": 8.7075, "price": "medium", "rating": 4.3, "description": "200'den fazla çay çeşidi olan butik çay evi.", "description_en": "Boutique tea house with over 200 tea varieties.", "bestTime": "İkindi", "tips": "Çay tadımı seanslarını sormayı unutmayın.", "tips_en": "Ask about tea tasting sessions."}
]

# BATCH 10: Ek Tarihi Yerler
batch_10 = [
    {"name": "Providenzkirche", "name_en": "Providence Church", "area": "Altstadt", "category": "Tarihi", "tags": ["kilise", "barok", "tarihi"], "distanceFromCenter": 0.3, "lat": 49.4088, "lng": 8.7000, "price": "free", "rating": 4.2, "description": "1661'de inşa edilen zarif Barok kilise.", "description_en": "Elegant Baroque church built in 1661.", "bestTime": "Gündüz", "tips": "Sessiz bir mola için ideal.", "tips_en": "Ideal for a quiet break."},
    {"name": "Jesuitenkirche", "name_en": "Jesuit Church", "area": "Altstadt", "category": "Tarihi", "tags": ["kilise", "barok", "mimari"], "distanceFromCenter": 0.2, "lat": 49.4100, "lng": 8.7045, "price": "free", "rating": 4.4, "description": "18. yüzyıldan kalma görkemli Barok Cizvit kilisesi.", "description_en": "Magnificent Baroque Jesuit church from 18th century.", "bestTime": "Gündüz", "tips": "İç mekan dekorasyonu etkileyici.", "tips_en": "Interior decoration is impressive."},
    {"name": "Marstall (Eski Ahır)", "name_en": "Marstall Stables", "area": "Altstadt", "category": "Tarihi", "tags": ["üniversite", "tarihi", "yemekhane"], "distanceFromCenter": 0.2, "lat": 49.4108, "lng": 8.7095, "price": "free", "rating": 4.1, "description": "16. yüzyıl prens ahırı, şimdi üniversite yemekhanesi.", "description_en": "16th century prince's stables, now university cafeteria.", "bestTime": "Öğle", "tips": "Öğrenci yemekhanesinde ucuz öğle yemeği.", "tips_en": "Cheap lunch at student cafeteria."},
    {"name": "Hexenturm (Cadı Kulesi)", "name_en": "Witch Tower", "area": "Altstadt", "category": "Tarihi", "tags": ["kule", "ortaçağ", "hapishane"], "distanceFromCenter": 0.25, "lat": 49.4095, "lng": 8.7050, "price": "free", "rating": 4.2, "description": "Ortaçağ şehir surlarından kalan kule, cadıların hapsedildiği söylenir.", "description_en": "Tower from medieval city walls, said to have imprisoned witches.", "bestTime": "Gündüz", "tips": "Şimdi kadın hastalıkları kliniğinin parçası.", "tips_en": "Now part of women's clinic."}
]

# BATCH 11: Ek Doğa & Park Alanları  
batch_11 = [
    {"name": "Botanik Bahçesi", "name_en": "Botanical Garden", "area": "Neuenheim", "category": "Park", "tags": ["bahçe", "bitki", "bilim"], "distanceFromCenter": 1.0, "lat": 49.4170, "lng": 8.6780, "price": "free", "rating": 4.5, "description": "Üniversiteye bağlı, 12.000'den fazla bitki türü barındıran tropikal seralar.", "description_en": "University-affiliated, tropical greenhouses with over 12,000 plant species.", "bestTime": "Gündüz", "tips": "Seralar kış aylarında bile güzel.", "tips_en": "Greenhouses are nice even in winter."},
    {"name": "Stadtwald (Şehir Ormanı)", "name_en": "City Forest", "area": "Schloss", "category": "Doğa", "tags": ["orman", "yürüyüş", "doğa"], "distanceFromCenter": 2.0, "lat": 49.4000, "lng": 8.7200, "price": "free", "rating": 4.4, "description": "Kalenin arkasında uzanan geniş orman alanı. Yürüyüş ve bisiklet parkurları.", "description_en": "Extensive forest area behind the castle. Hiking and cycling trails.", "bestTime": "Gündüz", "tips": "Her seviye için yürüyüş rotaları mevcut.", "tips_en": "Hiking routes for all levels available."},
    {"name": "Handschuhsheim Bağları", "name_en": "Handschuhsheim Vineyards", "area": "Handschuhsheim", "category": "Manzara", "tags": ["üzüm bağı", "şarap", "manzara"], "distanceFromCenter": 3.0, "lat": 49.4280, "lng": 8.6850, "price": "free", "rating": 4.3, "description": "Şehrin kuzeyindeki üzüm bağları, yerel şarap tadımı.", "description_en": "Vineyards north of city, local wine tasting.", "bestTime": "Sonbahar", "tips": "Bağbozumu zamanı (Eylül-Ekim) en güzel.", "tips_en": "Harvest time (Sept-Oct) is most beautiful."},
    {"name": "Iqbal Ufer", "name_en": "Iqbal Bank", "area": "Neuenheim", "category": "Park", "tags": ["nehir", "yürüyüş", "piknik"], "distanceFromCenter": 0.6, "lat": 49.4150, "lng": 8.7050, "price": "free", "rating": 4.2, "description": "Neckar'ın karşı yakasında huzurlu nehir kenarı yürüyüşü.", "description_en": "Peaceful riverside walk on opposite bank of Neckar.", "bestTime": "İkindi", "tips": "Alte Brücke'den karşıya geçip yürüyün.", "tips_en": "Cross from Alte Brücke and walk."}
]

# BATCH 12: Ek Alışveriş & Özel Mekanlar
batch_12 = [
    {"name": "Antiquariat Hatry", "name_en": "Hatry Antiquarian", "area": "Altstadt", "category": "Alışveriş", "tags": ["kitap", "antika", "koleksiyon"], "distanceFromCenter": 0.2, "lat": 49.4095, "lng": 8.7040, "price": "variable", "rating": 4.5, "description": "Nadir kitaplar ve antika materyaller satan eski kitapçı.", "description_en": "Old bookshop selling rare books and antique materials.", "bestTime": "Gündüz", "tips": "Kitap severler için cennet.", "tips_en": "Paradise for book lovers."},
    {"name": "Heidelberg Seramik", "name_en": "Heidelberg Ceramics", "area": "Altstadt", "category": "Alışveriş", "tags": ["seramik", "el işi", "hediyelik"], "distanceFromCenter": 0.15, "lat": 49.4100, "lng": 8.7085, "price": "medium", "rating": 4.3, "description": "El yapımı yerel seramik ve çömlekçilik ürünleri.", "description_en": "Handmade local ceramics and pottery.", "bestTime": "Gündüz", "tips": "Özel hediyelik için ideal.", "tips_en": "Ideal for special gifts."},
    {"name": "Galeria Kaufhof", "name_en": "Galeria Kaufhof", "area": "Altstadt", "category": "Alışveriş", "tags": ["mağaza", "alışveriş", "moda"], "distanceFromCenter": 0.1, "lat": 49.4098, "lng": 8.7050, "price": "variable", "rating": 4.0, "description": "Hauptstraße üzerinde büyük alışveriş mağazası.", "description_en": "Large department store on Hauptstraße.", "bestTime": "Gündüz", "tips": "En üst katta şehir manzaralı kafe.", "tips_en": "Cafe with city view on top floor."},
    {"name": "Wochenmarkt", "name_en": "Weekly Market", "area": "Altstadt", "category": "Alışveriş", "tags": ["pazar", "yiyecek", "yerel"], "distanceFromCenter": 0.1, "lat": 49.4096, "lng": 8.7095, "price": "low", "rating": 4.6, "description": "Çarşamba ve Cumartesi kurulan yerel üreticiler pazarı.", "description_en": "Local producers market on Wed and Sat.", "bestTime": "Sabah", "tips": "Taze ekmek, peynir ve meyve için en iyi adres.", "tips_en": "Best for fresh bread, cheese and fruit."}
]

# BATCH 13: Ek Aktiviteler
batch_13 = [
    {"name": "Kano Kiralama Neckar", "name_en": "Neckar Canoe Rental", "area": "Neuenheim", "category": "Deneyim", "tags": ["kano", "su sporu", "nehir"], "distanceFromCenter": 0.5, "lat": 49.4140, "lng": 8.7000, "price": "medium", "rating": 4.4, "description": "Neckar Nehri'nde kano veya kayak kiralayarak şehri keşfedin.", "description_en": "Explore the city by renting canoe or kayak on Neckar River.", "bestTime": "Yaz", "tips": "Güneşli günler için ideal.", "tips_en": "Ideal for sunny days."},
    {"name": "Segway Turu Heidelberg", "name_en": "Heidelberg Segway Tour", "area": "Altstadt", "category": "Deneyim", "tags": ["segway", "tur", "eğlence"], "distanceFromCenter": 0.2, "lat": 49.4095, "lng": 8.7060, "price": "high", "rating": 4.3, "description": "Segway ile eski şehri ve nehir kenarını keşfedin.", "description_en": "Explore old town and riverside by Segway.", "bestTime": "Gündüz", "tips": "Önceden rezervasyon yapın.", "tips_en": "Book in advance."},
    {"name": "Fotoğraf Yürüyüşü", "name_en": "Photography Walk", "area": "Altstadt", "category": "Deneyim", "tags": ["fotoğraf", "tur", "sanat"], "distanceFromCenter": 0.0, "lat": 49.4095, "lng": 8.7065, "price": "medium", "rating": 4.5, "description": "Rehberli fotoğraf turu ile en güzel açıları keşfedin.", "description_en": "Discover best angles with guided photography tour.", "bestTime": "Gün batımı", "tips": "Gün batımı turları en popüler.", "tips_en": "Sunset tours most popular."},
    {"name": "Şarap Tadımı Turu", "name_en": "Wine Tasting Tour", "area": "Handschuhsheim", "category": "Deneyim", "tags": ["şarap", "tadım", "tur"], "distanceFromCenter": 3.0, "lat": 49.4280, "lng": 8.6850, "price": "medium", "rating": 4.6, "description": "Yerel bağlarda üretilen Palatinate şaraplarının tadımı.", "description_en": "Tasting of Palatinate wines produced in local vineyards.", "bestTime": "İkindi", "tips": "Riesling ve Spätburgunder'i deneyin.", "tips_en": "Try Riesling and Spätburgunder."}
]

def enrich():
    filepath = 'assets/cities/heidelberg.json'
    all_new = batch_8 + batch_9 + batch_10 + batch_11 + batch_12 + batch_13
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace('ö', 'o').replace('ü', 'u').replace('ä', 'a').replace('ß', 'ss').replace('(', '').replace(')', '')
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        places_to_add.append(place)
        time.sleep(0.3)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places. Total: {len(data['highlights'])}")

if __name__ == "__main__":
    enrich()
