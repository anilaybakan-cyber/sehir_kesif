
import json
import requests
import time
import urllib.parse
import os
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase (if not already initialized)
if not firebase_admin._apps:
    cred = credentials.Certificate('service_account.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'myway-3fe75.firebasestorage.app'
    })

BUCKET = storage.bucket()
API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    try:
        # Search bias for Matera/Puglia region
        find_place_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(place_name)}&inputtype=textquery&fields=place_id,photos,formatted_address,name&key={API_KEY}&locationbias=circle:50000@40.6635,16.6061"
        response = requests.get(find_place_url)
        data = response.json()

        if data['status'] == 'OK' and len(data['candidates']) > 0:
            candidate = data['candidates'][0]
            if 'photos' in candidate:
                photo_reference = candidate['photos'][0]['photo_reference']
                return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={API_KEY}"
    except Exception as e:
        print(f"Error finding photo for {place_name}: {e}")
    return None

def download_and_upload_image(google_url, place_id, city_name):
    try:
        # Download
        local_path = f"/tmp/{place_id}.jpg"
        response = requests.get(google_url, stream=True)
        if response.status_code == 200:
            with open(local_path, 'wb') as f:
                f.write(response.content)
            
            # Upload
            remote_path = f"cities/{city_name.lower()}/{place_id}.jpg"
            blob = BUCKET.blob(remote_path)
            blob.upload_from_filename(local_path)
            blob.make_public()
            
            # Cleanup
            if os.path.exists(local_path):
                os.remove(local_path)
                
            return f"https://storage.googleapis.com/{BUCKET.name}/{remote_path}"
    except Exception as e:
        print(f"Error uploading {place_id}: {e}")
    return None

