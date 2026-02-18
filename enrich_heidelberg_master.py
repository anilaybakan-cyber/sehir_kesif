#!/usr/bin/env python3
"""
Heidelberg Enrichment Script with Firebase Storage Upload
- Fetches photos from Google Places API
- Downloads and uploads to Firebase Storage
- Creates comprehensive highlight data
"""

import json
import requests
import time
import urllib.parse
import os
from google.cloud import storage

# Configuration
API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'
FIREBASE_BUCKET = 'myway-3fe75.firebasestorage.app'
CITY_NAME = 'heidelberg'
CITY_COORDS = {'lat': 49.4093, 'lng': 8.6943}

def get_google_photo_url(place_name, city_name="Heidelberg Germany"):
    """Fetches a photo URL from Google Places API"""
    queries = [f"{place_name} {city_name}", place_name]
    for query in queries:
        try:
            find_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:15000@{CITY_COORDS['lat']},{CITY_COORDS['lng']}"
            response = requests.get(find_url)
            data = response.json()
            if data['status'] == 'OK' and data['candidates']:
                if 'photos' in data['candidates'][0]:
                    ref = data['candidates'][0]['photos'][0]['photo_reference']
                    photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={ref}&key={API_KEY}"
                    print(f"  ✓ Found: {place_name}")
                    return photo_url
        except Exception as e:
            continue
    print(f"  ✗ Not found: {place_name}")
    return None

def download_and_upload_to_firebase(photo_url, place_id):
    """Downloads photo and uploads to Firebase Storage"""
    try:
        # Download the image
        response = requests.get(photo_url, stream=True, allow_redirects=True)
        if response.status_code == 200:
            # Save locally first
            local_path = f"/tmp/{place_id}.jpg"
            with open(local_path, 'wb') as f:
                f.write(response.content)
            
            # Upload to Firebase Storage
            storage_client = storage.Client()
            bucket = storage_client.bucket(FIREBASE_BUCKET)
            blob = bucket.blob(f"cities/{CITY_NAME}/{place_id}.jpg")
            blob.upload_from_filename(local_path)
            blob.make_public()
            
            # Return Firebase URL
            firebase_url = f"https://storage.googleapis.com/{FIREBASE_BUCKET}/cities/{CITY_NAME}/{place_id}.jpg"
            print(f"    ↑ Uploaded to Firebase: {place_id}")
            os.remove(local_path)
            return firebase_url
    except Exception as e:
        print(f"    ✗ Upload failed: {e}")
    return None

# =============================================================================
# HEIDELBERG DATA - Based on blog research
# Sources: Journavel, Gezimanya, Avrupa Rüyası, GetYourGuide, TripAdvisor
# =============================================================================

