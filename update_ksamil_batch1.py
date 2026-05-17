import json

path = "assets/cities/ksamil.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mapping generated content (TR, EN)
updates = {
    "ChIJKWCz49FrWxMRbdaiyLMUzIc": {
        "tr": "Ksamil, berrak suları ve Adriyatik kıyısındaki doğal güzellikleri ile Arnavutluk Rivierası'nın kalbidir. Bölgedeki adalar ve bembeyaz kumsallar, burayı her yıl binlerce turistin akın ettiği popüler bir tatil destinasyonu yapmaktadır.",
        "en": "Ksamil is the heart of the Albanian Riviera, renowned for its crystal-clear Adriatic waters and stunning natural beauty. The nearby islands and pristine white beaches attract thousands of visitors annually seeking a Mediterranean paradise."
    },
    "ChIJYYzwRQBrWxMRZGFK94FuDqk": {
        "tr": "Mirror Beach, adını gün boyu sularında oluşan ayna gibi yansımalardan alan, Arnavutluk'un en özgün ve sessiz koylarından biridir. Kayaların arasındaki kristal denizi, burayı kalabalıktan kaçıp gerçek huzuru bulmak isteyenler için vazgeçilmez bir nokta kılar.",
        "en": "Mirror Beach is one of Albania's most unique and secluded bays, named for the mirror-like reflections that dance across its waters. Its crystal sea nestled between cliffs makes it an essential escape for those seeking true Mediterranean peace."
    },
    "ChIJ_0aCmwBrWxMRt58M1VhxV2I": {
        "tr": "Pulëbardha Beach, kayalıklarla çevrili turkuaz suları ve ince çakıllı kumsalıyla bilinen, Arnavutluk'un en büyüleyici sahil şeritlerinden biridir. Deniz manzarasını tepeden gören yerel restoranları, ziyaretçilere taze deniz ürünleri eşliğinde unutulmaz bir deneyim sunmaktadır.",
        "en": "Pulëbardha Beach is a stunning coastal gem known for its turquoise waters surrounded by cliffs and fine pebble sands. Local cliffside restaurants offer visitors an unforgettable experience, serving fresh seafood with sweeping views of the Ionian Sea."
    },
    "ChIJZY4ygCxqWxMRzDWCTY8vnOk": {
        "tr": "Lori Beach, sığ denizi ve huzurlu kumları ile aileler için Ksamil'deki en popüler ve güvenli noktalardan biridir. Turkuaz koyun kenarına kurulu şezlongları ve samimi kafeleri ile Ege-İyon havasını en doğal haliyle hissedeceğiniz keyifli bir plajdır.",
        "en": "Lori Beach is one of the most popular and safe spots in Ksamil for families, offering shallow waters and soft sands. Its beachside cafes and loungers set along the turquoise cove allow you to feel the authentic Ionian vibe in its purest form."
    },
    "ChIJ9aS8O_tBWxMRU8k9fW8zWI4": {
        "tr": "Corfu Sailing Centre, adrenalin tutkunları ve deniz severler için profesyonel yelken eğitimleri ve heyecan dolu turlar sunan kentsel bir merkezdir. Adriyatik'in rüzgarıyla buluşacağınız bu nokta, denizcilik kültürünü yakından tanımak isteyen gezginlerin uğrak duraklarındandır.",
        "en": "Corfu Sailing Centre is an urban hub for adrenaline junkies and sea lovers, offering professional sailing lessons and exciting boat tours. Meeting the Adriatic winds at this point, it is a top destination for travelers wanting to immerse in maritime culture."
    },
    "ChIJe-jSaABrWxMR8OjQa5ikkgw": {
        "tr": "Poda Ksamil, modern konsepti ve denize sıfır konumuyla bölgenin en seçkin buluşma noktalarından biri olarak öne çıkmaktadır. Hem lüks bir konaklama deneyimi hem de akşamları canlı müzik eşliğinde harika kokteyller sunarak Ksamil'in sosyal hayatına enerji katar.",
        "en": "Poda Ksamil stands out as one of the region's elite meeting points with its modern concept and beachfront location. Offering both a luxury stay and an energetic social scene with live music and signature cocktails, it defines the town's vibrant pulse."
    },
    "ChIJuwgwDKRrWxMR0bcTh4Dnv_E": {
        "tr": "Pantai Plazhi Ksamilit, kristal suları ve yumuşak kumuyla Arnavutluk Rivierası'nın en sevilen halk plajlarından biridir. Çevredeki adalara olan yakınlığı ve geniş deniz manzarası ile kentin doğal güzelliklerini panoramik olarak izleyebileceğiniz ferah bir sahil alanıdır.",
        "en": "Pantai Plazhi Ksamilit is one of the most beloved public beaches of the Albanian Riviera, famed for its crystal waters and soft sands. Its proximity to the islands and wide vistas make it a refreshing spot to enjoy the panoramic beauty of the coast."
    },
    "ChIJfdWL3yprWxMRmCTkh6k02yU": {
        "tr": "Rilinda Beach, samimi atmosferi ve deniz üzerindeki iskelesiyle gün batımını izlemek için Ksamil'deki en romantik duraklardan biridir. Yerel lezzetleri ve taze meyve suları ile hem gündüz güneşin hem de gece denizin huzurunun tadını çıkarabileceğiniz sakin bir mekandır.",
        "en": "Rilinda Beach is one of the most romantic spots in Ksamil for watching the sunset, featuring a cozy atmosphere and a wooden pier over the water. Serving local flavors and fresh juices, it’s a tranquil oasis to enjoy both the sun and the night's calm."
    },
    "ChIJP2xPbwBrWxMR8NRp8uKCl7w": {
        "tr": "Heart of Ksamil, kentin merkezinde yer alan ve butik dükkanları ile yerel el sanatlarını keşfedebileceğiniz samimi bir meydandır. Civarın kültürel dokusunu yansıtan kafeleri ve hediyelik eşya noktaları ile turistler için kentsel bir buluşma ve dinlenme alanı görevi görür.",
        "en": "Heart of Ksamil is a cozy square in the town center where you can discover boutique shops and local handicrafts. With cafes and souvenir spots reflecting the neighborhood’s culture, it serves as an urban meeting and relaxation hub for every traveler."
    },
    "ChIJMflKAgBrWxMRL2pTegsreX8": {
        "tr": "Ksamil Beach, bembeyaz kumları ve üç küçük adaya bakan manzarasıyla bölgenin en ikonik ve fotojenik sahilidir. Turkuazın her tonunu görebileceğiniz denizi ve sahildeki modern tesisleri ile ziyaretçilere tam kapsamlı bir Akdeniz yaz deneyimi sunmaktadır.",
        "en": "Ksamil Beach is the most iconic and photogenic shore in the region, boasting brilliant white sands and views across to the three small islands. With every shade of turquoise in its waters and modern facilities, it offers a full Mediterranean summer escape."
    },
    "ChIJBW-lEThrWxMR0iMR88euQNk": {
        "tr": "Bora Bora Beach, isminden de anlaşılacağı gibi tropik bir hava sunan, Ksamil'in en popüler ve hareketli eğlence plajlarından biridir. Gün boyu devam eden müzik, ferahlatıcı içecekler ve su sporları imkanlarıyla kentin tatil enerjisinin en yüksek olduğu noktalardan biridir.",
        "en": "Bora Bora Beach offers a tropical vibe as its name suggests, serving as one of Ksamil's most popular and lively entertainment beaches. With music playing all day, refreshing drinks, and waterspooks, it is where the town's holiday energy is at its highest."
    },
    "ChIJX4chYABrWxMREQL9C4wDDQU": {
        "tr": "Public Beach, yerel halk ve turistlerin iç içe olduğu, Ksamil'in en samimi ve doğal sahil alanlarından biridir. Giriş ücreti olmayan geniş alanları ve kristal deniziyle, kentin sahil ruhunu hiçbir kısıtlama olmadan yaşamak isteyenler için harika bir seçenektir.",
        "en": "Public Beach is one of the friendliest and most natural coastal areas in Ksamil, where locals and tourists mingle freely. With vast free spaces and crystal-clear waters, it's a great choice for those wanting to live the town's seaside spirit without limits."
    },
    "ChIJRVikcABrWxMR7i6Rotq0Vto": {
        "tr": "Ksamill, bölgedeki yerel yaşamın ve butik turizmin buluştuğu, henüz keşfedilmemiş sessiz sokakları ve gizli bahçeleri ile büyüleyen bir mahalledir. Arnavutluk misafirperverliğini yakından görebileceğiniz pansiyonları ve ev yapımı zeytinyağlıları ile kentin en otantik rotasıdır.",
        "en": "Ksamill is an enchanting neighborhood where local life meets boutique tourism, filled with undiscovered quiet streets and hidden gardens. With guesthouses showcasing Albanian hospitality and homemade olive oil dishes, it is the town's most authentic route."
    },
    "ChIJs4tzcwBrWxMRvhSxtGVRy-8": {
        "tr": "Chill Island Flow, adından da anlaşılacağı gibi sakinliği ve 'yavaş yaşam' felsefesini benimseyen, Ksamil'in en huzurlu dinlenme noktalarından biridir. Hafif müzik eşliğinde hamaklarda uzanabileceğiniz bu gizli köşe, kentsel gürültüden kaçıp kafa dinlemek için idealdir.",
        "en": "Chill Island Flow adopts a philosophy of 'slow living' and calm, serving as one of Ksamil's most peaceful retreats. A hidden corner where you can relax in hammocks to ambient music, it is the ideal spot to escape urban noise and clear your mind."
    },
    "ChIJsdAPUHVrWxMRsBOkZ4PmHFE": {
        "tr": "Ksamil Lifeguard noktası, plajların güvenliğini sağlayan ve sahil boyunca huzuru koruyan profesyonel bir gözetleme alanıdır. Ziyaretçilerin güvenle yüzebilmesi için çalışan personeli ve ilk yardım imkanlarıyla, kentin en güvenli tatil noktalarından birinin kalbidir.",
        "en": "The Ksamil Lifeguard point is a professional observation area ensuring safety and maintaining peace along the beaches. With staff dedicated to safe swimming and first-aid facilities, it is the heart of one of the town's most secure vacation destinations."
    },
    "ChIJNUnQOVprWxMRpo7wd8XnYlI": {
        "tr": "Tongo Adası Tekne Turu, Adriyatik'in saklı kalmış koylarına düzenlenen ve teknede taze balık barbeküsü sunan Ksamil'in en sevilen aktivitesidir. Kristal sularda yüzme molaları ve yerel içecekler eşliğinde geçen bu tur, kentin deniz kültürünü en iyi yansıtan deneyimdir.",
        "en": "The Boat Trip to Tongo Island is one of Ksamil's favorite activities, leading to hidden Adriatic coves and featuring a fresh fish BBQ on board. With swimming stops in crystal waters and local drinks, it's the experience that best reflects the town's maritime culture."
    },
    "ChIJFYB3zVVrWxMRNOsmJmYUoLU": {
        "tr": "Mëndra Traditional Albanian Restaurant, kuşaklar boyu aktarılan tariflerle Arnavutluk mutfağının en seçkin örneklerini sunan kentsel bir lezzet kalesidir. Odun ateşinde pişen etleri ve taze deniz mahsulleriyle, kentin gastronomi dünyasındaki en prestijli duraktır.",
        "en": "Mëndra Traditional Albanian Restaurant is a culinary stronghold offering the finest examples of Albanian cuisine through time-honored recipes. With wood-fired meats and fresh seafood, it stands as the most prestigious gastronomic landmark in town."
    },
    "ChIJi0wF0FNrWxMRUhEOsvnPy7A": {
        "tr": "Ksamil Beach East, kentin doğu yakasında yer alan ve daha sakin deniziyle bilinen, güneşin batışını izlemek için mükemmel bir sahil şerididir. Kayalıkların arasından süzülen berrak suyuyla, kentin kalabalığından uzaklaşıp doğayla baş başa kalmak isteyenlerin gizli limanıdır.",
        "en": "Ksamil Beach East, located on the town's eastern edge, is a coastal strip known for its calm seas and perfect sunset views. With clear water flowing through rocks, it’s a secret harbor for those looking to escape the crowds and stay close to nature."
    },
    "ChIJ0ajwIwBrWxMRy293ctJ0iuc": {
        "tr": "La Calita de Arena Blanca, adını bembeyaz kumlarından alan ve Akdeniz esintilerini Arnavutluk'a taşıyan şık ve butik bir plaj kulübüdür. Gurme kokteylleri ve rahat şezlongları ile kentsel sosyal hayatın en nezih ve modern deniz keyfini sunan duraklarındandır.",
        "en": "La Calita de Arena Blanca is a chic boutique beach club named for its white sands, bringing Mediterranean vibes to Albania. With gourmet cocktails and comfortable loungers, it offers one of the most refined and modern seaside experiences in the town's social life."
    },
    "ChIJnxF3UwBrWxMRCXa5ipCH7tA": {
        "tr": "Island Rocks, Ksamil adalarının çevresindeki doğal kaya oluşumlarıdır ve şnorkel tutkunları için bölgedeki en zengin su altı yaşamına ev sahipliği yapar. Suyun altındaki renkli balıklar ve mercan benzeri yapılarla, kentin su altı dünyasına açılan bir doğa penceresidir.",
        "en": "Island Rocks are natural rock formations around the Ksamil islands, hosting the richest underwater life in the region for snorkeling fans. With colorful fish and coral-like structures beneath the surface, it’s a natural window into the town's underwater world."
    },
    "ChIJZ3wyUABrWxMRbVI6a-mK6Fs": {
        "tr": "Instagrammable Spot, Ksamil'in turkuaz denizini ve adalarını en iyi açıdan gören, hatıra fotoğrafı çektirmek için kentin en popüler noktasıdır. Turkuazın her tonuna hakim bu eşsiz manzara, kente gelen her turistin dijital albümünde yer alan ikonik bir görsel duraktır.",
        "en": "This Instagrammable Spot is the most popular point in town to capture memories with the best views of Ksamil's turquoise sea and islands. Commanding every shade of blue, this unique vista is an iconic visual stop found in every traveler's digital album."
    },
    "ChIJf8bDewBrWxMRLhYgBgqvnPQ": {
        "tr": "Isola delle Ninne, ismini mitolojik hikayelerden alan ve berrak suyuyla büyüleyen kentsel bir gizli koydur. Sessizliği ve bakir doğasıyla bilinen bu alan, kentin en sakin sahillerinden biridir ve ziyaretçilerine gerçek bir huzur ve dinginlik vaat etmektedir.",
        "en": "Isola delle Ninne is a charming urban cove named after mythological tales, mesmerizing visitors with its clear waters. Known for its silence and untouched nature, it is one of the quietest shores in town, promising visitors true peace and serenity."
    },
    "ChIJqfOEVgBrWxMR0Tusl0-ZNLI": {
        "tr": "Sheqer Lake Park, Ksamil'in hemen arkasında yer alan ve tatlı su ile denizin buluştuğu noktadaki doğal bir kuş cenneti ve rekreasyon alanıdır. Yemyeşil bitki örtüsü ve yürüyüş yolları ile kentin doğa ile iç içe olan en ferah rotalarından biridir.",
        "en": "Sheqer Lake Park is a natural bird sanctuary and recreation area located behind Ksamil where fresh water meets the sea. With its lush vegetation and walking paths, it is one of the most refreshing routes in town for those seeking a connection with nature."
    },
    "ChIJT8n4Zs5rWxMRWz6-ahFHWpg": {
        "tr": "Tirana Hotel Ksamil, samimi aile işletmesi sıcaklığını modern konaklama imkanlarıyla birleştiren kentin en köklü otellerinden biridir. Sahile olan yakınlığı ve terasındaki yerel kahvaltı sunumu ile kente gelen ziyaretçiler için konforlu ve samimi bir konaklama durağıdır.",
        "en": "Tirana Hotel Ksamil is one of the town's long-standing hotels, merging a warm family-run feel with modern stay options. Its proximity to the beach and local terrace breakfast make it a comfortable and friendly hub for visitors traveling to the city."
    },
    "ChIJg7z3QPkUWxMRRIUwvnoG7E4": {
        "tr": "Oskar Hotel, Ksamil ve Saranda arasındaki stratejik konumu ve muazzam deniz manzaralı balkonları ile tanınan kentsel bir dinlenme merkezidir. Şık odaları ve profesyonel hizmet anlayışı ile kentin kuzey sahilindeki en prestijli konaklama duraklarından biridir.",
        "en": "Oskar Hotel is an urban retreat known for its strategic location between Ksamil and Saranda and balconies with immense sea views. With chic rooms and professional service, it stands as one of the most prestigious stay locations on the town's northern coast."
    },
    "ChIJyW6aysZrWxMRRO_28nm5jRg": {
        "tr": "Hotel NEBO, futuristik mimarisi ve Adriyatik'e tepeden bakan panoramik pencereleri ile Ksamil seyahatine lüks ve estetik katan bir konaklama noktasıdır. Akşamları gün batımını en iyi gören terasıyla kentin en stil sahibi ve modern yaşam alanlarından biri haline gelmiştir.",
        "en": "Hotel NEBO adds luxury and aesthetics to every Ksamil trip with its futuristic architecture and panoramic windows overlooking the Adriatic. With a terrace offering the best sunset views, it has become one of the town's most stylish and modern living spaces."
    },
    "ChIJo93F7L8UWxMR_kljVRSdtZ8": {
        "tr": "Eval Hotel Saranda, denize sıfır özel plaj alanı ve geniş havuzu ile Ksamil yakınlarında tam kapsamlı bir yaz tatili deneyimi sunmaktadır. Yerel ve dünya mutfaklarından seçkin lezzetler sunan restoranıyla kentin turizm haritasında kalitesiyle öne çıkan bir duraktır.",
        "en": "Eval Hotel Saranda offers a full summer vacation experience near Ksamil with its private beachfront and large swimming pool. Its restaurant serving elite local and global dishes makes it a standout destination on the town's tourism map."
    },
    "ChIJ9fkh-OQVWxMRnlY74EN80NA": {
        "tr": "The First Hotel Saranda, kentin canlanan turizm bölgesinde yer alan, modern tasarımı ve butik hizmet anlayışıyla gezginlerin yeni favorisidir. Şehrin enerjisini ve denizin huzurunu birleştiren konumuyla kentsel keşifler için ideal bir başlangıç noktası sunmaktadır.",
        "en": "The First Hotel Saranda is a new favorite for travelers in the town's reviving tourism district, known for its modern design and boutique service. Its location, blending city energy with seaside calm, offers an ideal starting point for every urban exploration."
    },
    "ChIJfzvgZgBCWxMROIrIIHGIGt4": {
        "tr": "EUCALYPTUS, ismini çevreleyen devasa okaliptüs ağaçlarından alan ve gölgesinde serin bir Ege-İyon mutfağı sunan kentsel bir gurme bahçesidir. Taze otlarla hazırlanan mezeleri ve özgün sunumlarıyla kentin gastronomi kültüründeki en doğal ve lezzetli duraklardan biridir.",
        "en": "EUCALYPTUS is a gourmet urban garden named after the surrounding giant trees, offering cool Aegean-Ionian cuisine in their shade. With appetizers prepared from fresh herbs and original service, it’s one of the most natural and tasty stops in the town's food culture."
    },
    "ChIJWyzT9gBCWxMRr_FDzc57WkA": {
        "tr": "Taverna Galini, geleneksel Arnavut ve Yunan lezzetlerini birleştiren kentsel bir deniz ürünleri evidir. Liman manzarası eşliğinde servis edilen günlük avlanmış balıkları ve samimi aile atmosferi ile kentin en köklü ve güvenilir lezzet durakları arasında yer almaktadır.",
        "en": "Taverna Galini is an urban seafood home merging traditional Albanian and Greek flavors. With daily catches served against harbor views and a warm family atmosphere, it ranks among the town's most long-standing and reliable culinary destinations."
    },
    "ChIJG4hykctrWxMRcH5Sq-E6uI0": {
        "tr": "Ciao Bar Restaurant, modern İtalyan dokunuşlarını Ksamil'in yerel malzemeleriyle harmanlayan, kentin en popüler gastronomi duraklarından biridir. Panoramik deniz manzaralı terası ve iddialı şarap kavıyla kentsel sosyal hayatın en prestijli akşam yemeği rotalarından biridir.",
        "en": "Ciao Bar Restaurant is one of the town's most popular gastronomic spots, blending modern Italian touches with Ksamil's local ingredients. With its panoramic terrace and ambitious wine cellar, it’s a prestigious dinner route in the town's social life."
    },
    "ChIJvwFT5MxrWxMR9u3cH8V_Wfc": {
        "tr": "Guvat Bar Restorant, denize hakim terası ve deniz mahsulleri kulesiyle ünlü olan Ksamil'in en ikonik restoranlarından biridir. Romantik akşam yemekleri ve şık sunumlarıyla kentin en özel günleri için tercih edilen, lezzet ve manzaranın buluştuğu en prestijli duraktır.",
        "en": "Guvat Bar Restorant is one of Ksamil's most iconic restaurants, famed for its terrace over the sea and signature seafood towers. A top choice for romantic dinners and chic service, it is the most prestigious landmark where flavor meets the Adriatic view."
    },
    "ChIJbVPuz7drWxMRGLFHFZrzZLM": {
        "tr": "Foga Beach Restaurant, kentsel kumsalda yer alan ve ayağınız kumdayken taze balık yeme imkanı sunan kentin en samimi plaj işletmelerinden biridir. Hafif müzik ve deniz esintisi eşliğinde sunulan Ege mezeleriyle, kentin sahil ruhunu en iyi yansıtan lezzet duraklarındandır.",
        "en": "Foga Beach Restaurant is one of the friendliest beach spots in town, offering fresh fish with your feet in the sand. Serving Aegean appetizers accompanied by soft music and sea breezes, it’s a flavor destination that best reflects the town's coastal spirit."
    },
    "ChIJDbReLs1rWxMR86b1eqbnrFQ": {
        "tr": "Veranda By Apollonia, sofistike tasarımı ve dünya mutfağından seçkin örnekleri ile Ksamil'in en lüks ve modern restoranıdır. Bembeyaz dekorasyonu ve turkuaz denize bakan devasa terasıyla kentsel sosyal hayatın en ikonik ve 'chic' buluşma noktası haline gelmiştir.",
        "en": "Veranda By Apollonia is Ksamil's most luxury and modern restaurant, featuring sophisticated design and elite global cuisine. With its white decor and vast terrace facing the turquoise sea, it has become the town's most iconic and 'chic' urban social hub."
    },
    "ChIJa8B3WchrWxMRdnQZ607_8o0": {
        "tr": "Restaurant Pizza Malasi, geleneksel İtalyan odun fırını tekniklerini Ksamil'in taze ürünleriyle birleştiren, kentin en sevilen ve samimi pizzacı duraklarından biridir. Ailelerin ve gençlerin favorisi olan mekan, kentin gastronomi haritasında samimiyetiyle öne çıkan bir duraktır.",
        "en": "Restaurant Pizza Malasi is a beloved and friendly pizzeria merging traditional Italian wood-fired techniques with Ksamil's fresh produce. A favorite for families and youth alike, it stands out on the town's gastronomic map for its warmth and authenticity."
    },
    "ChIJgbKsfdJrWxMRvYw5_vMdhSo": {
        "tr": "FastFood KOKO, kentin hızla gelişen bölgesinde yer alan ve yerel sokak lezzetlerini modern bir dokunuşla sunan kentsel bir atıştırmalık merkezidir. Taze malzemeleri ve hızlı servisiyle, kenti keşfederken pratik ve lezzetli bir mola vermek isteyenlerin uğrak durağıdır.",
        "en": "FastFood KOKO is an urban snack hub in the town's rapidly growing district, offering local street flavors with a modern twist. With fresh ingredients and quick service, it is a staple stop for those wanting a practical and tasty break while exploring the city."
    },
    "ChIJo8p-6MxrWxMRis9-kFm_gOk": {
        "tr": "Restuarant Momento, isminden de anlaşılacağı gibi Ksamil'de geçirdiğiniz anları unutulmaz kılan, kentin en nezih deniz ürünleri duraklarından biridir. Şık tasarımı ve Adriyatik'in mavisine bakan masalarıyla kentsel gastronomi dünyasında prestijli bir yer tutmaktadır.",
        "en": "Restaurarant Momento, as its name suggests, makes your Ksamil moments unforgettable as one of the town's most refined seafood destinations. With its chic design and tables facing the Adriatic blue, it holds a prestigious place in the town's culinary world."
    },
    "ChIJt_ETo9BrWxMR6y-K_Y5D7J8": {
        "tr": "Bar Restaurant Tre Ishujt, Ksamil'in meşhur üç adasına en yakın konumda yer alan ve panoramik manzara sunan kentsel bir lezzet kalesidir. Deniz mahsulleri risottosu ve ferahlatıcı içecekleri ile kentin manzara ve lezzet anlamındaki en ikonik ve prestijli duraklarındandır.",
        "en": "Bar Restaurant Tre Ishujt is a culinary stronghold offering panoramic views from its position closest to Ksamil's famous three islands. With seafood risotto and refreshing drinks, it stands as one of the town's most iconic and prestigious stops for both flavor and vistas."
    },
    "ChIJQyT2GThrWxMR7mD2C76rU9U": {
        "tr": "Joni Restaurant Ksamil, kentsel kıyıda yer alan ve modern Arnavut mutfağının en seçkin örneklerini sunan prestijli bir lezzet durağıdır. Şık ambiyansı ve denizin üzerindeki terasıyla, kentin gastronomi dünyasında kalite ve estetiğin buluştuğu en önemli rotalardan biridir.",
        "en": "Joni Restaurant Ksamil is a prestigious culinary destination on the urban coast, presenting elite examples of modern Albanian cuisine. With its chic ambiance and terrace over the waves, it’s a key route where quality and aesthetics meet in the town's food scene."
    }
}

for h in data["highlights"]:
    if h["id"] in updates:
        h["description"] = updates[h["id"]]["tr"]
        h["description_en"] = updates[h["id"]]["en"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Ksamil Batch 1 (40 venues).")
