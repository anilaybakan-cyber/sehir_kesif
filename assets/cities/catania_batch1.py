import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
30: {'d': "Etna'nın 3.340 metrelik zirvesine yakın bu gözlem platformu, volkanik kraterlerin ağzına bakılan ve Sicilya ovasından Tirenyen Denizi'ne uzanan 360 derece panoramanın tadıldığı dünyanın en dramatik belveder noktalarından biridir. Gün batımında kızıl lav izleri ve mor gökyüzü, Etna'nın canlı bir varlık olduğunu acı bir güzellikle hatırlatır.",
    'de': "Near Etna's 3,340-metre summit, this observation platform is one of the world's most dramatic belvedere points where you look into the mouths of volcanic craters and savour a 360-degree panorama stretching from the Sicilian plain to the Tyrrhenian Sea. At sunset, red lava traces and purple sky bitterly remind you that Etna is a living presence.",
    't': "Kablo arabası ve güneydeki rifüjden yürüyüş seçenekleri mevcut; zirveye yakın bölgeler rehber eşliğinde ziyaret edilmeli. Kışın kar ekipmanı şart.",
    'te': "Cable car and walking from the southern refuge are available options; areas near the summit must be visited with a guide. Snow equipment is essential in winter."},

32: {'d': "Aci Trezza açıklarında yükselen bu bazalt kayalıklar, Homeros'un 'Odysseia'sında Kyklop Polifem'in Odysseus'a fırlattığı kaya olarak anlatılmaktadır. Sicilya balıkçılığının sembolü olan bu siyah yalçın kayaların önünde sabah erken saatte teknelerle çıkan yerel balıkçıların manzarası, mitoloji ile gündelik yaşamı birleştiren büyülü bir sahneyi oluşturur.",
    'de': "These basalt rock stacks rising off Aci Trezza are described in Homer's 'Odyssey' as the rocks that Cyclops Polyphemus hurled at Odysseus. Local fishermen setting out in boats in the early morning before these black jagged rocks, the symbol of Sicilian fishing, form a magical scene that unites mythology with daily life.",
    't': "Aci Trezza, Catania'dan otobüsle 20 dakika; sabah balıkçı çıkışını görmek için 06:30-07:30 arası limanda olun.",
    'te': "Aci Trezza is 20 minutes from Catania by bus; be at the harbor between 6:30-7:30am to see the morning fishermen's departure."},

38: {'d': "San Nicola alla Rena Manastırı'nın Sicilya'nın en büyük Benediktin yapısı olduğuna dair bilgi, çatısına çıkılana dek salt bir istatistikten ibarettir. Çatı terasına ulaşıldığında Etna'nın konisi, Catania'nın Barok çan kuleleri ve Sicilya düzlüğünün bütünü gözler önüne serilir; bu manzara şehrin en unutulmaz anlarından birini oluşturur.",
    'de': "The fact that San Nicola alla Rena Monastery is Sicily's largest Benedictine structure is merely a statistic until you climb to its roof. Once the rooftop terrace is reached, Etna's cone, Catania's Baroque bell towers, and the entirety of the Sicilian plain are revealed before you; this view constitutes one of the city's most unforgettable moments.",
    't': "Çatı turu belirli saatlerde rehber eşliğinde düzenlenir; manastır resepsiyonundan saat ve ücret bilgisi alın.",
    'te': "Rooftop tours are organized with a guide at specific hours; get time and fee information from the monastery reception."},

39: {'d': "Via dei Crociferi'nin en çarpıcı noktasında yükselen Collegiata Kilisesi cephesi, 18. yüzyıl Sicilya Barok mimarisinin volkanik siyah bazalt üzerine işlenmiş en olgun ifadelerinden biridir. Asimetrisi kasıtlı olan bu cephe, gün içinde güneş açısına göre farklı derinlikler oluşturan gölge oyunuyla mimarinin canlı bir sahne olduğunu kanıtlar.",
    'de': "The Collegiata Church facade rising at the most striking point of Via dei Crociferi is one of the most mature expressions of 18th-century Sicilian Baroque architecture carved into volcanic black basalt. This intentionally asymmetric facade proves that architecture is a living stage with shadow plays creating different depths according to the sun angle throughout the day.",
    't': "Cephe fotoğrafları için sabah 10-11 arası güneş açısı en idealdir; yakın çekimde Barok kabartmaların detayları ortaya çıkar.",
    'te': "The sun angle between 10-11am is most ideal for facade photographs; in close-up, the details of Baroque reliefs emerge."},

