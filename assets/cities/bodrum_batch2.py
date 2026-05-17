import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
51: {'d': "İtalyan Michelin yıldızlı şef Stefano Ciotti imzasını taşıyan bu trattoria, Yalıkavak Marina'nın en şık restoranları arasında yerini almıştır. El açması makarna, deniz taralası risotto ve Calabria'dan getirilen malzemelerle hazırlanan antipasto tabakları, İtalyan ev mutfağının zarafetiyle Bodrum'da buluşur.",
    'de': "Bearing the signature of Italian Michelin-starred chef Stefano Ciotti, this trattoria has secured its place among Yalıkavak Marina's most stylish restaurants. Hand-rolled pasta, scallop risotto, and antipasto plates prepared with ingredients imported from Calabria bring the elegance of Italian home cooking to Bodrum."},

54: {'d': "İbiza ve Monaco'dan Bodrum'a taşınan Bagatelle, Yalıkavak Marina'nın en iddialı Fransız-Akdeniz mutfağı temsilcisidir. Fransız şampanyası eşliğinde yüksek sesle çalınan funk müzik, günbatımından sonra masaları dans pistine dönüştürür; bu mekan hem restoran hem de gece başlangıç noktasıdır.",
    'de': "Transplanted from Ibiza and Monaco to Bodrum, Bagatelle is Yalıkavak Marina's boldest French-Mediterranean cuisine representative. Loud funk music paired with French champagne turns tables into a dance floor after sunset; this venue serves simultaneously as a restaurant and a night-starting point."},

61: {'d': "Bitez kıyısındaki METT Hotel & Beach Resort, günübirlikçilere de açık olan plaj kulübüyle Bodrum'un en tasarım odaklı sahil deneyimlerinden birini sunar. Şezlongların sıralandığı mermer döşemeli güverte, cam kenarlı havuz ve kabinlerdeki özel servis, Bodrum'un kuzey kıyısında lüks plaj tarifini yeniden yazıyor.",
    'de': "METT Hotel & Beach Resort on Bitez's shore offers one of Bodrum's most design-focused beach experiences with its beach club also open to day visitors. The marble-decked area lined with sun loungers, glass-edged pool, and private cabin service are rewriting the luxury beach definition on Bodrum's northern coast.",
    't': "Günübirlik masa rezervasyonu için en az 3-5 gün önceden arayın; yaz zirvesinde boş yer bulmak oldukça zordur.",
    'te': "Call at least 3-5 days ahead for a day-use table reservation; finding a free spot in peak summer is quite difficult."},

62: {'d': "Bodrum'un Bitez ilçesinde, sahil yolu üzerinde küçük bir dükkânda faaliyet gösteren bu dondurmacı, taze meyveyle yaptığı el yapımı Türk dondurmasıyla sezon boyunca kapısında kuyruk oluşturur. İncirli, sakızlı ve taze limonlu dondurma çeşitleri, Bodrum bölgesinin yerli meyvelerinden üretilir.",
    'de': "Operating in a small shop on Bitez's seafront road, this ice cream maker forms queues at its door throughout the season with handmade Turkish ice cream using fresh local fruit. Fig, mastic, and fresh lemon ice cream varieties are produced from the Bodrum region's own local fruits."},

63: {'d': "Bodrum esnafı ve yerel sakinlerin yıllarca bağlı kaldığı Sünger Pizza, kişisel boy pizza seçenekleri ve Türk damak zevkine uyarlanmış İtalyan malzemeleriyle yarımadanın en samimi pizza deneyin sunar. Açık döner fırını ve hamur işi kokusu, bu restoranı her yaştan insanın uğradığı bir toplantı noktasına dönüştürmüştür.",
    'de': "Sünger Pizza, to which Bodrum tradespeople and local residents have remained loyal for years, offers the peninsula's most sincere pizza experience with personal-size options and Italian ingredients adapted to Turkish palates. The open rotary oven and dough scent have turned this restaurant into a meeting point for people of all ages."},

65: {'d': "Bodrum'un Gündoğan kasabasındaki Etrim Halıcılık, Türkiye'nin el dokuma halı ve kilim geleneğini yaşatan, aynı zamanda modern tasarım anlayışıyla yorumlayan ender atölyelerden biridir. İpek halıların dokunuş süreci gözlemlenebilir; ustalar hem halının tarihini hem de motiflerin anlamını anlatır.",
    'de': "Etrim Halıcılık in Bodrum's Gündoğan district is one of Turkey's rare workshops that both preserves the hand-woven rug and kilim tradition and interprets it through a modern design sensibility. The weaving process of silk rugs can be observed while masters explain both the history and the meaning of the motifs.",
    't': "Üretim atölyesini önceden haber vererek ziyaret etmek mümkün; halı alışverişi planlamadan da gidilmeye değer bir yerdedir.",
    'te': "It is possible to visit the production workshop by giving advance notice; it is worth going even without plans to purchase a rug."},

