import json

# Manual enrichment data (Cappadocia - ALL 33 items)
updates = {
    "Crowne Plaza Nevsehir": {
        "description": "Nevşehir merkezinde modern konaklama imkanı sunan lüks otel. İş seyahatleri ve Kapadokya keşifleri için konforlu bir üs.",
        "description_en": "Luxury hotel offering modern accommodation in Nevşehir center. Comfortable base for business trips and Cappadocia explorations."
    },
    "Forum Kapadokya": {
        "description": "Nevşehir'in en büyük alışveriş ve yaşam merkezi. Sinema, mağazalar, restoranlar ve yerel markaların buluşma noktası.",
        "description_en": "Nevşehir's largest shopping and lifestyle center. Meeting point for cinema, shops, restaurants, and local brands."
    },
    "Nevsehir Museum": {
        "description": "Kapadokya bölgesinin arkeolojik ve etnografik eserlerini sergileyen müze. Neolitik dönemden Osmanlı'ya tarih yolculuğu.",
        "description_en": "Museum exhibiting archaeological and ethnographic artifacts of Cappadocia region. History journey from Neolithic to Ottoman."
    },
    "Urgup Hamam": {
        "description": "Ürgüp merkezde tarihi Türk hamamı deneyimi. Geleneksel kese, köpük masajı ve rahatlatıcı otantik atmosfer.",
        "description_en": "Historic Turkish bath experience in Ürgüp center. Traditional scrub, foam massage, and relaxing authentic atmosphere."
    },
    "Keles Cave Cafe": {
        "description": "Mağara içine oyulmuş otantik kafe, vadi manzarasına hakim. Türk kahvesi, nargile ve yerel şarap tadımı için ideal.",
        "description_en": "Authentic cafe carved into cave, overlooking valley views. Ideal for Turkish coffee, hookah, and local wine tasting."
    },
    "Uchisar Kaya Otel": {
        "description": "Güvercinlik Vadisi manzaralı, kayalara oyulmuş ilk otellerden. Panoramik teras, yüzme havuzu ve gün batımı keyfi.",
        "description_en": "One of the first hotels carved into rocks, with Pigeon Valley views. Panoramic terrace, swimming pool, and sunset joy."
    },
    "Taskonaklar": {
        "description": "Uçhisar'da lüks butik otel, her odası özel tasarımlı mağara süitler. Balayı çiftleri ve sakinlik arayanlar için romantik.",
        "description_en": "Luxury boutique hotel in Uçhisar, each room specially designed cave suites. Romantic for honeymooners and peace seekers."
    },
    "Petra Inn": {
        "description": "Uçhisar kalesi eteklerinde restore edilmiş tarihi konak. Geleneksel mimari, modern konfor ve büyüleyici teras manzarası.",
        "description_en": "Restored historic mansion at foot of Uçhisar castle. Traditional architecture, modern comfort, and enchanting terrace view."
    },
    "Ansia Hotel": {
        "description": "Peri bacaları manzarasına uyanacağınız konforlu mağara otel. Balonları izlemek için ideal teras ve sıcak misafirperverlik.",
        "description_en": "Comfortable cave hotel where you wake up to fairy chimney views. Ideal terrace for watching balloons and warm hospitality."
    },
    "Koza Cave Hotel": {
        "description": "Instagram fenomeni terasıyla ünlü, sürdürülebilir butik otel. Yerel halılarla süslü teras, organik kahvaltı ve şık dekor.",
        "description_en": "Sustainable boutique hotel famous for its Instagram phenomenon terrace. Terrace adorned with local rugs, organic breakfast, and chic decor."
    },
    "Ayvali Village": {
        "description": "Ürgüp yakınlarında turist kalabalığından uzak, otantik Kapadokya köyü. Taş evler, kayısı bahçeleri ve huzurlu yaşam.",
        "description_en": "Authentic Cappadocia village away from tourist crowds near Ürgüp. Stone houses, apricot orchards, and peaceful life."
    },
    "Uchisar Old Square": {
        "description": "Uçhisar köyünün tarihi meydanı, eski taş dükkanlar ve çeşme. Hediyelik eşya tezgahları, köy kahvesi ve doku.",
        "description_en": "Historic square of Uçhisar village, old stone shops, and fountain. Souvenir stalls, village coffeehouse, and texture."
    },
    "Temenni Library": {
        "description": "Ürgüp Temenni Tepesi'nde tarihi kütüphane binası, şimdi sosyal tesis. Eşsiz Ürgüp manzarası ve çay molası.",
        "description_en": "Historic library building on Ürgüp Temenni Hill, now social facility. Unique Ürgüp view and tea break."
    },
    "Urgup Big Mosque": {
        "description": "Ürgüp'ün merkezindeki en büyük cami, modern ve Selçuklu mimarisi sentezi. Geniş avlu, huzur ve ibadet.",
        "description_en": "Largest mosque in Ürgüp center, synthesis of modern and Seljuk architecture. Spacious courtyard, peace, and worship."
    },
    "Damsa Dam": {
        "description": "Ürgüp yakınlarında piknik ve mesire alanı, baraj gölü. Hafta sonu yerel halkın kaçış noktası, doğa ve serinlik.",
        "description_en": "Picnic and recreation area near Ürgüp, dam lake. Weekend escape spot for locals, nature, and coolness."
    },
    "Hala Sultan Tomb": {
        "description": "Bölgedeki önemli dini ziyaret noktalarından biri, manevi atmosfer. Selçuklu dönemi türbe mimarisi ve sessizlik.",
        "description_en": "One of the important religious pilgrimage sites in region, spiritual atmosphere. Seljuk era tomb architecture and silence."
    },
    "Kadi Castle": {
        "description": "Ürgüp'te 'Kadı Kalesi' olarak bilinen tarihi kaya yerleşimi. Savunma amaçlı tüneller, odalar ve panoramik manzara.",
        "description_en": "Historic rock settlement known as 'Kadi Castle' in Ürgüp. Defensive tunnels, rooms, and panoramic view."
    },
    "Alti Kapi Tomb": {
        "description": "Ürgüp'te altı pencereli, Selçuklu komutanına ait anıt mezar. 12. yüzyıl taş işçiliği ve tarihi miras.",
        "description_en": "Monumental tomb with six windows in Ürgüp, belonging to Seljuk commander. 12th-century stonework and historic heritage."
    },
    "Goreme Roman Castle": {
        "description": "Göreme'de Roma döneminden kalma kaya oyma kale ve mezarlar. Az bilinen tarihi nokta, vadi manzarası ve keşif.",
        "description_en": "Rock-cut castle and tombs from Roman period in Göreme. Little-known historic spot, valley views, and discovery."
    },
    "Bezirhane Goreme": {
        "description": "Eskiden bezir yağı (keten tohumu) üretilen tarihi kaya mekan. Şimdi kültürel etkinlikler ve konserler için kullanılıyor.",
        "description_en": "Historic rock venue formerly used for producing linseed oil. Now used for cultural events and concerts."
    },
    "Ayan Yorgi Church": {
        "description": "Avanos yakınlarında kayaya oyulmuş eski Rum kilisesi. Solmuş freskler, tarihi atmosfer ve sessiz inanç mirası.",
        "description_en": "Old Greek church carved into rock near Avanos. Faded frescoes, historic atmosphere, and silent heritage of faith."
    },
    "Uzumlu Church": {
        "description": "Kızılçukur Vadisi'nde, üzüm salkımı freskleriyle ünlü kilise. St. Nichitas'a adanmış, doğa yürüyüşü rotasında gizli hazine.",
        "description_en": "Church famous for grape cluster frescoes in Red Valley. Dedicated to St. Nichitas, hidden treasure on hiking route."
    },
    "Cambazli Church": {
        "description": "Ortahisar yakınlarında, cambaz (ip cambazı) freskleri içermese de bu adla bilinen yapı. Haç planlı mimari ve tarihi doku.",
        "description_en": "Structure near Ortahisar known by this name covering acrobat meanings. Cross-plan architecture and historic texture."
    },
    "Sarica Church": {
        "description": "Mustafapaşa yakınlarında restore edilmiş, kubbeli kaya kilisesi. Erken dönem Hıristiyanlık sanatı ve manastır yaşamı izleri.",
        "description_en": "Restored domed rock church near Mustafapaşa. Traces of Early Christianity art and monastic life."
    },
    "St. Basil Mustafapasa": {
        "description": "Sinasos (Mustafapaşa) girişinde, vadiye bakan aziz şapeli. Taş merdivenlerle inilen, mistik ve korunaklı ibadethane.",
        "description_en": "Saint chapel overlooking valley at entrance of Sinasos (Mustafapaşa). Mystic and sheltered place of worship descended by stone stairs."
    },
    "Mara Monastery": {
        "description": "Ürgüp yakınlarında, nehir kenarında tarihi manastır kalıntıları. Sessiz, doğa ile iç içe ve keşfedilmeyi bekleyen tarih.",
        "description_en": "Historic monastery ruins near Ürgüp, by the river. Silent, intertwined with nature, and history waiting to be discovered."
    },
    "Gomeda Bridge": {
        "description": "Gomeda Vadisi girişinde tarihi taş köprü. Vadi yürüyüşlerinin başlangıç noktası, fotoğrafçılık ve pastoral manzara.",
        "description_en": "Historic stone bridge at entrance of Gomeda Valley. Starting point for valley hikes, photography, and pastoral scenery."
    },
    "Ayvasil Church": {
        "description": "Göreme ile Çavuşin arasında, yol kenarındaki kaya kilise. Aziz Basil'e adanmış, mezar nişleri ve fresk kalıntıları.",
        "description_en": "Rock church by the road between Göreme and Çavuşin. Dedicated to St. Basil, burial niches, and fresco remains."
    },
    "Hacli Church": {
        "description": "Güllüdere Vadisi tepesinde, tavanındaki büyük haç kabartmasıyla ünlü. Zorlu tırmanış sonrası ödül niteliğinde manzara.",
        "description_en": "Famous for large cross relief on ceiling, atop Rose Valley. View rewarding after a challenging climb."
    },
    "Three Crosses Church": {
        "description": "Güllüdere'de tavanında üç haç oyması bulunan kilise. İkonoklastik dönem süslemeleri, fresksiz ama etkileyici mimari.",
        "description_en": "Church with three cross carvings on ceiling in Rose Valley. Iconoclastic period decorations, frescoless but impressive architecture."
    },
    "Joachim Anna Church": {
        "description": "Meryem Ana'nın ebeveynlerine adanmış narin şapel. Kızılçukur yürüyüşünde karşılaşılan, hüzünlü ve güzel bir yapı.",
        "description_en": "Delicate chapel dedicated to parents of Virgin Mary. Sad and beautiful structure encountered on Red Valley hike."
    },
    "Direkli Church": {
        "description": "Ihlara Vadisi'nin en büyük kiliselerinden, yüksek sütunlarıyla (direk) ünlü. Manastır kompleksi ve nehir sesi.",
        "description_en": "One of largest churches in Ihlara Valley, famous for tall columns (pillars). Monastery complex and sound of river."
    },
    "Bezirhane Ihlara": {
        "description": "Ihlara köyü girişinde, eskiden yağhane olarak kullanılan devasa kaya oyuğu. Yöresel mimari ve endüstriyel tarih.",
        "description_en": "Massive rock cavity at entrance of Ihlara village, formerly used as oil mill. Local architecture and industrial history."
    }
}

filepath = 'assets/cities/kapadokya.json'
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

print(f"\n✅ Manually enriched {count} items (Cappadocia - COMPLETE).")
