#!/usr/bin/env python3
import json

updates = {
    "ChIJt7XXBe5OmRIRsFp2uDDUEmk": {
        "description": "Ibiza'nın en şık ve popüler koylarından biri olan Cala Jondal, kristal berrak suyu ve çevresindeki çam ormanlarıyla ünlüdür. Adanın en prestijli beach club'larına ev sahipliği yapan bu plaj, hem güneşin tadını çıkarmak hem de enerjik İbiza atmosferini solumak isteyen gezginlerin favori duraklarından biridir.",
        "description_en": "One of Ibiza's most chic and popular bays, Cala Jondal is famous for its crystal-clear water and surrounding pine forests. Hosting the island's most prestigious beach clubs, this beach is a favorite stop for travelers wanting to both enjoy the sun and breathe in the energetic Ibiza atmosphere."
    },
    "ChIJI8OUxhJFmRIRY9_8Shwa2kM": {
        "description": "UNESCO koruması altındaki Ses Salines Doğal Parkı'nın bir parçası olan bu ikonik plaj, bembeyaz kumları ve sığ turkuaz deniziyle bilinir. Adanın en hareketli sahil şeridinde yer alan bu bölge, şık restoranları ve müzik dolu atmosferiyle Akdeniz yazının gerçek ruhunu yansıtır.",
        "description_en": "Part of the UNESCO-protected Ses Salines Natural Park, this iconic beach is known for its white sands and shallow turquoise sea. Located on the island's most vibrant coastline, this area reflects the true spirit of Mediterranean summer with its chic restaurants and music-filled atmosphere."
    },
    "ChIJV9zdNitEmRIRlwxcfS_UlUU": {
        "description": "Ibiza'nın en büyük çocuk eğlence merkezlerinden biri olan Gran Piruleto Park, dev kaydırakları, su oyunları ve oyun alanlarıyla aileler için harika bir duraktır. Playa d'en Bossa'da yer alan bu park, çocukların güvenle eğlendiği, yetişkinlerin ise dinlendiği neşeli bir atmosfer sunuyor.",
        "description_en": "One of Ibiza's largest children's entertainment centers, Gran Piruleto Park is a great stop for families with its giant slides, water games, and playgrounds. Located in Playa d'en Bossa, this park offers a cheerful atmosphere where children have safe fun while adults relax."
    },
    "ChIJ63ixeLBGmRIRgoui5dSSuvc": {
        "description": "Dalt Vila'nın antik surları üzerindeki en stratejik noktalardan biri olan San Pedro Burcu, kentin tarihi savunma ihtişamını sergiliyor. Surların üzerinden körfeze ve limana açılan panaromik manzara, İbiza'nın binlerce yıllık geçmişini ve bugünkü modern güzelliğini bir arada görmenizi sağlar.",
        "description_en": "One of the most strategic points on the ancient walls of Dalt Vila, the San Pedro Bastion showcases the city's historical defensive grandeur. The panoramic view of the bay and harbor from the walls allows you to see Ibiza's thousands of years of past and its modern beauty together."
    },
    "ChIJF72dOLBGmRIR2xf-1Q3mtWI": {
        "description": "Dalt Vila'nın dar ve tarihi sokaklarında yer alan Museo Puget, 20. yüzyılın başlarındaki İbiza yaşamını ressam Narcís Puget Riquer ve oğlunun eserleriyle sergiliyor. Geleneksel kıyafetler ve eski kentsel manzaraların betimlendiği koleksiyon, adanın kültürel mirasına ve sanatsal köklerine derin bir yolculuk sunar.",
        "description_en": "Located in the narrow and historical streets of Dalt Vila, Museo Puget exhibits early 20th-century Ibiza life through the works of painter Narcís Puget Riquer and his son. The collection, depicting traditional costumes and old urban scenes, offers a deep journey into the island's cultural heritage and artistic roots."
    },
    "ChIJy6diybNGmRIR5Hh-p34fbIU": {
        "description": "Arnavut kaldırımlı Sa Penya mahallesinin uçurum kenarında yer alan Casa Broner, modernizmin İbiza'daki en etkileyici mimari örneklerinden biridir. Mimar Erwin Broner tarafından tasarlanan bu ev müze, minimalist şıklığı ve muazzam deniz manzarasıyla hem tasarım meraklıları hem de tarih severler için ilham vericidir.",
        "description_en": "Perched on the cliff edge of the cobbled Sa Penya neighborhood, Casa Broner is one of the most impressive architectural examples of modernism in Ibiza. Designed by architect Erwin Broner, this house museum is inspiring for both design buffs and history lovers with its minimalist elegance and magnificent sea views."
    },
    "ChIJATDjK0pBmRIRg1axFLLYbN4": {
        "description": "Marina Ibiza'da yer alan kentin en prestijli eğlence duraklarından biri olan bu casino, modern tasarımı ve lüks atmosferiyle her gece elit bir kitleyi ağırlar. Şık barı ve seçkin oyun alanlarıyla İbiza'nın kozmopolit gece hayatına sofistike ve heyecan dolu bir alternatif sunuyor.",
        "description_en": "One of the city's most prestigious entertainment spots in Marina Ibiza, this casino hosts an elite crowd every night with its modern design and luxury atmosphere. With its chic bar and exclusive gaming areas, it offers a sophisticated and exciting alternative to Ibiza's cosmopolitan nightlife."
    },
    "ChIJq1PwZ7tGmRIR2SeKsTFOnAc": {
        "description": "Dünyanın en iyi korunmuş antik mezarlıklarından biri kabul edilen Puig des Molins, kentin Fenike-Kartaca döneminden kalan paha biçilemez bir mirasdır. Binlerce hipoje mezarın bulunduğu bu geniş alan ve yanındaki müze, Akdeniz'in antik inanç ve geleneklerine dair sarsıcı ve bilgilendirici bir keşif sunar.",
        "description_en": "Considered one of the world's best-preserved ancient necropolises, Puig des Molins is a priceless heritage from the city's Phoenician-Carthaginian period. This vast area with thousands of hypogeum tombs and the adjacent museum offers a poignant and informative discovery of the Mediterranean's ancient beliefs and traditions."
    },
    "ChIJT3i09LBGmRIRkfAK1UW_oqU": {
        "description": "Eski kentin girişindeki bu prestijli galeri, İbiza'nın ışığını ve renklerini tuvallerine yansıtan yerel sanatçı Marta Torres'in eserlerine ev sahipliği yapar. Sanatın doğayla ve adanın dokusuyla bütünleştiği bu modern mekan, kentin yaratıcı enerjisini ve estetik ruhunu solumak için mükemmel bir duraktır.",
        "description_en": "This prestigious gallery at the entrance of the old town hosts works by local artist Marta Torres, who reflects Ibiza's light and colors on her canvases. This modern space, where art integrates with nature and the island's texture, is a perfect stop to breathe in the city's creative energy and aesthetic spirit."
    },
    "ChIJDcbsaABHmRIRtjv1P_JhOlg": {
        "description": "Playa d'en Bossa sahil şeridine tepeden bakan bu seyir noktası, adanın en uzun plajının ve berrak sularının kesintisiz manzarasını sunuyor. Özellikle gün doğumu ve gün batımı saatlerinde gökyüzünün büründüğü renkleri izlemek ve kenti kuş bakışı fotoğraflamak isteyenler için harika bir noktadır.",
        "description_en": "This viewpoint overlooking the Playa d'en Bossa coastline offers an uninterrupted view of the island's longest beach and its clear waters. It's a great spot for those wanting to watch the colors the sky takes especially at sunrise and sunset and to photograph the city from a bird's eye view."
    },
    "ChIJF7yYiLFHmRIRgzOuGV61EiY": {
        "description": "İbiza'nın gizli koylarını ve kristal mağaralarını denizden keşfetmek isteyen maceraperestler için kano turları eşsiz bir deneyimdir. Dalga sesleri eşliğinde adanın sarp kayalıklarını ve ulaşılamaz koylarını kürek çekerek keşfetmek, denizin huzurunu ve gücünü iliklerinize kadar hissettirir.",
        "description_en": "Kayak tours are a unique experience for adventurers wanting to explore Ibiza's hidden bays and crystal caves from the sea. Exploring the island's steep cliffs and inaccessible coves by rowing accompanied by the sound of waves makes you feel the sea's peace and power to your bones."
    },
    "ChIJcV_JeudHmRIRUFCq61MYFcE": {
        "description": "İbiza merkezinde ailelerin ve doğa severlerin favorisi olan bu geniş park, yeşil alanları, çocuk oyun parkları ve spor sahalarıyla ferah bir mola yeridir. Modern tasarımı ve güvenli atmosferiyle şehrin koşturmacasından kaçıp palmiye ağaçları altında huzur bulmak için mükemmel bir tercihtir.",
        "description_en": "A favorite for families and nature lovers in the heart of Ibiza, this vast park is a spacious break spot with green areas, children's playgrounds, and sports fields. With its modern design and safe atmosphere, it's a perfect choice to escape city hustle and find peace under palm trees."
    },
    "ChIJ9ZO2Jo5GmRIRGnkHI4sjRqc": {
        "description": "Eski bir İbiza malikanesinin özenle restore edilmesiyle hayat bulan bu kültürel nokta, adanın geleneksel mimarisini ve kırsal yaşam tarihini sergiliyor. Zeytin bahçeleri arasındaki huzurlu konumuyla İbiza'nın sadece bir eğlence adası değil, aynı zamanda köklü bir tarım mirasına sahip olduğunu hatırlatan bir duraktır.",
        "description_en": "Brought to life by the careful restoration of an old Ibiza manor, this cultural spot exhibits the island's traditional architecture and rural life history. With its peaceful location among olive groves, it's a stop reminding us that Ibiza is not just a party island, but also possesses a deep-rooted agricultural heritage."
    },
    "ChIJuYqL1PtHmRIRC5FA9-HcMOg": {
        "description": "Kentin ana liman girişinde yer alan turizm ofisi, İbiza'yı keşfetmeye yeni başlayanlar için en güncel harita, etkinlik ve ulaşım bilgilerini sunan profesyonel bir karşılama merkezidir. Uzman personeliyle, adanın saklı hazinelerini ve en iyi rotalarını planlamanıza yardımcı olacak önemli bir başlangıç noktasıdır.",
        "description_en": "Located at the city's main harbor entrance, the tourism office is a professional welcoming center offering the most up-to-date maps, events, and transport info for those just starting to explore Ibiza. With its expert staff, it's an important starting point to help plan your island routes and find hidden treasures."
    },
    "ChIJr4Y8QQBHmRIRG2z1R0EgXHo": {
        "description": "İbiza'nın bohem ve sanatsal ruhunu yansıtan bu modern atölye-galeri, yerel zanaatkarların el yapımı objelerinden özgün takılara kadar geniş bir seçki sunuyor. Şehrin dokusuyla uyumlu bu butik mekan, kendiniz veya sevdikleriniz için adadan anlamlı ve stil sahibi bir hatıra almak için harika bir adrestir.",
        "description_en": "Reflecting Ibiza's bohemian and artistic spirit, this modern workshop-gallery offers a wide selection ranging from local artisans' handmade objects to original jewelry. This boutique space compatible with the city's texture is a great address to buy a meaningful and stylish souvenir for yourself or loved ones."
    },
    "ChIJPWyHnbBGmRIR6WEFcSzx0Z4": {
        "description": "Kentin en görkemli meydanlarından birinde yükselen Vara de Rei Heykeli, İbiza'nın tarihine yön veren önemli askeri liderlerden biri adına dikilmiştir. Çevresindeki tarihi binalar, şık kafeler ve her zaman hareketli olan sosyal atmosferiyle bu anıt, kentin buluşma noktalarının ve modern kimliğinin bir parçasıdır.",
        "description_en": "Rising in one of the city's most grand squares, the Vara de Rei Statue was erected in honor of one of the important military leaders who shaped Ibiza's history. With its surrounding historical buildings, chic cafes, and always vibrant social atmosphere, this monument is a part of the city's meeting points and modern identity."
    },
    "ChIJtxOFLUJHmRIRjTrcnBgrrNc": {
        "description": "Dalt Vila'nın girişinde, begonviller ve renkli çiçeklerle bezenmiş bu karakteristik yapı, adanın en fotojenik ve ikonik binalarından biridir. Beyaz duvarları ve her mevsim canlı kalan bitki örtüsüyle 'Çiçekli Ev', kentin kartpostallık silüetini tamamlayan en zarif ve estetik köşe taşlarından biridir.",
        "description_en": "At the entrance of Dalt Vila, this characteristic building adorned with bougainvillaea and colorful flowers is one of the island's most photogenic and iconic structures. With its white walls and vegetation that stays vibrant in every season, the 'House of Flowers' is one of the most elegant and aesthetic cornerstones completing the city's postcard silhouette."
    },
    "ChIJqyuvZ6NGmRIRQp-US8cRqig": {
        "description": "Denize sıfır konumu ve modern mimarisiyle öne çıkan bu otel, İbiza'nın en havalı ve huzurlu konaklama duraklarından biridir. Panaromik deniz manzaralı terası, şık spa alanı ve kalitesiyle kentin hem eğlence noktalarına yakın hem de gürültüden uzak kalmak isteyen seçkin gezginlerin favori adresleri arasındadır.",
        "description_en": "Standing out with its seafront location and modern architecture, this hotel is one of Ibiza's coolest and most peaceful accommodation stops. With its terrace featuring panoramic sea views, chic spa area, and quality, it is among the favorite addresses for elite travelers wanting to be near entertainment while staying away from noise."
    },
    "ChIJqTPRsNJFmRIRk-wzViSEhhg": {
        "description": "Tarihi bir kulenin gölgesinde, masmavi denizle bütünleşen bu prestijli otel, lüks ve sükuneti bir arada sunuyor. Şık havuz alanı ve sofistike tasarımıyla Playa d'en Bossa'nın kalbinde yer alan bu tesis, adanın lüks yaşam tarzını ve Akdeniz güneşini doyasıya hissetmek için muazzam bir yaşam alanıdır.",
        "description_en": "In the shadow of a historical tower, this prestigious hotel integrated with the deep blue sea offers luxury and tranquility together. Located in the heart of Playa d'en Bossa with a chic pool area and sophisticated design, this facility is a magnificent living space to fully feel the island's luxury lifestyle and Mediterranean sun."
    },
    "ChIJtYq10khBmRIRpuEdMZ-oU5c": {
        "description": "Marina Botafoch'ta kentin silüetine ve Dalt Vila'nın görkemli manzarasına hakim olan bu otel, modern sanatla konforu birleştiriyor. Şık barı ve seçkin mönüsüyle bildiğimiz bu tesis, İbiza'nın yat limanı kültürünü ve kozmopolit lüksünü en rafine haliyle deneyimlemenizi sağlıyor.",
        "description_en": "Dominating the city's silhouette and the grand view of Dalt Vila in Marina Botafoch, this hotel combines modern art with comfort. Known for its chic bar and exclusive menu, this facility allows you to experience Ibiza's yacht harbor culture and cosmopolitan luxury in its most refined form."
    },
    "ChIJY0V3EElBmRIROuGesgRI-2U": {
        "description": "İkonik tasarımı ve marinadaki prestijli konumuyla Ocean Drive, 1920'lerin Art Deco stilini modern İbiza ruhuyla buluşturuyor. Özellikle gün batımı kokteylleri ve etkileyici DJ performanslarıyla ünlü çatı terası, kentin elit gece hayatına başlamak için adanın en stil sahibi duraklarından biridir.",
        "description_en": "With its iconic design and prestigious location in the marina, Ocean Drive brings 1920s Art Deco style together with the modern spirit of Ibiza. Its roof terrace, particularly famous for sunset cocktails and impressive DJ performances, is one of the island's most stylish stops to begin the city's elite nightlife."
    },
    "ChIJX6raWfJGmRIRAOfTWfnGZy0": {
        "description": "Eski bir çiftliğin (finca) büyüleyici bir butik otele dönüştürülmesiyle hayata geçen Casa Maca, zeytin ve incir ağaçları arasında huzurlu bir vaha sunuyor. Dalt Vila'ya bakan muazzam manzarası ve yöresel malzemelerle hazırlanan gurme mutfağıyla, adanın otantik ve lüks kırsal yaşamını keşfetmek için benzersizdir.",
        "description_en": "Brought to life by transforming an old farmhouse (finca) into a charming boutique hotel, Casa Maca offers a peaceful oasis among olive and fig trees. With its magnificent view overlooking Dalt Vila and gourmet cuisine prepared with local ingredients, it is unique for exploring the island's authentic and luxury rural life."
    },
    "ChIJudLO7LFGmRIRR1r6AXmyWCY": {
        "description": "Dalt Vila'nın tarihi surları içinde, kentin en yüksek ve en prestijli noktasında yer alan bu malikane otel, gerçek bir aristokratik lüks vadediyor. Antik taş duvarları, şık dekorasyonu ve körfeze bakan panaromik terasıyla, kendinizi İbiza'nın tarihinde özel hissedeceğiniz romantik ve rafine bir adrestir.",
        "description_en": "Located within the historical walls of Dalt Vila at the city's highest and most prestigious point, this manor hotel promises true aristocratic luxury. With its ancient stone walls, chic decoration, and panoramic terrace overlooking the bay, it is a romantic and refined address where you will feel special in Ibiza's history."
    },
    "ChIJrUJ3McJ-YQ0RIj4SyNJ7u7Y": {
        "description": "Playa d'en Bossa'nın kristal sularına sıfır konumuyla Garbi Ibiza, modern tasarımı ve ferahlatıcı spa olanaklarıyla huzurlu bir yaz tatili sunuyor. Eğlencenin merkezinde olmasına rağmen sunduğu sükunet ve yüksek kaliteli hizmet anlayışıyla, adanın enerjisini ve güneşini dengelemek isteyen gezginlerin favorisidir.",
        "description_en": "With its seafront location on the crystal waters of Playa d'en Bossa, Garbi Ibiza offers a peaceful summer holiday with modern design and refreshing spa facilities. Despite being in the center of entertainment, it is a favorite for travelers wanting to balance the island's energy and sun with its tranquility and high-quality service."
    },
    "ChIJn_CNWDlBmRIRZ7aWhGYmuLI": {
        "description": "Talamanca koyunun sakinliğinde, minimalist şıklığı ve modern konforuyla öne çıkan bu otel, marinaya yürüme mesafesindeki konumuyla büyük bir avantaj sunar. Şehrin kozmopolit havasını hissedip aynı zamanda huzurlu bir akşam geçirmek isteyenler için ideal olan tesis, adanın çağdaş tatil anlayışını yansıtır.",
        "description_en": "Standing out with its minimalist elegance and modern comfort in the tranquility of Talamanca bay, this hotel offers a great advantage with its walking distance to the marina. Ideal for those wanting to feel the city's cosmopolitan air while having a peaceful evening, the facility reflects the island's contemporary holiday concept."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/ibiza.json.draft'
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

print(f"✅ Ibiza Part 1: Enriched {count} items.")
