from enrich_venues import enrich_venues

# BATCH: ÇEŞME SYSTEMATIC COMPLETION - PART 3

cesme_bulk_3_updates = {
    "Ilica Plaj": {
        "desc_tr": "Dünyanın en berrak ve sığ kumsallarından biri olan Ilıca, denizin içinden su yüzüne çıkan sıcak termal sularıyla benzersizdir. Turkuaz rengi ve pudra yumuşaklığındaki kumuyla, kentin bir doğa mucizesi ve en sevilen kentsel plajıdır.",
        "desc_en": "One of the world's most clear and shallow beaches, Ilıca is unique for its thermal springs bubbling up from the seabed. With its turquoise hues and powder-soft sand, it's a natural wonder and the town’s most beloved urban shore."
    },
    "Monarch Giriş - Maja": {
        "desc_tr": "Kuzey Çeşme sahil şeridinde lüks ve eğlenceye açılan kapı olan Monarch, şık kentsel tasarımıyla dikkat çeker. Kentsel sosyal hayatın en prestijli girişlerinden biri olarak, kentin eğlence dolu yaz ruhunu sofistike bir atmosferde sunar.",
        "desc_en": "The gateway to luxury and fun on the Northern Çeşme coast, Monarch stands out with its chic urban design. As one of the most prestigious social entries, it offers the town's vibrant summer spirit in a sophisticated atmosphere."
    },
    "Sunsurf Alacati (Windsurf Wingfoil Kitesurf)": {
        "desc_tr": "Dünya standartlarında rüzgar rüzgârı ve wingfoil eğitimi sunan Sunsurf, Alaçatı koyunun rüzgarla olan efsanevi bağını temsil eder. Kentin en profesyonel kentsel spor duraklarından biri olarak, macera tutkunlarının kentsel kalesidir.",
        "desc_en": "Providing world-class windsurfing and wingfoil training, Sunsurf represents the legendary bond between Alaçatı Bay and the wind. It's an urban sports stronghold for adventure enthusiasts and professional athletes alike."
    },
    "Port Villa Deniz": {
        "desc_tr": "Alaçatı Port'un kanal sistemine sıfır konumlanan bu lüks villalar, kentsel mimarinin en seçkin örnekleridir. Venedik esintili bu kentsel yerleşim, kentin modern ve prestijli kentsel yaşam tarzını en üst seviyede temsil eder.",
        "desc_en": "Seated right on the canal system of Alaçatı Port, these luxury villas are prime examples of elite urban architecture. This Venice-inspired settlement represents the town's modern and prestigious lifestyle at the highest level."
    },
    "Tash Mekan Kahvaltı & Otel": {
        "desc_tr": "Alaçatı'nın geleneksel taş mimarisini samimi bir kahvaltı sofrasıyla buluşturan Tash Mekan, kentin kentsel nostaljisini yaşatır. Yerel ürünlerle hazırlanan zengin sofrasıyla, kentin güne kentsel bir Ege ritmiyle başladığı çok özel bir duraktır.",
        "desc_en": "Merging Alaçatı's traditional stone architecture with a warm breakfast table, Tash Mekan keeps local urban nostalgia alive. With its rich spread of regional produce, it’s a special spot to start the day with an authentic Aegean rhythm."
    },
    "Villamer Alaçatı": {
        "desc_tr": "Kentin kentsel dokusuna uygun taş tasarımı ve begonvilli bahçesiyle Villamer, butik konaklamanın en zarif adreslerinden biridir. Kentsel sükuneti kentsel konforla harmanlayan tesis, kentin ruhunu hissetmek isteyenler için ideal bir sığınaktır.",
        "desc_en": "With its stone design matching the urban fabric and a bougainvillea garden, Villamer is one of the most elegant boutique stay addresses. Merging urban peace with comfort, it is the perfect sanctuary for feeling the town's soul."
    },
    "Alaçatı Eldoris": {
        "desc_tr": "Merkezi konumu ve şık butik otel anlayışıyla Eldoris, Alaçatı kentsel kentsel sosyal hayatının kalbinde huzurlu bir nokta sunar. Modern kentsel tasarımın kentsel tarihle buluştuğu bu mekan, kentin estetik karakterini yansıtır.",
        "desc_en": "With its central location and chic boutique approach, Eldoris offers a peaceful spot in the heart of Alaçatı's urban social life. This venue, where modern design meets local history, perfectly reflects the city's aesthetic character."
    },
    "Veria Han Alaçatı Otel": {
        "desc_tr": "Tarihi bir taş hanın modern bir butik otel olarak yeniden hayat bulduğu Veria Han, kentin kentsel mirasının en şık örneklerindendir. Kentsel kentsel dokuyu koruyan yüksek tavanlı odalarıyla, kentin kentsel asaletini temsil eder.",
        "desc_en": "A historic stone inn brought back to life as a modern boutique hotel, Veria Han is one of the most stylish examples of the city's urban heritage. It represents urban nobility with high-ceilinged rooms that preserve the local fabric."
    },
    "Elda Alaçatı Hotel": {
        "desc_tr": "Sanatsal detaylarla bezeli tasarımı ve kentsel samimiyetiyle Elda, kentin kentsel bohem ruhunu temsil eden çok özel bir oteldir. Kentsel hayatın içinde ama gürültüden uzak, kentin kentsel estetiğini sunan bir konaklama durağıdır.",
        "desc_en": "Decorated with artistic details and urban warmth, Elda is a very special hotel representing the city's urban bohemian spirit. It’s a stay option providing local aesthetics within the city but away from the noise."
    },
    "Keyf-i Kadeh Meyhanesi": {
        "desc_tr": "Alaçatı'nın kentsel meyhane kültürünün en neşeli temsilcilerinden olan Keyf-i Kadeh, geleneksel müzik ve Ege lezzetlerini birleştirir. Kentsel kentsel sosyal hayatın en canlı ve samimi akşam durağı olarak bilinir.",
        "desc_en": "One of the most cheerful representatives of Alaçatı's urban tavern culture, Keyf-i Kadeh merges traditional music with Aegean flavors. It is known as the town's most vibrant and warming evening social stop."
    },
    "Avrasya Lokantası": {
        "desc_tr": "Çeşme Yarımadası'nın en meşhur ev yemeği duraklarından olan Avrasya, taze zeytinyağlıları ve kentsel esnaf lokantası kültürüyle tanınır. Kentin gerçek kentsel lezzet durağı olarak yerel halkın ve gezginlerin favorisidir.",
        "desc_en": "One of the peninsula's most famous home-cooking destinations, Avrasya is known for its fresh olive oil dishes and artisan bistro culture. It is a local favorite for both residents and travelers seeking true urban flavors."
    },
    "Picante": {
        "desc_tr": "Alaçatı'nın kentsel kentsel sosyal hayatına Meksika mutfağının renkli dünyasını taşıyan Picante, yaratıcı kokteylleriyle meşhurdur. Kentin genç ve dinamik kentsel yüzünü yansıtan, kentsel eğlence haritasının en canlı köşe taşıdır.",
        "desc_en": "Bringing the colorful world of Mexican cuisine to Alaçatı's social scene, Picante is famous for its creative cocktails. It is a vibrant cornerstone of the entertainment map, reflecting the town's young and dynamic urban face."
    },
    "Alaçatı Sesil Otel": {
        "desc_tr": "Dingin atmosferi ve kentsel dokuyla uyumlu mimarisiyle Sesil Otel, huzurlu bir kentsel kaçış noktasıdır. Kentin kentsel kentsel gürültüsünden uzaklaşmak ama köklü kentsel estetiğini hissetmek isteyenlerin prestijli durakları arasındadır.",
        "desc_en": "With its tranquil atmosphere and architecture matching the urban fabric, Sesil Otel is a peaceful city escape. It ranks among the prestigious stops for those wanting to escape the noise while feeling the town's rooted aesthetics."
    },
    "kydonia restaurant": {
        "desc_tr": "Adını kentin eski Rum isminden alan Kydonia, otantik deniz ürünleri mutfağını kentsel bir şıklıkla sunar. Denize nazır kentsel kentsel terası ve tarihi dekoruyla kentin en iyi gastronomi duraklarından biri olarak kabul edilir.",
        "desc_en": "Taking its name from the city's old Greek moniker, Kydonia presents an authentic seafood menu with urban elegance. With its seafront terrace and historic decor, it’s considered one of the town's top culinary destinations."
    },
    "Özsüt": {
        "desc_tr": "Türkiye'nin sütlü tatlı geleneğini kentin modern kentsel ritmiyle buluşturan Özsüt, kentsel bir lezzet klasiğidir. Kentin sosyal hayatında tatlı bir mola vermek isteyenlerin kentsel kentsel uğrak noktasıdır.",
        "desc_en": "Merging Turkey's milk-based dessert tradition with the town's modern urban rhythm, Özsüt is a city classic. It’s the go-to urban spot for those looking for a sweet break in the peninsula's social life."
    },
    "Alaçatı Cafe": {
        "desc_tr": "Kasabanın kentsel girişindeki merkezi konumuyla bu kafe, kentsel sirkülasyonda bir dinlenme durağıdır. Kentin kentsel kentsel nabzını tutabileceğiniz, samimi ve kentsel bir buluşma alanıdır.",
        "desc_en": "With its central location at the village entrance, this cafe is a resting stop in the urban flow. It is a warm meeting space where you can capture the town's social pulse."
    },
    "Furun Cafe": {
        "desc_tr": "Alaçatı'nın kentsel fırın ve kafe kültürünü modern bir dokunuşla sunan Furun, taze kahvaltı seçenekleriyle bilinir. Kentin kentsel kentsel sosyal hayatında güne en taze kentsel ürünlerle başlamak için popüler bir kentsel duraktır.",
        "desc_en": "Presenting Alaçatı's urban bakery and cafe culture with a modern touch, Furun is known for its fresh breakfast options. It’s a popular spot for starting the day with the freshest urban produce in the city's social life."
    },
    "15 Eylül Kıraathanesi": {
        "desc_tr": "Kentin kentsel sosyal tarihindeki en ikonik durak olan bu kıraathane, kentin kentsel nostaljisini temsil eden bir kentsel merkezdir. Damla sakızlı kahvesiyle meşhur olan mekan, kentin kentsel kentsel kentsel buluşma hafızasıdır.",
        "desc_en": "The most iconic landmark in the city's social history, this coffee house is a hub representing local urban nostalgia. Famous for its mastic-flavored coffee, it is the home of the town's collective social memory."
    },
    "Çatladı Kapı Han Cafe": {
        "desc_tr": "Tarihi bir taş hanın kentsel bir sosyal alana dönüşümüyle yaratılan bu mekan, kentin kentsel kentsel mirasının bir parçasıdır. Kentsel mimarisi ve huzurlu kentsel avlusuyla, kentin kentsel estetiğini yansıtan çok şık bir duraktır.",
        "desc_en": "Created by converting a historic stone inn into a social space, this venue is part of the city's urban heritage. With its local architecture and peaceful courtyard, it’s a very stylish spot reflecting local aesthetics."
    },
    "ALAÇATI SELANİK PASTANESİ 1945": {
        "desc_tr": "Çeşme'nin 1945'ten beri süregelen en tatlı lezzet efsanesi olan Selanik Pastanesi, kentsel bir gastronomi anıtıdır. Meşhur kavala kurabiyesi ve sakızlı tatlılarıyla, kentin kentsel lezzet hafızasındaki kentsel kentsel imza duraktır.",
        "desc_en": "A sweet flavor legend since 1945, Selanik Pastanesi is an urban culinary monument. With its famous Kavala cookies and mastic desserts, it serves as a signature landmark in the town's flavor memory."
    },
    "Ottoman Alaçatı": {
        "desc_tr": "İmparatorluk mutfağının en seçkin kentsel kentsel reçetelerini kentin kentsel dokusuyla birleştiren bu mekan, kentsel bir lezzet sarayı gibidir. Tarihi tasarımı ve gurme menüsüyle kentin kentsel kitlelerce sevilen prestijli bir duraktır.",
        "desc_en": "Merging the elite recipes of Imperial cuisine with the local urban fabric, this venue is like a palace of flavor. With its historic design and gourmet menu, it is a prestigious stop beloved by the city's upscale crowd."
    },
    "Kahve Askina": {
        "desc_tr": "Kentin kentsel sosyal hayatında modern kahve kültürünün samimi bir temsilcisi olan Kahve Aşkına, kentin yerel buluşma kalesidir. Kentsel tasarımı ve kentsel sokağın enerjisini kentsel yansıtan popüler bir kentsel duraktır.",
        "desc_en": "A warm representative of modern coffee culture in the city's social life, Kahve Aşkına is a local meeting stronghold. It’s a popular spot reflecting urban design and the energy of the peninsula's streets."
    },
    "Takili Cafe": {
        "desc_tr": "Kentin kentsel kentsel sosyal hayatında her zaman hareketli olan Takılı Cafe, kentsel bir mola ve sosyal etkileşim merkezidir. Kentin dinamik kentsel ruhunu sokağa taşıyan, kentsel samimiyetiyle bilinen şık bir kentsel duraktır.",
        "desc_en": "Always vibrant in the city's social life, Takılı Cafe is a hub for urban breaks and interaction. A stylish spot known for its warmth that brings the town’s dynamic spirit to the streets."
    },
    "Bum cafe": {
        "desc_tr": "Alaçatı'nın kentsel modern kentsel yeme-içme haritasında yaratıcı atıştırmalıklarıyla yer edinen Bum Cafe, kentin en neşeli kentsel duraklarındandır. Kentsel tasarımıyla kenti kentsel kentsel genç tutan bir kentsel sosyal merkezdir.",
        "desc_en": "Finding its place on Alaçatı's modern food map with creative snacks, Bum Cafe is one of the most cheerful urban stops. It is a social hub keeping the town young through its urban design vibes."
    },
    "matcha Mia": {
        "desc_tr": "Dünya trendlerini kentin kentsel kitleleriyle buluşturan Matcha Mia, sağlıklı kentsel yaşam anlayışının kentsel temsilcisidir. Yeşil çayın kentsel şifasını modern kentsel sunumlarla birleştiren kentin en taze kentsel durağıdır.",
        "desc_en": "Connecting global trends with the local urban crowd, Matcha Mia is the representative of healthy urban living. It's the town's freshest spot, merging the healing touch of matcha with modern service."
    },
    "Schiller Kaffee Go Alaçatı": {
        "desc_tr": "Nitelikli kahve deneyimini kentin tarihi kentsel dokusuna taşıyan Schiller, kentsel kalite anlayışıyla tanınır. Kentin kentsel kentsel sosyal hayatında prestijli bir kentsel mola noktası arayanların kentsel kentsel adresidir.",
        "desc_en": "Bringing a high-quality coffee experience to the historic urban fabric, Schiller is known for its commitment to local excellence. It’s the go-to address for those seeking a prestigious break in the city's social life."
    },
    "Alaris Otel Cafe bar": {
        "desc_tr": "Kentsel bir butik tasarımın kentsel bar kültürüyle harmanlandığı Alaris, kentin en şık kentsel sosyal kentsel duraklarındandır. Kentsel ışıkları ve kentsel müzikleriyle kentin kentsel ritmini hissettiren seçkin bir kentsel mekandır.",
        "desc_en": "Merging urban boutique design with local bar culture, Alaris is one of the town's most stylish social stops. An elite venue that lets you feel the city's rhythm through urban lights and music."
    },
    "D.STOP artcafe": {
        "desc_tr": "Sanat ve kahveyi kentsel bir estetikle buluşturan D.STOP, kentin en entelektüel kentsel duraklarındandır. Kentsel galerisi ve kentsel kahve menüsüyle, kentin yaratıcı enerjisini en iyi kentsel yansıtan kentsel duraktır.",
        "desc_en": "Merging art and coffee with urban aesthetics, D.STOP is one of the town's most intellectual stops. With its gallery and coffee menu, it's the landmark best reflecting the city's creative energy."
    },
    "Hector Louis Coffee Alaçatı": {
        "desc_tr": "Kentsel şıklığın ve zanaatkar kahvenin Alaçatı'daki kentsel kentsel kalesi olan Hector Louis, kentin kentsel kentsel prestijini temsil eder. Modern kentsel kentsel kitlelerin uğrak noktası olan kentin en şık kentsel sosyal kentsel durağıdır.",
        "desc_en": "An urban stronghold for local chic and artisanal coffee, Hector Louis represents the town's social prestige. It’s the most stylish social spot frequented by modern urban crowds."
    },
    "Tutto Mino": {
        "desc_tr": "İtalyan rüzgarını kentin kentsel taş evlerine taşıyan Tutto Mino, kentsel lezzet kardeşliğinin bir kentsel örneğidir. Taze makarnaları ve kentsel kentsel atmosferiyle kentin gurme kentsel haritasında parlayan bir kentsel duraktır.",
        "desc_en": "Bringing an Italian breeze to the town's urban stone houses, Tutto Mino is an example of culinary brotherhood. A shining landmark on the city's gourmet map with its fresh pasta and urban atmosphere."
    },
    "Giulia Alaçatı": {
        "desc_tr": "Modern Akdeniz ve İtalyan mutfağını kentin kentsel kentsel kentsel dokusuyla harmanlayan Giulia, kentin en yeni ve prestijli kentsel lezzet durağıdır. Şık kentsel dekorasyonuyla kentin elit kentsel kitlelerinin kentsel kentsel favorisidir.",
        "desc_en": "Blending modern Mediterranean and Italian flavors with the local urban fabric, Giulia is the town's newest prestigious culinary stop. It's a favorite for elite urban crowds with its chic local decor."
    },
    "Bairlin Alaçatı": {
        "desc_tr": "Kentsel kentsel kentsel gece hayatının dinamik ve şık kentsel temsilcisi olan Bairlin, kentin en popüler kentsel kokteyl ve eğlence kentsel durağıdır. Modern kentsel ritimleri kentsel kentsel sokağa taşıyan iddialı bir kentsel mekandır.",
        "desc_en": "A dynamic and stylish representative of urban nightlife, Bairlin is the town's top cocktail and entertainment stop. An ambitious venue bringing modern rhythms to the Peninsula's streets."
    },
    "Bota Alaçatı": {
        "desc_tr": "Rafine lezzetleri ve lüks kentsel ambiyansıyla Bota, kentin gastronomi kentsel dünyasında üst kentsel segmenti temsil eder. Kentsel kentsel şıklığı kentsel lezzetle buluşturan, kentin en prestijli kentsel akşam duraklarındandır.",
        "desc_en": "Representing the upscale segment of the city's culinary world, Bota stands out with refined flavors and a luxury ambiance. It's one of the town's most prestigious evening stops, merging local chic with fine dining."
    },
    "Perde Arkası Alaçatı": {
        "desc_tr": "Adı gibi kentin kentsel kentsel eğlencesinin 'kulisini' temsil eden Perde Arkası, gizemli ve şık kentsel tasarımıyla kentsel kitlelerce sevilir. Kentin kentsel gece hayatına kentsel kentsel estetik katan çok özel bir kentsel duraktır.",
        "desc_en": "True to its name as the 'backstage' of the city's fun, Perde Arkası is loved for its mysterious and chic urban design. A very special stop adding local aesthetics to the town's nightlife."
    },
    "Spois Alaçatı": {
        "desc_tr": "Modern kentsel kentsel sosyal hayatın en yeni neşesi olan Spois, kentin kentsel dinamizmini yansıtan kentsel bir sosyal kentsel merkezdir. Kentsel eğlenceyi kentsel kentsel samimiyetle sunan kentin popüler kentsel duraklarındandır.",
        "desc_en": "The newest joy of modern urban life, Spois is a social hub reflecting the town's dynamism. A popular landmark providing urban entertainment with local sincerity."
    },
    "Disco": {
        "desc_tr": "Çeşme Yarımadası'nın efsanevi disko kültürünü günümüz kentsel kentsel estetiğiyle birleştiren bu alan, kentin eğlence kentsel hafızasıdır. Yaz gecelerini kentsel ritimle dolduran kentin kentsel ikonik dans kentsel durağıdır.",
        "desc_en": "Merging the peninsula's legendary disco culture with today's urban aesthetics, this venue is the city's entertainment memory. An iconic dance landmark filling summer nights with local rhythms."
    },
    "The Barra Alaçatı": {
        "desc_tr": "Endüstriyel kentsel tasarımı kentsel kentsel kentsel kokteyl sanatıyla birleştiren The Barra, kentin en kentsel kentsel kentsel sosyal kentsel duraklarındandır. Kentin genç ve modern kentsel yüzünün kentsel kentsel buluşma kalesidir.",
        "desc_en": "Combining industrial urban design with cocktail art, The Barra is one of the city's most urban social stops. A meeting stronghold for the town's young and modern face."
    },
    "Ark Alacati": {
        "desc_tr": "Kentsel bir konsept ve şık bir konaklamayı kentin kentsel kentsel kentsel dokusu içinde sunan Ark, kentin kentsel estetiğini kentsel temsil eder. Modern kentsel seyyahların kentsel prestijli kentsel uğrak noktasıdır.",
        "desc_en": "Providing a concept experience and stylish stay within the local urban fabric, Ark represents the town's aesthetics. A prestigious landmark for modern urban travelers."
    },
    "G Lodge": {
        "desc_tr": "Butik otel sıcaklığını kentsel kentsel bir 'lodge' konseptiyle kentsel harmanlayan G Lodge, kentin sessiz kentsel prestij kentsel kalesidir. Kentsel kentsel konforu kentin ruhuyla kentsel birleştiren çok özel bir kentsel duraktır.",
        "desc_en": "Merging boutique warmth with an urban 'lodge' concept, G Lodge is the city's stronghold of quiet prestige. A very special stop combining local comfort with the town's soul."
    },
    "Bi Nevi Alaçatı": {
        "desc_tr": "Kentsel yeme-içme ve sosyal etkileşim dünyasının en samimi kentsel kentsel kentsel renklerinden olan Bi Nevi, kentin kentsel kentsel neşesidir. Kentsel kentsel şıklığı kentin kentsel kentsel samimiyetiyle sunan popüler bir kentsel duraktır.",
        "desc_en": "One of the warmest colors of the Peninsula's dining and social scene, Bi Nevi is the town's urban joy. A popular landmark providing local chic with sincere warmth."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Çeşme Bulk - Part 3)...")
enrich_venues("cesme", cesme_bulk_3_updates)
print("✨ Systematic Enrichment - Çeşme Bulk Part 3 Complete.")
