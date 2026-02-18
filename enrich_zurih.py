import json
import os

new_zurih_batch1 = [
    {
        "name": "Augustinergasse",
        "name_en": "Augustinergasse",
        "area": "Altstadt",
        "category": "Tarihi",
        "tags": ["sokak", "renkli", "orta çağ", "bayraklar"],
        "distanceFromCenter": 0.2,
        "lat": 47.3719,
        "lng": 8.5402,
        "price": "free",
        "rating": 4.7,
        "description": "Zürih'in en güzel ve en renkli sokaklarından biri. Cumbalı evleri ve asılı İsviçre bayraklarıyla Orta Çağ atmosferini iliklerinize kadar hissettirir.",
        "description_en": "One of Zurich's most beautiful and colorful historical narrow streets, famous for its overhanging bay windows and vibrant Swiss flags.",
        "imageUrl": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Fotoğraf çekmek için en iyi noktalardan biridir, sabah erken saatlerde daha sakin olur.",
        "tips_en": "A prime spot for photography; early morning offers the best light and fewest crowds."
    },
    {
        "name": "Schipfe",
        "name_en": "Schipfe",
        "area": "Altstadt",
        "category": "Tarihi",
        "tags": ["nehir kenarı", "zanaat", "tarihi", "limmat"],
        "distanceFromCenter": 0.3,
        "lat": 47.3739,
        "lng": 8.5422,
        "price": "free",
        "rating": 4.6,
        "description": "Limmat nehri kıyısında, Zürih'in en eski mahallelerinden biri. Eskiden gemicilerin yük boşalttığı bu sokak şimdi tasarım atölyelerine ev sahipliği yapıyor.",
        "description_en": "One of the city's oldest quarters along the Limmat River. Once a docking place for boats, it now houses artisan workshops and design studios.",
        "imageUrl": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Nehir kenarındaki banklarda oturup karşı kıyıdaki Niederdorf manzarasını izleyin.",
        "tips_en": "Sit on the riverside benches to enjoy the peaceful view of the Niederdorf district across the water."
    },
    {
        "name": "Paradeplatz",
        "name_en": "Paradeplatz",
        "area": "City",
        "category": "Tarihi",
        "tags": ["finans", "bankalar", "merkez", "ikonik"],
        "distanceFromCenter": 0.1,
        "lat": 47.3697,
        "lng": 8.5391,
        "price": "free",
        "rating": 4.4,
        "description": "Dünya finansının kalbinin attığı meydan. Büyük İsviçre bankalarının genel merkezleri burada bulunur.",
        "description_en": "The hub of the Swiss banking world. Located at the intersection of Bahnhofstrasse, it’s home to the headquarters of major Swiss banks.",
        "imageUrl": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800",
        "bestTime": "Hafta içi mesai saatleri",
        "bestTime_en": "Weekday business hours",
        "tips": "Meydandaki Sprüngli'den meşhur 'Luxemburgerli' makaronlarından mutlaka deneyin.",
        "tips_en": "Don't miss the famous 'Luxemburgerli' macaroons at the iconic Sprüngli shop on the corner."
    },
    {
        "name": "ETH Polyterrasse",
        "name_en": "ETH Polyterrasse",
        "area": "University District",
        "category": "Manzara",
        "tags": ["panoroma", "üniversite", "teras", "ücretsiz"],
        "distanceFromCenter": 0.5,
        "lat": 47.3762,
        "lng": 8.5477,
        "price": "free",
        "rating": 4.8,
        "description": "ETH Zürih üniversitesinin önündeki devasa teras. Şehrin, Limmat nehrinin ve Alpler'in panoramik manzarasını sunar.",
        "description_en": "A massive terrace in front of the ETH Zurich main building, offering one of the best panoramic views of the city, the Limmat, and the Alps.",
        "imageUrl": "https://images.unsplash.com/photo-1473951574080-01fe45ec8643?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Polybahn füniküleri ile Central meydanından buraya 2 dakikada çıkabilirsiniz.",
        "tips_en": "Take the historic Polybahn funicular from Central for a quick 2-minute trip up to the terrace."
    },
    {
        "name": "Viadukt (Markthalle)",
        "name_en": "Im Viadukt",
        "area": "Zürich West",
        "category": "Alışveriş",
        "tags": ["hipster", "yemek pazarı", "mimari", "tasarım"],
        "distanceFromCenter": 2.5,
        "lat": 47.3884,
        "lng": 8.5273,
        "price": "medium",
        "rating": 4.6,
        "description": "Eski bir demiryolu viyadüğünün kemerleri altına kurulmuş şık mağazalar ve büyük bir yemek pazarı.",
        "description_en": "A unique shopping street integrated into the arches of a functional railway viaduct, featuring boutiques and a gourmet market hall.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Cumartesi öğle",
        "bestTime_en": "Saturday lunch",
        "tips": "Markthalle kısmında taze yerel peynirlerin ve şarküteri ürünlerinin tadına bakın.",
        "tips_en": "Check out the Markthalle section for high-quality local cheeses, bread, and regional specialties."
    },
    {
        "name": "Frau Gerolds Garten",
        "name_en": "Frau Gerolds Garten",
        "area": "Zürich West",
        "category": "Deneyim",
        "tags": ["beer garden", "konteyner", "açık hava", "lokal"],
        "distanceFromCenter": 2.6,
        "lat": 47.3853,
        "lng": 8.5188,
        "price": "medium",
        "rating": 4.5,
        "description": "Konteynerler, bitkiler ve sanat eserleriyle dolu, Zürih West'in en popüler açık hava eğlence alanı.",
        "description_en": "A vibrant urban garden and meeting point made of shipping containers, offering outdoor bars, small shops, and a relaxed atmosphere.",
        "imageUrl": "https://images.unsplash.com/photo-1514525253361-bee1a2399222?w=800",
        "bestTime": "Yaz akşamları",
        "bestTime_en": "Summer evenings",
        "tips": "Kışın burada kurulan fondü çadırı (Fondue-Zelt) çok meşhurdur, rezervasyon şarttır.",
        "tips_en": "In winter, their cozy fondue tent is a MUST; make sure to book weeks in advance."
    },
    {
        "name": "Freitag Tower",
        "name_en": "Freitag Tower",
        "area": "Zürich West",
        "category": "Alışveriş",
        "tags": ["konteyner", "tasarım", "çanta", "ikonik"],
        "distanceFromCenter": 2.6,
        "lat": 47.3861,
        "lng": 8.5186,
        "price": "medium",
        "rating": 4.4,
        "description": "Üst üste dizilmiş 17 nakliye konteyneriyle inşa edilmiş, Zürih'in en meşhur çanta mağazası ve aynı zamanda bir sanat objesi.",
        "description_en": "Constructed from 17 rusted shipping containers, this is the flagship store for the famous Freitag bags made from recycled truck tarps.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "En üstteki seyir terasına ücretsiz çıkıp Zürich West'in endüstriyel manzarasını görebilirsiniz.",
        "tips_en": "Climb all the way to the top terrace for a free view of the industrial and trendy Zurich West district."
    },
    {
        "name": "Pavillon Le Corbusier",
        "name_en": "Pavillon Le Corbusier",
        "area": "Seefeld",
        "category": "Müze",
        "tags": ["mimari", "tasarım", "renkli", "modern"],
        "distanceFromCenter": 2.0,
        "lat": 47.3557,
        "lng": 8.5519,
        "price": "medium",
        "rating": 4.5,
        "description": "Ünlü mimar Le Corbusier tarafından tasarlanan son eser. Renkli emaye panelleri ve çelik yapısıyla bir sanat eseri.",
        "description_en": "The last building designed by the world-famous architect Le Corbusier. A colorful masterpiece of glass, steel, and enamel panels.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Güneşli öğleden sonra",
        "bestTime_en": "Sunny afternoon",
        "tips": "Göl kıyısında yer alan bu yapının içindeki mobilya tasarımlarını mutlaka inceleyin.",
        "tips_en": "Located right by the lake, the interior showroom features some of the architect's legendary furniture designs."
    },
    {
        "name": "Botanischer Garten (Eski Botanik Bahçesi)",
        "name_en": "Alter Botanischer Garten",
        "area": "City",
        "category": "Park",
        "tags": ["sessiz", "doğa", "tarihi bahçe", "vaha"],
        "distanceFromCenter": 0.5,
        "lat": 47.3711,
        "lng": 8.5342,
        "price": "free",
        "rating": 4.6,
        "description": "Şehrin kalbinde, bankaların arasında gizli kalmış huzurlu bir vaha. Tropikal bitki evi (Palmenhaus) görülmeye değer.",
        "description_en": "A peaceful hilltop oasis hidden amidst the city's banking district. Home to an 1851 octagonal palm house and rare plants.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Öğle arası",
        "bestTime_en": "Lunch break",
        "tips": "Tepedeki Gessner bahçesi, Orta Çağ tıbbi bitkileriyle doludur.",
        "tips_en": "Climb up to the 'Gessner-Garten' at the highest point to see a medieval medicinal herb garden."
    },
    {
        "name": "Bürkliplatz Market",
        "name_en": "Bürkliplatz Market",
        "area": "Riverside",
        "category": "Alışveriş",
        "tags": ["pazar", "çiçek", "lokal", "bit pazarı"],
        "distanceFromCenter": 0.5,
        "lat": 47.3667,
        "lng": 8.5414,
        "price": "medium",
        "rating": 4.4,
        "description": "Göl kenarında kurulan, taze çiçeklerin ve yerel peynirlerin satıldığı pazar. Cumartesi günleri dev bir bit pazarına dönüşür.",
        "description_en": "A lovely market on the lakeshore featuring fresh flowers and local produce. It turns into a massive flea market every Saturday.",
        "imageUrl": "https://images.unsplash.com/photo-1544333346-bf0375179462?w=800",
        "bestTime": "Salı/Cuma sabahları",
        "bestTime_en": "Tuesday/Friday mornings",
        "tips": "Cumartesi günleri antika ve vintage ürünler bulmak için erken gelmeniz önerilir.",
        "tips_en": "Arrive early on Saturdays to snag the best vintage finds at the flea market section."
    },
    {
        "name": "Kronenhalle",
        "name_en": "Kronenhalle",
        "area": "Bellevue",
        "category": "Restoran",
        "tags": ["sanat", "tarihi", "fine dining", "picasso"],
        "distanceFromCenter": 0.4,
        "lat": 47.3669,
        "lng": 8.5469,
        "price": "high",
        "rating": 4.7,
        "description": "Gerçek bir müze-restoran. Masanızı çevreleyen duvarlarda orijinal Picasso, Matisse ve Chagall tabloları görebilirsiniz.",
        "description_en": "A world-famous institution where you dine surrounded by original masterpieces by Picasso, Chagall, and Matisse.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "bestTime": "Akşam yemeği",
        "bestTime_en": "Dinner",
        "tips": "Zürih usulü dana eti (Zürcher Geschnetzeltes) burada yenebilecek en iyi yemektir.",
        "tips_en": "Ordering the 'Zürcher Geschnetzeltes' with Rösti is the classic experience here."
    },
    {
        "name": "Cafe Schober",
        "name_en": "Cafe Schober",
        "area": "Niederdorf",
        "category": "Kafe",
        "tags": ["tatlı", "sıcak çikolata", "tarihi", "nostalji"],
        "distanceFromCenter": 0.3,
        "lat": 47.3717,
        "lng": 8.5442,
        "price": "high",
        "rating": 4.6,
        "description": "Zürih'in en eski ve en görkemli pastanelerinden biri. 'Péclard' olarak da bilinir, iç mekanı bir saray odasını andırır.",
        "description_en": "One of Zurich's most historic and sumptuously decorated cafes, famous for its incredible hot chocolate and handmade pastries.",
        "imageUrl": "https://images.unsplash.com/photo-1506764483492-1813517e5735?w=800",
        "bestTime": "Öğleden sonra kahvesi",
        "bestTime_en": "Afternoon coffee",
        "tips": "Sıcak çikolatası krema ile servis edilir ve şehirdeki en iyilerden biridir.",
        "tips_en": "Their hot chocolate served with a dollop of cream is legendary in the city."
    },
    {
        "name": "MFO-Park",
        "name_en": "MFO-Park",
        "area": "Oerlikon",
        "category": "Park",
        "tags": ["mimari", "çelik", "modern", "bitki"],
        "distanceFromCenter": 4.5,
        "lat": 47.4121,
        "lng": 8.5402,
        "price": "free",
        "rating": 4.5,
        "description": "Modern bir park tasarımı harikası. Dev bir çelik iskeletin tırmanıcı bitkilerle kaplanarak devasa bir açık hava 'odasına' dönüştüğü yer.",
        "description_en": "An architectural marvel: a massive steel trellis structure covered in climbing plants, creating a giant multi-level outdoor green space.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Yaz başı (bitkiler yeşilken)",
        "bestTime_en": "Early summer (when fully green)",
        "tips": "Merdivenlerle en üst kata çıkıp Oerlikon bölgesinin manzarasına bakın.",
        "tips_en": "Climb the various staircases within the structure to see unique perspectives from different levels."
    },
    {
        "name": "Urania Sternwarte",
        "name_en": "Urania Observatory",
        "area": "City",
        "category": "Deneyim",
        "tags": ["yıldızlar", "teleskop", "tarihi", "gözlemevi"],
        "distanceFromCenter": 0.4,
        "lat": 47.3739,
        "lng": 8.5403,
        "price": "medium",
        "rating": 4.4,
        "description": "Şehrin ortasındaki tarihi gözlemevi kulesi. Jüpiter'den Satürn'ün halkalarına kadar evreni keşfedebilirsiniz.",
        "description_en": "A historic public observatory with a 50-meter high tower, offering guided tours and views of the stars through a massive telescope.",
        "imageUrl": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800",
        "bestTime": "Açık hava geceleri",
        "bestTime_en": "Clear nights",
        "tips": "Hemen altındaki Jules Verne Bar'da bir içki içip şehri izlemek de harikadır.",
        "tips_en": "The Jules Verne Panorama Bar located right below the observatory offers great sunset views."
    },
    {
        "name": "Sukkulenten-Sammlung",
        "name_en": "Succulent Collection",
        "area": "Enge",
        "category": "Park",
        "tags": ["kaktüs", "sukkulent", "botanik", "ücretsiz"],
        "distanceFromCenter": 2.0,
        "lat": 47.3528,
        "lng": 8.5350,
        "price": "free",
        "rating": 4.7,
        "description": "Dünyanın en büyük kaktüs ve etli bitki koleksiyonlarından biri. 6500'den fazla tür barındırır.",
        "description_en": "One of the world's most extensive collections of succulents and cacti, featuring over 6,500 species in beautiful glasshouses.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Giriş ücretsizdir; göl kenarındaki yürüyüş yolunun hemen üzerindedir.",
        "tips_en": "Entry is free; it's a perfect quick stop during a stroll along the Lake Zurich promenade."
    },
    {
        "name": "St. Peter Kirche",
        "name_en": "St. Peter Church",
        "area": "Altstadt",
        "category": "Tarihi",
        "tags": ["saat kulesi", "kilise", "tarihi", "en büyük"],
        "distanceFromCenter": 0.3,
        "lat": 47.3711,
        "lng": 8.5408,
        "price": "free",
        "rating": 4.5,
        "description": "Avrupa'nın en büyük kilise saati kadranına (8.7 metre) sahip olan, Zürih'in en eski kiliselerinden biri.",
        "description_en": "One of Zurich's four main churches, famous for having the largest church clock face in Europe (8.7 meters in diameter).",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kilisenin içi Barok pencereleri ve sade tasarımıyla çok huzurludur.",
        "tips_en": "Step inside to see the beautiful 18th-century Baroque interior and enjoy the peaceful acoustics."
    },
    {
        "name": "Rietberg Museum",
        "name_en": "Museum Rietberg",
        "area": "Enge",
        "category": "Müze",
        "tags": ["dünya sanatı", "park", "villalar", "kültür"],
        "distanceFromCenter": 2.1,
        "lat": 47.3582,
        "lng": 8.5299,
        "price": "medium",
        "rating": 4.6,
        "description": "Avrupa dışındaki kültürlere adanmış tek İsviçre müzesi. Muazzam bir Asya, Afrika ve Amerika kıtası koleksiyonuna sahiptir.",
        "description_en": "The only art museum in Switzerland dedicated to non-European cultures, set in a historic park with a stunning modern emerald-glass entrance.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Müzenin 'Smaragd' lakaplı cam girişi mimari açıdan çok etkileyicidir.",
        "tips_en": "The futuristic 'Smaragd' glass pavilion entrance is a stark and beautiful contrast to the historic villas."
    },
    {
        "name": "Widder Bar",
        "name_en": "Widder Bar",
        "area": "City",
        "category": "Bar",
        "tags": ["kokteyl", "caz", "lüks", "kütüphane"],
        "distanceFromCenter": 0.3,
        "lat": 47.3725,
        "lng": 8.5397,
        "price": "high",
        "rating": 4.7,
        "description": "250'den fazla viski çeşidi ve harika caz müziğiyle şehrin en sofistike barı. Widder Hotel'in içinde yer alır.",
        "description_en": "A legendary destination for spirits and jazz lovers, featuring over 250 varieties of single malt whiskies and top-tier mixology.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Dünya standartlarında kokteyller için barmenlerden tavsiye almaktan çekinmeyin.",
        "tips_en": "Ask the expert bartenders for a custom creation; their knowledge of spirits is unmatched in Zurich."
    },
    {
        "name": "Old Crow",
        "name_en": "Old Crow Bar",
        "area": "Altstadt",
        "category": "Bar",
        "tags": ["viski", "butik", "samimi", "kokteyl"],
        "distanceFromCenter": 0.3,
        "lat": 47.3719,
        "lng": 8.5408,
        "price": "high",
        "rating": 4.8,
        "description": "Viski meraklıları için bir hac mekanı. 1600'den fazla nadir içki çeşidiyle Zürih'in en özel barlarından biri.",
        "description_en": "A true pilgrimage site for spirits connoisseurs, boasting a collection of over 1,600 rare bottles in a cozy, professional setting.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Menü devasadır, ne sevdiğinizi söyleyin porsiyonlar halinde tadım yapabilirsiniz.",
        "tips_en": "The menu is extensive; tell the staff your flavor preference and let them guide you through the rare selections."
    },
    {
        "name": "Clouds (Prime Tower)",
        "name_en": "Clouds Bar",
        "area": "Zürich West",
        "category": "Bar",
        "tags": ["manzara", "gökdelen", "lüks", "rooftop"],
        "distanceFromCenter": 2.5,
        "lat": 47.3858,
        "lng": 8.5173,
        "price": "high",
        "rating": 4.5,
        "description": "Zürih West'in kalbinde, 35. katta yer alan, şehrin en iyi rooftop barlarından biri. Panoramik manzara eşliğinde içki içmek için ideal.",
        "description_en": "Located on the 35th floor of the Prime Tower, offering breathtaking views over Zurich's industrial west and the city skyline.",
        "imageUrl": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Bar kısmına girmek restorana göre daha kolaydır, pencere kenarı için erken gidin.",
        "tips_en": "The bar area is generally easier to access than the restaurant; arrive early for prime window seats."
    },
    {
        "name": "Sternen Grill",
        "name_en": "Sternen Grill",
        "area": "Bellevue",
        "category": "Restoran",
        "tags": ["sosis", "bratwurst", "ikonik", "hızlı yemek"],
        "distanceFromCenter": 0.5,
        "lat": 47.3667,
        "lng": 8.5447,
        "price": "medium",
        "rating": 4.4,
        "description": "Zürih'in en meşhur sosisçisi. Bellevue meydanında bir sandviç bratwurst yemek tam bir yerel gelenektir.",
        "description_en": "A culinary institution at Bellevue. Famous for its St. Galler Bratwurst served with a crispy gold Bürli roll and fiery mustard.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Öğle yemeği veya Gece atıştırmalığı",
        "bestTime_en": "Lunch or late night snack",
        "tips": "Hardalları çok acıdır (Bürli hardalı), sadece bir tutam sürmeniz yeterli olacaktır.",
        "tips_en": "Beware: their signature mustard is legendary for its extreme heat use it sparingly!"
    },
    {
        "name": "Haus Hiltl (Dünyanın İlk Vejetaryen Restoranı)",
        "name_en": "Haus Hiltl",
        "area": "City",
        "category": "Restoran",
        "tags": ["vejetaryen", "tarihi", "büfe", "vegan"],
        "distanceFromCenter": 0.3,
        "lat": 47.3732,
        "lng": 8.5367,
        "price": "medium",
        "rating": 4.6,
        "description": "1898'de açılan ve dünyanın en eski vejetaryen restoranı olarak Guinness Rekorlar Kitabı'na giren efsanevi mekan.",
        "description_en": "Founded in 1898, it holds the Guinness World Record for being the oldest continuously open vegetarian restaurant in the world.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Öğle yemeği",
        "bestTime_en": "Lunch",
        "tips": "Yüzlerce çeşit içeren açık büfesinden tabağınızı doldurup ağırlığına göre ödeme yapabilirsiniz.",
        "tips_en": "The massive buffet lets you pay by weight; try the vegetarian version of Zurich's 'Geschnetzeltes'."
    }
]

