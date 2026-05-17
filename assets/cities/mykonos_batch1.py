import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
0: {'t': "Gün batımını izlemek için Little Venice restoranlarından birinde önceden masa rezervasyonu yapın; en iyi cephe masaları günler öncesinden dolar.",
    'te': "Book a table at one of the Little Venice restaurants in advance to watch sunset; the best front-row tables fill days ahead."},

1: {'d': "Mykonos'un ikonası olan bu altı yel değirmeni, 16. yüzyıldan bu yana adasının siluetini tanımlamaktadır. Bembeyaz badanalı gövdeleri, hasır çatıları ve arkalarında yükselen Mykonos kasabasıyla gün batımı saatinde dünyanın en çok fotoğraflanan manzaralarından birini oluştururlar.",
    'de': "These six iconic windmills have defined the silhouette of Mykonos since the 16th century. Their whitewashed bodies, thatched roofs, and the Mykonos town rising behind them create one of the world's most photographed sunset scenes.",
    't': "Gün batımından 45 dakika önce değirmenlerin önüne gidin; her yıl binlerce fotoğrafçı aynı noktada toplanır, erken gelin.",
    'te': "Arrive at the windmills 45 minutes before sunset; thousands of photographers gather at the same spot each year, so arrive early."},

6: {'d': "Mykonos kasabası, yani Hora, dar labirent sokakları, pelikan sakinleri ve bembeyaz kubbeleriyle Kikladlar mimarisinin en saf ve en fotoğrafenik temsilcisidir. Araplıkların arkasında saklanan küçük kiliseler ve mavi kapılı evler, her kıvrımda yeni bir keşfin kapısını aralar.",
    'de': "Mykonos Town, or Hora, is the purest and most photogenic representative of Cycladic architecture with its labyrinthine narrow lanes, pelican residents, and gleaming white domes. Small churches hidden behind laundry lines and houses with blue doors open a new discovery at every turn.",
    't': "Sokaklar kasıtlı olarak düzensiz yapılmıştır; haritaya bağlı kalmayın, kaybolmak buradaki en güzel keşfin kendisidir.",
    'te': "The streets were intentionally designed to be irregular; don't rely on a map — getting lost is itself the best discovery here."},

8: {'d': "Mykonos'un eski limanı Hora Limanı, küçük beyaz balıkçı teknelerinin rıhtıma yanaştığı, kahve içen yerel yaşlıların ve yoğun sezon turistlerinin iç içe geçtiği canlı bir alandır. Sabahın erken saatlerinde balıkçılar avlarını sergilediğinde liman, gerçek Mykonos yaşamını en yalın biçimiyle sunar.",
    'de': "Mykonos Old Port, or Hora Harbor, is a lively area where small white fishing boats dock, coffee-drinking local elders and peak-season tourists intermingle. In the early morning when fishermen display their catch, the harbor presents real Mykonos life in its most unfiltered form.",
    't': "Sabah 06:30-08:00 arası limana gidin; taze balık satışı ve gerçek balıkçı atmosferi için en doğru saatlerdir.",
    'te': "Visit the harbor between 6:30 and 8am for fresh fish sales and the most authentic fisherman atmosphere."},

12: {'t': "Plaj kulübüne sabah 10:00 öncesi gelin; öğleden sonra tüm masalar dolu olur. Yüksek sesli müzik sabah 11'den itibaren başlar, sakin bir gün planlayanlar için uygun değil.",
     'te': "Arrive at the beach club before 10am; all tables are full by the afternoon. Loud music starts from 11am, not suitable for those planning a quiet day."},

14: {'d': "Psarou Plajı'na nazır konumuyla Nammos, dünyaca tanınan marka restoranlar arasındaki Mykonos temsilcisidir. Denize sıfır şezlongları, kendi şarap mahzeni ve balık buğlamasından taze sashimiye uzanan menüsüyle lüks plaj gastronomi deneyimini Ege'de zirveye taşır.",
    'de': "Overlooking Psarou Beach, Nammos is the Mykonos representative among world-renowned brand restaurants. With its sea-level sun loungers, its own wine cellar, and a menu stretching from steamed fish to fresh sashimi, it elevates the luxury beach gastronomy experience to its peak in the Aegean."},

