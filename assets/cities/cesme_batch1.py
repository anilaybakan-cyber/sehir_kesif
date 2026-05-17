import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
0:  {'t': "Kale müzesi hafta içi sabah 09:00-17:00 arası açıktır; cuma namazı saatlerinde kapanabilir. Kale surlarının üstünden Sakız Adası'nı görmek için berrak hava şart.",
     'te': "The castle museum is open weekdays 9am-5pm; it may close during Friday prayer. Clear weather is essential to see Chios island from the castle walls."},

1:  {'t': "Alaçatı Çarşı, özellikle Temmuz-Ağustos hafta sonları taşıp akar; sabah 09:00-11:00 arası ya da öğleden sonra 16:00 sonrası daha sakin gezebilirsiniz.",
     'te': "Alaçatı Bazaar overflows especially on July-August weekends; you can browse more calmly between 9-11am or after 4pm."},

2:  {'t': "Değirmenlerin önündeki taş kaldırım ve tepe manzarası için altın saat fotoğrafçılığına uygun; gün batımında ışık tepeden vurur ve taşların rengi değişir.",
     'te': "Golden hour photography suits the cobblestone path in front of the mills and hilltop view; at sunset the light hits from above and the stones change color."},

3:  {'t': "Marina'da tekne kiralama için Haziran-Eylül döneminde en az 1-2 gün önceden rezervasyon yapmanız gerekir; günlük fiyatlar sezona ve tekne tipine göre değişir.",
     'te': "For boat rental at the marina, book at least 1-2 days ahead during June-September; daily prices vary by season and boat type."},

5:  {'t': "Ayayorgi Yolu'nda güneş batarken yürüyüş yapmak Çeşme'nin en romantik deneyimlerinden biridir; rahat spor ayakkabı giyin çünkü bazı bölümler taşlık.",
     'te': "Walking the Ayayorgi Path at sunset is one of Çeşme's most romantic experiences; wear comfortable shoes as some sections are rocky."},

7:  {'t': "Pırlanta Plajı'nın doğu ucu çoğunlukla daha az kalabalıktır; öğle sonrası 14:00'dan itibaren gelin, rüzgar bu saatte rölanti yapar ve deniz sakinleşir.",
     'te': "The eastern end of Pırlanta Beach is usually less crowded; come from 2pm onwards as the wind eases at this hour and the sea calms."},

8:  {'t': "Dalyan Plaj'da öğle öncesi yerinizi alın; yazın plaj kısa sürede dolmaktadır. Gün içinde dükkanlarda taze limon ve reyhan karışımlı limonata deneyin.",
     'te': "Claim your spot at Dalyan Beach before noon; in summer the beach fills up quickly. During the day try the fresh lemon and basil lemonade from the shops."},

9:  {'t': "Boyalık Plajı, Çeşme merkezine 3 km uzaklıkta; minibüsle ulaşabilirsiniz. Rüzgarlı günlerde dalgalar biraz sertleşir, küçük çocuklar için batı ucundaki sığ bölge daha güvenlidir.",
     'te': "Boyalık Beach is 3 km from Çeşme center; accessible by minibus. On windy days the waves get a bit rough; the shallow western end is safer for young children."},

10: {'t': "Paşalimanı koyuna tekneyle ya da yürüyüş yoluyla ulaşılabilir; plaj kafe ve şezlong yok, doğal yapısını koruyor. Yiyecek ve içecek yanınızda getirin.",
    'te': "Paşalimanı cove is accessible by boat or on foot; no beach café or sun loungers, it preserves its natural state. Bring your own food and drinks."},

11: {'t': "Germiyan köyü Çeşme ilçesine 12 km uzaklıkta; araçla ulaşmak en kolay seçenek. Köy içindeki küçük kahvaltı bahçelerinde sabah molası için mükemmel bir yer.",
    'te': "Germiyan village is 12 km from Çeşme district; the easiest option is by car. The small breakfast gardens inside the village are a perfect place for a morning break."},

