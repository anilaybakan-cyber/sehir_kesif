import json
import os
import random

CITY_FILES = [
    "dubrovnik.json", "mykonos.json", "amalfi.json", "bodrum.json", 
    "palermo.json", "bari.json", "catania.json", "cannes.json", 
    "saint_tropez.json", "sardinya.json"
]

TEMPLATES = {
    "Tarihi": {
        "tr": [
            "{city} kentinin yüzyıllara meydan okuyan tarihi dokusunu ve {name} bölgesinin mimari ihtişamını yansıtan bu alan, kentin kültürel mirasına açılan en prestijli ve entelektüel kentsel tarih penceresidir. Akdeniz'in kadim ruhunu hissedebileceğiniz bu nokta, kenti keşfeden gezginlere unutulmaz bir kentsel deneyim sunar.",
            "{city} silüetinin en ikonik parçalarından biri olan {name}, kentin tarihsel evrimini ve kentsel hafızasını koruyan paha biçilemez bir kentsel duraktır. Burası, her köşesinde farklı bir hikaye barındıran ve kentin kentsel kimliğini tanımlayan en derin kaza kaledir.",
            "Antik dokularla modern kentsel enerjiyi birleştiren {name}, {city} kentinin kültürel kimliğini tanımlayan ve kenti keşfeden gezginlere mistik bir atmosfer sunan kentsel bir prestij ve tarih kalesidir."
        ],
        "en": [
            "An urban cultural stronghold in {city} showcasing the historical layers and architectural grandeur of {name}, offering travelers a deep dive into the region's rich heritage. As you wander through this landmark, you feel the pulse of centuries-old memories and the town's evolution.",
            "As a prestigious and intellectual landmark of {city}, {name} preserves the town's millennia-old memory and serves as a vital window into the historical evolution of the entire area for every urban explorer.",
            "This historical gemstone in {city} defines the local cultural identity, combining ancient textures with the timeless spirit of {name} to create a sophisticated and active social presence in the heart of town."
        ],
        "tips": ["Sabah erkenden gelip surlarda fotoğraf çekin.", "Rahat ayakkabılar giyin, zemin kaygan olabilir."],
        "tips_en": ["Arrive early for the best light on the stones.", "Wear comfortable sneakers; the ground can be slippery."],
        "bestTime": "Sabah (08:00 - 10:00)",
        "duration": "2 - 3 Saat"
    },
    "Müze": {
        "tr": [
            "{city} kentinin sanat ve tarih koleksiyonlarını barındıran {name}, ziyaretçilerine kentin entelektüel derinliğini ve kentsel estetiğini sunan çok katmanlı bir kültürel kaza kaledir. Sergilenen eserler, kentin sanat vizyonunu ve kentsel gelişimini anlamak için eşsiz bir fırsat sunar.",
            "Kentsel sanat dünyasının {city} kentindeki en prestijli temsilcisi olan {name}, hem mimarisi hem de içindeki değerlerle kentsel bir ilham kaynağıdır. Kentin kültürel nabzını tutan bu müze, her yaştan kentsel gezgin için eğitici ve etkileyici bir duraktır."
        ],
        "en": [
            "A prestigious urban window into the art and history of {city}, {name} offers its visitors a multi-layered cultural experience that highlights the town's intellectual depth and aesthetic evolution through the ages.",
            "Standing as the peak of the city's artistic scene, {name} is a sophisticated urban landmark in {city} where contemporary vision meets historical treasures, providing a deep and inspiring social discovery."
        ],
        "tips": ["Müze kartınızı yanınızda bulundurun.", "Sesli rehber alarak detayları kaçırmayın."],
        "tips_en": ["Carry your digital ticket to skip the queue.", "Get an audio guide to fully appreciate the exhibits."],
        "bestTime": "Öğleden Önce (10:00 - 13:00)",
        "duration": "1.5 - 2 Saat"
    },
    "Restoran": {
        "tr": [
            "{city} gastronomisinin en seçkin temsilcilerinden biri olan {name}, otantik lezzetleri modern bir kentsel sunumla birleştirerek misafirlerine unutulmaz bir kentsel lezzet kaçış rotası sunar. Şehrin yerel tatlarını en prestijli şekilde deneyimleyebileceğiniz bu adres, kentsel sosyal hayatın da kalbidir.",
            "Yerel malzemelerin ve geleneksel yemeklerin ustalıkla harmanlandığı {name}, {city} kentinin kalbindeki en samimi ve şık kentsel lezzet duraklarından bir tanesidir. Kentsel gurme gezginler için mutlaka keşfedilmesi gereken prestijli bir kaza kaledir."
        ],
        "en": [
            "A prestigious culinary destination in {city} known for its authentic flavors and vibrant social atmosphere, {name} is the perfect spot for experiencing high-end local gastronomy with a professional urban touch.",
            "Merging traditional recipes with modern urban flair, this restaurant offers a sophisticated social escape for food lovers visiting {name} in {city}, defining the town's active and flavorful dining profile."
        ],
        "tips": ["Akşam yemeği için birkaç gün önceden yer ayırtın.", "Yerel spesiyalleri şefe sormayı unutmayın."],
        "tips_en": ["Book a table a few days in advance for dinner.", "Ask the chef for the daily local specials."],
        "bestTime": "Akşam (19:30 - 21:30)",
        "duration": "2 Saat"
    },
    "Park": {
        "tr": [
            "{city} kentinin kalbinde yeşil bir vaha olan {name}, kentsel dinamizmden uzaklaşmak isteyenler için huzurlu ve estetik bir kentsel dinlenme alanı sunar. Doğanın kentsel mimariyle buluştuğu bu park, hem yerel halk hem de gezginler için çok sevilen bir kentsel sosyal kaçış noktasıdır.",
            "{city} silüetinin en ferahlatıcı noktalarından biri olan {name}, kentin aktif tempousuna taze bir nefes katan prestijli bir kentsel sosyal ve doğal buluşma alanıdır."
        ],
        "en": [
            "A lush urban oasis in the heart of {city}, {name} offers a peaceful and aesthetic social escape for those looking to retreat from the active city energy while enjoying synchronized local nature and design.",
            "Representing the peak of natural tranquility in {city}, this park is a prestigious destination for morning walks and social gatherings, defining the urban wellness culture of the town today."
        ],
        "tips": ["Rahat bir yürüyüş için spor giyinin.", "Gün batımı saatlerinde ışık muhteşem olur."],
        "tips_en": ["A great spot for a morning jog or picnic.", "The lighting is perfect for photos during the golden hour."],
        "bestTime": "Sabah veya Gün Batımı",
        "duration": "1 - 2 Saat"
    },
    "Deneyim": {
        "tr": [
            "{city} kentinin ruhunu en yakından hissedebileceğiniz {name}, kentin kentsel enerjisini ve kültürel nabzını yansıtan kentsel bir prestij noktası ve sofistike bir kentsel sosyal duraktır. Burası, her ziyarette kentin yeni ve heyecan verici bir yönünü keşfetmenizi sağlayan kentsel bir vizyon alanıdır.",
            "{city} kenti keşfinde kentsel dinamizmi ve sosyal hayatı birleştiren {name}, kentin kentsel haritasına karakter katan en sevilen ve tatlı kentsel duraklardan birisi olan kentsel bir kaza kaledir."
        ],
        "en": [
            "A sophisticated urban destination reflecting the town's modern energy and creative pulse, {name} is a vital part of the {city} social map where every traveler discovers something unique and professional.",
            "As a refined social and cultural point in {city}, {name} offers a high-quality experience that perfectly merges urban convenience with local aesthetic charm for an active holiday mood."
        ],
        "tips": ["Kameranızı yanınıza almayı unutmayın.", "Yerel halkla sohbet etmek deneyimi derinleştirir."],
        "tips_en": ["Don't forget to keep your camera ready for the views.", "Engaging with locals here makes the experience richer."],
        "bestTime": "Gün Boyu",
        "duration": "1 - 1.5 Saat"
    }
}

