from enrich_venues import enrich_venues

# BATCH: BODRUM SYSTEMATIC COMPLETION - PART 2

bodrum_bulk_2_updates = {
    "Kızılhisarlı Mustafa Paşa Camii": {
        "desc_tr": "Bodrum Limanı'nın girişinde yer alan bu zarif cami, 1723 yılında Kaptan-ı Derya Kızılhisarlı Mustafa Paşa tarafından yaptırılmıştır. Beyaz badanalı duvarları ve kentin kentsel dokusuyla uyumlu mimarisiyle, Bodrum'un en önemli Osmanlı miraslarından biridir.",
        "desc_en": "Standing at the entrance of Bodrum Harbor, this elegant mosque was built in 1723 by Admiral Kızılhisarlı Mustafa Paşa. With its whitewashed walls and architecture harmonizing with the town's texture, it is a key Ottoman heritage site."
    },
    "Herodotus Statue": {
        "desc_tr": "Antik Halikarnassos'ta doğan ve 'Tarihin Babası' olarak bilinen ünlü tarihçi Herodot'un anısına dikilen bu heykel, kentin köklü tarihini simgeler. Liman yakınındaki konumuyla ziyaretçilere kentin binlerce yıllık entelektüel geçmişini hatırlatır.",
        "desc_en": "This statue honors Herodotus, the 'Father of History,' who was born in ancient Halicarnassus. Located near the harbor, it serves as a proud reminder of the city's deep intellectual roots spanning thousands of years."
    },
    "Private Boat": {
        "desc_tr": "Bodrum'un saklı koylarını ve kristal sularını keşfetmenin en özel yolu olan özel tekne turları, kişiye özel bir Ege serüveni sunar. Kendi rotanızı belirleyebileceğiniz bu deneyim, denizin ortasında lüks, huzur ve özgürlüğü birleştirir.",
        "desc_en": "The most exclusive way to explore Bodrum's hidden bays and crystal waters, private boat tours offer a personalized Aegean adventure. Tailoring your own route allows you to blend luxury, tranquility, and freedom on the open sea."
    },
    "Gulet Bodrum Queen": {
        "desc_tr": "Geleneksel Bodrum gulet mimarisinin en şık örneklerinden biri olan Bodrum Queen, misafirlerine lüks bir mavi yolculuk deneyimi yaşatır. Geniş güvertesi ve konforlu kabinleriyle, Ege'nin serin sularında unutulmaz bir tatilin adresidir.",
        "desc_en": "A prime example of traditional Bodrum gulet craftsmanship, the Bodrum Queen offers guests a luxurious Blue Cruise experience. With its spacious decks and comfortable cabins, it’s the gateway to an unforgettable holiday on the Aegean."
    },
    "Luna art tattoo bodrum": {
        "desc_tr": "Bodrum merkezinde sanatın vücut bulduğu Luna Art, kentin en popüler dövme stüdyolarından biridir. Hijyenik ortamı ve yetenekli sanatçılarıyla, tatil anılarını kalıcı birer sanat eserine dönüştürmek isteyenlerin uğrak noktasıdır.",
        "desc_en": "Where art meets the body in central Bodrum, Luna Art is one of the town's most popular tattoo studios. With its hygienic setting and talented artists, it's the go-to spot for turning holiday memories into permanent masterpieces."
    },
    "Alman Kulesi": {
        "desc_tr": "Bodrum Kalesi'nin içindeki bu tarihi kule, Orta Çağ'da Alman şövalyeleri tarafından savunma amaçlı kullanılmıştır. Kule üzerindeki orijinal kabartmalar ve şövalye armaları, Avrupa tarihinin Ege kıyılarındaki izlerini büyüleyici bir şekilde sergiler.",
        "desc_en": "Inside Bodrum Castle, this historic tower was used for defense by German knights in the Middle Ages. Its original reliefs and knightly coats of arms provide a fascinating look at European history on the shores of the Aegean."
    },
    "Bodrum promenad": {
        "desc_tr": "Bodrum Limanı boyunca uzanan bu geniş sahil yolu, kentin en canlı ve fotografik rotasıdır. Bir yanda lüks yatlar diğer yanda begonvillerle süslü dükkanlar eşliğinde yürürken, kentin enerjisini ve deniz kokusunu her adımda hissedebilirsiniz.",
        "desc_en": "Stretching along the Bodrum Harbor, this wide promenade is the city's most vibrant and photographic route. Walking between luxury yachts and bougainvillea-covered shops, you feel the city's energy and the scent of the sea."
    },
    "Atrium Hotel": {
        "desc_tr": "Bodrum merkezinde yer alan Atrium Hotel, antik Roma mimarisinden esinlenen avlusu ve palmiye ağaçlarıyla çevrili havuzuyla huzurlu bir vaha sunar. Samimi atmosferi ve kente yakınlığıyla, klasik bir Bodrum tatili arayanlar için idealdir.",
        "desc_en": "Located in central Bodrum, Atrium Hotel offers a peaceful oasis with its Roman-inspired courtyard and palm-fringed pool. Its warm atmosphere and proximity to the town center make it ideal for a classic Bodrum getaway."
    },
    "Hillstone Bodrum Hotel& SPA": {
        "desc_tr": "Kentin tepelerinde konumlanan Hillstone, Bodrum Kalesi ve denizin üzerinde yükselen panoramik manzarasıyla lüksün adresidir. Geniş spa alanları, sonsuzluk havuzları ve şık tasarımıyla, yarımadanın en prestijli konaklama deneyimlerinden birini vaat eder.",
        "desc_en": "Perched on the city's heights, Hillstone defines luxury with its panoramic views of Bodrum Castle and the sea. With extensive spa facilities, infinity pools, and elegant design, it promises one of the peninsula's most prestigious stays."
    },
    "Sevin Otel Bodrum": {
        "desc_tr": "Bodrum'un merkezinde, çarşıya ve denize sadece bir adım mesafedeki Sevin Otel, geleneksel konukseverliği uygun fiyatlı konforla birleştirir. Begonvillerle süslü bahçesiyle, kentin kalbinde samimi bir konaklama alternatifi sunar.",
        "desc_en": "In the heart of Bodrum, just steps from the bazaar and the sea, Sevin Otel blends traditional hospitality with affordable comfort. Its bougainvillea-fringed garden offers a cozy accommodation alternative in the town center."
    },
    "Nagi Beach Hotel": {
        "desc_tr": "Gümbet'in en popüler noktalarından birinde yer alan Nagi Beach, geniş plajı ve yeşil bahçeleriyle hem eğlenceyi hem huzuru arayanlara hitap eder. Denize sıfır konumu ve canlı atmosferiyle, Bodrum'un enerjik tatil ruhunu mükemmel yansıtır.",
        "desc_en": "Located in one of Gümbet's top spots, Nagi Beach caters to those seeking both fun and peace with its wide beach and lush gardens. Its seafront location and vibrant vibe perfectly reflect Bodrum's energetic holiday spirit."
    },
    "Queen's Apart Hotel": {
        "desc_tr": "Gümbet'in sosyal yaşamına yakınlığıyla bilinen Queen's Apart, ev konforunda bir tatil sunan ferah odalarıyla tanınır. Özellikle aileler ve uzun süreli konaklamalar için ideal, rahat ve samimi bir atmosfer sunar.",
        "desc_en": "Known for its proximity to Gümbet's social scene, Queen's Apart offers a home-away-from-home experience with its spacious apartments. It provides a comfortable and friendly atmosphere, ideal for families and long stays."
    },
    "AYAZ AQUA BEACH HOTEL": {
        "desc_tr": "Gümbet koyuna hakim konumuyla Ayaz Aqua, geniş havuzları ve özel plajıyla her yaşa uygun bir tatil dünyası sunar. Canlı akşam eğlenceleri ve her şey dahil konseptiyle, Bodrum'da kesintisiz eğlence arayanların tercihidir.",
        "desc_en": "Overlooking Gümbet Bay, Ayaz Aqua offers a world of holiday fun with its large pools and private beach. With its all-inclusive concept and nightly entertainment, it is a go-to for those seeking non-stop fun in Bodrum."
    },
    "Delfi Hotel Spa & Wellness": {
        "desc_tr": "Bodrum merkezine yakınlığı ve profesyonel spa hizmetleriyle tanınan Delfi Hotel, kentin en köklü konaklama noktalarından biridir. Geniş bahçesi, havuzu ve sağlık merkeziyle, hem dinlenmek hem de kente karışmak isteyenler için doğru adrestir.",
        "desc_en": "Famous for its proximity to central Bodrum and professional spa services, Delfi Hotel is one of the town's established landmarks. With its expansive gardens and pool, it's perfect for those wanting to relax while staying near the action."
    },
    "Doria Hotel Bodrum": {
        "desc_tr": "Bitez'in tepesinde, Ege Denizi'ne hakim bir noktada yer alan Doria Hotel, modern ve minimalist tasarımıyla öne çıkar. Özel plajı, gurme restoranları ve sessizliğiyle, Bodrum'da sofistike ve huzurlu bir kaçış noktasıdır.",
        "desc_en": "Perched on a hill in Bitez overlooking the Aegean, Doria Hotel stands out with its modern and minimalist design. With its private beach and gourmet dining, it is a sophisticated and peaceful escape in Bodrum."
    },
    "Okaliptus Otel": {
        "desc_tr": "Adını gölgesine sığındığı okaliptüs ağaçlarından alan bu Bitez klasiği, denize sıfır konumu ve samimi dokusuyla ünlüdür. Bahçesindeki huzur ve denizin hemen yanındaki konumuyla, gerçek Bodrum ruhunu her mevsim yaşatır.",
        "desc_en": "A Bitez classic named after the shade-giving eucalyptus trees, this hotel is famous for its beachfront location and cozy vibe. Its peaceful garden and proximity to the waves keep the authentic spirit of Bodrum alive year-round."
    },
    "Dinç Pansiyon": {
        "desc_tr": "Bodrum sahil yolunda bir efsane olan Dinç Pansiyon, mütevazı yapısı ve denize nazır odalarıyla onlarca yıldır gezginlerin favorisidir. Kentin sosyal hayatının kalbinde, her sabah denize karşı uyanmak isteyenler için nostaljik bir duraktır.",
        "desc_en": "A legend on the Bodrum coast road, Dinç Pansiyon has been a traveler favorite for decades with its modest charm and seafront rooms. It’s a nostalgic spot for those wanting to wake up to the sound of waves in the heart of town."
    },
    "L'onda Oda Bodrum": {
        "desc_tr": "Marina bölgesinin girişinde, modern tasarımı geleneksel taş işçiliğiyle birleştiren bu butik otel, bir tasarım harikasıdır. Şık bahçesi ve rafine detaylarıyla, kentin içinde lüks ve estetik dolu bir konaklama deneyimi sunar.",
        "desc_en": "At the entrance to the Marina area, this boutique hotel is a design marvel blending modern aesthetics with traditional stonework. Its chic garden and refined details offer a stylish and artistic stay within the city."
    },
    "La Pasion Bodrum": {
        "desc_tr": "Bodrum'un beyaz sokaklarından birinde gizlenmiş bu şık avlu restoranı, İspanyol mutfağının en seçkin örneklerini sunar. Romantik atmosferi, geniş şarap kavı ve yaratıcı tapaslarıyla, kentin en prestijli akşam yemeği mekanlarından biridir.",
        "desc_en": "Hidden in one of Bodrum's white alleys, this chic courtyard restaurant serves exquisite Spanish cuisine. With its romantic atmosphere and creative tapas, it is one of the city's most prestigious and unique dining destinations."
    },
    "Köşem Cafe & Restaurant & Bar": {
        "desc_tr": "Limanın en hareketli köşesinde yer alan Köşem, sabah kahvaltısından gece kokteyllerine kadar günün her saati canlıdır. Bodrum Kalesi'ni tam karşıdan gören eşsiz manzarasıyla, kentin en iyi seyir ve lezzet noktalarından biridir.",
        "desc_en": "Located at the harbor's busiest corner, Köşem pulses with life from breakfast until late-night cocktails. With a perfect direct view of Bodrum Castle, it’s one of the town's prime spots for watching the world go by with a great meal."
    },
    "Körfez Restoran": {
        "desc_tr": "Bodrum'un en köklü deniz ürünleri lokantalarından biri olan Körfez, yıllardır değişmeyen kalitesiyle bir gastronomi kalesidir. Limana nazır masalarında sunulan taze balıkları ve meşhur mezeleriyle, kentin gerçek denizci ruhunu yansıtır.",
        "desc_en": "One of Bodrum's most established seafood landmarks, Körfez is a culinary stronghold of consistent quality. Its harbor-front tables serve the freshest daily catch and famous appetizers, perfectly reflecting the town's maritime spirit."
    },
    "Limoon Eskiçeşme": {
        "desc_tr": "Eskiçeşme'nin huzurlu sokaklarında saklı olan bu mekan, butik tasarımı ve özenle hazırlanmış kahvaltılarıyla meşhurdur. Samimi ve modern bir mahalle kafesi havasıyla, Bodrum'da güne keyifli başlamak isteyen yerel halkın favorisidir.",
        "desc_en": "Tucked away in the peaceful streets of Eskiçeşme, this spot is famous for its boutique design and carefully crafted breakfasts. With a warm, modern neighborhood-cafe feel, it's a local favorite for starting the day in Bodrum."
    },
    "Ayhan Suite Hotel Bodrum": {
        "desc_tr": "Gümbet'in girişinde yer alan Ayhan Suite, modern ve ferah daire konseptiyle özellikle uzun konaklayan gezginler için tasarlanmıştır. Şık havuzu ve kente kolay ulaşım sağlayan konumuyla konforlu bir Bodrum üssüdür.",
        "desc_en": "Located at the entrance to Gümbet, Ayhan Suite is designed for convenience with its modern and spacious apartment concept. With a stylish pool and easy city access, it provides a comfortable home base in Bodrum."
    },
    "Alin's Kafe & Restoran": {
        "desc_tr": "Bodrum Limanı'nın girişinde, modern tasarımı ve zengin menüsüyle gün boyu hizmet veren Alin's, kentin en popüler buluşma noktalarından biridir. Kaleye karşı kahvenizi yudumlamak için Yarımada'nın en ikonik ve konforlu duraklarındandır.",
        "desc_en": "At the gateway to Bodrum Harbor, Alin's is a popular all-day hub known for its modern design and extensive menu. It's one of the peninsula's most iconic spots to sip coffee with a stunning direct view of the castle."
    },
    "Begonvil": {
        "desc_tr": "Adını Bodrum’un simgesi olan çiçekten alan Begonvil, samimi atmosferi ve kentin ruhunu yansıtan pastel tonlarıyla huzur dolu bir duraktır. Çiçeklerin gölgesinde Ege lezzetlerini tadabileceğiniz, kentin karmaşasından uzak bir kaçış noktasıdır.",
        "desc_en": "Named after Bodrum's signature flower, Begonvil is a peaceful spot radiating the town's spirit with its pastel tones. It offers a escape from the urban rush, where you can savor Aegean flavors in the shade of blooming flowers."
    },
    "Denizciler Derneği Cafe": {
        "desc_tr": "Bodrum'un denizci yüreğinin attığı bu kafe, kentin gerçek sahipleri olan kaptanların ve süngercilerin uğrak yeridir. Liman içindeki otantik konumu ve meşhur tavşan kanı çayıyla, Bodrum'un en samimi ve gerçek kentsel mirasıdır.",
        "desc_en": "The heart of Bodrum's maritime community, this cafe is where captains and sponge divers gather. With its authentic harbor setting and famous Turkish tea, it's one of the town's most genuine and soulful heritage sites."
    },
    "Trafo Cafe & Restaurant": {
        "desc_tr": "Eski bir elektrik trafosunun kültür merkezine dönüşümüyle yaratılan bu mekan, kentin sanatsal yüzünü temsil eder. Bodrum Kalesi'ne hakim geniş terası ve şık restoranıyla, kentin en özel manzara ve kültür duraklarından biridir.",
        "desc_en": "Housed in a converted historical transformer station, this venue represents Bodrum's artistic side. With its expansive terrace overlooking the castle and its chic restaurant, it’s a premier spot for culture and cocktails."
    },
    "Kraft Bistro": {
        "desc_tr": "Yeni nesil gastronomi anlayışını Bodrum'a taşıyan Kraft Bistro, zanaatkar lezzetleri ve geniş kraft içecek menüsüyle tanınır. Modern dekorasyonu ve yaratıcı mutfağıyla, kentin genç ve dinamik sosyal hayatının önemli bir parçasıdır.",
        "desc_en": "Bringing a new-wave culinary approach to Bodrum, Kraft Bistro is known for its artisanal flavors and extensive craft beverage menu. Its modern decor and creative kitchen make it a staple of the city's dynamic social scene."
    },
    "CEBECIZADE TURK KAHVESI": {
        "desc_tr": "Bodrum çarşısının nostaljik sokaklarında, geleneksel Türk kahvesi sanatını en saf haliyle sunan bu mekan bir tarih hazinesidir. Közde pişen kahvesi ve otantik sunumuyla, kentin karmaşasında huzurlu bir mola noktasıdır.",
        "desc_en": "A historical gem in the nostalgic alleys of the Bodrum bazaar, this spot serves traditional Turkish coffee in its purest form. With its slow-brewed coffee and authentic presentation, it's a peaceful island in the city buzz."
    },
    "MUSTO BİSTRO": {
        "desc_tr": "Marina bölgesinin en sevilen buluşma noktası olan Musto Bistro, dünya mutfağından seçkin lezzetleri samimi bir mahalle havasında sunar. Şık dekorasyonu ve gün boyu süren enerjisiyle, Bodrum kentsel sosyal hayatının en prestijli durağıdır.",
        "desc_en": "The most beloved meeting point in the Marina area, Musto Bistro offers premium international flavors with a friendly neighborhood feel. Its chic decor and all-day energy make it a prestigious staple of Bodrum's social life."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Bodrum Bulk - Part 2)...")
enrich_venues("bodrum", bodrum_bulk_2_updates)
print("✨ Systematic Enrichment - Bodrum Bulk Part 2 Complete.")