# BATCH 1: Ana Turistik Yerler
batch_1 = [
    {
        "name": "Heidelberg Kalesi (Schloss)",
        "name_en": "Heidelberg Castle",
        "area": "Schloss",
        "category": "Tarihi",
        "tags": ["kale", "rönesans", "panorama", "ikonik"],
        "distanceFromCenter": 0.5,
        "lat": 49.4107,
        "lng": 8.7153,
        "price": "medium",
        "rating": 4.9,
        "description": "Almanya'nın en romantik kalesi. Rönesans ve Gotik mimari öğeleri taşıyan, 16-17. yüzyıldan kalma muhteşem harabe. İçinde dünyanın en büyük şarap fıçısı (Heidelberg Tun - 220.000 litre) ve Alman Eczacılık Müzesi bulunur.",
        "description_en": "Germany's most romantic castle. Magnificent ruins from the 16-17th century with Renaissance and Gothic architecture. Contains the world's largest wine barrel and German Pharmacy Museum.",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Füniküler (Bergbahn) ile çıkın, muhteşem manzara. Akşam ışıklandırması efsanevi.",
        "tips_en": "Take the funicular (Bergbahn), amazing view. Evening illumination is legendary."
    },
    {
        "name": "Alte Brücke (Karl Theodor Köprüsü)",
        "name_en": "Old Bridge",
        "area": "Altstadt",
        "category": "Tarihi",
        "tags": ["köprü", "nehir", "ikonik", "fotoğraf"],
        "distanceFromCenter": 0.3,
        "lat": 49.4118,
        "lng": 8.7101,
        "price": "free",
        "rating": 4.8,
        "description": "1788'de inşa edilen tarihi taş köprü, Neckar Nehri üzerinde. Köprü maymunu heykeli (Brückenaffe) meşhur fotoğraf noktası. Kale manzarası eşsiz.",
        "description_en": "Historic stone bridge built in 1788 over the Neckar River. The bridge monkey statue is a famous photo spot. Castle view is unmatched.",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Maymun heykelinin elini tutup dilek dileyin - yerel gelenek!",
        "tips_en": "Touch the monkey statue's hand and make a wish - local tradition!"
    },
    {
        "name": "Philosophenweg (Filozoflar Yolu)",
        "name_en": "Philosophers' Walk",
        "area": "Neuenheim",
        "category": "Yürüyüş",
        "tags": ["yürüyüş", "manzara", "romantik", "doğa"],
        "distanceFromCenter": 0.8,
        "lat": 49.4158,
        "lng": 8.7016,
        "price": "free",
        "rating": 4.9,
        "description": "Neckar Nehri'nin karşı yakasında, Heiligenberg yamacındaki efsanevi yürüyüş yolu. Hegel, Goethe gibi filozofların düşünerek yürüdüğü söylenir. Kale ve eski şehir panoraması.",
        "description_en": "Legendary walking path on the Heiligenberg slope across the Neckar. Said to be walked by philosophers like Hegel and Goethe. Castle and old town panorama.",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Gün batımında gidin, Heidelberg'in en güzel manzarası burada.",
        "tips_en": "Go at sunset, the most beautiful view of Heidelberg is here."
    },
    {
        "name": "Altstadt (Eski Şehir)",
        "name_en": "Old Town",
        "area": "Merkez",
        "category": "Deneyim",
        "tags": ["tarihi", "yürüyüş", "alışveriş", "mimari"],
        "distanceFromCenter": 0.0,
        "lat": 49.4094,
        "lng": 8.7063,
        "price": "free",
        "rating": 4.8,
        "description": "II. Dünya Savaşı'nda bombalanmayan nadir Alman şehirlerinden biri. Barok binalar, dar sokaklar, kafeler ve butiklerle dolu. Avrupa'nın en uzun yaya caddesine (Hauptstraße) ev sahipliği yapar.",
        "description_en": "One of the few German cities not bombed in WWII. Full of Baroque buildings, narrow streets, cafes and boutiques. Home to Europe's longest pedestrian street.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kaybolun bu sokaklarda, her köşede sürpriz keşfedeceksiniz.",
        "tips_en": "Get lost in these streets, you'll discover surprises at every corner."
    },
    {
        "name": "Heiliggeistkirche (Kutsal Ruh Kilisesi)",
        "name_en": "Church of the Holy Spirit",
        "area": "Marktplatz",
        "category": "Tarihi",
        "tags": ["kilise", "gotik", "meydan", "mimari"],
        "distanceFromCenter": 0.1,
        "lat": 49.4096,
        "lng": 8.7099,
        "price": "free",
        "rating": 4.6,
        "description": "1398-1544 yılları arasında inşa edilen Gotik kilise, Marktplatz'ın merkezinde. Kuleye çıkarak şehrin panoramik manzarasını görebilirsiniz.",
        "description_en": "Gothic church built between 1398-1544, in the center of Marktplatz. Climb the tower for a panoramic city view.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kuleye çıkış 2€, muhteşem manzara için değer.",
        "tips_en": "Tower climb is 2€, worth it for the stunning view."
    },
    {
        "name": "Heidelberg Üniversitesi",
        "name_en": "Heidelberg University",
        "area": "Altstadt",
        "category": "Tarihi",
        "tags": ["üniversite", "tarihi", "akademik", "mimari"],
        "distanceFromCenter": 0.2,
        "lat": 49.4095,
        "lng": 8.7067,
        "price": "low",
        "rating": 4.7,
        "description": "1386'da kurulan Almanya'nın en eski üniversitesi. Nobel ödüllü 56 bilim insanı yetiştirmiş. Eski kampüs binaları ve Üniversite Müzesi görülmeye değer.",
        "description_en": "Germany's oldest university founded in 1386. Produced 56 Nobel laureates. Old campus buildings and University Museum worth visiting.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Öğrenci hapishanesini (Studentenkarzer) mutlaka ziyaret edin!",
        "tips_en": "Must visit the Student Prison (Studentenkarzer)!"
    }
]

