
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
        # Search bias for Cairo
        find_place_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(place_name)}&inputtype=textquery&fields=place_id,photos,formatted_address,name&key={API_KEY}&locationbias=circle:20000@30.0444,31.2357"
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
        "name": "Step Pyramid of Djoser",
        "name_en": "Step Pyramid of Djoser",
        "area": "Saqqara",
        "category": "Tarihi",
        "tags": ["piramit", "ilk", "tarih"],
        "lat": 29.8700,
        "lng": 31.2100,
        "price": "high",
        "rating": 4.8,
        "description": "Tarihin ilk piramidi ve ilk büyük taş yapısı. Mimar Imhotep tarafından yapılmıştır.",
        "description_en": "First pyramid and first major stone structure in history. Built by architect Imhotep.",
        "bestTime": "Sabah",
        "tips": "İçine girmek için ayrı bilet gerekir.",
        "tips_en": "Separate ticket required to enter inside."
    },
    {
        "name": "Bibliotheca Alexandrina",
        "name_en": "Bibliotheca Alexandrina",
        "area": "Alexandria",
        "category": "Kültür",
        "tags": ["kütüphane", "modern", "iskenderiye"],
        "lat": 31.2100,
        "lng": 29.9100,
        "price": "medium",
        "rating": 4.9,
        "description": "Antik İskenderiye Kütüphanesi'nin modern bir yorumu olan muhteşem mimari eser. (Günübirlik Gezi)",
        "description_en": "Magnificent architectural work, a modern interpretation of Ancient Library of Alexandria. (Day Trip)",
        "bestTime": "Gündüz",
        "tips": "Müzeleri ve okuma salonunu gezin.",
        "tips_en": "Visit museums and reading hall."
    },
    {
        "name": "Red Pyramid",
        "name_en": "Red Pyramid",
        "area": "Dahshur",
        "category": "Tarihi",
        "tags": ["piramit", "kırmızı", "dahshur"],
        "lat": 29.8000,
        "lng": 31.2000,
        "price": "medium",
        "rating": 4.7,
        "description": "Gerçek piramit formunun (düz kenarlı) ilk başarılı örneği. Taşlarının renginden adını alır.",
        "description_en": "First successful example of true pyramid form (smooth-sided). Named after color of its stones.",
        "bestTime": "Sabah",
        "tips": "İçine girmek ücretsizdir ama yorucudur.",
        "tips_en": "Free to enter inside but tiring."
    },
    {
        "name": "Bent Pyramid",
        "name_en": "Bent Pyramid",
        "area": "Dahshur",
        "category": "Tarihi",
        "tags": ["piramit", "eğik", "ilginç"],
        "lat": 29.7900,
        "lng": 31.2000,
        "price": "medium",
        "rating": 4.6,
        "description": "Yapımı sırasında açısı değiştirildiği için eğik görünen, kaplamaları en iyi korunmuş piramit.",
        "description_en": "Pyramid looking bent as angle changed during construction, with best preserved casing.",
        "bestTime": "Sabah",
        "tips": "Dahshur bölgesi çok sakindir.",
        "tips_en": "Dahshur area is very quiet."
    },
    {
        "name": "Wadi El Rayan",
        "name_en": "Wadi El Rayan",
        "area": "Fayoum",
        "category": "Doğa",
        "tags": ["şelale", "çöl", "göl"],
        "lat": 29.1500,
        "lng": 30.4000,
        "price": "low",
        "rating": 4.5,
        "description": "Mısır'ın çöl ortasındaki tek şelalesine ev sahipliği yapan milli park. (Günübirlik Gezi)",
        "description_en": "National park housing Egypt's only waterfall in middle of desert. (Day Trip)",
        "bestTime": "Gündüz",
        "tips": "Kum kayağı yapabilirsiniz.",
        "tips_en": "You can do sand boarding."
    },
    {
        "name": "Citadel of Qaitbay",
        "name_en": "Citadel of Qaitbay",
        "area": "Alexandria",
        "category": "Tarihi",
        "tags": ["kale", "deniz", "fener"],
        "lat": 31.2150,
        "lng": 29.8850,
        "price": "medium",
        "rating": 4.7,
        "description": "Antik İskenderiye Feneri'nin yıkıntıları üzerine ve taşları kullanılarak yapılan kale.",
        "description_en": "Citadel built on ruins and using stones of Ancient Lighthouse of Alexandria.",
        "bestTime": "Gündüz",
        "tips": "Deniz manzarası harikadır.",
        "tips_en": "Sea view is great."
    },
    {
        "name": "Waterway",
        "name_en": "The Waterway",
        "area": "New Cairo",
        "category": "Eğlence",
        "tags": ["restoran", "modern", "lüks"],
        "lat": 30.0400,
        "lng": 31.4800,
        "price": "high",
        "rating": 4.7,
        "description": "Lüks restoranlar ve kafelerin bulunduğu, New Cairo'nun en popüler açık hava kompleksi.",
        "description_en": "New Cairo's most popular open-air complex with luxury restaurants and cafes.",
        "bestTime": "Akşam",
        "tips": "Akşam yemeği için rezervasyon şart.",
        "tips_en": "Reservation required for dinner."
    },
    {
        "name": "Serapeum of Saqqara",
        "name_en": "Serapeum of Saqqara",
        "area": "Saqqara",
        "category": "Tarihi",
        "tags": ["yer altı", "gizem", "lahit"],
        "lat": 29.8750,
        "lng": 31.2100,
        "price": "medium",
        "rating": 4.9,
        "description": "Apis boğalarının mumyalandığı dev granit lahitlerin bulunduğu gizemli yer altı galerisi.",
        "description_en": "Mysterious underground gallery with huge granite sarcophagi where Apis bulls were mummified.",
        "bestTime": "Gündüz",
        "tips": "Mühendislik harikasıdır.",
        "tips_en": "It is an engineering marvel."
    },
    {
        "name": "Tunis Village",
        "name_en": "Tunis Village Fayoum",
        "area": "Fayoum",
        "category": "Kültür",
        "tags": ["köy", "sanat", "çömlek"],
        "lat": 29.4000,
        "lng": 30.5000,
        "price": "free",
        "rating": 4.6,
        "description": "Fayoum vahasında, çömlek atölyeleri ve butik otelleriyle ünlü sanat köyü.",
        "description_en": "Art village in Fayoum oasis famous for pottery workshops and boutique hotels.",
        "bestTime": "Hafta sonu",
        "tips": "Evelyne'in çömlek okulunu gezin.",
        "tips_en": "Visit Evelyne's pottery school."
    },
    {
        "name": "Stanley Bridge",
        "name_en": "Stanley Bridge",
        "area": "Alexandria",
        "category": "Manzara",
        "tags": ["köprü", "deniz", "ikonik"],
        "lat": 31.2300,
        "lng": 29.9500,
        "price": "free",
        "rating": 4.7,
        "description": "İskenderiye kordon boyunun simgesi haline gelen, denizin üzerinden geçen ikonik köprü.",
        "description_en": "Iconic bridge passing over sea, becoming symbol of Alexandria corniche.",
        "bestTime": "Akşam",
        "tips": "Gün batımı fotoğrafları için ideal.",
        "tips_en": "Ideal for sunset photos."
    },
    {
        "name": "Imhotep Museum",
        "name_en": "Imhotep Museum",
        "area": "Saqqara",
        "category": "Müze",
        "tags": ["müze", "tarih", "saqqara"],
        "lat": 29.8650,
        "lng": 31.2150,
        "price": "included",
        "rating": 4.5,
        "description": "Saqqara bölgesinden çıkarılan eserlerin ve mimar Imhotep'in onuruna yapılmış müze.",
        "description_en": "Museum built in honor of architect Imhotep and artifacts excavated from Saqqara region.",
        "bestTime": "Gündüz",
        "tips": "Giriş biletine dahildir.",
        "tips_en": "Included in entrance ticket."
    },
    {
        "name": "Wadi El Hitan",
        "name_en": "Wadi El Hitan",
        "area": "Fayoum",
        "category": "Doğa",
        "tags": ["unesco", "balina", "fosil"],
        "lat": 29.2800,
        "lng": 30.0100,
        "price": "medium",
        "rating": 4.9,
        "description": "UNESCO Dünya Mirası listesindeki 'Balinalar Vadisi'. Çöl ortasında dev balina fosilleri vardır.",
        "description_en": "'Valley of Whales' on UNESCO World Heritage list. Has giant whale fossils in middle of desert.",
        "bestTime": "Kış",
        "tips": "Müzesi çok bilgilendiricidir.",
        "tips_en": "Its museum is very informative."
    },
    {
        "name": "Montaza Palace",
        "name_en": "Montaza Palace Gardens",
        "area": "Alexandria",
        "category": "Doğa",
        "tags": ["saray", "bahçe", "plaj"],
        "lat": 31.2800,
        "lng": 30.0150,
        "price": "medium",
        "rating": 4.5,
        "description": "Kral Faruk'un yazlık sarayı ve geniş bahçeleri. Denize girmek ve piknik için popülerdir.",
        "description_en": "King Farouk's summer palace and vast gardens. Popular for swimming and picnicking.",
        "bestTime": "Gündüz",
        "tips": "Sarayın içine girilmiyor, bahçesi geziliyor.",
        "tips_en": "Cannot enter palace, gardens are visited."
    },
    {
        "name": "Pyramid of Teti",
        "name_en": "Pyramid of Teti",
        "area": "Saqqara",
        "category": "Tarihi",
        "tags": ["piramit", "metinler", "içerisi"],
        "lat": 29.8750,
        "lng": 31.2200,
        "price": "included",
        "rating": 4.4,
        "description": "Dışarıdan yıkıntı gibi görünse de, içi hiyeroglif 'Piramit Metinleri' ile doludur.",
        "description_en": "Though looking like ruin from outside, inside is full of hieroglyphic 'Pyramid Texts'.",
        "bestTime": "Sabah",
        "tips": "İçeri girmek kolaydır.",
        "tips_en": "Easy to enter inside."
    },
    {
        "name": "Magic Lake",
        "name_en": "Magic Lake Fayoum",
        "area": "Fayoum",
        "category": "Doğa",
        "tags": ["göl", "çöl", "renk"],
        "lat": 29.2500,
        "lng": 30.2500,
        "price": "free",
        "rating": 4.8,
        "description": "Günün saatine göre rengi değişen, kum tepeleriyle çevrili büyüleyici göl.",
        "description_en": "Enchanting lake surrounded by sand dunes, changing color according to time of day.",
        "bestTime": "Gün batımı",
        "tips": "4x4 araçla gidilir.",
        "tips_en": "Reached by 4x4 vehicle."
    },
    {
        "name": "Memphis Open Air Museum",
        "name_en": "Memphis Open Air Museum",
        "area": "Memphis",
        "category": "Müze",
        "tags": ["heykel", "ramses", "antik"],
        "lat": 29.8500,
        "lng": 31.2500,
        "price": "medium",
        "rating": 4.4,
        "description": "Antik Mısır'ın ilk başkenti Memphis'ten kalan dev Ramses heykelinin bulunduğu açık hava müzesi.",
        "description_en": "Open air museum housing giant Ramses statue remaining from Ancient Egypt's first capital Memphis.",
        "bestTime": "Gündüz",
        "tips": "Yatık duran dev heykel etkileyicidir.",
        "tips_en": "Lying giant statue is impressive."
    },
    {
        "name": "Kom el Shoqafa",
        "name_en": "Catacombs of Kom el Shoqafa",
        "area": "Alexandria",
        "category": "Tarihi",
        "tags": ["mezarlık", "roma", "yeraltı"],
        "lat": 31.1800,
        "lng": 29.8900,
        "price": "medium",
        "rating": 4.6,
        "description": "Mısır, Yunan ve Roma sanatının karıştığı, Orta Çağ'ın 7 harikasından sayılan yeraltı mezarlığı.",
        "description_en": "Underground cemetery considered one of 7 wonders of Middle Ages, mixing Egyptian, Greek and Roman art.",
        "bestTime": "Gündüz",
        "tips": "Merdivenle çok aşağı iniliyor.",
        "tips_en": "Descending way down by stairs."
    },
    {
        "name": "Point 90 Mall",
        "name_en": "Point 90 Mall",
        "area": "New Cairo",
        "category": "Alışveriş",
        "tags": ["avm", "sinema", "gençlik"],
        "lat": 30.0250,
        "lng": 31.4900,
        "price": "medium",
        "rating": 4.5,
        "description": "AUC (Amerikan Üniversitesi) karşısında, gençlerin popüler buluşma noktası.",
        "description_en": "Popular meeting point for youth, across from AUC (American University).",
        "bestTime": "Akşam",
        "tips": "Sineması çok iyidir.",
        "tips_en": "Cinema is very good."
    },
    {
        "name": "Fish Garden",
        "name_en": "Fish Garden",
        "area": "Zamalek",
        "category": "Doğa",
        "tags": ["park", "romantik", "mağara"],
        "lat": 30.0600,
        "lng": 31.2150,
        "price": "low",
        "rating": 4.2,
        "description": "Mağara şeklinde yapılmış akvaryum kalıntıları olan romantik ve tarihi bir park.",
        "description_en": "Romantic and historic park with aquarium ruins built in cave shape.",
        "bestTime": "Gündüz",
        "tips": "Eski Mısır filmlerinin setidir.",
        "tips_en": "Set of old Egyptian movies."
    },
    {
        "name": "Garden 8",
        "name_en": "Garden 8",
        "area": "New Cairo",
        "category": "Eğlence",
        "tags": ["şık", "restoran", "butik"],
        "lat": 30.0500,
        "lng": 31.4700,
        "price": "high",
        "rating": 4.6,
        "description": "Lüks markaların ve fine-dining restoranların bulunduğu butik açık hava AVM.",
        "description_en": "Boutique open-air mall with luxury brands and fine-dining restaurants.",
        "bestTime": "Akşam",
        "tips": "Oldukça sakindir.",
        "tips_en": "Quite quiet."
    },
    {
        "name": "Pyramid of Unas",
        "name_en": "Pyramid of Unas",
        "area": "Saqqara",
        "category": "Tarihi",
        "tags": ["piramit", "hazine", "yazıt"],
        "lat": 29.8680,
        "lng": 31.2130,
        "price": "included",
        "rating": 4.5,
        "description": "İçindeki koridorları ve mezar odası tamamen hiyerogliflerle kaplı ilk piramit.",
        "description_en": "First pyramid with corridors and burial chamber completely covered in hieroglyphs.",
        "bestTime": "Sabah",
        "tips": "Okumayı deneyin.",
        "tips_en": "Try reading."
    },
    {
        "name": "Pompey's Pillar",
        "name_en": "Pompey's Pillar",
        "area": "Alexandria",
        "category": "Tarihi",
        "tags": ["sütun", "roma", "antik"],
        "lat": 31.1820,
        "lng": 29.8960,
        "price": "medium",
        "rating": 4.3,
        "description": "İskenderiye'deki en büyük antik anıt olan tek parça, devasa granit sütun.",
        "description_en": "Biggest ancient monument in Alexandria, a single massive granite pillar.",
        "bestTime": "Gündüz",
        "tips": "Sfenks heykelleriyle çevrilidir.",
        "tips_en": "Surrounded by sphinx statues."
    },
    {
        "name": "Birqash Camel Market",
        "name_en": "Birqash Camel Market",
        "area": "Birqash",
        "category": "Kültür",
        "tags": ["pazar", "deve", "kaos"],
        "lat": 30.1500,
        "lng": 31.0500,
        "price": "low",
        "rating": 4.1,
        "description": "Afrika'nın en büyük deve pazarı. Kaotik ve tozlu ama fotoğrafçılar için eşsizdir.",
        "description_en": "Africa's largest camel market. Chaotic and dusty but unique for photographers.",
        "bestTime": "Cuma Sabah",
        "tips": "Erken saatte gidin, turistler için şaşırtıcı olabilir.",
        "tips_en": "Go early, can be shocking for tourists."
    },
    {
        "name": "Smart Village",
        "name_en": "Smart Village Cairo",
        "area": "6th of October",
        "category": "Modern",
        "tags": ["iş", "teknoloji", "park"],
        "lat": 30.0700,
        "lng": 31.0200,
        "price": "free",
        "rating": 4.4,
        "description": "Mısır'ın teknoloji ve iş merkezi. Modern mimari örnekleri ve yeşil alanlar vardır.",
        "description_en": "Egypt's technology and business hub. Has examples of modern architecture and green areas.",
        "bestTime": "Hafta içi",
        "tips": "Giriş için izin gerekebilir.",
        "tips_en": "Entry may require permission."
    },
    {
        "name": "Petrified Forest",
        "name_en": "Petrified Forest Protectorate",
        "area": "New Cairo",
        "category": "Doğa",
        "tags": ["fosil", "orman", "çöl"],
        "lat": 30.0100,
        "lng": 31.4500,
        "price": "low",
        "rating": 3.9,
        "description": "Milyonlarca yıllık taşlaşmış ağaç gövdelerinin bulunduğu koruma alanı.",
        "description_en": "Protected area with millions of years old petrified tree trunks.",
        "bestTime": "Gündüz",
        "tips": "Rehbersiz çok şey ifade etmeyebilir.",
        "tips_en": "May not mean much without guide."
    },
    {
        "name": "Andalus Garden",
        "name_en": "Al-Andalus Garden",
        "area": "Zamalek",
        "category": "Doğa",
        "tags": ["bahçe", "endülüs", "nil"],
        "lat": 30.0450,
        "lng": 31.2260,
        "price": "low",
        "rating": 4.3,
        "description": "Nil kenarında, Endülüs İslam mimarisi tarzında düzenlenmiş şirin park.",
        "description_en": "Cute park organized in Andalusian Islamic architecture style by the Nile.",
        "bestTime": "Akşam",
        "tips": "Nil'i izlemek için banklar vardır.",
        "tips_en": "Has benches to watch the Nile."
    },
    {
        "name": "Roman Amphitheatre",
        "name_en": "Kom el-Dikka",
        "area": "Alexandria",
        "category": "Tarihi",
        "tags": ["tiyatro", "roma", "mozaik"],
        "lat": 31.1950,
        "lng": 29.9050,
        "price": "medium",
        "rating": 4.4,
        "description": "Mısır'da bulunan tek Roma amfitiyatrosu. Kuş villası ve mozaikler de buradadır.",
        "description_en": "Only Roman amphitheatre found in Egypt. Bird villa and mosaics are also here.",
        "bestTime": "Gündüz",
        "tips": "Tam şehir merkezindedir.",
        "tips_en": "Right in city center."
    },
    {
        "name": "Abu al-Abbas al-Mursi Mosque",
        "name_en": "Abu al-Abbas al-Mursi Mosque",
        "area": "Alexandria",
        "category": "Tarihi",
        "tags": ["cami", "mimari", "iskenderiye"],
        "lat": 31.2050,
        "lng": 29.8800,
        "price": "free",
        "rating": 4.7,
        "description": "İskenderiye'nin en büyük ve güzel camisi. Endülüs mimarisi ve krem rengi kubbeleriyle ünlüdür.",
        "description_en": "Alexandria's largest and most beautiful mosque. Famous for Andalusian architecture and cream domes.",
        "bestTime": "Gündüz",
        "tips": "Deniz kenarındadır.",
        "tips_en": "Located by the sea."
    },
    {
        "name": "Family Park",
        "name_en": "Family Park Cairo",
        "area": "New Cairo",
        "category": "Doğa",
        "tags": ["park", "aile", "hayvanat bahçesi"],
        "lat": 30.0800,
        "lng": 31.5000,
        "price": "medium",
        "rating": 4.5,
        "description": "Hayvanat bahçesi, müze ve treni olan, aileler için ideal devasa park.",
        "description_en": "Massive park ideal for families, with zoo, museum and train.",
        "bestTime": "Hafta sonu",
        "tips": "Tüm gün geçirilebilir.",
        "tips_en": "Can spend whole day."
    },
    {
        "name": "Qanater Barrages",
        "name_en": "Qanater Gardens",
        "area": "Qanater",
        "category": "Doğa",
        "tags": ["piknik", "nil", "tarihi"],
        "lat": 30.1900,
        "lng": 31.1100,
        "price": "low",
        "rating": 4.2,
        "description": "Nil'in Delta'ya ayrıldığı noktadaki tarihi barajlar ve geniş piknik bahçeleri.",
        "description_en": "Historic barrages and vast picnic gardens at point where Nile splits into Delta.",
        "bestTime": "Gündüz",
        "tips": "Nil tekne turuyla gidilebilir.",
        "tips_en": "Can be reached by Nile boat tour."
    },
    {
        "name": "Karanis",
        "name_en": "Karanis",
        "area": "Fayoum",
        "category": "Tarihi",
        "tags": ["antik", "şehir", "tapınak"],
        "lat": 29.5000,
        "lng": 30.9000,
        "price": "low",
        "rating": 4.3,
        "description": "Fayoum bölgesindeki en büyük Greko-Romen antik kenti kalıntıları.",
        "description_en": "Remains of largest Greco-Roman ancient city in Fayoum region.",
        "bestTime": "Gündüz",
        "tips": "Timsah tapınağını görün.",
        "tips_en": "See crocodile temple."
    },
    {
        "name": "Lake View Plaza",
        "name_en": "Lake View Plaza",
        "area": "New Cairo",
        "category": "Eğlence",
        "tags": ["modern", "restoran", "meydan"],
        "lat": 30.0300,
        "lng": 31.4800,
        "price": "medium",
        "rating": 4.4,
        "description": "New Cairo'da popüler restoranların ve dükkanların olduğu açık hava kompleksi.",
        "description_en": "Open air complex with popular restaurants and shops in New Cairo.",
        "bestTime": "Akşam",
        "tips": "Gençlerin uğrak yeridir.",
        "tips_en": "Hangout spot for youth."
    },
    {
        "name": "Papyrus Institute",
        "name_en": "Papyrus Institute",
        "area": "Giza",
        "category": "Kültür",
        "tags": ["kağıt", "sanat", "tarih"],
        "lat": 29.9900,
        "lng": 31.1500,
        "price": "free",
        "rating": 4.2,
        "description": "Antik Mısır'da papirüs kağıdının nasıl yapıldığını gösteren atölye ve dükkan.",
        "description_en": "Workshop and shop showing how papyrus paper was made in Ancient Egypt.",
        "bestTime": "Gündüz",
        "tips": "Satın almak zorunda değilsiniz, izleyin.",
        "tips_en": "Don't have to buy, just watch."
    },
    {
        "name": "Royal Jewelry Museum",
        "name_en": "Royal Jewelry Museum",
        "area": "Alexandria",
        "category": "Müze",
        "tags": ["mücevher", "saray", "lüks"],
        "lat": 31.2500,
        "lng": 29.9600,
        "price": "high",
        "rating": 4.7,
        "description": "Mısır kraliyet ailesinin paha biçilemez mücevherlerinin sergilendiği göz kamaştırıcı müze.",
        "description_en": "Dazzling museum exhibiting priceless jewelry of Egyptian royal family.",
        "bestTime": "Gündüz",
        "tips": "Sarayın kendisi de bir mücevher gibidir.",
        "tips_en": "Palace itself is like a jewel."
    },
    {
        "name": "Helwan Wax Museum",
        "name_en": "Helwan Wax Museum",
        "area": "Helwan",
        "category": "Müze",
        "tags": ["balmumu", "tarih", "ilginç"],
        "lat": 29.8500,
        "lng": 31.3300,
        "price": "low",
        "rating": 4.0,
        "description": "Mısır tarihini canlandıran balmumu heykellerin olduğu, biraz eski ama ilginç müze.",
        "description_en": "Slightly old but interesting museum with wax statues depicting Egyptian history.",
        "bestTime": "Gündüz",
        "tips": "Metro ile gidilebilir.",
        "tips_en": "Reachable by metro."
    },
    {
        "name": "Maadi Grand Mall",
        "name_en": "Maadi Grand Mall",
        "area": "Maadi",
        "category": "Alışveriş",
        "tags": ["avm", "eski", "yerel"],
        "lat": 29.9700,
        "lng": 31.2900,
        "price": "low",
        "rating": 3.8,
        "description": "Maadi'nin eski ve nostaljik alışveriş merkezi. Küçük dükkanlar ve terziler vardır.",
        "description_en": "Maadi's old and nostalgic mall. Has small shops and tailors.",
        "bestTime": "Gündüz",
        "tips": "Uygun fiyatlı alışveriş için iyidir.",
        "tips_en": "Good for affordable shopping."
    },
    {
        "name": "Dream Park",
        "name_en": "Dream Park",
        "area": "6th of October",
        "category": "Eğlence",
        "tags": ["lunapark", "adrenalin", "çocuk"],
        "lat": 29.9600,
        "lng": 31.0500,
        "price": "medium",
        "rating": 4.4,
        "description": "Ortadoğu'nun en büyük lunaparklarından biri. Hız trenleri ve aile oyuncakları vardır.",
        "description_en": "One of Middle East's largest amusement parks. Has roller coasters and family rides.",
        "bestTime": "Hafta sonu",
        "tips": "Biletler girişte alınabilir.",
        "tips_en": "Tickets can be bought at gate."
    },
    {
        "name": "Alexandria National Museum",
        "name_en": "Alexandria National Museum",
        "area": "Alexandria",
        "category": "Müze",
        "tags": ["tarih", "müze", "iskenderiye"],
        "lat": 31.2000,
        "lng": 29.9100,
        "price": "medium",
        "rating": 4.6,
        "description": "Güzel bir İtalyan villasında, şehrin tüm tarihini anlatan kompakt ve modern müze.",
        "description_en": "Compact and modern museum in a beautiful Italian villa, telling entire history of city.",
        "bestTime": "Gündüz",
        "tips": "Kronolojik sırayla gezin.",
        "tips_en": "Visit in chronological order."
    },
    {
        "name": "Carpet Schools",
        "name_en": "Saqqara Carpet Schools",
        "area": "Saqqara",
        "category": "Alışveriş",
        "tags": ["halı", "dokuma", "sanat"],
        "lat": 29.8600,
        "lng": 31.2200,
        "price": "high",
        "rating": 4.5,
        "description": "Saqqara yolunda, el dokuması ipek ve yün halıların yapıldığı okullar.",
        "description_en": "Schools on Saqqara road where hand-woven silk and wool carpets are made.",
        "bestTime": "Gündüz",
        "tips": "Pazarlık yapmayı unutmayın.",
        "tips_en": "Don't forget to bargain."
    },
    {
        "name": "Japanese Garden",
        "name_en": "Japanese Garden Helwan",
        "area": "Helwan",
        "category": "Doğa",
        "tags": ["bahçe", "buda", "heykel"],
        "lat": 29.8400,
        "lng": 31.3200,
        "price": "low",
        "rating": 3.9,
        "description": "1917'de kurulan, Asya esintili heykeller ve göletlerle dolu tarihi park.",
        "description_en": "Historic park established in 1917, full of Asian-inspired statues and ponds.",
        "bestTime": "Gündüz",
        "tips": "Fotoğraf çekimi için ilginçtir.",
        "tips_en": "Interesting for photography."
    },
    {
        "name": "Community Services Association",
        "name_en": "CSA Maadi",
        "area": "Maadi",
        "category": "Kültür",
        "tags": ["bahçe", "kafe", "yabancılar"],
        "lat": 29.9550,
        "lng": 31.2650,
        "price": "free",
        "rating": 4.6,
        "description": "Yabancıların (expat) buluşma noktası olan, içinde organik market ve kafe bulunan bahçeli merkez.",
        "description_en": "Expat meeting point, a center with garden containing organic market and cafe.",
        "bestTime": "Sabah",
        "tips": "Kahvaltısı popülerdir.",
        "tips_en": "Breakfast is popular."
    },
    {
        "name": "Osana Family Wellness",
        "name_en": "Osana Family Wellness",
        "area": "Maadi",
        "category": "Sağlık",
        "tags": ["yoga", "kafe", "huzur"],
        "lat": 29.9600,
        "lng": 31.2600,
        "price": "medium",
        "rating": 4.8,
        "description": "Eski bir villada hizmet veren yoga stüdyosu ve sağlıklı yemekler sunan kafe.",
        "description_en": "Yoga studio and cafe serving healthy food in an old villa.",
        "bestTime": "Sabah",
        "tips": "Bahçesi çok huzurludur.",
        "tips_en": "Garden is very peaceful."
    },
    {
        "name": "Craves",
        "name_en": "Crave",
        "area": "Various",
        "category": "Restoran",
        "tags": ["zincir", "modern", "dünya"],
        "lat": 30.0600,
        "lng": 31.2200,
        "price": "medium",
        "rating": 4.5,
        "description": "Kahire'nin en güvenilir ve sevilen modern restoran zinciri. Menüsü çok geniştir.",
        "description_en": "Cairo's most reliable and loved modern restaurant chain. Menu is very extensive.",
        "bestTime": "Akşam",
        "tips": "Çikolatalı fondanı meşhurdur.",
        "tips_en": "Chocolate fondant is famous."
    },
    {
        "name": "Taboula",
        "name_en": "Taboula",
        "area": "Garden City",
        "category": "Restoran",
        "tags": ["lübnan", "meze", "şık"],
        "lat": 30.0380,
        "lng": 31.2330,
        "price": "medium",
        "rating": 4.7,
        "description": "Garden City'de Latin Amerika elçiliği yakınında harika Lübnan yemekleri sunan restoran.",
        "description_en": "Restaurant serving great Lebanese food near Latin American embassy in Garden City.",
        "bestTime": "Akşam",
        "tips": "Mezeleri bir harika.",
        "tips_en": "Appetizers are wonderful."
    },
    {
        "name": "Dahab Island",
        "name_en": "Dahab Island",
        "area": "Nile",
        "category": "Doğa",
        "tags": ["ada", "köy", "tarım"],
        "lat": 30.0000,
        "lng": 31.2200,
        "price": "free",
        "rating": 4.4,
        "description": "Nil'in ortasında, tarım yapan çiftçilerin yaşadığı sakin bir ada. Şehir içinde köy hayatı.",
        "description_en": "Quiet island in middle of Nile where farmers live. Village life inside city.",
        "bestTime": "Gündüz",
        "tips": "Tekneyle geçilir.",
        "tips_en": "Crossed by boat."
    },
    {
        "name": "Nile City Boat",
        "name_en": "Nile City Boat",
        "area": "Zamalek",
        "category": "Eğlence",
        "tags": ["tekne", "restoran", "sinema"],
        "lat": 30.0650,
        "lng": 31.2220,
        "price": "medium",
        "rating": 4.4,
        "description": "İçinde Starbucks, Chili's gibi zincirlerin olduğu popüler tekne kompleksi.",
        "description_en": "Popular boat complex containing chains like Starbucks, Chili's.",
        "bestTime": "Akşam",
        "tips": "Gün batımı kahve keyfi için ideal.",
        "tips_en": "Ideal for sunset coffee."
    },
    {
        "name": "Colossus of Ramses",
        "name_en": "Colossus of Ramses II",
        "area": "Memphis",
        "category": "Tarihi",
        "tags": ["heykel", "ramses", "dev"],
        "lat": 29.8510,
        "lng": 31.2510,
        "price": "included",
        "rating": 4.6,
        "description": "Memphis müzesinin yıldızı, 10 metre uzunluğundaki devasa kireçtaşı heykel.",
        "description_en": "Star of Memphis museum, magnificent 10-meter long limestone statue.",
        "bestTime": "Gündüz",
        "tips": "Detaylı işçiliğine zemin kattan değil balkondan bakın.",
        "tips_en": "View detailed craftsmanship from balcony, not ground floor."
    },
    {
        "name": "Qasr Qarun",
        "name_en": "Qasr Qarun",
        "area": "Fayoum",
        "category": "Tarihi",
        "tags": ["tapınak", "çöl", "karanlık"],
        "lat": 29.4000,
        "lng": 30.4000,
        "price": "low",
        "rating": 4.3,
        "description": "Fayoum'da, labirent gibi odalarıyla ünlü, iyi korunmuş Ptolemaios tapınağı.",
        "description_en": "Well preserved Ptolemaic temple in Fayoum, famous for labyrinth-like rooms.",
        "bestTime": "Gündüz",
        "tips": "İçerisi zifiri karanlıktır, fener gerekir.",
        "tips_en": "Pitch black inside, flashlight needed."
    },
    {
        "name": "Blue Nile Boat",
        "name_en": "Blue Nile Boat",
        "area": "Zamalek",
        "category": "Restoran",
        "tags": ["tekne", "lüks", "asya"],
        "lat": 30.0580,
        "lng": 31.2240,
        "price": "high",
        "rating": 4.5,
        "description": "Asya mutfağı ve şık restoranlarıyla bilinen lüks tekne.",
        "description_en": "Luxury boat known for Asian cuisine and chic restaurants.",
        "bestTime": "Akşam",
        "tips": "Revolving Restoranı vardır.",
        "tips_en": "Has Revolving Restaurant."
    },
    {
        "name": "Supreme Constitutional Court",
        "name_en": "Supreme Constitutional Court of Egypt",
        "area": "Maadi",
        "category": "Mimari",
        "tags": ["modern", "firavun", "mimari"],
        "lat": 29.9800,
        "lng": 31.2400,
        "price": "free",
        "rating": 4.7,
        "description": "Modern firavun tapınağı tarzında inşa edilmiş, Nil kıyısındaki görkemli mahkeme binası.",
        "description_en": "Grand court building on Nile bank built in modern Pharaonic temple style.",
        "bestTime": "Gündüz",
        "tips": "İçine girilmez ama dışarıdan görülmeye değerdir.",
        "tips_en": "Cannot enter inside but worth seeing from outside."
    }
]

def process_city():
    city_name = "kahire"
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