LOCAL_TIPS = {
    "dubrovnik": ["Eski Şehir (Old Town) surlarında turu tam tur yapın.", "Teleferik ile Srd Dağı'na çıkıp gün batımını seyredin.", "Lokrum Adası'na giden teknelere binip doğada bir gün geçirin.", "Buza Bar'da surların dibinde denize girin.", "Sabah 08:00'den önce şehre girmek kalabalıktan korur."],
    "mykonos": ["Labirent gibi Chora sokaklarında kaybolun (bu bilinçli yapılır).", "Küçük Venedik'te (Little Venice) kokteyl yudumlayarak gün batımını izleyin.", "Adanın kuzeyindeki Agios Sostis gibi daha sakin plajları keşfedin.", "Delos adasına günübirlik tarih turu yapın.", "Araç yerine ATV veya scooter ile ulaşım daha pratiktir."],
    "amalfi": ["Positano'ya giden feribottan kıyı şeridini fotoğraflayın.", "Limon sorbesini mutlaka kendi limonu içinde deneyin.", "Sentiero degli Dei (Tanrılar Yolu) yürüyüş parkurunu keşfedin.", "Ravello'daki Villa Cimbrone'nin bahçelerini mutlaka görün.", "Otobüs biletlerinizi binmeden önce tabaccheria'lardan alın."],
    "bodrum": ["Bodrum Kalesi ve Sualtı Arkeoloji Müzesi'ne yarım gün ayırın.", "Gümüşlük'te gün batımı yemeği bir Bodrum klasiğidir.", "Tekne turu ile Akvaryum Koyu gibi berrak durakları gezin.", "Antik Tiyatro'daki yaz konserlerini takip edin.", "Zeki Müren Sanat Müzesi'ne nostalji turu yapın."],
    "palermo": ["Teatro Massimo'nun büyüleyici mimarisini fotoğraflayın.", "Yerel pazarlarda (Ballarò veya Vucciria) sokak lezzetlerini tadın.", "Isola delle Femmine plajında turkuaz deniz keyfi yapın.", "Palazzo dei Normanni'nin altın detaylarını kaçırmayın.", "Gerçek Sicilya cannoli'sini bir yerel pastanede deneyin."],
    "bari": ["Eski Bari'nin (Bari Vecchia) ara sokaklarında 'orecchiette' yapan kadınları izleyin.", "Castello Svevo kalesinin iç avlusunu gezin.", "Polignano a Mare'ye trenle 20 dakikada günübirlik gezi yapın.", "Focaccia Barese en popüler sokak lezzetidir, mutlaka deneyin.", "Lungomare sahil yolunda akşam yürüyüşü yapın."],
    "catania": ["Etna Yanardağı'na düzenlenen güvenli turlara katılın.", "Piazza del Duomo'daki fil heykelini (Liotru) görün.", "La Pescheria (balık pazarı) sabahları çok renklidir.", "San Benedetto Kilisesi'ndeki Barok detayları inceleyin.", "Arancini lezzetini farklı dolgularla tadın."],
    "cannes": ["La Croisette kordonunda şık bir yürüyüş yapın.", "Palais des Festivals önündeki ünlü basamaklarda fotoğraf çekilin.", "Le Suquet bölgesinin dar sokaklarından limanı seyredin.", "Île Sainte-Marguerite adasına kısa bir feribot yolculuğu yapın.", "Marché Forville pazarından yerel taze ürünler alın."],
    "saint_tropez": ["Eski Liman'da (Vieux Port) görkemli yatları izleyin.", "Pampelonne Plajı'nın ünlü plaj kulüplerinde vakit geçirin.", "Place des Lices meydanında yerel halkın petank oynamasını izleyin.", "Tarte Tropézienne'i anavatanında deneyin.", "Kalenin (Citadel) tepesinden tüm körfezi görün."],
    "sardinya": ["Costa Smeralda'nın pırlanta gibi denizinde yüzün.", "Alghero'nun Katalan esintili sokaklarını gezin.", "Nuraghe antik kalıntılarını ziyaret ederek tarih öncesine gidin.", "La Maddalena Takımadaları'na günübirlik tekne turu yapın.", "Taze ıstakoz ve yerel şaraplarını tadın."]
}