# BATCH 2: Müzeler & Kültür
batch_2 = [
    {
        "name": "Studentenkarzer (Öğrenci Hapishanesi)",
        "name_en": "Student Prison",
        "area": "Altstadt",
        "category": "Müze",
        "tags": ["müze", "üniversite", "tarihi", "ilginç"],
        "distanceFromCenter": 0.2,
        "lat": 49.4098,
        "lng": 8.7075,
        "price": "low",
        "rating": 4.7,
        "description": "1778-1914 yılları arasında yaramaz öğrencilerin hapsedildiği üniversite hapishanesi. Duvarlar öğrencilerin grafitileri ve karikatürleriyle kaplı.",
        "description_en": "University prison where naughty students were jailed from 1778-1914. Walls covered with students' graffiti and caricatures.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Duvar yazıları yüzyılın öğrenci mizahını yansıtıyor.",
        "tips_en": "Wall writings reflect a century of student humor."
    },
    {
        "name": "Kurpfälzisches Museum",
        "name_en": "Palatinate Museum",
        "area": "Altstadt",
        "category": "Müze",
        "tags": ["müze", "sanat", "tarih", "arkeoloji"],
        "distanceFromCenter": 0.2,
        "lat": 49.4105,
        "lng": 8.7080,
        "price": "medium",
        "rating": 4.5,
        "description": "Palatinate bölgesinin sanat ve tarih müzesi. Riemenschneider'in orijinal Windsheim altar eseri ve arkeolojik koleksiyonlar.",
        "description_en": "Art and history museum of the Palatinate region. Original Windsheim altar by Riemenschneider and archaeological collections.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Pazar günleri giriş ücretsiz.",
        "tips_en": "Free entry on Sundays."
    },
    {
        "name": "Alman Eczacılık Müzesi",
        "name_en": "German Pharmacy Museum",
        "area": "Schloss",
        "category": "Müze",
        "tags": ["müze", "eczacılık", "bilim", "kale"],
        "distanceFromCenter": 0.5,
        "lat": 49.4108,
        "lng": 8.7155,
        "price": "medium",
        "rating": 4.4,
        "description": "Kale içinde bulunan, 18-19. yüzyıl eczacılık tarihini anlatan ilginç müze. Antik ilaçlar, laboratuvar ekipmanları.",
        "description_en": "Interesting museum inside the castle depicting 18-19th century pharmacy history. Ancient medicines, lab equipment.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kale biletine dahil, ekstra ücret yok.",
        "tips_en": "Included in castle ticket, no extra charge."
    },
    {
        "name": "Carl Bosch Müzesi",
        "name_en": "Carl Bosch Museum",
        "area": "Weststadt",
        "category": "Müze",
        "tags": ["müze", "bilim", "nobel", "kimya"],
        "distanceFromCenter": 1.5,
        "lat": 49.4040,
        "lng": 8.6860,
        "price": "medium",
        "rating": 4.3,
        "description": "Nobel ödüllü kimyager Carl Bosch'un yaşamı ve çalışmalarını sergileyen müze.",
        "description_en": "Museum showcasing the life and work of Nobel Prize-winning chemist Carl Bosch.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Bilim meraklıları için ilginç.",
        "tips_en": "Interesting for science enthusiasts."
    },
    {
        "name": "Heidelberg Hayvanat Bahçesi",
        "name_en": "Heidelberg Zoo",
        "area": "Neuenheim",
        "category": "Deneyim",
        "tags": ["hayvanat bahçesi", "aile", "çocuk", "doğa"],
        "distanceFromCenter": 1.2,
        "lat": 49.4175,
        "lng": 8.6905,
        "price": "medium",
        "rating": 4.4,
        "description": "2000'den fazla hayvan türü barındıran, çocuklu aileler için ideal hayvanat bahçesi.",
        "description_en": "Zoo housing over 2000 animal species, ideal for families with children.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Hafta içi daha az kalabalık.",
        "tips_en": "Less crowded on weekdays."
    }
]

