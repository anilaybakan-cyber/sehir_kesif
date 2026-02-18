import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    try:
        find_place_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(place_name)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:15000@37.0662,37.3833"
        response = requests.get(find_place_url)
        data = response.json()
        if data['status'] == 'OK' and len(data['candidates']) > 0:
            candidate = data['candidates'][0]
            if 'photos' in candidate:
                photo_reference = candidate['photos'][0]['photo_reference']
                return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={API_KEY}"
        return None
    except:
        return None

# BATCH 13: MORE KEBAB & MEAT SPECIALISTS  
batch_13 = [
    {"name": "Şehitkamil Kebapçısı", "name_en": "Sehitkamil Kebab", "area": "Şehitkamil", "category": "Restoran", "tags": ["kebap", "yerel", "lezzet"], "distanceFromCenter": 1.5, "lat": 37.0710, "lng": 37.3760, "price": "medium", "rating": 4.5, "description": "Mahalle kebapçısı, turist görmemiş gerçek yerel lezzet.", "description_en": "Neighborhood kebab place, authentic local flavor unseen by tourists.", "bestTime": "Öğle", "bestTime_en": "Lunch", "tips": "Öğle saatlerinde esnaf kalabalığı olur.", "tips_en": "Crowded with tradesmen at lunch."},
    {"name": "Ciğer Sarayı", "name_en": "Liver Palace", "area": "Şahinbey", "category": "Restoran", "tags": ["ciğer", "şiş", "lokanta"], "distanceFromCenter": 0.6, "lat": 37.0605, "lng": 37.3795, "price": "low", "rating": 4.6, "description": "Ciğer şiş konusunda uzmanlaşmış, temiz ve düzenli lokanta.", "description_en": "Restaurant specialized in liver skewers, clean and orderly.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Kahvaltıda ciğer Antep geleneğidir.", "tips_en": "Liver for breakfast is an Antep tradition."},
    {"name": "Etçi Mehmet", "name_en": "Butcher Mehmet", "area": "Şehitkamil", "category": "Restoran", "tags": ["et", "steak", "modern"], "distanceFromCenter": 2.5, "lat": 37.0780, "lng": 37.3680, "price": "high", "rating": 4.7, "description": "Premium et kesimi ve modern sunum yapan butik restoran.", "description_en": "Boutique restaurant with premium meat cuts and modern presentation.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "T-bone steak çok popüler, önceden sipariş verin.", "tips_en": "T-bone steak is very popular, order in advance."},
    {"name": "Ocakbaşı Ali Usta", "name_en": "Ocakbasi Ali Usta", "area": "Şahinbey", "category": "Restoran", "tags": ["ocakbaşı", "mangal", "geleneksel"], "distanceFromCenter": 0.8, "lat": 37.0580, "lng": 37.3780, "price": "medium", "rating": 4.5, "description": "Geleneksel ocakbaşı, közde pişen etler ve muhteşem meze.", "description_en": "Traditional grill, meats cooked over embers and wonderful meze.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Ocağın başında oturmak en iyi deneyim.", "tips_en": "Sitting by the grill is the best experience."},
    {"name": "Kaburga Dolma Evi", "name_en": "Stuffed Rib House", "area": "Şahinbey", "category": "Restoran", "tags": ["kaburga", "dolma", "spesiyal"], "distanceFromCenter": 0.5, "lat": 37.0625, "lng": 37.3820, "price": "high", "rating": 4.8, "description": "Antep'e özgü kaburga dolması yapan nadir restoranlardan.", "description_en": "One of the rare restaurants making Antep's special stuffed ribs.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Önceden sipariş verin, hazırlanması zaman alır.", "tips_en": "Order in advance, it takes time to prepare."},
    {"name": "Pide Salonu", "name_en": "Pide Hall", "area": "Şehitkamil", "category": "Restoran", "tags": ["pide", "lahmacun", "hızlı"], "distanceFromCenter": 1.2, "lat": 37.0690, "lng": 37.3770, "price": "low", "rating": 4.4, "description": "Hızlı servis, lezzetli Antep pidesi ve lahmacun.", "description_en": "Fast service, delicious Antep pide and lahmacun.", "bestTime": "Öğle", "bestTime_en": "Lunch", "tips": "Kuşbaşılı pide favorimiz.", "tips_en": "Our favorite is diced meat pide."},
    {"name": "Tantuni Durağı", "name_en": "Tantuni Stop", "area": "Şahinbey", "category": "Sokak Lezzeti", "tags": ["tantuni", "dürüm", "hızlı"], "distanceFromCenter": 0.4, "lat": 37.0615, "lng": 37.3810, "price": "low", "rating": 4.3, "description": "Mersin usulü tantuni yapan, geç saatlere kadar açık mekan.", "description_en": "Place making Mersin style tantuni, open until late hours.", "bestTime": "Gece", "bestTime_en": "Night", "tips": "Gece acıkınca en iyi adres.", "tips_en": "Best address when hungry at night."}
]

# BATCH 14: MORE TRADITIONAL & HOME COOKING
batch_14 = [
    {"name": "Ana Lokantası", "name_en": "Mother's Restaurant", "area": "Şahinbey", "category": "Restoran", "tags": ["ev yemeği", "anne", "sulu"], "distanceFromCenter": 0.5, "lat": 37.0620, "lng": 37.3815, "price": "low", "rating": 4.5, "description": "Günlük pişen ev yemekleri, anne eli değmiş lezzet.", "description_en": "Daily cooked home meals, taste touched by mother's hand.", "bestTime": "Öğle", "bestTime_en": "Lunch", "tips": "Taze yemek için 12:00'da gidin.", "tips_en": "Go at 12:00 for fresh food."},
    {"name": "Esnaf Lokantası", "name_en": "Tradesman's Restaurant", "area": "Şahinbey", "category": "Restoran", "tags": ["esnaf", "ekonomik", "doyurucu"], "distanceFromCenter": 0.3, "lat": 37.0630, "lng": 37.3825, "price": "low", "rating": 4.3, "description": "Çarşı esnafının gittiği ekonomik ve doyurucu lokanta.", "description_en": "Economical and filling restaurant visited by bazaar tradesmen.", "bestTime": "Öğle", "bestTime_en": "Lunch", "tips": "Tabldot menüyle 3-4 çeşit yemek yiyebilirsiniz.", "tips_en": "With set menu you can eat 3-4 types of food."},
    {"name": "Ekşili Köfte Evi", "name_en": "Sour Meatball House", "area": "Şahinbey", "category": "Restoran", "tags": ["köfte", "ekşili", "ev yapımı"], "distanceFromCenter": 0.4, "lat": 37.0625, "lng": 37.3820, "price": "medium", "rating": 4.6, "description": "Antep'e özgü ekşili köfte yapan uzman mekan.", "description_en": "Expert place making Antep's special sour meatballs.", "bestTime": "Öğle", "bestTime_en": "Lunch", "tips": "Yanında pilav ve cacık şart.", "tips_en": "Rice and tzatziki are a must alongside."},
    {"name": "Analı Kızlı Lokantası", "name_en": "Anali Kizli Restaurant", "area": "Şahinbey", "category": "Restoran", "tags": ["analı kızlı", "geleneksel", "tencere"], "distanceFromCenter": 0.5, "lat": 37.0618, "lng": 37.3812, "price": "medium", "rating": 4.7, "description": "Antep'in müthiş lezzeti 'Analı Kızlı' yapan nadir yerlerden.", "description_en": "One of the rare places making Antep's amazing dish 'Anali Kizli'.", "bestTime": "Öğle", "bestTime_en": "Lunch", "tips": "İsmi gibi eğlenceli bir yemek, mutlaka deneyin.", "tips_en": "A fun dish like its name, must try."},
    {"name": "Firik Pilavı Evi", "name_en": "Firik Pilaf House", "area": "Şahinbey", "category": "Restoran", "tags": ["firik", "pilav", "yöresel"], "distanceFromCenter": 0.6, "lat": 37.0610, "lng": 37.3805, "price": "medium", "rating": 4.5, "description": "Antep'e özgü firik buğdayından pilav yapan mekan.", "description_en": "Place making pilaf from Antep's special firik wheat.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Kuzu incik ile firik pilavı harika ikili.", "tips_en": "Lamb shank with firik pilaf is a great duo."},
    {"name": "Oruk Evi", "name_en": "Oruk House", "area": "Şahinbey", "category": "Restoran", "tags": ["oruk", "içli köfte", "geleneksel"], "distanceFromCenter": 0.4, "lat": 37.0622, "lng": 37.3818, "price": "medium", "rating": 4.6, "description": "İçli köftenin Antep versiyonu 'Oruk' yapan usta.", "description_en": "Master making 'Oruk', the Antep version of stuffed meatballs.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Sulu ve kuru olmak üzere iki versiyonu var.", "tips_en": "There are two versions: with broth and dry."}
]

# BATCH 15: MORE SPECIALTY CAFES & BARS
batch_15 = [
    {"name": "Rooftop Bar", "name_en": "Rooftop Bar", "area": "Şehitkamil", "category": "Bar", "tags": ["bar", "manzara", "gece"], "distanceFromCenter": 2.0, "lat": 37.0750, "lng": 37.3700, "price": "high", "rating": 4.4, "description": "Şehir manzaralı çatı bar, kokteyl ve canlı müzik.", "description_en": "Rooftop bar with city view, cocktails and live music.", "bestTime": "Gece", "bestTime_en": "Night", "tips": "Hafta sonu canlı müzik var.", "tips_en": "Live music on weekends."},
    {"name": "Bira Evi", "name_en": "Beer House", "area": "Şehitkamil", "category": "Bar", "tags": ["bira", "pub", "sosyal"], "distanceFromCenter": 1.5, "lat": 37.0720, "lng": 37.3750, "price": "medium", "rating": 4.2, "description": "Yerli ve ithal biralar, spor maçları izleme imkanı.", "description_en": "Local and imported beers, ability to watch sports matches.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Maç günleri çok kalabalık.", "tips_en": "Very crowded on match days."},
    {"name": "Specialty Coffee", "name_en": "Specialty Coffee", "area": "Şehitkamil", "category": "Kafe", "tags": ["kahve", "3. dalga", "modern"], "distanceFromCenter": 2.5, "lat": 37.0780, "lng": 37.3680, "price": "high", "rating": 4.5, "description": "Üçüncü dalga kahve akımının Antep temsilcisi.", "description_en": "Antep representative of the third wave coffee movement.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Pour-over kahve deneyin.", "tips_en": "Try pour-over coffee."},
    {"name": "Kitap Kafe", "name_en": "Book Cafe", "area": "Şahinbey", "category": "Kafe", "tags": ["kitap", "sessiz", "okuma"], "distanceFromCenter": 0.5, "lat": 37.0630, "lng": 37.3820, "price": "medium", "rating": 4.4, "description": "Kitap okumak için sessiz ortam sunan huzurlu kafe.", "description_en": "Peaceful cafe offering quiet environment for reading.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Laptop ile çalışmak için ideal.", "tips_en": "Ideal for working with laptop."},
    {"name": "Çikolata Evi", "name_en": "Chocolate House", "area": "Şehitkamil", "category": "Kafe", "tags": ["çikolata", "tatlı", "premium"], "distanceFromCenter": 2.0, "lat": 37.0760, "lng": 37.3720, "price": "high", "rating": 4.6, "description": "El yapımı çikolatalar ve sıcak çikolata.", "description_en": "Handmade chocolates and hot chocolate.", "bestTime": "İkindi", "bestTime_en": "Afternoon", "tips": "Fıstıklı çikolata Antep versiyonu mutlaka deneyin.", "tips_en": "Must try pistachio chocolate Antep version."}
]

# BATCH 16: MORE HISTORIC & RELIGIOUS SITES
batch_16 = [
    {"name": "Boyacı Camii", "name_en": "Boyaci Mosque", "area": "Şahinbey", "category": "Tarihi", "tags": ["cami", "tarihi", "mimari"], "distanceFromCenter": 0.3, "lat": 37.0628, "lng": 37.3822, "price": "free", "rating": 4.4, "description": "17. yüzyıldan kalma, zarif mimarisiyle dikkat çeken cami.", "description_en": "17th century mosque, notable for its elegant architecture.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Çarşı gezisi sırasında uğrayın.", "tips_en": "Stop by during bazaar visit."},
    {"name": "Ömer Ersoy Camii", "name_en": "Omer Ersoy Mosque", "area": "Şahinbey", "category": "Tarihi", "tags": ["cami", "modern", "büyük"], "distanceFromCenter": 0.5, "lat": 37.0620, "lng": 37.3810, "price": "free", "rating": 4.5, "description": "Modern mimariyle inşa edilmiş, şehrin en büyük camilerinden.", "description_en": "One of the city's largest mosques, built with modern architecture.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Cuma namazı çok kalabalık.", "tips_en": "Friday prayer is very crowded."},
    {"name": "Tahta Kahve Camii", "name_en": "Tahta Kahve Mosque", "area": "Şahinbey", "category": "Tarihi", "tags": ["cami", "ahşap", "nadir"], "distanceFromCenter": 0.4, "lat": 37.0625, "lng": 37.3815, "price": "free", "rating": 4.3, "description": "Ahşap süslemeleriyle dikkat çeken küçük tarihi cami.", "description_en": "Small historic mosque notable for its wooden decorations.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Küçük ama çok otantik.", "tips_en": "Small but very authentic."},
    {"name": "Naib Hamamı", "name_en": "Naib Hamam", "area": "Şahinbey", "category": "Tarihi", "tags": ["hamam", "tarihi", "mimari"], "distanceFromCenter": 0.3, "lat": 37.0632, "lng": 37.3828, "price": "free", "rating": 4.2, "description": "Artık kullanılmayan ama mimarisi korunan tarihi hamam.", "description_en": "Historic bath no longer in use but with preserved architecture.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Dışarıdan fotoğraf çekilebilir.", "tips_en": "Can take photos from outside."},
    {"name": "Kendirci Camii", "name_en": "Kendirci Mosque", "area": "Şahinbey", "category": "Tarihi", "tags": ["cami", "osmanlı", "tarihi"], "distanceFromCenter": 0.4, "lat": 37.0618, "lng": 37.3812, "price": "free", "rating": 4.4, "description": "Osmanlı döneminden kalma, şehrin en eski camilerinden.", "description_en": "From Ottoman period, one of the city's oldest mosques.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Namaz vakitlerinde girmek saygılı olur.", "tips_en": "Entering during prayer times is respectful."}
]

# BATCH 17: MORE VIEWPOINTS & UNIQUE EXPERIENCES
batch_17 = [
    {"name": "Şehitlik Tepesi", "name_en": "Martyrs Hill", "area": "Şahinbey", "category": "Manzara", "tags": ["tepe", "anıt", "manzara"], "distanceFromCenter": 1.0, "lat": 37.0550, "lng": 37.3750, "price": "free", "rating": 4.5, "description": "Şehitleri anmak için yapılan anıt ve şehir manzarası.", "description_en": "Monument to commemorate martyrs and city view.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "25 Aralık'ta resmi tören yapılır.", "tips_en": "Official ceremony on December 25th."},
    {"name": "Panorama 25 Aralık Müzesi", "name_en": "Panorama December 25 Museum", "area": "Şahinbey", "category": "Müze", "tags": ["panorama", "tarih", "savaş"], "distanceFromCenter": 0.8, "lat": 37.0580, "lng": 37.3800, "price": "low", "rating": 4.7, "description": "Gaziantep savunmasını anlatan etkileyici panoramik müze.", "description_en": "Impressive panoramic museum telling the Gaziantep defense.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Rehberli tur almak deneyimi artırır.", "tips_en": "Taking a guided tour enhances the experience."},
    {"name": "Astronomi Müzesi", "name_en": "Astronomy Museum", "area": "Şehitkamil", "category": "Müze", "tags": ["uzay", "bilim", "çocuk"], "distanceFromCenter": 5.0, "lat": 37.1000, "lng": 37.3500, "price": "medium", "rating": 4.4, "description": "Planetaryum ve uzay sergisi olan interaktif müze.", "description_en": "Interactive museum with planetarium and space exhibition.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Çocuklar için harika, planetaryum gösterisi mutlaka izleyin.", "tips_en": "Great for kids, must watch planetarium show."},
    {"name": "Savaş Araçları Müzesi", "name_en": "War Vehicles Museum", "area": "Şehitkamil", "category": "Müze", "tags": ["tank", "uçak", "askeri"], "distanceFromCenter": 3.0, "lat": 37.0900, "lng": 37.3600, "price": "low", "rating": 4.3, "description": "Tank, uçak ve askeri araçların sergilendiği açık hava müzesi.", "description_en": "Open-air museum exhibiting tanks, planes and military vehicles.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Çocuklar araçların üzerine çıkabiliyor.", "tips_en": "Children can climb on the vehicles."},
    {"name": "Halfeti Sular Altı Köyü", "name_en": "Halfeti Underwater Village", "area": "Halfeti", "category": "Deneyim", "tags": ["sular altı", "köy", "baraj"], "distanceFromCenter": 120.0, "lat": 37.2600, "lng": 37.8800, "price": "free", "rating": 4.6, "description": "Baraj sularıyla kısmen batan köylerin kalıntıları.", "description_en": "Remains of villages partially submerged by dam waters.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Tekne turu ile birleştirin.", "tips_en": "Combine with boat tour."},
    {"name": "Kara Gül Bahçesi", "name_en": "Black Rose Garden", "area": "Halfeti", "category": "Doğa", "tags": ["gül", "siyah", "nadir"], "distanceFromCenter": 120.0, "lat": 37.2550, "lng": 37.8750, "price": "free", "rating": 4.7, "description": "Dünyada sadece burada yetişen nadir siyah güllerin bahçesi.", "description_en": "Garden of rare black roses that grow only here in the world.", "bestTime": "İlkbahar", "bestTime_en": "Spring", "tips": "Mayıs-Haziran en güzel çiçeklenme zamanı.", "tips_en": "May-June is the best flowering time."}
]

# BATCH 18: MORE SHOPPING & LOCAL PRODUCTS
batch_18 = [
    {"name": "Kuruyemişçi Çarşısı", "name_en": "Nuts Bazaar", "area": "Şahinbey", "category": "Alışveriş", "tags": ["kuruyemiş", "fıstık", "ceviz"], "distanceFromCenter": 0.3, "lat": 37.0630, "lng": 37.3825, "price": "medium", "rating": 4.6, "description": "Her türlü kuruyemiş ve özellikle Antep fıstığı.", "description_en": "All kinds of nuts, especially Antep pistachios.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Kavrulmuş ve çiğ farkını sorun.", "tips_en": "Ask the difference between roasted and raw."},
    {"name": "Baharatçı", "name_en": "Spice Shop", "area": "Şahinbey", "category": "Alışveriş", "tags": ["baharat", "isot", "biber"], "distanceFromCenter": 0.3, "lat": 37.0628, "lng": 37.3822, "price": "low", "rating": 4.7, "description": "Antep isotu ve çeşitli baharatlar satan geleneksel dükkan.", "description_en": "Traditional shop selling Antep isot and various spices.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "İsot Antep'e özgü, mutlaka alın.", "tips_en": "Isot is unique to Antep, must buy."},
    {"name": "Hediyelik Eşya Dükkanı", "name_en": "Souvenir Shop", "area": "Şahinbey", "category": "Alışveriş", "tags": ["hediyelik", "hatıra", "turistik"], "distanceFromCenter": 0.2, "lat": 37.0635, "lng": 37.3830, "price": "medium", "rating": 4.2, "description": "Antep temalı hatıralar ve hediyelikler.", "description_en": "Antep-themed souvenirs and gifts.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Mınyatür bakır eşyalar güzel hediye.", "tips_en": "Miniature copper items are nice gifts."},
    {"name": "Dokumacılar Çarşısı", "name_en": "Weavers Bazaar", "area": "Şahinbey", "category": "Alışveriş", "tags": ["dokuma", "kilim", "halı"], "distanceFromCenter": 0.4, "lat": 37.0622, "lng": 37.3818, "price": "high", "rating": 4.4, "description": "El dokuma kilim ve halıların satıldığı çarşı.", "description_en": "Bazaar where handwoven kilims and rugs are sold.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Fiyat pazarlığı yapmayı unutmayın.", "tips_en": "Don't forget to bargain."},
    {"name": "Altın Çarşısı", "name_en": "Gold Bazaar", "area": "Şahinbey", "category": "Alışveriş", "tags": ["altın", "takı", "mücevher"], "distanceFromCenter": 0.3, "lat": 37.0632, "lng": 37.3828, "price": "high", "rating": 4.3, "description": "Altın ve gümüş takıların satıldığı kuyumcular çarşısı.", "description_en": "Jewelers bazaar where gold and silver jewelry is sold.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Antep işi bilezikler çok değerli.", "tips_en": "Antep-style bracelets are very valuable."}
]

def enrich():
    filepath = 'assets/cities/gaziantep.json'
    all_new = batch_13 + batch_14 + batch_15 + batch_16 + batch_17 + batch_18
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    print(f"Loaded {len(data['highlights'])} existing places.")
    
    existing_names = {p['name'].lower() for p in data['highlights']}
    places_to_add = []
    
    for place in all_new:
        if place['name'].lower() in existing_names:
            print(f"Skipping: {place['name']}")
            continue
        print(f"Processing: {place['name']}")
        place_id = place['name'].lower().replace(' ', '-').replace('ç', 'c').replace('ğ', 'g').replace('ı', 'i').replace('ö', 'o').replace('ş', 's').replace('ü', 'u').replace('(', '').replace(')', '')
        place['id'] = place_id
        photo_url = get_google_photo_url(place['name'])
        if not photo_url and 'name_en' in place:
            photo_url = get_google_photo_url(place['name_en'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        places_to_add.append(place)
        time.sleep(0.3)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nAdded {len(places_to_add)} new places. Total: {len(data['highlights'])}")

if __name__ == "__main__":
    enrich()