16: {'d': "Mykonos'un efsanevi JackieO' Beach Club'ı, LGBTQ+ dostu kimliği, canlı drag performansları ve muhteşem Super Paradise Plajı kıyısındaki konumuyla adanın en özgür ve en renkli gündüz-gece adresi olarak uluslararası üne kavuşmuştur.",
    'de': "Mykonos's legendary JackieO' Beach Club has earned international fame as the island's most liberated and colorful day-to-night address with its LGBTQ+-friendly identity, live drag performances, and location on the stunning Super Paradise Beach."},

17: {'d': "Psarou Plajı kıyısındaki Principote, el yapımı İtalyan makarnasını Mykonos günbatımı manzarasıyla buluşturan rafine bir Akdeniz restoranıdır. Şnorkel yaparak yüzdükten sonra şezlongta kuruyan plaj ziyaretçilerinden, akşam yemeğine gelenlerden oluşan çeşitli müdavim kitlesiyle sezon boyunca hareketlidir.",
    'de': "On Psarou Beach, Principote is a refined Mediterranean restaurant that pairs handmade Italian pasta with Mykonos sunset views. Lively throughout the season with a diverse regular clientele from beach visitors drying off sun loungers after snorkeling to evening diners."},

18: {'d': "Ftelia Plajı'nın kuzey kıyısında rüzgara açık bir konumda yer alan Alemagou, Mykonos'un en sanatsal ve en alternatif sahil deneyimlerinden birini sunar. Eski ahşap tekne malzemelerinden yapılmış mobilyaları, özenle seçilmiş müziği ve ufuk çizgisine bakan terasyıyla Mykonos'un kalabalık güney plajlarına alışkın olanlara bambaşka bir his yaşatır.",
    'de': "Located on the north shore of Ftelia Beach facing the open wind, Alemagou offers one of Mykonos's most artistic and alternative beach experiences. With furniture crafted from old boat timber, carefully curated music, and a terrace facing the horizon, it delivers a completely different feeling to those accustomed to Mykonos's crowded southern beaches."},

21: {'t': "Ornos plajı Mykonos'un en aile dostu sahillerinden biridir; sığ ve sakin sularıyla çocuklar için güvenlidir. Plajın sol ucundaki küçük restoran sezonun en uygun fiyatlı balık öğünlerinden birini sunar.",
     'te': "Ornos beach is one of Mykonos's most family-friendly shores; shallow and calm waters make it safe for children. The small restaurant at the left end of the beach offers one of the season's most affordable fish meals."},

28: {'d': "Kayalıklara oyulmuş adeta saklı bir mağara restoranı olan Spilia, büyük gruplar için kolayca keşfedilemeyen gizli bir deniz deneyimi sunar. Yemek masaları dalgaların çarptığı kayalıkların hemen üzerinde kurulmuştur; deniz ürünleri ve yerel Yunan mezeleri, gürleyen Ege sesiyle birlikte ikiye katlanır.",
    'de': "Spilia, carved into the rocks like a hidden cave restaurant, offers a secret sea experience not easily discovered by large groups. Dining tables are set just above the rocks where waves crash; seafood and local Greek mezze double in flavor accompanied by the roar of the Aegean."},

33: {'d': "Mykonos kasabasının kalbindeki m-eating, yerel şarap sandviçlerinden modern Yunan deniz ürünleri tabağına kadar geniş bir menüyle kasabaya özgü samimi bir restoran deneyimi sunar. Ufak kapasiteli iç mekanı ve taş duvarlı dekorasyonuyla kasabanın en içten gelen mutfak durağından biridir.",
    'de': "At the heart of Mykonos town, m-eating offers a sincere restaurant experience unique to the town with a wide menu from local wine sandwiches to modern Greek seafood plates. With its small-capacity interior and stone-walled decoration, it is one of the town's most heartfelt culinary stops."},

35: {'d': "Uluslararası Beefbar zincirinin Mykonos kolu, tanınan Wagyu ve Black Angus et menüsünü Yunanistan'ın en popüler adasına taşımıştır. Beyaz taş mimarisi içindeki çarpıcı siyah-altın iç mekan tasarımı ve Marina yakınındaki konumuyla klasik Mykonos beyazından ayrışan kendine özgü bir atmosfer sunar.",
    'de': "The Mykonos branch of the international Beefbar chain has brought its renowned Wagyu and Black Angus meat menu to Greece's most popular island. Its striking black-and-gold interior design within white stone architecture and proximity to the Marina offer a uniquely distinct atmosphere that sets it apart from classic Mykonos white."},

