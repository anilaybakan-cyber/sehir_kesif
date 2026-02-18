import json

# Manual enrichment data (Fes Batch 1: 40 items)
updates = {
    "Bab Chorfa": {
        "description": "Fes el-Bali'ye giriş sağlayan tarihi surları geçmiş anıtsal kapı. Şerif'lerin kapısı anlamına gelen yapı, Merinid dönemi mimarisinin örneği.",
        "description_en": "Monumental gate providing entry to Fes el-Bali through historic walls. Structure meaning 'Gate of the Sherifs', example of Marinid-period architecture."
    },
    "Place Baghdadi": {
        "description": "Fes el-Bali'nin kuzey girişindeki hareketli meydan, yerel halkın buluşma noktası. Kafeler, esnaf ve medina yaşamının nabzı.",
        "description_en": "Busy square at northern entrance of Fes el-Bali, meeting point for locals. Cafes, merchants, and pulse of medina life."
    },
    "Jnan Palace": {
        "description": "Tarihi saray-hotel kompleksi, geleneksel Fas mimarisi ve lüks bahçeler. Çeşmeler, seramik mozaikler ve aristokrat atmosfer.",
        "description_en": "Historic palace-hotel complex with traditional Moroccan architecture and luxury gardens. Fountains, ceramic mosaics, and aristocratic atmosphere."
    },
    "Centre de Formation aux Metiers de l'Artisanat": {
        "description": "Geleneksel Fas el sanatlarını öğreten zanaat merkezi, dokuma, seramik ve deri işleme. Atölye turları, yerel üretim ve ustalar.",
        "description_en": "Craft center teaching traditional Moroccan handicrafts including weaving, ceramics, and leather work. Workshop tours, local production, and masters."
    },
    "Kasbah An-Nouar": {
        "description": "Mellah (Yahudi mahallesi) yakınındaki tarihi kale yapısı, Fas askeri mimarisinin örneği. Surlar, kuleler ve stratejik konum.",
        "description_en": "Historic fortress structure near Mellah (Jewish quarter), example of Moroccan military architecture. Walls, towers, and strategic location."
    },
    "Place des Alaouites": {
        "description": "Kraliyet Sarayı'nın önündeki geniş meydan, resmi törenlerin yapıldığı alan. Altın kapılar, muhafızlar ve görkemli görünüm.",
        "description_en": "Wide square in front of Royal Palace where official ceremonies take place. Golden gates, guards, and magnificent appearance."
    },
    "Bab Segma": {
        "description": "Fes'in kuzey surlarındaki tarihi kapı, şehrin eski savunma sisteminin parçası. Mermer süslemeler ve İslami kaligrafi.",
        "description_en": "Historic gate in Fes's northern walls, part of city's old defense system. Marble decorations and Islamic calligraphy."
    },
    "Petit Mechouar": {
        "description": "Kraliyet Sarayı bölgesindeki küçük tören meydanı, resmi etkinlikler için kullanılır. Tarihi önemi ve saray atmosferi.",
        "description_en": "Small ceremonial square in Royal Palace area, used for official events. Historical significance and palace atmosphere."
    },
    "Rue des Mérinides": {
        "description": "Merinid hanedanlığından kalma tarihi cadde, eski medreselere ve camilere açılır. Ortaçağ atmosferi ve mimari miras.",
        "description_en": "Historic street from Marinid dynasty opening to old madrasas and mosques. Medieval atmosphere and architectural heritage."
    },
    "Bab el-Amer": {
        "description": "Fes el-Jdid'e giriş sağlayan tarihi kapı, 14. yüzyıl surlarının parçası. Mellah mahallesine yakın, stratejik konum.",
        "description_en": "Historic gate providing entry to Fes el-Jdid, part of 14th-century walls. Near Mellah quarter, strategic location."
    },
    "Borj Sheikh Ahmed": {
        "description": "Medinanın dışında yükselen eski kale kulesi, şehir panoraması ve tarihi savunma yapısı. Manzara noktası ve fotoğrafçılık.",
        "description_en": "Old fortress tower rising outside the medina, city panorama and historic defense structure. Viewpoint and photography."
    },
    "Bab Guissa Mosque": {
        "description": "Bab Guissa kapısı yakınındaki tarihi cami, yerel cemaatin ibadet mekanı. İslami mimari, minare ve dini yaşam.",
        "description_en": "Historic mosque near Bab Guissa gate, place of worship for local congregation. Islamic architecture, minaret, and religious life."
    },
    "Palais Mokri": {
        "description": "19. yüzyıldan kalma tarihi saray, geleneksel Fas zanaatkarlarının şaheserlerini barındırır. Ahşap oyma, çini ve stuko.",
        "description_en": "19th-century historic palace housing masterpieces of traditional Moroccan craftsmen. Wood carving, tiles, and stucco."
    },
    "Bab Khoukha": {
        "description": "Medina surlarındaki küçük kapı, yerel halkın kullandığı dar geçiş. Otantik mahalle yaşamına açılan portal.",
        "description_en": "Small gate in medina walls, narrow passage used by locals. Portal opening to authentic neighborhood life."
    },
    "Bab Ftitou": {
        "description": "Fes el-Bali'nin doğusundaki tarihi kapı, tüccar kervanlarının giriş noktası. Ticaret tarihi ve şehir planlama örneği.",
        "description_en": "Historic gate east of Fes el-Bali, entry point for merchant caravans. Trade history and example of urban planning."
    },
    "Place de Florence": {
        "description": "Ville Nouvelle'deki modern meydan, Fransız sömürge döneminden kalma şehir planlaması. Kafeler, ağaçlık ve dinlenme alanı.",
        "description_en": "Modern square in Ville Nouvelle, urban planning from French colonial period. Cafes, trees, and rest area."
    },
    "Avenue Hassan II": {
        "description": "Fes'in modern kesimindeki ana bulvar, bankalar, dükkanlar ve restoranlar. Şehrin çağdaş yüzü ve günlük yaşam.",
        "description_en": "Main boulevard in Fes's modern section with banks, shops, and restaurants. City's contemporary face and daily life."
    },
    "Bab Jiaf": {
        "description": "Medinanın batısındaki tarihi kapı, Karaouine Camii'ne yakın stratejik giriş. Yaya trafiği ve eski şehir yaşamı.",
        "description_en": "Historic gate west of medina, strategic entry near Karaouine Mosque. Pedestrian traffic and old city life."
    },
    "Hotel Sahrai": {
        "description": "Fes'e bakan tepede konumlanan lüks boutique otel, modern tasarım ve geleneksel dokunuşlar. Infinity havuz, spa ve panoramik manzara.",
        "description_en": "Luxury boutique hotel on hill overlooking Fes with modern design and traditional touches. Infinity pool, spa, and panoramic views."
    },
    "Sidi Moussa Tannery": {
        "description": "Chouara dışındaki daha küçük deri atölyesi, geleneksel boyama teknikleri. Daha az kalabalık, otantik zanaat deneyimi.",
        "description_en": "Smaller leather workshop outside Chouara with traditional dyeing techniques. Less crowded, authentic craft experience."
    },
    "Souk Al-Attarine": {
        "description": "Baharat ve parfüm sokağı, egzotik kokular ve geleneksel Fas ilaçları. Safran, gül suyu ve aromatik yağlar.",
        "description_en": "Spice and perfume street with exotic scents and traditional Moroccan remedies. Saffron, rose water, and aromatic oils."
    },
    "Souk Mejjad": {
        "description": "Geleneksel cilt ve kağıt ürünlerinin satıldığı sokak. El yapımı defterler, deri kaplama ve Fas kitap sanatı.",
        "description_en": "Street where traditional leather and paper products are sold. Handmade notebooks, leather binding, and Moroccan book art."
    },
    "Souk Serrajine": {
        "description": "Saraciye (at ekipmanları) satılan geleneksel çarşı. Deri eyer, at bakımı malzemeleri ve Berber zanaatı.",
        "description_en": "Traditional market selling saddlery (horse equipment). Leather saddles, horse care supplies, and Berber craftsmanship."
    },
    "Souk Nejjarine": {
        "description": "Marangozluk ve ahşap işçiliğinin sokağı, Nejjarine Çeşmesi ve Müzesi'nin evi. Oyma kapılar, mobilya ve geleneksel zanaat.",
        "description_en": "Street of carpentry and woodworking, home to Nejjarine Fountain and Museum. Carved doors, furniture, and traditional craft."
    },
    "Coin Berbere": {
        "description": "Berber el sanatları ve kilimlerinin satıldığı dükkan. Geleneksel Amazigh desenleri, tribal halılar ve etnik hediyeler.",
        "description_en": "Shop selling Berber handicrafts and rugs. Traditional Amazigh patterns, tribal carpets, and ethnic gifts."
    },
    "Les Tanneries de Fes": {
        "description": "Deri işleme atölyeleri ve showroom'ları zinciri, fabrika turları ve satış. Çanta, ceket ve aksesuar seçenekleri.",
        "description_en": "Chain of leather processing workshops and showrooms with factory tours and sales. Bag, jacket, and accessory options."
    },
    "Tissages Berbères": {
        "description": "El dokuması Berber halı ve kilim uzmanı dükkan. Bölgesel motifler, doğal boyalar ve otantik dokuma.",
        "description_en": "Shop specializing in handwoven Berber carpets and kilims. Regional motifs, natural dyes, and authentic weaving."
    },
    "Chez les Potiers": {
        "description": "Fes'in çömlekçi mahallesindeki seramik atölyesi ve satış noktası. Mavi-beyaz Fassi seramik, tabak ve vazo.",
        "description_en": "Ceramic workshop and sales point in Fes's potter quarter. Blue-white Fassi ceramics, plates, and vases."
    },
    "Au Fil d'Or": {
        "description": "Altın ve gümüş iplikle nakış yapılan geleneksel terzilik. Kaftan, takım ve Fas düğün kıyafetleri.",
        "description_en": "Traditional tailoring with gold and silver thread embroidery. Kaftan, suits, and Moroccan wedding outfits."
    },
    "Broderie de Fes": {
        "description": "Fes nakış geleneğini yaşatan atölye, el işi masa örtüleri ve tekstil. İnce işçilik ve hediye seçenekleri.",
        "description_en": "Workshop keeping Fes embroidery tradition alive with handmade tablecloths and textiles. Fine craftsmanship and gift options."
    },
    "Souk Haik": {
        "description": "Kumaş ve tekstil pazarı, geleneksel Fas döşemelik ve giysilik kumaşlar. Renkli seçenekler ve pazarlık kültürü.",
        "description_en": "Fabric and textile market with traditional Moroccan upholstery and clothing fabrics. Colorful options and bargaining culture."
    },
    "Medin'Art": {
        "description": "Medina içindeki çağdaş sanat galerisi, yerel ve uluslararası sanatçı eserleri. Modern Fas sanatı ve kültürel köprü.",
        "description_en": "Contemporary art gallery in the medina with local and international artist works. Modern Moroccan art and cultural bridge."
    },
    "Souk Jeld": {
        "description": "Deri ürünlerinin satıldığı çarşı, çanta, cüzdan ve ayakkabı. El yapımı Fas derisi ve uygun fiyatlar.",
        "description_en": "Market selling leather goods including bags, wallets, and shoes. Handmade Moroccan leather and affordable prices."
    },
    "Antique Shop Fes": {
        "description": "Fas antika ve koleksiyon eşyaları dükkanı. Eski halılar, takılar, bakır kaplar ve nostaljik hazineler.",
        "description_en": "Moroccan antiques and collectibles shop. Old carpets, jewelry, copper vessels, and nostalgic treasures."
    },
    "Galerie Chez Zemama": {
        "description": "Berber halıları ve etnik sanat eserleri galerisi. Nadir parçalar, tarihi dokumalar ve koleksiyon kalitesi.",
        "description_en": "Gallery of Berber carpets and ethnic artworks. Rare pieces, historic weavings, and collection quality."
    },
    "Cooperative de Tissage": {
        "description": "Kadın kooperatifi dokuma atölyesi, el tezgahında halı üretimi. Sosyal girişim, adil ticaret ve zanaat desteği.",
        "description_en": "Women's cooperative weaving workshop with handloom carpet production. Social enterprise, fair trade, and craft support."
    },
    "Argansouss": {
        "description": "Argan yağı ve kozmetik ürünleri dükkanı, organik Fas güzellik gelenekleri. Cilt bakımı, saç bakımı ve doğal ürünler.",
        "description_en": "Argan oil and cosmetic products shop with organic Moroccan beauty traditions. Skincare, haircare, and natural products."
    },
    "Dar El Ghalia": {
        "description": "Geleneksel Riad'da butik dükkan, el yapımı seramik ve tekstil. Otantik Fas dekorasyonu ve hediyelik seçenekler.",
        "description_en": "Boutique shop in traditional Riad with handmade ceramics and textiles. Authentic Moroccan decoration and gift options."
    },
    "Souk Tillis": {
        "description": "Mozaik çini (zellige) ustalarının sokağı, geleneksel Fas çini sanatı. Geometrik desenler ve renkli karolar.",
        "description_en": "Street of mosaic tile (zellige) masters, traditional Moroccan tile art. Geometric patterns and colorful tiles."
    },
    "Fes Drum Shop": {
        "description": "Geleneksel Fas davulları ve perküsyon aletleri. Darbuka, bendir ve Gnawa müziği enstrümanları.",
        "description_en": "Traditional Moroccan drums and percussion instruments. Darbuka, bendir, and Gnawa music instruments."
    }
}

filepath = 'assets/cities/fes.json'
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

print(f"\n✅ Manually enriched {count} items (Fes Batch 1).")