40: {'d': "1434'te kurulan Catania Üniversitesi'nin Orta Çağ'dan Barok'a uzanan tarihi binalarla çevrilmiş avlusu, öğrencilerin ve ziyaretçilerin bir arada dolaştığı nadiren rekabete açık entelektüel bir kamu alanı oluşturur. Sütunlu koridorları, tarihi kitabe taşları ve meydan çeşmesiyle üniversite avlusu şehrin en yaşayan tarihi mekanlarından biridir.",
    'de': "The courtyard of Catania University, founded in 1434, surrounded by historic buildings stretching from the Middle Ages to Baroque, forms a rarely competitive intellectual public space where students and visitors mingle. With its columned corridors, historic inscription stones, and square fountain, the university courtyard is one of the city's most living historic spaces.",
    't': "Üniversite müzesi (Museo Civico) burada ziyarete açıktır; Sicilya jeolojisi ve volkanizm koleksiyonu için ücretli giriş gereklidir.",
    'te': "The university museum (Museo Civico) is open for visits here; paid entry is required for the Sicily geology and volcanism collection."},

43: {'d': "Catania'nın UNESCO listesindeki tarihi merkezinde yer alan Badia di Sant'Agata'nın eliptik kubbesi, şehrin Barok silüetinin en tanınan öğelerinden biridir. Kubbeye çıkılabilen bu yapı, Catania çatılarını ve uzakta kararan Etna'yı kuşbakışı görmek için Piazza del Duomo'nun en erişilebilir yüksek perspektifini sunar.",
    'de': "The elliptical dome of Badia di Sant'Agata in Catania's UNESCO-listed historic center is one of the most recognized elements of the city's Baroque silhouette. This structure, accessible to the dome, offers the most accessible high perspective of Piazza del Duomo for a bird's-eye view of Catania's rooftops and the darkening Etna in the distance.",
    't': "Kubbe ziyareti için belli saatlerde biletli giriş mevcut; Piazza del Duomo üzerindeki en iyi fotoğraf açısı buradan elde edilir.",
    'te': "Ticketed entry is available at certain hours for dome access; the best photographic angle over Piazza del Duomo is obtained from here."},

44: {'d': "19. yüzyılda Catania'ya kazandırılan Villa Bellini, lavanta bahçeleri, palmiye gölgeli yürüyüş yolları ve merkezindeki büyük havuzuyla şehrin en sevilen kamusal yeşil alanıdır. Bellinilerin ağırlıklı olduğu Catania halkının bir kısmının öğle dinlencesi geçirdiği bu parkta, sabahları yaşlı erkeklerin satranç oynadığı köşk hâlâ aktif.",
    'de': "Villa Bellini, gifted to Catania in the 19th century, is the city's most beloved public green space with lavender gardens, palm-shaded walking paths, and a large central pond. In this park where a portion of Catania's largely Bellini population takes their midday rest, the pavilion where elderly men play chess in the mornings is still active.",
    't': "Park, şehrin Barok mirasının yoğunluğundan dinginleşmek için idealdir; piknik için öğle öncesi saatler en sakin ve gölgeli anlardır.",
    'te': "The park is ideal for decompressing from the intensity of the city's Baroque heritage; the hours before noon are the quietest and shadiest moments for a picnic."},

45: {'d': "Catania Botanik Bahçesi'nin 19. yüzyıldan kalma sera yapıları, volkanik Etna toprağında büyüyen tropikal bitkiler, Sicilya'ya özgü endemik türler ve dev nilüfer havuzlarıyla kentin en etkileyici ama en az ziyaret edilen yeşil köşelerinden birini oluşturur. Barok kentle yüz yüze gelen bu botanik sığınak, şehir dışına çıkmak istemeden doğayla buluşmayı sağlar.",
    'de': "The 19th-century greenhouse structures of Catania Botanical Garden form one of the city's most impressive yet least visited green corners with tropical plants growing in volcanic Etna soil, endemic species unique to Sicily, and giant lily pads. This botanical refuge facing the Baroque city allows you to connect with nature without wanting to leave the city.",
    't': "Giriş ücretlidir; hafta içi sabah saatlerinde neredeyse ziyaretçisiz bir sessizlik hakimdir. Öğleden sonra güneş sera yapılarını ısıtır.",
    'te': "Entry is paid; on weekday mornings a visitor-free silence prevails. In the afternoon the sun heats the greenhouse structures."},

47: {'t': "Plaj, şehir merkezinden dolmuşla 15 dakikada ulaşılabilir; sabah erken saatler kalabalıktan uzak. Öğle vakti yoğun Sicilya güneşi için güneş kremi ve gölgelik şart.",
    'te': "The beach is reachable by minibus in 15 minutes from the city center; early morning hours are crowd-free. Sunscreen and shade are essential for the intense Sicilian midday sun."},

