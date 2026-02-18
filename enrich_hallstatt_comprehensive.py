
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
        find_place_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(place_name)}&inputtype=textquery&fields=place_id,photos,formatted_address,name&key={API_KEY}&locationbias=circle:30000@47.7000,13.6000"
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
        "name": "Basilika St. Michael Mondsee",
        "name_en": "Basilica of St. Michael",
        "area": "Mondsee",
        "category": "Tarihi",
        "tags": ["kilise", "sound of music", "tarih"],
        "lat": 47.8560,
        "lng": 13.3500,
        "price": "free",
        "rating": 4.7,
        "description": "Sound of Music filmindeki düğün sahnesinin çekildiği ünlü barok kilise.",
        "description_en": "Famous baroque church where the wedding scene in The Sound of Music was filmed.",
        "bestTime": "Gündüz",
        "tips": "İçindeki sunak çok etkileyicidir.",
        "tips_en": "The altar inside is very impressive."
    },
    {
        "name": "Drachenwand Klettersteig",
        "name_en": "Dragon Wall Via Ferrata",
        "area": "Mondsee",
        "category": "Aktivite",
        "tags": ["tırmanış", "macera", "manzara"],
        "lat": 47.8100,
        "lng": 13.3500,
        "price": "free",
        "rating": 4.8,
        "description": "Mondsee gölüne bakan, cesaret isteyen ama manzarasıyla büyüleyen tırmanış rotası.",
        "description_en": "Climbing route overlooking Lake Mondsee, daring but fascinating with its view.",
        "bestTime": "Sabah",
        "tips": "Sadece deneyimli tırmanışçılar için.",
        "tips_en": "Only for experienced climbers."
    },
    {
        "name": "Schloss Fuschl",
        "name_en": "Fuschl Castle",
        "area": "Fuschl am See",
        "category": "Tarihi",
        "tags": ["kale", "otel", "göl"],
        "lat": 47.7960,
        "lng": 13.2700,
        "price": "high",
        "rating": 4.6,
        "description": "Fuschlsee kıyısında, masalsı bir yarımada üzerinde duran tarihi kale otel.",
        "description_en": "Historic castle hotel standing on a fairytale peninsula on the shores of Fuschlsee.",
        "bestTime": "Gündüz",
        "tips": "Göl kenarında yürüyüş yapın.",
        "tips_en": "Take a walk by the lake."
    },
    {
        "name": "Fuschlsee Bad",
        "name_en": "Fuschlsee Beach",
        "area": "Fuschl am See",
        "category": "Doğa",
        "tags": ["plaj", "yüzme", "göl"],
        "lat": 47.7950,
        "lng": 13.3000,
        "price": "medium",
        "rating": 4.7,
        "description": "Turkuaz renkli suyuyla ünlü Fuschlsee'de yüzmek için en popüler plaj.",
        "description_en": "Most popular beach for swimming in Fuschlsee, famous for its turquoise water.",
        "bestTime": "Yaz",
        "tips": "Su çok berraktır.",
        "tips_en": "Water is very clear."
    },
    {
        "name": "Red Bull Headquarters",
        "name_en": "Red Bull HQ",
        "area": "Fuschl am See",
        "category": "Mimar",
        "tags": ["modern", "mimari", "ilginç"],
        "lat": 47.7900,
        "lng": 13.2800,
        "price": "free",
        "rating": 4.4,
        "description": "Ünlü boğa heykelleriyle dikkat çeken, fütüristik Red Bull genel merkezi.",
        "description_en": "Futuristic Red Bull headquarters, notable for its famous bull statues.",
        "bestTime": "Gündüz",
        "tips": "İçeri girilmez ama dışarıdan görülmeye değer.",
        "tips_en": "Cannot enter inside but worth seeing from outside."
    },
    {
        "name": "Hinterer Gosausee",
        "name_en": "Lake Gosau (Rear)",
        "area": "Gosau",
        "category": "Doğa",
        "tags": ["göl", "yürüyüş", "sessiz"],
        "lat": 47.5100,
        "lng": 13.5500,
        "price": "free",
        "rating": 4.9,
        "description": "Ön gölden (Vorderer) yaklaşık 1 saatlik yürüyüşle ulaşılan, daha sessiz ve vahşi göl.",
        "description_en": "Quieter and wilder lake reached by a 1-hour walk from the front lake (Vorderer).",
        "bestTime": "Gündüz",
        "tips": "Yolu düz ve kolaydır.",
        "tips_en": "Path is flat and easy."
    },
    {
        "name": "Laserer Alpin Klettersteig",
        "name_en": "Laserer Alpin Via Ferrata",
        "area": "Gosau",
        "category": "Aktivite",
        "tags": ["tırmanış", "göl", "spor"],
        "lat": 47.5300,
        "lng": 13.5000,
        "price": "free",
        "rating": 4.8,
        "description": "Doğrudan Gosausee gölü üzerinde yer alan, manzaralı via ferrata rotası.",
        "description_en": "Scenic via ferrata route located directly over Lake Gosau.",
        "bestTime": "Sabah",
        "tips": "Ekipman kiralayabilirsiniz.",
        "tips_en": "You can rent equipment."
    },
    {
        "name": "Zwieselalm",
        "name_en": "Zwieselalm",
        "area": "Gosau",
        "category": "Doğa",
        "tags": ["yayla", "manzara", "kayak"],
        "lat": 47.5500,
        "lng": 13.4800,
        "price": "medium",
        "rating": 4.7,
        "description": "Kışın kayak, yazın yürüyüş cenneti olan, Dachstein manzaralı yayla.",
        "description_en": "Plateau with Dachstein view, a ski paradise in winter and hiking in summer.",
        "bestTime": "Tüm yıl",
        "tips": "Gosaukammbahn ile çıkılır.",
        "tips_en": "Ascend with Gosaukammbahn."
    },
    {
        "name": "Gablonzer Hütte",
        "name_en": "Gablonzer Hut",
        "area": "Gosau",
        "category": "Restoran",
        "tags": ["dağ evi", "konaklama", "yemek"],
        "lat": 47.5400,
        "lng": 13.4900,
        "price": "medium",
        "rating": 4.6,
        "description": "Zwieselalm'da bulunan, terasından muazzam manzaralar sunan dağ evi.",
        "description_en": "Mountain hut in Zwieselalm offering magnificent views from its terrace.",
        "bestTime": "Öğle",
        "tips": "Gece konaklama imkanı vardır.",
        "tips_en": "Overnight stay available."
    },
    {
        "name": "Urzeitwald Gosau",
        "name_en": "Primeval Forest Park",
        "area": "Gosau",
        "category": "Eğlence",
        "tags": ["çocuk", "dinazor", "park"],
        "lat": 47.5800,
        "lng": 13.5200,
        "price": "medium",
        "rating": 4.5,
        "description": "Çocuklar için dinozorlar ve ilkel çağ temalı eğlence parkı.",
        "description_en": "Amusement park for children themed around dinosaurs and primeval times.",
        "bestTime": "Gündüz",
        "tips": "Aileler için harika bir durak.",
        "tips_en": "Great stop for families."
    },
    {
        "name": "Donnerkogel Klettersteig",
        "name_en": "Donnerkogel Via Ferrata",
        "area": "Gosau",
        "category": "Aktivite",
        "tags": ["tırmanış", "ünlü", "merdiven"],
        "lat": 47.5450,
        "lng": 13.4850,
        "price": "free",
        "rating": 4.9,
        "description": "Meşhur 'Cennete Merdiven'in (Sky Ladder) bulunduğu zorlu tırmanış rotası.",
        "description_en": "Challenging climbing route featuring the famous 'Sky Ladder'.",
        "bestTime": "Sabah",
        "tips": "Sosyal medyada çok popülerdir.",
        "tips_en": "Very popular on social media."
    },
    {
        "name": "Löckernmoos",
        "name_en": "Lockernmoos Bog",
        "area": "Gosau",
        "category": "Doğa",
        "tags": ["doğa", "yürüyüş", "göl"],
        "lat": 47.5600,
        "lng": 13.5100,
        "price": "free",
        "rating": 4.6,
        "description": "Dağların tepesinde, özel bir ekosisteme sahip yüksek turba bataklığı ve gölü.",
        "description_en": "High peat bog and lake with a special ecosystem atop the mountains.",
        "bestTime": "Sabah",
        "tips": "Gün doğumunda çok güzeldir.",
        "tips_en": "Very beautiful at sunrise."
    },
    {
        "name": "Badestrand Obertraun",
        "name_en": "Obertraun Beach",
        "area": "Obertraun",
        "category": "Doğa",
        "tags": ["plaj", "yüzme", "aile"],
        "lat": 47.5500,
        "lng": 13.6700,
        "price": "free",
        "rating": 4.7,
        "description": "Hallstatt gölünün karşı kıyısında, daha sakin ve geniş plaj alanı.",
        "description_en": "Quieter and wider beach area on the opposite shore of Lake Hallstatt.",
        "bestTime": "Yaz",
        "tips": "Hallstatt kalabalığından kaçmak için ideal.",
        "tips_en": "Ideal to escape Hallstatt crowds."
    },
    {
        "name": "Dachstein Hai",
        "name_en": "Dachstein Shark",
        "area": "Obertraun",
        "category": "Sanat",
        "tags": ["heykel", "fotoğraf", "dağ"],
        "lat": 47.5300,
        "lng": 13.6900,
        "price": "free",
        "rating": 4.5,
        "description": "Heilbronn dairesel yolu üzerinde, prehistorik denizi simgeleyen köpekbalığı heykeli.",
        "description_en": "Shark sculpture symbolizing the prehistoric sea on the Heilbronn circular trail.",
        "bestTime": "Gündüz",
        "tips": "İçine girip fotoğraf çekilebilirsiniz.",
        "tips_en": "You can go inside and take photos."
    },
    {
        "name": "Heilbronner Kapelle",
        "name_en": "Heilbronn Chapel",
        "area": "Obertraun",
        "category": "Tarihi",
        "tags": ["şapel", "dağ", "anıt"],
        "lat": 47.5250,
        "lng": 13.6850,
        "price": "free",
        "rating": 4.6,
        "description": "Dachstein platosunda, trajik bir kazayı anmak için yapılmış küçük şapel.",
        "description_en": "Small chapel on the Dachstein plateau built to commemorate a tragic accident.",
        "bestTime": "Gündüz",
        "tips": "Yürüyüşçülerin uğrak noktasıdır.",
        "tips_en": "Frequent stop for hikers."
    },
    {
        "name": "Gjaid Alm",
        "name_en": "Gjaid Alm",
        "area": "Obertraun",
        "category": "Restoran",
        "tags": ["dağ evi", "yemek", "konaklama"],
        "lat": 47.5350,
        "lng": 13.6800,
        "price": "medium",
        "rating": 4.5,
        "description": "Krippenstein istasyonuna yakın, geleneksel yemekler sunan dağ evi.",
        "description_en": "Mountain hut serving traditional food near Krippenstein station.",
        "bestTime": "Öğle",
        "tips": "Kaiserschmarrn tatlısını deneyin.",
        "tips_en": "Try the Kaiserschmarrn dessert."
    },
    {
        "name": "Simonyhütte",
        "name_en": "Simony Hut",
        "area": "Dachstein",
        "category": "Konaklama",
        "tags": ["dağ evi", "buzul", "tırmanış"],
        "lat": 47.5000,
        "lng": 13.6000,
        "price": "medium",
        "rating": 4.8,
        "description": "Dachstein buzulunun hemen altında, yüksek irtifada bulunan tarihi dağ evi.",
        "description_en": "Historic mountain hut located at high altitude just below the Dachstein glacier.",
        "bestTime": "Yaz",
        "tips": "Zirve tırmanışı yapacakların ana kampıdır.",
        "tips_en": "Base camp for those climbing the summit."
    },
    {
        "name": "Rettenbachwildnis",
        "name_en": "Rettenbach Wilderness",
        "area": "Bad Ischl",
        "category": "Doğa",
        "tags": ["vadi", "nehir", "yürüyüş"],
        "lat": 47.6900,
        "lng": 13.6500,
        "price": "free",
        "rating": 4.6,
        "description": "Kayalar ve nehir arasında, vahşi ve romantik bir doğa yürüyüşü alanı.",
        "description_en": "Wild and romantic nature hiking area between rocks and river.",
        "bestTime": "Gündüz",
        "tips": "Fotoğrafçılar için harika ışık sunar.",
        "tips_en": "Offers great light for photographers."
    },
    {
        "name": "Katrin Seilbahn",
        "name_en": "Katrin Cable Car",
        "area": "Bad Ischl",
        "category": "Aktivite",
        "tags": ["teleferik", "manzara", "dağ"],
        "lat": 47.7000,
        "lng": 13.6100,
        "price": "high",
        "rating": 4.7,
        "description": "Bad Ischl'den Katrin dağına çıkan nostaljik teleferik. 7 göl manzarası sunar.",
        "description_en": "Nostalgic cable car from Bad Ischl to Mount Katrin. Offers views of 7 lakes.",
        "bestTime": "Gündüz",
        "tips": "Teleferik 15 dakika sürer.",
        "tips_en": "Cable car takes 15 minutes."
    },
    {
        "name": "Siriuskogel",
        "name_en": "Siriuskogel",
        "area": "Bad Ischl",
        "category": "Manzara",
        "tags": ["kule", "yemek", "manzara"],
        "lat": 47.7080,
        "lng": 13.6200,
        "price": "free",
        "rating": 4.6,
        "description": "Kısa bir yürüyüşle ulaşılan, tepesinde gözlem kulesi ve restoran olan seyir tepesi.",
        "description_en": "Observation hill with a tower and restaurant at the top, reached by a short walk.",
        "bestTime": "Akşamüzeri",
        "tips": "Şefin özel yemeklerini tadın.",
        "tips_en": "Taste the chef's specials."
    },
    {
        "name": "Marmorschlössl",
        "name_en": "Marble Palace",
        "area": "Bad Ischl",
        "category": "Tarihi",
        "tags": ["saray", "sisi", "müze"],
        "lat": 47.7150,
        "lng": 13.6180,
        "price": "medium",
        "rating": 4.4,
        "description": "İmparatoriçe Sisi'nin çay evi olarak kullandığı, Kaiservilla parkındaki mermer köşk.",
        "description_en": "Marble pavilion in Kaiservilla park used by Empress Sisi as a tea house.",
        "bestTime": "Gündüz",
        "tips": "Şu anda fotoğraf müzesidir.",
        "tips_en": "Currently a photography museum."
    },
    {
        "name": "Stadtmuseum Bad Ischl",
        "name_en": "Bad Ischl City Museum",
        "area": "Bad Ischl",
        "category": "Müze",
        "tags": ["tarih", "kültür", "nişan"],
        "lat": 47.7110,
        "lng": 13.6240,
        "price": "medium",
        "rating": 4.3,
        "description": "İmparator Franz Joseph ve Sisi'nin nişanlandığı tarihi bina ve şehir müzesi.",
        "description_en": "Historic building and city museum where Emperor Franz Joseph and Sisi got engaged.",
        "bestTime": "Gündüz",
        "tips": "Tarihi olayların anlatımını dinleyin.",
        "tips_en": "Listen to the narration of historical events."
    },
    {
        "name": "Lehár Villa",
        "name_en": "Lehar Villa",
        "area": "Bad Ischl",
        "category": "Müze",
        "tags": ["müzik", "ev", "tarihi"],
        "lat": 47.7100,
        "lng": 13.6260,
        "price": "medium",
        "rating": 4.5,
        "description": "Ünlü besteci Franz Lehár'ın yaşadığı ve eserlerini bestelediği nehir kıyısındaki villa.",
        "description_en": "Riverside villa where famous composer Franz Lehár lived and composed his works.",
        "bestTime": "Gündüz",
        "tips": "Müzik severler için kutsal bir mekandır.",
        "tips_en": "A sacred place for music lovers."
    },
    {
        "name": "EurothermenResort Bad Ischl",
        "name_en": "Eurothermen Resort",
        "area": "Bad Ischl",
        "category": "Rahatlama",
        "tags": ["termal", "spa", "havuz"],
        "lat": 47.7130,
        "lng": 13.6220,
        "price": "high",
        "rating": 4.5,
        "description": "İmparatorluk döneminden beri kullanılan tuzlu su kaplıcaları ve modern spa.",
        "description_en": "Saltwater thermal springs and modern spa used since the imperial era.",
        "bestTime": "Akşam",
        "tips": "Yorgunluk atmak için birebir.",
        "tips_en": "Perfect for relieving fatigue."
    },
    {
        "name": "Konditorei Zauner",
        "name_en": "Zauner Confectionery",
        "area": "Bad Ischl",
        "category": "Kafe",
        "tags": ["tatlı", "tarihi", "ünlü"],
        "lat": 47.7120,
        "lng": 13.6230,
        "price": "medium",
        "rating": 4.8,
        "description": "1832'den beri hizmet veren, İmparatorluk tedarikçisi unvanlı tarihi pastane.",
        "description_en": "Historic confectionery serving since 1832, holding the title of Imperial Supplier.",
        "bestTime": "Öğleden sonra",
        "tips": "Zaunerstollen tatlısını mutlaka deneyin.",
        "tips_en": "definitely try the Zaunerstollen dessert."
    },
    {
        "name": "Esplanade Bad Ischl",
        "name_en": "Bad Ischl Esplanade",
        "area": "Bad Ischl",
        "category": "Yürüyüş",
        "tags": ["nehir", "yürüyüş", "merkez"],
        "lat": 47.7110,
        "lng": 13.6210,
        "price": "free",
        "rating": 4.6,
        "description": "Traun nehri boyunca uzanan, Sisi'nin de yürüyüş yaptığı zarif kordon boyu.",
        "description_en": "Elegant promenade along the Traun river where Sisi also walked.",
        "bestTime": "Akşamüzeri",
        "tips": "Pazar günleri konserler olur.",
        "tips_en": "Concerts take place on Sundays."
    },
    {
        "name": "Trinkhalle Bad Ischl",
        "name_en": "Pump Room",
        "area": "Bad Ischl",
        "category": "Tarihi",
        "tags": ["mimari", "etkinlik", "merkez"],
        "lat": 47.7125,
        "lng": 13.6200,
        "price": "free",
        "rating": 4.4,
        "description": "Eskiden şifalı suların içildiği, şimdi sergi ve etkinlik alanı olan görkemli bina.",
        "description_en": "Grand building formerly used for drinking healing waters, now an exhibition and event space.",
        "bestTime": "Gündüz",
        "tips": "Turizm ofisi buradadır.",
        "tips_en": "Tourism office is here."
    },
    {
        "name": "Schloss Ort",
        "name_en": "Ort Castle",
        "area": "Gmunden",
        "category": "Tarihi",
        "tags": ["kale", "göl", "ikonik"],
        "lat": 47.9100,
        "lng": 13.7900,
        "price": "medium",
        "rating": 4.7,
        "description": "Traunsee gölü üzerindeki bir adada bulunan, köprüyle karaya bağlanan masalsı kale.",
        "description_en": "Fairytale castle on an island in Lake Traunsee, connected to land by a bridge.",
        "bestTime": "Gün batımı",
        "tips": "Düğünlerin popüler mekanıdır.",
        "tips_en": "Popular venue for weddings."
    },
    {
        "name": "Gmundner Keramik Manufaktur",
        "name_en": "Gmundner Ceramics Manufactory",
        "area": "Gmunden",
        "category": "Alışveriş",
        "tags": ["seramik", "sanat", "hediyelik"],
        "lat": 47.9200,
        "lng": 13.7800,
        "price": "free",
        "rating": 4.6,
        "description": "Avusturya'nın meşhur yeşil çizgili seramiklerinin üretildiği tarihi fabrika.",
        "description_en": "Historic factory where Austria's famous green-striped ceramics are produced.",
        "bestTime": "Gündüz",
        "tips": "Fabrika turuna katılabilirsiniz.",
        "tips_en": "You can join a factory tour."
    },
    {
        "name": "Grünberg Seilbahn",
        "name_en": "Grunberg Cable Car",
        "area": "Gmunden",
        "category": "Aktivite",
        "tags": ["teleferik", "manzara", "dağ"],
        "lat": 47.9150,
        "lng": 13.8000,
        "price": "high",
        "rating": 4.5,
        "description": "Gmunden'den Grünberg dağına çıkan teleferik.",
        "description_en": "Cable car from Gmunden to Grünberg mountain.",
        "bestTime": "Gündüz",
        "tips": "Treetop walk'a buradan gidilir.",
        "tips_en": "Access to treetop walk is from here."
    },
    {
        "name": "Baumwipfelpfad Salzkammergut",
        "name_en": "Treetop Walk Salzkammergut",
        "area": "Gmunden",
        "category": "Aktivite",
        "tags": ["yürüyüş", "kule", "manzara"],
        "lat": 47.9160,
        "lng": 13.8050,
        "price": "medium",
        "rating": 4.8,
        "description": "Ağaçların tepesinde yürüyüş yolu ve devasa bir gözlem kulesi.",
        "description_en": "Walkway among treetops and a massive observation tower.",
        "bestTime": "Gündüz",
        "tips": "Kuledeki kaydıraktan kayabilirsiniz.",
        "tips_en": "You can slide down from the tower."
    },
    {
        "name": "Traunstein",
        "name_en": "Traunstein Mountain",
        "area": "Gmunden",
        "category": "Doğa",
        "tags": ["dağ", "ikonik", "zorlu"],
        "lat": 47.8700,
        "lng": 13.8400,
        "price": "free",
        "rating": 4.9,
        "description": "Gölün koruyucusu olarak bilinen, piramit şeklindeki heybetli dağ.",
        "description_en": "Imposing pyramid-shaped mountain known as the guardian of the lake.",
        "bestTime": "Sabah",
        "tips": "Tırmanışı zordur, hazırlıklı olun.",
        "tips_en": "Climbing is difficult, be prepared."
    },
    {
        "name": "Miesweg",
        "name_en": "Miesweg Trail",
        "area": "Gmunden",
        "category": "Doğa",
        "tags": ["yürüyüş", "göl", "macera"],
        "lat": 47.8800,
        "lng": 13.8300,
        "price": "free",
        "rating": 4.7,
        "description": "Traunstein dağlarının eteklerinde, gölün hemen üzerindeki kayalık patika.",
        "description_en": "Rocky trail just above the lake at the foot of Traunstein mountains.",
        "bestTime": "Gündüz",
        "tips": "Dar geçitler ve harika manzaralar vardır.",
        "tips_en": "There are narrow passages and great views."
    },
    {
        "name": "Toscanapark",
        "name_en": "Toscana Park",
        "area": "Gmunden",
        "category": "Doğa",
        "tags": ["park", "yürüyüş", "göl"],
        "lat": 47.9050,
        "lng": 13.7950,
        "price": "free",
        "rating": 4.6,
        "description": "Ort kalesinin yakınında, göl kenarında geniş ve huzurlu bir park.",
        "description_en": "Large and peaceful park by the lake near Ort castle.",
        "bestTime": "Gündüz",
        "tips": "Piknik için idealdir.",
        "tips_en": "Ideal for a picnic."
    },
    {
        "name": "Langbathseen",
        "name_en": "Langbath Lakes",
        "area": "Ebensee",
        "category": "Doğa",
        "tags": ["göl", "yürüyüş", "yüzme"],
        "lat": 47.8300,
        "lng": 13.6800,
        "price": "free",
        "rating": 4.8,
        "description": "Dağların arasında gizlenmiş iki harika göl. Ön gölde yüzülebilir.",
        "description_en": "Two wonderful lakes hidden among mountains. Swimming is allowed in the front lake.",
        "bestTime": "Yaz",
        "tips": "İki gölün etrafını yürümek 2 saat sürer.",
        "tips_en": "Walking around both lakes takes 2 hours."
    },
    {
        "name": "Feuerkogel Seilbahn",
        "name_en": "Feuerkogel Cable Car",
        "area": "Ebensee",
        "category": "Aktivite",
        "tags": ["teleferik", "manzara", "kayak"],
        "lat": 47.8100,
        "lng": 13.7200,
        "price": "high",
        "rating": 4.6,
        "description": "Ebensee'den güneşli plato Feuerkogel'e çıkan teleferik.",
        "description_en": "Cable car from Ebensee to the sunny plateau Feuerkogel.",
        "bestTime": "Gündüz",
        "tips": "Yukarıda birçok yürüyüş rotası vardır.",
        "tips_en": "There are many hiking routes at the top."
    },
    {
        "name": "Rindbach Wasserfall",
        "name_en": "Rindbach Waterfall",
        "area": "Ebensee",
        "category": "Doğa",
        "tags": ["şelale", "doğa", "yürüyüş"],
        "lat": 47.8000,
        "lng": 13.7500,
        "price": "free",
        "rating": 4.5,
        "description": "Ebensee yakınlarında güzel bir şelale ve kanyon yürüyüşü.",
        "description_en": "Beautiful waterfall and canyon walk near Ebensee.",
        "bestTime": "Gündüz",
        "tips": "Mağara turuyla birleştirilebilir.",
        "tips_en": "Can be combined with cave tour."
    },
    {
        "name": "Offensee",
        "name_en": "Lake Offensee",
        "area": "Ebensee",
        "category": "Doğa",
        "tags": ["göl", "yüzme", "sakin"],
        "lat": 47.7600,
        "lng": 13.8300,
        "price": "free",
        "rating": 4.7,
        "description": "Tote Gebirge dağlarının eteğinde, sakin ve huzurlu bir yüzme gölü.",
        "description_en": "Calm and peaceful swimming lake at the foot of Tote Gebirge mountains.",
        "bestTime": "Yaz",
        "tips": "Kışın tamamen donar ve üzerinde yürünebilir.",
        "tips_en": "Completely freezes in winter and can be walked on."
    },
    {
        "name": "KZ-Gedenkstätte Ebensee",
        "name_en": "Ebensee Concentration Camp Memorial",
        "area": "Ebensee",
        "category": "Tarihi",
        "tags": ["tarih", "anıt", "savaş"],
        "lat": 47.7900,
        "lng": 13.7600,
        "price": "free",
        "rating": 4.6,
        "description": "II. Dünya Savaşı tarihine tanıklık eden, hüzünlü ve etkileyici anıt alanı.",
        "description_en": "Sorrowful and impressive memorial site witnessing WWII history.",
        "bestTime": "Gündüz",
        "tips": "Büyük mağara tünelleri ziyaret edilebilir.",
        "tips_en": "Large cave tunnels can be visited."
    },
    {
        "name": "Almsee",
        "name_en": "Lake Almsee",
        "area": "Grünau",
        "category": "Doğa",
        "tags": ["göl", "doğa", "koruma"],
        "lat": 47.7500,
        "lng": 13.9500,
        "price": "free",
        "rating": 4.8,
        "description": "Doğa koruma alanı içinde, kristal berraklığında bir dağ gölü.",
        "description_en": "Crystal clear mountain lake within a nature reserve.",
        "bestTime": "Gündüz",
        "tips": "Konrad Lorenz araştırmalarını burada yapmıştır.",
        "tips_en": "Konrad Lorenz conducted his research here."
    },
    {
        "name": "Cumberland Wildpark",
        "name_en": "Cumberland Wildlife Park",
        "area": "Grünau",
        "category": "Doğa",
        "tags": ["hayvanlar", "park", "aile"],
        "lat": 47.8000,
        "lng": 13.9400,
        "price": "medium",
        "rating": 4.7,
        "description": "Yerel vahşi hayvanların doğal ortamlarında görülebileceği devasa park.",
        "description_en": "Huge park where local wild animals can be seen in their natural habitats.",
        "bestTime": "Gündüz",
        "tips": "Yürüyüş parkuru uzundur, rahat ayakkabı giyin.",
        "tips_en": "Walking trail is long, wear comfortable shoes."
    },
    {
        "name": "Laudachsee",
        "name_en": "Lake Laudach",
        "area": "Gmunden",
        "category": "Doğa",
        "tags": ["göl", "yürüyüş", "dağ"],
        "lat": 47.8900,
        "lng": 13.8500,
        "price": "free",
        "rating": 4.6,
        "description": "Grünberg teleferiğinden kısa bir yürüyüşle ulaşılan saklı göl.",
        "description_en": "Hidden lake reached by a short walk from Grünberg cable car.",
        "bestTime": "Gündüz",
        "tips": "Göl kenarında restoran vardır.",
        "tips_en": "There is a restaurant by the lake."
    },
    {
        "name": "Traunsee Schifffahrt",
        "name_en": "Traunsee Boat Tour",
        "area": "Gmunden",
        "category": "Aktivite",
        "tags": ["tekne", "tur", "göl"],
        "lat": 47.9150,
        "lng": 13.7900,
        "price": "medium",
        "rating": 4.5,
        "description": "Avusturya'nın en derin gölünde tarihi buharlı gemiyle gezi.",
        "description_en": "Trip on a historic steamship on Austria's deepest lake.",
        "bestTime": "Yaz",
        "tips": "Gisela gemisi dünyanın en eskilerindendir.",
        "tips_en": "Ship Gisela is one of the oldest in the world."
    },
    {
        "name": "Kalvarienberg Bad Ischl",
        "name_en": "Calvary Hill",
        "area": "Bad Ischl",
        "category": "Tarihi",
        "tags": ["kilise", "yürüyüş", "manzara"],
        "lat": 47.7120,
        "lng": 13.6150,
        "price": "free",
        "rating": 4.4,
        "description": "Şapel ve istasyonlarıyla ünlü, şehir manzaralı kutsal tepe.",
        "description_en": "Sacred hill with city views, famous for its chapel and stations.",
        "bestTime": "Gündüz",
        "tips": "Kısa ama dik bir yürüyüştür.",
        "tips_en": "Short but steep walk."
    },
    {
        "name": "Sophien Doppelblick",
        "name_en": "Sophies View",
        "area": "Bad Ischl",
        "category": "Manzara",
        "tags": ["manzara", "yürüyüş", "sisi"],
        "lat": 47.7180,
        "lng": 13.6280,
        "price": "free",
        "rating": 4.5,
        "description": "İmparatoriçe Sisi'nin annesi Sophie'nin sevdiği manzara noktası.",
        "description_en": "Viewpoint loved by Empress Sisi's mother Sophie.",
        "bestTime": "Gündüz",
        "tips": "Şehrin en iyi kuşbakışı manzaralarından biri.",
        "tips_en": "One of the best bird's eye views of the city."
    },
    {
        "name": "Egelsee",
        "name_en": "Lake Egel",
        "area": "Scharfling",
        "category": "Doğa",
        "tags": ["göl", "küçük", "sakin"],
        "lat": 47.8000,
        "lng": 13.4000,
        "price": "free",
        "rating": 4.3,
        "description": "Ay gibi şekliyle bilinen, orman içindeki küçük bataklık gölü.",
        "description_en": "Small bog lake in the forest, known for its moon-like shape.",
        "bestTime": "Gündüz",
        "tips": "Sadece yürüyerek ulaşılır.",
        "tips_en": "Only accessible by walking."
    },
    {
        "name": "Sonnstein",
        "name_en": "Sonnstein Mountain",
        "area": "Traunkirchen",
        "category": "Doğa",
        "tags": ["dağ", "manzara", "tırmanış"],
        "lat": 47.8500,
        "lng": 13.7800,
        "price": "free",
        "rating": 4.7,
        "description": "Traunsee gölünün muhteşem manzarasına hakim zirve.",
        "description_en": "Summit dominating the magnificent view of Lake Traunsee.",
        "bestTime": "Sabah",
        "tips": "Kleiner Sonnstein daha popülerdir.",
        "tips_en": "Kleiner Sonnstein is more popular."
    },
    {
        "name": "Johannesbergkapelle",
        "name_en": "Johannesberg Chapel",
        "area": "Traunkirchen",
        "category": "Tarihi",
        "tags": ["şapel", "manzara", "tarih"],
        "lat": 47.8450,
        "lng": 13.7900,
        "price": "free",
        "rating": 4.6,
        "description": "Küçük bir tepe üzerindeki pitoresk şapel. Kartpostallık manzaralar sunar.",
        "description_en": "Picturesque chapel on a small hill. Offers postcard views.",
        "bestTime": "Gündüz",
        "tips": "Merdivenle çıkılır.",
        "tips_en": "Accessible by stairs."
    },
    {
        "name": "Spitzvilla",
        "name_en": "Spitz Villa",
        "area": "Traunkirchen",
        "category": "Kafe",
        "tags": ["tarihi", "manzara", "kafe"],
        "lat": 47.8400,
        "lng": 13.7950,
        "price": "medium",
        "rating": 4.5,
        "description": "Göl kenarında, tarihi bir villada hizmet veren şık kafe ve restoran.",
        "description_en": "Stylish cafe and restaurant serving in a historic villa by the lake.",
        "bestTime": "Öğleden sonra",
        "tips": "Bahçesi göl kenarındadır.",
        "tips_en": "Its garden is by the lake."
    },
    {
        "name": "Fischerkanzel",
        "name_en": "Fishermans Pulpit",
        "area": "Traunkirchen",
        "category": "Tarihi",
        "tags": ["kilise", "sanat", "ilginç"],
        "lat": 47.8460,
        "lng": 13.7920,
        "price": "free",
        "rating": 4.7,
        "description": "Bölge kilisesinde bulunan, balıkçı teknesi şeklindeki eşsiz vaiz kürsüsü.",
        "description_en": "Unique pulpit in the shape of a fishing boat located in the parish church.",
        "bestTime": "Gündüz",
        "tips": "Mucizevi balık avını simgeler.",
        "tips_en": "Symbolizes the miraculous catch of fish."
    }
]

def process_city():
    city_name = "hallstatt"
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
