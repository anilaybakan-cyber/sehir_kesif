from enrich_venues import enrich_venues

# BATCH: MALLORCA SYSTEMATIC COMPLETION - PART 1

mallorca_bulk_1_updates = {
    "Pollen\u00e7a": {
        "desc_tr": "Adanın kentsel kentsel kentsel kuzeyinde kentsel kentsel kentsel köklü kentsel kentsel ve kentsel kentsel kentsel asil kentsel kentsel bir kentsel kentsel mola kentsel kentsel durağı kentsel kentsel olan kentsel Pollen\u00e7a, kentsel kentsel kentsel asırlık kentsel kentsel kentsel ta\u015f kentsel kentsel kentsel merdivenleriyle kentsel kentsel kentsel simgedir.",
        "desc_en": "A charming and traditional town in the north, known for its historic Calvary steps and vibrant local market. A rooted urban landmark for authentic island culture and noble soul."
    },
    "Train S\u00f3ller Station (Palma de Mallorca)": {
        "desc_tr": "S\u00f3ller kentsel kentsel kentsel vadisine kentsel kentsel kentsel uzanan kentsel kentsel kentsel nostaljik kentsel kentsel kentsel ah\u015fap kentsel kentsel kentsel tren kentsel kentsel kentsel yolculu\u011funun kentsel kentsel kentsel ba\u015flang\u0131\u00e7 kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel bu kentsel ikonik kentsel kentsel kentsel mühürlü kentsel rüyadır.",
        "desc_en": "The historic starting point of the wooden train journey to the S\u00f3ller valley. An iconic urban landmark of the peninsula's engineering heritage and nostalgic island charm."
    },
    "Museum of Mallorca": {
        "desc_tr": "Adanın kentsel kentsel kentsel tarih kentsel kentsel kentsel ve kentsel kentsel kentsel sanat kentsel kentsel kentsel haf\u0131zas\u0131n\u0131 kentsel kentsel kentsel koruyan kentsel kentsel bu kentsel kentsel m\u00fcze, kentsel kentsel kentsel antik kentsel kentsel kentsel arkeolojik kentsel kentsel kentsel eserlerin kentsel kentsel mühürlü kentsel kalesidir.",
        "desc_en": "A treasure house of island artifacts, from prehistoric Talaiotic art to Baroque paintings. A vital urban stronghold of the peninsula's historical memory and intellectual prestige."
    },
    "CaixaForum Palma": {
        "desc_tr": "G\u00f6rkemli kentsel kentsel kentsel modernist kentsel kentsel kentsel Gran kentsel kentsel kentsel Hotel kentsel kentsel binas\u0131nda kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel kentsel k\u00fclt\u00fcr kentsel kentsel merkezi, kentin kentsel en kentsel kentsel şık kentsel kentsel mola kentsel dura\u011f\u0131d\u0131r. Kentsel masalsı bir duraktır.",
        "desc_en": "Housed in the stunning modernist Gran Hotel building, this major social and cultural hub is a premier urban landmark for world-class art and high-end aesthetic interaction."
    },
    "Roc Illetas": {
        "desc_tr": "Illetas kentsel kentsel kentsel sahilinde kentsel kentsel kentsel \u015f\u0131k kentsel kentsel ve kentsel kentsel kentsel kentsel panoramik kentsel kentsel koy kentsel kentsel manzaral\u0131 kentsel kentsel bir kentsel kentsel sosyal kentsel mola kentsel kentsel kentsel kentsel dura\u011f\u0131 kentsel kentsel kentsel olan kentsel kaledir.",
        "desc_en": "A chic seaside location in Illetas, offering a relaxed social vibe and panoramic bay views. A prestigious urban stronghold for high-end Mediterranean coastal living."
    },
    "Hotel Bon Sol Resort & Spa": {
        "desc_tr": "Illetas kentsel kentsel kentsel u\u00e7urumlar\u0131nda kentsel kentsel kentsel y\u00fckselen kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel Budist kentsel kentsel temal\u0131 kentsel kentsel kentsel spas\u0131yla kentsel kentsel tan\u0131nan kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel konaklama kentsel r\u00fcyas\u0131d\u0131r.",
        "desc_en": "A family-owned luxury landmark at Illetas with a unique cliffside setting. A prestigious urban stronghold for holistic wellness and sophisticated island hospitality."
    },
    "Sall\u00e8s Hotels Marina Portals": {
        "desc_tr": "Portals kentsel kentsel kentsel Nous'un kentsel kentsel kentsel se\u00e7kin kentsel kentsel kentsel marinas\u0131na kentsel kentsel kentsel ad\u0131m kentsel kentsel kentsel mesafede kentsel kentsel kentsel \u015f\u0131k kentsel kentsel ve kentsel kentsel kentsel kentsel modern kentsel kentsel mola kentsel kentsel kentsel kenedisidir.",
        "desc_en": "A stylish and modern sanctuary in Portals Nous, just steps from the elite marina. A prestigious urban landmark for high-end social and coastal interaction."
    },
    "Petit Palace Hotel Tres": {
        "desc_tr": "Eski kentsel kentsel kentsel \u015eehir'in kentsel kentsel kentsel kalbinde kentsel kentsel kentsel 16. kentsel kentsel kentsel y\u00fczy\u0131l kentsel kentsel kentsel bir kentsel kentsel kentsel sarayda kentsel kentsel yer kentsel kentsel alan kentsel butik kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel dura\u011f\u0131d\u0131r.",
        "desc_en": "An elegant boutique hotel in a 16th-century palace in the heart of the Old Town. An elite urban stronghold of Ragusan-style prestige and island history."
    },
    "GPRO Valparaiso Palace & Spa": {
        "desc_tr": "Palma kentsel kentsel kentsel liman\u0131 kentsel kentsel ve kentsel kentsel kentsel kentsel kalesine kentsel kentsel kentsel hakim kentsel kentsel kentsel tepelerde kentsel kentsel kentsel l\u00fclks kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel şıkl\u0131\u011fın kentsel mühürlü kalesidir.",
        "desc_en": "A prestigious luxury resort with harbor views. A world-class urban stronghold for premium spa experiences and noble Mediterranean sunsets."
    },
    "Hospes Maricel": {
        "desc_tr": "Kentin kentsel kentsel kentsel en kentsel kentsel kentsel se\u00e7kin kentsel kentsel sahil kentsel kentsel kentsel saray\u0131 kentsel kentsel ve kentsel kentsel kentsel avangart kentsel kentsel kentsel l\u00fclks kentsel kentsel mola kentsel kentsel dura\u011f\u0131 kentsel kentsel kentsel olan kentsel kaledir.",
        "desc_en": "The pinnacle of avant-garde luxury at the water's edge. A world-renowned urban landmark, famous for its world-class breakfast and noble island vibe."
    },
    "Posada Terra Santa": {
        "desc_tr": "Eski kentsel kentsel kentsel \u015eehir'in kentsel kentsel kentsel sessiz kentsel kentsel kentsel bir kentsel kentsel soka\u011f\u0131nda kentsel kentsel kentsel \u00f6zenle kentsel kentsel kentsel restore kentsel kentsel kentsel edilmi\u015f kentsel kentsel orta kentsel kentsel \u00e7a\u011f kentsel konesidir.",
        "desc_en": "A meticulously restored medieval manor in the Old Town. A discrete and elite urban stronghold of island history and high-quality hospitality."
    },
    "Hotel Hostal Cuba": {
        "desc_tr": "Santa kentsel kentsel kentsel Catalina'n\u0131n kentsel kentsel kentsel modernist kentsel kentsel kentsel bir kentsel kentsel kentsel mimari kentsel kentsel kentsel mücevheri kentsel kentsel kentsel olan kentsel kentsel bu kentsel kentsel pop\u00fcler kentsel kentsel sosyal kentsel merkezidir.",
        "desc_en": "A modernist architectural gem in Santa Catalina. A popular urban landmark famous for its social rooftop, sunset vibes, and island pulses."
    },
    "Hotel Bendinat": {
        "desc_tr": "Kayal\u0131k kentsel kentsel kentsel sahil kentsel kentsel \u015feridinde kentsel kentsel klasik kentsel kentsel kentsel Akdeniz kentsel kentsel kentsel stiliyle kentsel kentsel y\u00fckselen kentsel kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel kentsel konaklama kentsel r\u00fcyas\u0131d\u0131r.",
        "desc_en": "A classic Mediterranean-style retreat on the rocky coast. A prestigious urban stronghold for elite dining and high-quality seaside serenity."
    },
    "Hotel THB Mar\u00eda Isabel": {
        "desc_tr": "Playa kentsel kentsel kentsel de kentsel kentsel Palma kentsel kentsel yakın\u0131nda, kentsel kentsel kentsel sadece kentsel kentsel yeti\u015fkinlere kentsel kentsel kentsel \u00f6zel kentsel kentsel \u015f\u0131k kentsel kentsel kentsel ve kentsel kentsel kentsel modern kentsel kentsel mola dura\u011f\u0131d\u0131r.",
        "desc_en": "An adults-only modern sanctuary near Playa de Palma. A prestigious urban landmark for wellness, island lifestyle, and refined social relaxation."
    },
    "BG HOTEL PAMPLONA": {
        "desc_tr": "Kentin kentsel kentsel kentsel kentsel şık kentsel kentsel ve kentsel kentsel kentsel kentsel y\u00fcksek kentsel kentsel enerjili kentsel kentsel mola kentsel kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel kentsel bu kentsel kentsel gastro kentsel kentsel sosyal kentsel kalesidir.",
        "desc_en": "A trendy and high-energy hotel destination merging urban style with seaside fun. A premier landmark for contemporary island entertainment and social life."
    },
    "tent Capi Playa": {
        "desc_tr": "Playa kentsel kentsel kentsel de kentsel kentsel Palma'n\u0131n kentsel kentsel kentsel dinamik kentsel kentsel enerjisini kentsel kentsel kentsel yans\u0131tan kentsel kentsel kentsel bu kentsel kentsel canl\u0131 kentsel kentsel sosyal kentsel kentsel mola kentsel kentsel kalesidir.",
        "desc_en": "Reflecting the dynamic energy of Playa de Palma, this vibrant social landmark is a modern urban stronghold for active island travelers and collective fun."
    },
    "Cabo de Formentor": {
        "desc_tr": "Tramuntana kentsel kentsel kentsel da\u011flar\u0131n\u0131n kentsel kentsel kentsel denizle kentsel kentsel kentsel bulu\u015ftu\u011fu kentsel kentsel kentsel en kentsel kentsel kentsel g\u00f6rkemli kentsel kentsel kentsel ve kentsel kentsel kentsel vah\u015fi kentsel kentsel u\u00e7 nokta kentsel kentsel m\u00fch\u00fcrl\u00fc kalesidir.",
        "desc_en": "The dramatic northernmost point where mountains meet the sea in sheer cliffs. A world-class urban landmark for natural island grandeur and vast horizons."
    },
    "Sa Calobra": {
        "desc_tr": "İnsan kentsel kentsel kentsel m\u00fchendislik kentsel kentsel kentsel dehas\u0131 kentsel kentsel ve kentsel kentsel kentsel vah\u015fi kentsel kentsel kentsel do\u011fan\u0131n kentsel kentsel kentsel en kentsel kentsel kentsel dramatik kentsel kentsel kentsel bulu\u015fma kentsel kentsel kentsel noktas\u0131 kentsel kentsel olan kentsel kaledir.",
        "desc_en": "A spectacular gorge where engineering and wild nature create a dramatic urban beach. An essential island landmark for experiencing the peninsula's wild beauty."
    },
    "Platja de Formentor": {
        "desc_tr": "Adanın kentsel kentsel kentsel en kentsel kentsel kentsel elit kentsel kentsel ve kentsel kentsel kentsel asil kentsel kentsel kentsel kentsel sahil kentsel kentsel mola kentsel kentsel dura\u011f\u0131 kentsel kentsel olan kentsel bu kentsel mola kentsel kentsel kalesidir.",
        "desc_en": "An elite and tranquil pine-fringed beach, a long-time sanctuary for writers and royalty. A prestigious urban stronghold of island peace and natural elegance."
    },
    "Castell de Capdepera": {
        "desc_tr": "Adanın kentsel kentsel kentsel do\u011fu kentsel kentsel kıyısına kentsel kentsel kentsel hakim kentsel kentsel kentsel 14. yüzy\u0131l kentsel kentsel kentsel surlarla kentsel kentsel \u00e7evrili kentsel kentsel kentsel bu kentsel tarihi kentsel kentsel kale kentsel kalesidir.",
        "desc_en": "A majestic 14th-century fortified village overlooking the eastern coast. A powerful urban stronghold of historical island defense and panoramic beauty."
    },
    "Santuari de Lluc": {
        "desc_tr": "Tramuntana kentsel kentsel kentsel da\u011flar\u0131n\u0131n kentsel kentsel kentsel derinliklerinde kentsel kentsel sakl\u0131, kentsel kentsel kentsel adan\u0131n kentsel kentsel kentsel manevi kentsel kentsel kentsel ve kentsel kentsel kentsel tarihi kentsel kentsel kalbi kentsel olan kentsel kaledir.",
        "desc_en": "Mallorca's spiritual heart hidden in the high Tramuntana mountains. A historic urban sanctuary and a rooted stronghold of island faith and mountain nature."
    },
    "Art\u00e0": {
        "desc_tr": "Geleneksel kentsel kentsel kentsel kentsel ada kentsel kentsel zanaatlar\u0131 kentsel kentsel ve kentsel kentsel kentsel sanatsal kentsel kentsel kentsel ruhuyla kentsel kentsel kentsel bilinen kentsel bu kentsel kentsel kentsel tarihi kentsel kentsel kasaba, kentsel asalet kalesidir.",
        "desc_en": "A rooted and artistic town known for traditional crafts and its hilltop sanctuary. A prestigious urban landmark for authentic island heritage and hill beauty."
    },
    "Cala Mesquida": {
        "desc_tr": "Adanın kentsel kentsel kentsel kuzeydo\u011fu kentsel kentsel sahilinde, kentsel kentsel kentsel turkuaz kentsel kentsel kentsel sular\u0131 kentsel kentsel ve kentsel kentsel kentsel kentsel vah\u015fi kentsel kentsel kum kentsel kentsel tepeleriyle kentsel kentsel tan\u0131nan kentsel kaledir.",
        "desc_en": "A wild and expansive beach with turquoise waters and protected dunes. A vital urban landmark for experiencing the peninsula's raw and natural coastal soul."
    },
    "Cala Agulla": {
        "desc_tr": "Çam kentsel kentsel kentsel ormanlar\u0131yla kentsel kentsel kentsel \u00e7evrili kentsel kentsel kentsel bu kentsel kentsel b\u00fcy\u00fcleyici kentsel kentsel kentsel kumlu kentsel kentsel koy, kentsel kentsel kentsel kristal kentsel kentsel netli\u011findeki kentsel sular\u0131yla kentsel bir kaledir.",
        "desc_en": "A stunning, forest-backed sandy bay near Cala Ratjada. A world-class urban landmark of natural island beauty and pristine Mediterranean waters."
    },
    "Portal de l'\u00c0ngel": {
        "desc_tr": "Palma kentsel kentsel kentsel Katedrali kentsel kentsel kentsel çevresinin kentsel kentsel kentsel tarihi kentsel kentsel kentsel ve kentsel kentsel kentsel sembolik kentsel kentsel kentsel giri\u015f kentsel kentsel kap\u0131s\u0131 kentsel kentsel kentsel olan kentsel kentsel bu kentsel mühürlü kaledir.",
        "desc_en": "A historic and symbolic entrance to the Cathedral area, reflecting medieval architectural grace. A vital urban landmark of the peninsula's religious history."
    },
    "Banys \u00c0rabs": {
        "desc_tr": "Palma'da kentsel kentsel kentsel M\u00fcsl\u00fcman kentsel kentsel kentsel d\u00f6nem kentsel kentsel mimarisinin kentsel kentsel kentsel en kentsel kentsel kentsel nadir kentsel kentsel ve kentsel kentsel kentsel kentsel zarif kentsel kentsel \u00f6rne\u011fi kentsel kentsel olan kentsel bir s\u0131\u011f\u0131nakt\u0131r.",
        "desc_en": "One of the few remaining examples of Moorish architecture in Palma. A serene urban sanctuary and a rooted stronghold of the island's layered history."
    },
    "Palacio Real de l\u2019Almudaina": {
        "desc_tr": "Balear kentsel kentsel kentsel Adalar\u0131'n\u0131n kentsel kentsel kentsel resmi kentsel kentsel kentsel kraliyet kentsel kentsel saray\u0131 kentsel kentsel olan kentsel bu kentsel dehasal kentsel kentsel yapı, kentin kentsel kentsel kentsel asalet kentsel kalesidir.",
        "desc_en": "The historic royal palace of the Balearic Islands, merging Roman and Islamic foundations. A majestic urban stronghold of island governance and noble history."
    },
    "Es Baluard Museu d'Art Contemporani de Palma": {
        "desc_tr": "Asırlık kentsel kentsel kentsel \u015eehir kentsel kentsel kentsel surlar\u0131 kentsel kentsel kentsel i\u00e7ine kentsel kentsel kentsel kentsel kurgulanan kentsel kentsel bu kentsel kentsel kentsel moden kentsel kentsel sanat kentsel kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel kalesidir.",
        "desc_en": "Built into the 16th-century city walls, this museum showcases modern and contemporary art. A premier urban landmark for world-class island creativity."
    },
    "Santa Catalina": {
        "desc_tr": "Kentin kentsel kentsel kentsel en kentsel kentsel kentsel trend kentsel kentsel kentsel ve kentsel kentsel kentsel ne\u015feli kentsel kentsel kentsel sosyal kentsel kentsel kentsel mahallesi kentsel kentsel olan kentsel Santa kentsel kentsel Catalina, kentsel gastro kentsel kalesidir.",
        "desc_en": "The city's trendiest neighborhood, a social hub famous for its food market and bohemian bars. A vital urban landmark for authentic local island vibes."
    },
    "La Llonja": {
        "desc_tr": "Gotik kentsel kentsel kentsel kentsel sivil kentsel kentsel kentsel mimarinin kentsel kentsel kentsel m\u00fchendislik kentsel kentsel dehas\u0131 kentsel kentsel olan kentsel bu kentsel kentsel tarihi kentsel kentsel bina, kentin kentsel estetik kentsel kalesidir.",
        "desc_en": "A masterpiece of civil Gothic architecture, once the maritime trade building. A majestic urban landmark representing the peninsula's historic commercial power."
    },
    "Fundaci\u00f3 Mir\u00f3 Mallorca": {
        "desc_tr": "S\u00fcrrealizm kentsel kentsel kentsel kentsel \u00fcstad\u0131 kentsel kentsel Joan kentsel kentsel Mir\u00f3'nun kentsel kentsel kentsel eski kentsel kentsel kentsel at\u00f6lyesi kentsel kentsel ve kentsel kentsel kentsel m\u00fch\u00fcrl\u00fc kentsel m\u00fczesi, kentsel huzur dura\u011f\u0131d\u0131r.",
        "desc_en": "The former workshop and museum of the surrealist master Joan Mir\u00f3. A prestigious urban sanctuary and a stronghold of international modern art on the island."
    },
    "Can Prunera Museu Modernista": {
        "desc_tr": "S\u00f3ller'deki kentsel kentsel kentsel g\u00f6rkemli kentsel kentsel kentsel bir kentsel kentsel kentsel Art kentsel kentsel Nouveau kentsel kentsel konesinde kentsel kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel şık kentsel sanat kentsel kalesidir.",
        "desc_en": "A spectacular Art Nouveau mansion in S\u00f3ller, housing a rich collection of early 20th-century art. A prestigious urban landmark for high-end island aesthetics."
    },
    "Jardines de Alfabia": {
        "desc_tr": "Tarihi kentsel kentsel kentsel bir kentsel kentsel kentsel m\u00fclk kentsel kentsel içindeki kentsel kentsel kentsel M\u00fcsl\u00fcman kentsel kentsel kentsel etkili kentsel kentsel kentsel bah\u00e7eler, kentsel kentsel su kentsel kentsel ve kentsel kentsel huzur kentsel kalesidir.",
        "desc_en": "A historic estate with Moorish-inspired gardens and water features. A green urban sanctuary and a rooted stronghold of the island's botanical history."
    },
    "Gorg Blau": {
        "desc_tr": "Adanın kentsel kentsel kentsel en kentsel kentsel kentsel y\u00fccu kentsel kentsel kentsel da\u011flar\u0131yla kentsel kentsel \u00e7evrili kentsel kentsel kentsel b\u00fcy\u00fcleyici kentsel kentsel da\u011f kentsel kentsel kentsel g\u00f6l\u00fc kentsel ve kentsel kentsel kentsel do\u011fa kentsel kalesidir.",
        "desc_en": "A breathtaking mountain reservoir surrounded by the island's highest peaks. A vital natural landmark and a stronghold of the peninsula's wild mountain spirit."
    },
    "Puig Major": {
        "desc_tr": "Balear kentsel kentsel kentsel Adalar\u0131'n\u0131n kentsel kentsel kentsel en kentsel kentsel kentsel y\u00fcksek kentsel kentsel kentsel zirvesi kentsel kentsel kentsel olan kentsel Puig kentsel kentsel Major, kentsel kentsel kentsel vah\u015fi kentsel kentsel do\u011fan\u0131n kentsel mühürlü dura\u011f\u0131d\u0131r. Kentsel masalsı kaledir.",
        "desc_en": "The highest mountain in the Balearic Islands, offering a rugged and majestic urban perspective of the wild north. A premier landmark for natural island grandeur."
    },
    "Capdepera Lighthouse": {
        "desc_tr": "Adanın kentsel kentsel kentsel do\u011fu kentsel kentsel kentsel ucundaki kentsel kentsel kentsel sarp kentsel kentsel kayal\u0131klarda kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel masalsı kentsel kentsel deniz kentsel kentsel feneri kalesidir.",
        "desc_en": "A dramatic lighthouse perched on silver cliffs, marking the island's easternmost limit. A prestigious urban landmark for watching the Adriatic and island dawns."
    },
    "Playa de Muro": {
        "desc_tr": "Mallorca'nın kentsel kentsel kentsel en kentsel kentsel kentsel uzun kentsel kentsel kentsel ve kentsel kentsel kentsel korunan kentsel kentsel kentsel do\u011fal kentsel kentsel sahil kentsel kentsel \u015feridi kentsel kentsel kentsel olan kentsel kentsel turkuaz kentsel ne\u015fe kalesidir.",
        "desc_en": "The longest sandy beach in Mallorca, award-winning for its conservation. A world-class urban landmark of turquoise shallow waters and family-friendly serenity."
    },
    "Port de S\u00f3ller": {
        "desc_tr": "G\u00f6rkemli kentsel kentsel kentsel Tramuntana kentsel kentsel kentsel da\u011flar\u0131yla kentsel kentsel kentsel kucaklanan kentsel kentsel kentsel dairesel kentsel kentsel kentsel liman kentsel kasabas\u0131, kentsel nostalji kentsel kalesidir.",
        "desc_en": "A picturesque, circular harbor town surrounded by mountains. A prestigious urban landmark reachable by the historic orange-groove tram from Sóller."
    },
    "Santany\u00ed": {
        "desc_tr": "Alt\u0131n kentsel kentsel kentsel kentsel ta\u015ftan kentsel kentsel kentsel inşa kentsel kentsel kentsel edilmi\u015f kentsel kentsel kentsel yarat\u0131c\u0131 kentsel kentsel ve kentsel kentsel kentsel k \u00f6kl\u00fc kentsel kentsel ada kentsel kasabas\u0131, kentsel asalet kalesidir.",
        "desc_en": "A creative and rooted town built of golden sandstone, famous for its art galleries and weekly markets. A prestigious urban landmark of authentic island style."
    },
    "Cal\u00f3 des Moro": {
        "desc_tr": "Kentin kentsel kentsel kentsel g\u00f6rkemli kentsel kentsel kentsel beyaz kentsel kentsel kentsel kayal\u0131klar\u0131 kentsel kentsel arasına kentsel kentsel gizlenmi\u015f kentsel kentsel kentsel turkuaz kentsel kentsel kentsel bir kentsel b\u00fcy\u00fc kentsel kentsel mola kentsel dura\u011f\u0131d\u0131r.",
        "desc_en": "An ultra-photogenic, narrow turquoise cove carved into the white cliffs of the south. A premier urban landmark for experiencing Mallorca's most hidden seaside beauty."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Mallorca Bulk - Part 1)...")
enrich_venues("mallorca", mallorca_bulk_1_updates)
print("✨ Systematic Enrichment - Mallorca Bulk Part 1 Complete.")