# BATCH 3: Manzara Noktaları & Doğa
batch_3 = [
    {
        "name": "Königstuhl",
        "name_en": "King's Throne",
        "area": "Schloss",
        "category": "Manzara",
        "tags": ["tepe", "manzara", "teleferik", "orman"],
        "distanceFromCenter": 3.0,
        "lat": 49.3989,
        "lng": 8.7271,
        "price": "medium",
        "rating": 4.7,
        "description": "568 metre yüksekliğinde, Heidelberg'in en yüksek noktası. Füniküler ile ulaşılır. Gözlemevi, doğa parkuru ve şahin gösterisi.",
        "description_en": "568 meters high, Heidelberg's highest point. Accessed by funicular. Observatory, nature trails and falconry show.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Açık havada etrafı 360 derece görebilirsiniz.",
        "tips_en": "In clear weather you can see 360 degrees around."
    },
    {
        "name": "Heidelberger Bergbahn (Füniküler)",
        "name_en": "Heidelberg Funicular",
        "area": "Schloss",
        "category": "Deneyim",
        "tags": ["füniküler", "ulaşım", "manzara", "tarihi"],
        "distanceFromCenter": 0.4,
        "lat": 49.4095,
        "lng": 8.7120,
        "price": "medium",
        "rating": 4.6,
        "description": "1890'dan beri çalışan tarihi füniküler sistemi. Kornmarkt'tan Kale ve ardından Königstuhl'a çıkar.",
        "description_en": "Historic funicular system operating since 1890. Goes from Kornmarkt to Castle and then to Königstuhl.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Gidiş-dönüş bilet alın, daha ekonomik.",
        "tips_en": "Buy round-trip ticket, more economical."
    },
    {
        "name": "Thingstätte",
        "name_en": "Thingstatte Amphitheater",
        "area": "Heiligenberg",
        "category": "Tarihi",
        "tags": ["amfi tiyatro", "nazi", "tarihi", "orman"],
        "distanceFromCenter": 2.5,
        "lat": 49.4235,
        "lng": 8.7020,
        "price": "free",
        "rating": 4.3,
        "description": "Nazi döneminde inşa edilen açık hava amfi tiyatro. Ürkütücü tarih, ama muhteşem lokasyon.",
        "description_en": "Open-air amphitheater built during Nazi era. Creepy history, but stunning location.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Philosophenweg'den yürüyerek ulaşılabilir.",
        "tips_en": "Can be reached by walking from Philosophenweg."
    },
    {
        "name": "Neckarwiese",
        "name_en": "Neckar Meadow",
        "area": "Neuenheim",
        "category": "Park",
        "tags": ["park", "piknik", "nehir", "yerel"],
        "distanceFromCenter": 0.5,
        "lat": 49.4145,
        "lng": 8.6980,
        "price": "free",
        "rating": 4.5,
        "description": "Neckar Nehri kıyısında geniş yeşil alan. Öğrencilerin ve yerellerin buluşma noktası. Piknik için ideal.",
        "description_en": "Large green area by the Neckar River. Meeting point for students and locals. Ideal for picnics.",
        "bestTime": "İkindi",
        "bestTime_en": "Afternoon",
        "tips": "Yaz akşamları barbekü yapan yerellerle dolup taşıyor.",
        "tips_en": "Summer evenings overflowing with locals barbecuing."
    },
    {
        "name": "Schlossgarten (Kale Bahçesi)",
        "name_en": "Castle Garden",
        "area": "Schloss",
        "category": "Park",
        "tags": ["bahçe", "kale", "manzara", "tarihi"],
        "distanceFromCenter": 0.5,
        "lat": 49.4102,
        "lng": 8.7140,
        "price": "free",
        "rating": 4.6,
        "description": "Kalenin teraslarında yayılan tarihi bahçeler. Şehrin en güzel manzara noktalarından biri.",
        "description_en": "Historic gardens spreading on castle terraces. One of the most beautiful viewpoints in the city.",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Gün batımında gelin, kaleye girmeden bile harika manzara.",
        "tips_en": "Come at sunset, great view even without entering the castle."
    }
]