12: {'t': "Erythrai Tiyatrosu, Ildırı köyünün içindedir; köye araçla ulaşıp sonra yürüyerek gidin. Yazın öğle üstü sıcaklıkta ziyaret etmekten kaçının, sabah 09:00-11:00 idealdir.",
    'te': "Erythrai Theatre is inside Ildırı village; drive to the village and then walk. Avoid visiting in midday summer heat; 9-11am is ideal."},

15: {'t': "Before Sunset Beach Kulübü'nde şezlong rezervasyonu önceden yapılabilir; günbatımı saatlerinde (18:00-20:00) yer bulmak çok güçleşir.",
    'te': "Sun lounger reservation at Before Sunset Beach Club can be made in advance; finding a spot during sunset hours (6-8pm) becomes very difficult."},

19: {'t': "Sole & Mare Beach Club yazın minimum konsomüsyon uygulamaktadır; Temmuz-Ağustos için haftanın ilk günlerinde rezervasyon daha kolay alınır.",
    'te': "Sole & Mare Beach Club applies a minimum consumption charge in summer; reservations are easier to get on weekdays in July-August."},

23: {'t': "Marin Alaçatı sezon boyunca özellikle hafta sonları kapasitesine çabuk ulaşır; akşam yemeği için en az 2-3 gün önceden rezervasyon alın.",
    'te': "Marin Alaçatı quickly reaches capacity especially on weekends throughout the season; reserve at least 2-3 days ahead for dinner."},

24: {'t': "Hacımemiş Mahallesi'nin dar taş sokaklarında öğle sonrası gezinti yapın; sabahın ilk saatlerinde dükkanlar henüz açılmamış olabilir, öğleden sonra tüm dükkanlar hizmet verir.",
    'te': "Stroll through Hacımemiş Neighborhood's narrow stone streets in the afternoon; in early morning hours shops may not yet be open, all shops serve in the afternoon."},

41: {'t': "Çiftlik köyündeki bu küçük cami tarihi mimarisini korumaktadır; ziyaret için başörtüsü ve ayakkabı çıkarma adabına uyun. Köye araçla giderken dar yolları dikkate alın.",
    'te': "This small mosque in Çiftlik village preserves its historic architecture; observe headscarf and shoe-removal etiquette for a visit. Be mindful of narrow roads when driving to the village."},

43: {'t': "Çeşme Turistik Otelciler Birliği, konaklama seçenekleri ve bölge etkinlikleri hakkında ücretsiz bilgi sunar; turizm ofisi saatlerinde uğrayabilirsiniz.",
    'te': "The Çeşme Tourism Hoteliers Association offers free information about accommodation options and regional events; you can stop by during tourism office hours."},

44: {'t': "Aqua Toy City sezonluk olarak açık; Haziran-Eylül arası aktiftir. Hafta içi ziyaret daha az kalabalıktır; online bilet alımı kapı fiyatından daha ucuzdur.",
    'te': "Aqua Toy City is seasonally open; active between June-September. Weekday visits are less crowded; purchasing tickets online is cheaper than at the door."},

45: {'t': "Kethüda Çeşmesi, Çeşme kale meydanının yakınındadır; tarihi çeşmenin önünde kısa bir dinlenme molası için güzel bir köşe. Çeşme suları içilebilir niteliktedir.",
    'te': "Kethüda Fountain is near Çeşme castle square; a nice corner for a short rest in front of the historic fountain. The fountain waters are drinkable."},

46: {'t': "Küçük Asya kaynaklı bu tarihi çeşme, eski Rum mahallesi dokusunu yansıtır; etrafındaki tarihi yapılarla birlikte kısa bir fotoğraf turu için değerli bir köşe.",
    'te': "This historic fountain of Asia Minor origin reflects the texture of the old Greek neighborhood; a valuable corner for a short photography tour together with the surrounding historic buildings."},

