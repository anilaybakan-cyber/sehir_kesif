
import json
import requests
import time
import urllib.parse
import os

# Google Places API Key
API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name, location_bias=None):
    """
    Fetches a photo URL for a place using Google Places API.
    """
    try:
        # 1. Find Place ID
        find_place_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(place_name)}&inputtype=textquery&fields=place_id,photos,formatted_address,name&key={API_KEY}"
        
        # If we have location bias, add it
        if location_bias:
             find_place_url += f"&locationbias=circle:5000@{location_bias['lat']},{location_bias['lng']}"
        else:
             # Default bias to Gaziantep coordinates if not provided
             find_place_url += "&locationbias=circle:15000@37.0662,37.3833"

        print(f"Fetching photo for: {place_name}...")
        response = requests.get(find_place_url)
        data = response.json()

        if data['status'] == 'OK' and len(data['candidates']) > 0:
            candidate = data['candidates'][0]
            if 'photos' in candidate:
                photo_reference = candidate['photos'][0]['photo_reference']
                # 2. Get Photo URL
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={API_KEY}"
                print(f"  Found photo for: {place_name}")
                return photo_url
            else:
                print(f"  No photos found for: {place_name}")
                return None
        else:
            print(f"  Place not found: {place_name} (Status: {data['status']})")
            return None

    except Exception as e:
        print(f"  Error fetching photo for {place_name}: {e}")
        return None

# --- BATCH 1: UNESCO GASTRONOMY ICONS (KEBAB & BAKLAVA) ---
new_gaziantep_places_1 = [
    {
        "name": "Küşlemeci Halil Usta",
        "name_en": "Kuslemeci Halil Usta",
        "area": "Şehitkamil",
        "category": "Restoran",
        "tags": ["kebap", "küşleme", "efsane", "yerel"],
        "distanceFromCenter": 1.2,
        "lat": 37.0755,
        "lng": 37.3855,
        "price": "medium",
        "rating": 4.9,
        "description": "Gaziantep'te kebap denince akla gelen ilk durak. Lokum gibi küşlemesi ve bakır kaselerde sunduğu ayranıyla bir efsane.",
        "description_en": "The first stop that comes to mind for kebab in Gaziantep. A legend with its delight-like 'küşleme' (lamb tenderloin) and ayran served in copper bowls.",
        "bestTime": "Öğle",
        "bestTime_en": "Lunch",
        "tips": "Öğleden sonra giderseniz et kalmamış olabilir, 12:00-13:00 arası ideal.",
        "tips_en": "If you go in the afternoon meat might be finished, 12:00-13:00 is ideal."
    },
    {
        "name": "İmam Çağdaş",
        "name_en": "Imam Cagdas",
        "area": "Şahinbey",
        "category": "Restoran",
        "tags": ["kebap", "baklava", "tarihi", "turistik"],
        "distanceFromCenter": 0.3,
        "lat": 37.0620,
        "lng": 37.3810,
        "price": "high",
        "rating": 4.7,
        "description": "Hem kebabı (Ali Nazik) hem de baklavasıyla ünlü, şehrin en köklü ve şık restoranlarından biri.",
        "description_en": "One of the city's most established and stylish restaurants, famous for both its kebab (Ali Nazik) and baklava.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Ali Nazik kebabını burada denemelisiniz, baklavası da havuc dilimi olarak harikadır.",
        "tips_en": "You must try Ali Nazik kebab here, their carrot slice baklava is also great."
    },
    {
        "name": "Koçak Baklava",
        "name_en": "Kocak Baklava",
        "area": "Şehitkamil",
        "category": "Tatlı",
        "tags": ["baklava", "fıstık", "hediyelik", "ünlü"],
        "distanceFromCenter": 2.0,
        "lat": 37.0730,
        "lng": 37.3750,
        "price": "high",
        "rating": 4.9,
        "description": "Birçoklarına göre Gaziantep'in en iyi baklavacısı. Bol fıstıklı, çıtır çıtır ve tam kıvamında şerbetiyle unutulmaz.",
        "description_en": "According to many, the best baklava shop in Gaziantep. Unforgettable with plenty of pistachios, crispy texture and perfectly balanced syrup.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Sıcak baklava saati genellikle öğleden sonradır, hediyelik paket yaptırabilirsiniz.",
        "tips_en": "Hot baklava time is usually in the afternoon, you can get gift packages made."
    },
    {
        "name": "Katmerci Zekeriya Usta",
        "name_en": "Katmerci Zekeriya Usta",
        "area": "Şahinbey",
        "category": "Tatlı",
        "tags": ["katmer", "kahvaltı", "tarihi", "küçük"],
        "distanceFromCenter": 0.4,
        "lat": 37.0615,
        "lng": 37.3820,
        "price": "medium",
        "rating": 4.8,
        "description": "Gaziantep kahvaltısının vazgeçilmezi katmeri en geleneksel haliyle yapan, salaş ve samimi bir dükkan.",
        "description_en": "A casual and friendly shop making katmer, the indispensable item of Gaziantep breakfast, in its most traditional form.",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Katmer ağır bir tatlıdır, kişi başı 1 porsiyon fazla gelebilir, paylaşın.",
        "tips_en": "Katmer is a heavy dessert, 1 portion per person might be too much, share it."
    },
    {
        "name": "Çulcuoğlu Baklava",
        "name_en": "Culcuoglu Baklava",
        "area": "Şahinbey",
        "category": "Tatlı",
        "tags": ["baklava", "özel kare", "aile", "lezzet"],
        "distanceFromCenter": 0.8,
        "lat": 37.0600,
        "lng": 37.3780,
        "price": "medium",
        "rating": 4.8,
        "description": "Yerel halkın çok sevdiği, özellikle 'Özel Kare' baklavasıyla meşhur bir aile işletmesi.",
        "description_en": "A family business loved by locals, especially famous for its 'Special Square' baklava.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Şöbiyet tatlısını da denemenizi öneririm.",
        "tips_en": "I recommend trying the Sobiyet dessert as well."
    },
    {
        "name": "Kebapçı Ömer",
        "name_en": "Kebapci Omer",
        "area": "Şehitkamil",
        "category": "Restoran",
        "tags": ["kebap", "salaş", "lezzet", "yerel"],
        "distanceFromCenter": 1.5,
        "lat": 37.0700,
        "lng": 37.3900,
        "price": "medium",
        "rating": 4.6,
        "description": "Turistik olmayan, gerçek Gaziantep esnafının gittiği, lezzetiyle şaşırtan salaş bir kebapçı.",
        "description_en": "A casual kebab shop that is not touristic, visited by real Gaziantep tradesmen, surprising with its flavor.",
        "bestTime": "Öğle",
        "bestTime_en": "Lunch",
        "tips": "Kıyma kebabı (Adana değil, Antep usulü) çok başarılıdır.",
        "tips_en": "Minced meat kebab (Antep style, not Adana) is very successful."
    },
    {
        "name": "Ayıntap Baklava",
        "name_en": "Ayintap Baklava",
        "area": "Şehitkamil",
        "category": "Tatlı",
        "tags": ["baklava", "modern", "çeşit", "taze"],
        "distanceFromCenter": 2.5,
        "lat": 37.0780,
        "lng": 37.3720,
        "price": "medium",
        "rating": 4.7,
        "description": "Son yıllarda yıldızı parlayan, hafif ve çıtır baklavalarıyla dikkat çeken modern bir baklavacı.",
        "description_en": "A modern baklava shop whose star has risen in recent years, notable for its light and crispy baklavas.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Midye baklavası görsel şölen sunar.",
        "tips_en": "Mussel baklava offers a visual feast."
    },
    {
        "name": "Aşina Gaziantep Mutfağı",
        "name_en": "Asina Gaziantep Cuisine",
        "area": "Şehitkamil",
        "category": "Restoran",
        "tags": ["yöresel", "yuvalama", "aile", "yemek"],
        "distanceFromCenter": 1.8,
        "lat": 37.0720,
        "lng": 37.3680,
        "price": "medium",
        "rating": 4.5,
        "description": "Sadece kebap değil, Antep'in sulu tencere yemeklerini (Yuvalama, Ekşili Ufak Köfte) de bulabileceğiniz geniş menülü restoran.",
        "description_en": "Restaurant with a wide menu where you can find not only kebabs but also Antep's stew dishes (Yuvalama, Sour Small Meatballs).",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Yuvalama çorbası ana yemek kadar doyurucudur.",
        "tips_en": "Yuvalama soup is as filling as a main course."
    }
]

