from enrich_venues import enrich_venues

# BATCH: ÇEŞME SYSTEMATIC COMPLETION - PART 1

cesme_bulk_1_updates = {
    "Çeşme, Ilıca Yıldızburnu küçük halk plajı.": {
        "desc_tr": "Ilıca'nın Yıldızburnu bölgesinde yer alan bu küçük halk plajı, denizin içinden kaynayan sıcak termal sularıyla ünlüdür. Kışın bile denize girilebilen bu özel nokta, kentin doğal bir şifalı havuzu gibidir.",
        "desc_en": "Located in the Yıldızburnu area of Ilıca, this small public beach is famous for its thermal springs bubbling up from the seabed. A natural healing pool where you can swim even in winter, it's a unique coastal gem."
    },
    "Ayayorgi Yolu": {
        "desc_tr": "Çeşme'nin dünyaca ünlü beach club'larına ev sahipliği yapan Ayayorgi Koyu'na inen bu yol, adrenalin ve eğlencenin başlangıcıdır. Turkuaz sulara ve gece hayatına açılan bu rota, kentin en enerjik sokağıdır.",
        "desc_en": "Leading down to the world-famous Ayayorgi Bay and its legendary beach clubs, this road marks the start of excitement and fun. It is the town's most energetic route, opening up to turquoise waters and vibrant nightlife."
    },
    "Dalyan Plaj": {
        "desc_tr": "Sakin denizi ve balıkçı kasabası atmosferiyle bilinen Dalyan Plajı, Çeşme'nin huzur arayanlar için en doğru adresidir. Yerel balıkçı tekneleri eşliğinde, kentin en samimi ve doğal deniz keyfini sunar.",
        "desc_en": "Known for its calm waters and fishing village atmosphere, Dalyan Beach is the perfect choice for those seeking peace in Çeşme. Surrounded by local boats, it offers the town's most authentic and natural seaside joy."
    },
    "paşalimanı": {
        "desc_tr": "Çeşme'nin en nezih ve sakin koylarından biri olan Paşalimanı, turkuazın en açık tonlarına sahip deniziyle büyüleyicidir. Lüks villaların ve huzurlu plajların buluştuğu bu bölge, kentin seçkin bir dinlenme köşesidir.",
        "desc_en": "One of Çeşme's most refined and tranquil bays, Paşalimanı is mesmerizing with its lightest shades of turquoise. A blend of luxury villas and peaceful shores, it serves as an elite relaxation corner in town."
    },
    "Germiyan": {
        "desc_tr": "Türkiye'nin ilk CittaSlow (Sakin Şehir) köyü olan Germiyan, evlerin duvarlarını süsleyen el yapımı çiçek resimleriyle meşhurdur. Geleneksel ekmeği ve sanatla iç içe geçmiş köy sokaklarıyla, kentin en otantik kültürel durağıdır.",
        "desc_en": "Turkey's first CittaSlow village, Germiyan is famous for the hand-painted flower murals adorning its houses. With its traditional sourdough bread and artistic streets, it is the town's most authentic cultural stop."
    },
    "Erythrai Tiyatrosu": {
        "desc_tr": "Ildırı köyünde yer alan Antik Erythrai kentinin en önemli kalıntısı olan bu tiyatro, denize hakim konumuyla büyüleyicidir. Likya ve İyonya tarihini hissedebileceğiniz bu alan, kentin binlerce yıllık geçmişine açılan bir penceredir.",
        "desc_en": "The most significant remnant of the Ancient city of Erythrai in Ildırı, this theater is stunning for its command over the sea. A place to feel Ionian history, it serves as a window into the peninsula's millennia-old past."
    },
    "Kleopatra Koyu": {
        "desc_tr": "Adını kristal netliğindeki suyundan ve altın sarısı kumundan alan bu saklı koy, doğanın şekillendirdiği devasa kayalıklarla korunur. Kalabalıklardan uzak, bakir bir doğada deniz keyfi yapmak isteyenlerin kentsel gizli limanıdır.",
        "desc_en": "Named after its crystal-clear water and golden sand, this hidden bay is protected by massive natural rock formations. It's a secret urban harbor for those looking to enjoy a pristine sea day away from the city crowds."
    },
    "Fly-Inn Beach": {
        "desc_tr": "Çeşme'nin Altınkum bölgesinde yer alan Fly-Inn, kaliteli müzik ve modern plaj konseptini kentin en berrak sularıyla birleştirir. Geniş güneşlenme alanları ve iddialı mutfağıyla, kentin en köklü beach club deneyimlerinden birini sunar.",
        "desc_en": "Located in the Altınkum area, Fly-Inn merges premium music and a modern beach concept with the town's clearest waters. With vast sun decks and an ambitious kitchen, it offers one of the most established beach club experiences."
    },
    "OM Paparazzi": {
        "desc_tr": "Ayayorgi Koyu'nun ilk ve en klasik beach club'ı olan Paparazzi, onlarca yıldır kalitesinden ödün vermeyen bir kentsel simgedir. Nezih atmosferi ve gurme restoranıyla, kentin eğlence tarihindeki en prestijli duraktır.",
        "desc_en": "The first and most classic beach club in Ayayorgi Bay, Paparazzi is an urban icon that hasn't compromised on quality for decades. With its refined vibe and gourmet dining, it’s a prestigious landmark in the town's party history."
    },
    "Sole & Mare Beach Club": {
        "desc_tr": "Ayayorgi'nin en enerjik ve popüler noktalarından biri olan Sole & Mare, gündüz güneşin gece ise müziğin kalbidir. Turkuaz denize kurulu locaları ve ünlü 'happy hour' partileriyle, kentin eğlence dolu yaz ruhunu mükemmel yansıtır.",
        "desc_en": "One of Ayayorgi's most energetic spots, Sole & Mare is the heart of sun by day and music by night. With its piers over turquoise water and famous happy hours, it perfectly captures the town's vibrant summer spirit."
    },
    "Derya Beach Restaurant": {
        "desc_tr": "Denize sıfır konumu ve taze Ege lezzetleriyle tanınan Derya Beach, samimi bir aile işletmesi sıcaklığı sunar. Hem plaj keyfi hem de denizin hemen yanında taze balık yemek isteyenler için kentin en doğal lezzet duraklarındandır.",
        "desc_en": "Famous for its seafront location and fresh Aegean flavors, Derya Beach offers the warmth of a family-run gem. It's a natural flavor stop for those wanting to swim and then savor fresh fish right by the waves."
    },
    "Zio Beach Club": {
        "desc_tr": "Alaçatı'nın lüks ve konforu birleştiren sahil şeridinde yer alan Zio, şık tasarımı ve seçkin atmosferiyle bilinir. Gastronomi ile eğlenceyi harmanlayan mekan, kentin kentsel sosyal hayatında sofistike bir plaj günü vaat eder.",
        "desc_en": "Located on Alaçatı's upscale shoreline, Zio is known for its chic design and elite atmosphere. Blending gastronomy with entertainment, it promises a sophisticated beach day in the town's urban social scene."
    },
    "Marin Alaçatı": {
        "desc_tr": "Alaçatı Port bölgesinin kentsel ve modern yüzünü temsil eden bu marina, lüks teknelerin ve şık mekanların buluşma noktasıdır. Kanallar üzerindeki mimarisi ve seçkin restoranlarıyla, kentin en 'Venedik' esintili ve lüks rotasıdır.",
        "desc_en": "Representing the modern face of Alaçatı Port, this marina is a hub for luxury yachts and chic venues. With its canal-based architecture and elite dining, it's the town's most 'Venice-inspired' and upscale route."
    },
    "İmren Helva Ve Tatlı Evi": {
        "desc_tr": "Çeşme'nin 1941'den beri yaşayan efsanesi olan İmren, meşhur sakızlı dondurması, helvası ve kurabiyeleriyle bir kentsel mirastır. Kentin lezzet hafızasında en tatlı yeri tutan bu mekan, geleneksel Ege tatlılarının merkezidir.",
        "desc_en": "A living legend since 1941, İmren is an urban heritage site famous for its mastic ice cream, halva, and cookies. Holding the sweetest spot in the town's memory, it's the center of traditional Aegean confectionery."
    },
    "Kumrucu Şevki Çeşme Merkez-Cafe-Cafeterya-Fast Food-Çeşme Kumrucu": {
        "desc_tr": "Çeşme'nin en ikonik lezzeti olan 'Kumru'nun en meşhur adresi olan Şevki, kentin gastronomi sembolüdür. Sıcak ekmeği ve özel malzemeleriyle hazırlanan kumrularıyla, kente gelenlerin asla es geçmediği bir lezzet durağıdır.",
        "desc_en": "The most famous home for 'Kumru'—Çeşme's iconic sandwich—Şevki is a culinary symbol of the town. With its fresh-baked bread and special ingredients, it's a stop no visitor to the city should ever miss."
    },
    "Kumrucu Hüseyin Gıda San. Tic. Ltd. Şti.": {
        "desc_tr": "Geleneksel kumru tarifini yıllardır bozmadan sürdüren Kumrucu Hüseyin, bu kentsel lezzetin en otantik temsilcilerinden biridir. Eski usul kömür ateşinde pişen malzemeleriyle, kentin gerçek kumru lezzetini keşfedeceginiz bir duraktır.",
        "desc_en": "Maintaining the traditional Kumru recipe for years, Kumrucu Hüseyin is one of the most authentic representatives of this urban flavor. Cooked over traditional coal fires, it’s the place to discover the city's true taste."
    },
    "Asma Yaprağı": {
        "desc_tr": "Alaçatı'nın begonvillerle süslü bir bahçesinde yer alan Asma Yaprağı, tarladan sofraya Ege mutfağının en seçkin örneğidir. Yerel malzemelerle hazırlanan günlük mezeleriyle, kentin gastronomi dünyasındaki en prestijli durağıdır.",
        "desc_en": "Set in a bougainvillea-filled garden, Asma Yaprağı is a prime example of farm-to-table Aegean cuisine. With daily appetizers made from local ingredients, it stands as the most prestigious culinary landmark in town."
    },
    "Uzo Müzesi": {
        "desc_tr": "Alaçatı'nın mistik ve tarihi atmosferinde, bölgenin ortak içki kültürü olan Uzo ve Rakı'nın öykülerini anlatan bu alan, kültürel bir köprü vazifesi görür. Antik kapları ve tadım notlarıyla kentin entelektüel duraklarından biridir.",
        "desc_en": "Set in the mystical atmosphere of Alaçatı, this space tells the story of the shared spirit culture of the region, Uzo and Raki. With its collection of ancient vessels, it serves as an intellectual and cultural bridge."
    },
    "Ferdi Baba Restaurant - Çeşme Marina": {
        "desc_tr": "Çeşme Marina'nın en prestijli noktasında yer alan Ferdi Baba, deniz ürünleri sanatını lüks bir ambiyansla sunar. Tekne manzarası eşliğinde servis edilen taze meze ve balıklarıyla, kentin en elit akşam yemeği adresidir.",
        "desc_en": "The most prestigious spot in Çeşme Marina, Ferdi Baba presents the art of seafood within a luxury ambiance. With fresh catch served against a forest of yacht masts, it is the town's premier elite dining destination."
    },
    "Kalamare Restaurant": {
        "desc_tr": "Dalyan Köyü'nün sakin limanına nazır olan Kalamare, adı gibi taze kalamar ve deniz ürünlerindeki ustalığıyla bilinir. Kentin kentsel karmaşasından uzak, gerçek bir balıkçı kasabası lezzeti arayanların vazgeçilmezidir.",
        "desc_en": "Overlooking the quiet harbor of Dalyan Village, Kalamare is famous for its mastery of fresh calamari and local seafood. It’s an essential stop for those seeking authentic village flavors away from the urban rush."
    },
    "Horasan Balık": {
        "desc_tr": "Çeşme merkezinde, yaratıcı balık mezeleri ve modern sunumlarıyla gastronomi tutkunlarının favorisi olan Horasan, kentin en özel restoranlarından biridir. Samimi ama sofistike mutfağıyla kentin gizli lezzet kalesidir.",
        "desc_en": "A favorite for foodies in central Çeşme, Horasan stands out with its creative seafood appetizers and modern service. With its cozy yet sophisticated kitchen, it acts as the town's secret culinary stronghold."
    },
    "Agrilia Restaurant": {
        "desc_tr": "Alaçatı'nın kalbinde tarihi bir taş binada hizmet veren Agrilia, kentin bohem ve şık ruhunu mutfağına taşır. Ege malzemelerini dünya teknikleriyle birleştiren mekan, kentin en entelektüel ve lezzetli akşam yemeği duraklarındandır.",
        "desc_en": "Housed in a historic stone building in central Alaçatı, Agrilia brings the town's bohemian-chic spirit to the plate. Merging Aegean ingredients with global techniques, it is one of the city's most intellectual dining spots."
    },
    "Eflatun Alaçatı": {
        "desc_tr": "Hacımemiş'in dar sokaklarından birinde, rengarenk bir avluda yer alan Eflatun, samimi ve kaliteli bir mahalle restoranıdır. Mevsimsel ürünlerle hazırlanan yaratıcı menüsüyle, kentin modern Ege mutfağını en iyi temsil eden yerlerden biridir.",
        "desc_en": "Set in a colorful courtyard in a narrow Hacımemiş alley, Eflatun is a warm and high-quality neighborhood bistro. Its creative menu of seasonal produce perfectly represents the city's modern Aegean culinary scene."
    },
    "Kırmızı Ardıç Kuşu": {
        "desc_tr": "Alaçatı'nın en keyifli köşelerinden birinde, yaratıcı pizzaları ve özgün Ege yorumlarıyla tanınan bu mekan bir tasarım harikasıdır. Sanatla iç içe geçmiş dekorasyonu ve lezzetli menüsüyle kentsel sosyal hayatın en sevilen duraklarındandır.",
        "desc_en": "A design marvel in one of Alaçatı's most pleasant corners, famous for its creative pizzas and original Aegean twists. With its art-filled decor and tasty menu, it's a beloved staple of the town's social life."
    },
    "Dost Pide & Pizza": {
        "desc_tr": "Çeşme'nin en köklü lezzet duraklarından biri olan Dost Pide, onlarca yıldır değişmeyen kalitesiyle bir kentsel klasiktir. İncecik hamuru ve bol malzemeli pideleriyle, kentin hem yerlilerinin hem de müdavimlerinin vazgeçilmezidir.",
        "desc_en": "One of Çeşme's longest-standing flavor hubs, Dost Pide is an urban classic of uncompromised quality. With its thin crust and rich toppings, it remains a favorite for both locals and regular peninsula visitors."
    },
    "Veli Usta": {
        "desc_tr": "Çeşme'nin dondurma ve tatlı tarihindeki en önemli isimlerden olan Veli Usta, özellikle sakızlı ve meyveli dondurmalarıyla meşhurdur. Kentin her köşesinde karşınıza çıkabilecek bu lezzet markası, kentin serinleten bir sembolüdür.",
        "desc_en": "One of the most important names in Çeşme's dessert history, Veli Usta is legendary for its mastic and fruit ice creams. Found across the town, this brand is a cooling and delicious symbol of the peninsula."
    },
    "Köşe Kahve": {
        "desc_tr": "Alaçatı'nın tam merkezinde, kentin kentsel ritminin en yoğun olduğu kentsel kavşakta yer alan Köşe Kahve, kentin en popüler buluşma noktasıdır. Beyaz sandalyeleri ve begonvilli atmosferiyle, kentin o meşhur kalabalığını izlemek için idealdir.",
        "desc_en": "At the very center of Alaçatı, where the town's urban rhythm is most intense, Köşe Kahve is the primary meeting hub. With its white chairs and bougainvillea vibe, it’s the best place to watch the famous crowds go by."
    },
    "Sailors Alaçatı": {
        "desc_tr": "Tarihi bir Rum konağının restore edilmesiyle yaratılan bu mekan, hem butik otel hem de şık bir kafe olarak kentsel tarihe tanıklık eder. Alaçatı'nın köklü mimarisini ve kentsel estetiğini en zarif haliyle yansıtan bir kentsel duraktır.",
        "desc_en": "Housed in a restored Greek mansion, this venue serves as both a boutique hotel and a chic cafe witnessing urban history. It elegantly reflects Alaçatı's rooted architecture and aesthetic charm."
    },
    "Çiftlik Köy Cami": {
        "desc_tr": "Balıkçı köyü kültürünün içinde yer alan bu huzurlu cami, mütevazı mimarisi ve kentsel dinginliğiyle bilinir. Çeşme Yarımadası'nın geleneksel köy hayatını ve yerel inanç bağlarını kentsel doku içinde yaşatan samimi bir yapıdır.",
        "desc_en": "Set within a fishing village culture, this peaceful mosque is known for its modest architecture and urban tranquility. It’s a sincere structure keeping traditional village life and local bonds alive in the peninsula's fabric."
    },
    "Çeşme Müzesi": {
        "desc_tr": "Çeşme Kalesi'nin içine gizlenmiş olan bu müze, sualtı arkeolojisinden antik Erythrai buluntularına kadar kentin binlerce yıllık hafızasını saklar. Tarihin surlar arasındaki bu fısıltısı, kentin en önemli kültürel hazinesidir.",
        "desc_en": "Tucked inside the Çeşme Castle, this museum guards the town's millennia-old memory, from underwater archaeology to Erythrai finds. This whisper of history within the walls is the city's most vital cultural treasure."
    },
    "Kethüda Çeşmesi": {
        "desc_tr": "Çeşme'ye adını veren o meşhur tarihi çeşmelerin en zarif örneklerinden biri olan Kethüda Çeşmesi, 18. yüzyıl Osmanlı sanatını yansıtır. Kent merkezindeki bu anıtsal yapı, kentin kentsel kimliğinin ve su külturünün en somut izidir.",
        "desc_en": "One of the most elegant examples of the historic fountains that gave Çeşme its name, Kethüda reflects 18th-century Ottoman art. This monumental structure in the town center is a concrete trace of the city's identity and water culture."
    },
    "Küçük Cami": {
        "desc_tr": "Çeşme çarşısının kalbinde yer alan ve samimi mimarisiyle dikkat çeken bu cami, kentin günlük kentsel yaşamının manevi duraklarından biridir. Beyaz badanalı yapısıyla kentin genel estetiğine uyum sağlayan tarihi bir yapıdır.",
        "desc_en": "Located in the heart of the Çeşme bazaar and notable for its cozy architecture, this mosque is a spiritual stop in daily urban life. Its whitewashed style harmonizes perfectly with the city's general aesthetic."
    },
    "Ayios Haralambos Kilisesi": {
        "desc_tr": "Restore edilerek bir kültür merkezine dönüştürülen bu eski Ortodoks kilisesi, kentin en ihtişamlı yapılarından biridir. Yüksek tavanları ve sanatsal ambiyansıyla, günümüzde kentin en prestijli sergi ve konserlerine ev sahipliği yapar.",
        "desc_en": "Converted into a cultural center after restoration, this former Orthodox church is one of the town's most grand structures. With its high ceilings and artistic aura, it now hosts the city's most prestigious exhibitions and concerts."
    },
    "Cezayirli Gazi Hasan Paşa Anıtı": {
        "desc_tr": "Çeşme sahilinde, kentin denizci geçmişini simgeleyen bu anıt, yanında evcilleştirilmiş aslanıyla tasvir edilen ünlü Osmanlı paşasına adanmıştır. Kalesi ve limanıyla kentin kahramanlık dolu tarihindeki en fotografik sembolüdür.",
        "desc_en": "Standing on the shore as a symbol of maritime past, this monument honors the famous Ottoman admiral depicted with his domesticated lion. It’s a photographic symbol of the town's heroic history next to its castle and harbor."
    },
    "Kırım Hanı I. Kaplan Giray Han Heykeli": {
        "desc_tr": "Çeşme'deki Kırım Tatar mirasını ve kentin misafirperver tarihini temsil eden bu heykel, asırlar boyu süren kültürel bağların bir simgesidir. Kent meydanındaki konumuyla ziyaretçilere kentin çok kültürlü derinliğini hatırlatır.",
        "desc_en": "Representing the Crimean Tatar heritage and the town's welcoming history, this statue is a symbol of centuries-old cultural ties. Its location in the town square reminds visitors of the city's multi-cultural depth."
    },
    "Cesme meydan": {
        "desc_tr": "Limanın, kalenin ve çarşının kesiştiği bu geniş meydan, kentin kentsel sahnesinin başrolündedir. Gün boyu süren hareketliliği, palmiye ağaçları ve deniz manzarasıyla kentin gerçek enerjisini burada hissedebilirsiniz.",
        "desc_en": "Where the harbor, castle, and bazaar converge, this wide square is the main stage for the town's urban life. With its all-day buzz, palms, and sea views, it's where you truly feel the city's genuine energy."
    },
    "ALAÇATI MEYDANI": {
        "desc_tr": "Alaçatı'nın tarihi dokusunun merkezinde yer alan bu meydan, kasabanın kentsel ve sosyal kalbidir. Etrafındaki taş binalar, kafeler ve Likya lahitleriyle, kentin bohem şıklığını ve binlerce yıllık tarihini tek bir noktada buluşturur.",
        "desc_en": "At the center of Alaçatı's historic fabric, this square is the town's urban and social heart. Surrounded by stone buildings, cafes, and Lycian tombs, it merges bohemian chic with millennia of history in one spot."
    },
    "Nirvana Cesme Tekne Turu": {
        "desc_tr": "Çeşme Limanı'ndan kalkan Nirvana turları, kentin saklı koylarını ve kristal netliğindeki Eşek Adası gibi rotaları keşfetmenin en eğlenceli yoludur. Deniz üzerinde geçen bu keyifli gün, kentin 'mavi yolculuk' ruhunu herkese yaşatır.",
        "desc_en": "Departing from Çeşme Harbor, Nirvana tours are the most fun way to explore hidden coves and crystal-clear spots like Eşek Island. This joyful day at sea brings the town's 'Blue Cruise' spirit to life for everyone."
    },
    "Tekke Plaj": {
        "desc_tr": "Çeşme merkezine en yakın ve en geniş halk plajı olan Tekke, kaleye nazır konumu ve sığ deniziyle bilinir. Kentin günlük kentsel rutini içinde, hemen denize girmek isteyen yerli ve yabancı ziyaretçilerin en pratik deniz durağıdır.",
        "desc_en": "The closest and widest public beach to central Çeşme, Tekke is known for its view of the castle and shallow waters. In the city's daily routine, it serves as the most practical sea stop for both locals and tourists."
    },
    "MADO Çeşme Marina": {
        "desc_tr": "Marina'nın en şık köşelerinden birinde yer alan Mado, kentin lüks yat manzarasını geleneksel tatlarla birleştirir. Deniz havasını içinize çekerek kahvenizi yudumlamak için kentin en prestijli ve konforlu duraklarından biridir.",
        "desc_en": "In one of the Marina's most stylish corners, Mado blends view of luxury yachts with traditional flavors. It is one of the town's most prestigious and comfortable spots to sip a coffee while breathing in the sea air."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Çeşme Bulk - Part 1)...")
enrich_venues("cesme", cesme_bulk_1_updates)
print("✨ Systematic Enrichment - Çeşme Bulk Part 1 Complete.")