47: {'t': "Küçük Cami, Çeşme merkezinde kolay bulunur; namaz vakitlerinde ziyaretçi kabul etmez. Çarşamba ve Cumartesi sabahları çevre pazar günleriyle birlikte ziyaret için ideal.",
    'te': "The Small Mosque is easily found in Çeşme center; it does not accept visitors during prayer times. Wednesday and Saturday mornings are ideal to visit together with the surrounding market days."},

48: {'t': "Ayios Haralambos Kilisesi, Çeşme'nin Rum mirasının önemli parçalarından biridir; restorasyon süreçleri nedeniyle ziyaret saatlerini önceden kontrol edin.",
    'te': "Ayios Haralambos Church is one of the important pieces of Çeşme's Greek heritage; check visiting hours in advance due to ongoing restoration processes."},

49: {'t': "Cezayirli Hasan Paşa Anıtı, Çeşme Marina yakınında bulunmaktadır; deniz yürüyüşü sırasında kolayca ziyaret edebilirsiniz. Anıtın önündeki meydan akşamları yerel halkla canlanır.",
    'te': "The Cezayirli Hasan Pasha Monument is located near Çeşme Marina; you can easily visit it during a waterfront walk. The square in front of the monument comes alive with locals in the evenings."},

50: {'t': "Dinlenme terasları özellikle ilkbahar ve sonbaharda deniz manzarası için idealdir; yaz aylarında güneşten korunmak için öğleden sonra 16:00'dan sonra gelin.",
    'te': "The rest terraces are ideal for sea views especially in spring and autumn; in summer months come after 4pm to protect from the sun."},

51: {'t': "I. Kaplan Giray Han Heykeli, Çeşme Kalesi yakınındadır; tarihi kale turu ile birlikte ziyaret edilmesi için pratik bir güzergah oluşturur.",
    'te': "The Khan Kaplan Giray I Monument is near Çeşme Castle; it forms a practical route to visit together with the historic castle tour."},

52: {'t': "CesmeCity.Com, bölgeye ait pratik yerel bilgi kaynağıdır; Çeşme ve Alaçatı'daki açık mekanlar, etkinlikler ve yerel tavsiyeler için faydalı bir dijital kaynak.",
    'te': "CesmeCity.Com is a practical local information resource for the area; a useful digital resource for open venues, events, and local recommendations in Çeşme and Alaçatı."},

53: {'t': "Çeşme Merkez Meydanı'nda akşam saatlerinde yerel halkın paseo (yürüyüş) ritüeli yaşanır; bu saatlerde meydan etrafındaki kafeler dolup taşar. Deniz kenarındaki masalar için erken gelin.",
    'te': "In the evening, the local paseo (promenade) ritual takes place in Çeşme Central Square; the cafés around the square fill up at this time. Arrive early for tables by the sea."},

54: {'t': "Güneşlenme Terası, Çeşme Marina bölgesinde yer alır; sabah erken saatlerde yer bulmak kolaydır. Öğleden sonra kalabalık artar, güneş kremi ve havlu yanınızda olsun.",
    'te': "The Sunbathing Terrace is located in Çeşme Marina area; it is easy to find a spot in the early morning. It gets crowded in the afternoon; have sunscreen and a towel with you."},

55: {'t': "Alaçatı Meydanı'nın etrafındaki taş binalarda küçük butikler ve el sanatları dükkanları bulunur; sabah 10:00-12:00 arası alışveriş için en sakin saatlerdir.",
    'te': "Small boutiques and handicraft shops are found in the stone buildings around Alaçatı Square; between 10am-12pm are the quietest hours for shopping."},

56: {'t': "Bu tarihi heykel veya anıtı ziyaret ederken çevresindeki tarihi dokuyı da keşfedin; Çeşme'nin kültürel miras haritasında önemli bir nokta olarak değerlendirin.",
    'te': "While visiting this historic statue or monument, explore the historic fabric around it; consider it as an important point on Çeşme's cultural heritage map."},