# --- BATCH 2: STREET FOOD LEGENDS (NOHUT, CİĞER, BEYRAN) ---
new_gaziantep_places_2 = [
    {
        "name": "Metanet Lokantası",
        "name_en": "Metanet Restaurant",
        "area": "Şahinbey",
        "category": "Restoran",
        "tags": ["beyran", "çorba", "kahvaltı", "acı"],
        "distanceFromCenter": 0.3,
        "lat": 37.0630,
        "lng": 37.3825,
        "price": "medium",
        "rating": 4.8,
        "description": "Gaziantep'te güne başlamanın en 'sert' yolu: Beyran çorbası. Sabahın erken saatlerinde dolup taşan efsane mekan.",
        "description_en": "The 'hardest' way to start the day in Gaziantep: Beyran soup. Legendary place overflowing in the early hours of the morning.",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Sabah 05:00-09:00 arası gitmek bir ritüeldir, sarımsağı boldur.",
        "tips_en": "Going between 05:00-09:00 is a ritual, it has plenty of garlic."
    },
    {
        "name": "Ciğerci Ali Haydar Usta",
        "name_en": "Cigerci Ali Haydar",
        "area": "Şahinbey",
        "category": "Sokak Lezzeti",
        "tags": ["ciğer", "kahvaltı", "şiş", "salaş"],
        "distanceFromCenter": 0.5,
        "lat": 37.0605,
        "lng": 37.3800,
        "price": "low",
        "rating": 4.8,
        "description": "Sabah kahvaltısında ciğer yemek Antep geleneğidir. Ali Haydar Usta bu işin piri, ciğerleri lokum gibi.",
        "description_en": "Eating liver for breakfast is an Antep tradition. Ali Haydar Usta is the master of this, his liver is like Turkish delight.",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Saat 08:30 dedin mi ciğer biter, çok erken gitmelisiniz.",
        "tips_en": "Liver runs out by 08:30, you must go very early."
    },
    {
        "name": "Dürümcü Recep Usta",
        "name_en": "Durumcu Recep Usta",
        "area": "Şahinbey",
        "category": "Sokak Lezzeti",
        "tags": ["nohut dürüm", "vejetaryen", "ekonomik", "hızlı"],
        "distanceFromCenter": 0.6,
        "lat": 37.0590,
        "lng": 37.3790,
        "price": "cheap",
        "rating": 4.7,
        "description": "Gaziantep'in meşhur nohut dürümü. Tırnaklı pide içinde kemik suyunda pişmiş nohut, patates ve baharatlar.",
        "description_en": "Gaziantep's famous chickpea wrap. Chickpeas cooked in bone broth, potatoes and spices inside fingernail pita.",
        "bestTime": "Öğle",
        "bestTime_en": "Lunch",
        "tips": "Acısı boldur, 'az acılı' isterseniz belirtin.",
        "tips_en": "It's very spicy, specify if you want 'less spicy'."
    },
    {
        "name": "Löküs Ciğer",
        "name_en": "Lokus Ciger",
        "area": "Şehitkamil",
        "category": "Restoran",
        "tags": ["ciğer", "gece", "lezzet", "kömür"],
        "distanceFromCenter": 1.0,
        "lat": 37.0680,
        "lng": 37.3750,
        "price": "medium",
        "rating": 4.6,
        "description": "Gece acıkanların uğrak noktası. Kömür ateşinde pişen ciğer şişleri ve yanındaki mezeleriyle meşhur.",
        "description_en": "Stopover for those hungry at night. Famous for its charcoal-grilled liver skewers and accompanying appetizers.",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Soğan salatası ciğerin en iyi eşlikçisidir.",
        "tips_en": "Onion salad is the best companion for liver."
    },
    {
        "name": "Kelebek Lahmacun",
        "name_en": "Kelebek Lahmacun",
        "area": "Şehitkamil",
        "category": "Restoran",
        "tags": ["lahmacun", "çıtır", "sarımsaklı", "hızlı"],
        "distanceFromCenter": 1.5,
        "lat": 37.0710,
        "lng": 37.3700,
        "price": "medium",
        "rating": 4.7,
        "description": "Antep usulü sarmısaklı lahmacunu en iyi yapan yerlerden. İncecik hamuru ve bol malzemesiyle bağımlılık yapar.",
        "description_en": "One of the best places making Antep style garlic lahmacun. Addictive with its thin dough and plentiful toppings.",
        "bestTime": "Öğle",
        "bestTime_en": "Lunch",
        "tips": "Yanına buz gibi bir ayran söylemeyi unutmayın.",
        "tips_en": "Don't forget to order an ice-cold ayran with it."
    },
    {
        "name": "Tostçu Erol",
        "name_en": "Tostcu Erol",
        "area": "Şahinbey",
        "category": "Sokak Lezzeti",
        "tags": ["tost", "sosyal medya", "fenomen", "atom"],
        "distanceFromCenter": 2.5,
        "lat": 37.0550,
        "lng": 37.3650,
        "price": "low",
        "rating": 4.3,
        "description": "Sosyal medya fenomeni haline gelen, 'Atom' tostuyla ünlü, bol malzemeli ve eğlenceli tostçu.",
        "description_en": "Fun toast shop famous for its 'Atom' toast, which became a social media phenomenon, with plentiful ingredients.",
        "bestTime": "Öğle",
        "bestTime_en": "Lunch",
        "tips": "Sıra beklemeyi göze alın, internette meşhur olduğu için kalabalıktır.",
        "tips_en": "Be prepared to wait in line, it is crowded because it is famous on the internet."
    },
    {
        "name": "Mutfak Sanatları Merkezi (MSM)",
        "name_en": "Culinary Arts Center",
        "area": "Şahinbey",
        "category": "Restoran",
        "tags": ["gastronomi", "yöresel", "modern sunum", "unesco"],
        "distanceFromCenter": 0.5,
        "lat": 37.0650,
        "lng": 37.3840,
        "price": "medium",
        "rating": 4.8,
        "description": "Gaziantep Belediyesi bünyesinde, unutulmaya yüz tutmuş yöresel yemekleri orijinal tarifleriyle sunan, lezzet garantili mekan.",
        "description_en": "Taste-guaranteed venue run by Gaziantep Municipality, serving forgotten regional dishes with original recipes.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Firik pilavı ve ayvalı taraklık gibi özel yemekleri deneyin.",
        "tips_en": "Try special dishes like Firik pilaf and quince taraklik."
    },
    {
        "name": "Sakıp Usta",
        "name_en": "Sakip Usta",
        "area": "Şehitkamil",
        "category": "Restoran",
        "tags": ["beyran", "paça", "gece", "çorba"],
        "distanceFromCenter": 1.2,
        "lat": 37.0740,
        "lng": 37.3780,
        "price": "medium",
        "rating": 4.5,
        "description": "Zengin menüsü ve özellikle paça çorbasıyla bilinen, günün her saati işlek popüler lokanta.",
        "description_en": "Popular restaurant busy at all hours of the day, known for its rich menu and especially trotter soup.",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Kemik suyu çorbaları çok şifalıdır.",
        "tips_en": "Bone broth soups are very healing."
    }
]

