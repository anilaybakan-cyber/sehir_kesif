import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
119: {'d': "Bodrum'un bar sokağının kalbinde yer alan Adamik, sezonun en popüler elektronik müzik mekanlarından biri olarak genç kitlelerin akın ettiği bir gece kulübüdür. Uluslararası DJ'lerin sahne aldığı terası ve lazer ışık gösterisiyle dışarıdan bakıldığında bile sezonun enerjisini hissettirir.",
    'de': "Located at the heart of Bodrum's bar street, Adamik is a nightclub that young crowds flock to as one of the season's most popular electronic music venues. With its terrace where international DJs perform and laser light shows, it radiates the season's energy even when viewed from outside.",
    't': "Kapıda uzun kuyruk oluşabilir; gece 01:00 sonrası girişin daha hızlı olduğu bilinir. Önceden bilet veya guestlist kaydı yaptırın.",
    'te': "Long queues can form at the door; entry is known to be faster after 1am. Register for a ticket or guestlist entry in advance."},

120: {'d': "Bodrum gece hayatının geçiş noktaları arasında değerlendirilen bu mekan, bar sokağındaki geç başlayan akşam programlarının önemli duraklarından biri haline gelmiştir. Canlı performanslar ve sahne gösterileriyle sezon boyunca dolu olan mekan, Bodrum'un eğlence ekosisteminin köklü parçalarından biridir.",
    'de': "Considered one of the transition points of Bodrum's nightlife, this venue has become one of the important stops in the late-starting evening programs on bar street. Filled throughout the season with live performances and stage shows, it is one of the established parts of Bodrum's entertainment ecosystem.",
    't': "Saat 23:00 sonrası canlanan mekan; erken gitmeniz gerekiyorsa önce başka bir yerde akşam yemeği yiyin.",
    'te': "The venue comes alive after 11pm; if you need to go early, have dinner elsewhere first."},

121: {'d': "Bodrum'un bar sokağının üst katlarına uzanan Posh Club, panoramik terasıyla Bodrum körfezi ve kale manzarasını arka plan olarak kullanan en görsel gece kulüplerinden biridir. VIP masa rezervasyonlu kapalı alanı ve açık terasıyla hem bakımlı hem çılgın bir gece için iki farklı ruh hali sunar.",
    'de': "Extending to the upper floors of Bodrum's bar street, Posh Club is one of the most visual nightclubs using panoramic terrace views of Bodrum Bay and the castle as a backdrop. With its VIP table-reserved indoor area and open terrace, it offers two different moods for both a refined and a wild night.",
    't': "Terasta masa almak için sezon zirvesinde rezervasyon şart; gece kulübüne dönüşmeden önce akşam yemeği servisi de yapılıyor.",
    'te': "A reservation is essential for a terrace table in peak season; dinner service is also offered before it transforms into a nightclub."},

122: {'d': "Bodrum'un sakin koylarından birinde yer alan bu plaj kulübü, hem yerel tatilcilerin hem de teknesiyle gelen yat sakinlerinin uğrak noktasına dönüşmüştür. Doğaya entegre şezlonguyla ve önünde uzanan berrak sularıyla günü saatlerce geçirmeye elverişli huzurlu bir koy deneyimi sunar.",
    'de': "Located in one of Bodrum's tranquil coves, this beach club has become the go-to point for both local holidaymakers and yacht residents arriving by boat. With its nature-integrated sun loungers and the clear waters stretching before it, it offers a peaceful cove experience suitable for spending hours of the day.",
    't': "Hem kara yolundan hem de tekneden erişilebilir; koy içindeki berraklık sayesinde şnorkel ekipmanı mutlaka yanınızda olsun.",
    'te': "Accessible both by land and by boat; the clarity within the cove means you should always have snorkel equipment with you."},

124: {'d': "Bodrum'un gece hayatında köklü isimlerden biri olan Vittoria, hem canlı müzik hem de DJ performanslarıyla geniş yelpazede bir gece programı sunar. Bar sokağındaki konumu ve kültürel konsept zenginliğiyle pek çok sanatçının kariyer başlangıcına sahne olmuştur.",
    'de': "One of the established names in Bodrum's nightlife, Vittoria offers a broad nightly program with both live music and DJ performances. With its bar street location and cultural concept richness, it has hosted the career beginnings of many artists.",
    't': "Canlı müzik geceleri için etkinlik takvimini önceden takip edin; özellikle Temmuz gelişimleri aylarca önceden duyuruluyor.",
    'te': "Follow the event calendar in advance for live music nights; July performances in particular are announced months ahead."},