40: {'d': "Mykonos kasabasına hakim konumuyla Zuma'nın Yunanistan ayağı, klasik Japon-Brezilya menüsünü adadan izlenen Ege manzarasıyla buluşturur. Robata ızgarasından çıkan wagyu dilimi ve ponzu soslu sashimi, dünyanın her köşesinden gelen üst segment turist profiline hitap eden sezonun en prestijli masalarındandır.",
    'de': "With its commanding position over Mykonos town, the Greek outpost of Zuma pairs its classic Japanese-Brazilian menu with Aegean views from the island. A wagyu slice from the robata grill and sashimi with ponzu sauce are among the season's most prestigious tables, catering to high-end tourists from every corner of the world."},

43: {'d': "Mykonos'un en iyi günbatımı barlarından biri olan 180° Sunset Bar, Hora kasabasının yüksek bir noktasından Ege'yi ve Delos adasının siluetini tam 180 derece panoramada sunar. El yapımı Yunan kokteylleri ve denize doğru uzanan terasıyla burada geçirilen altın saat, günün en akılda kalıcı anına dönüşür.",
    'de': "One of Mykonos's best sunset bars, 180° Sunset Bar presents the Aegean and the silhouette of Delos island in a full 180-degree panorama from a high point of Hora town. With handcrafted Greek cocktails and a terrace reaching toward the sea, the golden hour spent here becomes the day's most memorable moment.",
    't': "Rezervasyon zorunludur; günbatımı masaları saatler öncesinde doluyor. Erken gelip kokteyl saatini balkon masasında başlatın.",
    'te': "A reservation is essential; sunset tables fill hours in advance. Arrive early and start cocktail hour at the balcony table."},

48: {'d': "1978'den bu yana Mykonos bar sahnesinin en köklü eğlence mekanlarından biri olan Skandinavian Bar, yetkilendirilen DJ'leri, tematik geceleri ve adanın en canlı içki atmosferiyle her milliyetten ziyaretçinin buluşma noktasıdır. Geç saatte şehrin en ünlü kulüpleri açılmadan önce ısınma turu için biçilmiş kaftan.",
    'de': "One of the most established entertainment venues on the Mykonos bar scene since 1978, Skandinavian Bar is the meeting point for visitors of every nationality with its licensed DJs, themed nights, and the island's liveliest drink atmosphere. The perfect warm-up stop before the island's most famous clubs open late in the night.",
    't': "Gece 23:00-01:00 arası en kalabalık saatler; bu saatler öncesinde gelirseniz daha rahat bir yer bulabilirsiniz.",
    'te': "The busiest hours are between 11pm and 1am; if you arrive before these hours you can find a more comfortable spot."},

49: {'d': "Mykonos kasabasının merkezindeki Breeze Cocktail Bar, şık dekorasyonu ve özenle hazırlanan imza kokteylleriyle kasabanın en seçkin bar adreslerinden biridir. Gün batımından gece yarısına uzanan seansları, hem romantik çift akşamları hem de arkadaş grubu buluşmaları için ideal bir köşe sunar.",
    'de': "Breeze Cocktail Bar in the center of Mykonos town is one of the town's most distinguished bar addresses with its elegant décor and carefully crafted signature cocktails. Its sessions stretching from sunset to midnight offer an ideal corner for both romantic couples' evenings and friend group gatherings.",
    't': "Mekanın imza içkisi olan 'Aegean Breeze'yi deneyin; adaya özgü yerel likörlerle hazırlanan sınırlı üretim bir kokteyldir.",
    'te': "Try the venue's signature drink 'Aegean Breeze'; it is a limited-production cocktail prepared with local liqueurs unique to the island."},

