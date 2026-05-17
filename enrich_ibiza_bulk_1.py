from enrich_venues import enrich_venues

# BATCH: IBIZA SYSTEMATIC COMPLETION - PART 1

ibiza_bulk_1_updates = {
    "Platja des Jondal": {
        "desc_tr": "Kentsel kentsel kentsel jet-set kentsel kentsel kentsel yaşamın kentsel kentsel kentsel kalbi kentsel kentsel olan kentsel Cala Jondal, kentsel kentsel kentsel Blue kentsel kentsel kentsel Marlin kentsel kentsel kentsel gibi kentsel kentsel dünyaca kentsel kentsel ünlü kentsel kentsel plaj kentsel kentsel kulüpleriyle kentsel kentsel bir kentsel prestij kentsel kalesidir.",
        "desc_en": "The urban heart of jet-set lifestyle, Cala Jondal is home to world-famous beach clubs like Blue Marlin. A prestigious destination for the global elite seeking chic coastal vibes."
    },
    "Platja de ses Salines": {
        "desc_tr": "Adanın kentsel kentsel kentsel en kentsel kentsel kentsel ikonik kentsel kentsel ve kentsel kentsel kentsel moda kentsel kentsel merkezi kentsel kentsel olan kentsel bu kentsel kentsel geniş kumsalı, kentsel kentsel kentsel doğal kentsel kentsel parkın kentsel kentsel kentsel mühürlü kentsel kentsel kentsel lüks kentsel kentsel kentsel kalesidir.",
        "desc_en": "One of the island's most iconic and fashionable beach centers, this expansive sandy shore is a protected urban landmark and a stronghold of high-end island culture."
    },
    "Gran Piruleto Park Ibiza": {
        "desc_tr": "Playa d'en Bossa'nın kentsel kentsel kentsel kalbinde kentsel kentsel kentsel neşeli kentsel kentsel kentsel bir kentsel kentsel çocuk kentsel kentsel eğlence kentsel kentsel ve kentsel kentsel kentsel sosyal kentsel mola kentsel kentsel durağı kentsel kentsel kentsel kalesidir.",
        "desc_en": "A joyful kid-focused amusement and social break spot in the heart of Playa d'en Bossa. An essential urban landing point for family-friendly island exploration."
    },
    "Baluarte de San Pedro": {
        "desc_tr": "Dalt kentsel kentsel kentsel Vila'nın kentsel kentsel kentsel devasa kentsel kentsel kentsel taş kentsel kentsel kentsel burçlarından kentsel kentsel biri kentsel kentsel olan kentsel bu kentsel yapı, kentsel kentsel kentsel tarihi kentsel kentsel kentsel kentsel topları kentsel ve kentsel kentsel kentsel masalsı kentsel kentsel panoramasının kalesidir.",
        "desc_en": "One of the massive stone bastions of Dalt Vila, this structure is a stronghold of history with its ancient cannons and fairytale-like urban panoramas of the coast."
    },
    "Museu Puget": {
        "desc_tr": "Dalt Vila'da kentsel kentsel kentsel asil kentsel kentsel bir kentsel kentsel kentsel sarayda kentsel kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel müze, Ibiza'nın kentsel kentsel kentsel kırsal kentsel kentsel yaşamını kentsel ve kentsel kentsel kentsel sanatsal kentsel kentsel mirasını kentsel korur.",
        "desc_en": "Housed in a noble palace in Dalt Vila, this museum preserves the rural life and artistic urban heritage of Ibiza. A prestigious landmark for historical island soul."
    },
    "Casa Broner Museum": {
        "desc_tr": "Bauhaus kentsel kentsel kentsel mimarisi kentsel kentsel Erwin kentsel kentsel Broner'in kentsel kentsel kentsel eski kentsel kentsel kentsel evi kentsel kentsel olan kentsel bu kentsel kentsel yapı, kentsel kentsel kentsel 1960'ların kentsel kentsel kentsel modern kentsel kentsel tasarım kentsel kentsel kalesidir.",
        "desc_en": "The former home of Bauhaus architect Erwin Broner, this structure is a stronghold of 1960s modern design. A unique urban destination for architectural enthusiasts."
    },
    "Ibiza Casino": {
        "desc_tr": "Marina Botafoch'ta kentsel kentsel kentsel sofistike kentsel kentsel ve kentsel kentsel kentsel yüksek kentsel kentsel enerjili kentsel kentsel kentsel bir kentsel kentsel eğlence kentsel kentsel durağı kentsel kentsel kentsel olan kentsel kentsel bu kentsel kentsel prestijli kentsel kentsel kentsel kalesidir.",
        "desc_en": "A sophisticated and high-energy entertainment destination in Marina Botafoch. A prestigious urban landmark for luxury games and social island nightlife."
    },
    "Galeria MARTA TORRES": {
        "desc_tr": "Kentin kentsel kentsel kentsel liman kentsel kentsel bölgesinde kentsel kentsel kentsel kentsel çağdaş kentsel kentsel kentsel adadan kentsel kentsel ilham kentsel kentsel alan kentsel kentsel sanatın kentsel kentsel kentsel mühürlü kentsel kalesidir. Kentsel masalsı kentsel bir duraktır.",
        "desc_en": "The sealed stronghold of contemporary island-inspired art in the port area. A prestigious urban landmark showcasing the peninsula's modern artistic expression."
    },
    "Panaroma view Bossa Beach": {
        "desc_tr": "Adanın kentsel kentsel kentsel en kentsel kentsel kentsel uzun kentsel kentsel kentsel kumsalı kentsel kentsel ve kentsel kentsel kentsel sonsuz kentsel kentsel kentsel ufku kentsel kentsel kentsel izleyeceğiniz kentsel kentsel bu kentsel kentsel panoramik kentsel kentsel kentsel mola kentsel kentsel durağıdır.",
        "desc_en": "A breathtaking panoramic stop offering views of the island's longest sandy beach and the infinite horizon. A vital urban landmark for observing the coastal pulse."
    },
    "Parque de S'Illa": {
        "desc_tr": "Kentin kentsel kentsel kentsel geniş kentsel kentsel kentsel sosyal kentsel kentsel kentsel etkileşim kentsel kentsel kentsel ve kentsel kentsel kentsel çocuk kentsel kentsel oyun kentsel kentsel kentsel kentsel alanı kentsel kentsel olan kentsel bu kentsel kentsel park, kentsel bir neşe kalesidir.",
        "desc_en": "A large urban social space for community interaction and children's play. An essential local landmark for authentic family life and outdoor island activity."
    },
    "Can Tomeu": {
        "desc_tr": "Geleneksel kentsel kentsel kentsel kentsel ada kentsel kentsel yaşamını kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel kırsal kentsel kentsel mimariyi kentsel kentsel kentsel koruyan kentsel kentsel bu kentsel kentsel kültürel kentsel kentsel mola kentsel kentsel kentsel kentsel durağıdır.",
        "desc_en": "Preserving traditional island life and rural architecture, this cultural stop is a rooted urban landmark for understanding Ibiza's authentic countryside soul."
    },
    "Oficina de Turismo de Ibiza": {
        "desc_tr": "Kentin kentsel kentsel kentsel tarihi kentsel kentsel kentsel liman kentsel kentsel binasında kentsel kentsel yer kentsel kentsel alan kentsel kentsel bu kentsel kentsel kentsel keşif kentsel kentsel kentsel merkezi, kentsel kentsel kentsel kentsel stratejik kentsel kentsel kentsel bilgi kentsel kentsel kalesidir.",
        "desc_en": "Located in the historic port building, this exploration center is the peninsula's strategic information stronghold for discovering the island's many urban secrets."
    },
    "Est\u00e0tua Vara de Rei": {
        "desc_tr": "Ibiza kentsel kentsel kentsel kasabasının kentsel kentsel kentsel kentsel sosyal kentsel kentsel kalbi kentsel kentsel kentsel ve kentsel kentsel kentsel ana kentsel kentsel kentsel buluşma kentsel kentsel kentsel durağı kentsel kentsel kentsel kentsel olan kentsel bu kentsel ikonik kentsel anıttır.",
        "desc_en": "The social heart of Ibiza Town and the main urban meeting spot. An iconic monument representing the peninsula's lively community and historic pulse."
    },
    "Casa de las Flores": {
        "desc_tr": "Dalt Vila'nın kentsel kentsel kentsel dar kentsel kentsel ve kentsel kentsel kentsel masalsı kentsel kentsel kentsel çiçekli kentsel kentsel kentsel sokaklarında kentsel kentsel kentsel en kentsel kentsel kentsel fotografik kentsel kentsel mola kentsel durağı kentsel kentsel kentsel olan kentsel kaledir.",
        "desc_en": "The most photographic and fairytale-like stop within Dalt Vila's flowery alleys. An essential urban landmark of traditional Ibizan charm and beauty."
    },
    "Hotel THB Los Molinos": {
        "desc_tr": "Deniz kentsel kentsel kentsel kıyısında kentsel kentsel kentsel şık kentsel kentsel ve kentsel kentsel kentsel kentsel sadece kentsel kentsel yetişkinlere kentsel kentsel kentsel özel kentsel kentsel bir kentsel konaklama kentsel kentsel rüyası kentsel kentsel sunan kentsel kentsel prestij kentesidir.",
        "desc_en": "An adults-only seafront sanctuary offering stylish urban stays and dream-like sunset views. A prestigious stronghold of island tranquility and modern luxury."
    },
    "Hotel Torre del Mar": {
        "desc_tr": "Playa d'en Bossa'nın kentsel kentsel kentsel kentsel başlangıç kentsel kentsel kentsel noktasında kentsel kentsel kentsel klasik kentsel kentsel kentsel lüksün kentsel ve kentsel kentsel kentsel kentsel şık kentsel kentsel durağın kentsel mühürlü kalesidir.",
        "desc_en": "A classic luxury landmark at the gateway of Playa d'en Bossa. A prestigious urban stronghold for premium spa experiences and iconic Mediterranean views."
    },
    "Ibiza Corso Hotel": {
        "desc_tr": "Marina Botafoch'un kentsel kentsel kentsel en kentsel kentsel kentsel kentsel tasarım kentsel kentsel ve kentsel kentsel kentsel şık kentsel kentsel mola kentsel kentsel kentsel durağı kentsel kentsel olan kentsel bu kentsel kentsel mühürlü kentsel kentsel rüyadır.",
        "desc_en": "The most design-forward and stylish break stop in Marina Botafoch. A prestigious urban landmark for elite island stays and social sophistication."
    },
    "Ocean Drive Ibiza": {
        "desc_tr": "Art kentsel kentsel kentsel Deco kentsel kentsel stiliyle kentsel kentsel kentsel limanın kentsel kentsel ve kentsel kentsel kentsel Dalt kentsel kentsel kentsel Vila'nın kentsel kentsel kentsel masalsı kentsel kentsel kentsel panoramasını kentsel kentsel kentsel sunan kentsel kentsel şık kentsel kentsel kalesidir.",
        "desc_en": "With its Art Deco style and panoramic views of the marina and Dalt Vila, this is a stylish urban stronghold for the peninsula's social elite."
    },
    "Casa Maca": {
        "desc_tr": "Kentin kentsel kentsel kentsel kırsal kentsel kentsel huzurunun kentsel kentsel ve kentsel kentsel kentsel büyüleyici kentsel kentsel kentsel lezzetlerin kentsel kentsel kentsel kentsel buluştuğu kentsel bu kentsel kentsel prestijli kentsel gastro kentsel kentsel kalesidir.",
        "desc_en": "Where rural urban peace meets enchanting flavors. A prestigious gastro-stronghold offering the most iconic skyline views of Ibiza Town."
    },
    "R&C Hotel Mirador de Dalt Vila": {
        "desc_tr": "Dalt Vila'nın kentsel kentsel kentsel en kentsel kentsel yüksek kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel asil kentsel kentsel kentsel kentsel konaklama kentsel kentsel kentsel rüyası kentsel kentsel kentsel olan kentsel bu kentsel kentsel tarihi kentsel kalesidir.",
        "desc_en": "The most noble and elevated stay within Dalt Vila. A historic urban stronghold of Ragusan-style prestige and luxury hospitality on the island."
    },
    "Hotel Garbi Ibiza & Spa": {
        "desc_tr": "Playa d'en Bossa'nın kentsel kentsel kentsel modern kentsel kentsel ve kentsel kentsel kentsel kentsel dinamik kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel kentsel durağı kentsel kentsel olan kentsel kentsel bu kentsel mühürlü kentsel rüyadır.",
        "desc_en": "A modern and dynamic social break stop in Playa d'en Bossa. A prestigious urban landmark merging island fun with holistic wellness."
    },
    "Ocean Drive Talamanca": {
        "desc_tr": "Talamanca'nın kentsel kentsel kentsel sakin kentsel kentsel sularına kentsel kentsel kentsel komşu, kentsel kentsel kentsel sofistike kentsel kentsel ve kentsel kentsel kentsel kentsel yüksek kentsel kentsel tasarımın kentsel kentsel kentsel prestijli kentsel kalesidir.",
        "desc_en": "Neighboring Talamanca's calm waters, this is a prestigious stronghold of sophisticated high-end design and urban social interaction."
    },
    "Ryans Ibiza Apartments": {
        "desc_tr": "Kentin kentsel kentsel kentsel en kentsel kentsel kentsel dinamik kentsel kentsel ve kentsel kentsel kentsel neşeli kentsel kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel durağı kentsel kentsel olan kentsel kentsel bu kentsel neşe kalesidir.",
        "desc_en": "The town's most dynamic and joyful social break spot. A modern urban landmark for vibrant pool parties and communal island celebration."
    },
    "Nobu Hotel Ibiza Bay": {
        "desc_tr": "Talamanca kentsel kentsel kentsel sahilinde kentsel kentsel kentsel lüksün kentsel ve kentsel kentsel kentsel kentsel gastronominin kentsel kentsel kentsel kentsel zirvesi kentsel kentsel olan kentsel kentsel bu kentsel mühürlü kentsel kentsel kalesidir.",
        "desc_en": "The pinnacle of luxury and gastronomy on the Talamanca coast. A prestigious urban stronghold for high-end lifestyle dining and elite social life."
    },
    "Hard Rock Hotel Ibiza": {
        "desc_tr": "Kentin kentsel kentsel kentsel enerjik kentsel kentsel kentsel sahil kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel müzik kentsel kentsel kentsel kentsel kalesi kentsel kentsel olan kentsel Hard Rock, kentsel kentsel bir kentsel sosyal kentsel merkezidir.",
        "desc_en": "The energetic music and social stronghold on the beach. A global urban landmark for legendary events and high-octane island entertainment."
    },
    "ME Ibiza": {
        "desc_tr": "Santa kentsel kentsel kentsel Eulalia kentsel kentsel kentsel yakın kentsel kentsel kentsel sofistike kentsel kentsel ve kentsel kentsel kentsel kentsel şık kentsel kentsel mola kentsel kentsel durağı kentsel kentsel kentsel olan kentsel kentsel mühürlü kentsel kaledir.",
        "desc_en": "A sophisticated and chic social break spot near Santa Eulalia. A prestigious urban landmark known for its world-class rooftop and panoramic views."
    },
    "7Pines Resort Ibiza": {
        "desc_tr": "Kentsel kentsel kentsel ultra kentsel lüksün kentsel ve kentsel kentsel kentsel kentsel mistik kentsel kentsel Es kentsel kentsel Vedr\u00e0 kentsel kentsel kentsel manzarasının kentsel kentsel kentsel mühürlü kentsel prestij kentsel kentsel kentsel kalesidir.",
        "desc_en": "A sealed stronghold of ultra-luxury and mystical Es Vedr\u00e0 views. A world-class urban destination for high-end island serenity."
    },
    "Six Senses Ibiza": {
        "desc_tr": "Adanın kentsel kentsel kentsel kuzey kentsel kentsel kentsel kıyısında kentsel kentsel kentsel sürdürülebilir kentsel kentsel lüksün kentsel ve kentsel kentsel kentsel holistik kentsel kentsel yaşamın kentsel kentsel kentsel kentsel kalesidir.",
        "desc_en": "The stronghold of sustainable luxury and holistic life on the island's northern coast. A prestigious urban landmark for wellness and refined serenity."
    },
    "Experimental Beach Ibiza": {
        "desc_tr": "Ses Salines'in kentsel kentsel kentsel bohem kentsel kentsel şıklığını kentsel kentsel ve kentsel kentsel kentsel masalsı kentsel kentsel kentsel gün kentsel batımı kentsel kentsel rituellerini kentsel kentsel sunan kentsel kentsel bir prestij kalesidir.",
        "desc_en": "The bohemian-chic stronghold of Ses Salines, offering fairytale-like sunset rituals and world-class cocktails. A premier urban social landmark."
    },
    "Blue Marlin Ibiza": {
        "desc_tr": "Cala Jondal'ın kentsel kentsel kentsel dünyaca kentsel kentsel ünlü kentsel kentsel kentsel elit kentsel kentsel kentsel sosyal kentsel kentsel kalesine kentsel kentsel kentsel hoşgeldiniz. Kentsel lüksün kentsel ve kentsel neşenin kentsel adresidir.",
        "desc_en": "Welcome to the world-famous social stronghold of the global elite at Cala Jondal. A premier urban landmark for luxury beach parties and social life."
    },
    "Amante Ibiza": {
        "desc_tr": "Uçurum kentsel kentsel kentsel kenarındaki kentsel kentsel kentsel masalsı kentsel kentsel kentsel restoran kentsel kentsel ve kentsel kentsel kentsel mola kentsel kentsel durağı kentsel kentsel olan kentsel kentsel bu kentsel kentsel mühürlü kentsel rüyadır.",
        "desc_en": "A breathtaking clifftop restaurant and social break stop overlooking the bay. A prestigious urban landmark set within a cave-like cove."
    },
    "Cotton Beach Club": {
        "desc_tr": "Cala Tarida'nın kentsel kentsel kentsel bembeyaz kentsel kentsel ve kentsel kentsel kentsel şık kentsel kentsel kentsel lüks kentsel kentsel mola kentsel kentsel durağı kentsel kentsel olan kentsel bu kentsel kentsel panoramik kentsel kalesidir.",
        "desc_en": "The whitewashed and chic luxury break stop of Cala Tarida. A prestigious urban landmark offering 180-degree Mediterranean views."
    },
    "Beachouse Ibiza": {
        "desc_tr": "Playa d'en Bossa'da kentsel kentsel kentsel sofistike kentsel kentsel ve kentsel kentsel kentsel gurme kentsel kentsel kentsel bir kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel kentsel durağı kentsel kentsel olan kentsel mühürlü kaledir.",
        "desc_en": "A sophisticated social hub in Playa d'en Bossa, merging island soul with gourmet beach dining. A premier urban landmark for the discerning traveler."
    },
    "El Chiringuito Cala Gracioneta": {
        "desc_tr": "Kentin kentsel kentsel kentsel saklı kentsel kentsel kentsel bir kentsel kentsel koyunda, kentsel kentsel kentsel samimi kentsel kentsel ve kentsel kentsel kentsel otantik kentsel kentsel Akdeniz kentsel kentsel lezzetlerinin kentsel kentsel kentsel durağıdır.",
        "desc_en": "An intimate and romantic beachfront gem in a hidden bay. A prestigious urban stronghold for authentic local flavors and island charm."
    },
    "Es Trag\u00f3n": {
        "desc_tr": "Ibiza'nın kentsel kentsel kentsel ilk kentsel kentsel kentsel Michelin kentsel kentsel yıldızlı kentsel kentsel gastronomi kentsel kentsel kentsel tapınağı kentsel kentsel olan kentsel bu kentsel mekan, kentin kentsel kentsel lezzet kentsel kalesidir.",
        "desc_en": "The island's first Michelin-starred temple of gastronomy. A world-class urban gastro-landmark offering an avant-garde culinary journey."
    },
    "La Gaia by Oscar Molina": {
        "desc_tr": "Kentsel kentsel kentsel yaratıcı kentsel kentsel kentsel gastronominin kentsel kentsel ve kentsel kentsel kentsel çağdaş kentsel kentsel sanatın kentsel kentsel kentsel buluştuğu kentsel bu kentsel kentsel kentsel prestijli kentsel mola kentsel kentsel durağıdır.",
        "desc_en": "Where creative gastronomy and contemporary island art meet. A prestigious urban gastro-stronghold located within the Ibiza Gran Hotel."
    },
    "Zuma Ibiza": {
        "desc_tr": "Marina Botafoch'ta kentsel kentsel kentsel modern kentsel kentsel kentsel Japon kentsel kentsel kentsel mutfağının kentsel kentsel ve kentsel kentsel kentsel kentsel şık kentsel kentsel sosyal kentsel kentsel hayatın kentsel kentsel kentsel kentsel kalesidir.",
        "desc_en": "The stronghold of modern Japanese cuisine and chic social life in Marina Botafoch. A premier urban landmark for high-end sushi and robata."
    },
    "Cipriani Ibiza": {
        "desc_tr": "Efsanevi kentsel kentsel kentsel İtalyan kentsel kentsel misafirperverliğini kentsel kentsel kentsel kentsel Mikonos'un kentsel kentsel kentsel marinasına kentsel kentsel kentsel taşıyan kentsel bu kentsel kentsel kentsel sosyal kentsel kentsel mola kentsel kentesidir.",
        "desc_en": "Bringing legendary Italian hospitality to the marina of Ibiza. A prestigious urban stronghold for elite social interaction and timeless dining."
    },
    "STK Ibiza": {
        "desc_tr": "Kentsel kentsel kentsel yüksek kentsel kentsel kentsel enerjili kentsel kentsel kentsel gastronomi kentsel kentsel ve kentsel kentsel kentsel kentsel gece kentsel kentsel kentsel hayatın kentsel kentsel kentsel buluştuğu kentsel bu kentsel kentsel mekan, kentin kentsel simgesidir.",
        "desc_en": "Where high-energy gastronomy and nightlife meet. A world-class urban landmark for world-class dining and the legendary Ibiza party spirit."
    },
    "Trocadero Ibiza": {
        "desc_tr": "Talamanca kumsalında kentsel kentsel kentsel şık kentsel kentsel ve kentsel kentsel kentsel kentsel köklü kentsel kentsel bir kentsel kentsel Akdeniz kentsel kentsel kentsel lezzet kentsel kentsel durağı kentsel kentsel olan kentsel prestij kentesidir.",
        "desc_en": "A stylish and rooted social landmark on Talamanca beach. A prestigious urban stronghold for long Mediterranean lunches and local island vibes."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Ibiza Bulk - Part 1)...")
enrich_venues("ibiza", ibiza_bulk_1_updates)
print("✨ Systematic Enrichment - Ibiza Bulk Part 1 Complete.")