125: {'d': "Bodrum'un bar sokağındaki bu karaoke mekanı, hem yabancı turistlerin hem de yerel sakinlerin eğlenceli bir gece için tercih ettiği sıradışı duraklardan biridir. Türkçe ve İngilizce şarkı listesiyle dolu arşiv sistemi, sahnede bir an parlama fırsatı arayan herkese açık kapı ile bekler.",
    'de': "This karaoke venue on Bodrum's bar street is one of the unusual stops preferred by both foreign tourists and local residents for a fun night. The archive system loaded with Turkish and English song lists waits with an open door for everyone seeking a moment to shine on stage.",
    't': "Rezervasyon şart değil ama yoğun gecelerde özel odalar hızla dolar; grup planı yapıyorsanız önceden arayın.",
    'te': "A reservation is not required but private rooms fill quickly on busy nights; call ahead if you are planning as a group."},

126: {'d': "Bodrum'un bar sokağında yoğun sezon boyunca Türkçe ve İngilizce şarkı arşiviyle ziyaretçileri sahnede buluşturan bu karaoke kulübü, hem Bodrum sakinleri hem turistler için geç saatte eğlenceli bir gece programı seçeneği sunar. Grup rezervasyonları için özel odalar mevcuttur.",
    'de': "This karaoke club on Bodrum's bar street brings visitors together on stage with its Turkish and English song archive throughout the busy season, offering a fun late-night program option for both Bodrum residents and tourists. Private rooms are available for group reservations.",
    't': "Grup rezervasyonu için en az bir gün önceden iletişime geçin; özel içecek paketi seçenekleri de mevcut.",
    'te': "Contact at least one day in advance for a group reservation; private drinks package options are also available."},

127: {'d': "Bodrum Marina yakınındaki Catamaran Club, günübirlik katamaran turlarının yanı sıra haftalık kiralama ve yelken kursları da düzenleyen kapsamlı bir denizcilik merkezi olarak öne çıkar. Sabah saat 9'da körfezden açılan katamaran turu; Karaada, Orak Adası ve Gümüşlük koyu gibi Bodrum'un mavi durağlarına ulaşmanın en serinliği içindeki yoludur.",
    'de': "Near Bodrum Marina, Catamaran Club stands out as a comprehensive maritime center that organizes not only day catamaran tours but also weekly rentals and sailing courses. The catamaran tour departing from the bay at 9am is the most refreshing way to reach Bodrum's blue stops like Kara Island, Orak Island, and Gümüşlük cove.",
    't': "Tur kapasitesi sınırlı; Temmuz-Ağustos için 1 hafta önceden rezervasyon zorunlu olabilir.",
    'te': "Tour capacity is limited; reservation may be required 1 week in advance for July-August."},

128: {'d': "Yalıkavak Marina'nın vitrinindeki PORTO, akşam saatlerinde canlı DJ müziği ve uluslararası kokteyl menüsüyle marinayı bir gece eğlence üssüne dönüştüren en iddialı adreslerden biridir. Açık terasından izlenen marina manzarası ve mega yat silüetleri, içkinin yanında ek bir lezzet katar.",
    'de': "PORTO at the front of Yalıkavak Marina is one of the most ambitious addresses that transforms the marina into a nightlife hub in the evenings with live DJ music and an international cocktail menu. The marina view and mega yacht silhouettes seen from the open terrace add an extra flavor alongside the drinks.",
    't': "Happy hour 19-21 arası; en iyi yer manzaralı köşe masalarıdır. Uzun bekleyişten kaçmak için önceden masa ayırtın.",
    'te': "Happy hour runs from 7-9pm; the best spots are corner tables with a view. Book a table in advance to avoid a long wait."},

130: {'d': "Bodrum'un bar sokağında sezonun en kalabalık mekanlarından biri olan WI Club, yurt içi ve yurt dışından DJ'lerin sahne aldığı büyük kapasiteli açık hava eğlence alanıyla Bodrum gece hayatının simgesi haline gelmiştir. Ses ve ışık düzeni teknik olarak bölgedeki en gelişmiş kurulumlardan birini temsil eder.",
    'de': "WI Club, one of the busiest venues on Bodrum's bar street during the season, has become an icon of Bodrum nightlife with its large-capacity open-air entertainment area where domestic and international DJs perform. Its sound and lighting setup represents one of the most technically advanced installations in the area.",
    't': "Bilet fiyatları DJ kadrosuna göre değişir; yüksek profilli gecelerde ön satış biletleri günlerce önceden tükeniyor.",
    'te': "Ticket prices vary according to the DJ lineup; pre-sale tickets for high-profile nights sell out days in advance."},