48: {'d': "Catania'nın modern şehir planlamasının özeti olan Piazza Europa, büyük açık alanı ve denize bakan konumuyla hem yerel halkın akşam yürüyüşü hem de sezonluk açık hava etkinlikleri için şehrin başlıca toplanma noktalarından biridir. Özellikle yaz akşamları organizasyonların yapıldığı bu meydan, Catania'nın kültürel yaşamının yeni odaklarından biridir.",
    'de': "Piazza Europa, a summary of Catania's modern urban planning, is one of the city's main gathering points for both the locals' evening promenade and seasonal open-air events with its large open space and sea-facing position. This square where summer evening events are organized is one of the new centers of Catania's cultural life.",
    't': "Yaz akşamları açık hava konser ve festival programları için şehrin kültür etkinlik sitesini önceden kontrol edin.",
    'te': "Check the city's cultural events site in advance for summer evening outdoor concert and festival programs."},

49: {'d': "Catania'nın kuzey limanı Ognina'nın kayalık sahil yürüyüş yolu, siyah bazalt kayalara vuran dalga köpükleri ve önünden geçen balıkçı tekneleriyle şehrin en özgün akşam yürüyüşü güzergahlarından birini oluşturur. Arka planda Etna'nın silueti, öne çıkan volkanik kaya yapıları ve deniz yelkencileriyle bu lungomare Catania'ya özel eşsiz bir manzara sunar.",
    'de': "The rocky coastal walkway of Catania's northern harbor Ognina forms one of the city's most original evening walk routes with wave foam crashing against black basalt rocks and passing fishing boats. With Etna's silhouette in the background, protruding volcanic rock formations, and sea sailors, this lungomare offers a unique view specific to Catania.",
    't': "Akşam 18:00-20:00 arası Etna'ya batan günbatımı manzarası için en doğru saat; gün batarken volkanın arka plan olarak pıhtılaşan kızıllığı unutulmaz.",
    'te': "Between 6-8pm is the right time for sunset views dropping behind Etna; the volcano's clotting redness as a backdrop as the sun sets is unforgettable."},

50: {'d': "Catania Limanı girişindeki bu Barok zafer takı, 1696'da Viceroy Uzeda'nın şehre girişini kutlamak için inşa edilmiş olup Sicilya'nın İspanyol yönetimi döneminin en önemli kentsel simgelerinden biridir. Siyah bazalt ve beyaz mermer kombinasyonuyla oluşturulan bu görkemli yapı, Etna'nın volkanik taşını Avrupa Barok estetiğiyle buluşturmaktadır.",
    'de': "This Baroque triumphal arch at the entrance of Catania Harbor was built in 1696 to celebrate Viceroy Uzeda's entry into the city and is one of the most important urban symbols of Sicily's Spanish governance period. This magnificent structure created with a combination of black basalt and white marble brings Etna's volcanic stone together with European Baroque aesthetics.",
    't': "Kemer, Via Dusmet'ten limana geçerken görülür; deniz tarafından fotoğraf için liman yürüyüş yolunu kullanın.",
    'te': "The arch is visible when passing from Via Dusmet to the harbor; use the harbor walkway for photography from the sea side."},

51: {'d': "Catania'nın antik Roma hamamları olan Terme dell'Indirizzo, MS 4-5. yüzyıla tarihlenen mozaik taban kalıntılarıyla bugün kısmen bir konut bloğunun içine gömülmüş şekilde ayakta durmaktadır. Bu tarihi kaderin ironisi, Catania'nın antik çağla ne kadar iç içe yaşadığını açıkça ortaya koyar.",
    'de': "Catania's ancient Roman baths, Terme dell'Indirizzo, stand today partially buried within a residential block with mosaic floor remains dating to the 4th-5th centuries AD. The irony of this historical fate clearly reveals how intertwined Catania lives with antiquity.",
    't': "Kalıntılar konut alanının içinde olduğundan görünüm sınırlıdır; yakın bir mimarlık veya arkeoloji turu rehberi eşliğinde en iyi şekilde anlatılır.",
    'te': "Visibility is limited as the remains are within a residential area; best explained with a nearby architecture or archaeology tour guide."},

