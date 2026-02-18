import json

# Manual enrichment data (Lisbon - ALL 35 items)
updates = {
    "Belém Tower": {
        "description": "Portekiz'in Keşifler Çağı simgesi, UNESCO mirası kıyı kalesi. Manuelin mimarisi, Tagus Nehri manzarası ve tarihi zindanlar.",
        "description_en": "Portugal's Age of Discovery symbol, UNESCO heritage coastal fortress. Manueline architecture, Tagus River views, and historic dungeons."
    },
    "Castelo de S. Jorge": {
        "description": "Lizbon'a tepeden bakan tarihi Mağribi kalesi. Şehrin en iyi panoramik manzarası, yürüyüş surları ve tavus kuşları.",
        "description_en": "Historic Moorish castle overlooking Lisbon. Best panoramic views of the city, walking ramparts, and peacocks."
    },
    "Praça do Comércio": {
        "description": "Tagus Nehri kıyısında devasa meydan, Lizbon'un girişi. Sarı binalar, zafer takı (Rua Augusta Arch) ve tarihi kafeler.",
        "description_en": "Massive square on Tagus River bank, Lisbon's entrance. Yellow buildings, triumphal arch (Rua Augusta Arch), and historic cafes."
    },
    "Rossio Square": {
        "description": "Dalgalı taş döşemesiyle ünlü şehrin ana buluşma noktası. Çeşmeler, tiyatro binası ve tarihi atmosfer.",
        "description_en": "City's main meeting point famous for wavy cobblestones. Fountains, theater building, and historic atmosphere."
    },
    "Tram 28": {
        "description": "Alfama'nın dar yokuşlarını tırmanan ikonik sarı tramvay. Tarihi turistik rota, nostaljik deneyim ve fotoğrafçılık.",
        "description_en": "Iconic yellow tram climbing Alfama's narrow slopes. Historic tourist route, nostalgic experience, and photography."
    },
    "Santa Justa Lift": {
        "description": "Eiffel'in öğrencisi tarafından yapılan neogotik demir asansör. Baixa ile Bairro Alto'yu bağlar, çatı terası manzarası.",
        "description_en": "Neo-Gothic iron lift built by Eiffel's student. Connects Baixa and Bairro Alto, rooftop terrace view."
    },
    "MAAT Museum": {
        "description": "Sanat, Mimari ve Teknoloji Müzesi. Nehir kenarında fütüristik dalga şeklindeki bina, gün batımı terası ve sergiler.",
        "description_en": "Museum of Art, Architecture and Technology. Futuristic wave-shaped building by river, sunset terrace, and exhibitions."
    },
    "Miradouro de Santa Catarina": {
        "description": "Adamastor heykeliyle ünlü popüler gün batımı izleme noktası. Genç kalabalık, nehir manzarası ve sokak müziği.",
        "description_en": "Popular sunset viewing spot famous for Adamastor statue. Young crowd, river views, and street music."
    },
    "Miradouro das Portas do Sol": {
        "description": "Alfama'nın kırmızı çatılarına ve Tejo Nehri'ne bakan efsanevi balkon. Tramvay durağı, kafe ve mükemmel fotoğraf.",
        "description_en": "Legendary balcony overlooking Alfama's red roofs and Tagus River. Tram stop, cafe, and perfect photo."
    },
    "Pasteis de Belem": {
        "description": "1837'den beri orijinal Pastel de Nata'nın yapıldığı tarihi pastane. Gizli tarif, sıcak servis, tarçın ve pudra şekeri.",
        "description_en": "Historic pastry shop making original Pastel de Nata since 1837. Secret recipe, served warm, cinnamon, and powdered sugar."
    },
    "Manteigaria": {
        "description": "Sadece Pastel de Nata yapan modern klasik. Göz önünde üretim, sürekli sıcak çıkan çıtır tartlar ve çan sesi.",
        "description_en": "Modern classic making only Pastel de Nata. Production in plain sight, crispy tarts always served hot, and bell sound."
    },
    "A Ginjinha": {
        "description": "Geleneksel vişne likörü (Ginjinha) sunan tarihi büfe. Ayakta shot, tatlı vişne taneleri ve yapışkan zemin.",
        "description_en": "Historic kiosk serving traditional cherry liqueur (Ginjinha). Standing shot, sweet cherries, and sticky floor."
    },
    "Park Bar": {
        "description": "Otoparkın çatısında gizli teras bar. 25 Nisan Köprüsü manzarası, DJ performansları ve gün batımı kokteylleri.",
        "description_en": "Hidden terrace bar on parking garage roof. 25th of April Bridge views, DJ performances, and sunset cocktails."
    },
    "Calouste Gulbenkian Museum": {
        "description": "Dünya standartlarında sanat koleksiyonu ve muhteşem bahçeler. Mısır, İslam ve Avrupa sanatı. Huzurlu bir vaha.",
        "description_en": "World-class art collection and magnificent gardens. Egyptian, Islamic, and European art. A peaceful oasis."
    },
    "National Tile Museum": {
        "description": "Azulejo (çini) sanatının tarihini anlatan benzersiz müze. Eski manastır binası, altın şapel ve muazzam Lizbon panoraması panosu.",
        "description_en": "Unique museum telling history of Azulejo (tile) art. Old convent building, golden chapel, and massive Lisbon panorama panel."
    },
    "National Coach Museum": {
        "description": "Dünyanın en büyük kraliyet at arabası koleksiyonu. Altın varaklı, kadife döşemeli masalsı araçlar ve ihtişam.",
        "description_en": "World's largest royal coach collection. Fairy-tale vehicles with gold leaf, velvet upholstery, and splendor."
    },
    "Carmo Convent": {
        "description": "1755 depreminde yıkılan çatısız gotik kilise kalıntısı. Gökyüzü altında sütunlar, arkeoloji müzesi ve melankolik güzellik.",
        "description_en": "Roofless Gothic church ruins destroyed in 1755 earthquake. Columns under sky, archeology museum, and melancholic beauty."
    },
    "Lisbon Cathedral": {
        "description": "Şehrin en eski kilisesi (Sé de Lisboa), kale görünümünde. Depremlere direnmiş, hazine odası ve Romanesk mimari.",
        "description_en": "City's oldest church (Sé de Lisboa), fortress-like appearance. Withstood earthquakes, treasury room, and Romanesque architecture."
    },
    "Parque Eduardo VII": {
        "description": "Şehre tepeden bakan devasa park ve geometrik çalılar. Baixa ve nehre doğru inen muazzam perspektif.",
        "description_en": "Massive park overlooking city with geometric hedges. Enormous perspective descending towards Baixa and river."
    },
    "Embaixada": {
        "description": "19. yüzyıl Sarayı'nda konsept mağazalar ve restoranlar. Neo-Arap mimarisi, tasarım ürünleri ve lüks alışveriş.",
        "description_en": "Concept stores and restaurants in 19th-century Palace. Neo-Arab architecture, design products, and luxury shopping."
    },
    "Village Underground Lisboa": {
        "description": "Konteynerler ve eski otobüslerden oluşan yaratıcı ofis ve kafe alanı. Hipster ortamı, sokak sanatı ve etkinlikler.",
        "description_en": "Creative office and cafe space made of containers and old buses. Hipster vibe, street art, and events."
    },
    "Pensão Amor": {
        "description": "Eski bir genelevden dönüştürülmüş burlesk temalı bar. Kırmızı kadife, erotik sanat, kitapçı ve bohem gece hayatı.",
        "description_en": "Burlesque-themed bar converted from old brothel. Red velvet, erotic art, bookstore, and bohemian nightlife."
    },
    "Chapitô à Mesa": {
        "description": "Sirk okulunun restoranı, kalenin eteğinde. Panoramik nehir manzarası, rustik dekor ve yaratıcı Portekiz mutfağı.",
        "description_en": "Circus school's restaurant at foot of castle. Panoramic river views, rustic decor, and creative Portuguese cuisine."
    },
    "Fábrica Coffee Roasters": {
        "description": "Lizbon'un öncü 3. dalga kahvecisi. Kendi kavurdukları çekirdekler, endüstriyel dekor ve kahve tutkunları.",
        "description_en": "Lisbon's pioneer 3rd wave coffee shop. Roasting their own beans, industrial decor, and coffee lovers."
    },
    "Copenhagen Coffee Lab": {
        "description": "Danimarka kökenli minimalist fırın ve kahve zinciri. Hygge ortamı, Laptop dostu ve harika tarçınlı çörek.",
        "description_en": "Danish-origin minimalist bakery and coffee chain. Hygge atmosphere, laptop friendly, and great cinnamon bun."
    },
    "Dear Breakfast": {
        "description": "Bütün gün kahvaltı sunan şık ve popüler mekan. Yumurta çeşitleri, smoothie kaseleri ve beyaz mermer estetiği.",
        "description_en": "Stylish and popular venue serving all-day breakfast. Egg varieties, smoothie bowls, and white marble aesthetics."
    },
    "Tease": {
        "description": "Sıra dışı cupcake ve tatlılar sunan renkli kafe. Rock & roll dekoru, rahat koltuklar ve Bairro Alto yakınında mola.",
        "description_en": "Colorful cafe serving unusual cupcakes and desserts. Rock & roll decor, comfy armchairs, and break near Bairro Alto."
    },
    "Landeau Chocolate": {
        "description": "'Dünyanın en iyi çikolatalı keki' olduğu iddia edilen yer. Sadece kek ve içecek, LX Factory içinde şık durak.",
        "description_en": "Place claimed to have 'world's best chocolate cake'. Only cake and drinks, stylish stop inside LX Factory."
    },
    "O Trevo": {
        "description": "Anthony Bourdain'in ziyaret ettiği bifana (domuz sandviç) büfesi. Hızlı, ucuz, lezzetli ve yerel bira.",
        "description_en": "Bifana (pork sandwich) kiosk visited by Anthony Bourdain. Fast, cheap, delicious, and local beer."
    },
    "Casa da Índia": {
        "description": "Kaotik ve gürültülü geleneksel Portekiz tavernası (tasca). Izgara balık, piri piri tavuk ve ortak masalar.",
        "description_en": "Chaotic and noisy traditional Portuguese tavern (tasca). Grilled fish, piri piri chicken, and communal tables."
    },
    "Bonjardim": {
        "description": "Lizbon'un en iyi Piri Piri tavuğu ile ünlü restoran. 'Rei dos Frangos' (Tavukların Kralı), açık hava oturma alanı.",
        "description_en": "Restaurant famous for Lisbon's best Piri Piri chicken. 'Rei dos Frangos' (King of Chickens), outdoor seating."
    },
    "Pena Palace": {
        "description": "Sintra'da renkli, masalsı Romantik dönem sarayı. Dağ tepesinde sisler içinde, Disney şatolarına ilham kaynağı.",
        "description_en": "Colorful, fairy-tale Romantic era palace in Sintra. On mountain top amidst mists, inspiration for Disney castles."
    },
    "Quinta da Regaleira": {
        "description": "Sintra'daki gizemli malikane ve bahçeler. İnisiyasyon kuyusu, masonik semboller, mağaralar ve gotik kuleler.",
        "description_en": "Mysterious mansion and gardens in Sintra. Initiation well, Masonic symbols, caves, and Gothic towers."
    },
    "Cabo da Roca": {
        "description": "Kıta Avrupası'nın en batı ucu. 'Karanın bittiği ve denizin başladığı yer'. Fener, uçurumlar ve sert rüzgar.",
        "description_en": "Westernmost point of continental Europe. 'Where land ends and sea begins'. Lighthouse, cliffs, and strong wind."
    },
    "Cascais": {
        "description": "Lizbon'a yakın şık sahil kasabası. Plajlar, marina, dondurmacılar ve eski balıkçı köyü atmosferi.",
        "description_en": "Chic seaside town near Lisbon. Beaches, marina, ice cream shops, and old fishing village atmosphere."
    }
}

filepath = 'assets/cities/lizbon.json'
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

print(f"\n✅ Manually enriched {count} items (Lisbon - COMPLETE).")
