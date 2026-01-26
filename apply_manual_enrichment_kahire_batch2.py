import json

# Manual enrichment data (Kahire Batch 2: 40 items)
updates = {
    "Kazaz": {
        "description": "Otantik Mısır mutfağının yerel lezzetlerini sunan geleneksel restoran. Kebaplar, grîl etler ve Arap mezelerle, doyurucu öğle ve akşam yemekleri.",
        "description_en": "A traditional restaurant serving local flavors of authentic Egyptian cuisine. Satisfying lunches and dinners with kebabs, grilled meats, and Arab mezes."
    },
    "Gad": {
        "description": "Mısır'ın en popüler fast-food zinciri, koşeri, fuul ve taamiye ile ünlü. Hızlı servis, uygun fiyat ve geleneksel Mısır sokak yemekleri.",
        "description_en": "Egypt's most popular fast-food chain famous for koshari, fuul, and taamiye. Quick service, affordable price, and traditional Egyptian street food."
    },
    "Sufi Bookstore": {
        "description": "Kahire'nin en şık bağımsız kitapçılarından biri, İngilizce ve Arapça kitaplar. Kafe köşesi, sanat kitapları ve kültürel etkinlikler.",
        "description_en": "One of Cairo's most elegant independent bookstores with English and Arabic books. Cafe corner, art books, and cultural events."
    },
    "Beit Al-Harrawi": {
        "description": "18. yüzyıldan kalma restore edilmiş Osmanlı evi, sanat sergileri ve kültürel etkinliklere ev sahipliği yapıyor. Mashrabiya detayları, avlu ve tarihi atmosfer.",
        "description_en": "An 18th-century restored Ottoman house hosting art exhibitions and cultural events. Mashrabiya details, courtyard, and historic atmosphere."
    },
    "Townhouse Gallery": {
        "description": "Kahire'nin önde gelen çağdaş sanat mekanlarından biri, bağımsız sanatçıları destekleyen galeri. Avangard sergiler, performans sanatı ve atölyeler.",
        "description_en": "One of Cairo's leading contemporary art venues, a gallery supporting independent artists. Avant-garde exhibitions, performance art, and workshops."
    },
    "Room Art Space": {
        "description": "Alternatif sanat ve müzik etkinliklerine ev sahipliği yapan bağımsız kültür mekanı. Canlı müzik, sergi açılışları ve yaratıcı topluluk.",
        "description_en": "An independent cultural venue hosting alternative art and music events. Live music, exhibition openings, and creative community."
    },
    "Church of St. Barbara": {
        "description": "Kıpti Kahire'deki 5. yüzyıldan kalma tarihi kilise, azize Barbara'ya adanmış. Bizans ikonaları, ahşap oyma detayları ve dini miras.",
        "description_en": "A 5th-century historic church in Coptic Cairo dedicated to Saint Barbara. Byzantine icons, wood carving details, and religious heritage."
    },
    "Museum of Modern Egyptian Art": {
        "description": "20. yüzyıl Mısır sanatçılarının eserlerini sergileyen modern sanat müzesi. Heykel, resim ve Mısır sanat tarihine bakış.",
        "description_en": "A modern art museum exhibiting works of 20th-century Egyptian artists. Sculpture, painting, and view into Egyptian art history."
    },
    "Mahmoud Mokhtar Museum": {
        "description": "Modern Mısır heykelciliğinin öncüsü Mahmoud Mokhtar'ın eserlerini sergileyen müze. 'Mısır Uyanıyor' heykeli gibi ikonik eserler.",
        "description_en": "A museum exhibiting works of Mahmoud Mokhtar, pioneer of modern Egyptian sculpture. Iconic works like 'Egypt Awakening' statue."
    },
    "Talaat Harb Street": {
        "description": "Downtown Kahire'nin ana alışveriş ve yürüyüş caddesi, art deco binaları ve tarihi dükkanlarla. Nostaljik atmosfer, kafeler ve kitapçılar.",
        "description_en": "Downtown Cairo's main shopping and walking street with art deco buildings and historic shops. Nostalgic atmosphere, cafes, and bookstores."
    },
    "Mosque of Qijmas al-Ishaqi": {
        "description": "15. yüzyıldan kalma Memlük camii, zarif minaresi ve detaylı taş işçiliğiyle. El-Darb el-Ahmar mahallesinin tarihi cevheri.",
        "description_en": "A 15th-century Mamluk mosque with elegant minaret and detailed stonework. Historic gem of El-Darb el-Ahmar neighborhood."
    },
    "Al-Bursa El-Qadima": {
        "description": "Kahire'nin tarihi merkezi finansal bölgesi, eski mısır borsası ve art deco binalarla. Kent yenilemesi, trendy kafeler ve tarihi doku.",
        "description_en": "Cairo's historic central financial district with old Egyptian stock exchange and art deco buildings. Urban renewal, trendy cafes, and historic texture."
    },
    "Babel": {
        "description": "Ortadoğu ve Akdeniz mutfağını sunan şık restoran, meyveli nargile ve canlı atmosferiyle. Mezeler, griller ve romantik akşam yemekleri.",
        "description_en": "A stylish restaurant serving Middle Eastern and Mediterranean cuisine with fruity hookah and lively atmosphere. Mezes, grills, and romantic dinners."
    },
    "Le Pacha 1901": {
        "description": "Nil üzerinde demirli tarihi gemi-restoran, birden fazla yemek mekanı ve canlı eğlence. Fransız, Mısır ve uluslararası mutfak seçenekleri.",
        "description_en": "A historic ship-restaurant anchored on Nile with multiple dining venues and live entertainment. French, Egyptian, and international cuisine options."
    },
    "Sequoia (New/Alternative)": {
        "description": "Nil kenarında şık açık hava mekanı, kokteyller ve hafif yemekler sunan lounge. Gün batımı manzarası, DJ müziği ve sofistike atmosfer.",
        "description_en": "A stylish outdoor venue by Nile, lounge serving cocktails and light meals. Sunset views, DJ music, and sophisticated atmosphere."
    },
    "Wekalet el-Balah": {
        "description": "İkinci el giyim, vintage eşyalar ve kumaş pazarı. Pazarlık kültürü, sürpriz buluntular ve bütçe dostu alışveriş deneyimi.",
        "description_en": "Second-hand clothing, vintage items, and fabric market. Bargaining culture, surprise finds, and budget-friendly shopping experience."
    },
    "Ahbab El-Sayyeda": {
        "description": "Seyyide Zeynep Camii yakınında geleneksel Mısır yemekleri sunan halk lokantası. Hamam mahşi, fuul ve otantik mahalle lezzetleri.",
        "description_en": "A people's restaurant serving traditional Egyptian dishes near Sayyida Zeinab Mosque. Stuffed pigeon, fuul, and authentic neighborhood flavors."
    },
    "Sobhy Kaber": {
        "description": "Mısır kahvaltısının en iyi adreslerinden biri, fuul, falafel ve taze ekmek ile. Sabah kuyruğu, yerel deneyim ve uygun fiyat.",
        "description_en": "One of the best addresses for Egyptian breakfast with fuul, falafel, and fresh bread. Morning queue, local experience, and affordable price."
    },
    "Caveman Restaurant": {
        "description": "Mağara temalı dekorasyon ve büyük et porsiyonlarıyla dikkat çeken tematik restoran. Mangal etler, aileler için eğlence ve sıra dışı konsept.",
        "description_en": "A themed restaurant notable for cave-themed decoration and large meat portions. Grilled meats, family entertainment, and unusual concept."
    },
    "Gezira Art Center": {
        "description": "Zamalek'te konumlanan, Mısır ve uluslararası sanatçıların eserlerini sergileyen modern sanat merkezi. Dönemsel sergiler ve sanat eğitimi.",
        "description_en": "A modern art center in Zamalek exhibiting works of Egyptian and international artists. Periodic exhibitions and art education."
    },
    "9 Pyramids Lounge": {
        "description": "Piramitlerin manzarasına bakan, kokteyller ve hafif yemekler sunan çatı lounge'u. Muhteşem gün batımı, romantik atmosfer ve benzersiz konum.",
        "description_en": "A rooftop lounge overlooking pyramids serving cocktails and light meals. Magnificent sunset, romantic atmosphere, and unique location."
    },
    "Korba District": {
        "description": "Heliopolis'in tarihi kalbi, art deco binaları, vintage dükkanları ve nostaljik atmosferiyle. Belle Époque mimarisi, kafeler ve kültürel miras.",
        "description_en": "Historic heart of Heliopolis with art deco buildings, vintage shops, and nostalgic atmosphere. Belle Époque architecture, cafes, and cultural heritage."
    },
    "Abou El Sid": {
        "description": "Geleneksel Mısır mutfağını şık ortamda sunan ünlü restoran zinciri. Molokhia, koshary ve oryantal mezelerle, otantik gurme deneyimi.",
        "description_en": "A famous restaurant chain serving traditional Egyptian cuisine in elegant setting. Authentic gourmet experience with molokhia, koshary, and oriental mezes."
    },
    "October War Panorama": {
        "description": "1973 Arap-İsrail Savaşı'nı dramatik 360 derece panoramik tablolarla anlatan askeri müze. Mısır zafer anıtı, multimedya gösterileri.",
        "description_en": "A military museum telling the 1973 Arab-Israeli War with dramatic 360-degree panoramic paintings. Egyptian victory monument, multimedia shows."
    },
    "Wissa Wassef Art Center": {
        "description": "Dünyaca ünlü dokuma sanatı merkezi, çocukların el dokumalarıyla oluşturduğu tapestry koleksiyonu. El sanatları, galeri ve atölye ziyareti.",
        "description_en": "World-renowned weaving art center with tapestry collection created by children's hand-woven work. Handicrafts, gallery, and workshop visit."
    },
    "Marriott Mena House": {
        "description": "Piramitlerin eteğindeki efsanevi tarihi otel, 19. yüzyıldan beri misafirperverlik. Kraliyet atmosferi, havuz, bahçeler ve piramit manzarası.",
        "description_en": "Legendary historic hotel at foot of pyramids, hospitality since 19th century. Royal atmosphere, pool, gardens, and pyramid views."
    },
    "Cairo Festival City Mall": {
        "description": "Mısır'ın en büyük alışveriş merkezlerinden biri, uluslararası markalar ve eğlence seçenekleri. Sinema, restoranlar ve çeşme gösterileri.",
        "description_en": "One of Egypt's largest shopping malls with international brands and entertainment options. Cinema, restaurants, and fountain shows."
    },
    "Imam Shafi'i Mausoleum": {
        "description": "Dört büyük İslam hukuk ekolünden birinin kurucusu İmam Şafii'nin türbesi. Eyyubi dönemi mimarisi, dini ziyaret ve tarihi önem.",
        "description_en": "Mausoleum of Imam Shafi'i, founder of one of four major Islamic law schools. Ayyubid-period architecture, religious visit, and historic importance."
    },
    "Left Bank": {
        "description": "Zamalek'te Fransız tarzı kafe-restoran, kahvaltı ve brunch seçenekleriyle. Croissant, omlet ve kahve ile Avrupa esintisi.",
        "description_en": "A French-style cafe-restaurant in Zamalek with breakfast and brunch options. European breeze with croissant, omelet, and coffee."
    },
    "Cake Cafe": {
        "description": "El yapımı pasta ve tatlılarıyla ünlü butik kafe. Cheesecake, brownie ve specialty coffee ile tatlı mola.",
        "description_en": "A boutique cafe famous for handmade cakes and desserts. Sweet break with cheesecake, brownie, and specialty coffee."
    },
    "Road 9 Maadi": {
        "description": "Maadi'nin en popüler yeme-içme sokağı, dizi dizi restoran ve kafe seçenekleri. Uluslararası mutfaklar, bare ve gece hayatı.",
        "description_en": "Maadi's most popular dining street with row of restaurant and cafe options. International cuisines, bars, and nightlife."
    },
    "Arkan Plaza": {
        "description": "6 Ekim şehrinde modern açık hava alışveriş merkezi, markalar ve restoranlar. Yaşam tarzı mağazaları, kafeler ve aile aktiviteleri.",
        "description_en": "A modern open-air shopping center in 6th October city with brands and restaurants. Lifestyle stores, cafes, and family activities."
    },
    "Zed Park": {
        "description": "6 Ekim şehrinde büyük yeşil alan, spor tesisleri ve açık hava etkinlikleri. Yürüyüş yolları, piknik alanları ve aile eğlencesi.",
        "description_en": "A large green area in 6th October city with sports facilities and outdoor events. Walking paths, picnic areas, and family entertainment."
    },
    "Walk of Cairo": {
        "description": "New Cairo'da açık hava alışveriş ve yeme-içme kompleksi. Restoran terblası, kafeler ve akşam yürüyüşleri için ideal.",
        "description_en": "An open-air shopping and dining complex in New Cairo. Restaurant terraces, cafes, and ideal for evening walks."
    },
    "Mosque of Al-Salih Tala'i": {
        "description": "Bab Zuweila karşısındaki 12. yüzyıl Fatımi camii, yükseltilmiş platformuyla dikkat çekici. Tarihi mimari, antik çarşı kalıntıları.",
        "description_en": "A 12th-century Fatimid mosque opposite Bab Zuweila, notable for raised platform. Historic architecture, ancient market remains."
    },
    "Beshtak Palace": {
        "description": "14. yüzyıldan kalma Memlük sarayı, restore edilerek kültür merkezine dönüştürülmüş. El-Muizz Sokağı'nın görkemli yapısı, sergiler.",
        "description_en": "A 14th-century Mamluk palace restored and converted to cultural center. Magnificent structure of Al-Muizz Street, exhibitions."
    },
    "Textile Museum": {
        "description": "Mısır dokuma ve tekstil tarihini antik dönemden günümüze anlatan müze. Kıpti kumaşlar, İslami dokumalar ve moda tarihi.",
        "description_en": "A museum telling Egyptian weaving and textile history from ancient times to present. Coptic fabrics, Islamic weavings, and fashion history."
    },
    "Hammams of Cairo": {
        "description": "Tarihi Mısır hamamlarında geleneksel Osmanlı banyosu deneyimi. Sıcak buhar, masaj ve tarihî yapılarda wellness.",
        "description_en": "Traditional Ottoman bath experience in historic Egyptian hammams. Hot steam, massage, and wellness in historical buildings."
    },
    "Nile Maxim": {
        "description": "Nil üzerinde lüks yemekli gezi teknesi, canlı müzik ve oryantal dans gösterileri. Gourmet yemek, nehir manzarası ve gece eğlencesi.",
        "description_en": "A luxury dinner cruise boat on Nile with live music and oriental dance shows. Gourmet dining, river views, and night entertainment."
    },
    "Capital Business Park": {
        "description": "5. Yerleşim Bölgesi'nde modern iş ve alışveriş kompleksi. Kafe ve restoranlar, açık hava alanları ve iş-yaşam dengesi.",
        "description_en": "A modern business and shopping complex in 5th Settlement. Cafes and restaurants, outdoor areas, and work-life balance."
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

print(f"\n✅ Manually enriched {count} items (Kahire Batch 2).")
