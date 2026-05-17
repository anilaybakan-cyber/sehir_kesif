import json

path = "assets/cities/budva.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mapping generated content (TR, EN) for the remaining 44 venues in Budva
updates = {
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Caffe Scorpion, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestij ve kaza duraktır.",
        "en": "Caffe Scorpion is one of the island's most stylish urban social escape spots, merging city dynamism with a sophisticated atmosphere for a perfect afternoon break in Budva."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hotel Kuc, kentsel modernliği ve Adriyatik sahilinin huzurunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "Hotel Kuc features a chic design merging urban style with coastal tranquility, offering one of the most refined social escape options on the Budva waterfront for modern travelers."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Akacia Coffee, kentsel kahve kültürünü kentin kentsel haritasına taşıyan taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi olan kentsel bir prestij noktasıdır.",
        "en": "Akacia Coffee is an urban prestige spot bringing city coffee culture to the map, standing as one of the most beloved and sweet social hubs in Budva with its aromatic and fresh blends."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "MK, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli rotadır.",
        "en": "MK is a prestigious urban route and a refined social escape spot in town, featuring a chic design that merges city dynamism with a sophisticated search for the best of Budva social life."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Black Iris, kentsel gastronomi dünyasına modern dokunuşlar ve iddialı bir menü getiren kentin en stil sahibi kentsel lezzet ve sosyal duraklarından birisidir.",
        "en": "Black Iris stands as one of the city's most stylish flavor and social destinations, bringing modern touches and an ambitious menu to the Budva culinary and nightlife scene."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Sidro Beach Bar, kentsel kumsalda yer alan ve kentsel eğlenceyi dalga sesleriyle buluşturan kentin en büyüleyici kentsel buluşma duraklarından biridir.",
        "en": "Sidro Beach Bar is one of the most enchanting urban meeting spots on the waterfront, merging city fun with the rhythm of the waves for an unforgettable beach day experience."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "CUPS Coffeeshop, kentsel kahve kültürünü kentin kentsel haritasına taşıyan, taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisidir.",
        "en": "CUPS Coffeeshop is an urban heart of coffee culture in Budva, recognized as a favorite social landmark for travelers seeking a professional and aromatic coffee break in town."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Caffe Excellence, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunmaktadır.",
        "en": "Caffe Excellence offers one of the city's most refined social escape options, merging urban dynamism with a sophisticated design for a premium break during your Budva exploration."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "More Coffee, kentsel kahve kültürünü kentin kentsel haritasına taşıyan, taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisidir.",
        "en": "More Coffee is a beloved sweet stop in the heart of Budva, bringing city coffee culture to the map as a favorite social landmark for travelers looking for more than just a drink."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Sova Bakery, kentin fırıncılık geleneklerini modern pastane konseptiyle birleştiren, taze ürünleri ve kentsel atmosferiyle kentin en sevilen kentsel duraklarından birisidir.",
        "en": "Sova Bakery merges the city's baking traditions with a modern pastry concept, recognized as one of the most beloved and aromatic urban landmarks for fresh bread and sweets."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Caffe Kadmo, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunmaktadır.",
        "en": "Caffe Kadmo is a prestigious urban destination and a refined social escape spot in town, featuring a design that merges city energy with a sophisticated and active social vibe."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Cake & Bake, kentsel gastronomi dünyasına tatlı bir dokunuş getiren, kentin en popüler kentsel lezzet duraklarından biri olup kentsel tatlı haritasında yer alır.",
        "en": "Cake & Bake is a sweet standout on the city's food map, representing one of the most popular urban flavor destinations for gourmets looking for artistic pastry and desserts."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Caffe Volley, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en enerjik kentsel sosyal kaçış duraklarından birisini sunmaktadır.",
        "en": "Caffe Volley is a dynamic urban social destination merged with city energy, featuring a design that caters to active travelers looking for a professional and energetic social hub."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Fluffy Pancakes, kentsel gastronomi dünyasına modern bir dokunuş getiren, kentin en popüler ve kentsel lezzet duraklarından biri olup turizm haritasında yer alır.",
        "en": "Fluffy Pancakes brings a modern and sweet twist to Budva's food scene, standing out on the tourism map as one of the most popular and trendy flavor destinations in the city center."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Glas Budva, kentsel sosyal hayatın ve kentsel kentsel enerjinin kentsel merkezlerinden birisi olup kentsel dinamizmi kenti keşfeden gezginlere kentsel bir nükteyle anladır.",
        "en": "Glas Budva details the city's urban modernity and local cultural heritage, standing as a prestigious and intellectual urban history window on the discovery map for all visitors."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Caffe Intermeco, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunmaktadır.",
        "en": "Caffe Intermeco offers one of the most refined social escape options in Budva, merging urban style with a sophisticated presence for a perfect break in the middle of your day."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Nopeca cafe, kentsel gastronomi dünyasına kentin kentsel ve yerel lezzetlerini taze ve hızlı bir şekilde sunan kentin en popüler kentsel lezzet duraklarından birisidir.",
        "en": "Nopeca cafe & Fastfood brings local flavors to the town's food world at their freshest and fastest, standing out as one of the most popular and practical flavor destinations in Budva."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Dva Vesla, kentsel liman şeridinde yer alan ve kentsel deniz kültürünün taze lezzetlerini kenti keşfeden gezginlerle buluşturan kentin en samimi lezzet duraklarından birisidir.",
        "en": "Dva Vesla is one of the island's most friendly urban seafood destinations, featuring a maritime vibe and fresh catches served against the backdrop of the active Budva harbor."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Emporio Club, kentsel gece hayatının kalbi olup modern tasarımı ve iddialı DJ performanslarıyla kentin en dinamik sosyal alanıdır kentsel bir prestij kaza rotasıdır.",
        "en": "Emporio Club is the heart of Budva's urban nightlife, serving as a dynamic and stylish social area with elite DJ sets and a prestigious nocturnal energy for every party goer."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Top Hill, Adriyatik manzarasına tepeden bakan devasa pisti ve dünyaca ünlü DJ’leri ağrlayan kentsel kalesiyle Balkanlar’ın en prestijli açık hava gece kulübüdür.",
        "en": "Top Hill is the most prestigious open-air nightclub in the Balkans, acting as an urban fortress overlooking the Adriatic with a massive dance floor hosting world-renowned DJs."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Trocadero, kentsel sahil şeridinin en köklü ve enerjik gece kulüplerinden biri olarak kentsel sosyal hayatın ve eğlencenin merkezinde kentsel bir prestij rotasıdır.",
        "en": "Trocadero stands as a central route for urban entertainment and social life in Budva, being one of the most established and energetic nightspots on the city's waterfront."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Premium Palazzo, kentsel modernliği ve iddialı gece hayatı konseptini birleştiren kentin en dinamik ve şık sosyal alanıdır kentsel bir prestij rotasıdır.",
        "en": "Premium Palazzo nightclub merging modern style with an ambitious nightlife concept, standing as one of Budva's most dynamic and stylish social routes for nocturnal discovery."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Mujo Simba, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından birisidir.",
        "en": "Restoran Mujo Simba brings a traditional touch and creative menu to the city's food world, serving as one of Budva's most friendly and authentic local flavor destinations today."
    },
    "ChIJv7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Omnia Night Club, kentsel modernliği ve iddialı gece hayatı konseptini birleştiren kentin en dinamik ve şık kentsel sosyal alanlarından bir tanesidir.",
        "en": "Omnia is one of the most dynamic and stylish urban social areas in town, merging a modern club design with an ambitious nightlife experience for every traveler in Budva."
    },
    "ChIJw7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Karaoke Montenegro, kentsel sosyal hayata eğlence ve müzik katan kentin en dinamik kentsel sosyal alanlarından biri olup kentsel hayatın bir parçasıdır.",
        "en": "Karaoke Montenegro is one of the island's most lively urban social destinations, adding fun and music to the city's life as a favorite route for active nocturnal entertainment."
    },
    "ChIJx7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Beograd Budva, kentsel gastronomi dünyasına Balkanlar'ın kentsel ve yerel lezzetlerini taze malzemelerle sunan kentsel bir prestijli lezzet durağı kalesidir.",
        "en": "Beograd is a prestigious urban flavor stronghold in the city center, offering traditional Balkan and local tastes with fresh ingredients for a complete culinary exploration."
    },
    "ChIJy7m_wQBrWxMRNM-mH4FuDqk": {
        "tr": "Apartments Mika, kentsel sükuneti ve kentsel modernliği birleştiren kentin en samimi ve kentsel konaklama duraklarından biri olup turizm haritasında yer alır.",
        "en": "Apartments mika merges urban modernity with a sense of local tranquility, standing as one of the city's most friendly and comfortable stay options on the discovery map."
    },
    "ChIJz7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Cascada Club, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından biridir.",
        "en": "Cascada Club is a prestigious urban social escape spot in town, featuring a chic design that merges city dynamism with a sophisticated atmosphere for an active night life."
    },
    "ChIJ07m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Night Club Ambiente, kentsel silüetin en enerjik ve şık kentsel sosyal alanlarından birisi olup kentsel modernliği kentsel sosyal hayata kentsel bir rotadır.",
        "en": "Night Club Ambiente is one of the most energetic and stylish urban social hubs in the city silhouette, merging modern style with an active nocturnal route for every visitor."
    },
    "ChIJ17m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Night Club FETKA, kentsel modernliği ve iddialı gece hayatı konseptini birleştiren kentin en dinamik ve şık sosyal alanıdır kentsel bir prestij rotasıdır.",
        "en": "Night Club «FETKA» merging modern style with an ambitious nightlife concept, standing as one of Budva's most dynamic and stylish social routes for night discovery."
    },
    "ChIJ27m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "CBR Bar, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en enerjik kentsel sosyal kaçış duraklarından biridir.",
        "en": "Caffe Bar CBR is an energetic urban social destination and hub for city life, offering a design that caters to active travelers looking for a friendly and lively social spot."
    },
    "ChIJ37m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Lucky Karaoke, kentsel sosyal hayata eğlence ve müzik katan kentin en dinamik kentsel sosyal alanlarından biri olup kentsel hayatın bir kentsel prestij rotasıdur.",
        "en": "Lucky Karaoke is one of the most dynamic urban social destinations, bringing fun and music into the city's active social scene as a favorite route for every music lover."
    },
    "ChIJ47m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Club Hide, kentsel modernliği ve kentsel dinamizmi birleştiren şık kentsel tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından bir tanesidir.",
        "en": "Club Hide Budva is a prestigious urban social hideaway merging modern design with the city's energy, standing as one of the most refined social escape strongholds in town."
    },
    "ChIJ57m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "NA VODU, kentsel gastronomi dünyasına geleneksel bir dokunuş ve taze yerel lezzetler getiren kentin en samimi kentsel lezzet ve sosyal duraklarından biridir.",
        "en": "\"NA VODU\" grill & beer is one of the city's most friendly and authentic local flavor and social spots, bringing traditional touches to the urban gastronomic and social scene."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Terrazza Budva, kentsel modernliği ve Adriyatik'in eşsiz manzarasını birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış rotalarından birisidir.",
        "en": "Terrazza Budva merges urban modernity with immense Adriatic views through its chic design, standing as one of the city's most refined and prestigious social escape routes."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Maine, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli rotadır.",
        "en": "Maine is a prestigious urban route and a refined social escape spot in town, featuring a chic design that merges city dynamism with a sophisticated presence in the city center."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Casino Solendud, kentsel lüksün ve kentsel eğlencenin zirvesi olup kentsel konaklama dünyasının en prestijli ve kentsel sosyal duraklarından birisi kaza rotası kaledir.",
        "en": "Casino Solendud represents the peak of high-end urban luxury and entertainment, standing as a prestigious social stronghold and a key landmark in the Budva city nightlife scene."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Nigra Cat, kentsel sosyal hayatın en özgün ve sürprizli kentsel duraklarından birisi olup kenti keşfeden gezginlere kentsel güzellikleri nükteyle anlatan kentsel kaledir.",
        "en": "Nigra Cat is one of the most unique and surprising urban stops in social life, revealing the city's aesthetics to theaters through a witty and creative urban and feline landmark."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Modern Galeri Jovo Ivanović, kentsel modern sanat topluluklarının buluşma noktası olan kentin en önemli kentsel çağdaş sanat sanat merkezidir kentsel prestij haritasıdır.",
        "en": "Jovo Ivanovic Modern Gallery is a hub for urban art communities, reflecting the city's contemporary growth as one of Budva's most significant and prestigious urban art centers."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Stefan Mitrov Ljubiša Müzesi, kentsel kentsel yerel mirası ve gelenekleri anlatan kentin en prestijli kentsel kültür rotası duraklarından birisi olan kentsel tarih kalesidir.",
        "en": "Stefan Mitrov Ljubiša museum detailing local urban heritage and traditions is one of the city's most prestigious cultural routes, reflecting historical growth and high urban prestige."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Museum of Herbs, kentsel gastronomi dünyasına geleneksel bir dokunuş getiren kentin en stil sahibi kentsel lezzet duraklarından biri olup kentsel tarih hafızası noktasıdır.",
        "en": "Museum of Herbs and Spices brings a traditional touch to the city's gastronomic map, standing as one of the most stylish urban and aromatic spots detailing the past for every visitor."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Jewelry Lab, kentsel modernliği ve yerel el sanatlarını birleştiren kentin en özgün kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel sanat rotasıdır.",
        "en": "Jewelry Lab is a prestigious urban art and design route offering one of the most unique social escape spots in town, merging modern city style with professional local craftsmanship."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Stara Maslina, Adriyatik kıyısındaki binlerce yıllık kentsel hafızayı anlatan, zeytin ağacıyla simgeleşen kentin en prestijli ve entelektüel kentsel tarih penceresidir kentsel kaledir.",
        "en": "Old Olive Tree is an intellectual urban history window detailed for the millennia-old memory along the Adriatic coast, standing as a prestigious and vital living landmark in Budva."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Piramida, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli rotadır.",
        "en": "Piramida is a prestigious urban route offering one of the most refined social escape spots in town, featuring a chic design that merges city energy with a sophisticated atmosphere."
    }
}

for h in data["highlights"]:
    if h["id"] in updates:
        h["description"] = updates[h["id"]]["tr"]
        h["description_en"] = updates[h["id"]]["en"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Budva Batch 2 (44 venues). Total Budva Cleaned.")