# --- BATCH 3: HISTORIC COFFEE & CULTURE ---
new_gaziantep_places_3 = [
    {
        "name": "Tahmis Kahvesi",
        "name_en": "Tahmis Coffee",
        "area": "Şahinbey",
        "category": "Kafe",
        "tags": ["kahve", "tarihi", "menengiç", "1635"],
        "distanceFromCenter": 0.3,
        "lat": 37.0620,
        "lng": 37.3815,
        "price": "medium",
        "rating": 4.8,
        "description": "1635'ten beri ayakta olan, Türkiye'nin en eski kahvehanelerinden. Menengiç kahvesi içmek ve tarihi atmosferi solumak için eşsiz.",
        "description_en": "One of Turkey's oldest coffeehouses, standing since 1635. Unique for drinking Menengiç coffee and breathing the historic atmosphere.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kahvenin yanında gelen çerezler (menengiç tohumu) çok lezzetlidir.",
        "tips_en": "The snacks (menengiç seeds) served with coffee are very delicious."
    },
    {
        "name": "Kır Kahvesi (Gaziantep Kalesi)",
        "name_en": "Kir Kahvesi",
        "area": "Şahinbey",
        "category": "Kafe",
        "tags": ["manzara", "kale", "çay", "dinlenme"],
        "distanceFromCenter": 0.2,
        "lat": 37.0650,
        "lng": 37.3830,
        "price": "medium",
        "rating": 4.4,
        "description": "Gaziantep Kalesi'nin eteklerinde, şehre tepeden bakarken yorgunluk çayı içebileceğiniz keyifli bahçe.",
        "description_en": "Pleasant garden at the foot of Gaziantep Castle where you can drink fatigue tea while overlooking the city.",
        "bestTime": "İkindi",
        "bestTime_en": "Afternoon",
        "tips": "Gün batımına yakın saatlerde kale manzarası çok güzeldir.",
        "tips_en": "Castle view is very beautiful close to sunset."
    },
    {
        "name": "Gümrük Hanı",
        "name_en": "Gumruk Han",
        "area": "Şahinbey",
        "category": "Tarihi",
        "tags": ["han", "kahve", "dibek", "el sanatı"],
        "distanceFromCenter": 0.3,
        "lat": 37.0625,
        "lng": 37.3820,
        "price": "medium",
        "rating": 4.7,
        "description": "\"Yaşayan Müze\" olarak bilinen tarihi han. Avlusunda Dibek kahvesi (çift renkli) içebilir, üst kattaki gümüşçüleri gezebilirsiniz.",
        "description_en": "Historic inn known as 'Living Museum'. You can drink Dibek coffee (bi-color) in its courtyard and visit the silversmiths upstairs.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Çift renkli (sütlü ve sade) Osmanlı kahvesi sunumu çok ilginçtir.",
        "tips_en": "The presentation of bi-color (milky and plain) Ottoman coffee is very interesting."
    },
    {
        "name": "Tütün Hanı",
        "name_en": "Tutun Hani",
        "area": "Şahinbey",
        "category": "Kafe",
        "tags": ["han", "mağara", "tarihi", "nargile"],
        "distanceFromCenter": 0.4,
        "lat": 37.0610,
        "lng": 37.3800,
        "price": "medium",
        "rating": 4.5,
        "description": "Eşsiz mağara bölümleri olan tarihi bir han. Yazın serin, kışın sıcak atmosferiyle bilinir.",
        "description_en": "A historic inn with unique cave sections. Known for its cool atmosphere in summer and warm in winter.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Mağara odalarında oturmak farklı bir deneyimdir.",
        "tips_en": "Sitting in cave rooms is a different experience."
    },
    {
        "name": "Bayazhan",
        "name_en": "Bayazhan",
        "area": "Şehitkamil",
        "category": "Restoran",
        "tags": ["han", "müze", "şık", "akşam yemeği"],
        "distanceFromCenter": 0.8,
        "lat": 37.0680,
        "lng": 37.3700,
        "price": "high",
        "rating": 4.6,
        "description": "Restore edilmiş görkemli bir han binasında hizmet veren müze, restoran ve pub kompleksi.",
        "description_en": "Museum, restaurant and pub complex serving in a restored magnificent inn building.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Akşam yemeği için şık bir tercih, rezervasyon yaptırın.",
        "tips_en": "A stylish choice for dinner, make a reservation."
    },
    {
        "name": "Hışvahan",
        "name_en": "Hisvahan",
        "area": "Şahinbey",
        "category": "Restoran",
        "tags": ["han", "otel", "lüks", "kale"],
        "distanceFromCenter": 0.2,
        "lat": 37.0645,
        "lng": 37.3835,
        "price": "high",
        "rating": 4.8,
        "description": "Kale altında bulunan, muhteşem bir restorasyondan geçmiş butik otel ve restoran. Tarihi doku lüksle buluşmuş.",
        "description_en": "Boutique hotel and restaurant under the castle, undergone a magnificent restoration. Historic texture meets luxury.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Tercihen özel bir akşam yemeği için idealdir.",
        "tips_en": "Ideally for a special dinner."
    },
    {
        "name": "Papirüs Kafe",
        "name_en": "Papirus Cafe",
        "area": "Şahinbey",
        "category": "Kafe",
        "tags": ["konak", "bahçe", "nostalji", "sakin"],
        "distanceFromCenter": 0.4,
        "lat": 37.0630,
        "lng": 37.3850,
        "price": "medium",
        "rating": 4.6,
        "description": "Eski bir Ermeni konağının avlusunda hizmet veren, asma altı gölgesiyle huzur veren saklı bir bahçe.",
        "description_en": "A hidden garden serving in the courtyard of an old Armenian mansion, giving peace with its shade under the vine.",
        "bestTime": "İkindi",
        "bestTime_en": "Afternoon",
        "tips": "Nostaljik atmosferde kitap okumak için harika.",
        "tips_en": "Great for reading a book in a nostalgic atmosphere."
    },
    {
        "name": "Kahveci Seddar Bey",
        "name_en": "Kahveci Seddar Bey",
        "area": "Şahinbey",
        "category": "Kafe",
        "tags": ["kahve", "köz", "osmanlı", "küçük"],
        "distanceFromCenter": 0.3,
        "lat": 37.0620,
        "lng": 37.3800,
        "price": "medium",
        "rating": 4.7,
        "description": "Közde pişirdiği çift köpüklü kahvesiyle ünlü, küçük ve samimi bir kahve dükkanı.",
        "description_en": "Small and friendly coffee shop famous for its double-foam coffee cooked on embers.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kahve sunumu şov niteliğindedir, videoya çekmeye hazır olun.",
        "tips_en": "Coffee presentation is like a show, be ready to record video."
    }
]

