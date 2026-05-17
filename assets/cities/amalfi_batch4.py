import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
96: {'d': "Ravello'nun üst mahallelerindeki bu küçük şapel, taş duvarları ve tek renkli vitray camıyla hafif gizemli bir atmosfer yaratır. Azize Lucia'ya adanan sunak ve eski votif tablolar, burayı köy halkının yüzyıllardır dua etmek için geldiği sessiz bir ibadet yeri olarak canlı tutar.",
    'de': "This small chapel in Ravello's upper quarters creates a subtly mysterious atmosphere with its stone walls and single stained glass window. An altar dedicated to Saint Lucy and old votive plaques keep it as the quiet place of prayer where village residents have come to worship for centuries.",
    't': "Şapel sürekli açık olmayabilir; Ravello'nun diğer kiliselerini gezerken uğramanız yeterlidir.",
    'te': "The chapel may not always be open; simply try the door when passing by during visits to Ravello's other churches."},

97: {'d': "Ravello yakınındaki küçük Scala köyüne ait bu kilise, 11. yüzyıl fresk kalıntıları ve bölgenin en yüksek çan kulesiyle gizli bir tarihi hazinedir. Ravello'nun kalabalık merkezinden sadece birkaç dakika uzakta, arka sokaklarda saklanan yapı tamamen farklı bir sakinlik içinde durur.",
    'de': "Belonging to the small village of Scala near Ravello, this church with its 11th-century fresco remnants and the area's tallest bell tower is a hidden historic treasure. Tucked in back streets just minutes from Ravello's busy center, it stands in a completely different serenity.",
    't': "Scala köyüne dolmuş ile ulaşılabilir; turistlerin neredeyse uğramadığı bu köy başlı başına gezmeye değer.",
    'te': "Scala village is reachable by local bus and is well worth exploring on its own — tourists almost never go there."},

98: {'d': "Agerola'dan Nocelle'ye uzanan Tanrıların Yolu, Amalfi Sahili'nin üzerinde asılı kalmış gibi hissettiren kayalık teras patikasından geçer. Her 200 metrede değişen manzara; zeytinlikler, kuru taş duvarlar, Positano'nun çatıları ve Capri silüeti sırayla çerçeveye girer.",
    'de': "The Path of the Gods from Agerola to Nocelle passes along a rocky terrace path that makes you feel suspended above the Amalfi Coast. Every 200 metres the view changes: olive groves, dry-stone walls, Positano's rooftops, and Capri's silhouette each enter the frame.",
    't': "Nocelle'den Positano'ya minibüs var; tek yönlü yürüyüp aşağı sahile inerek günü güzel tamamlarsınız.",
    'te': "A minibus runs from Nocelle to Positano; walk one way and descend to the beach below for a perfect end to the day."},

99: {'d': "Positano'nun en yoğun turistik noktasında yükselen bu kilise, altın mozaikli Bizans tarzı ana sunağı, kara madonnası ikonası ve denize bakan çan kulesiyle 18. yüzyıldan bu yana köyün simgesi olmuştur. İçerisi beklenilenin çok ötesinde görkemlidir; çoğu ziyaretçiyi şaşırtır.",
    'de': "Rising at Positano's busiest tourist point, this church has been the village's emblem since the 18th century with its golden-mosaic Byzantine high altar, iconic Black Madonna, and sea-facing bell tower. Its interior is far grander than expected and surprises most visitors.",
    't': "Kısa kollu ve omuzları örtecek bir eşarp yanınızda bulundurun; kiliseye girişte örtünme zorunludur.",
    'te': "Carry a scarf to cover your shoulders and upper arms — modest dress is required to enter."},