54: {'d': "Via Crociferi'nin en gözde kemerlerinden biri olan San Benedetto Kemeri, 18. yüzyıl Catania'sının Benediktin manastır topluluklarına olan saygısını yansıtmakta olup bugün yaya trafiği ve kültürel miras turizminin bir arada aktığı özgün bir geçit oluşturmaktadır. Kemerin altından bakıldığında Via Crociferi'nin perspektifi Sicilya Barok'unun en dramatik eksenlerinden birini ortaya koyar.",
    'de': "The San Benedetto Arch, one of Via Crociferi's most admired arches, reflects 18th-century Catania's respect for Benedictine monastic communities and today forms an original passage where pedestrian traffic and cultural heritage tourism flow together. Looking from beneath the arch, the perspective of Via Crociferi reveals one of Sicilian Baroque's most dramatic axes.",
    't': "Kemer altında durup Via Crociferi boyunca uzanan eksenin fotoğrafını çekin; bu perspektif şehrin en tekrarlanamaz görsel deneyimlerinden biridir.",
    'te': "Stand beneath the arch and photograph the axis stretching along Via Crociferi; this perspective is one of the city's most irreproducible visual experiences."},

56: {'d': "Catania'nın Barok mirası içinde daha az bilinen ama uzmanların dikkat çektiği Reburdone Sarayı, cephesindeki karmaşık taş işçiliği ve kemer detaylarıyla siyah bazalt yüzeyine oyulan Sicilya Barok'unun en ince örneklerinden birini oluşturur. Kalabalık güzergahlardan biraz sapa bu saray, şehrin görsel mirasını daha sakin bir atmosferde incelemek için mükemmel bir köşedir.",
    'de': "The Reburdone Palace, less known within Catania's Baroque heritage but highlighted by experts, forms one of the finest examples of Sicilian Baroque carved into black basalt surfaces with its complex stonework and arch details on the facade. This palace slightly off the crowded routes is a perfect corner for examining the city's visual heritage in a calmer atmosphere.",
    't': "Taş işçiliği fotoğrafları için sabah yumuşak ışığında güneye dönük cephe idealdir; öğleden sonra ışık gölge kontrasti fazla artmaktadır.",
    'te': "The south-facing facade in soft morning light is ideal for stonework photographs; by afternoon the light-shadow contrast increases too much."},

57: {'d': "Catania'nın 18. yüzyıl saray mimarisinin az bilinen köşelerinden birini temsil eden Pedagaggi Sarayı, üçlü kemer girişi ve üst katta uzanan balkon sıralarıyla Sicilya Barok'un konut mimarisine yansımasının en özgün örneklerinden birini oluşturur.",
    'de': "Representing one of the little-known corners of Catania's 18th-century palace architecture, Pedagaggi Palace forms one of the most original examples of Sicilian Baroque's reflection in residential architecture with its triple arch entrance and rows of balconies extending on the upper floor.",
    't': "Saray, Via Vittorio Emanuele üzerinde yer alır; tarihi merkez yürüyüşünde dikkat etmeden geçilebilecek bu kemer, yakından bakınca cepheyi açığa çıkarır.",
    'te': "The palace is on Via Vittorio Emanuele; this arch can be passed without noticing on a historic center walk, but looking closely reveals the full facade."},

60: {'d': "Indirizzo Sarayı'nın avlu bahçesi, Catania'nın Barok şatafatı içinde neredeyse kimsenin bilmediği küçük bir huzur köşesidir. Portakal ve limon ağaçlarının gölgelediği taş döşemeli bu avlu, yerleşim alanlarına yakın konumuyla şehrin gündelik yaşam ile tarihin iç içe geçtiğini en sessiz biçimde gösteren mekânlardan biridir.",
    'de': "The courtyard garden of Palazzo Indirizzo is a small peace corner that almost no one knows within Catania's Baroque splendor. This cobblestone courtyard shaded by orange and lemon trees is one of the most quietly demonstrating places where daily life and history intertwine, thanks to its proximity to residential areas.",
    't': "Avluya giriş genellikle serbesttir; saatler ve kapı durumu için yakın dükkanlardan bilgi almak faydalı olabilir.",
    'te': "Entry to the courtyard is generally free; it may be useful to get information about hours and gate status from nearby shops."},

61: {'d': "Catania'nın koruyucu azizesi Sant'Agata'ya adanmış bu küçük kilisedeki sunak, şehrin dini sanat hazinesinin en değerli parçalarından bazılarını barındırır. Altın yaldız kaplama üzerindeki Santo Sepolcro tablosu ve azizeye ait röliklerle birlikte sunulan yakın koruma, şehir halkının bu mekâna derin bağlılığını yansıtır.",
    'de': "The altar in this small church dedicated to Catania's patron saint Sant'Agata houses some of the most valuable pieces of the city's religious art treasury. The Santo Sepolcro painting on gilded frames and the close protection offered alongside relics belonging to the saint reflect the city population's deep attachment to this space.",
    't': "Her yıl Şubat'ta düzenlenen Sant'Agata Festivali sırasında bu küçük kilise şehrin en aktif ibadet merkezlerinden birine dönüşür.",
    'te': "During the Sant'Agata Festival held every February, this small church transforms into one of the city's most active worship centers."},