# BATCH 4: Restoranlar & Kafeler
batch_4 = [
    {
        "name": "Zum Roten Ochsen",
        "name_en": "Red Ox Inn",
        "area": "Altstadt",
        "category": "Restoran",
        "tags": ["restoran", "geleneksel", "bira", "öğrenci"],
        "distanceFromCenter": 0.2,
        "lat": 49.4091,
        "lng": 8.7078,
        "price": "medium",
        "rating": 4.5,
        "description": "1703'ten beri faaliyet gösteren tarihi öğrenci meyhanesi. Mark Twain ve Bismarck burada içmiş. Otantik Alman mutfağı.",
        "description_en": "Historic student tavern operating since 1703. Mark Twain and Bismarck drank here. Authentic German cuisine.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Tarihi atmosfer için duvarlardaki isimleri inceleyin.",
        "tips_en": "For historic atmosphere, examine the names on the walls."
    },
    {
        "name": "Zum Seppl",
        "name_en": "Seppl's",
        "area": "Altstadt",
        "category": "Restoran",
        "tags": ["restoran", "geleneksel", "bira", "schnitzel"],
        "distanceFromCenter": 0.2,
        "lat": 49.4088,
        "lng": 8.7075,
        "price": "medium",
        "rating": 4.4,
        "description": "Geleneksel Alman meyhanesi, öğrencilerin favorisi. Bira, schnitzel ve canlı atmosfer.",
        "description_en": "Traditional German tavern, student favorite. Beer, schnitzel and lively atmosphere.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Schnitzel porsiyon büyük, paylaşın.",
        "tips_en": "Schnitzel portion is big, share it."
    },
    {
        "name": "Brauhaus Vetter",
        "name_en": "Vetter's Brewery",
        "area": "Altstadt",
        "category": "Restoran",
        "tags": ["bira fabrikası", "restoran", "yerel bira", "yemek"],
        "distanceFromCenter": 0.1,
        "lat": 49.4100,
        "lng": 8.7095,
        "price": "medium",
        "rating": 4.5,
        "description": "Kendi birasını üreten tarihi bira fabrikası restoran. Vetter 33 birası dünyanın en güçlü biraları arasında.",
        "description_en": "Historic brewery restaurant producing its own beer. Vetter 33 among world's strongest beers.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Vetter 33 birasını deneyin ama dikkat, çok güçlü!",
        "tips_en": "Try Vetter 33 beer but careful, very strong!"
    },
    {
        "name": "Café Knösel",
        "name_en": "Cafe Knosel",
        "area": "Altstadt",
        "category": "Kafe",
        "tags": ["kafe", "tatlı", "geleneksel", "pasta"],
        "distanceFromCenter": 0.3,
        "lat": 49.4105,
        "lng": 8.7060,
        "price": "medium",
        "rating": 4.6,
        "description": "1863'ten beri hizmet veren efsanevi kafe. Heidelberg Öpücüğü (Studentenkuss) çikolatasının icadı burada.",
        "description_en": "Legendary cafe serving since 1863. Heidelberg Kiss (Studentenkuss) chocolate was invented here.",
        "bestTime": "İkindi",
        "bestTime_en": "Afternoon",
        "tips": "Studentenkuss çikolatasını hediyelik alın.",
        "tips_en": "Buy Studentenkuss chocolate as a souvenir."
    },
    {
        "name": "Schnitzelbank",
        "name_en": "Schnitzelbank",
        "area": "Altstadt",
        "category": "Restoran",
        "tags": ["restoran", "schnitzel", "yerel", "ekonomik"],
        "distanceFromCenter": 0.2,
        "lat": 49.4092,
        "lng": 8.7085,
        "price": "low",
        "rating": 4.3,
        "description": "Uygun fiyatlı, büyük porsiyonlu schnitzel için en iyi adres. Öğrencilerin favorisi.",
        "description_en": "Best address for affordable, large portion schnitzel. Student favorite.",
        "bestTime": "Öğle",
        "bestTime_en": "Lunch",
        "tips": "Öğle menüsü çok ekonomik.",
        "tips_en": "Lunch menu is very economical."
    },
    {
        "name": "Essighaus",
        "name_en": "Vinegar House",
        "area": "Altstadt",
        "category": "Restoran",
        "tags": ["fine dining", "gurme", "şarap", "romantik"],
        "distanceFromCenter": 0.2,
        "lat": 49.4098,
        "lng": 8.7070,
        "price": "high",
        "rating": 4.7,
        "description": "Tarihi binada fine dining deneyimi. Özel günler ve romantik akşamlar için ideal.",
        "description_en": "Fine dining experience in historic building. Ideal for special occasions and romantic evenings.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Rezervasyon şart.",
        "tips_en": "Reservation required."
    },
    {
        "name": "Chocolaterie Yilliy",
        "name_en": "Chocolaterie Yilliy",
        "area": "Altstadt",
        "category": "Tatlı",
        "tags": ["çikolata", "tatlı", "el yapımı", "hediyelik"],
        "distanceFromCenter": 0.1,
        "lat": 49.4100,
        "lng": 8.7088,
        "price": "medium",
        "rating": 4.6,
        "description": "El yapımı pralinler ve çikolatalar. Hediyelik için mükemmel.",
        "description_en": "Handmade pralines and chocolates. Perfect for gifts.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Tatma seti alabilirsiniz.",
        "tips_en": "You can get a tasting set."
    }
]

