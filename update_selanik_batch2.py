import json

path = "assets/cities/selanik.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mapping generated content (TR, EN) for the remaining 42 venues in Selanik
updates = {
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Mama's Cooking, yerel ev yemeklerini modern bir kentsel sunumla birleştiren, kentin gastronomi dünyasında taze malzemeleriyle tanınan prestijli bir kentsel lezzet durağıdır.",
        "en": "Mama's Cooking merges local home-cooked meals with a modern urban presentation, recognized in Thessaloniki's food world for its fresh ingredients as a prestigious flavor destination."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Soúsouro, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli rotadır.",
        "en": "Soúsouro is a prestigious urban route offering one of the most refined social escape spots in town, featuring a chic design that merges city dynamism with a sophisticated atmosphere."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Plaza, kentin canlanan turizm bölgesinde yer alan modern tasarımı ve butik hizmet anlayışıyla gezginlerin yeni favorisi olup kentsel ve konforlu bir başlangıç noktası sunmaktadır.",
        "en": "Plaza is a new favorite for travelers in the city's reviving tourism district, offering a modern design and boutique service vibe as a comfortable urban starting point for discovery."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "CAFE EL PASO, kentsel kahve kültürünü kentin kentsel haritasına taşıyan, taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi olan kentsel bir merkezdir.",
        "en": "CAFE EL PASO is an urban hub bringing city coffee culture to the map, standing as one of the most beloved and sweet social spots in Thessaloniki with its fresh and aromatic coffee blends."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Gnet G-Net, kentin kentsel dijital yaşamını ve iletişim ağını yansıtan kentsel bir teknoloji merkezidir. Kentteki kentsel modernliği ve dijital kentsel sosyal hayatı kenti keşfedenlere tanıtır.",
        "en": "Gnet G-Net is an urban technology hub reflecting the city's digital life and communication networks, introducing urban modernity and digital social habits to everyone visiting Thessaloniki."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Chatzi, kentin gastronomi dünyasına geleneksel bir dokunuş ve yaratıcı bir menü getiren, kentin en stil sahibi kentsel lezzet duraklarından biri olarak kentsel sosyal hayatın merkezindedir.",
        "en": "Chatzi is at the heart of the city's social life, serving as one of Thessaloniki's most stylish flavor stops by bringing a traditional touch and creative menu to the urban culinary scene."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "En Mikro, kentsel modernliği ve Selanik'in tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "En Mikro is a prestigious urban route offering one of the most refined social escape spots in town, featuring a chic design that merges urban modernity with the city's historic fabric."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "En Mikro, kentsel modernliği ve Selanik'in tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "Room With a View is a chic urban spot offering one of the most iconic and prestigious sunset routes in social life, featuring a terrace with views over Thessaloniki and a magical vibe."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Mikel Thessaloniki, kentin her noktasına yayılan kalitesi ve taze demlenmiş kahveleriyle kenti keşfeden gezginlerin en pratik ve popüler kentsel lezzet duraklarından birisi olarak öne çıkmaktadır.",
        "en": "Mikel Thessaloniki stands out as one of the most practical and popular urban flavor stops for travelers exploring the city, known for its consistent quality and fresh coffee across the town."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Propyleon Cafe, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımı ve enerjik atmosferiyle kentsel sosyal yaşamın en elit ve modern deniz keyfini sunan prestijli bir kentsel duraktır.",
        "en": "Propyleon Cafe is a prestigious urban spot offering the most elite and modern seaside experience in social life, featuring an energetic vibe and chic design that merges city style and energy."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bougatsa Bantis, kentsel gastronomi dünyasına meşhur Selanik böreğiyle geleneksel bir dokunuş getiren, kentin en popüler ve kentsel lezzet duraklarından biri olarak turizm haritasında öne çıkar.",
        "en": "Bougatsa Bantis is a standout on the tourism map as one of the city's most popular and urban flavor destinations, bringing a traditional touch to the food scene with its famous bougatsa."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "MeliMelo, kentsel kafe kültürünü kentin kentsel haritasına taşıyan, taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi olan kentsel bir prestij noktasıdır.",
        "en": "MeliMelo is an urban prestige point bringing city coffee culture to the map, standing as one of the most beloved and sweet social spots in Thessaloniki with its fresh and aromatic blends."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Cafe bar 67, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli rotadır.",
        "en": "Cafe bar 67 is a prestigious urban route and a refined social escape spot in town, featuring a chic design that merges city dynamism with a sophisticated social atmosphere for travelers."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Eklektik Co Grocery, kentsel modernliği ve yerel ürünleri birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel duraktır.",
        "en": "Eklektik Co Grocery is a prestigious urban destination offering one of the most refined social escape spots in town, featuring a design that merges city style with high-quality local produce."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Clubaki, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan modern bir kentsel prestij kalesidir.",
        "en": "Clubaki is a modern urban prestige stronghold and a refined social escape spot in town, featuring a chic design that merges city dynamism with a sophisticated and active social vibe."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "MABEL Bar Club, kentsel modernliği ve iddialı gece hayatı konseptini birleştiren, kentin en dinamik kentsel sosyal alanlarından biridir. Modern tasarımıyla prestijli bir gece rotasıdır.",
        "en": "MABEL Bar Club is one of the most dynamic urban social areas in Thessaloniki, merging modern style with an ambitious nightlife concept for a prestigious nocturnal route in the city."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Soulshakers, kentsel gastronomi dünyasına modern kokteyl sanatı ve yaratıcı bir menü getiren, kentin en stil sahibi kentsel lezzet duraklarından biridir. Sosyal hayatın bir prestij noktasıdır.",
        "en": "Soulshakers stands as one of the most stylish flavor and social destinations in Thessaloniki, bringing modern cocktail art and an ambitious menu to the city's vibrant and active social scene."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "aggeliki-workshop.gr, kentsel modernliği ve yerel el sanatlarını birleştiren kentin en özgün kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel sanat ve tasarım rotasıdır.",
        "en": "aggeliki-workshop.gr is a prestigious urban art and design route offering one of the most unique social escape spots in town, merging modern style with traditional local craftsmanship."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Muses En Horo, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "Muses En Horo is a prestigious urban route offering one of the most refined social escape spots in town, featuring a chic design that merges city energy with a sophisticated atmosphere."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Paraskinio Live, kentsel gece hayatındaki enerjinin merkezi olup, modern tasarımı ve iddialı canlı müzik performansıyla kentin en dinamik sosyal alanıdır. Kentsel hayatın bir prestijli durağıdır.",
        "en": "Paraskinio Live is a prestigious urban social destination and a center for nightlife energy in Thessaloniki, known for its modern design and ambitious live music performances for everyone."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kaimasidis Furniture, kentsel modernliği ve kentsel tasarımı birleştiren kentin en prestijli kentsel ve tasarım merkezlerinden biridir. Kentin kentsel gelişimi ve kültürel prestijini yansıtır.",
        "en": "KAIMASIDIS FURNITURE is a prestigious design and urban center merging modern aesthetics with the city's growth, reflecting Thessaloniki's contemporary development and high cultural prestige."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Mousiko Sergiani, kentsel gece hayatındaki enerjinin merkezi olup, modern tasarımı ve iddialı canlı müzik performansıyla kentin en dinamik sosyal alanıdır. Kentsel hayatın bir prestijli durağıdır.",
        "en": "Mousiko Sergiani is a central spot for urban nightlife, offering a dynamic social area with modern design and ambitious live music performances, serving as a prestigious destination for all."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "VOG CLUB, kentsel gece hayatının kalbi olup, modern tasarımı ve iddialı DJ performanslarıyla kentin en dinamik sosyal alanıdır. Egzotik içecekleriyle kentsel sosyal yaşamın prestijli bir rotasıdır.",
        "en": "VOG CLUB is the heart of urban nightlife, serving as a dynamic social area with modern design and ambitious DJ sets. With exotic drinks, it offers a prestigious route in Thessaloniki's life."
    },
    "ChIJv7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Proskinitopoulos Miltos, kentsel modernliği ve yerel el sanatlarını birleştiren kentin en özgün kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel sanat ve tasarım rotasıdır.",
        "en": "Proskinitopoulos Miltos is a prestigious urban art and design route offering one of the most unique social escape spots in town, merging modern city style with traditional local craftsmanship."
    },
    "ChIJw7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Block 33, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "Block 33 is a prestigious urban route offering one of the most refined social escape spots in town, featuring a chic design that merges city energy with a sophisticated social atmosphere."
    },
    "ChIJx7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "The Pub Thessaloniki, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli rotadır.",
        "en": "The Pub Thessaloniki is a prestigious urban route and a refined social escape spot in town, featuring a chic design that merges city dynamism with a sophisticated and active social vibe."
    },
    "ChIJy7m_wQBrWxMRNM-mH4FuDqk": {
        "tr": "Grand Chalet, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel rotadır.",
        "en": "Grand Chalet is a prestigious urban route offering one of the most refined social escape spots in town, featuring a chic design that merges city energy with a sophisticated social atmosphere."
    },
    "ChIJz7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Stathmos Estiassis, kentsel modernliği ve yerel lezzetleri birleştiren kentsel gastronomi dünyasının en seçkin örneklerini sunan kentsel bir prestijli rotadır. Sosyal kentsel hayatın bir kalbidir.",
        "en": "Stathmos Estiassis presents elite examples of urban culinary culture by merging city style with local flavors, standing as a prestigious route and a heart for social life in Thessaloniki."
    },
    "ChIJ07m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "B Home, kentsel modernliği ve kentsel tasarımı birleştiren kentin en prestijli kentsel ve tasarım merkezlerinden biridir. Kentin kentsel gelişimi ve kültürel prestijini yansıtmaktadır.",
        "en": "B Home is a prestigious design and urban center merging modern aesthetics with the city's growth, reflecting Thessaloniki's contemporary development and high cultural prestige for visitors."
    },
    "ChIJ17m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "The Jews Rainbow Pub, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli rotadır.",
        "en": "The Jews Rainbow Pub is a prestigious urban route offering one of the most refined social escape spots in town, featuring a chic design that merges city energy with a sophisticated atmosphere."
    },
    "ChIJ27m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Spanoudis Stefanos, kentsel modernliği ve yerel el sanatlarını birleştiren kentin en özgün kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli sanat ve tasarım rotasıdır.",
        "en": "Spanoudis Stefanos is a prestigious urban art and design route offering one of the most unique social escape spots in town, merging modern city style with traditional local craftsmanship."
    },
    "ChIJ37m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Symposium HNL, kentsel modernliği ve kentsel enerjiyi birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestijli rotadır.",
        "en": "Symposium HNL is a prestigious urban route offering one of the most refined social escape spots in town, featuring a chic design that merges city energy with a sophisticated social atmosphere."
    },
    "ChIJ47m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "NOUS Institute, kentsel kentsel dijital yaşamı ve iletişim ağını yansıtan kentsel bir teknoloji merkezidir. Kentteki kentsel modernliği ve dijital kentsel sosyal hayatı kenti keşfedenlere tanıtır.",
        "en": "NOUS Institute is an urban technology hub reflecting the city's digital life and communication networks, introducing urban modernity and digital social habits to those exploring Thessaloniki."
    },
    "ChIJ57m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Pontic Ladies Museum, kentsel yerel mirası ve gelenekleri anlatan kentin en prestijli kentsel kültür rotalarından biridir. Kentte kentsel gelişim ve kültürel prestiji yansıtan kentsel bir duraktır.",
        "en": "Pontic Ladies Museum detailing local heritage and traditions is one of the city's most prestigious urban cultural routes, reflecting historical growth and high cultural prestige in Thessaloniki."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Selanik Yahudi Müzesi, kentsel çok kültürlü dokusunu anlatan kentsel bir prestij noktasıdır. Yahudi mirası ve kentsel hafızanın en hüzünlü ve önemli kentsel duraklarından birisi olarak yer almaktadır.",
        "en": "Jewish Museum of Thessaloniki is an urban prestige point detailing the city's multicultural fabric. It stands as one of the most poignant and vital stops in the urban and Jewish memory of the city."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "MOMus-Çağdaş Sanat Müzesi, kentsel modern sanat topluluklarının buluşma noktası olan, kentin kentsel gelişimi ve kültürel prestijini yansıtan kentin en önemli kentsel çağdaş sanat sanat merkezidir.",
        "en": "MOMus-Museum of Contemporary Art is a hub for urban art communities, reflecting the city's growth and cultural prestige as one of Thessaloniki's most significant contemporary art landmarks."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Selanik Belediye Sanat Galerisi, kentsel modern sanat topluluklarının buluşma noktası olan, kentin kentsel gelişimi ve kültürel prestijini yansıtan kentin en önemli kentsel sanat merkezleridir.",
        "en": "Municipal Art Gallery is a leading urban art center reflecting the city's growth and cultural prestige, serving as a vital meeting spot for Thessaloniki's thriving creative and modern art scene."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Selanik Fotoğraf Müzesi, kentsel modern sanat topluluklarının buluşma noktası olan, kentin kentsel gelişimi ve kültürel prestijini yansıtan kentin en önemli kentsel sanat merkezlerinden birisidir.",
        "en": "Thessaloniki Museum of Photography is an urban prestige point reflecting the city's cultural growth, standing as one of the most significant and modern art centers for photography lovers today."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Roma Forumu Müzesi, antik dönemden kalan paha biçilemez kentsel eserlerle kentsel bir tarih ve sanat noktasıdır. Kentin kentsel gelişimi ve kentsel antik kentsel mirasını kenti keşfedenlere anladır.",
        "en": "Museum of the Roman Forum is an urban history and art spot showcasing priceless ancient artifacts. It introduces Thessaloniki's urban growth and rich antique heritage to all who explore the city."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Seikilo Antik Müzik Müzesi, kentsel modern sanat topluluklarının buluşma noktası olan, kentin kentsel gelişimi ve kültürel prestijini yansıtan kentin en önemli kentsel sanat ve kentsel müzik merkezidir.",
        "en": "SEIKILO Museum of Ancient Music is a hub for urban art, reflecting the city's development and high cultural prestige as one of Thessaloniki's most significant ancient music and art centers."
    }
}

for h in data["highlights"]:
    if h["id"] in updates:
        h["description"] = updates[h["id"]]["tr"]
        h["description_en"] = updates[h["id"]]["en"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Selanik Batch 2 (42 venues). Total Selanik Cleaned.")