def enrich_zurih_batch1():
    filepath = 'assets/cities/zurih.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Cleanup fillers in existing highlights
    for h in data.get('highlights', []):
        if "City bölgesinde bulunan dikkat çekici bir nokta" in h['description'] or "zengin tarihine tanıklık eden" in h['description'] or "en romantik köşelerinden" in h['description'] or "kültürel zenginliğinin en güzel örneklerinden" in h['description'] or "sanat sahnesinin nabzını tutan" in h['description'] or "yeşil ciğerlerinden biri" in h['description'] or "karakterini en iyi yansıtan" in h['description']:
             if h['name'] == "Grossmünster":
                 h['description'] = "Zürih'in simgesi ikiz kuleli kilise. 16. yüzyılda Reform hareketlerinin başladığı bu yapı, şehir manzarasını izlemek için en iyi yerdir."
                 h['description_en'] = "The symbolic twin-towered cathedral where the Swiss-German Reformation began. Climbing the Karlsturm offers the best views of the city."
             if h['name'] == "Bahnhofstrasse":
                 h['description'] = "Dünyanın en pahalı ve lüks alışveriş caddelerinden biri. 1.4 km boyunca uzanan cadde, tasarım markaları ve bankalarla doludur."
                 h['description_en'] = "One of the world's most exclusive shopping avenues, stretching 1.4km from the main station to the lake with luxury boutiques."
             if h['name'] == "Uetliberg Mountain":
                 h['description'] = "Zürih'in yerel dağı. Trenle kolayca ulaşılabilen zirvesinden şehri, gölü ve Alpler'i kuş bakışı izleyebilirsiniz."
                 h['description_en'] = "Zurich's local mountain. Accessible by train, it offers a panoramic view of the entire city and the snow-capped Alps."
             if h['name'] == "Lake Zurich (Zürichsee)":
                 h['description'] = "Şehrin kalbindeki masmavi göl. Yazın yüzmek, tekne turu yapmak veya kıyısında yürüyüş yapmak Zürih'in en büyük keyfidir."
                 h['description_en'] = "The pristine blue lake at the heart of the city, perfect for boat cruises, swimming in the summer, or a scenic promenade walk."
             if h['name'] == "Lindenhof":
                 h['description'] = "Eski kentin üzerindeki tarihi tepe. Roma döneminden kalma bu park, Limmat nehri ve Grossmünster'in en iyi manzarasını sunar."
                 h['description_en'] = "An elevated historic park in the Old Town, offering a tranquil escape and the most photographed view of the river and city skyline."
             if h['name'] == "Fraumünster":
                 h['description'] = "Yeşil sivri kulesiyle tanınan tarihi kilise. Marc Chagall'ın tasarladığı büyüleyici vitray pencereleriyle dünya çapında ünlüdür."
                 h['description_en'] = "Famous for its slender blue spire and the world-renowned stained-glass windows designed by artist Marc Chagall."
             if h['name'] == "Kunsthaus Zürich":
                 h['description'] = "İsviçre'nin en önemli sanat müzesi. Monet, Picasso ve Munch gibi ustaların eserlerinin yanı sıra devasa bir modern sanat koleksiyonuna sahiptir."
                 h['description_en'] = "Switzerland's most important art museum, housing masterpieces from the Middle Ages to contemporary art, including Monet and Munch."
             if h['name'] == "Niederdorf":
                 h['description'] = "Eski şehrin araç trafiğine kapalı, hareketli bölgesi. Orta Çağ sokakları, butikleri ve akşamları canlanan bar/restoranlarıyla ünlüdür."
                 h['description_en'] = "The pedestrian heart of the Old Town, filled with narrow alleys, unique shops, and a vibrant nightlife and dining scene."
             if h['name'] == "FIFA World Football Museum":
                 h['description'] = "Futbolun tarihine yolculuk. Orijinal Dünya Kupası'nı görebileceğiniz, interaktif oyunlarla dolu modern bir spor müzesi."
                 h['description_en'] = "An interactive tribute to the world's most popular sport, featuring over 1,000 exhibits and the original FIFA World Cup Trophy."
             if h['name'] == "Lindt Home of Chocolate":
                 h['description'] = "Çikolata tutkunları için bir cennet. 9 metrelik devasa çikolata şelalesi ve sınırsız tadım imkanı sunan modern bir müze."
                 h['description_en'] = "A chocolate lover's dream featuring a 9-meter tall chocolate fountain and an immersive museum with unlimited chocolate tasting."
             if h['name'] == "Zürich Opera House":
                 h['description'] = "Avrupa'nın en iyi opera binalarından biri. Barok mimarisi ve ödüllü performanslarıyla Zürih'in kültür kalbi."
                 h['description_en'] = "A world-class stage for opera and ballet, set in a stunning Neo-Baroque building at the Sechseläutenplatz square."
             if h['name'] == "Zoo Zürich":
                 h['description'] = "Masoala Yağmur Ormanı bölümüyle ünlü, dünyanın en modern hayvanat bahçelerinden biri. Doğal yaşam alanlarına çok yakındır."
                 h['description_en'] = "Ranked among the best in Europe, famous for its massive Masoala Rainforest hall and commitment to nature conservation."
             if h['name'] == "Swiss National Museum (Landesmuseum)":
                 h['description'] = "Şato benzeri görkemli binasında, İsviçre'nin tarihini ve kültürünü Orta Çağ'dan günümüze anlatan en kapsamlı müze."
                 h['description_en'] = "Housed in a fairytale castle, it traces Swiss cultural history from its origins to the present day through fascinating exhibits."
             if h['name'] == "ETH Polybahn":
                 h['description'] = "1889'dan beri hizmet veren nostaljik kırmızı füniküler. Sadece 2 dakikada sizi şehir merkezinden üniversite terasına taşır."
                 h['description_en'] = "A charming 19th-century red funicular that whisks passengers from Central to the ETH university terrace in just over 100 seconds."
             if h['name'] == "Confiserie Sprüngli":
                 h['description'] = "1836'dan beri Zürih'in lüks çikolata ve makaron (Luxemburgerli) simgesi. Paradeplatz'daki merkezi bir klasiktir."
                 h['description_en'] = "The gold standard of Swiss confectionery since 1836, world-famous for their 'Luxemburgerli' macaroons and artisanal chocolates."
             if h['name'] == "Zürich West (Im Viadukt)":
                 h['description'] = "Eski bir demiryolu viyadüğünün kemerleri altına dizilmiş tasarım dükkanları ve gurme yemek pazarıyla modern bir ticaret alanı."
                 h['description_en'] = "A trendy shopping and dining destination built into the historic stone arches of a functional 1894 railway viaduct."
             if h['name'] == "Freitag Flagship Store":
                 h['description'] = "Geri dönüştürülmüş konteynerlerden yapılmış dev kule. Zürih'in dünyaca ünlü markasının simge mağazası ve seyir noktası."
                 h['description_en'] = "An iconic 26-meter tower made of shipping containers, home to the brand's recycled bags and a great industrial viewing platform."
             if h['name'] == "China Garden (Chinagarten)":
                 h['description'] = "Zürih'in partner şehri Kunming'in bir hediyesi. Göl kıyısında, Çin mimarisi ve bitkileriyle huzur dolu bir tapınak bahçesi."
                 h['description_en'] = "A gift from Zurich's Chinese sister city Kunming, this is one of the highest-ranking temple gardens outside China."
             if h['name'] == "Zeughauskeller":
                 h['description'] = "Eski bir cephanelik binasında hizmet veren tarihi restoran. Geleneksel İsviçre yemeklerini otantik bir atmosferde sunar."
                 h['description_en'] = "Set in a former 15th-century arsenal, this historic restaurant serves hearty Swiss classics like veal with creamy mushroom sauce."
             if h['name'] == "Rheinfall (Günübirlik)":
                 h['description'] = "Avrupa'nın en büyük şelalesi. Zürih'ten kısa bir yolculukla ulaşılan bu doğa harikasında suyun gücünü tekneyle yakından hissedin."
                 h['description_en'] = "Europe's most powerful waterfall. A majestic natural spectacle just a short train ride away from Zurich's city center."
             if h['name'] == "Rapperswil Castle":
                 h['description'] = "Zürih Gölü'nün diğer ucundaki 'Güller Şehri'. Orta Çağ şatosu ve 600'den fazla çeşit barındıran gül bahçeleriyle ünlüdür."
                 h['description_en'] = "The 'City of Roses' located at the upper end of the lake, featuring a 13th-century castle and beautiful Mediterranean-style gardens."
             if h['name'] == "Chapel Bridge, Lucerne":
                 h['description'] = "İsviçre'nin en çok fotoğraflanan noktalarından biri. 45 dakikalık bir tren yolculuğuyla ulaşabileceğiniz masalsı bir Orta Çağ köprüsü."
                 h['description_en'] = "The iconic wooden bridge and water tower of Lucerne, easily visited as a day trip from Zurich for a quintessential Swiss experience."
             if h['name'] == "Titlis Dağı (Günübirlik)":
                 h['description'] = "Dönen teleferikle 3000 metreye tırmanın. Yaz kış kar görebileceğiniz, buzul mağarası ve asma köprüsüyle tam bir macera dağı."
                 h['description_en'] = "A glacier paradise at 3,020 meters above sea level, home to the world’s first revolving cable car and the highest suspension bridge in Europe."
             if h['name'] == "Stein am Rhein (Günübirlik)":
                 h['description'] = "Duvarları bütünüyle fresklerle kaplı binalarıyla ünlü, İsviçre'nin en iyi korunmuş Orta Çağ kasabalarından biri."
                 h['description_en'] = "A fairytale medieval town on the Rhine, famous for its intact old center and buildings with stunningly painted facades."
             if h['name'] == "Hiltl":
                 h['description'] = "Dünyanın en eski vejetaryen restoranı. Guinness Rekorlar Kitabı'na giren bu devasa mekan, sağlıklı ve lezzetli açık büfesiyle ünlüdür."
                 h['description_en'] = "The world's first vegetarian restaurant (est. 1898), offering a massive buffet that attracts even the most dedicated meat-lovers."
             if h['name'] == "Jules Verne Panoramabar":
                 h['description'] = "Eski bir gözlemevi kulesinin içinde yer alan, 360 derece şehir manzarasına sahip en şık kokteyl barı."
                 h['description_en'] = "Located in a former observatory tower, this bar offers a magical 360-degree panoramic view of the city skyline and lake."
             if h['name'] == "Botanical Garden (University of Zurich)":
                 h['description'] = "Gelecekten gelmiş gibi duran üç devasa cam kubbesiyle ünlü, nadide tropikal bitkilerin sergilendiği bir doğa laboratuvarı."
                 h['description_en'] = "Famous for its futuristic glass domes, it houses flora from all over the world in different climatic zones."
             if h['name'] == "Sechseläutenplatz":
                 h['description'] = "Zürih'in en büyük kent meydanı. Göl ile Operayı birleştiren bu alan, film festivalleri ve Noel pazarlarının ev sahibidir."
                 h['description_en'] = "Zurich's largest city square, a noble stone plaza that hosts grand events, film festivals, and the magical Christmas market."
             if h['name'] == "Langstrasse":
                 h['description'] = "Şehrin en kozmopolit ve renkli bölgesi. Gece hayatı, sokak yemekleri ve Zürih'in alternatif yüzünü keşfetmek için ideal."
                 h['description_en'] = "Zurich's multicultural heart, where gritty nightlife meets hip cafes, offering the city's most diverse social atmosphere."
             if h['name'] == "Focus Terra":
                 h['description'] = "Dünyanın oluşumunu ve jeolojiyi interaktif bir şekilde anlatan, özellikle deprem simülatörüyle ünlü modern bir bilim müzesi."
                 h['description_en'] = "A fascinating interactive research museum for earth sciences, featuring a high-tech earthquake simulator and towering crystals."
             if h['name'] == "Rieter Park & Museum":
                 h['description'] = "Göl manzaralı dev bir park içinde yer alan, Avrupa dışı sanat eserlerine adanmış İsviçre'nin en huzurlu müze komplekslerinden biri."
                 h['description_en'] = "A museum for non-European art set in a sprawling hilltop park with centuries-old trees and a clear view of the Glarus Alps."
             if h['name'] == "Beyer Clock and Watch Museum":
                 h['description'] = "Zamanın tarihine yolculuk. Dünyanın en nadide saat koleksiyonlarından birini Bahnhofstrasse'deki bir butiğin altında keşfedin."
                 h['description_en'] = "One of the world's leading horological collections, showcasing timekeeping history from sundials to futuristic atomic clocks."
             if h['name'] == "Cabaret Voltaire":
                 h['description'] = "1916'da Dadaist sanat akımının doğduğu yer. Bugün hem bir sergi alanı hem de avangart bir kafe/bar olarak hizmet verir."
                 h['description_en'] = "The birthplace of the world-famous Dada art movement in 1916, still serving as a hub for artistic experimentation and avant-garde culture."
             if h['name'] == "Thermalbad & Spa Zürich":
                 h['description'] = "Eski bir bira fabrikasının içinde, çatısındaki göl manzaralı havuzu ve antik taş tonozlarıyla şehrin en lüks spa deneyimi."
                 h['description_en'] = "Housed in a former brewery, this spa features antique stone vaults and a spectacular rooftop infinity pool with views over the whole city."
             if h['name'] == "Münsterhof":
                 h['description'] = "Fraumünster'in önündeki tarihi meydan. Araç trafiğine kapatıldıktan sonra şık kafeleriyle şehrin en zarif dinlenme noktalarından biri oldu."
                 h['description_en'] = "A noble pedestrian square surrounded by guild houses, once a pig market and now the site of elegant outdoor dining and markets."
             if h['name'] == "B2 Hotel Wine Library":
                 h['description'] = "Eski bir bira fabrikasının kütüphane-bara dönüştürülmüş hali. Binlerce kitap ve dev avizeler eşliğinde şarap tadımı yapabilirsiniz."
                 h['description_en'] = "A stunning hotel lobby lounge featuring 33,000 books on floor-to-ceiling shelves and dramatic chandeliers made of beer bottles."
             if h['name'] == "Bellevue":
                 h['description'] = "Gölün nehirle birleştiği devasa kavşak ve meydan. Tramvayların düğüm noktası olan bu yer, günün her saati hareketli ve canlıdır."
                 h['description_en'] = "The busy lakefront transportation hub where the river meets Lake Zurich, packed with kiosks, restaurants, and people-watching spots."

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_zurih_batch1:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_zurih_batch1()
print(f"Zurich now has {count} highlights.")