55: {'d': "Hora kasabasının korunaklı sokaklarında saklanan bu küçük Ortodoks kilisesi, mavi kubbeli çan kulesi ve bembeyaz badanalı duvarlarıyla Kiklad mimarisinin en fotoğrafenik köşelerinden birini oluşturuyor. Turist kalabalığının girip çıktığı tanınmış kiliselerin aksine burası, sakin ve samimi bir ibadet atmosferini korur.",
    'de': "Hidden in the sheltered streets of Hora town, this small Orthodox church forms one of the most photogenic corners of Cycladic architecture with its blue-domed bell tower and gleaming whitewashed walls. Unlike the well-known churches with tourist crowds flowing in and out, it maintains a quiet and sincere atmosphere of worship.",
    't': "Kapı sabah erken ve akşam ayini saatlerinde açık; içeri girerken sessiz olun ve fotoğraf çekmeden önce izin isteyin.",
    'te': "The door is open in the early morning and at evening service time; be silent when entering and ask permission before taking photos."},

56: {'d': "Little Venice mahallesinin Alefkandra manzarası, Mykonos'un en romantik perspektiflerinden biridir. Dalgaların balkona inen renkli evlere çarptığı bu manzara, güneşin Ege'ye battığı anlarda pembe-altın tonlarıyla dünyanın en tanınan ada günbatımı fotoğraflarından birini oluşturur.",
    'de': "The Alefkandra view of Little Venice neighborhood is one of Mykonos's most romantic perspectives. This view of waves crashing against colorful balconied houses, in pink-gold tones as the sun sets into the Aegean, forms one of the world's most recognized island sunset photographs.",
    't': "En iyi açı için Kastro bölgesindeki küçük çıkıntıdan ya da yakın bir kafenin dış terasından bakın.",
    'te': "For the best angle, look from the small outcrop in the Kastro area or from the outdoor terrace of a nearby café."},

60: {'d': "Mykonos'un feribot ve kruvaziyer gemilerine hizmet eden yeni limanı, Hora'nın hareketli balıkçı limanından farklı olarak günlük binlerce yolcunun geçtiği lojistik bir merkezdir. Liman çevresinde oluşan taze balık pazarı ve kahvaltı kafeleri, sezon boyunca sabahın erken saatlerinde canlı bir hava yaratır.",
    'de': "The new harbor of Mykonos serving ferries and cruise ships is, unlike Hora's lively fishing harbor, a logistical center through which thousands of daily passengers pass. A fresh fish market and breakfast cafés forming around the harbor create a lively atmosphere in the early morning hours throughout the season.",
    't': "Feribot saatlerinde liman çevresi çok kalabalıklanır; gelişlerde ve gidişlerde en az 30 dakika önceden orada olun.",
    'te': "The harbor area gets very crowded at ferry times; be there at least 30 minutes before arrivals and departures."},

62: {'d': "Mykonos'un kayalık kıyısında suyun üzerine uzanan Cavo Tagoo, bütünleşik havuzu ve cam kenarları sayesinde denizle birleşen otel mimarisinin en çarpıcı örneklerinden biridir. Gündüz otel havuzu bir plaj kulübüne dönüşür; günbatımında ise manzara, Yunan adalarının en dramatik ufuk çizgilerinden birini sunar.",
    'de': "Cavo Tagoo extending over the rocky Mykonos coastline is one of the most striking examples of hotel architecture that merges with the sea thanks to its integrated pool and glass edges. During the day the hotel pool transforms into a beach club; at sunset the view presents one of the Greek islands' most dramatic horizon lines."},

65: {'d': "Mykonos kasabasının arka sokaklarına saklanmış bu küçük meyhane, ev yapımı mezeler, taze balık ızgaraları ve meze-rakı geleneğini modern Mykonos gürültüsünden arındırılmış sade bir mekanda yaşatır. Yerli nüfusun sık uğradığı burada turistler azınlıktır, bu da onu kasabanın en özgün köşelerinden biri yapar.",
    'de': "This small tavern hidden in Mykonos town's back streets preserves the mezze-raki tradition with homemade mezze and fresh grilled fish in a simple venue stripped of modern Mykonos noise. Locals frequent it often and tourists are a minority, making it one of the town's most genuine corners."},

67: {'d': "Adının İtalyancası 'balık tezgahı' anlamına gelen bu küçük balıkçı dükkânı ve mini restoran, sabah erken saatlerde tekne ile gelen taze ürünleri hem satıyor hem de pişiriyor. Paketleme olmadan orada yenilen ızgara sardalya ve ahtapot salatası, Mykonos'un en ucuz ve en özgün deniz ürünleri deneyimine kapı aralar.",
    'de': "This small fishmonger shop and mini-restaurant, whose Italian name means 'fish counter,' both sells and cooks fresh produce arriving by boat in the early morning. Grilled sardines and octopus salad eaten on the spot without packaging opens the door to Mykonos's cheapest and most authentic seafood experience."},

