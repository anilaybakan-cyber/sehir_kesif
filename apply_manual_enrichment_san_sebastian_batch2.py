import json

# Manual enrichment data (San Sebastian Batch 2: 40 items)
updates = {
    "Zarautz Beach": {
        "description": "Bask Bölgesi'nin en uzun kumsalı (2.5 km), sörf mecca'sı ve yaz festivalleri merkezi. Yılın her döneminde sörfçülerin akın ettiği dalgalar, sahil restoranları ve canlı plaj atmosferi.",
        "description_en": "Basque Country's longest beach (2.5 km), a surf mecca and summer festival center. Waves attracting surfers year-round, beachfront restaurants, and lively beach atmosphere."
    },
    "Photomuseum": {
        "description": "Fotoğraf sanatının tarihini ve çağdaş yorumlarını sergileyen, Zarautz'daki önemli görsel sanat müzesi. Dönemsel sergiler, atölyeler ve Bask fotoğrafçılığına bakış.",
        "description_en": "An important visual art museum in Zarautz exhibiting photography art history and contemporary interpretations. Periodic exhibitions, workshops, and a look at Basque photography."
    },
    "Cristobal Balenciaga Museum": {
        "description": "Efsanevi moda tasarımcısının doğum yeri Getaria'da, haute couture tarihini ve Balenciaga'nın şaheserlerini sergileyen dünya çapında ünlü müze. Moda tutkunları için hac yeri.",
        "description_en": "A world-renowned museum in designer's birthplace Getaria, exhibiting haute couture history and Balenciaga masterpieces. A pilgrimage site for fashion enthusiasts."
    },
    "Elkano": {
        "description": "Dünyanın en iyi balık restoranlarından biri, Getaria'da odun ızgarasında pişirilen dev turbot balığıyla efsane. Michelin yıldızlı lezzet, rezervasyon şart.",
        "description_en": "One of the world's best fish restaurants, legendary in Getaria for giant turbot grilled over wood. Michelin-starred flavor, reservation required."
    },
    "Kaia Kaipe": {
        "description": "Getaria limanında, balıkçı teknelerinin hemen önünde taze deniz ürünleri sunan panoramik restoran. Izgarada pişen balık, txakoli şarabı ve okyanus manzarası.",
        "description_en": "A panoramic restaurant in Getaria harbor serving fresh seafood right in front of fishing boats. Grilled fish, txakoli wine, and ocean views."
    },
    "Ermita de San Telmo": {
        "description": "Dalgaların üzerine inşa edilmiş gibi görünen, Zumaia'daki dramatik konumlu küçük şapel. Eduardo Chillida'nın Rüzgar Tarağı heykeline benzer atmosferle, muhteşem okyanus manzarası.",
        "description_en": "A small chapel in dramatic location in Zumaia, appearing to be built on waves. Magnificent ocean views with atmosphere similar to Eduardo Chillida's Wind Comb sculpture."
    },
    "Itzurun Beach": {
        "description": "Game of Thrones'un çekim mekanlarından biri, Flysch jeolojik oluşumlarıyla ünlü dramatik plaj. Milyonlarca yıllık kaya katmanları ve okyanus dalgalarıyla, doğanın mucizesi.",
        "description_en": "One of Game of Thrones filming locations, a dramatic beach famous for Flysch geological formations. A nature miracle with millions of years old rock layers and ocean waves."
    },
    "Algorri Interpretation Center": {
        "description": "Flysch'ın jeolojik tarihini ve Deba-Zumaia sahili boyunca oluşan kaya formasyonlarını anlatan bilim merkezi. Rehberli turlar, eğitici sergiler ve doğa yürüyüşleri.",
        "description_en": "A science center explaining Flysch's geological history and rock formations along Deba-Zumaia coast. Guided tours, educational exhibitions, and nature walks."
    },
    "Asador Bedua": {
        "description": "Yüzyıllık gelenekle odun ızgarasında et pişiren, Getaria yakınlarındaki efsanevi asador. Chuletón (dev biftek), sebze ızgara ve samimi köy atmosferi.",
        "description_en": "A legendary asador near Getaria grilling meat on wood fire with century-old tradition. Chuletón (giant steak), grilled vegetables, and intimate village atmosphere."
    },
    "Akelarre": {
        "description": "3 Michelin yıldızlı, şef Pedro Subijana'nın 50 yıldır lezzetler yarattığı efsanevi restoran. Bask mutfağının öncüleri arasında, okyanus manzaralı tadım menüleri.",
        "description_en": "A 3 Michelin-starred legendary restaurant where chef Pedro Subijana has created flavors for 50 years. Among pioneers of Basque cuisine, tasting menus with ocean views."
    },
    "Martin Berasategui": {
        "description": "Dünyada en çok Michelin yıldızına sahip şeflerden birinin imza restoranı, 3 Michelin yıldızlı gastronomi tapınağı. İnovasyonun zirvesi, yaratıcı Bask lezzetleri.",
        "description_en": "Signature restaurant of one of the world's most Michelin-starred chefs, a 3 Michelin-starred gastronomy temple. Peak of innovation, creative Basque flavors."
    },
    "Kokotxa": {
        "description": "Eski Şehir'in kalbinde, modern Bask mutfağının en iyi örneklerini sunan Michelin yıldızlı restoran. Pintxos barlarının ortasında fine-dining deneyimi.",
        "description_en": "A Michelin-starred restaurant in the heart of Old Town serving best examples of modern Basque cuisine. Fine-dining experience amid pintxos bars."
    },
    "Amelia by Paulo Airaudo": {
        "description": "Arjantin kökenli şefin Bask mutfağına yaratıcı dokunuşlar kattığı, 2 Michelin yıldızlı yenilikçi restoran. Küresel etkiler, yerel malzemeler ve sanatsal sunum.",
        "description_en": "A 2 Michelin-starred innovative restaurant where Argentine chef adds creative touches to Basque cuisine. Global influences, local ingredients, and artistic presentation."
    },
    "San Sebastian International Film Festival": {
        "description": "Her Eylül düzenlenen, dünyanın en prestijli film festivallerinden biri. Hollywood yıldızları, dünya prömiyerleri ve sinema tutkunlarının buluştuğu kültürel etkinlik.",
        "description_en": "One of the world's most prestigious film festivals held every September. A cultural event where Hollywood stars, world premieres, and cinema enthusiasts meet."
    },
    "Mercado de Navidad": {
        "description": "Aralık ayında kurulan geleneksel Noel pazarı, el yapımı hediyeler, sıcak içecekler ve bayram atmosferi. Işıl ışıl süslemeler ve yerel lezzetlerle kış sihri.",
        "description_en": "Traditional Christmas market set up in December with handmade gifts, hot drinks, and festive atmosphere. Winter magic with sparkling decorations and local flavors."
    },
    "La Perla Gym": {
        "description": "Tarihi La Perla binasındaki modern spor salonu, La Concha plajı manzarası eşliğinde fitness. Belle Époque estetiği ile çağdaş ekipmanların buluştuğu benzersiz mekan.",
        "description_en": "A modern gym in historic La Perla building, fitness with La Concha beach views. A unique venue where Belle Époque aesthetics meet contemporary equipment."
    },
    "Hegalak Sports Center": {
        "description": "Olimpik yüzme havuzu, spor salonları ve wellness hizmetleri sunan modern spor kompleksi. Yüzme, fitness ve sauna ile aktif tatil programı.",
        "description_en": "A modern sports complex offering Olympic swimming pool, gyms, and wellness services. Active vacation program with swimming, fitness, and sauna."
    },
    "Real Club de Tenis": {
        "description": "1902'den beri hizmet veren köklü tenis kulübü, kortlar ve sosyal tesislerle elit spor deneyimi. Misafir oyuncuları kabul eden, zarif atmosferi olan klüp.",
        "description_en": "An established tennis club serving since 1902, elite sports experience with courts and social facilities. A club accepting guest players with elegant atmosphere."
    },
    "Club de Golf Basozabal": {
        "description": "Şehre yakın konumuyla, yeşil tepeler ve dağ manzaraları arasında 18 delikli golf sahası. Profesyonel tesisler, restoran ve golf tutkunları için ideal adres.",
        "description_en": "An 18-hole golf course among green hills and mountain views, close to the city. Professional facilities, restaurant, and ideal address for golf enthusiasts."
    },
    "Hipodromo de San Sebastian": {
        "description": "1916'dan beri at yarışlarına ev sahipliği yapan tarihi hipodrom. Yaz aylarında yarış etkinlikleri, sosyal atmosfer ve Bask at sporları geleneği.",
        "description_en": "A historic hippodrome hosting horse races since 1916. Summer racing events, social atmosphere, and Basque equestrian sports tradition."
    },
    "Casino Kursaal": {
        "description": "İkonik Kursaal binasındaki modern kumarhane, rulet, blackjack ve slot makineleriyle eğlence. Akşam kıyafeti gerekli, sofistike gece yaşamı deneyimi.",
        "description_en": "A modern casino in the iconic Kursaal building, entertainment with roulette, blackjack, and slot machines. Evening dress required, sophisticated nightlife experience."
    },
    "Dabadaba": {
        "description": "Canlı müzik konserlerinden DJ setlerine kadar geniş programıyla şehrin alternatif kültür merkezi. Rock, elektronik ve indie müzik sahnesi.",
        "description_en": "The city's alternative culture center with wide program from live music concerts to DJ sets. Rock, electronic, and indie music scene."
    },
    "Bataplan Disco": {
        "description": "La Concha plajına bakan, yaz gecelerinin en popüler gece kulübü. Teras partileri, dans pistı ve okyanus manzarası eşliğinde eğlence.",
        "description_en": "The most popular nightclub of summer nights overlooking La Concha beach. Entertainment with terrace parties, dance floor, and ocean views."
    },
    "Gu San Sebastian": {
        "description": "Şık tasarımı ve premium müzik seçkisiyle tanınan elit gece kulübü. VIP bölümler, kaliteli kokteyller ve sofistike kalabalıkla zarif gece hayatı.",
        "description_en": "An elite nightclub known for stylish design and premium music selection. Elegant nightlife with VIP sections, quality cocktails, and sophisticated crowd."
    },
    "Museo del Whisky": {
        "description": "Dünyanın farklı bölgelerinden viski koleksiyonu ve tadım oturumları sunan butik müze-bar. Viski meraklıları için eğitici ve lezzetli bir deneyim.",
        "description_en": "A boutique museum-bar offering whisky collection and tasting sessions from different regions of the world. An educational and delicious experience for whisky enthusiasts."
    },
    "Altxerri Bar & Jazz": {
        "description": "Canlı caz konserlerine ev sahipliği yapan, şehrin en eski caz mekanlarından biri. Samimi atmosfer, kaliteli müzik ve gece geç saatlere kadar caz keyfi.",
        "description_en": "One of the city's oldest jazz venues hosting live jazz concerts. Intimate atmosphere, quality music, and jazz enjoyment until late at night."
    },
    "Etxekalte": {
        "description": "Yerel gastronomi, kültür ve sanat etkinliklerine ev sahipliği yapan topluluk merkezi. Yemek atölyeleri, konserler ve Bask kültürüne dalış fırsatı.",
        "description_en": "A community center hosting local gastronomy, culture, and art events. Food workshops, concerts, and opportunity to dive into Basque culture."
    },
    "Momo Donostia": {
        "description": "Modern kokteyl kültürünü Bask şehrine taşıyan, yaratıcı içecekleriyle ünlü kokteyl barı. Mixology ustaları, özel reçeteler ve şık atmosfer.",
        "description_en": "A cocktail bar famous for creative drinks, bringing modern cocktail culture to the Basque city. Mixology masters, special recipes, and stylish atmosphere."
    },
    "Narru": {
        "description": "Geleneksel Bask mutfağını modern sunumlarla yorumlayan şık restoran. Deniz ürünleri, yerel üretim ve mevsimlik menülerle gurme deneyim.",
        "description_en": "A stylish restaurant interpreting traditional Basque cuisine with modern presentations. Gourmet experience with seafood, local produce, and seasonal menus."
    },
    "Casa Urola": {
        "description": "Eski Şehir'de yerel malzemelerle hazırlanan geleneksel Bask yemekleri sunan sevilen restoran. Pirzola, balık ve mevsimlik sebzelerle otantik lezzetler.",
        "description_en": "A beloved restaurant in Old Town serving traditional Basque dishes prepared with local ingredients. Authentic flavors with chops, fish, and seasonal vegetables."
    },
    "Bar Desy": {
        "description": "Gros mahallesinin sevilen barı, samimi atmosferi ve kaliteli şarap seçkisiyle dikkat çekiyor. Yerel halkın buluşma noktası, sohbet ve içki için ideal.",
        "description_en": "A beloved bar in Gros neighborhood, notable for intimate atmosphere and quality wine selection. A local meeting point, ideal for conversation and drinks."
    },
    "Pub Drop": {
        "description": "Rock ve metal müzik seven kalabalığın buluştuğu alternatif bar. Canlı konserlere ev sahipliği yapan, samimi ve enerjik atmosfer.",
        "description_en": "An alternative bar where rock and metal music loving crowd gathers. Hosting live concerts, intimate and energetic atmosphere."
    },
    "Caledonian": {
        "description": "İskoç tarzı pub, geniş viski ve bira seçkisiyle rugby ve futbol maçlarının izlendiği spor barı. Britanik atmosfer ve canlı maç geceleri.",
        "description_en": "A Scottish-style pub, a sports bar where rugby and football matches are watched with wide whisky and beer selection. British atmosphere and live match nights."
    },
    "Rocher de la Vierge": {
        "description": "Biarritz'de denize uzanan kayalık üzerindeki ikonik Meryem heykeli ve manzara noktası. Dramatik okyanus manzarası, fotoğraf için ideal.",
        "description_en": "An iconic Virgin Mary statue and viewpoint on a rock extending into the sea in Biarritz. Dramatic ocean views, ideal for photography."
    },
    "Saint-Jean-de-Luz": {
        "description": "Fransa sınırının hemen ötesinde, Kral XIV. Louis'nin evlendiği tarihi Bask kasabası. Renkli limanı, güzel plajları ve gurme lezzetleriyle günlük gezi için ideal.",
        "description_en": "A historic Basque town just across the French border where King Louis XIV married. Ideal for day trip with colorful harbor, beautiful beaches, and gourmet flavors."
    },
    "Bayonne Cathedral": {
        "description": "Fransız Bask Bölgesi'nin en etkileyici Gotik katedrali, UNESCO Dünya Mirası listesinde. Vitrayları, kemerli yapısı ve dini tarihiyle görülmeye değer.",
        "description_en": "The most impressive Gothic cathedral of French Basque Country, on UNESCO World Heritage list. Worth seeing with stained glass, arched structure, and religious history."
    },
    "Oma Painted Forest": {
        "description": "Sanatçı Agustín Ibarrola'nın çam ağaçlarına boyala oluşturduğu renkli açık hava sanat eseri. Orman içinde yürüyüş yaparken değişen perspektiflerle büyüleyici deneyim.",
        "description_en": "A colorful open-air artwork created by artist Agustín Ibarrola by painting pine trees. An enchanting experience with changing perspectives while walking through the forest."
    },
    "Guernica Tree": {
        "description": "Bask özgürlüğünün sembolü tarihi meşe ağacı, Guernica'da. Baskların geleneksel olarak yeminlerini ettiği kutsal yer ve Bask kimliğinin kalbi.",
        "description_en": "The historic oak tree symbol of Basque freedom, in Guernica. A sacred place where Basques traditionally took oaths and the heart of Basque identity."
    },
    "Vitoria-Gasteiz Green Ring": {
        "description": "Avrupa'nın en çevreci şehirlerinden birini çevreleyen, parklarla bağlantılı yeşil kuşak. Bisiklet yolları, yürüyüş parkurları ve doğa koruma alanlarıyla ekolojik keşif.",
        "description_en": "A green belt connected by parks surrounding one of Europe's most eco-friendly cities. Ecological discovery with bike paths, walking trails, and nature reserves."
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

print(f"\n✅ Manually enriched {count} items (San Sebastian Batch 2).")
