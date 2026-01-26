import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Antalya", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:50000@36.8841,30.7056"
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

# BATCH 9: Alanya Bölgesi
batch_9 = [
    {"name": "Alanya Kalesi", "name_en": "Alanya Castle", "area": "Alanya", "category": "Tarihi", "tags": ["kale", "manzara", "tarihi"], "distanceFromCenter": 130.0, "lat": 36.5340, "lng": 32.0000, "price": "low", "rating": 4.8, "description": "Yarımada tepesinde muhteşem manzaralı Selçuklu kalesi.", "description_en": "Seljuk castle with magnificent view on peninsula top.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "Teleferik ile çıkabilirsiniz.", "tips_en": "You can take cable car."},
    {"name": "Kızıl Kule", "name_en": "Red Tower", "area": "Alanya", "category": "Tarihi", "tags": ["kule", "selçuklu", "müze"], "distanceFromCenter": 130.0, "lat": 36.5420, "lng": 31.9970, "price": "low", "rating": 4.7, "description": "Alanya'nın simgesi, sekizgen Selçuklu kulesi.", "description_en": "Symbol of Alanya, octagonal Seljuk tower.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "İçinde etnografya müzesi var.", "tips_en": "Ethnography museum inside."},
    {"name": "Tophane (Tersane)", "name_en": "Tophane Shipyard", "area": "Alanya", "category": "Tarihi", "tags": ["tersane", "deniz", "selçuklu"], "distanceFromCenter": 130.0, "lat": 36.5400, "lng": 31.9960, "price": "low", "rating": 4.5, "description": "Selçuklu dönemi deniz tersanesi, kemerli yapı.", "description_en": "Seljuk period naval shipyard, arched structure.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Kızıl Kule ile birlikte gezin.", "tips_en": "Visit with Red Tower."},
    {"name": "Damlataş Mağarası", "name_en": "Damlatash Cave", "area": "Alanya", "category": "Doğa", "tags": ["mağara", "sarkıt", "şifa"], "distanceFromCenter": 130.0, "lat": 36.5440, "lng": 31.9880, "price": "low", "rating": 4.4, "description": "15.000 yıllık sarkıt/dikitler, astım için şifa.", "description_en": "15,000-year-old stalactites, healing for asthma.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "İçi serin, hafif ceket alın.", "tips_en": "Cool inside, bring light jacket."},
    {"name": "Alanya Teleferik", "name_en": "Alanya Cable Car", "area": "Alanya", "category": "Deneyim", "tags": ["teleferik", "manzara", "kale"], "distanceFromCenter": 130.0, "lat": 36.5380, "lng": 31.9920, "price": "medium", "rating": 4.6, "description": "Plajdan kaleye teleferik, muhteşem manzara.", "description_en": "Cable car from beach to castle, stunning view.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "İniş yürüyerek daha keyifli.", "tips_en": "Walking down is more enjoyable."},
    {"name": "Alanya Limanı", "name_en": "Alanya Harbor", "area": "Alanya", "category": "Manzara", "tags": ["liman", "tekne", "gece"], "distanceFromCenter": 130.0, "lat": 36.5430, "lng": 31.9940, "price": "free", "rating": 4.5, "description": "Tekne turları, restoranlar ve gece hayatı.", "description_en": "Boat tours, restaurants and nightlife.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Akşam yürüyüşü için ideal.", "tips_en": "Ideal for evening walk."},
    {"name": "İncekum Plajı", "name_en": "Incekum Beach", "area": "Alanya", "category": "Plaj", "tags": ["plaj", "ince kum", "doğal"], "distanceFromCenter": 110.0, "lat": 36.6100, "lng": 31.8500, "price": "low", "rating": 4.6, "description": "İnce kumlu, sığ ve sakin aile plajı.", "description_en": "Fine sand, shallow and calm family beach.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Çocuklu aileler için ideal.", "tips_en": "Ideal for families with children."}
]

# BATCH 10: Kemer Bölgesi  
batch_10 = [
    {"name": "Kemer Marina", "name_en": "Kemer Marina", "area": "Kemer", "category": "Manzara", "tags": ["marina", "yat", "lüks"], "distanceFromCenter": 45.0, "lat": 36.5980, "lng": 30.5610, "price": "free", "rating": 4.5, "description": "Lüks yat limanı, restoranlar ve gece hayatı.", "description_en": "Luxury yacht marina, restaurants and nightlife.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Akşam yemeği için güzel mekanlar.", "tips_en": "Nice places for dinner."},
    {"name": "Moonlight Beach Kemer", "name_en": "Moonlight Beach Kemer", "area": "Kemer", "category": "Plaj", "tags": ["plaj", "eğlence", "merkez"], "distanceFromCenter": 45.0, "lat": 36.5960, "lng": 30.5580, "price": "low", "rating": 4.4, "description": "Kemer'in en popüler merkezi plajı.", "description_en": "Kemer's most popular central beach.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Park altında plaj.", "tips_en": "Beach under park."},
    {"name": "Tahtalı Dağı Teleferik", "name_en": "Tahtali Mountain Cable Car", "area": "Kemer", "category": "Deneyim", "tags": ["teleferik", "dağ", "manzara"], "distanceFromCenter": 65.0, "lat": 36.5360, "lng": 30.4650, "price": "high", "rating": 4.8, "description": "2365 metreye, Akdeniz ve dağ manzarası.", "description_en": "To 2365 meters, Mediterranean and mountain view.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "Zirvede çok soğuk, mont alın.", "tips_en": "Very cold at summit, bring coat."},
    {"name": "Göynük Kanyonu", "name_en": "Goynuk Canyon", "area": "Kemer", "category": "Doğa", "tags": ["kanyon", "yürüyüş", "şelale"], "distanceFromCenter": 40.0, "lat": 36.6850, "lng": 30.5400, "price": "low", "rating": 4.6, "description": "Yürüyüş parkuru, şelaleler ve doğal havuzlar.", "description_en": "Hiking trail, waterfalls and natural pools.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Su ayakkabısı ile gidin.", "tips_en": "Go with water shoes."},
    {"name": "Beldibi Mağarası", "name_en": "Beldibi Cave", "area": "Kemer", "category": "Tarihi", "tags": ["mağara", "tarih öncesi", "arkeoloji"], "distanceFromCenter": 30.0, "lat": 36.7120, "lng": 30.5680, "price": "free", "rating": 4.2, "description": "Paleolitik dönem yaşam izleri taşıyan mağara.", "description_en": "Cave with Paleolithic period life traces.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Yoldan biraz yürümek gerekiyor.", "tips_en": "Need to walk a bit from road."}
]

# BATCH 11: Kaş Bölgesi
batch_11 = [
    {"name": "Kaş Merkez", "name_en": "Kas Center", "area": "Kaş", "category": "Manzara", "tags": ["sahil kasabası", "butik", "romantik"], "distanceFromCenter": 180.0, "lat": 36.2000, "lng": 29.6380, "price": "free", "rating": 4.8, "description": "Şirin Akdeniz sahil kasabası, butik oteller.", "description_en": "Charming Mediterranean coastal town, boutique hotels.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "Gün batımı için meydana gidin.", "tips_en": "Go to square for sunset."},
    {"name": "Antiphellos Antik Tiyatrosu", "name_en": "Antiphellos Ancient Theater", "area": "Kaş", "category": "Tarihi", "tags": ["antik", "tiyatro", "deniz manzarası"], "distanceFromCenter": 180.0, "lat": 36.2010, "lng": 29.6350, "price": "free", "rating": 4.6, "description": "Deniz manzaralı Helenistik dönem tiyatrosu.", "description_en": "Hellenistic period theater with sea view.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "Gün batımında muhteşem.", "tips_en": "Magnificent at sunset."},
    {"name": "Kaya Mezarları Kaş", "name_en": "Rock Tombs Kas", "area": "Kaş", "category": "Tarihi", "tags": ["kaya mezarı", "likya", "tarihi"], "distanceFromCenter": 180.0, "lat": 36.1990, "lng": 29.6400, "price": "free", "rating": 4.5, "description": "Şehir merkezindeki etkileyici Likya kaya mezarları.", "description_en": "Impressive Lycian rock tombs in city center.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Ücretsiz, her an gezilebilir.", "tips_en": "Free, can visit anytime."},
    {"name": "Big Pebble Beach Kaş", "name_en": "Big Pebble Beach Kas", "area": "Kaş", "category": "Plaj", "tags": ["plaj", "şnorkel", "dalış"], "distanceFromCenter": 180.0, "lat": 36.1970, "lng": 29.6320, "price": "free", "rating": 4.5, "description": "Şnorkel ve dalış için kristal berrak sular.", "description_en": "Crystal clear waters for snorkeling and diving.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Şnorkel ekipmanı kiralayın.", "tips_en": "Rent snorkeling equipment."},
    {"name": "Meis Adası Günlük Tur", "name_en": "Kastellorizo Day Trip", "area": "Kaş", "category": "Deneyim", "tags": ["ada", "yunanistan", "günlük tur"], "distanceFromCenter": 185.0, "lat": 36.1500, "lng": 29.5900, "price": "high", "rating": 4.7, "description": "Kaş'tan 20 dakikada Yunan adası Meis.", "description_en": "Greek island Meis 20 minutes from Kas.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Pasaport gerekli.", "tips_en": "Passport required."},
    {"name": "Limanagzi Koyu", "name_en": "Limanagzi Bay", "area": "Kaş", "category": "Plaj", "tags": ["koy", "tekne", "yüzme"], "distanceFromCenter": 182.0, "lat": 36.1850, "lng": 29.6250, "price": "low", "rating": 4.6, "description": "Tekne ile veya yürüyerek ulaşılan saklı koy.", "description_en": "Hidden bay reached by boat or walking.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Tekne turu ile gidin.", "tips_en": "Go with boat tour."}
]

# BATCH 12: Daha Fazla Restoran & Kafe
batch_12 = [
    {"name": "Tuvana Hotel Restaurant", "name_en": "Tuvana Hotel Restaurant", "area": "Kaleiçi", "category": "Restoran", "tags": ["fine dining", "tarihi", "bahçe"], "distanceFromCenter": 0.2, "lat": 36.8845, "lng": 30.7060, "price": "high", "rating": 4.7, "description": "Tarihi konakta bahçe ortamında fine dining.", "description_en": "Fine dining in garden setting of historic mansion.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Romantik bir akşam yemeği için ideal.", "tips_en": "Ideal for romantic dinner."},
    {"name": "Hasanağa Restaurant", "name_en": "Hasanaga Restaurant", "area": "Muratpaşa", "category": "Restoran", "tags": ["türk mutfağı", "deniz ürünleri", "lüks"], "distanceFromCenter": 3.0, "lat": 36.8750, "lng": 30.7350, "price": "high", "rating": 4.6, "description": "Deniz ürünleri ve Türk mutfağı.", "description_en": "Seafood and Turkish cuisine.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Meze çeşitleri çok zengin.", "tips_en": "Meze varieties are very rich."},
    {"name": "Arma Restaurant", "name_en": "Arma Restaurant", "area": "Kaleiçi", "category": "Restoran", "tags": ["deniz ürünleri", "manzara", "tarihi"], "distanceFromCenter": 0.3, "lat": 36.8815, "lng": 30.7030, "price": "high", "rating": 4.5, "description": "Tarihi depo binasında deniz ürünleri.", "description_en": "Seafood in historic warehouse building.", "bestTime": "Gün batımı", "bestTime_en": "Sunset", "tips": "Teras manzarası muhteşem.", "tips_en": "Terrace view is magnificent."},
    {"name": "Club Arma", "name_en": "Club Arma", "area": "Kaleiçi", "category": "Bar", "tags": ["bara", "gece hayatı", "manzara"], "distanceFromCenter": 0.3, "lat": 36.8812, "lng": 30.7028, "price": "high", "rating": 4.4, "description": "Marina manzarası eşliğinde gece eğlencesi.", "description_en": "Night entertainment with marina view.", "bestTime": "Gece", "bestTime_en": "Night", "tips": "Hafta sonu DJ performansları.", "tips_en": "DJ performances on weekends."},
    {"name": "Deniz Lokantası", "name_en": "Deniz Lokantasi", "area": "Kemer", "category": "Restoran", "tags": ["balık", "deniz ürünleri", "yerel"], "distanceFromCenter": 45.0, "lat": 36.5985, "lng": 30.5620, "price": "medium", "rating": 4.5, "description": "Kemer'de taze balık ve deniz ürünleri.", "description_en": "Fresh fish and seafood in Kemer.", "bestTime": "Akşam", "bestTime_en": "Evening", "tips": "Günlük balığı sorun.", "tips_en": "Ask for daily fish."},
    {"name": "Simena View Restaurant", "name_en": "Simena View Restaurant", "area": "Demre", "category": "Restoran", "tags": ["manzara", "deniz ürünleri", "köy"], "distanceFromCenter": 160.0, "lat": 36.1975, "lng": 29.8555, "price": "medium", "rating": 4.6, "description": "Kaleköy'de deniz manzaralı yemek.", "description_en": "Dining with sea view in Kalekoy.", "bestTime": "Öğle", "bestTime_en": "Lunch", "tips": "Tekne turunda öğle molası için ideal.", "tips_en": "Ideal for lunch break on boat tour."}
]

# BATCH 13: Ek Deneyimler & Turlar
batch_13 = [
    {"name": "Antalya Aquarium", "name_en": "Antalya Aquarium", "area": "Konyaaltı", "category": "Deneyim", "tags": ["akvaryum", "aile", "eğlence"], "distanceFromCenter": 3.5, "lat": 36.8700, "lng": 30.6480, "price": "high", "rating": 4.5, "description": "Dünyanın en büyük tünel akvaryumlarından.", "description_en": "One of the world's largest tunnel aquariums.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Köpekbalığı dalışı yapılabilir.", "tips_en": "Shark diving available."},
    {"name": "Mini City Antalya", "name_en": "Mini City Antalya", "area": "Konyaaltı", "category": "Deneyim", "tags": ["minyatür", "çocuk", "eğitim"], "distanceFromCenter": 3.5, "lat": 36.8695, "lng": 30.6475, "price": "medium", "rating": 4.3, "description": "Türkiye'nin minyatür tarihi yapıları.", "description_en": "Miniature historical structures of Turkey.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Çocuklar için eğitici.", "tips_en": "Educational for children."},
    {"name": "Sandland Kum Heykeller", "name_en": "Sandland Sand Sculptures", "area": "Lara", "category": "Deneyim", "tags": ["kum heykel", "sanat", "sergi"], "distanceFromCenter": 10.0, "lat": 36.8530, "lng": 30.8050, "price": "medium", "rating": 4.4, "description": "Dev kum heykeller açık hava sergisi.", "description_en": "Giant sand sculptures open air exhibition.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Fotoğraf için harika.", "tips_en": "Great for photos."},
    {"name": "Perge Bisiklet Turu", "name_en": "Perge Bicycle Tour", "area": "Aksu", "category": "Deneyim", "tags": ["bisiklet", "antik kent", "tur"], "distanceFromCenter": 18.0, "lat": 36.9580, "lng": 30.8530, "price": "medium", "rating": 4.5, "description": "Bisikletle antik kenti keşif.", "description_en": "Exploring ancient city by bicycle.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Sabah serin saatlerde.", "tips_en": "Cool morning hours."},
    {"name": "Kekova Kayak Turu", "name_en": "Kekova Kayak Tour", "area": "Demre", "category": "Deneyim", "tags": ["kayak", "batık şehir", "macera"], "distanceFromCenter": 160.0, "lat": 36.1880, "lng": 29.8660, "price": "medium", "rating": 4.8, "description": "Batık şehir üzerinde kayakla gezinti.", "description_en": "Kayaking over submerged city.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Cam tabanlı kayak daha iyi.", "tips_en": "Glass bottom kayak is better."},
    {"name": "Likya Yolu Yürüyüşü", "name_en": "Lycian Way Hiking", "area": "Kaş", "category": "Deneyim", "tags": ["yürüyüş", "likya", "doğa"], "distanceFromCenter": 180.0, "lat": 36.2500, "lng": 29.5000, "price": "free", "rating": 4.9, "description": "Dünyanın en güzel 10 yürüyüş rotasından.", "description_en": "One of world's 10 most beautiful hiking routes.", "bestTime": "İlkbahar", "bestTime_en": "Spring", "tips": "Etaplara bölünebilir.", "tips_en": "Can be divided into stages."}
]

# BATCH 14: Ek Alışveriş & Pazar
batch_14 = [
    {"name": "Migros AVM", "name_en": "Migros Mall", "area": "Konyaaltı", "category": "Alışveriş", "tags": ["avm", "süpermarket", "alışveriş"], "distanceFromCenter": 2.0, "lat": 36.8730, "lng": 30.6680, "price": "variable", "rating": 4.2, "description": "Merkezi alışveriş merkezi.", "description_en": "Central shopping center.", "bestTime": "Gündüz", "bestTime_en": "Daytime", "tips": "Sinema ve yeme-içme alanları.", "tips_en": "Cinema and dining areas."},
    {"name": "Antalya Organic Market", "name_en": "Antalya Organic Market", "area": "Muratpaşa", "category": "Alışveriş", "tags": ["organik", "yerel", "pazar"], "distanceFromCenter": 2.5, "lat": 36.8820, "lng": 30.7250, "price": "medium", "rating": 4.5, "description": "Organik ürünler ve yerel üreticiler.", "description_en": "Organic products and local producers.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Cumartesi günleri.", "tips_en": "On Saturdays."},
    {"name": "Alanya Cuma Pazarı", "name_en": "Alanya Friday Market", "area": "Alanya", "category": "Alışveriş", "tags": ["pazar", "tekstil", "yerel"], "distanceFromCenter": 130.0, "lat": 36.5500, "lng": 32.0100, "price": "low", "rating": 4.4, "description": "Dev açık hava pazarı, tekstil ağırlıklı.", "description_en": "Giant open air market, textile focused.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Cuma günleri, çok kalabalık.", "tips_en": "Fridays, very crowded."},
    {"name": "Kaş Cuma Pazarı", "name_en": "Kas Friday Market", "area": "Kaş", "category": "Alışveriş", "tags": ["pazar", "butik", "el yapımı"], "distanceFromCenter": 180.0, "lat": 36.2020, "lng": 29.6410, "price": "medium", "rating": 4.5, "description": "El yapımı ürünler ve yerel lezzetler.", "description_en": "Handmade products and local delicacies.", "bestTime": "Sabah", "bestTime_en": "Morning", "tips": "Lavanta ve zeytinyağı sabunu alın.", "tips_en": "Buy lavender and olive oil soap."},
    {"name": "Konyaaltı Antika Pazarı", "name_en": "Konyaalti Antique Market", "area": "Konyaaltı", "category": "Alışveriş", "tags": ["antika", "koleksiyon", "eski"], "distanceFromCenter": 2.5, "lat": 36.8680, "lng": 30.6520, "price": "variable", "rating": 4.3, "description": "Antika meraklıları için pazar.", "description_en": "Market for antique enthusiasts.", "bestTime": "Hafta sonu", "bestTime_en": "Weekend", "tips": "Pazarlık şart.", "tips_en": "Bargaining required."}
]

def enrich():
    filepath = 'assets/cities/antalya.json'
    all_new = batch_9 + batch_10 + batch_11 + batch_12 + batch_13 + batch_14
    
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
        place['id'] = place['name'].lower().replace(' ', '-').replace('ç', 'c').replace('ğ', 'g').replace('ı', 'i').replace('ö', 'o').replace('ş', 's').replace('ü', 'u').replace('(', '').replace(')', '').replace('&', 'and')
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