# BATCH 5: Alışveriş & Meydanlar
batch_5 = [
    {
        "name": "Hauptstraße",
        "name_en": "Main Street",
        "area": "Altstadt",
        "category": "Alışveriş",
        "tags": ["caddesi", "alışveriş", "yaya", "mağaza"],
        "distanceFromCenter": 0.0,
        "lat": 49.4095,
        "lng": 8.7050,
        "price": "variable",
        "rating": 4.5,
        "description": "1.6 km uzunluğuyla Avrupa'nın en uzun yaya caddelerinden biri. Butikler, kafeler, restoranlar sıralanır.",
        "description_en": "At 1.6 km, one of Europe's longest pedestrian streets. Lined with boutiques, cafes, restaurants.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Baştan sona yürümek en az 1 saat alır.",
        "tips_en": "Walking end to end takes at least 1 hour."
    },
    {
        "name": "Marktplatz (Pazar Meydanı)",
        "name_en": "Market Square",
        "area": "Altstadt",
        "category": "Meydan",
        "tags": ["meydan", "pazar", "herkül", "kilise"],
        "distanceFromCenter": 0.1,
        "lat": 49.4096,
        "lng": 8.7095,
        "price": "free",
        "rating": 4.6,
        "description": "Eski şehrin kalbi. Ortasındaki Herkül çeşmesi ve çevresindeki Heiliggeistkirche dikkat çeker. Çarşamba ve Cumartesi pazarı.",
        "description_en": "Heart of the old town. Hercules fountain in center and surrounding Heiliggeistkirche. Market on Wed and Sat.",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Cumartesi sabahı yerel pazarı deneyimleyin.",
        "tips_en": "Experience local market on Saturday morning."
    },
    {
        "name": "Kornmarkt",
        "name_en": "Corn Market",
        "area": "Altstadt",
        "category": "Meydan",
        "tags": ["meydan", "manzara", "kale", "füniküler"],
        "distanceFromCenter": 0.2,
        "lat": 49.4095,
        "lng": 8.7115,
        "price": "free",
        "rating": 4.5,
        "description": "Füniküler istasyonunun bulunduğu meydan. Kale manzarası hayranlık uyandırıcı. Meryem heykeli meydanın ortasında.",
        "description_en": "Square where funicular station is located. Castle view is breathtaking. Madonna statue in center.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kaleye çıkmadan önce burada mola verin.",
        "tips_en": "Take a break here before going to castle."
    },
    {
        "name": "Universitätsplatz",
        "name_en": "University Square",
        "area": "Altstadt",
        "category": "Meydan",
        "tags": ["meydan", "üniversite", "aslan", "tarihi"],
        "distanceFromCenter": 0.2,
        "lat": 49.4100,
        "lng": 8.7055,
        "price": "free",
        "rating": 4.4,
        "description": "Üniversitenin merkezi meydanı. Aslan çeşmesi (Löwenbrunnen) ve Yeni Üniversite binası burada.",
        "description_en": "Central square of university. Lion fountain and New University building here.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Üniversite turlarına buradan başlayın.",
        "tips_en": "Start university tours from here."
    },
    {
        "name": "Plöck Sokağı",
        "name_en": "Plock Street",
        "area": "Altstadt",
        "category": "Alışveriş",
        "tags": ["sokak", "butik", "alternatif", "yerel"],
        "distanceFromCenter": 0.3,
        "lat": 49.4085,
        "lng": 8.7080,
        "price": "variable",
        "rating": 4.3,
        "description": "Hauptstraße'ye paralel, daha sakin alternatif. Vintage dükkanlar, yerel butikler.",
        "description_en": "Parallel to Hauptstraße, calmer alternative. Vintage shops, local boutiques.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Daha özgün hediyelikler için buraya gelin.",
        "tips_en": "Come here for more unique souvenirs."
    }
]