133: {'d': "Bodrum gece hayatının sabaha karşı canlanan saatlerinin adresi olan Sobe Gaga, after-party anlayışıyla özellikle ana mekanların kapandıktan sonra partisini sürdürmek isteyen kitleye hitap eder. Sezonun en uzun süre açık kalan kulübü olarak sabah saatlerine kadar DJ müziğiyle çalışmaya devam eder.",
    'de': "Sobe Gaga, the address of Bodrum nightlife's hours that come alive toward dawn, caters to the crowd wanting to continue their party especially after the main venues close with an after-party concept. Continuing to operate with DJ music until the morning hours, it is the season's longest-running club.",
    't': "Gece 02:00'den önce gelmenize gerek yok; mekanın en canlı hali gece 03:00'den sonra yaşanır.",
    'te': "No need to arrive before 2am; the venue's liveliest period comes after 3am."},

136: {'d': "Roberto Cavalli'nin dünya genelindeki eğlence mekanlarından birinin Bodrum versiyonu olan Cavalli, Yalıkavak Marina'nın en lüks ve en tasarım odaklı gece kulübü unvanını taşır. Altın detaylı iç mekanı, moda endüstrisinden isimlerin sahne aldığı DJ geceleri ve VIP servisiyle marina yaşamını bir üst statüye taşır.",
    'de': "The Bodrum version of one of Roberto Cavalli's worldwide entertainment venues, Cavalli holds the title of Yalıkavak Marina's most luxurious and design-focused nightclub. With its gold-detailed interior, DJ nights featuring names from the fashion industry, and VIP service, it elevates marina life to a higher status.",
    't': "Dress code katı uygulanır; spor giyim ve terlik kesinlikle kabul edilmez. VIP masa için haftalar öncesinden rezervasyon yapın.",
    'te': "Dress code is strictly enforced; sportswear and flip-flops are definitely not accepted. Make a VIP table reservation weeks in advance."},

155: {'d': "Bodrum Marina girişindeki Poseidon Port buluşma noktası, tur teknelerinin, feribot yolcularının ve sahil gezginlerinin kesiştiği canlı bir kavşaktır. Tekne turlarına biniş-iniş noktası olarak işlev görmesinin yanı sıra akşam saatlerinde taze dondurma satıcıları ve sokak müzisyenleriyle renkli bir sahile dönüşür.",
    'de': "The Poseidon Port meeting point at the entrance to Bodrum Marina is a lively junction where tour boats, ferry passengers, and waterfront strollers converge. Beyond functioning as a boarding and disembarking point for boat tours, it transforms into a colorful scene in the evenings with fresh ice cream vendors and street musicians.",
    't': "Tekne turu satın alımlarında liman acentalarını karşılaştırın; aynı güzergah için fiyat ve kalite farkı önemli olabilir.",
    'te': "Compare harbor agencies when purchasing a boat tour; price and quality differences for the same route can be significant."},

156: {'d': "Bodrum'un yelken ve denizcilik dünyasında tanınan bir isim olan Fahri Çetinkaya, aynı zamanda özel tekne kiralama ve kaptanlık hizmetleri veren bir Bodrum köklüsüdür. Yarımadanın en bilgili kılavuz kaptanlarından biri olarak, daha az bilinen koylara ve alternatif mavilerin rotasına yönlendirebilir.",
    'de': "Fahri Çetinkaya, a well-known name in Bodrum's sailing and maritime world, is also a Bodrum native providing private boat rental and captaincy services. As one of the peninsula's most knowledgeable pilot captains, he can guide you to lesser-known coves and the route of alternative blue destinations.",
    't': "Bireysel ya da özel grup turu için doğrudan iletişime geçin; sabit program yoktur, tamamen kişiye özel bir deneyim sunar.",
    'te': "Contact directly for an individual or private group tour; there is no fixed program, offering a completely tailor-made experience."},

