from enrich_venues import enrich_venues

# BATCH: BODRUM SYSTEMATIC COMPLETION - FINAL PART

bodrum_final_updates = {
    "Blue Point Didim Beach Club": {
        "desc_tr": "Didim'in en seçkin plaj kulüplerinden biri olan Blue Point, kristal berraklığında denizi ve lüks güneşlenme teraslarıyla Bodrum'dan günübirlik kaçışlar için popüler bir duraktır. Beyaz kumları ve VIP hizmet kalitesiyle, Ege'de prestijli bir deniz günü vaat eder.",
        "desc_en": "One of Didim's most exclusive beach clubs, Blue Point is a popular day-trip destination from Bodrum for its crystal-clear waters and luxury sun decks. With its white sands and VIP service, it promises a prestigious day by the Aegean."
    },
    "Mandalin": {
        "desc_tr": "Bodrum merkezinde canlı müzik ve eğlencenin kalbi sayılan Mandalin, kentin en popüler performans sahnelerinden biridir. Eski bir Bodrum binasının otantik dokusunda, kaliteli müzik ve neşeli atmosferiyle kentin gece hayatına yön verir.",
        "desc_en": "Considered the heart of live music in central Bodrum, Mandalin is one of the city's most popular performance venues. Set in an authentic historic building, it shapes the town’s nightlife with top-quality music and a vibrant atmosphere."
    },
    "SJ TRAVEL & YACHTING (Luxury Gulet Charter, Yacht charter, Cruises Bodrum-TURKEY)": {
        "desc_tr": "Bodrum'un köklü denizcilik mirasını lüksle birleştiren SJ Travel, kişiye özel gulet turları ve yat kiralama hizmetlerinde uzmandır. Yarımada'nın saklı koylarını konfor ve ayrıcalıkla keşfetmek isteyenler için güvenilir bir kapıdır.",
        "desc_en": "Combining Bodrum's deep maritime heritage with luxury, SJ Travel specializes in personalized gulet charters and yacht services. It is a trusted gateway for those looking to explore the peninsula's hidden bays with comfort and exclusivity."
    },
    "Bodrum Travel Guide": {
        "desc_tr": "Bodrum Yarımadası'nın her köşesini bir yerel gibi keşfetmeniz için profesyonel rehberlik hizmetleri sunan bu merkez, tatilinizi bir keşif yolculuğuna dönüştürür. Tarihi alanlardan gizli lezzet duraklarına kadar kentin tüm sırlarını sizinle paylaşır.",
        "desc_en": "Providing professional guiding services to help you explore every corner of the Bodrum Peninsula like a local, this hub turns your holiday into a journey of discovery. It shares all the town's secrets, from historic sites to hidden culinary gems."
    },
    "Historical (Turkish bath ) Tarihi Bardakçı Hamamı": {
        "desc_tr": "1749'da inşa edilen bu tarihi hamam, Bodrum'un yaşayan en eski geleneksel yıkanma merkezidir. Otantik kubbesi, mermer platformu ve geleneksel kese-köpük ritüelleriyle, kentin geçmişine mistik bir yolculuk sunan huzurlu bir vaha gibidir.",
        "desc_en": "Built in 1749, this historic bath is the oldest active traditional bathing center in Bodrum. With its authentic dome, marble platforms, and traditional scrub-and-foam rituals, it’s a peaceful oasis offering a mystical journey into the town's past."
    },
    "Bodrum": {
        "desc_tr": "Beyaz evleri, begonvillerle süslü sokakları ve binlerce yıllık kalesiyle kentin kalbi burasıdır. Antik Halikarnassos'un üzerine kurulu olan merkez bölge, hem tarihi hem de modern hayatın kusursuz bir uyum içinde olduğu bir Ege mozaiğidir.",
        "desc_en": "The heart of the city, with its white houses, bougainvillea-lined alleys, and a millennia-old castle. Built over ancient Halicarnassus, the central area is an Aegean mosaic where history and modern life exist in perfect harmony."
    },
    "Trafo Cafe & Restaurant - Bodrum Belediye A.Ş.": {
        "desc_tr": "Eski bir trafo binasının modern bir sosyal tesise dönüşümüyle yaratılan Trafo, kaleye ve marina girişine hakim terasıyla eşsizdir. Bodrum'un sanatsal atmosferinde kaliteli bir mola vermek için kentin en ferah ve nezih duraklarından biridir.",
        "desc_en": "Created by converting an old electricity transformer into a modern social facility, Trafo is unique for its terrace overlooking the castle and marina. It’s one of the town's most airy and refined spots for a quality break in Bodrum's artistic hub."
    },
    "Shell": {
        "desc_tr": "Bodrum Yarımadası'nı keşfederken kentin girişinde veya yol üzerindeki bu modern tesis, gezginler için konforlu bir mola noktasıdır. Yenilenen marketi ve profesyonel hizmetiyle, kenti keşfetmeden önceki son durak veya güvenilir bir yol arkadaşıdır.",
        "desc_en": "A modern pit stop for travelers exploring the Bodrum Peninsula, whether at the city entrance or along the routes. With its updated convenience store and professional service, it’s a reliable roadside companion for any journey."
    },
    "NLT Pazarlama Bodrum": {
        "desc_tr": "Bodrum'un yerel üretim ve pazarlama ağının önemli merkezlerinden biri olan bu nokta, kentsel ticaretin nabzını tutar. Kentin dinamik yapısına ve yerel işletmelerin büyümesine katkı sağlayan stratejik bir iş merkezidir.",
        "desc_en": "One of the important centers of Bodrum's local production and marketing network, capturing the pulse of urban commerce. It is a strategic business hub contributing to the city's dynamic structure and the growth of local enterprises."
    },
    "Kahve Dünyası - Bodrum Marina": {
        "desc_tr": "Marina bölgesinin en canlı noktasında yer alan Kahve Dünyası, taze kavrulmuş kahveleri ve yerel lezzetlerle harmanlanan çikolatalarıyla kentin bir klasiğidir. Marinadaki teknelere karşı kahvenizi yudumlayabileceğiniz, hem yerli halkın hem de turistlerin buluşma noktasıdır.",
        "desc_en": "Located at the most vibrant spot of the Marina area, Kahve Dünyası is a classic with its freshly roasted coffee and chocolates blended with local flavors. It’s a meeting point for both locals and tourists to sip coffee facing the harbor yachts."
    },
    "Cafe De Nargile": {
        "desc_tr": "Bodrum çarşısının girişinde, deniz meltemine hakim masalarıyla Cafe De Nargile kentin en eski sosyal duraklarından biridir. Geleneksel nargile kültürü ve taze demlenmiş çayıyla, kentin kentsel nabzını tutabileceğiniz samimi bir mekandır.",
        "desc_en": "At the gateway to the Bodrum bazaar, with tables catching the sea breeze, Cafe De Nargile is one of the town's oldest social spots. With traditional shisha culture and fresh tea, it's a warm place to experience the city's urban pulse."
    },
    "Gumbet Belediye Cafe": {
        "desc_tr": "Gümbet koyuna en hakim noktada yer alan bu belediye kafesi, uygun fiyatlı servisi ve muazzam manzarasıyla kentin gizli kalmış bir hazinesidir. Denizin ve güneşin keyfini sakin bir ortamda çıkarmak isteyenler için ideal bir aile durağıdır.",
        "desc_en": "Perched at a vantage point overlooking Gümbet Bay, this municipal cafe is a hidden gem with its budget-friendly service and immense views. It’s an ideal family spot for those wanting to enjoy the sea and sun in a peaceful setting."
    },
    "Gusto Cafe Bodrum": {
        "desc_tr": "Yeni nesil bir kafe ve bistro deneyimi sunan Gusto, modern dekorasyonu ve yaratıcı menüsüyle Bodrum merkezinde fark yaratır. Kaliteli kahveleri ve gurme atıştırmalıklarıyla, kentin içinde stil sahibi bir mola noktası arayanların adresidir.",
        "desc_en": "Offering a modern cafe and bistro experience, Gusto stands out in central Bodrum with its contemporary decor and creative menu. It is the go-to for those seeking a stylish break with quality coffee and gourmet snacks."
    },
    "KARYA FIRIN": {
        "desc_tr": "Bodrum'un en sevilen fırın ve pastanelerinden olan Karya, özellikle sabahları çıkan taze poğaçaları ve meşhur pastalarıyla lezzet durağıdır. Yerel halkın kahvaltı alışkanlıklarının başında gelen bu mekan, kentin en tatlı ritüellerinden biridir.",
        "desc_en": "One of Bodrum's most beloved bakeries, Karya is a flavor hub famous for its fresh daily pastries and iconic cakes. A staple of local breakfast routines, it is one of the town's sweetest daily rituals."
    },
    "Eski Hesap Kullanılmıyor": {
        "desc_tr": "Bodrum'un tarihine karışmış olan eski bir ticari kaydı temsil eden bu nokta, kentin kentsel arşivinin bir parçasıdır. Günümüzde dijital bir iz olarak kalsa da, kentin ticari hafızasında yer tutan bir referans noktasıdır.",
        "desc_en": "Representing a historical commercial record in Bodrum's urban past, this spot is part of the city's digital archive. While it remains a digital footprint today, it stands as a point of reference in the city's commercial memory."
    },
    "Kim Bodrum": {
        "desc_tr": "Bodrum'un sanatsal ve butik ruhunu ürünlerine yansıtan Kim Bodrum, yaratıcı ve yerel tasarımlarıyla kentin modern alışveriş duraklarından biridir. Özgün takıları ve tasarım objeleriyle, kentin estetik karakterini keşfetmek isteyenler için ilgi çekicidir.",
        "desc_en": "Reflecting Bodrum's artistic and boutique spirit in its products, Kim Bodrum is one of the city's modern shopping stops with creative local designs. Its unique jewelry and objects attract those wanting to discover the city's aesthetic character."
    },
    "Bodrum Sobe Gaga VIP After Night Club": {
        "desc_tr": "Bodrum gecelerinin geç vakitlerdeki en hareketli adresi olan Sobe Gaga, VIP konsepti ve enerjik müzikleriyle tanınır. Sabahın ilk ışıklarına kadar süren eğlence anlayışı ve iddialı kokteylleriyle, kentin gece hayatında özel bir yere sahiptir.",
        "desc_en": "The most vibrant late-night address in Bodrum, Sobe Gaga is known for its VIP concept and high-energy music. With entertainment lasting until dawn and bold cocktails, it holds a special place in the city's nightlife scene."
    },
    "Unique Bodrum": {
        "desc_tr": "Adı gibi benzersiz bir atmosfer sunan bu mekan, gastronomi ve eğlenceyi Yarımada'nın lüks dokusuyla birleştirir. Şık tasarımı ve seçkin kitlesiyle, Bodrum'da özel bir akşam geçirmek isteyenlerin prestijli duraklarından biridir.",
        "desc_en": "Offering a unique atmosphere as its name suggests, this venue blends gastronomy and entertainment within the peninsula's luxury texture. With its chic design and elite clientele, it's a prestigious stop for an exclusive evening in Bodrum."
    },
    "Disco": {
        "desc_tr": "Bodrum'un klasik disko kültürünü günümüze taşıyan bu alan, yüksek enerjili müzikleri ve nostaljik atmosferiyle kentin eğlence hafızasını yaşatır. Yaz boyunca tatilin coşkusunu paylaşmak isteyenlerin vazgeçilmez dans pistidir.",
        "desc_en": "Carrying Bodrum's classic disco culture into the present, this venue keeps the city's entertainment memory alive with high-energy music and a nostalgic vibe. It's an indispensable dance floor for those seeking holiday excitement all summer."
    },
    "Cavalli Bodrum": {
        "desc_tr": "Lüks ve moda dünyasının esintilerini Bodrum gecelerine taşıyan Cavalli, gösterişli tasarımı ve elit eğlence anlayışıyla kentin en şık duraklarından biridir. Yüksek kaliteli servisi ve imza etkinlikleriyle Bodrum'un jet-set durakları arasındadır.",
        "desc_en": "Bringing echoes of the world of luxury and fashion to Bodrum nights, Cavalli is one of the town's most stylish spots with its opulent design and elite entertainment. It ranks among Bodrum's jet-set destinations with premium service and signature events."
    },
    "Nox Bodrum": {
        "desc_tr": "Modern ses ve ışık sistemleriyle donatılmış Nox, Bodrum gece hayatına karanlık ve gizemli bir şıklık katar. Elektronik müzik severlerin uğrak noktası olan mekan, kentin kentsel eğlence anlayışını bir adım ileriye taşıyan iddialı bir duraktır.",
        "desc_en": "Equipped with modern sound and light systems, Nox adds a dark and mysterious elegance to Bodrum nightlife. A hub for electronic music lovers, it is an ambitious spot that pushes the town's urban entertainment offerings forward."
    },
    "Bodrum Castle Tickets and Entrance": {
        "desc_tr": "Bodrum Kalesi'nin görkemli kapısı, ziyaretçileri Orta Çağ'ın ve şövalyelerin dünyasına açılan bir yolculuğun başlangıcına davet eder. İhtişamlı surların gölgesinde başlayan bu giriş, kentin en büyük tarihi hazinesini keşfetmenin ilk adımıdır.",
        "desc_en": "The grand gate of Bodrum Castle invites visitors to the start of a journey into the world of knights and the Middle Ages. This entrance under the shadow of majestic walls is the first step in exploring the city's greatest historical treasure."
    },
    "Müze": {
        "desc_tr": "Antik dünyanın izlerinin ve sualtı hazinelerinin korunduğu bu alan, Bodrum'un binlerce yıllık tarihine açılan bir penceredir. Eserlerin sessiz anlatımıyla kentin köklü geçmişini keşfedebileceğiniz, kültür ve tarihin buluştuğu en önemli kentsel mirastır.",
        "desc_en": "A window into Bodrum's millennia-old history, where traces of the ancient world and underwater treasures are preserved. It is the most important urban heritage site where culture and history meet, allowing you to discover the city's roots through silent artifacts."
    },
    "Yalcin Sivrikaya Plaj ve Liman alani": {
        "desc_tr": "Yalıkavak bölgesinde yer alan bu yerel kıyı şeridi, sakin denizi ve samimi atmosferiyle yerli halkın nefes aldığı özel noktalardan biridir. Kentin doğal dokusunu koruyan bu sahil, huzurlu bir akşam yürüyüşü veya deniz molası için idealdir.",
        "desc_en": "This local stretch of coastline in the Yalıkavak area is a special spot where locals breathe, known for its calm sea and warm vibe. Preserving the city's natural texture, it's ideal for a peaceful evening walk or a simple sea break."
    },
    "Ordinaryus Yalcin Sivrikaya plaji": {
        "desc_tr": "Yalıkavak'ın karakteristik sahillerinden biri olan bu alan, doğal yapısı ve kentsel karmaşadan uzak konumuyla bilinir. Denizin ve güneşin tadını en yalın haliyle çıkarmak isteyenler için, Bodrum'un gerçek yerel değerlerinden biridir.",
        "desc_en": "One of Yalıkavak's characterful coastal spots, known for its natural structure and location away from the urban rush. It is one of Bodrum's authentic local values for those wanting to enjoy the sea and sun in their simplest form."
    },
    "Yel Değirmenleri": {
        "desc_tr": "Bodrum ile Gümbet'i birbirinden ayıran tepe üzerindeki bu tarihi yeldeğirmenleri, kentin en ikonik silüetini oluşturur. 18. yüzyıldan kalan bu yapılar, özellikle gün batımında kenti kuşbakışı izleyebileceğiniz en popüler noktadır.",
        "desc_en": "Perched on the hill dividing Bodrum and Gümbet, these historic windmills form the city's most iconic silhouette. Dating back to the 18th century, they offer the most popular vantage point for a sunset bird's-eye view of the town."
    },
    "Yelken Bay Beach Hotel ( Lud’da)": {
        "desc_tr": "Bitez'in en nezih noktalarından biri olan Lud bölgesinde yer alan bu otel, modern konforu Ege'nin serinliğiyle buluşturur. Şık plajı ve rafine hizmet kalitesiyle, kentin içinde lüks ve huzur dolu bir tatil üssü arayanların terciidir.",
        "desc_en": "Located in the elite Lud area of Bitez, this hotel merges modern comfort with the freshness of the Aegean. With its stylish beach and refined service, it's the choice for those seeking a luxury and peaceful holiday base within the town."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Bodrum Bulk - FINAL)...")
enrich_venues("bodrum", bodrum_final_updates)
print("✨ Systematic Enrichment - Bodrum Bulk FINAL Complete.")