64: {'d': "Catania'nın arka sokaklarında saklanan bu küçük Barok çeşme, 18. yüzyıl su mühendisliğini köy zanaatkârlığının güzelliğiyle birleştiren ve turistlerin büyük çoğunluğunun fark etmeden geçtiği nadide bir detaydır. Aslan maskı biçimli su ağzı ve üzerindeki yosun örtüsüyle çeşme, Catania'nın aktif ama görünmez tarihi katmanını temsil eder.",
    'de': "This small Baroque fountain hidden in Catania's back streets is a rare detail that combines 18th-century water engineering with the beauty of village craftsmanship, passed unnoticed by the vast majority of tourists. With its lion mask-shaped water spout and the moss covering above it, the fountain represents Catania's active but invisible historical layer.",
    't': "Çeşmeye ulaşmak için Piazza del Duomo'dan hareketle tarihi sokakları küçük ölçekli kent yürüyüşü programlarında soran rehberlerden destek alın.",
    'te': "To reach the fountain, get support from guides in small-scale urban walk programs who can be asked starting from Piazza del Duomo."},

65: {'d': "Catania'nın yüksek bir noktasındaki bu çatı katı bar, Etna'yı ve şehrin Barok kubbelerini aynı anda gören geniş açık terasyyla şehrin en çarpıcı gündoğumu ve gün batımı seyir noktalarından biri olarak öne çıkmaktadır. Akşam saatlerinde Sicilya aperol spritz ve arancini atıştırmasıyla izlenen Etna silueti, mekânı adeta şehrin sembolik aynasına dönüştürür.",
    'de': "This rooftop bar at a high point of Catania stands out as one of the city's most striking sunrise and sunset viewpoints with its wide open terrace that simultaneously looks at Etna and the city's Baroque domes. The Etna silhouette watched with Sicilian aperol spritz and arancini snacking in the evening hours transforms the venue into the city's symbolic mirror.",
    't': "Akşam yemek saatlerinde yer dolmaktadır; gün batımı için en az 1 saat önceden gelin ve Etna'ya bakan köşe masası talep edin.",
    'te': "The venue fills up at dinner hours; arrive at least 1 hour before sunset and request a corner table facing Etna."},

66: {'d': "Etna yamaçlarındaki bağlarda yetişen Nerello Mascalese ve Carricante üzümlerinden üretilen şaraplar, volkanik mineraller sayesinde dünyada başka hiçbir şarap bölgesinde bulunmayan eşsiz bir toprak tadı taşır. Bu tadım turlarında Etna DOC şarapları, üzümün yetiştiği kara toprak ve lav taşı bağ duvarlarının hikayesiyle birlikte sunulur.",
    'de': "Wines produced from Nerello Mascalese and Carricante grapes grown in vineyards on Etna's slopes carry a unique earthy taste found in no other wine region in the world thanks to volcanic minerals. In these tasting tours, Etna DOC wines are presented together with the story of the black soil where the grape grows and the lava stone vineyard walls.",
    't': "Bağ ziyareti ile birleştirilen tadım turları için Etna kuzey yamacında faaliyet gösteren küçük aile bağlarını tercih edin; büyük üreticiler yerine mikro-etikettler daha özgün bir deneyim sunar.",
    'te': "For tasting tours combined with vineyard visits, prefer small family vineyards operating on Etna's northern slope; micro-labels rather than large producers offer a more original experience."},

68: {'d': "Catania'nın en sembolik sokak yemeği olan arancino, Sicilya mutfağının tek bir kızarmış pirinç topunda ne kadar derin bir lezzet dili geliştirdiğinin en çarpıcı kanıtıdır. Bu tur durağı; klasik etli-beşamel dolgusundan fıstıklı-ricottalı modern yorumlara uzanan geniş yelpazede Catania'nın en köklü arancino ustalarının mekanlarını birbirine bağlar.",
    'de': "Arancino, Catania's most symbolic street food, is the most striking evidence of how deep a flavor language Sicilian cuisine has developed in a single fried rice ball. This tour stop connects the venues of Catania's most deep-rooted arancino masters across a wide spectrum from the classic meat-béchamel filling to modern pistachio-ricotta interpretations.",
    't': "En iyi arancino hâlâ sıcakken tadıma girer; fırından yeni çıktığında içi akışkan ve pişme kokusu yoğundur. Sabah 08-10 arası en taze saatlerdir.",
    'te': "The best arancino is tasted while still hot; when fresh from the oven the inside is fluid and the cooking scent is intense. Between 8-10am are the freshest hours."},

