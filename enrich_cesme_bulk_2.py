from enrich_venues import enrich_venues

# BATCH: ÇEŞME SYSTEMATIC COMPLETION - PART 2

cesme_bulk_2_updates = {
    "atasuıts apart otel restaurant leventin yeri balık restaurant": {
        "desc_tr": "Dalyan Köyü'nün en samimi köşesinde yer alan Levent'in Yeri, taze deniz ürünlerini kentsel karmaşadan uzak bir bahçe ortamında sunar. Mezelerdeki ustalığı ve her sabah denizden gelen taze balıklarıyla, kentin gerçek balıkçı mutfağını temsil eder.",
        "desc_en": "Set in a cozy corner of Dalyan Village, Levent'in Yeri serves fresh seafood in a peaceful garden setting away from the urban rush. With its mastery of appetizers and daily catch, it represents the town's authentic maritime kitchen."
    },
    "Dalyan Küçük Ev - Bistro / Event": {
        "desc_tr": "Dalyan'ın tarihi dokusuna sadık kalarak dekore edilmiş bu şık bistro, hem gurme lezzetleri hem de özel etkinliklere ev sahipliği yapan atmosferiyle bilinir. Kentsel estetiği Ege neşesiyle birleştiren, kentin en özel kutlama ve yeme-içme noktalarından biridir.",
        "desc_en": "Decorated with loyalty to Dalyan's historic fabric, this chic bistro is known for both gourmet flavors and its event-ready atmosphere. Merging urban aesthetics with Aegean joy, it’s one of the town's most special celebration and dining spots."
    },
    "Kumrucu Hikmet": {
        "desc_tr": "Çeşme çarşısının en sevilen ve en köklü kumrucularından biri olan Hikmet, odun ateşinde kızaran susamlı ekmekleriyle meşhurdur. Geleneksel kumru lezzetini en hızlı ve en lezzetli haliyle kentsel ritmin içinde sunan bir duraktır.",
        "desc_en": "One of the most beloved and long-standing Kumru shops in the Çeşme bazaar, Hikmet is famous for its sesame bread toasted over wood fires. It offers the traditional Kumru flavor at its fastest and tastiest within the city's pulse."
    },
    "Fish Restaurant": {
        "desc_tr": "Dalyan'ın balıkçı limanı boyunca sıralanan bu tesisler, Ege'nin en taze ürünlerini denize sıfır sofralarda buluşturur. Kentin denizle olan kadim bağını, taze rakı-balık sofralarında en derin haliyle yaşayabileceğiniz kentsel bir duraktır.",
        "desc_en": "Lined along Dalyan's fishing harbor, these establishments bring the Aegean's freshest bounty to seafront tables. It’s an urban stop where you can deeply experience the town's ancient bond with the sea at traditional Raki-fish tables."
    },
    "Çeşme Tekne Turu / Grandstar Çeşme Tekne Turları": {
        "desc_tr": "Çeşme'den Eşek Adası ve Karaada gibi saklı cennetlere yelken açan Grandstar turları, kentin en eğlenceli deniz yolculuğunu sunar. Mavi ile yeşilin buluştuğu koylarda gün boyu süren eğlence, kentin 'mavi yolculuk' geleneğinin en canlı parçasıdır.",
        "desc_en": "Sailing from Çeşme to hidden paradises like Eşek Island and Karaada, Grandstar tours offer the town's most joyful sea journey. The all-day fun in bays where blue meets green is a vibrant part of the peninsula's 'Blue Cruise' tradition."
    },
    "Balıkçı Niyazi": {
        "desc_tr": "Çeşme sahil yolunun efsaneleşmiş isimlerinden olan Balıkçı Niyazi, rafine servis anlayışı ve zengin meze çeşitliliğiyle bir gastronomi kalesidir. Kentsel şıklığı denizin dinginliğiyle birleştiren mekan, en prestijli akşam yemeklerinin adresidir.",
        "desc_en": "A legendary name on the Çeşme coast road, Balıkçı Niyazi is a culinary stronghold with its refined service and rich appetizer variety. Merging urban elegance with the stillness of the sea, it’s a premier address for prestigious dinners."
    },
    "Gizli Meyhane": {
        "desc_tr": "Alaçatı'nın begonvilli dar sokakları arasına saklanmış bu meyhane, adı gibi gizemli ve samimi bir atmosfer sunar. Geleneksel Ege şarkıları eşliğinde kentin kentsel gürültüsünden uzak, nostaljik ve kaliteli bir kentsel akşam vaat eder.",
        "desc_en": "Tucked away in Alaçatı's narrow, bougainvillea-filled alleys, this tavern offers a mysterious and warm atmosphere true to its name. It promises a nostalgic urban evening with traditional Aegean songs, away from the city's noise."
    },
    "Parmis House": {
        "desc_tr": "Çeşme'nin kalbinde taş mimari ile modern butik anlayışı birleştiren Parmis House, kentsel huzuru en estetik haliyle sunar. Begonvillerle süslü bahçesi ve özenle dekore edilmiş odalarıyla, kentin bohem ruhuna sanatsal bir dokunuş katar.",
        "desc_en": "Blending stone architecture with modern boutique flair in the heart of Çeşme, Parmis House offers urban tranquility in its most aesthetic form. With its flowery garden and carefully decorated rooms, it adds an artistic touch to the town's spirit."
    },
    "Fırat Mert Restoran": {
        "desc_tr": "Çeşme'nin yerel lezzet hafızasında önemli bir yer tutan Fırat Mert, taze deniz ürünleri ve geleneksel pişirme teknikleriyle tanınır. Limana hakim konumu ve kentsel samimiyetiyle, kentin en sevilen aile ve deniz restoranlarından biridir.",
        "desc_en": "Holding an important place in Çeşme's local food memory, Fırat Mert is known for fresh seafood and traditional cooking techniques. With its harbor view and urban warmth, it's one of the town's most beloved family seafood spots."
    },
    "Kumrucu Çınar": {
        "desc_tr": "Çeşme'nin kentsel gastronomisinde kumrunun en çıtır adresi olan Çınar, hızlı ve lezzetli servisiyle bilinir. Kentin sosyal ritminin bir parçası olan bu mekan, kumruyu geleneksel usulde en kaliteli malzemelerle sunan bir kentsel duraktır.",
        "desc_en": "Known for the crispest 'Kumru' in Çeşme's urban gastronomy, Çınar is famous for quick and delicious service. A part of the city's social rhythm, it serves the traditional sandwich with top-quality ingredients."
    },
    "ÖMÜR PİDE ÇEŞME": {
        "desc_tr": "Çeşme merkezinin en köklü pide fırınlarından olan Ömür Pide, kuşaktan kuşağa aktarılan lezzet kalitesiyle bilinir. İncecik hamuru ve kente has malzemeleriyle, kentsel esnaf kültürünün en samimi ve gerçek lezzet miraslarındandır.",
        "desc_en": "One of central Çeşme's oldest pita bakeries, Ömür Pide is known for quality passed down through generations. With its thin dough and local ingredients, it is one of the most warming and authentic flavor heritages of local artisan culture."
    },
    "La Cuisine": {
        "desc_tr": "Alaçatı'nın sofistike kentsel dokusunda, modern ve yaratıcı bir mutfak deneyimi sunan La Cuisine, gastronomi tutkunlarının prestijli durağıdır. Şık sunumları ve kentin kentsel estetiğiyle bütünleşen tasarımıyla kentin elit restoranları arasındadır.",
        "desc_en": "Offering a modern and creative culinary experience in Alaçatı's sophisticated fabric, La Cuisine is a prestigious stop for foodies. It ranks among the town's elite restaurants with its chic presentations and design integrated with urban aesthetics."
    },
    "Grand Rüya Butik Hotel & Cafe Bar": {
        "desc_tr": "Çeşme'nin kentsel merkezinde yer alan bu tesis, rüya gibi bir konaklamayı modern bir kafe-bar konseptiyle birleştirir. Kentin kentsel hareketliliğine yakınlığı ve şık tasarımıyla, hem dinlenmek hem de şehre karışmak isteyenler için ideal bir üstür.",
        "desc_en": "Situated in central Çeşme, this venue combines a dream-like stay with a modern cafe-bar concept. Its proximity to urban activity and chic design make it an ideal base for those wanting to both relax and merge with the city vibe."
    },
    "Cafe De Lucchi": {
        "desc_tr": "Çeşme Marina'nın en fotografik köşelerinden birinde yer alan Cafe De Lucchi, modern tasarımı ve marina manzaralı masalarıyla bilinir. Gün boyu kaliteli kahve ve kentsel sosyal hayatın en iyi seyir noktalarından birini sunan şık bir duraktır.",
        "desc_en": "Located in one of Çeşme Marina's most photographic corners, Cafe De Lucchi is known for its modern design and harbor-view tables. It’s a stylish spot providing quality coffee and one of the best vantage points for urban social life."
    },
    "SIDIKA": {
        "desc_tr": "Alaçatı'nın en popüler modern meyhane konseptlerinden biri olan Sıdıka, Ege otları ve zeytinyağlılarındaki ustalığıyla tanınır. Kentsel bohem ruhunu kadeh sesleriyle birleştiren, kentin en nezih ve kaliteli kentsel akşam duraklarındandır.",
        "desc_en": "One of Alaçatı's most popular modern tavern concepts, Sıdıka is famous for its mastery of Aegean herbs and olive oil dishes. Merging urban bohemian spirit with the sound of clinking glasses, it is one of the town's most refined evening stops."
    },
    "Ilhan Nargile": {
        "desc_tr": "Çeşme çarşısının huzurlu bir köşesinde, geleneksel nargile keyfini kentsel nostaljiyle birleştiren İlhan, kentin bir buluşma klasiğidir. Taze çayı ve otantik atmosferiyle, kentin kentsel karmaşasından kaçıp derin sohbetler etmek isteyenlerin adresidir.",
        "desc_en": "In a peaceful corner of the Çeşme bazaar, İlhan combines traditional shisha with urban nostalgia as a local meeting classic. With fresh tea and an authentic vibe, it is the home for deep chats away from the city's rush."
    },
    "petit coin": {
        "desc_tr": "Adı gibi 'küçük bir köşe' olan bu saklı kafe, Alaçatı'nın kalbinde huzurlu ve estetik bir vaha sunar. Butik lezzetleri, kaliteli tatlıları ve kentsel kentsel sükunetiyle, kentin en özel ve sessiz kentsel kaçış noktalarından biridir.",
        "desc_en": "True to its name as a 'small corner,' this hidden cafe offers a peaceful and aesthetic oasis in the heart of Alaçatı. With boutique flavors, quality sweets, and urban silence, it is one of the town's most exclusive and quiet escape spots."
    },
    "Tius Bar": {
        "desc_tr": "Çeşme'nin sosyal hayatının en enerjik ve modern duraklarından biri olan Tius Bar, yaratıcı kokteylleri ve kaliteli müzikleriyle tanınır. Kentin kentsel eğlence haritasında tasarım ve konforu birleştiren prestijli bir kentsel duraktır.",
        "desc_en": "One of the most energetic and modern stops in Çeşme social life, Tius Bar is known for its creative cocktails and premium music. It is a prestigious urban landmark merging design and comfort on the peninsula's entertainment map."
    },
    "Cafe Red And White": {
        "desc_tr": "Çeşme merkezindeki ikonik tasarımıyla dikkat çeken Red and White, gün boyu süren canlı atmosferi ve kentsel marina manzarasıyla sevilir. Modern kentsel yaşamın her tonunu yansıtan bu kafe, kentin popüler bir mola ve sosyal merkezidir.",
        "desc_en": "Standing out with its iconic design in central Çeşme, Red and White is loved for its all-day vibe and urban marina views. Reflecting every shade of modern urban life, it is a popular gathering and social hub in town."
    },
    "MUQA CAFE": {
        "desc_tr": "Tasarımdaki ustalığı kahve kültürüyle harmanlayan MUQA, kentin modern kentsel kentsel estetiğini temsil eden çok şık bir duraktır. Kaliteli mola anları ve kentsel ilham arayanlar için kentin en nezih ve yeni nesil konseptlerinden biridir.",
        "desc_en": "Blending design mastery with coffee culture, MUQA is a very stylish spot representing the town's modern urban aesthetics. It is one of the most refined new-wave concepts for those seeking quality breaks and urban inspiration."
    },
    "Yuka coffee": {
        "desc_tr": "Yeni nesil (3. dalga) kahve akımını kentin kalbine taşıyan Yuka Coffee, zanaatkar kavurma yöntemleri ve minimalist tasarımıyla bilinir. Kentin genç ve dinamik kentsel yüzünü yansıtan en taze ve modern lezzet duraklarından biridir.",
        "desc_en": "Bringing the new-wave (3rd wave) coffee movement to the heart of the city, Yuka Coffee is known for its artisanal roasting and minimalist design. It's one of the freshest and most modern flavor stops, reflecting the town's young urban face."
    },
    "Pusat Marin Çeşme": {
        "desc_tr": "Çeşme'nin denizci ruhunu kentsel bir yaşam tarzıyla birleştiren Pusat Marin, hem denizcilik ekipmanları hem de şık butik anlayışıyla bilinir. Kentin denizle olan derin bağını modern ve kentsel bir tasarım çerçevesinde sunan özel bir noktadır.",
        "desc_en": "Merging Çeşme's maritime soul with an urban lifestyle, Pusat Marin is known for both marine equipment and its chic boutique flair. It’s a special spot presenting the town's deep bond with the sea within a modern urban design frame."
    },
    "Açaí Concept Caffé Türkiye": {
        "desc_tr": "Dünya çapındaki 'sağlıklı kentsel yaşam' trendini kentin sahil şeridine taşıyan bu mekan, taze meyve kâseleri ve modern sunumlarıyla meşhurdur. Dinamik ve fit bir kentsel kaçış noktası arayanların kentsel favorisidir.",
        "desc_en": "Bringing the global 'healthy urban living' trend to the peninsula's coastline, this venue is famous for its fresh acai bowls and modern service. It's an urban favorite for those seeking a dynamic and fit lifestyle retreat."
    },
    "Hasan Mersin Sakız Reçel Tatlı ve Dondurma Evi": {
        "desc_tr": "Çeşme'nin simgesi olan sakız ağaçlarından gelen bereketi kavanozlara sığdıran Hasan Mersin, kentin en tatlı kentsel mirasıdır. Onlarca yıldır sürdürülen sakız reçeli ve tatlı geleneğiyle kentin lezzet pusulasıdır.",
        "desc_en": "Capturing the bounty of Çeşme's signature mastic trees in jars, Hasan Mersin is the town's sweetest urban heritage. A flavor compass with a decades-long tradition of mastic jam and confectionery."
    },
    "Coffee Mood No:50 & Çeşme": {
        "desc_tr": "Çeşme çarşısının enerjisini modern bir kahve evi konseptiyle buluşturan Coffee Mood, kentin kentsel buluşma noktalarından biridir. Yaratıcı kahve menüsü ve kentsel sokağın nabzını tutan konumuyla kentin popüler bir durağıdır.",
        "desc_en": "Merging the energy of the Çeşme bazaar with a modern coffee house concept, Coffee Mood is one of the city's urban meeting hubs. A popular landmark with a creative coffee menu and a location that captures the street's pulse."
    },
    "Bi Cafe Bistro & Lounge": {
        "desc_tr": "Gündüz şık bir bistro, gece ise kentsel bir lounge olan bu mekan, kentsel sosyal hayatın en konforlu ve modern adreslerinden biridir. Seçkin menüsü ve kentin merkezindeki prestijli konumuyla bir kentsel klasiktir.",
        "desc_en": "A chic bistro by day and an urban lounge by night, this venue is one of the most comfortable and modern addresses for urban social life. A city classic with an elite menu and a prestigious central location."
    },
    "Seçkin Çay Ocağı": {
        "desc_tr": "Çeşme çarşısının kalbinde, zamana karşı direnen en samimi kentsel duraklardan biri olan Seçkin, gerçek bir kentsel buluşma noktasıdır. Taze çayı ve esnaf kültürüyle, kentin en samimi kentsel dokusunu burada soluyabilirsiniz.",
        "desc_en": "A warming urban stop in the heart of the Çeşme bazaar that resists time, Seçkin is a true local meeting point. Here you can breathe in the town's most sincere urban fabric through fresh tea and artisan culture."
    },
    "Çınaraltı Cafe & Kahvaltı": {
        "desc_tr": "Asırlık çınar ağaçlarının gölgesinde, kentin en geleneksel ve meşhur kahvaltı deneyimini sunan bu mekan bir kentsel ikondur. Çeşme'nin meşhur boyozu ve gevrekleriyle güne kentsel bir Ege ritmiyle başlamak için en doğru yerdir.",
        "desc_en": "Under the shade of centuries-old plane trees, this venue offers the city's most traditional and famous breakfast experience as an urban icon. The best place to start the day with an Aegean rhythm, featuring Çeşme's famous pastries."
    },
    "Bedevi Ayayorgi - Çeşme": {
        "desc_tr": "Egzotik ve bohem tasarımıyla Ayayorgi Koyu'nda fark yaratan Bedevi, kentin en lüks ve enerjik kentsel eğlence komplekslerinden biridir. Kentsel eğlenceyi doğanın turkuazıyla birleştiren, kentin en iddialı kentsel duraklarındandır.",
        "desc_en": "Standing out in Ayayorgi Bay with its exotic and bohemian design, Bedevi is one of the town's most luxurious and energetic entertainment complexes. An ambitious urban landmark merging modern party culture with nature's turquoise."
    },
    "Zum Alaçatı": {
        "desc_tr": "Alaçatı'nın gece hayatına modern ve enerjik bir soluk getiren Zum, kentin en popüler dans ve kentsel sosyal duraklarından biridir. Yüksek kaliteli müzik ve tasarım odaklı atmosferiyle kentin dinamik kentsel ruhunu yansıtır.",
        "desc_en": "Bringing a modern and energetic breath to Alaçatı nightlife, Zum is one of the most popular dance and urban social stops. It reflects the town's dynamic spirit with high-quality music and a design-focused atmosphere."
    },
    "MERTPARADISE": {
        "desc_tr": "Kentin saklı kalmış doğal güzelliklerini modern bir resort konforuyla sunan Mertparadise, kentsel huzur ve lüksün buluşma noktasıdır. Geniş kumsal alanı ve profesyonel hizmetiyle kentin prestijli kentsel kaçış noktalarından biridir.",
        "desc_en": "Presenting hidden natural beauty with modern resort comfort, Mertparadise is where urban peace and luxury meet. With its wide beach area and professional service, it stands as a prestigious urban escape."
    },
    "Chilly Çeşme": {
        "desc_tr": "Modern gastronomi anlayışını kentin sahil şeridine taşıyan Chilly, yaratıcı menüsü ve şık kentsel atmosferiyle bilinir. Kentin genç ve kentsel kitlelerce sevilen, yeni nesil bir lezzet ve kentsel sosyal durağıdır.",
        "desc_en": "Bringing modern culinary concepts to the coastline, Chilly is known for its creative menu and chic urban atmosphere. A new-generation flavor and social hub beloved by the town's young and trendy urban crowd."
    },
    "Escape Beach Alaçatı": {
        "desc_tr": "Alaçatı Port'un en popüler plaj kulüplerinden olan Escape, sığ ama pırıl pırıl denizi ve eğlenceli aktiviteleriyle kentsel bir tatil klasiğidir. Aileler ve genç kitleler için kentin en enerjik kentsel deniz noktalarından biridir.",
        "desc_en": "One of Alaçatı Port's most popular beach clubs, Escape is an urban holiday classic with its shallow, sparkling waters and fun activities. One of the town's most energetic sea spots for families and young crowds alike."
    },
    "Alaçatı Borçın Su Sporları": {
        "desc_tr": "Dünyanın en önemli rüzgar sörfü merkezlerinden olan Alaçatı koyunda, profesyonel eğitim ve su sporları imkanı sunan bu nokta bir kentsel spor kalesidir. Kentin rüzgarla olan bağını en heyecanlı haliyle keşfedebileceğiniz kentsel bir duraktır.",
        "desc_en": "Found in the Alaçatı bay, one of the world's top windsurfing hubs, this spot is a sports stronghold providing professional training. An urban landmark where you can experience the town's bond with the wind at its most exciting."
    },
    "Hacı Memiş Cami": {
        "desc_tr": "Hacımemiş mahallesinin kalbinde yer alan bu tarihi cami, kentin kentsel tarihinde ve kültürel dokusunda önemli bir yere sahiptir. Taş mimarisi ve dingin atmosferiyle, kentin modernleşen yapısı içinde tarihin kentsel soluğudur.",
        "desc_en": "In the heart of the Hacımemiş district, this historic mosque holds a key place in the town's urban history and cultural fabric. With its stone architecture, it is the urban breath of history within the city's modern layout."
    },
    "Alaçatı Pazaryeri Camii": {
        "desc_tr": "Eski bir kiliseden camiye dönüştürülen ve kentsel bir hoşgörü sembolü olan bu yapı, kentin en ilginç kentsel mimari örneklerinden biridir. Kentsel tarihin katmanlarını ve kentin çok kültürlü geçmişini en iyi anlatan kentsel duraktır.",
        "desc_en": "A symbol of urban shared history, this former church converted to a mosque is one of the town's most intriguing architectural examples. It's the best urban stop to understand the city's layered and multicultural past."
    },
    "Küçük Ev": {
        "desc_tr": "Alaçatı çarşısındaki tarihi ve şirin yapısıyla tanınan bu butik mekan, ev konforunda lezzetler ve samimi bir kentsel atmosfer sunar. Kentin kentsel sosyal haritasında sıcak ve mütevazı bir lezzet kentsel durağıdır.",
        "desc_en": "Known for its historic and charming structure in the Alaçatı bazaar, this boutique spot offers home-style flavors and a warm vibe. A sincere and modest flavor stop on the town's urban social map."
    },
    "Alaçatı Sulak Alanı": {
        "desc_tr": "Kentin hemen kıyısında yer alan bu doğal ekosistem, flamingo gibi pek çok göçmen kuşa ev sahipliği yapan bir kentsel doğa mucizesidir. Kentin kentsel yapısı içindeki bu yeşil vaha, kentsel ekolojik dengenin en hassas kentsel mirasıdır.",
        "desc_en": "This natural ecosystem right by the town is an urban wonder hosting many migratory birds like flamingos. A green oasis within the urban layout, it is the most sensitive ecological heritage of the peninsula."
    },
    "Birds of Alaçati": {
        "desc_tr": "Alaçatı'nın zengin biyobölgeleri ve sulak alanlarındaki kuş çeşitliliğini gözlemleyebileceğiniz bu kentsel tema alanı, kentin kentsel doğa turizmindeki en özel noktasıdır. Kentin kentsel ekolojisini keşfetmek isteyenler için benzersiz bir duraktır.",
        "desc_en": "An urban theme area where you can observe the bird diversity in Alaçatı's rich bio-regions, marking the town's most special spot for nature tourism. A unique stop for those wanting to explore the peninsula's urban ecology."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Çeşme Bulk - Part 2)...")
enrich_venues("cesme", cesme_bulk_2_updates)
print("✨ Systematic Enrichment - Çeşme Bulk Part 2 Complete.")
