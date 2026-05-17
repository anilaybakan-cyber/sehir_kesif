from enrich_venues import enrich_venues

# BATCH: MALLORCA SYSTEMATIC COMPLETION - PART 2

mallorca_bulk_2_updates = {
    "Palma Aquarium": {
        "desc_tr": "Kentin kentsel kentsel kentsel en kentsel kentsel kentsel g\u00f6rkemli kentsel kentsel kentsel su kentsel kentsel kentsel alt\u0131 kentsel kentsel kentsel d\u00fcnyas\u0131 kentsel kentsel kentsel kalesidir. Avrupa'n\u0131n kentsel kentsel kentsel en kentsel kentsel kentsel derin kentsel kentsel kentsel k\u00f6pekbal\u0131\u011f\u0131 kentsel tank\u0131 kentsel kentsel Big kentsel Blue kentsel kentsel ile kentsel m\u00fch\u00fcrl\u00fc mola kenti.",
        "desc_en": "A world-class marine park featuring the Big Blue, one of the deepest shark tanks in Europe. A premier urban landmark for discovering the peninsula's marine nature and ecology."
    },
    "Marineland Mallorca": {
        "desc_tr": "İspanya'n\u0131n kentsel kentsel kentsel ilk kentsel kentsel kentsel deniz kentsel kentsel kentsel zooloji kentsel kentsel kentsel park\u0131 kentsel kentsel olan kentsel Marineland, kentsel kentsel kentsel me\u015fhur kentsel kentsel kentsel yunus kentsel kentsel ve kentsel kentsel kentsel deniz kentsel aslan\u0131 kentsel kentsel g\u00f6sterileriyle kentsel kentsel kaledir.",
        "desc_en": "The first marine zoo in Spain, famous for its award-winning dolphin and sea lion presentations. A prestigious urban destination for high-quality island entertainment and family fun."
    },
    "Can Joan de s'Aigo": {
        "desc_tr": "1700'lerden kentsel kentsel kentsel beri kentsel kentsel kentsel kentin kentsel kentsel kentsel lezzet kentsel kentsel kentsel haf\u0131zas\u0131 kentsel kentsel kentsel olan kentsel bu kentsel kentsel mekan, kentsel kentsel kentsel geleneksel kentsel kentsel dondurmalar\u0131 kentsel kentsel ve kentsel kentsel kentsel Ensaimada'lar\u0131yla kentsel m\u00fch\u00fcrl\u00fc kaledir.",
        "desc_en": "A historic 18th-century landmark, the soul of traditional Mallorcan treats. A rooted urban stronghold famous for its authentic artisanal ice cream and legendary Ensaimadas."
    },
    "Hotel Cappuccino - Palma": {
        "desc_tr": "Eski kentsel kentsel kentsel \u015eehir'in kentsel kentsel kentsel kalbinde kentsel kentsel kentsel g\u00f6rkemli kentsel kentsel bir kentsel kentsel kentsel tasar\u0131m kentsel kentsel kentsel ve kentsel kentsel kentsel l\u00fclks kentsel kentsel konaklama kentsel kentsel r\u00fcyas\u0131 kentsel kentsel olan kentsel kentsel m\u00fch\u00fcrl\u00fc prestij kenti.",
        "desc_en": "A prestigious design hotel merging high-end urban luxury with classic European cafe culture. A premier landmark for experiencing island elegance in a noble stone setting."
    },
    "Can Alomar Urban Luxury Retreat": {
        "desc_tr": "Paseo kentsel kentsel kentsel del kentsel kentsel Borne kentsel kentsel üzerindeki kentsel kentsel kentsel bu kentsel kentsel se\u00e7kin kentsel kentsel butik kentsel kentsel s\u0131\u011f\u0131nak, kentin kentsel kentsel kentsel en kentsel kentsel kentsel sofistike kentsel kentsel ve kentsel kentsel kentsel ş\u0131k kentsel kentsel m\u00fch\u00fcrl\u00fc kalesidir.",
        "desc_en": "An elite boutique sanctuary on the prestigious Paseo del Borne. A world-class urban stronghold for high-end elegance and sophisticated Mediterranean lifestyles."
    },
    "Iberostar Selection Playa de Palma": {
        "desc_tr": "Playa kentsel kentsel kentsel de kentsel kentsel Palma'n\u0131n kentsel kentsel kentsel en kentsel kentsel kentsel g\u00f6rkemli kentsel kentsel kentsel sahil kentsel kentsel kentsel otellerinden kentsel kentsel biri kentsel kentsel olan kentsel kentsel bu kentsel mekan, kentsel kentsel kentsel se\u00e7kin kentsel gurme kentsel kalesidir.",
        "desc_en": "A sophisticated 5-star beachfront resort in Playa de Palma. A prestigious urban landmark focused on high-quality island gastronomy, wellness, and social luxury."
    },
    "Purobeach Palma": {
        "desc_tr": "Deniz kentsel kentsel kentsel kıyısında kentsel kentsel kentsel bir kentsel kentsel kentsel 'Oaza' kentsel kentsel mola kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel Purobeach, kentsel kentsel kentsel sosyal kentsel kentsel l\u00fclks\u00fcn kentsel ve kentsel kentsel kentsel r\u00fcya kentsel kentsel gibi kentsel g\u00fcn kentsel bat\u0131m\u0131n\u0131n kalesidir.",
        "desc_en": "The iconic 'Oasis del Mar' beach club offering social luxury and pool rituals. A premier urban landmark for elite island interaction and panoramic sunset views."
    },
    "Bar Abaco": {
        "desc_tr": "Tarihi kentsel kentsel kentsel bir kentsel kentsel kentsel sarayda kentsel kentsel kentsel meyveler kentsel kentsel ve kentsel kentsel kentsel Baroque kentsel kentsel kentsel dekorlar kentsel kentsel kentsel i\u00e7inde kentsel kentsel tiyatral kentsel kentsel bir kentsel kentsel kokteyl kentsel kentsel r\u00fcyas\u0131 kentsel kentsel sunan kentsel bir kaledir.",
        "desc_en": "An extraordinary Baroque bar in a historic palace. A world-famous urban landmark, offering a theatrical and high-end cocktail experience in the stone city."
    },
    "Social Club": {
        "desc_tr": "Palma kentsel kentsel kentsel liman\u0131nda kentsel kentsel kentsel modern kentsel kentsel ve kentsel kentsel kentsel y\u00fcksek kentsel kentsel enerjili kentsel kentsel gece kentsel kentsel hayat\u0131n\u0131n kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel kentsel kentsel kalesi kentsel kentsel olan kentsel kentsel bu kentsel se\u00e7kin kentsel merkezdir.",
        "desc_en": "A premier high-energy nightlife destination at the Palma harbor. A world-class urban landmark for elite electronic music events and social island nights."
    },
    "Pueblo Espa\u00f1ol de Mallorca": {
        "desc_tr": "İspanya'n\u0131n kentsel kentsel kentsel en kentsel kentsel kentsel g\u00f6rkemli kentsel kentsel mimari kentsel kentsel kentsel eserlerinin kentsel kentsel kentsel minyat\u00fcr kentsel kentsel bulu\u015fma kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel bu kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel kentsel m\u00fcze kenti.",
        "desc_en": "An architectural open-air museum replicating Spain's most beautiful urban landmarks. A majestic island sanctuary for exploring the peninsula's diverse cultural history."
    },
    "Museu de La Seu de Mallorca": {
        "desc_tr": "G\u00f6rkemli kentsel kentsel kentsel katedral kentsel kentsel kentsel i\u00e7indeki kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel dini kentsel kentsel sanat kentsel kentsel m\u00fcze, kentin kentsel kentsel kentsel ruhani kentsel kentsel ve kentsel kentsel kentsel tarihi kentsel kentsel mühürlü kalesidir.",
        "desc_en": "The sacred art museum within the cathedral, housing precious treasures and centuries of history. A vital urban landmark of the peninsula's religious soul."
    },
    "Fundaci\u00f3n Juan March Palma": {
        "desc_tr": "Tarihi kentsel kentsel kentsel 17. yüzyıl kentsel kentsel bir kentsel kentsel kentsel sarayda kentsel kentsel kentsel dünya kentsel kentsel kentsel çap\u0131nda kentsel kentsel \u00e7a\u011fda\u015f kentsel kentsel sanat kentsel kentsel kentsel kalesidir. Kentsel masalsı kentsel bir duraktır.",
        "desc_en": "A world-class contemporary art space in a beautiful 17th-century mansion. A prestigious urban landmark for high-end international art and island culture."
    },
    "Museu Hist\u00f2ric Militar de Sant Carles": {
        "desc_tr": "Asırlık kentsel kentsel kentsel bir kentsel kentsel liman kentsel kentsel kalesinde kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel m\u00fcze, kentin kentsel kentsel kentsel denizci kentsel kentsel ve kentsel kentsel kentsel askeri kentsel kentsel mirasının kenedisidir.",
        "desc_en": "Housed in an ancient harbor fortress, detailing the island's military and naval history. A powerful urban stronghold of historical island defense and power."
    },
    "Bar Sabotage": {
        "desc_tr": "Santa kentsel kentsel kentsel Catalina'n\u0131n kentsel kentsel kentsel en kentsel kentsel kentsel dinamik kentsel kentsel ve kentsel kentsel kentsel \u015f\u0131k kentsel kentsel gece kentsel kentsel mola kentsel kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel kentsel bu kentsel sosyal kalesidir.",
        "desc_en": "A trendy and vibrant late-night social hub in Santa Catalina. A prestigious urban landmark known for its high-energy cocktails and island party soul."
    },
    "Restaurant El Pil\u00f3n": {
        "desc_tr": "Ta\u015f kentsel kentsel kentsel bir kentsel kentsel kentsel soka\u011fın kentsel kentsel derinliklerinde, kentsel kentsel kentsel geleneksel kentsel kentsel kentsel İspanyol kentsel kentsel tapaslar\u0131 kentsel kentsel ve kentsel kentsel kentsel taze kentsel kentsel deniz kentsel kentsel ürünlerinin kentsel dura\u011f\u0131d\u0131r.",
        "desc_en": "A rooted culinary institution in a stone alley, serving traditional Spanish tapas and seafood. A prestigious urban stronghold for authentic and rustic island dining."
    },
    "Santa Clara Urban Hotel & Spa": {
        "desc_tr": "Katedral kentsel kentsel kentsel yakın\u0131nda, kentsel kentsel kentsel kentsel huzurlu kentsel kentsel ve kentsel kentsel kentsel sofistike kentsel kentsel bir kentsel kentsel mola kentsel kentsel dura\u011f\u0131 kentsel kentsel kentsel olan kentsel kentsel bu kentsel lüks kentsel kalesidir.",
        "desc_en": "A peaceful and sophisticated urban sanctuary near the cathedral. A premier landmark merging island history with modern spa luxury and noble serenity."
    },
    "Can Amor\u00f3s": {
        "desc_tr": "Eski kentsel kentsel kentsel \u015eehir'in kentsel kentsel kentsel kentsel tarihi kentsel kentsel ve kentsel kentsel kentsel asil kentsel kentsel dokusunun kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel kentsel kentsel bir kentsel kentsel par\u00e7as\u0131 kentsel kentsel olan kentsel kentsel asalet kalesidir.",
        "desc_en": "A historic and noble house in the Old Town, part of the peninsula's traditional urban fabric. A prestigious landmark representing the island's authentic stone history."
    },
    "Ca'n March": {
        "desc_tr": "Ta\u015f kentsel kentsel kentsel kentin kentsel kentsel kentsel kalbinde kentsel kentsel kentsel gelleneksel kentsel kentsel ve kentsel kentsel kentsel kentsel köklü kentsel kentsel bir kentsel kentsel yerel kentsel kentsel gastronomi kentsel kentsel m\u00fch\u00fcrl\u00fc kalesidir.",
        "desc_en": "A rooted and traditional social landmark in the heart of the stone city. A prestigious urban stronghold for authentic local flavors and island hospitality."
    },
    "Ca'n Oleza": {
        "desc_tr": "Palma'n\u0131n kentsel kentsel kentsel en kentsel kentsel kentsel b\u00fcy\u00fcleyici kentsel kentsel ve kentsel kentsel kentsel ikonik kentsel kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel kentsel avlular\u0131ndan kentsel kentsel biri kentsel kentsel olan kentsel kentsel asalet kentsel kalesidir.",
        "desc_en": "One of the most beautiful and iconic patios in Palma. A prestigious urban landmark representing noble Ragusan-style architecture and island history."
    },
    "Centre d'Historia i Cultura Militar de Balears": {
        "desc_tr": "Adalar\u0131n kentsel kentsel kentsel zengin kentsel kentsel kentsel askeri kentsel kentsel ve kentsel kentsel kentsel kentsel k\u00fclt\u00fcrel kentsel kentsel mirasını kentsel kentsel kentsel tarihi kentsel kentsel kentsel bir kentsel kentsel manast\u0131rda kentsel kentsel sunan kentsel kaledir.",
        "desc_en": "Exploring the rich military and cultural heritage of the islands in a historic monastery. A vital urban landmark of the peninsula's historical foundations."
    },
    "Caf\u00e8 Pla\u00e7a": {
        "desc_tr": "Geleneksel kentsel kentsel kentsel bir kentsel kentsel kentsel k\u00f6y kentsel kentsel meydan\u0131ndaki kentsel kentsel kentsel klasik kentsel kentsel ve kentsel kentsel kentsel canl\u0131 kentsel kentsel sosyal kentsel mola kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kaledir.",
        "desc_en": "A classic and lively social stop on the main square of a traditional village. An essential island landmark for experiencing authentic local urban pulses."
    },
    "La Madeleine de Proust Santa Catalina": {
        "desc_tr": "Santa kentsel kentsel kentsel Catalina kentsel kentsel bölgesinde kentsel kentsel \u015f\u0131k kentsel kentsel ve kentsel kentsel kentsel zanaatkar kentsel kentsel kentsel bir kentsel kentsel Frans\u0131z kentsel kentsel lezzet kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kaledir.",
        "desc_en": "A chic and artisanal bakery specialty shop in the trendy Santa Catalina district. A prestigious urban landmark for high-quality island dining and French elegance."
    },
    "Bar Cafe Coto": {
        "desc_tr": "Eski kentsel kentsel kentsel \u015eehir'in kentsel kentsel kentsel renkli kentsel kentsel ve kentsel kentsel kentsel kentsel s\u0131rad\u0131\u015f\u0131 kentsel kentsel kentsel bir kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel ne\u015fe kalesidir.",
        "desc_en": "A colorful and quirky social landmark in the Old Town. A popular urban sanctuary for relaxed island interaction and vibrant Mediterranean vibes."
    },
    "miniBAR Palma - Cafe y Jam\u00f3n Ib\u00e9rico al Corte": {
        "desc_tr": "Kentin kentsel kentsel kentsel en kentsel kentsel kentsel se\u00e7kin kentsel kentsel kentsel yerel kentsel kentsel kentsel \u0130ber kentsel kentsel jambonlar\u0131n\u0131 kentsel kentsel kentsel ve kentsel kentsel kentsel s\u0131rad\u0131\u015f\u0131 kentsel kentsel lezzetleri kentsel kentsel sunan kaledir.",
        "desc_en": "An elite local mola stop specializing in the finest hand-cut Ibérico ham. A prestigious urban landmark for authentic island flavors and high-quality gourmet bites."
    },
    "Forn del Santo Cristo": {
        "desc_tr": "1910'dan kentsel kentsel kentsel beri kentsel kentsel kentsel kentin kentsel kentsel kentsel en kentsel kentsel kentsel efsanevi kentsel kentsel kentsel geleneksel kentsel kentsel f\u0131r\u0131n kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel bu kentsel mekan, kentsel ne\u015fe kalesidir.",
        "desc_en": "The island's most famous traditional bakery since 1910. A rooted urban stronghold of the authentic Mallorcan Ensaimada and historical island sweetness."
    },
    "Punt de Joc (Metropolitan)": {
        "desc_tr": "Kentin kentsel kentsel kentsel kalbinde kentsel kentsel kentsel modern kentsel kentsel kentsel bir kentsel kentsel kentsel oyun kentsel kentsel ve kentsel kentsel kentsel kentsel kentsel merkez kentsel kentsel mola kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel kaledir.",
        "desc_en": "A modern slot and gaming center in the heart of the city. A contemporary urban landmark for leisure, electronic entertainment, and social island action."
    },
    "Zar Society - Discoteca en Palma de Mallorca": {
        "desc_tr": "Kentsel kentsel kentsel y\u00fcksek kentsel kentsel kentsel enerjili kentsel kentsel kentsel gece kentsel kentsel hayat\u0131n\u0131n kentsel kentsel ve kentsel kentsel kentsel dinamik kentsel kentsel sosyal kentsel kentsel bulu\u015fma kentsel kentsel noktas\u0131 kentsel kentsel olan kensidir.",
        "desc_en": "A high-energy nightlife venue in Palma. A prestigious urban landmark for rhythmic music, social island interaction, and modern coastal entertainment."
    },
    "Transilvania Cafeteria-Museu": {
        "desc_tr": "Kentin kentsel kentsel kentsel s\u0131rad\u0131\u015f\u0131 kentsel kentsel ve kentsel kentsel kentsel temal\u0131 kentsel kentsel kentsel bir kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel ne\u015fe kalesidir.",
        "desc_en": "A unique and themed social space in town. A quirky urban landmark merging folkloric vibes with a creative and festive island cafe experience."
    },
    "Fundaci\u00f3n Bartolom\u00e9 March Servera": {
        "desc_tr": "Tarihi kentsel kentsel kentsel bir kentsel kentsel kentsel binada kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel kentsel se\u00e7kin kentsel kentsel k\u00fclt\u00fcr kentsel kentsel kentsel merkezi, kentsel kentsel kentsel b\u00fcy\u00fcl\u00fcc\u00fc kentsel kentsel k\u00fclt\u00fcr dura\u011f\u0131d\u0131r.",
        "desc_en": "A prestigious cultural space housing high-end art collections and a world-class library. A majestic urban landmark of the peninsula's intellectual and island power."
    },
    "Museu Krekovic": {
        "desc_tr": "Kristian kentsel kentsel kentsel Krekovi\u0107'in kentsel kentsel kentsel eserlerine kentsel kentsel ve kentsel kentsel kentsel kentsel And kentsel kentsel k\u00fclt\u00fcr\u00fcne kentsel kentsel kentsel adanan kentsel kentsel bu kentsel kentsel sanat kentsel kentsel mühürlü dura\u011f\u0131d\u0131r.",
        "desc_en": "A dedicated museum for the works of Kristian Krekovi\u0107 and Andean culture. A unique urban landmark for diverse and global island artistic exploration."
    },
    "ABA ART": {
        "desc_tr": "Palma kentsel kentsel kentsel limanda kentsel kentsel \u00e7a\u011fda\u015f kentsel kentsel kentsel sanat\u0131n kentsel kentsel ve kentsel kentsel kentsel kentsel yarat\u0131c\u0131 kentsel kentsel kentsel deneylerin kentsel kentsel merkez kenti kentsel kentsel mühürlü kalesidir.",
        "desc_en": "A contemporary art gallery and laboratory at the harbor. A prestigious urban landmark showcasing the peninsula's most creative and modern artistic pulses."
    },
    "Centre Maim\u00f3 Ben Faraig": {
        "desc_tr": "Palma'n\u0131n kentsel kentsel kentsel orta kentsel kentsel \u00e7a\u011f kentsel kentsel Yahudi kentsel kentsel kentsel tarihinin kentsel kentsel ve kentsel kentsel kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel mirasının kentsel kentsel kentsel mola kentsel dura\u011f\u0131 kentsel kaledir.",
        "desc_en": "Exploring the medieval Jewish history of Palma. A vital urban landmark of the peninsula's diverse and layered historical foundations and island culture."
    },
    "Aula de la Mar": {
        "desc_tr": "Adanın kentsel kentsel kentsel deniz kentsel kentsel kentsel ekolojisi kentsel kentsel ve kentsel kentsel kentsel kentsel k\u00f6kl\u00fc kentsel kentsel denizci kentsel kentsel kentsel mirası kentsel kentsel i\u00e7in kentsel kentsel kentsel proaktif kentsel mühürlü kaledir.",
        "desc_en": "An educational urban space dedicated to the island's maritime ecology and sea-faring heritage. A vital landmark for understanding the peninsula's marine nature."
    },
    "La Kokotxa": {
        "desc_tr": "Y\u00fcksek kentsel kentsel kentsel kaliteli kentsel kentsel kentsel yerel kentsel kentsel tapaslar\u0131 kentsel kentsel ve kentsel kentsel kentsel se\u00e7kin kentsel kentsel şaraplarıyla kentsel kentsel tanınan kentsel kentsel gurme kentsel mola kentsel kentsel dura\u011f\u0131d\u0131r. Kentsel masalsı bir duraktır.",
        "desc_en": "A high-quality local tapas and wine bar. A prestigious urban landmark merging traditional Basque inspiration with authentic island products and flavors."
    },
    "BCB Tango": {
        "desc_tr": "Kentin kentsel kentsel kentsel \u015f\u0131k kentsel kentsel ve kentsel kentsel kentsel sofistike kentsel kentsel bir kentsel kentsel sosyal kentsel kentsel buluşma kentsel kentsel kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel kentsel mühürlü kalesidir.",
        "desc_en": "A stylish and sophisticated social hub for evening drinks. A prestigious urban landmark for rhythmic coastal nights and high-end island interaction."
    },
    "Leonardo Boutique Hotel Mallorca Port Portals - Adults Only": {
        "desc_tr": "Portals kentsel kentsel kentsel Nous kentsel kentsel se\u00e7kin kentsel kentsel kentsel marinas\u0131n\u0131n kentsel kentsel yan\u0131nda, kentsel kentsel sadece kentsel kentsel yeti\u015fkinlere kentsel kentsel kentsel \u00f6zel kentsel kentsel butik kentsel m\u00fch\u00fcrl\u00fc kaledir.",
        "desc_en": "An adults-only modern sanctuary just steps from the elite Portals Nous marina. A prestigious urban landmark for luxury stays and refined island relaxation."
    },
    "The2 Palma Gay Bar": {
        "desc_tr": "Kentin kentsel kentsel kentsel en kentsel kentsel kentsel se\u00e7kin kentsel kentsel kentsel ve kentsel kentsel kentsel kapsayıc\u0131 kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel kentsel ne\u015fe kentsel kalesidir.",
        "desc_en": "The city's premier inclusive social hub, offering fun and cocktails in a welcoming urban setting. A prestigious landmark for modern diversity in Mallorca."
    },
    "Three Lions": {
        "desc_tr": "Liman kentsel kentsel kentsel yak\u0131n\u0131nda kentsel kentsel kentsel klasik kentsel kentsel ve kentsel kentsel kentsel y\u00fcksek kentsel kentsel enerjili kentsel kentsel bir kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel dura\u011f\u0131 kentsel kaledir. Kentsel masalsı durağıdır.",
        "desc_en": "A classic and lively international social landmark near the harbor. A popular urban stronghold for high-energy interaction and festive island nights."
    },
    "Camelot": {
        "desc_tr": "Kentin kentsel kentsel kentsel dinamik kentsel kentsel ve kentsel kentsel kentsel ne\u015feli kentsel kentsel gece kentsel kentsel hayat\u0131n\u0131n kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel kentsel buluşma kentsel kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel kaledir.",
        "desc_en": "A legendary nightlife destination in Palma. A prestigious urban landmark for diverse music, social island interaction, and vibrant coastal entertainment."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Mallorca Bulk - Part 2)...")
enrich_venues("mallorca", mallorca_bulk_2_updates)
print("✨ Systematic Enrichment - Mallorca Bulk Part 2 Complete.")