66: {'d': "Bodrum yarımadasının en iyi korunmuş geleneksel köylerinden biri olan Sandıma (Dereköy), sarmaşıklı taş evleri, arnavut kaldırımlı sokakları ve köy meydanındaki çınar altında oturmaya davet eden hanıyla zamanın ağır aktığı bir atmosfer taşır. Çoğu zaman misafir yerine yerel köylüler bulunur.",
    'de': "One of the Bodrum peninsula's best-preserved traditional villages, Sandıma (Dereköy) carries an atmosphere where time flows slowly, with its ivy-covered stone houses, cobblestone streets, and a village inn beneath the plane tree in the square that invites you to sit. Most of the time you will find local villagers rather than tourists.",
    't': "Pazar sabahları köylüler taze sebze ve peynir satar; bu saatten daha gerçek bir köy deneyimi bulmak zordur.",
    'te': "On Sunday mornings villagers sell fresh vegetables and cheese; it is hard to find a more authentic village experience than at this hour."},

69: {'d': "Bodrum liman bölgesine yakın konumlanan Dream Inn, yat turları için çıkış noktasına adım mesafesindeki konumuyla hem konforlu bir konaklama hem de deniz aktiviteleri için pratik bir üs olarak işlev görür. Küçük havuzu ve akşam serinliğinde keyif verilen terasıyla merkezi fiyat aralığındaki en iyi değerler arasında gösterilir.",
    'de': "Located close to Bodrum's harbor district, Dream Inn serves both as comfortable accommodation and a practical base for maritime activities, just steps from the yachting departure point. Its small pool and terrace pleasant in the evening cool are among the best values in the mid-price range.",
    't': "Liman yakınlığı sabah erken tekne turlarına ulaşmayı kolaylaştırır; araç kiralamak istemeyenler için ideal konum.",
    'te': "Proximity to the harbor makes early-morning boat tour access easy; an ideal location for those who don't want to rent a car."},

73: {'d': "Bodrum körfezinin girişindeki bu tarihi fener, 19. yüzyıldan bu yana Ege'nin bu kıyısına gelen gemilere yol göstermiştir. Akşamları fener ışığının su yüzeyinde yaptığı yansıma ve çevresindeki sarı ışık döngüsü, seyir halindeki yatlara eşsiz bir görsellik katarken kara tarafından da fotoğrafçıların gözdesi.",
    'de': "This historic lighthouse at the entrance of Bodrum Bay has guided ships to this Aegean shore since the 19th century. The reflection of the lighthouse beam on the water surface in the evenings and the surrounding golden light cycle add a unique visual for passing yachts, while on the landward side it is a photographer's favorite.",
    't': "Fenere en güzel açıdan ulaşmak için Karada yolundaki taş patikayı takip edin; yürüyüş yaklaşık 20 dakikadır.",
    'te': "Follow the stone path on the Karada road for the best angle to reach the lighthouse; the walk is about 20 minutes."},

79: {'d': "Tarihin atasının ve dünya tarihçiliğinin kurucusu kabul edilen Herodotos, antik çağda Halikarnassos adıyla bilinen bugünkü Bodrum'da doğmuştur. Ana yol üzerindeki bu anıt, MÖ 5. yüzyılda yaşamış ve Anadolu, Mısır, Pers İmparatorluğu'nun tarihini kaleme almış bu büyük aklı hem yerel hem de küresel bir kültürel abide olarak yâd eder.",
    'de': "Herodotus, considered the father of history and founder of historical writing, was born in what is now Bodrum, then known as Halicarnassus in antiquity. This monument on the main road commemorates the great mind who lived in the 5th century BC and wrote the histories of Anatolia, Egypt, and the Persian Empire as both a local and global cultural landmark.",
    't': "Heykel yakınındaki bilgi tabelaları Türkçe ve İngilizce olarak mevcuttur; ziyarette beş dakikanızı bilgi tahtasına ayırın.",
    'te': "Information boards near the statue are available in Turkish and English; dedicate five minutes to the information board during your visit."},

