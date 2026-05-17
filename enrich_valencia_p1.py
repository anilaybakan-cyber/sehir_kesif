#!/usr/bin/env python3
import json

updates = {
    "ChIJp0DSBFBPYA0RWQEYnnI354A": {
        "description": "Valensiya'nın Orta Çağ savunma surlarının hayatta kalan iki kapısından biri olan Quart Kuleleri, kentin askeri tarihine devasa taş gövdesiyle tanıklık eder. 15. yüzyıldan kalma bu kuleler, üzerlerindeki Napolyon savaşlarından kalan gülle izleriyle kentin dirençli ruhunu ve asaletini simgeleyen anıtsal bir duraktır.",
        "description_en": "One of the two surviving gates of Valencia's medieval defense walls, the Quart Towers witness the city me's military history with their massive stone bodies. These 15th-century towers, with cannonball marks from the Napoleonic wars, are a monumental stop symbolizing the city's resilient spirit and nobility."
    },
    "ChIJs3E16q5IYA0RIaj9Wq87iW0": {
        "description": "Viveros Bahçeleri'nin huzurlu atmosferinde yer alan bu müze, milyonlarca yıllık doğa tarihini etkileyici fosil ve iskelet koleksiyonlarıyla sergiliyor. Avrupa'nın en önemli paleontolojik koleksiyonlarından birine ev sahipliği yapan müze, özellikle devasa dinozor replikalarıyla çocuklar ve bilim meraklıları için havadar ve öğretici bir keşif noktasıdır.",
        "description_en": "Located in the peaceful atmosphere of Viveros Gardens, this museum exhibits millions of years of natural history with impressive fossil and skeleton collections. Hosting one of Europe's most significant paleontological collections, the museum is an airy and educational discovery point for children and science enthusiasts, especially with its giant dinosaur replicas."
    },
    "ChIJgWlkRa1IYA0Rn8Rxi08dej8": {
        "description": "Valensiya'nın kalbinde yer alan bu arkeolojik alan, kentin Roma, Vizigot ve Müslüman dönemlerine ait katmanlarını cam zemin altından görmenizi sağlar. Antik forum, hamamlar ve sokak kalıntılarıyla kentin yaklaşık 2000 yıllık kentsel evrimine tanıklık edebileceğiniz, tarihin derinliklerine açılan mistik ve sessiz bir penceredir.",
        "description_en": "This archaeological site in the heart of Valencia allows you to see the city's layers from Roman, Visigoth, and Muslim periods under a glass floor. It's a mystical and quiet window into the depths of history where you can witness the city's nearly 2000-year urban evolution through ancient forums, baths, and street remains."
    },
    "ChIJO8tx7sNIYA0Rtq3I4LdFoSE": {
        "description": "Sanat ve Bilim Şehri'nin en görkemli yapılarından biri olan Kraliçe Sofia Sanat Sarayı, modern mimarinin bir şaheseridir. Fütüristik tasarımı ve dört farklı sahnesiyle dünyanın en önemli opera ve performans merkezlerinden biri kabul edilen bina, kentin estetik vizyonunu ve kültürel prestijini Akdeniz göğüne taşıyan bir simgedir.",
        "description_en": "One of the most grand structures of the City of Arts and Sciences, the Queen Sofia Palace of Arts is a masterpiece of modern architecture. Considered one of the world's most significant opera and performance centers with its futuristic design and four different stages, the building is a symbol carrying the city's aesthetic vision and cultural prestige to the Mediterranean sky."
    },
    "ChIJdSAn8JlIYA0RdLvjJtEhtv4": {
        "description": "Barok mimarinin en görkemli örneklerinden biri olan Marqués de Dos Aguas Sarayı'nda yer alan bu müze, seramik sanatının en zarif dünyasını sergiliyor. Altın kaplamalı heybetli girişi ve paha biçilemez porselen koleksiyonlarıyla kentin asaletini ve el sanatlarındaki ustalığını yansıtan paha biçilemez bir kültürel hazinedir.",
        "description_en": "Located in the Palace of the Marqués de Dos Aguas, one of the grandest examples of Baroque architecture, this museum exhibits the most elegant world of ceramic art. With its gold-plated imposing entrance and priceless porcelain collections, it is a priceless cultural treasure reflecting the city me's nobility and mastery in crafts."
    },
    "ChIJuxhXYU9PYA0RTzodeNfP1Mw": {
        "description": "Valensiya İllüstrasyon ve Modernite Müzesi (MuVIM), aydınlanma döneminden günümüze modern düşüncenin ve görsel kültürün gelişimini cesur sergilerle sunuyor. Modern mimarisi ve kentin tarihsel gelişimini felsefi bir bakış açısıyla ele alan koleksiyonlarıyla, kentin entelektüel derinliğini keşfetmek isteyenler için ilham verici bir duraktır.",
        "description_en": "The Valencian Museum of Illustration and Modernity (MuVIM) presents the development of modern thought and visual culture from the Enlightenment to the present through bold exhibitions. With its modern architecture and collections addressing the city's historical development with a philosophical perspective, it is an inspiring stop for those wanting to explore the city's intellectual depth."
    },
    "ChIJO26w7o9FYA0RO6wuhxqX8Fc": {
        "description": "Ünlü mimar Norman Foster tarafından tasarlanan Valensiya Kongre Sarayı, kentin modern iş ve teknoloji dünyasındaki yerini simgeleyen fütüristik bir yapıdır. Işık oyunları, sürdürülebilir tasarımı ve uluslararası etkinliklere ev sahipliği yapmasıyla kentin kozmopolit enerjisini ve geleceğe dönük yüzünü temsil eden iddialı bir mimari simgedir.",
        "description_en": "Designed by famous architect Norman Foster, the Valencia Conference Centre is a futuristic structure symbolizing the city me's place in the modern business and technology world. With light plays, sustainable design, and hosting international events, it is an ambitious architectural symbol representing the city's cosmopolitan energy and future-oriented face."
    },
    "ChIJJ5T9FVNPYA0RRavjAQjSpS4": {
        "description": "Valensiya'nın eski kentine açılan en görkemli Gotik kapı olan Serranos Kuleleri, kentin tarihi ihtişamını ve savunma gücünü simgeler. 14. yüzyıldan kalma bu yapı, surların üzerinden sunduğu panaromik Turia Bahçeleri ve eski şehir manzarasıyla hem tarih meraklıları hem de fotoğraf tutkunları için büyüleyici ve havadar bir duraktır.",
        "description_en": "The Serranos Towers, the grandest Gothic gate opening to Valencia's old town, symbolize the city me's historical grandeur and defense power. This 14th-century structure is a fascinating and airy stop for both history buffs and photography enthusiasts with the panoramic Turia Gardens and old town views it offers from walls."
    },
    "ChIJ98E0IMFIYA0RX4pSCR-943Q": {
        "description": "Jonathan Swift'in ünlü karakteri Gulliver'in yere uzanmış devasa bir replikasından oluşan bu park, Valensiya'nın en yaratıcı ve neşeli oyun alanıdır. Çocukların ipler ve kaydıraklar üzerinde cüceler gibi koşturduğu bu fantastik tasarım, kentin aile dostu ve hayal gücüne değer veren modern yüzünü en eğlenceli haliyle yansıtır.",
        "description_en": "Consisting of a giant replica of Jonathan Swift's famous character Gulliver lying on the ground, this park is Valencia's most creative and joyful playground. This fantastic design where children run like Lilliputians over ropes and slides reflects the city me's family-friendly and imagination-valuing modern face in its most fun form."
    },
    "ChIJf3kiFBPYA0RVRd6OL2SDMA": {
        "description": "Eski bir yetimhanenin etkileyici bir kültür merkezine dönüştürülmesiyle hayata geçen La Beneficència, kentin arkeolojik ve etnolojik mirasına ev sahipliği yapıyor. Sessiz avluları ve kentin dünden bugüne sosyal tarihini anlatan sergileriyle, kentin hafızasını keşfetmek isteyenler için havadar, sakin ve bilgilendirici bir kültürel vaha niteliğindedir.",
        "description_en": "Brought to life by transforming an old orphanage into an impressive cultural center, La Beneficència hosts the city's archaeological and ethnological heritage. With quiet courtyards and exhibitions telling the city me's social history from yesterday to today, it is an airy, quiet, and informative cultural oasis for those wanting to explore the city's memory."
    },
    "ChIJU0Yei1BPYA0RTQbWU6KZhi8": {
        "description": "Valensiya'nın Prehistorya Müzesi, Paleolitik çağdan Roma dönemine kadar adanın en eski yerleşimcilerinin izini süren paha biçilemez bir koleksiyon sunuyor. Özellikle 'La Bastida de les Alcusses'ten çıkarılan antik savaşçı objeleri ve kentin köklü tarihsel katmanlarıyla, akademik düzeyde derin bir keşif durağıdır.",
        "description_en": "Valencia's Prehistory Museum offers a priceless collection tracing the island's earliest settlers from the Paleolithic age to the Roman period. It's a deep discovery stop at an academic level, especially with ancient warrior objects unearthed from 'La Bastida de les Alcusses' and the city's deep historical layers."
    },
    "ChIJ_cR0ta5IYA0RIfb-SwzNmk8": {
        "description": "Kentin en eski ve en görkemli bahçelerinden biri olan Viveros (Jardines del Real), asırlık ağaçları, şık heykelleri ve gül bahçeleriyle huzur dolu bir kaçış noktasıdır. Eskiden kraliyet sarayına ev sahipliği yapan bu alan, bugün Valensiya'nın yeşil kalbi olarak hem dinlenmek hem de kentin bitki örtüsünün tadını çıkarmak için en popüler duraktır.",
        "description_en": "One of the city's oldest and grandest gardens, Viveros (Jardines del Real) is a peaceful escape with century-old trees, chic statues, and rose gardens. Formerly hosting the royal palace, this area is today the green heart of Valencia and the most popular stop for both resting and enjoying the city me's flora."
    },
    "ChIJGyHg0V1IYA0RO00gORz97Tc": {
        "description": "Valensiya'nın deniz kıyısındaki mahallesinde yer alan Pirinç Müzesi, kentin dünyaca ünlü paella kültürünün ve tarım mirasının hikayesini anlatıyor. Eski bir pirinç fabrikasında kurulu olan müze, geleneksel işleme makineleri ve kentin bereketli topraklarındaki pirinç yetiştiriciliği tarihine dair samimi ve öğretici bir perspektif sunuyor.",
        "description_en": "Located in Valencia's seaside neighborhood, the Rice Museum tells the story of the city me's world-famous paella culture and agricultural heritage. Established in an old rice factory, the museum offers a sincere and educational perspective on traditional processing machinery and the history of rice farming in the city me's fertile lands."
    },
    "ChIJEdMF6FNPYA0RoNSmpYKP-T0": {
        "description": "Eski bir manastırın dinamik bir çağdaş sanat merkezine dönüştürülmesiyle hayat bulan CCCC, Valensiya'nın yaratıcı enerjisini en özgür haliyle sergiliyor. Gotik ve Rönesans avluları arasında düzenlenen avangart sergileri ve interaktif projeleriyle kentin sanat ruhunu geleceğe taşıyan en neşeli ve ilham verici duraklardan biridir.",
        "description_en": "Brought to life by transforming an old monastery into a dynamic contemporary art center, CCCC exhibits Valencia's creative energy in its freest form. It's one of the most joyful and inspiring stops carrying the city's artistic spirit to the future with avant-garde exhibitions and interactive projects organized among Gothic and Renaissance courtyards."
    },
    "ChIJl_6YvEpPYA0RV2zFBwTxvAM": {
        "description": "Valensiya Boğa Güreşi Müzesi, kentin bu tartışmalı ama köklü geleneğine dair paha biçilemez bir arşiv ve obje koleksiyonu sunar. Boğa güreşi alanının (Plaza de Toros) hemen yanında yer alan müze, kentin sosyal tarihinde derin izler bırakmış bu kültürel ritüelin kostümlerini, afişlerini ve tarihçesini merak edenler için bilgilendirici bir noktadır.",
        "description_en": "The Valencia Bullfighting Museum offers a priceless archive and object collection regarding this controversial but deep-rooted tradition of the city. Located right next to the bullring (Plaza de Toros), the museum is an informative spot for those curious about the costumes, posters, and history of this cultural ritual that has left deep marks in the city me's social history."
    },
    "ChIJadUei1BPYA0RR095153gDOc": {
        "description": "CCCC bünyesinde yer alan Sala Parpalló, Valensiya'nın en yenilikçi sergi alanlarından biri olarak çağdaş görsel sanatlara odaklanır. Modern sanatın sınırlarını zorlayan projeleri ve genç sanatçılara sunduğu platformla, kentin kozmopolit ruhunu ve sanatsal gelişimini yakından takip edebileceğiniz havadar ve kaliteli bir sanat durağıdır.",
        "description_en": "Located within CCCC, Sala Parpalló focuses on contemporary visual arts as one of Valencia's most innovative exhibition spaces. With projects pushing thresholds of modern art and the platform it offers to young artists, it is an airy and high-quality art stop where you can closely follow the city me's cosmopolitan spirit and artistic development."
    },
    "ChIJs07-wLRIYA0RA7f41tj5Z0Q": {
        "description": "Valensiya'nın kalbinde yer alan bu modern galeri, sanatın sadece binalar içinde değil, kentsel alanla bütünleşik bir şekilde yaşamasını savunuyor. Şık tasarımı ve seçkin sergi takvimiyle kentin butik sanat dünyasında önemli bir yer tutan galeri, yaratıcı zihinlerin buluştuğu ilham verici ve prestijli bir kültürel duraktır.",
        "description_en": "This modern gallery in the heart of Valencia advocates for art to live integrated with urban space, not just inside buildings. Holding an important place in the city me's boutique art world with its chic design and exclusive exhibition calendar, the gallery is an inspiring and prestigious cultural stop where creative minds meet."
    },
    "ChIJo7unzvFIYA0R3AHW6Cg6vXM": {
        "description": "Sanat ve Bilim Şehri'nin modern silüetinde yer alan Primus Valencia, minimalist tasarımı ve konforlu spa olanaklarıyla kentin en stil sahibi otellerinden biridir. Cam ve çeliğin dans ettiği mimarisi ve Akdeniz ışığını bolca alan ferah odalarıyla, Valensiya'nın fütüristik ruhunu yakından hissetmek isteyen gezginler için ideal bir konaklama adresidir.",
        "description_en": "Located in the modern silhouette of the City of Arts and Sciences, Primus Valencia is one of the city me's most stylish hotels with its minimalist design and comfortable spa facilities. With architecture where glass and steel dance and spacious rooms receiving plenty of Mediterranean light, it is an ideal accommodation address for travelers wanting to closely feel Valencia's futuristic spirit."
    },
    "ChIJiWifO_BIYA0RdERDCqS31_E": {
        "description": "Aqua Alışveriş Merkezi ile bütünleşik bir konumda bulunan bu otel, hem modern alışveriş konforu hem de Sanat ve Bilim Şehri manzarasıyla paha biçilemez bir avantaj sunuyor. Şık ve fonksiyonel tasarımıyla kentin kozmopolit temposuna uyum sağlayan tesis, Valensiya'nın fütüristik atmosferini solumak isteyenlerin favori durakları arasındadır.",
        "description_en": "Located in an integrated position with the Aqua Shopping Centre, this hotel offers a priceless advantage with both modern shopping comfort and views of sea the City of Arts and Sciences. Harmonizing with the city's cosmopolitan pace with its chic and functional design, the facility is among the favorite stops for those wanting to breathe in Valencia's futuristic atmosphere."
    },
    "ChIJr93TOyNGYA0RzZNIJD6JAFA": {
        "description": "Kentin biraz dışında, huzurlu bir bölgede yer alan bu devasa tesis, geniş spa'sı ve kapsamlı etkinlik alanlarıyla gerçek bir dinlenme vahasidir. Modern ve konforlu odalarıyla Valensiya'nın hem şehir imkanlarına yakın hem de kargaşadan uzak kalmak isteyen aileler ve etkinlik grupları için en iddialı ve kaliteli konaklama noktalarından biridir.",
        "description_en": "This massive facility located in a peaceful area just outside the city is a true oasis of relaxation with its wide spa and extensive event areas. With modern and comfortable rooms, it's one of the most ambitious and high-quality accommodation points for families and event groups wanting to stay near Valencia's city facilities while away from the chaos."
    },
    "ChIJ0dnyZDBPYA0ROz1Bc_kjM9E": {
        "description": "Valensiya'nın zengin şarap kültürünü butik bir gastronomi deneyimiyle sunan La Cepa Vieja, yerel bağların hikayesini tabaklarınıza taşıyor. Samimi atmosferi ve mevsimlik ürünlerle hazırlanan özgün mönüsüyle, kentin gastronomi mirasını gurme bir bakış açısıyla keşfetmek isteyenlerin yıllardır vazgeçilmez yerel adreslerinden biridir.",
        "description_en": "Presenting Valencia's rich wine culture with a boutique gastronomic experience, La Cepa Vieja brings the story of local vineyards to your plates. With its sincere atmosphere and original menu prepared with seasonal products, it has been one of the indispensable local addresses for years for those wanting to explore the city me's gastronomic heritage from a gourmet perspective."
    },
    "ChIJYVn8x7BIYA0RIb5xwMV46xI": {
        "description": "Tarihi bir sarayın asaletini modern lüksle birleştiren Hospes Palau de la Mar, Valensiya'nın en seçkin ve romantik konaklama duraklarından biridir. Panaromik iç avlusu, şık spa alanı ve kentin katedraline yürüme mesafesindeki konumuyla, kendinizi kentin tarihinde özel hissedeceğiniz rafine bir sığınak niteliğindedir.",
        "description_en": "Combining the nobility of a historical palace with modern luxury, Hospes Palau de la Mar is one of Valencia's most exclusive and romantic accommodation stops. With its panoramic inner courtyard, chic spa area, and location within walking distance of the city's cathedral, it serves as a refined sanctuary where you'll feel special in the city me's history."
    },
    "ChIJD1guwWlIYA0REfH09cBlg5o": {
        "description": "Kentin tarihi deniz hamamları geleneğini modern bir lüks resort anlayışıyla yaşatan Las Arenas, sahil şeridinde görkemli bir sütunlu bina olarak yükseliyor. Masmavi denizi kucaklayan bahçeleri ve aristokratik konforuyla, Valensiya'da deniz sefasını en üst seviyede ve stil sahibi bir atmosferde yaşamak isteyenlerin vazgeçilmez adresidir.",
        "description_en": "Keeping the city me's historic seaside baths tradition alive with a modern luxury resort concept, Las Arenas rises as a grand colonnaded building on the coastline. With its gardens embracing the deep blue sea and aristocratic comfort, it is the indispensable address for those wanting to live the seaside delight in Valencia at the highest level and in a stylish atmosphere."
    },
    "ChIJo9xXF0JIYA0RvKtIMKtAYbw": {
        "description": "Denize sıfır konumu ve butik atmosferiyle öne çıkan bu otel, Valensiya'nın taze sahil havasını ve güneşini en doğal haliyle sunuyor. Şık çatı terası ve kentin limanına olan yakınlığıyla bilinir. Özellikle kentin kozmopolit deniz yaşamını huzurlu bir akşamla birleştirmek isteyen gezginler için havadar ve kaliteli bir duraktır.",
        "description_en": "Standing out with its seafront location and boutique atmosphere, this hotel offers Valencia's fresh coastal air and sun in its most natural form. Known for its chic roof terrace and proximity to the city's harbor, it's an airy and high-quality stop especially for travelers wanting to combine the city me's cosmopolitan marine life with a peaceful evening."
    },
    "ChIJfVqoQbBHYA0RgH3sszFVE0k": {
        "description": "Valensiya'nın bereketli tarlaları (La Huerta) içinde saklı bir vaha olan bu tarihi konak, geleneksel ile lüksün harika bir birleşimidir. Reyhan ve portakal çiçekleri kokulu bahçeleri ve mistik tasarımıyla, kentin kozmopolit kalabalığından uzaklaşıp adanın asude kırsal geçmişine tanıklık edebileceğiniz benzersiz ve samimi bir duraktır.",
        "description_en": "A hidden oasis within Valencia me's fertile fields (La Huerta), this historic mansion is a wonderful combination of traditional and luxury. With gardens smelling of basil and orange blossoms and a mystical design, it's a unique and sincere stop where you can witness the island's serene rural past away from the city's cosmopolitan crowds."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/valencia.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data.get('highlights', []):
    pid = place.get('id')
    if pid in updates:
        place['description'] = updates[pid]['description']
        place['description_en'] = updates[pid]['description_en']
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Valencia Part 1: Enriched {count} items.")
