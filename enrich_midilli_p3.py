#!/usr/bin/env python3
import json

updates = {
    "Blue Sardine": {
        "description": "Skala Eressos sahilinde, mavisinin her tonunu kucaklayan bu şirin restoran, adanın en taze deniz mahsulleri ve geleneksel Yunan mezeleriyle ünlüdür. Adisinden ismini alan meşhur sardalyası ve denizin hemen yanındaki masalarıyla, gerçek bir Ege akşamı yaşamak isteyenlerin vazgeçilmez durağıdır.",
        "description_en": "On the shores of Skala Eressos, embracing every shade of blue, this charming restaurant is famous for the island's freshest seafood and traditional Greek mezes. With its famous sardines, from which it takes its name, and tables right by the sea, it is an indispensable stop for those wanting an authentic Aegean evening."
    },
    "Olympos Dağı": {
        "description": "Midilli'nin en yüksek noktası olan Olympos Dağı, zirvesinden sunulan nefes kesici Ege manzarasıyla doğa tutkunlarını büyüler. Yemyeşil çam ormanları, zengin bitki örtüsü ve serin havasıyla hiking tutkunları için adadaki en popüler ve etkileyici rotalardan biridir.",
        "description_en": "The highest point of Lesbos, Mount Olympos, enchants nature enthusiasts with the breathtaking Aegean views offered from its summit. With its lush pine forests, rich flora, and cool air, it is one of the island's most popular and impressive routes for hiking enthusiasts."
    },
    "Kafeneio To Stavri": {
        "description": "Agiasos'un tarihi sokaklarında, dev bir çınar ağacının gölgesinde yer alan bu geleneksel kafe, adanın en otantik duraklarından biridir. Közde pişen kahvesi ve meşhur ballı yoğurduyla yerel halkın ve turistlerin buluşma noktası olan bu mekan, geçmişin huzurunu günümüze taşır.",
        "description_en": "Located in the historic streets of Agiasos under the shade of a massive plane tree, this traditional cafe is one of the island's most authentic stops. A meeting point for locals and tourists with its coal-fired coffee and famous honey yogurt, this venue brings the peace of the past to the present."
    },
    "Karini": {
        "description": "Midilli yolunda mistik bir durak olan Karini, devasa bir çınar ağacının gövdesindeki oyuğu ve çevresindeki doğal kaynak sularıyla ünlüdür. Ressam Theophilos'un da vakit geçirdiği ve eserlerine ilham olan bu bölge, doğayla tarihin iç içe geçtiği huzur dolu bir mola yeridir.",
        "description_en": "A mystical stop on the Lesbos road, Karini is famous for the hollow in a massive plane tree trunk and its surrounding natural spring waters. This area, where the painter Theophilos spent time and found inspiration for his works, is a peaceful break spot intertwined with nature and history."
    },
    "Restaurant To Stavri": {
        "description": "Agiasos'un serin vadi manzarasına hakim konumuyla Restaurant To Stavri, geleneksel Midilli fırın yemekleri ve taze ot mezeleriyle tanınır. Taş mimarisi ve samimi servisiyle, adanın kırsal lezzetlerini en doğal haliyle deneyimlemek isteyenler için mükemmel bir akşam yemeği noktasıdır.",
        "description_en": "Commanding a view of Agiasos's cool valley, Restaurant To Stavri is known for its traditional Lesbos oven dishes and fresh herb mezes. With its stone architecture and intimate service, it is a perfect dinner spot for those wanting to experience the island's rural flavors in their most natural form."
    },
    "Sanatorio": {
        "description": "Agiasos yakınlarında, çam ormanları arasına gizlenmiş bu tarihi sanatoryum kalıntıları, adanın az bilinen ama etkileyici yerlerinden biridir. Bozulmamış doğası ve sessiz atmosferiyle, keşif yapmayı sevenler ve tarihin sessiz tanıklıklarını merak eden gezginler için dingin bir rotadır.",
        "description_en": "Hidden among the pine forests near Agiasos, these historical sanatorium ruins are one of the island's lesser-known but impressive spots. With its unspoiled nature and quiet atmosphere, it is a serene route for those who love exploration and are curious about the silent witnesses of history."
    },
    "Megali Limni (Büyük Göl)": {
        "description": "Adanın merkezinde yer alan bu gölet, zengin biyolojik çeşitliliği ve çevresindeki geniş piknik alanlarıyla doğa severlerin favorisidir. Özellikle kuş gözlemcileri için önemli bir durak olan Megali Limni, Midilli'nin yeşil kalbinde huzurlu bir gün geçirmek isteyenler için idealdir.",
        "description_en": "Located in the center of the island, this pond is a favorite for nature lovers with its rich biodiversity and surrounding wide picnic areas. An important stop especially for birdwatchers, Megali Limni is ideal for those wanting to spend a peaceful day in the green heart of Lesbos."
    },
    "Golden Sand (Chrissi Ammos)": {
        "description": "Adını altın sarısı kumlarından alan Chrissi Ammos, sığ ve ılık deniziyle çocuklu aileler için güvenli bir plaj günüdür. Daha çok yerel halkın keşfettiği bu sessiz koy, kalabalıktan uzak, masmavi suların tadını çıkarmak isteyenler için saklı bir cennet niteliğindedir.",
        "description_en": "Taking its name from its golden sands, Chrissi Ammos offers a safe beach day for families with children with its shallow and warm sea. This quiet bay, discovered mostly by locals, is a hidden paradise for those wanting to enjoy deep blue waters away from crowds."
    },
    "Evriaki Plajı": {
        "description": "Gera Körfezi'nde yer alan Evriaki Plajı, sakin denizi ve sahil boyunca dizili şirin balıkçı tavernalarıyla bilinir. Yerel bir atmosferde yüzmek ve ardından denize sıfır masalarda taze deniz ürünlerinin tadına bakmak için adanın en huzurlu köşelerinden biridir.",
        "description_en": "Located in the Gulf of Gera, Evriaki Beach is known for its calm sea and charming fish tavernas lined along the coast. It's one of the island's most peaceful corners to swim in a local atmosphere and then taste fresh seafood at tables right by the sea."
    },
    "Kunturutidia": {
        "description": "Mytilene yakınlarında saklı bir sahil yerleşimi olan Kunturutidia, geleneksel mimarisi ve sessiz koylarıyla tanınır. Şehrin koşturmacasından kaçıp kristal berraklığındaki sularda serinlemek ve adanın özgün kıyı yaşamını hissetmek için harika bir keşif noktasıdır.",
        "description_en": "A hidden coastal settlement near Mytilene, Kunturutidia is known for its traditional architecture and quiet bays. It's a great discovery point to escape city hustle, cool off in crystal-clear waters, and feel the island's authentic coastal life."
    },
    "Kalloni Tuzlaları": {
        "description": "Adanın en önemli ekolojik alanlarından biri olan Kalloni Tuzlaları, flamingo gibi onlarca kuş türüne ev sahipliği yapan devasa bir sulak alandır. Özellikle gün batımı saatlerinde pembe göçmen kuşların dansını izlemek için fotoğraf tutkunlarına eşsiz kareler sunar.",
        "description_en": "One of the most important ecological areas on the island, Kalloni Salt Pans is a massive wetland hosting dozens of bird species like flamingos. It offers unique shots for photography enthusiasts, especially to watch the dance of pink migratory birds during sunset hours."
    },
    "Mousiko Kafeneio": {
        "description": "Mytilene'nin merkezindeki dar sokaklarda yer alan bu tarihi kafe, adanın eski şehir kültürünü yansıtan en samimi mekanlardan biridir. Ahşap masaları ve nostaljik dekoruyla sunulan geleneksel kahveleri ve yerel atıştırmalıkları, adanın ruhunu solumak için birebirdir.",
        "description_en": "Located in the narrow streets in the center of Mytilene, this historic cafe is one of the most intimate venues reflecting the island's old city culture. Its traditional coffees and local snacks served with wooden tables and nostalgic decor are perfect for breathing in the island's spirit."
    },
    "Vatoussa Meydanı": {
        "description": "Midilli'nin en karakteristik köylerinden biri olan Vatoussa'nın merkezi meydanı, asırlık çınar ağaçları ve tarihi taş binalarıyla köy yaşamının nabzını tutar. Geleneksel kafelerinde yerel halkla sohbet edebileceğiniz, huzur ve samimiyet dolu tipik bir Yunan meydanıdır.",
        "description_en": "The central square of Vatoussa, one of the most characteristic villages of Lesbos, keeps the pulse of village life with its century-old plane trees and historic stone buildings. It is a typical Greek square full of peace and sincerity, where you can chat with locals in traditional cafes."
    },
    "Vatera Sahili (Uzun)": {
        "description": "Andanın güneyinde 8 kilometre boyunca uzanan masmavi Vatera Sahili, kristal berrak suları ve sükunetiyle ünlüdür. Adanın en geniş plaj alanı olması sayesinde kalabalıktan izole, deniz ve güneşle baş başa kalmak isteyenler için muazzam bir özgürlük sunar.",
        "description_en": "Stretching for 8 kilometers in the south of the island, the deep blue Vatera Coast is famous for its crystal-clear waters and tranquility. Being the island's widest beach area, it offers immense freedom for those wanting to be alone with the sea and sun, isolated from crowds."
    },
    "Charamida Plajı": {
        "description": "Mytilene havalimanı yakınlarındaki Charamida, berrak turkuaz suları ve sığ deniziyle hem yerlilerin hem de turistlerin favorisidir. Sahil boyu dizili şık tesisleri ve eğlenceli atmosferiyle, ferahlatıcı bir yüzme molası ve gün boyu güneşlenme için harika bir tercihtir.",
        "description_en": "Charamida near Mytilene airport is a favorite for both locals and tourists with its clear turquoise and shallow waters. With its chic facilities lined along the shore and fun atmosphere, it is a great choice for a refreshing swim break and sunbathing all day."
    },
    "Niselia": {
        "description": "Petra yakınlarındaki bu şirin sahil mahallesi, huzurlu atmosferi ve geleneksel tavernalarıyla adanın samimi yüzünü yansıtır. Kristal sularında yüzdükten sonra kıyıdaki bir masada taze mezelerin tadına bakmak, Midilli'nin yavaş yaşam ritmini hissetmenizi sağlayan en güzel deneyimlerden biridir.",
        "description_en": "This charming coastal neighborhood near Petra reflects the island's sincere side with its peaceful atmosphere and traditional tavernas. After swimming in crystal waters, tasting fresh mezes at a seaside table is one of the best experiences to feel Lesbos' slow rhythm of life."
    },
    "Podaras Plajı": {
        "description": "Sigri'nin biraz dışında yer alan bu vahşi ve rüzgarlı plaj, sarp doğası ve bozulmamış kumsalıyla maceracı gezginlerin keşif noktasıdır. Turistik tesislerden uzak, tamamen doğayla baş başa kalınan bu koy, adanın az bilinen ama en etkileyici manzaralarından biridir.",
        "description_en": "Located slightly outside of Sigri, this wild and windy beach is a discovery point for adventurous travelers with its steep nature and unspoiled shore. Away from tourist facilities, this bay stays entirely alone with nature, being one of the island's lesser-known but most impressive views."
    },
    "Gavathas Plajı": {
        "description": "Adanın kuzeybatısındaki bu huzur dolu kumsal, sığ ve dingin deniziyle çocuklu ailelerin en sevdiği sığınaklardan biridir. Kıyıda sıralanmış asırlık balıkçı evleri ve sessiz tavernalarıyla, geçmişin sade ve huzurlu ada yaşamını korumayı başarmıştır.",
        "description_en": "This peaceful beach in the northwest of the island is one of the favorite sanctuaries for families with children with its shallow and calm sea. It has succeeded in preserving the simple and peaceful island life of the past with its century-old fisherman houses and quiet tavernas lined along the shore."
    },
    "To Ouzadiko tou Baboukou": {
        "description": "Molyvos Limanı'nın en ikonik duraklarından olan bu geleneksel uzo evi, yüzlerce uzo çeşidi ve bunlara eşlik eden efsanevi deniz mahsulleri mezeleriyle ünlüdür. Adriyatik meltemi eşliğinde kurulan sofralarda, uzo kültürünün gerçek tarihini ve lezzetini deneyimleyebilirsiniz.",
        "description_en": "One of the most iconic stops in Molyvos Harbor, this traditional ouzo house is famous for its hundreds of ouzo varieties and the legendary seafood mezes that accompany them. On tables set with the Adriatic breeze, you can experience the true history and flavor of the ouzo culture."
    },
    "Apaggkio": {
        "description": "Plomari'nin dar sokaklarında gizli bir hazine gibi beliren Apaggkio, otantik dekoru ve yaratıcı Yunan mezeleriyle rafine lezzetler sunuyor. Samimi ve loş atmosferiyle, adada kendinizi özel hissedeceğiniz romantik ve lezzet dolu bir akşam yemeği için mükemmeldir.",
        "description_en": "Appearing like a hidden treasure in the narrow streets of Plomari, Apaggkio offers refined flavors with its authentic decor and creative Greek mezes. With its intimate and dimly lit atmosphere, it is perfect for a romantic and flavor-filled dinner where you'll feel special on the island."
    },
    "Kalderimi": {
        "description": "Mytilene çarşısının kalbinde yer alan bu otantik restoran, adanın en iyi geleneksel yemeklerini ve zeytinyağlılarını sunan bir lezzet durağıdır. Arnavut kaldırımlı bir sokaktaki masaları ve ev yapımı lezzetleriyle, şehrin tarihini tadarken samimiyet dolu bir öğün geçireceğiniz bir yerdir.",
        "description_en": "Located in the heart of Mytilene market, this authentic restaurant is a flavor stop offering the island's best traditional dishes and olive oil treats. With tables on a cobbled street and homemade flavors, it's a place where you'll have a meal full of sincerity while tasting the city's history."
    },
    "Anemomilos Restaurant": {
        "description": "Adını yanı başındaki tarihi yel değirmeninden alan bu mekan, eşsiz deniz manzarası ve kaliteli Akdeniz mutfağıyla biliniyor. Özellikle gün batımında renkleriyle büyüleyen denizi seyrederken usta şefler tarafından hazırlanan deniz ürünlerini tatmak için adanın en şık adreslerinden biridir.",
        "description_en": "Taking its name from the historic windmill right beside it, this venue is known for its unique sea views and quality Mediterranean cuisine. It is one of the island's most chic addresses to taste seafood prepared by master chefs while watching the sea especially enchanting with its colors at sunset."
    },
    "Trygonas": {
        "description": "Plomari merkezinde yer alan bu şirin yerel kafe, adanın uzo ve meze kültürünü en samimi haliyle yansıtıyor. Yerel halkın uğrak yeri olan bu durakta, ahşap masalar üzerinde sunulan taze köy ürünleri ve hafif müzik eşliğinde yavaş yaşamanın tadına varabilirsiniz.",
        "description_en": "Located in the center of Plomari, this charming local cafe reflects the island's ouzo and meze culture in its most sincere form. At this stop, a frequent place for locals, you can savor slow living with fresh village products served on wooden tables and soft music."
    },
    "Soulatso": {
        "description": "Molyvos sahilindeki dekoratif şıklığı ve muazzam körfez manzarasıyla bilinen Soulatso, yenilikçi kokteylleri ve zengin içki seçkisiyle öne çıkar. Gün boyu serinletici bir mola yeri, akşamları ise ay ışığı altında neşeli sohbetlerin yapıldığı popüler bir liman barıdır.",
        "description_en": "Known for its decorative elegance and magnificent bay views on the Molyvos coast, Soulatso stands out with its innovative cocktails and rich drink selection. It's a popular harbor bar serving as a refreshing break spot during the day and a place for cheerful moonlight conversations in the evening."
    },
    "Women's Cooperative of Mesotopos": {
        "description": "Mesotopos köyünde kurulan bu kooperatif, köylü kadınların el emeğiyle hazırladığı geleneksel eriştelerden, ev yapımı kurabiyelere kadar adanın saf lezzetlerini sunuyor. Yöresel üretimi desteklemek ve Midilli'nin unutulmaya yüz tutmuş tariflerini tatmak isteyenler için çok değerli bir duraktır.",
        "description_en": "Established in Mesotopos village, this cooperative offers the island's pure flavors ranging from traditional handmade noodles to homemade cookies prepared by village women. It is a very valuable stop for those wanting to support local production and taste Lesbos's nearly forgotten recipes."
    },
    "Andissa Meydanı": {
        "description": "Andissa köyünün serin havası ve asırlık çınar ağaçlarıyla çevrili meydanı, adanın kuzeybatısındaki en samimi köy yaşamı noktasıdır. Geleneksel kahvehanelerinde uzo içerken yerel halkın dilden dile dolaşan hikayelerini dinleyebileceğiniz, huzur ve tarih kokan tipik bir Yunan meydanıdır.",
        "description_en": "The square of Andissa village, surrounded by cool air and century-old plane trees, is the most sincere village life spot in the island's northwest. It's a typical Greek square smelling of peace and history, where you can listen to stories passed from mouth to mouth among locals while drinking ouzo in traditional coffee houses."
    },
    "Lapsarna Plajı": {
        "description": "Yolculuğun sonundaki saklı ödül olan Lapsarna Plajı, ıssızlığı ve kristal berrak turkuaz sularıyla tanınır. Hiçbir tesisin bulunmadığı, sadece doğanın kucağında gün boyu denizin ve sessizliğin tadını çıkarabileceğiniz bu koy, adanın en iyi korunan plajlarından biridir.",
        "description_en": "The hidden reward at the end of the journey, Lapsarna Beach is known for its desolation and crystal-clear turquoise waters. With no facilities available, this bay where you can only enjoy the sea and silence in nature's lap all day is one of the island's best-preserved beaches."
    },
    "Pesas Şelaleleri": {
        "description": "Achladeri yakınlarında ormanlık alanların içine gizlenmiş bu doğal şelaleler, adanın serin ve taze nefesidir. Yaz aylarında bile serinletici suyun sesiyle dinlenmek ve doğa fotoğrafçılığı yapmak isteyenler için az bilinen ama keşfedilmeyi bekleyen bir huzur vahasıdır.",
        "description_en": "Hidden inside forested areas near Achladeri, these natural waterfalls are the island's cool and fresh breath. It is a lesser-known but awaiting-to-be-discovered oasis of peace for those wanting to relax with the sound of cooling water even in summer and do nature photography."
    },
    "Klapados": {
        "description": "Kalloni vadi manzarasına hakim bir noktada yer alan bu tarihi bölge, adanın Osmanlı döneminden kalma özgün mimari izlerini ve huzurlu kırsal yaşamını yansıtır. Zengin bitki çeşitliliği arasındaki yürüyüş patikalarıyla, doğa ve tarih meraklılarına hitap eden sessiz bir keşif noktasıdır.",
        "description_en": "Commanding a view of the Kalloni valley, this historical area reflects original architectural traces from the island's Ottoman period and its peaceful rural life. With walking paths among rich plant diversity, it's a quiet discovery point appealing to nature and history enthusiasts."
    },
    "Rani Plajı": {
        "description": "Skala Kalloni yakınındaki Rani Plajı, sakin ve sığ deniziyle çocuklu ailelerin en rahat edeceği plajlardan biridir. Çevresindeki birkaç şirin kafesi ve huzurlu kumsalıyla, gürültüden uzak, güvenli ve keyifli bir deniz günü geçirmek isteyenlerin gizli adresidir.",
        "description_en": "Rani Beach near Skala Kalloni is one of the beaches where families with children will be most comfortable with its calm and shallow sea. With a few charming cafes nearby and its peaceful shore, it's the hidden address for those wanting a safe and pleasant sea day away from noise."
    },
    "Parasol (Skala Eressos)": {
         "description": "Eressos sahilinin bohem rüzgarını en iyi hisseden Parasol, yaratıcı dekorasyonu ve sahil kenarındaki rahat localarıyla tanınır. Yaz boyunca enerjik müzikleri ve seçkin kokteylleriyle adanın özgür ruhunu yansıtan en popüler ve neşeli sahil barı olmayı başarıyor.",
         "description_en": "Best feeling the bohemian winds of Eressos coast, Parasol is known for its creative decoration and relaxed seaside booths. Succeeding in being the most popular and joyous beach bar reflecting the island's free spirit with energetic music and elite cocktails throughout the summer."
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

print(f"✅ Midilli Part 3: Enriched {count} items.")