# --- BATCH 4: MUSEUMS & HISTORY ---
new_gaziantep_places_4 = [
    {
        "name": "Zeugma Mozaik Müzesi",
        "name_en": "Zeugma Mosaic Museum",
        "area": "Şehitkamil",
        "category": "Müze",
        "tags": ["mozaik", "tarih", "roma", "çingene kızı"],
        "distanceFromCenter": 2.5,
        "lat": 37.0750,
        "lng": 37.3860,
        "price": "medium",
        "rating": 4.9,
        "description": "Dünyanın en büyük mozaik müzelerinden biri. Meşhur 'Çingene Kızı' mozaiği ve Zeugma antik kentinden çıkarılan eserler burada.",
        "description_en": "One of the largest mosaic museums in the world. Famous 'Gypsy Girl' mosaic and artifacts excavated from Zeugma ancient city are here.",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Müzeyi gezmek en az 2-3 saat sürer, rahat ayakkabı giyin.",
        "tips_en": "Touring the museum takes at least 2-3 hours, wear comfortable shoes."
    },
    {
        "name": "Hamam Müzesi",
        "name_en": "Hamam Museum",
        "area": "Şahinbey",
        "category": "Müze",
        "tags": ["hamam", "kültür", "sabun", "mimari"],
        "distanceFromCenter": 0.3,
        "lat": 37.0640,
        "lng": 37.3820,
        "price": "low",
        "rating": 4.6,
        "description": "Lala Mustafa Paşa Külliyesi'nin hamam bölümünde kurulan, Osmanlı hamam kültürünü ve geleneklerini anlatan müze.",
        "description_en": "Museum established in the hamam section of Lala Mustafa Pasha Complex, explaining Ottoman hamam culture and traditions.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Soğukluk, ılıklık ve sıcaklık bölümlerinin mimarisi etkileyicidir.",
        "tips_en": "The architecture of the cold, warm and hot sections is impressive."
    },
    {
        "name": "Emine Göğüş Mutfak Müzesi",
        "name_en": "Emine Gogus Culinary Museum",
        "area": "Şahinbey",
        "category": "Müze",
        "tags": ["mutfak", "yemek", "kültür", "araç gereç"],
        "distanceFromCenter": 0.2,
        "lat": 37.0630,
        "lng": 37.3830,
        "price": "low",
        "rating": 4.5,
        "description": "Türkiye'nin ilk mutfak müzesi. Gaziantep mutfak kültüründe kullanılan araç gereçler ve sofra düzeni sergileniyor.",
        "description_en": "Turkey's first culinary museum. Utensils and table settings used in Gaziantep culinary culture are exhibited.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Mutfak severler için eski bakır kapları görmek ilginç olabilir.",
        "tips_en": "For kitchen lovers, seeing old copper vessels can be interesting."
    },
    {
        "name": "Gaziantep Kalesi",
        "name_en": "Gaziantep Castle",
        "area": "Şahinbey",
        "category": "Tarihi",
        "tags": ["kale", "manzara", "savunma", "savaş"],
        "distanceFromCenter": 0.0,
        "lat": 37.0665,
        "lng": 37.3833,
        "price": "low",
        "rating": 4.6,
        "description": "Şehrin merkezindeki tepede heybetle duran kale. İçindeki panoramik müzede Antep savunması anlatılıyor (Deprem sonrası durumu kontrol ediniz).",
        "description_en": "The castle standing majestically on the hill in the city center. The panoramic museum inside tells the defense of Antep (Check status after earthquake).",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kalenin tepesinden şehir manzarası harikadır.",
        "tips_en": "City view from the top of the castle is wonderful."
    },
    {
        "name": "Oyun ve Oyuncak Müzesi",
        "name_en": "Gaziantep Toy Museum",
        "area": "Şahinbey",
        "category": "Müze",
        "tags": ["oyuncak", "çocuk", "nostalji", "mağara"],
        "distanceFromCenter": 0.5,
        "lat": 37.0610,
        "lng": 37.3850,
        "price": "low",
        "rating": 4.8,
        "description": "Tarihi bir Antep evinde, mağaraları da kullanarak sergilenen binlerce oyuncak. Hem çocuklar hem yetişkinler için büyüleyici.",
        "description_en": "Thousands of toys exhibited in a historic Antep house, also using the caves. Fascinating for both children and adults.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Avrupalı porselen bebekler koleksiyonu çok değerlidir.",
        "tips_en": "European porcelain dolls collection is very valuable."
    },
    {
        "name": "Medusa Cam Eserler Müzesi",
        "name_en": "Medusa Glass Works Museum",
        "area": "Şahinbey",
        "category": "Müze",
        "tags": ["cam", "sanat", "roma", "özel"],
        "distanceFromCenter": 0.3,
        "lat": 37.0650,
        "lng": 37.3820,
        "price": "medium",
        "rating": 4.5,
        "description": "Eski bir Antep evinde, Roma dönemine ait cam eserlerin ve antikaların sergilendiği özel müze.",
        "description_en": "Private museum in an old Antep house where Roman period glass works and antiques are exhibited.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Müze binasının avlusu da çok şirindir.",
        "tips_en": "The courtyard of the museum building is also very cute."
    },
    {
        "name": "Atatürk Anı Müzesi",
        "name_en": "Ataturk Memorial Museum",
        "area": "Şahinbey",
        "category": "Müze",
        "tags": ["tarih", "atatürk", "konak", "cumhuriyet"],
        "distanceFromCenter": 0.4,
        "lat": 37.0620,
        "lng": 37.3840,
        "price": "free",
        "rating": 4.7,
        "description": "Atatürk'ün Gaziantep'i ziyareti sırasında konakladığı ve sonradan müzeye dönüştürülen tarihi bina.",
        "description_en": "Historic building where Ataturk stayed during his visit to Gaziantep, later converted into a museum.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Dönemin eşyaları ve fotoğrafları tarihi hissettiriyor.",
        "tips_en": "Items and photos of the period make you feel the history."
    },
    {
        "name": "Şeyh Fethullah Camii",
        "name_en": "Seyh Fethullah Mosque",
        "area": "Şahinbey",
        "category": "Tarihi",
        "tags": ["cami", "avlu", "sessiz", "manevi"],
        "distanceFromCenter": 0.6,
        "lat": 37.0600,
        "lng": 37.3800,
        "price": "free",
        "rating": 4.8,
        "description": "Gaziantep'in en huzurlu ve manevi atmosferi yüksek camilerinden biri. Avlusu ve mimarisi görülmeye değer.",
        "description_en": "One of the most peaceful and spiritually high atmosphere mosques in Gaziantep. Its courtyard and architecture are worth seeing.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Şehrin gürültüsünden kaçıp kafa dinlemek için ideal.",
        "tips_en": "Ideal for escaping the city noise and resting your mind."
    }
]

