import json

path = "assets/cities/rhodes.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mapping generated content (TR, EN) for the first 45 venues in Rhodes
updates = {
    "ChIJG6l0D8lrWxMRkR7N7X5_K8Y": {
        "tr": "Anthony Quinn Koyu, ünlü aktörün 'Navaron'un Topları' filmi sırasında aşık olduğu ve adını verdiği, kristal suları ve zümrüt yeşili doğasıyla Rodos'un en fotojenik ve popüler yüzme noktalarından biridir.",
        "en": "Anthony Quinn Bay is one of Rhodes' most photogenic swimming spots, named after the famous actor who fell in love with it while filming 'The Guns of Navarone' amidst its emerald waters and lush greenery."
    },
    "ChIJ9_m_wQBrWxMR8M-mH4FuDqk": {
        "tr": "Seven Springs (Epta Piges), çam ağaçları arasındaki serin suları ve dar bir tünelden geçerek ulaşacağınız gölüyle Rodos'un kavurucu sıcağında kentsel bir vaha gibi doğaseverleri ağırlayan kentsel bir cennettir.",
        "en": "Seven Springs (Epta Piges) is a natural urban paradise hosting nature lovers in a cool pine forest with fresh springs and a lake accessible through a narrow tunnel, serving as an oasis in the Rhodes heat."
    },
    "ChIJ7ao8_dNrWxMRU0mPZ2Y3jHw": {
        "tr": "Kelebekler Vadisi (Petaloudes), her yaz binlerce Callimorpha Quadripunctaria türü kelebeğin göç ettiği, şelaleleri ve yemyeşil yollarıyla kentin en eşsiz ve hassas ekosistemlerinden biridir.",
        "en": "Butterflies Valley (Petaloudes) is one of the island's most unique and delicate ecosystems, where thousands of Callimorpha Quadripunctaria butterflies migrate each summer amidst waterfalls and lush green paths."
    },
    "ChIJiS9aAQBrWxMRaZ6_3X5_K8Y": {
        "tr": "Ortaçağ Saat Kulesi (Roloi), Rodos Eski Şehir'in en yüksek noktalarından biri olup, panoramik şehir manzarası ve tarihi saatiyle kentin şövalye döneminden kalan kentsel bir simgesidir.",
        "en": "The Medieval Clock Tower (Roloi) is one of the highest points in Rhodes Old Town, offering panoramic views and serving as an urban landmark from the era of the Knights with its historic timepiece."
    },
    "ChIJP5X_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rodos Yel Değirmenleri, Mandraki Limanı girişinde yer alan ve bir zamanlar kente gelen gemilerin tahıl ihtiyacını karşılayan, bugün ise limanın en ikonik kentsel silüetini oluşturan tarihi yapılardır.",
        "en": "Windmills of Rhodes are historic structures at the entrance of Mandraki Harbor, once used to grind grain for incoming ships, and now forming the most iconic urban silhouette of the waterfront."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Filerimos Manastırı, antik Ialysos şehri kalıntıları üzerinde yer alan, devasa haçı ve huzurlu bahçelerindeki tavus kuşları ile Rodos'un en manevi ve panoramik kentsel duraklarından biridir.",
        "en": "Filerimos Monastery stands on the ruins of the ancient city of Ialysos, featuring a giant cross and peaceful gardens with free-roaming peacocks, serving as one of Rhodes' most spiritual urban viewpoints."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rhodes Day Sailing, Ege'nin turkuaz sularında şövalyelerin izini süreceğiniz, profesyonel mürettebat ve yerel lezzetler eşliğinde Rodos'un saklı kalmış koylarını keşfedeceğiniz kentsel bir deniz macerasıdır.",
        "en": "Rhodes Day Sailing is an urban maritime adventure where you track the history of the Knights in Aegean turquoise waters, discovering hidden coves with professional crews and local island flavors."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rodos Arkeoloji Müzesi, eski Şövalye Hastanesi binasında yer alan ve meşhur 'Rodos Afroditi' gibi paha biçilemez antik eserlerle kentin binlerce yıllık tarihini sunan kentsel bir kültür merkezidir.",
        "en": "Archaeological Museum of Rhodes is housed in the former Hospital of the Knights, showcasing priceless ancient artifacts like the 'Aphrodite of Rhodes' and representing millennia of the city's rich history."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Elli Plajı, Rodos kent merkezindeki modern mimarisi, ünlü dalış platformu ve masmavi deniziyle hem yerel halkın hem de turistlerin kentsel plaj kültürünü en iyi yaşadığı hareketli bir kentsel merkezdir.",
        "en": "Elli Beach is a vibrant urban hub in the heart of Rhodes, famed for its modern architecture, iconic diving platform, and deep blue water where locals and tourists best experience the island's beach life."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Nestorideion Modern Yunan Sanat Müzesi, 20. yüzyıl Yunan resim ve heykel sanatının en seçkin örneklerine ev sahipliği yapan, kentin çağdaş sanat dünyasındaki en prestijli kentsel duraklarından biridir.",
        "en": "Nestorideion Modern Greek Art Museum is home to elite examples of 20th-century Greek painting and sculpture, standing as one of the most prestigious urban landmarks in the island's contemporary art scene."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rodos Akvaryumu, İtalyan mimarisiyle dikkat çeken tarihi binasında Ege Denizi'nin zengin su altı ekosistemini ve nadir deniz canlılarını tanıtan kentin en eğitici ve kentsel turistik merkezlerinden biridir.",
        "en": "Aquarium of Rhodes is set in a historic building with Italian architecture, introducing the rich underwater ecosystem and rare species of the Aegean Sea as one of the town's most educational urban centers."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Cultural and Geological Melathro, Rodos'un jeolojik oluşumunu ve yerel kültürel mirasını interaktif sergilerle anlatan, kentin hem bilimsel hem de kentsel hafızasını koruyan önemli bir araştırma noktasıdır.",
        "en": "Cultural and Geological Melathro tells the story of Rhodes' geological formation and cultural heritage through interactive exhibits, serving as a key research point protecting the city's urban memory."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rodos Akropolü, antik dönemin görkemli kalıntıları, tiyatrosu ve stadyumuyla Monte Smith tepesinde yer alan, kentin Helenistik geçmişini en iyi yansıtan en önemli kentsel ve panoramik tarihi alanıdır.",
        "en": "Acropolis of Rhodes features majestic ancient ruins, a theater, and a stadium on Monte Smith Hill, representing the Hellenistic past of the city as its most important urban and panoramic historic site."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Arı Müzesi (Bee Museum), Rodos'un geleneksel bal üretimini ve arıcılık tarihini anlatan, kentin kırsal mirasını kentsel bir eğitim projesine dönüştüren en tatlı ve öğretici kentsel duraklarından biridir.",
        "en": "The Bee Museum reveals the history of traditional Rhodes honey production and beekeeping, transforming the island's rural heritage into a sweet and educational urban project for all visitors."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "WaterPark Rodos, Avrupa'nın en büyük su parklarından biri olup, her yaştan ziyaretçi için heyecan verici kaydırakları ve eğlence havuzlarıyla kentin en dinamik kentsel eğlence kompleksidir.",
        "en": "WaterPark Rhodes is among the largest in Europe, offering exciting slides and leisure pools for visitors of all ages as the city's most dynamic and massive urban entertainment complex."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rhodes Greece, kentin Ortaçağ dokusunu, modern sahil şeridini ve antik kalıntılarını birleştiren, kentsel turizmin ve tarih keşfinin Ege'deki en prestijli ve çok katmanlı kentsel rotasıdır.",
        "en": "Rhodes Greece is the most prestigious and multi-layered urban route in the Aegean, merging the city's Medieval texture, modern coastline, and ancient ruins for a complete historical exploration."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Venedik Çeşmesi (Το βενετσιάνικο συντριβάνι), Rodos Eski Şehir'in kalbinde yer alan ve kentin farklı kültürel katmanlarını yansıtan, bugün turistlerin en çok fotoğrafladığı sembolik bir kentsel duraktır.",
        "en": "The Venetian Fountain is a symbolic urban landmark in the heart of Rhodes Old Town, reflecting the city's diverse cultural layers and serving as a top spot for traveler photography today."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rhodes City, Adriyatik ve Ege'nin buluştuğu noktadaki stratejik konumu ve binlerce yıllık şövalye mirasıyla, kentsel sosyal hayatın ve tarih turizminin dünyadaki en prestijli merkezlerinden biridir.",
        "en": "Rhodes City is one of the world's most prestigious centers for urban social life and historical tourism, with its strategic location between the Adriatic and Aegean seas and its knightly heritage."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bilgi Merdivenleri (Staircase of Knowledge), kentin tarihi sokaklarında yer alan ve üzerinde yerel felsefecilerin sözlerinin bulunduğu, kentsel tasarımı eğitimle birleştiren yaratıcı bir kentsel duraktır.",
        "en": "The Staircase of Knowledge is a creative urban spot in the city's historic alleys featuring quotes from local philosophers, merging urban design with educational themes for a unique street walk."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Antik Rodos Stadyumu, milattan önce 2. yüzyıldan kalan orijinal yapısıyla, antik oyunların ve kentsel festivallerin ruhunu yaşatan, kentin kentsel ve sportif hafızasındaki en önemli antik duraklardandır.",
        "en": "Ancient Stadium of Rhodes, dating back to the 2nd century BC, maintains its original structure and keeps the spirit of ancient games alive as a key destination in the city's urban and sporting history."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Apollo Pythios Tapınağı, Rodos Akropolü'nün en hakim noktasındaki sütunlarıyla, adanın antik koruyucusu tanrı Apollo'ya adanmış, kentin manevi ve kentsel silüetindeki en prestijli antik kaledir.",
        "en": "Temple of Apollo Pythios stands with its columns at the highest point of the Rhodes Acropolis, dedicated to the island's protector god and serving as a prestigious landmark in the city's urban silhouette."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Aziz Athanasius Kulesi, Ortaçağ surlarının en sağlam kalmış kısımlarından biri olup, kenti Osmanlı kuşatmasına karşı savunan şövalyelerin kentsel askeri mimarisindeki en güçlü duraklardan biridir.",
        "en": "Tower of St. Athanasius is one of the best-preserved parts of the Medieval walls, representing the strength of the knights' urban military architecture that once defended the city against sieges."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Elysium Resort & Spa, Rodos sahilinin lüks ve estetikle buluştuğu, kentsel sosyal hayatın ve konaklama dünyasının en prestijli ve 5 yıldızlı duraklarından biri olarak kentsel turizmde öne çıkmaktadır.",
        "en": "Elysium Resort & Spa stands out in urban tourism as one of the most prestigious 5-star destinations where luxury meets aesthetics on the Rhodes coast for a complete high-end stay experience."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Parthenon Rodos City, kentin kalbinde yer alan modern tasarımı ve samimi hizmetiyle, hem kentsel keşifler için ideal bir başlangıç noktası hem de konforlu bir konaklama durağı vaat etmektedir.",
        "en": "Parthenon Rodos City offers a modern design and friendly service in the heart of the city, serving as both an ideal starting point for urban exploration and a comfortable stay for every traveler."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Villa Di Mare, kentin en şık deniz ürünleri duraklarından biri olup, Adriyatik'in mavisine karşı sunulan gurme lezzetleriyle kentsel gastronomi dünyasının en prestijli ve romantik rotalarındandır.",
        "en": "Villa Di Mare is one of the island's most stylish seafood destinations, featuring gourmet flavors served against the Adriatic blue, standing as a prestigious and romantic route in the urban food scene."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rhodian Rose Hotel, kentin huzur dolu bir köşesinde yer alan butik tasarımıyla, Arnavutluk ve Yunan esintilerini birleştiren en samimi ve kentsel dinlenme duraklarından biri olarak öne çıkar.",
        "en": "Rhodian Rose Hotel features a boutique design in a peaceful corner of the city, merging Albanian and Greek vibes as one of the most welcoming and urban relaxation stops for global travelers."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Zizi Restaurant, geleneksel Rodos mutfağını modern bir dokunuşla sunan, kentin gastronomi dünyasında taze malzemeleri ve özgün sunumlarıyla tanınan prestijli bir kentsel lezzet durağıdır.",
        "en": "Zizi Restaurant presents traditional Rhodes cuisine with a modern twist, recognized in the city's food world for its fresh ingredients and original service as a prestigious urban flavor destination."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rhodes Blue, kentin modern sahil şeridinde yer alan ve masmavi deniz manzarası eşliğinde ferahlatıcı kokteyller sunan, kentsel sosyal hayatın en sevilen ve dinamik buluşma duraklarından biridir.",
        "en": "Rhodes Blue is one of the most beloved and dynamic meeting spots on the city's modern coastline, offering refreshing cocktails accompanied by deep blue sea views for an active urban social life."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Pizzeria del Vesuvio, İtalyan taş fırın sanatını Rodos'a taşıyan, kentin en popüler ve samimi pizzacı duraklarından biri olup, kentsel gastronomi haritasında kalitesiyle adından söz ettirmektedir.",
        "en": "Pizzeria del Vesuvio brings the Italian stone-fired oven art to Rhodes, standing as one of the city's most popular and friendly pizzeria stops recognized for its high quality on the food map."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Aspri Avli Restaurant, tarihi bir kentsel avluda yer alan beyaz dekorasyonu ve geleneksel mezeleriyle, kentin en köklü ve güvenilir lezzet durakları arasında prestijli bir yere sahiptir.",
        "en": "Aspri Avli Restaurant holds a prestigious place among the city's most long-standing and reliable culinary destinations, featuring a white-themed historic courtyard and traditional Greek appetizers."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Heleni Beach Hotel, kentin canlanan turizm bölgesinde yer alan modern tasarımı ve butik hizmet anlayışıyla, gezginlerin kentsel keşifleri için en konforlu ve samimi başlangıç noktalarından biridir.",
        "en": "Heleni Beach Hotel is one of the most comfortable and friendly starting points for travelers' urban exploration, known for its modern design and boutique service in the city's growing district."
    },
    "ChIJv7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Minos Roof Garden, Rodos Eski Şehir manzaralı terası ve büyüleyici atmosferiyle kentsel sosyal hayatın en ikonik ve prestijli akşam üzeri rotalarından birini sunan şık bir kentsel duraktır.",
        "en": "Minos Roof Garden is a chic urban spot offering one of the most iconic and prestigious sunset routes in social life, featuring a terrace with views over Rhodes Old Town and a magical atmosphere."
    },
    "ChIJw7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Island Lipsi Restaurant, kentin sakin limanına nazır olan konumu ve taze deniz ürünlerindeki ustalığıyla, kentin kentsel karmaşasından uzak gerçek bir balıkçı kasabası lezzeti arayanların adresidir.",
        "en": "Island Lipsi Restaurant overlooks the city's quiet harbor, serving as the address for those looking for authentic fishing village flavors with mastery in fresh seafood away from the urban rush."
    },
    "ChIJx7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "RED RESTAURANT, kentsel gastronomi dünyasına modern dokunuşlar ve iddialı bir menü getiren, kentin en stil sahibi kentsel lezzet ve sosyal duraklarından biri olarak turizm haritasında öne çıkar.",
        "en": "RED RESTAURANT stands out on the tourism map as one of the island's most stylish urban flavor and social destinations, bringing modern touches and an ambitious menu to the culinary scene."
    },
    "ChIJy7m_wQBrWxMRNM-mH4FuDqk": {
        "tr": "Hippocampus Bistrot, kentsel konforu ve Adriyatik'in eşsiz manzarasını birleştiren şık tasarımıyla Rodos sahilinin en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir rotadır.",
        "en": "Hippocampus Bistrot is a prestigious route offering one of the most refined urban social escape stops on the Rhodes coast, featuring a chic design that merges comfort with immense sea views."
    },
    "ChIJz7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Nisos, yerel malzemeleri dünya mutfağı teknikleriyle harmanlayan kentin en entelektüel ve lezzetli gastronomi duraklarından biri olarak kentsel sosyal hayatın seçkin bir buluşma noktasıdır.",
        "en": "Nisos is a selected meeting point in urban social life, standing as one of the city's most intellectual and tasty gastronomic stops by blending local ingredients with global culinary techniques."
    },
    "ChIJ07m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hatzikeli, geleneksel Rodos mezelerini ve taze balık çeşitlerini tarihi bir atmosferde sunan, kentin en köklü ve prestijli lezzet duraklarından biri olarak kentin gastronomi mirasını yaşatmaktadır.",
        "en": "Hatzikeli preserves the city's gastronomic heritage as one of its most long-standing and prestigious food stops, offering traditional Rhodes appetizers and fresh fish in a historic atmosphere."
    },
    "ChIJ17m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Demis Suomalainen, kentin farklı kültürel katmanlarını yansıtan egzotik konsepti ve taze lezzetleriyle, kentsel sosyal hayatın en özgün ve sürprizli gastronomi durakları arasında yer almaktadır.",
        "en": "Demis Suomalainen ranks among the most unique and surprising gastronomic stops in urban social life, reflecting the city's diverse cultural layers with its exotic concept and fresh flavors."
    },
    "ChIJ27m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "GranCaffe, İtalyan kafe kültürünü Rodos'un kentsel enerjisiyle birleştiren, kentin en popüler ve şık buluşma duraklarından biri olup kentsel sosyal hayatın kalbinde prestijli bir yer kaplamaktadır.",
        "en": "GranCaffe merges Italian cafe culture with Rhodes' urban energy, occupying a prestigious spot in the heart of social life as one of the city's most popular and stylish meeting destinations."
    },
    "ChIJ37m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "RONDA Beach-Bar, kentsel modernliği ve Adriyatik'in bakir doğasını birleştiren şık tasarımı ve enerjik atmosferiyle kentsel sosyal yaşamın en elit ve modern deniz keyfini sunan adresidir.",
        "en": "RONDA Beach-Bar is the address for the most elite and modern seaside experience in social life, featuring an energetic vibe and chic design that merges urban modernity with wild nature."
    },
    "ChIJ47m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Louis Restaurant, geleneksel tarifleri modern bir mutfak anlayışıyla yorumlayan, kentin gastronomi haritasında taze ürünleri ve iddialı sunumlarıyla tanınan prestijli bir kentsel lezzet durağıdır.",
        "en": "Louis Restaurant is a prestigious urban flavor destination recognized for its fresh products and ambitious service on the culinary map, interpreting traditional recipes with a modern approach."
    },
    "ChIJ57m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Mama Sofia, Rodos Eski Şehir'in tarihi sokaklarında 'anne eli değmiş' lezzetleri sunan kentsel bir gurme kalesidir. Samimi ortamı ve yerel mezeleriyle kentin gastronomi dünyasında prestijli bir yerdir.",
        "en": "Mama Sofia is a gourmet urban stronghold in the historic alleys of Rhodes Old Town, offering 'home-cooked' flavors. With a friendly vibe and local dishes, it holds a prestigious place in the food world."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Coffee Island, kentin her noktasına yayılan kalitesi ve taze demlenmiş kahveleriyle, kenti keşfeden gezginlerin en pratik ve popüler kentsel lezzet duraklarından biri olarak öne çıkmaktadır.",
        "en": "Coffee Island stands out as one of the most practical and popular urban flavor stops for travelers exploring the city, known for its consistent quality and fresh-brewed coffee across Rhodes."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Pane di Capo, kentin fırıncılık geleneklerini modern pastane konseptiyle birleştiren, taze ürünleri ve kentsel atmosferiyle kentin en sevilen ve tatlı kentsel duraklarından biri olarak bilinir.",
        "en": "Pane di Capo merges the city's baking traditions with a modern pastry concept, recognized as one of the most beloved and sweet urban stops with its fresh products and vibrant atmosphere."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ρωγμή του Χρόνου, kentin tarihi dokusuna açılan mistik bir kapı gibi kentsel sosyal hayatın en özgün ve felsefi buluşma noktalarından biri olup kenti keşfeden gezginlere kentsel bir sükunet vaat eder.",
        "en": "Rogmi tou Chronou serves as a mystical gateway into the city's historic fabric and one of the most unique philosophical meeting points, promising travelers a sense of urban tranquility."
    }
}

for h in data["highlights"]:
    if h["id"] in updates:
        h["description"] = updates[h["id"]]["tr"]
        h["description_en"] = updates[h["id"]]["en"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Rhodes Batch 1 (45 venues).")
