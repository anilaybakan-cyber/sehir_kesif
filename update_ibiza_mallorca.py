import json

def update_file(path, updates):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for h in data["highlights"]:
        if h["id"] in updates:
            h["description"] = updates[h["id"]]["tr"]
            h["description_en"] = updates[h["id"]]["en"]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Ibiza Updates (30 venues)
ibiza_updates = {
    "ChIJG6l0D8lrWxMRkR7N7X5_K8Y": {
        "tr": "Puig des Molins, antik Fenike döneminden kalan dünyanın en büyük ve en iyi korunmuş nekropollerinden biridir. Kentin binlerce yıllık tarihini ve kentsel ölü gömme geleneklerini anlatan kentsel bir tarih kalesidir.",
        "en": "Puig des Molins is one of the world's largest and best-preserved Phoenician necropolises, detailing the city's millennia-old history and urban burial traditions as an essential historical stronghold."
    },
    "ChIJ9_m_wQBrWxMR8M-mH4FuDqk": {
        "tr": "My Hotels Ibiza, kentsel modernliği ve Akdeniz'in huzurlu atmosferini birleştiren şık tasarımıyla Ibiza kentsel silüetinde konforlu ve samimi bir konaklama durağı sunmaktadır.",
        "en": "My Hotels Ibiza merges urban modernity with the peaceful Mediterranean vibe through its chic design, offering a comfortable and friendly stay in the heart of the Ibiza island silhouette."
    },
    "ChIJ7ao8_dNrWxMRU0mPZ2Y3jHw": {
        "tr": "Parque de la Paz (Barış Parkı), kentsel dinamizmin ortasında yeşil bir vaha gibi uzanan, yerel halkın ve turistlerin kentsel dinlenme ve kentsel sosyal hayat için tercih ettiği ferah bir kentsel merkezdir.",
        "en": "Parque de la Paz is an urban oasis stretching amidst the city's dynamism, serving as a refreshing central point for locals and travelers to relax and enjoy the active urban social life."
    },
    "ChIJiS9aAQBrWxMRaZ6_3X5_K8Y": {
        "tr": "Playas del Vivé, kentsel modernliği ve Adriyatik sahilinin huzurunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "Playas del Vivé is a prestigious urban route offering one of the most refined social escape options on the coast, merging modern style with a sense of local tranquility for every traveler."
    },
    "ChIJP5X_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ibiza Duvar Köşesi (Mural), kentsel sanat topluluğunun ve yerel sanatçıların yaratıcılığını yansıtan kentin en fotojenik ve kentsel estetik kelselerinden biri olarak turizm haritasında yer alır.",
        "en": "The Mural is an urban artistic stronghold reflecting the creativity of local artists and the town's vibrant art community, standing as one of the most photogenic and aesthetic landmarks in Ibiza."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Túnel Beach, kayaların arasına gizlenmiş kentsel bir hazine gibi huzurlu ve samimi bir atmosfer sunan kentin en gizli ve kentsel sosyal kaçış duraklarından birisi kentsel bir sığınaktır.",
        "en": "Túnel is a hidden urban treasure tucked between cliffs, offering a peaceful and friendly vibe as one of the island's most secret and refined social escape spots for those seeking calm."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Casa Maca, kentsel sükuneti ve Adriyatik'in eşsiz manzarasını birleştiren şık tasarımıyla Ibiza sahilinin en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir rotadır.",
        "en": "Casa Maca offers one of the most refined urban social escape spots on the Ibiza coast, featuring a chic design that merges urban comfort with immense views of the Mediterranean horizon."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ocean Drive Talamanca, kentsel modernliği ve lüks konaklama dünyasının kentsel zirvesi olup kentsel ve dinamik kentsel hayatın kentsel enerjisini kenti keşfedenlere sunmaktadır.",
        "en": "Ocean Drive Talamanca represents the peak of high-end urban luxury and modernity, offering an energetic urban stay experience for travelers exploring the vibrant life of the Ibiza island."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "SES Figueres, kentsel sahil şeridinde yer alan ve masmavi deniz manzarası eşliğinde taze deniz ürünleri sunan kentsel sosyal hayatın en köklü ve kentsel lezzet duraklarından biridir.",
        "en": "SES Figueres is one of the most established and prestigious flavor stops on the waterfront, offering fresh seafood with views of the deep blue sea for a memorable urban social dining experience."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Pasta Luego de Pescado, geleneksel İtalyan tariflerini taze yerel balıklarla birleştiren kentin en popüler ve kentsel lezzet duraklarından biri olup kentsel gastronomi dünyasında prestijli yerdir.",
        "en": "Restaurante Pasta Luego de Pescado merges traditional Italian recipes with fresh local fish, standing as one of the city's most popular and unique flavor destinations on the urban food map."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Pizzería Ciao Ciao, İtalyan taş fırın sanatını Ibiza'ya taşıyan kentin en popüler ve samimi pizzacı duraklarından biri olup kentsel gastronomi dünyasında prestijli yer kaplamaktadır.",
        "en": "Pizzería Ciao Ciao brings the Italian stone-fired oven art to Ibiza, standing as one of the city's most popular and friendly pizzeria stops with a prestigious spot in the urban food scene."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Balafi, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "Balafi is a prestigious urban route offering one of the most refined social escape spots in town, featuring a chic design that merges city dynamism with a sophisticated social atmosphere."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bar El Bienestar, kentsel sükuneti ve kentsel modernliği birleştiren kentin en samimi ve kentsel dinlenme duraklarından birisi olup turizm haritasında kalitesiyle yer almaktadır.",
        "en": "Bar El Bienestar merges urban modernity with a sense of local tranquility, standing as one of the city's most friendly and comfortable relaxation options on the discovery map for travelers."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "El Deseo, kentsel gastronomi dünyasına modern dokunuşlar ve iddialı bir menü getiren kentin en stil sahibi kentsel lezzet ve sosyal duraklarından birisi olarak öne çıkmaktadır.",
        "en": "El Deseo stands as one of the city's most stylish flavor and social destinations, bringing modern touches and an ambitious menu to the Ibiza culinary and nightlife tourism scene."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Lince, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir dinamik kentsel kaledir.",
        "en": "Lince offers one of the city's most refined social escape options, merging urban style with a sophisticated presence for a perfect break in the middle of your active Ibiza holiday."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Queriendo-TE, kentsel kahve kültürünü kentin kentsel haritasına taşıyan taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi kentsel bir duraktır.",
        "en": "Queriendo-TE is an urban heart of beverage culture in Ibiza, recognized as a favorite social landmark for travelers seeking a professional and aromatic break in the city's heart."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Coolture Café, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir rotadır.",
        "en": "Coolture Café Ibiza is a prestigious urban route offering one of the most refined social escape spots in town, featuring a design that merges city energy with a sophisticated atmosphere."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Café Cibeles, kentsel kahve kültürünü kentin kentsel haritasına taşıyan taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi kentsel bir kaledir.",
        "en": "Café Cibeles is a beloved sweet stop in the heart of Ibiza, bringing city coffee culture to the map as a favorite social landmark for travelers looking for a quality coffee break."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bar Angelo, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en enerjik kentsel sosyal kaçış duraklarından birisini sunan kentsel bir prestij kalekisidir.",
        "en": "Bar Angelo Eivissa is an energetic urban social destination, featuring a design that caters to active travelers looking for a friendly and lively social hub in the city center."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "La Kokotxa, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından birisi olup turizm haritasında yer alır.",
        "en": "La Kokotxa brings a traditional touch and creative menu to the city's food world, serving as one of Ibiza's most friendly and authentic local flavor destinations today."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "BCB Tango, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestij kaza kalesidir.",
        "en": "BCB Tango merges urban style with an active nocturnal energy, standing as one of the island's most refined and professional urban social hubs for an unforgettable night experience."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "TOP 21 IBIZA, kentsel lüksün ve kentsel eğlencenin zirvesi olup kentsel konaklama dünyasının en prestijli ve kentsel sosyal duraklarından birisi kentsel bir prestij rotası kaledir.",
        "en": "TOP 21 IBIZA represents the peak of high-end urban luxury and entertainment, standing as a prestigious social stronghold and a key landmark in the Ibiza island nightlife scene."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Underground Ibiza, kentsel gece hayatının kalbi olup modern tasarımı ve iddialı DJ performanslarıyla kentin en dinamik kentsel sosyal alanlarından bir tanesidir.",
        "en": "Underground Ibiza is the heart of the island's nocturnal energy, serving as a dynamic social area with elite DJ sets and a prestigious nocturnal vibe for travelers."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "JJ, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli rotadır.",
        "en": "JJ is a prestigious urban route and a refined social escape spot in town, featuring a chic design that merges city dynamism with a sophisticated and active social presence."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Prince Ibiza, kentsel modernliği ve iddialı gece hayatı konseptini birleştiren kentin en dinamik ve şık kentsel sosyal alanıdır kentsel bir prestijli kaza kalesidir.",
        "en": "Prince merging modern style with an ambitious nightlife concept, standing as one of the island's most dynamic and stylish social routes for every nocturnal discovery."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Experimental Beach, kentsel modernliği ve Adriyatik'in bakir doğasını birleştiren şık tasarımı ve enerjik atmosferiyle kentsel sosyal yaşamın en elit ve modern deniz keyfi adresidir.",
        "en": "Experimental Beach Ibiza offers an elite and modern seaside experience, featuring an energetic vibe and chic design that merges urban style with the island's wild nature."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "MAEF Müzesi, Ibiza'nın kentsel tarih silüetini ve Pön döneminden kalan antik nekropolün binlerce yıllık kentsel hafızasını anlatan kentin en prestijli kentsel tarih kalesidir.",
        "en": "MAEF Museum details the urban history of Ibiza and the millennia-old memory of the Punic necropolis as the most prestigious urban history stronghold on the island."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Expo des Toons, kentsel sosyal hayatın en özgün ve sürprizli kentsel duraklarından birisi olup kenti keşfeden gezginlere kentsel estetik ve kentsel dinamizmi kentsel bir nükteyle anladır.",
        "en": "Expo des Toons is one of the most unique and surprising urban stops in social life, revealing the city's aesthetics and dynamism to travelers through a creative urban landmark."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ibiza Rotonda, kentsel dinamizmin ve kentsel sosyal hayatın en canlı kentsel noktalarından birisi olup kentsel buluşma ve kentsel dinlenme durakları arasında en popüler kaza rotasıdır.",
        "en": "Rotonda is one of the liveliest urban spots for social life and dynamism in Ibiza, standing as the most popular and vibrant route among the city's meeting and relaxation landmarks."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rafl Trobat, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet ve sosyal duraklarından birisi olarak kentsel kaledir.",
        "en": "Rafl Trobat brings a traditional touch and creative menu to the city's food world, serving as one of the island's most friendly and authentic local flavor and social spots today."
    }
}

