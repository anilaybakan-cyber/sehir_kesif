import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
3: {'d': "Antik Myndos şehrinin MÖ 4. yüzyıldan kalma ana kapısı, Bodrum yarımadasındaki en iyi korunmuş Helenistik mimari kalıntılarından biridir. İki kuleyle güçlendirilmiş bu kapı, günümüzde şehir merkezinin içinde ayakta durmaya devam etmesiyle tarihin ne kadar derine köklü olduğunu hatırlatır.",
    'de': "The main gate of ancient Myndos dating from the 4th century BC is one of the best-preserved Hellenistic architectural remains on the Bodrum peninsula. Reinforced by two towers, this gate continues to stand within the modern city center, a reminder of how deeply rooted history runs here.",
    't': "Kapının etrafındaki küçük otoparkta durun; çevre sakinlerinden daha detaylı tarihi bilgi almak mümkündür.",
    'te': "Park near the gate; local residents nearby can provide more detailed historical background if asked."},

8: {'d': "Bodrum'un üst mahallelerinde, zeytinliklerin arasına sıkışmış Karakaya, geleneksel taş evleri ve bakımlı bahçeleriyle yarımadanın en sakin köy deneyimini sunar. Tepeden bakıldığında Bodrum kalesinin silueti ve körfezin mavisi bir arada görülür; sessizliği arayan ziyaretçilerin gizli cenneti.",
    'de': "Nestled among olive groves in Bodrum's upper quarters, Karakaya offers the peninsula's most tranquil village experience with its traditional stone houses and well-tended gardens. From the hilltop, Bodrum Castle's silhouette and the blue of the bay appear together — a hidden paradise for visitors seeking quiet.",
    't': "Sabah erken ziyarette yerel meyve bahçelerinden taze incir ve zeytin satın alabilirsiniz; öğleden sonra köy neredeyse uyur.",
    'te': "On an early morning visit you can buy fresh figs and olives from local orchards; by afternoon the village is almost asleep."},

18: {'d': "Bağla Koyu'nun mavi sularına nazır konumlanan bu yerleşim yeri, Bodrum'un en serin ve en az kalabalık koylarından birine yürüme mesafesindedir. Gün batımında denizin aldığı turuncu renk ve sahile vurduğu ışık, sabah erkenden kamp kuran fotoğrafçıların favori karelerini oluşturur.",
    'de': "Overlooking the blue waters of Bağla Cove, this settlement is within walking distance of one of Bodrum's coolest and least crowded bays. The orange glow the sea takes at sunset and the light striking the shore create the favorite shots of photographers who camp here from early morning.",
    't': "Koy, yaz aylarında bile görece tenha kalır; kalabalıktan kaçmak isteyenler için sabah ziyareti idealdir.",
    'te': "The cove remains relatively uncrowded even in summer; a morning visit is ideal for those wanting to avoid the crowds."},

23: {'d': "Bodrum'un kuzey kıyılarında uzanan Küçükbük Sahili, ince kumlu kıyısı ve zeytinliklere dayanan sırtıyla aile tatilcilerinin tercih ettiği sakin bir plajdır. Önünde uzanan küçük çakıl kayalıkları ve berrak sığ denizi, şnorkel için de oldukça elverişlidir.",
    'de': "Stretching along Bodrum's northern coast, Küçükbük Beach is a tranquil shore preferred by family holidaymakers for its fine sandy shoreline backed by olive groves. The small rocky outcrops and clear shallow water in front are also well-suited for snorkeling.",
    't': "Plajın sağ ucundaki kayalıklar şnorkel için en iyi noktayı oluşturur; deniz altı kayalarda ahtapot ve renkli balıklara rastlamak olasıdır.",
    'te': "The rocks at the right end of the beach form the best snorkeling spot; octopus and colorful fish are often spotted among the underwater rocks."},

24: {'d': "Bodrum'un iç kesimlerindeki Mazıköy, geleneksel meyhaneleri ve geniş zeytinlikleriyle yarımadanın en özgün kırsal durakları arasındadır. Köy meydanındaki çınar ağacının altında içilen bir bardak yerel rakı ve taze mezelerin tadı, Bodrum'un turistik koşturmacasından tamamen farklı bir dünya sunar.",
    'de': "Mazıköy in Bodrum's hinterland is among the peninsula's most genuine rural stops with its traditional taverns and sweeping olive groves. A glass of local raki and fresh mezze under the plane tree in the village square offers a world completely different from Bodrum's touristy hustle.",
    't': "Köy mezehanelerine öğleden sonra gelin; yerel halk o saatte toplanır ve en taze mezeler hazırdır.",
    'te': "Come to the village taverns in the afternoon; locals gather then and the freshest mezze are ready."},

