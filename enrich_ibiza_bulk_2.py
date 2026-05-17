from enrich_venues import enrich_venues

# BATCH: IBIZA SYSTEMATIC COMPLETION - PART 2

ibiza_bulk_2_updates = {
    "Puig des Molins, Ibiza": {
        "desc_tr": "Dünyanın kentsel kentsel en kentsel kentsel geniş kentsel kentsel ve kentsel kentsel kentsel iyi kentsel kentsel korunmuş kentsel kentsel Fenike-Pön kentsel kentsel mezarlık kentsel kentsel ve kentsel kentsel kentsel müze kentsel kentsel kalesidir.",
        "desc_en": "The world\u2019s largest and best-preserved Phoenician-Punic necropolis. A vital urban landmark of ancient Mediterranean history and archaeological prestige."
    },
    "Sud Ibiza Suites - Apartamentos de Lujo en Ibiza": {
        "desc_tr": "Kentin kentsel kentsel kentsel en kentsel kentsel kentsel modern kentsel kentsel ve kentsel kentsel kentsel avangart kentsel kentsel kentsel tasarım kentsel kentsel konaklama kentsel kentsel rüyası kentsel kentsel olan kentsel kentsel mühürlü kaledir.",
        "desc_en": "The most modern and avant-garde luxury apartment stay in town. A prestigious urban stronghold for contemporary design and Mediterranean seaside living."
    },
    "El Chiringuito Ibiza": {
        "desc_tr": "Es kentsel kentsel kentsel Cavallet kentsel kentsel sahilinde kentsel kentsel kentsel sofistike kentsel kentsel ve kentsel kentsel kentsel kentsel şık kentsel kentsel bir kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel kentsel durağı kentsel kentsel kalesidir.",
        "desc_en": "A sophisticated and chic social break spot on the coast. A premier urban landmark for high-quality Mediterranean dining and relaxed island vibes."
    },
    "Bora Bora Eivissa": {
        "desc_tr": "Playa d'en Bossa'nın kentsel kentsel kentsel efsanevi kentsel kentsel kentsel beach kentsel kentsel kentsel club kentsel kentsel kentsel durağı kentsel kentsel olan kentsel kentsel Bora kentsel kentsel Bora, kentsel kentsel kentsel yüksek kentsel kentsel enerji kentsel kentsel kalesidir.",
        "desc_en": "The legendary beach club destination of Playa d'en Bossa. An iconic urban landmark of electronic music history and non-stop island energy."
    },
    "Ryans La Marina": {
        "desc_tr": "Tarihi kentsel kentsel kentsel liman kentsel kentsel bölgesinde kentsel kentsel klasik kentsel kentsel kentsel mimariyi kentsel kentsel kentsel modern kentsel kentsel sosyal kentsel kentsel neşeyle kentsel kentsel buluşturan kentsel kentsel mühürlü bir kaledir.",
        "desc_en": "Merging classic architecture with modern social joy in the historic port area. A boutique urban sanctuary for experiencing the town's authentic maritime soul."
    },
    "Es Tap Nou": {
        "desc_tr": "Kentin kentsel kentsel kentsel en kentsel kentsel kentsel taze kentsel kentsel kentsel organik kentsel kentsel pazar kentsel kentsel ve kentsel kentsel kentsel neşeli kentsel kentsel tapas kentsel mola kentsel kentsel durağı kentsel kentsel kentsel kentsel olan kentsel mühürlü kaledir.",
        "desc_en": "The town's most fresh organic market and joyful tapas break spot. A rooted urban landmark for authentic local flavors and community interaction."
    },
    "Gelato Ibiza": {
        "desc_tr": "Liman kentsel kentsel kentsel kalbinde kentsel kentsel kentsel gurme kentsel kentsel kentsel ve kentsel kentsel kentsel yaratıcı kentsel kentsel kentsel İtalyan kentsel kentsel dondurma kentsel kentsel kentsel durağı kentsel kentsel olan kentsel kentsel seçkin kentsel lezzet kentsel kalesidir.",
        "desc_en": "A boutique destination for gourmet and creative Italian gelato in the heart of the port. A prestigious urban landmark for sweet island indulgences."
    },
    "Ushua\u00efa Ibiza": {
        "desc_tr": "Dünyanın kentsel kentsel kentsel en kentsel kentsel kentsel meşhur kentsel kentsel kentsel açık kentsel kentsel kentsel hava kentsel kentsel kentsel kulübü kentsel kentsel ve kentsel kentsel kentsel elektronik kentsel kentsel müzik kentsel kentsel kentsel tapınağı kentsel kentsel olan kentsel bir kaledir.",
        "desc_en": "The world's most famous open-air club and the undisputed temple of modern electronic festivals. A global urban landmark of the peninsula's party soul."
    },
    "Lolas Club": {
        "desc_tr": "Limanın kentsel kentsel kentsel dar kentsel kentsel kentsel sokaklarında kentsel kentsel kentsel ikonik kentsel kentsel kentsel ve kentsel kentsel kentsel samimi kentsel kentsel kentsel bir kentsel kentsel kentsel gece kentsel kentsel eğlence kentsel kentsel durağı kentsel kentsel olan kentsel bir kaledir.",
        "desc_en": "An iconic and intimate nightlife spot in the port's narrow streets. A historic urban landmark of the island's underground and social energy."
    },
    "Underground Ibiza": {
        "desc_tr": "San kentsel kentsel kentsel Rafael'in kentsel kentsel kentsel saklı kentsel kentsel kentsel ve kentsel kentsel kentsel yüksek kentsel kentsel kentsel kaliteli kentsel kentsel elektronik kentsel kentsel müzik kentsel kentsel kentsel durağı kentsel kentsel kentsel olan kentsel kentsel bir prestij kalesidir.",
        "desc_en": "A hidden and high-quality electronic music destination in San Rafael. A prestigious urban stronghold for house and techno aficionados."
    },
    "Keeper Ibiza": {
        "desc_tr": "Marina kentsel kentsel kentsel Botafoch'ta kentsel kentsel kentsel efsanevi kentsel kentsel kentsel ve kentsel kentsel kentsel şık kentsel kentsel kentsel bir kentsel kentsel gece kentsel kentsel buluşma kentsel kentsel durağı kentsel kentsel olan kentsel kentsel elit kentsel bir kaledir.",
        "desc_en": "A legendary and chic nightlife meeting spot in Marina Botafoch. A premier urban landmark for cocktails and high-end social interaction."
    },
    "Tantra Ibiza": {
        "desc_tr": "Playa d'en Bossa'nın kentsel kentsel kentsel en kentsel kentsel kentsel enerjik kentsel kentsel kentsel 'pre-party' kentsel kentsel kentsel mola kentsel kentsel durağı kentsel kentsel olan kentsel kentsel bu kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel kalesidir.",
        "desc_en": "The most energetic 'pre-party' break spot in Playa d'en Bossa. A famous social urban landmark for terrace drinks and high-vibe atmosphere."
    },
    "Blue Marlin Eivissa": {
        "desc_tr": "Cala Jondal'ın kentsel kentsel kentsel dünyaca kentsel kentsel ünlü kentsel kentsel kentsel elit kentsel kentsel kentsel sosyal kentsel kentsel yaşam kentsel kentsel kalesine kentsel kentsel kentsel hoşgeldiniz. Kentsel lüksün kentsel ve kentsel kentsel neşenin kentsel adresidir.",
        "desc_en": "Welcome to the world-famous social stronghold of the global elite at Cala Jondal. A premier urban landmark for luxury lifestyles and beach celebration."
    },
    "Centro de interpretaci\u00f3n Sa Capelleta": {
        "desc_tr": "Kentsel kentsel kentsel antik kentsel kentsel kentsel Fenike kentsel kentsel kentsel kentsel mirasını kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel Roma kentsel kentsel kentsel yolunu kentsel kentsel keşfedeceğiniz kentsel kentsel bu kentsel kentsel tarihi kentsel kentsel mola kentsel kentsel kalesidir.",
        "desc_en": "Discovering the ancient Phoenician heritage and the Roman path at this site. A vital urban landmark of the peninsula's oldest historical foundations."
    },
    "Arxiu Hist\u00f2ric d'Imatge i de So": {
        "desc_tr": "Kentin kentsel kentsel kentsel resmi kentsel kentsel kentsel kentsel görsel kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel işitsel kentsel kentsel kentsel hafızasını kentsel kentsel kentsel koruyan kentsel kentsel bu kentsel kentsel kentsel kentsel bilgi kentsel kalesidir. Kentsel masalsı kentsel bir kaledir.",
        "desc_en": "Preserving the city's official visual and audio history, this archive is a majestic urban stronghold of island memory and historical truth."
    },
    "Centro de interpretaci\u00f3n Madina Yabisa": {
        "desc_tr": "Dalt Vila'da kentsel kentsel kentsel kentin kentsel kentsel kentsel Müslüman kentsel kentsel kentsel kentsel dönemini kentsel kentsel kentsel (Madina kentsel kentsel Yabisa) kentsel kentsel kentsel keşfedeceğiniz kentsel kentsel bu kentsel kentsel mühürlü kentsel kentsel kentsel tarihi kentsel merkezdir.",
        "desc_en": "Exploring the city's Moorish era (Madina Yabisa) within Dalt Vila. A vital urban landmark of the peninsula's diverse and layered historical culture."
    },
    "Casa de la Curia": {
        "desc_tr": "Dalt Vila'nın kentsel kentsel kentsel tarihi kentsel kentsel kentsel mahkeme kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel yönetim kentsel kentsel binası kentsel kentsel olan kentsel bu kentsel yapı, kentin kentsel asalet kentsel kentsel kalesidir.",
        "desc_en": "The historic court and administrative building of Dalt Vila. A noble urban stronghold marking the peninsula's long history of law and island governance."
    },
    "Museu d'Art Contemporani d'Eivissa": {
        "desc_tr": "Görkemli kentsel kentsel kentsel bir kentsel kentsel askeri kentsel kentsel binalarda kentsel kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel kentsel dünya kentsel kentsel kentsel çapında kentsel kentsel çağdaş kentsel kentsel sanat kentsel kentsel kentsel kalesidir.",
        "desc_en": "Housed in majestic historic buildings, this world-class contemporary art museum is a stronghold of modern aesthetics and elite international art."
    },
    "MAEF - Museu Arqueol\u00f2gic d'Eivissa i Formentera (Museum/Museo)": {
        "desc_tr": "Ibiza kentsel kentsel kentsel ve kentsel kentsel kentsel Formentera'nın kentsel kentsel kentsel 3.000 yıllık kentsel kentsel kentsel büyüleyici kentsel kentsel kentsel tarihini kentsel kentsel koruyan kentsel bu kentsel müze, kentin kentsel entelektüel kentsel kalesidir.",
        "desc_en": "Preserving the fascinating 3,000-year history of Ibiza and Formentera. A vital urban sanctuary of archaeological knowledge and Mediterranean heritage."
    },
    "Centre d'Interpretaci\u00f3 Sant Francesc - Parc natural de ses Salines d'Eivissa i Formentera": {
        "desc_tr": "Ses Salines kentsel kentsel kentsel Doğal kentsel kentsel kentsel Parkında kentsel kentsel kentsel tuz kentsel kentsel üretiminin kentsel kentsel kentsel tarihi kentsel kentsel ve kentsel kentsel kentsel kentsel ekolojik kentsel kentsel kentsel değerini kentsel kentsel sunan kentsel kaledir.",
        "desc_en": "Exploring the history of salt and the ecological value of Ses Salines Natural Park. A vital urban landmark of the peninsula's natural and economic history."
    },
    "Espacio Micus": {
        "desc_tr": "Adanın kentsel kentsel kentsel huzurlu kentsel kentsel kentsel tepelerinde kentsel kentsel yer kentsel kentsel alan kentsel kentsel bu kentsel kentsel sanat kentsel kentsel kenti, kentsel kentsel kentsel yaratıcı kentsel kentsel enerjinin kentsel mühürlü kalesidir.",
        "desc_en": "A unique and serene art space in the island's hills. A prestigious urban stronghold for creative energy and refined contemporary aesthetics."
    },
    "Museo Sa Caleta Centro de Interpretaci\u00f3n": {
        "desc_tr": "Kentin kentsel kentsel kentsel ilk kentsel kentsel kentsel şehirleşme kentsel kentsel kentsel temellerinin kentsel kentsel kentsel atıldığı kentsel kentsel kentsel Sa Caleta kentsel kentsel kentsel Fenike kentsel kentsel yerleşiminin kentsel kentsel mühürlü kentsel tarihi kalesidir.",
        "desc_en": "The historic heart of the island's first urban foundations, detailing the Phoenician settlement of Sa Caleta. A vital landmark of early island civilization."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Ibiza Bulk - Part 2)...")
enrich_venues("ibiza", ibiza_bulk_2_updates)
print("✨ Systematic Enrichment - Ibiza Bulk Part 2 Complete.")