# BATCH 6: Aktiviteler & Deneyimler
batch_6 = [
    {
        "name": "Neckar Nehri Tekne Turu",
        "name_en": "Neckar River Boat Tour",
        "area": "Altstadt",
        "category": "Deneyim",
        "tags": ["tekne", "nehir", "tur", "manzara"],
        "distanceFromCenter": 0.3,
        "lat": 49.4120,
        "lng": 8.7090,
        "price": "medium",
        "rating": 4.5,
        "description": "Neckar Nehri üzerinde şehri keşfetmenin farklı bir yolu. Kaleden köprüye muhteşem manzaralar.",
        "description_en": "Different way to explore the city on Neckar River. Stunning views from castle to bridge.",
        "bestTime": "İkindi",
        "bestTime_en": "Afternoon",
        "tips": "Güneşli bir gün seçin.",
        "tips_en": "Choose a sunny day."
    },
    {
        "name": "Noel Pazarı",
        "name_en": "Christmas Market",
        "area": "Altstadt",
        "category": "Deneyim",
        "tags": ["noel", "pazar", "kış", "festival"],
        "distanceFromCenter": 0.1,
        "lat": 49.4096,
        "lng": 8.7098,
        "price": "free",
        "rating": 4.8,
        "description": "Kasım sonu-Aralık boyunca kurulan büyüleyici Noel pazarı. Glühwein, geleneksel yiyecekler ve el işi hediyelikler.",
        "description_en": "Enchanting Christmas market from late Nov-Dec. Glühwein, traditional foods and handcrafted gifts.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Akşam ışıkları altında daha büyülü.",
        "tips_en": "More magical under evening lights."
    },
    {
        "name": "Bisiklet Turu Neckar Vadisi",
        "name_en": "Neckar Valley Bike Tour",
        "area": "Dış Çevre",
        "category": "Deneyim",
        "tags": ["bisiklet", "doğa", "vadi", "tur"],
        "distanceFromCenter": 5.0,
        "lat": 49.4300,
        "lng": 8.7500,
        "price": "medium",
        "rating": 4.6,
        "description": "Neckar Nehri boyunca bisiklet turu. Komşu köyler ve şato kalıntılarını keşfedin.",
        "description_en": "Bike tour along Neckar River. Discover neighboring villages and castle ruins.",
        "bestTime": "Bahar-Yaz",
        "bestTime_en": "Spring-Summer",
        "tips": "Bisiklet kiralama Hauptbahnhof'ta mevcut.",
        "tips_en": "Bike rental available at Hauptbahnhof."
    },
    {
        "name": "Heidelberg Kalesi Işık Gösterisi",
        "name_en": "Castle Illumination Show",
        "area": "Schloss",
        "category": "Deneyim",
        "tags": ["ışık", "gösteri", "gece", "romantik"],
        "distanceFromCenter": 0.5,
        "lat": 49.4107,
        "lng": 8.7153,
        "price": "free",
        "rating": 4.9,
        "description": "Yaz aylarında (Haziran, Temmuz, Eylül) yapılan muhteşem kale ışıklandırması ve havai fişek gösterisi.",
        "description_en": "Magnificent castle illumination and fireworks show in summer (June, July, September).",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Alte Brücke veya Philosophenweg'den izleyin.",
        "tips_en": "Watch from Alte Brücke or Philosophenweg."
    },
    {
        "name": "Schwetzingen Sarayı (Günlük Gezi)",
        "name_en": "Schwetzingen Palace Day Trip",
        "area": "Schwetzingen",
        "category": "Günlük Gezi",
        "tags": ["saray", "bahçe", "barok", "gezi"],
        "distanceFromCenter": 15.0,
        "lat": 49.3833,
        "lng": 8.5667,
        "price": "medium",
        "rating": 4.6,
        "description": "Heidelberg'den 15 dk uzaklıkta muhteşem Barok saray ve bahçeleri. Alman Versay'ı olarak bilinir.",
        "description_en": "Magnificent Baroque palace and gardens 15 min from Heidelberg. Known as the German Versailles.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Spargelzeit (kuşkonmaz sezonu) Nisan-Haziran çok özel.",
        "tips_en": "Spargelzeit (asparagus season) April-June is very special."
    },
    {
        "name": "Neckarsteinach Dört Kale",
        "name_en": "Neckarsteinach Four Castles",
        "area": "Neckarsteinach",
        "category": "Günlük Gezi",
        "tags": ["kale", "yürüyüş", "orman", "gezi"],
        "distanceFromCenter": 12.0,
        "lat": 49.4025,
        "lng": 8.8369,
        "price": "free",
        "rating": 4.5,
        "description": "Tek köyde dört kale kalıntısı. Neckar boyunca güzel yürüyüş rotası.",
        "description_en": "Four castle ruins in one village. Beautiful hiking route along the Neckar.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Trenle 15 dakikada ulaşılır.",
        "tips_en": "Reachable by train in 15 minutes."
    }
]

