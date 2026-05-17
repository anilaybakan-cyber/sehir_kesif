from enrich_venues import enrich_venues

# BATCH 2: AMALFI, MYKONOS, DUBROVNIK - PART 2

# AMALFI UPDATES
amalfi_updates = {
    "Spiaggia di Positano Marina Grande": {
        "desc_tr": "Dünyanın en çok fotoğraflanan plajlarından biri olan Spiaggia Grande, Positano'nun dikey mimarisinin dibinde, turuncu ve mavi şemsiyeleriyle ikonik bir görüntü sunar. Jet-set hayatının kalbinde, her an ünlü bir simaya rastlayabileceğiniz şık bir sahil şerididir.",
        "desc_en": "One of the world's most photographed beaches, Spiaggia Grande is the vibrant heart of Positano. Flanked by colorful cliffside houses and iconic orange-and-blue umbrellas, it’s a chic coastal stretch where the jet-set spirit is always alive."
    },
    "Pasticceria Pansa Amalfi": {
        "desc_tr": "1830'dan beri Amalfi Katedrali'nin gölgesinde hizmet veren Pansa, kentin en köklü lezzet dururudur. Limon kabuğu şekerlemeleri, 'dita di apostoli' tatlısı ve taze demlenmiş kahvesiyle, tarihin tadını alabileceğiniz zarif bir mekandır.",
        "desc_en": "Serving locals and travelers since 1830 in the shadow of the Duomo, Pansa is an Amalfi institution. Famous for its candied lemon peels and delicate pastries, it offers a refined taste of the coast’s storied culinary heritage."
    },
    "Museo della Carta": {
        "desc_tr": "Kağıt üretiminin Avrupa'daki ilk merkezlerinden biri olan Amalfi'de, 13. yüzyıldan kalma bir taş değirmende yer alan bu müze büyüleyicidir. El yapımı kâğıdın asırlık üretim serüvenini canlı makineler eşliğinde keşfedebilirsiniz.",
        "desc_en": "Housed in a 13th-century stone mill, this museum tells the story of Amalfi’s legacy as one of Europe’s first papermaking centers. Visitors can witness the centuries-old traditional process and see ancient machinery still in action."
    },
    "Valle delle Ferriere": {
        "desc_tr": "Amalfi'nin dik yamaçlarının arkasına saklanmış bu doğa koruma alanı, şelaleleri ve nemli mikro klimasıyla tropikal bir ormanı andırır. Eski demir dövme atölyelerinin kalıntıları arasından geçen parkur, kıyının kalabalığından tam bir kaçış sunar.",
        "desc_en": "A lush nature reserve hidden behind Amalfi’s steep ridges, this valley feels like a tropical oasis with its waterfalls and rare ferns. The hiking trail through ancient ironwork ruins offers a serene escape into the coast’s wild interior."
    }
}