157: {'d': "Bodrum'un iç kesimlerinde, kentin gürültüsünden uzakta doğanın içinde doğal ürünler üreten Ergin Farm, kendi zeytinlik ve meyve bahçesinden elde ettiği soğuk sıkım zeytinyağı, pekmez ve reçel çeşitleriyle ziyaretçilere Ege kırsalının en taze tadını sunar.",
    'de': "Ergin Farm, producing natural products in the midst of nature away from the town's noise in Bodrum's hinterland, offers visitors the freshest taste of the Aegean countryside with cold-pressed olive oil, molasses, and jam varieties obtained from its own olive grove and fruit orchard.",
    't': "Ziyaret öncesi irtibata geçin; hasat sezonlarında (ekim-kasım için zeytin) çiftlik turu ve zeytinyağı yapımını izleme imkânı sunuluyor.",
    'te': "Contact before visiting; during harvest seasons (October-November for olives), farm tours and olive oil production observation opportunities are offered."},

162: {'d': "Bodrum yarımadasının en yüksek noktalarından birine tırmanan bu seyir tepesi, tan vaktinde pembe-altın renklerine bürünen Ege manzarasını, körfezi ve uzakta Kos Adası silüetini tek çerçevede sunar. Sabah 05:30-06:30 arasında çekilen gün doğumu fotoğrafları, Bodrum'un en eşsiz perspektiflerinden birini oluşturur.",
    'de': "This viewpoint climbing to one of the highest points of the Bodrum peninsula presents the Aegean view in pink-gold hues at dawn, the bay, and the distant silhouette of Kos Island in a single frame. Sunrise photos taken between 5:30 and 6:30am constitute one of Bodrum's most unique perspectives.",
    't': "Gün doğumundan en az 30 dakika önce yola çıkın; tepeye yürüyüş 20-25 dakika sürer ve bazı bölümler karanlıkta olabilir.",
    'te': "Set out at least 30 minutes before sunrise; the walk to the top takes 20-25 minutes and some sections may be in darkness."},

163: {'d': "Yalıkavak tepelerinden birinde yer alan bu belveder noktası, güneşin Ege'ye battığı anı, altın saatini ve hemen ardından gökyüzünü kaplayan leylak tonlarını izlemek için Bodrum'un en popüler akşam seyir noktalarından biridir. Her akşam bir düzine fotoğrafçı ve çiftin buluştuğu bu tepe, sessizliğiyle bile başlı başına bir deneyim sunar.",
    'de': "Located on one of Yalıkavak's hills, this belvedere point is one of Bodrum's most popular evening viewpoints for watching the moment the sun sets into the Aegean, the golden hour, and the lavender tones that immediately fill the sky. This hilltop where a dozen photographers and couples meet each evening offers a complete experience in its silence alone.",
    't': "Gün batımından 1 saat önce gelinmesi önerilen bu nokta için araç ile gidiliyorsa park yeri oldukça sınırlı.",
    'te': "This point is recommended to visit 1 hour before sunset; if going by car, parking is very limited."},

164: {'d': "Yalıkavak'ın kuzey kıyısındaki bu halk plajı, ücretli özel plaj kulüplerine alternatif arayan ziyaretçilere ücretsiz, temiz ve ulaşılabilir bir sahil deneyimi sunar. Berrak sığ suları aile grupları ve çocuklar için idealdir; plaj girişinde kiralık şemsiye ve şezlong da mevcuttur.",
    'de': "On Yalıkavak's northern coast, this public beach offers visitors seeking an alternative to paid private beach clubs a free, clean, and accessible coastal experience. The clear shallow waters are ideal for family groups and children; rental umbrellas and sun loungers are also available at the beach entrance.",
    't': "Sabah 09:00 öncesi en sakin ve en temiz zamandır; öğleden sonra kalabalık artar.",
    'te': "Before 9am is the quietest and cleanest time; crowds increase in the afternoon."},

165: {'d': "Yalıkavak kıyısındaki bu plaj ve liman alanı, doğal bir koy yapısında günübirlik tekne çıpası ve hafif dalış için elverişli özelliklere sahiptir. Küçük çakıl ve kum karışımı kıyısıyla aile tatilinin sakin bir alternatifidir; yakınındaki küçük kafeler de rahatlama için uygundur.",
    'de': "This beach and harbor area on the Yalıkavak coast is naturally suited for day-use boat anchoring and light diving within a natural cove structure. With its small pebble and sand mixed shore, it is a quiet alternative for a family holiday; nearby small cafés are also suitable for relaxation.",
    't': "Tekne çıpası için en iyi pozisyon koyun güneye bakan iç tarafıdır; akşam rüzgarından korunumluyken sığ ve berrak kalır.",
    'te': "The best anchoring position for a boat is the south-facing inner side of the cove; it remains shallow and clear while protected from the evening wind."},

