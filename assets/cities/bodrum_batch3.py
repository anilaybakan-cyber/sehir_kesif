import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
92: {'d': "Bodrum Kalesi'ne yakın konumuyla Doria Hotel, tarihin tam içinden bakmanızı sağlayan kale manzaralı odaları ve zarif taş mimarisiyle butik konaklama arayan gezginlerin tercihidir. Kahvaltı terasında kaleye bakarak içilen sabah kahvesi, Bodrum'daki günün en değerli başlangıcına dönüşür.",
    'de': "With its location close to Bodrum Castle, Doria Hotel is the preference of travelers seeking boutique accommodation, with its castle-view rooms that let you look out from the middle of history and elegant stone architecture. Morning coffee on the breakfast terrace while gazing at the castle becomes the most memorable start to a day in Bodrum."},

93: {'d': "Bodrum merkezi yakınındaki Okaliptüs Otel, adını bahçesindeki okaliptüs ağaçlarından alır. Küçük havuzu ve bakımlı yeşil alanlarıyla kentin kalabalığından uzakta sakin bir konaklama sunar; yürüme mesafesinde kasaba merkezi ve liman bölgesi erişilebilir.",
    'de': "Okaliptüs Otel near central Bodrum takes its name from the eucalyptus trees in its garden. It offers a tranquil stay away from the town's hustle with its small pool and well-tended green areas; the town center and harbor district are accessible on foot."},

95: {'d': "Bodrum'un şık butik oda konseptini en iyi yansıtan mekanlardan L'onda Oda, minimalist dekoru, balkonlu deniz manzaralı odaları ve mahremiyet anlayışıyla çiftlere yönelik kaçış destinasyonu olarak popülerlik kazanmıştır. Yürüme mesafesinde Marina ve eski çarşı konumu günlük lojistiği kolaylaştırır.",
    'de': "L'onda Oda, one of the best reflections of Bodrum's elegant boutique room concept, has gained popularity as a couples' escape destination with its minimalist décor, balconied sea-view rooms, and privacy-focused approach. Walking-distance access to the Marina and old bazaar simplifies daily logistics."},

97: {'d': "İspanyolca 'tutku' anlamına gelen adıyla uyumlu olan La Pasion, Bodrum'un üst mahalle sakinlerinin sevdiği küçük bar-restoranlarından biridir. Taze deniz ürünlü tapaslar ve İspanya'dan ithal şarap listesi, güneybatı Akdeniz havasını Bodrum'un mahallesine taşır.",
    'de': "True to its Spanish name meaning 'passion', La Pasion is one of the small bar-restaurants loved by Bodrum's upper neighborhood residents. Fresh seafood tapas and an imported Spanish wine list bring the southwestern Mediterranean atmosphere to Bodrum's neighborhood streets."},

99: {'d': "Bodrum eski limanında, teknelerin gölgesinde kurulan Körfez Restoran, deniz ürünleri piyango çorbası ve taze levrek mezgit gibi sıradan sezon balıklarıyla yerel halkın sofrasına yakın bir mekan olarak bilinir. Dış görünüşünden çok içindeki otantik balıkçı lokantası deneyimi ön plandadır.",
    'de': "Körfez Restoran, set up in Bodrum's old harbor in the shade of boats, is known as a venue close to local residents' table with its seafood soup and fresh sea bass and whiting among the everyday seasonal fish. The authentic fishing tavern experience inside takes precedence over the exterior appearance."},

101: {'d': "Bodrum merkezi yakınında apart otel konforunu sunan Ayhan Suite, uzun dönem konaklamayı tercih edenlerin ya da aile gruplarının pratik ihtiyaçlarına yönelik mutfaklı suite odalarıyla bölgedeki değerli seçenekler arasındadır. Terasından liman bölgesi ve sahil şeridine yakın günlük erişim avantajı taşır.",
    'de': "Offering apart hotel comfort near central Bodrum, Ayhan Suite is among the area's valuable options with kitchenette suites catering to the practical needs of those preferring long stays or family groups. It benefits from easy daily access to the harbor district and seafront from its terrace."},