69: {'d': "Sicilya sabahının olmazsa olmaz ritüeli olan granita con brioche, Catania'da özellikle krem karamel, fıstık ve kara dut çeşitleriyle doruk noktasına ulaşır. Bu sabah durakları turu, Piazza del Duomo çevresindeki tarihi pastahaneleri ve Etna ürünleriyle üretilen el yapımı granitaları bir arada keşfetmenin en lezzetli yolunu sunmaktadır.",
    'de': "Granita con brioche, the indispensable ritual of the Sicilian morning, reaches its peak in Catania especially with cream caramel, pistachio, and mulberry varieties. This morning stops tour offers the most delicious way to simultaneously discover the historic pastry shops around Piazza del Duomo and the handmade granitas produced with Etna products.",
    't': "Granita sabah 07:30-09:30 arası en taze haliyle sunulur; bu saatlerden sonra bazı çeşitler tükenebilir.",
    'te': "Granita is served at its freshest between 7:30-9:30am; after these hours some varieties may sell out."},

71: {'d': "Catania'nın Via Etnea'sındaki Cafe Comis, günlük granita con brioche, arancino ve taze sıkılmış kan portakalı suyuyla saatlerce öğrencilerin ve yöre halkının dolup taştığı gerçek bir Catania sabahı istasyonudur. Sicilya kahvesi kültürünü en özgün biçimde sunan mekanlar arasında köklü bir yere sahiptir.",
    'de': "Cafe Comis on Catania's Via Etnea is a genuine Catania morning station that fills with students and local residents for hours, with its daily granita con brioche, arancino, and freshly squeezed blood orange juice. It holds a deep-rooted place among the venues presenting Sicilian coffee culture in its most authentic form.",
    't': "Sabah 08:00-09:30 arası kalabalık en yoğun; öğle saatlerinde daha sakin bir ortamda granita ve kahve keyfi yaşanır.",
    'te': "The crowd is at its peak between 8:00-9:30am; at noon a more relaxed granita and coffee pleasure is experienced."},

72: {'d': "Catania'nın tarihi Barok ekseninde yer alan Cafe Agata, aziz günü Şubat'ta düzenlenen Sant'Agata Festivali döneminde şehrin en aktif ve kalabalık pastane-kafeterya noktası hâline gelir. Festival sezonunun dışında da arancino, cassata ve granita ile öğrencilerin ve yerel halkın sevdiği özgün bir Catania buluşma köşesidir.",
    'de': "Cafe Agata on Catania's historic Baroque axis becomes the city's most active and crowded pastry-cafeteria point during the Sant'Agata Festival held in February on the saint's day. Outside festival season too, it is an original Catania meeting corner loved by students and locals with its arancino, cassata, and granita.",
    't': "Şubat başındaki Sant'Agata Festivali döneminde cafe'ye girmek için kuyrukta beklemek gerekebilir; bu tarihlerde şehrin pek çok pastanesi özel festival tatlıları çıkarır.",
    'te': "During the Sant'Agata Festival in early February it may be necessary to wait in line to enter; many of the city's pastry shops release special festival sweets at these dates."},

74: {'d': "Piazza del Duomo yakınındaki Cafe Spinella, 1936'dan bu yana Catania'nın en prestijli kahve ve pastacılık mekanları arasında yerini koruyan tarihi bir kafedir. Cam vitrinlerdeki el yapımı cassata siciliana, granita di gelsomino ve fıstıklı torrone ile bu kafe, Sicilya pastacılık geleneğinin tüm derinliğini tek bir vitrin içinde özetliyor.",
    'de': "Cafe Spinella near Piazza del Duomo is a historic café that has maintained its place among Catania's most prestigious coffee and pastry venues since 1936. With handmade cassata siciliana, granita di gelsomino, and pistachio torrone in glass display cases, this café summarizes the full depth of Sicilian pastry tradition within a single showcase.",
    't': "Sabah 07:30'da granita con brioche siparişini verin; yaz döneminde bu saat yoğundur ama Piazza del Duomo manzaralı ayakta yeme geleneği burada yaşatılır.",
    'te': "Place your granita con brioche order at 7:30am; this hour is busy in summer but the standing-to-eat tradition with a Piazza del Duomo view is preserved here."},