103: {'d': "Positano'nun küçük limanından kalkan bu tekne turları, Grotta dello Smeraldo, Li Galli adaları ve Capri'ye gün uzunluğunda yolculuklar düzenler. Şnorkel molalı ve açık deniz öğle yemekli özel tur seçenekleriyle Amalfi Sahili'ni denizden keşfetmenin en unutulmaz yoludur.",
    'de': "Departing from Positano's small harbor, these boat tours organize day-long voyages to Grotta dello Smeraldo, the Li Galli Islands, and Capri. With private charters offering snorkel stops and an open-sea lunch, they are the most unforgettable way to discover the Amalfi Coast from the water.",
    't': "Güneş kremi ve deniz hastalığı ilacı yanınızda olsun; rüzgarlı günlerde dalgalar beklenenden güçlü olabilir.",
    'te': "Bring sunscreen and seasickness tablets; on windy days swells can be stronger than expected."},

106: {'d': "SS163 sahil yolu üzerindeki bu belveder noktası, Amalfi şehrinin tamamını, limanını ve arka plandaki dağları tek çerçevede yakalamak için mükemmel bir fotoğraf durağı sunar. Sabah sisinin dağılmasından sonraki ilk iki saat, bu açıdan en net görüntüleri verir.",
    'de': "This viewpoint on the SS163 coastal road offers the perfect photography stop to capture the entire town of Amalfi, its harbor, and the mountains behind in a single frame. The first two hours after morning mist clears give the sharpest views from this angle.",
    't': "Araçla uğramanız gerekiyorsa park yeri çok sınırlı; sabah erken veya sezon dışı gelmeyi tercih edin.",
    'te': "If stopping by car, parking is very limited; early morning or off-season visits are much easier."},

108: {'d': "Ravello'nun hemen batısında uzanan bu belveder terası, Amalfi Kıyısı'nı kesintisiz bir panoramada sunar. Öndeki limon bahçelerinin sarısı, arkadaki dağların yeşili ve aşağıdaki denizin mavisi bir arada bu üçlü renk paleti, Güney İtalya'nın özeti gibidir.",
    'de': "This belvedere terrace just west of Ravello presents the Amalfi Coast in an uninterrupted panorama. The yellow of lemon groves in front, the green of mountains behind, and the blue of the sea below form a three-color palette that feels like a summary of Southern Italy.",
    't': "Gün batımından bir saat önce gelindiğinde ışık en dramatik halini alır; sabırlı bekleyiş ödüllendiricidir.",
    'te': "Arriving one hour before sunset brings the most dramatic light — patient waiting here is generously rewarded."},

113: {'d': "Amalfi'nin hemen doğusunda kayalıklara yaslanmış bu sakin belveder, kıyı yolunun gürültüsünden uzakta küçük bir terasyı üzerinden sahilin doğu ucuna bakmanızı sağlar. Sabah saatlerinde balıkçıların kullandığı bu köşe, Amalfi yaşamının sessiz ve gerçek bir fotoğrafıdır.",
    'de': "Perched against the rocks just east of Amalfi, this quiet belvedere lets you gaze at the eastern end of the coast from a small terrace away from the coastal road noise. Used by fishermen in the mornings, this corner is a quiet and authentic photograph of real Amalfi life.",
    't': "Sabah 6-8 arasında balıkçı teknelerinin çıkışını izlemek için mükemmel; güneşin denizden yükselişini de buradan görebilirsiniz.",
    'te': "Perfect for watching fishing boats depart between 6 and 8am; the sun rising from the sea is also visible from here."},

115: {'d': "Positano'nun en seçkin otellerinden biri olan Hotel Poseidon, kentin güzel konumundan Tyrrhen Denizi'ne uzanan panoraması, şezlong sıralarıyla kaplı geniş terasları ve kaliteli restoranıyla yüksek bütçeli ziyaretçilerin gözdesi olmayı sürdürüyor.",
    'de': "One of Positano's most distinguished hotels, Hotel Poseidon continues to be the go-to choice for high-budget visitors with its wide terraces lined with sun loungers, Tyrrhenian Sea panorama, and quality restaurant from an enviable position in town."},

