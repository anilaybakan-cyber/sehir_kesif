import json

# Manual enrichment data (Batch 3: 20 items)
updates = {
    "Fonte dos Pisões": {
        "description": "Sintra dağlarının eteklerinde, yemyeşil ormanın içinde yer alan bu tarihi çeşme, yarı dairesel zarif yapısıyla dikkat çekiyor. Sürekli akan kristal berraklığındaki suyu, yüzyıllardır yolcuları serinleten bu nostaljik durağı, doğa yürüyüşlerinde mola vermek için ideal kılıyor.",
        "description_en": "Located in the lush forests at the foot of Sintra mountains, this historic fountain draws attention with its elegant semi-circular structure. Its crystal-clear water flowing continuously makes this nostalgic stop, which has refreshed travelers for centuries, ideal for a break during nature walks."
    },
    "Miradouro da Vigia": {
        "description": "Colares köyü yakınlarında konumlanan bu seyir noktası, Atlantik Okyanusu'nun engin mavisini ve dramatik falez manzaralarını sunuyor. Özellikle gün batımında, ufukta kaybolan güneşin okyanusa yansıyan turuncu ve mor tonlarını izlemek için Sintra bölgesinin en romantik köşelerinden biri.",
        "description_en": "Located near the village of Colares, this viewpoint offers the vast blue of the Atlantic Ocean and dramatic cliff views. Especially at sunset, it is one of the most romantic corners of the Sintra region to watch the orange and purple hues of the sun reflected on the ocean as it disappears on the horizon."
    },
    "Igreja de Santa Maria": {
        "description": "Sintra'nın tarihi merkezinde, gotik dönemin izlerini taşıyan etkileyici portaliyle dikkat çeken ana kilise. 14. yüzyıldan kalma bu yapı, iç mekanındaki aziz heykelleri, ahşap retablo ve barok sunakla ziyaretçilerini geçmişe bir yolculuğa çıkarıyor.",
        "description_en": "The main church in the historic center of Sintra, notable for its impressive portal bearing traces of the Gothic period. Dating from the 14th century, this structure takes visitors on a journey to the past with its saint statues, wooden retable, and baroque altar inside."
    },
    "Igreja de São Martinho": {
        "description": "12. yüzyıla dayanan köklü tarihiyle Sintra'nın en eski kiliselerinden biri olan bu mütevazı yapı, terasından Milli Saray'ın ikonik bacalarına bakan eşsiz bir manzara sunuyor. Romanın mimari kalıntılarını ve gotik dokunuşları bir arada barındırıyor.",
        "description_en": "One of Sintra's oldest churches with a rich history dating back to the 12th century, this humble structure offers a unique view of the iconic chimneys of the National Palace from its terrace. It houses Romanesque architectural remnants and Gothic touches together."
    },
    "Ferreira de Castro Museum": {
        "description": "Portekiz'in ünlü yazarı Ferreira de Castro'nun son yıllarını geçirdiği eve dönüştürülmüş bu müze, edebiyat severler için sakin ve ilham verici bir sığınak. Yazarın kişisel eşyaları, el yazmaları ve kütüphanesi, 20. yüzyıl Portekiz edebiyatına özgün bir bakış sunuyor.",
        "description_en": "Converted into the house where famous Portuguese writer Ferreira de Castro spent his last years, this museum is a quiet and inspiring refuge for literature lovers. The writer's personal belongings, manuscripts, and library offer a unique look at 20th century Portuguese literature."
    },
    "Camara Municipal de Sintra": {
        "description": "Sintra'nın ana meydanında görkemli bir şekilde yükselen Belediye Binası, Manueline ve romantik dönem mimarisinin muhteşem bir karışımını sergiliyor. Cephesindeki ince işçilikli taş oymalar ve zarif kemerleriyle, şehrin idari kalbinin attığı yer olmanın ötesinde görsel bir şölen sunuyor.",
        "description_en": "Rising majestically in Sintra's main square, the City Hall showcases a magnificent blend of Manueline and romantic period architecture. With its finely crafted stone carvings and elegant arches on its facade, it offers a visual feast beyond being the administrative heart of the city."
    },
    "Pelourinho de Sintra": {
        "description": "Kraliyet Sarayı'nın hemen önündeki meydanda, şehrin tarihine tanıklık eden gotik tarzda bir adalet sütunu (pelourinho). Orta Çağ'da kamu ilanlarının okunduğu ve mahkumların teşhir edildiği bu sütun, bugün Portekiz'in tarihi mirasının önemli bir parçası olarak korunuyor.",
        "description_en": "A Gothic-style justice pillar (pelourinho) in the square right in front of the Royal Palace, witnessing the city's history. This pillar, where public announcements were read and prisoners were displayed in the Middle Ages, is preserved today as an important part of Portugal's historical heritage."
    },
    "Adega Regional de Colares": {
        "description": "Dünyada benzeri görülmemiş, kumda yetiştirilen asmaların üzümlerinden üretilen efsanevi Colares şaraplarının tarihi üretim merkezi. 19. yüzyılda kurulan bu kooperatif şaraphane, filoksera salgınından kurtulan nadir asma çeşitlerinin korunduğu canlı bir şarap tarihi müzesidir.",
        "description_en": "The historic production center of legendary Colares wines produced from grapes of vines grown in sand, unique in the world. Established in the 19th century, this cooperative winery is a living wine history museum where rare vine varieties that survived the phylloxera outbreak are preserved."
    },
    "Aldeia da Mata Pequena": {
        "description": "Sintra dağlarının gizli bir köşesinde, zamanın durduğu masalsı bir taş köy. Tamamen restore edilerek eko-turizme açılan bu köy, geleneksel Portekiz kır yaşamını deneyimlemek, butik konaklama yapmak veya sessizlik içinde doğa yürüyüşü yapmak isteyenler için büyüleyici bir kaçış noktası.",
        "description_en": "A fairytale stone village where time has stopped, in a hidden corner of Sintra mountains. Completely restored and opened to eco-tourism, this village is a fascinating escape point for those wanting to experience traditional Portuguese rural life, boutique accommodation, or nature walks in silence."
    },
    "Penedo": {
        "description": "Sintra dağlarının yamaçlarına tünemiş, labirent gibi dar sokakları ve badanalı beyaz evleriyle büyüleyen otantik bir köy. Köyün tepesinden Atlantik Okyanusu'na uzanan muhteşem manzarası ve devasa granit kayalarının gölgesinde geçirilen huzurlu anlar, unutulmaz bir deneyim sunuyor.",
        "description_en": "An authentic village perched on the slopes of Sintra mountains, enchanting with its labyrinthine narrow streets and whitewashed houses. The magnificent view extending to the Atlantic Ocean from the top of the village and peaceful moments spent in the shadow of giant granite rocks offer an unforgettable experience."
    },
    "Praia da Adraga": {
        "description": "Yüksek kayalıkların arasında saklı, vahşi güzelliğiyle nefes kesen bir plaj. Altın renkli kumları, dramatik kaya oluşumları ve güçlü dalgalarıyla film setlerine bile ev sahipliği yapmış bu cennet, kalabalıktan uzakta doğanın ham güzelliğini arayanlar için mükemmel bir destinasyon.",
        "description_en": "A beach hidden among high cliffs, breathtaking with its wild beauty. With its golden sands, dramatic rock formations, and powerful waves, this paradise that has even hosted film sets is a perfect destination for those seeking the raw beauty of nature away from crowds."
    },
    "Praia da Aguda": {
        "description": "Dik ve nefes kesici merdivenleri inen cesur gezginleri ödüllendiren, neredeyse el değmemiş bir plaj. Turistik kalabalıklardan uzak bu vahşi kumsal, yalnızca doğa seslerini dinlemek ve okyanusun hırçın güzelliğiyle baş başa kalmak isteyenler için gizli bir hazine.",
        "description_en": "An almost untouched beach rewarding brave travelers who descend its steep and breathtaking stairs. This wild beach away from tourist crowds is a hidden treasure for those wanting only to listen to nature sounds and be alone with the wild beauty of the ocean."
    },
    "Farol do Cabo da Roca": {
        "description": "Avrupa kıtasının en batı noktasında, okyanusu gözetleyen ikonik deniz feneri. 18. yüzyılda inşa edilen ve hâlâ aktif olan bu fener, 'karanın bittiği ve denizin başladığı yer' sloganıyla ünlü Cabo da Roca burnunun tartışmasız sembolüdür.",
        "description_en": "An iconic lighthouse watching over the ocean at the westernmost point of the European continent. Built in the 18th century and still active, this lighthouse is the undisputed symbol of Cabo da Roca cape, famous for its slogan 'where the land ends and the sea begins'."
    },
    "Lagoa Azul": {
        "description": "Sintra ormanlarının derinliklerinde, çam ve okaliptüs ağaçlarıyla çevrili, adını yansıttığı mavimsi-yeşil tonlarından alan büyüleyici bir göl. Kuş cıvıltıları eşliğinde piknik yapmak, kitap okumak veya sadece meditasyon yapmak için şehrin gürültüsünden uzak huzurlu bir vaha.",
        "description_en": "A fascinating lake in the depths of Sintra forests, surrounded by pine and eucalyptus trees, named after the bluish-green tones it reflects. A peaceful oasis away from the city noise for picnicking, reading, or just meditating accompanied by birdsong."
    },
    "Rio da Mula": {
        "description": "Sintra bölgesinin yürüyüş rotalarının kesiştiği noktada, ormanla çevrili pitoresk bir baraj gölü. Serin sularında serinlemek (izin verilen dönemlerde), kano yapmak veya gölün etrafındaki patikalarda yürümek için yerel halkın ve doğa severlerin favori kaçış noktalarından biri.",
        "description_en": "A picturesque reservoir surrounded by forest at the intersection of hiking routes in the Sintra region. One of the favorite escape points of locals and nature lovers for cooling off in its cool waters (when permitted), canoeing, or walking on the trails around the lake."
    },
    "Convento dos Capuchos Walk": {
        "description": "Efsanevi Capuchos Manastırı'nı çevreleyen, yüzyıllık devasa ağaçların gölgesinde uzanan mistik orman yürüyüş parkuru. Yosun kaplı kayalar, doğal kaynaklar ve antik ağaçların oluşturduğu yeşil tünel, manevi bir atmosfer yaratarak ziyaretçileri büyüleyen bir deneyim sunuyor.",
        "description_en": "A mystical forest walking trail extending in the shadow of centuries-old giant trees surrounding the legendary Capuchos Monastery. The green tunnel created by moss-covered rocks, natural springs, and ancient trees creates a spiritual atmosphere, offering an enchanting experience for visitors."
    },
    "Ramalhão Palace": {
        "description": "Bir zamanlar Portekiz kraliyet ailesinin yazlık ikametgahı olarak kullanılan, bugün ise özel bir okula ev sahipliği yapan zarif neoklasik saray. Bakımlı bahçeleri ve görkemli cephesiyle, şehrin dışından bile göze çarpan aristokratik ihtişamını korumaya devam ediyor.",
        "description_en": "An elegant neoclassical palace once used as a summer residence of the Portuguese royal family, now housing a private school. With its well-maintained gardens and magnificent facade, it continues to preserve its aristocratic grandeur visible even from outside the city."
    },
    "Quinta da Vigia": {
        "description": "Sintra'nın karakteristik mimari tarzını yansıtan, romantik dönemden kalma tarihi bir malikane (quinta). Geniş arazisi, eski bahçeleri ve tipik Sintra evlerinin özelliklerini taşıyan ana binasıyla, bölgenin aristokratik geçmişine bir pencere açıyor.",
        "description_en": "A historic manor (quinta) from the romantic period reflecting Sintra's characteristic architectural style. With its large estate, old gardens, and main building bearing features of typical Sintra houses, it opens a window to the aristocratic past of the region."
    },
    "Old Town Steps": {
        "description": "Sintra'nın kalbinde, ana meydandan yukarı mahallelere kıvrılarak yükselen, çiçeklerle süslü pitoresk merdivenli sokaklar. Her köşede fotoğraf çekmeye değer manzaralar sunan bu taş basamaklar, şehrin romantik karakterinin en çok hissedildiği yerlerden biri.",
        "description_en": "Picturesque stepped streets rising winding from the main square to upper neighborhoods in the heart of Sintra, decorated with flowers. These stone steps offering views worth photographing at every corner are one of the places where the romantic character of the city is felt most."
    },
    "Jardim da Vigia": {
        "description": "Colares yakınlarında, turistik rotalardan uzakta saklı, küçük ama büyüleyici bir bahçe. Okyanus manzarasıyla birleşen yeşil alanları, sakin ortamı ve az keşfedilmiş doğasıyla, kalabalık mekanlardan kaçmak isteyenler için ideal bir sığınak sunuyor.",
        "description_en": "A small but charming garden hidden near Colares, away from tourist routes. With its green areas combined with ocean views, calm atmosphere, and unexplored nature, it offers an ideal refuge for those wanting to escape crowded places."
    }
}

filepath = 'assets/cities/sintra.json'
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

print(f"\n✅ Manually enriched {count} items (Batch 3).")
