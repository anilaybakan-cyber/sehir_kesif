from enrich_venues import enrich_venues

# BATCH 1: BODRUM, KAŞ, ÇEŞME - PART 2

# BODRUM UPDATES
bodrum_updates = {
    "Pedasa Antik Kenti": {
        "desc_tr": "Leleg uygarlığına başkentlik yapmış bu saklı antik kent, zeytin ağaçları arasındaki doğa yürüyüşü parkurlarıyla ulaşılır. Gökyüzüyle birleşen sur kalıntıları ve sessiz atmosferi, Bodrum'un binlerce yıllık tarihine yolculuk yapmak isteyenler için eşsizdir.",
        "desc_en": "Once the capital of the Lelegian civilization, this hidden ancient city is reached via scenic trails through olive groves. Its standing ruins and silent atmosphere provide a unique journey into Bodrum's ancient history, away from the coastal crowds."
    },
    "Dibeklihan Kültür ve Sanat Köyü": {
        "desc_tr": "Geleneksel Ege mimarisinin modern sanatla buluştuğu Dibeklihan, sergi salonları, atölyeleri ve şık restoranlarıyla Yarımada'nın kültür kalbidir. Akşamları düzenlenen açık hava konserleri ve film gösterimleri buraya masalsı bir ruh katar.",
        "desc_en": "Where traditional Aegean architecture meets modern art, Dibeklihan is the peninsula's cultural heart with its galleries, workshops, and boutique dining. Its open-air concerts and cinema nights offer a magical experience under the stars."
    },
    "Akvaryum Koyu": {
        "desc_tr": "Adını suyunun cam berraklığından alan Akvaryum Koyu, sadece tekne turlarıyla ulaşılabilen bakir bir doğa harikasıdır. Şnorkelle dalış yaparken balıkları çıplak gözle görebileceğiniz bu koy, turkuazın en saf tonlarını sunar.",
        "desc_en": "Named for its crystal-clear waters, Aquarium Bay is a pristine natural wonder accessible only by boat. It's an unparalleled location for snorkeling where you can see fish swimming alongside you in vibrant turquoise depths."
    },
    "Yalıkavak Marina": {
        "desc_tr": "Uluslararası tasarım ödülleriyle tescillenmiş dünyanın en lüks marinalarından biri olan Yalıkavak, mega yatların ve haute couture markaların buluşma noktasıdır. Dünya çapındaki restoranları ve jet-set atmosferiyle Bodrum'un prestij sembolüdür.",
        "desc_en": "An award-winning destination for global travelers and mega-yachts, Yalıkavak Marina hosts elite boutiques and world-class dining. With its luxurious atmosphere and stunning architecture, it stands as a symbol of prestige in Bodrum."
    },
    "Milta Bodrum Marina": {
        "desc_tr": "Bodrum merkezinin kalbinde yer alan Milta Marina, modern donanımı ve kentsel dokusuyla yatçıların favorisidir. Marina içindeki nezih butikler ve limana bakan şık restoranlar, kentin en keyifli yürüyüş ve sosyal yaşam duraklarından birini oluşturur.",
        "desc_en": "Located in the heart of the city, Milta Marina combines top-tier facilities with urban charm. Its upscale boutiques and harbor-view restaurants offer a refined social experience for both yachtsmen and visitors in central Bodrum."
    },
    "MACAKIZI BODRUM": {
        "desc_tr": "Bodrum'un 'boho-lüks' tarzını dünyaya tanıtan Maçakızı, zeytin ağaçlarıyla çevrili ikonik iskelesi ve gurme mutfağıyla bir yaşam tarzıdır. Rafine eğlence anlayışı ve kusursuz tasarımıyla yarımadanın en prestijli noktasıdır.",
        "desc_en": "An iconic standard-bearer of 'boho-luxury,' Maçakızı is a legendary lifestyle destination known for its famous seaside deck and gourmet cuisine. It represents the height of sophistication and refined Mediterranean entertainment."
    },
    "Nikki Beach Resort & Spa Bodrum": {
        "desc_tr": "Torba Koyu'nun manzarasına hakim Nikki Beach, dünya çapında ünlü plaj kulübü konseptini Bodrum'a taşır. Canlı DJ performansları, yaratıcı kokteylleri ve şık havuz başı partileriyle Yarımada'da eğlencenin en enerjik adresidir.",
        "desc_en": "Overlooking the stunning Torba Bay, Nikki Beach brings its world-renowned club concept to Bodrum. With live DJ sets, creative cocktails, and chic poolside events, it is the most energetic address for daytime entertainment."
    },
    "Lucca beach": {
        "desc_tr": "Cennet Koyu'nun masmavi sularında yer alan Lucca Beach, İstanbul'un ikonik markasının sahil konseptidir. Rafine bir mutfak, tasarım odaklı bir dekorasyon ve kaliteli müzikle lüks bir deniz günü vaat eder.",
        "desc_en": "Nestled in the pristine waters of Paradise Bay, Lucca Beach is the coastal outpost of Istanbul's iconic brand. It offers a luxurious day at sea with a refined menu, designer aesthetics, and sophisticated music."
    }
}

