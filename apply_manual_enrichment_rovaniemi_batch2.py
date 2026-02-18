import json

# Manual enrichment data (Rovaniemi Batch 2: 40 items)
updates = {
    "Santasport Institute": {
        "description": "Spor ve wellness merkezi, yüzme havuzu, spor salonu ve antrenman tesisleri. Finlandiya olimpik hazırlık merkezi, sağlıklı yaşam.",
        "description_en": "Sports and wellness center with swimming pool, gym, and training facilities. Finnish Olympic preparation center, healthy living."
    },
    "Ounasvaara Summer Bobsleigh Track": {
        "description": "Yaz aylarında kızak pisti, yazın bile bobsled heyecanı. Aileler için eğlence, tepe aşağı hız ve macera.",
        "description_en": "Summer bobsled track, bobsled excitement even in summer. Fun for families, downhill speed, and adventure."
    },
    "Bearhill Husky": {
        "description": "Husky çiftliği ve köpek kızağı turları, samimi aile işletmesi. Husky tanışma, yavru köpekler ve kış macerası.",
        "description_en": "Husky farm and dog sled tours, intimate family business. Meeting huskies, puppies, and winter adventure."
    },
    "Ollero Eco Lodge": {
        "description": "Sürdürülebilir turizm odaklı eko konaklama, doğa içinde izole kulübeler. Kuzey Işıkları, sessizlik ve çevre dostu tatil.",
        "description_en": "Eco accommodation focused on sustainable tourism with isolated cabins in nature. Northern Lights, silence, and eco-friendly vacation."
    },
    "Syväsenvaara Fell": {
        "description": "Rovaniemi yakınındaki tepe, kış sporları ve yaz yürüyüşleri. Kayak, snowboard ve panoramik Laponya manzarası.",
        "description_en": "Hill near Rovaniemi for winter sports and summer hiking. Skiing, snowboarding, and panoramic Lapland views."
    },
    "Pöyliövaara": {
        "description": "Doğa yürüyüşü ve outdoor aktiviteler için tepeler, Lapon vahşi doğası. Trekking rotaları, kuş gözlemi ve fotoğrafçılık.",
        "description_en": "Hills for nature hiking and outdoor activities in Lappish wilderness. Trekking routes, bird watching, and photography."
    },
    "Rovaniemi Disc Golf Park": {
        "description": "Disk golf sahası, doğa içinde eğlenceli spor aktivitesi. Yaz aylarında popüler, aileler ve arkadaşlar için.",
        "description_en": "Disc golf course, fun sports activity in nature. Popular in summer, for families and friends."
    },
    "Vaattunki Wilderness Area": {
        "description": "El değmemiş Lapon doğası, trekking ve kamp için vahşi alan. Ayı gözlemi, balıkçılık ve nordik macera.",
        "description_en": "Untouched Lappish nature, wild area for trekking and camping. Bear watching, fishing, and Nordic adventure."
    },
    "Sierijärvi Reindeer Farm": {
        "description": "Aile işletmesi ren geyiği çiftliği, geleneksel Sami kültürü ve yaşam tarzı. Ren geyiği safari, besleme ve kültürel deneyim.",
        "description_en": "Family-run reindeer farm with traditional Sami culture and lifestyle. Reindeer safari, feeding, and cultural experience."
    },
    "Chalet Hotel Rovaniemi": {
        "description": "Ounasvaara'daki şale tarzı otel, kayak pistlerine yakın konum. Dağ manzarası, sauna ve kış tatili atmosferi.",
        "description_en": "Chalet-style hotel in Ounasvaara near ski slopes. Mountain views, sauna, and winter vacation atmosphere."
    },
    "Lapland Hotels Sky Ounasvaara": {
        "description": "Ounasvaara tepesinde cam odalı otel, Kuzey Işıkları izleme. Aurora borealis, lüks konaklama ve romantik kaçış.",
        "description_en": "Hotel with glass rooms on Ounasvaara hill for Northern Lights viewing. Aurora borealis, luxury accommodation, and romantic escape."
    },
    "Napapiirin Porofarmi": {
        "description": "Kuzey Kutup Dairesi'ndeki ren geyiği çiftliği, safari turları ve Sami kültürü. Ren geyiği kızağı, besleme ve fotoğraf.",
        "description_en": "Reindeer farm at Arctic Circle with safari tours and Sami culture. Reindeer sleigh, feeding, and photography."
    },
    "Rovaniemi Local History Museum": {
        "description": "Şehrin yerel tarihini ve Lapon kültürünü anlatan müze. Eski fotoğraflar, günlük yaşam eşyaları ve bölge mirası.",
        "description_en": "Museum telling city's local history and Lappish culture. Old photos, daily life items, and regional heritage."
    },
    "Restaurant Aitta": {
        "description": "Geleneksel Lapon yemeklerini modern sunumla harmanlayan fine-dining restoran. Ren geyiği, yaban mersini ve nordik gastronomi.",
        "description_en": "Fine-dining restaurant blending traditional Lappish dishes with modern presentation. Reindeer, lingonberry, and Nordic gastronomy."
    },
    "Frans & Chérie Bistro": {
        "description": "Fransız esintili modern bistro, şık atmosfer ve kaliteli yemekler. Brunch, akşam yemeği ve kokteyller.",
        "description_en": "French-inspired modern bistro with stylish atmosphere and quality food. Brunch, dinner, and cocktails."
    },
    "Amarillo Rovaniemi": {
        "description": "Tex-Mex zincir restoranı, burger, fajita ve margarita. Aileler için rahat, renkli atmosfer.",
        "description_en": "Tex-Mex chain restaurant with burger, fajitas, and margaritas. Comfortable for families, colorful atmosphere."
    },
    "Himo": {
        "description": "Şehrin popüler gece kulübü, DJ müziği ve dans. Hafta sonu partileri, gece hayatı ve gençlik.",
        "description_en": "City's popular nightclub with DJ music and dancing. Weekend parties, nightlife, and youth."
    },
    "Hemingway's Rovaniemi": {
        "description": "Geniş kokteyl seçkisi ve rahat atmosferiyle bar-restoran. Akşam içkileri, sosyal ortam ve şehir merkezinde buluşma.",
        "description_en": "Bar-restaurant with wide cocktail selection and comfortable atmosphere. Evening drinks, social setting, and city center meeting."
    },
    "Oliver's Corner": {
        "description": "İrlanda tarzı pub, canlı müzik geceleri ve yerel bira. Samimi atmosfer, sports bar ve sosyal mekan.",
        "description_en": "Irish-style pub with live music nights and local beer. Intimate atmosphere, sports bar, and social venue."
    },
    "Bull Bar & Grill": {
        "description": "Amerikan tarzı steakhouse ve bar, et yemekleri ve sporlar. Büyük porsiyonlar, TV ekranları ve rahat ortam.",
        "description_en": "American-style steakhouse and bar with meat dishes and sports. Large portions, TV screens, and comfortable setting."
    },
    "Uitto Pub": {
        "description": "Yerel halkın favori pub'ı, Finlandiya biracılık kültürü. Samimi ortam, uygun fiyat ve mahalle barı.",
        "description_en": "Local favorite pub with Finnish beer culture. Intimate setting, affordable prices, and neighborhood bar."
    },
    "Irish Arms": {
        "description": "Klasik İrlanda pub'ı, Guinness ve canlı müzik. Pub quiz geceleri, futbol maçları ve sosyal atmosfer.",
        "description_en": "Classic Irish pub with Guinness and live music. Pub quiz nights, football matches, and social atmosphere."
    },
    "Roka Street Bistro": {
        "description": "Modern sokak yemekleri ve fusion mutfak konsepti. Yaratıcı tabaklar, casual dining ve genç şefler.",
        "description_en": "Modern street food and fusion cuisine concept. Creative dishes, casual dining, and young chefs."
    },
    "Choco Deli": {
        "description": "El yapımı çikolata ve tatlılar sunan butik kafe. Sıcak kakao, pralin ve Finlandiya tatlı kültürü.",
        "description_en": "Boutique cafe serving handmade chocolate and desserts. Hot cocoa, pralines, and Finnish dessert culture."
    },
    "Antinkaapo": {
        "description": "Geleneksel Lapon yemekleri ve bölgesel tarifler sunan restoran. Ev yapımı lezzetler, ren geyiği çorbası ve yöresel mutfak.",
        "description_en": "Restaurant serving traditional Lappish dishes and regional recipes. Homemade flavors, reindeer soup, and local cuisine."
    },
    "Zoomit": {
        "description": "Finlandiya fast-food zinciri, hamburger, patates kızartması ve milkshake. Hızlı servis, çocuk menüleri ve pratik yemek.",
        "description_en": "Finnish fast-food chain with hamburger, fries, and milkshakes. Quick service, kids' menus, and practical meal."
    },
    "Ravintola Valdemari": {
        "description": "Finlandiya klasik yemekleri ve nordik lezzetler sunan geleneksel restoran. Lohikeitto, karjalanpiirakka ve aile atmosferi.",
        "description_en": "Traditional restaurant serving Finnish classic dishes and Nordic flavors. Salmon soup, Karelian pie, and family atmosphere."
    },
    "Saigon Noodle Bar": {
        "description": "Vietnam mutfağı ve noodle çeşitleri sunan Asya restoranı. Pho, banh mi ve Uzak Doğu lezzetleri.",
        "description_en": "Asian restaurant serving Vietnamese cuisine and noodle varieties. Pho, banh mi, and Far East flavors."
    },
    "Hai Long": {
        "description": "Çin ve Vietnam mutfağı sunan Asya restoranı. Dim sum, spring roll ve geleneksel tarifler.",
        "description_en": "Asian restaurant serving Chinese and Vietnamese cuisine. Dim sum, spring rolls, and traditional recipes."
    },
    "Rang Mahal": {
        "description": "Hint mutfağı ve tandoor yemekleri sunan restoran. Tikka masala, naan ve baharatlı lezzetler.",
        "description_en": "Restaurant serving Indian cuisine and tandoor dishes. Tikka masala, naan, and spicy flavors."
    },
    "Wingston": {
        "description": "Tavuk kanat ve Amerikan tarzı pub yemekleri sunan casual mekan. Soslar, bira ve spor izleme.",
        "description_en": "Casual venue serving chicken wings and American-style pub food. Sauces, beer, and sports watching."
    },
    "Pure Pizza": {
        "description": "Napoli usulü pizza ve İtalyan lezzetler sunan pizzeria. İnce hamur, taze malzemeler ve otantik İtalyan lezzeti.",
        "description_en": "Pizzeria serving Neapolitan-style pizza and Italian flavors. Thin crust, fresh ingredients, and authentic Italian taste."
    },
    "Kauppayhtiö": {
        "description": "Tarihi binada modern kafe-restoran, Finlandiya kahvaltısı ve brunch. Nostaljik atmosfer, taze pastalar ve kahve.",
        "description_en": "Modern cafe-restaurant in historic building with Finnish breakfast and brunch. Nostalgic atmosphere, fresh pastries, and coffee."
    },
    "Hook": {
        "description": "Balık ve deniz ürünleri sunan casual restoran. Fish and chips, salmon ve nordik deniz lezzetleri.",
        "description_en": "Casual restaurant serving fish and seafood. Fish and chips, salmon, and Nordic sea flavors."
    },
    "Cafe Rovaniemi": {
        "description": "Şehir merkezinde geleneksel Finlandiya kafesi, kahve ve pulla. Korvapuusti, munkki ve fika kültürü.",
        "description_en": "Traditional Finnish cafe in city center with coffee and pulla. Cinnamon bun, doughnuts, and fika culture."
    },
    "Roy Club": {
        "description": "Şehrin gece kulübü, canlı müzik ve dans pistleri. Hafta sonu eğlencesi, DJ geceleri ve sosyal hayat.",
        "description_en": "City's nightclub with live music and dance floors. Weekend entertainment, DJ nights, and social life."
    },
    "Half Moon Night Club": {
        "description": "Disco ve dans müziği barı, retro atmosfer ve parti. Gece hayatı, kokteyller ve eğlence.",
        "description_en": "Disco and dance music bar with retro atmosphere and party. Nightlife, cocktails, and entertainment."
    },
    "Wanha Mestari": {
        "description": "Eski usul Finlandiya pub'ı, yerel biralar ve samimi ortam. Mahalle barı, canlı sohbetler ve akşam keyfi.",
        "description_en": "Old-style Finnish pub with local beers and intimate setting. Neighborhood bar, lively conversations, and evening enjoyment."
    },
    "Paha Kurki Rockhouse": {
        "description": "Rock müzik barı, canlı konserler ve alternatif sahne. Metal, rock ve underground müzik kültürü.",
        "description_en": "Rock music bar with live concerts and alternative scene. Metal, rock, and underground music culture."
    },
    "People's Pub": {
        "description": "Şehrin popüler halk barı, uygun fiyatlı içecekler ve spor yayınları. Samimi atmosfer, yerel halk ve sosyalleşme.",
        "description_en": "City's popular people's bar with affordable drinks and sports broadcasts. Intimate atmosphere, locals, and socializing."
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

print(f"\n✅ Manually enriched {count} items (Rovaniemi Batch 2).")
