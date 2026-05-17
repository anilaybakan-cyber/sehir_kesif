from enrich_venues import enrich_venues

# BATCH: BODRUM SYSTEMATIC COMPLETION - PART 1

bodrum_bulk_updates = {
    "Gündoğan Sahil Sitesi": {
        "desc_tr": "Gündoğan'ın en huzurlu köşelerinden biri olan bu bölge, sabahları çarşaf gibi denizi ve akşamları esen hafif Meltem rüzgarıyla bilinir. Geleneksel balıkçı kasabası dokusunu modern bir konforla birleştiren sahil yürüyüş yoluyla ünlüdür.",
        "desc_en": "One of Gündoğan's most peaceful corners, this area is known for its glass-like morning sea and refreshing evening breeze. Its promenade, blending traditional fishing village charm with modern comfort, is perfect for sunset strolls."
    },
    "Küçükbük Sahil": {
        "desc_tr": "Türkbükü ve Gündoğan arasında saklı bir cennet olan Küçükbük, kristal netliğindeki denizi ve geniş kumsalıyla yerel halkın en sevdiği noktalardan biridir. Gösterişten uzak, doğal ve sakin bir deniz günü geçirmek isteyenler için ideal bir sığınaktır.",
        "desc_en": "A hidden paradise between Türkbükü and Gündoğan, Küçükbük is a local favorite for its crystal-clear water and wide sandy beach. It is an ideal sanctuary for those seeking a natural and tranquil day by the sea, away from the crowds."
    },
    "Mazıköy": {
        "desc_tr": "Bodrum'un en bakir ve doğal kalmış köylerinden biri olan Mazı, zeytin ağaçlarının denizle buluştuğu eşsiz koylara sahiptir. Elektrik ve modern dünya karmaşasından uzakta, tarladan sofraya lezzetler ve turkuaz sular arasında gerçek bir Ege deneyimi sunar.",
        "desc_en": "One of Bodrum's most pristine villages, Mazı features unique bays where olive groves meet the sea. Far from the hustle of modern life, it offers a real Aegean experience with farm-to-table flavors and stunning turquoise waters."
    },
    "Kule Rock City": {
        "desc_tr": "Bodrum Barlar Sokağı'nın kalbinde yer alan bu ikonik mekan, kentin rock müzik kültürünün kalesidir. Yüksek enerjili canlı performansları ve kendine has dekorasyonuyla, Bodrum'un gece hayatında alternatif ve samimi bir durak arayanların favorisidir.",
        "desc_en": "Located in the heart of Bodrum's Bar Street, this iconic venue is the stronghold of the city's rock culture. With its high-energy live performances and distinctive decor, it's a favorite for those seeking an alternative and authentic nightlife experience."
    },
    "ENT Restaurant": {
        "desc_tr": "Şef odaklı bir gastronomi noktası olan ENT, Bodrum'un yerel malzemelerini modern pişirme teknikleriyle birleştiren rafine bir mutfağa sahiptir. Zeytin ağaçları altındaki şık bahçesiyle, Yarımada'nın en özel akşam yemeği duraklarından biridir.",
        "desc_en": "A chef-driven gastronomic destination, ENT offers a refined menu that blends Bodrum’s local ingredients with modern techniques. Set in a stylish garden under olive trees, it is one of the peninsula's most exclusive dining experiences."
    },
    "Zuma Bodrum": {
        "desc_tr": "Yalıkavak Marina'nın lüks atmosferinde yer alan dünyaca ünlü Zuma, modern Japon mutfağını (Izakaya) benzersiz bir deniz manzarası eşliğinde sunar. Şık barı ve jet-set ortamıyla, Bodrum'da rafine eğlence ve gastronominin buluşma noktasıdır.",
        "desc_en": "Located in the luxurious Yalıkavak Marina, the world-renowned Zuma offers modern Japanese cuisine (Izakaya) with stunning sea views. With its chic bar and jet-set atmosphere, it is the ultimate intersection of fine dining and nightlife in Bodrum."
    },
    "Melengeç Balık Restaurant": {
        "desc_tr": "Gümüşlük sahilinde, denizin içindeki masaları ve begonvillerle süslü dekorasyonuyla tanınan Melengeç, kentin en romantik restoranlarından biridir. Taze deniz mahsulleri ve meşhur gün batımı manzarasıyla masalsı bir Ege akşamı vaat eder.",
        "desc_en": "Famous for its tables set right in the shallow water and its bougainvillea-covered decor, Melengeç is one of Gümüşlük's most romantic spots. It promises a magical Aegean evening with fresh seafood and legendary sunset views."
    },
    "Dereköy Lokantası": {
        "desc_tr": "Bodrum'un iç kesimlerindeki bir köyde yer alan bu lokanta, bahçeden sofraya konseptiyle yerel ürünlere hayat verir. Samimi atmosferi ve yaratıcı dokunuşlarla sunulan geleneksel lezzetleriyle, gerçek Bodrum gastronomi ruhunu yaşatır.",
        "desc_en": "Located in a village in Bodrum's interior, this eatery breathes life into local produce with a farm-to-table concept. Its warm atmosphere and traditional flavors with creative twists embody the true culinary soul of Bodrum."
    },
    "The Trattoria by Stefano Ciotti": {
        "desc_tr": "Michelin yıldızlı şef dokunuşunu Bodrum'un Ege havasıyla birleştiren bu trattoria, gerçek İtalyan lezzetlerini en rafine haliyle sunar. Yalıkavak'ta elit bir akşam yemeği için modern ve şık bir atmosfer arayanların ilk tercihlerinden biridir.",
        "desc_en": "Combining Michelin-starred chef touches with Bodrum's Aegean atmosphere, this trattoria serves authentic Italian flavors in their most refined form. It’s a top choice for an elite and modern dining experience in Yalıkavak."
    },
    "Malva Restaurant & Cocktail Bar": {
        "desc_tr": "Modern ve rafine bir Ege mutfağı sunan Malva, yerel malzemeleri yaratıcı kokteyllerle buluşturan bir gastronomi durağıdır. Özellikle gün batımı saatlerinde sunduğu panoramik manzara ve sofistike ambiyansıyla dikkat çeker.",
        "desc_en": "Offering modern and refined Aegean cuisine, Malva is a gastronomic hub that pairs local ingredients with creative cocktails. It is particularly known for its panoramic views and sophisticated ambiance during sunset."
    },
    "KITCHEN by Osman Sezener": {
        "desc_tr": "Şef Osman Sezener’in 'topraktan tabağa' felsefesini Bodrum’a taşıyan KITCHEN, odun ateşinde pişen özel lezzetleriyle tanınır. Zeytin ağaçları arasındaki rustik şıklığıyla, gastronomi tutkunları için unutulmaz bir deneyim sunar.",
        "desc_en": "Bringing Chef Osman Sezener’s 'field-to-table' philosophy to Bodrum, KITCHEN is famous for its unique flavors cooked over wood-fire. With its rustic-chic setting amidst olive groves, it offers an unforgettable experience for foodies."
    },
    "Bagatelle Bodrum": {
        "desc_tr": "Fransız Rivierası’nın neşeli ve şık enerjisini Bodrum’a taşıyan Bagatelle, hem bir plaj kulübü hem de gurme bir restorandır. Canlı atmosferi ve eğlence dolu akşam yemekleriyle Yalıkavak Marina’nın en canlı noktalarından biridir.",
        "desc_en": "Bringing the joyful and chic energy of the French Riviera to Bodrum, Bagatelle functions as both a beach club and a gourmet restaurant. It is one of Yalıkavak Marina’s most vibrant spots, famous for its lively dinner parties."
    },
    "Novikov Bodrum": {
        "desc_tr": "Asya ve İtalyan mutfağını tek bir çatı altında toplayan Novikov, en taze deniz ürünlerini ve yaratıcı sushi çeşitlerini sunar. Yalıkavak Marina’daki modern mimarisi ve seçkin kitlesiyle, Yarımada'nın en lüks duraklarından biridir.",
        "desc_en": "Bringing Asian and Italian cuisines together under one roof, Novikov serves the freshest seafood and creative sushi. With its modern architecture and elite clientele in Yalıkavak Marina, it’s one of the peninsula's most luxurious stops."
    },
    "Hakkasan Bodrum": {
        "desc_tr": "Dünya çapında Michelin yıldızı deneyimiyle tanınan Hakkasan, modern Çin mutfağını Bodrum'un eşsiz manzarasına karşı sunar. Zarif dekorasyonu ve ikonik lezzetleriyle, kentin en prestijli açık hava restoranlarından biridir.",
        "desc_en": "Bringing its world-renowned Michelin-starred experience to Bodrum, Hakkasan serves modern Chinese cuisine against a stunning backdrop. With its elegant decor and iconic dishes, it is one of the city's most prestigious open-air venues."
    },
    "Lucca by the Sea": {
        "desc_tr": "İstanbul'un efsanevi markası Lucca'nın deniz kıyısındaki yansıması olan bu mekan, rafine kokteylleri ve dünya mutfağından seçkin lezzetleriyle bilinir. Şık tasarımı ve kaliteli müziğiyle Bodrum'un sosyal yaşam kalbinde yer alır.",
        "desc_en": "The seaside reflection of Istanbul's legendary Lucca, this venue is known for its refined cocktails and premium international menu. With its chic design and high-quality music, it sits at the heart of Bodrum's social scene."
    },
    "Fenix Bodrum": {
        "desc_tr": "Latin ve Akdeniz lezzetlerini egzotik bir dekorasyonla harmanlayan Fenix, Bodrum akşamlarına hareket katan bir restorandır. Şık barı ve enerjik DJ performanslarıyla, Yalıkavak Marina'da akşam yemeğinden gece hayatına geçişin adresidir.",
        "desc_en": "Blending Latin and Mediterranean flavors with exotic decor, Fenix is a restaurant that brings vibrant energy to Bodrum nights. With its stylish bar and DJ sets, it’s the go-to spot in Yalıkavak for transitioning from dinner to nightlife."
    },
    "Sünger Pizza Restaurant": {
        "desc_tr": "Bodrum merkezinin en eski ve sevilen klasiklerinden biri olan Sünger Pizza, sadece pizzalarıyla değil, taze deniz ürünlü spesiyalleriyle de meşhurdur. Salaş ama şık atmosferiyle gerçek bir şehir efsanesi ve her ziyaretçinin mutlaka uğradığı bir duraktır.",
        "desc_en": "One of central Bodrum's oldest and most beloved classics, Sünger Pizza is famous not just for its pizzas, but also for its fresh seafood specials. A true local legend with a casual-chic vibe, it is a must-visit for every traveler."
    },
    "Kısmet Lokantası": {
        "desc_tr": "Bodrum'un yerel lezzetlerini en saf haliyle sunan Kısmet, günlük çıkan ev yemekleri ve taze Ege otlarıyla ünlüdür. Bir aile işletmesi sıcaklığında, kentin ticaret ve sosyal yaşamının kalbinde, gerçek Bodrum tadını arayanların vazgeçilmezidir.",
        "desc_en": "Offering central Bodrum's local flavors in their purest form, Kısmet is famous for its daily home-cooked specials and fresh Aegean herbs. With family-run warmth, it is an essential stop for those seeking the authentic taste of the town."
    },
    "İngiliz Kulesi": {
        "desc_tr": "Bodrum Kalesi'nin en görkemli burçlarından biri olan İngiliz Kulesi, Orta Çağ şövalyelerinin yaşantısını günümüze taşıyan tarihi bir anıttır. İçindeki şövalye armaları ve gotik pencereleriyle, kalede tarihin en yoğun hissedildiği noktadır.",
        "desc_en": "One of the most grand towers of Bodrum Castle, the English Tower is a historical monument reflecting the life of medieval knights. With its carved coats of arms and Gothic windows, it’s where history is felt most intensely within the fortress."
    },
    "Tarihi Bardakçı Hamamı": {
        "desc_tr": "1749 yılından beri hizmet veren bu tarihi hamam, Bodrum'un en eski yapılarından biri olarak geleneksel Türk hamamı kültürünü yaşatır. Otantik kubbesi ve mermer kurnalarıyla, kentin geçmişine dokunabileceğiniz huzurlu ve mistik bir duraktır.",
        "desc_en": "Serving since 1749, this historic bath is one of Bodrum's oldest structures, keeping the traditional Turkish hammam culture alive. With its authentic dome and marble basins, it offers a peaceful and mystical journey into the town's past."
    },
    "Deniz Feneri": {
        "desc_tr": "Bodrum liman girişini bekleyen bu ikonik deniz feneri, Yarımada'nın en fotografik ve romantik noktalarından biridir. Özellikle gün batımında kaleye ve denize karşı sunduğu manzara, Bodrum'un denizci ruhunu mükemmel bir şekilde simgeler.",
        "desc_en": "Guarding the entrance to Bodrum harbor, this iconic lighthouse is one of the peninsula's most photographic and romantic spots. The view it offers at sunset against the castle perfectly symbolizes Bodrum’s enduring maritime spirit."
    },
    "Gümüşlük": {
        "desc_tr": "Antik Myndos şehri üzerine kurulu olan Gümüşlük, bohem atmosferi, denizin içindeki balık restoranları ve büyüleyici gün batımlarıyla ünlüdür. Kentin kentsel karmaşasından uzak, sanat ve huzur dolu ruhuyla Yarımada'nın en özel köşesidir.",
        "desc_en": "Built over the ancient city of Myndos, Gümüşlük is famous for its bohemian charm, seaside fish restaurants, and stunning sunsets. Far from the urban hustle, its art-filled and serene spirit makes it the peninsula's most unique corner."
    },
    "Thor Yıldız Batığı": {
        "desc_tr": "Bodrum'un en popüler dalış noktalarından biri olan Thor Yıldız Batığı, su altı dünyasını keşfetmek isteyenler için yapay bir resif görevi görür. Batığın etrafındaki zengin deniz yaşamı ve kristal netliğindeki görüş mesafesi, unutulmaz bir dalış deneyimi sunar.",
        "desc_en": "A favorite spot for diving enthusiasts, the Thor Yıldız Shipwreck serves as an artificial reef for exploring the underwater world. The vibrant marine life surrounding the wreck and crystal-clear visibility offer an unforgettable diving adventure."
    },
    "Statue plongeur": {
        "desc_tr": "Bodrum limanında yer alan bu heybetli heykel, kentin temelini atan süngercilere ve cesur dalgıçlara adanmış bir saygı duruşudur. Bodrum'un bir balıkçı kasabasından dünya kentine dönüşüm hikayesini simgeleyen önemli bir kentsel anıttır.",
        "desc_en": "Located in Bodrum harbor, this imposing statue is a tribute to the sponge divers who laid the town's foundations. It serves as an important urban monument symbolizing Bodrum's transformation from a fishing village to a global destination."
    },
    "Red&White": {
        "desc_tr": "Bodrum sahilinde samimi ve rahat atmosferiyle bilinen Red&White, plaj keyfini kaliteli kahveler ve lezzetli atıştırmalıklarla birleştiren popüler bir duraktır. Denize sıfır masalarıyla, kentin içinde konforlu bir mola noktasıdır.",
        "desc_en": "Known for its warm and relaxed vibe on the Bodrum shore, Red&White is a popular spot that blends beach fun with quality coffee and delicious snacks. Its seaside tables offer a comfortable and chic break in the heart of town."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Bodrum Bulk - Part 1)...")
enrich_venues("bodrum", bodrum_bulk_updates)
print("✨ Systematic Enrichment - Bodrum Bulk Part 1 Complete.")
