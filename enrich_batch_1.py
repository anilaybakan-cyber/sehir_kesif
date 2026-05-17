from enrich_venues import enrich_venues

# BATCH 1: BODRUM, KAŞ, ÇEŞME

# BODRUM UPDATES
bodrum_updates = {
    "Karakaya": {
        "desc_tr": "Gümüşlük sırtlarında yer alan bu terk edilmiş Rum köyü, taş evleri ve dar sokaklarıyla tarih öncesi bir atmosfer sunar. Sessizliği ve Ege rüzgarını solumak, kentin karmaşasından kaçmak isteyenler için saklı bir sığınaktır.",
        "desc_en": "Perched on the hills above Gümüşlük, this abandoned Greek village features atmospheric stone houses and narrow alleys. It is a silent sanctuary for those looking to escape the hustle and bustle and soak in the Aegean breeze."
    },
    "Türkbükü Halk Plajı": {
        "desc_tr": "Bodrum'un en popüler ve şık duraklarından olan Türkbükü'ndeki bu sahil, denizin üzerindeki iskeleleri ve akşamları hareketlenen restoranlarıyla ünlüdür. Ege'nin serin sularında yüzerken bölgenin lüks dokusunu hissedebilirsiniz.",
        "desc_en": "One of Bodrum's most stylish spots, this beach in Türkbükü is famous for its over-water decks and vibrant seaside dining. It offers a perfect blend of refreshing Aegean waters and the region's elite atmosphere."
    },
    "Yalıkavak Halk Plajı": {
        "desc_tr": "Yalıkavak'ın rüzgarlı ama taze havasında yer alan bu geniş plaj, kristal netliğindeki deniziyle bilinir. Gün batımının en güzel izlendiği noktalardan biri olan sahil, hem yerli halkın hem de turistlerin vazgeçilmezidir.",
        "desc_en": "Known for its refreshing breeze and crystal-clear sea, this wide beach in Yalıkavak is a local favorite. It is also one of the prime spots on the peninsula to witness a spectacular sunset over the Aegean."
    },
    "Camel beach": {
        "desc_tr": "Adını sahilinde gezinen develerden alan bu plaj, sığ denizi ve ince kumuyla özellikle çocuklu ailelerin favorisidir. Kargı Koyu'nun doğal güzelliğini yansıtan sahil, Bodrum'un en geniş kumsal alanlarından birine sahiptir.",
        "desc_en": "Named after the camels that can often be seen on its sands, this beach is a family favorite for its shallow waters and fine sand. It boasts one of the largest sandy stretches in the area, showcasing the natural beauty of Kargı Bay."
    },
    "Aspat koyu ıssız adacık": {
        "desc_tr": "Aspat Koyu'nun açıklarında yer alan bu küçük adacık, sadece tekne ile ulaşılabilen bir huzur noktasıdır. Tertemiz denizi ve etrafındaki zengin deniz yaşamıyla şnorkel yapmak ve kalabalıklardan uzaklaşmak için idealdir.",
        "desc_en": "A small islet off Aspat Bay, this spot is a sanctuary of peace accessible only by boat. Its pristine waters and rich marine life make it a perfect destination for snorkeling and escaping the tourist crowds."
    },
    "Bağla Sitesi (BAĞLA KOYU EVLERİ)": {
        "desc_tr": "Bodrum'un en temiz koylarından biri olan Bağla'da yer alan bu bölge, turkuaz suları ve sakinliğiyle bilinir. Doğayla iç içe, huzurlu bir deniz günü geçirmek isteyenler için Yarımada'nın en sevilen duraklarından biridir.",
        "desc_en": "Located in one of Bodrum's cleanest bays, this area is renowned for its turquoise waters and tranquility. It is a beloved destination for those seeking a peaceful day by the sea, surrounded by natural beauty."
    },
    "Bardakçı koyu": {
        "desc_tr": "Bodrum merkezine en yakın koylardan biri olan Bardakçı, antik dönem efsanelerine konu olan bir su kaynağına sahiptir. Kaleden izlenen panoramik manzarası ve berrak deniziyle kentin içinde ama kentin dışında bir deneyim sunar.",
        "desc_en": "One of the closest bays to central Bodrum, Bardakçı is tied to ancient legends of natural springs. With its clear waters and panoramic views of the castle, it offers a refreshing escape right in the heart of town."
    },
    "Torba Plajı": {
        "desc_tr": "Zeytinlikler ve çam ağaçlarıyla çevrili Torba Plajı, sakin denizi ve huzurlu atmosferiyle bilinir. Bodrum'un kalabalığından uzak, geleneksel balıkçı köyü dokusunu hala koruyan bu sahil, ruhunuzu dinlendirmek için mükemmeldir.",
        "desc_en": "Surrounded by pine trees and olive groves, Torba Beach is known for its calm sea and serene atmosphere. It still retains the charm of a traditional fishing village, offering a perfect spot to relax away from the crowds."
    },
    "Karaada": {
        "desc_tr": "Bodrum'un tam karşısında yer alan Karaada, mağaralarından çıkan şifalı çamurları ve sıcak su kaynaklarıyla ünlüdür. Adanın yemyeşil doğası ve tekne turlarının vazgeçilmez duraklarından biri olması, burayı eşsiz kılar.",
        "desc_en": "Located right across from Bodrum, Black Island (Karaada) is famous for its therapeutic mud baths and natural hot springs found within caves. Its lush greenery and crystal coves make it a top stop for boat tours."
    },
    "Cennet Koyu": {
        "desc_tr": "Adının hakkını veren Cennet Koyu, masmavi suları çevreleyen çam ormanlarıyla Yarımada'nın en bakir noktalarından biridir. Sadece tekneyle veya zorlu bir yolla ulaşılabilmesi, buranın sessizliğini ve doğasını korumuştur.",
        "desc_en": "True to its name (Paradise Bay), this is one of the peninsula's most untouched spots, where pine forests meet turquoise waters. Its limited access has preserved its natural beauty and peaceful atmosphere."
    },
    "D-Marin Turgutreis Marina": {
        "desc_tr": "Bodrum Yarımadası'nın en batısında yer alan bu marina, eşsiz adalar manzarası ve kaliteli yaşam alanlarıyla ünlüdür. Marina içindeki butikler ve sahil yolu, özellikle gün batımında kentin en şık yürüyüş rotasını oluşturur.",
        "desc_en": "Located at the western tip of the peninsula, this marina is famous for its stunning island views and upscale facilities. The promenade and boutiques offer a refined experience, especially during the legendary local sunsets."
    }
}