25: {'d': "Bodrum'un karşısında yükselen Orak Adası, Ege'nin en berrak sularına ev sahipliği yapmasıyla dalış ve şnorkel tutkunlarının uğrak noktasıdır. Adanın güney koylarındaki 15-20 metre derinlikte bile dipte yüzen balıkları çıplak gözle izleyebildiğiniz bu şeffaf sulara bir kez girince adayı bırakmak zorlaşır.",
    'de': "Rising opposite Bodrum, Orak Island hosts the Aegean's clearest waters and is the go-to destination for diving and snorkeling enthusiasts. In the southern coves, the waters are so transparent that fish swimming at 15-20 metres depth are visible to the naked eye — once you enter these waters, leaving becomes difficult.",
    't': "Adaya yalnızca özel tekne ya da günlük tur tekneleriyle ulaşılır; Bodrum'dan hareket eden sabah turları en uygun seçenek.",
    'te': "The island is only accessible by private boat or day-tour boats; morning tours departing from Bodrum are the most convenient option."},

26: {'d': "Karaada (Siyah Ada), Bodrum açıklarındaki bu çarpıcı volkanik ada, içindeki doğal kara çamur kaplıcalarıyla ünlüdür. Çamura bulanan ziyaretçiler birkaç dakika bekledikten sonra denizde durulanır ve cilt görünür biçimde canlanır; bu nedenle ada yüzyıllardır kaplıca tedavisine gelenler için kutsaldır.",
    'de': "Karaada (Black Island), this striking volcanic island off Bodrum is famous for its natural black mud thermal baths inside a cave. Visitors coat themselves in mud, wait a few minutes, then rinse in the sea — the skin visibly revives, which is why the island has been sacred to spa-seekers for centuries.",
    't': "Beyaz kıyafet giymeyin; çamur lekeleri çıkmaz. Ada turları genellikle öğleden önce kalkıp akşam döner.",
    'te': "Don't wear white clothing as mud stains are permanent. Island tours typically depart before noon and return by evening."},

27: {'d': "Bodrum yarımadasının sakin batı koylarından biri olan Cennet Koyu, adını tam hak ediyor. Kristal berraklığındaki sığ suları ve gölge veren zeytinlikleriyle koy, tekne çıpası ya da sahil şezlongu deneyimini en doğal hâliyle yaşatır.",
    'de': "Cennet Koyu (Heaven Cove) on Bodrum peninsula's quiet western bays fully deserves its name. With crystal-clear shallow waters and shading olive trees, the cove offers the boat-anchor or beach-lounger experience in its most natural form.",
    't': "Koy, yaz zirvesinde bile görece sakin kalır; sabah 10'dan önce gelip günü tam kullanın.",
    'te': "The cove stays relatively peaceful even at summer peak; arrive before 10am and make the most of the full day."},

29: {'d': "Yalıkavak'ın dönüşümünün sembolü olan bu marina, dünyanın dört bir yanından gelen mega yatları demirleyen yüzer iskelesiyle Türkiye'nin en prestijli deniz üsleri arasına girmiştir. Marifetli restoranlar, uluslararası tasarım butikleri ve akşamları yat ışıklarının denize yansımasıyla marinada yürüyüş tek başına bir deneyimdir.",
    'de': "The symbol of Yalıkavak's transformation, this marina has earned its place among Turkey's most prestigious maritime bases with its floating pier hosting mega yachts from around the world. Skilled restaurants, international design boutiques, and the reflection of yacht lights in the evening water make a marina stroll a complete experience on its own.",
    't': "Akşam 19-21 arası marina en canlı halini yaşar; yat sahipleri güverteye çıkar, restoranlar dolmaya başlar.",
    'te': "Between 7 and 9pm the marina is at its liveliest; yacht owners emerge on deck and restaurants begin to fill."},

33: {'d': "Bodrum'un efsanevi bar sokağı üzerindeki Kule Rock City, her yaz sezonunda dünyaca tanınan DJ'lerin sahne aldığı açık hava sahnesiyle gece hayatının kalbi haline gelir. Yüzde yüz Türkiye yapımı konser atmosferiyle elektronik müzik tutkunlarının Ege'deki adresi bu mekan.",
    'de': "On Bodrum's legendary bar street, Kule Rock City becomes the heart of nightlife each summer season with its open-air stage hosting world-renowned DJs. One hundred percent Turkish-made concert atmosphere makes this venue the Aegean address for electronic music enthusiasts.",
    't': "Yoğun sezon biletleri gün içinde satılır; etkinlik takvimini önceden takip edin ve erken bilet alın.",
    'te': "High-season tickets sell out during the day; follow the event calendar in advance and buy early."},

