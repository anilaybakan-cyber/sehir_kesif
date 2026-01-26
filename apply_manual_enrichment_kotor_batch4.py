import json

# Manual enrichment data (Kotor Batch 4: 40 items)
updates = {
    "Church of St. Mary Collegiate": {
        "description": "13. yüzyıldan kalma, içinde Azize Ozana Kotorska'nın 600 yıldır bozulmamış bedeninin cam bir tabut içinde sergilendiği önemli Katolik kilisesi. Kotor'un en değerli dini hazinelerinden birini barındıran, hac için önemli bir durak.",
        "description_en": "A 13th-century Catholic church displaying the incorrupt body of Saint Ozana of Kotor in a glass coffin, untouched for 600 years. An important pilgrimage stop housing one of Kotor's most precious religious treasures."
    },
    "Karampana Well": {
        "description": "Eskiden şehrin tek tatlı su kaynağı olan, barok dönemden kalma süslemeli tarihi kuyu. Karapana Meydanı'nın ortasında yer alan bu yapı, eski şehir yaşamının önemli bir parçası olarak korunuyor.",
        "description_en": "A historic well with baroque decorations, once the city's only freshwater source. Located in the center of Karapana Square, this structure is preserved as an important part of old city life."
    },
    "Cinema Square": {
        "description": "Ortasında asırlık büyük bir ağacın gölgelendirdiği, eski sinema binasının bulunduğu atmosferik meydan. Şimdi açık hava kafeleri, küçük sergiler ve yerel müzisyenlere ev sahipliği yapan canlı bir buluşma noktası.",
        "description_en": "An atmospheric square shaded by a centuries-old large tree in the center, where the old cinema building is located. Now a lively meeting point hosting outdoor cafes, small exhibitions, and local musicians."
    },
    "Salad Square": {
        "description": "Eskiden taze sebze pazarının kurulduğu, şimdi şık kafeler ve restoranlarla çevrili tarihi meydan. Kotor'un günlük yaşamının nabzını tutabileceğiniz, yerel halkın öğle molası için tercih ettiği hareketli bir köşe.",
        "description_en": "A historic square where a fresh vegetable market once stood, now surrounded by stylish cafes and restaurants. A lively corner where you can feel the pulse of Kotor's daily life, preferred by locals for lunch breaks."
    },
    "Konoba Trpeza": {
        "description": "Taze Adriyatik balıkları ve deniz ürünlerinin zarif sunumlarıyla öne çıkan, Kotor'un en kaliteli restoranlarından biri. Şarap kavı, profesyonel servisi ve romantik atmosferiyle özel akşam yemekleri için ideal bir adres.",
        "description_en": "One of Kotor's finest restaurants, featuring elegant presentations of fresh Adriatic fish and seafood. An ideal address for special dinners with its wine cellar, professional service, and romantic atmosphere."
    },
    "Luna Rossa": {
        "description": "Geleneksel Karadağ mutfağının en iyi örneklerini, özellikle meşhur Njeguški biftek ve kuzu etlerini sunan otantik restoran. Taş duvarlar, mumlar ve canlı müzikle çerçevelenen sıcak atmosferi, yerel lezzetleri keşfetmek için mükemmel.",
        "description_en": "An authentic restaurant offering the best examples of traditional Montenegrin cuisine, especially the famous Njeguški steak and lamb dishes. Perfect for discovering local flavors with its warm atmosphere framed by stone walls, candles, and live music."
    },
    "Hostel Pupa Bar": {
        "description": "Sırtçantalı gezginlerin sosyalleştiği, uygun fiyatlı içkiler ve canlı atmosferiyle ünlü rahat bar. Kotor'un gece hayatına dalmak, yeni insanlarla tanışmak ve yerel seyahat ipuçları almak için harika bir başlangıç noktası.",
        "description_en": "A comfortable bar where backpackers socialize, famous for its affordable drinks and lively atmosphere. A great starting point to dive into Kotor's nightlife, meet new people, and get local travel tips."
    },
    "Church of St. Eustahije": {
        "description": "Dobrota kıyısında konumlanan, deniz manzaralı güzel terasıyla ve etkileyici çan kulesiyle dikkat çeken tarihi kilise. Venedik döneminden kalma eserleri ve huzurlu atmosferiyle, sahil yürüyüşlerinde mola vermek için ideal.",
        "description_en": "A historic church on the Dobrota coast, notable for its beautiful terrace with sea views and impressive bell tower. Ideal for taking a break during coastal walks with its Venetian-era artifacts and peaceful atmosphere."
    },
    "Mudra Art Cuisine": {
        "description": "Lüks Huma Hotel bünyesinde, modern gastronomi ve sanatı bir araya getiren sofistike restoran. Yaratıcı tabaklar, özenli sunumlar ve körfez manzarasıyla, özel bir yemek deneyimi arayanlar için Kotor'un en prestijli adreslerinden.",
        "description_en": "A sophisticated restaurant within the luxury Huma Hotel, combining modern gastronomy and art. One of Kotor's most prestigious addresses for those seeking a special dining experience with creative dishes, meticulous presentations, and bay views."
    },
    "Radonicich Palace": {
        "description": "Dobrota'nın zengin kaptan ailelerine ait, 18. yüzyıldan kalma görkemli barok saray. Denizcilik tarihine tanıklık eden mimarisi ve dekoratif ayrıntılarıyla, körfezin aristokratik geçmişini yansıtan önemli bir anıt.",
        "description_en": "A magnificent baroque palace from the 18th century belonging to Dobrota's wealthy captain families. An important monument reflecting the bay's aristocratic past with its architecture and decorative details witnessing maritime history."
    },
    "Tripkovic Palace": {
        "description": "18. yüzyıldan kalma, Dobrota'nın en görkemli ve büyük tarihi saraylarından biri. Venedik tarzı cephe süslemeleri, geniş bahçesi ve denize bakan konumuyla, kaptan ailelerinin zenginliğini gözler önüne seriyor.",
        "description_en": "One of Dobrota's most magnificent and largest historic palaces from the 18th century. Displaying captain families' wealth with Venetian-style facade decorations, large garden, and sea-facing position."
    },
    "Cogimar Beach": {
        "description": "Gündüz güneş ve deniz keyfi, akşam ise kokteyl ve müzik eşliğinde eğlence sunan çok amaçlı plaj mekanı. DJ setleri, plaj partileri ve şık atmosferiyle, Kotor'un genç ve enerjik kitlesinin favorisi.",
        "description_en": "A multipurpose beach venue offering sun and sea enjoyment by day, entertainment with cocktails and music by evening. A favorite of Kotor's young and energetic crowd with DJ sets, beach parties, and stylish atmosphere."
    },
    "Aquarium Boka": {
        "description": "Adriyatik denizi ve Kotor Körfezi'nin zengin deniz yaşamını tanıtan, Karadağ'ın kuzey bölgesindeki tek akvaryum. Çocuklar ve aileler için eğitici, yağmurlu günlerde ziyaret edilebilecek keyifli bir mekan.",
        "description_en": "The only aquarium in Montenegro's northern region introducing the rich marine life of the Adriatic Sea and Bay of Kotor. An enjoyable place to visit on rainy days, educational for children and families."
    },
    "Almara Beach Club": {
        "description": "Lustica yarımadasında, beyaz kumları ve turkuaz suları ile cennet gibi bir plaj kulübü. Şezlonglar, havuzbaşı barlar, gourmet yemekler ve profesyonel servisle, lüks bir plaj günü yaşamak isteyenler için ideal.",
        "description_en": "A paradise-like beach club on the Lustica Peninsula with white sand and turquoise waters. Ideal for those wanting to experience a luxury beach day with sunbeds, poolside bars, gourmet food, and professional service."
    },
    "Fort Arza": {
        "description": "Avusturya-Macaristan İmparatorluğu döneminden kalma, Lustica yarımadasının ucunda denize bakan etkileyici deniz kalesi. Restore edilerek butik bir otele dönüştürülmüş olup, tarihi atmosferde benzersiz bir konaklama sunuyor.",
        "description_en": "An impressive sea fortress from the Austro-Hungarian Empire era, overlooking the sea at the tip of the Lustica Peninsula. Restored and converted into a boutique hotel, offering unique accommodation in a historic atmosphere."
    },
    "The Clubhouse": {
        "description": "Porto Montenegro marinasında, yat sahiplerinin ve marina personelinin buluşma noktası olan rahat bar ve restoran. Canlı atmosfer, spor yayınları ve kaliteli içkilerle, marinanın sosyal merkezi.",
        "description_en": "A comfortable bar and restaurant at Porto Montenegro marina, a meeting point for yacht owners and marina staff. The marina's social center with lively atmosphere, sports broadcasts, and quality drinks."
    },
    "Big Ben": {
        "description": "Tivat'ın deniz kenarında, geniş terasıyla yerel halkın ve turistlerin buluştuğu popüler kafe ve restoran. Kahvaltıdan gece içkilerine kadar geniş menüsü ve rahat ortamıyla, her saate uygun bir mekan.",
        "description_en": "A popular cafe and restaurant on Tivat's seaside with a wide terrace where locals and tourists meet. A venue suitable for every hour with its extensive menu from breakfast to evening drinks and comfortable atmosphere."
    },
    "Waikiki Beach Tivat": {
        "description": "Tivat şehir merkezine yakın, şezlongları, güneşlenme alanları ve sahil restoranıyla donatılmış popüler plaj. Yüzme, güneşlenme ve deniz kenarında yemek yemek için aileler ve gençlerin tercih ettiği canlı bir sahil.",
        "description_en": "A popular beach near Tivat city center, equipped with sunbeds, sunbathing areas, and a beach restaurant. A lively shore preferred by families and young people for swimming, sunbathing, and eating by the sea."
    },
    "St. Sava Church": {
        "description": "Tivat'ın en büyük Ortodoks kilisesi, şehrin siluetini belirleyen kubbesi ve çan kulesiyel dikkat çekiyor. Modern içi tasarımı, ikonaları ve cemaat aktiviteleriyle, dini ve kültürel yaşamın merkezi.",
        "description_en": "Tivat's largest Orthodox church, notable for its dome and bell tower defining the city's silhouette. The center of religious and cultural life with its modern interior design, icons, and community activities."
    },
    "Ponta Seljanovo": {
        "description": "Deniz fenerinin bulunduğu burnun ucunda, düz kayalar üzerinde güneşlenme ve yüzme için ideal bir nokta. Şezlong veya restoran olmayan, doğal haliyle korunan, yerel halkın favorisi sakin bir köşe.",
        "description_en": "An ideal spot for sunbathing and swimming on flat rocks at the tip of the cape where the lighthouse is located. A quiet corner preferred by locals, preserved in its natural state without sunbeds or restaurants."
    },
    "Maestral": {
        "description": "Kalardovo plajı yakınında, özellikle lezzetli kalamar ve ahtapot yemekleriyle ünlü, deniz kenarında konumlanan restoran. Taze deniz ürünleri, yerel şaraplar ve rahat atmosferiyle, yemek molası için güvenilir bir adres.",
        "description_en": "A seaside restaurant near Kalardovo beach, especially famous for its delicious squid and octopus dishes. A reliable address for a meal break with fresh seafood, local wines, and relaxed atmosphere."
    },
    "Savina Monastery": {
        "description": "Herceg Novi'nin hemen dışında, 11. yüzyılda kurulan barok mimarisi ve muhteşem körfez manzarasıyla büyüleyen tarihi Ortodoks manastırı. Freskleri, antik ikonaları ve huzurlu bahçeleriyle, bölgenin en önemli dini merkezlerinden.",
        "description_en": "A historic Orthodox monastery just outside Herceg Novi, established in the 11th century, enchanting with its baroque architecture and magnificent bay views. One of the region's most important religious centers with its frescoes, ancient icons, and peaceful gardens."
    },
    "Skver Harbor": {
        "description": "Herceg Novi'nin kalbi ve ana buluşma noktası olan tarihi liman meydanı. Denizcilerin, balıkçıların ve gezginlerin kaynaştığı bu canlı alan, sahil restoranları, tatlı dükkanları ve tekne turlarının hareket noktası.",
        "description_en": "The historic harbor square at the heart of Herceg Novi and main meeting point. This lively area where sailors, fishermen, and travelers mingle is the departure point for coastal restaurants, sweet shops, and boat tours."
    },
    "Belavista Square": {
        "description": "Herceg Novi'nin eski şehrinin (Stari Grad) ana meydanı, şehrin vizyonunu ve anlamını temsil eden başmelek Mikail heykeline ev sahipliği yapıyor. Kafeler, butikler ve panoramik manzarasıyla, tarihi merkezin kalbi.",
        "description_en": "The main square of Herceg Novi's old town (Stari Grad), hosting the statue of Archangel Michael representing the city's vision and meaning. The heart of the historic center with cafes, boutiques, and panoramic views."
    },
    "Igalo Mud Beach": {
        "description": "Şifalı olduğuna inanılan çamuruyla ünlü, Igalo'nun termal turizm merkezindeki benzersiz plaj. Romatizma, cilt hastalıkları ve eklem rahatsızlıkları için doğal tedavi arayanların ziyaret ettiği sağlık turizmi destinasyonu.",
        "description_en": "A unique beach in Igalo's thermal tourism center, famous for its mud believed to have healing properties. A health tourism destination visited by those seeking natural treatment for rheumatism, skin diseases, and joint disorders."
    },
    "Lipci Prehistoric Drawings": {
        "description": "M.Ö. 8. yüzyıla tarihlenen, kaya yüzeyine oyulmuş geyik avı sahnelerini içeren tarih öncesi mağara sanatı. Risan yakınlarında bulunan bu antik eserler, bölgenin binlerce yıllık insan yerleşiminin kanıtı.",
        "description_en": "Prehistoric rock art dating to the 8th century BC, featuring deer hunting scenes carved on rock surfaces. These ancient artifacts found near Risan are evidence of thousands of years of human settlement in the region."
    },
    "Forza Mare": {
        "description": "Ünlü yıldızların ve jet sosyetenin tercih ettiği, Kotor Körfezi'nin en lüks butik otellerinden biri. Özel plajı, spa'sı, gurme restoranı ve Adriyatik manzaralı süitleriyle, benzersiz bir lüks deneyim sunuyor.",
        "description_en": "One of the Bay of Kotor's most luxurious boutique hotels, preferred by famous stars and jet setters. Offering a unique luxury experience with its private beach, spa, gourmet restaurant, and suites with Adriatic views."
    },
    "Tramontana Beach Bar": {
        "description": "Morinj plajında, devasa ağaçların gölgesinde rahat bir atmosfer sunan sahil barı. Dalgaların sesi, soğuk içkiler ve basit ama lezzetli atıştırmalıklarla, plaj gününün tadını çıkarmak için mükemmel bir dinlenme noktası.",
        "description_en": "A beach bar on Morinj beach offering a relaxed atmosphere in the shade of giant trees. A perfect resting point to enjoy a beach day with the sound of waves, cold drinks, and simple but delicious snacks."
    },
    "Palazzo Radomiri": {
        "description": "18. yüzyıldan kalma tarihi bir kaptan sarayından dönüştürülmüş, deniz kenarında konumlanan lüks butik otel. Antik mobilyalar, özgün dekorasyon ve Adriyatik manzaralı odalarıyla, romantik bir konaklama deneyimi sunuyor.",
        "description_en": "A luxury boutique hotel located by the sea, converted from an 18th-century historic captain's palace. Offering a romantic accommodation experience with antique furniture, original decoration, and rooms with Adriatic views."
    },
    "Orahovac Beach": {
        "description": "Kotor Körfezi'nin güneşi en uzun süre alan plajlarından biri, meşe ağaçlarıyla çevrili huzurlu ortamıyla dikkat çekiyor. Çakıl taşlı kumsalı, berrak suları ve sahil restoranlarıyla, sakin bir yüzme deneyimi için ideal.",
        "description_en": "One of the beaches in the Bay of Kotor receiving the longest sunshine, notable for its peaceful environment surrounded by oak trees. Ideal for a calm swimming experience with its pebble beach, clear waters, and coastal restaurants."
    },
    "Church of St. Matthew": {
        "description": "Dobrota'da, İtalyan Rönesans ustası Giovanni Bellini'nin 'Madonna ve Çocuk' tablosuna ev sahipliği yapan tarihi kilise. Bu değerli sanat eseri, küçük kiliseyi Adriyatik bölgesinin önemli kültürel duraklarından biri yapıyor.",
        "description_en": "A historic church in Dobrota housing a 'Madonna and Child' painting by Italian Renaissance master Giovanni Bellini. This valuable artwork makes the small church one of the important cultural stops in the Adriatic region."
    },
    "Radoncic Palace": {
        "description": "Dobrota'nın denizci kaptan ailelerinin zenginliğini ve sosyal statüsünü yansıtan, 18. yüzyıldan kalma görkemli barok saray. Körfez manzaralı cephesi ve tarihi atmosferiyle, denizcilik tarihine tanıklık eden bir anıt.",
        "description_en": "A magnificent baroque palace from the 18th century reflecting the wealth and social status of Dobrota's seafaring captain families. A monument witnessing maritime history with its bay-view facade and historic atmosphere."
    },
    "Church of St. Elijah": {
        "description": "Yukarı Stoliv köyünün tepesinde konumlanan, çan kulesinden Kotor Körfezi'nin muhteşem manzarasını sunan küçük ama etkileyici kilise. Köy atmosferi ve panoramik görünümüyle, zorlu yürüyüşün ödüllendirici bir finali.",
        "description_en": "A small but impressive church located on top of Upper Stoliv village, offering magnificent views of the Bay of Kotor from its bell tower. A rewarding finale to the challenging hike with its village atmosphere and panoramic views."
    },
    "Markov Rt": {
        "description": "Kotor Körfezi'nin daha sakin güney tarafında bulunan, uzun çakıl taşlı kumsalı ve berrak sularıyla popüler plaj. Yerel aileler ve yüzme tutkunlarının tercih ettiği, kalabalık Kotor plajlarına alternatif bir destinasyon.",
        "description_en": "A popular beach on the calmer southern side of the Bay of Kotor with its long pebble beach and clear waters. An alternative destination to crowded Kotor beaches, preferred by local families and swimming enthusiasts."
    },
    "Bronza Palace": {
        "description": "Eskiden Venedik döneminde gümrük binası olarak kullanılan, Kotor'un tarihi limanına bakan görkemli yapı. Ticaret tarihine tanıklık eden bu bina, şehrin deniz ticareti geçmişinin önemli bir parçası.",
        "description_en": "A magnificent building overlooking Kotor's historic harbor, once used as a customs house in the Venetian period. This building witnessing trade history is an important part of the city's maritime commerce past."
    },
    "Morinj Beach": {
        "description": "Tatlı su kaynaklarının denize karıştığı noktada bulunan, benzersiz ekosistemine sahip çakıl taşlı plaj. Karstik pınarların soğuk sularıyla serinleyebileceğiniz, körfezin en otantik ve sakin plajlarından biri.",
        "description_en": "A pebble beach with a unique ecosystem at the point where freshwater springs meet the sea. One of the bay's most authentic and quiet beaches where you can cool off in the cold waters of karst springs."
    },
    "Ladovina Kitchen & Wine Bar": {
        "description": "Kotor eski şehrinin hemen dışında, ağaçlarla gölgelenen güzel bir bahçede hizmet veren şık restoran ve şarap barı. Modern Karadağ mutfağı, yerel şaraplar ve romantik atmosferiyle, özel akşamlar için mükemmel.",
        "description_en": "A stylish restaurant and wine bar serving in a beautiful garden shaded by trees just outside Kotor's old town. Perfect for special evenings with modern Montenegrin cuisine, local wines, and romantic atmosphere."
    },
    "Mon Ami": {
        "description": "Silah Meydanı'na bakan konumuyla, özellikle kahvaltı ve ev yapımı dondurmalarıyla ünlü şirin kafe. Güçlü espresso, taze hamur işleri ve meydan manzarasıyla, güne başlamak için ideal bir durak.",
        "description_en": "A cute cafe overlooking the Square of Arms, especially famous for its breakfast and homemade ice cream. An ideal stop to start the day with strong espresso, fresh pastries, and square views."
    },
    "Konoba Akustik": {
        "description": "Skurda Nehri kenarında, akşamları canlı müzik eşliğinde yemek yiyebileceğiniz atmosferik restoran. Nehrin şırıltısı, yerel lezzetler ve samimi ortamıyla, Kotor'un en romantik yemek deneyimlerinden birini sunuyor.",
        "description_en": "An atmospheric restaurant by the Skurda River where you can dine accompanied by live music in the evenings. Offering one of Kotor's most romantic dining experiences with the babbling of the river, local flavors, and intimate atmosphere."
    }
}

filepath = 'assets/cities/kotor.json'
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

print(f"\n✅ Manually enriched {count} items (Kotor Batch 4).")