# BATCH 7: Gece Hayatı & Barlar
batch_7 = [
    {
        "name": "Untere Straße (Bar Sokağı)",
        "name_en": "Lower Street (Bar Street)",
        "area": "Altstadt",
        "category": "Gece Hayatı",
        "tags": ["bar", "gece", "öğrenci", "canlı"],
        "distanceFromCenter": 0.2,
        "lat": 49.4085,
        "lng": 8.7100,
        "price": "medium",
        "rating": 4.3,
        "description": "Öğrencilerin gece hayatının merkezi. 20'den fazla bar yan yana sıralanır.",
        "description_en": "Center of student nightlife. Over 20 bars lined up side by side.",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Perşembe ve Cuma en kalabalık geceler.",
        "tips_en": "Thursday and Friday are busiest nights."
    },
    {
        "name": "Destille",
        "name_en": "Destille",
        "area": "Altstadt",
        "category": "Bar",
        "tags": ["bar", "viski", "kokteyl", "vintage"],
        "distanceFromCenter": 0.2,
        "lat": 49.4090,
        "lng": 8.7102,
        "price": "medium",
        "rating": 4.4,
        "description": "Vintage dekorlu, zengin viski ve kokteyl menüsüyle öne çıkan bar.",
        "description_en": "Bar with vintage decor, rich whiskey and cocktail menu.",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Happy hour akşam 18-20 arası.",
        "tips_en": "Happy hour 6-8pm."
    },
    {
        "name": "Havana Bar",
        "name_en": "Havana Bar",
        "area": "Altstadt",
        "category": "Bar",
        "tags": ["latin", "dans", "kokteyl", "müzik"],
        "distanceFromCenter": 0.2,
        "lat": 49.4088,
        "lng": 8.7095,
        "price": "medium",
        "rating": 4.2,
        "description": "Latin müzik ve dans, Küba atmosferi. Mojito ve rum kokteylleri.",
        "description_en": "Latin music and dance, Cuban atmosphere. Mojito and rum cocktails.",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Cumartesi geceleri salsa kursu.",
        "tips_en": "Salsa lessons on Saturday nights."
    },
    {
        "name": "Nachtschwärmer",
        "name_en": "Night Owl",
        "area": "Altstadt",
        "category": "Gece Hayatı",
        "tags": ["kulüp", "dans", "elektronik", "gece"],
        "distanceFromCenter": 0.3,
        "lat": 49.4082,
        "lng": 8.7110,
        "price": "medium",
        "rating": 4.1,
        "description": "Elektronik müzik ve DJ'lerle hafta sonları canlanan gece kulübü.",
        "description_en": "Nightclub coming alive on weekends with electronic music and DJs.",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Gece yarısından sonra kalabalıklaşır.",
        "tips_en": "Gets crowded after midnight."
    }
]

def enrich_heidelberg():
    """Main function to enrich Heidelberg data"""
    filepath = 'assets/cities/heidelberg.json'
    
    # Combine all batches
    all_new = batch_1 + batch_2 + batch_3 + batch_4 + batch_5 + batch_6 + batch_7
    
    # Load existing data
    with open(filepath, 'r') as f:
        data = json.load(f)
    print(f"Loaded {len(data['highlights'])} existing places.")
    
    existing_names = {p['name'].lower() for p in data['highlights']}
    places_to_add = []
    
    for place in all_new:
        if place['name'].lower() in existing_names:
            print(f"Skip: {place['name']}")
            continue
        
        print(f"Processing: {place['name']}")
        
        # Generate ID
        place_id = place['name'].lower()
        for char, repl in [(' ', '-'), ('ö', 'o'), ('ü', 'u'), ('ä', 'a'), ('ß', 'ss'), ('(', ''), (')', '')]:
            place_id = place_id.replace(char, repl)
        place['id'] = place_id
        
        # Fetch Google Photo
        photo_url = get_google_photo_url(place['name'])
        
        if photo_url:
            # For now, just use Google API URL directly
            # Firebase upload requires authentication setup
            place['imageUrl'] = photo_url
            place['source'] = 'google'
        else:
            place['imageUrl'] = "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
            place['source'] = 'unsplash_fallback'
        
        places_to_add.append(place)
        time.sleep(0.3)
    
    # Add new places
    data['highlights'].extend(places_to_add)
    
    # Save
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Added {len(places_to_add)} new places to {filepath}")
    print(f"Total highlights now: {len(data['highlights'])}")

if __name__ == "__main__":
    enrich_heidelberg()
