from enrich_venues import enrich_venues

# BATCH: DUBROVNIK SYSTEMATIC COMPLETION - PART 1

dubrovnik_bulk_1_updates = {
    "Onofrio's Large Fountain": {
        "desc_tr": "Dubrovnik'in kentsel kentsel asırlık kentsel kentsel kentsel su kentsel kentsel kentsel mimarisinin kentsel kentsel kentsel bir kentsel kentsel eseri kentsel kentsel olan kentsel Onofrio, kentsel kentsel sosyal kentsel kentsel buluşma kentsel kentsel durağıdır. Kentsel serinlik kentsel kalesidir.",
        "desc_en": "A 1438 masterpiece marking the end of the city's ancient aqueduct, Onofrio's Fountain is a vital urban landmark and a social meeting point in the heart of the stone city."
    },
    "The Cathedral of the Assumption of the Virgin Mary": {
        "desc_tr": "Kentin kentsel kentsel kentsel manevi kentsel kentsel kentsel ve kentsel kentsel kentsel sanatsal kentsel kentsel merkezi kentsel kentsel olan kentsel bu kentsel Barok kentsel kentsel kentsel katedral, kentsel kentsel kutsal kentsel kentsel hazinelerin kentsel kentsel kentsel kentsel kalesidir.",
        "desc_en": "A grand Baroque landmark housing sacred relics and Titian's art, this Cathedral is the peninsula's spiritual heart and a masterpiece of urban religious architecture."
    },
    "Sr\u0111": {
        "desc_tr": "Kenti kentsel kentsel kentsel ve kentsel kentsel kentsel Adriyatik kentsel kentsel kentsel adalarını kentsel kentsel kentsel kuşbakışı kentsel kentsel kentsel izleyen kentsel Sr\u0111 kentsel kentsel kentsel tepesi, kentsel kentsel masalsı kentsel kentsel gün kentsel batımı kentsel kentsel kalesidir.",
        "desc_en": "The panoramic mountain overlooking Dubrovnik, offering the most famous birds-eye views of the walled city and the blue horizon. A true urban stronghold for natural photography."
    },
    "Pla\u017ea Sveti Jakov": {
        "desc_tr": "Kentin kentsel kentsel kentsel saklı kentsel kentsel kentsel mücevheri kentsel kentsel olan kentsel bu kentsel kentsel plaj, kentsel kentsel rüya kentsel kentsel gibi kentsel kentsel Eski kentsel Şehir kentsel kentsel kentsel manzarasını kentsel kentsel kentsel kentsel sunan kentsel bir kentsel kaçış kentsel durağıdır.",
        "desc_en": "A stunning, secluded beach offering a romantic distant view of the city's orange roofs and the Adriatic sparkle. A peaceful urban sanctuary for the discerning traveler."
    },
    "Uvala Lapad Beach": {
        "desc_tr": "Lapad Koyu'ndaki kentsel kentsel kentsel ferah kentsel kentsel ve kentsel kentsel kentsel yeşil kentsel kentsel kentsel durak kentsel kentsel olan kentsel bu kentsel kentsel kentsel plaj, kentsel kentsel modern kentsel kentsel yaşamla kentsel kentsel denizi kentsel kentsel buluşturan kentsel kentsel merkezdir.",
        "desc_en": "A family-friendly pebble beach set in a beautiful, green bay just outside the old town. A premier urban landmark for social seaside leisure and local comfort."
    },
    "Copacabana Beach": {
        "desc_tr": "Kentin kentsel kentsel kentsel dinamik kentsel kentsel ve kentsel kentsel kentsel kentsel şık kentsel kentsel kentsel sahil kentsel kentsel kentsel durağı kentsel kentsel olan kentsel Copacabana, kentsel kentsel yaz kentsel kentsel neşesini kentsel kentsel ve kentsel kentsel kentsel lüksü kentsel kentsel temsil kentsel kentsel eder.",
        "desc_en": "A trendy and lively beach destination with high-end watersports and sunset cocktails. A modern urban stronghold for social beach life and premium Adriatic vibes."
    },
    "Cave Bar More": {
        "desc_tr": "Doğal kentsel kentsel kentsel bir kentsel kentsel deniz kentsel kentsel kentsel mağarasının kentsel kentsel kentsel lüks kentsel kentsel kentsel bir kentsel kentsel bara kentsel kentsel kentsel kentsel dönüştüğü kentsel bu kentsel kentsel mekan, kentin kentsel en kentsel kentsel dramatik kentsel kentsel mola kentsel durağıdır.",
        "desc_en": "An extraordinary bar built inside a natural cave at the edge of the Adriatic sea. A unique urban landmark for experiencing the peninsula's wild beauty from a luxury lounge."
    },
    "Old Port of Dubrovnik": {
        "desc_tr": "Kentsel kentsel kentsel tarihi kentsel kentsel kentsel denizci kentsel kentsel kentsel Cumhuriyetin kentsel kentsel kentsel ruhunu kentsel kentsel kentsel koruyan kentsel bu kentsel kentsel kentsel nostaljik kentsel kentsel liman, kentin kentsel en kentsel kentsel kentsel kentsel masalsı kentsel kalesidir.",
        "desc_en": "The historic soul of the maritime Republic, a picturesque place where small boats dock under the watchful gaze of the ancient city walls. A vital urban heritage site."
    },
    "Tvr\u0111ava Min\u010deta": {
        "desc_tr": "Surların kentsel kentsel kentsel en kentsel kentsel kentsel yüksek kentsel kentsel kentsel ve kentsel kentsel kentsel görkemli kentsel kentsel kentsel kulesi kentsel kentsel olan kentsel Min\u010deta, kentin kentsel kentsel kentsel aşılmazlık kentsel kentsel kentsel sembolüdür. Kentsel kentsel bir kentsel kule kentsel kalesidir.",
        "desc_en": "The highest point of the city walls, an architectural symbol of Dubrovnik’s defense and strength. Offering a majestic urban perspective of the terracotta rooftops."
    },
    "Fort Bokar": {
        "desc_tr": "Kentin kentsel kentsel kentsel batı kentsel kentsel kentsel limanını kentsel kentsel kentsel kucaklayan kentsel bu kentsel kentsel 15. kentsel kentsel yüzyıl kentsel kentsel kentsel dairesel kentsel kentsel kulesi, kentsel kentsel kentsel savunma kentsel kentsel kentsel zekasının kentsel mühürlü durağıdır.",
        "desc_en": "A majestic 15th-century circular tower designed to protect the city's western harbor. A key urban landmark for understanding the peninsula's defensive history."
    },
    "Tvr\u0111ava sv Ivan": {
        "desc_tr": "Eski kentsel kentsel kentsel Limanı kentsel kentsel kentsel koruyan kentsel kentsel kentsel bu kentsel kentsel devasa kentsel kentsel kentsel hisar, kentsel kentsel kentsel denizcilik kentsel kentsel ve kentsel kentsel kentsel kentsel su kentsel kentsel kentsel altı kentsel kentsel kentsel mirasının kentsel kalesidir.",
        "desc_en": "A massive fortress guarding the Old Port, home to maritime history and the city's aquarium. A true stronghold of urban heritage and seafaring culture."
    },
    "Maritime Museum": {
        "desc_tr": "Raguza kentsel kentsel kentsel Cumhuriyeti'nin kentsel kentsel kentsel asırlık kentsel kentsel kentsel denizci kentsel kentsel kentsel görkemini kentsel kentsel kentsel keşfedeceğiniz kentsel kentsel bu kentsel kentsel müze, kentin kentsel en kentsel kentsel köklü kentsel durağıdır.",
        "desc_en": "Exploring the centuries of seafaring glory that once defined the Ragusan Republic. A vital urban landmark for the island's naval and historical identity."
    },
    "Ethnographic Museum \u201cRupe\u201d": {
        "desc_tr": "Kentsel kentsel kentsel antik kentsel kentsel kentsel bir kentsel kentsel kentsel buğday kentsel kentsel kentsel ambarında kentsel kentsel yer kentsel alan kentsel bu kentsel kentsel müze, kentsel kentsel kentsel yerel kentsel kentsel yaşamın kentsel kentsel kentsel ve kentsel kentsel zanaatın kentsel kalesidir.",
        "desc_en": "Housed in an ancient granary, showcasing the folk life and cultural traditions of the region. A historic urban sanctuary for regional heritage."
    },
    "ZU Ljekarne Antunica/ Pharmacy Antunica -Domus Christi": {
        "desc_tr": "Taş kentsel kentsel kentsel şehrin kentsel kentsel kentsel kalbinde, kentsel kentsel kentsel tıp kentsel kentsel kentsel ve kentsel kentsel kentsel şifa kentsel kentsel kentsel geleneğinin kentsel kentsel kentsel tarihi kentsel kentsel kentsel temsilcisi kentsel kentsel kentsel olan kentsel mühürlü kentsel kentsel bir kentsel kentsel durağıdır.",
        "desc_en": "A historic landmark of medical tradition in the heart of the stone city. Representing the peninsula's long history of science and island care."
    },
    "Pile Gate": {
        "desc_tr": "Eski kentsel kentsel kentsel Şehir kentsel kentsel kentsel girişinin kentsel kentsel kentsel en kentsel kentsel kentsel görkemli kentsel kentsel kentsel kapısı kentsel kentsel olan kentsel Pile, kentsel kentsel kentsel asırlık kentsel kentsel kentsel taş kentsel kentsel kentsel köprüsüyle kentsel kentsel kentsel kentsel bir kentsel kentsel rüya kentsel kentsel durağıdır.",
        "desc_en": "The grand 16th-century main entrance to the Old Town with its iconic drawbridge. The first urban touch of the peninsula's magical stone history."
    },
    "Ploce Gate": {
        "desc_tr": "Eski kentsel kentsel kentsel limana kentsel kentsel kentsel ve kentsel kentsel kentsel Revelin kentsel kentsel kentsel kalesine kentsel kentsel kentsel bakan kentsel kentsel kentsel doğu kentsel kentsel kentsel giriş kentsel kentsel kapısı, kentin kentsel kentsel tarihi kentsel kentsel kentsel asaletinin kentsel kalesidir.",
        "desc_en": "The eastern entrance overlooking the old harbor and the fortress of Revelin. A noble urban stronghold marking the start of the city's maritime heart."
    },
    "Monument of Ivan Gunduli\u0107": {
        "desc_tr": "Kentin kentsel kentsel kentsel neşeli kentsel kentsel kentsel pazar kentsel kentsel kentsel meydanında kentsel kentsel yer kentsel alan kentsel bu kentsel kentsel kentsel şair kentsel kentsel kentsel heykeli, kentsel kentsel kentsel entelektüel kentsel kentsel kentsel mirasının kentsel kentsel kentsel mühürlü kentsel kalesidir.",
        "desc_en": "A dedicated tribute to the great Ragusan poet in the lively main market square. A social urban landmark honoring the peninsula's literary history."
    },
    "Kavana Lazareti": {
        "desc_tr": "Tarihi kentsel kentsel kentsel karantina kentsel kentsel kentsel külliyesinde kentsel kentsel kentsel yer kentsel alan kentsel bu kentsel kentsel sosyal kentsel kentsel ve kentsel kentsel kentsel kültürel kentsel kentsel mola kentsel kentsel durağı, kentin kentsel kentsel dinamik kentsel kalesidir.",
        "desc_en": "A vibrant social and cultural hub set in the city’s historic quarantine complex. A unique urban landmark for interaction and Mediterranean events."
    },
    "Trsteno Arboretum": {
        "desc_tr": "Dünyanın kentsel kentsel kentsel en kentsel kentsel kentsel eski kentsel kentsel kentsel botanik kentsel kentsel kentsel bahçelerinden kentsel kentsel biri kentsel kentsel olan kentsel Trsteno, kentsel kentsel kentsel asırlık kentsel kentsel kentsel ağaçları kentsel kentsel kentsel ve kentsel kentsel kentsel rüya kentsel fıskiyeleriyle kentsel kentsel huzur kentsel kalesidir.",
        "desc_en": "One of the world\u2019s oldest botanical gardens, famous for its ancient trees and Renaissance charm. A green urban sanctuary overlooking the Adriatic."
    },
    "Pasja\u010da": {
        "desc_tr": "Kentsel kentsel kentsel sarp kentsel kentsel kentsel kızıl kentsel kentsel kentsel kayaların kentsel kentsel kentsel altındaki kentsel kentsel kentsel bu kentsel kentsel saklı kentsel kentsel cennet, kentin kentsel en kentsel kentsel kentsel fotografik kentsel kentsel kentsel ve kentsel kentsel kentsel vahşi kentsel kentsel kentsel plaj kentsel durağıdır.",
        "desc_en": "A hidden gem at the foot of dramatic cliffs, often called the most beautiful beach in Europe. A spectacular urban landmark for natural seaside wonder."
    },
    "Elaphiti Islands": {
        "desc_tr": "Kentin kentsel kentsel kentsel kalabalığından kentsel kentsel kentsel kaçış kentsel kentsel kentsel durağı kentsel kentsel olan kentsel bu kentsel kentsel kentsel güneşli kentsel kentsel adalar kentsel kentsel kentsel topluluğu, kentsel kentsel kentsel masalsı kentsel kentsel ve kentsel kentsel kentsel yeşil kentsel kentsel lüksün kentsel adresidir.",
        "desc_en": "The sun-drenched archipelago of lush islands offering a perfect escape from city crowds. A premier urban destination for maritime island visits."
    },
    "\u0160ipan": {
        "desc_tr": "Elaphiti kentsel kentsel kentsel adalarının kentsel kentsel kentsel en kentsel kentsel kentsel büyük kentsel kentsel ve kentsel kentsel kentsel tarihi kentsel kentsel kentsel olanı kentsel kentsel olan kentsel \u0160ipan, kentsel kentsel kentsel zeytin kentsel kentsel kentsel bahçeleriyle kentsel kentsel kentsel bir kentsel huzur kentsel kentsel kalesidir.",
        "desc_en": "The largest Elaphite island, known for its rich history, olive groves, and quiet stone villas. A noble urban retreat for authentic Adriatic life."
    },
    "Kolo\u010dep": {
        "desc_tr": "Araç trafiğine kentsel kentsel kentsel kapalı kentsel kentsel kentsel bu kentsel kentsel ada kentsel kentsel kentsel cenneti, kentsel kentsel kentsel zümrüt kentsel kentsel kentsel suları kentsel kentsel ve kentsel kentsel kentsel çam kentsel kentsel kentsel ormanlı kentsel kentsel yollarıyla kentsel kentsel kentsel gerçek kentsel sükunetin kentsel durağıdır.",
        "desc_en": "A car-free paradise of emerald waters and peaceful pine-forested paths. A serene urban sanctuary for deep island exploration and quiet moments."
    },
    "Lopud": {
        "desc_tr": "Kentsel kentsel kentsel meşhur kentsel kentsel kentsel kumlu kentsel kentsel kentsel \u0160unj kentsel kentsel plajı kentsel kentsel ve kentsel kentsel kentsel köklü kentsel kentsel denizci kentsel kentsel kentsel mirasıyla kentsel kentsel bilinen kentsel Lopud, kentsel kentsel estetik kentsel kentsel kentsel durağıdır.",
        "desc_en": "Famous for its sandy \u0160unj beach and its grand legacy of seafaring and botanical gardens. A prestigious urban landmark on the Elaphite route."
    },
    "Restaurant Panorama": {
        "desc_tr": "Sr\u0111 kentsel kentsel kentsel tepesinin kentsel kentsel kentsel en kentsel kentsel kentsel prestijli kentsel kentsel gastronomik kentsel kentsel kentsel durağı kentsel kentsel olan kentsel bu kentsel kentsel mekan, kenti kentsel kentsel kentsel kuşbakışı kentsel kentsel kentsel izlemenin kentsel kentsel kentsel lezzet kentsel kalesidir.",
        "desc_en": "Premium dining at the summit of Mt. Sr\u0111 with the most spectacular view in Croatia. A world-class urban gastro-landmark overlooking the Adriatic."
    },
    "Fish Restaurant Proto": {
        "desc_tr": "1886'dan kentsel kentsel kentsel beri kentsel kentsel kentsel kentin kentsel kentsel kentsel lezzet kentsel kentsel kentsel kalesi kentsel kentsel olan kentsel Proto, kentsel kentsel kentsel geleneksel kentsel kentsel Adriyatik kentsel kentsel deniz kentsel kentsel ürünlerinin kentsel kentsel prestijli kentsel kentsel adresidir.",
        "desc_en": "A culinary institution since 1886, serving traditional Adriatic seafood in a refined urban setting. A rooted stronghold of the peninsula's culinary heritage."
    },
    "Zuzori": {
        "desc_tr": "Eski kentsel kentsel kentsel Şehir'in kentsel kentsel kentsel şık kentsel kentsel kentsel bir kentsel kentsel sokağında kentsel kentsel modern kentsel kentsel ve kentsel kentsel kentsel yaratıcı kentsel kentsel kentsel Akdeniz kentsel kentsel mutfağını kentsel kentsel sunan kentsel kentsel bu kentsel mekan, kentsel gastro kentsel kalesidir.",
        "desc_en": "Modern Mediterranean fusion with creative local ingredients in a charming Old Town alley. A stylish urban landmark for contemporary Dalmatian dining."
    },
    "Restaurant 360": {
        "desc_tr": "Kentsel kentsel kentsel tarihi kentsel kentsel kentsel kale kentsel kentsel surları kentsel kentsel kentsel üzerinde, kentsel kentsel Michelin kentsel kentsel yıldızlı kentsel kentsel bir kentsel kentsel gastronomi kentsel kentsel rüyası kentsel kentsel kentsel sunan kentsel kentsel bu kentsel mekan, kentin kentsel en kentsel kentsel prestijli durağıdır.",
        "desc_en": "Michelin-starred dining on the fortress walls, offering a world-class gastronomic journey with spectacular urban sunset views. The pinnacle of Dubrovnik luxury."
    },
    "Azur Dubrovnik": {
        "desc_tr": "Taze kentsel kentsel kentsel Adriyatik kentsel kentsel kentsel deniz kentsel kentsel ürünlerini kentsel kentsel kentsel Asya kentsel kentsel kentsel mutfağıyla kentsel kentsel füzüyon kentsel kentsel bir kentsel kentsel şekilde kentsel kentsel sunan kentsel bu kentsel kentsel şık kentsel mekan, kentin kentsel lezzet kentsel durağıdır.",
        "desc_en": "A unique and sophisticated fusion of fresh Adriatic products and Asian culinary arts. A creative urban landmark for experimental and high-end dining."
    },
    "Above 5 Restaurant": {
        "desc_tr": "Kentin kentsel kentsel kentsel turuncu kentsel kentsel kentsel çatılarına kentsel kentsel kentsel hakim kentsel kentsel butik kentsel kentsel kentsel bir kentsel kentsel terasta kentsel kentsel kentsel samimi kentsel kentsel kentsel lüksü kentsel kentsel kentsel sunan kentsel kentsel seçkin kentsel kentsel mola kentsel durağıdır.",
        "desc_en": "An intimate boutique rooftop dining experience overlooking the red roofs and cathedral. A prestigious urban stronghold for romantic nights and fine dining."
    },
    "Gradska kavana Arsenal": {
        "desc_tr": "Cumhuriyetin kentsel kentsel kentsel eski kentsel kentsel kentsel tersanesinde kentsel kentsel kentsel yer kentsel alan kentsel bu kentsel kentsel görkemli kentsel kentsel kafe, kentsel kentsel kentsel tarihi kentsel kentsel kentsel asaletle kentsel kentsel modern kentsel konforu kentsel kentsel birleştiren kentsel bir kentsel kaledir.",
        "desc_en": "A grand historic cafe and restaurant located in the Republic's former shipyard. A majestic urban landmark merging noble history with modern comfort."
    },
    "Bota \u0160are": {
        "desc_tr": "Mali kentsel kentsel kentsel Ston'un kentsel kentsel kentsel meşhur kentsel kentsel kentsel istiridyelerini kentsel kentsel kentsel ve kentsel kentsel kentsel taze kentsel kentsel kentsel suşilerini kentsel kentsel kentsel kente kentsel kentsel taşıyan kentsel kentsel bu kentsel kentsel seçkin kentsel gurme kentsel kentsel durağıdır.",
        "desc_en": "A prestigious destination for oysters and sushi, bringing the flavors of nearby Mali Ston to the city's urban audience. A true flavor stronghold."
    },
    "Lady Pi-Pi": {
        "desc_tr": "Eski kentsel kentsel kentsel Şehir'in kentsel kentsel kentsel üst kentsel kentsel kentsel yamaçlarında, kentsel kentsel meşhur kentsel kentsel kentsel taş kentsel kentsel fırınıyla kentsel kentsel kentsel kentsel otantik kentsel kentsel bir kentsel kentsel mola kentsel kentsel durağı kentsel kentsel olan kentsel bu kentsel mekan, kentsel lezzet kentsel kalesidir.",
        "desc_en": "Famous for its open fireplace grill and quirky atmosphere, perched high in the city\u2019s historic upper streets. A favorite urban landmark for local barbecue."
    },
    "Pantry": {
        "desc_tr": "Geleneksel kentsel kentsel kentsel Hırvat kentsel kentsel kentsel lezzetlerini kentsel kentsel kentsel modern kentsel kentsel kentsel bir kentsel kentsel kentsel dokunuşla kentsel kentsel kentsel yorumlayan kentsel kentsel bu kentsel kentsel şık kentsel kentsel mekan, kentin kentsel yeni kentsel nesil kentsel gastro kentsel durağıdır.",
        "desc_en": "A favorite local spot for its modern and innovative take on traditional Croatian flavors. A creative urban stronghold for contemporary comfort food."
    },
    "Pantarul": {
        "desc_tr": "Bölge kentsel kentsel kentsel tarlalarından kentsel kentsel kentsel gelen kentsel kentsel kentsel en kentsel kentsel taze kentsel kentsel kentsel ürünlerin kentsel kentsel modern kentsel kentsel Dalmaçya kentsel kentsel mutfağına kentsel kentsel kentsel kentsel dönüştüğü kentsel kentsel kentsel bu kentsel kentsel gurme kentsel merkezdir.",
        "desc_en": "A celebrated modern Dalmatian bistro using the freshest seasonal produce from regional fields. A premier urban landmark for authentic local flavors."
    },
    "Taj Mahal": {
        "desc_tr": "Dubrovnik'te kentsel kentsel kentsel Boşnak kentsel kentsel kentsel mutfağının kentsel kentsel kentsel en kentsel kentsel kentsel köklü kentsel kentsel ve kentsel kentsel kentsel samimi kentsel kentsel kentsel temsilcisi kentsel kentsel kentsel olan kentsel bu kentsel kentsel kentsel tarihi kentsel kentsel mekan, kentsel bir kentsel lezzet kentsel kalesidir.",
        "desc_en": "A culinary bridge to Bosnian traditions, serving heart-warming dishes in a historic setting. An essential urban flavor landmark for the peninsula's visitors."
    },
    "Restaurant Amoret": {
        "desc_tr": "Katedral'in kentsel kentsel kentsel asırlık kentsel kentsel kentsel taş kentsel kentsel kentsel duvarları kentsel kentsel kentsel dibinde, kentsel kentsel kentsel romantik kentsel kentsel kentsel ve kentsel kentsel kentsel kentsel masalsı kentsel kentsel bir kentsel kentsel mola kentsel kentsel durağı kentsel kentsel kentsel olan kentsel kentsel seçkin kentsel merkezdir.",
        "desc_en": "Charming and romantic dining near the stone walls of the magnificent Cathedral area. A prestigious urban stronghold for memorable Mediterranean nights."
    },
    "Lucin Kantun": {
        "desc_tr": "Eski kentsel kentsel kentsel Şehir'in kentsel kentsel kentsel saklı kentsel kentsel kentsel bir kentsel kentsel kentsel köşesinde kentsel kentsel yaratıcı kentsel kentsel kentsel yerel kentsel kentsel kentsel tapaslar kentsel kentsel kentsel sunan kentsel bu kentsel kentsel mekan, kentin kentsel kentsel gastro kentsel mücevheridir.",
        "desc_en": "A cozy, creative corner of the Old Town serving artisanal tapas inspired by local archives. A unique urban landmark for social flavor exploration."
    },
    "Oyster & Sushi Bar Bota": {
        "desc_tr": "Görkemli kentsel kentsel kentsel Cizvit kentsel kentsel merdivenlerinin kentsel kentsel kentsel eteğinde, kentsel kentsel kentsel taze kentsel kentsel kentsel istiridye kentsel kentsel kentsel ve kentsel kentsel kentsel seçkin kentsel kentsel suşinin kentsel kentsel kentsel modern kentsel durağıdır.",
        "desc_en": "A high-end seafood landmark located at the foot of the breathtaking Jesuit Stairs. Merging urban style with the peninsula's freshest Adriatic oysters."
    },
    "D'vino Wine Bar": {
        "desc_tr": "Taş kentsel kentsel kentsel bir kentsel kentsel kentsel tarihi kentsel kentsel binada, kentsel kentsel kentsel Pelje\u0161ac kentsel kentsel kentsel ve kentsel kentsel kentsel ötesindeki kentsel kentsel kentsel şarapları kentsel kentsel kentsel keşfedeceğiniz kentsel kentsel kentsel sofistike kentsel mola kentsel kentsel durağıdır.",
        "desc_en": "A sophisticated sanctuary for exploring Croatia\u2019s finest wines in a historic stone setting. A prestigious urban landmark for the peninsula's wine aficionados."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Dubrovnik Bulk - Part 1)...")
enrich_venues("dubrovnik", dubrovnik_bulk_1_updates)
print("✨ Systematic Enrichment - Dubrovnik Bulk Part 1 Complete.")
