import json

# Manual enrichment data (Tromso Batch 1: 40 items)
updates = {
    "Kurbadet": {
        "description": "Tarihi kaplıca binası, kültürel etkinliklere ve sergilere ev sahipliği yapıyor. Art nouveau mimarisi, şehir merkezi ve topluluk mekanı.",
        "description_en": "Historic spa building hosting cultural events and exhibitions. Art nouveau architecture, city center, and community venue."
    },
    "Rådstua Teaterhus": {
        "description": "Tromsø'nun tarihi tiyatro binası, konserler ve performanslar. Norveç sanatı, kültür geceleri ve yerel prodüksiyonlar.",
        "description_en": "Tromsø's historic theater building with concerts and performances. Norwegian art, culture nights, and local productions."
    },
    "Skansen Fort": {
        "description": "18. yüzyıldan kalma tarihi kale kalıntısı, şehir manzarası ve tarihi yürüyüş. Norveç savunma tarihi, fotoğrafçılık ve keşif.",
        "description_en": "18th-century historic fort remains with city views and historic walk. Norwegian defense history, photography, and exploration."
    },
    "Tromsø Torg": {
        "description": "Şehir merkezinin ana meydanı, alışveriş, kafeler ve buluşma noktası. Yerel yaşam, pazar günleri ve sosyal sahne.",
        "description_en": "Main square of city center with shopping, cafes, and meeting point. Local life, market days, and social scene."
    },
    "Prostneset": {
        "description": "Limanın burnundaki manzara noktası, fiyort panoraması ve gün batımı. Fotoğrafçılık, yürüyüş ve arktik manzara.",
        "description_en": "Viewpoint at harbor tip with fjord panorama and sunset. Photography, walking, and Arctic scenery."
    },
    "Kongsparken": {
        "description": "Şehir merkezindeki yeşil park, heykeller ve dinlenme alanları. Piknik, yürüyüş ve şehir oazı.",
        "description_en": "Green park in city center with sculptures and rest areas. Picnic, walking, and city oasis."
    },
    "Tromsøya": {
        "description": "Tromsø'nun kurulduğu ana ada, şehir merkezini ve ana turistik noktaları barındırır. Kültür, tarih ve arktik yaşam.",
        "description_en": "Main island where Tromsø is founded, hosting city center and main tourist points. Culture, history, and Arctic life."
    },
    "Fangstmonumentet": {
        "description": "Avcılık ve balıkçılık geleneğini onurlandıran anıt heykel. Norveç denizci tarihi, kültürel sembol ve fotoğraf noktası.",
        "description_en": "Monument honoring hunting and fishing tradition. Norwegian maritime history, cultural symbol, and photo spot."
    },
    "Kirkeparken": {
        "description": "Domkirke etrafındaki park alanı, ağaçlık yollar ve şehir molası. Tarihi kilise, huzurlu ortam ve merkezi konum.",
        "description_en": "Park area around Domkirke with tree-lined paths and city break. Historic church, peaceful setting, and central location."
    },
    "Tromsø Rådhus (City Hall)": {
        "description": "Modernist belediye binası, kamu hizmetleri ve şehir yönetimi. 1960'lar mimarisi, şehir meydanı ve resmi yapı.",
        "description_en": "Modernist city hall with public services and city administration. 1960s architecture, city square, and official building."
    },
    "Aurora Kino Fokus": {
        "description": "Şehrin modern sinema kompleksi, uluslararası ve Norveç filmleri. Film geceleri, popcorn ve kültür.",
        "description_en": "City's modern cinema complex with international and Norwegian films. Movie nights, popcorn, and culture."
    },
    "Tromsø Gallery of Contemporary Art": {
        "description": "Çağdaş Norveç ve uluslararası sanat sergileri. Modern sanat, dönemsel sergiler ve kültürel buluşma.",
        "description_en": "Contemporary Norwegian and international art exhibitions. Modern art, periodic exhibitions, and cultural meeting."
    },
    "Small Projects": {
        "description": "Bağımsız sanat galerisi ve alternatif sanat mekanı. Yerel sanatçılar, deneysel çalışmalar ve kültür.",
        "description_en": "Independent art gallery and alternative art venue. Local artists, experimental works, and culture."
    },
    "Tromsø Souvenir Shop": {
        "description": "Norveç hediyelik eşyaları ve Tromsø hatıraları. Vikting temalı ürünler, yerel el sanatları ve turist mağazası.",
        "description_en": "Norwegian souvenirs and Tromsø memorabilia. Viking-themed products, local handicrafts, and tourist shop."
    },
    "Jekta Storsenter": {
        "description": "Kuzey Norveç'in en büyük alışveriş merkezi, markalar ve restoranlar. Aile alışverişi, sinema ve hafta sonu aktivitesi.",
        "description_en": "Northern Norway's largest shopping mall with brands and restaurants. Family shopping, cinema, and weekend activity."
    },
    "Galleri Nord": {
        "description": "Kuzey Norveç sanatçılarının eserlerini sergileyen galeri. Arktik sanat, yerel üretim ve kültürel miras.",
        "description_en": "Gallery exhibiting works of Northern Norwegian artists. Arctic art, local production, and cultural heritage."
    },
    "Krane Art Gallery": {
        "description": "Çağdaş sanat galerisi, resim ve heykel sergileri. Norveç ve uluslararası sanatçılar, satış ve koleksiyon.",
        "description_en": "Contemporary art gallery with painting and sculpture exhibitions. Norwegian and international artists, sales and collection."
    },
    "Wabi Sabi Jewellery": {
        "description": "El yapımı takı ve mücevherat dükkanı, Norveç tasarımı. Gümüş, doğal taşlar ve yerel zanaatkarlar.",
        "description_en": "Handmade jewelry shop with Norwegian design. Silver, natural stones, and local craftsmen."
    },
    "Ludwig Mack Statue": {
        "description": "Mack Bira'nın kurucusu Ludwig Mack'in anıt heykeli. Yerel tarih, bira mirası ve şehir simgesi.",
        "description_en": "Monument statue of Ludwig Mack, founder of Mack Brewery. Local history, beer heritage, and city symbol."
    },
    "Magic Ice Bar Tromsø": {
        "description": "Tamamen buzdan yapılmış bar, buz heykelleri ve soğuk kokteyller. Benzersiz deneyim, ısıtmalı kıyafetler ve kış büyüsü.",
        "description_en": "Bar made entirely of ice with ice sculptures and cold cocktails. Unique experience, heated clothing, and winter magic."
    },
    "Tromsø Kjøtt": {
        "description": "Yerel et ürünleri ve Norveç gastronomisi sunan restoran. Ren geyiği, balina ve arktik lezzetler.",
        "description_en": "Restaurant serving local meat products and Norwegian gastronomy. Reindeer, whale, and Arctic flavors."
    },
    "Graffi Grill": {
        "description": "Casual burger ve grill restoranı, hızlı servis ve lezzetli yemekler. Öğle yemeği, aileler ve pratik seçenek.",
        "description_en": "Casual burger and grill restaurant with quick service and tasty food. Lunch, families, and practical option."
    },
    "Tromsø Mikrobryggeri": {
        "description": "Yerel craft bira üretim tesisi ve tadım barı. Arktik biracılık, taze içecekler ve bira kültürü.",
        "description_en": "Local craft beer production facility and tasting bar. Arctic brewing, fresh drinks, and beer culture."
    },
    "Art of the Arctic": {
        "description": "Arktik temalı sanat ve hediyelik eşya dükkanı. Kuzey Işıkları baskıları, Sami sanatı ve Norveç tasarımı.",
        "description_en": "Arctic-themed art and souvenir shop. Northern Lights prints, Sami art, and Norwegian design."
    },
    "Husfliden Tromsø": {
        "description": "Geleneksel Norveç el sanatları ve folklor ürünleri mağazası. Örme giyisiler, ahşap işler ve ulusal kostümler.",
        "description_en": "Traditional Norwegian handicrafts and folklore products store. Knitted clothing, woodwork, and national costumes."
    },
    "Reimper's": {
        "description": "Liman bölgesinde deniz ürünleri ve Norveç mutfağı sunan şık restoran. Taze balık, romantik yemekler ve liman manzarası.",
        "description_en": "Elegant restaurant serving seafood and Norwegian cuisine in harbor area. Fresh fish, romantic dining, and harbor views."
    },
    "Tromsø Domkirke Park": {
        "description": "Norveç'in en kuzey katedrali çevresindeki park alanı. Ahşap kilise, tarihi mezarlık ve huzurlu yürüyüş.",
        "description_en": "Park area around Norway's northernmost cathedral. Wooden church, historic cemetery, and peaceful walk."
    },
    "Arctic Cathedral (Night)": {
        "description": "Gece aydınlatmasında Arktik Katedrali'nin görüntüsü, ikonik fotoğraf anı. Yıldızlar, Kuzey Işıkları arka planı ve mimari.",
        "description_en": "Arctic Cathedral view in night lighting, iconic photo moment. Stars, Northern Lights background, and architecture."
    },
    "Tromsø Bridge (Pedestrian Walk)": {
        "description": "Tromsøbrua üzerinden yaya yürüyüşü, fiyort ve şehir manzarası. Günün her saati güzel, fotoğrafçılık ve spor.",
        "description_en": "Pedestrian walk over Tromsøbrua with fjord and city views. Beautiful at all hours, photography, and sport."
    },
    "Tromsø Geist": {
        "description": "Alternatif gece kulübü ve canlı müzik mekanı. DJ geceleri, konserler ve genç kalabalık.",
        "description_en": "Alternative nightclub and live music venue. DJ nights, concerts, and young crowd."
    },
    "Norges Råfisklag": {
        "description": "Norveç'in ham balık kooperatifi binası, balıkçılık tarihi ve ekonomi. Endüstriyel miras ve yerel yaşam.",
        "description_en": "Norwegian raw fish cooperative building with fishing history and economy. Industrial heritage and local life."
    },
    "Varden": {
        "description": "Tromsøya'nın en yüksek noktası, panoramik şehir ve fiyort manzarası. Kolay tırmanış, fotoğrafçılık ve açık hava.",
        "description_en": "Highest point of Tromsøya with panoramic city and fjord views. Easy climb, photography, and outdoors."
    },
    "Ornfløya": {
        "description": "Kartal tepesi anlamına gelen zirve, zorlu trekking ve muhteşem manzara. Outdoor macera, dağ yürüyüşü ve doğa.",
        "description_en": "Peak meaning 'Eagle Mountain' for challenging trekking and magnificent views. Outdoor adventure, mountain hiking, and nature."
    },
    "Skulsfjord": {
        "description": "Tromsø yakınındaki fiyort, balıkçılık ve doğa aktiviteleri. Tekne turları, balık tutma ve arktik manzara.",
        "description_en": "Fjord near Tromsø for fishing and nature activities. Boat tours, fishing, and Arctic scenery."
    },
    "Tromvik": {
        "description": "Balıkçı köyü, deniz kenarı atmosferi ve yerel yaşam. Kuzey Işıkları gözlem noktası, restoran ve huzur.",
        "description_en": "Fishing village with seaside atmosphere and local life. Northern Lights observation point, restaurant, and peace."
    },
    "Kjølen": {
        "description": "Tromsø yakınındaki dağ bölgesi, kayak ve yürüyüş. Kış sporları, yaz trekkingleri ve arktik doğa.",
        "description_en": "Mountain area near Tromsø for skiing and hiking. Winter sports, summer treks, and Arctic nature."
    },
    "Sandnessundet Bridge": {
        "description": "Kvaløya'yı ana karaya bağlayan köprü, manzaralı sürüş. Fiyort geçişi, fotoğrafçılık ve ulaşım.",
        "description_en": "Bridge connecting Kvaløya to mainland for scenic drive. Fjord crossing, photography, and transport."
    },
    "Nordtinden": {
        "description": "Kuzey tepesi anlamına gelen dağ zirvesi, zorlu tırmanış ve ödüllendirici panorama. Macera, outdoor ve zirveler.",
        "description_en": "Mountain peak meaning 'North Peak' for challenging climb and rewarding panorama. Adventure, outdoor, and summits."
    },
    "Ramfjord": {
        "description": "Tromsø yakınındaki fiyort, balıkçılık ve outdoor aktiviteler. Balık tutma, tekne turları ve doğal güzellik.",
        "description_en": "Fjord near Tromsø for fishing and outdoor activities. Fishing, boat tours, and natural beauty."
    },
    "Oldervik": {
        "description": "Küçük kıyı köyü, deniz kenarı yaşam ve balıkçı geleneği. Sakin ortam, doğa yürüyüşleri ve arktik köy.",
        "description_en": "Small coastal village with seaside life and fishing tradition. Quiet setting, nature walks, and Arctic village."
    }
}

filepath = 'assets/cities/tromso.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data['highlights']:
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        print(f"Enriched: {name}")
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Manually enriched {count} items (Tromso Batch 1).")
