from enrich_venues import enrich_venues

# BATCH: KAŞ SYSTEMATIC COMPLETION - FINAL PART

kas_final_updates = {
    "Kahramanlar Turizm": {
        "desc_tr": "Kaş'ın yerel ulaşım ve lojistik ağında uzmanlaşmış olan Kahramanlar Turizm, havalimanı transferlerinden çevre turlarına kadar geniş bir hizmet yelpazesi sunar. Kentin çevresindeki saklı köyleri ve antik kentleri keşfetmek isteyenler için güvenilir bir operasyon merkezidir.",
        "desc_en": "Specializing in Kaş's local transportation and logistics, Kahramanlar Turizm offers a wide range of services from airport transfers to scenic tours. It’s a reliable hub for those looking to explore the hidden villages and ancient cities surrounding the town."
    },
    "Giant Stride Shop & Cafe & Bar": {
        "desc_tr": "Kaş'ın dünyaca ünlü dalış kültürünün kalbinde yer alan Giant Stride, hem profesyonel bir dalış merkezi hem de denizcilerin buluştuğu keyifli bir kafedir. Su altı maceralarınızdan sonra limana karşı bir şeyler yudumlamak için kentin en bohem duraklarından biridir.",
        "desc_en": "At the heart of Kaş's world-famous diving culture, Giant Stride is both a professional dive center and a charming cafe where maritime souls gather. It’s one of the town's most bohemian spots to sip a drink facing the harbor after underwater adventures."
    },
    "Miramar Pansiyon": {
        "desc_tr": "Kaş Limanı'na nazır, begonvillerin gölgesindeki bu pansiyon, kentin en köklü ve samimi konaklama noktalarından biridir. Geleneksel Akdeniz ev sıcaklığını modern konforla birleştiren mekan, her sabah kentin uyanışına tanıklık etmek isteyenler için idealdir.",
        "desc_en": "Overlooking the Kaş Harbor in the shade of bougainvilleas, this pension is one of the most established and friendly stay options in town. Blending Mediterranean warmth with modern comfort, it’s ideal for those wanting to witness the town's awakening each morning."
    },
    "Naturel": {
        "desc_tr": "Kaş'ın doğasından ilham alan bu dükkan, el yapımı sabunlardan doğal yağlara ve yerel el sanatlarına kadar geniş bir seçki sunar. Kentin saf ve organik ruhunu yanınızda götürmek için keşfedebileceğiniz en kokulu kentsel duraktır.",
        "desc_en": "Inspired by Kaş's nature, this shop offers a wide selection from handmade soaps to natural oils and local handicrafts. It is the most fragrant urban stop to discover if you want to take the city’s pure and organic spirit with you."
    },
    "Sardunya Restaurant": {
        "desc_tr": "Kaş'ın denize en yakın masalarına sahip olan Sardunya, Akdeniz mutfağının en seçkin deniz ürünlerini ve mezelerini sunar. Dalga sesleri eşliğinde yenen romantik bir akşam yemeği için kentin en ikonik ve prestijli lezzet duraklarından biridir.",
        "desc_en": "Featuring tables set right by the waves, Sardunya serves the Mediterranean’s finest seafood and appetizers. It is one of the town's most iconic and prestigious culinary destinations for a romantic dinner accompanied by the sound of the sea."
    },
    "Kas Camping": {
        "desc_tr": "Kent merkezine sadece bir adım mesafede, denize sıfır bir doğa harikası olan Kaş Camping, kentin en özgür konaklama alanıdır. Zeytin ağaçları altındaki kafesi ve tertemiz deniziyle, yıllardır Kaş müdavimlerinin vazgeçilmez kentsel vaha durağıdır.",
        "desc_en": "A natural wonder right by the sea and just steps from the town center, Kaş Camping is the city's freest accommodation area. With its cafe under olive trees and pristine waters, it’s been an indispensable urban oasis for Kaş regulars for decades."
    },
    "Oxygen Pub": {
        "desc_tr": "Kaş'ın sosyal hayatının en hareketli noktalarından biri olan Oxygen, geniş içecek menüsü ve modern tasarımıyla kentin nabzını tutar. Genç ve dinamik bir kitleye hitap eden mekan, kentsel eğlence anlayışını sokağa taşıyan enerjisiyle bilinir.",
        "desc_en": "One of the most vibrant spots in Kaş's social scene, Oxygen captures the city's pulse with its extensive drink menu and modern design. Catering to a young, dynamic crowd, it is known for its energy that brings urban entertainment to the streets."
    },
    "Noel Baba Cafe&Bistro": {
        "desc_tr": "Çarşı içindeki merkezi konumu ve sıcak atmosferiyle Noel Baba, gün boyu kentin her kesiminden misafirini ağırlar. Ev yapımı lezzetleri ve samimi servisiyle, Kaş sokaklarında yürürken keyifli bir lezzet molası vermek isteyenlerin adresidir.",
        "desc_en": "With its central location in the bazaar and warm atmosphere, Noel Baba welcomes guests from all walks of life. With home-style flavors and friendly service, it's the go-to for a delightful break while wandering through the Kaş streets."
    },
    "No.10 Cafe Kaş": {
        "desc_tr": "Kaş'ın yeni nesil kafe kültürünü temsil eden No.10, özellikle taze hazırlanan pastaları ve gurme kahveleriyle meşhurdur. Şık ve minimalist dekorasyonuyla, kentin kentsel ritminden kopmadan huzurlu bir mola vermek isteyenler için çok özel bir duraktır.",
        "desc_en": "Representing Kaş's new-wave cafe culture, No.10 is famous for its freshly baked cakes and gourmet coffee. With its chic, minimalist decor, it’s a special spot for a peaceful break without losing the city's urban rhythm."
    },
    "Kaş Fenerbahçeliler Derneği": {
        "desc_tr": "Spor tutkusunu kentsel sosyal hayatla birleştiren bu nokta, hem maç günlerinin heyecanlı merkezi hem de gün boyu samimi sohbetlerin adresidir. Kaş'ın yerel dinamizmini ve toplumsal bağlarını yansıtan sıcak bir duraktır.",
        "desc_en": "Merging sports passion with urban social life, this spot is an exciting hub on match days and a warm address for friendly chats. It is a welcoming stop reflecting Kaş’s local dynamism and community bonds."
    },
    "Mola çay evi": {
        "desc_tr": "Uzun Çarşı'nın hemen girişinde, kentin en samimi geleneksel duraklarından olan Mola Çay Evi, meşhur tavşan kanı çayı ve kentsel nostaljisiyle bilinir. Kaş'ın o meşhur insan trafiğini izlemek ve kısa bir 'mola' vermek için en doğru yerdir.",
        "desc_en": "Right at the entrance to Uzun Çarşı, Mola Çay Evi is one of the town's warmest traditional stops, known for its classic Turkish tea and urban nostalgia. It’s the perfect place to watch the famous Kaş foot traffic and take a brief 'break'."
    },
    "Süleyman Çavuş Kahvehanesi (Tatlı-Limonata)": {
        "desc_tr": "Kaş çarşısının yaşayan efsanesi olan bu kahve hane, özellikle taze limonuyla hazırlanan ev yapımı limonatası ve geleneksel tatlılarıyla meşhurdur. Kentin tarihini ve samimi esnaf kültürünü her yudumda hissettiren kentsel bir mirastır.",
        "desc_en": "A living legend of the Kaş bazaar, this coffee house is famous for its homemade lemonade and traditional sweets. It’s an urban heritage site that lets you feel the town's history and sincere artisan culture with every sip."
    },
    "Dessert Shop": {
        "desc_tr": "Kaş çarşısının tatlı duraklarından biri olan bu nokta, geleneksel Türk tatlılarından kentin kendine has kurabiyelerine kadar geniş bir seçki sunar. Tatilinize lezzetli ve tatlı bir anı katmak için kentin en uğrak kentsel lezzet köşelerinden biridir.",
        "desc_en": "One of the sweet stops in the Kaş bazaar, this spot offers a wide range from traditional Turkish desserts to the town's unique cookies. It's a popular urban flavor corner to add a delicious and sweet memory to your holiday."
    },
    "Kas Simit": {
        "desc_tr": "Kaş sabahlarının olmazsa olmazı taze simitleri burada bulabilirsiniz. Susam kokusuyla sokağı saran bu küçük fırın, kentin yerel ritmini ve en taze kentsel kahvaltı geleneğini en samimi haliyle sunar.",
        "desc_en": "The essential part of Kaş mornings, you can find the freshest simits here. With the scent of sesame filling the street, this small bakery offers the town's local rhythm and freshest urban breakfast tradition in its simplest form."
    },
    "Coflow Coffee": {
        "desc_tr": "Nitelikli kahvenin Kaş'taki en popüler adresi olan Coflow, zanaatkar kavurma yöntemleri ve modern baristasıyla tanınır. Kentin enerjik ve genç ruhunu yansıtan bu mekan, kentsel sosyal hayatın en yeni ve prestijli duraklarındandır.",
        "desc_en": "Kaş's top destination for specialty coffee, Coflow is known for its artisanal roasting methods and modern baristas. Reflecting the town's energetic and young soul, it’s one of the newest and most prestigious stops in urban social life."
    },
    "Old Town Cafe-Bar & Billiards": {
        "desc_tr": "Eski çarşının otantik atmosferinde yer alan bu mekan, hem bilardo keyfi hem de geniş içecek menüsüyle akşam saatlerinin uğrak noktasıdır. Kentin kentsel eğlence kültüründe kendine has bir yere sahip olan sakin ve keyifli bir duraktır.",
        "desc_en": "Located in the authentic atmosphere of the old bazaar, this venue is a popular evening spot with its billiard tables and extensive drink menu. It has a unique place in the town’s urban entertainment culture as a calm and enjoyable stop."
    },
    "Mumi Kaş Nargile Cafe & Kaş Kahvaltı": {
        "desc_tr": "Kaş Marina'ya karşı zengin bir serpme kahvaltı ve akşamları huzurlu bir nargile keyfi sunan Mumi, panoramik manzarasıyla bilinir. Kentin hem dinamik hem de sakin yüzünü tek bir noktada buluşturan kentsel bir seyir balkonudur.",
        "desc_en": "Offering a rich traditional breakfast against the Kaş Marina and a peaceful shisha experience in the evenings, Mumi is known for its panoramic views. It’s an urban viewing balcony merging the city's dynamic and calm sides."
    },
    "Blue Soul Coffee & More": {
        "desc_tr": "Modern bir tasarım anlayışını kaliteli kahveyle birleştiren Blue Soul, Kaş'ın en şık kentsel köşelerinden biridir. Sadece bir kafe değil, aynı zamanda kentin ilham veren bohem stilini yansıtan bir tasarım ve buluşma alanıdır.",
        "desc_en": "Combining a modern design ethos with quality coffee, Blue Soul is one of Kaş's most stylish urban corners. It’s not just a cafe, but a design and meeting space reflecting the town's inspiring bohemian style."
    },
    "Nazilli Cafe": {
        "desc_tr": "Kaş'ın en meşhur ev yemeği duraklarından olan Nazilli, özellikle taze zeytinyağlıları ve kente has 'Nazilli pidesi' ile bilinir. Onlarca yıldır değişmeyen lezzet kalitesiyle, kentin bir gastronomi kalesi ve yerel favorisidir.",
        "desc_en": "One of Kaş's most famous home-cooking destinations, Nazilli is known for its fresh olive oil dishes and signature 'Nazilli pide.' With flavor quality unchanged for decades, it is a culinary stronghold and local favorite."
    },
    "Akay Cafe": {
        "desc_tr": "Kentin sosyal merkezine yakın, ağaçların gölgesindeki bu samimi kafe, Kaş'ın sakinliğini hissetmek isteyenler için bir sığınaktır. Taze hazırlanan meyve suları ve kentsel mahalle havasıyla, gün boyu huzur veren bir duraktır.",
        "desc_en": "Close to the social center yet tucked under the shade of trees, this friendly cafe is a sanctuary for those wanting to feel Kaş's tranquility. With fresh juices and an urban neighborhood vibe, it’s a peaceful all-day stop."
    },
    "Bla Bla Cafe Kaş": {
        "desc_tr": "Dinamik tasarımı ve neşeli ismiyle Kaş sosyal hayatının en renkli duraklarından biri olan Bla Bla, yaratıcı kokteylleri ve genç atmosferiyle bilinir. Kentin kentsel eğlence haritasında modern ve samimi bir duraktır.",
        "desc_en": "One of the most colorful stops in Kaş social life, Bla Bla is known for its dynamic design, cheerful name, and creative cocktails. It is a modern and friendly landmark on the city's urban entertainment map."
    },
    "Shotbar": {
        "desc_tr": "Kaş gece hayatının en küçük ama en iddialı mekanlarından olan Shotbar, sokağa taşan enerjisiyle tanınır. Kentin kalbinde, müziğin ve eğlencenin nabzını tutan, samimiyetiyle kentin kentsel ritmini yükselten bir duraktır.",
        "desc_en": "One of the smallest yet boldest venues in Kaş nightlife, Shotbar is known for its energy that spills into the streets. In the heart of town, it boosts the urban rhythm with music, fun, and genuine sincerity."
    },
    "Dott's": {
        "desc_tr": "Kaş'ta modern bir bistro ve şarap evi deneyimi sunan Dott's, rafine lezzetleri ve şık ambiyansıyla kentin en prestijli duraklarından biridir. Akdeniz'in yerel malzemelerini dünya mutfağıyla birleştiren kentsel bir gurme merkezidir.",
        "desc_en": "Offering a modern bistro and wine house experience in Kaş, Dott's is one of the town's most prestigious spots with its refined flavors and chic ambiance. It is an urban gourmet hub merging local ingredients with global cuisine."
    },
    "L'Apéro Kaş": {
        "desc_tr": "Fransız mutfağının inceliğini Kaş'ın Akdenizli ruhuyla birleştiren L'Apéro, kentin en özgün restoranlarından biridir. Geniş şarap kavı ve yaratıcı menüsüyle, kentsel kentsel sosyal hayatta sofistike bir akşam yemeği arayanların adresidir.",
        "desc_en": "Blending the finesse of French cuisine with Kaş's Mediterranean soul, L'Apéro is one of the city's most unique restaurants. With its extensive wine cellar and creative menu, it's the destination for a sophisticated urban dinner."
    },
    "Cistern 5th century BC": {
        "desc_tr": "Kentin kentsel dokusu içine gizlenmiş bu antik Likya sarnıcı, kentin binlerce yıl öncesindeki su yönetimi dehasını sergiler. Bugün bir sanat galerisi veya kentsel bir hafıza mekanı olarak kullanılan sarnıç, Kaş'ın mistik tarihinin sessiz tanığıdır.",
        "desc_en": "Tucked within the urban fabric, this ancient Lycian cistern showcases the water-management genius from millennia ago. Used today as an art gallery or a site of urban memory, it is a silent witness to Kaş's mystical history."
    },
    "Kastellorizo Folk Art Museum (Kavos Mosque)": {
        "desc_tr": "Hemen karşıdaki Meis Adası'nın girişinde yer alan bu eski cami, günümüzde halk sanatları müzesi olarak hizmet vermektedir. Adanın zengin kültürel geçmişini ve el emeği eserlerini sergileyen bu tarihi yapı, Kaş ziyaretinin mecburi bir parçasıdır.",
        "desc_en": "Located at the entrance to neighboring Meis Island, this former mosque now serves as a folk art museum. Exhibiting the island's rich cultural past and handicrafts, this historic building is an essential part of any Kaş visit."
    },
    "Meduseum - Megisti Puzzle Museum": {
        "desc_tr": "Meis Adası'ndaki bu benzersiz müze, dünyanın her yerinden gelen antik ve modern bulmacaları sergileyerek zihinsel bir yolculuk sunar. Küçük ama entelektüel derinliği büyük olan bu mekan, Kaş'ın karşı kıyısındaki en ilginç duraktır.",
        "desc_en": "This unique museum on Meis Island offers a mental journey by exhibiting ancient and modern puzzles from around the world. Small in size but rich in intellectual depth, it is the most intriguing stop across the water from Kaş."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Kaş Bulk - FINAL)...")
enrich_venues("kas", kas_final_updates)
print("✨ Systematic Enrichment - Kaş Bulk FINAL Complete.")
