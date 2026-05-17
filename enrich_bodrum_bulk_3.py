from enrich_venues import enrich_venues

# BATCH: BODRUM SYSTEMATIC COMPLETION - PART 3

bodrum_bulk_3_updates = {
    "Bodrum Lokum bitez mağaza - K.Plus Gıda .A.Ş": {
        "desc_tr": "Bodrum'un geleneksel lezzetlerini modern bir sunumla birleştiren bu mağaza, özellikle taze meyvelerle hazırlanan Bodrum lokumlarıyla meşhurdur. Bitez'in mandalina kokulu sokaklarında, kentin en tatlı hediyeliklerini bulabileceğiniz bir duraktır.",
        "desc_en": "Blending tradition with modern flair, this shop is famous for its fresh Turkish delights made with local Bodrum fruits. Located in the mandarin-scented streets of Bitez, it’s the perfect spot to find the town’s sweetest souvenirs."
    },
    "Kaya Apart & Pansiyon Bodrum": {
        "desc_tr": "Bodrum'un merkezinde, beyaz badanalı dış cephesi ve begonvillerle süslü balkonlarıyla ev konforu sunan bir aile işletmesidir. Şehrin enerjisine bir adım mesafede ama kendi içinde sessiz ve samimi bir konaklama deneyimi arayanların adresidir.",
        "desc_en": "A family-run gem in central Bodrum, featuring whitewashed walls and bougainvillea-covered balconies. It offers a cozy, friendly stay just steps away from the city's buzz but with a peaceful, authentic atmosphere."
    },
    "Eylül cafe": {
        "desc_tr": "Bodrum Limanı'na nazır masalarıyla Eylül Cafe, sabahın ilk ışıklarından gece geç saatlere kadar kentin nabzını tutan samimi bir mekandır. Özellikle taze demlenmiş çayı ve liman manzaralı kahvaltılarıyla kentin bir klasiğidir.",
        "desc_en": "Overlooking the Bodrum harbor, Eylül Cafe is a warm spot that captures the town's pulse from morning till night. It's a local classic, famous for its freshly brewed tea and breakfasts with a view of the bobbing yachts."
    },
    "Adamik": {
        "desc_tr": "Bodrum Barlar Sokağı'nın en eski ve en karakterli mekanlarından biri olan Adamik, samimi bar kültürü ve nostaljik atmosferiyle bilinir. Yıllardır değişmeyen çizgisiyle kentin yerlilerinin ve müdavimlerinin vazgeçilmez buluşma noktasıdır.",
        "desc_en": "One of the oldest and most atmospheric bars on Bar Street, Adamik is known for its genuine bar culture and nostalgic vibe. With a consistent style over the decades, it remains a favorite meeting point for locals and regulars."
    },
    "Posh Club Bodrum": {
        "desc_tr": "Gümbet'in en popüler gece kulüplerinden biri olan Posh, yüksek enerjili müzikleri ve etkileyici ışık şovlarıyla tanınır. Yaz gecelerinde ünlü DJ performanslarına ev sahipliği yapan mekan, Bodrum gece hayatının en dinamik duraklarındandır.",
        "desc_en": "One of Gümbet's most popular nightspots, Posh is famous for its high-energy music and impressive light shows. Hosting top DJs throughout the summer, it stands as one of the most dynamic stages of the Bodrum nightlife scene."
    },
    "Vittoria Bodrum": {
        "desc_tr": "Bodrum merkezinde şık bir restoran ve kulüp deneyimini birleştiren Vittoria, kentin en elit eğlence adreslerinden biridir. İtalyan mutfağından seçkiler sunan akşam yemeği sonrası, sabahın ilk ışıklarına kadar süren kaliteli eğlencesiyle meşhurdur.",
        "desc_en": "Combining an upscale restaurant and club experience, Vittoria is one of central Bodrum's most elite venues. After a dinner of Italian specialties, it transforms into a high-end party spot that lasts until the early morning."
    },
    "THİSCO KARAOKE": {
        "desc_tr": "Bodrum gece hayatına renk katan Thisco, kentin en popüler ve eğlenceli karaoke barlarından biridir. Profesyonel ses sistemi ve geniş şarkı listesiyle, tatilinize unutulmaz ve kahkaha dolu anlar katmak için ideal bir mekandır.",
        "desc_en": "Adding a fun twist to Bodrum's nights, Thisco is one of the town's most popular karaoke bars. With a professional sound system and vast song library, it's the perfect place to add hilarious and memorable moments to your holiday."
    },
    "Catamaran Club Bodrum": {
        "desc_tr": "Denizin ortasında eğlence vaat eden kentin dünyaca ünlü 'yüzen diskosu' Catamaran, cam tabanı ve açık güvertesiyle benzersiz bir deneyim sunar. Bodrum Kalesi'ne karşı teknede dans etmek, kentin en ikonik gece hayatı ritüellerinden biridir.",
        "desc_en": "The world-famous 'floating disco' of Bodrum, Catamaran offers a unique party experience with its glass floor and open-air decks. Dancing on the waves against the backdrop of the castle is an iconic Bodrum nightlife ritual."
    },
    "PORTO Bodrum": {
        "desc_tr": "Milta Marina'nın girişinde yer alan Porto, lüks yat manzarası ve Akdeniz mutfağından seçkin lezzetleriyle bilinir. Şık tasarımı ve rafine servisiyle, kentin merkezinde prestijli bir akşam yemeği için en doğru adreslerden biridir.",
        "desc_en": "Located at the entrance of Milta Marina, Porto is known for its view of luxury yachts and a premium Mediterranean menu. With its chic design and refined service, it’s a top choice for a prestigious dinner in the city center."
    },
    "KAVALYE BAR": {
        "desc_tr": "Bodrum Kalesi'nin gölgesinde, tarihi bir taş binada yer alan Kavalye Bar, kentin en karakteristik ve nostaljik duraklarından biridir. Samimi atmosferi ve kentin sosyal tarihini yansıtan dokusuyla, bir Bodrum klasiği olarak bilinir.",
        "desc_en": "Nestled in a historic stone building in the shadow of Bodrum Castle, Kavalye Bar is one of the most characteristic and nostalgic spots in town. With its cozy vibe and rich social history, it stands as an enduring Bodrum classic."
    },
    "WI CLUB BODRUM": {
        "desc_tr": "Bodrum merkezinde modern bir gece kulübü deneyimi sunan WI Club, iddialı ses sistemleri ve özel etkinlikleriyle kentin yeni nesil eğlence yüzüdür. Şık tasarımı ve enerjik atmosferiyle, geceyi zirvede yaşamak isteyenlerin tercihidir.",
        "desc_en": "Offering a modern nightlife experience in central Bodrum, WI Club is the city's new-age entertainment face with its powerful sound systems and exclusive events. It’s the go-to for those looking to experience the night at its peak."
    },
    "Halikarnas Disco": {
        "desc_tr": "Bir dönem dünyanın en iyi gece kulüplerinden biri olarak kabul edilen Halikarnas, kentin eğlence tarihine damga vurmuş sembolik bir noktadır. Bugün kentsel bir hafıza merkezi olan bölge, Bodrum'un modern turizm hikayesinin başladığı yerdir.",
        "desc_en": "Once regarded as one of the best nightspots in the world, Halikarnas is a symbolic landmark that defined the town's party history. Today, it stands as a piece of urban memory where Bodrum's modern tourism story began."
    },
    "Osmanlı Tersanesi Sanat Galerisi": {
        "desc_tr": "Bodrum Marina'nın hemen yanındaki tarihi Osmanlı Tersanesi bünyesinde yer alan bu galeri, sanatı tarihin büyüleyici atmosferiyle buluşturur. Eski tersane kulesi ve korunan taş yapıları, kentin en etkileyici sergi alanlarını oluşturur.",
        "desc_en": "Located within the historic Ottoman Shipyard next to the Marina, this gallery merges contemporary art with a fascinating historical setting. The old shipyard tower and stone structures create one of the city's most impressive exhibit spaces."
    },
    "Halikarnas Balıkçısı Müzesi": {
        "desc_tr": "Bodrum'u dünyaya tanıtan Cevat Şakir Kabaağaçlı'ya (Halikarnas Balıkçısı) adanmış bu müze, yazarın kişisel eşyaları ve eserlerine ev sahipliği yapar. Kentin modern kimliğinin mimarı olan yazarın anısını yaşatan bu yer, kentin kültürel ruhudur.",
        "desc_en": "Dedicated to the man who put Bodrum on the map, Cevat Şakir Kabaağaçlı (The Fisherman of Halicarnassus), this museum houses his belongings and works. It honors the writer who built the town's modern identity."
    },
    "Akyarlar bodrum": {
        "desc_tr": "Bodrum Yarımadası'nın en güney ucunda yer alan Akyarlar, kristal netliğindeki denizi ve incecik kumuyla kentin en özel köşelerinden biridir. Eski bir Rum balıkçı köyü olan bölge, günümüzde huzuru ve sessizliğiyle Yarımada'nın saklı cevheridir.",
        "desc_en": "At the southernmost tip of the peninsula, Akyarlar is one of the most special corners with its crystal-clear water and fine sand. Once a Greek fishing village, it is now a hidden gem cherished for its peace and tranquility."
    },
    "Serçe Limanı Cam Batığı Sergisi": {
        "desc_tr": "Bodrum Kalesi içindeki Sualtı Müzesi'nde yer alan bu sergi, 11. yüzyıla ait bir gemiden çıkan 3 tonluk cam koleksiyonunu sergiler. Dünyanın en önemli sualtı arkeoloji buluntularından biri olan bu batık, tarihin şeffaf bir tanığı gibidir.",
        "desc_en": "Part of the Underwater Museum inside the castle, this exhibit features a 3-ton glass collection from an 11th-century shipwreck. It’s one of the world's most significant underwater finds, standing as a transparent witness to history."
    },
    "Karia Princess Museum": {
        "desc_tr": "Bodrum Kalesi içinde yer alan bu özel bölüm, Karya Prensesi Ada'ya ait mezar buluntularını ve kraliçenin gerçek boyutlu bir büstünü sergiler. Antik dönemin en güçlü kadınlarından birinin yaşantısına dair gizemli bir yolculuk sunar.",
        "desc_en": "Located within Bodrum Castle, this special section hosts the funerary finds of the Carian Princess Ada and a life-sized bust of the queen. It offers a mysterious journey into the life of one of antiquity's most powerful women."
    },
    "Bodrum Belediyesi Kent Müzesi": {
        "desc_tr": "Bodrum'un merkezindeki tarihi bir konakta yer alan Kent Müzesi, yarımadanın binlerce yıllık yaşam kültürünü, kıyafetlerini ve geleneklerini sergiler. Kentin bir süngerci kasabasından bugüne evrilen hikayesini en iyi anlatan duraktır.",
        "desc_en": "Housed in a historical mansion in central Bodrum, the City Museum exhibits the peninsula's life culture, traditions, and attire spanning millennia. It’s the best place to see how the town evolved from a sponge-diving village."
    },
    "Mars Tapınağı": {
        "desc_tr": "Bodrum'un kentsel dokusu arasına gizlenmiş olan bu tapınak kalıntıları, antik Halikarnassos'un askeri ve dini önemini yansıtır. Roma dönemine ait bu kalıntılar, kentin binlerce yıllık sokaklarında tarihin nasıl canlandığını gösteren nadir izlerdendir.",
        "desc_en": "Tucked away within Bodrum's modern streets, these temple ruins reflect the military and religious importance of ancient Halicarnassus. The Roman-era remains are rare echoes of the city's once-majestic skyline."
    },
    "cafer paşa türbesi": {
        "desc_tr": "Osmanlı Tersanesi'nin yakınındaki bu tarihi türbe, kentin Osmanlı dönemindeki stratejik denizcilik önemini simgeler. Sakin ve manevi atmosferiyle, Bodrum Kalesi'ne karşı tarihin sessiz tanıklarından biridir.",
        "desc_en": "Located near the old Ottoman Shipyard, this historic tomb symbolizes Bodrum's strategic maritime importance during the Ottoman era. With its spiritual atmosphere, it stands as a silent witness facing the castle."
    },
    "Art Halicarnassus": {
        "desc_tr": "Bodrum'un sanatsal ruhunu en iyi yansıtan galerilerden biri olan Art Halicarnassus, yerel ve uluslararası sanatçıların heykel ve tablolarına ev sahipliği yapar. Modern ve kentsel tasarımıyla kentin en özel sergi duraklarından biridir.",
        "desc_en": "One of the galleries best capturing Bodrum's creative soul, Art Halicarnassus hosts sculptures and paintings by local and global artists. Its modern and urban design makes it a premier stop for art lovers in town."
    },
    "Antik Mezarlar": {
        "desc_tr": "Bodrum sokaklarında yürürken bir okul bahçesinde veya yol kenarında karşınıza çıkabilen bu lahit mezarlar, antik kentin bugün hala yaşayan bir tarih olduğunu kanıtlar. Bu kaya mezarları, Halikarnassos'un ebedi sakinlerinin sessiz anıtlarıdır.",
        "desc_en": "Scattered throughout Bodrum—sometimes in schoolyards or by roadsides—these sarcophagus tombs prove the city is still a living history. These rock graves are silent monuments to the eternal inhabitants of ancient Halicarnassus."
    },
    "Gümbet Yeldeğirmenleri": {
        "desc_tr": "Bodrum ile Gümbet'i birbirinden ayıran tepe üzerindeki bu tarihi yeldeğirmenleri, kentin en ikonik silüetini oluşturur. 18. yüzyıldan kalan bu yapılar, özellikle gün batımında kenti kuşbakışı izleyebileceğiniz en popüler noktadır.",
        "desc_en": "Perched on the hill dividing Bodrum and Gümbet, these historic windmills form the city's most iconic silhouette. Dating back to the 18th century, they offer the most popular vantage point for a sunset bird's-eye view of the town."
    },
    "Kadir Akorak Atölyesi": {
        "desc_tr": "Bodrum'un en saygın sanatçılarından birinin atölyesi olan bu mekan, yaratıcılığın ve kentsel bohemin kalbidir. Sanatçının özgün dünyasını ve Bodrum'un ilham veren doğasını eserlerinde nasıl hayat bulduğunu burada görebilirsiniz.",
        "desc_en": "The atelier of one of Bodrum's most respected artists, this space is the heart of creativity and urban bohemianism. Here, you can witness how the artist's unique world and Bodrum's inspiring nature come to life in art."
    },
    "Simge Yachting": {
        "desc_tr": "Yalıkavak Marina merkezli Simge Yachting, kişiye özel mavi yolculuk tasarımlarıyla bilinen prestijli bir ekiptir. Ege'nin en lüks gulet ve yatlarını, en saklı koylarla buluşturan bir kapıdır.",
        "desc_en": "Based in Yalıkavak Marina, Simge Yachting is a prestigious team known for designing personalized Blue Cruises. It is a gateway linking the Aegean's most luxurious yachts with its most secluded, hidden bays."
    },
    "Tilkicik Residence": {
        "desc_tr": "Yalıkavak'ın en sakin ve huzurlu koylarından biri olan Tilkicik'te yer alan bu tesis, modern mimarisi ve denize sıfır konumuyla bilinir. Kentin lüks dokusunu, denizin dinginliğiyle birleştiren bir konaklama adresidir.",
        "desc_en": "Located in Tilkicik Bay, one of Yalıkavak's most serene and peaceful spots, this residence stands out with its modern architecture and seafront location. It blends city luxury with the tranquility of the sea."
    },
    "Çocuk Parkı": {
        "desc_tr": "Eskiçeşme bölgesinde, kaleye ve marina girişine bakan bu kentsel park, hem çocuklar için bir eğlence alanı hem de yetişkinler için kentin en güzel seyir noktalarından biridir. Kentin içinde nefes alan, ferah bir duraktır.",
        "desc_en": "Located in the Eskiçeşme district, this urban park overlooking the castle and marina is both a playground for kids and one of the best vantage points for adults. It’s a refreshing green break in the heart of town."
    },
    "Beach club": {
        "desc_tr": "Bodrum'un meşhur plaj kulübü kültürünü simgeleyen bu alan, turkuaz suların kıyısında modern bir eğlence ve konfor dünyası sunar. Şık iskeleleri, kaliteli müziği ve imza kokteylleriyle kentin tatil enerjisinin merkezidir.",
        "desc_en": "Representing Bodrum's famous beach club culture, this spot offers a world of modern entertainment and comfort by turquoise waters. With its chic piers, great music, and signature cocktails, it’s the hub of holiday energy."
    },
    "Oxso Bodrum": {
        "desc_tr": "Bodrum merkezinin en yeni ve modern kulüp tasarımlarından biri olan Oxso, yüksek enerjili atmosferi ve şık iç mimarisiyle dikkat çeker. Genç ve dinamik bir kitleye hitap eden mekan, kentin gece hayatına yeni bir soluk getirmiştir.",
        "desc_en": "One of central Bodrum's newest and most modern club designs, Oxso stands out with its high-energy atmosphere and chic interior. Catering to a young, dynamic crowd, it has brought a fresh breath to the city's nightlife."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Bodrum Bulk - Part 3)...")
enrich_venues("bodrum", bodrum_bulk_3_updates)
print("✨ Systematic Enrichment - Bodrum Bulk Part 3 Complete.")