57: {'t': "Nirvana Tekne Turu için sabah kalkışlı günlük turlar mevcut; Eylül ayı turlarında kalabalık azalır ve fiyatlar düşer. Öğle yemeği tekne üzerinde servis edilir.",
    'te': "Daily tours with morning departure are available for Nirvana Boat Tour; in September tours crowds decrease and prices drop. Lunch is served on the boat."},

58: {'t': "Tekke Plaj'a araçla ulaşmak güçtür; tekne veya deniz taksi seçeneğini kullanmak hem kolay hem de manzaralıdır. Plajda tesis yoktur, gerekli her şeyi yanınızda getirin.",
    'te': "It is difficult to reach Tekke Beach by car; using a boat or sea taxi option is both easy and scenic. There are no facilities at the beach; bring everything you need."},

59: {'t': "Casa ARK, Alaçatı'nın en samimi boutique oteli olarak bilinir; kahvaltı için rezervasyona sahip olmayan misafirlere sınırlı sayıda yer ayrılmaktadır, önceden arayın.",
    'te': "Casa ARK is known as Alaçatı's most intimate boutique hotel; a limited number of spots are reserved for guests without a breakfast reservation, call ahead."},

98: {'t': "Bedevi Ayayorgi Çeşme'de Paskalya haftasında canlanır; bu dönemde bölgeye özgü yerel dini törenler ve pazar günleri yapılır. Araçla girerken köy yollarına dikkat edin.",
    'te': "Bedevi Ayayorgi in Çeşme comes alive during Easter week; local religious ceremonies and market days unique to the region are held during this period. Be careful on village roads when entering by car."},

99: {'t': "Bu müzik ve eğlence mekanı Alaçatı'nın en hareketli gece durakları arasındadır; gece 23:00-03:00 saatleri en kalabalık dilimdir. Önceden konser programını kontrol edin.",
    'te': "This music and entertainment venue is among Alaçatı's liveliest night stops; 11pm-3am is the busiest period. Check the concert schedule in advance."},

100: {'t': "ZUM Alaçatı, çarşı içinde özenle hazırlanmış kokteyller ve yerel meze tabakları sunar; akşam yemeği için rezervasyon önerilir, şaraba eşlik eden peynir tahtası menüsünü deneyin.",
    'te': "ZUM Alaçatı serves carefully crafted cocktails and local mezze plates in the bazaar; reservation is recommended for dinner, try the cheese board menu accompanying the wine."},

101: {'t': "MERTPARADISE için önceden rezervasyon yapın; etkinlik günlerinde minimum konsomüsyon uygulanır. Sahil giriş saatleri ve fiyatları için sosyal medya sayfalarını takip edin.",
    'te': "Book in advance for MERTPARADISE; a minimum consumption charge applies on event days. Follow their social media pages for beach entry hours and prices."},

102: {'t': "Chilly Çeşme, Marina'ya yakın konumuyla yat tutkunlarının sevdiği bir mekandır; deniz tarafındaki masalar için akşam seansı rezervasyonu günler öncesinden alınmalıdır.",
    'te': "Chilly Çeşme is a venue loved by yacht enthusiasts thanks to its proximity to the Marina; sea-side table reservations for evening sessions must be made days in advance."},

103: {'t': "Escape Beach Alaçatı, rüzgar sporları için Alaçatı'nın en popüler alternatif sahillerinden biridir; rüzgarın en istikrarlı olduğu Haziran-Eylül arası kite ve windsurfer için ideal.",
    'te': "Escape Beach Alaçatı is one of Alaçatı's most popular alternative beaches for wind sports; June-September when the wind is most consistent is ideal for kite and windsurf."},

104: {'t': "Kalinda Inn, huzurlu ve küçük kapasiteli bir butik oteldir; sezon boyunca genellikle hızlı dolar. En az 2-3 hafta önceden rezervasyon yapmanız önerilir.",
    'te': "Kalinda Inn is a peaceful, small-capacity boutique hotel; it usually fills up quickly throughout the season. Booking at least 2-3 weeks in advance is recommended."},

