import json

# Manual enrichment data (Lucerne - ALL 50 items)
updates = {
    "Chapel Bridge (Kapellbrücke)": {
        "description": "Avrupa'nın en eski ahşap kapalı köprüsü, 17. yüzyıl resimleriyle süslü. 1333'ten beri Luzern'in simgesi, Su Kulesi ile birlikte.",
        "description_en": "Europe's oldest covered wooden bridge decorated with 17th-century paintings. Lucerne's symbol since 1333, together with Water Tower."
    },
    "Lion Monument": {
        "description": "Fransız Devrimi'nde ölen İsviçre muhafızlarını anmak için kayaya oyulmuş ölmekte olan aslan. Mark Twain'in 'dünyanın en hüzünlü heykeli' dediği anıt.",
        "description_en": "Dying lion carved into rock commemorating Swiss guards killed in French Revolution. Monument Mark Twain called 'world's saddest statue'."
    },
    "Musegg Wall": {
        "description": "Ortaçağ'dan kalma şehir surları ve dokuz kule, bazıları tırmanılabilir. Panoramik şehir ve göl manzarası, tarihi yürüyüş.",
        "description_en": "Medieval city walls and nine towers, some climbable. Panoramic city and lake views, historic walk."
    },
    "Mount Pilatus": {
        "description": "Luzern'in efsanevi dağı, dünyanın en dik dişli tren yolu. Dragon yolu, göl manzarası ve İsviçre Alpleri panoraması.",
        "description_en": "Lucerne's legendary mountain with world's steepest cogwheel railway. Dragon path, lake views, and Swiss Alps panorama."
    },
    "Mount Rigi": {
        "description": "Alplerin kraliçesi, İsviçre'nin ilk dağ turizm noktası. Gün doğumu turu, kış sporları ve göller manzarası.",
        "description_en": "Queen of the Alps, Switzerland's first mountain tourism destination. Sunrise tour, winter sports, and lakes panorama."
    },
    "Lake Lucerne Boat Tour": {
        "description": "Vierwaldstättersee'de nostaljik buharlı gemi veya modern tekne turu. Alp manzaraları, köy durakları ve İsviçre romantizmi.",
        "description_en": "Nostalgic steamboat or modern boat tour on Lake Lucerne. Alpine scenery, village stops, and Swiss romanticism."
    },
    "Swiss Museum of Transport": {
        "description": "İsviçre'nin en popüler müzesi, ulaşım tarihi ve interaktif sergiler. Trenler, uçaklar, planetaryum ve aileler için ideal.",
        "description_en": "Switzerland's most popular museum with transport history and interactive exhibits. Trains, planes, planetarium, and ideal for families."
    },
    "Rosengart Collection": {
        "description": "Picasso ve Paul Klee'nin önemli eserlerini barındıran sanat müzesi. 300'den fazla modern sanat eseri, özel koleksiyon.",
        "description_en": "Art museum housing important works by Picasso and Paul Klee. Over 300 modern art pieces, private collection."
    },
    "Jesuit Church": {
        "description": "İsviçre'nin ilk büyük barok kilisesi, beyaz iç mekan ve süslemeli tavan. River Reuss kıyısında, dini mimari şaheseri.",
        "description_en": "Switzerland's first large Baroque church with white interior and ornate ceiling. On River Reuss, religious architectural masterpiece."
    },
    "KKL Luzern": {
        "description": "Jean Nouvel tasarımı çok amaçlı kültür merkezi, konser salonu ve müzeler. Çağdaş mimari, göl manzarası ve akustik.",
        "description_en": "Jean Nouvel-designed multi-purpose culture center with concert hall and museums. Contemporary architecture, lake views, and acoustics."
    },
    "Glacier Garden": {
        "description": "20 milyon yıllık buzul kalıntıları ve ayna labirenti. Jeoloji müzesi, palmiye fosilleri ve aileler için eğlence.",
        "description_en": "20-million-year-old glacier remains and mirror labyrinth. Geology museum, palm fossils, and fun for families."
    },
    "Bourbaki Panorama": {
        "description": "1871 Fransız-Prusya Savaşı'nı gösteren dev dairesel resim. 100 metre çapında, 3D efekt ve tarihsel drama.",
        "description_en": "Giant circular painting depicting 1871 Franco-Prussian War. 100 meters diameter, 3D effect, and historical drama."
    },
    "Spreuer Bridge": {
        "description": "Kapellbrücke'den sonra ikinci tarihi ahşap köprü, Ölüm Dansı resimleriyle. 1408'den beri, karanlık sanat ve nehir geçişi.",
        "description_en": "Second historic wooden bridge after Kapellbrücke with Dance of Death paintings. Since 1408, dark art, and river crossing."
    },
    "Old Town Squares": {
        "description": "Luzern'in tarihi meydanları, fresk süslemeli binalar ve çeşmeler. Kornmarkt, Weinmarkt ve lonca evleriyle ortaçağ atmosferi.",
        "description_en": "Lucerne's historic squares with fresco-decorated buildings and fountains. Kornmarkt, Weinmarkt, and medieval atmosphere with guild houses."
    },
    "Richard Wagner Museum": {
        "description": "Besteci Richard Wagner'in 6 yıl yaşadığı göl kenarı villası. Tribschen'de müze, müzik tarihi ve romantik konum.",
        "description_en": "Lakeside villa where composer Richard Wagner lived for 6 years. Museum in Tribschen, music history, and romantic location."
    },
    "Chateau Guetsch": {
        "description": "Tepede masal şatosu görünümlü otel-restoran, şehir panoraması. Füniküler ile ulaşım, romantik yemek ve İsviçre lüksü.",
        "description_en": "Fairy-tale castle-looking hotel-restaurant on hill with city panorama. Funicular access, romantic dining, and Swiss luxury."
    },
    "Wirtshaus Galliker": {
        "description": "1856'dan beri hizmet veren geleneksel İsviçre restoranı. Zürcher geschnetzeltes, rösti ve yerel bira.",
        "description_en": "Traditional Swiss restaurant serving since 1856. Zürcher geschnetzeltes, rösti, and local beer."
    },
    "Old Swiss House": {
        "description": "İkonik odun panelli restoran, masa başında schnitzel hazırlama. 1859'dan beri, İsviçre mutfağı ve turist favorisi.",
        "description_en": "Iconic wood-paneled restaurant with tableside schnitzel preparation. Since 1859, Swiss cuisine, and tourist favorite."
    },
    "Mill'Feuille": {
        "description": "Fransız pastalarıyla ünlü butik kafe, croissant ve tart. Artisan ekmek, şık atmosfer ve kahve kültürü.",
        "description_en": "Boutique cafe famous for French pastries, croissants, and tarts. Artisan bread, elegant atmosphere, and coffee culture."
    },
    "Rathaus Brauerei": {
        "description": "Belediye binasının yanındaki bira fabrikası-restoran. Taze bira, İsviçre yemekleri ve nehir kenarı terası.",
        "description_en": "Brewery-restaurant next to city hall. Fresh beer, Swiss dishes, and riverside terrace."
    },
    "Manor Department Store": {
        "description": "İsviçre department store zinciri, moda ve ev eşyaları. Çatı terası restoran, şehir merkezinde alışveriş.",
        "description_en": "Swiss department store chain with fashion and home goods. Rooftop restaurant, city center shopping."
    },
    "Max Chocolatier": {
        "description": "El yapımı İsviçre çikolatası ustası, truffle ve pralin. Tadım oturumları, hediye kutuları ve gurme lezzet.",
        "description_en": "Handmade Swiss chocolate master with truffles and pralines. Tasting sessions, gift boxes, and gourmet flavor."
    },
    "Bachmann": {
        "description": "Geleneksel İsviçre pastanesi, patlama bonbonları ve tatlılar. Yerel favorisi, kahve eşliği ve nostaljik mekan.",
        "description_en": "Traditional Swiss pastry shop with explosion bonbons and desserts. Local favorite, coffee pairing, and nostalgic venue."
    },
    "Heini": {
        "description": "1957'den beri hizmet veren İsviçre konditörü, Luzerner Lebkuchen. Meringue, tatlılar ve şehir merkezinde mola.",
        "description_en": "Swiss confectioner serving since 1957 with Luzerner Lebkuchen. Meringue, desserts, and city center break."
    },
    "Villa Schweizerhof": {
        "description": "Göl kenarında tarihi lüks otel, klasik İsviçre misafirperverliği. 1845'ten beri, zarif odalar ve panoramik manzara.",
        "description_en": "Historic luxury hotel on lake with classic Swiss hospitality. Since 1845, elegant rooms, and panoramic views."
    },
    "Grottino 1313": {
        "description": "Ortaçağ mahzeninde İtalyan restoranı, atmosferik yemek deneyimi. Makarna, pizza ve romantik akşam yemeği.",
        "description_en": "Italian restaurant in medieval cellar, atmospheric dining experience. Pasta, pizza, and romantic dinner."
    },
    "Burgerstube": {
        "description": "Şehrin en iyi burgerleri, yaratıcı kombinasyonlar ve craft bira. Modern casual, yerel et ve gece mola.",
        "description_en": "City's best burgers with creative combinations and craft beer. Modern casual, local meat, and night break."
    },
    "Mount Titlis": {
        "description": "Orta İsviçre'nin en yüksek zirvesi, döner teleferik (Rotair). Buzul mağarası, asma köprü ve karla kaplı macera.",
        "description_en": "Central Switzerland's highest peak with rotating cable car (Rotair). Glacier cave, suspension bridge, and snow-covered adventure."
    },
    "Inseli Park": {
        "description": "Göl kenarında şehir parkı, piknik alanları ve sahil yürüyüşü. Aileler için yeşil alan, oyun parkı ve dinlenme.",
        "description_en": "Lakeside city park with picnic areas and shore walk. Green area for families, playground, and relaxation."
    },
    "Ufschotti": {
        "description": "Yaz aylarında göl kıyısı aktiviteleri, konserler ve açık hava etkinlikleri. Gençler için buluşma noktası, gün batımı.",
        "description_en": "Summer lakeside activities, concerts, and outdoor events. Meeting point for youth, sunset."
    },
    "Hammetschwand Lift": {
        "description": "Avrupa'nın en yüksek açık hava asansörü, Bürgenstock'ta konumlu. 152 metre, göl manzarası ve mühendislik harikası.",
        "description_en": "Europe's highest open-air elevator located at Bürgenstock. 152 meters, lake views, and engineering marvel."
    },
    "Buergenstock Resort": {
        "description": "Dağ tepesinde lüks resort, göl manzarası ve wellness. Audrey Hepburn'ün düğün yeri, spa ve İsviçre lüksü.",
        "description_en": "Luxury resort on mountain top with lake views and wellness. Audrey Hepburn's wedding venue, spa, and Swiss luxury."
    },
    "Sammlung Rosengart": {
        "description": "Picasso ve Klee'nin önemli eserlerinin bulunduğu özel sanat koleksiyonu. 200'den fazla eser, modern sanat ve müze.",
        "description_en": "Private art collection with important works of Picasso and Klee. Over 200 works, modern art, and museum."
    },
    "Hofkirche": {
        "description": "Luzern'in ana kilisesi, Rönesans cephesi ve gotik iç mekan. Saint Leodegar'a adanmış, organ konserleri.",
        "description_en": "Lucerne's main church with Renaissance facade and Gothic interior. Dedicated to Saint Leodegar, organ concerts."
    },
    "Nadelwehr": {
        "description": "Reuss Nehri'ndeki tarihi ahşap seti, su seviyesi kontrolü. Mühendislik mirası, nehir manzarası ve fotoğrafçılık.",
        "description_en": "Historic wooden needle weir on Reuss River for water level control. Engineering heritage, river views, and photography."
    },
    "Two Hands": {
        "description": "Avustralya tarzı specialty kahve ve brunch mekanı. Flat white, avokado tost ve genç kalabalık.",
        "description_en": "Australian-style specialty coffee and brunch venue. Flat white, avocado toast, and young crowd."
    },
    "Alpineum": {
        "description": "Alp manzarası temalı eski panorama müzesi, 3D dağ dioramaları. Nostaljik turizm ve İsviçre dağları.",
        "description_en": "Old panorama museum with Alpine scenery theme and 3D mountain dioramas. Nostalgic tourism and Swiss mountains."
    },
    "Seebad Luzern": {
        "description": "Göl üzerinde yüzen ahşap yüzme alanı, yaz aktivitesi. Güneşlenme, dalma ve şehir içi plaj.",
        "description_en": "Floating wooden swimming area on lake for summer activity. Sunbathing, diving, and urban beach."
    },
    "Treibhaus": {
        "description": "Alternatif kültür merkezi, canlı müzik ve bar. Konserler, DJ geceleri ve genç kültürü.",
        "description_en": "Alternative culture center with live music and bar. Concerts, DJ nights, and youth culture."
    },
    "Werkstatt": {
        "description": "Endüstriyel tasarımlı bar ve kafe, craft kokteyller. Gece hayatı, sosyal atmosfer ve modern mekan.",
        "description_en": "Industrial-design bar and cafe with craft cocktails. Nightlife, social atmosphere, and modern venue."
    },
    "Penthouse Bar": {
        "description": "Şehir manzaralı çatı barı, premium kokteyller ve gece eğlencesi. Montana Hotel'de, sofistike atmosfer.",
        "description_en": "Rooftop bar with city views, premium cocktails, and night entertainment. At Montana Hotel, sophisticated atmosphere."
    },
    "Louis Bar": {
        "description": "Tarihi otel barı, klasik kokteyller ve zarif atmosfer. Palace Luzern'de, nostalji ve lüks.",
        "description_en": "Historic hotel bar with classic cocktails and elegant atmosphere. At Palace Luzern, nostalgia, and luxury."
    },
    "Bodu": {
        "description": "Modern Asya mutfağı sunan şık restoran, sushi ve dim sum. Fusion lezzetler, sofistike ortam.",
        "description_en": "Elegant restaurant serving modern Asian cuisine with sushi and dim sum. Fusion flavors, sophisticated setting."
    },
    "Brasserie Bodu": {
        "description": "Fransız tarzı brasserie, bistro klasikleri ve şarap. Steak frites, casual fine-dining ve romantik yemek.",
        "description_en": "French-style brasserie with bistro classics and wine. Steak frites, casual fine-dining, and romantic dining."
    },
    "Schiff": {
        "description": "Gölün kıyısında geleneksel İsviçre restoranı, balık ve et. Terrasa manzarası, aile yemekleri ve yerel lezzet.",
        "description_en": "Traditional Swiss restaurant on lakeside with fish and meat. Terrace views, family meals, and local flavor."
    },
    "Pfistern": {
        "description": "Tarihi binada restoran ve bar, İsviçre ve uluslararası mutfak. Nehir manzarası, tarihi atmosfer.",
        "description_en": "Restaurant and bar in historic building with Swiss and international cuisine. River views, historic atmosphere."
    },
    "Zunfthaus zu Pfistern": {
        "description": "Ortaçağ lonca evinde gastronomi, geleneksel İsviçre yemekleri. Tarihi mekan, özel etkinlikler ve lüks.",
        "description_en": "Gastronomy in medieval guild house with traditional Swiss dishes. Historic venue, private events, and luxury."
    },
    "Wochentagsmarkt": {
        "description": "Haftalık çiftçi pazarı, taze ürünler ve yerel spesiyaliteler. Bahnhofstrasse'de, İsviçre malzemeleri ve pazar kültürü.",
        "description_en": "Weekly farmers' market with fresh produce and local specialties. On Bahnhofstrasse, Swiss ingredients, and market culture."
    },
    "Fasnacht": {
        "description": "Luzern karnavalı, renkli geçitler ve maskeler. Her yıl Şubat-Mart, İsviçre'nin en büyük festivali.",
        "description_en": "Lucerne carnival with colorful parades and masks. Every February-March, Switzerland's biggest festival."
    },
    "Shamrock Irish Pub": {
        "description": "Authentic İrlanda pub'ı, canlı müzik ve Guinness. Spor maçları, sosyal atmosfer ve gece hayatı.",
        "description_en": "Authentic Irish pub with live music and Guinness. Sports matches, social atmosphere, and nightlife."
    }
}

filepath = 'assets/cities/lucerne.json'
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

print(f"\n✅ Manually enriched {count} items (Lucerne - COMPLETE).")