81: {'d': "Etna'nın güney yamaçlarından geçen bu yürüyüş rotası, katılaşmış lav akıntıları ve volkanik kaya formasyonları arasında doğanın hem yıkıcı hem yenileyici yüzünü aynı anda sergileyen bir deneyim sunar. Karanlık lav tünellerinden geçerken oluşan sessizlik ve boşluk hissi, Etna'nın son binlerce yıldır yarımadanın yapısını nasıl şekillendirdiğini fiziksel olarak kavratır.",
    'de': "This hiking route passing through Etna's southern slopes offers an experience that simultaneously showcases nature's both destructive and regenerative face among solidified lava flows and volcanic rock formations. The silence and emptiness felt when passing through dark lava tunnels physically conveys how Etna has shaped the peninsula's structure over the last thousands of years.",
    't': "Rehber eşliğinde yürüyüş önerilir; özellikle lav tüneli geçişleri için kafa feneri ve sağlam yürüyüş ayakkabısı zorunludur.",
    'te': "Walking with a guide is recommended; a headlamp and sturdy hiking shoes are essential especially for lava tunnel passages."},

85: {'d': "Etna'nın kuzeybatı cephesindeki bu lav yürüyüş güzergahı, 2001 ve 2002 patlamalarından kalan taze lav akıntılarının üzerinden geçerek volkanik aktivitenin son izlerini hissetmenizi sağlar. Katılaşmış siyah lav ile arka planda beliren taze sarı/turuncu renkli kraterlerin kontrastı, doğanın en ham hâlini çerçeveler.",
    'de': "This lava hiking route on Etna's northwestern flank takes you over fresh lava flows remaining from the 2001 and 2002 eruptions, letting you feel the latest traces of volcanic activity. The contrast between solidified black lava and fresh yellow/orange-colored craters appearing in the background frames nature in its most raw state.",
    't': "Bu rota aktif kısımlara yakın geçtiğinden kılavuzla birlikte gitmek zorunludur; yerel yetkililer koşullara göre erişimi kısıtlayabilir.",
    'te': "Since this route passes near active sections, going with a guide is mandatory; local authorities may restrict access based on conditions."},

89: {'d': "Etna'nın doğu yamaçlarındaki bu lav alanı yürüyüşü, karanlık taş yüzeyleri ile volkanik bombaların (fırlatılan lav parçacıkları) bıraktığı kratercikleri keşfetmek için doğaya daldığınız ve dünyadan koptuğunuz hissini veren bir Etna rotasıdır. Yer yer oluşan buhar delikleri (fumarol) toprağın hâlâ nefes aldığını sessizce kanıtlar.",
    'de': "This lava field walk on Etna's eastern slopes is an Etna route that gives you the feeling of plunging into nature and disconnecting from the world as you discover dark stone surfaces and small craters left by volcanic bombs (ejected lava fragments). Steam holes (fumaroles) forming here and there quietly prove that the ground is still breathing.",
    't': "Fumarol bölgeleri kükürt gazı içerebilir; derin nefes almaktan kaçının ve bölgeden hızlıca geçin. Tur rehberinizin güvenlik talimatlarına uyun.",
    'te': "Fumarole areas may contain sulfur gas; avoid breathing deeply and pass through the area quickly. Follow your tour guide's safety instructions."},

93: {'d': "Etna'nın kuzey yamacında, deniz seviyesinden yaklaşık 2.000 metrede gerçekleştirilen bu lav yürüyüşü, siyah lapilli yüzeyleri ve uzakta gökyüzüne karışan tütme kraterleriyle adeta başka bir gezegende yürüme hissi yaratır. Gün boyunca değişen krater dumanı ve bulut oluşumları bu coğrafyayı her saatte farklı kılar.",
    'de': "This lava walk carried out on Etna's northern slope at approximately 2,000 metres above sea level creates a feeling of walking on another planet with its black lapilli surfaces and smoking craters blending into the sky in the distance. The crater smoke and cloud formations changing throughout the day make this geography different at every hour.",
    't': "Sabah erken saatte başlanan yürüyüş daha net görüş ve serin hava sağlar; öğleden sonra sis ve bulut oluşumu manzarayı kapatabilir.",
    'te': "A walk started early in the morning provides clearer visibility and cooler air; in the afternoon fog and cloud formation may block the view."},

97: {'d': "Etna'nın güneybatı kesimindeki bu özel lav yürüyüş güzergahı, tarihi patlamalardan kalan donmuş lav tünellerini, eski lav köprülerini ve volkanik tüf kalıntılarını aynı rotada sunarak Etna jeolojisinin evrimini adım adım hissettirmektedir.",
    'de': "This special lava hiking route in Etna's southwestern sector presents frozen lava tunnels from historic eruptions, old lava bridges, and volcanic tuff remains on the same route, making you feel the evolution of Etna's geology step by step.",
    't': "Jeoloji rehberli turlar mevcut; sıradan yürüyüş rehberinden farklı olarak lav oluşumu ve Etna stratigrafisini öğrenmek isteyenler için en verimli seçenek.",
    'te': "Geology-guided tours are available; the most productive option for those wanting to learn about lava formation and Etna stratigraphy, unlike an ordinary hiking guide."},

