import json

# Manual enrichment data (Giethoorn Batch 2: 40 items)
updates = {
    "Uitkijktoren Woldberg": {
        "description": "Weerribben-Wieden Milli Parkı'nın panoramik manzarasını sunan ahşap gözetleme kulesi. Sulak alanlar, sazlıklar ve yaban hayatını kuşbakışı izleme fırsatı.",
        "description_en": "A wooden observation tower offering panoramic views of Weerribben-Wieden National Park. Opportunity to view wetlands, reeds, and wildlife from bird's eye."
    },
    "Zuideindigerwijde": {
        "description": "Giethoorn'un güney kesimindeki geniş göl, yelken, kano ve su sporları için ideal. Sakin sular, doğa manzaraları ve açık hava aktiviteleri.",
        "description_en": "A wide lake in southern Giethoorn, ideal for sailing, canoeing, and water sports. Calm waters, nature views, and outdoor activities."
    },
    "Aquarium Giethoorn": {
        "description": "Hollanda'nın tatlı su balıklarını ve yerli su yaşamını sergileyen küçük ama eğitici akvaryum. Aileler ve çocuklar için interaktif öğrenme deneyimi.",
        "description_en": "A small but educational aquarium exhibiting freshwater fish and local aquatic life of the Netherlands. Interactive learning experience for families and children."
    },
    "Shell Gallery Gloria Maris": {
        "description": "Dünyanın dört bir yanından toplanan deniz kabuklarını sergileyen benzersiz koleksiyon. Nadir türler, fosiller ve deniz biyolojisi hakkında bilgi.",
        "description_en": "A unique collection exhibiting seashells collected from around the world. Rare species, fossils, and information about marine biology."
    },
    "Pottenbakkerij Rhoda": {
        "description": "El yapımı seramikler ve çömlekçilik atölyesi sunan geleneksel zanaat dükkanı. Kendi çanak çömleğinizi yapma deneyimi ve benzersiz hediyelikler.",
        "description_en": "A traditional craft shop offering handmade ceramics and pottery workshops. Experience of making your own pottery and unique souvenirs."
    },
    "De Kruumte": {
        "description": "Giethoorn'da kahve, pasta ve hafif öğle yemeği sunan şirin kafe. Bahçe oturma alanı, ev yapımı tatlılar ve samimi atmosfer.",
        "description_en": "A cute cafe in Giethoorn serving coffee, pastries, and light lunch. Garden seating area, homemade desserts, and intimate atmosphere."
    },
    "Giethoorn High Bridge": {
        "description": "Köyün en yüksek ahşap köprüsü, tekne trafiğine izin veren yapısıyla kanal manzarası sunan nokta. Fotoğraf çekmek için ideal konum.",
        "description_en": "The village's highest wooden bridge, a point offering canal views with structure allowing boat traffic. Ideal location for photography."
    },
    "Noorderind": {
        "description": "Giethoorn'un kuzey kesimi, daha sakin ve daha az turistik bölge. Otantik sazlık evler, dar kanallar ve huzurlu köy yaşamı.",
        "description_en": "Northern section of Giethoorn, a quieter and less touristy area. Authentic thatched houses, narrow canals, and peaceful village life."
    },
    "Beulakerwijde Viewpoint": {
        "description": "Beulakerwijde gölünün manzarasını sunan gözlem noktası. Su kuşları, gün batımı ve doğa fotoğrafçılığı için ideal lokasyon.",
        "description_en": "An observation point offering views of Beulakerwijde lake. Ideal location for waterbirds, sunset, and nature photography."
    },
    "De Aardigheit": {
        "description": "Hollanda kahvaltısı ve öğle yemeği sunan, taze ürünler ve ev yapımı tariflerle çalışan kafe. Pannenkoeken, sandviçler ve sıcak içecekler.",
        "description_en": "A cafe serving Dutch breakfast and lunch, working with fresh products and homemade recipes. Pancakes, sandwiches, and hot drinks."
    },
    "Restaurant De Dames van de Jonge": {
        "description": "Modern Hollanda mutfağını geleneksel tariflerle harmanlayan şık restoran. Mevsimlik menü, yaratıcı sunumlar ve romantik akşam yemekleri.",
        "description_en": "A stylish restaurant blending modern Dutch cuisine with traditional recipes. Seasonal menu, creative presentations, and romantic dinners."
    },
    "De Grachthof Lounge": {
        "description": "De Grachthof'un lounge bölümü, kokteyller ve özel içecekler sunan rahat bar. Akşam keyfi, kanal manzarası ve sofistike atmosfer.",
        "description_en": "De Grachthof's lounge section, a comfortable bar serving cocktails and special drinks. Evening enjoyment, canal views, and sophisticated atmosphere."
    },
    "Ijs & Zo": {
        "description": "Artisan dondurma ve taze sorbeler sunan butik dondurma dükkanı. Doğal malzemeler, mevsimlik tatlar ve Hollanda usulü dondurma.",
        "description_en": "A boutique ice cream shop serving artisan ice cream and fresh sorbets. Natural ingredients, seasonal flavors, and Dutch-style ice cream."
    },
    "Restaurant De Pergola": {
        "description": "Akdeniz esintili menüsü ve açık hava terasıyla dikkat çeken restoran. Pizza, salata ve hafif yemekler, yaz akşamları için ideal.",
        "description_en": "A restaurant notable for Mediterranean-inspired menu and outdoor terrace. Pizza, salads, and light meals, ideal for summer evenings."
    },
    "Piccola Roma": {
        "description": "Otantik İtalyan mutfağı sunan, pizza ve makarna çeşitleriyle sevilen restoran. Aile dostu ortam, lezzetli porsiyonlar ve uygun fiyat.",
        "description_en": "A restaurant serving authentic Italian cuisine, loved for pizza and pasta varieties. Family-friendly environment, delicious portions, and affordable price."
    },
    "Bovenmeester": {
        "description": "Eski okul binasında konumlanan, Hollanda home cooking ve brunch sunan kafe-restoran. Nostaljik dekor, yerel malzemeler ve samimi atmosfer.",
        "description_en": "A cafe-restaurant in old school building serving Dutch home cooking and brunch. Nostalgic decor, local ingredients, and intimate atmosphere."
    },
    "Grand Café De Eendracht": {
        "description": "Geniş terasıyla Hollanda pub yemekleri ve bira sunan sosyal buluşma noktası. Canlı atmosfer, spor etkinlikleri ve yerel halk.",
        "description_en": "A social meeting point with large terrace serving Dutch pub food and beer. Lively atmosphere, sports events, and locals."
    },
    "Snackpoint Giethoorn": {
        "description": "Hollanda fast-food klasikleri: patat, kroket ve frikandel sunan pratik atıştırma noktası. Hızlı servis, uygun fiyat ve doyurucu lezzetler.",
        "description_en": "Practical snack point serving Dutch fast-food classics: fries, croquettes, and frikandel. Quick service, affordable price, and satisfying flavors."
    },
    "Bakkerij Toet": {
        "description": "Taze ekmek, pasta ve Hollanda tatlıları sunan geleneksel fırın. Stroopwafel, oliebollen ve ev yapımı lezzetlerle kahvaltı durağı.",
        "description_en": "Traditional bakery serving fresh bread, pastries, and Dutch sweets. Breakfast stop with stroopwafel, oliebollen, and homemade delights."
    },
    "Het Proeflokaal": {
        "description": "Yerel bira, peynir ve Hollanda lezzetleri tadabileceğiniz tadım mekanı. Hollanda gastronomisini keşfetmek için eğitici ve lezzetli deneyim.",
        "description_en": "A tasting venue where you can taste local beer, cheese, and Dutch flavors. An educational and delicious experience to discover Dutch gastronomy."
    },
    "Smit Giethoorn Catering": {
        "description": "Piknik sepetleri, tekne yemekleri ve özel etkinlikler için catering hizmeti. Romantik tekne gezisi, gurme piknik ve özel anlar.",
        "description_en": "Catering service for picnic baskets, boat meals, and special events. Romantic boat trip, gourmet picnic, and special moments."
    },
    "Restaurant De Gele Lis": {
        "description": "Kanal kenarında konumlanan, Hollanda deniz ürünleri ve geleneksel yemekler sunan restoran. Taze balık, yerel tarifler ve manzaralı yemek.",
        "description_en": "A restaurant by the canal serving Dutch seafood and traditional dishes. Fresh fish, local recipes, and dining with views."
    },
    "Zuivelhoeve Steenwijk": {
        "description": "Hollanda peynirleri, süt ürünleri ve çiftlik lezzetlerinin satıldığı yerel dükkan. Gouda, Edam ve bölgesel peynir çeşitleri.",
        "description_en": "A local shop selling Dutch cheeses, dairy products, and farm delights. Gouda, Edam, and regional cheese varieties."
    },
    "De Bovenstreek": {
        "description": "Giethoorn'un üst bölgesi, daha geniş kanallar ve çiftlik arazileriyle karakterize edilen alan. Bisiklet turu için ideal, kırsal manzaralar.",
        "description_en": "Upper part of Giethoorn, an area characterized by wider canals and farmlands. Ideal for bike tour, rural scenery."
    },
    "Kiersche Wijde": {
        "description": "Weerribben-Wieden bölgesindeki doğal göl, kuş gözlemciliği ve kano için popüler. Turna kuşları, balıkçıl ve su yüzeyi bitkiler.",
        "description_en": "A natural lake in Weerribben-Wieden region, popular for bird watching and canoeing. Cranes, herons, and water surface plants."
    },
    "Tjasker Kalenberg": {
        "description": "Kalenberg köyündeki geleneksel Hollanda yel değirmeni, küçük boyutu ve tarihi işleviyle ilgi çekici. Su pompalama sistemi ve Hollanda mühendisliği.",
        "description_en": "Traditional Dutch windmill in Kalenberg village, interesting with small size and historic function. Water pumping system and Dutch engineering."
    },
    "Belt-Schutsloot": {
        "description": "Giethoorn yakınında, kanallar ve sazlık evlerle dolu pitoresk köy. Daha az turistik, otantik Hollanda köy yaşamı deneyimi.",
        "description_en": "A picturesque village near Giethoorn full of canals and thatched houses. Less touristy, authentic Dutch village life experience."
    },
    "Scheerwolde": {
        "description": "Bölgedeki küçük tarım köyü, geleneksel çiftlikler ve kırsal yaşam. Bisiklet rotalarında durak, huzurlu Hollanda kırsalı.",
        "description_en": "A small agricultural village in the area with traditional farms and rural life. Stop on bike routes, peaceful Dutch countryside."
    },
    "Muggenbeet": {
        "description": "Giethoorn ile Weerribben arasında konumlanan küçük yerleşim, doğa parkına geçiş noktası. Sakin kanallar, yeşil alanlar ve kuş gözlemi.",
        "description_en": "A small settlement between Giethoorn and Weerribben, gateway to nature park. Quiet canals, green areas, and bird watching."
    },
    "Pontje Jonen": {
        "description": "Kanal karşısına geçmek için küçük feribot, geleneksel ulaşım deneyimi. Bisikletçiler ve yayalar için pratik, yerel yaşamın parçası.",
        "description_en": "A small ferry to cross the canal, traditional transportation experience. Practical for cyclists and pedestrians, part of local life."
    },
    "Waterreijk Weerribben Wieden": {
        "description": "Milli parkın su yollarını keşfetmek için organize turlar ve aktiviteler. Rehberli kano turları, doğa eğitimi ve ekolojik farkındalık.",
        "description_en": "Organized tours and activities to explore national park's waterways. Guided canoe tours, nature education, and ecological awareness."
    },
    "Beulakerwijde": {
        "description": "Giethoorn yakınındaki büyük göl, yelken, kürek ve su sporları için popüler. Yaz aylarında canlı, kış aylarında buz pateni alanı.",
        "description_en": "A large lake near Giethoorn, popular for sailing, rowing, and water sports. Lively in summer, ice skating area in winter."
    },
    "Belterwijde": {
        "description": "Beulakerwijde'ye bağlanan geniş göl alanı, su kuşları ve doğal yaşam için önemli habitat. Sessiz koylar, sazlıklar ve doğa fotoğrafçılığı.",
        "description_en": "A wide lake area connecting to Beulakerwijde, important habitat for waterbirds and wildlife. Quiet coves, reeds, and nature photography."
    },
    "Gemaal A.F. Stroink": {
        "description": "Tarihi pompa istasyonu, Hollanda su mühendisliğinin önemli örneği. Su yönetimi tarihi, antik makineler ve mühendislik merakı.",
        "description_en": "Historic pumping station, an important example of Dutch water engineering. Water management history, antique machines, and engineering curiosity."
    },
    "Vollenhove": {
        "description": "Eski Zuiderzee kıyısındaki tarihi kasaba, balıkçı geçmişi ve ortaçağ mimarisiyle. Marinaları, restore edilmiş evleri ve sessiz atmosferi.",
        "description_en": "A historic town on the old Zuiderzee coast with fishing past and medieval architecture. Marinas, restored houses, and quiet atmosphere."
    },
    "Ossenzijl": {
        "description": "Weerribben-Wieden'in kuzey kapısı, doğa parkına erişim için alternatif giriş noktası. Kano kiralama, yürüyüş başlangıcı ve doğa merkezi.",
        "description_en": "Northern gateway of Weerribben-Wieden, alternative entry point for nature park access. Canoe rental, hiking start, and nature center."
    },
    "Kalenbergergracht": {
        "description": "Kalenberg köyünü geçen tarihi kanal, sazlık evler ve ahşap köprülerle. Tekne turu için ideal, pitoresk Hollanda manzarası.",
        "description_en": "A historic canal passing through Kalenberg village with thatched houses and wooden bridges. Ideal for boat tour, picturesque Dutch scenery."
    },
    "Zwartsluis": {
        "description": "IJsselmeer'e açılan tarihi liman kasabası, yat limanı ve balıkçı geçmişiyle. Kanal evleri, köprüler ve su üzerindeki yaşam.",
        "description_en": "A historic port town opening to IJsselmeer with yacht marina and fishing past. Canal houses, bridges, and life on the water."
    },
    "Museum Schoonewelle": {
        "description": "Yerel tarih ve gelenekleri sergileyen küçük köy müzesi. Eski çiftlik aletleri, balıkçılık ekipmanları ve bölge kültürü.",
        "description_en": "A small village museum exhibiting local history and traditions. Old farm tools, fishing equipment, and regional culture."
    },
    "Sint-Jansklooster": {
        "description": "Ortaçağ manastır kalıntıları üzerine kurulmuş köy, tarihi kilisesi ve huzurlu atmosferiyle. Bisiklet rotalarında durak, kültürel miras.",
        "description_en": "A village built on medieval monastery ruins with historic church and peaceful atmosphere. Stop on bike routes, cultural heritage."
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

print(f"\n✅ Manually enriched {count} items (Giethoorn Batch 2).")
