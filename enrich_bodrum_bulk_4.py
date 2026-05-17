from enrich_venues import enrich_venues

# BATCH: BODRUM SYSTEMATIC COMPLETION - PART 4

bodrum_bulk_4_updates = {
    "Poseidon Port Meet Point": {
        "desc_tr": "Yalıkavak Marina'da tekne turlarının ve deniz maceralarının başlangıç noktası olan Poseidon, kentin en hareketli 'buluşma' noktalarından biridir. Masmavi sulara açılmadan önce kentin heyecanlı atmosferini soluyabileceğiniz stratejik bir konumdadır.",
        "desc_en": "The starting point for boat tours and marine adventures in Yalıkavak Marina, Poseidon is one of the town's busiest meeting hubs. It’s the perfect strategic spot to soak in the exciting atmosphere before heading out to the deep blue."
    },
    "Fahri Çetinkaya": {
        "desc_tr": "Bodrum'un geleneksel tekstil sanatını modern tasarımlarla buluşturan bu butik mağaza, yüksek kaliteli ev tekstili ve yerel dokumalarıyla bilinir. Kentin estetik ruhunu evinize taşımak isteyenler için özenle seçilmiş bir koleksiyon sunar.",
        "desc_en": "Merging traditional Bodrum textiles with modern design, this boutique is known for its high-quality home linens and local weaves. It offers a curated collection for those looking to bring the town’s aesthetic soul into their homes."
    },
    "Ergin Farm": {
        "desc_tr": "Yalıkavak'ın sırtlarında, doğayla baş başa kalabileceğiniz Ergin Farm, organik tarım ve geleneksel köy kahvaltısıyla meşhurdur. Tarladan sofraya taze ürünleri ve huzurlu çiftlik atmosferiyle, Bodrum'da sakin bir sabahın değişmez adresidir.",
        "desc_en": "Perched on the hills of Yalıkavak, Ergin Farm is famous for its organic farming and traditional village breakfasts. With farm-to-table freshness and a serene farm atmosphere, it's a staple for a peaceful morning in Bodrum."
    },
    "Halk plajı": {
        "desc_tr": "Yalıkavak'ın kristal sularına açılan bu geniş halk plajı, kentin en temiz ve huzurlu sahillerinden biridir. Mavi bayraklı denizi ve eşsiz gün batımı manzarasıyla, hem yerel halkın hem de kenti keşfedenlerin favori yüzme noktalarından biridir.",
        "desc_en": "Opening onto the crystal waters of Yalıkavak, this wide public beach is one of the cleanest and most peaceful shores in the area. With its Blue Flag sea and stunning sunset views, it's a favorite swimming spot for both locals and travelers."
    },
    "Kybele house": {
        "desc_tr": "Yalıkavak'ın otantik dokusuna sadık kalınarak tasarlanmış Kybele House, sanat ve konforun iç içe geçtiği butik bir konaklama noktasıdır. Yaratıcı atmosferi ve özenle dekore edilmiş odalarıyla, kentin bohem ruhunu yansıtan bir sığınaktır.",
        "desc_en": "Designed with loyalty to Yalıkavak's authentic texture, Kybele House is a boutique stay where art and comfort meet. Its creative atmosphere and meticulously decorated rooms make it a sanctuary reflecting the town's bohemian spirit."
    },
    "Tilkicik Koyu": {
        "desc_tr": "Yarımada'nın en sakin ve korunaklı koylarından biri olan Tilkicik, turkuaz suları ve lüks sahilleriyle ünlüdür. Rüzgara kapalı yapısıyla gün boyu çarşaf gibi olan denizi, Bodrum'da kesintisiz deniz keyfi arayanların vazgeçilmezidir.",
        "desc_en": "One of the peninsula's most tranquil and sheltered bays, Tilkicik is famous for its turquoise waters and upscale shores. Its calm, wind-protected sea makes it a must-visit for those seeking uninterrupted swimming joy in Bodrum."
    },
    "LA LOCAL BEACH & HOTEL YALIKAVAK": {
        "desc_tr": "Modern bir plaj kulübü anlayışını şık bir konaklama ile birleştiren La Local, Yalıkavak'ın en enerjik noktalarından biridir. Kaliteli müziği, gurme lezzetleri ve denize sıfır konumuyla Bodrum tatiline stil sahibi bir dokunuş katar.",
        "desc_en": "Combining a modern beach club concept with stylish accommodation, La Local is one of Yalıkavak's most energetic spots. With premium music, gourmet flavors, and a beachfront location, it adds a stylish touch to any Bodrum holiday."
    },
    "Şafak Zirvesi": {
        "desc_tr": "Yalıkavak'ın en yüksek noktalarından biri olan Şafak Zirvesi, tüm yarımadayı kuşbakışı gören efsanevi bir manzaraya sahiptir. Özellikle sabahın ilk ışıklarında kentin sessizliğini ve doğanın uyanışını izlemek için eşsiz bir seyir terasıdır.",
        "desc_en": "One of the highest points in Yalıkavak, Şafak Zirvesi boasts a legendary panoramic view of the entire peninsula. It is a unique vantage point to watch the city's silence and nature's awakening during the first light of dawn."
    },
    "Top peak sunset view": {
        "desc_tr": "Bodrum'un en ünlü 'gün batımı' noktası olan bu tepe, denizin ve ufuk çizgisinin binbir renge büründüğü masalsı bir manzara sunar. Fotoğraf tutkunları ve romantik bir akşam başlangıcı arayanlar için kentin en popüler doğal balkonudur.",
        "desc_en": "Bodrum's most famous sunset spot, this peak offers a magical view where the sea and horizon blend into a thousand colors. It is the most popular natural balcony in town for photographers and those seeking a romantic evening start."
    },
    "T.C. Kültür ve Turizm Bakanlığı Yalıkavak Halk Plajı": {
        "desc_tr": "Bakanlık standartlarında hizmet sunan bu mavi bayraklı plaj, temizliği ve profesyonel işletmesiyle öne çıkar. Yalıkavak'ın serin sularında güvenle ve konforla denize girmek isteyen aileler için kentin en güvenilir duraklarından biridir.",
        "desc_en": "This Blue Flag beach, serving at ministry standards, stands out for its cleanliness and professional management. It’s one of the town's most reliable spots for families wanting to swim safely and comfortably in Yalıkavak's cool waters."
    },
    "Öykümnaz Sivrikaya Koyu": {
        "desc_tr": "Sivrikaya bölgesinde yer alan bu saklı koy, el değmemiş doğası ve akvaryum berraklığındaki deniziyle bilinir. Kalabalıklardan uzak, sadece dalga sesleri ve rüzgarın eşlik ettiği bakir bir deniz günü geçirmek isteyenlerin gizli adresidir.",
        "desc_en": "Tucked away in the Sivrikaya region, this hidden bay is known for its untouched nature and aquarium-clear water. It’s a secret escape for those seeking a pristine day by the sea, accompanied only by the sound of waves."
    },
    "Feraya Hanım koyu": {
        "desc_tr": "Yalıkavak yakınlarında yer alan ve doğal yapısıyla korunan Feraya Hanım Koyu, turkuazın en saf tonlarını sunar. Kayalık yapısı sayesinde suyun berraklığının bozulmadığı bu koy, şnorkel tutkunları için saklı bir su altı cennetidir.",
        "desc_en": "Located near Yalıkavak and naturally preserved, Feraya Hanım Bay offers the purest shades of turquoise. Thanks to its rocky shore keeping the water crystal clear, it’s a hidden underwater paradise for snorkeling enthusiasts."
    },
    "Ortakent Viewpoint": {
        "desc_tr": "Ortakent'in tepelerinde, tüm Bodrum Yarımadası'nı ve çevre adaları gören bu nokta, kentin en geniş panoramik açılarından birine sahiptir. Doğanın ve mavinin her tonunu tek bir karede yakalayabileceğiniz bir seyir mirasıdır.",
        "desc_en": "Perched on the hills of Ortakent, this spot offers one of the widest panoramic views of the Bodrum Peninsula and surrounding islands. It’s a viewing heritage where you can capture every shade of nature and blue in a single frame."
    },
    "4 reasons Hotel Yalikavak": {
        "desc_tr": "Bodrum'un en özgün butik otellerinden biri olan 4 Reasons, gastronomi, müzik, tasarım ve huzur odaklı felsefesiyle tanınır. Zeytin ağaçları içindeki konumuyla, kentin lüks ve sofistike yüzünü temsil eden çok özel bir konaklama noktasıdır.",
        "desc_en": "One of Bodrum's most original boutique hotels, 4 Reasons is famous for its philosophy focused on gastronomy, music, design, and peace. Set amidst olive groves, it is an exclusive stay representing the town's sophisticated side."
    },
    "Èlite Hotel Bodrum": {
        "desc_tr": "Yalıkavak sahilinde lüks ve konforun buluştuğu Elite Hotel, modern mimarisi ve geniş sosyal alanlarıyla kentin prestijli duraklarından biridir. Denize hakim konumu ve rafine hizmet kalitesiyle unutulmaz bir Bodrum tatili vaat eder.",
        "desc_en": "Where luxury meets comfort on the Yalıkavak shore, Elite Hotel is a prestigious landmark with modern architecture and expansive social areas. Its seafront location and refined service guarantee an unforgettable Bodrum holiday."
    },
    "Yalıpark Beach Hotel": {
        "desc_tr": "Yalıkavak'ın en canlı noktalarından birinde yer alan Yalıpark, misafirlerine 'denizin üzerinde' bir konaklama hissi sunar. Şık plajı ve havuzuyla, kentin enerjik temposuna dahil olurken aynı zamanda konforu bırakmak istemeyenlerin tercihidir.",
        "desc_en": "Located in one of Yalıkavak's most vibrant spots, Yalıpark gives guests a feeling of staying 'above the sea.' With its chic beach and pool, it's the choice for those who want comfort without missing the town's energetic rhythm."
    },
    "Ali Baba Restaurant": {
        "desc_tr": "Yalıkavak'ın en köklü ve klasik balıkçılarından olan Ali Baba, yıllardır değişmeyen taze deniz ürünleri ve meşhur mezeleriyle bir gelenektir. Limana nazır masalarında, kentin gerçek Ege mutfağı ruhunu en samimi haliyle sunar.",
        "desc_en": "One of Yalıkavak's most established and classic fish restaurants, Ali Baba is a tradition with its consistently fresh seafood and famous appetizers. It serves the authentic spirit of Aegean cuisine at its harbor-front tables."
    },
    "Liona Hotel": {
        "desc_tr": "Gündoğan'ın modern mimari simgelerinden olan Liona, minimalist tasarımı ve huzur dolu ambiyansıyla kentin çağdaş yüzünü temsil eder. Zeytinlikler arasındaki konumu ve rafine detaylarıyla, kaliteli bir kaçış noktasıdır.",
        "desc_en": "A modern architectural landmark in Gündoğan, Liona represents the contemporary face of the town with its minimalist design and serene ambiance. Set among olive groves, it’s a premier spot for a high-quality escape."
    },
    "Yaprak Şarküteri": {
        "desc_tr": "Yalıkavak'ın en ünlü gurme durağı olan Yaprak Şarküteri, yerel peynirlerden özel zeytinyağlarına kadar yarımadanın lezzet hazinesidir. Tatil dönüşü kentin tadını yanında götürmek isteyenlerin en çok uğradığı lezzet noktasıdır.",
        "desc_en": "The most famous gourmet destination in Yalıkavak, Yaprak Deli is a treasure trove of local flavors, from regional cheeses to special olive oils. It's the top stop for those wanting to take a piece of Bodrum's taste back home."
    },
    "Çimentepe Apart Otel": {
        "desc_tr": "Yalıkavak'ta tarihin ve manzaranın kucaklaştığı Çimentepe, kentin en eski ve en karakteristik apart otellerinden biridir. Yüksek konumu sayesinde sunduğu eşsiz deniz manzarasıyla, gerçek bir Bodrum klasiğidir.",
        "desc_en": "Where history and scenery embrace in Yalıkavak, Çimentepe is one of the most characterful and longest-standing apart hotels. It's a true Bodrum classic, offering unique sea views from its elevated location."
    },
    "Balıkçı Hasanın Yeri": {
        "desc_tr": "Yalıkavak sahilinde, samimi atmosferi ve denizden yeni çıkmış taze ürünleriyle tanınan Balıkçı Hasan, gerçek bir yerel favoridir. Salaş şıklığı ve enfes Ege mezeleriyle, kentin en keyifli gurme duraklarından biridir.",
        "desc_en": "On the Yalıkavak shore, famous for its friendly atmosphere and products fresh from the sea, Balıkçı Hasan is a true local favorite. Its casual-chic vibe and exquisite Aegean appetizers make it a premier culinary destination."
    },
    "Yelken Bay Beach Hotel": {
        "desc_tr": "Bitez'in en şık sahillerinden birinde yer alan Yelken Bay, modern tasarımı ve enerjik plaj kültürüyle öne çıkar. Yarımada'da güneşin ve denizin keyfini, kaliteli müzik ve konforlu bir konaklama ile birleştiren bir adrestir.",
        "desc_en": "Located on one of Bitez’s most stylish shores, Yelken Bay stands out with its modern design and energetic beach culture. It’s the place to blend sun and sea with premium music and comfortable lodging on the peninsula."
    },
    "Sofi’s Marina Brasserie": {
        "desc_tr": "Yalıkavak Marina'da Avrupa esintili bir brasserie deneyimi sunan Sofi's, rafine mutfağı ve şık barıyla kentin sosyal yaşam kalbidir. Marinadaki lüks yatlar eşliğinde gün boyu süren enerjisiyle kentin en prestijli noktalarındandır.",
        "desc_en": "Offering a European-inspired brasserie experience in Yalıkavak Marina, Sofi's is the heart of social life with its refined kitchen and chic bar. It’s one of the town's most prestigious spots, pulsing with all-day energy."
    },
    "Kavaklı Köftecisi": {
        "desc_tr": "Bodrum'un en ünlü lezzet duraklarından biri olan Kavaklı Köftecisi, kuşaktan kuşağa aktarılan gizli tarifiyle bir şehir efsanesidir. Kente gelen her ziyaretçinin mutlaka uğradığı, samimi ve gerçek bir lezzet mirasıdır.",
        "desc_en": "One of Bodrum's most famous food landmarks, Kavaklı Köftecisi is a local legend with a secret recipe passed down through generations. A sincere and authentic heritage of flavor, it’s a must-stop for every visitor."
    },
    "Artemis Pension": {
        "desc_tr": "Yalıkavak merkezinde, kentsel dokuya uyumlu mimarisi ve sıcak konukseverliğiyle bilinen Artemis, bütçe dostu ama kaliteli bir konaklama alternatifi sunar. Bodrum'un gerçek mahalle kültürünü hissetmek isteyenler için idealdir.",
        "desc_en": "In the heart of Yalıkavak, known for its town-harmonious architecture and warm hospitality, Artemis offers an affordable yet high-quality stay. Ideal for those wanting to feel Bodrum’s authentic neighborhood culture."
    },
    "Indigo Restaurant & Bar": {
        "desc_tr": "Yalıkavak Marina'nın en trendy duraklarından biri olan Indigo, yaratıcı mutfağı ve iddialı kokteyl menüsüyle dikkat çeker. Modern tasarımı ve kentin enerjisini yansıtan ambiyansıyla, marina akşamlarının vazgeçilmezidir.",
        "desc_en": "One of Yalıkavak Marina's trendiest spots, Indigo stands out with its creative menu and bold cocktail list. With modern design and an ambiance reflecting the town's energy, it's a staple for marina evenings."
    },
    "Lecafe Ristorante İtaliano": {
        "desc_tr": "Bodrum'da gerçek İtalyan lezzetlerinin adresi olan LeCafe, odun ateşinde pizzaları ve taze makarnalarıyla bir lezzet durağıdır. Marina manzaralı şık terasıyla, kentin en romantik ve nezih restoranları arasında yer alır.",
        "desc_en": "Bodrum's home for authentic Italian flavors, LeCafe is famous for its wood-fired pizzas and fresh pastas. With its elegant terrace overlooking the marina, it ranks among the city’s most romantic and refined restaurants."
    },
    "Sevilla Çakıroğlu Restaurant": {
        "desc_tr": "Ege malzemelerini İspanyol mutfak teknikleriyle harmanlayan Sevilla Çakıroğlu, kentin en yaratıcı gastronomi noktalarından biridir. Şık sunumları ve geniş kavıyla, Yalıkavak'ta farklı ve kaliteli bir akşam yemeği arayanları ağırlar.",
        "desc_en": "Blending Aegean ingredients with Spanish techniques, Sevilla Çakıroğlu is one of the town's most creative food spots. It welcomes those seeking a unique and high-quality dinner in Yalıkavak with its elegant service."
    },
    "Panorama Pasanda Restaurant": {
        "desc_tr": "Adının hakkını veren bu mekan, tüm Bodrum Yarımadası'nı ayaklarınızın altına seren nefes kesici bir manzaraya sahiptir. Özellikle gün batımı saatlerinde, doğanın sunduğu bu görsel şöleni lezzetli bir yemekle taçlandırmak için eşsizdir.",
        "desc_en": "True to its name, this venue offers a breathtaking view that puts the entire Bodrum Peninsula at your feet. It is unparalleled for crowning nature's visual sunset feast with a delicious meal."
    },
    "COOKSHOP. Bodrum": {
        "desc_tr": "Yalıkavak Marina'nın popüler ve dinamik adreslerinden olan Cookshop, geniş menüsü ve samimi atmosferiyle kentin buluşma noktasıdır. Marinadaki lüks doku içinde, kaliteli ve ferah bir mola vermek isteyenlerin favorisidir.",
        "desc_en": "A popular and dynamic hub in Yalıkavak Marina, Cookshop is a favorite meeting point with its extensive menu and friendly vibe. It’s perfect for a high-quality, refreshing break amidst the marina's luxury."
    },
    "1AZ Fast Food By Kavaklı Köfteci": {
        "desc_tr": "Kavaklı Köftecisi'nin kalitesini hızlı servis anlayışıyla birleştiren 1AZ, kentin en popüler 'lezzet molası' duraklarındandır. Geleneksel köfte tadını modern bir sunumla tatmak isteyenlerin pratik ve lezzetli adresidir.",
        "desc_en": "Merging the quality of Kavaklı Köftecisi with a quick-service concept, 1AZ is one of the town's most popular 'flavor break' stops. It’s the practical and delicious address for those wanting traditional taste with modern speed."
    },
    "Caba Restaurant": {
        "desc_tr": "Yalıkavak'ta rafine bir gastronomi deneyimi sunan Caba, deniz ürünlerindeki ustalığı ve şık dekorasyonuyla bilinir. Kentin elit akşam yemeği duraklarından biri olarak, hem lezzet hem de estetik arayan misafirlerini ağırlar.",
        "desc_en": "Offering a refined gastronomic experience in Yalıkavak, Caba is known for its seafood mastery and chic decor. As one of the town's elite dining spots, it welcomes guests looking for both flavor and aesthetic merit."
    },
    "Saraybosna Köftecisi": {
        "desc_tr": "Balkanların meşhur köfte kültürünü Bodrum'a taşıyan bu durak, özgün tarifleri ve samimi ortamıyla tanınır. Yalıkavak çarşısında geleneksel ve farklı bir lezzet deneyimi arayanların vazgeçilmez uğrak noktasıdır.",
        "desc_en": "Bringing the famous Balkan meatball culture to Bodrum, this spot is known for its original recipes and friendly setting. It's an indispensable stop for those seeking a traditional yet different taste in the Yalıkavak bazaar."
    },
    "Yalıkavak İskele Cafe - Bodrum Belediye A.Ş.": {
        "desc_tr": "Tarihi Yalıkavak iskelesinde yer alan bu belediye kafesi, kentin en samimi ve huzurlu seyir noktalarından biridir. Denizin hemen yanı başındaki masalarında, kentin ruhunu en ekonomik ve gerçek haliyle soluyabileceğiniz bir duraktır.",
        "desc_en": "Located at the historical Yalıkavak pier, this municipal cafe is one of the town's most genuine and peaceful vantage points. It’s a spot where you can soak in the city’s soul most economically and authentically by the waves."
    },
    "Haremlique Istanbul Yalıkavak Marina": {
        "desc_tr": "Lüks ve estetiğin temsilcisi Haremlique, Yalıkavak Marina'daki butiğiyle Osmanlı saray geleneğinin modern yansımasını sunar. Zarif ev tekstili ve özel parfüm koleksiyonlarıyla, Bodrum tatilinize prestij ve kalite katar.",
        "desc_en": "Representing luxury and aesthetic merit, the Haremlique boutique in Yalıkavak Marina offers a modern reflection of Ottoman palace tradition. With its elegant linens and perfume collections, it adds prestige to any Bodrum stay."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Bodrum Bulk - Part 4)...")
enrich_venues("bodrum", bodrum_bulk_4_updates)
print("✨ Systematic Enrichment - Bodrum Bulk Part 4 Complete.")