106: {'t': "Alaçatı Borçın Su Sporları, rüzgara açık Alaçatı koyunda windsurf ve kitesurf dersleri verir; ön bilgi olmadan başlayabilirsiniz, ilk ders yaklaşık 2-3 saat sürer.",
    'te': "Alaçatı Borçın Water Sports gives windsurf and kitesurf lessons in Alaçatı's wind-exposed bay; you can start without prior knowledge, the first lesson takes approximately 2-3 hours."},

107: {'t': "Hacı Memiş Cami, Alaçatı Çarşı'nın merkezine yakın konumuyla yürüyüş sırasında uğrayabileceğiniz tarihi bir dini mekandır; namaz vakitleri dışında ziyaret edilebilir.",
    'te': "Hacı Memiş Mosque is a historic religious site close to the center of Alaçatı Bazaar that you can stop by during a walk; it can be visited outside prayer times."},

108: {'t': "Alaçatı Pazar Yeri Cami, haftalık Alaçatı pazarının kurulduğu alanın hemen yanında yer alır; Perşembe günü pazar kuruluşu sırasında bölge özellikle canlı ve fotoğrafçılık için zengindir.",
    'te': "Alaçatı Market Mosque is located right next to the area where the weekly Alaçatı market is set up; the area is particularly lively and rich for photography during the Thursday market setup."},

109: {'t': "Küçük Ev, Alaçatı'nın en gözde butik konaklama seçeneklerinden biridir; bahçesi ve taş duvarları ile özgün bir deneyim sunar. Erken rezervasyon şarttır, sezon boyunca genellikle dolu.",
    'te': "Küçük Ev is one of Alaçatı's most sought-after boutique accommodation options; offering an original experience with its garden and stone walls. Early reservation is essential, usually full throughout the season."},

110: {'t': "Telcabin, Çeşme yarımadasında deniz manzaralı teleferik deneyimi sunar; gün batımı saatlerinde hem ışık hem manzara açısından en ideal zaman dilimidir.",
    'te': "Telcabin offers a cable car experience with sea views on the Çeşme peninsula; sunset hours are the most ideal time slot both for light and scenery."},

111: {'t': "Alaçatı Sulak Alanı, sonbaharda ve ilkbaharda göç eden kuşların konakladığı doğa alanıdır; sabah 07:00-09:00 arası kuş gözlemi için en uygun saatlerdir. Dürbün getirmeniz önerilir.",
    'te': "Alaçatı Wetland is a nature area where migratory birds rest in autumn and spring; between 7-9am are the most suitable hours for birdwatching. Bringing binoculars is recommended."},

112: {'t': "Birds of Alaçatı, kuş gözlemi ve doğa alanı rehberli turlar için başvurulabilecek lokal bir kaynak; Alaçatı sulak alanındaki gözlem noktaları ve sezonluk kuş türleri hakkında bilgi edinebilirsiniz.",
    'te': "Birds of Alaçatı is a local resource for birdwatching and nature area guided tours; you can get information about observation points in Alaçatı wetland and seasonal bird species."},

114: {'t': "Oasis Aquapark, Çeşme'de aileler için popüler bir seçenektir; Temmuz-Ağustos yaz ortasında yoğun olduğundan hafta içi sabah girişi en sakin deneyimi sağlar. Online bilet alımı indirimli.",
    'te': "Oasis Aquapark is a popular option for families in Çeşme; as it is busy in mid-July-August, a weekday morning entry provides the calmest experience. Online ticket purchase is discounted."},

115: {'t': "Çeşme şehir merkezi, kalesi ve marinasıyla yürüyerek keşfedilebilir bir ölçektedir; otoyol trafiğinden uzak dar sokaklarda kaybolmak en iyi keşif yöntemidir.",
    'te': "Çeşme city center is walkable in scale with its castle and marina; getting lost in the narrow streets away from highway traffic is the best method of discovery."},