# KAŞ UPDATES
kas_updates = {
    "Linckia Roastery Cafe": {
        "desc_tr": "Kaş'ın en sevilen yeni nesil kahvecilerinden biri olan Linckia, özenle seçilmiş çekirdekleri ve taze kavrulmuş kahveleriyle bilinir. Modern tasarımı ve huzurlu atmosferiyle, kentin hareketliliğinden kaçıp kaliteli bir mola vermek isteyenlerin favorisidir.",
        "desc_en": "A favorite for third-wave coffee lovers in Kaş, Linckia is known for its specialty beans and freshly roasted aromas. With its modern design and tranquil vibe, it’s the perfect spot for a quality caffeine break in the heart of town."
    },
    "SPOKO COFFEE & CAKE & SANDWICH": {
        "desc_tr": "Ev yapımı pastaları ve taze sandviçleriyle tanınan SPOKO, Kaş çarşısında samimi bir mola noktasıdır. Özellikle kahvelerinin yanına eşlik eden özgün tatlılarıyla, kentin en tatlı saklı bahçelerinden biri olarak bilinir.",
        "desc_en": "Known for its homemade cakes and fresh sandwiches, SPOKO is a cozy retreat in the Kaş market. Its unique selection of desserts and quality coffee make it one of the town's most charming hidden gems for a quick bite."
    },
    "Heybe Cafe": {
        "desc_tr": "Geleneksel Türk kahvaltısını ve ev yemeklerini Kaş'ın yerel dokusuyla sunan Heybe, samimiyetiyle öne çıkar. Çiçeklerle bezeli masaları ve güleryüzlü hizmetiyle, kendinizi kentin otantik yaşamına dahil hissedeceğiniz bir duraktır.",
        "desc_en": "Serving traditional Turkish breakfast and home-cooked meals, Heybe captures the authentic spirit of Kaş. With its flower-lined tables and warm hospitality, it’s a perfect place to feel like a local in the heart of the village."
    },
    "Leymona Beach & Restaurant & Bar": {
        "desc_tr": "Kaş'ın en güzel deniz erişimine sahip noktalarından biri olan Leymona, hem beach club hem de restoran konseptini başarıyla birleştirir. Meis Adası'na bakan manzarası ve gurme mutfağıyla, kentin en nezih deniz duraklarından biridir.",
        "desc_en": "Boasting one of the best coastal spots in Kaş, Leymona combines a relaxed beach day with high-end dining. Overlooking Meis Island, its gourmet menu and refined atmosphere offer a top-tier Mediterranean experience."
    },
    "Kaş su altı müzesi": {
        "desc_tr": "Dalış tutkunları için benzersiz bir deneyim sunan bu su altı müzesi, çeşitli heykeller ve yapay batıklarla deniz dibini bir sanat galerisine dönüştürür. Kaş'ın berrak sularında süzülürken tarih ve sanatı suyun altında keşfedeceksiniz.",
        "desc_en": "Offering a surreal experience for divers, this underwater museum features sculptures and artificial reefs that turn the seabed into a gallery. Explore art and marine life combined in the crystal-clear depths of Kaş."
    },
    "Phellos Antik Kenti": {
        "desc_tr": "Kaş sırtlarındaki tepelerde yer alan Phellos, muazzam bir manzara eşliğinde Likya lahitleri ve sur kalıntılarını sunar. Kente tepeden bakan konumu ve sessiz doğasıyla, tarihin doğayla iç içe geçtiği etkileyici bir keşif rotasıdır.",
        "desc_en": "Located high on the ridges overlooking Kaş, Phellos features impressive Lycian sarcophagi and ancient walls. Its commanding views and silent, wild nature make it a powerful destination for those seeking history off the beaten path."
    }
}

# ÇEŞME UPDATES
cesme_updates = {
    "Hacımemiş Mahallesi": {
        "desc_tr": "Alaçatı'nın kalbinde yer alan ama daha otantik bir dokuya sahip olan Hacımemiş, sanat galerileri, antikacılar ve gurme restoranlarıyla ünlüdür. Kasabanın modern yüzünü temsil eden bu mahalle, her köşe başında bir sürpriz vaat eder.",
        "desc_en": "The authentic heart of Alaçatı, Hacımemiş is famous for its art galleries, antique shops, and boutique eateries. Representing the modern and sophisticated face of the town, it promises a creative surprise around every corner."
    },
    "Before Sunset Beach": {
        "desc_tr": "Azmak Koyu'nda yer alan Before Sunset, rafine eğlence anlayışı ve muazzam gün batımı partileriyle Çeşme'nin en lüks plaj kulüplerinden biridir. Şık tasarımı ve gurme menüsüyle, günün her saatinde seçkin bir deneyim sunar.",
        "desc_en": "Located in Azmak Bay, Before Sunset is one of Çeşme's premier beach clubs, famous for its refined vibe and legendary sunset parties. Its chic design and gourmet kitchen ensure an elite experience from day to night."
    },
    "The Beach of Momo": {
        "desc_tr": "Dalyan'da yer alan Momo, İtalyan Riviera'sını andıran atmosferi ve enerjik happy hour'larıyla Çeşme gece hayatının gündüz versiyonudur. 'Boho-chic' tarzı ve özel kokteylleriyle kentin en popüler buluşma noktasıdır.",
        "desc_en": "Bringing an Italian Riviera vibe to Dalyan, Momo is the daytime center of Çeşme's social scene. With its 'boho-chic' style and signature cocktails, it is the most sought-after spot for a vibrant and stylish beach day."
    },
    "Boyalık Plajı": {
        "desc_tr": "Ilıca Plajı'na benzer ince kumu ve turkuaz deniziyle bilinen Boyalık, kentin merkezine yakın ama daha sakin bir alternatif sunar. Kristal berraklığındaki suları, huzurlu bir deniz günü ve uzun yürüyüşler için idealdir.",
        "desc_en": "Known for its fine white sand and turquoise sea, Boyalık offers a tranquil alternative near the city center. Its crystal-clear waters are perfect for a peaceful day of swimming and long walks along the shore."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Batch 1 Enrichment - PART 2: Bodrum, Kaş, Çeşme...")
enrich_venues("bodrum", bodrum_updates)
enrich_venues("kas", kas_updates)
enrich_venues("cesme", cesme_updates)
print("✨ Batch 1 - Part 2 Enrichment Complete.")