# --- BATCH 5: NATURE & PARKS & PROMENADES ---
new_gaziantep_places_5 = [
    {
        "name": "Dülükbaba Tabiat Parkı",
        "name_en": "Dulukbaba Nature Park",
        "area": "Şehitkamil",
        "category": "Park",
        "tags": ["piknik", "orman", "kamp", "mangal"],
        "distanceFromCenter": 8.0,
        "lat": 37.1200,
        "lng": 37.3300,
        "price": "low",
        "rating": 4.6,
        "description": "Türkiye'nin en büyük tabiat parklarından biri. Hafta sonu Gazianteplilerin mangal ve piknik klasiği.",
        "description_en": "One of Turkey's largest nature parks. A barbecue and picnic classic for Gaziantep locals on weekends.",
        "bestTime": "Hafta içi",
        "bestTime_en": "Weekday",
        "tips": "Hafta sonu çok kalabalık olur, sakinlik isterseniz hafta içi gidin.",
        "tips_en": "It gets very crowded on weekends, go on weekdays if you want quiet."
    },
    {
        "name": "Alleben Göleti",
        "name_en": "Alleben Pond",
        "area": "Şahinbey",
        "category": "Park",
        "tags": ["göl", "yürüyüş", "bisiklet", "manzara"],
        "distanceFromCenter": 5.0,
        "lat": 37.0300,
        "lng": 37.3000,
        "price": "free",
        "rating": 4.5,
        "description": "Şehir stresinden kaçış noktası. Göl kenarında yürüyüş parkuru, bisiklet yolları ve piknik alanları mevcut.",
        "description_en": "Escape point from city stress. Walking track, bicycle paths and picnic areas are available by the lake.",
        "bestTime": "İkindi",
        "bestTime_en": "Afternoon",
        "tips": "Gün batımında göl manzarası fotojeniktir.",
        "tips_en": "Lake view is photogenic at sunset."
    },
    {
        "name": "Botanık Bahçesi",
        "name_en": "Botanical Garden",
        "area": "Şehitkamil",
        "category": "Park",
        "tags": ["bitki", "çiçek", "fotoğraf", "sakin"],
        "distanceFromCenter": 2.0,
        "lat": 37.0800,
        "lng": 37.3500,
        "price": "low",
        "rating": 4.7,
        "description": "Farklı bitki türlerini görebileceğiniz, peyzajıyla büyüleyen huzurlu bir bahçe. Düğün fotoğrafçılarının da uğrak yeri.",
        "description_en": "A peaceful garden fascinating with its landscape where you can see different plant species. Frequent destination for wedding photographers too.",
        "bestTime": "Bahar",
        "bestTime_en": "Spring",
        "tips": "Japon bahçesi bölümü çok estetiktir.",
        "tips_en": "Japanese garden section is very aesthetic."
    },
    {
        "name": "Kavaklık Parkı",
        "name_en": "Kavaklik Park",
        "area": "Şahinbey",
        "category": "Park",
        "tags": ["çay bahçesi", "dere", "koşu", "merkez"],
        "distanceFromCenter": 1.5,
        "lat": 37.0550,
        "lng": 37.3600,
        "price": "free",
        "rating": 4.6,
        "description": "Şehrin en eski ve en yeşil parklarından. Alleben Deresi kenarında çay içmek ve yürüyüş yapmak için harika.",
        "description_en": "One of the oldest and greenest parks of the city. Great for drinking tea and walking by the Alleben Creek.",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Sabah yürüyüşü sonrası park içindeki çay bahçelerinde mola verin.",
        "tips_en": "Take a break at the tea gardens inside the park after morning walk."
    },
    {
        "name": "Masal Parkı",
        "name_en": "Fairytale Park",
        "area": "Şehitkamil",
        "category": "Park",
        "tags": ["çocuk", "masal", "heykeller", "eğlence"],
        "distanceFromCenter": 2.5,
        "lat": 37.0750,
        "lng": 37.3600,
        "price": "free",
        "rating": 4.5,
        "description": "Türk masal kahramanlarının heykelleri ve canlandırmalarıyla dolu, çocuklar için harika bir tematik park.",
        "description_en": "A wonderful thematic park for children, full of statues and enactments of Turkish fairytale heroes.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Çocuklu aileler için mutlaka gidilmesi gereken bir yer.",
        "tips_en": "A must-visit place for families with children."
    },
    {
        "name": "Gaziantep Hayvanat Bahçesi",
        "name_en": "Gaziantep Zoo",
        "area": "Şahinbey",
        "category": "Park",
        "tags": ["hayvanlar", "safari", "büyük", "aile"],
        "distanceFromCenter": 6.0,
        "lat": 37.0350,
        "lng": 37.3100,
        "price": "low",
        "rating": 4.7,
        "description": "Türkiye'nin en büyük, Avrupa'nın sayılı hayvanat bahçelerinden. Safari parkı ve zooloji müzesi de içeriyor.",
        "description_en": "One of Turkey's largest and Europe's few zoos. Also contains a safari park and zoology museum.",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Gezmek için en az yarım gün ayırmalısınız, çok büyük.",
        "tips_en": "You should allocate at least half a day to tour, it's very big."
    },
    {
        "name": "100. Yıl Atatürk Kültür Parkı",
        "name_en": "100th Year Ataturk Culture Park",
        "area": "Şahinbey",
        "category": "Park",
        "tags": ["büyük", "etkinlik", "merkezi", "yürüyüş"],
        "distanceFromCenter": 1.0,
        "lat": 37.0650,
        "lng": 37.3650,
        "price": "free",
        "rating": 4.6,
        "description": "Şehrin akciğeri konumunda, kilometrelerce uzanan devasa park. İçinde spor alanları, kafeler ve göletler var.",
        "description_en": "Huge park stretching for kilometers, acting as the lung of the city. Contains sports areas, cafes and ponds.",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Akşamları çok canlıdır, yerel halk buraya akar.",
        "tips_en": "Very lively in the evenings, locals flock here."
    },
    {
        "name": "Erikçe Piknik Alanı",
        "name_en": "Erikce Picnic Area",
        "area": "Şehitkamil",
        "category": "Park",
        "tags": ["piknik", "macera parkı", "etkinlik", "kayak"],
        "distanceFromCenter": 7.0,
        "lat": 37.1100,
        "lng": 37.3500,
        "price": "low",
        "rating": 4.5,
        "description": "Çam ormanları içinde, hem piknik yapabileceğiniz hem de macera parkında eğlenebileceğiniz (suni kayak pisti var) alan.",
        "description_en": "Area in pine forests where you can both picnic and have fun in the adventure park (has artificial ski slope).",
        "bestTime": "Hafta sonu",
        "bestTime_en": "Weekend",
        "tips": "Çocuklar ve gençler için aktiviteler boldur.",
        "tips_en": "Activities are plentiful for children and youth."
    }
]