def get_template(cat, lang, name, city):
    category = cat if cat in TEMPLATES else "Deneyim"
    templates = TEMPLATES[category][lang]
    # Consistently pick a template based on name/city
    idx = sum(ord(c) for c in (name + city)) % len(templates)
    return templates[idx].format(name=name, city=city)

def overhaul_file(filename):
    path = os.path.join("assets/cities", filename)
    if not os.path.exists(path): return
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    city_key = filename.replace(".json", "")
    city_name = data.get("city", city_key.capitalize())
    
    # Add root localTips
    if city_key in LOCAL_TIPS:
        data["localTips"] = LOCAL_TIPS[city_key]
    
    # Process highlights
    venues = data.get("highlights", []) if isinstance(data, dict) else data
    updated = 0
    for h in venues:
        if not isinstance(h, dict) or "name" not in h: continue
        
        cat = h.get("category", "Deneyim")
        if cat not in TEMPLATES: cat = "Deneyim"
        
        # Hyper-Premium Description
        h["description"] = get_template(cat, "tr", h["name"], city_name)
        name_en = h.get("name_en") or h["name"]
        h["description_en"] = get_template(cat, "en", name_en, city_name)
        
        # Metadata
        meta = TEMPLATES[cat]
        idx = sum(ord(c) for c in (h["name"] + city_name)) % len(meta["tips"])
        h["tips"] = meta["tips"][idx]
        h["tips_en"] = meta["tips_en"][idx]
        h["bestTime"] = meta["bestTime"]
        h["duration"] = meta["duration"]
        
        # Ensure image is present
        if not h.get("imageUrl"):
            h["imageUrl"] = f"https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/{city_key}/{h.get('id', 'default')}.jpg"
            
        updated += 1
        
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Overhauled {filename}: {updated} venues updated.")

def main():
    for f in CITY_FILES:
        overhaul_file(f)

if __name__ == "__main__":
    main()
