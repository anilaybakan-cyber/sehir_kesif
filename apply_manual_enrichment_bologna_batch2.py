import json

# Manual enrichment data (Bologna Batch 2: 40 items)
updates = {
    "Orto Botanico di Bologna": {
        "description": "Dünyanın en eski botanik bahçelerinden biri, 1568'den beri bitki araştırmaları için hizmet veriyor. Nadir türler, sera ve üniversite mirası.",
        "description_en": "One of the world's oldest botanical gardens, serving plant research since 1568. Rare species, greenhouse, and university heritage."
    },
    "Villa Spada": {
        "description": "18. yüzyıldan kalma aristokrat villası, geniş İtalyan bahçesi ve teras manzarasıyla. Düğünler, etkinlikler ve romantik kaçış için ideal.",
        "description_en": "18th-century aristocratic villa with large Italian garden and terrace views. Ideal for weddings, events, and romantic getaway."
    },
    "Bagni di Mario (conserva di Valverde)": {
        "description": "Rönesans döneminden kalma yeraltı su deposu, Bologna'nın antik su sisteminin mühendislik harikası. Rehberli turlar ve tarihi keşif.",
        "description_en": "Underground water cistern from Renaissance period, engineering marvel of Bologna's ancient water system. Guided tours and historic discovery."
    },
    "Museo Ebraico": {
        "description": "Bologna ve Emilia-Romagna Yahudi toplumunun tarihini ve kültürünü sergileyen müze. Holokost anıları, dini eserler ve topluluk mirası.",
        "description_en": "Museum exhibiting history and culture of Bologna and Emilia-Romagna Jewish community. Holocaust memories, religious artifacts, and community heritage."
    },
    "Museo Morandi": {
        "description": "20. yüzyıl İtalyan ressamı Giorgio Morandi'nin eserlerini sergileyen müze. Natürmort resimleri, gravürler ve minimalist sanat anlayışı.",
        "description_en": "Museum exhibiting works of 20th-century Italian painter Giorgio Morandi. Still-life paintings, engravings, and minimalist art approach."
    },
    "Palazzo Pepoli Campogrande": {
        "description": "Barok dönemi sarayı, fresk tavanlar ve dönem mobilyalarıyla. 17. yüzyıl aristokrat yaşamı, resim koleksiyonu ve tarihi atmosfer.",
        "description_en": "Baroque-period palace with frescoed ceilings and period furniture. 17th-century aristocratic life, painting collection, and historic atmosphere."
    },
    "Museo del Patrimonio Industriale": {
        "description": "Bologna'nın endüstriyel mirasını ve teknolojik evrimini anlatan müze. Tekstil makineleri, otomotiv ve şehrin üretim geçmişi.",
        "description_en": "Museum telling Bologna's industrial heritage and technological evolution. Textile machines, automotive, and city's manufacturing past."
    },
    "Accademia Filarmonica": {
        "description": "Mozart'ın da üye olduğu tarihi müzik akademisi, konserlere ve müzik eğitimine ev sahipliği yapıyor. Barok tavan, müzik tarihi ve kültürel miras.",
        "description_en": "Historic music academy where Mozart was also a member, hosting concerts and music education. Baroque ceiling, music history, and cultural heritage."
    },
    "Palazzo Belloni": {
        "description": "Rönesans sarayı, özel sergilere ve kültürel etkinliklere ev sahipliği yapıyor. Tarihi mimari, sanat gösterileri ve elite atmosfer.",
        "description_en": "Renaissance palace hosting private exhibitions and cultural events. Historic architecture, art shows, and elite atmosphere."
    },
    "Museo d'Arte Davia Bargellini": {
        "description": "Dekoratif sanatlar ve uygulamalı sanatlar müzesi, mobilya, seramik ve tekstil koleksiyonu. 18. yüzyıl İtalyan ev kültürü.",
        "description_en": "Decorative and applied arts museum with furniture, ceramics, and textile collection. 18th-century Italian home culture."
    },
    "Collezioni Comunali d'Arte": {
        "description": "Palazzo d'Accursio'daki şehir sanat koleksiyonu, Rönesans'tan modern döneme resimler. Belediye binasında sanat hazineleri.",
        "description_en": "City art collection in Palazzo d'Accursio with paintings from Renaissance to modern period. Art treasures in municipal building."
    },
    "Museo della Comunicazione": {
        "description": "İletişim tarihini kutlayan müze, radyo, televizyon ve telekomünikasyon. Nostalji, teknoloji evrimi ve medya kültürü.",
        "description_en": "Museum celebrating communication history with radio, television, and telecommunications. Nostalgia, technology evolution, and media culture."
    },
    "Casa Carducci": {
        "description": "Nobel ödüllü İtalyan şair Giosuè Carducci'nin ev-müzesi. El yazmaları, kişisel eşyalar ve edebiyat mirası.",
        "description_en": "House-museum of Nobel Prize-winning Italian poet Giosuè Carducci. Manuscripts, personal belongings, and literary heritage."
    },
    "Museo del Tessuto e della Tappezzeria": {
        "description": "Tekstil ve döşemecilik tarihini sergileyen niş müze. Antik kumaşlar, dokuma teknikleri ve moda evrimi.",
        "description_en": "Niche museum exhibiting textile and upholstery history. Antique fabrics, weaving techniques, and fashion evolution."
    },
    "Museo della Beata Vergine di San Luca": {
        "description": "San Luca Bazilikası'ndaki dini sanat ve hac kültürünü sergileyen müze. İkonik Madonna, hac gelenekleri ve manevi miras.",
        "description_en": "Museum exhibiting religious art and pilgrimage culture at San Luca Basilica. Iconic Madonna, pilgrimage traditions, and spiritual heritage."
    },
    "Museo di Zoologia": {
        "description": "Üniversite zooloji koleksiyonu, hayvan türleri ve doğal tarih. Aileler ve bilim meraklıları için eğitici deneyim.",
        "description_en": "University zoology collection with animal species and natural history. Educational experience for families and science enthusiasts."
    },
    "Museo della Sanità": {
        "description": "Tıp ve sağlık tarihini sergileyen müze, antik cerrahi aletler ve ilaç koleksiyonu. Sağlık bilimi evrimi.",
        "description_en": "Museum exhibiting medical and health history with antique surgical instruments and pharmaceutical collection. Health science evolution."
    },
    "Parma Cathedral": {
        "description": "Parma'daki Romanesk katedral, Correggio'nun meşhur kubbe freskiyle. İtalyan dini mimarisi ve Rönesans sanatı şaheseri.",
        "description_en": "Romanesque cathedral in Parma with Correggio's famous dome fresco. Italian religious architecture and Renaissance art masterpiece."
    },
    "Ravenna Mosaics (San Vitale)": {
        "description": "UNESCO korumasındaki Bizans mozaikleri, Ravenna'nın altın çağına tanıklık. San Vitale Bazilikası ve Justinyen dönemi sanat hazineleri.",
        "description_en": "UNESCO-protected Byzantine mosaics witnessing Ravenna's golden age. San Vitale Basilica and Justinian-period art treasures."
    },
    "Labirinto della Masone": {
        "description": "Dünyanın en büyük bambu labirenti, sanat galerisi ve şarap mahzeniyle. Franco Maria Ricci'nin eseri, sıra dışı kültürel deneyim.",
        "description_en": "World's largest bamboo labyrinth with art gallery and wine cellar. Franco Maria Ricci's creation, extraordinary cultural experience."
    },
    "Parma Ham Factory Tour": {
        "description": "Prosciutto di Parma üretim tesisi turu, geleneksel olgunlaştırma sürecini keşfedin. Tadım, aile çiftlikleri ve gurme yolculuk.",
        "description_en": "Prosciutto di Parma production facility tour, discover traditional aging process. Tasting, family farms, and gourmet journey."
    },
    "Parmigiano Reggiano Dairy": {
        "description": "İtalya'nın en ünlü peynirinin üretildiği mandıra turu. Sabah erken ziyaret, peynir yapımı ve tadım deneyimi.",
        "description_en": "Dairy tour where Italy's most famous cheese is produced. Early morning visit, cheese making, and tasting experience."
    },
    "Brisighella": {
        "description": "Romagna'daki ortaçağ kasabası, saat kulesi, UNESCO korumalı sokakları ve zeytinyağıyla ünlü. Tepedeki kale ve romantik atmosfer.",
        "description_en": "Medieval town in Romagna famous for clock tower, UNESCO-protected streets, and olive oil. Hilltop castle and romantic atmosphere."
    },
    "Comacchio": {
        "description": "Po Deltası'ndaki 'Küçük Venedik', kanal köprüleri ve yılan balığı lezzetleriyle. Balıkçı geleneği, lagün manzaraları ve doğa.",
        "description_en": "Po Delta's 'Little Venice' with canal bridges and eel delicacies. Fishing tradition, lagoon views, and nature."
    },
    "Mirabilandia": {
        "description": "İtalya'nın en büyük tema parklarından biri, roller coaster'lar ve aile eğlencesi. Su parkı, gösteriler ve yaz tatili aktivitesi.",
        "description_en": "One of Italy's largest theme parks with roller coasters and family entertainment. Water park, shows, and summer vacation activity."
    },
    "Villaggio della Salute Più": {
        "description": "Termal kaplıcalar ve wellness kompleksi, sağlık turizmi ve rahatlama. Sıcak havuzlar, spa hizmetleri ve doğa ortamı.",
        "description_en": "Thermal springs and wellness complex, health tourism and relaxation. Hot pools, spa services, and natural setting."
    },
    "Autodromo di Imola": {
        "description": "Efsanevi Imola yarış pisti, Formula 1 ve MotoGP yarışlarına ev sahipliği. Ayrton Senna anısı, motorsporları ve heyecan.",
        "description_en": "Legendary Imola racing circuit hosting Formula 1 and MotoGP races. Ayrton Senna tribute, motorsports, and excitement."
    },
    "Palazzo dei Diamanti": {
        "description": "Ferrara'daki Rönesans sarayı, elmas biçimli cephe taşlarıyla ünlü. Sanat sergileri, mimari harika ve kültürel merkez.",
        "description_en": "Renaissance palace in Ferrara famous for diamond-shaped facade stones. Art exhibitions, architectural marvel, and cultural center."
    },
    "Casa Pavarotti": {
        "description": "Efsanevi tenor Luciano Pavarotti'nin Modena'daki ev-müzesi. Kişisel eşyalar, kostümler ve opera dünyasına bakış.",
        "description_en": "House-museum of legendary tenor Luciano Pavarotti in Modena. Personal belongings, costumes, and glimpse into opera world."
    },
    "Castelvetro di Modena": {
        "description": "Lambrusco bağlarıyla çevrili şirin ortaçağ kasabası. Şarap tadımı, kale manzarası ve İtalyan şarap yolu.",
        "description_en": "Charming medieval town surrounded by Lambrusco vineyards. Wine tasting, castle views, and Italian wine route."
    },
    "Nonantola Abbey": {
        "description": "8. yüzyıldan kalma Benediktin manastırı, Romanesk mimari ve dini sanat. Keşişlik tarihi, fresk kalıntıları ve manevi atmosfer.",
        "description_en": "8th-century Benedictine monastery with Romanesque architecture and religious art. Monastic history, fresco remains, and spiritual atmosphere."
    },
    "Dardagna Waterfalls": {
        "description": "Emilia-Romagna Apennin Dağları'ndaki şelaleler, doğa yürüyüşü ve fotoğrafçılık. Orman patikası, temiz hava ve doğa kaçışı.",
        "description_en": "Waterfalls in Emilia-Romagna Apennine Mountains for nature hiking and photography. Forest trail, fresh air, and nature escape."
    },
    "Monte Sole Historical Park": {
        "description": "İkinci Dünya Savaşı'ndaki Marzabotto katliamı anısına kurulan tarihi park. Anma yeri, yürüyüş rotaları ve tarihsel farkındalık.",
        "description_en": "Historic park established in memory of WWII Marzabotto massacre. Memorial site, hiking trails, and historical awareness."
    },
    "Abbey of Pomposa": {
        "description": "Ferrara yakınlarındaki 9. yüzyıl Benediktin manastırı, fresk hazineleri ve çan kulesiyle. Müzikal nota sisteminin doğum yeri.",
        "description_en": "9th-century Benedictine monastery near Ferrara with fresco treasures and bell tower. Birthplace of musical notation system."
    },
    "Opificio": {
        "description": "Eski fabrika binasında kurulan yeme-içme ve kültür mekanı. Craft bira, yerel yemekler ve alternatif etkinlikler.",
        "description_en": "Dining and culture venue established in old factory building. Craft beer, local food, and alternative events."
    },
    "Fienile Fluò": {
        "description": "Kırsal alanda restore edilmiş samanlıkta organik restoran ve farm-to-table deneyimi. Doğa ortamı, sürdürülebilir mutfak ve slow food.",
        "description_en": "Organic restaurant and farm-to-table experience in restored rural barn. Natural setting, sustainable cuisine, and slow food."
    },
    "Velostazione Dynamo": {
        "description": "Bisiklet kültürünü kutlayan kafe, bisiklet tamiri ve topluluk mekanı. Çevre dostu ulaşım, kahve ve aktif yaşam.",
        "description_en": "Cafe celebrating bicycle culture with bike repair and community space. Eco-friendly transportation, coffee, and active living."
    },
    "Mercato Ritrovato": {
        "description": "Cumartesi günleri kurulan organik çiftçi pazarı, yerel üreticiler ve taze ürünler. Slow food hareketi, sürdürülebilir alışveriş.",
        "description_en": "Organic farmers' market set up on Saturdays with local producers and fresh products. Slow food movement, sustainable shopping."
    },
    "Ex Forno Mambo": {
        "description": "Eski fırın binasında alternatif kültür merkezi, canlı müzik ve sanat etkinlikleri. Bologna'nın underground sahnesinin kalbi.",
        "description_en": "Alternative culture center in old bakery building with live music and art events. Heart of Bologna's underground scene."
    },
    "Sartoria Gastronomica": {
        "description": "Yemek atölyeleri ve İtalyan mutfağı kursları sunan gastronomi okulu. Pasta yapımı, yerel tarifler ve interaktif öğrenme.",
        "description_en": "Gastronomy school offering cooking workshops and Italian cuisine courses. Pasta making, local recipes, and interactive learning."
    }
}

filepath = 'assets/cities/bologna.json'
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

print(f"\n✅ Manually enriched {count} items (Bologna Batch 2).")