# --- BATCH 6: SHOPPING & BAZAARS & HANDICRAFTS ---
new_gaziantep_places_6 = [
    {
        "name": "Bakırcılar Çarşısı",
        "name_en": "Coppersmith Bazaar",
        "area": "Şahinbey",
        "category": "Alışveriş",
        "tags": ["tarhi", "bakır", "el sanatı", "sesler"],
        "distanceFromCenter": 0.3,
        "lat": 37.0635,
        "lng": 37.3820,
        "price": "medium",
        "rating": 4.8,
        "description": "Yüzyıllardır çekiç seslerinin yankılandığı, el işçiliği bakır eşyaların üretildiği ve satıldığı otantik çarşı.",
        "description_en": "Authentic bazaar where hammer sounds have echoed for centuries, and handcrafted copper goods are produced and sold.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Ustalardan bir isminizi bakıra işlemelerini isteyebilirsiniz.",
        "tips_en": "You can ask masters to engrave your name on copper."
    },
    {
        "name": "Zincirli Bedesten",
        "name_en": "Zincirli Bedesten",
        "area": "Şahinbey",
        "category": "Alışveriş",
        "tags": ["bedesten", "hediyelik", "baharat", "tarihi"],
        "distanceFromCenter": 0.3,
        "lat": 37.0630,
        "lng": 37.3825,
        "price": "medium",
        "rating": 4.7,
        "description": "L şeklindeki tarihi kapalı çarşı. Turistik hediyelikler, kumaşlar ve baharatlar bulabilirsiniz.",
        "description_en": "L-shaped historic covered bazaar. You can find tourist souvenirs, fabrics and spices.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kutnu kumaşından yapılan şallara bakın.",
        "tips_en": "Look at shawls made of Kutnu fabric."
    },
    {
        "name": "Yemeniciler Çarşısı",
        "name_en": "Yemeniciler Bazaar",
        "area": "Şahinbey",
        "category": "Alışveriş",
        "tags": ["ayakkabı", "deri", "geleneksel", "film"],
        "distanceFromCenter": 0.3,
        "lat": 37.0628,
        "lng": 37.3822,
        "price": "medium",
        "rating": 4.6,
        "description": "Geleneksel deri ayakkabı olan 'Yemeni'lerin yapıldığı çarşı. Harry Potter ve Truva gibi filmler için çarıklar buradan gitmiştir.",
        "description_en": "Bazaar where traditional leather shoes 'Yemeni' are made. Sandals for movies like Harry Potter and Troy were sent from here.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Renkli yemeniler çok şık ve rahattır, denemeden almayın.",
        "tips_en": "Colorful yemenis are very stylish and comfortable, don't buy without trying."
    },
    {
        "name": "Almacı Pazarı",
        "name_en": "Almaci Bazaar",
        "area": "Şahinbey",
        "category": "Alışveriş",
        "tags": ["kuruyemiş", "baharat", "fıstık", "gurme"],
        "distanceFromCenter": 0.3,
        "lat": 37.0633,
        "lng": 37.3823,
        "price": "medium",
        "rating": 4.8,
        "description": "Gaziantep'in gurme marketi. En kaliteli Antep fıstığı, salça, kurutulmuş sebze (patlıcan, biber) burada bulunur.",
        "description_en": "Gaziantep's gourmet market. Top quality pistachios, tomato paste, dried vegetables (eggplant, pepper) are found here.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kurutulmuş dolmalık patlıcan ve biber almadan dönmeyin.",
        "tips_en": "Don't return without buying dried stuffed eggplants and peppers."
    },
    {
        "name": "Kutnu Kumaş Tanıtım Merkezi",
        "name_en": "Kutnu Fabric Center",
        "area": "Şahinbey",
        "category": "Alışveriş",
        "tags": ["kumaş", "ipek", "yöresel", "kraliyet"],
        "distanceFromCenter": 0.5,
        "lat": 37.0640,
        "lng": 37.3850,
        "price": "medium",
        "rating": 4.6,
        "description": "Gaziantep'e özgü, geçmişte padişah kaftanlarında kullanılan 'Kutnu' kumaşının hikayesi ve satışı.",
        "description_en": "Story and sales of 'Kutnu' fabric, unique to Gaziantep, used in sultan kaftans in the past.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kutnu kumaşından kravat veya fular güzel bir hediyedir.",
        "tips_en": "Tie or scarf made of Kutnu fabric is a nice gift."
    },
    {
        "name": "Söylemez Pasajı",
        "name_en": "Soylemez Passage",
        "area": "Şahinbey",
        "category": "Alışveriş",
        "tags": ["pasaj", "ucuz", "giyim", "yerel"],
        "distanceFromCenter": 0.4,
        "lat": 37.0610,
        "lng": 37.3810,
        "price": "cheap",
        "rating": 4.2,
        "description": "Şehrin yerlilerinin alışveriş yaptığı, uygun fiyatlı tekstil ürünleri ve çeyizliklerin bulunduğu eski pasaj.",
        "description_en": "Old passage where locals shop, containing affordable textile products and dowry items.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Pazarlık burada bir kuraldır.",
        "tips_en": "Bargaining is a rule here."
    },
    {
        "name": "Sedefçiler Çarşısı",
        "name_en": "Mother of Pearl Bazaar",
        "area": "Şahinbey",
        "category": "Alışveriş",
        "tags": ["sedef", "ahşap", "kakma", "sanat"],
        "distanceFromCenter": 0.3,
        "lat": 37.0630,
        "lng": 37.3830,
        "price": "high",
        "rating": 4.7,
        "description": "Ceviz ağacı üzerine sedef kakma sanatı yapan ustaların atölyelerinin olduğu çarşı. Mobilyalar sanat eseri gibidir.",
        "description_en": "Bazaar with workshops of masters doing mother-of-pearl inlay art on walnut wood. Furniture is like artwork.",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Küçük sedef kutular veya tavla takımları harika hatıralardır.",
        "tips_en": "Small mother-of-pearl boxes or backgammon sets are great souvenirs."
    },
    {
        "name": "Gaziler Caddesi",
        "name_en": "Gaziler Street",
        "area": "Şahinbey",
        "category": "Alışveriş",
        "tags": ["cadde", "kalabalık", "alışveriş", "canlı"],
        "distanceFromCenter": 0.2,
        "lat": 37.0600,
        "lng": 37.3800,
        "price": "variable",
        "rating": 4.3,
        "description": "Gaziantep'in İstiklal Caddesi. Sadece yayalara açık, mağazalarla dolu, şehrin en hareketli caddesi.",
        "description_en": "Gaziantep's Istiklal Street. Pedestrian-only, full of shops, the most lively street of the city.",
        "bestTime": "Akşamüstü",
        "bestTime_en": "Late Afternoon",
        "tips": "Kalabalığa karışıp şehrin ritmini hissetmek için yürüyün.",
        "tips_en": "Walk to mix with the crowd and feel the rhythm of the city."
    }
]

