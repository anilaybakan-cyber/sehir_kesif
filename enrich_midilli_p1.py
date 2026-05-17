#!/usr/bin/env python3
import json

updates = {
    "Sigri": {
        "description": "Midilli'nin en uç batı ucunda yer alan Sigri, sakin atmosferi, volkanik kayalıkları ve dünyanın nadir doğal oluşumlarından biri olan Taşlaşmış Orman'a olan yakınlığı ile bilinir. Kristal berraklığındaki koyları ve rüzgarlı kıyılarıyla hem doğa aşıkları hem de huzur arayanlar için saklı bir cennettir.",
        "description_en": "Located at the Westernmost tip of Lesbos, Sigri is known for its serene atmosphere, volcanic rocks, and its proximity to the world-rare Petrified Forest. With its crystal-clear bays and windy shores, it is a hidden paradise for both nature lovers and those seeking peacefulness."
    },
    "Eressos Plajı": {
        "description": "Adanın en ünlü ve uzun kumsallarından biri olan Skala Eressos, ince volkanik kumu ve berrak deniziyle her yıl binlerce turisti ağırlar. Bohem bir yaşam tarzına sahip olan bu bölge, sahil boyu dizili kafeleri, gün batımı manzaraları ve canlı gece hayatıyla adanın en popüler duraklarından biridir.",
        "description_en": "One of the most famous long sandy beaches on the island, Skala Eressos welcomes thousands of tourists every year with its fine volcanic sand and clear waters. Known for its bohemian lifestyle, this area is a popular stop with its beachside cafes, sunset views, and vibrant nightlife."
    },
    "Vatera Plajı": {
        "description": "Midilli'nin güneyinde 8 kilometre boyunca uzanan Vatera, adanın en büyük ve en geniş plajıdır. Dev dalgalardan uzak, huzurlu denizi ve serinletici çam ormanlarıyla çevrili yapısı sayesinde aileler için mükemmel bir plaj günü sunar.",
        "description_en": "Stretching for 8 kilometers in the south of Lesbos, Vatera is the island's largest and widest beach. Its peaceful sea, away from giant waves, and its surroundings framed by cooling pine forests offer the perfect beach day for families."
    },
    "Kadınlar Kooperatifi (Petra)": {
        "description": "Petra köyünün kalbinde yer alan bu kooperatif, geleneksel Midilli mutfağını ve el sanatlarını yaşatmak isteyen kadınlar tarafından kurulmuştur. Ev yapımı reçeller, yerel peynirler ve el işi hediyeliklerin bulunduğu bu mekan, yerel kültürü desteklemek ve otantik tatlara ulaşmak için idealdir.",
        "description_en": "Located in the heart of Petra village, this cooperative was founded by women who wish to preserve traditional Lesbos cuisine and handicrafts. Featuring homemade jams, local cheeses, and handcrafted gifts, it's the ideal place to support local culture and taste authentic flavors."
    },
    "Vafios Taverna": {
        "description": "Geleneksel Midilli lezzetlerini en doğal haliyle sunan Vafios Taverna, adanın kuzeyinde meşhur kuzu eti yemekleri ve zeytinyağlı mezeleriyle adından söz ettirir. Köy mimarisine uygun sıcak atmosferi ve muhteşem vadi manzarasıyla akşam yemeklerinin en unutulmaz adreslerinden biridir.",
        "description_en": "Presenting traditional Lesbos flavors in their most natural form, Vafios Taverna is famous in the north for its lamb dishes and olive oil mezes. With its warm village-style atmosphere and magnificent valley views, it is one of the most unforgettable addresses for dinner."
    },
    "Ouzadiko Baboukos": {
        "description": "Molyvos Limanı'nda yer alan Baboukos, adanın en ünlü uzo ve balık adreslerinden biridir. Günlük tutulan taze deniz ürünleri, Midilli'ye özgü uzo çeşitleri ve denizin hemen dibindeki masalarıyla gerçek bir Yunan adası akşamı vadediyor.",
        "description_en": "Situated at Molyvos Harbor, Baboukos is one of the island's most famous ouzo and fish spots. With daily fresh seafood catch, a wide range of Lesbos-native ouzo, and tables right by the water, it promises an authentic Greek island evening."
    },
    "Tsalikis": {
        "description": "Skala Kalloni bölgesinde deniz ürünleri konusunda uzmanlaşmış olan Tsalikis, özellikle bölgenin meşhur sardalyasıyla tanınır. Aile işletmesi sıcaklığı ve taze malzemelerle hazırlanan zengin menüsüyle hem yerel halkın hem de turistlerin favori restoranlarından biridir.",
        "description_en": "Specializing in seafood in the Skala Kalloni area, Tsalikis is particularly renowned for the region's famous sardines. With the warmth of a family-run business and a rich menu prepared with fresh ingredients, it is a favorite for both locals and tourists."
    },
    "Gorgona": {
        "description": "Skala Skamnias'ın büyüleyici limanında yer alan Gorgona, denize sıfır konumu ve otantik Yunan mezeleriyle huzuru sofranıza getiriyor. Ağaçların altındaki masaları ve muhteşem Ege manzarasıyla, yavaş ve keyifli bir ada öğle yemeği için mükemmeldir.",
        "description_en": "Located in the charming harbor of Skala Skamnias, Gorgona brings tranquility to your table with its seafront position and authentic Greek mezes. With tables under the trees and magnificent Aegean views, it is perfect for a slow and enjoyable island lunch."
    },
    "Be Happy": {
        "description": "Petra'nın kalabalığından uzak, serin bir mola vermek isteyenler için harika bir kafe olan Be Happy, taze kahveleri ve ev yapımı tatlılarıyla bilinir. Güler yüzlü servisi ve samimi dekorasyonuyla gün ortasında enerji toplamak için uğranması gereken noktalardan biridir.",
        "description_en": "Away from Petra's crowds, Be Happy is a great cafe for those seeking a cool break, known for its fresh coffees and homemade desserts. With friendly service and intimate decor, it is one must-visit spot to recharge in the middle of the day."
    },
    "Parasol Beach Bar": {
        "description": "Skala Eressos plajının enerjik duraklarından biri olan Parasol, bohem tasarımı ve yenilikçi kokteylleriyle plaj keyfini katlar. Canlı müzik performansları ve dinlendirici localarıyla gün boyu güneşlenip akşamüstü partilerine katılmak için idealdir.",
        "description_en": "One of the energetic stops at Skala Eressos beach, Parasol enhances beach enjoyment with its bohemian design and innovative cocktails. It's ideal for sunbathing during the day and joining sunset parties followed by live music performances."
    },
    "Theophilos Müzesi": {
        "description": "Ünlü Yunan naif ressamı Theophilos Hatzimihail'in eserlerine ev sahipliği yapan bu müze, adanın kültürel mirasını anlamak isteyenler için bir hazinedir. Ressamın yaşamı boyunca yaptığı duvar resimleri ve tablolar, Midilli'nin tarihini ve günlük yaşamını renkli bir perspektifle sunar.",
        "description_en": "Hosting the works of famous Greek naive painter Theophilos Hatzimihail, this museum is a treasure for those wanting to understand the island's cultural heritage. The murals and paintings created by the artist during his life present the history and daily life of Lesbos from a colorful perspective."
    },
    "Sappho Meydanı": {
        "description": "Midilli şehrinin merkezi olan bu meydan, antik çağın ünlü şairi Sappho'nun adını taşır. Liman manzarası, çevresindeki tarihi binalar ve heykellerle şehrin sosyal yaşamının nabzının attığı, buluşma ve yürüyüşlerin ana noktasıdır.",
        "description_en": "The central square of Mytilene city, this square is named after the famous ancient poet Sappho. With harbor views, surrounding historical buildings, and statues, it is the main point for social meetings and strolls, where the pulse of city life beats."
    },
    "Özgürlük Heykeli": {
        "description": "Midilli Limanı'nın girişinde gururla yükselen bu anıt, Yunan direncinin ve özgürlüğünün bir simgesidir. New York'taki örnekle benzerlik gösteren bu yapı, limana yanaşan tekneleri karşılayan etkileyici bir silüet oluşturur.",
        "description_en": "Proudly rising at the entrance of Mytilene Harbor, this monument is a symbol of Greek resistance and freedom. Showing similarities to the New York version, it creates an impressive silhouette welcoming boats arriving at the harbor."
    },
    "Molyvos Limanı": {
        "description": "Renkli teknelerin ve kıyıya dizili balıkçı restoranlarının bulunduğu Molyvos Limanı, adanın en fotojenik yerlerinden biridir. Kışın sakin, yazın ise cıvıl cıvıl olan bu liman, kalesinden süzülen tarihi gölgeler altında akşam yürüyüşleri için büyüleyicidir.",
        "description_en": "Molyvos Harbor, with its colorful boats and seaside fish restaurants, is one of the most photogenic places on the island. Calm in winter and lively in summer, it is enchanting for evening strolls under the historic shadows falling from the castle."
    },
    "Eftalou Plajı": {
        "description": "Termal kaynaklarıyla ünlü olan Eftalou Plajı, kristal berrak suları ve sakin atmosferiyle huzur arayanların tercihidir. Doğal sıcak su havuzları ve kıyıdaki çakıl taşlarıyla adada farklı ve yenileyici bir deniz deneyimi sunar.",
        "description_en": "Famous for its thermal springs, Eftalou Beach is preferred by those seeking serenity with its crystal-clear waters and calm atmosphere. With natural hot spring pools and pebbles along the shore, it offers a different and refreshing beach experience on the island."
    },
    "Molyvos Çarşısı": {
        "description": "Geleneksel taş evler arasında kıvrılan Arnavut kaldırımlı sokaklardan oluşan Molyvos Çarşısı, yerel sanatçıların atölyeleri ve hediyelik dükkanlarıyla doludur. Mor salkımlı çiçeklerin sarktığı bu dar sokaklarda gezinmek, adanın kendine has estetiğini hissetmek için birebirdir.",
        "description_en": "The Molyvos Market, consisting of cobbled streets winding between traditional stone houses, is filled with local artist workshops and souvenir shops. Strolling through these narrow streets draped with wisteria is perfect for feeling the island's unique aesthetic."
    },
    "Congas Beach Bar": {
        "description": "Molyvos sahilinde palmiye ağaçları arasında gizlenen Congas, egzotik kokteylleri ve tropik müzikleriyle ünlü bir plaj barıdır. Rahat şezlongları ve samimi servisiyle kendinizi bir ada masalında gibi hissettiren popüler bir eğlence noktasıdır.",
        "description_en": "Hidden among palm trees on Molyvos beach, Congas is a beach bar famous for its exotic cocktails and tropical music. With relaxed loungers and friendly service, it's a popular spot that makes you feel like you're in an island fairytale."
    },
    "Tropicana Platanos": {
        "description": "Molyvos Meydanı'nda devasa bir çınar ağacının gölgesinde yer alan bu mekan, gün boyu serinletici içecekleri ve akşamüstü kokteylleriyle bilinir. Geleneksel ile modernin buluştuğu bu durak, yerel halkın ve turistlerin en sevdiği sosyal merkezlerden biridir.",
        "description_en": "Located under the shadow of a massive plane tree in Molyvos Square, this venue is known for its refreshing drinks during the day and sunset cocktails. This stop, where tradition meets modernity, is one of the favorite social hubs for both locals and tourists."
    },
    "Le Grand Bleu": {
        "description": "Molyvos manzarasına hakim bir noktada yer alan Le Grand Bleu, yaratıcı Akdeniz mutfağı ve şık atmosferiyle öne çıkan bir restorandır. Özellikle gün batımı saatlerinde vadiye ve denize bakan terasında romantik akşam yemekleri için mükemmel bir seçenektir.",
        "description_en": "Commanding a view of Molyvos, Le Grand Bleu is a restaurant standing out with its creative Mediterranean cuisine and chic atmosphere. It is a perfect choice for romantic dinners on its terrace overlooking the valley and sea, especially at sunset."
    },
    "Platanos Meydanı, Plomari": {
        "description": "Plomari köyünün merkezindeki bu küçük meydan, ortasındaki tarihi çınar ağacıyla köy yaşamının kalbidir. Çevresindeki kafelerde oturanların uzo yanındaki mezelerle akşamın tadını çıkardığı, samimiyet dolu tipik bir Yunan meydanıdır.",
        "description_en": "This small square in the center of Plomari village is the heart of village life with its historic plane tree in the middle. It is a typical Greek square full of sincerity, where those sitting in surrounding cafes enjoy the evening with ouzo and mezes."
    },
    "Taverna 7 Thalasses": {
        "description": "Mytilene Limanı'nda yer alan 7 Thalasses, taze balık ve yaratıcı deniz ürünleri sunumlarıyla adanın en prestijli lokantalarından biridir. Dalgaların hemen yanında, kaliteli servis ve zengin şarap mönüsü eşliğinde seçkin bir akşam yemeği deneyimi sunar.",
        "description_en": "Located at Mytilene Harbor, 7 Thalasses is one of the island's most prestigious eateries with its fresh fish and creative seafood presentations. It offers an elite dinner experience by the waves, accompanied by quality service and a rich wine menu."
    },
    "Ambelikos Traditional Guesthouse": {
        "description": "Adanın iç kısımlarında, huzur dolu bir vadiye karşı yer alan bu konukevi, geleneksel mimari ve modern konforun harika bir örneğidir. Şehir gürültüsünden uzaklaşmak ve Midilli'nin doğasını derinden hissetmek isteyen gezginler için dingin bir sığınaktır.",
        "description_en": "Located in the island's interior facing a peaceful valley, this guesthouse is a wonderful example of traditional architecture and modern comfort. It is a serene sanctuary for travelers wanting to escape city noise and deeply feel the nature of Lesbos."
    },
    "Melinda Plajı": {
        "description": "Plomari yakınlarındaki bu el değmemiş plaj, sarp kayalıkları ve cam gibi berrak sularıyla tanınır. Kalabalıktan uzak kalmak, doğal oluşumlu mağaraların yanında yüzmek ve huzur dolu bir gün geçirmek isteyenlerin gizli favorisidir.",
        "description_en": "This untouched beach near Plomari is known for its steep cliffs and glass-clear waters. It is a hidden favorite for those wanting to stay away from crowds, swim near natural caves, and spend a peaceful day."
    },
    "Anaxos Plajı": {
        "description": "Adanın kuzeyinde yer alan ve masmavi sularıyla bilinen Anaxos, hem geniş plaj alanı hem de çevresindeki lezzetli tavernalarıyla bilinir. Çocuklar için uygun park alanları ve sığ deniziyle turistik ama son derece konforlu bir yaz mekanıdır.",
        "description_en": "Located in the north of the island and known for its deep blue waters, Anaxos is famous for its wide beach area and surrounding delicious tavernas. With playgrounds suitable for children and shallow sea, it's a touristic yet highly comfortable summer destination."
    },
    "Kantina": {
        "description": "Adanın en uç noktalarındaki ıssız yollarda bir vaha gibi beliren Kantina, basit ama taze atıştırmalıkları ve serinletici içecekleriyle meşhurdur. Yol üzerindeki bu küçük durak, Midilli'nin keşfedilmemiş yollarında maceraya atılanlar için kurtarıcı bir lezzet noktasıdır.",
        "description_en": "Appearing like an oasis on deserted roads at the island's farthest points, Kantina is famous for its simple yet fresh snacks and refreshing drinks. This small roadside stop is a lifesaver food spot for those venturing on Lesbos' undiscovered roads."
    },
    "Thalassa Restaurant": {
        "description": "Molyvos kıyılarında denizin üzerinde bir balkonu andıran konumuyla Thalassa, taze deniz mahsulleri ve otantik Yunan tatlarını bir araya getiriyor. Akşam üstü vuran dalga sesleri ve lamba ışıkları altında, adanın romantik ruhunu sofraya taşıyan bir mekandır.",
        "description_en": "Resembling a balcony over the water on Molyvos shores, Thalassa brings together fresh seafood and authentic Greek tastes. It is a venue that brings the island's romantic spirit to the table under lamp lights and the sound of sunset waves."
    },
    "Avlaki Plajı": {
        "description": "Petra yakınlarındaki Avlaki, küçük koyu ve şeffaf sularıyla adanın saklı incilerinden biridir. Ziyaretçilerine huzur dolu bir yüzme keyfi sunan bu plaj, çevresindeki ağaçlar ve sessizliğiyle tam bir kaçış noktasıdır.",
        "description_en": "Avlaki near Petra is one of the island's hidden gems with its small bay and transparent waters. Offering a peaceful swimming delight to visitors, this beach is a complete escape point with its surrounding trees and silence."
    },
    "Reef Bar": {
        "description": "Skala Eressos sahilindeki modern ve şık tasarımıyla dikkat çeken Reef Bar, yaratıcı barmenleri ve chill-out müzikleriyle bilinir. Gecenin ilerleyen saatlerinde canlanan enerjisiyle adanın genç ve dinamik kitlesinin en sevdiği buluşma noktalarından biridir.",
        "description_en": "Standing out with its modern and chic design on Skala Eressos coast, Reef Bar is known for its creative bartenders and chill-out music. With an energy that picks up late at night, it is one of the favorite meeting points for the island's young and dynamic crowd."
    },
    "Sigri Limanı": {
        "description": "Adanın en batısındaki bu sessiz liman, taze balık teknelerinin sığındığı ve bozulmamış köy yaşamının devam ettiği bir yerdir. Çevresindeki küçük tavernalarda denizden yeni çıkmış ürünleri tadarken, güneşin engin Ege üzerinde batışını sessizce izleyebilirsiniz.",
        "description_en": "This quiet harbor at the farthest west of the island is a place where fresh fish boats shelter and unspoiled village life continues. While tasting fresh catch at nearby small tavernas, you can silently watch the sun set over the vast Aegean."
    },
    "Pusula (Fanari)": {
        "description": "Midilli Limanı'nın girişinde, denize hakim bir noktada yer alan Fanari, muazzam kale manzarası ve kaliteli hizmetiyle bir klasik haline gelmiştir. Hafif rüzgar eşliğinde kaliteli kahvenizi yudumlamak veya akşam içkilerini yudumlamak için şehrin en nezih sahil kafesidir.",
        "description_en": "Located at the entrance of Mytilene Harbor with a commanding view of the sea, Fanari has become a classic with its magnificent castle view and quality service. It's the city's most refined seaside cafe to sip quality coffee or evening drinks accompanied by a gentle breeze."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/midilli.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data.get('highlights', []):
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Midilli Part 1: Enriched {count} items.")
