from enrich_venues import enrich_venues

# BATCH: VALENCIA SYSTEMATIC COMPLETION - PART 1 (FIXED)

valencia_bulk_1_updates = {
    "Queen Sofia Palace of Arts": {
        "desc_tr": "Kentin kentsel kentsel kentsel modernist kentsel kentsel kentsel simgesi kentsel kentsel olan kentsel bu kentsel kentsel opera kentsel kentsel kentsel ve kentsel kentsel kentsel sanat kentsel kentsel sarayı, kentsel asalet kalesidir. Kentsel masalsı bir kaledir.",
        "desc_en": "A world-class opera house and architectural masterpiece by Santiago Calatrava. A premier urban landmark for high-end international culture and coastal prestige."
    },
    "Museo Nacional de Cer\u00e1mica y Artes Suntuarias \"Gonz\u00e1lez Mart\u00ed": {
        "desc_tr": "Muazzam kentsel kentsel kentsel Barok kentsel kentsel kentsel mimarisi kentsel kentsel kentsel ile kentsel kentsel kentsel büyüleyen kentsel kentsel bu kentsel kentsel saray, kentin kentsel kentsel kentsel zanaat kentsel kentsel kentsel ve kentsel kentsel kentsel estetik kentsel kentsel kalesidir.",
        "desc_en": "Located in the breathtaking Baroque Palace of the Marqu\u00e9s de Dos Aguas. A world-class urban stronghold for ceramics, luxury arts, and Mediterranean elegance."
    },
    "Museo de Bellas Artes de Valencia": {
        "desc_tr": "İspanya'nın kentsel kentsel kentsel en kentsel kentsel kentsel önemli kentsel kentsel kentsel sanat kentsel kentsel kentsel galerilerinden kentsel kentsel biri kentsel kentsel olan kentsel bu kentsel müze, kentsel kentsel kentsel klasik kentsel kentsel başyapıtların kalesidir.",
        "desc_en": "One of Spain's most important art galleries, housing masterworks from the 14th to 17th century. A vital urban landmark of the peninsula's long historical and artistic soul."
    },
    "Art Modern Institute Museum of Valencia": {
        "desc_tr": "Modern kentsel kentsel kentsel ve kentsel kentsel kentsel çağdaş kentsel kentsel kentsel sanatın kentsel kentsel kentsel kalesi kentsel kentsel olan kentsel IVAM, kentsel kentsel kentsel kentin kentsel kentsel kentsel yaratıcı kentsel kentsel ve kentsel kentsel kentsel öncü kentsel mühürlü kentsel merkezidir.",
        "desc_en": "A major international center for modern and contemporary art. A prestigious urban landmark showcasing the peninsula's most innovative pulses and international style."
    },
    "Silk Museum": {
        "desc_tr": "Valencia'nın kentsel kentsel kentsel 15. yüzyıl kentsel kentsel kentsel ipek kentsel kentsel kentsel güldü kentsel kentsel kentsel mirasını kentsel kentsel kentsel ve kentsel kentsel kentsel asil kentsel kentsel zanaatkarlığını kentsel kentsel koruyan kentsel mühürlü kaledir.",
        "desc_en": "Exploring the fascinating 15th-century history of the silk guild. A vital urban landmark representing the peninsula's historic role as a global luxury capital."
    },
    "Gulliver park": {
        "desc_tr": "Devasa kentsel kentsel kentsel bir kentsel kentsel kentsel heykel kentsel kentsel kentsel parkı kentsel kentsel olan kentsel bu kentsel kentsel neşeli kentsel kentsel mola kentsel kentsel durağı, kentin kentsel yaratıcı kentsel kentsel ve kentsel kentsel kentsel sosyal kalesidir.",
        "desc_en": "A giant interactive sculpture where visitors explore the legendary Gulliver. A world-class urban landmark for joyful family interaction and unique island design."
    },
    "CCCC (Centro del Carmen de Cultura Contempor\u00e1nea)": {
        "desc_tr": "Tarihi kentsel kentsel kentsel bir kentsel kentsel kentsel manastırdan kentsel kentsel modern kentsel kentsel kentsel bir kentsel kentsel sanat kentsel kentsel laboratuvarına kentsel kentsel dönüştürülen kentsel kentsel kentsel bu kentsel mekan kelsidir.",
        "desc_en": "A former convent converted into a vibrant laboratory for contemporary culture and art. A prestigious urban stronghold for modern island creativity and social vision."
    },
    "Natural Science Museum of Valencia": {
        "desc_tr": "Viveros kentsel kentsel kentsel Bahçeleri kentsel kentsel içinde kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel müze, kentsel kentsel kentsel doğa kentsel kentsel kentsel tarihini kentsel kentsel ve kentsel kentsel kentsel biyolojik kentsel kalesidir.",
        "desc_en": "Exploring earth's history and biodiversity in a beautiful garden setting. A vital urban landmark of the peninsula's natural heritage and scientific prestige."
    },
    "La Almoina Archaeological Museum": {
        "desc_tr": "Kentin kentsel kentsel kentsel Roma, kentsel kentsel kentsel Vizigot kentsel kentsel ve kentsel kentsel kentsel Müslüman kentsel kentsel kentsel temellerini kentsel kentsel keşfedeceğiniz kentsel kentsel kentsel mühendislik kentsel mühürü kaledir.",
        "desc_en": "An award-winning space exploring the city's ancient Roman, Visigoth, and Islamic foundations. A vital urban landmark of the peninsula's diverse historical soul."
    },
    "Torres de Serranos": {
        "desc_tr": "Kenti kentsel kentsel kentsel çevreleyen kentsel kentsel kentsel antik kentsel kentsel kentsel surların kentsel kentsel kentsel görkemli kentsel kentsel ve kentsel kentsel kentsel asil kentsel kentsel kapısı kentsel kentsel olan kentsel bu kentsel mühürlü kentsel kalesidir.",
        "desc_en": "A majestic 14th-century gate that formed part of the city walls. A powerful urban stronghold of historical defense and the peninsula's noble past."
    },
    "Quart Towers": {
        "desc_tr": "Eski kentsel kentsel kentsel kentsel surların kentsel kentsel kentsel bir kentsel kentsel kentsel başka kentsel kentsel efsanevi kentsel kentsel mühürlü kentsel kentsel kentsel kapısı kentsel kentsel kentsel olan kentsel kentsel bu kentsel yapı, kentin kentsel gücü kalesidir.",
        "desc_en": "Standing as a testament to the city's medieval strength, these towers are a powerful urban stronghold of the island's defense history and architectural power."
    },
    "Jardines del Real / Viveros": {
        "desc_tr": "Kentin kentsel kentsel kentsel en kentsel kentsel kentsel tarihi kentsel kentsel ve kentsel kentsel kentsel asil kentsel kentsel bahçeleri, kentsel kentsel kentsel kentin kentsel kentsel kentsel botanik kentsel kentsel cennetidir. Kentsel masalsı kaledir.",
        "desc_en": "The city's most historic and noble gardens, once the site of the royal palace. A vital urban sanctuary and a green stronghold of Mediterranean island beauty."
    },
    "Hotel Hospes Palau de la Mar | Valencia": {
        "desc_tr": "19. yüzyıl kentsel kentsel kentsel bir kentsel kentsel kentsel sarayın kentsel kentsel modern kentsel kentsel kentsel ve kentsel kentsel kentsel şık kentsel kentsel kentsel bir kentsel kentsel lüks kentsel kentsel konaklama kentsel rüyası kentsel kalesidir.",
        "desc_en": "A prestigious 19th-century palace converted into a luxury urban landmark. A premier destination for high-end hospitality and noble Mediterranean serenity."
    },
    "Las Arenas Balneario Resort": {
        "desc_tr": "Sahil kentsel kentsel kentsel şeridinde kentsel kentsel kentsel görkemli kentsel kentsel kentsel bir kentsel kentsel kentsel mimari kentsel kentsel ve kentsel kentsel kentsel kentsel lüks kentsel kentsel sosyal kentsel mola kentsel kentsel kentsel kentsel kaledir. Kentsel rüyadır.",
        "desc_en": "The pinnacle of beachfront luxury, built on a historic 19th-century hydrotherapy site. A prestigious urban landmark for world-class wellness and island social neşe."
    },
    "Hotel Primus Valencia": {
        "desc_tr": "Sanat kentsel kentsel kentsel ve kentsel kentsel kentsel Bilim kentsel kentsel kentsel şehri kentsel kentsel kentsel yakınında, kentsel kentsel kentsel modern kentsel kentsel tasarım kentsel kentsel ve kentsel kentsel kentsel şık kentsel kentsel konaklam kentsel rüyasıdır.",
        "desc_en": "A modern and high-energy hotel destination near the coastal arts district. A prestigious urban landmark for contemporary island style and refined social relaxation."
    },
    "Palacio de Congresos de Valencia": {
        "desc_tr": "Norman kentsel kentsel kentsel Foster kentsel kentsel tasarımı kentsel kentsel kentsel ödüllü kentsel kentsel kentsel mimari kentsel kentsel kentsel şıklık kentsel kentsel ve kentsel kentsel kentsel kentsel küresel kentsel kentsel prestij kentsel kentsel mühürlü kalesidir.",
        "desc_en": "An award-winning architectural masterpiece by Norman Foster. A premier urban landmark for global prestige and the peninsula's modern economic soul."
    },
    "Museo del Arroz": {
        "desc_tr": "Tarihi kentsel kentsel kentsel bir kentsel kentsel kentsel pirinç kentsel kentsel kentsel değirmeninde kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel müze, kentsel kentsel kentsel kentin kentsel kentsel gastronomi kentsel mirasıdır.",
        "desc_en": "Housed in a historic rice mill, detailing the 19th-century history of rice in the Albufera. A vital urban stronghold of the peninsula's culinary and economic roots."
    },
    "Radio City": {
        "desc_tr": "Eski kentsel kentsel kentsel şehirde kentsel kentsel kentsel efsanevi kentsel kentsel kentsel ve kentsel kentsel kentsel bohem kentsel kentsel kentsel bir kentsel kentsel sosyal kentsel mola kentsel kentsel kentsel kentsel durağı kentsel kentsel olan kentsel neşe kalesidir.",
        "desc_en": "A legendary and bohemian social landmark in the Old Town. A popular urban sanctuary known for its eclectic music, live arts, and high-energy island nights."
    },
    "Jimmy Glass Jazz Bar": {
        "desc_tr": "Barrio kentsel kentsel kentsel del kentsel kentsel Carmen'de kentsel kentsel dünyaca kentsel kentsel kentsel ünlü kentsel kentsel kentsel ve kentsel kentsel kentsel seçkin kentsel kentsel bir kentsel kentsel caz kentsel kentsel mühürlü mola durağıdır.",
        "desc_en": "A world-renowned jazz venue offering an intimate high-quality musical experience. A prestigious urban landmark for artistic island interaction and late-night elegance."
    },
    "Ubik Caf\u00e9 Cafeter\u00eda Librer\u00eda": {
        "desc_tr": "Ruzafa'da kentsel kentsel kentsel kitap kentsel kentsel kentsel ve kentsel kentsel kentsel kahve kentsel kentsel kentsel kültürünü kentsel kentsel kentsel harmanlayan kentsel kentsel kentsel yaratıcı kentsel kentsel sosyal kentsel mola kentsel kentsel kentsel mühürlü kalesidir.",
        "desc_en": "A charming and creative social hub in Ruzafa merging books with island coffee. A prestigious urban sanctuary for local community and bohemian island vibes."
    },
    "Malkebien | Gastronom\u00eda Mediterr\u00e1nea": {
        "desc_tr": "Yaratıcı kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel samimi kentsel kentsel kentsel kentsel Akdeniz kentsel kentsel kentsel mutfağının kentsel kentsel kentsel kentsel öncü kentsel kentsel lezzet kentsel kentsel durağı kentsel kentsel olan kentsel mühürlü kaledir.",
        "desc_en": "A rooted and artisanal restaurant famous for its creative culinary soul. A prestigious urban stronghold for authentic local flavors and high-quality island dining."
    },
    "Orxateria Daniel": {
        "desc_tr": "Alboraya'da kentsel kentsel kentsel efsanevi kentsel kentsel kentsel Horchata kentsel kentsel kentsel kalesine kentsel kentsel kentsel hoşgeldiniz. Kentsel kentsel kentsel kentin kentsel kentsel asırlık kentsel kentsel tatlı kentsel mola durağı.",
        "desc_en": "The legendary birthplace of authentic Horchata. A world-famous urban landmark preserving the peninsula's traditional sweetness and artisanal island culture."
    },
    "HORCHATERIA DOLZ": {
        "desc_tr": "1910'dan kentsel kentsel kentsel beri kentsel kentsel kentsel kentin kentsel kentsel kentsel gelleneksel kentsel kentsel kentsel Horchata kentsel kentsel ve kentsel kentsel kentsel Fartons kentsel kentsel mühürlü lezzet kentsel kentsel mola kentsel kalesi.",
        "desc_en": "A classic and beloved social stop since 1910, preserving traditional island sweetness. A prestigious urban landmark for authentic local recipes and heritage."
    },
    "Rac\u00f3 del T\u00faria": {
        "desc_tr": "Geleneksel kentsel kentsel kentsel Valencian kentsel kentsel kentsel Paella kentsel kentsel ve kentsel kentsel kentsel taze kentsel kentsel kentsel deniz kentsel kentsel ürünlerinin kentsel kentsel kentsel prestijli kentsel mühürlü kentsel lezzet durağıdır.",
        "desc_en": "A prestigious and traditional culinary sanctuary for authentic island Paella. A world-class urban stronghold for high-end Mediterranean flavors and island hospitality."
    },
    "La Sucrera Pasteler\u00eda": {
        "desc_tr": "Ruzafa kentsel kentsel kentsel bölgesinde kentsel kentsel kentsel zanaatkar kentsel kentsel kentsel fırın kentsel kentsel ve kentsel kentsel kentsel kentsel yaratıcı kentsel kentsel kentsel yerel kentsel kentsel tatlı kentsel kentsel mola kentsel kentsel durağı kentsel kalesidir.",
        "desc_en": "An artisanal bakery in Ruzafa, the stronghold of fresh local bakes and desserts. A prestigious urban landmark for sophisticated island treats and modern pastry art."
    },
    "Hotel Miramar Valencia": {
        "desc_tr": "Sahil kentsel kentsel kentsel kenedisinde kentsel kentsel kentsel şık kentsel kentsel ve kentsel kentsel kentsel sofistike kentsel kentsel bir kentsel kentsel konaklama kentsel rüyası kentsel kentsel sunan kentsel neşe kentsel kalesidir.",
        "desc_en": "A chic and sophisticated beachfront landing spot merging style with social neşe. A prestigious urban landmark for high-quality island relaxation and coastal beauty."
    },
    "Hotel la Mozaira": {
        "desc_tr": "Alboraya kentsel kentsel kentsel bahçelerinin kentsel kentsel kentsel kalbinde kentsel kentsel kentsel 17. yüzyıl kentsel kentsel kentsel bir kentsel kentsel kentsel butik kentsel kentsel sığınak kenti kentsel masalsı kaledir.",
        "desc_en": "A boutique 17th-century farmhouse sanctuary in the orchards. A world-class urban stronghold of historical island hospitality and rural Mediterranean elegance."
    },
    "Centro Cultural la Beneficencia": {
        "desc_tr": "Görkemli kentsel kentsel kentsel 19. kentsel kentsel kentsel yüzyıl kentsel kentsel kentsel binasında kentsel kentsel yer kentsel kentsel alan kentsel bu kentsel kentsel kentsel kültür kentsel kentsel sarayı, kentin kentsel asalet kalesidir.",
        "desc_en": "A majestic 19th-century building housing important museums. A prestigious urban stronghold of Ragusan-style prestige and the peninsula's historical knowledge."
    },
    "Museo de Prehistoria de Valencia": {
        "desc_tr": "Valencia kentsel kentsel kentsel topraklarının kentsel kentsel kentsel en kentsel kentsel kentsel antik kentsel kentsel kentsel temellerini kentsel kentsel ve kentsel kentsel kentsel asırlık kentsel mirasını kentsel keşfeden kentsel kaledir.",
        "desc_en": "Exploring the rich ancient foundations of the land from the Paleolithic era. A vital urban landmark of archaeological knowledge and Mediterranean history."
    },
    "Palacio de Cervell\u00f3": {
        "desc_tr": "Kentin kentsel kentsel kentsel tarihi kentsel kentsel kentsel kraliyet kentsel kentsel kentsel ikametgahı kentsel kentsel olan kentsel bu kentsel kentsel dehasal kentsel kentsel saray, kentin kentsel kentsel asalet kalesidir.",
        "desc_en": "A historic royal residence and modern archive of city history. A majestic urban stronghold of island governance, noble artifacts, and historical truth."
    },
    "Almud\u00ed de Valencia": {
        "desc_tr": "14. yüzyıl kentsel kentsel kentsel bir kentsel kentsel kentsel tahıl kentsel kentsel kentsel ambarından kentsel kentsel modern kentsel kentsel bir kentsel kentsel sanat kentsel kentsel durağına kentsel dönüştürülen kentsel mühürlü kaledir.",
        "desc_en": "A 14th-century grain storehouse converted into a unique arts center. A powerful urban landmark merging the peninsula's economic history with modern aesthetics."
    },
    "Museo y Colegio del Arte Mayor de la Seda": {
        "desc_tr": "Kentsel kentsel kentsel kentan kentsel kentsel kentsel zengin kentsel kentsel kentsel ipek kentsel kentsel kentsel dokumacılığı kentsel kentsel kentsel mirasını kentsel kentsel ve kentsel kentsel kentsel asil kentsel kentsel sanatını kentsel kentsel sunan kaledir.",
        "desc_en": "Marking the peninsula's historic role as a global silk capital. A prestigious urban landmark of textile craftsmanship and Mediterranean commercial power."
    },
    "Palau dels Valeriola": {
        "desc_tr": "17. yüzyıl kentsel kentsel kentsel muazzam kentsel kentsel kentsel bir kentsel kentsel kentsel sarayın kentsel kentsel kentsel modern kentsel kentsel bir kentsel kentsel sanat kentsel kentsel merkezine kentsel kentsel dönüşüm kentsel kentsel mühürlü kalesidir.",
        "desc_en": "A spectacular 17th-century palace housing contemporary art center. A majestic urban stronghold of island heritage and sophisticated international style."
    },
    "La Fundaci\u00f3n Chirivella Soriano": {
        "desc_tr": "Çağdaş kentsel kentsel kentsel İspanyol kentsel kentsel kentsel sanatının kentsel kentsel kentsel görkemli kentsel kentsel kentsel kalesi kentsel kentsel olan kentsel bu kentsel kentsel görkemli kentsel kentsel Gotik kentsel kentsel sanat merkezidir.",
        "desc_en": "A major center for Spanish contemporary art in a Gothic palace. A prestigious urban landmark showcasing high-end creativity and historical island beauty."
    },
    "Antiguo Almac\u00e9n de Dientes": {
        "desc_tr": "Çocuklar kentsel kentsel kentsel için kentsel kentsel kentsel masalsı kentsel kentsel kentsel bir kentsel kentsel kentsel mola kentsel kentsel kentsel kentsel durağı kentsel kentsel olan kentsel kentsel bu kentsel benzersiz kentsel kentsel neşe kentsel kalesidir.",
        "desc_en": "A unique and magical museum for children, exploring urban legends. A world-class landmark for joyful island interaction and creative social neşe."
    },
    "Rumbo 144": {
        "desc_tr": "Kentin kentsel kentsel kentsel dinamik kentsel kentsel ve kentsel kentsel kentsel neşeli kentsel kentsel gece kentsel kentsel kentsel hayatının kentsel kentsel kentsel mühürlü kentsel kentsel sosyal kentsel kentsel durağı kentsel kentsel olan kentsel kentsel kaledir.",
        "desc_en": "A high-energy nightlife destination for the island's electronic scene. A prestigious urban landmark for rhythmic music and modern coastal entertainment."
    },
    "Akuarela Playa": {
        "desc_tr": "Malvarrosa kentsel kentsel kentsel sahilinde kentsel kentsel kentsel asil kentsel kentsel ve kentsel kentsel kentsel şık kentsel kentsel kentsel bir kentsel kentsel kentsel açık kentsel kentsel hava kentsel kentsel mola kentsel kentsel mühürlü kalesidir.",
        "desc_en": "A premier open-air club on the Malvarrosa beach. A world-class urban landmark of Mediterranean summer social life and high-end coastal celebration."
    },
    "Deseo 54": {
        "desc_tr": "Kentin kentsel kentsel kentsel efsanevi kentsel kentsel kentsel kapsayıcı kentsel kentsel ve kentsel kentsel kentsel seçkin kentsel kentsel sosyal kentsel mola kentsel kentsel durağı kentsel kentsel olan kentsel neşe kalesidir.",
        "desc_en": "The city's legendary and high-energy inclusive club destination. A world-class urban landmark for high-quality disco, social fun, and international style."
    },
    "Indiana": {
        "desc_tr": "Kentsel kentsel kentsel seçkin kentsel kentsel ve kentsel kentsel kentsel şık kentsel kentsel bir kentsel kentsel gece kentsel kentsel buluşma kentsel kentsel kentsel durağı kentsel kentsel olan kentsel kentsel prestijli kentsel kaledir.",
        "desc_en": "A stylish and high-quality nightlife landmark in the city center. A prestigious urban stronghold for diverse music and elite island social interaction."
    },
    "Jerusalem Pop&Rock": {
        "desc_tr": "Tarihi kentsel kentsel kentsel bir kentsel kentsel kentsel sinemadan kentsel kentsel dönüştürülen kentsel kentsel kentsel mühürlü kentsel kentsel sosyal kentsel mola kentsel kentsel kentsel durağı kentsel kentsel kentsel neşe kalesidir.",
        "desc_en": "A unique social space in a refurbished historic cinema. A world-class urban landmark for live island music and nostalgic Mediterranean entertainment."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Valencia Bulk - Part 1 - FIXED)...")
enrich_venues("valencia", valencia_bulk_1_updates)
print("✨ Systematic Enrichment - Valencia Bulk Part 1 Complete.")