166: {'d': "Yalıkavak'ın seyrek ziyaret edilen koyları arasındaki bu plaj, plaj kulübü düzeninin dışında kalmak isteyenler için kum, güneş ve temiz denizin en sade halini sunuyor. Özellikle sezon dışında neredeyse tenha olan bu plaj, dinginliği seven gezginlerin sığınağıdır.",
    'de': "This beach among Yalıkavak's sparsely visited coves offers the most understated form of sand, sun, and clean sea for those wishing to stay outside the beach club arrangement. Almost deserted especially off-season, this beach is a refuge for travelers who love tranquility.",
    't': "Sezon dışında (Eylül-Ekim) bu plaj gerçek huzurunu yaşar; deniz hâlâ yüzmeye yeter sıcaklıkta olur.",
    'te': "Off-season (September-October) this beach lives its true tranquility; the sea is still warm enough for swimming."},

167: {'d': "Bodrum yarımadasının batı uçlarından birine uzanan Öykümnaz Sivrikaya Koyu, etrafı sarmalayan çam ağaçları ve berrak Ege suları ile günübirlik tekne turlarının favori çıpa noktalarından biridir. Koyun küçük sahilinde kumsalda yemek yemek ya da yüzmek için saatlerce kalabilirsiniz.",
    'de': "Öykümnaz Sivrikaya Cove extending to one of the western tips of the Bodrum peninsula is one of the favorite anchoring spots for day-use boat tours with its surrounding pine trees and clear Aegean waters. You can stay for hours on the cove's small beach to eat on the sand or swim.",
    't': "Koya yalnızca tekneyle ulaşılabilir; Bodrum ve Yalıkavak'tan düzenlenen günlük tur programlarında yer alır.",
    'te': "The cove is accessible only by boat; it is included in daily tour programs organized from Bodrum and Yalıkavak."},

168: {'d': "Bodrum şehrinin tepesine hakim olan bu Osmanlı dönemi yel değirmenleri, uzaktan bakıldığında Bodrum silüetinin en tanınmış öğelerinden birini oluşturur. Günbatımında çarklarının arkasından süzülen kızıl ışık ve aşağıda yayılan körfez manzarası, Bodrum fotoğrafçılığının klasiklerinden biridir.",
    'de': "These Ottoman-era windmills dominating the hilltop above Bodrum town form one of the most recognizable elements of Bodrum's silhouette when viewed from a distance. The red light filtering through their blades at sunset and the bay panorama spread below are among the classics of Bodrum photography.",
    't': "Yel değirmenlerine ulaşmak için Bodrum merkezinden 20 dakika yürüyüş veya taksiyle çıkış; gün batımından 1 saat önce yukarıda olun.",
    'te': "Reaching the windmills requires a 20-minute walk from Bodrum center or a taxi; be up there 1 hour before sunset."},

169: {'d': "Yalıkavak'ın Feraya Hanım Koyu, etrafındaki kayalıklar ve derin mavi rengiyle tekne sahiplerinin sığındığı bir küçük cennet parçasıdır. Adını eski bir yerel aileye borçlu olan koy, küçük ve sığ sahiliyle çocuklar ve yüzücüler için de güvenli bir ortam sunar.",
    'de': "Feraya Hanım Cove in Yalıkavak is a small piece of paradise where boat owners take refuge, with its surrounding rocks and deep blue. Named after an old local family, the cove with its small shallow beach also provides a safe environment for children and swimmers.",
    't': "Koya tekne veya kayak ile gidilir; Yalıkavak Marina'dan organize edilen saatlik kayak kiralama servisi mevcuttur.",
    'te': "The cove is reached by boat or kayak; hourly kayak rental service organized from Yalıkavak Marina is available."},

