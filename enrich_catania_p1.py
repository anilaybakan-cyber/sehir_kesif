#!/usr/bin/env python3
import json

updates = {
    "cat_vuciata_kitchen": {
        "description": "Catania'nın tarihi pazar yerinin kalbinde yer alan Vuciata, taze deniz ürünleri ve yerel Sicilya malzemeleriyle hazırlanan gurme bir mutfaktır. Geleneksel tatları modern bir vizyonla yeniden yorumlayan mekan, kentin gastronomi mirasını en otantik ve şık haliyle keşfetmek isteyenler için muazzam bir duraktır.",
        "description_en": "Located in the heart of Catania's historical market, Vuciata is a gourmet kitchen prepared with fresh seafood and local Sicilian ingredients. Reinterpreting traditional flavors with a modern vision, the venue is a magnificent stop for those wanting to explore the city me's gastronomic heritage in its most authentic and stylish form."
    },
    "cat_lognina_rest": {
        "description": "Catania'nın karakteristik balıkçı limanı Ognina'da yer alan bu seçkin restoran, denize sıfır bir masada Akdeniz'in en taze lezzetlerini sunuyor. Dalga sesleri eşliğinde, yerel balıkçıların günlük avıyla hazırlanan mönüsüyle kentin denizle olan kopmaz bağını ve kaliteli gastronomi ruhunu temsil eden bir adrestir.",
        "description_en": "Located in Catania's characteristic fishing harbor Ognina, this elite restaurant offers the Mediterranean's freshest flavors at a seafront table. With a menu prepared with the daily catch of local fishermen accompanied by the sound of waves, it is an address representing the city me's unbreakable bond with the sea and the spirit of quality gastronomy."
    },
    "cat_vermut_aperitivo": {
        "description": "Kentin hareketli sokakları arasında yer alan bu şık bar, Sicilya usulü aperitivo kültürünün ve tazeleyici kokteyllerin merkezidir. Modern tasarımı ve kentin kozmopolit kitlesini bir araya getiren sosyal dokusuyla, akşamüstü güneşini ferahlatıcı bir içecek ve gurme atıştırmalıklar eşliğinde uğurlamak için en havalı duraklardandır.",
        "description_en": "Located among the city's vibrant streets, this chic bar is the center of Sicilian style aperitivo culture and refreshing cocktails. With its modern design and social texture bringing together the city's cosmopolitan crowd, it's one of the coolest stops to bid farewell to the afternoon sun with a refreshing drink and gourmet snacks."
    },
    "cat_cutilisci_seaside": {
        "description": "San Giovanni Li Cuti'nin ikonik siyah volkanik taşlı plajında yer alan Cutilisci, denizden tabağa en taze Akdeniz lezzetlerini sunuyor. Doğal dekorasyonu ve Catania'nın eşsiz sahil silüetine karşı sunduğu huzurlu atmosferiyle, kentin sahil gastronomisini en samimi haliyle yaşatan kaliteli bir lezzet limanıdır.",
        "description_en": "Located on the iconic black volcanic stone beach of San Giovanni Li Cuti, Cutilisci offers the freshest Mediterranean flavors from sea to plate. With its natural decoration and peaceful atmosphere offered against Catania's unique coastal silhouette, it is a high-quality flavor harbor making you experience the city's seaside gastronomy in its most sincere form."
    },
    "cat_trattoria_u_fichera_": {
        "description": "Piazza Carlo Alberto pazarının neşeli karmaşasının hemen yanında yer alan bu bölge, kentin asırlık alışveriş geleneğini ve yerel yaşamın nabzını yansıtır. Etrafındaki tarihi yapılar ve taze ürün kokularıyla kentin sosyal tarihini solumak, yerel halkla iç içe kalarak Catania'nın gerçek enerjisini hissetmek için paha biçilemez bir noktadır.",
        "description_en": "Located right next to the joyful chaos of the Piazza Carlo Alberto market, this area reflects the city me's century-old shopping tradition and the pulse of local life. With surrounding historical structures and scents of fresh products, it's a priceless point to breathe in the city's social history and feel Catania's real energy by staying intertwined with the local people."
    },
    "cat_trattoria_da_turi_16": {
        "description": "Catania'nın en şık ve geniş bulvarlarından biri olan Via Umberto I, kentin 19. yüzyıl mimarisini ve modern alışveriş kültürünü bir araya getiriyor. Heybetli binaları, şık butikleri ve ağaçlıklı yürüyüş yollarıyla kentin klasik zarafetini ve kozmopolit ritmini hissetmek isteyen gezginler için havadar ve kaliteli bir duraktır.",
        "description_en": "One of Catania's most stylish and wide boulevards, Via Umberto I brings together the city me's 19th-century architecture and modern shopping culture. With imposing buildings, chic boutiques, and tree-lined walking paths, it's an airy and high-quality stop for travelers wanting to feel the city's classic elegance and cosmopolitan rhythm."
    },
    "cat_trattoria_sikulo_18": {
        "description": "Catania'nın en eski ve en neşeli sokak pazarlarından biri olan 'Fera o Luni', kentin günlük yaşamının en renkli ve kaotik sahnesidir. Taze sebzelerden otantik Sicilya peynirlerine kadar adanın tüm bereketini sergileyen bu pazar, kentin yerel ruhunu, seslerini ve kokularını en saf haliyle keşfetmek isteyenler için bir açık hava müzesidir.",
        "description_en": "One of Catania me's oldest and most joyful street markets, 'Fera o Luni' is the most colorful and chaotic scene of the city me's daily life. Showcasing all the island's abundance from fresh vegetables to authentic Sicilian cheeses, this market is an open-air museum for those wanting to explore the city me's local spirit, sounds, and scents in their purest form."
    },
    "cat_trattoria_salvo_24": {
        "description": "Catania limanını kuşatan bu tarihi kemerler, kentin savunma ve ulaşım tarihindeki önemli bir mimari simgedir. Denize komşu masaları ve kentin tarihi surlarının bir parçası olan devasa taş yapısıyla kentin geçmişteki deniz ticareti gücünü ve estetik vizyonunu simgeleyen etkileyici ve havadar bir sahil durağıdır.",
        "description_en": "These historical arches surrounding Catania harbor are an important architectural symbol in the city me's defense and transport history. Symbolizing the city's past maritime trade power and aesthetic vision with its seafront tables and massive stone structure being part of the city's historical walls, it is an impressive and airy coastal stop."
    },
    "cat_trattoria_da_turi_26": {
        "description": "Catania'nın ana ulaşım kapısı olan bu tarihi istasyon, kentin modern dünyaya açılan pencerelerinden biridir. Etkileyici dış cephesi ve kentin merkezine yakın konumuyla kentin kozmopolit enerjisini ilk anda hissetmenizi sağlayan yapı, Etna'nın gölgesindeki bu kadim kente gelişin ve ayrılışın nostaljik bir sembolüdür.",
        "description_en": "Catania's main transport gateway, this historical station is one of the city me's windows opening to the modern world. Allowing you to feel the city me's cosmopolitan energy at first sight with its impressive facade and location near the city center, the structure is a nostalgic symbol of arrival and departure in this ancient city in the shadow of Etna."
    },
    "cat_trattoria_da_turi_31": {
        "description": "Catania'nın entelektüel kalbinde yer alan bu tarihi kitapçı, kentin kültür ve sanat dünyasının en köklü duraklarından biridir. Binlerce kitap arasında kentin edebi mirasını keşfedebileceğiniz, yazar imza günleri ve kültürel etkinliklerle kentin yaratıcı enerjisini soluyabileceğiniz, samimi ve havadar bir kültürel vaha niteliğindedir.",
        "description_en": "Located in the intellectual heart of Catania, this historical bookstore is one of the most deep-rooted stops of the city me's world of culture and art. It is a sincere and airy cultural oasis where you can explore the city me's literary heritage among thousands of books and breathe in the city me's creative energy with book signings and cultural events."
    },
    "cat_trattoria_u_fichera_33": {
        "description": "Catania sokaklarının vazgeçilmez bir parçası olan tarihi içecek büfelerinden Chiosco Giammona, kentin meşhur soda ve taze meyve karışımlarını sunar. Yaz sıcağında yerel bir mola vermek, kentin günlük ritmini izlemek ve geleneksel İtalyan içecek kültürünü en samimi haliyle tatmak için kentin en karakteristik noktalarından biridir.",
        "description_en": "One of the historical drink kiosks that are an indispensable part of Catania streets, Chiosco Giammona offers the city me's famous soda and fresh fruit mixes. It is one of the city's most characteristic points for taking a local break in the summer heat, watching the city's daily rhythm, and tasting the traditional Italian drink culture in its most sincere form."
    },
    "cat_trattoria_salvo_34": {
        "description": "Onlarca yıllık geçmişiyle Catania'nın en sevilen pastanelerinden biri olan Quaranta, Sicilya usulü cannoli ve cassata gibi tatlıların en taze adresidir. Sokağa yayılan mis gibi hamur işi kokularıyla kenti büyüleyen pastane, hem yerel halkın hem de tatlı tutkunu gezginlerin günün her saati uğradığı samimi bir lezzet durağıdır.",
        "description_en": "One of Catania's most beloved bakeries with decades of history, Quaranta is the freshest address for sweets like Sicilian style cannoli and cassata. Enchanting the city with the scents of pastries spreading into the street, the bakery is a sincere flavor stop where both local people and dessert-loving travelers stop by at all hours."
    },
    "cat_trattoria_etnea_35": {
        "description": "Piazza Mazzini'nin tarihi atmosferine hakim olan Bar Mazzini, kentin aristokratik geçmişiyle modern sosyal yaşamını buluşturan keyifli bir duraktır. Sabah güneşinde kahvenizi içip çevredeki tarihi heykelleri izlemek ve kentin kozmopolit ritmini dengelemek için Catania'nın en şık ve havadar adreslerinden biridir.",
        "description_en": "Dominating the historical atmosphere of Piazza Mazzini, Bar Mazzini is a pleasant stop bringing together the city me's aristocratic past with modern social life. It is one of Catania's most stylish and airy addresses to have your coffee in the morning sun, watch the surrounding historical statues, and balance the city me's cosmopolitan rhythm."
    },
    "cat_trattoria_salvo_39": {
        "description": "Catania'nın modern mahallelerinde yer alan bu şık pastane, geleneksel Sicilya tatlılarını modern bir estetikle yeniden yorumluyor. Sanat eseri gibi tasarlanmış pastaları ve uzmanlıkla hazırlanan dondurmalarıyla kentin gastronomi vizyonunu üst seviyeye taşıyan bu mekan, kalite ve lezzet arayan gastronomi tutkunları için idealdir.",
        "description_en": "Located in Catania's modern neighborhoods, this stylish bakery reinterprets traditional Sicilian sweets with a modern aesthetic. Carrying the city me's gastronomic vision to a high level with its cakes designed like artworks and expertly prepared ice creams, this venue is ideal for gastronomy enthusiasts seeking quality and flavor."
    },
    "cat_trattoria_da_turi_41": {
        "description": "Catania'nın meşhur sokak lezzeti Crispelle'nin en otantik adresi olan bu ufak dükkan, kuşaklar boyu devredilen gizli tarifleriyle tanınır. Sıcak ve çıtır hamur içi enfes dolgularla hazırlanan bu yerel atıştırmalık, kentin gastronomi ruhunu en hızlı ve samimi haliyle keşfetmek isteyen her gezginin mutlaka denemesi gereken bir tattır.",
        "description_en": "The most authentic address of Catania's famous street food Crispelle, this small shop is known for its secret recipes passed down through generations. This local snack prepared with exquisite fillings inside hot and crispy dough is a taste every traveler wanting to explore the city me's gastronomic spirit in its fastest and most sincere form must try."
    },
    "cat_trattoria_sikulo_43": {
        "description": "Catania'nın dar ve tarihi sokaklarında bir zaman yolculuğu vadeden Trattoria Serafino, en taze yerel ürünlerle hazırlanan 'Pasta alla Norma' gibi klasikleriyle ünlüdür. Adeta bir Sicilya evine davetliymişsiniz gibi hissettiren samimi atmosferi ve anne eli değmiş lezzetleriyle, kentin gerçek mutfak mirasını deneyimlemek için kusursuzdur.",
        "description_en": "Promising a time travel in Catania's narrow and historical streets, Trattoria Serafino is famous for classics like 'Pasta alla Norma' prepared with the freshest local products. It is perfect for experiencing the city me's real culinary heritage with its sincere atmosphere making you feel as if invited to a Sicilian home and flavors touched by a mother's hand."
    },
    "cat_trattoria_salvo_44": {
        "description": "Modern Catania gastronomisinin iddialı temsilcilerinden Bavetta, geleneksel ile fütüristik anlayışı birleştiren şık bir restorandır. Seçkin şarap mönüsü ve Sicilya'nın bereketli topraklarından gelen ürünlerin sanatsal sunumuyla, kentin kozmopolit ruhunu kaliteli bir akşam yemeği eşliğinde yaşamak isteyenlerin favorisidir.",
        "description_en": "One of the ambitious representatives of modern Catania gastronomy, Bavetta is a stylish restaurant combining traditional and futuristic concepts. With an exclusive wine menu and artistic presentation of products coming from Sicily me's fertile lands, it is a favorite for those wanting to experience the city me's cosmopolitan spirit accompanied by a high-quality dinner."
    },
    "cat_trattoria_da_turi_46": {
        "description": "Catania'nın ilk Michelin yıldızlı restoranı olan Sapio, kentin gastronomi vizyonunu evrensel bir seviyeye taşıyor. Şık mönüleri, minimalist tasarımı ve Sicilya lezzetlerini moleküler ve estetik bir dille yeniden anlatan şefleriyle, kentsel lüksü ve mutfak sanatını bir araya getiren olağanüstü ve prestijli bir duraktır.",
        "description_en": "Catania me's first Michelin-starred restaurant, Sapio, carries the city me's gastronomic vision to a universal level. With its stylish menus, minimalist design, and chefs re-telling Sicilian flavors in a molecular and aesthetic language, it is an extraordinary and prestigious stop bringing together urban luxury and culinary art."
    },
    "cat_trattoria_sikulo_53": {
        "description": "Kentin tarihi merkezinde yer alan Gisira, klasik İtalyan pizzasını Sicilya'nın yerel malzemeleriyle taçlandıran modern bir pizzacıdır. Taş fırından çıkan çıtır pizzaları ve kentin kozmopolit neşesini yansıtan havadar iç tasarımıyla, hem hızlı hem de kaliteli bir öğün arayan modern gezginlerin adresi haline gelmiştir.",
        "description_en": "Located in the city's historical center, Gisira is a modern pizzeria crowning classic Italian pizza with local Sicilian ingredients. With crispy pizzas from the stone oven and an airy interior design reflecting the city me's cosmopolitan joy, it has become the address for modern travelers seeking both a fast and high-quality meal."
    },
    "cat_trattoria_salvo_54": {
        "description": "U Fichera, Catania'nın pazar mahallelerindeki samimi meyhane kültürünü yaşatan, adı yerel lezzetlerle özdeşleşmiş efsanevi bir duraktır. Izgara et kokularının sokağa taştığı, kentin gerçek ve filtresiz sosyal dokusuyla tanışabileceğiniz bu mekan, İbiza'nın enerjisini Sicilya'nın gelenekleriyle buluşturan neşeli bir keşiştir.",
        "description_en": "U Fichera is a legendary stop associated with local flavors, keeping the sincere tavern culture alive in Catania's market neighborhoods. This venue where the scent of grilled meat spills into the street and you can meet the city me's real and unfiltered social texture, is a joyful discovery bringing together Ibiza's energy with Sicilian traditions."
    },
    "cat_trattoria_etnea_55": {
        "description": "Kentin katedral meydanına (Piazza Duomo) ev sahipliği yapan Prestipino, Catania'nın en zarif bar-pastane duraklarından biri kabul edilir. Heybetli barok binaların gölgesinde, kentin asaletini taze kahveler ve sanatsal pastalarla dengeleyebileceğiniz, kentin aristokratik ruhunu solumak için ideal ve iddialı bir duraktır.",
        "description_en": "Hosting the city's cathedral square (Piazza Duomo), Prestipino is considered one of Catania's most elegant bar-bakery stops. It is an ideal and ambitious stop for breathing in the city me's aristocratic spirit, where you can balance the city's nobility with fresh coffees and artistic pastries in the shadow of imposing baroque buildings."
    },
    "cat_trattoria_u_fichera_": {
        "description": "Catania'nın her köşesinde hissedilen bu yerel lezzet adı, kentin mutfak mirasının bir sembolüdür. Taze mezeleri, samimi servisi ve adanın her daim sıcak olan sosyal duraklarına yaptığı vurguyla kentin gerçek gastronomi ruhunu yaşatan bu bölge, yerel yaşamı keşfetmek isteyenler için havadar ve samimi bir odak noktasıdır.",
        "description_en": "This local flavor name felt in every corner of Catania is a symbol of the city me's culinary heritage. This area keeping the city me's real gastronomic spirit alive with fresh mezes, sincere service, and emphasis on the island's always warm social stops is an airy and sincere focal point for those wanting to explore local life."
    },
    "cat_trattoria_sikulo_63": {
        "description": "Palazzo Biscari'nin büyüleyici iç mekanları, Catania Barok mimarisinin en süslü ve görkemli duraklarından biri olarak kentin aristokratik ihtişamını yansıtır. Aynalarla kaplı balo salonu, detaylı freskleri ve kentin tarihsel asaletini bir mücevher gibi saklayan yapısıyla, tarihin ihtişamına tanıklık edebileceğiniz muazzam bir mirastır.",
        "description_en": "The fascinating interiors of Palazzo Biscari reflect the city me's aristocratic grandeur as one of the most ornate and grand stops of Catania Baroque architecture. With its ballroom covered in mirrors, detailed frescoes, and structure preserving the city me's historical nobility like a jewel, it is a magnificent heritage where you can witness the grandeur of history."
    },
    "cat_trattoria_etnea_65": {
        "description": "Piazza Duomo'nun altında saklı kalan Achillean Hamamları, kentin Roma dönemine ait termal kültürünü ve mühendislik zekasını sergiliyor. Sular altındaki mistik atmosferi ve antik sütun kalıntılarıyla kentin görülmeyen derinliklerine açılan bu kapı, Catania'nın binlerce yıllık kentsel katmanlarını anlamak için paha biçilemez bir keşiftir.",
        "description_en": "The Achillean Baths hidden under Piazza Duomo exhibit the city me's Roman period thermal culture and engineering intelligence. This gateway opening to the city me's unseen depths with its mystical atmosphere underwater and ancient column remains is a priceless discovery to understand Catania me's thousand-year urban layers."
    },
    "cat_trattoria_sikulo_68": {
        "description": "Via Crociferi, geç akşamüstü güneşinin sarı taş binalarda yarattığı büyüyle kentin en mistik ve sessiz sokaklarından biri haline gelir. Barok kiliselerin arasından süzülürken kentin dinsel mirasını ve asude geçmişini hissedebileceğiniz, hem romantik hem de tarihi bir atmosfer arayan gezginler için havadar bir duraktır.",
        "description_en": "Via Crociferi becomes one of the city's most mystical and quiet streets with the magic the late afternoon sun creates on its yellow stone buildings. It is an airy stop for travelers seeking both a romantic and historical atmosphere, where you can feel the city's religious heritage and serene past while gliding through Baroque churches."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/catania.json.draft'
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

print(f"✅ Catania Part 1: Enriched {count} items.")