# MYKONOS UPDATES
mykonos_updates = {
    "Kiki's Tavern": {
        "desc_tr": "Agios Sostis Koyu'nda elektriksiz hizmet veren bu efsanevi taverna, basitliğin lükse dönüştüğü yerdir. Kömür ateşinde pişen taze ahtapotu ve devasa salatalarıyla, Mykonos'un en otantik ve lezzetli gastronomi deneyimini vaat eder.",
        "desc_en": "Operating without electricity on the shores of Agios Sostis, this legendary taverna redefined island simplicity. Known for its charcoal-grilled octopus and shaded outdoor tables, it offers the most authentic and soulful dining experience in Mykonos."
    },
    "Alemagou": {
        "desc_tr": "Ftelia Plajı'nda 'organik-minimalizm' tarzıyla tasarlanan Alemagou, bohem ruhu Mikonos şıklığıyla birleştirir. Ege'nin sert rüzgarlarına karşı huzurlu bir sığınak sunan mekân, özellikle rafine müzikleri ve yaratıcı mutfağıyla bilinir.",
        "desc_en": "A masterclass in organic minimalism on Ftelia Beach, Alemagou blends bohemian spirit with Mykonian elegance. Providing a sophisticated sanctuary from the island’s northern winds, it is celebrated for its eclectic music and creative Aegean cuisine."
    },
    "Spilia Restaurant": {
        "desc_tr": "Agia Anna Koyu'nda bir deniz mağarasının içine kurulu olan Spilia, Mykonos'un en dramatik yemek noktasıdır. Denizden yeni çıkarılmış deniz ürünlerini, dalgaların kayalara çarptığı bir atmosferde yemek, unutulmaz bir deneyimdir.",
        "desc_en": "Nestled inside a natural sea cave on Agia Anna beach, Spilia is Mykonos' most dramatic dining destination. Enjoying freshly caught seafood while the waves crash against the rocks just inches away is a quintessential island memory."
    },
    "Principote Mykonos": {
        "desc_tr": "Panormos Koyu'nun kristal sularında yer alan Principote, haute couture eğlence anlayışının zirvesidir. El yapımı dekorasyonu, kusursuz servisi ve adanın en şık beach club atmosferiyle lüksü yeniden tanımlar.",
        "desc_en": "Overlooking the crystalline waters of Panormos Bay, Principote represents the pinnacle of high-end beach entertainment. With its artisanal design and impeccable service, it defines the luxury beach club experience in Mykonos."
    }
}

# DUBROVNIK UPDATES
dubrovnik_updates = {
    "Culture Club Revelin": {
        "desc_tr": "16. yüzyıldan kalma bir kalenin devasa taş duvarları arasında yer alan Revelin, dünyanın en eşsiz gece kulüplerinden biridir. Orta Çağ atmosferini modern ışık şovları ve dünya çapındaki DJ performanslarıyla birleştirir.",
        "desc_en": "Set within the thick stone walls of a 16th-century fortress, Revelin is one of the world's most unique nightclubs. It blends a majestic medieval atmosphere with cutting-edge light shows and performances by global DJs."
    },
    "Nautika": {
        "desc_tr": "Lovrjenac ve Bokar kalelerinin tam ortasında, Adriyatik'in kıyısında yer alan Nautika, Dubrovnik'in en prestijli restoranıdır. Geleneksel Hırvat mutfağını modern tekniklerle sunan mekan, dünyanın en romantik teraslarından birine sahiptir.",
        "desc_en": "Positioned at the edge of the sea between the Bokar and Lovrjenac fortresses, Nautika is Dubrovnik's most prestigious dining venue. Offering refined Croatian seafaring traditions, it boasts one of the world's most romantic terraces."
    },
    "Stradun": {
        "desc_tr": "Eski Şehrin ana damarı olan bu kireçtaşı cadde, yüzyıllardır parlatılmış mermer görünümüyle büyüleyicidir. Mağazalar, kafeler ve tarihi anıtlarla çevrili Stradun, günün her saati şehrin nabzını tutan görkemli bir yürüyüş yoludur.",
        "desc_en": "The limestone-paved main artery of the Old Town, Stradun has been polished to a marble-like sheen by centuries of footsteps. Lined with historic landmarks and cafes, it is the grand stage where Dubrovnik’s daily life unfolds."
    },
    "Banje Beach": {
        "desc_tr": "Eski Şehir surlarının hemen yanında yer alan Banje, Dubrovnik'in en popüler plaj kulübüdür. Gündüz berrak sularda serinleyip surları izleyebileceğiniz mekan, akşamları ise Adriyatik kıyısının en canlı eğlence noktasına dönüşür.",
        "desc_en": "Located just outside the city walls, Banje is Dubrovnik’s premier beach club. Offering a front-row view of the Old Town while you swim in crystal waters, it transforms into a vibrant nightlife hub as the sun sets over the Adriatic."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Batch 2 Enrichment - PART 2: Amalfi, Mykonos, Dubrovnik...")
enrich_venues("amalfi", amalfi_updates)
enrich_venues("mykonos", mykonos_updates)
enrich_venues("dubrovnik", dubrovnik_updates)
print("✨ Batch 2 Enrichment - Part 2 Complete.")