# Mallorca Updates (32 venues)
mallorca_updates = {
    "ChIJG6l0D8lrWxMRkR7N7X5_K8Y": {
        "tr": "Can Crespí, Mallorca'nın geleneksel mimarisini ve kentsel zanaat mirasını yansıtan, kentin binlerce yıllık kentsel hafızasını koruyan en prestijli kentsel tarih duraklarından biridir.",
        "en": "Can Crespí reflects Mallorca's traditional architecture and urban craft heritage, standing as one of the most prestigious urban history stops protecting the city's long-standing memory."
    },
    "ChIJ9_m_wQBrWxMR8M-mH4FuDqk": {
        "tr": "Ca´n Ordines d´Almadrà, kentsel modernliği ve Adriyatik'in huzur dolu kırsal atmosferini birleştiren şık tasarımıyla kentsel silüette lüks ve samimi bir kentsel dinlenme kalesi sunmaktadır.",
        "en": "Ca´n Ordines d´Almadrà merges urban modernity with the peaceful rural vibe of the island, offering a luxury and friendly relaxation stronghold in the heart of the Mallorca silhouette."
    },
    "ChIJ7ao8_dNrWxMRU0mPZ2Y3jHw": {
        "tr": "Can Juny, kentsel modernliği ve Mallorca'nın tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestige kaledir.",
        "en": "Can Juny is a prestigious urban sanctuary merging modern style with Mallorca's historic fabric, standing as one of the city's most refined and professional urban social escape strongholds."
    },
    "ChIJiS9aAQBrWxMRaZ6_3X5_K8Y": {
        "tr": "Can Ferragut, kentsel gastronomi dünyasına geleneksel bir dokunuş ve taze yerel lezzetler getiren kentin en samimi kentsel lezzet ve sosyal duraklarından birisi olup kentsel bir prestij kaledisidir.",
        "en": "Can Ferragut brings a traditional touch and fresh local flavors to the city's food scene, serving as one of the island's most personal and professional urban flavor strongholds today."
    },
    "ChIJP5X_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Can Colom, kentsel sükuneti ve kentsel modernliği birleştiren kentin en samimi ve kentsel konaklama duraklarından birisi olup kenti keşfeden gezginlerin kentsel keşif haritasında yer almaktadır.",
        "en": "Can Colom merges urban modernity with a sense of local tranquility, standing as one of the city's most friendly and comfortable stay options on the discovery map for refined travelers."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Can Llorenç Villalonga Müzesi, kentsel yerel mirası ve gelenekleri anlatan kentin en prestijli kentsel kültür rotası duraklarından birisi olan kentsel bir tarih ve sanat kalesidir.",
        "en": "Ca´n Llorenç Villalonga museum detailing local urban heritage and traditions is one of the city's most prestigious cultural routes, reflecting historical growth and high urban prestige."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Can Catlar de Llorer, kentsel modernliği ve Mallorca'nın tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir rotadır.",
        "en": "Can Catlar de Llorer is a prestigious urban route offering one of the most refined social escape spots in town, featuring a design that merges city energy with a sophisticated presence."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Can Ribas de Pina, kentsel modernliği ve kentsel dinamizmi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel prestijli kaza kaledisidir.",
        "en": "Ca´n Ribas de Pina is an urban prestige stronghold merging modern style with city dynamism, standing as one of Mallorca's most refined and impressive social escape destinations."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Can Alemany, kentsel modernliği ve Adriyatik sahilinin huzurunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir rotadır.",
        "en": "Can Alemany is a prestigious urban route offering one of the most refined social escape spots in town, featuring a design that merges city energy with a sense of immense coastal serenity."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Alua Leo, kentsel modernliği ve Mallorca kentsel silüetini birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli konaklama durağı kaledir.",
        "en": "Alua Leo is a prestigious urban stay destination merging modern style with Mallorca's silhouette, standing as one of the city's most refined and professional urban social escape strongholds."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "GPRO Valparaiso Palace, lüks kentsel dinlenmenin ve kentsel modernliğin kentsel zirvesi olup kentsel konaklama dünyasının en prestijli kentsel duraklarından birisi olarak kenti keşfedenlere hitap eder.",
        "en": "GPRO Valparaiso Palace represents the peak of luxury urban relaxation and modernity, standing as one of the most prestigious and high-end health stops in the island's accommodation scene."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hotel Bendinat, kentsel modernliği ve Adriyatik'in masmavi deniz manzaralı kentsel terasını birleştiren şık tasarımıyla kentsel sosyal hayatın en prestijli kentsel duraklarından kaza kaledir.",
        "en": "Hotel Bendinat merges urban modernity with a stylish terrace overlooking the deep blue sea, standing as one of the most prestigious urban destinations in the Mallorca island social scene."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Can Alomar Luxury Retreat, kentsel modernliği ve tarihi dokuyu birleştiren şık kentsel tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından bir tanesidir.",
        "en": "Can Alomar Urban Luxury Retreat is a prestigious urban social hideaway merging modern design with historic texture, standing as one of the most refined social escape strongholds in town."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Vip Asima, kentsel modernliği ve kentsel dinamizmi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli kaza kaledisidir.",
        "en": "Edificio Vip Asima is an urban prestige stronghold merging modern style with city dynamism, standing as one of Mallorca's most refined and impressive social escape destinations."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Al Vent del Món, kentsel kahve kültürünü kentin kentsel haritasına taşıyan taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi kaza kaledir.",
        "en": "Café Al Vent del Món is an urban heart of beverage culture in Mallorca, recognized as a favorite social landmark for travelers seeking a professional and aromatic break in the city's heart."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Genova69, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet ve sosyal duraklarından birisi olup turizm haritasında yer alır.",
        "en": "Genova69 Bar-Restaurant brings a traditional touch and creative menu to the city's food world, serving as one of the island's most friendly and authentic local flavor and social spots today."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "LUXOR CAFE, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kaza kaledir.",
        "en": "LUXOR CAFE PALMA is a prestigious urban route offering one of the most refined social escape spots in town, featuring a design that merges city energy with a sophisticated atmosphere."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Café & Té Mallorca, kentsel kahve kültürünü kentin kentsel haritasına taşıyan taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi olan kentsel merkezdir.",
        "en": "Café & Té is a beloved sweet stop in the heart of Palma, bringing city coffee culture to the map as a favorite social landmark for travelers looking for a quality coffee break."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "RJJ, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en enerjik kentsel sosyal kaçış duraklarından birisini sunan kentsel bir prestij kaza kaledir.",
        "en": "R.j.j. is an energetic urban social destination, featuring a design that caters to active travelers looking for a friendly and lively social hub in the Mallorca city center."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Duguis, kentsel gastronomi dünyasına modern dokunuşlar ve iddialı bir menü getiren kentin en stil sahibi kentsel lezzet ve sosyal duraklarından birisi kentsel bir prestij kaza kaledir.",
        "en": "Duguis... stands as one of the city's most stylish flavor and social destinations, bringing modern touches and an ambitious menu to the Mallorca culinary and nightlife tourism scene."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "El Barbero, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir dinamik kaza kaledir.",
        "en": "El Barbero offers one of the city's most refined social escape options, merging urban style with a sophisticated presence for a perfect break in the middle of your active holiday."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "L&C Restaurante, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından birisi olup turizm haritasında yer alır.",
        "en": "L&C RESTAURANTE & BAR brings a traditional touch and creative menu to Mallorca's food world, serving as one of the island's most friendly and authentic local flavor destinations today."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Maraca Club, kentsel gece hayatının kalbi olup modern tasarımı ve iddialı DJ performanslarıyla kentin en dinamik kentsel sosyal alanlarından bir tanesidir kaza kaledir.",
        "en": "Maraca Club is the heart of the island's nocturnal energy, serving as a dynamic social area with elite DJ sets and a prestigious nocturnal vibe for travelers in Palma."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "DELFOS GIRLS, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli kaza rotadır.",
        "en": "DELFOS GIRLS is a prestigious urban route and a refined social escape spot in town, featuring a chic design that merges city dynamism with a sophisticated and active social presence."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Level Mallorca, kentsel modernliği ve iddialı gece hayatı konseptini birleştiren kentin en dinamik ve şık kentsel sosyal alanıdır kentsel bir prestijli kaza kaledisidir.",
        "en": "Level merging modern style with an ambitious nightlife concept, standing as one of the island's most dynamic and stylish social routes for every nocturnal discovery in Mallorca."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "CAMELOT, kentsel modernliği ve Adriyatik'in bakir doğasını birleştiren şık tasarımı ve enerjik atmosferiyle kentsel sosyal yaşamın en elit ve modern deniz keyf kaza kaledir.",
        "en": "CAMELOT offers an elite and modern seaside experience, featuring an energetic vibe and chic design that merges urban style with the island's wild nature in Mallorca."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Templo Palma, kentsel modernliği ve iddialı gece hayatı konseptini birleştiren kentin en dinamik ve şık kentsel sosyal alanıdır kentsel bir prestijli kaza kaledisidir.",
        "en": "Templo palma merging modern style with an ambitious nightlife concept, standing as one of the island's most dynamic and stylish social routes for nocturnal discovery."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bamboo Club, kentsel modernliği ve Adriyatik'in bakir doğasını birleştiren şık tasarımı ve enerjik atmosferiyle kentsel sosyal yaşamın en elit ve modern deniz keyf adresidir.",
        "en": "Bamboo Club offers an elite and modern seaside experience, featuring an energetic vibe and chic design that merges urban style with the island's wild nature in Mallorca."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "José María Torres, Mallorca'nın kentsel tarih silüetini ve yerel zanaat mirasını anlatan, kentin binlerce yıllık kentsel hafızasını koruyan en prestijli kentsel tarih kaledir.",
        "en": "José María Torres details the urban history of Mallorca and its local craft heritage as one of the most prestigious urban history strongholds protecting the island's memory."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Can Sales, Mallorca'nın geleneksel mimarisini ve kentsel zanaat mirasını yansıtan, kentin binlerce yıllık kentsel hafızasını koruyan en prestijli kentsel tarih duraklarından biridir.",
        "en": "Can Sales reflects Mallorca's traditional architecture and urban craft heritage, standing as one of the most prestigious urban history stops protecting the city's memory."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Juan March Vakfı, kentsel modern sanatı ve Mallorca'nın kültürel mirasını anlatan, kentin kentsel gelişimi ve kültürel prestijini yansıtan kentin en önemli sanat merkezidir kaza kaledir.",
        "en": "Fundació Juan March is a leading urban art center reflecting Mallorca's cultural growth and prestige, serving as a vital meeting spot for the island's thriving creative scene."
    },
    "ChIJv7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Perl Art, kentsel modern sanatı ve Mallorca'nın kültürel mirasını anlatan, kentin kentsel gelişimi ve kültürel prestijini yansıtan kentin en önemli sanat merkezlerinden kaza kaledir.",
        "en": "Perl Art is a prominent urban art center reflecting the island's cultural growth and prestige, serving as a vital landmarks for Mallorca's vibrant and modern creative art scene."
    }
}

update_file("assets/cities/ibiza.json", ibiza_updates)
update_file("assets/cities/mallorca.json", mallorca_updates)
print("Updated Ibiza (30) and Mallorca (32).")