80: {'d': "Bodrum'da özel tekne kiralamak; Kara Ada kaplıcaları, Orak Adası kristal suları ve Gökçebel Koyu'nun el değmemiş doğasını keşfetmenin en özgür yoludur. Tüm gün süren özel bir tekne turu, sabah 9'dan akşam 19'a kadar yaklaşık 4-5 kovaya uğrayan ve öğle yemekli bir sahil macerası anlamına gelir.",
    'de': "Renting a private boat in Bodrum is the freest way to discover the Kara Ada thermal baths, Orak Island's crystal waters, and the untouched nature of Gökçebel Cove. A full-day private boat tour means a coastal adventure from 9am to 7pm that stops at approximately 4-5 bays and includes lunch onboard.",
    't': "Tekne pazarlığını liman meydanında doğrudan kaptanlarla yapın; sabah 8'den önce varırsanız fiyatlar daha uygun olur.",
    'te': "Negotiate the boat deal directly with captains in the harbor square; arriving before 8am gives you better prices."},

82: {'d': "Bodrum liman bölgesindeki bu dövme stüdyosu, yıllardır marinaların yarım tonlu dağıttığı mavi-beyaz estetiğine karşılık ince çizgi ve suluboya tekniklerindeki uzmanlaşmasıyla öne çıkmıştır. Denizle bağlantılı, Ege esinli tasarımlar konusunda sanatçıyla önceden danışmak buradaki iyi pratiği oluşturur.",
    'de': "This tattoo studio in Bodrum's harbor district has stood out for years against the half-tone blue-and-white aesthetic of the marinas through its specialization in fine-line and watercolor techniques. Consulting the artist in advance about sea-related and Aegean-inspired designs constitutes the good practice here.",
    't': "Seans öncesi randevu zorunludur; özellikle Temmuz-Ağustos döneminde randevu almak için 2-3 hafta önceden yazmak gerekebilir.",
    'te': "An appointment before the session is mandatory; especially in July-August, writing 2-3 weeks in advance may be necessary to secure one."},

84: {'d': "Bodrum'un marina ile eski liman arasını birleştiren bu yürüyüş güzergahı, akşamları salınım yapan yatlar, kafeler ve dondurma arabalarıyla dolup taşar. Sahil şeridini boydan boya yürümek, hem kaleye uzanan en iyi manzarayı sunar hem de Bodrum'un gece çıkan sosyal sahnesini gözlemlemek için mükemmel bir tutur.",
    'de': "This walkway connecting Bodrum's marina with the old harbor fills with swaying yachts, cafes, and ice cream carts in the evenings. Walking the waterfront end to end offers both the best view toward the castle and a perfect circuit for observing Bodrum's lively evening social scene.",
    't': "Gün batımından 30 dakika önce kaleden kışla mevkiine uzanan yolun orta noktasında durun; çift taraflı yansıma fotoğrafçılar için idealdır.",
    'te': "Stand at the midpoint of the path between the castle and the barracks location 30 minutes before sunset; the double-sided reflection is ideal for photographers."},

85: {'d': "Bodrum liman bölgesinde, atrium mimarisiyle tasarlanmış bu otel, merkezi avlusundaki portakal ağaçları ve serin köşeleriyle şehrin gürültüsünden kaçmak için zarif bir dinlenme noktası sunar. Havuzu ve kafe terası, günübirlik ziyaretçilere de keyifli bir mola imkânı tanır.",
    'de': "In Bodrum's harbor district, this hotel designed with atrium architecture offers an elegant retreat from the city's noise with its orange trees and cool corners in the central courtyard. The pool and café terrace also provide a pleasant break opportunity for day visitors."},

87: {'d': "Bodrum merkeze yürüme mesafesinde konumlanan Sevin Otel, dar sokaklara arayanlara yakın bölgedeki en hesaplı aile oteli seçeneklerinden biridir. Sabah kahvaltısında sunulan yöresel ürünler ve konforlu odalarıyla güne iyi başlamak ve ardından liman bölgesini keşfetmek için pratik bir köstür.",
    'de': "Located within walking distance of central Bodrum, Sevin Otel is one of the most affordable family hotel options in the immediate area for those looking for narrow street access. A practical base for starting the day well with local produce at breakfast and then exploring the harbor district."},

89: {'d': "Bodrum'un kalabalık merkezi yakınında apart otel konforunu sunan Queen's, uzun dönem ve tatilci konaklamalar için mutfaklı, özerk yaşam alanlarıyla değerli bir seçenektir. Terası ve merkezi konumu sayesinde Bodrum yaşamını içeriden gözlemlemek için tercih edilen adreslerden biridir.",
    'de': "Offering apart hotel comfort near Bodrum's bustling center, Queen's is a valuable option for long-stay and vacationer accommodations with its kitchenette-equipped autonomous living spaces. One of the preferred addresses for observing Bodrum life from the inside thanks to its terrace and central location."},
}

apply_batch('bodrum.json', U)