new_places = [
    {
        "name": "Castelmezzano",
        "name_en": "Castelmezzano",
        "area": "Dolomiti Lucane",
        "category": "Manzara",
        "tags": ["kasaba", "dağ", "en güzel"],
        "lat": 40.5300,
        "lng": 16.0500,
        "price": "free",
        "rating": 4.9,
        "description": "Dolomiti Lucane kayalıklarına oyulmuş, İtalya'nın en güzel köylerinden biri. (1 saat mesafe)",
        "description_en": "One of Italy's most beautiful villages carved into Dolomiti Lucane rocks. (1 hr away)",
        "bestTime": "Gündüz",
        "tips": "Gece ışıklandırması büyüleyicidir.",
        "tips_en": "Night lighting is fascinating."
    },
    {
        "name": "Pietrapertosa",
        "name_en": "Pietrapertosa",
        "area": "Dolomiti Lucane",
        "category": "Manzara",
        "tags": ["kasaba", "rakım", "kale"],
        "lat": 40.5200,
        "lng": 16.0600,
        "price": "free",
        "rating": 4.8,
        "description": "Basilicata'nın en yüksek rakımlı, kayaların zirvesine tünemiş masalsı kasabası.",
        "description_en": "Basilicata's highest altitude fairytale town perched on top of rocks.",
        "bestTime": "Gündüz",
        "tips": "Saraceno Kalesi'ne tırmanın.",
        "tips_en": "Climb Saraceno Castle."
    },
    {
        "name": "Volo dell'Angelo",
        "name_en": "Flight of the Angel",
        "area": "Dolomiti Lucane",
        "category": "Macera",
        "tags": ["zipline", "adrenalin", "uçuş"],
        "lat": 40.5250,
        "lng": 16.0550,
        "price": "high",
        "rating": 4.9,
        "description": "Castelmezzano ve Pietrapertosa arasında, vadinin üzerinden saatte 120 km hızla uçarak geçilen zipline.",
        "description_en": "Zipline flying over valley at 120 km/h between Castelmezzano and Pietrapertosa.",
        "bestTime": "Gündüz",
        "tips": "Önceden rezervasyon şarttır.",
        "tips_en": "Reservation required in advance."
    },
    {
        "name": "Aliano",
        "name_en": "Aliano",
        "area": "Aliano",
        "category": "Tarihi",
        "tags": ["edebiyat", "carlo levi", "sürgün"],
        "lat": 40.3100,
        "lng": 16.2300,
        "price": "free",
        "rating": 4.6,
        "description": "'İsa Bu Köye Uğramadı' kitabının yazarı Carlo Levi'nin sürgün edildiği, 'Calanchi' (kötü topraklar) manzaralı köy.",
        "description_en": "Village with 'Calanchi' (badlands) views where Carlo Levi, author of 'Christ Stopped at Eboli', was exiled.",
        "bestTime": "Gündüz",
        "tips": "Carlo Levi'nin evini ziyaret edin.",
        "tips_en": "Visit Carlo Levi's house."
    },
    {
        "name": "Church of San Domenico",
        "name_en": "Church of San Domenico",
        "area": "Centro",
        "category": "Tarihi",
        "tags": ["kilise", "romanest", "meydan"],
        "lat": 40.6685,
        "lng": 16.6070,
        "price": "free",
        "rating": 4.5,
        "description": "Piazza Vittorio Veneto'da bulunan, romanest tarzdaki etkileyici kilise.",
        "description_en": "Impressive Romanesque style church located in Piazza Vittorio Veneto.",
        "bestTime": "Gündüz",
        "tips": "Gül penceresi çok detaylıdır.",
        "tips_en": "Rose window is very detailed."
    },
    {
        "name": "Matera Central Station",
        "name_en": "Matera Central Station",
        "area": "Centro",
        "category": "Mimari",
        "tags": ["modern", "stefano boeri", "istasyon"],
        "lat": 40.6700,
        "lng": 16.6030,
        "price": "free",
        "rating": 4.4,
        "description": "Ünlü mimar Stefano Boeri tarafından tasarlanan, Matera'nın modern yüzünü simgeleyen yeni tren istasyonu.",
        "description_en": "New train station designed by famous architect Stefano Boeri, symbolizing Matera's modern face.",
        "bestTime": "Gündüz",
        "tips": "Mimari meraklıları için görülmeye değer.",
        "tips_en": "Worth seeing for architecture enthusiasts."
    },
    {
        "name": "Ginosa",
        "name_en": "Ginosa",
        "area": "Ginosa",
        "category": "Tarihi",
        "tags": ["mağara", "kanyon", "bakir"],
        "lat": 40.5800,
        "lng": 16.7500,
        "price": "free",
        "rating": 4.5,
        "description": "Matera'ya çok benzeyen ancak daha az turistik, kanyon yamacına kurulu mağara evlerin olduğu kasaba.",
        "description_en": "Town with cave houses built on canyon slope, looking very similar to Matera but less touristy.",
        "bestTime": "Gündüz",
        "tips": "Keşfedilmemiş bir hazinedir.",
        "tips_en": "An undiscovered treasure."
    },
    {
        "name": "Melfi Castle",
        "name_en": "Melfi Castle",
        "area": "Melfi",
        "category": "Tarihi",
        "tags": ["kale", "norman", "müze"],
        "lat": 40.9900,
        "lng": 15.6500,
        "price": "medium",
        "rating": 4.7,
        "description": "Volkanik Vulture bölgesine hakim, İtalya'nın en önemli Norman kalelerinden biri.",
        "description_en": "One of Italy's most important Norman castles, overlooking volcanic Vulture region.",
        "bestTime": "Gündüz",
        "tips": "İçindeki arkeoloji müzesi çok zengindir.",
        "tips_en": "Archaeology museum inside is very rich."
    },
    {
        "name": "Laghi di Monticchio",
        "name_en": "Monticchio Lakes",
        "area": "Vulture",
        "category": "Doğa",
        "tags": ["göl", "krater", "nilüfer"],
        "lat": 40.9300,
        "lng": 15.6100,
        "price": "free",
        "rating": 4.8,
        "description": "Sönmüş Vulture yanardağının kraterinde oluşmuş, yemyeşil doğa içindeki ikiz göller.",
        "description_en": "Twin lakes in lush nature formed in crater of extinct Vulture volcano.",
        "bestTime": "Gündüz",
        "tips": "Beyaz nilüferleri görmek için ilkbaharda gidin.",
        "tips_en": "Go in spring to see white water lilies."
    },
    {
        "name": "Sassula",
        "name_en": "Sassula",
        "area": "Sasso Caveoso",
        "category": "Restoran",
        "tags": ["modern", "tadım", "mağara"],
        "lat": 40.6640,
        "lng": 16.6125,
        "price": "high",
        "rating": 4.6,
        "description": "Geleneksel lezzetleri modern tekniklerle yorumlayan şık mağara restoranı.",
        "description_en": "Chic cave restaurant interpreting traditional flavors with modern techniques.",
        "bestTime": "Akşam",
        "tips": "Sunumları sanat eseri gibidir.",
        "tips_en": "Presentations are like works of art."
    },
    {
        "name": "5 Lire",
        "name_en": "5 Lire Matera",
        "area": "Centro",
        "category": "Bar",
        "tags": ["sokak", "aperitivo", "genç"],
        "lat": 40.6670,
        "lng": 16.6060,
        "price": "low",
        "rating": 4.5,
        "description": "Yerel gençlerin aperitivo için buluştuğu, samimi ve hareketli sokak barı.",
        "description_en": "Friendly and lively street bar where local youth meet for aperitivo.",
        "bestTime": "Akşam",
        "tips": "Kokteylleri çok uygundur.",
        "tips_en": "Cocktails are very affordable."
    },
    {
        "name": "Birrificio degli Ostinati",
        "name_en": "Birrificio degli Ostinati",
        "area": "Outskirts",
        "category": "Bar",
        "tags": ["bira", "üretim", "bahçe"],
        "lat": 40.6500,
        "lng": 16.5800,
        "price": "medium",
        "rating": 4.7,
        "description": "Şehir dışında, kendi biralarını üreten ve geniş bir bahçesi olan keyifli birrificio.",
        "description_en": "Pleasant brewery outside city producing its own beers with a large garden.",
        "bestTime": "Hafta sonu",
        "tips": "Yaz akşamları için mükemmeldir.",
        "tips_en": "Perfect for summer evenings."
    },
    {
        "name": "Enoteca Il Buco",
        "name_en": "Enoteca Il Buco",
        "area": "Centro",
        "category": "Bar",
        "tags": ["şarap", "küçük", "samimi"],
        "lat": 40.6665,
        "lng": 16.6075,
        "price": "medium",
        "rating": 4.5,
        "description": "Adı gibi 'kovuk' kadar küçük ama şarap kavı kocaman olan sevimli şarap evi.",
        "description_en": "Cute wine house small as a 'hole' as its name suggests but with huge wine cellar.",
        "bestTime": "Akşam",
        "tips": "Ayaküstü bir kadeh için ideal.",
        "tips_en": "Ideal for a quick glass."
    },
    {
        "name": "Bar Ridola",
        "name_en": "Bar Ridola",
        "area": "Centro",
        "category": "Kafe",
        "tags": ["kahve", "teras", "geleneksel"],
        "lat": 40.6650,
        "lng": 16.6090,
        "price": "medium",
        "rating": 4.4,
        "description": "Via Ridola üzerinde, geleni geçeni izleyebileceğiniz klasik bir İtalyan barı.",
        "description_en": "Classic Italian bar on Via Ridola where you can watch passersby.",
        "bestTime": "Gündüz",
        "tips": "Dondurmalı kahvesi (caffè leccese) güzeldir.",
        "tips_en": "Tip: Iced coffee with almond milk (caffè leccese) is nice."
    },
    {
        "name": "Bar Sottozero",
        "name_en": "Bar Sottozero Matera",
        "area": "Centro",
        "category": "Fırın",
        "tags": ["panzerotti", "gece", "atıştırmalık"],
        "lat": 40.6710,
        "lng": 16.6020,
        "price": "low",
        "rating": 4.6,
        "description": "Gece geç saatlere kadar açık olan, özellikle panzerotti'si ile meşhur mekan.",
        "description_en": "Venue open late at night, especially famous for its panzerotti.",
        "bestTime": "Gece",
        "tips": "Bira ve panzerotti ikilisi klasiktir.",
        "tips_en": "Beer and panzerotti duo is classic."
    },
    {
        "name": "Castellaneta",
        "name_en": "Castellaneta",
        "area": "Castellaneta",
        "category": "Tarihi",
        "tags": ["sinema", "valentino", "kanyon"],
        "lat": 40.6300,
        "lng": 16.9300,
        "price": "free",
        "rating": 4.3,
        "description": "Sessiz sinemanın efsanesi Rodolfo Valentino'nun doğum yeri. Müzesi gezilebilir. (40 dk mesafe)",
        "description_en": "Birthplace of silent movie legend Rodolfo Valentino. Museum can be visited. (40 min away)",
        "bestTime": "Gündüz",
        "tips": "Kanyon manzarası (Gravina di Castellaneta) da vardır.",
        "tips_en": "Also has canyon view (Gravina di Castellaneta)."
    },
    {
        "name": "San Severino Lucano",
        "name_en": "San Severino Lucano",
        "area": "Pollino",
        "category": "Doğa",
        "tags": ["milli park", "dağ", "yürüyüş"],
        "lat": 40.0100,
        "lng": 16.1400,
        "price": "free",
        "rating": 4.7,
        "description": "Pollino Milli Parkı'nın kalbi. Doğa yürüyüşü ve temiz hava için harika bir durak.",
        "description_en": "Heart of Pollino National Park. Great stop for hiking and fresh air.",
        "bestTime": "Gündüz",
        "tips": "Bosco Magnano ormanı çok güzeldir.",
        "tips_en": "Bosco Magnano forest is very beautiful."
    },
    {
        "name": "Guardia Perticara",
        "name_en": "Guardia Perticara",
        "area": "Basilicata",
        "category": "Tarihi",
        "tags": ["taş", "köy", "mimari"],
        "lat": 40.3600,
        "lng": 16.1000,
        "price": "free",
        "rating": 4.6,
        "description": "Bütün evlerin yontma taştan yapıldığı, 'Taş Evler Köyü' olarak bilinen büyüleyici yer.",
        "description_en": "Fascinating place known as 'Village of Stone Houses' where all houses are made of hewn stone.",
        "bestTime": "Gündüz",
        "tips": "Dar sokaklarında kaybolun.",
        "tips_en": "Get lost in narrow streets."
    },
    {
        "name": "Mercato Ortofrutticolo",
        "name_en": "Matera Market",
        "area": "Centro",
        "category": "Alışveriş",
        "tags": ["pazar", "taze", "yerel"],
        "lat": 40.6720,
        "lng": 16.5980,
        "price": "low",
        "rating": 4.4,
        "description": "Yerel üreticilerin taze meyve, sebze ve peynir sattığı açık hava pazarı.",
        "description_en": "Open air market where local producers sell fresh fruit, vegetables and cheese.",
        "bestTime": "Cumartesi Sabah",
        "tips": "En taze ürünler sabah erkenden bulunur.",
        "tips_en": "Freshest products found early morning."
    },
    {
        "name": "Parco Giovanni Paolo II",
        "name_en": "Pope John Paul II Park",
        "area": "Centro",
        "category": "Park",
        "tags": ["yeşil", "dinlenme", "aile"],
        "lat": 40.6620,
        "lng": 16.6020,
        "price": "free",
        "rating": 4.3,
        "description": "Şehir merkezinde, 'Boschetto' olarak da bilinen, ağaçlar içinde sakin bir park.",
        "description_en": "Quiet park in city center among trees, also known as 'Boschetto'.",
        "bestTime": "Gündüz",
        "tips": "Çocuklu aileler için uygundur.",
        "tips_en": "Suitable for families with children."
    },
    {
        "name": "Chiesa di Santa Maria di Costantinopoli",
        "name_en": "Church of Santa Maria di Costantinopoli",
        "area": "Sasso Barisano",
        "category": "Tarihi",
        "tags": ["kilise", "küçük", "barok"],
        "lat": 40.6695,
        "lng": 16.6095,
        "price": "free",
        "rating": 4.4,
        "description": "Sasso Barisano'nun kalbinde, zarif bir mimariye sahip küçük kilise.",
        "description_en": "Small church with elegant architecture in heart of Sasso Barisano.",
        "bestTime": "Gündüz",
        "tips": "İçindeki ahşap tavan ilginçtir.",
        "tips_en": "Wooden ceiling inside is interesting."
    },
    {
        "name": "Stadio XXI Settembre",
        "name_en": "Stadio XXI Settembre",
        "area": "Centro",
        "category": "Spor",
        "tags": ["futbol", "tarih", "yerel"],
        "lat": 40.6730,
        "lng": 16.6000,
        "price": "medium",
        "rating": 4.2,
        "description": "Matera'nın tarihi futbol stadyumu. Yerel maç atmosferini koklamak için.",
        "description_en": "Matera's historic football stadium. To smell local match atmosphere.",
        "bestTime": "Maç günü",
        "tips": "Franco Salerno adıyla da bilinir.",
        "tips_en": "Also known as Franco Salerno."
    }
]

