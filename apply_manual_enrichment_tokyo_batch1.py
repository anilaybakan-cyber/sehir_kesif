import json

# Manual enrichment data (Tokyo - ALL 46 items)
updates = {
    "Senso-ji Temple": {
        "description": "Tokyo'nun en eski ve renkli Budist tapınağı, Asakusa'da. Dev kırmızı fener (Kaminarimon), Nakamise alışveriş sokağı ve tütsü dumanı.",
        "description_en": "Tokyo's oldest and most colorful Buddhist temple in Asakusa. Giant red lantern (Kaminarimon), Nakamise shopping street, and incense smoke."
    },
    "Meiji Jingu": {
        "description": "İmparator Meiji'ye adanmış orman içindeki Şinto tapınağı. Devasa torii kapıları, huzurlu yürüyüş yolları ve sake fıçı duvarı.",
        "description_en": "Shinto shrine in forest dedicated to Emperor Meiji. Massive torii gates, peaceful walking paths, and sake barrel wall."
    },
    "Shibuya Crossing": {
        "description": "Dünyanın en kalabalık yaya geçidi, neon ışıklar ve dev ekranlar. Lost in Translation filmiyle ikonikleşen Tokyo kaosu.",
        "description_en": "World's busiest pedestrian crossing, neon lights, and giant screens. Tokyo chaos made iconic by Lost in Translation movie."
    },
    "Tokyo Skytree": {
        "description": "Japonya'nın en yüksek yapısı (634m), modern yayın kulesi. İki gözlem güvertesi, cam zemin ve Sora-machi alışveriş merkezi.",
        "description_en": "Japan's tallest structure (634m), modern broadcasting tower. Two observation decks, glass floor, and Sora-machi mall."
    },
    "teamLab Planets": {
        "description": "Suya girdiğiniz immersive dijital sanat müzesi. Çıplak ayak gezilen, çiçekler ve kristal ışıklarla dolu etkileyici deneyim.",
        "description_en": "Immersive digital art museum where you enter water. Impressive experience walked barefoot, full of flowers and crystal lights."
    },
    "Ghibli Museum": {
        "description": "Hayao Miyazaki'nin anime dünyasına açılan kapı. Mitaka'da masalsı mimari, orijinal eskizler ve sadece orada izlenen kısa filmler.",
        "description_en": "Gate to Hayao Miyazaki's anime world. Fairy-tale architecture in Mitaka, original sketches, and short films exclusive to museum."
    },
    "Shinjuku Gyoen": {
        "description": "Gökdelenlerin ortasında devasa yeşil vaha. Japon, İngiliz ve Fransız bahçeleri, özellikle baharda sakura (kiraz çiçeği) izleme noktası.",
        "description_en": "Massive green oasis amidst skyscrapers. Japanese, English, and French gardens, especially a sakura viewing spot in spring."
    },
    "Tsukiji Outer Market": {
        "description": "Eski balık pazarının dış kısmı, sokak lezzetleri cenneti. Taze suşi, tamagoyaki (Japon omleti) ve deniz ürünleri tadımı.",
        "description_en": "Outer part of old fish market, street food paradise. Fresh sushi, tamagoyaki (Japanese omelet), and seafood tasting."
    },
    "Akihabara Electric Town": {
        "description": "Anime, manga ve elektronik kültürünün merkezi (Otaku kültürü). Maid kafeler, figür dükkanları ve çok katlı oyun salonları.",
        "description_en": "Center of anime, manga, and electronics culture (Otaku culture). Maid cafes, figure shops, and multi-story arcades."
    },
    "Ichiran Ramen": {
        "description": "Tonkotsu ramen zinciri, tek kişilik kabinlerde (focus booth) yemek deneyimi. Özelleştirilebilir lezzet formu ve efsanevi et suyu.",
        "description_en": "Tonkotsu ramen chain, dining experience in solo booths (focus booths). Customizable flavor form and legendary broth."
    },
    "Afuri Ramen": {
        "description": "Yuzu (Japon narenciyesi) aromalı hafif ramen ile ünlü zincir. Ferahlatıcı lezzet, ince erişte ve modern atmosfer.",
        "description_en": "Chain famous for Yuzu (Japanese citrus) flavored light ramen. Refreshing taste, thin noodles, and modern atmosphere."
    },
    "Sushi Zanmai": {
        "description": "7/24 açık popüler suşi zinciri, 'Ton Balığı Kralı' Kiyoshi Kimura. Kaliteli, uygun fiyatlı ve her zaman taze.",
        "description_en": "Popular 24/7 sushi chain, 'Tuna King' Kiyoshi Kimura. Quality, affordable, and always fresh."
    },
    "Gonpachi Nishi-Azabu": {
        "description": "Kill Bill filmindeki dövüş sahnesine ilham veren restoran. Geleneksel Japon dekoru, izakaya yemekleri ve canlı atmosfer.",
        "description_en": "Restaurant that inspired the fight scene in Kill Bill. Traditional Japanese decor, izakaya dishes, and lively atmosphere."
    },
    "Pokemon Cafe": {
        "description": "Pokemon temalı resmi kafe, pikachu şeklinde yemekler. Rezervasyon zorunlu, özel şovlar ve hayranlar için alışveriş.",
        "description_en": "Official Pokemon-themed cafe, pikachu-shaped dishes. Reservation mandatory, special shows, and shopping for fans."
    },
    "Koffee Mameya": {
        "description": "Omotesando'da minimalist kahve laboratuvarı. Baristalar kahve doktoru gibi, dünyanın en iyi çekirdekleri ve kişisel reçeteler.",
        "description_en": "Minimalist coffee lab in Omotesando. Baristas like coffee doctors, world's best beans, and personal recipes."
    },
    "Ueno Park": {
        "description": "Müzeler, tapınaklar ve hayvanat bahçesiyle dolu dev park. Binlerce kiraz ağacıyla Tokyo'nun en popüler sakura (hanami) mekanı.",
        "description_en": "Giant park filled with museums, temples, and zoo. Tokyo's most popular sakura (hanami) spot with thousands of cherry trees."
    },
    "Tokyo National Museum": {
        "description": "Japonya'nın en eski ve büyük müzesi, Ueno Park'ta. Samuray zırhları, kimonolar, kılıçlar ve ulusal hazineler.",
        "description_en": "Japan's oldest and largest museum, in Ueno Park. Samurai armor, kimonos, swords, and national treasures."
    },
    "Golden Gai": {
        "description": "Shinjuku'da 200'den fazla minyatür barın olduğu dar sokaklar. Savaş sonrası atmosferi, sadece 5-6 kişilik mekanlar ve gece hayatı.",
        "description_en": "Narrow streets in Shinjuku with over 200 miniature bars. Post-war atmosphere, venues for only 5-6 people, and nightlife."
    },
    "Harajuku Takeshita Street": {
        "description": "Gençlik modası ve kawaii (sevimli) kültürünün kalbi. Renkli krepçiler, kostüm dükkanları ve çılgın sokak stili.",
        "description_en": "Heart of youth fashion and kawaii (cute) culture. Colorful crepes, costume shops, and crazy street style."
    },
    "Yayoi Kusama Museum": {
        "description": "Puantiyeli sanatın kraliçesi Yayoi Kusama'ya adanmış müze. Sonsuzluk aynaları, bal kabağı heykelleri ve sınırlı bilet.",
        "description_en": "Museum dedicated to queen of polka dot art Yayoi Kusama. Infinity mirrors, pumpkin sculptures, and limited tickets."
    },
    "Roppongi Hills": {
        "description": "Lüks alışveriş, ofis ve sanat kompleksi. Mori Sanat Müzesi ve Tokyo City View gözlem güvertesi burada.",
        "description_en": "Luxury shopping, office, and art complex. Mori Art Museum and Tokyo City View observation deck are here."
    },
    "Ginza Shopping District": {
        "description": "Tokyo'nun en lüks alışveriş semti, flagship mağazalar ve gurme restoranlar. Hafta sonu araçsız yaya caddesi (Hokosha Tengoku).",
        "description_en": "Tokyo's most luxury shopping district, flagship stores, and gourmet restaurants. Weekend vehicle-free pedestrian street (Hokosha Tengoku)."
    },
    "Nakameguro": {
        "description": "Meguro Nehri boyunca uzanan hip semt, sakura zamanı pembe tünel. Tasarımcı dükkanları, kafeler ve huzurlu yürüyüş.",
        "description_en": "Hip district along Meguro River, pink tunnel during sakura time. Designer shops, cafes, and peaceful walk."
    },
    "Odaiba": {
        "description": "Tokyo Körfezi'ndeki yapay ada, fütüristik binalar. Gundam heykeli, plaj, Rainbow Bridge manzarası ve alışveriş.",
        "description_en": "Artificial island in Tokyo Bay, futuristic buildings. Gundam statue, beach, Rainbow Bridge view, and shopping."
    },
    "Yoyogi Park": {
        "description": "Meiji Tapınağı yanındaki geniş park, rockabillies dansçıları ve piknikçiler. Hafta sonu etkinlikleri, müzisyenler ve özgür atmosfer.",
        "description_en": "Large park next to Meiji Shrine, rockabillies dancers, and picnickers. Weekend events, musicians, and free atmosphere."
    },
    "Robot Restaurant": {
        "description": "Shinjuku'da neon ışıklar, robotlar ve dansçılarla çılgın şov. (Not: Kapanmış olabilir, kontrol edilmeli, turist tuzağı ama eğlenceli).",
        "description_en": "Crazy show with neon lights, robots, and dancers in Shinjuku. (Note: May be closed, check, tourist trap but fun)."
    },
    "Maid Cafe": {
        "description": "Akihabara'da garsonların hizmetçi kostümüyle servis yaptığı kafeler. 'Moe moe kyun' büyüleri, ketçap sanatı ve otaku deneyimi.",
        "description_en": "Cafes in Akihabara where waitresses serve in maid costumes. 'Moe moe kyun' spells, ketchup art, and otaku experience."
    },
    "Hamarikyu Gardens": {
        "description": "Gökdelenlerin gölgesinde deniz suyuyla beslenen hendekli Edo dönemi bahçesi. Çay evi, çiçek tarlaları ve su otobüsü durağı.",
        "description_en": "Edo period garden with sea water moat in shadow of skyscrapers. Tea house, flower fields, and water bus stop."
    },
    "Nezu Museum": {
        "description": "Kengo Kuma tasarımı modern bina ve muhteşem Japon bahçesi. Asya sanatı koleksiyonu, huzur ve estetik mimari.",
        "description_en": "Kengo Kuma designed modern building and magnificent Japanese garden. Asian art collection, peace, and aesthetic architecture."
    },
    "Kabukicho Tower": {
        "description": "Shinjuku'da yeni açılan eğlence gökdeleni. Oteller, sinema, tiyatro ve neon ışıklı yeme-içme alanı (Yokocho).",
        "description_en": "Newly opened entertainment skyscraper in Shinjuku. Hotels, cinema, theater, and neon-lit dining hall (Yokocho)."
    },
    "Warner Bros. Studio Tour Tokyo": {
        "description": "Harry Potter dünyasının yapım aşamaları (Making of Harry Potter). Setler, kostümler ve Butterbeer. Londra'dan sonra ikinci.",
        "description_en": "Making of Harry Potter world. Sets, costumes, and Butterbeer. Second one after London."
    },
    "Gotokuji Temple": {
        "description": "Binlerce Maneki-neko (şans kedisi) heykelinin bulunduğu tapınak. Kedi severler için hac yeri, huzurlu ve fotostik.",
        "description_en": "Temple filled with thousands of Maneki-neko (lucky cat) statues. Pilgrimage site for cat lovers, peaceful and photogenic."
    },
    "Shimokitazawa": {
        "description": "Bohem semt, ikinci el giyim (thrift) mağazaları ve vintage cenneti. Tiyatrolar, canlı müzik mekanları ve köri restoranları.",
        "description_en": "Bohemian district, thrift stores, and vintage paradise. Theaters, live music venues, and curry restaurants."
    },
    "Kichijoji": {
        "description": "Tokyo'nun yaşanacak en popüler semti, Inokashira Parkı yanında. Harmonica Yokocho (dar ara sokaklar) ve butikler.",
        "description_en": "Tokyo's most popular neighborhood to live, next to Inokashira Park. Harmonica Yokocho (narrow alleys) and boutiques."
    },
    "Daikanyama T-Site": {
        "description": "Dünyanın en güzel kitapçılarından biri (Tsutaya Books). Modern mimari, tasarım kitapları, kafe ve lüks semt atmosferi.",
        "description_en": "One of world's most beautiful bookstores (Tsutaya Books). Modern architecture, design books, cafe, and luxury neighborhood atmosphere."
    },
    "Sushi Dai": {
        "description": "Toyosu Balık Pazarı'nda saatlerce sıra beklenen efsane suşi restoranı. Şefin seçimi (Omakase) kahvaltı, eriyen balıklar.",
        "description_en": "Legendary sushi restaurant in Toyosu Fish Market with hours-long lines. Chef's choice (Omakase) breakfast, melting fish."
    },
    "Tempura Kondo": {
        "description": "Ginza'da iki Michelin yıldızlı tempura restoranı. İncecik kaplama, sebze tempuraları (havuç) sanat eseri gibi.",
        "description_en": "Two Michelin-starred tempura restaurant in Ginza. Thin batter, vegetable tempuras (carrot) like art pieces."
    },
    "Hedgehog Cafe HARRY": {
        "description": "Kirpileri sevip besleyebileceğiniz hayvan kafesi. Harajuku'da benzersiz deneyim, fotoğrafçılık ve sevimlilik.",
        "description_en": "Animal cafe where you can pet and feed hedgehogs. Unique experience in Harajuku, photography, and cuteness."
    },
    "2D Cafe": {
        "description": "Shin-Okubo'da çizgi roman (manga) dünyasında gibi hissettiren kafe. Siyah-beyaz illüzyon dekor, bubble tea ve tatlılar.",
        "description_en": "Cafe in Shin-Okubo making you feel inside a comic book (manga). Black-white illusion decor, bubble tea, and desserts."
    },
    "Savoy Pizza": {
        "description": "Tokyo'nun en iyi Napoli pizzası (gerçekten). Odun ateşi, tuzlu hamur ve Ugly Delicious belgeseliyle ünlü.",
        "description_en": "Tokyo's best Neapolitan pizza (really). Wood fire, salty dough, and famous from Ugly Delicious documentary."
    },
    "Bear Pond Espresso": {
        "description": "Shimokitazawa'da kült kahve dükkanı, 'Angel Stain' espressosu meşhur. Fotoğraf yasak, ciddi kahve kuralı.",
        "description_en": "Cult coffee shop in Shimokitazawa, famous for 'Angel Stain' espresso. No photos, strict coffee rule."
    },
    "Kagari Ramen": {
        "description": "Ginza'da tavuk suyu (tori-paitan) rameniyle ünlü, Michelin Bib Gourmand. Kremsi çorba, zarif sunum ve uzun kuyruk.",
        "description_en": "Michelin Bib Gourmand famous for chicken broth (tori-paitan) ramen in Ginza. Creamy soup, elegant presentation, and long line."
    },
    "Bar High Five": {
        "description": "Efsanevi barmen Hidetsugu Ueno'nun kokteyl barı. Menü yok, ruh halinize göre özel içki hazırlıyorlar. Dünya klasmanı.",
        "description_en": "Legendary bartender Hidetsugu Ueno's cocktail bar. No menu, they prepare custom drinks based on your mood. World class."
    },
    "Yanaka Ginza": {
        "description": "Eski Tokyo (Shitamachi) atmosferini koruyan alışveriş sokağı. Sokak kedileri, geleneksel atıştırmalıklar ve nostalji.",
        "description_en": "Shopping street preserving Old Tokyo (Shitamachi) atmosphere. Street cats, traditional snacks, and nostalgia."
    },
    "Rikugien Garden": {
        "description": "Tokyo'nun en güzel peyzaj bahçelerinden biri, waka şiirlerine dayalı sahneler. Sonbahar yaprakları ışıklandırmasıyla ünlü.",
        "description_en": "One of Tokyo's most beautiful landscape gardens, scenes based on waka poems. Famous for autumn foliage illumination."
    },
    "Tokyo Disneyland": {
        "description": "Amerika dışındaki ilk Disney parkı. Klasik Disney büyüsü, Cinderella Kalesi ve Japon misafirperverliği.",
        "description_en": "First Disney park outside America. Classic Disney magic, Cinderella Castle, and Japanese hospitality."
    }
}

filepath = 'assets/cities/tokyo.json'
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

print(f"\n✅ Manually enriched {count} items (Tokyo - COMPLETE).")