35: {'d': "Bodrum'un en seçkin plaj kulüplerinden biri olan Nikki Beach, Maldivler'e özgü şezlong dizileri, sonsuzluk havuzu ve canlı DJ performanslarıyla lüks plaj deneyimini Ege'ye taşıyor. Papalardaki İtalyan usulü aperitifler ve özel kabin rezervasyonuyla güneş banyosunu şölenin merkezine dönüştürür.",
    'de': "One of Bodrum's most exclusive beach clubs, Nikki Beach brings the luxury beach experience to the Aegean with its Maldives-style lounger rows, infinity pool, and live DJ performances. Italian-style aperitifs and private cabana reservations make sunbathing the center of a celebration.",
    't': "Önceden kabin ya da masa rezervasyonu yapmadan gelmek yaz zirvesinde neredeyse imkânsız; en az 2 hafta önceden ayırtın.",
    'te': "Coming without a cabana or table reservation in the summer peak is almost impossible; book at least 2 weeks in advance."},

36: {'d': "Bodrum'un sakin Bitez körfezi kıyısındaki Lucca Beach, şezlong ve şemsiyesiyle aile dostu bir plaj atmosferi sunarken akşam saatlerinde düzenli olarak canlı müzik etkinliklerine ev sahipliği yapar. Koyun korunaklı yapısı yelkenli sörfü için de Ege'nin en uygun noktalarından biridir.",
    'de': "On the shores of Bodrum's tranquil Bitez bay, Lucca Beach offers a family-friendly beach atmosphere with sun loungers and umbrellas while hosting regular live music events in the evenings. The sheltered shape of the bay also makes it one of the Aegean's best spots for windsurfing.",
    't': "Bitez körfezi öğleden sonra batı rüzgarı alır; windsurf ekipmanı kiralama noktaları plajın her iki ucundadır.",
    'te': "Bitez bay receives westerly winds in the afternoon; windsurfing equipment rental points are at both ends of the beach."},

42: {'d': "Bodrum liman kenarındaki Gemibaşı, balıkçı tekne atmosferini ile lokantasını aynı çatı altında buluşturan bir Bodrum klasiğidir. Sabah erken saat avından gelen lüfer, çupra ve levrek burada mangal ya da zeytinyağlı tava olarak tabağa gelir; deniz rüzgarı eşliğinde yenen taze balık bu mekanı sezon boyunca dolu tutar.",
    'de': "Gemibaşı on Bodrum's harbor front is a Bodrum classic that brings the fishing boat atmosphere together with its restaurant under one roof. Bluefish, sea bream, and sea bass from the early morning catch arrive here grilled or pan-fried in olive oil; fresh fish eaten in the sea breeze keeps this place full throughout the season.",
    't': "Balık seçimi için erken gelin; servis ekibine günün en taze geleni sorun ve porsiyonun büyüklüğünü önceden öğrenin.",
    'te': "Come early to choose your fish; ask the service team what came in freshest today and check portion sizes in advance."},

43: {'d': "Bodrum'un en seçkin deniz ürünleri restoranlarından Orfoz, körfeze nazır terasıyla sezon boyunca ayrımını koruyan bir adrestir. Şeftali koyu kalamarı, ıstakoz ve taze balıktan oluşan menüsü kadar kapsamlı yerel şarap listesi de mekanı sıradan balık lokantalarından bir üst basamağa taşır.",
    'de': "Among Bodrum's most refined seafood restaurants, Orfoz maintains its seasonal distinction with a terrace facing the bay. A menu featuring Şeftali Cove calamari, lobster, and fresh fish alongside an extensive local wine list elevates it a tier above ordinary fish restaurants.",
    't': "Akşam rezervasyonu için en az 2-3 gün önceden arayın; körfez manzaralı masa talepleri önceliklidir.",
    'te': "Call at least 2-3 days ahead for an evening reservation; requests for a bay-view table are prioritized."},

44: {'d': "Bodrum yarımadasının doğal güzelliğini mutfağa taşıyan ENT Restaurant, deniz manzaralı terasında Ege otlu peynirlerini, yerel balıkları ve kendi bahçesindeki otlarla tatlandırılmış mezeleri sunar. Bodrum'un modern gastronomik sahnesinin öne çıkan adreslerinden biri olarak yerel tatlarla yaratıcı yorumları bir arada bulabilirsiniz.",
    'de': "ENT Restaurant brings the natural beauty of the Bodrum peninsula into the kitchen, serving Aegean herb cheeses, local fish, and mezze seasoned with its own garden herbs on its sea-view terrace. As one of Bodrum's prominent modern gastronomic addresses, you can find local flavors alongside creative interpretations.",
    't': "Menüdeki Ege ot koleksiyonu haftalık değişir; güncel seçenekler için garsondan yardım isteyin.",
    'te': "The Aegean herb collection on the menu changes weekly; ask the waiter for the current options."},