103: {'d': "Bodrum'un zeytinliklerle kaplı tepelerinde konumlanan bu pansiyon, gün doğumunda Ege mavisiyle boyanan manzarasını ve ev yapımı otlu peynirini sunduğu güne merhaba kahvaltısıyla doğanın içinde hissettiriyor. Konum itibarıyla yaz kalabalığına rağmen muazzam bir huzur sunabilecek az sayıda mekanın başında geliyor.",
    'de': "Located on Bodrum's olive-grove-covered hills, this pension feels immersed in nature with its view painted Aegean blue at sunrise and a good-morning breakfast serving homemade herb cheese. In terms of location, it tops the short list of places that can offer remarkable tranquility despite summer crowds."},

104: {'d': "Bodrum Denizcilik Derneği bünyesindeki bu sahil kafesi, yerel denizcilerin ve tekne sahiplerinin sabah sohbet ettiği, bardak çayını gazetesiyle içtiği özgün bir mekandır. Marina kalabalığından uzak, eski liman yakınlarındaki bu kafe Bodrum'un gerçek denizci kimliğini yansıtır.",
    'de': "This seafront café within Bodrum Sailing Association is an authentic spot where local sailors and boat owners have morning conversations and sip their tea with the newspaper. Located near the old harbor away from the marina crowds, this café reflects Bodrum's true seafaring identity."},

105: {'d': "Belediye işletmesinde olan bu kafe ve restoran, Bodrum'un en merkezi noktalarından birinde konumuyla hem yerel halk hem de turistler için erişilebilir ve uygun fiyatlı bir mola sunar. Bodrum Belediyesi'nin yönetimindeki bu mekan, standart menü içinde bölgeye özgü taze sıkılmış meyve suları ve yerel tatlılarıyla öne çıkar.",
    'de': "Operated by the municipality, this café and restaurant offers an accessible and reasonably priced break for both locals and tourists from its position at one of Bodrum's most central points. Managed by Bodrum Municipality, this venue stands out within its standard menu for freshly squeezed regional fruit juices and local desserts."},

107: {'d': "Bodrum'un liman bölgesinde yer alan bu mekan, Türkiye'nin en güçlü uluslararası hizmet ağına sahip akaryakıt istasyonu zincirinin marina yakınındaki noktasıdır. Kıyı yolcuları ve tekne sahipleri için pratik bir uğrak noktasına sahip olmakla birlikte kafesi ve marketi de günübirlik ziyaretçilere hizmet verir.",
    'de': "Located in Bodrum's harbor district, this venue is the marina-area point of Turkey's strongest international service network fuel station chain. While serving as a practical stop for coastal travelers and boat owners, its café and market also serve day visitors."},

108: {'d': "Bodrum'un eski çarşısının içinde, taştan bir koridorda saklanan bu geleneksel Türk kahvesi, günlük backgammon oynayanları, yerel esnafı ve semtin sakinlerini buluşturur. Açık köz üzerinde demlenen sıkı Türk kahvesi ve yanında lokum, kentin modernleşen yüzünden önce var olan otantik Bodrum ritüelini yaşatır.",
    'de': "Hidden in a stone corridor within Bodrum's old bazaar, this traditional Turkish coffeehouse brings together daily backgammon players, local tradespeople, and neighborhood residents. Strong Turkish coffee brewed over open coals with Turkish delight alongside preserves the authentic Bodrum ritual that existed before the town's modernizing face."},

109: {'d': "Yalıkavak Marina civarındaki bu perakende noktası, marinada yat donatım ve bakım malzemeleri ile denizcilik aksesuarları konusunda uzman bir tedarikçi olarak deniz tutkunlarına hizmet eder. Sezon öncesi tur hazırlığı yapan yat sahipleri için bölgedeki pratik tedarik noktalarından biridir.",
    'de': "This retail point near Yalıkavak Marina serves maritime enthusiasts as a supplier specializing in yacht outfitting and maintenance materials and nautical accessories in the marina area. It is one of the practical supply points in the area for yacht owners preparing for a pre-season tour."},

110: {'d': "Bodrum'un arka mahallelerindeki Musto Bistro, yerel halkın izleme açısından zengin caddesi boyunca serilmiş masaları ve günlük değişen iki kurs menüsüyle şehrin gürültüsüne rağmen sakin bir öğle yemeği köşesi sunar. Mezgit güveci ve yerel zeytinyağlı sebze yemekleri favori sipariş kalemidir.",
    'de': "Musto Bistro in Bodrum's back neighborhoods offers a tranquil lunch corner despite the town's noise with its tables spread along a people-watching-rich street and a two-course daily changing menu. Whiting casserole and local olive oil vegetable dishes are the favorite order items."},