116: {'t': "Flu Alaçatı Tiny House Otel, küçük ve özgün mimarisiyle Alaçatı'nın butik konaklama kültürünü yansıtır; bahçe ve kahvaltı dahil rezervasyonlar için en az 3 hafta önceden yer ayırtın.",
    'te': "Flu Alaçatı Tiny House Hotel reflects Alaçatı's boutique accommodation culture with its small and original architecture; book at least 3 weeks in advance for garden and breakfast-included reservations."},

117: {'t': "Ilıca Plajı, Çeşme'nin en kalabalık ve en erişilebilir plajıdır; ücretsiz kamu bölümü ile ücretli plaj kulüpleri yan yana yer alır. Sabah 08:00-10:00 arasında yer bulmak çok kolaydır.",
    'te': "Ilıca Beach is Çeşme's most crowded and most accessible beach; the free public section and paid beach clubs are side by side. Finding a spot is very easy between 8-10am."},

119: {'t': "Monarch Girişi - Maja, Alaçatı'nın gece eğlence sahnesi için önemli bir referans noktasıdır; hafta sonu geceleri yoğun olduğundan önceden rezervasyon tavsiye edilir.",
    'te': "Monarch Entry - Maja is an important reference point for Alaçatı's nightlife scene; reservation is recommended in advance as weekend nights are busy."},

120: {'t': "Sunsurf Alaçatı, rüzgar koşullarına göre günlük dersler düzenler; rüzgarlı günlerde (Kuzey-Batı Meltem) en iyi windsurfing koşulları oluşur. Deneyim düzeyinize uygun ders programı için arayın.",
    'te': "Sunsurf Alaçatı organizes daily lessons based on wind conditions; the best windsurfing conditions form on windy days (Northwest Meltem). Call for a lesson program suitable for your experience level."},

156: {'t': "Giulia Alaçatı, Alaçatı Çarşı bölgesinde seçkin Akdeniz mutfağı sunan bir mekandır; akşam yemeği için rezervasyon önerilir, şaraplı tadım menüsü için önceden bilgi alın.",
     'te': "Giulia Alaçatı is a venue serving select Mediterranean cuisine in the Alaçatı Bazaar area; reservation is recommended for dinner, get information in advance about the wine tasting menu."},

158: {'t': "Bota Alaçatı, barı ve canlı müziğiyle Alaçatı'nın akşam saatlerinde tercih edilen mekanlarından biridir; Perşembe-Cumartesi geceleri özellikle hareketlidir.",
     'te': "Bota Alaçatı is one of Alaçatı's preferred evening venues with its bar and live music; Thursday-Saturday nights are particularly lively."},

159: {'t': "Perde Arkası Alaçatı, adından da anlaşılacağı üzere Alaçatı sahnesinin arka planını keşfetmek için ilginç bir duraktır; tiyatro ve sanat etkinlikleri için programı takip edin.",
     'te': "Perde Arkası Alaçatı is, as understood from its name, an interesting stop for discovering the backstage of the Alaçatı scene; follow the program for theater and art events."},

160: {'t': "Spois Alaçatı, spor ve aktif tatil arayanlar için organizasyonlar düzenler; kitesurftan bisiklet turuna geniş aktivite yelpazesi mevcuttur. Önceden program ve fiyat bilgisi alın.",
     'te': "Spois Alaçatı organizes activities for those seeking sports and active holidays; a wide activity range from kitesurfing to bicycle tours is available. Get program and price information in advance."},

161: {'t': "Bu gece kulübü, sezonun en yüksek döneminde Alaçatı'nın en kalabalık eğlence mekanları arasına girmektedir; yoğun gecelerde giriş için bekleme süresi uzun olabilir.",
     'te': "This nightclub is among Alaçatı's most crowded entertainment venues during the peak of the season; waiting time for entry on busy nights can be long."},

162: {'t': "The Barra Alaçatı, butik bar ortamı ve özel kokteylleriyle sakin bir akşam için iyi bir tercih; Alaçatı Çarşı içinde, yürüme mesafesinde diğer restoran ve barlara yakın konumda.",
     'te': "The Barra Alaçatı is a good choice for a quiet evening with its boutique bar atmosphere and special cocktails; located inside Alaçatı Bazaar, close to other restaurants and bars within walking distance."},