45: {'d': "Bodrum'un liman tarafındaki Miam, hem sıradan bir kahve molası hem de akşam yemeği için geçerli kılan esnek menüsü ve sahil bölgesindeki en geniş açık terası ile her saatte insanlarla dolup taşan bir mekan. Taze sıkılmış mandalina suyu ve limonlu tart, sabah kahvaltısının favorilerinden.",
    'de': "Located on Bodrum's harbor side, Miam fills with people at every hour thanks to its flexible menu suitable for both a simple coffee break and a dinner, and the widest open terrace in the seafront area. Freshly squeezed tangerine juice and lemon tart are favorites at the morning breakfast.",
    't': "Öğlen ve akşam arasında sakin bir pencere var; 15-18 arası en az kalabalık ve en rahat zamandır.",
    'te': "There is a quiet window between lunch and dinner; between 3 and 6pm is the least crowded and most comfortable time."},

46: {'d': "Yalıkavak Marina'nın prestijli adreslerinden biri olan Zuma Bodrum, Japon-Brezilya mutfağını temsil eden dünya markasının Türkiye'deki en büyük lokasyonudur. Robata ızgaraları ve sushi seçenekleri kadar dikkat çeken canlı müzik programı ve su üstü terası, Zuma'yı marinada bir gece için biçilmiş kaftana dönüştürür.",
    'de': "One of Yalıkavak Marina's prestigious addresses, Zuma Bodrum is the largest Turkish location of the world brand representing Japanese-Brazilian cuisine. The live music program and over-water terrace are as striking as the robata grills and sushi selections, making Zuma the perfect choice for a marina night.",
    't': "Sezon zirvesinde akşam yemeği için en az bir hafta önceden rezervasyon şart; happy hour için erken gelip bar tarafını tercih edin.",
    'te': "An evening dinner reservation at least a week in advance is essential at peak season; arrive early for happy hour and opt for the bar side."},

48: {'d': "Gümüşlük'ün huzurlu körfez kıyısında, taşların üzerine oturarak yemek yenilen masalarıyla hayran bırakan Limon Restaurant, denizin içinden geçen tek yolun sonunda saklanan bu sakin köyü daha da büyülü kılar. Taze balık ve Ege meze çeşitleri, Gümüşlük akşamlarının saadetini tamamlar.",
    'de': "On the tranquil bay shore of Gümüşlük, Limon Restaurant enchants with its tables placed on rocks where you dine literally at the water's edge, making the quiet village at the end of the single road crossing through the sea even more magical. Fresh fish and Aegean mezze complete the bliss of Gümüşlük evenings.",
    't': "Akşam saat 19-20 için önceden rezervasyon yapın; en iyi kaya masaları saatler öncesinde talep edilir.",
    'te': "Book in advance for 7-8pm; the best rock tables are claimed hours ahead."},

49: {'d': "Bodrum'un yerel gastronomi tutkunlarının yıllardır bağlı olduğu Melengeç Balık, günlük piyasa balığına göre şekillenen kısa menüsü ve büyük porsiyonlarıyla kendine özgü bir düşük profilli şöhret inşa etmiştir. Ismarladığınız balığın tazesini seçmek için açık buzdolabı önünde durmak buradaki geleneksel ritüeldir.",
    'de': "Melengeç Balık, to which Bodrum's local gastronomy enthusiasts have been loyal for years, has built its own understated fame with its short daily market-fish menu and generous portions. Standing before the open cold cabinet to personally select the freshest fish you ordered is the traditional ritual here.",
    't': "Balık fiyatları kiloya göre değişir; sipariş vermeden önce fiyat sorun. Mevsim dışı ziyarette açık olup olmadığını önceden kontrol edin.",
    'te': "Fish prices vary by weight; ask before ordering. For an off-season visit, check in advance whether it is open."},

50: {'d': "Dereköy'ün sakin zeytin bahçeleri arasına kurulmuş bu köy lokantası, şehrin gürültüsünden kaçmak isteyenlere çiğ köfte, taş fırın pide ve köy kahvaltısı sunuyor. Sac kavurmasındaki Ege otları ve ev yapımı yoğurt, yarımadanın dağ mutfağını keşfetmek için mükemmel bir başlangıç noktasıdır.",
    'de': "Set among the tranquil olive groves of Dereköy, this village restaurant offers çiğ köfte, stone-oven pide, and village breakfast to those escaping the city's noise. Aegean herbs in the sac kavurma and homemade yogurt make it an excellent starting point for discovering the peninsula's mountain cuisine.",
    't': "Sabah 8-11 arası köy kahvaltısı için geleneğe dönüşmüş; saatlerce oturup dinlenmek isteyenler için ideal bir gün başlangıcıdır.",
    'te': "Visiting between 8 and 11am for village breakfast has become traditional here; it is the ideal start to a day for those wanting to sit and unwind for hours."},
}

apply_batch('bodrum.json', U)