# KAŞ UPDATES
kas_updates = {
    "Patara Beach": {
        "desc_tr": "Türkiye'nin en uzun plajlarından olan Patara, aynı zamanda Caretta Caretta'ların yumurtlama alanıdır. Kum tepeleri ve antik kentin içinden geçerek ulaşılan bu devasa sahil, masalsı gün batımıyla ünlüdür.",
        "desc_en": "One of Turkey’s longest beaches, Patara is a protected nesting ground for Caretta Caretta turtles. Accessible through ancient ruins and vast sand dunes, it offers a cinematic setting for watching the sunset."
    },
    "Saklikent National Park": {
        "desc_tr": "Eşen Çayı'nın sarp kayalıklar arasında binlerce yılda şekillendirdiği bu devasa kanyon, serin suları ve göğe uzanan duvarlarıyla büyüleyicidir. Kanyonun içinde yürümek ve rafting yapmak adrenalin dolu bir deneyim sunar.",
        "desc_en": "Carved by icy river waters over millennia, this massive canyon features towering walls and refreshing waterfalls. Walking through the gorge or rafting down the river is an adrenaline-filled highlight for nature lovers."
    },
    "Hidayet Bay Beach": {
        "desc_tr": "Çukurbağ Yarımadası'nda gizlenmiş olan bu koy, akvaryum gibi berrak deniziyle şnorkel tutkunlarının vazgeçilmezidir. Gürültüden uzak, zeytin ağaçlarının gölgesinde huzurlu bir deniz keyfi için en ideal noktalardan biridir.",
        "desc_en": "Tucked away on the Çukurbağ Peninsula, this bay boasts aquarium-clear waters, making it a favorite for snorkeling. Framed by olive trees, it offers a peaceful and secluded Mediterranean swimming experience."
    },
    "Küçük Çakıl Plajı": {
        "desc_tr": "Kaş'ın merkezinde yer alan bu küçük ama ikonik plaj, yer altından fışkıran soğuk kaynak suları sayesinde yazın en sıcak günlerinde bile buz gibi ferah bir deniz deneyimi sunar. Çevresindeki mekanlarla çok canlıdır.",
        "desc_en": "A tiny but iconic pebble beach in central Kaş, famous for its icy-cold natural springs that bubble up from the seabed. It provides a refreshing blast of cool water even during the peak of the Mediterranean summer."
    },
    "Büyükçakıl Plajı": {
        "desc_tr": "Kaş merkezine yürüme mesafesinde olan bu geniş plaj, akşamüstü sahil kenarındaki restoranların dekorlarıyla adeta bir şölen alanına dönüşür. Denizin içinden çıkan tatlı su kaynakları suyu serin ve berrak tutar.",
        "desc_en": "A short walk from the town center, this wide pebble beach is famous for its seaside restaurants that come alive at twilight. Natural freshwater springs keep the sea exceptionally clear and refreshingly cool."
    },
    "Kas Merkez Mosque": {
        "desc_tr": "Kaş'ın çarşı meydanına hakim konumuyla dikkat çeken bu cami, bölgenin mimari dokusunu ve kültürel merkezini temsil eder. Meydanın hareketliliği içinde huzurlu duruşuyla kentin ruhunu yansıtır.",
        "desc_en": "Overlooking the bustling town square, this mosque is a central landmark that reflects the local architectural and cultural fabric. It stands as a peaceful presence amidst the vibrant energy of Kaş's main streets."
    }
}

