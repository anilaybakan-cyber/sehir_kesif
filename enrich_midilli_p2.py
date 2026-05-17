#!/usr/bin/env python3
import json

updates = {
    "Ligona Vadisi": {
        "description": "Midilli'nin gizli doğa harikalarından biri olan Ligona Vadisi, terk edilmiş su değirmenleri ve süzülen şelaleleriyle masalsı bir atmosfer sunar. Yürüyüş tutkunları için ideal olan bu vadi, zengin bitki örtüsü ve kuş sesleri eşliğinde adanın vahşi doğasını keşfetmek isteyenler için eşsizdir.",
        "description_en": "One of the hidden natural wonders of Lesbos, Ligona Valley offers a fairytale atmosphere with its abandoned watermills and cascading waterfalls. Ideal for hiking enthusiasts, this valley is unique for those wanting to explore the island's wild nature accompanied by rich flora and birdsong."
    },
    "Monkey Bar": {
        "description": "Skala Eressos'un en popüler eğlence noktalarından biri olan Monkey Bar, renkli kokteylleri ve sahil kenarındaki rahat atmosferiyle bilinir. Özellikle akşamüstü saatlerinde başlayan canlı müzik ve DJ performanslarıyla adanın bohem ruhunu en iyi yansıtan mekanlardan biridir.",
        "description_en": "One of the most popular entertainment spots in Skala Eressos, Monkey Bar is known for its colorful cocktails and relaxed seaside atmosphere. It is one of the venues that best reflects the island's bohemian spirit, especially with live music and DJ performances starting in the late afternoon."
    },
    "Home Bar": {
        "description": "Mytilene merkezinde yer alan Home Bar, şık dekorasyonu ve kaliteli müzik seçkisiyle şehrin elit buluşma noktalarından biridir. Geniş içki mönüsü ve samimi ortamıyla, özellikle hafta sonları yerel gençlerin ve gezginlerin tercih ettiği popüler bir mekandır.",
        "description_en": "Located in the center of Mytilene, Home Bar is one of the city's elite meeting points with its chic decoration and quality music selection. With its wide drink menu and intimate atmosphere, it is a popular venue preferred by local youth and travelers, especially on weekends."
    },
    "Fiseye": {
        "description": "Petra sahilinde modern bir dokunuş sunan Fiseye, panoramik deniz manzarası ve yenilikçi aperatifleriyle bilinir. Gün batımını izlemek için mükemmel bir konumda olan bu mekan, taze içecekleri ve huzurlu ortamıyla ziyaretçilerine keyifli bir mola imkanı sunar.",
        "description_en": "Offering a modern touch on Petra coast, Fiseye is known for its panoramic sea views and innovative appetizers. Perfectly positioned for watching the sunset, this venue offers visitors a pleasant break with its fresh drinks and peaceful environment."
    },
    "Mousiko Kafenio (Mytilene)": {
        "description": "Mytilene'nin tarihi ara sokaklarında yer alan bu geleneksel kafe, adanın eski kahvehane kültürünü canlı tutuyor. Ahşap masaları, nostaljik dekoru ve sıkça düzenlenen canlı Yunan müziği akşamlarıyla adanın otantik ve samimi ruhunu hissetmek için harika bir yerdir.",
        "description_en": "Located in the historical side streets of Mytilene, this traditional cafe keeps the island's old coffee house culture alive. With its wooden tables, nostalgic decor, and frequently organized live Greek music evenings, it is a great place to feel the island's authentic and intimate spirit."
    },
    "Oxos Bar": {
        "description": "Molyvos'un en karakteristik mekanlarından biri olan Oxos Bar, denize hakim bir noktada, sarp kayalıkların üzerine kurulu terasıyla dikkat çeker. Özellikle akşamüstü saatlerinde hafif rüzgar eşliğinde sunulan serinletici kokteylleri ve muazzam manzarasıyla adanın en romantik duraklarındandır.",
        "description_en": "One of the most characteristic venues in Molyvos, Oxos Bar stands out with its terrace built on steep cliffs overlooking the sea. It's one of the island's most romantic stops, especially with its refreshing cocktails offered during late afternoon hours accompanied by a gentle breeze and magnificent views."
    },
    "Sto Nisi": {
        "description": "Midilli Mutfağının en taze deniz ürünlerini sunan Sto Nisi, geleneksel tarifleri modern sunumlarla birleştiriyor. Yerel uzo çeşitleri ve güler yüzlü hizmetiyle liman kenarında keyifli ve lezzet dolu bir akşam yemeği deneyimi vadediyor.",
        "description_en": "Presenting the freshest seafood of Lesbos cuisine, Sto Nisi combines traditional recipes with modern presentations. It promises a pleasant and flavor-filled dinner experience by the harbor with local ouzo varieties and friendly service."
    },
    "Panellinion": {
        "description": "Mytilene'nin en görkemli tarihi kafelerinden biri olan Panellinion, adanın zengin geçmişini yansıtan aristokratik bir havaya sahiptir. Yüksek tavanları ve klasik mermer masalarıyla, hem sabah kahvenizi içmek hem de şehrin tarihi dokusunu solumak için adanın en ikonik mekanlarından biridir.",
        "description_en": "One of Mytilene's most magnificent historic cafes, Panellinion has an aristocratic air reflecting the island's rich past. With its high ceilings and classic marble tables, it is one of the island's most iconic spots for both having morning coffee and breathing in the city's historical texture."
    },
    "Kambos Plajı": {
        "description": "Sigri yakınlarında yer alan Kambos Plajı, sakin denizi ve geniş kumsalıyla huzur arayanların uğrak yeridir. Doğal yapısı korunmuş olan bu plaj, şehir kalabalığından uzakta gün boyu güneşlenmek ve berrak sularda yüzmek isteyenler için mükemmel bir sessizlik sunar.",
        "description_en": "Located near Sigri, Kambos Beach is a frequent spot for those seeking peace with its calm sea and wide sandy beach. Preserved in its natural state, this beach offers perfect silence for those wanting to sunbathe all day and swim in clear waters away from city crowds."
    },
    "Drota Plajı": {
        "description": "Midilli'nin güney kıyılarının saklı mücevheri Drota, sarp dağların denize kavuştuğu bir noktada yer alır. Kristal berraklığında denizi ve çevresindeki birkaç küçük taze balık lokantasıyla adanın en bakir ve otantik deniz kaçamaklarından birini vadeder.",
        "description_en": "The hidden gem of Lesbos' southern shores, Drota is located where steep mountains meet the sea. With its crystal-clear waters and a few small fresh fish eateries nearby, it promises one of the island's most pristine and authentic sea escapes."
    },
    "Ambelia Plajı": {
        "description": "Petra ve Anaxos arasında kalan Ambelia Plajı, ince kumu ve sığ deniziyle bilinir. Daha çok yerel halkın tercih ettiği bu sessiz plaj, çocuklu aileler için güvenli bir yüzme alanı sunarken, huzurlu bir kitap okuma günü için de oldukça uygundur.",
        "description_en": "Situated between Petra and Anaxos, Ambelia Beach is known for its fine sand and shallow waters. Preferred mostly by locals, this quiet beach offers a safe swimming area for families with children and is also very suitable for a peaceful day of reading a book."
    },
    "Xampelia": {
        "description": "Doğa ve gastronominin buluştuğu Xampelia, adanın iç kısımlarında yer alan bir vaha gibidir. Geleneksel Midilli mezelerinin en taze hallerini sunan bu mekan, özellikle zeytin ağaçları gölgesindeki masalarıyla adanın huzur verici kırsal yaşamını sofranıza taşır.",
        "description_en": "Where nature and gastronomy meet, Xampelia is like an oasis located in the island's interior. Presenting the freshest versions of traditional Lesbos mezes, this venue brings the island's soothing rural life to your table, especially with its tables under the shade of olive trees."
    },
    "Tsichranta": {
        "description": "Adanın kuzeyinde yer alan Tsichranta, sakin koyu ve berrak sularıyla bilinir. Çevresindeki birkaç küçük pansiyon ve tavernasıyla, adanın turistik olmayan bölgelerinde gerçek bir Yunan adası yaşamı deneyimlemek isteyen gezginler için harika bir duraktır.",
        "description_en": "Located in the north of the island, Tsichranta is known for its calm bay and clear waters. With a few small guest houses and tavernas nearby, it's a great stop for travelers wanting to experience authentic Greek island life in the non-touristic parts of the island."
    },
    "Stelios Stamatis Çömlek Atölyesi": {
        "description": "Mantamados köyünün meşhur çömlekçilik geleneğini sürdüren bu atölye, el emeği ve sanatın buluştuğu bir duraktır. Geleneksel formların modern sanatla harmanlandığı eserleri görebilir, usta sanatçıların çamuru şekillendirişini yerinde izleyerek adanın zanaat mirasına tanıklık edebilirsiniz.",
        "description_en": "Continuing the famous pottery tradition of Mantamados village, this workshop is a stop where manual labor and art meet. You can see works where traditional forms are blended with modern art and witness the island's craft heritage by watching master artists shape clay on-site."
    },
    "Eirini Plomariou": {
        "description": "Plomari merkezinde yer alan bu şirin mekan, adanın en iyi ev yemeklerini ve el yapımı tatlılarını sunmasıyla bilinir. Sıcak bir aile işletmesi olan Eirini, samimi servisi ve geleneksel Midilli misafirperverliğiyle adada kendinizi evinizde hissetmenizi sağlayan nadir duraklardan biridir.",
        "description_en": "Located in the center of Plomari, this charming venue is known for offering the island's best home-cooked meals and handmade desserts. A warm family-run business, Eirini is one of the rare stops that makes you feel at home with its intimate service and traditional Lesbos hospitality."
    },
    "Achivadolimni": {
        "description": "Adanın en ilginç doğal oluşumlarından biri olan Achivadolimni, deniz ile bağlantılı küçük bir lagündür. Sessizliği ve içindeki çeşitli deniz canlılarıyla doğa gözlemcileri ve huzur arayanlar için saklı bir keşif noktası olup, adanın az bilinen güzelliklerinden biridir.",
        "description_en": "One of the most interesting natural formations on the island, Achivadolimni is a small lagoon connected to the sea. It's a hidden discovery point for nature observers and peace seekers with its silence and various marine species, being one of the island's lesser-known beauties."
    },
    "Pammegistoi Taxiarches (Mantamados)": {
        "description": "Midilli'nin en kutsal yerlerinden biri kabul edilen bu tarihi manastır, mucizevi olduğuna inanılan ve çamurdan yapılmış Taxiarchis ikonuna ev sahipliği yapar. Hem dini önemi hem de huzur verici avlusu ve ünlü ballı yoğurduyla adanın en çok ziyaret edilen ruhani merkezlerinden biridir.",
        "description_en": "Considered one of the most sacred places on Lesbos, this historic monastery houses the Taxiarchis icon, believed to be miraculous and made of mud. It is one of the island's most visited spiritual centers for both its religious significance and its soothing courtyard and famous honey yogurt."
    },
    "Tsamakia Plajı": {
        "description": "Mytilene şehir merkezine en yakın plajlardan biri olan Tsamakia, hem konumu hem de sunduğu tesislerle günlük bir deniz sefası için idealdir. Çam ağaçlarının altındaki gölgelik alanları ve kristal berraklığındaki sularıyla, şehirde kalırken mola vermek isteyenlerin favori duraklarından biridir.",
        "description_en": "One of the beaches closest to Mytilene city center, Tsamakia is ideal for a daily sea outing both because of its location and the facilities it offers. With shaded areas under pine trees and crystal-clear waters, it's a favorite stop for those wanting a break while staying in the city."
    },
    "Lighthouse of Mytilene": {
        "description": "Midilli Limanı'nın girişinde tarihi surların üzerinde yer alan bu zarif deniz feneri, adanın denizcilik geçmişinin simgelerinden biridir. Özellikle akşam saatlerinde limana giren teknelerle harika bir manzara sunan fener, şehrin silüetine nostaljik ve romantik bir hava katmaktadır.",
        "description_en": "Located on historical walls at the entrance of Mytilene Harbor, this elegant lighthouse is one of the symbols of the island's maritime history. Offering a great view with boats entering the harbor especially in the evenings, it adds a nostalgic and romantic air to the city's silhouette."
    },
    "Neon Kydonion": {
        "description": "Adanın doğu kıyısında yer alan bu şirin sahil yerleşimi, geleneksel taş evleri ve huzurlu limanıyla bilinir. Kalabalıktan uzak, sessiz tavernalarında taze deniz ürünlerinin tadına bakabileceğiniz ve adanın yerel yaşamına tanıklık edebileceğiniz dingin bir duraktır.",
        "description_en": "Located on the east coast of the island, this charming coastal settlement is known for its traditional stone houses and peaceful harbor. It is a serene stop away from crowds, where you can taste fresh seafood in quiet tavernas and witness the island's local life."
    },
    "Octopus Restaurant": {
        "description": "Molyvos Limanı'nda denizin hemen kıyısında yer alan Octopus, taze ahtapot ızgaraları ve yaratıcı deniz ürünleri mezeleriyle tanınır. Gün batımının en güzel izlendiği bu mekan, otantik ambiyansı ve kaliteli servisiyle adanın en popüler akşam yemeği adreslerinden biridir.",
        "description_en": "Situated right by the sea at Molyvos Harbor, Octopus is known for its fresh grilled octopus and creative seafood mezes. Being a place where the sunset is best viewed, it is one of the island's most popular dinner addresses with its authentic ambiance and quality service."
    },
    "Byzantino": {
        "description": "Mytilene'nin merkezinde yer alan bu şık mekan, geleneksel Yunan mutfağını modern tekniklerle birleştiriyor. Tarihi dokusu bozulmamış salonunda sunduğu özel tarifleri ve özenli şarap menüsüyle, şehirde rafine bir akşam yemeği deneyimi arayanlar için mükemmel bir alternatiftir.",
        "description_en": "Located in the center of Mytilene, this chic venue combines traditional Greek cuisine with modern techniques. It's a perfect alternative for those seeking a refined dinner experience in the city, with special recipes served in its well-preserved historical hall and an attentive wine menu."
    },
    "Anaxos Taverna": {
        "description": "Anaxos sahilinde dalgaların hemen dibinde yer alan bu tavernada, adanın lezzetli kuzu etlerinden taze deniz ürünlerine kadar geniş bir yelpazeyi bulabilirsiniz. Aile işletmesi sıcaklığı ve harika panoramik deniz manzarasıyla, samimi ve lezzet dolu bir öğle veya akşam yemeği için idealdir.",
        "description_en": "At this taverna right by the waves on Anaxos beach, you can find a wide range of dishes from the island's delicious lamb to fresh seafood. With the warmth of a family-run business and great panoramic sea views, it's ideal for a sincere and flavor-filled lunch or dinner."
    },
    "Petra Ouzeri": {
        "description": "Petra köyünün dar sokaklarında yer alan bu geleneksel uzo evi, yüzlerce uzo çeşidi ve bunlara eşlik eden taze mezeleriyle bilinir. Adanın uzo kültürünü en otantik haliyle deneyimlemek isteyenler için, samimi sohbetlerin ve yerel tatların merkezi olan bir duraktır.",
        "description_en": "Located in the narrow streets of Petra village, this traditional ouzo house is known for its hundreds of ouzo varieties and accompanying fresh mezes. For those wanting to experience the island's ouzo culture in its most authentic form, it's a stop where sincere conversations and local flavors converge."
    },
    "Limanaki": {
        "description": "Plomari Limanı'nın en sakin köşesinde yer alan Limanaki, taze balık yemekleri ve adaya özgü zeytinyağlı tatlarıyla öne çıkan bir restorandır. Denizin serinliğini hissedebileceğiniz verandasında sunduğu samimi servis ve kaliteli malzemelerle huzur dolu bir öğün vadediyor.",
        "description_en": "Situated at the quietest corner of Plomari Harbor, Limanaki is a restaurant standing out with its fresh fish dishes and island-specific olive oil treats. With intimate service and quality ingredients offered on its veranda where you can feel the sea breeze, it promises a peaceful meal."
    },
    "Mytilene Marina": {
        "description": "Adanın en modern yüzünü temsil eden Mytilene Marinası, lüks yatları ve sahil boyu dizili şık kafeleriyle bilinir. Gün boyu hareketli olan bu marina, yürüyüş yolları ve akşamları parlayan ışıklarıyla şehirde modern bir Akdeniz atmosferi yaşamak için idealdir.",
        "description_en": "Representing the most modern face of the island, Mytilene Marina is known for its luxury yachts and chic cafes lined along the coast. Lively throughout the day, this marina is ideal for experiencing a modern Mediterranean atmosphere with its walking paths and twinkling lights at night."
    },
    "Xirokastrou": {
        "description": "Midilli'nin iç kısımlarında yer alan bir vadiye hakim konumuyla Xirokastrou, geleneksel taş mimarisi ve sessiz yerel yaşamıyla bilinir. Turistik rotalardan uzak kalmak ve adanın kristal berrak havasında sakin bir doğa yürüyüşü yapmak isteyen gezginler için harika bir keşif noktasıdır.",
        "description_en": "Commanding a view of a valley in the interior of Lesbos, Xirokastrou is known for its traditional stone architecture and quiet local life. It's a great discovery point for travelers wanting to stay off touristic routes and take a calm nature walk in the island's crystal-clear air."
    },
    "Vatera Beach Bar": {
        "description": "Adanın en uzun plajı Vatera'nın kıyısında yer alan bu modern bar, serinletici içecekleri ve konforlu şezlonglarıyla bilinir. Yazın en sıcak günlerinde denizin hemen dibinde kaliteli müzik ve ferah kokteyller eşliğinde dinlenmek isteyenlerin popüler buluşma noktalarından biridir.",
        "description_en": "Located along the island's longest beach, Vatera, this modern bar is known for its refreshing drinks and comfortable loungers. It's one of the popular meeting points for those wanting to relax by the sea with quality music and fresh cocktails during the hottest summer days."
    },
    "Sto Nisi (Plomari)": {
        "description": "Plomari sahilinde yer alan Sto Nisi, taze deniz ürünleri ve geleneksel Yunan mutfağının en seçkin örneklerini sunuyor. Usta şeflerin elinden çıkan yerel tatları, denizin hemen üzerindeki balkonunda dalga sesleri eşliğinde deneyimlemek tatilin en keyifli anlarından biri olacaktır.",
        "description_en": "Located on the Plomari coast, Sto Nisi offers the most elite examples of fresh seafood and traditional Greek cuisine. Experiencing local tastes from master chefs on its balcony right over the sea, accompanied by the sound of waves, will be one of the holiday's most pleasant moments."
    },
    "Monkey Bar (Eressos)": {
         "description": "Skala Eressos'un bohem sahilinde yer alan bu popüler bar, enerjik müzikleri ve yaratıcı kokteylleriyle bilinir. Özellikle akşamüstü partileriyle tanınan mekan, adanın özgür ruhunu hissetmek isteyen genç gezginlerin her yaz vazgeçilmez duraklarından kalmayı başarıyor.",
         "description_en": "Located on the bohemian coast of Skala Eressos, this popular bar is known for its energetic music and creative cocktails. Famous especially for its sunset parties, the venue remains an indispensable stop every summer for young travelers wanting to feel the island's free spirit."
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

print(f"✅ Midilli Part 2: Enriched {count} items.")