112: {'d': "Bodrum'un Gümbet bölgesindeki bu nargile kafesi, denize yakın konumuyla hem nargile tutkunlarının hem de akşam saatlerinde oturup körfeze bakmak isteyenlerin tercihidir. Çeşitli tütün aromalarının yanı sıra taze sıkılmış meyve suları ve soğuk içecekleriyle hafif bir akşam molası için idealdir.",
    'de': "This shisha café in Bodrum's Gümbet district is the preference of both shisha enthusiasts and those wishing to sit and gaze at the bay in the evenings, thanks to its seafront location. Along with various tobacco aromas, it is ideal for a light evening break with freshly squeezed fruit juices and cold drinks."},

113: {'d': "Gümbet Belediyesi tarafından işletilen bu kafe, Gümbet plaj şeridi boyunca en erişilebilir ve en uygun fiyatlı oturma alanlarından birini sunar. Sabah kahvesinden öğle arası soğuk içeceğe kadar her saatte ziyaret edilebilir; yüz yüze gelen kıyı görüntüsü buranın en büyük artısıdır.",
    'de': "Operated by Gümbet Municipality, this café offers one of the most accessible and affordable seating areas along Gümbet's beachfront strip. Visitable at any hour from morning coffee to a midday cold drink; the facing coastal view is its greatest advantage."},

114: {'d': "Bodrum merkezinin kalabalık sokaklarından biraz içeride konumlanan Gusto Cafe, el yapımı kek ve tart çeşitleri ile bölgede pastane-kafe karmasını en iyi sunan mekanlar arasında yer alır. Günlük taze hazırlanan limonlu kek dilimi ve soğuk kâhveler, öğleden sonra molası için mükemmel eşleşmedir.",
    'de': "Located slightly inside one of Bodrum center's busy streets, Gusto Cafe is among the area's best venues offering the pastry-café blend, with its handmade cake and tart varieties. Daily fresh-prepared lemon cake slice and cold coffees are a perfect pairing for an afternoon break."},

115: {'d': "Bodrum esnafının sabah sıcak ekmek için uğradığı Karya Fırın, taş fırında pişirilen köy ekmeği, zeytinli pide ve simitiyle semtin en eski geleneksel fırınlarından biridir. Sabah erken saatlerde fırından çıkan sıcak ekmek kokusu sokağa yayılır ve esnafı ve okul çocuklarını içeri çeker.",
    'de': "Karya Fırın, where Bodrum tradespeople stop for hot morning bread, is one of the neighborhood's oldest traditional bakeries with its stone-oven-baked village bread, olive pide, and simit. In the early morning, the smell of hot bread from the oven spreads into the street, drawing in tradespeople and school children."},

116: {'d': "Türkiye'nin en ünlü lüks lokumu markalarından birinin Bitez şubesi olan bu mağaza, geleneksel Osmanlı lokum çeşitlerini hem kuru meyve dolgularıyla hem de Bodrum'a özgü mandalina ve incir aromalarıyla sunar. El yapımı ambalajlarıyla hediye kutuları satın almak isteyenler için ideal bir durak.",
    'de': "The Bitez branch of one of Turkey's most famous luxury Turkish delight brands, this shop offers traditional Ottoman Turkish delight varieties both with dried fruit fillings and with mandarin and fig aromas unique to Bodrum. An ideal stop for those wishing to purchase handcrafted gift boxes."},

117: {'d': "Bodrum'un orta ölçekli tatilci profiline hitap eden Kaya Apart, mutfaklı odaları ve merkezi olmayan ama yürünebilir konumuyla özellikle araçlı gelen ve yarımadayı kendi temposunda gezmek isteyen ailelerin tercih ettiği ekonomik bir konaklama seçeneğidir.",
    'de': "Kaya Apart, catering to Bodrum's mid-scale holidaymaker profile, is an economical accommodation option preferred especially by families arriving by car and wishing to explore the peninsula at their own pace, with its kitchenette rooms and non-central but walkable location."},
}

apply_batch('bodrum.json', U)