def enrich_gaziantep_master():
    filepath = 'assets/cities/gaziantep.json'
    all_new_places = (
        new_gaziantep_places_1 + 
        new_gaziantep_places_2 + 
        new_gaziantep_places_3 + 
        new_gaziantep_places_4 + 
        new_gaziantep_places_5 + 
        new_gaziantep_places_6
    )
    
    # Load existing data
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            print(f"Loaded {len(data['highlights'])} existing places.")
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return

    # Create a set of existing place names for checking duplicates
    existing_names = {p['name'].lower() for p in data['highlights']}
    
    places_to_add = []
    
    for place in all_new_places:
        if place['name'].lower() in existing_names:
            print(f"Skipping duplicate: {place['name']}")
            continue
            
        print(f"Processing: {place['name']}")

        # 1. Generate ID
        place_id = place['name'].lower().replace(' ', '-').replace('ç', 'c').replace('ğ', 'g').replace('ı', 'i').replace('ö', 'o').replace('ş', 's').replace('ü', 'u').replace('(', '').replace(')', '')
        place['id'] = place_id
        
        # 2. Fetch Image (Google)
        photo_url = get_google_photo_url(place['name'])
        
        if not photo_url and 'name_en' in place and place['name_en'] != place['name']:
            print(f"  Retrying with English name: {place['name_en']}...")
            photo_url = get_google_photo_url(place['name_en'])
        
        if photo_url:
            place['imageUrl'] = photo_url
            place['source'] = 'google'
        else:
            place['imageUrl'] = "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800&auto=format&fit=crop"
            place['source'] = 'unsplash_fallback'

        # 3. Add to list
        places_to_add.append(place)
        
        # Rate limit
        time.sleep(0.5)

    # Append new places
    data['highlights'].extend(places_to_add)
    
    # Save
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"\nSuccessfully added {len(places_to_add)} new places to {filepath}.")
    print(f"Total highlights now: {len(data['highlights'])}")

if __name__ == "__main__":
    enrich_gaziantep_master()
