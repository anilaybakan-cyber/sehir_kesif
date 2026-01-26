import json

# Manual enrichment data (Belgrad Batch 2: 40 items)
updates = {
    "Museum of Paja Jovanovic": {
        "description": "Ünlü Sırp ressam Paja Jovanović'in eserlerini ve atölyesini sergileyen küçük sanat müzesi. 19. yüzyıl Sırp resminin önemli figürü, portreleri ve tarihi sahneler.",
        "description_en": "A small art museum exhibiting works and studio of famous Serbian painter Paja Jovanović. An important figure of 19th century Serbian painting, portraits and historical scenes."
    },
    "Jevremovac Greenhouse": {
        "description": "Botanik bahçenin içindeki tarihi cam sera, tropikal ve egzotik bitki koleksiyonlarıyla. Kış aylarında sıcak kaçış, nadir türler ve botanik keşif.",
        "description_en": "A historic glass greenhouse inside the botanical garden with tropical and exotic plant collections. A warm escape in winter months, rare species and botanical discovery."
    },
    "Ušće Tower": {
        "description": "Yeni Belgrad'ın ikonik gökdeleni, şehrin en yüksek binalarından biri. Modern iş merkezi, Sava Nehri manzarası ve çağdaş Belgrad'ın simgesi.",
        "description_en": "An iconic skyscraper of New Belgrade, one of the city's tallest buildings. A modern business center, Sava River views and symbol of contemporary Belgrade."
    },
    "St. Sava Plateau": {
        "description": "Sveti Sava Kilisesi'ni çevreleyen geniş meydan, şehrin en büyük açık alanlarından biri. Festivaller, konserler ve toplumsal etkinlikler için merkezi buluşma noktası.",
        "description_en": "The wide square surrounding St. Sava Church, one of the city's largest open spaces. A central meeting point for festivals, concerts and community events."
    },
    "Tasmajdan Caves": {
        "description": "Şehir merkezinde antik Roma döneminden kalma olduğu düşünülen yeraltı mağaraları ve su kaynakları. Keşfedilmeyi bekleyen gizemli tarih, rehberli turlar mevcut değil.",
        "description_en": "Underground caves and water sources in city center thought to date from ancient Roman period. Mysterious history waiting to be explored, guided tours not available."
    },
    "Smokvica Molerova": {
        "description": "Sahil şeridinde konumlanan, Akdeniz lezzetleri ve deniz ürünleri sunan şık restoran. Gün batımı manzarası, romantik yemekler ve Adriyatik ilhamı.",
        "description_en": "A stylish restaurant located on the waterfront serving Mediterranean flavors and seafood. Sunset views, romantic dinners and Adriatic inspiration."
    },
    "Supermarket Deli": {
        "description": "Şehrin en popüler brunch mekanlarından biri, yaratıcı kahvaltı menüsü ve vintage dekorasyonuyla. Hafta sonu kuyruğu, Instagram'a uygun sunumlar ve kaliteli kahve.",
        "description_en": "One of the city's most popular brunch spots with creative breakfast menu and vintage decor. Weekend queues, Instagram-worthy presentations and quality coffee."
    },
    "Koffein": {
        "description": "Specialty coffee kültürünü Belgrad'a taşıyan, kaliteli kahve ve rahat atmosferiyle öne çıkan kafe. Uzman baristalar, özenli kahve hazırlama ve rahat çalışma ortamı.",
        "description_en": "A cafe bringing specialty coffee culture to Belgrade, standing out with quality coffee and comfortable atmosphere. Expert baristas, careful coffee preparation and comfortable work environment."
    },
    "Red Bread": {
        "description": "El yapımı pasta, taze ekmek ve kahvaltı seçenekleriyle ünlü butik fırın-kafe. Ev yapımı lezzetler, sıcak ortam ve Belgrad'ın brunch kültürünün bir parçası.",
        "description_en": "A boutique bakery-cafe famous for handmade pastries, fresh bread and breakfast options. Homemade flavors, warm atmosphere and part of Belgrade's brunch culture."
    },
    "Mama Shelter Rooftop": {
        "description": "Mama Shelter otelinin çatı katında, şehir manzaralı kokteyl barı ve restoran. DJ setleri, yaratıcı kokteyller ve panoramik gün batımı deneyimi.",
        "description_en": "A rooftop cocktail bar and restaurant at Mama Shelter hotel with city views. DJ sets, creative cocktails and panoramic sunset experience."
    },
    "Guli": {
        "description": "Geleneksel Sırp mutfağının en iyi örneklerini sunan, onlarca yıldır hizmet veren klasik restoran. Ćevapi, pljeskavica ve ev yapımı rakiyla otantik Balkan deneyimi.",
        "description_en": "A classic restaurant serving the best examples of traditional Serbian cuisine, serving for decades. Authentic Balkan experience with ćevapi, pljeskavica and homemade rakia."
    },
    "Ljubic": {
        "description": "Şehrin en eski ve sevilen lokantalarından biri, ev yemekleri ve geleneksel Sırp lezzetleriyle. Sade ortam, uygun fiyat ve doyurucu porsiyonlar.",
        "description_en": "One of the city's oldest and most beloved restaurants with home cooking and traditional Serbian flavors. Simple setting, affordable prices and satisfying portions."
    },
    "Berliner": {
        "description": "Berlin sokak yemeklerinden ilham alan, döner ve currywurst sunan modern fast-food mekanı. Gece geç saatlere kadar açık, pratik ve lezzetli sokak lezzeti.",
        "description_en": "A modern fast-food venue inspired by Berlin street food, serving döner and currywurst. Open until late at night, practical and delicious street food."
    },
    "Moritz Eis": {
        "description": "Ev yapımı dondurma ve sorbeler sunan, taze malzemelerle hazırlanan butik dondurma dükkanı. Sıra dışı tatlar, doğal içerikler ve yaz günlerinin favorisi.",
        "description_en": "A boutique ice cream shop serving homemade ice cream and sorbets prepared with fresh ingredients. Unusual flavors, natural ingredients and summer favorite."
    },
    "KC Grad": {
        "description": "Eski fabrika binasında konumlanan, canlı müzik, sanat sergileri ve kültürel etkinliklere ev sahipliği yapan yaratıcı merkez. Alternatif sahne, indie atmosfer ve gece hayatı.",
        "description_en": "A creative center located in old factory building hosting live music, art exhibitions and cultural events. Alternative scene, indie atmosphere and nightlife."
    },
    "Restoran Tabor": {
        "description": "Skadarlija'nın en köklü restoranlarından biri, canlı müzik eşliğinde geleneksel Sırp yemekleri. Nostaljik atmosfer, tarihi mekan ve Balkan ziyafeti.",
        "description_en": "One of Skadarlija's most established restaurants, traditional Serbian dishes with live music. Nostalgic atmosphere, historic venue and Balkan feast."
    },
    "Zaokret": {
        "description": "Vejetaryen ve vegan lezzetler sunan, sağlıklı beslenme odaklı modern kafeterya. Taze malzemeler, organik seçenekler ve diyet dostu menü.",
        "description_en": "A modern cafeteria focused on healthy eating, serving vegetarian and vegan flavors. Fresh ingredients, organic options and diet-friendly menu."
    },
    "Kafana Sfrj": {
        "description": "Titova Yugoslavya döneminin nostaljisini yaşatan, sosyalist dekorasyon ve retro atmosferle dikkat çeken kafana. Geleneksel yemekler, rakı ve SFRJ anıları.",
        "description_en": "A kafana reviving nostalgia of Tito's Yugoslavia, notable for socialist decoration and retro atmosphere. Traditional dishes, rakia and SFRY memories."
    },
    "Restoran Lovac": {
        "description": "Av etleri ve Sırp kırsal mutfağı sunan, şehir dışına yakın konumuyla bilinen restoran. Domuz, geyik ve tavşan etleri, açık hava yemek alanları.",
        "description_en": "A restaurant known for game meats and Serbian rural cuisine, located near city outskirts. Boar, deer and rabbit meats, outdoor dining areas."
    },
    "Mezestoran Dvorište": {
        "description": "Eski bir evin avlusunda kurulan, Akdeniz mezelerini ve Balkan şaraplarını sunan atmosferik restoran. Romantik ortam, avlu yemekleri ve sürpriz lezzetler.",
        "description_en": "An atmospheric restaurant set up in courtyard of an old house, serving Mediterranean mezes and Balkan wines. Romantic setting, courtyard dining and surprise flavors."
    },
    "Viminacium": {
        "description": "Roma dönemi askeri kampı ve antik şehir kalıntıları, Belgrad'dan günübirlik gezi mesafesinde. Arkeolojik kazılar, mozaikler ve antik Roma yaşamına yolculuk.",
        "description_en": "Roman period military camp and ancient city remains, within day trip distance from Belgrade. Archaeological excavations, mosaics and journey to ancient Roman life."
    },
    "Golubac Fortress": {
        "description": "Tuna Nehri kıyısında dramatik manzarayla yükselen, restore edilmiş ortaçağ kalesi. 14. yüzyıl mimarisi, interaktif sergiler ve nehir manzarası.",
        "description_en": "A restored medieval fortress rising with dramatic views along Danube River. 14th century architecture, interactive exhibitions and river views."
    },
    "Djerdap National Park": {
        "description": "Avrupa'nın en büyük nehir boğazı olan Demir Kapılar'ı barındıran milli park. Tekne turları, yürüyüş rotaları ve muhteşem Tuna manzaraları.",
        "description_en": "A national park housing Iron Gates, Europe's largest river gorge. Boat tours, hiking trails and magnificent Danube views."
    },
    "Lepenski Vir": {
        "description": "Mezoilitik dönemden kalma, 9000 yıllık insan yerleşim izlerini taşıyan arkeolojik alan. Eşsiz heykel başları, müze ve tarih öncesi uygarlıklara bakış.",
        "description_en": "An archaeological site from Mesolithic period bearing traces of 9000-year-old human settlement. Unique sculpture heads, museum and glimpse into prehistoric civilizations."
    },
    "Fruska Gora Monasteries": {
        "description": "Fruška Gora dağlarında 16 manastırın yer aldığı, Sırp Ortodoks mirasının kutsal bölgesi. Freskler, ikonalar ve huzurlu dağ manzaraları.",
        "description_en": "A sacred region of Serbian Orthodox heritage with 16 monasteries in Fruška Gora mountains. Frescoes, icons and peaceful mountain views."
    },
    "Hyatt Regency Tea Room": {
        "description": "Lüks otelin zarif çay salonu, İngiliz tarzı afternoon tea servisi ve kaliteli pastalar sunan mekan. Sofistike atmosfer, özel anlar için ideal.",
        "description_en": "The elegant tea room of luxury hotel, a venue serving English-style afternoon tea and quality pastries. Sophisticated atmosphere, ideal for special moments."
    },
    "Boletus": {
        "description": "Avantgard Sırp mutfağını sunan, yeni nesil şeflerin yönettiği modern restoran. Yerel malzemeler, yaratıcı sunumlar ve Belgrad'ın gastronomi sahnesinin yükselen yıldızı.",
        "description_en": "A modern restaurant run by new generation chefs serving avant-garde Serbian cuisine. Local ingredients, creative presentations and Belgrade's rising star of gastronomy scene."
    },
    "Makadam": {
        "description": "Pizza, makarna ve İtalyan lezzetlerinin kaliteli versiyonlarını sunan popüler restoran. Rahat atmosfer, aileler için uygun ve güvenilir lezzet.",
        "description_en": "A popular restaurant serving quality versions of pizza, pasta and Italian flavors. Comfortable atmosphere, family-friendly and reliable taste."
    },
    "Comunale Caffe e Cucina": {
        "description": "İtalyan kahve ve yemek kültürünü Belgrad'a taşıyan şık kafe-restoran. Espresso, bruschetta ve aperitivo saati ile Akdeniz esintisi.",
        "description_en": "A stylish cafe-restaurant bringing Italian coffee and food culture to Belgrade. Mediterranean breeze with espresso, bruschetta and aperitivo hour."
    },
    "Sakura": {
        "description": "Japon mutfağı sunan, sushi ve ramen çeşitleriyle tanınan Asya restoranı. Modern sunum, taze malzemeler ve Uzak Doğu lezzetleri.",
        "description_en": "An Asian restaurant serving Japanese cuisine, known for sushi and ramen varieties. Modern presentation, fresh ingredients and Far East flavors."
    },
    "Museum of Applied Art": {
        "description": "Mobilya, seramik, tekstil ve endüstriyel tasarım eserlerini sergileyen uygulamalı sanatlar müzesi. Zanaat tarihi, tasarım evrimi ve estetik keşif.",
        "description_en": "A museum of applied arts exhibiting furniture, ceramics, textiles and industrial design works. Craft history, design evolution and aesthetic discovery."
    },
    "Hyde Park": {
        "description": "Vračar semtinde küçük ama güzel kentsel park, ağaçlık alan ve bank sıralarıyla dinlenme molası için ideal. Londra'nın ünlü parkından ilham alan isim.",
        "description_en": "A small but beautiful urban park in Vračar district, ideal for rest break with wooded area and bench rows. Name inspired by London's famous park."
    },
    "Usce Park": {
        "description": "Sava ve Tuna nehirlerinin birleştiği noktada büyük kentsel park ve rekreasyon alanı. Açık hava konserleri, spor alanları ve nehir kenarı piknik.",
        "description_en": "A large urban park and recreation area at the confluence of Sava and Danube rivers. Open-air concerts, sports areas and riverside picnicking."
    },
    "Museum of Science and Technology": {
        "description": "Bilim ve teknoloji tarihini interaktif sergilerle anlatan, çocuklar ve meraklılar için eğlenceli müze. Dokunarak öğrenme, deneyler ve keşif.",
        "description_en": "A fun museum telling science and technology history with interactive exhibitions for children and enthusiasts. Hands-on learning, experiments and discovery."
    },
    "Pedagogical Museum": {
        "description": "Sırp eğitim tarihini, eski okul materyallerini ve ders araçlarını sergileyen niş müze. Nostaljik sınıflar, antik kitaplar ve eğitim evrimi.",
        "description_en": "A niche museum exhibiting Serbian education history, old school materials and teaching tools. Nostalgic classrooms, antique books and education evolution."
    },
    "Kula Sibinjanin Janka": {
        "description": "Zemun'un en yüksek noktasında bulunan ortaçağ kulesi, şehir ve nehir manzarası sunan gözlem noktası. Tarihi yapı, panoramik görünüm ve fotoğraf için ideal.",
        "description_en": "A medieval tower at Zemun's highest point, an observation point offering city and river views. Historic structure, panoramic view and ideal for photography."
    },
    "Lido Beach": {
        "description": "Tuna üzerindeki Ada Ciganlija'ya alternatif, Zemun yakınındaki nehir plajı. Kumsal, güneşlenme alanları ve nehir yüzme deneyimi.",
        "description_en": "A river beach near Zemun, alternative to Ada Ciganlija on Danube. Sandy beach, sunbathing areas and river swimming experience."
    },
    "Znak Pitanja": {
        "description": "Belgrad'ın en eski restoranlarından biri, 19. yüzyıldan beri hizmet veren tarihi mekan. Soru işareti anlamına gelen ismi, camideki hiyeroglifi yansıtıyor.",
        "description_en": "One of Belgrade's oldest restaurants, a historic venue serving since 19th century. Its name meaning 'question mark' reflects the hieroglyph in the mosque."
    },
    "Restoran Reka": {
        "description": "Sava Nehri üzerindeki teknede konumlanan, taze balık ve nehir manzarası sunan yüzer restoran. Romantik akşam yemekleri, su üzerinde ziyafet.",
        "description_en": "A floating restaurant located on a boat on Sava River, serving fresh fish and river views. Romantic dinners, feast on the water."
    },
    "Saran": {
        "description": "Nehir kenarında taze balık ve Sırp deniz ürünleri lezzetleri sunan köklü restoran. Saz balığı, sazan ve geleneksel pişirme yöntemleriyle Belgrad mutfağı.",
        "description_en": "A well-established restaurant by the river serving fresh fish and Serbian seafood flavors. Belgrade cuisine with catfish, carp and traditional cooking methods."
    }
}

filepath = 'assets/cities/belgrad.json'
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

print(f"\n✅ Manually enriched {count} items (Belgrad Batch 2).")
