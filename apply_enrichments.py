#!/usr/bin/env python3
import os
import json

updates = {
    "ALAÇATI MEYDANI": {
        "description": "Alaçatı'nın tarihi dokusunun merkezinde yer alan bu meydan, kasabanın sosyal kalbidir. Tarihi taş binalar, hareketli kafeler ve asırlık rüzgar değirmenleriyle çevrili olan meydan, bohem şıklığı binlerce yıllık Ege mirasıyla tek bir noktada buluşturur.",
        "description_en": "At the center of Alaçatı's historic fabric, this square is the town's urban and social heart. Surrounded by stone buildings, cafes, and Lycian tombs, it merges bohemian chic with millennia of history in one spot.",
        "localTip": "Akşam saatlerinde kalabalıklaşmadan önce erken saatlerde gelip taş sokakların ve begonvillerin harika fotoğraflarını çekebilirsiniz.",
        "localTip_en": "Arrive early before the evening crowds to capture stunning photos of the stone streets and vibrant bougainvillea."
    },
    "Aladja Imaret (Ishak Pasha Mosque)": {
        "description": "1484 yılında İshak Paşa tarafından yaptırılan Alaca İmaret, Selanik'teki erken dönem Osmanlı mimarisinin en büyüleyici örneklerinden biridir. Adını minaresindeki elmas biçimli renkli çinilerden alan bu tarihi anıt, günümüzde sanat sergilerine ve kültürel etkinliklere ev sahipliği yapmaktadır.",
        "description_en": "Built in 1484 by Ishak Pasha, Aladja Imaret is a stunning example of early Ottoman architecture in Thessaloniki, famous for its colorful minaret adorned with diamond-shaped glazed tiles. Today, this historic monument serves as an impressive cultural space hosting art exhibitions and events.",
        "localTip": "Yapının muazzam kubbe işçiliğini ve bahçesindeki tarihi sükuneti hissetmek için fotoğraf makinenizi yanınıza almayı unutmayın.",
        "localTip_en": "Don't forget your camera to capture the magnificent dome craftsmanship and the peaceful tranquility of its historic courtyard."
    },
    "Aquarium of Rhodes - Hydrobiological Station HCMR": {
        "description": "Adanın en kuzey ucunda, 1930'lardan kalma tarihi bir Art Deco binada yer alan Rodos Akvaryumu, Ege Denizi'nin zengin sualtı yaşamına büyüleyici bir pencere açar. Doğal bir deniz mağarası şeklinde tasarlanan tesis, hem halka açık bir akvaryum hem de önemli bir hidrobiyolojik araştırma merkezi olarak hizmet vermektedir.",
        "description_en": "Located at the northernmost tip of the island in a historic 1930s Art Deco building, the Aquarium of Rhodes offers a fascinating glimpse into the marine life of the Aegean Sea. Designed like an underwater sea cave, the facility functions as both a public aquarium and a major hydrobiological research center.",
        "localTip": "Akvaryum gezisinin ardından hemen dışarıdaki Elli Plajı'nda Ege ve Akdeniz'in birleştiği o büyüleyici noktada yürüyüş yapın.",
        "localTip_en": "After visiting the aquarium, take a walk outside at Elli Beach where the Aegean and Mediterranean seas beautifully meet."
    },
    "Bacio Nero - Stazione Centrale": {
        "description": "Palermo Merkez İstasyonu'nun hemen karşısında elverişli bir konuma sahip olan Bacio Nero, taze demlenmiş İtalyan kahvesi, sıcak cornetti ve otantik Sicilya cannoli'si tatmak için mükemmel bir lezzet durağıdır. Hızlı servisi ve samimi çalışanlarıyla bilinen mekan, tren yolculuğu veya şehir turu öncesi enerji toplamak için idealdir.",
        "description_en": "Conveniently located right across from Palermo Central Station, Bacio Nero is the perfect quick stop for freshly brewed Italian coffee, warm cornetti, and authentic Sicilian cannoli. Known for its quick service and welcoming staff, it's an ideal spot to recharge before a train journey or city tour.",
        "localTip": "Antep fıstıklı kremalı (pistachio) cannoli ve yanında taze bir espresso ile güne enerjik bir Sicilya başlangıcı yapın.",
        "localTip_en": "Kickstart your morning with a pistachio cream cannoli paired with a fresh espresso for a true Sicilian energy boost."
    },
    "Bocatería Harbin": {
        "description": "Valensiya'da yer alan Bocatería Harbin, çıtır ekmekli meşhur İspanyol sandviçleri (bocadillos) ve bol malzemeli sunumlarıyla öne çıkan sevilen bir lokal lezzet durağıdır. Mahalle sakinlerinin müdavimi olduğu bu samimi mekan, şehir keşfiniz sırasında hızlı, lezzetli ve bütçe dostu bir mola vermek için harika bir tercihtir.",
        "description_en": "Situated in Valencia, Bocatería Harbin is a highly praised local sandwich bar famous for its crispy bocadillos and generous Spanish fillings. Loved by locals for its relaxed, authentic neighborhood vibe, it is the perfect spot to grab an affordable and delicious bite during your city exploration.",
        "localTip": "İspanyol omletli (tortilla de patatas) ve taze sarımsak mayonezli bocadillo sandviçini mutlaka deneyin.",
        "localTip_en": "Be sure to try their bocadillo sandwich filled with Spanish potato omelette (tortilla) and fresh garlic aioli."
    },
    "Bongénie Grieder": {
        "description": "Cenevre'nin kalbindeki Rue du Marché üzerinde yer alan Bongénie Grieder, yedi kata yayılan lüks moda, şık ev dekorasyonu ve seçkin kozmetik markalarıyla kentin en prestijli çok katlı mağazasıdır. Zarif mimarisi ve dünyaca ünlü tasarımcıların özel koleksiyonlarıyla, sofistike bir alışveriş deneyiminin merkezidir.",
        "description_en": "Located in the heart of Geneva on Rue du Marché, Bongénie Grieder is an upscale department store offering seven floors of luxury fashion, chic home decor, and premium cosmetics. With its elegant architecture and curated designer collections, it stands as the premier destination for sophisticated shopping in the city.",
        "localTip": "Alışverişin ardından en üst kattaki şık kafe-barda Cenevre manzarasına karşı kahvenizi yudumlayarak dinlenin.",
        "localTip_en": "After shopping, relax at the chic rooftop café-bar on the top floor and enjoy your coffee with a view over Geneva."
    },
    "Boreal Coffee (Eaux-Vives)": {
        "description": "Hareketli Eaux-Vives semtinde yer alan Boreal Coffee Shop, Cenevre'deki üçüncü nesil nitelikli kahve kültürünün öncülerindendir. Sürdürülebilir kaynaklardan elde edilip ustalıkla kavrulan kahve çekirdekleri, sıcak İskandinav dekorasyonu ve ev yapımı tatlılarıyla kahve tutkunları için samimi bir buluşma noktasıdır.",
        "description_en": "Tucked away in the vibrant Eaux-Vives neighborhood, Boreal Coffee Shop is a pioneer of artisanal specialty coffee in Geneva. Featuring sustainably sourced beans roasted to perfection, cozy Nordic-style seating, and homemade pastries, it serves as a peaceful urban sanctuary for coffee lovers and digital nomads.",
        "localTip": "Taze demlenmiş bir Flat White ve yanında ev yapımı havuçlu kek ile Cenevre yağmurunu cam kenarından izleyin.",
        "localTip_en": "Pair a freshly brewed Flat White with a slice of homemade carrot cake while watching the Geneva rain by the window."
    },
    "Cannes Maritime Museum": {
        "description": "Suquet tepesinin zirvesinde, tarihi bir orta çağ kalesinin içinde yer alan Cannes Denizcilik Müzesi (Musée de la Castre), denizcilik objeleri, Akdeniz antikaları ve dünya ilkel sanatına ait benzersiz koleksiyonlar sergiler. Kalenin 12. yüzyıldan kalma kulesi, Cannes Körfezi ve Lérins Adaları'na doğru nefes kesici 360 derecelik panoramik bir manzara sunar.",
        "description_en": "Perched atop the Suquet hill inside a historic medieval fortress, the Musée de la Castre (Cannes Maritime Museum) showcases an extraordinary collection of maritime artifacts, Mediterranean antiquities, and global primitive art. The 12th-century tower of the castle offers breathtaking 360-degree views across the Bay of Cannes and the Lérins Islands.",
        "localTip": "Müzenin tarihi bahçesindeki çam ağaçlarının altından yat limanının ve batan güneşin eşsiz manzarasını fotoğraflayın.",
        "localTip_en": "Photograph the breathtaking view of the yacht harbor and sunset from beneath the pine trees in the museum's historic garden."
    },
    "Casa Stagnitta": {
        "description": "Palermo'nun tarihi merkezinde, Quattro Canti yakınında yer alan Casa Stagnitta, 1928'den bu yana kesintisiz hizmet veren Sicilya'nın en köklü ve ünlü kahve kavurma atölyelerinden biridir. İçeri adım attığınızda taze kavrulmuş çekirdek kokuları, nostaljik değirmenleri ve benzersiz Sicilya espresso harmanlarıyla zamanda tatlı bir yolculuğa çıkarsınız.",
        "description_en": "Situated in Palermo's historic center near Quattro Canti, Casa Stagnitta is one of Sicily's oldest and most renowned artisanal coffee roasters, operating continuously since 1928. Stepping inside feels like a journey through time, surrounded by the rich aroma of freshly roasted beans, vintage grinders, and exceptional Sicilian espresso blends.",
        "localTip": "Tarihi dükkandan özel kavrulmuş 'Miscela Bar' kahvesinden paket yaptırıp evinize Sicilya kokusunu götürün.",
        "localTip_en": "Purchase a bag of freshly roasted 'Miscela Bar' coffee to bring the genuine aroma of Sicily back to your home."
    },
    "Çeşme Tekne Turu / Grandstar Çeşme Tekne Turları": {
        "description": "Her sabah Çeşme Marina'dan yarımadanın en bakir turkuaz koylarına doğru yelken açan Grandstar Tekne Turları, unutulmaz bir deniz yolculuğu sunuyor. Eşek Adası, Mavi Koy ve Makri Adası gibi büyüleyici duraklara uğrayan turlar; kristal sularda yüzme molaları, neşeli müzikleri ve teknede ızgara balık ziyafetiyle Ege tatilinin vazgeçilmezidir.",
        "description_en": "Setting sail daily from Çeşme Marina to the peninsula's most pristine turquoise coves, Grandstar Boat Tours offer an unforgettable sea voyage. Cruising to iconic stops like Eşek Island, Blue Lagoon, and Makri Island, guests enjoy crystal-clear swimming breaks, lively music, and a delicious grilled fish lunch on deck.",
        "localTip": "Eşek Adası'nda mola verdiğinizde yanınızda getirdiğiniz havuç ve elmalarla adanın sevimli sakinlerini besleyebilirsiniz.",
        "localTip_en": "When stopping at Donkey Island, bring carrots and apples to feed the charming resident donkeys."
    },
    "Chatzi": {
        "description": "Selanik'in hareketli merkezinde yer alan Chatzi, otantik Yunan-Osmanlı tatlıları, bol şerbetli baklavaları ve nefis kremalı bougatsa'sıyla meşhur tarihi bir pastanedir. Nesiller boyu aktarılan geleneksel tarifleri aslına sadık kalarak yaşatan mekan, közde pişmiş köpüklü Yunan kahvesi eşliğinde nostaljik bir lezzet şöleni sunar.",
        "description_en": "Located in the vibrant heart of Thessaloniki, Chatzi is a historic confectionery famous for its authentic Greek-Ottoman desserts, syrupy baklava, and creamy bougatsa. Established decades ago, it preserves traditional recipes passed down through generations, offering a nostalgic culinary journey accompanied by strong Greek coffee.",
        "localTip": "Tarçın ve pudra şekeri serpilmiş sıcak kremalı bougatsa böreğinin tadına bakmadan Selanik'ten ayrılmayın.",
        "localTip_en": "Do not leave Thessaloniki without tasting their warm cream bougatsa pastry dusted with cinnamon and powdered sugar."
    },
    "Costarena": {
        "description": "Las Arenas sahilinin kumsalı boyunca uzanan Costarena, Akdeniz'in masmavi sularına hakim manzarasıyla öne çıkan seçkin bir plaj restoranı ve lounge alanıdır. Taze deniz mahsullü otantik Valensiya paellası, buz gibi sangriası ve rahatlatıcı bohem ambiyansıyla, dalga sesleri eşliğinde güneşli bir ziyafet için kusursuzdur.",
        "description_en": "Nestled right along the lively beachfront of Las Arenas, Costarena is a premium beach restaurant and lounge offering panoramic views across the Mediterranean. Famed for its authentic Valencian seafood paella, chilled sangria, and relaxed bohemian ambiance, it is the perfect spot for a sun-soaked afternoon feast.",
        "localTip": "Deniz mahsullü (Marisco) paella siparişinizi verirken yemeğin hazırlanmasının 30-40 dakika sürdüğünü unutmayın ve sahilin tadını çıkarın.",
        "localTip_en": "Remember that authentic seafood paella takes 30-40 minutes to prepare fresh, so sit back, relax, and enjoy the beach views."
    },
    "DANICA SJAJ": {
        "description": "Danica Sjaj, Dubrovnik'in nefes kesici sularında lüks tekne turları ve özel deniz transferi hizmeti sunan seçkin bir acentedir. Elaphiti Adaları, Elafiti mağaraları ve Mljet Milli Parkı'nın saklı turkuaz koylarına kişiye özel rotalar düzenleyen firma; deneyimli kaptanları, şık tekneleri ve sunduğu VIP konforla misafirlerine Adriyatik Denizi'nde unutulmaz bir denizcilik deneyimi yaşatır.",
        "description_en": "Danica Sjaj is a premium luxury boat and private transfer charter service operating in the breathtaking waters of Dubrovnik. Offering bespoke island-hopping itineraries to the Elaphiti Islands, Mljet National Park, and hidden turquoise sea caves, it provides travelers with an elite, intimate, and unforgettable Adriatic cruising experience on modern vessels equipped with professional skippers.",
        "localTip": "Kolocep Adası'ndaki saklı Mavi Mağara'yı (Blue Cave) şnorkelle keşfetmek için gün batımından önceki sakin saatleri tercih edin.",
        "localTip_en": "Book a private late afternoon charter to snorkel inside the Blue Cave on Kolocep Island when the waters are calmest and glowing blue."
    },
    "Dubrovnik Yacht Agent - Dubrovnik Luxury Travel Experts - Croatia": {
        "new_name": "Dubrovnik Yacht Agent",
        "description": "Dubrovnik'in öncü lüks yat kiralama ve denizcilik konsiyerj acentesi olan Dubrovnik Yacht Agent, Dalmaçya kıyıları boyunca kişiye özel deniz rotaları oluşturmakta uzmandır. Özel süperyat kiralamalarından VIP liman hizmetlerine ve ıssız adalardaki seçkin ziyafet organizasyonlarına kadar, uzman yerel ekibiyle gezginlere Adriyatik'in masmavi sularında kusursuz ve elit bir tatil sunar.",
        "description_en": "As the premier luxury yacht charter and concierge agency in Dubrovnik, Dubrovnik Yacht Agent specializes in crafting bespoke maritime itineraries across the Dalmatian coast. From organizing private superyacht charters and VIP port services to curating exclusive dining experiences on remote islands, their expert local team ensures a seamless and elite Adriatic voyage.",
        "localTip": "Lokrum Adası etrafında özel bir akşamüstü turu planlayarak Eski Şehir (Old Town) surlarının denizden batan güneş altındaki ihtişamını izleyin.",
        "localTip_en": "Arrange a private late afternoon cruise around Lokrum Island to admire the historic Old Town walls glowing beneath the setting sun from the sea."
    },
    "Estinbel Plajı": {
        "description": "Çeşme kıyılarının saklı kalmış doğa harikalarından biri olan Estinbel Plajı, kristal berraklığındaki turkuaz suları ve turistik kalabalıklardan uzak dingin atmosferiyle öne çıkar. Doğal kaya oluşumlarının rüzgardan koruduğu bu gizli cennet, sessizlik içinde yüzmek ve Ege'nin el değmemiş güzelliğini kucaklamak isteyen gezginler için kusursuz bir kaçış noktasıdır.",
        "description_en": "Hidden along the scenic Çeşme coastline, Estinbel Beach is an untouched natural haven praised for its crystal-clear turquoise waters and peaceful isolation away from the main tourist hubs. Sheltered by dramatic rock formations, it is a secret paradise perfect for travelers seeking tranquility, pristine swimming, and a serene connection with nature.",
        "localTip": "Plajda şezlong ve şemsiye kiralama imkanı kısıtlı olabileceği için yanınıza plaj havlunuzu, katlanabilir sandalyenizi ve soğuk içeceklerinizi almayı unutmayın.",
        "localTip_en": "As sunbed facilities may be limited in this untouched bay, bring your own beach towel, foldable chair, and refreshing cold drinks."
    },
    "F.P.Journe Le Restaurant": {
        "description": "Cenevre'nin kalbindeki Rue du Rhône üzerinde yer alan F.P.Journe Le Restaurant, efsanevi İsviçreli saat ustası tarafından hayata geçirilen seçkin bir gastronomi sarayıdır. Michelin yıldızlı ünlü şef Dominique Gauthier yönetimindeki mekan; saatçilik zanaatının zarafetini üst düzey Fransız mutfağıyla buluşturarak, lüks ve sofistike bir atmosferde kusursuz mevsimsel tadım menüleri sunar.",
        "description_en": "Located in the refined heart of Geneva on Rue du Rhône, F.P.Journe Le Restaurant is an exquisite gastronomic establishment created by the legendary Swiss watchmaker. Directed by Michelin-starred chef Dominique Gauthier, the restaurant merges haute horlogerie elegance with world-class French dining, offering impeccable seasonal tasting menus in a luxurious, timepiece-inspired ambiance.",
        "localTip": "Şefin imza yemeği olan trüf mantarlı ıstakoz ravioli ve İsviçre şarapları eşleşmesini mutlaka deneyimleyin (rezervasyon şarttır).",
        "localTip_en": "Make a reservation well in advance to experience the chef's signature lobster ravioli with truffles paired with premium Swiss wines."
    },
    "Grand Hotel et Des Palmes": {
        "description": "1874 yılında kapılarını açan Grand Hotel et Des Palmes, Richard Wagner'den Albert Camus'ye uzanan ünlü konuk listesiyle Palermo'nun en prestijli tarihi otelidir. Barok sütunları, kristal avizelerle aydınlanan görkemli salonları ve kış bahçesiyle başlı başına bir müze niteliği taşıyan yapı; sadece lobisinde kahve yudumlarken bile Sicilya'nın aristokrat geçmişini hissettirir.",
        "description_en": "Opened in 1874, Grand Hotel et Des Palmes has made its name as Palermo's most prestigious historical hotel with a famous guest list stretching from Richard Wagner to Albert Camus. With its Baroque columns, grand halls illuminated by crystal chandeliers, and lush winter garden, the hotel itself is a historic landmark; even sipping a coffee in the opulent lobby is a cultural experience.",
        "localTip": "Otelin büyüleyici Barok lobisindeki antika piyanonun etrafında oturup geleneksel Sicilya bademli bisküvisi eşliğinde bir ikindi çayı molası verin.",
        "localTip_en": "Sit around the antique piano in the hotel's magnificent Baroque lobby and enjoy an afternoon tea paired with traditional Sicilian almond biscuits."
    },
    "Port de Ramatuelle": {
        "description": "Saint-Tropez yakınlarında yer alan Port de Ramatuelle, Akdeniz balıkçı geleneğini modern yatçılık lüksüyle muhteşem bir uyum içinde harmanlayan büyüleyici bir sahil marinasıdır. Çam ağaçları ve şık deniz kıyısı bistrolarıyla çevrili olan liman, kentin kalabalığından uzakta rıhtım boyunca gün batımı yürüyüşleri yapmak için dingin ve kartpostallık bir sığınaktır.",
        "description_en": "Nestled near Saint-Tropez, Port de Ramatuelle is a charming coastal marina that beautifully combines Mediterranean fishing heritage with modern yachting luxury. Surrounded by pine trees and upscale waterfront bistros, it offers a tranquil, picturesque retreat away from the bustling town center, perfect for admiring sunset strolls along the docks.",
        "localTip": "Liman kıyısındaki restoranların açık teraslarında oturup taze istiridye tabağı ve soğuk Provans roze şarabı eşliğinde yatların süzülüşünü izleyin.",
        "localTip_en": "Secure a table on a waterfront terrace to enjoy fresh oysters and chilled Provence rosé while watching the elegant yachts glide by."
    },
    "Hotel Hospes Palau de la Mar | Valencia": {
        "description": "Valensiya'nın kalbindeki Navarro Reverter Bulvarı'nda, 19. yüzyıldan kalma iki görkemli aristokrat malikanesinin içinde yer alan Hospes Palau de la Mar, tarihi ihtişamı modern lüksle kusursuzca dengeler. Dingin avlu bahçesi, üstün nitelikli Bodyna Spa'sı ve minimalist zarafete sahip odalarıyla, Turia Bahçeleri'ne sadece birkaç adım mesafede huzurlu bir şehir vahasıdır.",
        "description_en": "Set inside two spectacular 19th-century aristocratic manor houses on Navarro Reverter Avenue, Hospes Palau de la Mar perfectly balances historical grandeur with modern luxury. Featuring a serene interior garden courtyard, a world-class Bodyna Spa, and elegant minimalist quarters, it serves as an exclusive urban oasis just steps from the Turia Gardens.",
        "localTip": "Şehir turunun yorgunluğunu atmak için otelin Roma esintili kapalı havuzunda ve dingin spa merkezinde kendinizi şımartın.",
        "localTip_en": "Treat yourself to a relaxing session at the hotel's Roman-inspired indoor spa pool after a long day of exploring Valencia's historic streets."
    },
    "Hotel ILUNION Valencia 4": {
        "description": "Valensiya'nın modern iş bölgesinde, Kongre Sarayı'nın hemen yakınında yer alan Hotel ILUNION Valencia 4, şık ve engelsiz erişime sahip bir konaklama deneyimi sunar. Fütüristik dış cephesi, geniş pencerelerinden şehri kucaklayan aydınlık odaları ve açık yüzme havuzuyla, hem konfor hem de tarihi merkeze hızlı metro bağlantısı arayan gezginlerin favorisidir.",
        "description_en": "Located in Valencia's modern business and commercial district near the Palacio de Congresos, Hotel ILUNION Valencia 4 offers a highly accessible and stylish stay. Standing out with its futuristic facade, bright rooms with sweeping city views, and outdoor swimming pool, it is the premier choice for modern travelers seeking comfort and excellent metro connections to the historic center.",
        "localTip": "Otelin hemen önündeki metro istasyonunu (Beniferri) kullanarak sadece 10 dakika içinde Valensiya'nın tarihi merkezine ulaşabilirsiniz.",
        "localTip_en": "Use the Beniferri metro station right across from the hotel to reach Valencia's historic city center in just 10 minutes."
    },
    "Hotel Miramar Valencia": {
        "description": "Las Arenas Plajı'nın altın sarısı kumsallarının hemen yanı başında yükselen Hotel Miramar Valencia, kesintisiz Akdeniz manzarası sunan butik bir sahil mücevheridir. Şık çatı katı teras barı, samimi deniz atmosferi ve hareketli Marina Real'e olan yakınlığıyla mekan, dalga sesleri eşliğinde huzurla uyanmak isteyenler için mükemmel bir sığınaktır.",
        "description_en": "Perched right on the golden sands of Las Arenas Beach, Hotel Miramar Valencia is a boutique coastal gem offering uninterrupted Mediterranean views. Celebrated for its stylish rooftop bar, intimate seaside atmosphere, and proximity to the vibrant Marina Real, it is the perfect sanctuary for waking up to the soothing sound of the waves.",
        "localTip": "Gün batımında otelin en üst katındaki Miramar Rooftop Lounge'a çıkıp Akdeniz meltemi eşliğinde imza kokteyllerin tadını çıkarın.",
        "localTip_en": "Head up to the Miramar Rooftop Lounge at sunset to sip signature cocktails while feeling the gentle Mediterranean sea breeze."
    },
    "Hotel Porta Felice": {
        "description": "Palermo'nun tarihi kalbinde, anıtsal Porta Felice kapısının ve Botanik Bahçesi'nin hemen yanında yer alan bu 4 yıldızlı butik otel, 18. yüzyıldan kalma restore edilmiş bir sarayda hizmet verir. Deniz manzarası eşliğinde kahvaltı sunulan çatı terası, dinlendirici spa kulübü ve şık odalarıyla misafirlerine otantik bir Sicilya kaçamağı sunar.",
        "description_en": "Situated in the historic heart of Palermo right next to the monumental Porta Felice gate and the Botanical Gardens, this boutique 4-star hotel occupies a beautifully restored 18th-century palazzo. Offering a panoramic rooftop terrace where breakfast is served overlooking the sea, a tranquil wellness club, and elegant rooms, it provides an authentic Sicilian escape.",
        "localTip": "Sabahları otelin çatı terasında Foro Italico sahiline ve Palermo limanına karşı kahvenizi içerken taze Sicilya peynirlerinin tadına bakın.",
        "localTip_en": "Start your morning on the rooftop terrace tasting fresh Sicilian cheeses and pastries while gazing out over the Foro Italico coastline."
    },
    "HOTEL TURIA VALENCIA": {
        "description": "Görkemli Turia Bahçeleri'ne bakan ve Nuevo Centro alışveriş merkezinin hemen karşısında yer alan Hotel Turia Valencia, pratik ve konforlu bir konaklama noktasıdır. Klasik İspanyol mimarisi, ferah özel balkonları ve içinden geçen yemyeşil park yollarıyla hem tarihi merkeze hem de Sanat ve Bilim Şehri'ne kolayca ulaşılabilecek stratejik bir konuma sahiptir.",
        "description_en": "Overlooking the magnificent Turia Gardens and located right across from the Nuevo Centro shopping mall, Hotel Turia Valencia provides a highly practical and comfortable stay. With its classic Spanish architecture, spacious private balconies, and proximity to both the historic Old Town and the City of Arts and Sciences via scenic park paths, it is ideal for all travelers.",
        "localTip": "Otelin hemen önündeki parktan bisiklet kiralayarak yemyeşil Turia Bahçeleri boyunca Sanat ve Bilim Şehri'ne (Ciudad de las Artes) keyifli bir sürüş yapın.",
        "localTip_en": "Rent a bicycle directly across from the hotel and enjoy a scenic ride through the lush Turia Gardens down to the City of Arts and Sciences."
    },
    "Kas Camping": {
        "description": "Kaş ilçe merkezine sadece birkaç dakikalık yürüme mesafesinde, denize sıfır muhteşem bir zeytinlik alana yayılan Kaş Camping, kentin en özgürlükçü ve efsanevi konaklama durağıdır. Asırlık zeytin ağaçları altındaki kamp alanları, ahşap bungalovları ve doğrudan kristal sulara inen özel ahşap iskeleleriyle mekan, onlarca yıldır müdavimlerinin vazgeçemediği bohem bir cennettir.",
        "description_en": "Situated right along the rugged turquoise coastline and just a short walk from Kaş town center, Kaş Camping is the town's most legendary and free-spirited beachfront sanctuary. Offering shaded camping pitches under ancient olive trees, private wooden bungalows, and private platforms directly into the crystal-clear sea, it has been an iconic bohemian oasis for decades.",
        "localTip": "Ahşap iskeledeki şezlonglarda otururken güneşin batan ışıklarının Meis Adası üzerindeki muhteşem yansımalarını izleyin.",
        "localTip_en": "Lounge on the wooden sea platforms late in the afternoon to watch the glowing sunset casting beautiful hues over Kastellorizo (Meis) island."
    },
    "La Ponche Quarter": {
        "description": "La Ponche, Saint-Tropez'nin tarihi ve otantik kalbidir; dar yaya sokakları, pastel renkli eski balıkçı evleri ve Arnavut kaldırımlı meydanlardan oluşan büyüleyici bir labirenttir. Brigitte Bardot'nun efsanevi 'Ve Tanrı Kadını Yarattı' filmini çektiği küçük ve tenha kumsala açılan bu mahalle, ziyaretçileri modern lüksten uzaklaştırıp kasabanın romantik ve bohem geçmişine götürür.",
        "description_en": "La Ponche is the historic, authentic heart of Saint-Tropez; an atmospheric labyrinth of narrow pedestrian alleys, pastel-colored fishermen's cottages, and cobblestone squares. Bordering a tiny secluded beach where Brigitte Bardot famously filmed 'And God Created Woman', this captivating quarter transports visitors far from modern glitz into the town's romantic, bohemian past.",
        "localTip": "Mahallenin dar sokaklarında kaybolduktan sonra küçük La Ponche kumsalında taşların üzerine oturup dalga seslerini dinleyin.",
        "localTip_en": "After getting lost in the charming alleyways, sit on the smooth pebbles at the secluded La Ponche beach and listen to the soothing waves."
    },
    "Las Arenas Balneario Resort": {
        "description": "Valensiya'nın 19. yüzyıldan kalma tarihi sahil hamamlarını 5 yıldızlı lüks bir resort konseptiyle görkemli bir şekilde yeniden canlandıran Las Arenas Balneario Resort, Akdeniz kıyısında mimari bir başyapıt olarak yükselir. Geniş palmiye bahçeleri, görkemli sütunları, ısıtmalı havuzları ve ihtişamlı spa merkeziyle tesis, Valensiya'da deniz keyfini en üst düzeyde yaşamak isteyenlerin tek adresidir.",
        "description_en": "Spectacularly resurrecting Valencia's historic 19th-century beachfront thermal baths with a world-class 5-star resort luxury concept, Las Arenas Balneario Resort stands as an architectural masterpiece along the Mediterranean coast. Surrounded by sprawling manicured gardens, spectacular colonnades, and opulent spa wellness pools, it is the pinnacle of coastal sophistication in Spain.",
        "localTip": "Otelin denize sıfır bahçesindeki Brasserie Sorolla restoranında geleneksel Valensiya deniz mahsullü yemeklerinin tadını çıkarın.",
        "localTip_en": "Dine on the seaside terrace at Brasserie Sorolla to experience gourmet Valencian seafood dishes with panoramic sea views."
    },
    "Luxury Yacht Rental": {
        "description": "Cannes'daki Luxury Yacht Rental, Fransız Rivierası'nın ihtişamını denizden keşfetmek isteyen seçkin gezginler için dünya standartlarında VIP yat kiralama hizmeti sunar. Huzur dolu Lérins Adaları ve Cap d'Antibes koylarına günübirlik lüks kaçamaklardan, Cannes Film Festivali döneminde süperyatlar güvertesinde düzenlenen görkemli partilere kadar uzman ekibiyle kusursuz bir deniz seyahati sağlar.",
        "description_en": "Luxury Yacht Rental in Cannes provides an elite, world-class yacht charter service catering to discerning travelers exploring the glamour of the French Riviera. From private day charters to the idyllic Lérins Islands and Cap d'Antibes to hosting lavish VIP parties aboard state-of-the-art superyachts during the Cannes Film Festival, their experienced crew ensures a flawless maritime escape.",
        "localTip": "Sainte-Marguerite Adası etrafındaki turkuaz sularda demirleyerek denizin ortasında şef elinden çıkma lüks bir Akdeniz öğle yemeği ziyafeti verin.",
        "localTip_en": "Drop anchor in the turquoise waters off Sainte-Marguerite Island to enjoy a gourmet Mediterranean lunch prepared by a private onboard chef."
    },
    "Maritime Museum": {
        "description": "Kotor Eski Şehir'deki Müze Meydanı'nda, 18. yüzyıldan kalma görkemli Barok Grgurina Sarayı'nda yer alan Karadağ Denizcilik Müzesi, Boka Körfezi'nin yüzyıllara yayılan şanlı denizcilik geçmişine ışık tutar. Müzede ince işçilikli gemi modelleri, tarihi seyir aletleri, korsan silahları ve efsanevi kaptanların etkileyici yağlıboya portreleri sergilenmektedir.",
        "description_en": "Housed inside the monumental 18th-century Baroque Grgurina Palace on Museum Square in Kotor Old Town, the Maritime Museum of Montenegro chronicles centuries of the Boka Bay's glorious seafaring past. The museum exhibits an extraordinary collection of intricately carved ship models, historic navigational instruments, captured pirate weapons, and striking portraits of legendary sea captains.",
        "localTip": "Sarayın üst katındaki pencerelerden tarihi Kotor meydanına ve dağların yamaçlarına vuran güneşin açısını fotoğraflayın.",
        "localTip_en": "Admire the stunning view of the historic town square and the dramatic mountain slopes from the palace's elegant upper-floor windows."
    },
    "Mr. Pickwick Pub": {
        "description": "1969 yılında İsviçre'nin ilk otantik İngiliz pub'ı olarak kurulan Mr. Pickwick Pub, Cenevre tren istasyonunun yakınında yer alan efsanevi bir buluşma noktasıdır. Canlı uluslararası atmosferi, zengin fıçı bira çeşitleri, dev ekranlardaki maç yayınları ve meşhur fish and chips tabağıyla hem yerel halkın hem de yabancı çalışanların favori sosyalleşme merkezidir.",
        "description_en": "Established in 1969 as the very first authentic English pub in Switzerland, Mr. Pickwick Pub is a legendary social institution in Geneva located near the main train station. Celebrated for its lively international atmosphere, extensive draft beer selection, live sports screenings, and famous fish and chips, it is the ultimate friendly gathering spot for locals and expats alike.",
        "localTip": "Geleneksel Fish & Chips tabağı ve yanında soğuk bir fıçı İrlanda birası (Guinness) sipariş ederek canlı maç yayınlarının coşkusuna ortak olun.",
        "localTip_en": "Order their classic Fish & Chips paired with a cold draft pint of Guinness while enjoying the lively international sports screenings."
    },
    "Oxygen Pub": {
        "description": "Kaş limanının hemen yakınında, gece hayatının kalbinde yer alan Oxygen Pub; yüksek enerjisi, imza kokteylleri ve muhteşem canlı müzik performanslarıyla efsaneleşmiş açık hava bir eğlence mekanıdır. Genç ve dinamik bir kitleyi ağırlayan mekan, modern endüstriyel tasarımı Akdeniz samimiyetiyle buluşturarak sabahın ilk ışıklarına kadar Kaş sokaklarında müziğin ritmini tutar.",
        "description_en": "Located in the vibrant heart of Kaş's nightlife near the harbor, Oxygen Pub is an iconic open-air venue celebrated for its pulsating energy, craft cocktails, and exceptional live music performances. Attracting a dynamic and youthful crowd, it seamlessly blends modern industrial design with Mediterranean charm, keeping the town's party spirit alive until the early morning hours.",
        "localTip": "Hafta sonları canlı müzik performanslarında yer bulabilmek için saat 21:30'dan önce gelip barda yerinizi ayırtın.",
        "localTip_en": "Arrive before 9:30 PM on weekends to secure a good spot at the bar for their highly popular live music performances."
    },
    "Perle du Lac": {
        "description": "Cenevre Gölü'nün masmavi kıyılarında, 19. yüzyıldan kalma yemyeşil ve özenle düzenlenmiş bir parkın içinde yer alan Parc de la Perle du Lac, kentin en nefes kesici romantik kaçış noktalarından biridir. Göl sularının üzerinden görkemli Mont Blanc Dağı'na uzanan kesintisiz manzarası, ulu ağaçlar altındaki yürüyüş yolları ve zarif çiçek bahçeleriyle tam bir huzur vahasıdır.",
        "description_en": "Set inside a lush, beautifully landscaped 19th-century park along the pristine shores of Lake Geneva, Parc de la Perle du Lac is one of the city's most breathtaking romantic sanctuaries. Offering sweeping unobstructed views across the water towards Mont Blanc, shaded walking paths under majestic trees, and elegant flower gardens, it is a haven of absolute peace.",
        "localTip": "Güneşli bir günde parkın çimlerinde piknik yapın veya kıyıdaki banklarda oturup Jet d'Eau fıskiyesinin uzaktan yansımasını izleyin.",
        "localTip_en": "Pack a picnic for a sunny afternoon on the grass or sit on a lakeside bench to admire the distant spray of the famous Jet d'Eau fountain."
    },
    "Plage des Canoubiers": {
        "description": "Saint-Tropez'nin kalabalık merkezine sadece birkaç kilometre mesafede yer alan Plage des Canoubiers, gösterişten uzak samimi atmosferiyle yerel halkın en çok tercih ettiği huzurlu bir kumsaldır. Çam ağaçları ve ünlülerin saklı villalarıyla çevrili olan sığ ve rüzgarsız suları, Pampelonne'un yoğun plaj kulüplerinden uzakta güvenli ve dinlendirici bir deniz keyfi sunar.",
        "description_en": "Located just a few kilometers from the bustling center of Saint-Tropez, Plage des Canoubiers is a peaceful sandy beach beloved by local residents for its unpretentious, family-friendly charm. Backed by umbrella pines and private celebrity villas, its sheltered shallow waters provide an idyllic, safe swimming environment away from the crowded beach clubs of Pampelonne.",
        "localTip": "Plaj kıyısındaki çam ağaçlarının gölgesinde oturup koya demirleyen klasik ahşap yelkenlilerin huzur veren süzülüşünü izleyin.",
        "localTip_en": "Sit in the pleasant shade of the umbrella pines along the shore and watch the classic wooden sailboats anchored gently in the bay."
    },
    "Principato": {
        "description": "Rodos'un tarihi sahil şeridi boyunca zarif bir şekilde yükselen Principato; Ege'nin büyüleyici güzelliğini sofistike Riviyera lüksüyle harmanlayan üst düzey bir plaj kulübü ve restorandır. Şık bohem locaları, gurme Akdeniz füzyon lezzetleri ve gün batımı şampanya partileriyle mekan, adada lüks ve konfor içinde güneşlenmenin en popüler adresidir.",
        "description_en": "Perched elegantly along the historic coastline of Rhodes, Principato is an upscale beachfront dining and day club destination merging Aegean beauty with sophisticated Riviera luxury. Famed for its chic bohemian cabanas, gourmet Mediterranean fusion cuisine, and premium champagne parties, it is the ultimate destination for soaking up the sun in impeccable style.",
        "localTip": "Deniz kenarındaki şık localarda yer bulabilmek için özellikle yaz aylarında günler öncesinden rezervasyon yaptırmayı unutmayın.",
        "localTip_en": "Make your reservation days in advance during the high summer season to secure one of their highly coveted beachfront cabanas."
    },
    "Sala Parpalló": {
        "description": "Valensiya'daki tarihi Centre del Carme (CCCC) kültür kompleksinin içinde yer alan Sala Parpalló, çağdaş görsel ve medya sanatlarına adanmış yenilikçi ve avangart bir sergi galerisidir. Ulusal ve uluslararası gelecek vadeden sanatçıların düşündürücü multidisipliner projelerine ve deneysel enstalasyonlarına ev sahipliği yapan mekan, kentin dinamik sanat vizyonunun merkezidir.",
        "description_en": "Housed inside the historic Centre del Carme Cultura Contemporània (CCCC) in Valencia, Sala Parpalló is an innovative avant-garde exhibition gallery dedicated to contemporary visual and media arts. Hosting thought-provoking multidisciplinary projects and experimental installations by emerging national and international creators, it stands as a dynamic cultural beacon in the city.",
        "localTip": "Sergiyi gezdikten sonra tarihi manastırın gotik ve rönesans esintili huzurlu iç avlularında oturup mimarinin tadını çıkarın.",
        "localTip_en": "After exploring the exhibition, sit in the peaceful Gothic and Renaissance cloisters of the historic monastery to soak up the serene architecture."
    },
    "Spomen ploča, Hrvatsko kraljevstvo": {
        "description": "Dubrovnik Eski Şehir'deki tarihi Pile Kapısı yakınında asırlık taş surlara yerleştirilen bu anıtsal kitabe, Hırvatistan Krallığı'nın 1000. kuruluş yıl dönümüne adanmış gurur verici bir tarihi belgedir. Üzerindeki kabartma armalar ve tarihi Glagolitik yazıtlarla anıt, ziyaretçilere Hırvatistan'ın köklü orta çağ egemenliğiyle bağ kurduran büyüleyici bir duraktır.",
        "description_en": "Embedded into the ancient stone walls near Pile Gate in Dubrovnik Old Town, this monumental commemorative plaque stands as a proud historical tribute to the Kingdom of Croatia's millennium anniversary. Carved with intricate heraldic symbols and Glagolitic inscriptions, it serves as a fascinating monumental touchpoint connecting travelers with Croatia's proud medieval sovereignty.",
        "localTip": "Pile Kapısı'ndan Eski Şehir'e (Old Town) girerken hemen sol taraftaki taş duvarda yer alan bu oymalı anıtın önünde durup ince işçiliğini inceleyin.",
        "localTip_en": "As you enter the Old Town through Pile Gate, look closely at the ancient stone wall on your left to admire the intricate carvings of this historic plaque."
    },
    "Starbucks": {
        "description": "Alışılmış küresel kahve kültürünü geleneksel Kiklad mimarisiyle muazzam bir şekilde harmanlayan Mikonos Starbucks, mavi panjurlu bembeyaz tarihi bir taş binada hizmet verir. Sevilen imza espresso içecekleri, buzlu çayları ve taze hamur işlerini asmalarla kaplı avlusunda sunan mekan, ada gezintiniz sırasında güvenilir ve ferah bir dinlenme durağıdır.",
        "description_en": "Beautifully blending familiar global coffee culture with traditional Cycladic architecture, the Starbucks in Mykonos Town is uniquely housed in a pristine white-washed stone building with blue shutters. Offering its signature handcrafted espresso beverages, iced teas, and fresh pastries in a charming shaded courtyard, it provides a welcoming, reliable rest stop during your island strolls.",
        "localTip": "Sıcak ada gününde buzlu bir Caramel Macchiato veya Cold Brew alıp gölgeli avludaki taş masalarda serinleyin.",
        "localTip_en": "Escape the hot island sun with an iced Caramel Macchiato or Cold Brew and relax at the stone tables inside the shaded courtyard."
    },
    "Strong Rooster": {
        "description": "Mikonos'un labirent gibi dolambaçlı sokaklarına gizlenmiş olan Strong Rooster (Kafeneio), yerel balıkçılar ve ada yaşlılarının buluşma noktası olan son derece otantik bir geleneksel kahvehanedir. Sıcak kumda demlenen köpüklü Yunan kahvesi, taze sabah börekleri ve koyu sohbetleriyle mekan, adanın turistik ışıltısının ardındaki gerçek yerel yaşama dokunmak için eşsiz bir fırsattır.",
        "description_en": "Tucked away in the labyrinthine alleys of Mykonos Town, Strong Rooster (Kafeneio) is a highly authentic traditional Greek coffeehouse beloved by local fishermen and island elders. Known for its robustly brewed Greek coffee boiled on hot sand, morning pastries, and spirited local conversations, it offers a rare, unpretentious slice of genuine island daily life.",
        "localTip": "Sabahın erken saatlerinde gelip kumda ağır ağır pişen geleneksel kahveden için ve adanın yaşlı sakinleriyle selamlaşın.",
        "localTip_en": "Visit early in the morning to enjoy traditional Greek coffee brewed slowly over hot sand while greeting the friendly island elders."
    },
    "Villa Igiea, a Rocco Forte hotel": {
        "description": "Kademeli bahçelerinden Palermo Körfezi'ne görkemli bir şekilde bakan Villa Igiea, Rocco Forte zarafetiyle restore edilmiş 19. yüzyıldan kalma efsanevi bir Art Nouveau sarayıdır. Ünlü Florio ailesi tarafından yaptırılan bu tarihi yapı; Belle Époque salonları, mis kokulu botanik bahçeleri, denize nazır yüzme havuzu ve üst düzey Sicilya mutfağıyla konuklarına masalsı bir aristokrat deneyimi yaşatır.",
        "description_en": "Majestically overlooking the Gulf of Palermo from its spectacular terraced gardens, Villa Igiea is a legendary 19th-century Art Nouveau palazzo restored to flawless 5-star Rocco Forte luxury. Originally built by the influential Florio family, the hotel enchants guests with its Belle Époque grand salons, fragrant botanical gardens, sea-view swimming pool, and world-class Sicilian dining.",
        "localTip": "Akşam saatlerinde otelin muazzam körfez manzaralı Terrazza Bar'ında oturup canlı piyano tınıları eşliğinde Sicilya şarabınızı yudumlayın.",
        "localTip_en": "Take a seat at the sea-view Terrazza Bar at twilight to sip premium Sicilian wine accompanied by enchanting live piano music."
    }
}

assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
count = 0

for filename in os.listdir(assets_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(assets_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            modified = False
            for h in data.get('highlights', []):
                name = h.get('name')
                if name in updates:
                    up = updates[name]
                    if 'new_name' in up:
                        h['name'] = up['new_name']
                    h['description'] = up['description']
                    h['description_en'] = up['description_en']
                    h['localTip'] = up['localTip']
                    h['localTip_en'] = up['localTip_en']
                    modified = True
                    count += 1
            
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Updated: {filename}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

print(f"\n🎉 Successfully enriched {count} items across city files!")
