import json

path = "assets/cities/budva.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mapping generated content (TR, EN) for the first 43 venues in Budva
updates = {
    "ChIJG6l0D8lrWxMRkR7N7X5_K8Y": {
        "tr": "Sveti Nikola Adası (Hawaii), Budva sahilinin tam karşısında yer alan ve kristal suları, kayalık kıyıları ve egzotik bitki örtüsüyle Karayipler'i anımsatan Karadağ'ın en büyük kentsel deniz kaçış noktasıdır.",
        "en": "Sveti Nikola Island (Hawaii) is Montenegro's largest urban maritime escape, located just off the Budva coast and reminiscent of the Caribbean with its crystal waters, rocky shores, and exotic flora."
    },
    "ChIJ9_m_wQBrWxMR8M-mH4FuDqk": {
        "tr": "Jaz Plajı, Adriyatik'in en geniş kentsel sahil şeritlerinden biri olup, sadece masmavi deniziyle değil, aynı zamanda dünyaca ünlü kentsel festivallere ve konserlere ev sahipliği yapan enerjik kentsel atmosferiyle tanınır.",
        "en": "Jaz Beach is one of the widest urban coastal stretches on the Adriatic, famed not only for its deep blue sea but also for its energetic urban vibe, hosting world-renowned music festivals and concerts."
    },
    "ChIJ7ao8_dNrWxMRU0mPZ2Y3jHw": {
        "tr": "Ričardova Glava Plajı, Budva Eski Şehir surlarının hemen dibinde yer alan kentsel bir prestij kalesidir. Tarihi dokuyla iç içe olan bu sahil, kentsel sosyal hayatın ve gün batımı keyfinin en ikonik duraklarındandır.",
        "en": "Ričardova Glava Beach is an urban prestige stronghold nestled against the Budva Old Town walls. This coastal spot, merged with historic textures, is one of the city's most iconic stops for social life and sunsets."
    },
    "ChIJiS9aAQBrWxMRaZ6_3X5_K8Y": {
        "tr": "Avala Resort & Villas, kentsel modernlikle tarihi surları birleştiren, Budva'nın en prestijli ve ikonik kentsel konaklama duraklarından birisidir. Panoramik deniz manzaralı havuzuyla kentsel lüksü adeta taçlandırmaktadır.",
        "en": "Avala Resort & Villas merges urban modernity with historic walls as one of Budva's most prestigious and iconic stay destinations. Its panoramic sea-view pool perfectly crowns the city's high-end luxury lifestyle."
    },
    "ChIJP5X_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Vaftizci Aziz John Kilisesi, 7. yüzyıldan kalan kentsel temelleri ve meşhur çan kulesiyle Budva Eski Şehir silüetinin en manevi ve panoramik kentsel duraklarından bir tanesi olarak kentsel tarihe ışık tutar.",
        "en": "Church of Saint John the Baptist, with its 7th-century foundations and iconic bell tower, stands as one of the most spiritual and panoramic landmarks in the Budva Old Town urban silhouette today."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Kosmač Kalesi, Avusturya-Macaristan imparatorluğu döneminden kalan ve Adriyatik kıyısını tepeden gören kentsel bir askeri mimari örneğidir. Kentin savunma tarihini ve kentsel stratejik önemini gezginlere anladır.",
        "en": "Fort Kosmač is a specimen of urban military architecture from the Austro-Hungarian era, overlooking the Adriatic coast. It reveals the city's defensive history and strategic urban importance to every traveler."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Brajići Yamaç Paraşütü Noktası, Adriyatik'in masmavi manzarasına karşı havalanacağınız, kentin en heyecan verici ve kentsel adrenalin duraklarından biridir. Gökyüzünden kentsel silüeti izlemek kentsel bir prestijdir.",
        "en": "Brajići Paragliding launch point is one of the city's most exciting urban adrenaline stops, where you soar against the Adriatic blue. Viewing the urban silhouette from the sky is a true prestige experience."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Budva Şehir Müzesi, Eski Şehir'deki tarihi binasında antik dönemden bugüne kentsel kültürel mirası ve arkeolojik buluntuları anlatan, kentin kentsel hafızasındaki en prestijli kentsel tarih penceresidir.",
        "en": "Budva City Museum, set in a historic Old Town building, details the city's urban cultural heritage and archaeological finds since ancient times as the most prestigious urban history window in the city."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kutsal Üçlü Kilisesi (Holy Trinity), kentsel silüetin en renkli ve estetik duraklarından biri olup kentsel Bizans mimarisini ve kentsel inanç kültürünü kenti keşfeden gezginlerle buluşturan önemli bir kaledir.",
        "en": "Holy Trinity Church is one of the most colorful and aesthetic landmarks in the urban silhouette, merging urban Byzantine architecture with the city's faith culture for every traveler exploring Budva."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Aquapark Budva, Adriyatik manzarasına karşı kurulan ve Avrupa'nın en prestijli su parklarından biri olarak kentin en dinamik kentsel eğlence kompleksidir. Her yaştan kentsel gezgin için kentsel bir eğlencedir.",
        "en": "Aquapark Budva is one of Europe's most prestigious water parks, built against Adriatic views as the city's most dynamic urban entertainment complex, offering fun for every age of urban traveler."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Montenegro Rent-a-Boat, Adriyatik'in gizli koylarını ve kentsel deniz kültürünü keşfetmek isteyenler için kentin en profesyonel kentsel deniz macerası noktalarından biri olarak turizm haritasında yer alır.",
        "en": "Montenegro rent-a-boat is one of the most professional urban maritime adventure points for those wanting to discover hidden Adriatic coves and urban sea culture on the city's tourism map."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Podmaine Manastırı, kentsel sükunetin ve kentsel maneviyatın kentsel zirvesi olan, freskleriyle ünlü kentsel bir tarih kalesidir. Kentin karmaşasından uzaklaşıp kentsel bir iç huzur vaat eden bir duraktır.",
        "en": "Podmaine Monastery is an urban history stronghold famous for its frescoes and serving as the peak of city tranquility and spirituality, promising a sense of inner peace away from the urban rush."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Budva Fıskiyeli Meydanı, kentsel dinamizmin ve kentsel sosyal hayatın en canlı kentsel noktalarından birisi olup kentsel buluşma ve kentsel dinlenme durakları arasında en popüler ve kentsel rotadır.",
        "en": "The traffic circle with Fountains is one of the liveliest urban spots for social life and dynamism, standing as the most popular and vibrant route among Budva's meeting and relaxation landmarks."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Topdent Montenegro, kentin modern sağlık turizmi haritasındaki en prestijli ve kentsel sağlık duraklarından birisi olarak kentsel kaliteyi ve kentsel uzmanlığı kenti keşfeden gezginlere sunmaktadır.",
        "en": "Topdent Montenegro stands as one of the most prestigious urban health stops on the city’s modern medical tourism map, offering urban quality and expertise to travelers visiting Budva today."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Flying Adventure Paragliding, kentsel silüetin ve Adriyatik'in paha biçilemez manzarasını gökyüzünden keşfedeceğiniz kentin en heyecan verici ve kentsel adrenalin kentsel macerasıduraklarından biridir.",
        "en": "Flying Adventure Paragliding is one of the town's most exciting urban adrenaline points, where you discover the urban silhouette and priceless Adriatic vistas from the sky for a unique city adventure."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Montenegrome, kentin kentsel modernliğini ve yerel kültürel mirasını anlatan, kenti keşfeden gezginlerin kentsel keşif haritasındaki en prestijli ve entelektüel kentsel tarih penceresidir.",
        "en": "montenegrome detail the city's urban modernity and local cultural heritage, standing as the most prestigious and intellectual urban history window on the discovery map for all Budva visitors."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Pet Friendly Beach, kentsel sosyal hayatın en samimi ve kentsel hayvan dostu duraklarından birisi olup kentin kentsel kumsal ruhunu tüm dostlarımızla paylaşabileceğiniz kentsel bir prestij noktasıdır.",
        "en": "Pet Friendly Beach is one of the friendliest urban and animal-loving stops in social life, serving as an urban prestige point where you can share the city's coastal spirit with all our furry friends."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Nenov Brod, kentsel liman şeridinde yer alan ve kentsel deniz kültürünün taze lezzetlerini kenti keşfeden gezginlerle buluşturan kentin en samimi ve kentsel lezzet duraklarından birisi olarak bilinir.",
        "en": "Nenov brod is known as one of the city's most friendly and urban flavor stops on the waterfront, bringing the fresh tastes of urban maritime culture to travelers exploring the coast of Budva."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Gringo Boat, Adriyatik'in gizli koylarını ve kentsel deniz kültürünü keşfetmek isteyenler için kentin en profesyonel kentsel deniz macerası noktalarından biri olup turizm haritasında yer alır.",
        "en": "Gringo Boat is one of the most professional urban maritime adventure points for those wanting to discover hidden Adriatic coves and urban sea culture on the city's active tourism map today."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ciapson Cat, kentsel sosyal hayatın en özgün ve sürprizli kentsel duraklarından birisi olup kentin kentsel estetik ve kentsel dinamizmini kenti keşfeden gezginlere kentsel bir nükteyle anladır.",
        "en": "Ciapson Cat is one of the most unique and surprising urban stops in social life, revealing the city's aesthetic and dynamism to travelers through a witty and creative urban landmark."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Public Dock Budva, kentsel liman hayatının kalbi olup kentin kentsel silüetini ve kentsel deniz ulaşımını kenti keşfedenlerin kentsel keşif albümündeki en ikonik ve fotojenik kentsel duraklardan kentselidir.",
        "en": "Public Dock is the heart of urban port life, standing as one of the most iconic and photogenic urban spots in discovery albums, merging city sights with Budva's maritime transportation network."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Panorama Boat Taxi, kentsel deniz ulaşımını kentsel bir panoramik keşfe dönüştüren kentin en popüler kentsel sosyal ve kentsel ulaşım duraklarından biri olarak kentsel hayatın bir parçasıdır.",
        "en": "Budva Taxi Panorama Boat transforms urban sea travel into a panoramic discovery, serving as one of the city's most popular social and transport stops in everyday urban life for visitors and locals."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Turist Market 4, kentin her noktasına yayılan kalitesi ve taze yerel ürünleriyle kenti keşfeden gezginlerin en pratik ve popüler kentsel lezzet duraklarından birisi olarak kentin kalbinde yer alır.",
        "en": "Turist Market 4 is a beloved urban stop in the city center, known for its quality and fresh local produce that serves as a practical and fast flavor destination for every urban traveler in Budva."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Budva Tourist Capital, kentin kentsel turizm dünyasındaki prestijini ve binlerce yıllık kültürel mirasını anlatan, kentsel sosyal hayatın ve kentsel turizmin en önemli ve kentsel rotasıdır.",
        "en": "Budva Tourist Capital details the city's prestige in urban tourism and its millennia-old cultural heritage, standing as the most vital and significant urban route for social life and city discovery."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hotel Mogren, Budva Eski Şehir surlarına nazır konumu ve kentsel tarihi dokusuyla kentsel konaklama dünyasının en prestijli ve köklü kentsel duraklarından birisi olup turizm haritasında yer alır.",
        "en": "Hotel Mogren is one of the city's most prestigious and established stay destinations, featuring a historic vibe and views of the Old Town walls that secure its spot on the tourism map."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hotel Sanja, kentsel modernliği ve kentsel sükuneti birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestij ve konaklama durağı kalesidir.",
        "en": "Hotel Sanja (formerly Olivia) is a prestigious urban stay destination merging modern style with a sense of urban tranquility, standing as one of Budva's most refined social escape strongholds."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hotel Admiral, kentsel modernliği ve Adriyatik'in masmavi deniz manzaralı kentsel terasını birleştiren şık tasarımıyla kentsel sosyal hayatın en prestijli ve 4 yıldızlı kentsel duraklarından biridir.",
        "en": "Hotel Admiral merges urban modernity with a stylish terrace overlooking the deep blue Adriatic, standing as one of the most prestigious 4-star urban destinations in the city's social scene."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hotel Adrović, kentsel prestijin ve kentsel gastronomi dünyasının birleştiği, Sveti Stefan manzaralı kentsel kalesiyle kentin en prestijli ve ikonik kentsel restoran ve konaklama duraklarından biridir.",
        "en": "Hotel & Restaurant Adrović is a prestigious hub where city prestige meets culinary culture, offering views of Sveti Stefan from its urban fortress as an iconic rest and dining destination."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Spa Resort Becici, lüks kentsel dinlenmenin ve kentsel modernliğin kentsel zirvesi olup kentsel konaklama dünyasının en prestijli ve kentsel sağlık duraklarından birisi olarak kenti keşfedenlere hitap eder.",
        "en": "Spa Resort Becici represents the peak of luxury urban relaxation and modernity, standing as one of the most prestigious and high-end health stops in the city's active accommodation scene."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hotel Aleksandar, kentsel modernliği ve Adriyatik sahilinin huzurunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "Hotel and Restaurant Aleksandar is a prestigious urban route offering one of the most refined social escape spots in town, featuring a design that merges city energy with coastal tranquility."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Astoria Budva, Eski Şehir'in kalbinde yer alan kentsel modernliği ve tarihi dokusuyla kentsel konaklama dünyasının en prestijli ve 'boutique' kentsel duraklarından birisi olup kentin kalbinde yer alır.",
        "en": "Astoria is one of the most prestigious boutique stay destinations in Budva Old Town, merging urban modernity with historic textures as a central landmark in the city's most active district."
    },
    "ChIJv7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hotel TQ Plaza, kentsel modernliği ve kentsel dinamizmi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli konaklama durağıdır.",
        "en": "Hotel TQ Plaza is a prestigious urban stay destination merging modern style with city dynamism, standing as one of Budva's most refined social escape strongholds in the modern center."
    },
    "ChIJw7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kod Saičića, geleneksel Balkan mutfağının kentsel gastronomi dünyasındaki taze ve yerel lezzet kalesi olup kentin en samimi ve kentsel lezzet duraklarından birisi olarak kentsel sosyal hayatın kalesidir.",
        "en": "Kod Saičića is a culinary stronghold for traditional Balkan kitchen flavors, recognized for its fresh local products as one of the city's most friendly and reliable urban taste destinations."
    },
    "ChIJx7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kužina, adından da anlaşılacağı gibi 'mutfağın kalbi' olup geleneksel Karadağ lezzetlerini kentsel bir modernlikle sunan kentin en popüler ve kentsel lezzet duraklarından birisi olarak öne çıkmaktadır.",
        "en": "Kužina is truly the 'heart of the kitchen,' offering traditional Montenegrin flavors with an urban modern touch as one of the city's most popular and authentic local flavor destinations today."
    },
    "ChIJy7m_wQBrWxMRNM-mH4FuDqk": {
        "tr": "Hong Kong Restaurant, kentsel gastronomi dünyasına Asya mutfağının kentsel ve egzotik dokunuşlarını getiren kentin en stil sahibi kentsel lezzet duraklarından birisi olup turizm haritasında yer alır.",
        "en": "Hong Kong Restaurant brings an exotic urban twist of Asian cuisine to the city's food world, standing out on the tourism map as one of Budva's most stylish and diverse flavor destinations."
    },
    "ChIJz7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Obala, kentsel sahil şeridinde yer alan ve masmavi deniz manzarası eşliğinde taze deniz ürünleri sunan kentsel sosyal hayatın en köklü ve kentsel lezzet duraklarından kentsel bir prestij noktasıdır.",
        "en": "Obala is one of the most established and prestigious flavor stops on the city waterfront, offering fresh seafood with views of the deep blue sea for a memorable urban social dining day."
    },
    "ChIJ07m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Tropico, kentsel kumsalda yer alan ve kentsel eğlenceyi dalga sesleriyle buluşturan kentin en büyüleyici kentsel buluşma duraklarından biridir. Kentsel modernliğiyle kentsel prestijli bir kentsel duraktır.",
        "en": "Tropico is one of the most enchanting urban meeting spots on the waterfront, merging city fun with the sound of the waves while maintaining its status as a prestigious destination in Budva."
    },
    "ChIJ17m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Restoran Kralj, kentsel gastronomi haritasında taze ürünleri ve iddialı sunumlarıyla tanınan prestijli bir kentsel lezzet durağıdır. Isminden de anlaşılacağı gibi kentsel lezzet kentsel krallığı duraktır.",
        "en": "Restoran Kralj is a prestigious urban flavor destination recognized for its fresh products and ambitious service on the food map, standing as a culinary kingdom in the heart of Budva."
    },
    "ChIJ27m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "WOW Restaurant, kentsel modernliği ve kentsel dinamizmi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli lezzet durağıdır.",
        "en": "WOW Restaurant & Bar is a prestigious urban flavor sanctuary merging modern style with city energy, standing as one of Budva's most refined and impressive social escape strongholds."
    },
    "ChIJ37m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Jadran Kod Krsta, kentsel liman şeridinin en köklü ve prestijli lezzet kalesi olup deniz ürünlerindeki uzmanlığıyla kentsel sosyal hayatın ve lezzet dünyasının en önemli kentsel rotası kentsel duraktır.",
        "en": "Jadran is the most established and prestigious flavor stronghold on the city harbor front, representing the peak of urban seafood expertise and serving as a vital route for every food lover."
    },
    "ChIJ47m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "La Bocca, kentsel modernliği ve Adriyatik sahilinin huzurunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "La Bocca is a prestigious urban route offering one of the most refined social escape spots in town, featuring a design that merges city energy with a sense of immense Adriatic seaside calm."
    },
    "ChIJ57m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "BALKAN BUDVA, kentsel gastronomi dünyasına kentin kentsel ve yerel Balkan lezzetlerini en taze haliyle sunan kentin en popüler ve kentsel lezzet duraklarından birisi olup turizm haritasında yer alır.",
        "en": "BALKAN BUDVA brings the heart of local Balkan cuisine to the town's food world at its freshest, standing out on the tourism map as one of the most popular and authentic flavor destinations."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Lim Restaurant, kentsel liman şeridinde yer alan ve kentsel deniz kültürünün taze lezzetlerini kenti keşfeden gezginlerle buluşturan kentin en samimi ve prestijli kentsel lezzet duraklarından biridir.",
        "en": "Lim Restaurant looks over the city waterfront, serving as the address for those looking for authentic flavor mastery in fresh seafood while staying close to the vibrant urban scene of Budva."
    }
}

for h in data["highlights"]:
    if h["id"] in updates:
        h["description"] = updates[h["id"]]["tr"]
        h["description_en"] = updates[h["id"]]["en"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Budva Batch 1 (43 venues).")
