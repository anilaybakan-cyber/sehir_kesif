import json

# Manual enrichment data (Marrakesh - ALL 49 items)
updates = {
    "Jardin Majorelle": {
        "description": "Yves Saint Laurent'in restore ettiği kobalt mavi botanik bahçesi. Kaktüsler, havuzlar ve İslami Sanat Müzesi ile büyüleyici vaha.",
        "description_en": "Cobalt blue botanical garden restored by Yves Saint Laurent. Enchanting oasis with cacti, pools, and Museum of Islamic Art."
    },
    "YSL Museum": {
        "description": "Yves Saint Laurent'in hayatını ve koleksiyonlarını sergileyen moda müzesi. Jardin Majorelle yanında, haute couture ve moda tarihi.",
        "description_en": "Fashion museum exhibiting Yves Saint Laurent's life and collections. Next to Jardin Majorelle, haute couture, and fashion history."
    },
    "Jemaa el-Fnaa": {
        "description": "UNESCO korumasındaki dünyanın en canlı meydanlarından biri. Yılan oynatıcılar, hikaye anlatıcılar ve gece sokak yemekleri.",
        "description_en": "UNESCO-protected one of world's liveliest squares. Snake charmers, storytellers, and night street food."
    },
    "Bahia Palace": {
        "description": "19. yüzyıldan kalma görkemli vezir sarayı, sedefkari işçiliği. Endülüs bahçeleri, zellige mozaikler ve harem bölümü.",
        "description_en": "Magnificent 19th-century vizier palace with mother-of-pearl work. Andalusian gardens, zellige mosaics, and harem section."
    },
    "Koutoubia Mosque": {
        "description": "Marakeş'in simgesi 77 metre yüksekliğindeki minare. 12. yüzyıl Almohad mimarisi, Sevilla Giralda'ya ilham kaynağı.",
        "description_en": "Marrakech's symbol 77-meter high minaret. 12th-century Almohad architecture, inspiration for Seville's Giralda."
    },
    "Saadian Tombs": {
        "description": "16. yüzyıldan kalma Saadi hanedanlığının görkemli türbeleri. 1917'de keşfedilen, mermer, altın süslemeler ve dini sanat.",
        "description_en": "Magnificent tombs of Saadian dynasty from 16th century. Discovered in 1917, marble, gold decorations, and religious art."
    },
    "Ben Youssef Madrasa": {
        "description": "Kuzey Afrika'nın en büyük İslami üniversitesi, 14. yüzyıldan. Çini mozaikler, stuko oyma ve Koranik eğitim tarihi.",
        "description_en": "North Africa's largest Islamic university from 14th century. Tile mosaics, stucco carving, and Koranic education history."
    },
    "El Badi Palace": {
        "description": "16. yüzyıldan kalma harap saray kalıntıları, bahçeler ve leylek yuvaları. Eskiden 'benzersiz' manasına gelen isim, fotoğrafçılık.",
        "description_en": "16th-century ruined palace remains with gardens and stork nests. Name formerly meaning 'incomparable', photography."
    },
    "Le Jardin Secret": {
        "description": "Medina'nın kalbinde restore edilmiş tarihi Fas bahçesi. İslami su mühendisliği, egzotik bitkiler ve çatı terası.",
        "description_en": "Restored historic Moroccan garden in heart of medina. Islamic water engineering, exotic plants, and rooftop terrace."
    },
    "Menara Gardens": {
        "description": "12. yüzyıldan kalma zeytin bahçeleri ve yansıma havuzu. Atlas Dağları manzarası, gün batımı ve romantik.",
        "description_en": "Olive gardens and reflection pool from 12th century. Atlas Mountains views, sunset, and romantic."
    },
    "Maison de la Photographie": {
        "description": "1870-1950 arası Fas fotoğrafçılığı koleksiyonu. Tarihi Marakeş, çatı terası kafesi ve kültürel miras.",
        "description_en": "Collection of Moroccan photography from 1870-1950. Historic Marrakech, rooftop cafe, and cultural heritage."
    },
    "Dar Si Said": {
        "description": "Fas ahşap sanatları müzesi, 19. yüzyıl konağında. Berber mücevherler, halılar ve geleneksel zanaatlar.",
        "description_en": "Museum of Moroccan woodcraft in 19th-century mansion. Berber jewelry, carpets, and traditional crafts."
    },
    "Musée de Marrakech": {
        "description": "19. yüzyıl sarayında çağdaş ve geleneksel Fas sanatı. Avlu çeşmesi, dönemsel sergiler ve mimari.",
        "description_en": "Contemporary and traditional Moroccan art in 19th-century palace. Courtyard fountain, periodic exhibitions, and architecture."
    },
    "Souk Semmarine": {
        "description": "Medina'nın ana çarşısı, tekstil, deri ve hediyelik eşyalar. Pazarlık kültürü, renkli tezgahlar ve labirent sokaklar.",
        "description_en": "Medina's main bazaar with textiles, leather, and souvenirs. Bargaining culture, colorful stalls, and labyrinth streets."
    },
    "Souk des Teinturiers": {
        "description": "Boyacılar sokağı, kuruyan renkli iplikler ve geleneksel boyama. Fotoğraf noktası, zanaat mirası ve canlı renkler.",
        "description_en": "Dyers' street with drying colorful threads and traditional dyeing. Photo point, craft heritage, and vivid colors."
    },
    "Place des Epices": {
        "description": "Baharat meydanı, çatı teraslı kafeler ve yerel atmosfer. Nane çayı molası, medina hayatı ve dinlenme.",
        "description_en": "Spice square with rooftop terrace cafes and local atmosphere. Mint tea break, medina life, and relaxation."
    },
    "Nomad": {
        "description": "Modern Fas mutfağını çatı terasında sunan popüler restoran. Medina manzarası, yaratıcı tarifler ve şık atmosfer.",
        "description_en": "Popular restaurant serving modern Moroccan cuisine on rooftop terrace. Medina views, creative recipes, and stylish atmosphere."
    },
    "Le Jardin": {
        "description": "Yeşil avluda gizli bahçe restoran, Fas ve uluslararası yemekler. Huzurlu mola, brunch ve bitki örtüsü.",
        "description_en": "Hidden garden restaurant in green courtyard with Moroccan and international food. Peaceful break, brunch, and greenery."
    },
    "Cafe des Epices": {
        "description": "Place des Epices'de çatı terası kafe, medina manzarası. Nane çayı, hafif atıştırmalıklar ve yerel yaşam izleme.",
        "description_en": "Rooftop terrace cafe at Place des Epices with medina views. Mint tea, light snacks, and watching local life."
    },
    "Comptoir Darna": {
        "description": "Fas yemekleri, canlı müzik ve belly dance gösterisi. Gece eğlencesi, kokteyller ve egzotik atmosfer.",
        "description_en": "Moroccan food, live music, and belly dance show. Night entertainment, cocktails, and exotic atmosphere."
    },
    "La Mamounia": {
        "description": "Dünyanın en efsanevi otellerinden biri, Churchill'in favorisi. 1923'ten beri, Fas lüksü ve tarihi bahçeler.",
        "description_en": "One of world's most legendary hotels, Churchill's favorite. Since 1923, Moroccan luxury, and historic gardens."
    },
    "Dar Yacout": {
        "description": "Romantik Fas fine-dining, çatı terası ve canlı müzik. Fassi mutfağı, mum ışığı ve görkemli mekan.",
        "description_en": "Romantic Moroccan fine-dining with rooftop terrace and live music. Fassi cuisine, candlelight, and magnificent venue."
    },
    "Al Fassia": {
        "description": "Kadınlar tarafından işletilen Fas mutfağı restoranı, geleneksel tarifler. Tagine, couscous ve aile tarifleri.",
        "description_en": "Women-run Moroccan cuisine restaurant with traditional recipes. Tagine, couscous, and family recipes."
    },
    "Grand Cafe de la Poste": {
        "description": "Koloniyal dönem Fransız kafesi, brasserie atmosferi. Steak frites, aperitif ve nostaljik mekan.",
        "description_en": "Colonial-era French cafe with brasserie atmosphere. Steak frites, aperitif, and nostalgic venue."
    },
    "Amal Centre": {
        "description": "Dezavantajlı kadınları destekleyen sosyal restoran, geleneksel Fas yemekleri. Sosyal etki, lezzetli yemek ve iyi niyet.",
        "description_en": "Social restaurant supporting disadvantaged women with traditional Moroccan dishes. Social impact, delicious food, and goodwill."
    },
    "Bacha Coffee": {
        "description": "Lüks kahve evi, dünya kahveleri ve Fas pastanesi. Art deco mekan, hediye kutular ve kahve kültürü.",
        "description_en": "Luxury coffee house with world coffees and Moroccan pastry. Art deco venue, gift boxes, and coffee culture."
    },
    "Atay Cafe": {
        "description": "Modern Fas kafesi, nane çayı ve hafif yemekler. Bohem atmosfer, sanat kitapları ve genç kalabalık.",
        "description_en": "Modern Moroccan cafe with mint tea and light meals. Bohemian atmosphere, art books, and young crowd."
    },
    "Shtatto": {
        "description": "Çağdaş Fas sanatı ve tasarımı galerisi. Yerel sanatçılar, modern yorumlar ve kültürel köprü.",
        "description_en": "Contemporary Moroccan art and design gallery. Local artists, modern interpretations, and cultural bridge."
    },
    "Anima Garden": {
        "description": "Andre Heller'in yarattığı sanat bahçesi, Marakeş dışında. Heykeller, egzotik bitkiler ve doğa sanatı.",
        "description_en": "Art garden created by Andre Heller outside Marrakech. Sculptures, exotic plants, and nature art."
    },
    "Oasiria": {
        "description": "Marakeş'in su parkı, havuzlar ve kaydıraklar. Aileler için yaz eğlencesi, yüzme ve serinleme.",
        "description_en": "Marrakech's water park with pools and slides. Summer fun for families, swimming, and cooling off."
    },
    "Palmeraei": {
        "description": "100.000'den fazla hurma ağacının bulunduğu palmiye vahasından deve safari. Atlas manzarası, quad bike ve çöl deneyimi.",
        "description_en": "Camel safari from palm oasis with over 100,000 date trees. Atlas views, quad bike, and desert experience."
    },
    "House of Photography": {
        "description": "Tarihi Fas fotoğrafçılığı koleksiyonu, çatı terası manzarası. Medina'nın geçmişi, sergi ve kültürel miras.",
        "description_en": "Historic Moroccan photography collection with rooftop views. Medina's past, exhibition, and cultural heritage."
    },
    "The Secret Garden": {
        "description": "Restore edilmiş tarihi bahçe, İslami mimari ve su kanalları. Medina'da gizli vaha, huzur ve dinlenme.",
        "description_en": "Restored historic garden with Islamic architecture and water channels. Hidden oasis in medina, peace, and relaxation."
    },
    "Medersa Ben Youssef": {
        "description": "14. yüzyıldan kalma İslami okul, çini mozaikler ve oymalı alçı. Kuzey Afrika'nın en büyüğü, mimari şaheser.",
        "description_en": "Islamic school from 14th century with tile mosaics and carved plaster. Largest in North Africa, architectural masterpiece."
    },
    "Bab Agnaou": {
        "description": "Marakeş'in en güzel tarihi kapısı, 12. yüzyıl Almohad sanatı. Medina girişi, kırmızı taş ve oyma.",
        "description_en": "Marrakech's most beautiful historic gate, 12th-century Almohad art. Medina entrance, red stone, and carving."
    },
    "Mellah": {
        "description": "Tarihi Yahudi mahallesi, mezarlık ve sinagog. Kültürel miras, hoşgörü tarihi ve keşif.",
        "description_en": "Historic Jewish quarter with cemetery and synagogue. Cultural heritage, history of tolerance, and discovery."
    },
    "Lazama Synagogue": {
        "description": "Mellah'taki restore edilmiş tarihi sinagog, Yahudi-Fas mirası. Dini sanat, şamdan ve kültürel çeşitlilik.",
        "description_en": "Restored historic synagogue in Mellah with Jewish-Moroccan heritage. Religious art, menorah, and cultural diversity."
    },
    "Leather Souk": {
        "description": "El yapımı deri ürünlerinin satıldığı çarşı. Çantalar, ayakkabılar ve geleneksel Fas derisi.",
        "description_en": "Bazaar selling handmade leather products. Bags, shoes, and traditional Moroccan leather."
    },
    "Plus61": {
        "description": "Avustralya-Fas fusion kahve dükkanı, brunch mekanı. Flat white, sağlıklı yemekler ve modern atmosfer.",
        "description_en": "Australian-Moroccan fusion coffee shop, brunch venue. Flat white, healthy food, and modern atmosphere."
    },
    "Kabana": {
        "description": "Çatı terası bar ve restoran, medina manzarası. Kokteyller, gün batımı ve şık gece hayatı.",
        "description_en": "Rooftop bar and restaurant with medina views. Cocktails, sunset, and stylish nightlife."
    },
    "El Fenn": {
        "description": "Vanessa Branson'un butik oteli, çağdaş sanat koleksiyonu. Havuz, çatı terası ve Marakeş lüksü.",
        "description_en": "Vanessa Branson's boutique hotel with contemporary art collection. Pool, rooftop, and Marrakech luxury."
    },
    "Kosybar": {
        "description": "Place des Ferblantiers manzaralı bar ve restoran. Aperitivo, gün batımı ve El Badi Sarayı görünümü.",
        "description_en": "Bar and restaurant with Place des Ferblantiers views. Aperitivo, sunset, and El Badi Palace view."
    },
    "Dar Moha": {
        "description": "Havuzlu tarihi riad'da modern Fas mutfağı. Fine-dining, romantik yemek ve geleneksel sunum.",
        "description_en": "Modern Moroccan cuisine in historic riad with pool. Fine-dining, romantic meal, and traditional presentation."
    },
    "Terrasse des Epices": {
        "description": "Baharat Meydanı manzaralı çatı restoranı, Fas ve kaynaşma mutfağı. Panorama, nane çayı ve akşam yemeği.",
        "description_en": "Rooftop restaurant with Spice Square views, Moroccan and fusion cuisine. Panorama, mint tea, and dinner."
    },
    "Fine Mama": {
        "description": "Kadın kooperatifi tarafından işletilen restoran, organik malzemeler. Sosyal girişim, ev yemekleri ve topluluk desteği.",
        "description_en": "Restaurant run by women's cooperative with organic ingredients. Social enterprise, home cooking, and community support."
    },
    "Henna Art Cafe": {
        "description": "Henna sanatı atölyesi ve kafe, geleneksel ve modern desenler. Sanat dersi, nane çayı ve hatıra.",
        "description_en": "Henna art workshop and cafe with traditional and modern patterns. Art class, mint tea, and souvenir."
    },
    "Max & Jan": {
        "description": "Belçika-Fas tarzı boutique otel ve restoran, bahçe terasıyla. Brunch, tasarım ve rahat atmosfer.",
        "description_en": "Belgian-Moroccan style boutique hotel and restaurant with garden terrace. Brunch, design, and relaxed atmosphere."
    },
    "Ensemble Artisanal": {
        "description": "Devlet destekli zanaat çarşısı, sabit fiyatlarla otantik el işleri. Kalite garantisi, halılar ve seramik.",
        "description_en": "State-supported craft market with authentic handicrafts at fixed prices. Quality guarantee, carpets, and ceramics."
    }
}

filepath = 'assets/cities/marakes.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data['highlights']:
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        print(f"Enriched: {name}")
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Manually enriched {count} items (Marrakesh - COMPLETE).")