170: {'d': "Yalıkavak kıyısındaki bu plaj, uzun plaj şeridi ve çakıl-kum karışımı yüzeyiyle Yalıkavak'ın en ulaşılabilir sahillerinden biridir. Fiziksel aktivite tutkunları için sabah erken saatlerde yürüyüş, yüzme ve açık deniz egzersizi için de tercih edilen bir noktadır.",
    'de': "This beach on the Yalıkavak coast is one of Yalıkavak's most accessible shores with its long beach strip and pebble-sand mixed surface. It is also a preferred point for physical activity enthusiasts for early morning walking, swimming, and open-water exercise.",
    't': "Sabah 07:00-09:00 arası yürüyüş için neredeyse boş olan plaj; günün geri kalanında kalabalık artar.",
    'te': "The beach is almost empty for walking between 7 and 9am; crowds increase for the rest of the day."},

171: {'d': "Yalıkavak'ın marina bölgesindeki bu butik otel, dört ayrı konu konseptiyle tasarlanmış odaları ve çatı katındaki panoramik havuzuyla marinayı 360 derece seyreden nadir tesisler arasındadır. Modern sanat eserleri ve kişiselleştirilmiş servis anlayışıyla tasarım turizmine ilgi duyan ziyaretçiler için biçilmiş kaftandır.",
    'de': "This boutique hotel in Yalıkavak's marina district is among the rare facilities that overlooks the marina 360 degrees with its rooms designed around four different theme concepts and rooftop panoramic pool. With modern artworks and a personalized service approach, it is tailor-made for visitors interested in design tourism."},

176: {'d': "Gümüşlük Mahallesi'ndeki bu şarküteri ve ızgara mezeleri mekânı, mandıra peyniri, ev yapımı sosis ve Ege otlarıyla tatlandırılmış zeytinleriyle hafif bir akşam atıştırması ya da piknik alışverişi için Gümüşlük'ün en keyifli duraklarından biridir.",
    'de': "This delicatessen and grilled mezze spot in Gümüşlük neighborhood is one of Gümüşlük's most enjoyable stops for a light evening snack or picnic shopping, with its dairy cheeses, homemade sausage, and olives seasoned with Aegean herbs."},

177: {'d': "Bodrum'a yakın konumuyla Çimentepe Apart Otel, uzun dönem tatil planlayanlar ya da ailelerin çocuklarla gelmesi için pratik mutfaklı apart odalarıyla uygun maliyetli ve bağımsız bir konaklama ortamı sunar. Toplu taşıma ile Bodrum merkeze ulaşım kolaydır.",
    'de': "With its location close to Bodrum, Çimentepe Apart Otel offers a cost-effective and independent accommodation environment with practical kitchenette apart rooms for those planning long holidays or families coming with children. Public transport access to central Bodrum is easy."},

178: {'d': "Gümüşlük'ün mütevazı ama efsane balıkçı restoranlarından biri olan Balıkçı Hasan'ın Yeri, sabah erken satte gelen pazartarlık balıklardan oluşan günlük menüsüyle yıllardır bölge halkının kalbinde ayrıcalıklı bir yere sahiptir. Mangal balığı ve haşlama ahtapot Gümüşlük'ün en özgün lezzetleri arasında sayılır.",
    'de': "One of Gümüşlük's humble yet legendary fish restaurants, Balıkçı Hasan'ın Yeri has held a special place in the hearts of local residents for years with its daily menu composed of early-morning market-negotiated fish. Grilled fish and boiled octopus rank among Gümüşlük's most authentic flavors."},

183: {'d': "Bodrum'un üst mahalle restoranları arasında öne çıkan Indigo, Ege mezeleri, taze balık ve yaratıcı kokteyl listesiyle hem öğle hem akşam için tercih edilen kalıcı bir adres haline gelmiştir. Açık teras ve iç mekan seçenekleriyle farklı hava koşullarında kullanılabilir esneklik sunar.",
    'de': "Standing out among Bodrum's upper neighborhood restaurants, Indigo has become a permanent address preferred for both lunch and dinner with its Aegean mezze, fresh fish, and creative cocktail list. It offers flexibility usable in different weather conditions with open terrace and indoor options."},

185: {'d': "İspanyol ismi ve Akdeniz mutfağı ilhamıyla Bodrum'da özgün bir konum edinen Sevilla Çakıroğlu Restaurant, hem yerel halkın hem de yabancı ziyaretçilerin sofra deneyimini zenginleştiren karma menüsüyle dikkat çeker. Ege zeytinyağı kültürüyle İspanya'nın tapas ruhunu harmanlayan tabaklar, yaratıcı bir mutfak yorumu sunar.",
    'de': "Having established a unique position in Bodrum with its Spanish name and Mediterranean cuisine inspiration, Sevilla Çakıroğlu Restaurant attracts attention with its mixed menu that enriches the dining experience of both locals and foreign visitors. Plates blending Aegean olive oil culture with Spain's tapas spirit offer a creative culinary interpretation."},