116: {'d': "Praiano'nun sakin mahallelerinden birinde konumlanan Hotel Conca d'Oro, deniz manzaralı kaya teras havuzu, limon bahçelerini andıran yeşil bahçesi ve misafirperver yerel aile yönetimiyle kalabalıktan uzak bir kıyı tatili için mükemmel bir sığınaktır.",
    'de': "Located in one of Praiano's quiet neighborhoods, Hotel Conca d'Oro is the perfect coastal hideaway away from the crowds, with its clifftop terrace pool facing the sea, lemon grove-like garden, and warm local family management."},

118: {'d': "Amalfi'nin yukarı mahallelerinde taş duvarlarla çevrilmiş bu butik villa oteli, Amalfi limanına ve sahilin tamamına açılan görkemli manzarasıyla şehir merkezindeki otellere kıyasla çok daha sakin ve huzurlu bir konaklama imkanı sunar.",
    'de': "Surrounded by stone walls in Amalfi's upper quarters, this boutique villa hotel offers a far more peaceful and tranquil stay than centrally located hotels, with a magnificent panorama spanning Amalfi harbor and the full stretch of the coast."},

119: {'d': "Ravello'nun hemen dışında, köy sınırında konumlanan Hotel Pellegrino, şehir merkezinin yoğunluğundan sadece beş dakika yürüme uzaklığında olmakla birlikte sessiz ve huzurlu bir konaklama imkanı sunar. Küçük bahçesi ve manzaralı terasıyla bölgeyi hem dinlenerek hem keşfederek görmek isteyenler için iyi bir seçenek.",
    'de': "Located just outside Ravello on the village boundary, Hotel Pellegrino offers a quiet and restful stay just five minutes on foot from the busy town center. With its small garden and view terrace, it suits those who want to both relax and explore the area."},

120: {'d': "Positano'nun taraçalı yamaçlarına sinen bu otel, şehrin ikonik renkli evlerine ve uzakta denize açılan terası, ferah odaları ve samimi aile yönetimiyle Positano'nun pahalı butik otelleri arasında iyi değer sunan seçeneklerden biridir.",
    'de': "Nestled into Positano's terraced hillside, this hotel offers good value among the town's pricey boutique options with its terrace opening to the town's iconic colorful houses and the sea beyond, along with spacious rooms and warm family management."},

121: {'d': "Praiano kıyısındaki bu zarif restoran, kayalık uçurum kenarındaki konumuyla hem nefes kesen Tyrrhen manzarası hem de taş fırında pişirilmiş taze balık sunar. Akşam menüsündeki kalamar doldurma ve kerevit risotto, muhteşem arka planla tamamlanınca unutulmaz bir yemek deneyimine dönüşür.",
    'de': "Perched on a rocky cliff edge in Praiano, this elegant restaurant offers both breathtaking Tyrrhenian views and fresh fish from a stone oven. The evening menu's stuffed squid and langoustine risotto become an unforgettable dining experience when paired with the spectacular backdrop."},

124: {'d': "Praiano'nun dramatik uçurum kenarına inşa edilmiş bu butik otel, denize sıfır manzaralı odaları ve özel şnorkel faaliyetleriyle Amalfi Sahili'nin en çarpıcı konaklamalarından birini sunar. Orijinal Saracen kulesi, otele özgün bir tarihi karakter katar.",
    'de': "Built on Praiano's dramatic cliff edge, this boutique hotel offers one of the Amalfi Coast's most striking stays with its sea-level rooms and private snorkeling activities. The original Saracen tower adds a unique historic character to the property."},

