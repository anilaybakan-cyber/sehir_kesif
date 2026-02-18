import json

# Manual enrichment data (San Sebastian Batch 1: 40 items)
updates = {
    "Hondarribia": {
        "description": "Rengarenk balkonları, orta çağ surları ve Michelin yıldızlı restoranlarıyla ünlü, Fransa sınırındaki masalsı Bask kasabası. Balıkçı limanı, tarihi kale ve manzaralı teraslarıyla günübirlik kaçamak için mükemmel.",
        "description_en": "A fairytale Basque town near the French border, famous for colorful balconies, medieval walls, and Michelin-starred restaurants. Perfect for a day getaway with fishing harbor, historic castle, and scenic terraces."
    },
    "Pasai Donibane": {
        "description": "Ünlü yazar Victor Hugo'nun hayran kaldığı, tek bir sokaktan oluşan pitoresk balıkçı köyü. Renkli evleri, deniz ürünleri restoranları ve otantik Bask atmosferiyle, şehirden romantik bir kaçış.",
        "description_en": "A picturesque fishing village of a single street that famous writer Victor Hugo admired. A romantic escape from the city with colorful houses, seafood restaurants, and authentic Basque atmosphere."
    },
    "Getaria": {
        "description": "Ünlü tasarımcı Balenciaga'nın doğduğu, ızgara balık ve txakoli şarabıyla ünlü sahil kasabası. Balenciaga Müzesi, Santa Maria kilisesi ve gurme lezzetlerle moda ve gastronomi tutkunlarının durağı.",
        "description_en": "A coastal town where famous designer Balenciaga was born, famous for grilled fish and txakoli wine. A stop for fashion and gastronomy enthusiasts with Balenciaga Museum, Santa Maria church, and gourmet flavors."
    },
    "Zarautz": {
        "description": "Bask Bölgesi'nin en uzun plajı, 2.5 km kumsalı ve canlı sörf kültürüyle ünlü sahil kasabası. Sörf okulları, plaj barları ve yaz festivalleriyle, aktif tatil arayanların favorisi.",
        "description_en": "A coastal town famous for Basque Country's longest beach, 2.5 km of sand, and vibrant surf culture. A favorite for those seeking active vacation with surf schools, beach bars, and summer festivals."
    },
    "Borda Berri": {
        "description": "İdiyazabal peynirli risotto ve dana yanağı gibi modern yorumlu pintxoslarıyla ödül kazanmış küçük bar. Dar mekanına rağmen büyük lezzetler, rezervasyon önerilir.",
        "description_en": "A small bar awarded for modern-twist pintxos like Idiazabal cheese risotto and beef cheek. Great flavors despite small space, reservation recommended."
    },
    "La Cuchara de San Telmo": {
        "description": "Tezgahta hazır ürün yok, her şey anında sipariş üzerine pişiriliyor. Yumurtalı ıspanak ve mantar, pul biberi soslu kuzu böbreği gibi sıcak pintxoslarla, tadım turlarının vazgeçilmezi.",
        "description_en": "No ready products on counter, everything cooked fresh to order. An essential stop for tasting tours with hot pintxos like spinach with egg and mushroom, lamb kidney in paprika sauce."
    },
    "Goiz Argi": {
        "description": "Meşhur 'brocheta de gambas' (karides şiş) ve kalamar dolmasıyla ünlü, yarım yüzyıldır hizmet veren klasik pintxos barı. Sade sunum, harika lezzetler ve efsanevi karides şişi.",
        "description_en": "A classic pintxos bar serving for half a century, famous for legendary 'brocheta de gambas' (shrimp skewer) and stuffed squid. Simple presentation, great flavors, and legendary shrimp skewer."
    },
    "Bar Zeruko": {
        "description": "Modern Bask mutfağının avangard pintxoslarını sunan, yaratıcı sunumları ve deneysel lezzetleriyle ünlü bar. Görsel şölen, moleküler teknikler ve sıra dışı kombinasyonlarla, yenilikçi mutfak deneyimi.",
        "description_en": "A bar serving avant-garde pintxos of modern Basque cuisine, famous for creative presentations and experimental flavors. An innovative culinary experience with visual feast, molecular techniques, and unusual combinations."
    },
    "Paseo Nuevo": {
        "description": "Monte Urgull'un çevresini dolaşan, dramatik okyanus manzaraları sunan sahil şeridi yürüyüş yolu. Dalgaların kayalara vurduğu bu romantik rota, gün batımı için mükemmel.",
        "description_en": "A coastal promenade circling Monte Urgull, offering dramatic ocean views. This romantic route where waves crash against rocks is perfect for sunset."
    },
    "Mercado de la Bretxa": {
        "description": "Şehrin en iyi şeflerinin taze malzeme tedarik ettiği, 1870'lerden kalma tarihi pazar. Deniz ürünleri, et, peynir ve sebze tezgahlarıyla, Bask gastronomisinin kalbi.",
        "description_en": "A historic market dating from 1870s where the city's best chefs source fresh ingredients. The heart of Basque gastronomy with seafood, meat, cheese, and vegetable stalls."
    },
    "Eureka! Zientzia Museoa": {
        "description": "Çocuklar ve meraklılar için bilim ve teknolojiyi interaktif sergilerle eğlenceli hale getiren müze. Dokunarak öğrenme, planetaryum ve bilim deneyleriyle, aileler için mükemmel aktivite.",
        "description_en": "A museum making science and technology fun with interactive exhibitions for children and enthusiasts. Perfect activity for families with hands-on learning, planetarium, and science experiments."
    },
    "Monte Ulia": {
        "description": "Turistik Monte Igueldo'ya alternatif, yerel halkın tercih ettiği doğa parkuru ve manzara noktası. Orman yürüyüşleri, kıyı patikları ve sakin atmosferiyle, kalabalıktan uzak doğa kaçışı.",
        "description_en": "A nature trail and viewpoint preferred by locals, alternative to touristy Monte Igueldo. A nature escape away from crowds with forest walks, coastal paths, and calm atmosphere."
    },
    "Kursaal Bridge": {
        "description": "Urumea Nehri'nin okyanusla buluştuğu noktada, Kursaal Kongre Merkezi'ne açılan ikonik köprü. Şehrin modern mimarisi ve nehir manzarasıyla, akşam yürüyüşleri için ideal.",
        "description_en": "An iconic bridge at the point where Urumea River meets the ocean, opening to Kursaal Congress Center. Ideal for evening walks with the city's modern architecture and river views."
    },
    "Cider House Experience": {
        "description": "Geleneksel 'sidreria' deneyimi: dev fıçılardan akan elmeli sirkeyi (cider) yakalarken doğrudan fıçıdan içme ritüeli. Geleneksel menü, sınırsız cider ve Bask kültürüne dalış.",
        "description_en": "Traditional 'sidrería' experience: the ritual of catching apple cider flowing from giant barrels and drinking directly from the barrel. Traditional menu, unlimited cider, and dive into Basque culture."
    },
    "Cristina Enea Park": {
        "description": "Şehrin merkezinde tavuskuşlarının dolaştığı, İngiliz tarzı romantik park. Botanik zenginliği, huzurlu göletleri ve gölgeli yürüyüş yollarıyla, şehir içi doğa molası.",
        "description_en": "A romantic English-style park in the city center where peacocks roam. An urban nature break with botanical richness, peaceful ponds, and shaded walking paths."
    },
    "A Fuego Negro": {
        "description": "Michelin rehberine giren, avangard sunumları ve yaratıcı kombinasyonlarıyla sınırları zorlayan pintxos barı. Duman efektleri, beklenmedik tatlar ve sanatsal tabak sunumlarıyla, gastronomi macerası.",
        "description_en": "A pintxos bar pushing boundaries with avant-garde presentations and creative combinations, listed in Michelin guide. A gastronomic adventure with smoke effects, unexpected tastes, and artistic plating."
    },
    "Tamboril": {
        "description": "Plaza de la Constitución'da konumlanan, mantarlı yumurta ve jamón ibérico gibi klasik pintxoslarıyla sevilen bar. Meydanın balkon manzarasında pintxos keyfi için mükemmel.",
        "description_en": "A bar loved for classic pintxos like mushroom egg and jamón ibérico, located in Plaza de la Constitución. Perfect for enjoying pintxos with the square's balcony views."
    },
    "Bar Martinez": {
        "description": "1942'den beri hizmet veren, soğuk pintxos geleneğini sürdüren klasik bar. Tortilla, anchovy ve jamon tostadası gibi geleneksel lezzetlerle, nostaljik Bask bar deneyimi.",
        "description_en": "A classic bar serving since 1942, continuing the cold pintxos tradition. A nostalgic Basque bar experience with traditional flavors like tortilla, anchovy, and jamón toast."
    },
    "Good Shepherd Cathedral": {
        "description": "San Sebastián'ın en büyük dini yapısı, 75 metre yüksekliğindeki kuleleri ve Neo-Gotik mimarisiyle şehrin simgesi. Etkileyici iç mekanı, vitrayları ve organ konserleriyle görülmeye değer.",
        "description_en": "San Sebastián's largest religious structure, a city symbol with 75-meter towers and Neo-Gothic architecture. Worth seeing with impressive interior, stained glass, and organ concerts."
    },
    "City Hall": {
        "description": "Eskiden kumarhane olarak inşa edilen, Belle Époque döneminin zarif mimarisini yansıtan belediye binası. Deniz kenarındaki konumu, bahçeleri ve tarihi önemiyle, fotoğraf için ideal.",
        "description_en": "A city hall built originally as a casino, reflecting the elegant architecture of Belle Époque era. Ideal for photography with its seaside location, gardens, and historic importance."
    },
    "San Martin Market": {
        "description": "Geleneksel pazarın modern versiyonu: taze ürünler, gurme dükkanlar ve yeme-içme alanlarının bir arada bulunduğu gastronomi merkezi. Pintxos turlarının başlangıç noktası.",
        "description_en": "Modern version of traditional market: a gastronomy center combining fresh products, gourmet shops, and dining areas. Starting point for pintxos tours."
    },
    "Gipuzkoa Plaza": {
        "description": "Kuğulu göleti, saat kulesi ve tarihi binalarla çevrili, şehrin en romantik meydanlarından. Bahçeleri, bank sıraları ve huzurlu atmosferiyle, dinlenme molası için ideal.",
        "description_en": "One of the city's most romantic squares, surrounded by swan pond, clock tower, and historic buildings. Ideal for rest break with gardens, bench rows, and peaceful atmosphere."
    },
    "La Perla Thalasso": {
        "description": "Belle Époque döneminden kalma tarihi binasında deniz suyu tedavileri ve wellness hizmetleri sunan lüks spa. La Concha plajı manzarası, jacuzzi ve sauna ile tam rahatlama.",
        "description_en": "A luxury spa offering seawater treatments and wellness services in its Belle Époque-era historic building. Complete relaxation with La Concha beach views, jacuzzi, and sauna."
    },
    "Atari": {
        "description": "Santa Maria kilisesinin merdivenlerinde konumlanan, gençlerin tercih ettiği şık bar. Yaratıcı kokteyller, DJ setleri ve tarihi atmosferin modern yorumuyla, gece hayatının başlangıç noktası.",
        "description_en": "A stylish bar located on Santa Maria church stairs, preferred by young crowd. Starting point for nightlife with creative cocktails, DJ sets, and modern interpretation of historic atmosphere."
    },
    "Sirimiri": {
        "description": "Gençlerin tercih ettiği, harika kokteylleri ve canlı müzik geceleriyle ünlü popüler bar. Samimi atmosfer, dans alanı ve gece geç saatlere kadar eğlence.",
        "description_en": "A popular bar with great cocktails and live music nights, preferred by young people. Intimate atmosphere, dance floor, and entertainment until late at night."
    },
    "The Loaf": {
        "description": "Zurriola plajına bakan, ekşi mayalı ekmek sandviçleri ve specialty coffee sunan modern kafe. Sörfçüler ve dijital göçebeler tarafından sevilen, rahat çalışma ortamı.",
        "description_en": "A modern cafe overlooking Zurriola beach, serving sourdough bread sandwiches and specialty coffee. A comfortable work environment loved by surfers and digital nomads."
    },
    "Bodega Donostiarra": {
        "description": "Gros mahallesinin klasiği, ızgara etler ve geleneksel pintxoslarla ünlü otantik bar-restoran. Yerel halkın gittiği, turistik olmayan gerçek Bask deneyimi.",
        "description_en": "A Gros neighborhood classic, an authentic bar-restaurant famous for grilled meats and traditional pintxos. A real Basque experience where locals go, non-touristy."
    },
    "Ni Neu": {
        "description": "Kursaal binasının içinde konumlanan, deniz manzaralı modern Bask mutfağı restoranı. Yaratıcı menü, şık atmosfer ve muhteşem manzarayla, özel akşamlar için ideal.",
        "description_en": "A modern Basque cuisine restaurant located inside Kursaal building with sea views. Ideal for special evenings with creative menu, stylish atmosphere, and magnificent views."
    },
    "Ramuntxo Berri": {
        "description": "Gros mahallesinin en iyi pintxos barlarından biri, foie gras pintxosu ve jamón ile ünlü. Bar tezgahı önünde yerel halkla omuz omuza pintxos keyfi.",
        "description_en": "One of Gros neighborhood's best pintxos bars, famous for foie gras pintxos and jamón. Pintxos enjoyment shoulder to shoulder with locals at the bar counter."
    },
    "Zabaleta": {
        "description": "Şehrin en iyi tortillalarından birini sunan, sade ama mükemmel pintxos barı. Kremamsı iç, karamelize dış tortillası ile, yumurta severlerin başvuru noktası.",
        "description_en": "A simple but perfect pintxos bar serving one of the city's best tortillas. The reference point for egg lovers with creamy interior and caramelized exterior tortilla."
    },
    "Bergara Bar": {
        "description": "Birçok ödül kazanmış pintxoslarıyla, şehrin en tanınmış barlarından biri. Gamba al ajillo ve jamón kroket gibi klasiklerin yanı sıra yaratıcı lezzetler de sunuyor.",
        "description_en": "One of the city's most recognized bars with award-winning pintxos. Offers creative flavors alongside classics like gamba al ajillo and jamón croquette."
    },
    "Zurriola Surf School": {
        "description": "Zurriola plajında sörf öğrenmek isteyenler için profesyonel eğitim ve ekipman kiralama. Her seviyeye uygun dersler, gruplar veya özel seanslarla, dalgalara atılın.",
        "description_en": "Professional training and equipment rental for those wanting to learn surfing at Zurriola beach. Jump into the waves with lessons suitable for all levels, groups, or private sessions."
    },
    "Ametzagaña Park": {
        "description": "Eski bir kalenin kalıntılarını barındıran, şehrin arka planındaki gizli doğa alanı. Yürüyüş rotaları, tarihi kalıntılar ve panoramik manzaralarla, kalabalıktan uzak keşif.",
        "description_en": "A hidden natural area in the city's background, containing remains of an old fortress. Discovery away from crowds with hiking trails, historic ruins, and panoramic views."
    },
    "Anoeta Stadium": {
        "description": "Real Sociedad futbol takımının modern ve yenilenmiş stadyumu. Maç günleri atmosferi, stadyum turları ve Bask futbol tutkusunu yakından hissetme fırsatı.",
        "description_en": "Real Sociedad football team's modern and renovated stadium. Match day atmosphere, stadium tours, and an opportunity to feel Basque football passion up close."
    },
    "Basque Culinary Center": {
        "description": "Dünyanın önde gelen gastronomi üniversitelerinden biri, Michelin yıldızlı şefler yetiştiren prestijli kurum. Açık dersler, atölyeler ve gastronomi etkinlikleriyle, yemek tutkunları için ilham kaynağı.",
        "description_en": "One of the world's leading gastronomy universities, a prestigious institution training Michelin-starred chefs. A source of inspiration for food enthusiasts with open classes, workshops, and gastronomy events."
    },
    "Miramon Park": {
        "description": "Teknoloji parkı ile iç içe geçmiş, yeşil alanlar, göletler ve yürüyüş yolları sunan modern rekreasyon bölgesi. Koşucular, bisikletliler ve aileler için aktif mola noktası.",
        "description_en": "A modern recreation area intertwined with technology park, offering green areas, ponds, and walking paths. An active rest point for runners, cyclists, and families."
    },
    "Albaola The Sea Factory of the Basques": {
        "description": "16. yüzyıl balina gemisi San Juan'ın birebir replikasının inşa edildiği canlı tersane müzesi. Bask denizcilik tarihini, gemi yapım tekniklerini ve maceraperest geçmişi keşfedin.",
        "description_en": "A living shipyard museum where a full-scale replica of 16th-century whaling ship San Juan is being built. Discover Basque maritime history, shipbuilding techniques, and adventurous past."
    },
    "Fuerte de San Marcos": {
        "description": "19. yüzyıldan kalma askeri kale, şehre ve okyanus manzarasına hakim konumuyla görülmeye değer. Tarihi surlar, savunma yapıları ve panoramik vistalarla, tarih ve manzara bir arada.",
        "description_en": "A 19th-century military fort, worth seeing with its position commanding views of city and ocean. History and scenery together with historic walls, defense structures, and panoramic vistas."
    },
    "Mater Museoa": {
        "description": "Geleneksel bir ton balığı gemisinin dönüştürüldüğü, Bask balıkçılık tarihini anlatan yüzen müze. Geminin iç mekanı, antik balıkçılık araçları ve denizcilik kültürüyle, benzersiz deneyim.",
        "description_en": "A floating museum converted from a traditional tuna fishing boat, telling Basque fishing history. A unique experience with the ship's interior, antique fishing tools, and maritime culture."
    },
    "Sagardoetxea Cider Museum": {
        "description": "Bask elma şarabı (cider) kültürünü, üretim sürecini ve tarihini interaktif sergilerle anlatan müze. Cider tadımı, elma bahçesi turu ve geleneksel sirke yapımı gösterisi.",
        "description_en": "A museum explaining Basque cider culture, production process, and history with interactive exhibitions. Cider tasting, apple orchard tour, and traditional cider-making demonstration."
    }
}

filepath = 'assets/cities/san_sebastian.json'
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

print(f"\n✅ Manually enriched {count} items (San Sebastian Batch 1).")