186: {'d': "Bodrum'un panoramik manzara noktalarından birinde konumlanan bu mekan, hem körfezi hem de karşı kıyıları kapsayan geniş seyir açısıyla akşam yemeğini görsel bir şölene dönüştürür. Türk mutfağı ile Ege deniz ürünlerini harmanlayan menüsü ve özenli servis anlayışıyla sezon boyunca tercih edilen bir adrestir.",
    'de': "Located at one of Bodrum's panoramic viewpoints, this venue transforms dinner into a visual feast with its wide viewing angle covering both the bay and the opposite shores. It is a seasonally preferred address with its menu blending Turkish cuisine with Aegean seafood and an attentive service approach."},

188: {'d': "Bodrum'un Kavaklı semtindeki bu fast food noktası, bölgenin sevilen köfte ustası Kavaklı'nın hazırladığı ızgara et sandviçleri ve kübik köftesiyle yerel halkın hızlı ve doyurucu öğün ihtiyacına cevap verir. İnce baharatlı bir köfte deneyimi için bölgedeki en pratik adresten biridir.",
    'de': "This fast food point in Bodrum's Kavaklı neighborhood meets the local population's need for a quick and filling meal with the grilled meat sandwiches and cube köfte prepared by the region's beloved köfte master Kavaklı. It is one of the most practical addresses in the area for a finely spiced köfte experience."},

189: {'d': "Yalıkavak'ın marina çevresindeki Caba Restaurant, Türk usulü tekel ve mezeleri İspanyol tapas kültürüyle buluşturan eklektik menüsüyle farklı damak tatlarına aynı anda hitap eder. Akşamları canlı müzik ve açık teras seçeneğiyle Yalıkavak'ın en samimi sosyal restoranlarından biri olarak bilinir.",
    'de': "Caba Restaurant around Yalıkavak's marina simultaneously appeals to different palates with its eclectic menu that brings Turkish monopoly and mezze together with Spanish tapas culture. Known as one of Yalıkavak's most authentic social restaurants with live music and an open terrace option in the evenings."},

191: {'d': "Belediye işletmesindeki bu iskele kafesi, Yalıkavak'ın en sakin deniz kıyısına çıkmadan içinde oturulan, berrak suların sesi eşliğinde kahve ya da simit yenilebilen sade ama tatmin edici bir mola sunuyor. Tekne turu bekleyişi ya da akşam serinliğinde bir bardak çay için en pratik nokta.",
    'de': "This municipality-operated pier café offers a simple but satisfying break where you can sit inside at Yalıkavak's calmest waterfront, sipping coffee or eating simit to the sound of clear waters. The most practical spot for waiting for a boat tour or for a glass of tea in the evening cool."},

192: {'d': "İstanbul'dan gelen Haremlique'nin Yalıkavak Marina şubesi, Osmanlı-Bohem estеtiğini marina ortamıyla buluşturan dekorasyonu ve el yapımı nevresim ve tekstil ürünleriyle hem alışveriş hem de mağaza içi deneyim için özgün bir adres sunar. Tasarım tutkunları için marina gezisinin keşfedilmeye değer köşelerinden biridir.",
    'de': "The Yalıkavak Marina branch of Istanbul's Haremlique offers a unique address for both shopping and an in-store experience with its decoration that brings Ottoman-Bohemian aesthetics together with a marina setting and handmade duvet covers and textile products. One of the marina walk's corners worth discovering for design enthusiasts."},

193: {'d': "Yalıkavak Marina çevresindeki bu yakıt istasyonu, uzun yaz sezonunun koşturmacasında marina çevresinde günlük ihtiyaçlarını karşılamak isteyen tekne sahipleri, tatilciler ve yolda olanlar için pratik bir uğrak noktasıdır. Kafesi ve marketi ile marina çevresinin gece gündüz açık sağlık noktaları arasındadır.",
    'de': "This fuel station near Yalıkavak Marina is a practical stopping point for boat owners, holidaymakers, and those on the road wanting to meet their daily needs around the marina during the long summer season's rush. With its café and market, it is among the round-the-clock convenience points of the marina area."},
}

apply_batch('bodrum.json', U)