101: {'d': "Etna'nın bu yamaç güzergahında, son 30 yılın en şiddetli patlamalarının izleri hâlâ taze durmaktadır. 1991-1993 lav akıntısının neredeyse Zafferana kasabasını yuttuğu yere kadar ulaşabileceğiniz bu rota, insanların doğal afet sınırında nasıl yaşadığını somut olarak gösterir.",
    'de': "On this hillside route of Etna, the traces of the most intense eruptions of the last 30 years still appear fresh. This route where you can reach near where the 1991-1993 lava flow almost swallowed the town of Zafferana concretely shows how people live on the edge of natural disaster.",
    't': "Zafferana Etnea kasabasından başlanan bu tur, yerel rehber eşliğinde tamamlandığında patlamanın kasabayı nasıl çevrelediğini adım adım anlayabilirsiniz.",
    'te': "Starting this tour from Zafferana Etnea town, when completed with a local guide you can understand step by step how the eruption surrounded the town."},

105: {'d': "Etna'nın bat tarafından erişilen bu lav yürüyüşü, volkanik kaya sütunları ve lapilli tarlalarının arasından geçerken 19. yüzyıldan bu yana değişmeden kalan bağ ve zeytinliklere kavuşuyor. Yıkım ile üretkenliğin yanyana var olduğu bu kontrast, Etna çiftçilerinin volkanla kurulan binlerce yıllık barışçıl gerilimi somutlaştırır.",
    'de': "This lava walk accessed from Etna's western side reaches vineyards and olive groves that have remained unchanged since the 19th century while passing through volcanic rock columns and lapilli fields. This contrast where destruction and productivity coexist embodies the thousands-of-years-long peaceful tension established by Etna farmers with the volcano.",
    't': "Bu güzergah üzerindeki bazı bağlar tadım imkânı sunmaktadır; tur operatörünüzle önceden düzenleme yaparak bağ ziyaretini yürüyüşe ekleyin.",
    'te': "Some vineyards along this route offer tasting opportunities; make arrangements with your tour operator in advance to add a vineyard visit to the walk."},

109: {'d': "Etna'nın kuzeydoğu konisine yakın bu lav yürüyüş rotası, aktif yan kraterlerin yakınından geçerek volkanik faaliyetin en dinamik yüzüne tanıklık etmenizi sağlar. Alttaki bazalt platosu ile üstteki krater duvarları arasındaki renk geçişi, siyahtan griye ve sarıya uzanan volkanik madde paletini gözler önüne serer.",
    'de': "This lava hiking route near Etna's northeastern cone allows you to witness the most dynamic face of volcanic activity by passing near active lateral craters. The color transition between the basalt plateau below and the crater walls above reveals the volcanic material palette stretching from black to grey and yellow.",
    't': "INGV (İtalya Ulusal Jeofizik ve Volkanoloji Enstitüsü) web sitesinden Etna aktivite durumunu kontrol edin; yüksek aktivite dönemlerinde bu krater bölgelerine erişim kapatılabilir.",
    'te': "Check Etna activity status on the INGV (Italian National Institute of Geophysics and Volcanology) website; access to these crater areas may be closed during high activity periods."},

113: {'d': "Etna'nın güney platosundaki bu son lav yürüyüş noktası, şimşek hızında katılaşmış lav yüzeylerinin oluşturduğu doğal heykel bahçesi gibi bir manzara sunar. Bazı yerlerde insan boyunda yükselen lav sütunları ve bombe şeklinde donmuş parçacıklar, patlamanın kinetik enerjisini kalıcı biçimde cisimleştirmiştir.",
    'de': "This final lava walk point on Etna's southern plateau presents a landscape like a natural sculpture garden formed by lava surfaces solidified at lightning speed. In some places, lava columns rising to human height and frozen particles in bomb shapes have permanently embodied the kinetic energy of the eruption.",
    't': "Güney platosu yaz aylarında oldukça sıcak ve gölgesiz olabilir; bol su, güneş kremi ve baş koruyucu şapka zorunludur.",
    'te': "The southern plateau can be very hot and shadeless in summer months; plenty of water, sunscreen, and a head-protecting hat are mandatory."},
}

apply_batch('catania.json', U)
