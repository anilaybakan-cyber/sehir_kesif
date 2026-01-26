import json

# Manual enrichment data (Napoli - ALL 49 items)
updates = {
    "L'Antica Pizzeria da Michele": {
        "description": "Dünyanın en ünlü pizzacısı, Eat Pray Love filmiyle meşhur. Sadece Margherita ve Marinara var, otantik Napoli pizzası.",
        "description_en": "World's most famous pizzeria, famous from Eat Pray Love. Only Margherita and Marinara, authentic Neapolitan pizza."
    },
    "Gino Sorbillo": {
        "description": "Via dei Tribunali'de efsanevi pizzacı, dev tekerlek pizzalar. Uzun kuyruklar, taze malzemeler ve Napoli'nin gururu.",
        "description_en": "Legendary pizzeria on Via dei Tribunali with giant wheel pizzas. Long lines, fresh ingredients, and pride of Naples."
    },
    "Mount Vesuvius": {
        "description": "Pompeii'yi yok eden aktif yanardağ, krater yürüyüşü ve körfez manzarası. Doğa tarihi, jeoloji ve macera.",
        "description_en": "Active volcano that destroyed Pompeii, crater hike, and bay views. Natural history, geology, and adventure."
    },
    "Pompeii Archaeological Park": {
        "description": "Antik Roma kenti kalıntıları, lavlar altında korunmuş tarih. Forum, hamamlar ve villalarla 2000 yıl öncesine yolculuk.",
        "description_en": "Ruins of ancient Roman city preserved under lava. Journey 2000 years back with Forum, baths, and villas."
    },
    "Naples National Archaeological Museum": {
        "description": "Dünyanın en önemli Roma sanatı müzelerinden biri. Pompeii mozaikleri, Farnese Heykelleri ve Gizli Gabine.",
        "description_en": "One of world's most important museums of Roman art. Pompeii mosaics, Farnese Sculptures, and Secret Cabinet."
    },
    "Castel dell'Ovo": {
        "description": "Napoli körfezindeki adacık üzerinde tarihi kale. 'Yumurta Kalesi' efsanesi, deniz manzarası ve Borgo Marinari.",
        "description_en": "Historic castle on islet in Bay of Naples. 'Egg Castle' legend, sea views, and Borgo Marinari."
    },
    "Spaccanapoli": {
        "description": "Napoli'yi tam ortadan ikiye bölen ikonik, dar ve uzun cadde. Kiliseler, dükkanlar, kaos ve şehrin kalbi.",
        "description_en": "Iconic, narrow, and long street splitting Naples exactly in two. Churches, shops, chaos, and heart of the city."
    },
    "San Severo Chapel": {
        "description": "Mermer işçiliğinin şaheseri 'Örtülü İsa' heykelini barındıran şapel. Barok sanat, masonik semboller ve gizem.",
        "description_en": "Chapel housing 'Veiled Christ' masterpiece of marble craftsmanship. Baroque art, Masonic symbols, and mystery."
    },
    "Toledo Metro Station": {
        "description": "Avrupa'nın en güzel metro istasyonu, sanat eseri gibi mozaikler. 'Sanat İstasyonları' projesi, okyanus teması.",
        "description_en": "Europe's most beautiful metro station with art-like mosaics. 'Art Stations' project, ocean theme."
    },
    "Piazza del Plebiscito": {
        "description": "Napoli'nin ana meydanı, San Francesco di Paola Kilisesi ve Kraliyet Sarayı. Konserler, yürüyüş ve geniş alan.",
        "description_en": "Naples' main square with San Francesco di Paola Church and Royal Palace. Concerts, walking, and vast space."
    },
    "Royal Palace of Naples": {
        "description": "Bourbon krallarının görkemli sarayı, tarihi apartmanlar ve taht odası. Zengin dekorasyon, sanat ve tarih.",
        "description_en": "Grand palace of Bourbon kings with historic apartments and throne room. Rich decoration, art, and history."
    },
    "Teatro di San Carlo": {
        "description": "Dünyanın en eski aktif opera binası, 1737'den beri. Altın ve kırmızı kadife dekor, mükemmel akustik ve bale.",
        "description_en": "World's oldest active opera house, since 1737. Gold and red velvet decor, perfect acoustics, and ballet."
    },
    "Galleria Umberto I": {
        "description": "Milano'daki Galleria'ya benzeyen cam tavanlı 19. yüzyıl pasajı. Mermer zemin, mağazalar ve zarif mimari.",
        "description_en": "19th-century glass-roofed arcade resembling Galleria in Milan. Marble floor, shops, and elegant architecture."
    },
    "Lungomare": {
        "description": "Napoli'nin sahil yürüyüş yolu, Vezüv ve Capri manzarası. Araçsız alan, restoranlar ve akşam yürüyüşü.",
        "description_en": "Naples' seaside promenade with Vesuvius and Capri views. Car-free zone, restaurants, and evening walk."
    },
    "Catacombs of San Gennaro": {
        "description": "Erken Hıristiyanlık dönemi yeraltı mezarları ve bazilikalar. Freskler, yerel aziz tarihi ve yeraltı şehri.",
        "description_en": "Early Christian underground tombs and basilicas. Frescoes, local saint history, and underground city."
    },
    "Naples Underground": {
        "description": "Şehrin altındaki tarihi tüneller, sarnıçlar ve sığınaklar. Roma dönemi su yolları ve İkinci Dünya Savaşı sığınakları.",
        "description_en": "Historic tunnels, cisterns, and shelters beneath the city. Roman aqueducts and WWII shelters."
    },
    "Pizzeria Starita": {
        "description": "Materdei bölgesinde tarihi pizzacı, 'L'Oro di Napoli' filmi mekanı. Kızarmış pizza (Montanara) ve gelenek.",
        "description_en": "Historic pizzeria in Materdei, 'L'Oro di Napoli' movie location. Fried pizza (Montanara) and tradition."
    },
    "50 Kalo": {
        "description": "Ciro Salvo'nun modern pizzacısı, yüksek hidrasyonlu hamur. Michelin rehberi, hafif pizza ve gurme malzemeler.",
        "description_en": "Ciro Salvo's modern pizzeria with high-hydration dough. Michelin guide, light pizza, and gourmet ingredients."
    },
    "Gran Caffe Gambrinus": {
        "description": "Napoli'nin en tarihi kafesi, Belle Époque tarzı. Espresso, sfogliatella ve edebi buluşma noktası.",
        "description_en": "Naples' most historic cafe, Belle Époque style. Espresso, sfogliatella, and literary meeting point."
    },
    "Sfogliatella Mary": {
        "description": "Galleria Umberto girişinde ünlü pastane büfesi. Sıcak, çıtır sfogliatella riccia veya frolla.",
        "description_en": "Famous pastry kiosk at Galleria Umberto entrance. Hot, crispy sfogliatella riccia or frolla."
    },
    "Pintauro": {
        "description": "Sfogliatella'nın mucidi sayılan tarihi pastane. Via Toledo'da, geleneksel tarif ve Napoli tatlısı.",
        "description_en": "Historic pastry shop considered inventor of sfogliatella. On Via Toledo, traditional recipe, and Neapolitan dessert."
    },
    "Via San Gregorio Armeno": {
        "description": "Noel betimlemeleri (presepio) atölyeleriyle ünlü dar sokak. El yapımı figürler, yıl boyu Noel süsleri.",
        "description_en": "Narrow street famous for nativity scene (presepio) workshops. Handmade figures, year-round Christmas decorations."
    },
    "Certosa di San Martino": {
        "description": "Şehre tepeden bakan eski manastır, şimdi müze. Barok kilise, müthiş manzara ve Napoli presepe koleksiyonu.",
        "description_en": "Former monastery overlooking city, now museum. Baroque church, amazing views, and Neapolitan presepe collection."
    },
    "Castel Sant'Elmo": {
        "description": "Yıldız şeklindeki ortaçağ kalesi, Napoli'nin en iyi 360 derece manzarası. Vomero tepesi, sanat sergileri.",
        "description_en": "Star-shaped medieval castle with Naples' best 360-degree views. Vomero hill, art exhibitions."
    },
    "Gay-Odin": {
        "description": "Tarihi çikolata dükkanı, 'Foresta' çikolatası ile ünlü. El yapımı pralinler, dondurma ve Napoli geleneği.",
        "description_en": "Historic chocolate shop famous for 'Foresta' chocolate. Handmade pralines, gelato, and Neapolitan tradition."
    },
    "Tandem Ragù": {
        "description": "Sadece Napoli usulü ragù (et sosu) servis eden restoran. Yavaş pişmiş sos, makarna ve ekmek banma ritüeli.",
        "description_en": "Restaurant serving only Neapolitan ragù (meat sauce). Slow-cooked sauce, pasta, and bread dipping ritual."
    },
    "Trattoria da Nennella": {
        "description": "İspanyol mahallesinde efsanevi esnaf lokantası. Kaotik eğlence, ucuz set menü ve garson şovları.",
        "description_en": "Legendary workers' trattoria in Spanish Quarter. Chaotic fun, cheap set menu, and waiter shows."
    },
    "Pescheria Azzurra": {
        "description": "Gündüz balıkçı, akşam deniz ürünleri lokantası. Taze balık, cuoppo (külah) kızartma ve sokak lezzeti.",
        "description_en": "Fishmonger by day, seafood eatery by night. Fresh fish, cuoppo (cone) fry, and street flavor."
    },
    "Friggitoria Vomero": {
        "description": "Vomero bölgesinde kızarmış sokak lezzetleri durağı. Panzerotti, arancini ve zeppole.",
        "description_en": "Fried street food stop in Vomero district. Panzerotti, arancini, and zeppole."
    },
    "Palazzo Reale": {
        "description": "Napoli Kraliyet Sarayı, Bourbonların ihtişamlı evi. Tarihi daireler, mobilyalar ve körfez manzarası.",
        "description_en": "Royal Palace of Naples, magnificent home of Bourbons. Historic apartments, furniture, and bay views."
    },
    "Museo Madre": {
        "description": "Donnaregina Çağdaş Sanat Müzesi. Tarihi binada modern enstalasyonlar, Jeff Koons ve Anish Kapoor.",
        "description_en": "Donnaregina Contemporary Art Museum. Modern installations in historic building, Jeff Koons and Anish Kapoor."
    },
    "Pignasecca Market": {
        "description": "Napoli'nin en eski açık hava pazarı, gıda ve giyim. Gürültülü, renkli ve otantik Napoli kaosu.",
        "description_en": "Naples' oldest open-air market, food and clothing. Noisy, colorful, and authentic Neapolitan chaos."
    },
    "Villa Comunale": {
        "description": "Sahil şeridinde tarihi şehir parkı, neoklasik heykeller. Yürüyüş, deniz havası ve Pazar antika pazarı.",
        "description_en": "Historic city park on seafront with neoclassical sculptures. Walking, sea air, and Sunday antique market."
    },
    "Mergellina": {
        "description": "Liman bölgesi ve şık sahil semti. Balıkçı tekneleri, chalet kafeler ve romantik yürüyüşler.",
        "description_en": "Harbor area and chic seaside district. Fishing boats, chalet cafes, and romantic walks."
    },
    "Posillipo": {
        "description": "Zengin villaları ve muhteşem manzarasıyla ünlü tepe semti. Napoli körfezinin en iyi panoraması.",
        "description_en": "Hillside district famous for wealthy villas and magnificent views. Best panorama of Bay of Naples."
    },
    "Virgiliano Park": {
        "description": "Posillipo tepesinde teras park, Nisida ve Capri manzarası. Piknik, koşu ve gün batımı noktası.",
        "description_en": "Terrace park on Posillipo hill with Nisida and Capri views. Picnic, jogging, and sunset spot."
    },
    "Cimitero delle Fontanelle": {
        "description": "Eski tüf ocağında binlerce isimsiz kafatası barındıran kemiklik. 'Pezzentelle' ruhları kültü ve mistik atmosfer.",
        "description_en": "Ossuary housing thousands of anonymous skulls in old tuff quarry. Cult of 'pezzentelle' souls and mystic atmosphere."
    },
    "Santa Chiara": {
        "description": "Gotik kilise ve majolica çinili muhteşem manastır avlusu. Sarı-mavi çiniler, limon ağaçları ve huzur.",
        "description_en": "Gothic church and magnificent cloister courtyard with majolica tiles. Yellow-blue tiles, lemon trees, and peace."
    },
    "Gesù Nuovo": {
        "description": "Elmas uçlu taş cephesiyle ünlü barok kilise. İçi altın ve fresklerle dolu, San Giuseppe Moscati kültü.",
        "description_en": "Baroque church famous for diamond-point stone facade. Interior full of gold and frescoes, cult of San Giuseppe Moscati."
    },
    "Palazzo dello Spagnolo": {
        "description": "Sanità bölgesinde rokoko tarzı merdivenleriyle ünlü saray. 'Şahin kanadı' merdivenler, mimari fotoğrafçılık.",
        "description_en": "Palace in Sanità district famous for Rococo style staircases. 'Hawk wing' stairs, architectural photography."
    },
    "Botanical Garden": {
        "description": "19. yüzyılda kurulan botanik bahçesi, nadir bitkiler. Şehir gürültüsünden kaçış, eğitim ve doğa.",
        "description_en": "Botanical garden founded in 19th century with rare plants. Escape from city noise, education, and nature."
    },
    "Concettina ai Tre Santi": {
        "description": "Sanità bölgesinde yenilikçi pizza deneyimi, Ciro Oliva. Tadım menüsü, modern dokunuşlar ve sosyal proje.",
        "description_en": "Innovative pizza experience in Sanità district, Ciro Oliva. Tasting menu, modern touches, and social project."
    },
    "Poppella": {
        "description": "'Fiocco di Neve' (Kar Tanesi) tatlısının yaratıcısı pastane. Hafif krema dolgulu yumuşak brioche, efsane lezzet.",
        "description_en": "Pastry shop creator of 'Fiocco di Neve' (Snowflake) dessert. Soft brioche with light cream filling, legendary flavor."
    },
    "Scaturchio": {
        "description": "Baba au rhum ve sfogliatella için klasik adres. Piazza San Domenico Maggiore'de, tarihi atmosfer.",
        "description_en": "Classic address for Baba au rhum and sfogliatella. In Piazza San Domenico Maggiore, historic atmosphere."
    },
    "Oak Naples": {
        "description": "Geniş şarap ve bira seçkisi sunan keyifli pub. Rahat ortam, aperitivo ve yerel gençler.",
        "description_en": "Pleasant pub offering wide selection of wine and beer. Relaxed setting, aperitivo, and local youth."
    },
    "L'Antiquario": {
        "description": "Speakeasy tarzı kokteyl barı, caz müzik ve şık garsonlar. Klasik kokteyller, sofistike gece hayatı.",
        "description_en": "Speakeasy style cocktail bar, jazz music, and elegant waiters. Classic cocktails, sophisticated nightlife."
    },
    "Galleria Borbonica": {
        "description": "Kraliyet sarayı altındaki askeri tünel, eski arabalar ve sığınaklar. Bourbon tüneli, rehberli macera.",
        "description_en": "Military tunnel under royal palace, vintage cars, and shelters. Bourbon tunnel, guided adventure."
    },
    "Teatro Bellini": {
        "description": "Tarihi tiyatro ve kültür merkezi, edebiyat kafesi. Kitapçılar, kahve ve sanatsal etkinlikler.",
        "description_en": "Historic theater and cultural center, literary cafe. Bookshops, coffee, and artistic events."
    },
    "Port'Alba": {
        "description": "Eski şehir kapısı ve kitapçılar sokağı. Sahaf tezgahları, müzik dükkanları ve entelektüel atmosfer.",
        "description_en": "Old city gate and street of booksellers. Second-hand book stalls, music shops, and intellectual atmosphere."
    }
}

filepath = 'assets/cities/napoli.json'
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

print(f"\n✅ Manually enriched {count} items (Napoli - COMPLETE).")
