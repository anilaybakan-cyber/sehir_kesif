from enrich_venues import enrich_venues

# BATCH: KAŞ SYSTEMATIC COMPLETION - PART 1

kas_bulk_1_updates = {
    "Manzara": {
        "desc_tr": "Kaş'ın en panoramik noktalarından biri olan bu seyir alanı, tüm kenti ve hemen karşısındaki Meis Adası'nı ayaklarınızın altına serer. Özellikle gün batımında kentin ışıklarının denize vurduğu o eşsiz anı izlemek için en popüler duraktır.",
        "desc_en": "One of Kaş's most panoramic spots, this viewpoint puts the entire town and the neighboring Meis Island right under your feet. It's the most popular place to watch the golden sunset and the city lights dancing on the sea."
    },
    "Tuğra Art Gallery": {
        "desc_tr": "Kaş'ın sanatsal dokusunu yansıtan Tuğra Art, yerel sanatçıların el emeği takılarını, seramiklerini ve özgün eserlerini sergiler. Kentin bohem ruhunu yanınızda götürmek için keşfedebileceğiniz en şık ve yaratıcı noktalardan biridir.",
        "desc_en": "Reflecting Kaş's artistic soul, Tuğra Art showcases handmade jewelry, ceramics, and original works by local artists. It’s one of the most stylish and creative spots to discover and take a piece of the town's bohemian spirit back home."
    },
    "Boat Trips by Captain Ergun | Kekova Tekne Turu | Kaş Tekne Turu | Кекова прогулка на лодке | Tekne Kiralama": {
        "desc_tr": "Kaş'ın en köklü denizcilik ekiplerinden biri olan Kaptan Ergun, misafirlerini Kekova'nın batık şehirlerine ve turkuaz koylarına ulaştırır. Profesyonel hizmeti ve lezzetli teknede öğle yemekleriyle, kentin en iyi mavi tur deneyimlerinden birini sunar.",
        "desc_en": "One of Kaş's most established maritime teams, Captain Ergun takes guests to the sunken cities and turquoise bays of Kekova. With professional service and delicious lunches served on board, it offers one of the best blue cruise experiences in town."
    },
    "Kaş Sailing & Catamaran Tours / Kaş / Turkey (Daily or Overnight) Rent a sailing yacht in Kas": {
        "desc_tr": "Akdeniz'in huzurlu sularında yelken açmanın en prestijli yolu olan bu turlar, günlük veya konaklamalı katamaran deneyimleri sunar. Rüzgarın eşlik ettiği bu sessiz yolculuk, Kaş'ın bakir koylarını keşfetmek için en sofistike rotadır.",
        "desc_en": "The most prestigious way to sail the peaceful waters of the Mediterranean, these tours offer daily or overnight catamaran experiences. This quiet, wind-powered journey is the most sophisticated route to exploring the pristine bays of Kaş."
    },
    "Hellenistic theatre": {
        "desc_tr": "Antik Antiphellos kentinin en görkemli kalıntısı olan bu tiyatro, denize doğru bakan nadir antik yapılardan biridir. Restorasyonuyla kentin silüetine değer katan tiyatro, bugün hala konserlere ve muazzam gün batımı manzaralarına ev sahipliği yapar.",
        "desc_en": "The most majestic ruin of the ancient city of Antiphellos, this theater is one of the rare ancient structures facing the sea. Adding value to the town's skyline, it still hosts concerts and offers breathtaking sunset views today."
    },
    "Great chair. Acdam doric tomb in Antiphellos ancient city": {
        "desc_tr": "Antik Antiphellos'un tepelerinde yer alan bu Dor tipi mezar yapısı, sağlam mimarisi ve kente hakim konumuyla dikkat çeker. Kayadan oyulmuş bu görkemli anıt, Kaş'ın Likya döneminden kalan en etkileyici tarihi miraslarından biridir.",
        "desc_en": "Located on the heights of ancient Antiphellos, this Doric-style tomb stands out for its solid architecture and commanding view of the town. This majestic rock-carved monument is one of Kaş's most impressive Lycian-era heritages."
    },
    "konaklama sepeti": {
        "desc_tr": "Kaş ve çevresindeki en seçkin villa ve apart seçeneklerini bir araya getiren bu merkez, konaklama deneyiminizi kişiselleştirir. Kentin otantik evlerinden lüks peninsulaya kadar, hayalinizdeki Akdeniz tatili için en doğru konaklama pusulasıdır.",
        "desc_en": "Bringing together the most exclusive villa and apartment options in and around Kaş, this hub personalizes your stay. From authentic townhouses to luxury peninsula villas, it’s the perfect compass for your dream Mediterranean holiday."
    },
    "Kas photo spot": {
        "desc_tr": "Uzun Çarşı'nın girişinde veya begonvillerle süslü taş evlerin arasında yer alan bu nokta, kentin en fotografik karesidir. Kaş'ın ikonik renklerini, Likya lahitlerini ve çiçekli sokaklarını tek bir kadrajda yakalayabileceğiniz bir görsel mirastır.",
        "desc_en": "Located at the entrance to Uzun Çarşı or among bougainvillea-covered stone houses, this spot is the town's most photographic. It's a visual heritage where you can capture iconic colors, Lycian tombs, and flowery alleys in a single frame."
    },
    "Seatown Hotel": {
        "desc_tr": "Kaş'ın kalbinde, her sabah Meis Adası manzarasına uyanabileceğiniz şık ve modern bir butik oteldir. Minimalist tasarımı ve kentin sosyal hayatına yakınlığıyla, hem konforu hem de kentsel hareketliliği arayanlar için idealdir.",
        "desc_en": "A stylish and modern boutique hotel in the heart of Kaş, where you can wake up to views of Meis Island every morning. With its minimalist design and proximity to social life, it’s ideal for those seeking both comfort and urban energy."
    },
    "Caretta Wall Kaş": {
        "desc_tr": "Kaş'ın en meşhur sualtı rotalarından biri olan Caretta Wall, dik kayalık yapısı ve deniz kaplumbağalarına ev sahipliği yapmasıyla bilinir. Kristal berraklığındaki suyu ve zengin sualtı faunasıyla, dalış tutkunları için bölgenin en heyecan verici noktasıdır.",
        "desc_en": "One of Kaş's most famous diving routes, Caretta Wall is known for its steep underwater cliffs and resident loggerhead turtles. With crystal-clear water and rich marine life, it's the area's most exciting spot for diving enthusiasts."
    },
    "Kaş Belediye Çarşısı": {
        "desc_tr": "Kentin sosyal yaşamının merkezinde yer alan bu çarşı, yerel üreticilerin taze ürünlerinden el sanatı hediyeliklere kadar pek çok seçenek sunar. Kaş'ın mahalle kültürünü tanımanıza yardımcı olan, kentsel dokunun en samimi parçasıdır.",
        "desc_en": "At the center of social life, this market offers everything from fresh local produce to handcrafted souvenirs. It’s one of the most warming parts of the urban fabric, helping you get to know Kaş’s neighborhood culture."
    },
    "Larsoy Travel & Tourism Office || ⛵️ Kekova Boat Tour || 🚙 Rent a Car || 🛵 Rent a Motorbike || ⛴️ Meis Ferry Ticket ||": {
        "desc_tr": "Kaş tatilinizi planlarken tüm ulaşım ve tur ihtiyaçlarınızı karşılayan bu ofis, Meis feribot bileti ve Kekova turlarında uzmandır. Kentin en güvenilir turizm duraklarından biri olarak, kenti ve çevresini keşfetmeniz için profesyonel çözümler sunar.",
        "desc_en": "A one-stop shop for all your transportation and tour needs in Kaş, this office specializes in Meis ferry tickets and Kekova tours. It is a reliable tourism hub providing professional solutions for exploring the town and its surroundings."
    },
    "Handmade Bracelets": {
        "desc_tr": "Kaş çarşısının renkli tezgahlarında, yerel zanaatkarların sabırla işlediği bu el yapımı bileklikler kentin bohem modasını yansıtır. Her biri bir hikaye taşıyan bu takılar, kentin yaratıcı enerjisini bileğinizde taşımanıza olanak sağlar.",
        "desc_en": "On the colorful stalls of the Kaş bazaar, these handmade bracelets, patiently crafted by local artisans, reflect the town's bohemian fashion. Each piece carries a story, allowing you to wear the town's creative energy on your wrist."
    },
    "Kekova tekne turu": {
        "desc_tr": "Kaş'tan kalkan ve tarihin sular altında kaldığı antik Simena'ya uzanan bu yolculuk, Akdeniz'in en büyüleyici deneyimidir. Turkuaz koylar, lahitler ve batık şehirler eşliğinde geçen bu tur, kentin mutlaka yapılması gerekenler listesinin en başındadır.",
        "desc_en": "Departing from Kaş and reaching ancient Simena, where history is submerged, this journey is the Mediterranean's most magical experience. Surrounded by turquoise bays and sunken ruins, it tops the town's must-do list."
    },
    "Kaş Merkez": {
        "desc_tr": "Kaş'ın beyaz badanalı evleri, Likya lahitleri ve begonvilli dar sokaklarıyla kentsel ruhunun attığı kalptir. Harbour çevresindeki balıkçı tekneleri ve Uzun Çarşı'nın butikleriyle, kentin en ikonik ve yaşayan kentsel dokusunu temsil eder.",
        "desc_en": "The heart of Kaş's urban spirit, with its whitewashed houses, Lycian sarcophagi, and narrow bougainvillea-filled alleys. With the fishing boats at the harbor and the boutiques of Uzun Çarşı, it represents the town's most iconic and living fabric."
    },
    "Atatürk Heykeli": {
        "desc_tr": "Kaş Limanı'nın girişinde, kentin en büyük ve görkemli meydanında yer alan bu heykel, resmi kutlamaların ve kentsel buluşmaların merkezidir. Meydandaki palmiyeler ve deniz manzarası eşliğinde, kentin girişini simgeleyen bir saygı duruşu niteliğindedir.",
        "desc_en": "Standing at the entrance to Kaş Harbor in the town's largest square, this statue is the hub for official celebrations and local gatherings. Set against palms and sea views, it serves as a symbolic salutation at the city's entrance."
    },
    "Hideaway Hotel": {
        "desc_tr": "Kaş Yarımadası'nın sessiz köşelerinden birinde yer alan bu otel, denize sıfır konumu ve panoramik terasıyla huzur vaat eder. Geleneksel Akdeniz mimarisiyle tasarlanmış odaları ve samimi bahçesiyle, tam bir kaçış noktasıdır.",
        "desc_en": "Located in a quiet corner of the Kaş Peninsula, this hotel promises peace with its seafront location and panoramic terrace. With Mediterranean-inspired rooms and a cozy garden, it is the perfect seaside escape."
    },
    "Amphora Hotel": {
        "desc_tr": "Çukurbağ Yarımadası'nda konumlanan Amphora, kentin en prestijli konaklama noktalarından biridir. Kendine ait plaj platformu, büyük yüzme havuzu ve kente hakim muazzam gün batımı manzarasıyla lüksün ve dinginliğin adresidir.",
        "desc_en": "Situated on the Çukurbağ Peninsula, Amphora is one of the town's most prestigious stay options. With its private beach platform, large pool, and immense sunset views over the town, it is a haven of luxury and tranquility."
    },
    "Hotel Sonne": {
        "desc_tr": "Merkezi konumu ve sadece yetişkinlere özel konseptiyle Hotel Sonne, Kaş'ta modern ve huzurlu bir konaklama sunar. Şık tasarımı ve Meis Adası'na bakan kahvaltı terasıyla, kentin en nezih ve sakin duraklarından biridir.",
        "desc_en": "With its central location and adult-only concept, Hotel Sonne offers a modern and peaceful stay in Kaş. Its chic design and breakfast terrace overlooking Meis Island make it one of the town's most refined and calm spots."
    },
    "Mavilim Otel": {
        "desc_tr": "Kaş'ın en uç noktasında, mavinin her tonuna hakim konumuyla Mavilim Otel, butik lüksün en zarif örneklerinden biridir. Denizin hemen yanı başındaki rüya gibi odaları ve sessiz ambiyansıyla, Ege ve Akdeniz'in buluşma noktasının en romantik köşesidir.",
        "desc_en": "Perched at the tip of the peninsula with a view of every shade of blue, Mavilim Otel is a prime example of boutique elegance. With dreamy rooms by the waves and a quiet ambiance, it’s the most romantic corner where the Aegean meets the Mediterranean."
    },
    "Kas Doga Park Hotel": {
        "desc_tr": "Kaş'ın girişinde, geniş bahçeleri ve doğayla uyumlu mimarisiyle dikkat çeken bu otel, ferah bir konaklama arayan aileler için idealdir. Şehrin gürültüsünden uzak, yeşil ve mavinin kucaklaştığı huzurlu bir kentsel vahadır.",
        "desc_en": "Located at the entrance to Kaş, this hotel stands out with its large gardens and nature-harmonious architecture. It’s an ideal peaceful oasis for families seeking a spacious stay where green and blue embrace, away from the urban noise."
    },
    "Doria Hotel & Yacht Club": {
        "desc_tr": "Kaş Marina'ya komşu olan bu prestijli tesis, modern tasarımı ve yüksek kaliteli yacht kulübü hizmetleriyle bilinir. Kendi plajı, gurme restoranı ve marinaya hakim konumuyla, kentin en elit ve sofistike konaklama deneyimini sunar.",
        "desc_en": "Neighboring the Kaş Marina, this prestigious hotel is known for its modern design and high-quality yacht club services. With its own beach, luxury dining, and marina views, it offers the town's most elite and sophisticated stay."
    },
    "Seaview Otel": {
        "desc_tr": "Yarımadanın tepelerinde, adeta bulutların üzerinde konaklıyormuş hissi veren Seaview, kentin en geniş panoramik manzarasına sahiptir. Kaş'ı ve adaları kuşbakışı izleyebileceğiniz sonsuzluk havuzuyla, kentin en estetik duraklarından biridir.",
        "desc_en": "Perched on the peninsula's heights, Seaview gives the feeling of staying above the clouds with the town's widest panoramic view. Its infinity pool overlooking Kaş and the islands makes it one of the city's most aesthetic spots."
    },
    "bayNURIS - Marina&Resort": {
        "desc_tr": "Kaş Marina'nın hemen girişinde yer alan BayNuris, modern resort konseptini butik bir samimiyetle harmanlar. Şık iskelesi ve kentin sosyal hayatına yürüme mesafesindeki konumuyla, Kaş tatiline ayrıcalıklı bir konfor katar.",
        "desc_en": "At the gateway to Kaş Marina, BayNuris blends a modern resort concept with boutique warmth. With its stylish pier and location within walking distance of social life, it adds exclusive comfort to any Kaş holiday."
    },
    "Club Barbarossa Hotel & Villas": {
        "desc_tr": "Kaş'ın en ikonik tesislerinden biri olan Club Barbarossa, denizin içinde yükselen taş platformları ve Likya stili villalarıyla benzersizdir. Doğal dokuyu lüksle birleştiren tesis, kentin en büyüleyici deniz ve gün batımı teraslarına sahiptir.",
        "desc_en": "One of Kaş's most iconic spots, Club Barbarossa is unique for its stone platforms rising from the sea and Lycian-style villas. Merging natural texture with luxury, it boasts the town's most magical sea and sunset terraces."
    },
    "Korsan Ada Hotel": {
        "desc_tr": "Yarımadanın sakin ucunda yer alan Korsan Ada, ismini karşıdaki adalardan alır ve misafirlerine kesintisiz bir deniz manzara eşliğinde huzur sunar. Şık ve sade odalarıyla, kentin karmaşasını arkasında bırakmak isteyenlerin gizli limanıdır.",
        "desc_en": "Located on the quiet tip of the peninsula, Korsan Ada takes its name from the islands across and offers guests peace with uninterrupted sea views. With chic, simple rooms, it’s a hidden harbor for those leaving the urban rush behind."
    },
    "Cafe Corner Restaurant": {
        "desc_tr": "Kaş'ın tam göbeğinde, kentin kentsel ritmini en iyi hissedebileceğiniz Cafe Corner, zengin menüsü ve samimi atmosferiyle bir buluşma noktasıdır. Meydana ve begonvilli sokaklara hakim masalarıyla, kentin en canlı ve nezih duraklarındandır.",
        "desc_en": "In the very heart of Kaş, Cafe Corner is a meeting point where you can best feel the city's pulse. With its rich menu and tables overlooking the square and bougainvillea-covered alleys, it’s one of the town's most vibrant spots."
    },
    "Smiley's": {
        "desc_tr": "Kaş sahil yolunun en sevilen lezzet duraklarından biri olan Smiley's, taze balıkları ve özellikle karides güveciyle meşhurdur. Samimi servisi ve denize nazır masalarıyla, kentin gerçek denizci mutfağını tatmak için en doğru adrestir.",
        "desc_en": "A beloved flavor destination on the Kaş coast road, Smiley's is famous for its fresh fish and signature shrimp casserole. With friendly service and tables facing the sea, it's the best place to taste authentic local maritime cuisine."
    },
    "Cinarlar Grup": {
        "desc_tr": "Kaş'ın kentsel ticaret ve gastronomi hayatında önemli bir yer tutan bu işletme, kentin en popüler pizza ve kafe duraklarını bünyesinde barındırır. Kaliteli hizmet anlayışıyla, Kaş'ın modern sosyal yüzünü temsil eden bir kentsel markadır.",
        "desc_en": "Playing a major role in Kaş's urban commerce and gastronomy, this group hosts some of the town's most popular pizza and cafe spots. With its commitment to quality, it is a local brand representing the modern social face of Kaş."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Kaş Bulk - Part 1)...")
enrich_venues("kas", kas_bulk_1_updates)
print("✨ Systematic Enrichment - Kaş Bulk Part 1 Complete.")
