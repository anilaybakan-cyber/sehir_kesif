import json

# Manual enrichment data (Kotor Batch 5 - FINAL: 50 items)
updates = {
    "Napoleon Tiyatrosu": {
        "description": "Fransız işgali döneminden (1807-1813) kalma, Kotor'un dar sokaklarında gizlenmiş tarihi küçük tiyatro. Napolyon ordusunun askerleri için inşa edilmiş bu yapı, şehrin çok katmanlı tarihine ve Fransız etkisine tanıklık ediyor.",
        "description_en": "A historic small theater from the French occupation period (1807-1813), hidden in Kotor's narrow streets. This structure built for Napoleon's army soldiers witnesses the city's multi-layered history and French influence."
    },
    "Letrika Caffe Bar": {
        "description": "Sanatsal dekorasyonu, vintage mobilyaları ve rahat ortamıyla yerel sanatçıların ve entelektüellerin buluştuğu atmosferik kafe. Özel kahve çeşitleri, el yapımı tatlılar ve kitaplı köşeleriyle, sakin bir mola için mükemmel.",
        "description_en": "An atmospheric cafe where local artists and intellectuals meet, with artistic decor, vintage furniture, and comfortable environment. Perfect for a quiet break with specialty coffees, handmade desserts, and book corners."
    },
    "Pub Old Town": {
        "description": "Dünyanın dört bir yanından gelen gezginlerin buluşma noktası olan, canlı ve hareketli İrlanda tarzı pub. Canlı müzik geceleri, geniş bira seçkisi ve samimi atmosferiyle, Kotor'un en popüler gece mekanlarından biri.",
        "description_en": "A lively Irish-style pub serving as a meeting point for travelers from around the world. One of Kotor's most popular nightlife venues with live music nights, wide beer selection, and friendly atmosphere."
    },
    "Konoba Bonaca": {
        "description": "Lüks yatların yanaştığı marinanın yanında, şık ve modern sunumlarıyla öne çıkan deniz ürünleri restoranı. Taze balıklar, Adriyatik kabukluları ve yerel şaraplarla, körfez manzarası eşliğinde sofistike bir yemek deneyimi.",
        "description_en": "A seafood restaurant next to the marina where luxury yachts dock, standing out with stylish and modern presentations. A sophisticated dining experience with fresh fish, Adriatic shellfish, and local wines accompanied by bay views."
    },
    "Pirun & Ozica": {
        "description": "Hem İtalyan hem de Balkan mutfağından lezzetler sunan, Kotor'un popüler fusion restoranı. Pizza, makarna ve geleneksel Karadağ yemeklerinin bir arada bulunduğu geniş menüsüyle, her damak zevkine hitap ediyor.",
        "description_en": "Kotor's popular fusion restaurant offering flavors from both Italian and Balkan cuisines. Appeals to every taste with its extensive menu featuring pizza, pasta, and traditional Montenegrin dishes together."
    },
    "Citadela Restaurant": {
        "description": "Kotor'un tarihi surlarının üzerinde konumlanan, muhteşem körfez manzarası eşliğinde yemek yiyebileceğiniz romantik restoran. Geleneksel lezzetler, yerel şaraplar ve gün batımında büyüleyici atmosferiyle unutulmaz bir deneyim.",
        "description_en": "A romantic restaurant located on Kotor's historic walls where you can dine accompanied by magnificent bay views. An unforgettable experience with traditional flavors, local wines, and enchanting atmosphere at sunset."
    },
    "Pržun": {
        "description": "Eski hapishane binasının atmosferik avlusunda hizmet veren, tarihi dokuyu modern gastronomiye dönüştüren benzersiz restoran. Taş duvarlar, demir parmaklıklar ve yumuşak aydınlatmayla, hem yemek hem de ambiyans için dikkat çekici.",
        "description_en": "A unique restaurant serving in the atmospheric courtyard of an old prison building, transforming historic texture into modern gastronomy. Remarkable for both food and ambiance with stone walls, iron bars, and soft lighting."
    },
    "Konoba Boka Bay": {
        "description": "Prčanj sahilinde, gün batımını izlerken taze midye, istiridye ve deniz ürünlerinin tadını çıkarabileceğiniz rahat sahil restoranı. Dalga sesleri, deniz esintisi ve yerel lezzetlerle dolu huzurlu bir akşam yemeği.",
        "description_en": "A comfortable seaside restaurant on Prčanj shore where you can enjoy fresh mussels, oysters, and seafood while watching the sunset. A peaceful dinner full of wave sounds, sea breeze, and local flavors."
    },
    "Mademoiselle Dine & Wine Lounge": {
        "description": "Deniz kenarında, şık ve sofistike bir yemek deneyimi sunan, Fransız ilhamıyla donatılmış lounge restoran. Gurme tabaklar, özenle seçilmiş şaraplar ve zarif servis anlayışıyla, özel kutlamalar için mükemmel.",
        "description_en": "A French-inspired lounge restaurant by the sea offering a stylish and sophisticated dining experience. Perfect for special celebrations with gourmet dishes, carefully selected wines, and elegant service."
    },
    "Do Do": {
        "description": "Sıcak yaz günlerinde serinlemek için doğal malzemelerden yapılan ev yapımı dondurmaları sunan popüler dondurmacı. Mevsimlik meyveler, gerçek süt ve geleneksel tariflerle hazırlanan lezzetleriyle, her yaştan ziyaretçinin favorisi.",
        "description_en": "A popular ice cream shop serving homemade ice cream made from natural ingredients to cool off on hot summer days. A favorite of visitors of all ages with flavors prepared with seasonal fruits, real milk, and traditional recipes."
    },
    "Pescaria Dekaderon": {
        "description": "Sadece o gün tutulan taze balıkları pişiren, küçük ama itinayla işletilen kaliteli balık restoranı. Sade sunum, dürüst lezzetler ve balık tutkunlarının takdir edeceği özgün bir konseptle dikkat çekiyor.",
        "description_en": "A small but meticulously run quality fish restaurant cooking only freshly caught fish of the day. Stands out with simple presentation, honest flavors, and an original concept appreciated by fish enthusiasts."
    },
    "Ombra Caffe & Lounge Bar": {
        "description": "Silah Meydanı'nda oturup geleni geçeni izlemek ve şehrin nabzını tutmak için ideal konumdaki şık kafe ve bar. Kaliteli kahveler, serinletici içkiler ve geniş terasıyla, gün boyu keyifli zaman geçirme garantisi.",
        "description_en": "A stylish cafe and bar in an ideal location to sit in the Square of Arms, watch passers-by, and feel the city's pulse. Guaranteed pleasant time all day with quality coffees, refreshing drinks, and wide terrace."
    },
    "Konoba Marius": {
        "description": "Şehir surlarının hemen dışında, denize bakan geniş terasıyla öne çıkan geleneksel Karadağ restoranı. Izgara etler, taze deniz ürünleri ve yerel şaraplarla, turistik kalabalıktan biraz uzakta otantik bir deneyim.",
        "description_en": "A traditional Montenegrin restaurant just outside the city walls, standing out with its wide terrace overlooking the sea. An authentic experience slightly away from tourist crowds with grilled meats, fresh seafood, and local wines."
    },
    "Bokeski Gusti": {
        "description": "Prcanj'da deniz kenarında, dev porsiyonları ve samimi aile ortamıyla tanınan otantik restoran. Balıktan ete geniş menüsü, uygun fiyatları ve cömert servisiyle yerel halkın ve bütçe dostu gezginlerin favorisi.",
        "description_en": "An authentic restaurant in Prcanj by the sea, known for its huge portions and friendly family atmosphere. A favorite of locals and budget-friendly travelers with its wide menu from fish to meat, affordable prices, and generous service."
    },
    "Havana Club": {
        "description": "Küba temalı dekorasyonu, Latin müzikleri ve egzotik kokteylleriyle Kotor'un en hareketli gece kulüplerinden biri. Salsa geceleri, canlı DJ performansları ve tropikal atmosferiyle, dans etmek isteyenlerin adresi.",
        "description_en": "One of Kotor's liveliest nightclubs with Cuban-themed decor, Latin music, and exotic cocktails. The address for those wanting to dance with salsa nights, live DJ performances, and tropical atmosphere."
    },
    "La Catedral Pasta Bar": {
        "description": "Hızlı ve lezzetli taze makarna çeşitleri sunan, İtalyan usulü küçük pasta barı. El yapımı makarnalar, ev yapımı soslar ve uygun fiyatlarıyla, acıkan gezginlerin hızla doyabileceği pratik bir seçenek.",
        "description_en": "A small Italian-style pasta bar offering fast and delicious fresh pasta varieties. A practical option where hungry travelers can quickly satisfy their hunger with handmade pasta, homemade sauces, and affordable prices."
    },
    "Forza Terra": {
        "description": "Lüks 5 yıldızlı otelin bünyesindeki, üst düzey gastronomi deneyimi sunan fine-dining restoran. Şef'in özel menüleri, mükemmel şarap eşleştirmeleri ve kusursuz servisiyele, Kotor'un en prestijli yemek adreslerinden.",
        "description_en": "A fine-dining restaurant within a luxury 5-star hotel offering a high-end gastronomy experience. One of Kotor's most prestigious dining addresses with chef's special menus, perfect wine pairings, and flawless service."
    },
    "The Harbour Pub": {
        "description": "Limanın karşısında, spor maçlarını büyük ekranlarda izleyip soğuk bira içebileceğiniz rahat İngiliz tarzı pub. Canlı maç atmosferi, dart oyunları ve dostane ortamıyla, spor tutkunlarının buluşma noktası.",
        "description_en": "A comfortable British-style pub across from the harbor where you can watch sports matches on big screens and drink cold beer. A meeting point for sports enthusiasts with live match atmosphere, dart games, and friendly environment."
    },
    "Siempre": {
        "description": "Saat Kulesi'nin hemen altında, şehrin en merkezi noktasında konumlanan popüler kafe ve bar. Kahvaltıdan gece içkilerine kadar geniş servis saatleri ve meydan manzarasıyla, Kotor'un her anına tanıklık eden bir mekan.",
        "description_en": "A popular cafe and bar located at the city's most central spot, right below the Clock Tower. A venue witnessing every moment of Kotor with wide service hours from breakfast to night drinks and square views."
    },
    "Marshall's Gelato": {
        "description": "Yoğun kıvamlı, kremamsı İtalyan usulü dondurmaları ve sorbeleriyle tanınan butik dondurmacı. Günlük taze üretim, doğal malzemeler ve yaratıcı aromaları, sıcak havalarda serinlemek için mükemmel bir durak.",
        "description_en": "A boutique ice cream shop known for its dense, creamy Italian-style ice creams and sorbets. A perfect stop to cool off in hot weather with daily fresh production, natural ingredients, and creative flavors."
    },
    "Blue Cave (Plava Spilja)": {
        "description": "Suyun güneş ışığıyla fosforlu maviye dönüştüğü, yüzülebilen büyüleyici deniz mağarası. Tekne turlarıyla ulaşılan bu doğa harikası, Adriyatik'in en mistik ve fotoğrafik köşelerinden birini oluşturuyor.",
        "description_en": "An enchanting sea cave where water turns phosphorescent blue with sunlight, suitable for swimming. This natural wonder reached by boat tours creates one of the most mystical and photographic corners of the Adriatic."
    },
    "Bigova": {
        "description": "Kotor'un arka tarafında, modern gelişmeden uzak kalmış, sakinliğini koruyan küçük balıkçı köyü. Taş evler, ahşap tekneler ve taze balık restoranlarıyla, otantik Karadağ kıyı yaşamını deneyimlemek için ideal.",
        "description_en": "A small fishing village behind Kotor, away from modern development, preserving its tranquility. Ideal for experiencing authentic Montenegrin coastal life with stone houses, wooden boats, and fresh fish restaurants."
    },
    "Waikiki Beach Resort": {
        "description": "Tivat'ta modern tasarımlı plaj alanı, havuz ve restoranıyla tam donanımlı sahil kompleksi. Şezlonglar, su sporları imkanları ve DJ müziğiyle, aktif bir plaj günü geçirmek isteyenler için ideal.",
        "description_en": "A fully equipped beach complex in Tivat with modern-design beach area, pool, and restaurant. Ideal for those wanting an active beach day with sunbeds, water sports, and DJ music."
    },
    "Bjelila": {
        "description": "Taş evleri, dar sokakları ve berrak deniziyle 'Küçük Venedik' olarak anılan pitoresk sahil köyü. Turistik kalabalıklardan uzak, sakin bir yüzme ve güneşlenme deneyimi arayanların gizli hazinesi.",
        "description_en": "A picturesque coastal village called 'Little Venice' with its stone houses, narrow streets, and crystal-clear sea. A hidden treasure for those seeking a quiet swimming and sunbathing experience away from tourist crowds."
    },
    "Kotor Cable Car (Lovcen)": {
        "description": "Kotor'dan Lovcen dağının zirvesine sadece 11 dakikada ulaştıran, muhteşem körfez manzaralı modern teleferik hattı. Tırmanış zahmetinden kurtularak, panoramik kabinlerde nefes kesici manzaranın tadını çıkarın.",
        "description_en": "A modern cable car line from Kotor to the peak of Mount Lovćen in just 11 minutes, with magnificent bay views. Enjoy the breathtaking scenery in panoramic cabins without the effort of climbing."
    },
    "Restaurant Galija": {
        "description": "Tivat'a tepeden bakan konumuyla, özellikle et yemekleri ve ızgara lezzetleriyle ünlü panoramik restoran. Kuzu çevirme, biftek ve geleneksel Karadağ mezelerini, körfez manzarası eşliğinde deneyimleyin.",
        "description_en": "A panoramic restaurant overlooking Tivat from above, especially famous for its meat dishes and grilled flavors. Experience lamb on spit, steak, and traditional Montenegrin appetizers accompanied by bay views."
    },
    "Grispolis": {
        "description": "Bigova koyunda, aile işletmesi olarak çalışan, kendi tuttukları balıkları servis eden otantik balık restoranı. Denizden sofraya taze lezzetler, samimi ortam ve uygun fiyatlarla, yerel deneyimin özü.",
        "description_en": "An authentic fish restaurant in Bigova bay, run as a family business, serving fish they catch themselves. The essence of local experience with fresh flavors from sea to table, friendly atmosphere, and affordable prices."
    },
    "Vinarija Delić": {
        "description": "Tivat tepelerinde konumlanan, aile işletmesi sempatik bir şarap evi ve tadım odası. Yerel üzüm çeşitlerinden üretilen boutique şarapları, zeytin yağları ve peynirlerle birlikte keşfedin.",
        "description_en": "A sympathetic family-run winery and tasting room located in the Tivat hills. Discover boutique wines produced from local grape varieties along with olive oils and cheeses."
    },
    "Pontus Beach Club": {
        "description": "Lustica yarımadasında, daha sakin ve aile dostu atmosferiyle dikkat çeken şık plaj kulübü. Şezlonglar, güneşlenme platformları, kaliteli yemek servisi ve profesyonel personelle, rahat bir plaj günü garantisi.",
        "description_en": "A stylish beach club on the Lustica Peninsula notable for its calmer and family-friendly atmosphere. Guaranteed comfortable beach day with sunbeds, sunbathing platforms, quality food service, and professional staff."
    },
    "Krasici": {
        "description": "Tivat körfezinin karşı kıyısında, yazlık evlerin yoğunlaştığı sakin yerleşim bölgesi. Yerel halkın hafta sonu kaçamağı, küçük plajları ve sahil restoranlarıyla, turistik olmayan otantik bir köşe.",
        "description_en": "A quiet residential area on the opposite shore of Tivat bay where summer houses are concentrated. An authentic non-touristy corner with small beaches and coastal restaurants, a weekend getaway for locals."
    },
    "Velja Spila Beach": {
        "description": "Plavi Horizonti'nin yakınında, turistik radarın dışında kalmış, doğal güzelliğini koruyan gizli plaj. Berrak suları, doğal gölgelikleri ve sakin atmosferiyle, kalabalıktan kaçmak isteyenlerin sığınağı.",
        "description_en": "A hidden beach near Plavi Horizonti, off the tourist radar, preserving its natural beauty. A refuge for those wanting to escape crowds with its crystal-clear waters, natural shade, and peaceful atmosphere."
    },
    "Restaurant Prova": {
        "description": "Gemi burnunu andıran ilginç mimarisiyle dikkat çeken, deniz kenarında konumlanan tematik restoran. Balık ve deniz ürünleri ağırlıklı menüsü, denizcilik temalı dekorasyonu ve manzarasıyla benzersiz bir yemek deneyimi.",
        "description_en": "A themed restaurant by the sea notable for its interesting architecture resembling a ship's bow. A unique dining experience with its fish and seafood-focused menu, nautical-themed decor, and views."
    },
    "Nevjesta Jadrana Viewpoint": {
        "description": "'Adriyatik'in Gelini' olarak bilinen, Kotor Körfezi'nin en romantik ve ikonik manzara noktası. Tüm körfezi, adaları ve çevre dağları tek bir karede görebileceğiniz, fotoğrafçıların ve çiftlerin favorisi.",
        "description_en": "Known as 'Bride of the Adriatic', the most romantic and iconic viewpoint of the Bay of Kotor. A favorite of photographers and couples where you can see the entire bay, islands, and surrounding mountains in one frame."
    },
    "Vrmac Tunnel": {
        "description": "Kotor ile Tivat arasını 10 dakikaya indiren, dağın içinden geçen stratejik tünel. Körfezi dolaşmadan doğrudan geçiş imkanı sunan bu mühendislik eseri, bölge ulaşımının kilit noktası.",
        "description_en": "A strategic tunnel passing through the mountain, reducing the journey between Kotor and Tivat to 10 minutes. This engineering feat offering direct passage without going around the bay is a key point of regional transportation."
    },
    "Church of St. Domnius": {
        "description": "Vrmac dağı yürüyüş rotası üzerinde, körfez manzarasına bakan yalnız ve huzurlu küçük kilise. Yürüyüşçülerin mola verdiği bu nokta, doğa ve tarihin buluştuğu atmosferik bir sığınak.",
        "description_en": "A lonely and peaceful small church on the Vrmac mountain hiking trail overlooking bay views. An atmospheric refuge where nature and history meet, a resting point for hikers."
    },
    "Pestori": {
        "description": "Dobrota'nın yukarısında, yeşillikler içinde sakin ve otantik bir ortamda hizmet veren aile restoranı. Ev yapımı geleneksel yemekler, taze malzemeler ve samimi servisiye, turistik mekanlardan farklı bir deneyim.",
        "description_en": "A family restaurant serving above Dobrota in a quiet and authentic environment surrounded by greenery. A different experience from tourist venues with homemade traditional dishes, fresh ingredients, and friendly service."
    },
    "Beach Bar Pirate": {
        "description": "Perast'ın sonunda, kayalıkların üzerinde kurulu denize girip müzik dinleyebileceğiniz rahat plaj barı. Soğuk içkiler, deniz manzarası ve laid-back atmosferiyle, sıcak bir günü taçlandırmak için mükemmel.",
        "description_en": "A comfortable beach bar at the end of Perast built on rocks where you can swim and listen to music. Perfect for crowning a hot day with cold drinks, sea views, and laid-back atmosphere."
    },
    "Verige Beach": {
        "description": "Kotor Körfezi'nin en dar boğazının kıyısında, temiz suyu ve feribot manzarasıyla popüler çakıl plajı. Geçen feribotları izleyerek yüzebileceğiniz, aile dostu ve sakin bir sahil.",
        "description_en": "A popular pebble beach on the shore of the Bay of Kotor's narrowest strait, with clean water and ferry views. A family-friendly and quiet shore where you can swim while watching passing ferries."
    },
    "Mirista Beach": {
        "description": "Zanjice plajının yanında, zeytin ağaçlarının gölgesinde beton platformlar üzerinde güneşlenen, sıra dışı bir sahil deneyimi. Berrak suları, doğal ortamı ve restoranıyla, Lustica yarımadasının gizli cennetlerinden.",
        "description_en": "An extraordinary beach experience next to Zanjice beach, sunbathing on concrete platforms in the shade of olive trees. One of the hidden paradises of the Lustica Peninsula with crystal-clear waters, natural environment, and restaurant."
    },
    "Prevlaka Island": {
        "description": "Tivat havaalanının yanında, tarihi kilise kalıntıları ve pitoresk plajlarıyla küçük ada. Kayık veya yüzerek ulaşılabilen bu sakin köşe, tarih ve doğa meraklıları için keşfedilecek bir hazine.",
        "description_en": "A small island next to Tivat airport with historic church ruins and picturesque beaches. This quiet corner accessible by boat or swimming is a treasure to discover for history and nature enthusiasts."
    },
    "Sveti Andrije": {
        "description": "Perast'ın yukarısındaki tepede bulunan, körfez manzaralı eski kale kalıntıları ve şapel. Zorlu yürüyüşün ödülü olarak, tüm Kotor Körfezi'ni gören muhteşem bir panorama sunuyor.",
        "description_en": "Old fortress ruins and chapel on the hill above Perast with bay views. As a reward for the challenging hike, it offers a magnificent panorama overlooking the entire Bay of Kotor."
    },
    "Church of St. Peter": {
        "description": "Prcanj sahilinde, yerel halkın kullandığı küçük tarihi kilise. Mütevazı mimarisi ve deniz kenarı konumuyla, köyün dini ve sosyal yaşamının merkezlerinden biri olarak yüzyıllardır hizmet veriyor.",
        "description_en": "A small historic church on the Prcanj shore used by locals. Serving for centuries as one of the centers of the village's religious and social life with its modest architecture and seaside location."
    },
    "Kotor Farmers Market": {
        "description": "Eski şehrin surları dışında her sabah kurulan, taze sebze, meyve, peynir ve yerel ürünlerin satıldığı geleneksel pazar. Yerel halkın alışveriş yaptığı, Karadağ'ın tarım kültürünü deneyimleyebileceğiniz canlı bir mekan.",
        "description_en": "A traditional market set up every morning outside the old town walls selling fresh vegetables, fruits, cheese, and local products. A lively place where you can experience Montenegro's agricultural culture, where locals shop."
    },
    "Shopping Centre Kamelija": {
        "description": "Kotor'un tek modern alışveriş merkezi, süpermarket, kafeler ve çeşitli dükkanlarla donatılmış. Günlük ihtiyaçlar, hediyelik eşyalar ve klimalı ortamda mola vermek için pratik bir adres.",
        "description_en": "Kotor's only modern shopping center, equipped with supermarket, cafes, and various shops. A practical address for daily needs, souvenirs, and taking a break in air-conditioned environment."
    },
    "Park Slobode": {
        "description": "Limanın hemen yanında, banklarında oturup denizi ve geçen gemileri izleyebileceğiniz gölgeli şehir parkı. Yorucu şehir gezisinden sonra serinlemek, dinlenmek ve manzaranın tadını çıkarmak için ideal.",
        "description_en": "A shaded city park right next to the harbor where you can sit on benches and watch the sea and passing ships. Ideal for cooling off, resting, and enjoying the view after a tiring city tour."
    },
    "Kampana Tower Viewpoint": {
        "description": "Şehir surlarının kuzey ucundaki Kampana Kulesi'nin tepesinden, Skurda Nehri ve çevre dağlarını gören manzara noktası. Daha az bilinen bu rota, ana kale tırmanışına alternatif bir panorama deneyimi sunuyor.",
        "description_en": "A viewpoint from the top of Kampana Tower at the northern end of the city walls, overlooking the Skurda River and surrounding mountains. This lesser-known route offers an alternative panorama experience to the main fortress climb."
    },
    "Skurda River": {
        "description": "Kotor'un kuzeyinden geçerek denize dökülen kısa nehir ve arkasında yükselen dramatik kanyon. Şehrin doğal güzelliğinin bir parçası olarak, yürüyüş rotalarına başlangıç noktası ve fotoğraf için pitoresk bir köşe.",
        "description_en": "A short river flowing north of Kotor into the sea and the dramatic canyon rising behind it. As part of the city's natural beauty, a picturesque corner for photography and starting point for hiking routes."
    },
    "Muo Promenade": {
        "description": "Kotor'un karşısındaki Muo köyünün sahil boyunca uzanan huzurlu yürüyüş yolu. Palmiye ağaçları, küçük restoranlar ve körfez manzarasıyla, kalabalık şehir merkezinden uzaklaşarak nefes almak için mükemmel.",
        "description_en": "A peaceful promenade extending along the shore of Muo village across from Kotor. Perfect for getting away from the crowded city center and breathing with palm trees, small restaurants, and bay views."
    },
    "Kotor Art Cinema Boka": {
        "description": "Eski şehrin içinde, bağımsız ve sanat filmlerinin gösterildiği küçük sinema salonu. Alternatif film gösterimleri, kültürel etkinlikler ve samimi atmosferiyle, sinema severlerin gizli buluşma noktası.",
        "description_en": "A small cinema hall inside the old town showing independent and art films. A secret meeting point for cinema lovers with alternative film screenings, cultural events, and intimate atmosphere."
    },
    "Gallery Nobilis": {
        "description": "Yerel Karadağ sanatçılarının tablolarının ve el yapımı sanat eserlerinin sergilendiği ve satıldığı şık sanat galerisi. Özgün hediyelik eşya ve koleksiyon parçası arayanlar için ilham verici bir mekan.",
        "description_en": "An elegant art gallery where paintings and handmade artworks by local Montenegrin artists are exhibited and sold. An inspiring venue for those seeking original souvenirs and collectibles."
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

print(f"\n✅ Manually enriched {count} items (Kotor Batch 5 FINAL).")
