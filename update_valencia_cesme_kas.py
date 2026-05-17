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

# Valencia Updates (31 venues)
valencia_updates = {
    "ChIJG6l0D8lrWxMRkR7N7X5_K8Y": {
        "tr": "La Beneficencia Kültür Merkezi, 19. yüzyıldan kalan tarihi binasında Valencia'nın kentsel tarihini ve yerel geleneklerini sergileyen kentin en prestijli kentsel kültür kalelerinden biridir.",
        "en": "Centro Cultural la Beneficencia is one of Valencia's most prestigious cultural strongholds, showcasing urban history and local traditions in a 19th-century historic building for every visitor."
    },
    "ChIJ9_m_wQBrWxMR8M-mH4FuDqk": {
        "tr": "El Bobo, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından biri olup kentsel sosyal hayatın merkezindedir.",
        "en": "El Bobo brings a traditional touch and creative menu to the city's food world, serving as one of Valencia's most friendly and authentic local flavor destinations in the active urban scene today."
    },
    "ChIJ7ao8_dNrWxMRU0mPZ2Y3jHw": {
        "tr": "Cuinar-te Ruzafa, kentsel gastronomi dünyasına modern dokunuşlar ve iddialı bir menü getiren kentin en stil sahibi kentsel lezzet ve sosyal duraklarından birisi kentsel bir prestij kaza kaledisidir.",
        "en": "Cuinar-te Ruzafa stands as one of the city's most stylish flavor and social destinations, bringing modern touches and an ambitious menu to the Valencia culinary and nightlife tourism scene."
    },
    "ChIJiS9aAQBrWxMRaZ6_3X5_K8Y": {
        "tr": "Bar Los Picapiedra, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir dinamik kaza kaledir.",
        "en": "Bar Los Picapiedra offers one of the city's most refined social escape options, merging urban style with a sophisticated presence for a perfect break in the middle of your active holiday."
    },
    "ChIJP5X_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Tridente, kentsel sahil şeridinde yer alan ve masmavi deniz manzarası eşliğinde taze deniz ürünleri sunan kentsel sosyal hayatın en köklü ve kentsel lezzet duraklarından kentsel bir prestij kaledir.",
        "en": "Restuarante Tridente is one of the most established and prestigious flavor stops on the waterfront, offering fresh seafood with views of the deep blue sea for a memorable urban social dining day."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Pelegrí Valencia, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından birisi olup turizm haritasında yer alır.",
        "en": "Restaurante Pelegrí Valencia brings a traditional touch and creative menu to the city's food world, serving as one of Valencia's most friendly and authentic local flavor destinations today."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kids Mafia, kentsel sosyal hayata eğlence ve neşe katan kentin en dinamik kentsel sosyal alanlarından biri olup çocuklu kentsel gezginler için kentsel bir prestij ve oyun kaza kaledir.",
        "en": "Kids Mafia is one of the city's most lively urban social destinations for families, adding fun and play into the active social life as a favorite route for travelers with children in Valencia."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Àmbit, kentsel modernliği ve Valencia'nın tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kaza kaledir.",
        "en": "Àmbit is a prestigious urban route offering one of the most refined social escape spots in town, featuring a design that merges city energy with a sophisticated and active social presence."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Pastís d'Or, kentin fırıncılık geleneklerini modern pastane konseptiyle birleştiren, taze ürünleri ve kentsel atmosferiyle kentin en sevilen kentsel duraklarından birisi kaza kaledisidir.",
        "en": "Pastís d'Or merges the city's baking traditions with a modern pastry concept, recognized as one of the most beloved and aromatic urban landmarks for fresh bread and sweets in Valencia."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Orxateria Daniel, kentsel gastronomi dünyasının yerel kenti için meşhur horchata lezzetini sunan kentsel bir prestij noktası olup kentin en köklü lezzet duraklarından bir tanesi kaledir.",
        "en": "Orxateria Daniel represents the peak of Valencia's local horchata culture, standing as a prestigious and established flavor stronghold and a vital route for every traditional food lover visiting."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ludoteca Mundo Mágico, kentsel sosyal hayata eğlence ve neşe katan kentin en dinamik kentsel sosyal alanlarından biri olup çocuklu kentsel gezginler için kentsel bir prestij ve oyun kaza kaledir.",
        "en": "Ludoteca Mundo Mágico is one of the city's most lively urban social destinations for families, adding fun and play into the active social life as a favorite route for travelers with children."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bocatería Harbin, kentsel gastronomi dünyasına hızlı ve lezzetli bir dokunuş getiren kentin en popüler kentsel lezzet duraklarından biri olup turizm haritasında yer alır kaza kaledir.",
        "en": "Bocatería Harbin brings a fast and tasty touch to Valencia's food scene, standing out on the tourism map as one of the most popular and practical flavor destinations in the city center today."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bar Bocho, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en samimi kentsel sosyal kaçış duraklarından birini sunan kentsel bir dinamik kaza kaledir.",
        "en": "Bar Bocho offers one of the city's most friendly social escape options, merging urban style with a sophisticated presence for a perfect break in the middle of your active Valencia discovery."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Esportiu A Cobert, kentsel dinamizmi ve kentsel spor hayatını birleştiren kentin en enerjik kentsel sosyal alanlarından biri olup kentsel sağlık ve spor durakları arasında en prestijli kaza kaledisidir.",
        "en": "Esportiu A Cobert merges urban dynamism with an active sporting life, standing as one of the city's most prestigious health and fitness landmarks on the discovery map for every traveler."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Café Balli, kentsel kahve kültürünü kentin kentsel haritasına taşıyan taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi olan kentsel bir kaza kaledir.",
        "en": "CAFÉ BALLI is an urban heart of beverage culture in Valencia, recognized as a favorite social landmark for travelers seeking a professional and aromatic break in the heart of the city today."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ya Ke Lounge, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestij kaza kaledir.",
        "en": "Ya Ke Lounge is a prestigious urban destination and a refined social escape spot in town, featuring a design that merges city energy with a sophisticated and active social presence for guests."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "PausaCaffe, kentsel kahve kültürünü kentin kentsel haritasına taşıyan taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi olan kentsel bir kaza kaledir.",
        "en": "PausaCaffe is a beloved sweet stop in the heart of Valencia, bringing city coffee culture to the map as a favorite social landmark for travelers looking for a soul-refreshing coffee break today."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Terra de Mar, kentsel sükuneti ve Adriyatik'in eşsiz manzarasını birleştiren şık tasarımıyla Valencia sahilinin en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli kaza kaledir.",
        "en": "Café Terra de Mar offers one of the most refined urban social escape spots on the coast, featuring a design that merges urban comfort with immense views of the Mediterranean horizon for all."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Cerrado, kentsel dinamizmin ortasında yer alan ve kentsel sosyal hayatın kentsel enerjisini kenti keşfeden gezginlere sunan kentsel bir prestijli kaza rotası kaza kaledisidir.",
        "en": "Cerrado details the city's urban modernity and local cultural heritage, standing as a prestigious and intellectual urban history window on the discovery map for all visitors in Valencia today."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bar Platers, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından birisi olup turizm haritasında yer alır kaza kaledir.",
        "en": "Bar Platers brings a traditional touch and creative menu to the city's food world, serving as one of Valencia's most friendly and authentic local flavor destinations in the active urban scene today."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "El Desván, kentsel gastronomi dünyasına modern dokunuşlar ve iddialı bir menü getiren kentin en stil sahibi kentsel lezzet ve sosyal duraklarından birisi olan kentsel bir kaza kaledir.",
        "en": "EL DESVÁN stands as one of the city's most stylish flavor and social destinations, bringing modern touches and an ambitious menu to the Valencia culinary and nightlife tourism map today."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Flamingos Swingers Club, kentsel modernliği ve iddialı gece hayatı konseptini birleştiren kentin en dinamik ve şık kentsel sosyal alanlarından biri olup kaza kaledir.",
        "en": "Flamingos Swingers Club is one of the island's most dynamic and stylish social areas, merging a modern club design with an ambitious and private nightlife experience for travelers."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Los Amigos, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından birisi olup turizm haritasında yer alır.",
        "en": "Los Amigos brings a traditional touch and creative menu to the city's food world, serving as one of Valencia's most friendly and authentic local flavor destinations in the urban scene today."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Blanquita Bar, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en samimi kentsel sosyal kaçış duraklarından birini sunan kentsel bir kaza kaledir.",
        "en": "Blanquita Bar offers one of the city's most friendly social escape options, merging urban style with a sophisticated presence for a perfect break in the middle of your active holiday."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Piko's Bar, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından birisi olup turizm haritasında yer alır.",
        "en": "Piko's Bar brings a traditional touch and creative menu to the city's food world, serving as one of Valencia's most friendly and authentic local flavor destinations in the urban scene today."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Apoquetanit, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir kaza kaledisidir.",
        "en": "Apoquetanit is a prestigious urban destination and a refined social escape spot in town, featuring a design that merges city energy with a sophisticated and active social presence for guests."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Leganés, kentsel dinamizmin ortasında yer alan ve kentsel sosyal hayatın kentsel enerjisini kenti keşfeden gezginlere sunan kentsel bir prestijli kaza rotası kaza kaledisidir.",
        "en": "Leganés details the city's urban modernity and local cultural heritage, standing as a prestigious and intellectual urban history window on the discovery map for all visitors in Valencia today."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "El Kubata, kentsel gastronomi dünyasına modern dokunuşlar ve iddialı bir menü getiren kentin en stil sahibi kentsel lezzet ve sosyal duraklarından birisi kaza kaledir.",
        "en": "El Kubata de Hojalata stands as one of the city's most stylish flavor and social destinations, bringing modern touches and an ambitious menu to the Valencia culinary and nightlife scene."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Palau dels Valeriola, kentsel silüetin en renkli ve estetik duraklarından biri olup kentsel Gotik mimariyi ve kentsel sanat kültürünü kenti keşfeden gezginlerle buluşturan bir kaledir.",
        "en": "Palau dels Valeriola is one of the most aesthetic landmarks in the urban silhouette, merging urban Gothic architecture with the city's art culture for every traveler exploring Valencia today."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Palau de Cervelló, kentsel silüetin en prestijli ve estetik duraklarından biri olup kentsel Barok mimariyi ve kentsel sanat kültürünü kenti keşfedenlerle buluşturan kentsel bir kaledir.",
        "en": "Palau de Cervelló is a prestigious urban landmark merging urban Baroque architecture with the town's history, serving as a vital and significant historical stronghold for every curious traveler."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Almudín de Valencia, kentsel silüetin en köklü ve estetik duraklarından biri olup kentsel tarihi dokuyu ve kentsel sanat kültürünü kenti keşfeden gezginlerle buluşturan bir kaledir.",
        "en": "Almudín de Valencia is one of the most established landmarks in the urban silhouette, merging historic Gothic architecture with the city's cultural life for every traveler exploring today."
    }
}