# ÇEŞME UPDATES
cesme_updates = {
    "Çeşme Kalesi": {
        "desc_tr": "1508 yılında II. Bayezid tarafından inşa edilen bu görkemli kale, hem kentin tarihini hem de körfezin manzarasını ayaklar altına serer. Müzesindeki paha biçilemez antik eserler ve kulelerinden görülen deniz panoraması büyüleyicidir.",
        "desc_en": "Built in 1508 by Sultan Bayezid II, this imposing fortress offers a panoramic view of the bay and a deep dive into local history. Its museum houses rare ancient artifacts, while its battlements provide stunning coastal vistas."
    },
    "Alaçatı Çarşı": {
        "desc_tr": "Alaçatı'nın ruhunu yansıtan bu tarihi çarşı, lavanta kokulu taş sokakları, antika dükkanları ve şık tasarım butikleriyle ünlüdür. Akşam saatlerinde kentin en canlı ve büyüleyici atmosferine ev sahipliği yapar.",
        "desc_en": "The heart of Alaçatı, this historic bazaar is famous for its stone-paved alleys, antique shops, and designer boutiques. In the evening, it transforms into a magical destination with vibrant cafes and a romantic atmosphere."
    },
    "Alaçatı Yel Değirmenleri": {
        "desc_tr": "Alaçatı'nın girişinde yer alan 150 yıllık bu tarihi taş değirmenler, kasabanın en ikonik sembolüdür. Özellikle gün batımında, Alaçatı manzarasını tepeden izlemek ve hatıra fotoğrafı çektirmek için kentin en popüler noktasıdır.",
        "desc_en": "These 150-year-old stone windmills stand at the entrance of Alaçatı as its most iconic symbol. They offer a perfect vantage point to view the town and are especially popular for capturing sunset photos."
    },
    "Çeşme Marina": {
        "desc_tr": "Modern mimari ile Ege'nin sıcaklığını birleştiren bu ödüllü marina, lüks yatların yanı sıra dünya mutfağından seçkin restoranları ve butikleriyle kentin en nezih sosyal alanlarından biridir.",
        "desc_en": "Linking modern design with Aegean warmth, this award-winning marina is a social hub featuring luxury yachts, high-end boutiques, and exquisite international restaurants right by the water."
    },
    "Altınkum Plajı": {
        "desc_tr": "Adını altın sarısı kumlarından alan bu plaj, soğuk ve kristal netliğindeki deniziyle Çeşme'nin en sevilen sahillerinden biridir. Geniş kumsalı ve doğasıyla Ege'nin ferahlığını sonuna kadar hissettirir.",
        "desc_en": "Famous for its golden sands and refreshingly cool, crystal-clear water, Altınkum is one of Çeşme's most beloved beaches. Its wide shore and pristine nature offer a perfect sense of Aegean freedom."
    },
    "Pırlanta Plajı": {
        "desc_tr": "Adını güneş altında parlayan incecik kumlarından alan bu plaj, sürekli esen rüzgarıyla kitesurf ve windsurf tutkunlarının dünya çapındaki duraklarındandır. Sığ deniziyle çocuklar için de oldukça güvenlidir.",
        "desc_en": "Named for its sands that glisten like diamonds under the sun, this beach is a world-renowned destination for kitesurfing and windsurfing thanks to its steady winds and shallow, safe waters."
    },
    "Delikli Koy": {
        "desc_tr": "Beyaz kayalıkları ve doğanın şekillendirdiği delikli kaya yapısıyla ünlenen bu bakir koy, Çeşme'nin en sessiz ve huzurlu köşelerinden biridir. Kamp tutkunları ve kalabalıktan kaçanlar için eşsiz bir doğa harikasıdır.",
        "desc_en": "Famous for its striking white limestone formations and a naturally hollowed rock, this secluded bay is a haven of peace. It's a favorite for campers and those seeking a quiet escape amidst wild, natural beauty."
    },
    "Ilıca Plajı": {
        "desc_tr": "Deniz içindeki termal su kaynakları sayesinde ılık olan suyu ve bembeyaz kumlarıyla Ilıca, adeta doğal bir kaplıca havuzu gibidir. Sığ denizi ve turkuaz rengiyle Çeşme'nin en ikonik sahillerinden biridir.",
        "desc_en": "Famous for its warm waters fed by underwater thermal springs, Ilıca is like a natural spa pool by the sea. Its turquoise waters and fine white sands make it one of the most iconic beaches in Turkey."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Batch 1 Enrichment: Bodrum, Kaş, Çeşme...")
enrich_venues("bodrum", bodrum_updates)
enrich_venues("kas", kas_updates)
enrich_venues("cesme", cesme_updates)
print("✨ Batch 1 Enrichment Complete.")