130: {'d': "Positano'nun yukarı mahallelerinde, el yapımı limon seramiği ve taze limon sıkacakları satan dükkanların arasına sıkışmış bu butik mekan, hem alışveriş hem de hafif bir öğle yemeği için idealdir. İnce taş duvarlı salonunda servis edilen taze makarna ve yöresel zeytinyağı, şehrin en iyi ev yemeklerinden birine eşdeğerdir.",
    'de': "Tucked among shops selling handmade lemon ceramics and fresh lemon squeezers in Positano's upper quarters, this boutique spot is ideal for both shopping and a light lunch. Fresh pasta and local olive oil served in its stone-walled room match some of the town's finest home cooking."},

132: {'d': "Agerola'nın dağ havasında konumlanan bu agriturismo, Amalfi Sahili bölgesinin organik sebze bahçelerinden toplanan ürünlerle hazırladığı köy kahvaltısı ve ev yapımı ricotta peyniriyle şehir gürültüsünden tamamen farklı bir doğa konaklama deneyimi sunar.",
    'de': "Located in the mountain air of Agerola, this agriturismo offers a nature-stay experience completely different from the city's noise, with a village breakfast and homemade ricotta prepared from the organic vegetable gardens of the Amalfi Coast hinterland."},

135: {'d': "Positano'nun plaj seviyesindeki bu kafe ve restoran, denize açılan geniş terasyı ve taşlı sahil zeminine yakın masalarıyla sabah kahvaltısından akşam yemeğine kadar her saatte insanlarla dolup taşar. Taze sıkılmış narenciye suları ve fırından çıkmış İtalyan hamur işleri için favori duraklardan biridir.",
    'de': "This café and restaurant at beach level in Positano fills with people from morning breakfast to evening dinner on its wide terrace facing the sea and tables close to the stony shore. It is a favorite stop for freshly squeezed citrus juices and oven-fresh Italian pastries."},

136: {'d': "1952'den bu yana Positano'nun üst mahallelerinde faaliyet gösteren Moressa, nesiller boyu devam eden bir aile geleneğini sürdürür. El yapımı makarna, taze otlu et yemekleri ve yöresel şarap listesiyle klasik Güney İtalya sofrasını Positano'daki günün en özgün yemek durakları arasına taşır.",
    'de': "Operating in Positano's upper quarters since 1952, Moressa maintains a family tradition passed down through generations. Handmade pasta, herb-fresh meat dishes, and a local wine list place it among the most authentic dining stops in Positano for a classic Southern Italian table."},

137: {'d': "Positano'nun dar sokaklarında aşağı inerken burnunuza gelen taze ekmek kokusu sizi bu küçük fırına çeker. Zeytinyağlı focaccia, limon kaplamalı pasta ve taze portakallı cornetto, bu aile fırınının Positanolu komşular ve sabah erkenci turistler arasındaki meşhur ürünleridir.",
    'de': "The scent of fresh bread wafting up Positano's narrow lanes as you descend draws you into this small bakery. Olive oil focaccia, lemon-glazed cake, and fresh orange cornetto are the beloved products of this family bakery among local residents and early-rising tourists alike."},

138: {'d': "Amalfi Sahili'nin en çok fotoğraf çekilen sokaklarından birinde konumlanan Angelo Cafe, ev yapımı limon kekinden geleneksel sfogliatella'ya kadar geniş bir pastacılık menüsü sunar. Küçük bahçeli terasında kahve içmek, kasabanın tipik Güney İtalya akşam atmosferini solumak için idealdir.",
    'de': "Located on one of the Amalfi Coast's most photographed streets, Angelo Cafe offers a wide pastry menu from homemade lemon cake to traditional sfogliatella. Drinking coffee on its small garden terrace is ideal for breathing in the town's typical Southern Italian evening atmosphere."},

139: {'d': "El yapımı Sicilya tarzı gelato ile Positano'nun en iyi dondurma dükkanları arasına girmeyi başaran Sofiposa, taze limon ve fıstıklı çikolata başta olmak üzere Kampanya meyveleriyle renklendirilen sezonluk tatlılarıyla ün kazanmıştır. Yürürken yenen bir top dondurma, Positano deneyiminin ayrılmaz parçasına dönüşür.",
    'de': "Having earned its place among Positano's best gelato shops with handmade Sicilian-style gelato, Sofiposa is celebrated for its seasonal sweets coloured by Campanian fruits, especially fresh lemon and pistachio chocolate. A scoop eaten while strolling becomes an inseparable part of the Positano experience."},