# Çeşme Updates (33 venues)
cesme_updates = {
    "ChIJG6l0D8lrWxMRkR7N7X5_K8Y": {
        "tr": "Fun Beach Club, Çeşme'nin en temiz sularına ve en enerjik kentsel sosyal atmosferine sahip kentsel bir deniz keyfi kalesi olup kentsel tatilcilerin en prestijli kaza kaledisidir.",
        "en": "Fun Beach Club is an urban maritime stronghold in Çeşme, famed for its crystal clear waters and energetic social vibe as the most prestigious coastal destination for every traveler."
    },
    "ChIJ9_m_wQBrWxMR8M-mH4FuDqk": {
        "tr": "Fava Alaçatı, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından biri olup kentsel sosyal hayatın merkezindedir.",
        "en": "Fava Alaçatı brings a traditional touch and creative menu to the city's food world, serving as one of Çeşme's most friendly and authentic local flavor destinations in the active urban scene."
    },
    "ChIJ7ao8_dNrWxMRU0mPZ2Y3jHw": {
        "tr": "Aqua Toy City, çocuklu gezginler için kentsel sosyal hayata eğlence ve neşe katan kentin en dinamik kentsel su parklarından biri olup kentsel prestij ve oyun kaza kaledir.",
        "en": "Aqua Toy City is one of the city's most lively urban water parks for families, adding fun and play into the active social life as a favorite route for travelers with children in Çeşme."
    },
    "ChIJiS9aAQBrWxMRaZ6_3X5_K8Y": {
        "tr": "Altın Yunus, kentsel modernliği ve Adriyatik sahilinin huzurunu birleştiren şık tasarımıyla Çeşme'nin en prestijli ve ikonik kentsel konaklama duraklarından kentsel bir kaza kaledisidir.",
        "en": "Altın Yunus is a prestigious urban stay destination merging modern style with coastal tranquility, standing as one of Çeşme's most iconic and professional social escape strongholds today."
    },
    "ChIJP5X_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Otel Arinnanda, kentsel sükuneti ve kentsel modernliği birleştiren kentin en samimi ve kentsel konaklama duraklarından birisi olup turizm haritasında yer almaktadır.",
        "en": "Otel Arinnanda merges urban modernity with a sense of local tranquility, standing as one of the city's most friendly and comfortable stay options on the discovery map for refined travelers."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Çeşme'li Butik Otel, kentsel sükuneti ve kentsel modernliği birleştiren kentin en samimi ve kentsel konaklama duraklarından birisi olup turizm haritasında yer almaktadır.",
        "en": "ÇEŞME'li Butik Otel merges urban modernity with local hospitality, standing as one of the city's most friendly and comfortable stay options on the discovery map for travelers today."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Burger King Marina, kentsel dinamizmin tam ortasında yer alan ve kenti keşfeden gezginlere pratik bir kentsel lezzet molası sunan kentsel bir prestijli kaza kaledir.",
        "en": "Burger King Marina offers a practical and fast flavor break in the heart of Çeşme's harbor, serving as a familiar urban stop for travelers exploring the active and bright city life."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Starbucks Marina, kentsel kahve kültürünü kentin kentsel haritasına taşıyan taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi olan kentsel merkezdir.",
        "en": "Starbucks Marina is a beloved social landmark in the heart of the city's port area, bringing global coffee culture and a great view to the map for every traveler in Çeşme."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kalinda Inn Otel, kentsel modernliği ve Ege sahilinin huzurunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kaledir.",
        "en": "Kalinda Inn merges urban modernity with the peace of the Aegean coast, standing as one of the city's most refined and professional urban social escape strongholds for every traveler."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Çeşme Kahvaltı Parkı, kentsel sosyal hayatın ve kentsel kentsel enerjinin kentsel merkezlerinden birisi olup kentsel dinamizmi kenti keşfeden gezginlere kentsel bir nükteyle anladır.",
        "en": "Park is a central urban point for social life and energy, providing a refreshing break for travelers exploring the city through its green spaces and vibrant urban atmosphere."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Telcabin, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli kaza kaledisidir.",
        "en": "Telcabin is a prestigious urban destination and a refined social escape spot in town, featuring a design that merges city energy with a sophisticated and active social presence in Çeşme."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Scott Stanley Forde Parkı, kentsel dinamizmin ortasında yer alan ve kentsel sosyal hayatın kentsel enerjisini kenti keşfeden gezginlere sunan kentsel bir prestijli kaza kaledisidir.",
        "en": "Scott Stanley Forde Parkı details the city's urban modernity and local cultural heritage, standing as a prestigious and intellectual urban history window on the discovery map for all visitors."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Oasis Aquapark, kentsel sosyal hayata eğlence ve neşe katan kentin en dinamik kentsel su parklarından biri olup kentsel prestij ve oyun kaza kaledir.",
        "en": "Oasis Aquapark is one of the city's most lively urban social destinations, adding fun and play into the active social life as a favorite route for travelers with children in Çeşme."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Tanay Tabiat Parkı, kentsel sükunetin ve kentsel modernliğin kentsel zirvesi olup kentsel dinlenme dünyasının en prestijli kentsel duraklarından birisi olan kentsel bir kaza kaledisidir.",
        "en": "Tanay Tabiat Parkı represents the peak of natural tranquility and urban escape, standing as a prestigious and high-end relaxation stop in the city's active tourism scene for every visitor."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "La Capria Suite, kentsel modernliği ve Alaçatı'nın tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestige kaledir.",
        "en": "La Capria Suite Hotel is a prestigious urban sanctuary merging modern style with Alaçatı's historic fabric, standing as one of the city's most refined and professional social escape strongholds."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Alaçatı Port Hotel, kentsel modernliği ve Adriyatik sahilinin huzurunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestige kaledir.",
        "en": "Alaçatı Port Hotel is a prestigious urban stay destination merging modern style with coastal tranquility, standing as one of the city's most refined and professional social escape strongholds."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Viento Hotel, kentsel modernliği ve Alaçatı'nın tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestige kaledir.",
        "en": "Viento Alaçatı Hotel is a prestigious urban sanctuary merging modern style with the town's historic fabric, standing as one of the most refined and professional social escape strongholds."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ala Otel, kentsel sükuneti ve kentsel modernliği birleştiren kentin en samimi ve kentsel konaklama duraklarından birisi olup turizm haritasında yer almaktadır.",
        "en": "Ala Otel Alaçatı merges urban modernity with a sense of local hospitality, standing as one of the town's most friendly and comfortable stay options on the discovery map for travelers today."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "The White Hotel, kentsel modernliği ve kentsel dinamizmi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestige kaza kaledir.",
        "en": "The White Alaçatı is a prestigious urban destination and a refined social escape spot in town, featuring a design that merges city energy with a sophisticated and active social presence."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "The Passion, kentsel modernliği ve Alaçatı'nın tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir kaza kaledir.",
        "en": "The Passion Alaçatı is a prestigious urban route offering one of the most refined social escape options, merging modern style with the historic fabric of Alaçatı for every traveler seeking calm."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "İmren Han Otel, kentsel modernliği ve Alaçatı'nın tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestige kaledir.",
        "en": "İmren Han Otel merges urban modernity with the historic texture of Alaçatı, standing as one of the city's most prestigious and established stay destinations on the active tourism map today."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kapari Butik Otel, kentsel sükuneti ve kentsel modernliği birleştiren kentin en samimi ve kentsel konaklama duraklarından birisi olup turizm haritasında yer almaktadır.",
        "en": "Alaçatı Kapari Butik Otel merges urban modernity with a sense of local tranquility, standing as one of the town's most friendly and comfortable stay options on the city's discovery map."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "ZUM Alaçatı, kentsel gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren kentin en samimi kentsel lezzet duraklarından biri olup kentsel sosyal hayatın kalesidir.",
        "en": "ZUM Alaçatı brings a traditional touch and creative menu to the town's food world, serving as one of the city's most friendly and authentic local flavor destinations in the active urban scene."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Marinera Residence, kentsel modernliği ve Adriyatik sahilinin huzurunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestige kaledir.",
        "en": "Marinera Residence is a prestigious urban stay destination merging modern style with coastal tranquility, standing as one of the city's most refined and professional social escape strongholds."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Dalyan Yelken, kentsel sahil şeridinde yer alan ve masmavi deniz manzarası eşliğinde taze deniz ürünleri sunan kentsel sosyal hayatın en köklü ve kentsel lezzet duraklarından biridir.",
        "en": "Dalyan Yelken Restoran Neco’nun Yeri is one of the most established flavor stops on the Çeşme waterfront, offering fresh seafood with views of the deep blue sea for a memorable dining day."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bahçelika Kahvaltı, kentsel gastronomi dünyasına kentin kentsel ve yerel lezzetlerini en taze haliyle sunan kentin en popüler kentsel lezzet duraklarından biridir.",
        "en": "Çeşme Bahçelika Kahvaltı brings local flavors to the town's food world at its freshest, standing out on the tourism map as one of the most popular and authentic breakfast destinations today."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bonjour Beach, Çeşme'nin en temiz sularına ve en enerjik kentsel sosyal atmosferine sahip kentsel bir deniz keyfi kalesi olup kentsel tatilcilerin en prestijli kaza kaledisidir.",
        "en": "Bonjour Beach is an urban maritime stronghold in Çeşme, famed for its crystal clear waters and energetic social vibe as the most prestigious coastal destination for travelers today."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Marina Cafe & Pub, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestige kaledir.",
        "en": "Marina&Cafe&Pub is a prestigious urban destination and refined social escape spot, featuring a design that merges city energy with a sophisticated and active social presence in Çeşme today."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Tarçın Kahvaltı, kentsel gastronomi dünyasına kentin kentsel ve yerel lezzetlerini en taze haliyle sunan kentin en popüler kentsel lezzet duraklarından biri olup kaza kaledir.",
        "en": "Tarçın Kahvaltı & Kafe brings traditional local flavors to the town's food world at its freshest, standing out as one of the most popular and friendly flavor destinations in the city center."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Cava Roof, kentsel modernliği ve kentsel dinamizmi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestige kaza kaledir.",
        "en": "Cava Roof is a prestigious urban destination and a refined social escape spot in town, featuring a design that merges city energy with a sophisticated and active social presence in Çeşme."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Aramızda Kalsın, kentsel gastronomi dünyasına kentin kentsel ve yerel lezzetlerini en taze haliyle sunan kentin en popüler kentsel lezzet duraklarından biri olup turizm haritasında yer alır.",
        "en": "Aramızda Kalsın Çeşme is a standout on the tourism map as one of the city's most popular and urban flavor destinations, bringing a traditional touch and modern music to the food scene."
    },
    "ChIJv7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bizim Ev Kafe, kentsel sükuneti ve kentsel modernliği birleştiren kentin en samimi ve kentsel dinlenme duraklarından birisi olup turizm haritasında yer almaktadır.",
        "en": "Bizim Ev Kafe Ceshme merges urban modernity with a sense of local hospitality, standing as one of the town's most friendly and comfortable relaxation options on the city's discovery map."
    },
    "ChIJw7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Yaz Gülü Cafe, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en samimi kentsel sosyal kaçış duraklarından birini sunan kentsel bir kaza kaledisidir.",
        "en": "Yaz gülü cafe is an energetic urban social destination and hub for city life, offering a design that caters to active travelers looking for a friendly and lively social spot in Çeşme center."
    }
}

# Kaş Update (1 venue)
kas_updates = {
    "ChIJG6l0D8lrWxMRkR7N7X5_K8Y": {
        "tr": "Kaş, kristal suları, antik Likya yolu ve masmavi deniziyle kentsel modernliği ve Akdeniz'in bakir doğasını buluşturan Türkiye'nin en prestijli kentsel dinlenme ve kentsel keşif kalesidir.",
        "en": "Kaş is Turkey's most prestigious urban relaxation and discovery stronghold, merging urban modernity with the wild Mediterranean nature, crystal waters, and the ancient Lycian Way for all."
    }
}

update_file("assets/cities/valencia.json", valencia_updates)
update_file("assets/cities/cesme.json", cesme_updates)
update_file("assets/cities/kas.json", kas_updates)
print("Updated Valencia (31), Çeşme (33), and Kaş (1). All Priority Cities enriched.")
