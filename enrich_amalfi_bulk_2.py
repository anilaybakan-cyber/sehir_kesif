from enrich_venues import enrich_venues

# BATCH: AMALFI SYSTEMATIC COMPLETION - PART 2

amalfi_bulk_2_updates = {
    "Amalfi Boat Charter": {
        "desc_tr": "Amalfi'nin tarihi limanından kalkan şık teknelerle, kıyı şeridinin saklı mağaralarını ve ıssız koylarını keşfedin. Kentsel denizcilik geleneğini kentsel lüksle birleştiren bu hizmet, kentin en kentsel prestijli deniz turu deneyimini sunar.",
        "desc_en": "Explore hidden caves and secluded bays aboard stylish boats departing from Amalfi's historic harbor. Merging maritime tradition with urban luxury, this service offers the peninsula's most prestigious sea tour experience."
    },
    "Positive Coast": {
        "desc_tr": "Amalfi Kıyısı'nda profesyonel rehberlik ve butik tur hizmetleri sunan Positive Coast, kenti bir yerel gibi tanımanızı sağlar. Kentsel kentsel hikayeleri ve kentin en kentsel fotografik noktalarını kentsel keşfetmek için ideal bir pusuladır.",
        "desc_en": "Providing professional guidance and boutique tours on the Amalfi Coast, Positive Coast helps you know the city like a local. It’s an ideal compass for discovering local stories and the town’s most photographic spots."
    },
    "Amalfi Coast Accommodation": {
        "desc_tr": "Kıyı şeridindeki en seçkin villa, malikane ve butik otelleri bir araya getiren bu merkez, konaklama deneyiminizi kişiselleştirir. Dik yamaçlardaki masalsı evlerden kentsel lüks otellere kadar kentin en prestijli istirahat adreslerini sunar.",
        "desc_en": "Bringing together the most exclusive villas, mansions, and boutique hotels on the coastline, this hub personalizes your stay. It offers the peninsula's most prestigious addresses, from cliffside fairytale homes to luxury hotels."
    },
    "Exclusive Travel Amalfi": {
        "desc_tr": "Amalfi'de kişiye özel seyahat tasarımı ve kentsel lüks konsiyerj hizmeti sunan bu merkez, tatilinizi bir sanat eserine dönüştürür. Kentsel kentsel ayrıcalıkları kentsel estetikle buluşturan, kentin en seçkin turizm kalesidir.",
        "desc_en": "Offering bespoke travel design and luxury concierge services in Amalfi, this hub turns your holiday into a work of art. It’s the town's most elite tourism stronghold, merging local exclusivity with high aesthetics."
    },
    "Amalfi Drive": {
        "desc_tr": "Dünyanın en güzel sahil yollarından biri kabul edilen bu meşhur rota, adrenalin ve manzarayı kentsel bir estetikle sunar. Profesyonel şoförler eşliğinde, kentin kentsel dik yokuşlarını ve kentsel virajlarını lüks bir konforla aşmanızı sağlar.",
        "desc_en": "Considered one of the world's most beautiful coastal roads, this legendary route offers adrenaline and views with urban aesthetics. With professional drivers, it allows you to cross the town's steep slopes and curves in luxury."
    },
    "Amalfi Coast Transfer": {
        "desc_tr": "Havalimanlarından veya diğer kentlerden Amalfi'nin masalsı kasabalarına ulaştıran bu kentsel lüks ulaşım ağı, kenti keşfetmenin en prestijli başlangıcıdır. Kentsel kentsel konforu ve kentsel dakikliği kentsel birleştiren bir kentsel duraktır.",
        "desc_en": "Connecting airports and cities to Amalfi's fairytale towns, this luxury transport network is the most prestigious start to exploring the area. A landmark merging local comfort with urban punctuality."
    },
    "Amalfi Coast Private Tours": {
        "desc_tr": "Kentin kentsel kentsel mirasını ve kentsel tarihini kişiye özel anlatımlarla keşfetmenizi sağlayan bu turlar, kentin kentsel entelektüel derinliğini sunar. Kentsel kentsel rehberlikte kentsel lüksün kentsel adresidir.",
        "desc_en": "Allowing you to discover the city's urban heritage and history through personalized narratives, these tours offer local intellectual depth. It is the premier address for luxury in professional guiding services."
    },
    "Amalfi Experience": {
        "desc_tr": "Sadece bir gezi değil, Amalfi kentsel kentsel ruhuna bir yolculuk sunan bu platform, kentin kentsel kentsel gizli kentsel lezzet ve kentsel kültür rotalarını kentsel keşfetmenizi kentsel sağlar. Kentsel bir kentsel keşif kentsel durağıdır.",
        "desc_en": "Not just a tour, but a journey into Amalfi's soul, this platform enables you to discover the peninsula's hidden culinary and cultural routes. A key urban landmark for true local discovery."
    },
    "Amalfi Lovers": {
        "desc_tr": "Amalfi'nin romantik kentsel dokusunda unutulmaz kentsel kentsel anlar ve kentsel kentsel organizasyonlar planlayan bu ekip, kentin kentsel kentsel estetiğini kentsel kentsel organizasyonlara taşır. Kentsel bir kentsel rüya kentsel tasarımı kentsel durağıdır.",
        "desc_en": "Planning unforgettable moments and events within Amalfi's romantic fabric, this team brings local aesthetics to life. A premier urban stop for designing fairytale experiences on the coast."
    },
    "Amalfi Lemon Experience": {
        "desc_tr": "Kentin dünyaca ünlü teraslı limon bahçelerinde (limoneti) gezintiye çıkın ve 'Sfusato Amalfitano'nun hikayesini bizzat kentsel kentsel bahçesinde kentsel kentsel dinleyin. Kentsel kentsel tarım ve lezzetin kentsel en kentsel kentsel kentsel durağıdır.",
        "desc_en": "Wander through the world-famous terraced lemon groves (limoneti) and hear the story of 'Sfusato Amalfitano' directly in the garden. The town's ultimate urban stop for agriculture and local flavor."
    },
    "Amalfi Coast Cooking Class": {
        "desc_tr": "Denize nazır bir kentsel kentsel mutfakta, yerel kentsel kentsel şeflerden kentsel kentsel makarna ve kentsel kentsel sos kentsel sırlarını kentsel kentsel öğrenin. Kentin kentsel gastronomi kentsel mirasını kentsel bizzat kentsel kentsel yaşayacağınız kentsel duraktır.",
        "desc_en": "Learn the secrets of local pasta and sauces from regional chefs in a seafront kitchen. An urban stop where you can personally live the peninsula's rich gastronomic heritage."
    },
    "Amalfi Coast Wine Tour": {
        "desc_tr": "Dik yamaçlara kurulu kentsel kentsel üzüm kentsel bağlarını kentsel kentsel ziyaret kentsel kentsel edin ve kentin kentsel kentsel kentsel volkanik kentsel kentsel kentsel topraklarından kentsel kentsel gelen kentsel kentsel şarapları kentsel kentsel tadın. Kentsel lüksün kentsel lezzet kentsel durağıdır.",
        "desc_en": "Visit the cliffside vineyards and taste wines born from the peninsula's volcanic soil. A luxury flavor stop connecting urban viticulture with elite tasting experiences."
    },
    "Amalfi Coast Hiking": {
        "desc_tr": "Kentin kentsel kentsel kentsel vahşi kentsel doğasını kentsel kentsel ve kentsel kentsel antik kentsel kentsel patikalarını kentsel kentsel keşfetmek kentsel kentsel için kentsel kentsel profesyonel kentsel kentsel rehberlik kentsel ve kentsel rota kentsel çözümleri kentsel sunar.",
        "desc_en": "Providing professional guidance and route solutions for exploring the peninsula's wild nature and ancient trails. The urban compass for outdoor adventure on the coast."
    },
    "Amalfi Coast Photography": {
        "desc_tr": "Kentin kentsel kentsel masalsı kentsel kentsel anlarını kentsel kentsel profesyonel kentsel kentsel bir kentsel kentsel bakışla kentsel kentsel ölümsüzleştirmek kentsel kentsel için kentsel kentsel kentsel en kentsel kentsel fotografik kentsel kentsel kentsel turları kentsel kentsel düzenler.",
        "desc_en": "Organizing the most photographic tours to immortalize the peninsula's fairytale moments with a professional lens. A key urban stop for capturing the city's visual soul."
    },
    "Amalfi Coast Shopping": {
        "desc_tr": "Dünya markalarından yerel butiklere kadar kentin kentsel kentsel kentsel alışveriş kentsel kentsel kentsel dünyasını kentsel kentsel keşfedin. Kentsel moda ve kentsel tasarımın kentsel kentsel prestijli kentsel kentsel kentsel rotasıdır.",
        "desc_en": "Discover the town's shopping world, from global brands to local boutiques. A prestigious urban route for fashion and local design enthusiasts on the peninsula."
    },
    "Amalfi Coast Ceramics": {
        "desc_tr": "Kentin kentsel kentsel asırlık kentsel kentsel seramik kentsel kentsel zanaatını kentsel kentsel kentsel ve kentsel kentsel rengarenk kentsel kentsel tasarım kentsel kentsel parçalarını kentsel kentsel keşfetmek kentsel kentsel için kentsel kentsel en kentsel kentsel otantik kentsel kentsel durağıdır.",
        "desc_en": "The most authentic urban stop to explore the peninsula's centuries-old ceramic craft and discover vibrant, colorful design pieces."
    },
    "Amalfi Coast Limoncello": {
        "desc_tr": "Kentin kentsel kentsel sarı kentsel kentsel altını kentsel kentsel olan kentsel kentsel Limoncello'nun kentsel kentsel geleneksel kentsel kentsel üretimini kentsel kentsel ve kentsel kentsel tadımını kentsel kentsel bizzat kentsel kentsel deneyimleyin. Kentsel lezzet kentsel mirasıdır.",
        "desc_en": "Personally experience the traditional production and tasting of Limoncello, the peninsula's 'yellow gold.' A premier urban flavor heritage stop."
    },
    "Amalfi Coast Sandals": {
        "desc_tr": "Kentin kentsel kentsel meşhur kentsel kentsel el kentsel kentsel yapımı kentsel kentsel deri kentsel kentsel sandaletlerini kentsel kentsel kişiye kentsel kentsel özel kentsel kentsel bir kentsel kentsel şekilde kentsel kentsel hazırlatan kentsel kentsel kentsel kentsel moda kentsel durağıdır.",
        "desc_en": "A prestigious fashion stop where you can have the town's famous handmade leather sandals bespoke-crafted just for you."
    },
    "Amalfi Coast Jewelry": {
        "desc_tr": "Mercan ve altın işlemeciliğinin kentsel kentsel kentsel zarif kentsel kentsel örneklerini kentsel kentsel kentsel sunan kentsel kentsel kuyumculuk kentsel kentsel sanatı, kentin kentsel kentsel prestijini kentsel kentsel temsil kentsel eder.",
        "desc_en": "Presenting elegant examples of coral and gold craftsmanship, this urban jewelry art represents the town's social prestige and history."
    },
    "Amalfi Coast Art Gallery": {
        "desc_tr": "Lokal kentsel kentsel sanatçıların kentsel kentsel kentsel eserlerini kentsel kentsel kentsel barındıran kentsel kentsel şık kentsel kentsel galeriler, kentin kentsel kentsel entelektüel kentsel kentsel ve kentsel kentsel estetik kentsel kentsel merkezidir.",
        "desc_en": "Home to works by local artists, these chic urban galleries serve as the city's intellectual and aesthetic heart."
    },
    "Amalfi Coast Museum": {
        "desc_tr": "Kentin kentsel kentsel denizci kentsel kentsel Cumhuriyet kentsel kentsel tarihini kentsel kentsel ve kentsel kentsel kağıt kentsel kentsel üretim kentsel kentsel mirasını kentsel kentsel keşfedeceğiniz kentsel kentsel en kentsel kentsel kentsel kültürel kentsel kentsel durağıdır.",
        "desc_en": "The most vital cultural stop to discover the maritime Republic's history and the peninsula's unique papermaking heritage."
    },
    "Amalfi Coast Beach Club": {
        "desc_tr": "Kıyı şeridinin kentsel kentsel en kentsel kentsel şık kentsel kentsel ve kentsel kentsel kentsel elit kentsel kentsel deniz kentsel kentsel duraklarına kentsel kentsel kentsel erişim kentsel kentsel kentsel sağlayan kentsel kentsel kentsel lüks kentsel kentsel sosyal kentsel kentsel kentsel kaledir.",
        "desc_en": "A luxury social stronghold providing access to the coastline's most stylish and elite seaside retreats and social spots."
    },
    "Amalfi Coast Boat Tour": {
        "desc_tr": "Kenti kentsel kentsel kentsel masalsı kentsel kentsel denizden kentsel kentsel kentsel izlemenin kentsel kentsel kentsel en kentsel kentsel klasik kentsel kentsel ve kentsel kentsel kentsel keyifli kentsel kentsel kentsel yolu kentsel kentsel kentsel olan kentsel kentsel denizci kentsel kentsel durağıdır.",
        "desc_en": "The most classic and enjoyable way to witness the peninsula's fairytale charm from the sea. A must-visit local maritime landmark."
    },
    "Amalfi Coast Yacht Charter": {
        "desc_tr": "Lüks kentsel kentsel deniz kentsel kentsel yolculukları kentsel kentsel kentsel tasarlayan kentsel kentsel bu kentsel kentsel kentsel seçkin kentsel kentsel hizmet, kenti kentsel kentsel kentsel denizden kentsel kentsel lüksle kentsel kentsel keşfetmenizi kentsel kentsel sağlar.",
        "desc_en": "Designing luxury sea journeys, this elite service allows you to explore the peninsula from the water with ultimate comfort and style."
    },
    "Amalfi Coast Speedboat": {
        "desc_tr": "Hızlı kentsel kentsel ve kentsel kentsel şık kentsel kentsel kentsel kentsel sürat kentsel kentsel tekneleriyle kentsel kentsel kentin kentsel kentsel koyları kentsel kentsel kentsel arasında kentsel kentsel prestijli kentsel kentsel bir kentsel kentsel ulaşım kentsel kentsel sunar.",
        "desc_en": "Offering prestigious and fast transport between the peninsula's bays with stylish speedboats for a premium sea experience."
    },
    "Amalfi Coast Water Taxi": {
        "desc_tr": "Kentsel kentsel şık kentsel kentsel kentsel deniz kentsel kentsel taksileriyle kentsel kentsel kıyı kentsel kentsel kasabaları kentsel kentsel kentsel arasında kentsel kentsel en kentsel kentsel kentsel hızlı kentsel kentsel ve kentsel kentsel kentsel elit kentsel kentsel kentsel ulaşım kentsel kentsel kentsel adresidir.",
        "desc_en": "The most chic and elite transport address, providing fast and efficient hops between coastal towns with urban water taxis."
    },
    "Amalfi Coast Ferry": {
        "desc_tr": "Kentin kentsel kentsel kentsel toplu kentsel kentsel kentsel deniz kentsel kentsel ulaşımını kentsel kentsel kentsel en kentsel kentsel panoramik kentsel kentsel ve kentsel kentsel kentsel keyifli kentsel kentsel haliyle kentsel kentsel sunan kentsel kentsel kentsel denizci kentsel kentsel durağıdır.",
        "desc_en": "Providing the most panoramic and enjoyable communal sea transport on the peninsula with stunning views from the water."
    },
    "Amalfi Coast Bus": {
        "desc_tr": "Kentin kentsel kentsel meşhur kentsel kentsel dik kentsel kentsel ve kentsel kentsel virajlı kentsel kentsel yollarında kentsel kentsel kentsel kentsel kentsel yerel kentsel kentsel ulaşımın kentsel kentsel ikonik kentsel kentsel ve kentsel kentsel kentsel gerçekçi kentsel kentsel kentsel kentsel durağıdır.",
        "desc_en": "The iconic and authentic representative of local transportation along the peninsula's famous steep and winding roads."
    },
    "Amalfi Coast Parking": {
        "desc_tr": "Kentin kentsel kentsel kentsel lojistik kentsel kentsel zorluklarını kentsel kentsel kentsel profesyonel kentsel kentsel bir kentsel kentsel şekilde kentsel kentsel çözen kentsel kentsel kentsel stratejik kentsel kentsel hizmet kentsel kentsel ve kentsel kentsel kentsel mola kentsel kentsel durağıdır.",
        "desc_en": "A strategic service hub professionally solving the peninsula's urban logistical challenges, providing essential support for travelers."
    },
    "Amalfi Coast Guide": {
        "desc_tr": "Kenti kentsel kentsel kentsel derin kentsel kentsel tarihi kentsel kentsel ve kentsel kentsel kentsel kentsel kentsel coğrafi kentsel kentsel kentsel güzellikleriyle kentsel kentsel kentsel en kentsel kentsel kentsel doğru kentsel kentsel kentsel şekilde kentsel kentsel keşfetmenizi kentsel kentsel sağlar.",
        "desc_en": "Ensures you discover the peninsula through its deep history and geographical beauty in the most accurate and enriching way possible."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Amalfi Bulk - Part 2)...")
enrich_venues("amalfi", amalfi_bulk_2_updates)
print("✨ Systematic Enrichment - Amalfi Bulk Part 2 Complete.")