164: {'t': "G Lodge, Alaçatı'da sakin ve lüks bir konaklama deneyimi arayanlar için tercih edilen bir butik oteldir; havuz ve bahçeli alanları için özellikle Mayıs ve Eylül ayları en ideal dönemlerdir.",
     'te': "G Lodge is a boutique hotel preferred by those seeking a calm and luxurious accommodation experience in Alaçatı; May and September are the most ideal periods especially for the pool and garden areas."},

165: {'t': "Bi Nevi Alaçatı, küçük ölçekli ama özenli konseptiyle Alaçatı çarşı kültürünü yansıtır; yerel el işi ürünler ve seçilmiş tasarım eşyaları için keşfedilmesi gereken bir adres.",
     'te': "Bi Nevi Alaçatı reflects the Alaçatı bazaar culture with its small-scale but meticulous concept; an address to discover for local handicrafts and selected design items."},

166: {'t': "Two Sexy Fish Alaçatı, deniz ürünleri ve yaratıcı menüsüyle Alaçatı'nın gözde restoran adreslerinden biridir; hafta sonları için en az 2 gün önceden rezervasyon yapın.",
     'te': "Two Sexy Fish Alaçatı is one of Alaçatı's favorite restaurant addresses with seafood and a creative menu; make a reservation at least 2 days in advance for weekends."},

167: {'t': "Mirror Alaçatı, sosyal medyada sık görülen fotoğraf noktalarıyla Alaçatı'nın en çok paylaşılan mekanları arasındadır; öğleden sonra 15:00-17:00 arası ışık ve kalabalık açısından en dengeli saattir.",
     'te': "Mirror Alaçatı is among Alaçatı's most shared venues with frequently seen photo spots on social media; the most balanced hour for light and crowds is between 3-5pm."},

168: {'t': "ZUM Alaçatı'da şarap tadımı için bir sommelier eşliğinde menü oluşturabilirsiniz; yerel Ege bağlarından seçilmiş butik şaraplar için uzun oturum rezervasyonu yapın.",
     'te': "At ZUM Alaçatı you can create a menu with a sommelier for wine tasting; make a long session reservation for boutique wines selected from local Aegean vineyards."},

169: {'t': "Lessroom Alaçatı, minimalist ve özgün konseptiyle konaklama arayanlar için ilginç bir seçenek; kapasite sınırlı olduğundan sezon başında rezervasyon yapılması önerilir.",
     'te': "Lessroom Alaçatı is an interesting option for those seeking accommodation with its minimalist and original concept; booking at the start of the season is recommended as capacity is limited."},

170: {'t': "Hey DJ Alaçatı, canlı DJ performansları ve dans imkânıyla Alaçatı'nın en enerjik gece mekanlarından biridir; Cuma ve Cumartesi geceleri en hareketli dönemlerdir.",
     'te': "Hey DJ Alaçatı is one of Alaçatı's most energetic night venues with live DJ performances and dancing; Friday and Saturday nights are the liveliest periods."},

171: {'t': "Cahide Alaçatı, ev yapımı reçel ve özenli kahvaltı sunumuyla Alaçatı'nın en çok önerilen kahvaltı mekanlarından biridir; hafta sonu sabahları kuyruk olabileceğinden erken gelin.",
     'te': "Cahide Alaçatı is one of Alaçatı's most recommended breakfast venues with homemade jam and a meticulous breakfast presentation; come early as there may be a queue on weekend mornings."},

172: {'t': "Balkabağa, Alaçatı Çarşı'nda taze kabak ve mevsim sebzeli ev yemekleri sunan samimi bir aile lokantasıdır; öğle yemeği için 12:00-13:00 arası en taze servis yapılır.",
     'te': "Balkabağa is a sincere family restaurant in Alaçatı Bazaar serving fresh pumpkin and seasonal vegetable home cooking; the freshest service for lunch is between 12-1pm."},

