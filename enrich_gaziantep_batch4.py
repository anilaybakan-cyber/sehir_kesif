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

# BATCH 19: FINAL FOOD ADDITIONS
batch_19 = [
    {"name": "Tirit Lokantası", "name_en": "Tirit Restaurant", "area": "Şahinbey", "category": "Restoran", "tags": ["tirit", "geleneksel", "kahvaltı"], "distanceFromCenter": 0.4, "lat": 37.0622, "lng": 37.3818, "price": "low", "rating": 4.5, "description": "Geleneksel Antep tiridi yapan nadir mekanlardan.", "description_en": "One of the rare places making traditional Antep tirit.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Sabah kahvaltısı için ideal.", "tips_en": "Ideal for breakfast."},
    {"name": "Kelle Paça", "name_en": "Kelle Paca", "area": "Şahinbey", "category": "Restoran", "tags": ["kelle", "paça", "şifa"], "distanceFromCenter": 0.3, "lat": 37.0630, "lng": 37.3825, "price": "low", "rating": 4.4, "description": "Kelle paça çorbası ustası, geç saatlere kadar açık.", "description_en": "Master of head and trotter soup, open until late hours.", "bestTime": "Gece", "bestTime_en": "Night", "tips": "Gece yarısı açık sayılı yerlerden.", "tips_en": "One of the few places open at midnight."},
    {"name": "Mumbar Dolma Evi", "name_en": "Mumbar Dolma House", "area": "Şahinbey", "category": "Restoran", "tags": ["mumbar", "dolma", "yöresel"], "distanceFromCenter": 0.5, "lat": 37.0618, "lng": 37.3812, "price": "medium", "rating": 4.6, "description": "Bağırsak dolması yapan (mumbar) otantik mekan.", "description_en": "Authentic place making stuffed intestine (mumbar).", "bestTime": "Öğle", "bestTime_en": "Lunch", "tips": "Cesaret ister ama çok lezzetlidir.", "tips_en": "Requires courage but very delicious."},
    {"name": "Şıllık Tatlıcısı", "name_en": "Sillik Dessert", "area": "Şahinbey", "category": "Tatlı", "tags": ["şıllık", "geleneksel", "nadir"], "distanceFromCenter": 0.4, "lat": 37.0625, "lng": 37.3820, "price": "low", "rating": 4.5, "description": "Antep'e özgü şıllık tatlısı yapan nadir yer.", "description_en": "Rare place making Antep's special sillik dessert.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Ramazan ayında çok popüler.", "tips_en": "Very popular during Ramadan."},
    {"name": "Sac Kavurma", "name_en": "Sac Kavurma", "area": "Şehitkamil", "category": "Restoran", "tags": ["kavurma", "et", "sac"], "distanceFromCenter": 1.5, "lat": 37.0700, "lng": 37.3760, "price": "high", "rating": 4.7, "description": "Saç üzerinde kavrulan etle ünlü et restoranı.", "description_en": "Meat restaurant famous for meat roasted on sac.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Porsiyon büyük, paylaşarak yiyin.", "tips_en": "Portions are big, share when eating."},
    {"name": "Çiğ Köfte Ustası", "name_en": "Cig Kofte Master", "area": "Şahinbey", "category": "Sokak Lezzeti", "tags": ["çiğ köfte", "vejetaryen", "acı"], "distanceFromCenter": 0.3, "lat": 37.0632, "lng": 37.3828, "price": "low", "rating": 4.5, "description": "El yapımı çiğ köfte, lavaş ve turşu.", "description_en": "Handmade raw meatballs, lavash and pickles.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Acılı olur, dikkat!", "tips_en": "It's spicy, be careful!"},
    {"name": "Patlıcan Kebabı Evi", "name_en": "Eggplant Kebab House", "area": "Şahinbey", "category": "Restoran", "tags": ["patlıcan", "kebap", "özel"], "distanceFromCenter": 0.5, "lat": 37.0620, "lng": 37.3815, "price": "medium", "rating": 4.6, "description": "Közlenmiş patlıcan üzerine kebap - Ali Nazik benzeri.", "description_en": "Kebab on grilled eggplant - similar to Ali Nazik.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Doyurucu, az sipariş verin.", "tips_en": "Filling, order less."},
    {"name": "Mercimek Köftecisi", "name_en": "Lentil Kofte", "area": "Şahinbey", "category": "Sokak Lezzeti", "tags": ["mercimek", "vejetaryen", "soğuk"], "distanceFromCenter": 0.3, "lat": 37.0628, "lng": 37.3822, "price": "low", "rating": 4.3, "description": "Vejetaryen seçenek - el yapımı mercimek köftesi.", "description_en": "Vegetarian option - handmade lentil kofte.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Hafif atıştırmalık olarak ideal.", "tips_en": "Ideal as a light snack."}
]

