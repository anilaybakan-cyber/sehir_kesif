import json

# Manual enrichment data (Seoul - ALL 42 items)
updates = {
    "Gyeongbokgung Palace": {
        "description": "Seul'ün en büyük ve görkemli kraliyet sarayı, 1395'ten. Muhafız değişim töreni, hanbok giyenlere ücretsiz giriş.",
        "description_en": "Seoul's largest and most magnificent royal palace, from 1395. Changing of guard ceremony, free entry for hanbok wearers."
    },
    "Bukchon Hanok Village": {
        "description": "Geleneksel Kore evlerinin (hanok) bulunduğu tarihi mahalle. Dar sokaklar, çatı manzaraları ve yaşayan tarih.",
        "description_en": "Historic neighborhood with traditional Korean houses (hanok). Narrow alleys, rooftop views, and living history."
    },
    "N Seoul Tower": {
        "description": "Namsan Dağı tepesindeki ikonik iletişim kulesi. Aşk kilitleri, teleferik yolculuğu ve 360 derece Seul panoraması.",
        "description_en": "Iconic communication tower atop Namsan Mountain. Love locks, cable car ride, and 360-degree Seoul panorama."
    },
    "Myeongdong Shopping Street": {
        "description": "Kore kozmetiği ve sokak yemekleri cenneti. Gece ışıkları, kalabalık ve alışverişin kalbi.",
        "description_en": "Paradise of Korean cosmetics and street food. Night lights, crowds, and heart of shopping."
    },
    "Lotte World Tower": {
        "description": "Kore'nin en yüksek, dünyanın 5. yüksek binası (555m). Gözlem güvertesi Seoul Sky, cam zemin ve lüks alışveriş.",
        "description_en": "Korea's tallest, world's 5th tallest building (555m). Observation deck Seoul Sky, glass floor, and luxury shopping."
    },
    "Starfield Library": {
        "description": "COEX Mall içindeki devasa, fütüristik kütüphane. 13 metrelik kitap rafları, okuma alanları ve Instagram noktası.",
        "description_en": "Massive, futuristic library inside COEX Mall. 13-meter bookshelves, reading areas, and Instagram spot."
    },
    "Dongdaemun Design Plaza": {
        "description": "Zaha Hadid tasarımı neofütüristik yapı (DDP). Moda haftaları, sergiler ve gece LED gül bahçesi.",
        "description_en": "Neo-futuristic structure designed by Zaha Hadid (DDP). Fashion weeks, exhibitions, and night LED rose garden."
    },
    "Changdeokgung Palace": {
        "description": "UNESCO Dünya Mirası listesindeki saray ve Gizli Bahçe (Huwon). Doğa ile uyumlu mimari ve kraliyet huzuru.",
        "description_en": "UNESCO World Heritage palace and Secret Garden (Huwon). Architecture in harmony with nature and royal peace."
    },
    "Lotte World Adventure": {
        "description": "Dünyanın en büyük kapalı tema parkı ve açık hava 'Magic Island'. Eğlence, masal şatosu ve buz pisti.",
        "description_en": "World's largest indoor theme park and outdoor 'Magic Island'. Fun, fairy tale castle, and ice rink."
    },
    "Hongdae Street": {
        "description": "Gençlik kültürü, sokak sanatçıları (busking) ve moda merkezi. Öğrenci enerjisi, kulüpler ve indie müzik.",
        "description_en": "Youth culture, street performers (busking), and fashion hub. Student energy, clubs, and indie music."
    },
    "Itaewon": {
        "description": "Seul'ün uluslararası mahallesi, çeşitlilik ve gece hayatı. Yabancı restoranlar, barlar ve Itaewon Class dizisi seti.",
        "description_en": "Seoul's international neighborhood, diversity, and nightlife. Foreign restaurants, bars, and Itaewon Class series set."
    },
    "Gwangjang Market": {
        "description": "Kore sokak yemeklerinin kalbi, Netflix ile ünlendi. Mung bean pancake, kalguksu ve canlı yeme-içme kültürü.",
        "description_en": "Heart of Korean street food, made famous by Netflix. Mung bean pancake, kalguksu, and lively dining culture."
    },
    "Insadong": {
        "description": "Geleneksel Kore sanatları, çay evleri ve antikalar sokağı. Ssamzigil alışveriş kompleksi ve kültürel hediyelikler.",
        "description_en": "Street of traditional Korean arts, tea houses, and antiques. Ssamzigil shopping complex and cultural souvenirs."
    },
    "Cheonggyecheon Stream": {
        "description": "Şehir merkezinde restore edilmiş yapay dere yürüyüş yolu. Gece ışıklandırması, fener festivalleri ve huzur.",
        "description_en": "Restored artificial stream walking path in city center. Night illumination, lantern festivals, and peace."
    },
    "Tosokchon Samgyetang": {
        "description": "Kore'nin en ünlü ginsengli tavuk çorbası (Samgyetang) restoranı. Geleneksel hanok evinde, başkanların favorisi.",
        "description_en": "Korea's most famous ginseng chicken soup (Samgyetang) restaurant. In traditional hanok house, favorite of presidents."
    },
    "Myeongdong Kyoja": {
        "description": "1966'dan beri hizmet veren efsanevi noodle ve mantı restoranı. Michelin Bib Gourmand, sarımsaklı kimchi ve kalguksu.",
        "description_en": "Legendary noodle and dumpling restaurant serving since 1966. Michelin Bib Gourmand, garlicky kimchi, and kalguksu."
    },
    "Onion Anguk": {
        "description": "Geleneksel Hanok mimarisinde modern fırın kafe. Taze hamur işleri, Pandoro ve tarihi atmosfer.",
        "description_en": "Modern bakery cafe in traditional Hanok architecture. Fresh pastries, Pandoro, and historic atmosphere."
    },
    "Cafe Layered": {
        "description": "İngiliz tarzı scone ve kekleriyle ünlü şirin kafe. Bukchon'da, vintage dekor ve tatlı cenneti.",
        "description_en": "Cute cafe famous for English-style scones and cakes. In Bukchon, vintage decor and dessert paradise."
    },
    "Stylenanda Pink Pool Cafe": {
        "description": "Tamamen pembe dekorasyonlu ve havuz temalı Instagram kafesi. Stylenanda moda mağazasının tepesinde.",
        "description_en": "Completely pink decorated and pool-themed Instagram cafe. On top of Stylenanda fashion store."
    },
    "Jungsik": {
        "description": "New Korean mutfağının öncüsü iki Michelin yıldızlı restoran. Geleneksel tatlara modern yorum, sanat gibi tabaklar.",
        "description_en": "Two Michelin-starred pioneer of New Korean cuisine. Modern interpretation of traditional flavors, art-like plates."
    },
    "Maple Tree House": {
        "description": "Premium Kore barbeküsü, kaliteli etler ve şık ortam. Itaewon'da, turist dostu ve otantik lezzet.",
        "description_en": "Premium Korean barbecue, quality meats, and stylish setting. In Itaewon, tourist friendly and authentic flavor."
    },
    "Noryangjin Fish Market": {
        "description": "Seul'ün en büyük balık pazarı, canlı deniz ürünleri. Alt katta seç, üst katta pişirt ye deneyimi.",
        "description_en": "Seoul's largest fish market, live seafood. Pick downstairs, have it cooked and eat upstairs experience."
    },
    "War Memorial of Korea": {
        "description": "Kore Savaşı tarihini anlatan devasa müze ve anıt. Askeri uçaklar, tanklar ve barış mesajı.",
        "description_en": "Massive museum and memorial telling history of Korean War. Military aircraft, tanks, and peace message."
    },
    "National Museum of Korea": {
        "description": "Kore tarihini ve sanatını sergileyen amiral gemisi müze. Devasa mimari, ücretsiz giriş ve kültürel hazineler.",
        "description_en": "Flagship museum exhibiting Korean history and art. Massive architecture, free entry, and cultural treasures."
    },
    "Leeum Samsung Museum of Art": {
        "description": "Samsung Vakfı'nın özel sanat müzesi, geleneksel ve çağdaş sanat. Mario Botta, Jean Nouvel ve Rem Koolhaas mimarisi.",
        "description_en": "Samsung Foundation's private art museum, traditional and contemporary art. Mario Botta, Jean Nouvel, and Rem Koolhaas architecture."
    },
    "Greem Cafe": {
        "description": "2D çizgi roman dünyası konseptli kafe (Yeonnam-dong 223-14). Siyah beyaz çizimler, optik illüzyon ve fotoğraf.",
        "description_en": "2D comic book world concept cafe (Yeonnam-dong 223-14). Black and white drawings, optical illusion, and photography."
    },
    "Ikseondong Hanok Village": {
        "description": "Restore edilmiş en eski hanok mahallesi, şimdi trend kafeler ve dükkanlar. Dar sokaklar, modern-geleneksel sentezi.",
        "description_en": "Restored oldest hanok neighborhood, now trendy cafes and shops. Narrow alleys, modern-traditional synthesis."
    },
    "Common Ground": {
        "description": "Mavi konteynerlerden yapılmış pop-up alışveriş merkezi. Genç markalar, sokak etkinlikleri ve fotoğraf fonu.",
        "description_en": "Pop-up shopping mall made of blue containers. Young brands, street events, and photography background."
    },
    "Banpo Bridge Rainbow Fountain": {
        "description": "Dünyanın en uzun köprü şelalesi, müzikli ışık gösterisi. Han Nehri kenarında gece pikniği ve romantizm.",
        "description_en": "World's longest bridge fountain, musical light show. Night picnic by Han River and romance."
    },
    "Everland": {
        "description": "Güney Kore'nin en büyük tema parkı, dev roller coaster T-Express. Hayvanat bahçesi, bahçeler ve festivaller.",
        "description_en": "South Korea's largest theme park, giant roller coaster T-Express. Zoo, gardens, and festivals."
    },
    "Gangnam Style Statue": {
        "description": "Psy'ın hit şarkısına adanmış dev el heykeli, COEX önünde. Şarkı çalıyor, Gangnam'ın simgesi.",
        "description_en": "Giant hand statue dedicated to Psy's hit song, in front of COEX. Song plays, symbol of Gangnam."
    },
    "Jogyesa Temple": {
        "description": "Kore Budizmi'nin merkezi tapınağı, şehir ormanında huzur. Renkli fenerler, nilüfer festivali ve asırlık ağaçlar.",
        "description_en": "Center temple of Korean Buddhism, peace in urban forest. Colorful lanterns, lotus festival, and century-old trees."
    },
    "Seoul Forest": {
        "description": "Şehrin akciğeri büyük park, geyik besleme alanı ve yürüyüş yolları. Baharda kiraz çiçeği, sonbaharda yapraklar.",
        "description_en": "Large park serving as city's lungs, deer feeding area, and walking trails. Cherry blossoms in spring, leaves in autumn."
    },
    "Olympic Park": {
        "description": "1988 Olimpiyatları mirası, spor ve kültür kompleksi. Yalnız Ağaç, heykel parkı ve geniş çim alanlar.",
        "description_en": "1988 Olympics legacy, sports and culture complex. Lone Tree, sculpture park, and vast lawns."
    },
    "Haneul Park": {
        "description": "Eski çöplükten dönüşen 'Gökyüzü Parkı', gümüş otları (silver grass) ile ünlü. Gün batımı, rüzgar tribünleri ve manzara.",
        "description_en": "'Sky Park' transformed from old landfill, famous for silver grass. Sunset, wind turbines, and views."
    },
    "Ewha Womans University": {
        "description": "Kore'nin en prestijli kadın üniversitesi, popüler kampüs mimarisi 'Ewha Campus Complex'. Alışveriş caddesi ve gençlik.",
        "description_en": "Korea's most prestigious women's university, popular campus architecture 'Ewha Campus Complex'. Shopping street and youth."
    },
    "Yeouido Hangang Park": {
        "description": "Han Nehri kıyısındaki en popüler park, bisiklet ve piknik. I Seoul U yazısı, nehir kruvaziyerleri ve festivaller.",
        "description_en": "Most popular park on Han River bank, cycling and picnics. I Seoul U sign, river cruises, and festivals."
    },
    "Blue House (Cheong Wa Dae)": {
        "description": "Eski başkanlık sarayı, mavi kiremitli çatı. Artık halka açık müze, bahçeler ve siyasi tarih.",
        "description_en": "Former presidential palace, blue tiled roof. Now public museum, gardens, and political history."
    },
    "COEX Aquarium": {
        "description": "Gangnam'daki dev akvaryum, 40.000 deniz canlısı. Köpekbalığı tüneli, penguenler ve tematik bölgeler.",
        "description_en": "Giant aquarium in Gangnam, 40,000 marine creatures. Shark tunnel, penguins, and thematic zones."
    },
    "Seokchon Lake": {
        "description": "Lotte World çevresindeki göl, yürüyüş ve koşu parkuru. Sakura festivali ve gökdelen manzarası.",
        "description_en": "Lake around Lotte World, walking and jogging track. Sakura festival and skyscraper views."
    },
    "Ddong Cafe": {
        "description": "Kakası temalı eğlenceli kafe (Poop Cafe), Insadong'da. Klozet şeklinde kupalar, kaka şeklinde waffle.",
        "description_en": "Fun poop-themed cafe (Poop Cafe) in Insadong. Toilet-shaped mugs, poop-shaped waffles."
    },
    "Bongeunsa Temple": {
        "description": "Gangnam'ın gökdelenleri arasında 1200 yıllık Budist tapınağı. Devasa Buda heykeli, huzur ve tapınak konaklaması.",
        "description_en": "1200-year-old Buddhist temple amidst Gangnam skyscrapers. Giant Buddha statue, peace, and temple stay."
    }
}

filepath = 'assets/cities/seul.json'
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

print(f"\n✅ Manually enriched {count} items (Seoul - COMPLETE).")
