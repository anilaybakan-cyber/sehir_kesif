import json

# Manual enrichment data (Kotor Batch 3: 30 items)
updates = {
    "Napolyon Tiyatrosu": {
        "description": "Fransız işgali döneminden (1807-1813) kalma, Kotor'un dar sokaklarında gizlenmiş tarihi küçük tiyatro. Napolyon ordusunun askerleri için inşa edilmiş bu yapı, şehrin çok katmanlı tarihine ve Fransız etkisine tanıklık ediyor.",
        "description_en": "A historic small theater from the French occupation period (1807-1813), hidden in Kotor's narrow streets. This structure built for Napoleon's army soldiers witnesses the city's multi-layered history and French influence."
    },
    "Banja Monastery": {
        "description": "Risan'ın yakınında, Kotor Körfezi'nin sakin bir köşesinde konumlanan, 12. yüzyılda kurulan huzurlu Ortodoks manastırı. Deniz kıyısındaki konumu, tarihi freskleri ve manastır bahçesinin sessizliğiyle, meditasyon ve dini keşif için ideal bir sığınak.",
        "description_en": "A peaceful Orthodox monastery established in the 12th century, located in a quiet corner of the Bay of Kotor near Risan. An ideal refuge for meditation and religious discovery with its seaside location, historic frescoes, and monastery garden's silence."
    },
    "Citadela Herceg Novi": {
        "description": "1979 depreminde büyük hasar görerek kısmen denize doğru yıkılan, Herceg Novi'nin tarihi kale kalıntıları. Osmanlı ve Venedik dönemlerinin izlerini taşıyan bu atmosferik harabe, şehrin dramatik tarihine tanıklık eden etkileyici bir anıt.",
        "description_en": "Historic fortress ruins of Herceg Novi, partially collapsed towards the sea during the 1979 earthquake. An impressive monument witnessing the city's dramatic history, this atmospheric ruin bears traces of Ottoman and Venetian periods."
    },
    "City Museum Herceg Novi": {
        "description": "Mirko Komnenovic'in barok tarzındaki tarihi evinde kurulu, Herceg Novi'nin zengin tarihini sergileyen şehir müzesi. Osmanlı, Venedik ve Avusturya dönemlerinden kalma eserler, yerel gelenekler ve denizcilik tarihiyle ilgili kapsamlı bir koleksiyon.",
        "description_en": "A city museum exhibiting Herceg Novi's rich history, established in Mirko Komnenovic's historic baroque-style house. A comprehensive collection of artifacts from Ottoman, Venetian, and Austrian periods, local traditions, and maritime history."
    },
    "Skadar Lake National Park": {
        "description": "Balkanların en büyük gölü ve Avrupa'nın en önemli kuş cenneti olan Skadar Gölü, pelikanlardan balıkçılara, nilüfer tarlalarından antik manastırlara kadar benzersiz bir ekosistem sunuyor. Tekne turları, kuş gözlemi ve yerel şarap tatımı için eşsiz bir doğa harikası.",
        "description_en": "Lake Skadar, the largest lake in the Balkans and one of Europe's most important bird sanctuaries, offers a unique ecosystem from pelicans to fishermen, from water lily fields to ancient monasteries. A unique natural wonder for boat tours, bird watching, and local wine tasting."
    },
    "Rijeka Crnojevica Bridge": {
        "description": "Eski ticaret yolunda, Crnojevic Nehri üzerine kurulu, 15. yüzyıldan kalma pitoresk taş köprü. At nalı şeklindeki kemeriyle, Karadağ'ın en fotoğrafik yerlerinden biri olan bu tarihi yapı, gün batımında büyüleyici yansımalar oluşturuyor.",
        "description_en": "A picturesque stone bridge from the 15th century built over the Crnojevic River on the old trade route. One of Montenegro's most photogenic places with its horseshoe-shaped arch, this historic structure creates enchanting reflections at sunset."
    },
    "Besac Fortress": {
        "description": "Virpazar kasabasına hakim tepede konumlanan, Skadar Gölü'nün muhteşem manzarasını sunan Osmanlı dönemi kalesi. Surlarından gölün tamamını görebilir, kalenin içindeki restoranda yerel yemeklerin tadını çıkarabilirsiniz.",
        "description_en": "An Ottoman-era fortress located on a hill overlooking the town of Virpazar, offering magnificent views of Lake Skadar. You can see the entire lake from its walls and enjoy local dishes at the restaurant inside the fortress."
    },
    "Rezevici Monastery": {
        "description": "Budva ile Petrovac arasında, zeytinlikler ve kayalık sahil manzarasıyla çevrili 13. yüzyıldan kalma Ortodoks manastırı. Denize nazır konumu, antik freskleri ve huzurlu atmosferiyle, ruhani bir kaçış arayanlar için ideal bir durak.",
        "description_en": "A 13th-century Orthodox monastery between Budva and Petrovac, surrounded by olive groves and rocky coastal scenery. An ideal stop for those seeking spiritual escape with its seaside location, ancient frescoes, and peaceful atmosphere."
    },
    "King Nikola's Palace": {
        "description": "Karadağ'ın son kralı Kral Nikola I'in Bar'daki deniz kenarı sarayı, şimdi şehir müzesine ev sahipliği yapıyor. Krali mobilyalar, portreler, giysiler ve tarihi belgelerle, Karadağ krallık tarihine açılan bir pencere.",
        "description_en": "The seaside palace of King Nikola I, the last king of Montenegro, in Bar, now housing the city museum. A window into Montenegro's royal history with royal furniture, portraits, clothing, and historic documents."
    },
    "Murici Beach": {
        "description": "Skadar Gölü'nün en güzel tatlı su plajlarından biri, turkuaz renkli berrak suyuyla yüzmek ve güneşlenmek için ideal. Gölde tekne turuyla ulaşılan bu saklı cennet, doğanın koynunda huzurlu bir gün geçirmek isteyenler için mükemmel.",
        "description_en": "One of Lake Skadar's most beautiful freshwater beaches, ideal for swimming and sunbathing with its turquoise clear water. This hidden paradise reached by boat tour on the lake is perfect for those wanting to spend a peaceful day in nature's embrace."
    },
    "Godinje Village": {
        "description": "Evlerin birbirine yeraltı tünelleriyle bağlandığı, asırlık şarapçılık geleneğiyle ünlü otantik Karadağ köyü. Yerel ailelerin evlerinde ürettikleri şarapları tadabileceğiniz, zamanın durduğu masalsı bir atmosfer.",
        "description_en": "An authentic Montenegrin village famous for its centuries-old winemaking tradition, where houses are connected by underground tunnels. A fairytale atmosphere where time has stopped, where you can taste wines produced by local families in their homes."
    },
    "Buljarica Beach": {
        "description": "2 kilometre uzunluğunda, henüz büyük yapılaşmadan uzak, kampçıların ve doğa severların favorisi olan geniş kumsallı plaj. Dalga sesleri, yıldızlı geceler ve otantik sahil atmosferiyle, turist kalabalıklarından kaçış arayanlar için cennet.",
        "description_en": "A wide sandy beach 2 kilometers long, still far from major construction, a favorite of campers and nature lovers. Paradise for those seeking escape from tourist crowds with wave sounds, starry nights, and authentic coastal atmosphere."
    },
    "Kamenovo Beach": {
        "description": "Budva ile Becici arasında, turkuaz rengi berrak deniziyle ünlü, kayalıklarla çevrili pitoresk plaj. Şezlong ve restoran imkanlarıyla donatılmış bu kumsal, hem dinlenme hem de aktif su sporları için mükemmel bir denge sunuyor.",
        "description_en": "A picturesque beach between Budva and Becici, famous for its turquoise clear sea, surrounded by rocks. Equipped with sunbeds and restaurant facilities, this beach offers a perfect balance for both relaxation and active water sports."
    },
    "Ploce Beach": {
        "description": "Kayalıklar üzerine inşa edilmiş yüzme havuzları, güneşlenme platformları ve gece köpük partileriyle ünlü özgün plaj konsepti. Budva'nın gündüz dinlenme, akşam ise eğlence arayan genç ve enerjik kitlesinin buluşma noktası.",
        "description_en": "A unique beach concept famous for swimming pools built on rocks, sunbathing platforms, and night foam parties. A meeting point for Budva's young and energetic crowd seeking daytime relaxation and evening entertainment."
    },
    "Winery Kopitovic": {
        "description": "Kotor yakınlarında, tarihi bir mahzende otantik Karadağ şarap tadımı deneyimi sunan aile şaraphanesi. Vranac başta olmak üzere yerel üzüm çeşitlerinden üretilen şarapları, geleneksel mezeler ve sıcak aile misafirperverliğiyle keşfedin.",
        "description_en": "A family winery near Kotor offering an authentic Montenegrin wine tasting experience in a historic cellar. Discover wines produced from local grape varieties, especially Vranac, with traditional appetizers and warm family hospitality."
    },
    "Biskupija": {
        "description": "St. Tryphon Katedrali'nin yanında yer alan tarihi Piskoposluk binası, kilise yönetiminin merkezi ve dini hazinelere ev sahipliği yapan önemli bir yapı. Kotor'un Katolik mirasının merkezi olarak, mimari ve tarihi önemiyle dikkat çekiyor.",
        "description_en": "The historic Bishopric building located next to St. Tryphon Cathedral, the center of church administration and home to religious treasures. Standing out for its architectural and historical importance as the center of Kotor's Catholic heritage."
    },
    "Napoleon's Theatre": {
        "description": "Balkanlardaki ilk tiyatrolardan biri olarak Napolyon dönemi Fransız işgali sırasında inşa edilen tarihi yapı. Küçük ama etkileyici iç mekanıyla, şehrin kültür hayatına yaptığı tarihsel katkının simgesi.",
        "description_en": "A historic building constructed during the Napoleonic French occupation as one of the first theaters in the Balkans. A symbol of the historical contribution to the city's cultural life with its small but impressive interior."
    },
    "Piazza of Wood": {
        "description": "Kotor'un kuzey kapısının (River Gate) hemen yanında, asırlık ağaçların gölgelendirdiği ve kedilerin buluştuğu atmosferik küçük meydan. Turistik kalabalıktan uzak, yerel halkın tercih ettiği sakin bir nefes alma noktası.",
        "description_en": "An atmospheric small square right next to Kotor's north gate (River Gate), shaded by centuries-old trees and where cats gather. A quiet breathing point away from tourist crowds, preferred by locals."
    },
    "Piazza of Flour": {
        "description": "Tarihi Pima ve Buca saraylarının çevrelediği, bir zamanlar un ticaretinin yapıldığı küçük meydan. Kotor'un ticaret geçmişine tanıklık eden taş döşemeli bu alan, şimdi sakin kafelere ve manzara fotoğraflarına ev sahipliği yapıyor.",
        "description_en": "A small square surrounded by the historic Pima and Buca palaces, where flour trade once took place. This stone-paved area witnessing Kotor's commercial past now hosts quiet cafes and scenic photographs."
    },
    "Church of St. Joseph": {
        "description": "Eski bir manastır okulunun parçası olarak inşa edilmiş, genellikle ziyaretçilerin dikkatinden kaçan mütevazı kilise. Kotor'un dini yapılarının bir parçası olarak, sade mimarisi ve huzurlu atmosferiyle kısa bir ziyareti hak ediyor.",
        "description_en": "A modest church built as part of an old monastery school, usually overlooked by visitors. As part of Kotor's religious buildings, it deserves a short visit with its simple architecture and peaceful atmosphere."
    },
    "Lombardic Palace": {
        "description": "St. Luke Meydanı'na bakan, 17. yüzyıldan kalma zarif tarihi konak. Venedik döneminin tipik soylu mimarisini yansıtan cephesi ve dekoratif detaylarıyla, meydanın en fotoğrafik köşelerinden birini oluşturuyor.",
        "description_en": "An elegant historic mansion from the 17th century overlooking St. Luke Square. Creating one of the most photogenic corners of the square with its facade reflecting typical noble architecture of the Venetian period and decorative details."
    },
    "Vrakjen Palace": {
        "description": "Kotor'un soylu ailelerinden birine ait, dışarıdan sade görünümüne rağmen iç mekanındaki freskleriyle bilinen tarihi saray. Rönesans dönemi Kotor hayatına ışık tutan sanat eserleri barındırıyor.",
        "description_en": "A historic palace belonging to one of Kotor's noble families, known for its interior frescoes despite its simple exterior appearance. It houses artworks shedding light on Renaissance-era Kotor life."
    },
    "St. Paul's Church": {
        "description": "Eski bir kiliseden restore edilerek çok amaçlı kültür mekanına dönüştürülen yapı, şimdi sergilere, konserlere ve özel etkinliklere ev sahipliği yapıyor. Kotor'un modern kültür sahnesinin merkezi olarak atmosferik bir mekan.",
        "description_en": "A structure converted from an old church into a multi-purpose cultural venue through restoration, now hosting exhibitions, concerts, and private events. An atmospheric venue as the center of Kotor's modern culture scene."
    },
    "South Gate Bastion": {
        "description": "Kotor'un güney girişi olan Gurdic Kapısı'nı koruyan, şehir surlarının en güçlü savunma noktalarından biri. Buradan şehrin ortaçağ savunma sistemini anlayabilir ve körfez manzarasının tadını çıkarabilirsiniz.",
        "description_en": "One of the city walls' strongest defense points protecting Gurdic Gate, Kotor's southern entrance. From here you can understand the city's medieval defense system and enjoy bay views."
    },
    "Kotor City Walls Walk (North)": {
        "description": "Kampana Kulesi'nden başlayarak nehre doğru uzanan, sur duvarları üzerinde yapılan atmosferik yürüyüş parkuru. Şehrin batı tarafını ve dağ manzarasını izleyebileceğiniz bu rota, ana kale tırmanışına alternatif bir deneyim sunuyor.",
        "description_en": "An atmospheric walking trail on the city walls extending from Kampana Tower towards the river. This route where you can view the city's west side and mountain landscape offers an alternative experience to the main fortress climb."
    },
    "Church of St. Anne": {
        "description": "Kotor'un dar sokaklarının arasına gizlenmiş, 12. yüzyıla ait küçük ve samimi Romanın kilisesi. Sade taş mimarisi ve yüzyıllara meydan okuyan yapısıyla, şehrin en eski dini yapılarından biri olarak dikkat çekiyor.",
        "description_en": "A small and intimate Romanesque church from the 12th century hidden among Kotor's narrow streets. Standing out as one of the city's oldest religious buildings with its simple stone architecture and structure defying centuries."
    },
    "St. Francis Church Ruins": {
        "description": "Eski Fransisken manastırının kalıntıları, şehrin güney bölümünde açık hava arkeoloji alanı olarak korunuyor. Gotik kemerleri ve taş duvar kalıntılarıyla, Kotor'un orta çağ dini hayatına tanıklık eden atmosferik bir mekan.",
        "description_en": "The ruins of the old Franciscan monastery, preserved as an open-air archaeological site in the city's southern part. An atmospheric venue witnessing Kotor's medieval religious life with its Gothic arches and stone wall remains."
    },
    "Smekja Palace": {
        "description": "Perast'ın en büyük tarihi sarayı, şimdi lüks bir butik otel ve özel plaja sahip restoran olarak hizmet veriyor. Barok mimarisi, denize bakan bahçeleri ve aristokratik atmosferiyle, körfezin en prestijli konaklama adreslerinden biri.",
        "description_en": "Perast's largest historic palace, now serving as a luxury boutique hotel and restaurant with a private beach. One of the bay's most prestigious accommodation addresses with its baroque architecture, sea-facing gardens, and aristocratic atmosphere."
    },
    "St. Nikola Church": {
        "description": "Perast'ın ana meydanında yer alan ana kilise ve şehrin siluetini belirleyen 55 metrelik etkileyici çan kulesi. İç mekanındaki ikonalar, ahşap sunağı ve kuleden görülen körfez manzarasıyla, kasabanın dini ve kültürel merkezi.",
        "description_en": "The main church in Perast's main square and the impressive 55-meter bell tower defining the town's silhouette. The town's religious and cultural center with its interior icons, wooden altar, and bay views seen from the tower."
    },
    "Risan Mosaics (Roman Villa)": {
        "description": "Hipnos (Uyku Tanrısı) mozaiğiyle dünyaca ünlü, Kotor Körfezi'ndeki en önemli Roma dönemi arkeolojik alanı. M.S. 2-3. yüzyıldan kalma villa kalıntıları ve muhteşem zemin mozaikleriyle, antik tarihi canlı bir şekilde deneyimleyin.",
        "description_en": "Montenegro's most important Roman-era archaeological site in the Bay of Kotor, world-famous for its Hypnos (God of Sleep) mosaic. Experience ancient history vividly with villa ruins and magnificent floor mosaics from the 2nd-3rd century AD."
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

print(f"\n✅ Manually enriched {count} items (Kotor Batch 3).")