173: {'t': "Wuu Club, Alaçatı'nın açık hava dans kültürünü yaşatan mekanlardan biridir; DJ etkinlikleri için haftalık programı sosyal medyadan takip edin ve yoğun gecelerde giriş için erkenden gidin.",
     'te': "Wuu Club is one of the venues that keeps Alaçatı's open-air dance culture alive; follow the weekly program from social media for DJ events and go early for entry on busy nights."},

174: {'t': "Bedevi Alaçatı, sakin bir atmosfer arayanlar için Alaçatı'nın daha özgün köşelerinden birini temsil eder; öğleden sonra sezonun en yoğun dönemlerinde bile görece sessiz kalır.",
     'te': "Bedevi Alaçatı represents one of Alaçatı's more original corners for those seeking a calm atmosphere; it remains relatively quiet even during the busiest periods of the season in the afternoon."},

175: {'t': "Cemiyet & Moon, Alaçatı'nın iki yüzünü — gündüz kahve ve sandviç, gece kokteyl ve müzik — aynı çatı altında birleştirir; akşam geçişi için 18:00-19:00 arası en keyifli saat.",
     'te': "Cemiyet & Moon unites two faces of Alaçatı — daytime coffee and sandwich, nighttime cocktail and music — under the same roof; 6-7pm is the most enjoyable hour for the evening transition."},

176: {'t': "Nezir's Tower, Alaçatı'nın tarihi taş kulelerinden biri üzerinde kurulmuş özgün bir konaklama veya café deneyimi sunar; terasa çıkmak için sabah erken gelmeniz en iyi manzara ışığını sağlar.",
     'te': "Nezir's Tower offers an original accommodation or café experience built on one of Alaçatı's historic stone towers; coming early in the morning for the terrace provides the best view light."},

177: {'t': "Estinbel Plajı, Çeşme yarımadasının sessiz koylarından biridir; motorlu araç erişimi kısıtlı olduğundan tekne ya da yürüyüş ile ulaşmak en iyi seçenektir. Tesis bulunmamaktadır.",
     'te': "Estinbel Beach is one of the quiet coves of the Çeşme peninsula; as motorized vehicle access is restricted, reaching it by boat or on foot is the best option. No facilities are present."},

178: {'t': "Bademlik Koyu, Çeşme'nin en sığ ve en berrak sularından birine sahip sakin bir koyudur; sabah erken saatler snorkel için idealdir. Bölgede tesis olmadığından yiyecek ve içecek yanınızda olsun.",
     'te': "Bademlik Cove is a quiet cove with one of Çeşme's shallowest and clearest waters; early morning hours are ideal for snorkeling. As there are no facilities in the area, bring food and drinks with you."},

179: {'t': "Çeşme Yarımadası'nı keşfetmek için araç kiralayarak koy koy gezmek en verimli yoldur; günübirlik tur programı ile birden fazla koyu ve kasabayı aynı gün ziyaret edebilirsiniz.",
     'te': "Renting a car to explore the Çeşme Peninsula bay by bay is the most efficient way; with a day-trip tour program you can visit multiple coves and towns on the same day."},

180: {'t': "Marinera Residence, Çeşme Marina'ya yürüme mesafesinde uzun dönem ya da haftalık kiralama için uygun bir residence seçeneği sunar; deniz manzaralı daireler için erken rezervasyon şarttır.",
     'te': "Marinera Residence offers a suitable residence option for long-term or weekly rental within walking distance of Çeşme Marina; early reservation is essential for sea-view apartments."},

181: {'t': "Point View, Çeşme yarımadasında panoramik deniz manzarası için iyi konumlanmış bir seyir noktasıdır; gün batımı saatlerinde buraya çıkmak için en az 30 dakika öncesinden gelin.",
     'te': "Point View is a well-positioned viewpoint for panoramic sea views on the Çeşme peninsula; arrive at least 30 minutes before sunset hours to come up here."},
}

apply_batch('cesme.json', U)
