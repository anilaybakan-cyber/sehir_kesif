import json

# Manual enrichment data (Rovaniemi Batch 1: 40 items)
updates = {
    "Snowman World": {
        "description": "Kuzey Kutup Dairesi'ndeki kardan adam temalı buz dünyası, buz bar, buz heykeller ve kış aktiviteleri. Sıcak içecekler, buz kızağı ve çocuklar için eğlence.",
        "description_en": "Snowman-themed ice world at Arctic Circle with ice bar, ice sculptures, and winter activities. Hot drinks, ice sledding, and fun for children."
    },
    "Santa's Igloos Arctic Circle": {
        "description": "Cam tavanlı iglo konaklama, yataktan Kuzey Işıkları izleme fırsatı. Büyülü kış deneyimi, aurora borealis ve romantik gece.",
        "description_en": "Glass-roofed igloo accommodation with opportunity to watch Northern Lights from bed. Magical winter experience, aurora borealis, and romantic night."
    },
    "Nova Skyland Hotel": {
        "description": "Modern tasarımlı cam kulübe konaklama, Lapon doğasında lüks ve konfor. Kuzey Işıkları, sauna ve kış maceraları merkezi.",
        "description_en": "Modern design glass cabin accommodation with luxury and comfort in Lappish nature. Northern Lights, sauna, and winter adventures center."
    },
    "Three Elves Restaurant": {
        "description": "Noel Baba Köyü'nde geleneksel Lapon ve Finlandiya mutfağı sunan restoran. Ren geyiği eti, somon ve kış lezzetleri.",
        "description_en": "Restaurant serving traditional Lappish and Finnish cuisine in Santa Claus Village. Reindeer meat, salmon, and winter flavors."
    },
    "Loft Cafe": {
        "description": "Şehir merkezinde modern kafe, specialty coffee ve Finlandiya tarzı brunch. Rahat atmosfer, yerel lezzetler ve kahve kültürü.",
        "description_en": "Modern cafe in city center with specialty coffee and Finnish-style brunch. Relaxed atmosphere, local flavors, and coffee culture."
    },
    "Santa Claus Reindeer": {
        "description": "Ren geyiği çiftliği ve safari deneyimi, ren geyiği kızağı turu ve hayvanlarla tanışma. Lapon kültürü, beslemeler ve fotoğraf fırsatı.",
        "description_en": "Reindeer farm and safari experience with reindeer sleigh tour and meeting animals. Lappish culture, feeding, and photo opportunity."
    },
    "Husky Park": {
        "description": "Husky köpek kızağı turu ve çiftlik ziyareti, Alaskan malamute ve husky'lerle tanışma. Macera dolu kış aktivitesi ve hayvan sevgisi.",
        "description_en": "Husky dog sled tour and farm visit, meeting Alaskan malamutes and huskies. Adventure-filled winter activity and animal love."
    },
    "Arctic Circle Snowmobile Park": {
        "description": "Kar motoru safari ve kış maceraları merkezi, orman turları ve gece safari'leri. Adrenalin, Lapon doğası ve kar deneyimi.",
        "description_en": "Snowmobile safari and winter adventures center with forest tours and night safaris. Adrenaline, Lappish nature, and snow experience."
    },
    "Mrs. Santa Claus Christmas Cottage": {
        "description": "Noel Anne'nin şirin evi, zencefilli kurabiye yapma atölyesi ve kış masalı. Aileler için aktivite, sıcak çikolata ve Noel ruhu.",
        "description_en": "Mrs. Santa Claus's charming house with gingerbread cookie making workshop and winter fairy tale. Activity for families, hot chocolate, and Christmas spirit."
    },
    "Santa's Pizza & Burger": {
        "description": "Noel Baba Köyü'nde casual yeme-içme mekanı, hamburger ve pizza seçenekleri. Aileler için pratik öğle yemeği, çocuk dostu menü.",
        "description_en": "Casual dining venue in Santa Claus Village with hamburger and pizza options. Practical lunch for families, child-friendly menu."
    },
    "Iisakki Glass Village": {
        "description": "Cam iglo köyü ve resort, Kuzey Işıkları izleme ve lüks konaklama. Aurora hunting turları, sauna ve nordik wellness.",
        "description_en": "Glass igloo village and resort with Northern Lights viewing and luxury accommodation. Aurora hunting tours, sauna, and Nordic wellness."
    },
    "Wild Nordic Finland": {
        "description": "Doğa turları ve safari organizatörü, vahşi yaşam fotoğrafçılığı ve macera. Ayı gözlemi, kuş gözlemciliği ve ekolojik turizm.",
        "description_en": "Nature tours and safari organizer with wildlife photography and adventure. Bear watching, bird watching, and ecological tourism."
    },
    "Balmuir Store Arctic Circle": {
        "description": "Finlandiya'nın premium ev tekstili markasının mağazası, kaşmir ve lüks ürünler. Nordik tasarım, hediye seçenekleri ve kalite.",
        "description_en": "Store of Finland's premium home textile brand with cashmere and luxury products. Nordic design, gift options, and quality."
    },
    "Valley of Snowmen": {
        "description": "Kardan adam temalı eğlence alanı, buz pateni pisti ve kar aktiviteleri. Kış festivali atmosferi, aileler için eğlence.",
        "description_en": "Snowman-themed entertainment area with ice skating rink and snow activities. Winter festival atmosphere, entertainment for families."
    },
    "Christmas House Restaurant & Coffee Bar": {
        "description": "Noel temalı restoran ve kafe, Finlandiya tatlıları ve sıcak içecekler. Tatil ruhu, Noel dekorasyonu ve mevsimlik lezzetler.",
        "description_en": "Christmas-themed restaurant and cafe with Finnish desserts and hot drinks. Holiday spirit, Christmas decorations, and seasonal flavors."
    },
    "Pentik Arctic Circle": {
        "description": "Finlandiya seramik ve ev dekorasyonu markasının mağazası. El yapımı çanak çömlek, nordik tasarım ve hediyelik ürünler.",
        "description_en": "Store of Finnish ceramic and home decoration brand. Handmade pottery, Nordic design, and gift products."
    },
    "Marimekko Outlet": {
        "description": "İkonik Finlandiya moda markasının outlet mağazası, desenli tekstiller ve giyim. Cesur renkler, Finlandiya stili ve indirimli ürünler.",
        "description_en": "Outlet store of iconic Finnish fashion brand with patterned textiles and clothing. Bold colors, Finnish style, and discounted products."
    },
    "Santa Claus Holiday Village": {
        "description": "Noel Baba Köyü'ndeki konaklama ve aktivite merkezi, Noel temalı odalar ve safari turları. Aile tatili, kış maceraları ve Noel büyüsü.",
        "description_en": "Accommodation and activity center in Santa Claus Village with Christmas-themed rooms and safari tours. Family vacation, winter adventures, and Christmas magic."
    },
    "Lumberjack's Candle Bridge (Jätkänkynttilä)": {
        "description": "Kemijoki Nehri üzerindeki ikonik aydınlatmalı köprü, şehrin simgesi. Gece yürüyüşü, nehir manzarası ve fotoğraf için ideal.",
        "description_en": "Iconic illuminated bridge over Kemijoki River, city symbol. Ideal for night walk, river views, and photography."
    },
    "Rovaniemi City Hall": {
        "description": "Alvar Aalto'nun tasarladığı modernist belediye binası, Finlandiya mimarisinin ikonu. Post-savaş yeniden inşa ve nordik tasarım.",
        "description_en": "Modernist city hall designed by Alvar Aalto, icon of Finnish architecture. Post-war reconstruction and Nordic design."
    },
    "Lappia Hall": {
        "description": "Alvar Aalto'nun tasarladığı kültür merkezi, konser salonu ve tiyatro. Modernist mimari, kültürel etkinlikler ve Lapon sanatı.",
        "description_en": "Cultural center designed by Alvar Aalto with concert hall and theater. Modernist architecture, cultural events, and Lappish art."
    },
    "Bio Rex Rovaniemi": {
        "description": "Şehrin modern sinema kompleksi, uluslararası filmler ve Finlandiya yapımları. Popcorn, film geceleri ve eğlence.",
        "description_en": "City's modern cinema complex with international films and Finnish productions. Popcorn, movie nights, and entertainment."
    },
    "Rinteenkulma Shopping Centre": {
        "description": "Şehir merkezindeki alışveriş merkezi, Finlandiya markaları ve günlük ihtiyaçlar. Moda, market ve kış ekipmanları.",
        "description_en": "Shopping center in city center with Finnish brands and daily necessities. Fashion, market, and winter equipment."
    },
    "Taiga Koru": {
        "description": "El yapımı Lapon mücevherati ve takı dükkanı, geleneksel Sami tasarımları. Gümüş, ren geyiği boynuzu ve benzersiz hediyeler.",
        "description_en": "Handmade Lappish jewelry and accessories shop with traditional Sami designs. Silver, reindeer antler, and unique gifts."
    },
    "Lauri Historical Manor": {
        "description": "Tarihi Lapon çiftliği ve müze, geleneksel yaşam tarzı ve zanaat atölyeleri. Ahşap işçiliği, folklor ve Lapon kültürü.",
        "description_en": "Historic Lappish farm and museum with traditional lifestyle and craft workshops. Woodworking, folklore, and Lappish culture."
    },
    "Curio": {
        "description": "Lapon el sanatları ve hediyelik eşya dükkanı, yerel sanatçıların eserleri. Özel tasarımlar, doğa ilhamı ve hatıra.",
        "description_en": "Lappish handicrafts and souvenir shop with works of local artists. Special designs, nature inspiration, and memorabilia."
    },
    "Arctic Design Shop": {
        "description": "Finlandiya tasarımı ve nordik ürünlerin satıldığı konsept mağaza. Modern ev eşyaları, moda aksesuarları ve yaratıcı hediyeler.",
        "description_en": "Concept store selling Finnish design and Nordic products. Modern home items, fashion accessories, and creative gifts."
    },
    "Mainostoimisto Seven-1": {
        "description": "Yerel yaratıcı ajans ve tasarım stüdyosu, Lapon temalı işler ve projeler. Grafik tasarım, pazarlama ve yaratıcı endüstri.",
        "description_en": "Local creative agency and design studio with Lappish-themed works and projects. Graphic design, marketing, and creative industry."
    },
    "Poturi": {
        "description": "Klasik Finlandiya yemekleri ve ev yapımı lezzetler sunan geleneksel restoran. Karjalanpiirakka, lohikeitto ve nordik mutfak.",
        "description_en": "Traditional restaurant serving classic Finnish dishes and homemade flavors. Karelian pie, salmon soup, and Nordic cuisine."
    },
    "Piece of Lapland": {
        "description": "Lapon ürünleri ve gastronomi dükkanı, ren geyiği eti, meyve marmelatları. Yöresel lezzetler, gurme hediyeler ve Lapon mutfağı.",
        "description_en": "Lappish products and gastronomy shop with reindeer meat and berry jams. Local flavors, gourmet gifts, and Lappish cuisine."
    },
    "Rovaniemi Tourist Information": {
        "description": "Şehir turizmiBürosu, geziBilgisi ve aktivite rezervasyonları. Haritalar, öneriler ve seyahat planlama yardımı.",
        "description_en": "City tourism office with travel information and activity reservations. Maps, recommendations, and travel planning assistance."
    },
    "Arctic Warriors": {
        "description": "Macera turları ve outdoor aktiviteler organizatörü, hayatta kalma kursları. Doğa becerileri, kış kampı ve ekstrem deneyimler.",
        "description_en": "Adventure tours and outdoor activities organizer with survival courses. Nature skills, winter camping, and extreme experiences."
    },
    "Lapland Safaris Office": {
        "description": "Laponya'nın en büyük safari operatörü, kar motoru, husky ve ren geyiği turları. Kuzey Işıkları avcılığı ve kış maceraları.",
        "description_en": "Lapland's largest safari operator with snowmobile, husky, and reindeer tours. Northern Lights hunting and winter adventures."
    },
    "Nordic Unique Travels": {
        "description": "Özel tasarım Laponya turları ve lüks seyahat deneyimleri. Butik safari, aurora turları ve kişiselleştirilmiş programlar.",
        "description_en": "Custom-designed Lapland tours and luxury travel experiences. Boutique safari, aurora tours, and personalized programs."
    },
    "Santa's Hotel Santa Claus": {
        "description": "Şehir merkezinde Noel temalı otel, aile odaları ve restoran. Merkezi konum, Noel dekorasyonu ve konforlu konaklama.",
        "description_en": "Christmas-themed hotel in city center with family rooms and restaurant. Central location, Christmas decoration, and comfortable accommodation."
    },
    "Scandic Rovaniemi City": {
        "description": "Şehir merkezinde modern zincir otel, iş ve leisure konukları için. Finlandiya kahvaltısı, sauna ve şehir manzarası.",
        "description_en": "Modern chain hotel in city center for business and leisure guests. Finnish breakfast, sauna, and city views."
    },
    "Hostel Café Koti": {
        "description": "Bütçe dostu hostel ve kafe, backpacker'lar ve genç gezginler için. Ortak alanlar, kahve ve sosyal atmosfer.",
        "description_en": "Budget-friendly hostel and cafe for backpackers and young travelers. Common areas, coffee, and social atmosphere."
    },
    "Ounasvaara Observation Tower": {
        "description": "Ounasvaara tepesindeki manzara kulesi, şehir ve orman panoraması. Kuzey Işıkları izleme noktası, fotoğrafçılık ve doğa.",
        "description_en": "Observation tower on Ounasvaara hill with city and forest panorama. Northern Lights viewing point, photography, and nature."
    },
    "Ounaskoski Beach": {
        "description": "Kemijoki Nehri kıyısında şehir plajı, yaz aylarında yüzme ve güneşlenme. Piknik alanları, doğa ve nehir kenarı dinlenme.",
        "description_en": "City beach by Kemijoki River for swimming and sunbathing in summer. Picnic areas, nature, and riverside relaxation."
    },
    "Santa's Forest (Joulukan Metsä)": {
        "description": "Noel temalı doğa yürüyüş parkuru, Noel Baba'nın ormanında keşif. Aileler için aktivite, kar yürüyüşü ve masal atmosferi.",
        "description_en": "Christmas-themed nature walking trail, exploration in Santa's forest. Activity for families, snow walking, and fairy-tale atmosphere."
    }
}

filepath = 'assets/cities/rovaniemi.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data['highlights']:
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        print(f"Enriched: {name}")
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Manually enriched {count} items (Rovaniemi Batch 1).")
