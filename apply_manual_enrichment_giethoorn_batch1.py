import json

# Manual enrichment data (Giethoorn Batch 1: 40 items)
updates = {
    "Dwarsgracht": {
        "description": "Giethoorn'un en pitoresk kanallarından biri, sazlık evler ve ahşap köprülerle çevrili huzurlu su yolu. Tekne turuyla keşfetmek için ideal, fotoğrafçıların favorisi.",
        "description_en": "One of Giethoorn's most picturesque canals, a peaceful waterway surrounded by thatched houses and wooden bridges. Ideal for exploring by boat tour, a photographer's favorite."
    },
    "Kalenberg": {
        "description": "Giethoorn'a komşu geleneksel Hollanda köyü, sazlık çatılı evleri ve kırsal atmosferiyle. Bisiklet turu için mükemmel durak, otantik Hollanda kırsal yaşamı.",
        "description_en": "A traditional Dutch village neighboring Giethoorn with thatched roof houses and rural atmosphere. Perfect stop for bike tour, authentic Dutch rural life."
    },
    "Wanneperveen": {
        "description": "Weerribben-Wieden Milli Parkı'na açılan kapı konumundaki küçük köy. Doğa yürüyüşleri, kuş gözlemciliği ve sulak alan keşfi için başlangıç noktası.",
        "description_en": "A small village serving as gateway to Weerribben-Wieden National Park. Starting point for nature walks, bird watching, and wetland exploration."
    },
    "Blokzijl": {
        "description": "17. yüzyıldan kalma tarihi liman kasabası, UNESCO adayı kent merkezi ve Michelin yıldızlı restoranıyla. Kanal evleri, tarihi sokaklar ve gurme lezzetler.",
        "description_en": "A historic port town from 17th century with UNESCO-candidate city center and Michelin-starred restaurant. Canal houses, historic streets, and gourmet flavors."
    },
    "E-Chopper Rental": {
        "description": "Elektrikli scooter kiralama noktası, çevreyi sessiz ve çevre dostu şekilde keşfetmek için. Kalenberg, Belt-Schutsloot ve çevre köylere eğlenceli ulaşım.",
        "description_en": "Electric scooter rental point for exploring the area quietly and eco-friendly. Fun transportation to Kalenberg, Belt-Schutsloot, and surrounding villages."
    },
    "Weerribben-Wieden Kano Rotaları": {
        "description": "Hollanda'nın en büyük turbalık milli parkında işaretlenmiş kano rotaları. Nadir kuş türleri, su zambakları ve el değmemiş doğayı keşfedin.",
        "description_en": "Marked canoe routes in the Netherlands' largest peatland national park. Discover rare bird species, water lilies, and untouched nature."
    },
    "Uijtwijktoren Woldberg": {
        "description": "Milli parkın panoramik manzarasını sunan gözetleme kulesi. Sulak alanlar, sazlıklar ve vahşi yaşamı kuşbakışı izleme fırsatı.",
        "description_en": "An observation tower offering panoramic views of the national park. Opportunity to view wetlands, reeds, and wildlife from bird's eye."
    },
    "De Rietstulp": {
        "description": "Sazlık çatılı geleneksel binada konumlanan, Hollanda mutfağı sunan aile restoranı. Pannenkoeken, erwtensoep ve yerel lezzetlerle otantik deneyim.",
        "description_en": "A family restaurant in traditional thatched building serving Dutch cuisine. Authentic experience with pancakes, pea soup, and local flavors."
    },
    "Ristorante Fratelli": {
        "description": "Giethoorn'da İtalyan mutfağı sunan, pizza ve makarna çeşitleriyle ünlü restoran. Kanal manzarası, açık hava terası ve Akdeniz lezzetleri.",
        "description_en": "A restaurant in Giethoorn serving Italian cuisine, famous for pizza and pasta varieties. Canal views, outdoor terrace, and Mediterranean flavors."
    },
    "Kaatje bij de Sluis": {
        "description": "Blokzijl'de Michelin yıldızlı restoran, Hollanda fine-dining kültürünün en iyi örneklerinden. Mevsimlik menüler, yaratıcı sunumlar ve gurme deneyim.",
        "description_en": "A Michelin-starred restaurant in Blokzijl, one of the best examples of Dutch fine-dining culture. Seasonal menus, creative presentations, and gourmet experience."
    },
    "Canal Grande": {
        "description": "Giethoorn'un ana su yolu, teknelerin geçtiği ve kanal evlerinin sıralandığı pitoresk kanal. Şişme motorlu tekneler yasak, sadece elektrikli veya kürekli tekneler.",
        "description_en": "Giethoorn's main waterway, a picturesque canal where boats pass and canal houses line up. Inflatable motorboats prohibited, only electric or rowing boats."
    },
    "Zuideindgerwijde": {
        "description": "Giethoorn'un güney kesimindeki geniş göl, yelken ve kano için ideal su alanı. Sakin sular, doğa manzaraları ve su sporları deneyimi.",
        "description_en": "A wide lake in southern Giethoorn, ideal water area for sailing and canoeing. Calm waters, nature views, and water sports experience."
    },
    "Potterie Giethoorn": {
        "description": "El yapımı seramik ve çömlek eserlerinin satıldığı, yerel zanaatkarın atölyesi. Benzersiz hediyelikler, Hollanda tasarımı ve sanatsal parçalar.",
        "description_en": "A local artisan's workshop selling handmade ceramics and pottery. Unique souvenirs, Dutch design, and artistic pieces."
    },
    "Het Wapen van Giethoorn": {
        "description": "Köyün merkezinde konumlanan, geleneksel Hollanda yemekleri sunan tarihi restoran-kafe. Yerel bira, Hollanda peyniri ve sıcak atmosfer.",
        "description_en": "A historic restaurant-cafe in the village center serving traditional Dutch dishes. Local beer, Dutch cheese, and warm atmosphere."
    },
    "Canal Grande Giethoorn": {
        "description": "Ana kanalın en işlek bölümü, turistik tekne turlarının başlangıç noktası. Ahşap köprüler, sazlık evler ve kartpostallık manzaralarla dolu.",
        "description_en": "The busiest section of the main canal, starting point for tourist boat tours. Full of wooden bridges, thatched houses, and postcard views."
    },
    "De Grachthof": {
        "description": "Kanal kenarında bahçeli oturma alanı sunan, Hollanda kahvaltısı ve öğle yemeği için ideal kafe. Pannenkoeken, taze waffle ve kahve keyfi.",
        "description_en": "A cafe with garden seating by the canal, ideal for Dutch breakfast and lunch. Pancakes, fresh waffles, and coffee enjoyment."
    },
    "'t Vonder": {
        "description": "Sazlık çatılı otantik binada, geleneksel Hollanda lezzetleri ve yerel içecekler sunan kafe-restoran. Samimi ortam, köy hayatı atmosferi.",
        "description_en": "A cafe-restaurant in authentic thatched building serving traditional Dutch flavors and local drinks. Intimate setting, village life atmosphere."
    },
    "Venezia Ijs": {
        "description": "İtalyan tarzı dondurma sunan, taze malzemelerle hazırlanan lezzetleriyle ünlü dondurma dükkanı. Kanal kenarında dondurma keyfi, yaz günlerinin favorisi.",
        "description_en": "An ice cream shop serving Italian-style ice cream, famous for flavors made with fresh ingredients. Ice cream enjoyment by the canal, summer favorite."
    },
    "Sint-Steen (St. Stephen's Stone)": {
        "description": "Giethoorn'un tarihi sembolü, köyün kuruluşuyla ilgili efsanelere konu olan antik taş. Yerel hikayeler, tarihi merak ve keşif noktası.",
        "description_en": "Giethoorn's historic symbol, an ancient stone subject to legends about the village's founding. Local stories, historic curiosity, and discovery point."
    },
    "De Eetkamer van Giethoorn": {
        "description": "Modern Hollanda mutfağını geleneksel tariflerle harmanlayan şık restoran. Mevsimlik menü, yerel malzemeler ve özenli sunum.",
        "description_en": "A stylish restaurant blending modern Dutch cuisine with traditional recipes. Seasonal menu, local ingredients, and careful presentation."
    },
    "Spar ter Schure": {
        "description": "Köyün küçük süpermarketi, günlük ihtiyaçlar ve piknik malzemeleri için pratik adres. Yerel ürünler, atıştırmalıklar ve temel gıdalar.",
        "description_en": "The village's small supermarket, practical address for daily needs and picnic supplies. Local products, snacks, and basic groceries."
    },
    "Restaurant 141": {
        "description": "Kanal kenarında konumlanan, uluslararası menüsü ve şık atmosferiyle dikkat çeken restoran. Akşam yemekleri, romantik ortam ve kaliteli servis.",
        "description_en": "A restaurant by the canal notable for international menu and stylish atmosphere. Dinners, romantic setting, and quality service."
    },
    "Giethoorn Floramics": {
        "description": "Çiçek ve bitki satışı yapan, bahçe dekorasyonu ve hediyelik ürünler sunan dükkan. Hollanda lalesi, mevsimlik çiçekler ve bahçe aksesuarları.",
        "description_en": "A shop selling flowers and plants, offering garden decoration and gift products. Dutch tulips, seasonal flowers, and garden accessories."
    },
    "Burgeth": {
        "description": "Giethoorn'un kuzeyinde yer alan küçük yerleşim alanı, otantik Hollanda köy yaşamını yansıtıyor. Sazlık evler, dar kanallar ve huzurlu atmosfer.",
        "description_en": "A small settlement north of Giethoorn reflecting authentic Dutch village life. Thatched houses, narrow canals, and peaceful atmosphere."
    },
    "De Witte Hoeve": {
        "description": "Tarihi beyaz çiftlik evinde konumlanan restoran ve etkinlik mekanı. Kırsal düğünler, özel yemekler ve romantik Hollanda kırsalı.",
        "description_en": "A restaurant and event venue in historic white farmhouse. Rural weddings, special dinners, and romantic Dutch countryside."
    },
    "Doopsgezinde Kerk Giethoorn": {
        "description": "17. yüzyıldan kalma Mennonit kilisesi, sade mimarisi ve barışçıl atmosferiyle dikkat çekiyor. Hollanda Protestan mirasının önemli örneği.",
        "description_en": "A 17th-century Mennonite church notable for simple architecture and peaceful atmosphere. An important example of Dutch Protestant heritage."
    },
    "De Fanfare": {
        "description": "Köyün sosyal merkezi, canlı müzik ve topluluk etkinliklerine ev sahipliği yapan mekan. Konserler, festivaller ve yerel kültürel yaşam.",
        "description_en": "The village's social center, a venue hosting live music and community events. Concerts, festivals, and local cultural life."
    },
    "Eetcafé de Fanfare": {
        "description": "De Fanfare binasında yer alan, geleneksel bar yemekleri ve bira sunan rahat kafe. Yerel halkla tanışma, samimi sohbetler ve Hollanda pub kültürü.",
        "description_en": "A comfortable cafe in De Fanfare building serving traditional bar food and beer. Meeting locals, intimate conversations, and Dutch pub culture."
    },
    "Rondvaart Zuideinde": {
        "description": "Giethoorn'un güney bölgesinden başlayan tekne turları, daha az kalabalık rotalarla köyü keşfetme fırsatı. Sessiz kanallar, doğa ve huzur.",
        "description_en": "Boat tours starting from Giethoorn's southern area, opportunity to explore village with less crowded routes. Quiet canals, nature, and peace."
    },
    "De Witte Eend": {
        "description": "Kanal kenarında şirin bir lokasyon, pannenkoeken ve kahve ile ünlü aile işletmesi kafe. Çocuk dostu, samimi ve sıcak atmosfer.",
        "description_en": "A cute location by the canal, family-run cafe famous for pancakes and coffee. Child-friendly, intimate, and warm atmosphere."
    },
    "Giethoorn Punterbuurt": {
        "description": "Geleneksel Hollanda düz dipli teknelerinin (punter) sergilendiği ve kiralandığı bölge. Otantik deneyim, el işçiliği tekneler ve kültürel miras.",
        "description_en": "An area where traditional Dutch flat-bottomed boats (punter) are displayed and rented. Authentic experience, handcrafted boats, and cultural heritage."
    },
    "Cornelisgracht": {
        "description": "Giethoorn'un en eski kanallarından biri, tarihi sazlık evler ve bakımlı bahçelerle çevrili. Sessiz ve romantik, keşfedilmeyi bekleyen köşe.",
        "description_en": "One of Giethoorn's oldest canals, surrounded by historic thatched houses and well-maintained gardens. Quiet and romantic, a corner waiting to be discovered."
    },
    "Paviljoen De Witte Hoeve": {
        "description": "De Witte Hoeve'nin açık hava pavyonu, yaz aylarında kahve ve hafif yemekler için ideal. Bahçe manzarası, doğa sesleri ve rahatlatıcı mola.",
        "description_en": "De Witte Hoeve's outdoor pavilion, ideal for coffee and light meals in summer. Garden views, nature sounds, and relaxing break."
    },
    "De Piccardt": {
        "description": "Hollanda kahvaltısı ve öğle yemeği sunan, yerel ürünler ve ev yapımı tariflerle çalışan kafe. Taze ekmek, peynir ve Hollanda tarzı brunch.",
        "description_en": "A cafe serving Dutch breakfast and lunch, working with local products and homemade recipes. Fresh bread, cheese, and Dutch-style brunch."
    },
    "Giethoorn Supermarket Plus": {
        "description": "Köyün büyük süpermarketi, çeşitli gıda ürünleri ve günlük ihtiyaçlar için alışveriş noktası. Piknik malzemeleri, içecekler ve atıştırmalıklar.",
        "description_en": "The village's larger supermarket, shopping point for various food products and daily needs. Picnic supplies, drinks, and snacks."
    },
    "Bed & Breakfast Giethoorn": {
        "description": "Geleneksel sazlık çatılı evde konaklama deneyimi, Hollanda köy yaşamını yaşama fırsatı. Ev yapımı kahvaltı, kanal manzarası ve samimi konaklama.",
        "description_en": "Accommodation experience in traditional thatched house, opportunity to live Dutch village life. Homemade breakfast, canal views, and intimate lodging."
    },
    "Chaletpark Kroondomein": {
        "description": "Doğa içinde şale tarzı konaklama tesisi, aileler ve gruplar için tatil köyü. Özel bahçeler, bisiklet kiralama ve huzurlu tatil.",
        "description_en": "A chalet-style accommodation facility in nature, resort for families and groups. Private gardens, bike rental, and peaceful vacation."
    },
    "Café-Restaurant De Rietstulp": {
        "description": "Sazlık çatılı ikonik binada, Hollanda ev yemekleri ve yerel içecekler sunan restoran. Stamppot, bitterballen ve geleneksel damak zevkleri.",
        "description_en": "A restaurant in iconic thatched building serving Dutch home cooking and local drinks. Stamppot, bitterballen, and traditional tastes."
    },
    "Black Sheep Hostel": {
        "description": "Bütçe dostu konaklama seçeneği, genç gezginler ve backpacker'lar için ideal. Ortak alanlar, sosyal atmosfer ve uygun fiyat.",
        "description_en": "Budget-friendly accommodation option, ideal for young travelers and backpackers. Common areas, social atmosphere, and affordable price."
    },
    "Giethoorn Boat": {
        "description": "Elektrikli tekne kiralama hizmeti, kanalları kendi başınıza keşfetme özgürlüğü. Ehliyetsiz kullanım, sessiz motor ve çevre dostu deneyim.",
        "description_en": "Electric boat rental service, freedom to explore canals on your own. No license required, quiet motor, and eco-friendly experience."
    }
}

filepath = 'assets/cities/giethoorn.json'
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

print(f"\n✅ Manually enriched {count} items (Giethoorn Batch 1).")