141: {'d': "Homeros'un Ulysses efsanesine ev sahipliği yaptığı söylenen Li Galli adalarından esinlenen bu deniz kıyısı konaklama mekanı, Positano'nun limanına bakan küçük ve samimi bir yapıdır. Denizci atmosferi, antika haritalar ve denize inen dar sokak manzarası ile eşsiz bir konaklama kişiliğine sahiptir.",
    'de': "Inspired by the Li Galli islands said to have hosted Homer's Ulysses legend, this small and sincere waterfront accommodation faces Positano's harbor. Its seafaring atmosphere, antique maps, and view of the narrow lane descending to the sea give it a unique lodging personality."},

150: {'d': "Maiori yakınındaki dağ sırtında yükselen bu hac yeri, 18. yüzyıldan kalma taş yollarla ulaşılan manzaralı terasıyla Amalfi Sahili bölgesinin en önemli dini mekanlarından biridir. Her Eylül'de İtalya'nın dört bir yanından hacılar bu yokuşu tırmanır.",
    'de': "Rising on a mountain ridge near Maiori, this pilgrimage sanctuary reached by 18th-century stone paths and its scenic terrace is one of the Amalfi Coast region's most important religious sites. Every September, pilgrims from across Italy climb this hillside.",
    't': "Ziyaret için rahat, kapalı ayakkabı şart; taş yollar uzun ve bazı bölümler dik.",
    'te': "Comfortable closed shoes are essential for the visit; the stone paths are long and some sections are steep."},

154: {'d': "Positano'nun az bilinen ama yerel halkın sık ziyaret ettiği bu küçük restoranı, taze avlanmış balıktan hazırlanan günlük menüsü ve ev yapımı dessert'leriyle kalabalık plaj restoranlarına alternatif aramak isteyenlerin sığınağıdır. Rezervasyon yapmak neredeyse zorunlu.",
    'de': "One of Positano's lesser-known but frequently visited local restaurants, Sisina's is a refuge for those seeking an alternative to crowded beach restaurants, with its daily menu prepared from freshly caught fish and homemade desserts. A reservation is almost essential.",
    't': "Müdavim yerel müşterilerin masa tuttuğu mekan; önceden arayıp rezervasyon yapın.",
    'te': "A regular local clientele claims tables here; call ahead to make a reservation before visiting."},

155: {'d': "Atrani kasabasının meydanında bulunan bu aile kafeteryası, yerel halkın günde birkaç kez espresso içmeye geldiği ve turistlerin nadiren uğradığı otantik bir iç İtalyan kafe deneyimi yaşatır. Taze hazırlanmış tramezzini sandviçleri ve ev yapımı granita ile kısa bir molayı keyifli bir mola hâline getirir.",
    'de': "Located in the square of Atrani village, this family café delivers an authentic inner Italian café experience where locals come for espresso several times a day and tourists rarely venture. Freshly made tramezzini sandwiches and homemade granita turn a quick break into an enjoyable stop."},

156: {'d': "Atrani'nin ana meydanında köy halkının yıllardan bu yana uğrak yeri olan Bar Mansi, kahve ve yerel pastacılık ürünleriyle tanınan sade bir Güney İtalya barıdır. Pozisyonu itibarıyla kolladiyata kilisesinin önündeki güzelliği yudum yudum içmek için mükemmel bir yer.",
    'de': "Bar Mansi in Atrani's main square has been the village's gathering spot for years, a simple Southern Italian bar known for its coffee and local pastries. Its position makes it the perfect place to slowly savour the beauty in front of the collegiate church."},
}

apply_batch('amalfi.json', U)