# BATCH 20: FINAL CULTURAL & NATURE ADDITIONS
batch_20 = [
    {"name": "Şehir Parkı", "name_en": "City Park", "area": "Şahinbey", "category": "Park", "tags": ["park", "merkez", "yeşil"], "distanceFromCenter": 0.5, "lat": 37.0640, "lng": 37.3850, "price": "free", "rating": 4.3, "description": "Şehir merkezinde dinlenmek için yeşil alan.", "description_en": "Green area to rest in the city center.", "bestTime": "İkindi", "bestTime_en": "Afternoon", "tips": "Çocuk oyun alanları mevcut.", "tips_en": "Playground areas available."},
    {"name": "Teleferik Tesisleri", "name_en": "Cable Car", "area": "Şahinbey", "category": "Deneyim", "tags": ["teleferik", "manzara", "eğlence"], "distanceFromCenter": 3.0, "lat": 37.0400, "lng": 37.3500, "price": "medium", "rating": 4.4, "description": "Şehir manzarası için teleferik turu.", "description_en": "Cable car tour for city view.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "Akşam ışıkları çok güzel görünür.", "tips_en": "Evening lights look very beautiful."},
    {"name": "Film Platosu", "name_en": "Movie Set", "area": "Şehitkamil", "category": "Deneyim", "tags": ["film", "set", "fotoğraf"], "distanceFromCenter": 10.0, "lat": 37.0200, "lng": 37.3000, "price": "medium", "rating": 4.2, "description": "Tarihi filmler için kullanılan replikalar.", "description_en": "Replicas used for historical movies.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Fotoğraf çekmek için harika dekorlar.", "tips_en": "Great decorations for taking photos."},
    {"name": "Dağ Evi Restaurant", "name_en": "Mountain House", "area": "Dülükbaba", "category": "Restoran", "tags": ["doğa", "manzara", "mangal"], "distanceFromCenter": 8.0, "lat": 37.1150, "lng": 37.3350, "price": "high", "rating": 4.5, "description": "Ormanlık alanda manzaralı restoran.", "description_en": "Restaurant with view in forested area.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Rezervasyon şart, hafta sonu çok dolu.", "tips_en": "Reservation required, very full on weekends."},
    {"name": "Antika Pazarı", "name_en": "Antique Market", "area": "Şahinbey", "category": "Alışveriş", "tags": ["antika", "eski", "koleksiyon"], "distanceFromCenter": 0.4, "lat": 37.0625, "lng": 37.3815, "price": "variable", "rating": 4.3, "description": "Eski eşyalar ve antikalar için pazar.", "description_en": "Market for old items and antiques.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Pazarlık şart, ilk fiyata almayın.", "tips_en": "Bargaining is a must, don't take first price."},
    {"name": "Etnografya Sergisi", "name_en": "Ethnography Exhibition", "area": "Şahinbey", "category": "Müze", "tags": ["etnografya", "kültür", "gelenek"], "distanceFromCenter": 0.5, "lat": 37.0630, "lng": 37.3820, "price": "low", "rating": 4.4, "description": "Antep yaşam kültürünü anlatan sergi.", "description_en": "Exhibition explaining Antep life culture.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Geleneksel kıyafetler çok ilginç.", "tips_en": "Traditional clothing is very interesting."},
    {"name": "Sanat Galerisi", "name_en": "Art Gallery", "area": "Şehitkamil", "category": "Müze", "tags": ["sanat", "modern", "sergi"], "distanceFromCenter": 2.0, "lat": 37.0750, "lng": 37.3700, "price": "free", "rating": 4.2, "description": "Yerel sanatçıların eserlerinden oluşan sergi.", "description_en": "Exhibition of works by local artists.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Değişen sergiler için web sitesini kontrol edin.", "tips_en": "Check website for changing exhibitions."},
    {"name": "Kültür Merkezi", "name_en": "Cultural Center", "area": "Şahinbey", "category": "Deneyim", "tags": ["kültür", "etkinlik", "konser"], "distanceFromCenter": 0.8, "lat": 37.0590, "lng": 37.3790, "price": "variable", "rating": 4.4, "description": "Konser ve kültürel etkinlikler için merkez.", "description_en": "Center for concerts and cultural events.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Etkinlik programını takip edin.", "tips_en": "Follow the event program."}
]

# BATCH 21: MORE SPECIALTY EXPERIENCES
batch_21 = [
    {"name": "Antep Mutfağı Kursu", "name_en": "Antep Cuisine Course", "area": "Şahinbey", "category": "Deneyim", "tags": ["kurs", "yemek", "aşçılık"], "distanceFromCenter": 0.5, "lat": 37.0640, "lng": 37.3840, "price": "high", "rating": 4.8, "description": "Ev hanımlarından Antep yemekleri öğrenin.", "description_en": "Learn Antep dishes from housewives.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Önceden rezervasyon şart.", "tips_en": "Prior reservation required."},
    {"name": "Fıstık Hasadı Turu", "name_en": "Pistachio Harvest Tour", "area": "Nizip", "category": "Deneyim", "tags": ["fıstık", "hasat", "tarım"], "distanceFromCenter": 45.0, "lat": 37.0300, "lng": 37.7800, "price": "medium", "rating": 4.6, "description": "Sonbaharda fıstık hasadına katılma deneyimi.", "description_en": "Experience participating in pistachio harvest in autumn.", "bestTime": "Eylül-Ekim", "bestTime_en": "September-October", "tips": "Sadece hasat mevsiminde mümkün.", "tips_en": "Only possible during harvest season."},
    {"name": "Geleneksel Oyun Gecesi", "name_en": "Traditional Game Night", "area": "Şahinbey", "category": "Deneyim", "tags": ["oyun", "tavla", "okey"], "distanceFromCenter": 0.3, "lat": 37.0625, "lng": 37.3820, "price": "low", "rating": 4.3, "description": "Kahvehanelerde yerel halkla tavla ve okey.", "description_en": "Backgammon and okey with locals in coffeehouses.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Kaybedeceğinizi kabul edin, rakipler usta!", "tips_en": "Accept you'll lose, opponents are experts!"},
    {"name": "Hammam Deneyimi", "name_en": "Hammam Experience", "area": "Şahinbey", "category": "Deneyim", "tags": ["hamam", "spa", "geleneksel"], "distanceFromCenter": 0.4, "lat": 37.0630, "lng": 37.3825, "price": "medium", "rating": 4.6, "description": "Otantik Türk hamamı deneyimi.", "description_en": "Authentic Turkish hammam experience.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Kese ve köpük masajı dahil paket alın.", "tips_en": "Get package including scrub and foam massage."},
    {"name": "Bakır Atölyesi Workshop", "name_en": "Copper Workshop", "area": "Şahinbey", "category": "Deneyim", "tags": ["bakır", "workshop", "el sanatı"], "distanceFromCenter": 0.3, "lat": 37.0632, "lng": 37.3828, "price": "medium", "rating": 4.5, "description": "Ustalardan bakır işçiliği öğrenin.", "description_en": "Learn coppersmith craft from masters.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Kendi kupanızı yapıp götürebilirsiniz.", "tips_en": "You can make and take your own cup."},
    {"name": "Gece Şehir Turu", "name_en": "Night City Tour", "area": "Merkez", "category": "Deneyim", "tags": ["tur", "gece", "ışıklar"], "distanceFromCenter": 0.0, "lat": 37.0662, "lng": 37.3833, "price": "medium", "rating": 4.4, "description": "Işıklandırılmış tarihi mekanların gece turu.", "description_en": "Night tour of illuminated historical places.", "bestTime": "Gece", "bestTime_en": "Night", "tips": "Kale gece çok etkileyici görünür.", "tips_en": "Castle looks very impressive at night."},
    {"name": "Bisiklet Turu", "name_en": "Bicycle Tour", "area": "Alleben", "category": "Deneyim", "tags": ["bisiklet", "spor", "doğa"], "distanceFromCenter": 5.0, "lat": 37.0350, "lng": 37.3100, "price": "low", "rating": 4.3, "description": "Alleben Göleti çevresinde bisiklet turu.", "description_en": "Bicycle tour around Alleben Pond.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Bisiklet kiralama noktası giriştedir.", "tips_en": "Bicycle rental point is at the entrance."},
    {"name": "Yürüyüş Parkuru", "name_en": "Walking Trail", "area": "Dülükbaba", "category": "Doğa", "tags": ["yürüyüş", "doğa", "orman"], "distanceFromCenter": 8.0, "lat": 37.1100, "lng": 37.3400, "price": "free", "rating": 4.5, "description": "Orman içinde işaretlenmiş yürüyüş parkuru.", "description_en": "Marked walking trail in the forest.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Rahat ayakkabı ve su şart.", "tips_en": "Comfortable shoes and water are a must."}
]

# BATCH 22: ADDITIONAL UNIQUE PLACES
batch_22 = [
    {"name": "Fotoğraf Müzesi", "name_en": "Photography Museum", "area": "Şahinbey", "category": "Müze", "tags": ["fotoğraf", "tarih", "sanat"], "distanceFromCenter": 0.4, "lat": 37.0625, "lng": 37.3815, "price": "low", "rating": 4.3, "description": "Eski Antep fotoğraflarından oluşan sergi.", "description_en": "Exhibition of old Antep photographs.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Şehrin nasıl değiştiğini görmek ilginç.", "tips_en": "Interesting to see how the city has changed."},
    {"name": "Minyatür Müzesi", "name_en": "Miniature Museum", "area": "Şahinbey", "category": "Müze", "tags": ["minyatür", "model", "sanat"], "distanceFromCenter": 0.5, "lat": 37.0630, "lng": 37.3820, "price": "low", "rating": 4.4, "description": "Tarihi yapıların minyatür modelleri.", "description_en": "Miniature models of historical buildings.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Çocuklar çok seviyor.", "tips_en": "Children love it."},
    {"name": "Seramik Atölyesi", "name_en": "Ceramics Workshop", "area": "Şahinbey", "category": "Deneyim", "tags": ["seramik", "çömlek", "sanat"], "distanceFromCenter": 0.4, "lat": 37.0622, "lng": 37.3818, "price": "medium", "rating": 4.4, "description": "Kendi seramik eşyanızı yapın.", "description_en": "Make your own ceramic item.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Eser kuruduktan sonra posta ile gönderilir.", "tips_en": "Item is mailed after drying."},
    {"name": "Ahşap Oymacılık", "name_en": "Wood Carving", "area": "Şahinbey", "category": "Alışveriş", "tags": ["ahşap", "oyma", "el sanatı"], "distanceFromCenter": 0.3, "lat": 37.0628, "lng": 37.3822, "price": "medium", "rating": 4.5, "description": "El yapımı ahşap oyma ürünleri.", "description_en": "Handmade wood carving products.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Özel sipariş de verilebilir.", "tips_en": "Custom orders can also be placed."},
    {"name": "Çarşı Rehberli Tur", "name_en": "Bazaar Guided Tour", "area": "Şahinbey", "category": "Deneyim", "tags": ["tur", "rehber", "çarşı"], "distanceFromCenter": 0.0, "lat": 37.0630, "lng": 37.3825, "price": "medium", "rating": 4.7, "description": "Uzman rehber eşliğinde çarşı gezisi.", "description_en": "Bazaar tour with expert guide.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Sabah daha az kalabalık.", "tips_en": "Less crowded in the morning."},
    {"name": "Gastronomi Turu", "name_en": "Gastronomy Tour", "area": "Merkez", "category": "Deneyim", "tags": ["yemek", "tur", "tadım"], "distanceFromCenter": 0.0, "lat": 37.0662, "lng": 37.3833, "price": "high", "rating": 4.9, "description": "UNESCO gastronomi şehrinin lezzetlerini keşfedin.", "description_en": "Discover the flavors of UNESCO gastronomy city.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Çok aç gidin, çok fazla tadım var.", "tips_en": "Go very hungry, there are many tastings."},
    {"name": "Güneş Battı Bar", "name_en": "Sunset Bar", "area": "Şehitkamil", "category": "Bar", "tags": ["bar", "günbatımı", "kokteyl"], "distanceFromCenter": 2.5, "lat": 37.0780, "lng": 37.3680, "price": "high", "rating": 4.5, "description": "Gün batımı manzaralı bar.", "description_en": "Bar with sunset view.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "17:00-19:00 arası en iyi saatler.", "tips_en": "Best hours between 17:00-19:00."},
    {"name": "Gece Pazarı", "name_en": "Night Market", "area": "Şehitkamil", "category": "Alışveriş", "tags": ["pazar", "gece", "sokak"], "distanceFromCenter": 1.5, "lat": 37.0720, "lng": 37.3750, "price": "low", "rating": 4.2, "description": "Akşamları kurulan sokak pazarı.", "description_en": "Street market set up in evenings.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Yaz aylarında daha canlı.", "tips_en": "More lively in summer months."}
]

def enrich():
    filepath = 'assets/cities/gaziantep.json'
    all_new = batch_19 + batch_20 + batch_21 + batch_22
    
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