68: {'d': "Agios Ioannis Plajı kıyısındaki Hippie Fish, Mykonos'ta yıllar içinde kendi sadık kitlesini oluşturmuş, hem plaj kulübü hem de Akdeniz deniz ürünleri restoranı kimliğine sahip özgün bir mekan olarak öne çıkıyor. Rengarenk Bohem dekorasyonu ve adadan ilham alan kokteyl listesiyle sakin bir öğle yemeği için idealdir.",
    'de': "On the shores of Agios Ioannis Beach, Hippie Fish stands out as a unique venue with both a beach club and Mediterranean seafood restaurant identity that has built its own loyal clientele in Mykonos over the years. With its colorful Bohemian décor and island-inspired cocktail list, it is ideal for a relaxed lunch."},

69: {'d': "İtalyan usulü ev yapımı makarna ve pizzasıyla Mykonos'un en samimi İtalyan mutfağı deneyin sunan Arte Italiana, turistik kasabada otantik lezzetlerin hâlâ ayakta tutulabildiğini kanıtlıyor. Günlük hazırlanan tagliatelle ve tahta fırından çıkan pizza, burayı yılın dört mevsimi ziyaret edilen bir yer hâline getiriyor.",
    'de': "Offering Mykonos's most sincere Italian cuisine experience with homemade Italian-style pasta and pizza, Arte Italiana proves that authentic flavors can still be sustained in a touristic town. Daily prepared tagliatelle and pizza from a wood-fired oven make it a year-round visited destination."},

73: {'d': "Mykonos kasabasının sakin bir köşesindeki Alegro, küçük kapasiteli terasıyla günlük piyasa tazeliğinde mezeleri ve yerel deniz ürünlerini kasabanın yüksek fiyatlı restoranlarının çok altında sunan gizli bir değerdir. Düzenli müdavim kitlesi, menünün her gün değişen özel yemek tahtasını takip etmek için tekrar tekrar gelir.",
    'de': "Alegro in a quiet corner of Mykonos town is a hidden value that serves daily market-fresh mezze and local seafood far below the town's high-priced restaurants on its small-capacity terrace. Its regular clientele returns again and again to follow the daily changing special dishes board."},

74: {'d': "Mykonos kasabasının dar sokaklarındaki Kalita, Kikladlar ev yemeklerini yabancı ziyaretçilere doğru anlatma misyonuyla yola çıkmış bir aile restoranıdır. Anneden öğrenilen domatesli fırın patlıcan ve keçi peynirli börek, mutfağın büyükannenin tarifi izlenerek pişirildiğini hissettiriyor.",
    'de': "Kalita in the narrow streets of Mykonos town is a family restaurant that set out with the mission of correctly conveying Cycladic home cooking to foreign visitors. Oven-baked eggplant with tomato and goat cheese börek learned from mother make you feel that the kitchen follows grandmother's recipe."},

75: {'d': "Küçük boyutuna rağmen Mykonos kasabasında yıllardır var olup söz sahibi olan Lucky Fish, taze adet balığı ve günlük seçilen balık mezesiyle yüksek fiyatlar yerine gerçek lezzeti öne çıkaran bir mekan olarak öne çıkıyor. Küçük masa kapasitesi nedeniyle bekleme listesi kısa sürede doluyor.",
    'de': "Despite its small size, Lucky Fish has been a voice in Mykonos town for years, standing out as a venue that prioritizes real flavor over high prices with fresh single-portion fish and daily selected fish mezze. Its small table capacity means the waiting list fills up quickly."},

76: {'d': "Hora kasabasının ticari merkezine yakın ama kalabalığın biraz dışında kalan Kazarma, yerel soğuk aperatifler, mezeler ve taze deniz ürünleri tabaklarıyla hem öğle hem akşam ziyaretine uygun rahat bir Yunan bistro deneyimi sunuyor.",
    'de': "Close to the commercial center of Hora but slightly away from the crowds, Kazarma offers a comfortable Greek bistro experience suitable for both lunch and dinner visits, with local cold aperitifs, mezze, and fresh seafood plates."},
}

apply_batch('mykonos.json', U)