def process_city():
    city_name = "matera"
    filepath = f'assets/cities/{city_name}.json'
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    existing_ids = {h.get('id', '') for h in data['highlights']}
    
    print(f"Processing {len(new_places)} new places for {city_name}...")
    
    added_count = 0
    for place in new_places:
        # Create ID
        place_id = place['name_en'].lower().replace(' ', '-').replace("'", "").replace(".", "")
        if place_id in existing_ids:
            print(f"Skipping {place['name']} (already exists)")
            continue
            
        print(f"Adding: {place['name']}")
        
        # Get Photo
        photo_url = get_google_photo_url(place['name'])
        final_photo_url = ""
        
        if photo_url:
            print(f"  Downloading & Uploading photo...")
            firebase_url = download_and_upload_image(photo_url, place_id, city_name)
            if firebase_url:
                final_photo_url = firebase_url
                print(f"  ✓ Photo uploaded: {firebase_url}")
            else:
                print(f"  ⚠ Photo upload failed, using Google URL directly")
                final_photo_url = photo_url
        else:
            print(f"  ⚠ No photo found")
            # Fallback or keep empty
            
        # Add to highlights
        new_highlight = place.copy()
        new_highlight['id'] = place_id
        if final_photo_url:
            new_highlight['imageUrl'] = final_photo_url
            new_highlight['source'] = 'firebase' if 'firebase' in final_photo_url else 'google'
        
        # Add default distance if not present (logic can be improved to calc from center)
        if 'distanceFromCenter' not in new_highlight:
            new_highlight['distanceFromCenter'] = 0.5
            
        data['highlights'].append(new_highlight)
        added_count += 1
        time.sleep(0.5) # Rate limit
        
    # Save
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"Added {added_count} new places to {city_name}!")

if __name__ == "__main__":
    process_city()
