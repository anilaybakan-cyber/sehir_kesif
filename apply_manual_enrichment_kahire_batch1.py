import json

# Manual enrichment data (Kahire Batch 1: 40 items)
updates = {
    "Pyramid of Menkaure": {
        "description": "Giza'nın üç büyük piramidinden en küçüğü, ancak taş işlemeciliği ve mimari detaylarıyla dikkat çekici. Granit kaplama kalıntıları, antik mühendisliğin incelikli örneği.",
        "description_en": "The smallest of Giza's three great pyramids, but notable for stonework and architectural details. Granite cladding remains, a subtle example of ancient engineering."
    },
    "Cairo Citadel": {
        "description": "12. yüzyılda Selahaddin Eyyubi tarafından inşa edilen Kahire'nin tarihi kalesi ve İslami yapılar kompleksi. Mehmet Ali Paşa Camii, müzeler ve panoramik şehir manzarası.",
        "description_en": "Cairo's historic citadel and Islamic structures complex built by Saladin in 12th century. Muhammad Ali Pasha Mosque, museums, and panoramic city views."
    },
    "Mosque-Madrassa of Sultan Hassan": {
        "description": "14. yüzyıldan kalma, Memlük mimarisinin en görkemli örneklerinden biri. Devasa boyutları, zarif süslemeleri ve akustik mükemmelliğiyle İslam dünyasının harikası.",
        "description_en": "One of the most magnificent examples of Mamluk architecture from 14th century. A wonder of the Islamic world with massive dimensions, elegant decorations, and acoustic perfection."
    },
    "Al-Rifa'i Mosque": {
        "description": "19. yüzyılda Sultan Hasan Camii'nin yanına inşa edilen, kraliyet ailesi mezarlarını barındıran anıtsal cami. Neo-Memlük mimarisi ve etkileyici iç tasarım.",
        "description_en": "A monumental mosque built beside Sultan Hassan Mosque in 19th century, housing royal family tombs. Neo-Mamluk architecture and impressive interior design."
    },
    "Coptic Museum": {
        "description": "Mısır'ın Hıristiyanlık tarihini ve Kıpti sanatını sergileyen dünyanın en kapsamlı koleksiyonu. Freskleri, el yazmaları ve dini eserlerle bin yıllık miras.",
        "description_en": "The world's most comprehensive collection exhibiting Egypt's Christian history and Coptic art. A thousand-year heritage with frescoes, manuscripts, and religious artifacts."
    },
    "Mosque of Ibn Tulun": {
        "description": "9. yüzyıldan kalma Kahire'nin en eski camii, orijinal Abbasi mimarisini koruyan nadir yapı. Sarmal minaresi, geniş avlusu ve sade zarafeti ile farklı.",
        "description_en": "Cairo's oldest mosque from 9th century, a rare structure preserving original Abbasid architecture. Distinctive with spiral minaret, vast courtyard, and simple elegance."
    },
    "Baron Empain Palace": {
        "description": "Belçikalı milyarder tarafından yaptırılan, Hint-Hinduist mimarisinden esinlenen egzotik saray. Kahire'nin en sıra dışı yapılarından, restore edilerek müzeye dönüştürülmüş.",
        "description_en": "An exotic palace built by Belgian millionaire, inspired by Hindu-Indian architecture. One of Cairo's most unusual structures, restored and converted into museum."
    },
    "Ben Ezra Synagogue": {
        "description": "Kıpti Kahire'de konumlanan tarihi sinagog, Mısır Yahudi mirasının önemli eseri. Eski Ahit'in antik parçalarının bulunduğu 'Genizah' keşfiyle ünlü.",
        "description_en": "A historic synagogue in Coptic Cairo, an important piece of Egyptian Jewish heritage. Famous for 'Genizah' discovery containing ancient Old Testament fragments."
    },
    "Al-Muizz Street": {
        "description": "Dünyada en çok tarihi İslami yapıyı barındıran açık hava müzesi sokak. Camiler, medreseler, han ve çeşmeleriyle, Fatımi Kahire'sinin canlı mirası.",
        "description_en": "An open-air museum street housing the most historic Islamic structures in the world. Living heritage of Fatimid Cairo with mosques, madrasas, khans, and fountains."
    },
    "Cave Church": {
        "description": "Mokattam Dağı'nın içine oyulmuş, 20.000 kişi kapasiteli dünyanın en büyük mağara kiliseselerinden biri. Kaya heykelleri, ayinler ve manevi atmosfer.",
        "description_en": "One of the world's largest cave churches carved into Mokattam Mountain, with 20,000 capacity. Rock carvings, services, and spiritual atmosphere."
    },
    "Nilometer": {
        "description": "Antik Mısır'dan kalma, Nil'in su seviyesini ölçmek için kullanılan binlerce yıllık yapı. Osmanlı döneminde restore edilmiş, pratik mühendislik harikası.",
        "description_en": "A thousands-year-old structure from ancient Egypt used to measure Nile water levels. Restored in Ottoman period, a practical engineering marvel."
    },
    "Felucca Ride": {
        "description": "Nil Nehri'nde geleneksel yelkenli tekneyle romantik gün batımı gezisi. Şehir siluetinin ışıklandığı akşamlarda, Kahire'nin en unutulmaz deneyimlerinden.",
        "description_en": "A romantic sunset trip on traditional sailboat on Nile River. One of Cairo's most unforgettable experiences as city silhouette lights up in evenings."
    },
    "Bab Zuweila": {
        "description": "Fatımi surlarının iki minareyle taçlandırılmış güney kapısı, şehrin en iyi korunmuş tarihsel kapısı. Merdiven tırmanarak panoramik manzara fırsatı.",
        "description_en": "The southern gate of Fatimid walls crowned with two minarets, the city's best-preserved historical gate. Opportunity for panoramic view by climbing stairs."
    },
    "Qalawun Complex": {
        "description": "13. yüzyıldan kalma, cami, medrese, hastane ve türbeyi bir arada barındıran Memlük mimari kompleksi. İslam mimarisinin şaheseri, göz kamaştırıcı detaylar.",
        "description_en": "A 13th-century Mamluk architectural complex housing mosque, madrasa, hospital, and mausoleum together. Masterpiece of Islamic architecture, dazzling details."
    },
    "Beit El-Suhaymi": {
        "description": "17. yüzyıldan kalma, geleneksel Osmanlı-Mısır evinin en güzel örneklerinden biri. Mashrabiya kafesler, avlu, çeşme ve otantik yaşam alanları.",
        "description_en": "One of the finest examples of traditional Ottoman-Egyptian house from 17th century. Mashrabiya lattice, courtyard, fountain, and authentic living spaces."
    },
    "Koshary Abou Tarek": {
        "description": "Mısır'ın ulusal yemeği koşeri'nin en ünlü adresi, yarım yüzyıldır hizmet veren efsane lokanta. Makarna, pirinç, mercimek ve domates sosuyla doyurucu lezzet.",
        "description_en": "The most famous address for Egypt's national dish koshari, a legendary restaurant serving for half a century. Satisfying flavor with pasta, rice, lentils, and tomato sauce."
    },
    "Groppi": {
        "description": "1920'lerden kalma art deco tarzı pastane ve kafe, Kahire'nin nostaljik Belle Époque atmosferini yansıtıyor. Çikolata, pasta ve kahve ile tarihi mola.",
        "description_en": "An art deco pastry shop and cafe from 1920s reflecting Cairo's nostalgic Belle Époque atmosphere. Historic break with chocolate, pastries, and coffee."
    },
    "Bab al-Futuh": {
        "description": "Fatımi surlarının kuzey kapısı, 11. yüzyıldan kalma askeri mimari şaheseri. Masif taş duvarlar, savunma kuleleri ve tarihi İslami şehir planlaması.",
        "description_en": "Northern gate of Fatimid walls, a military architectural masterpiece from 11th century. Massive stone walls, defense towers, and historic Islamic urban planning."
    },
    "Bab al-Nasr": {
        "description": "Fatımi surlarının 'Zafer Kapısı', ikiz kulelerle çevrili anıtsal giriş. Müstahkem yapısı ve tarihi önemiyle, ortaçağ Kahire'sinin kapısı.",
        "description_en": "The 'Victory Gate' of Fatimid walls, a monumental entrance flanked by twin towers. Gate of medieval Cairo with fortified structure and historical importance."
    },
    "Tahrir Square": {
        "description": "Modern Mısır tarihinin simgesi, 2011 Arap Baharı devriminin merkezi meydanı. Politik önemi, Mısır Müzesi komşuluğu ve şehir yaşamının nabzı.",
        "description_en": "Symbol of modern Egyptian history, central square of 2011 Arab Spring revolution. Political significance, Egyptian Museum neighbor, and pulse of city life."
    },
    "Valley Temple of Khafre": {
        "description": "Giza'daki Khafre Piramidi'ne bağlı cenaze tapınağı, mükemmel korunmuş granit yapısıyla. Sfenks'in hemen yanında, eski kraliyet ritüellerinin mekanı.",
        "description_en": "Funerary temple connected to Khafre Pyramid in Giza, with perfectly preserved granite structure. Right beside Sphinx, venue of ancient royal rituals."
    },
    "Sound and Light Show Giza": {
        "description": "Piramitler ve Sfenks'in ışık ve ses gösterisiyle canlandırıldığı gece programı. Eski Mısır tarihi, lazer projeksiyonlar ve dramatik anlatım.",
        "description_en": "Night program where Pyramids and Sphinx are brought to life with light and sound show. Ancient Egyptian history, laser projections, and dramatic narration."
    },
    "Panoramic View of the Pyramids": {
        "description": "Giza'daki çöl tepelerinden üç piramidi birden gören manzara noktası. Gün doğumu ve gün batımında muhteşem fotoğraf fırsatı, tur otobüslerinin durağı.",
        "description_en": "Viewpoint seeing all three pyramids from desert hills in Giza. Magnificent photo opportunity at sunrise and sunset, tour bus stop."
    },
    "Zamalek District": {
        "description": "Nil üzerindeki adada konumlanan, elçilikler, butikler ve kafelerle dolu kozmopolit mahalle. Kahire'nin en şık semti, ağaçlı caddeler ve Belle Époque mimarisi.",
        "description_en": "A cosmopolitan neighborhood on Nile island full of embassies, boutiques, and cafes. Cairo's most elegant district, tree-lined streets, and Belle Époque architecture."
    },
    "Church of St. George": {
        "description": "Kıpti Kahire'deki yuvarlak planlı tarihi kilise, aziz Yorgi'ye adanmış. Bizans dönemi temelleri, dini ikona koleksiyonu ve manevi atmosfer.",
        "description_en": "A round-plan historic church in Coptic Cairo dedicated to Saint George. Byzantine-era foundations, religious icon collection, and spiritual atmosphere."
    },
    "El Sawy Culturewheel": {
        "description": "Zamalek'te köprü altında kurulan alternatif kültür merkezi, konserler, sergiler ve atölyeler. Kahire'nin genç yaratıcı sahnesinin buluşma noktası.",
        "description_en": "An alternative culture center under a bridge in Zamalek with concerts, exhibitions, and workshops. Meeting point of Cairo's young creative scene."
    },
    "El Abd Patisserie": {
        "description": "Mısır tatlılarının en köklü adreslerinden biri, onlarca yıldır hizmet veren geleneksel pastane. Basbousa, kunafa ve baklava ile Arap tatlı kültürü.",
        "description_en": "One of the most established addresses for Egyptian sweets, traditional pastry shop serving for decades. Arab dessert culture with basbousa, kunafa, and baklava."
    },
    "Umm Kulthum Museum": {
        "description": "Arap müziğinin efsanevi sesine adanmış müze, kişisel eşyalar ve konser kayıtları. 'Doğu'nun Yıldızı'nın hayatı ve kültürel mirası.",
        "description_en": "A museum dedicated to the legendary voice of Arab music, personal belongings and concert recordings. Life and cultural legacy of 'The Star of the East'."
    },
    "Fustat Pottery Village": {
        "description": "Eski Mısır başkenti Fustat'ta konumlanan geleneksel seramik üretim merkezi. Çömlekçileri izleme, atölyeler ve el yapımı hediyelik eşyalar.",
        "description_en": "A traditional ceramic production center in old Egyptian capital Fustat. Watching potters, workshops, and handmade souvenirs."
    },
    "Darb 1718": {
        "description": "Tarihi binada konumlanan çağdaş sanat merkezi, sergiler, filmler ve kültürel etkinlikler. Kahire'nin alternatif sanat sahnesinin kalbi.",
        "description_en": "A contemporary art center in historic building with exhibitions, films, and cultural events. Heart of Cairo's alternative art scene."
    },
    "Qasr El Nil Bridge": {
        "description": "İkonik aslan heykeleriyle süslü, Nil Nehri'ni geçen tarihi köprü. Akşam yürüyüşleri, nehir manzarası ve Kahire'nin en romantik noktalarından.",
        "description_en": "A historic bridge crossing Nile River decorated with iconic lion statues. Evening walks, river views, and one of Cairo's most romantic spots."
    },
    "Talaat Harb Square": {
        "description": "Şehir merkezinde art deco binaları ve hareketli atmosferiyle dikkat çeken meydan. Mısır milliyetçi hareketinin öncüsünün heykeli ve alışveriş caddesi.",
        "description_en": "A square notable for art deco buildings and lively atmosphere in city center. Statue of pioneer of Egyptian nationalist movement and shopping street."
    },
    "Ataba Market": {
        "description": "Kahire'nin en kalabalık ve kaotik pazarlarından biri, her şeyin bulunduğu labirent. Elektronik, tekstil, gıda ve günlük ihtiyaçlar için deneyim.",
        "description_en": "One of Cairo's most crowded and chaotic markets, a labyrinth where everything is found. Experience for electronics, textiles, food, and daily needs."
    },
    "Eish & Malh": {
        "description": "Modern Mısır mutfağını geleneksel tariflerle yorumlayan trendy restoran. Yerel malzemeler, yaratıcı sunumlar ve çağdaş Kahire gastronomisi.",
        "description_en": "A trendy restaurant interpreting modern Egyptian cuisine with traditional recipes. Local ingredients, creative presentations, and contemporary Cairo gastronomy."
    },
    "Naguib Mahfouz Cafe": {
        "description": "Nobel ödüllü yazara adanan, Khan el-Khalili içindeki atmosferik kafe. Mısır kahvesi, shisha ve edebi sohbetler için nostaljik mekan.",
        "description_en": "An atmospheric cafe named after Nobel laureate writer, inside Khan el-Khalili. Nostalgic venue for Egyptian coffee, shisha, and literary conversations."
    },
    "Mashrabia Gallery": {
        "description": "Çağdaş Mısır ve Arap sanatını sergileyen öncü galeri. Genç sanatçılar, dönemsel sergiler ve Ortadoğu sanat sahnesine bakış.",
        "description_en": "A pioneering gallery exhibiting contemporary Egyptian and Arab art. Young artists, periodic exhibitions, and view into Middle Eastern art scene."
    },
    "Simonds Bakery": {
        "description": "Batı tarzı pastalar, taze ekmek ve kahvaltı seçenekleri sunan popüler fırın-kafe zinciri. Croissant, sandviç ve espresso ile modern mola.",
        "description_en": "A popular bakery-cafe chain serving Western-style pastries, fresh bread, and breakfast options. Modern break with croissant, sandwich, and espresso."
    },
    "Crimson Bar & Grill": {
        "description": "Nil kenarında konumlanan, sofistike atmosferi ve kokteylleriyle ünlü bar-restoran. Akşam yemekleri, panoramik nehir manzarası ve gece hayatı.",
        "description_en": "A bar-restaurant by the Nile famous for sophisticated atmosphere and cocktails. Dinners, panoramic river views, and nightlife."
    },
    "Diwan Bookstore": {
        "description": "Mısır'ın önde gelen kitapçı zinciri, Arapça ve İngilizce kitaplar ile kültürel ürünler. Rahat okuma köşeleri ve kahve ile birleşik deneyim.",
        "description_en": "Egypt's leading bookstore chain with Arabic and English books and cultural products. Comfortable reading corners and experience combined with coffee."
    },
    "Mokattam Corniche": {
        "description": "Mokattam Dağı'nın yamaçlarından Kahire'nin tüm manzarasını sunan yol ve manzara noktaları. Gün batımı izleme, şehir ışıkları ve açık hava keyfi.",
        "description_en": "Road and viewpoints offering panoramic Cairo views from slopes of Mokattam Mountain. Sunset watching, city lights, and outdoor enjoyment."
    }
}

filepath = 'assets/cities/kahire.json'
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

print(f"\n✅ Manually enriched {count} items (Kahire Batch 1).")
