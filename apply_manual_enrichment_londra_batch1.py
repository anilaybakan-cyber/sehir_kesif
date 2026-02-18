import json

# Manual enrichment data (London - ALL 26 items)
updates = {
    "Wallace Collection": {
        "description": "Tarihi bir malikanede sergilenen muazzam sanat koleksiyonu. 'Fragonard'ın Salıncağı' tablosu, zırhlar ve ücretsiz giriş.",
        "description_en": "Massive art collection displayed in a historic mansion. 'The Swing' by Fragonard, armors, and free admission."
    },
    "Saatchi Gallery": {
        "description": "Chelsea'de çağdaş sanatın kalbi, Charles Saatchi'nin galerisi. Tartışmalı sergiler, modern eserler ve şık kafe.",
        "description_en": "Heart of contemporary art in Chelsea, Charles Saatchi's gallery. Controversial exhibitions, modern works, and chic cafe."
    },
    "Design Museum": {
        "description": "Kensington'da modern tasarım ve mimari müzesi. Ürün tasarımı, moda sergileri ve minimalist mimari yapı.",
        "description_en": "Modern design and architecture museum in Kensington. Product design, fashion exhibitions, and minimalist architectural structure."
    },
    "Imperial War Museum": {
        "description": "Modern savaşların tarihini ve insan üzerindeki etkisini anlatan etkileyici müze. Holokost sergisi, tanklar ve uçaklar.",
        "description_en": "Impressive museum exploring history of modern war and its impact on people. Holocaust exhibition, tanks, and aircraft."
    },
    "Regent's Park": {
        "description": "Kraliyet parklarının en zarifi, gül bahçeleriyle ünlü. Açık hava tiyatrosu, göl ve Londra Hayvanat Bahçesi'ne ev sahipliği yapar.",
        "description_en": "Most elegant of Royal Parks, famous for rose gardens. Hosts open air theatre, lake, and London Zoo."
    },
    "Kyoto Garden": {
        "description": "Holland Park içinde saklı, huzur dolu Japon bahçesi. Şelale, koi balıkları, tavus kuşları ve zen atmosferi.",
        "description_en": "Peaceful Japanese garden hidden in Holland Park. Waterfall, koi fish, peacocks, and zen atmosphere."
    },
    "Eltham Palace": {
        "description": "Ortaçağ sarayı ile 1930'ların Art Deco tasarımının eşsiz birleşimi. Henry VIII'in çocukluk evi ve muhteşem hendek.",
        "description_en": "Unique blend of medieval palace and 1930s Art Deco design. Childhood home of Henry VIII and magnificent moat."
    },
    "Carnaby Street": {
        "description": "Londra'nın moda ve alışveriş sokağı, 'Swinging London'ın doğum yeri. Renkli süslemeler, butikler ve Kingly Court.",
        "description_en": "London's fashion and shopping street, birthplace of 'Swinging London'. Colorful decorations, boutiques, and Kingly Court."
    },
    "Fortnum & Mason": {
        "description": "Kraliyet onayı almış lüks departmanlı mağaza, 1707'den beri. Piknik sepetleri, çay salonu ve gurme lezzetler.",
        "description_en": "Luxury department store with Royal Warrant, since 1707. Picnic hampers, tea salon, and gourmet delights."
    },
    "Dishoom Covent Garden": {
        "description": "Bombay kafe kültürünü Londra'ya taşıyan efsanevi Hint restoranı. Bacon Naan Roll, siyah mercimek ve uzun kuyruklar.",
        "description_en": "Legendary Indian restaurant bringing Bombay cafe culture to London. Bacon Naan Roll, black daal, and long queues."
    },
    "Gloria": {
        "description": "Shoreditch'te 70'ler Capri havası estiren İtalyan trattoria. Dev limonlu tart, trüflü makarna ve abartılı dekor.",
        "description_en": "Italian trattoria in Shoreditch with 70s Capri vibe. Giant lemon tart, truffle pasta, and extravagant decor."
    },
    "Peggy Porschen": {
        "description": "Belgravia'nın pespembe, çiçeklerle süslü 'Instagramlık' pastanesi. Şık cupcakeler, çay saati ve peri masalı dekoru.",
        "description_en": "Belgravia's pink, floral 'Instagrammable' bakery. Chic cupcakes, tea time, and fairy tale decor."
    },
    "Cutty Sark": {
        "description": "Greenwich'te restore edilmiş tarihi çay klipperi gemisi. 19. yüzyıl denizcilik tarihi, güverte yürüyüşü ve müze.",
        "description_en": "Restored historic tea clipper ship in Greenwich. 19th-century maritime history, deck walk, and museum."
    },
    "Old Royal Naval College": {
        "description": "Barok mimarinin şaheseri, Painted Hall (Boyalı Salon) ile ünlü. Film seti olarak kullanılan görkemli sütunlar ve tavan.",
        "description_en": "Masterpiece of Baroque architecture, famous for Painted Hall. Magnificent columns and ceiling used as film set."
    },
    "Royal Albert Hall": {
        "description": "Kraliçe Victoria'nın eşi anısına açılan ikonik konser salonu. BBC Proms, kırmızı tuğla mimari ve dünya yıldızları.",
        "description_en": "Iconic concert hall opened in memory of Queen Victoria's husband. BBC Proms, red brick architecture, and world stars."
    },
    "Greenwich Market": {
        "description": "Kapalı pazar yeri, antikalar, el sanatları ve dünya mutfağı. Hafta sonu kalabalığı, sokak lezzetleri ve özgün hediyelikler.",
        "description_en": "Covered market with antiques, crafts, and world cuisine. Weekend crowds, street food, and unique gifts."
    },
    "Westminster Abbey": {
        "description": "Kraliyet taç giyme törenlerinin ve düğünlerinin yapıldığı gotik kilise. Newton ve Darwin'in mezarları, 1000 yıllık tarih.",
        "description_en": "Gothic church hosting royal coronations and weddings. Graves of Newton and Darwin, 1000 years of history."
    },
    "Covent Garden": {
        "description": "Sokak sanatçıları, lüks mağazalar ve Apple Market ile ünlü meydan. Opera binası, Neal's Yard ve canlı atmosfer.",
        "description_en": "Square famous for street performers, luxury shops, and Apple Market. Opera house, Neal's Yard, and lively atmosphere."
    },
    "Trafalgar Square": {
        "description": "Londra'nın kalbi, Nelson Sütunu ve aslan heykelleri. Ulusal Galeri önünde protesto, kutlama ve buluşma noktası.",
        "description_en": "Heart of London, Nelson's Column and lion statues. Protest, celebration, and meeting point in front of National Gallery."
    },
    "Piccadilly Circus": {
        "description": "Dev reklam ekranları ve Eros heykeli ile Londra'nın Times Meydanı. Tiyatrolar bölgesi (West End) giriş kapısı.",
        "description_en": "London's Times Square with giant advertising screens and Eros statue. Gateway to theatre district (West End)."
    },
    "St Paul's Cathedral": {
        "description": "Sir Christopher Wren'in başyapıtı, devasa kubbeli katedral. Fısıltı Galerisi, şehir manzarası ve Prenses Diana'nın düğün yeri.",
        "description_en": "Sir Christopher Wren's masterpiece, cathedral with massive dome. Whispering Gallery, city views, and Princess Diana's wedding venue."
    },
    "Kew Palace": {
        "description": "Kew Bahçeleri içindeki en küçük İngiliz kraliyet sarayı. Kral III. George'un evi, kırmızı tuğla ve samimi tarih.",
        "description_en": "Smallest British royal palace inside Kew Gardens. Family home of King George III, red brick, and intimate history."
    },
    "Science Museum": {
        "description": "Bilim ve teknoloji tarihini eğlenceli hale getiren müze. Apollo 10 kapsülü, buharlı makineler ve interaktif Wonderlab.",
        "description_en": "Museum making history of science and technology fun. Apollo 10 capsule, steam engines, and interactive Wonderlab."
    },
    "Churchill War Rooms": {
        "description": "İkinci Dünya Savaşı'nın yönetildiği gizli yeraltı sığınağı. Winston Churchill'in odası, harita odası ve savaş müzesi.",
        "description_en": "Secret underground bunker where WWII was directed. Winston Churchill's room, map room, and war museum."
    },
    "Twickenham Stadium": {
        "description": "İngiliz ragbisinin evi, dünyanın en büyük ragbi stadyumu. Müze, stadyum turu ve spor tarihi.",
        "description_en": "Home of England rugby, world's largest rugby stadium. Museum, stadium tour, and sports history."
    },
    "Wembley Stadium": {
        "description": "İngiltere futbolunun mabedi, ikonik kemeriyle ünlü dev stadyum. FA Cup finalleri, konserler ve efsanevi maçlar.",
        "description_en": "Temple of English football, giant stadium famous for iconic arch. FA Cup finals, concerts, and legendary matches."
    }
}

filepath = 'assets/cities/londra.json'
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

print(f"\n✅ Manually enriched {count} items (London - COMPLETE).")
