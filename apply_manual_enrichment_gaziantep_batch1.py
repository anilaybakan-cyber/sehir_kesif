import json

# Manual enrichment data (Gaziantep Batch 1: 40 items)
updates = {
    "Tarihi Yuvalama Evi": {
        "description": "Gaziantep'in en meşhur tencere yemeği yuvalama ve beğendinin en otantik haliyle yapıldığı tarihi restoran. Kuşaktan kuşağa aktarılan tarifler, bakır kaplar ve geleneksel sunum, Antep mutfağının özünü yansıtıyor.",
        "description_en": "A historic restaurant where Gaziantep's most famous stew dish yuvalama and beğendi are made in their most authentic form. Recipes passed down generations, copper pots, and traditional presentation reflect the essence of Antep cuisine."
    },
    "Karaoğlu Baklava": {
        "description": "1946'dan beri hizmet veren, kadayıf ve baklava ustası efsanevi pastane. Özellikle sütlü nuriye ve fıstıklı bürma türleriyle ünlü, hakiki Antep fıstığıyla hazırlanan tatlıların adres noktası.",
        "description_en": "A legendary pastry shop serving since 1946, master of kadayif and baklava. Famous especially for milky nuriye and pistachioburma varieties, the address for desserts prepared with genuine Antep pistachios."
    },
    "Güllüoğlu": {
        "description": "Gaziantep'ten başlayıp dünyaya yayılan baklava imparatorluğunun doğum yeri. Karamelize kaymak tabakası ve el açması yufkasıyla, baklavayı sanat formuna taşıyan efsane marka.",
        "description_en": "The birthplace of the baklava empire that started in Gaziantep and spread worldwide. The legendary brand that elevated baklava to an art form with caramelized cream layer and hand-rolled phyllo."
    },
    "Develi Kebap": {
        "description": "Antep usulü pide, lahmacun ve kebaplarıyla tanınan, şehrin en köklü kebapçılarından. Kıyma kalitesi, baharat dengesi ve odun ateşinde pişirme geleneğiyle, gerçek Antep lezzetinin adresi.",
        "description_en": "One of the city's most established kebab houses known for Antep-style pide, lahmacun, and kebabs. The address for real Antep flavor with meat quality, spice balance, and wood-fire cooking tradition."
    },
    "Beyran Ustası": {
        "description": "Sabahın köründe açılan, baharatlı kuzu ciğeri ve kemiğinden yapılan geleneksel beyran çorbası sunan meşhur lokal. Kış sabahlarının vazgeçilmez lezzeti, şifalı ve doyurucu bir başlangıç.",
        "description_en": "A famous local opening at crack of dawn, serving traditional beyran soup made from spicy lamb liver and bone. An indispensable winter morning flavor, a healing and filling start."
    },
    "Simit Sarayı Gaziantep": {
        "description": "Türkiye genelinde tanınan zincirin Gaziantep şubesi, hızlı kahvaltı ve simit çeşitleri için uygun seçenek. Şehir merkezinde pratik mola noktası, tanıdık lezzetler ve tutarlı kalite.",
        "description_en": "Gaziantep branch of the chain known throughout Turkey, a suitable choice for quick breakfast and simit varieties. A practical stop in city center, familiar flavors and consistent quality."
    },
    "Anadolu Sofrası": {
        "description": "Ev yemekleri, sulu yemekler ve geleneksel Antep lezzetleri sunan, öğlen yemeği için ideal aile lokantası. Günlük taze pişirilen yemekler, uygun fiyat ve samimi ortamıyla yerel favori.",
        "description_en": "A family restaurant ideal for lunch, serving home cooking, stews, and traditional Antep flavors. A local favorite with daily fresh-cooked dishes, affordable prices, and friendly atmosphere."
    },
    "Tatlidede": {
        "description": "Gerçek Antep fıstığından yapılan dondurma ve modern sunumlarıyla öne çıkan tatlıcı. Geleneksel tariflere çağdaş dokunuşlar ekleyen, şehrin yeni nesil tatlı mekanlarından.",
        "description_en": "A dessert shop standing out with ice cream made from real Antep pistachios and modern presentations. One of the city's new generation dessert venues adding contemporary touches to traditional recipes."
    },
    "Kadayıfçı Cemil Usta": {
        "description": "Tel kadayıf ve künefe yapan nadir ustalardan biri, geleneksel tarifleri koruyan authentic mekan. El açması ince tel kadayıf, taze lor peyniri ve özel şerbetiyle, nadide bir lezzet deneyimi.",
        "description_en": "One of the rare masters making shredded kadaif and kunefe, an authentic venue preserving traditional recipes. A rare taste experience with hand-made thin shredded kadaif, fresh lor cheese, and special syrup."
    },
    "Şerbet Evi": {
        "description": "Geleneksel Antep şerbetleri, limonata ve mey şırası sunan, sıcak yaz günlerinde serinleme durağı. Serin bir avluda tarihi tariflerle hazırlanan içecekler, Osmanlı dönemi lezzetlerine yolculuk.",
        "description_en": "A cooling stop on hot summer days serving traditional Antep sherbet, lemonade, and grape must. Drinks prepared with historic recipes in a cool courtyard, a journey to Ottoman-era flavors."
    },
    "Fıstıklı Dondurma": {
        "description": "Maraş dondurmacısından farklı, gerçek Antep fıstığından yapılan sade ve yoğun aromalı dondurma sunan butik mekan. Fıstık oranı yüksek, katkısız ve el yapımı ürünleriyle, dondurma tutkunlarının durağı.",
        "description_en": "A boutique venue serving plain and intensely flavored ice cream made from real Antep pistachios, different from Maraş ice cream makers. A stop for ice cream lovers with high pistachio ratio, additive-free and handmade products."
    },
    "Peynirli Künefe": {
        "description": "Hatay künefesinden farklı olarak Antep usulü, daha ince tel kadayıf ve özel peynirle hazırlanan künefe ustası. Gevrek dışı, uzayan peyniri ve hafif şerbetiyle, tatlı tutkunlarının gizli adresi.",
        "description_en": "A kunefe master preparing Antep-style kunefe with thinner shredded kadaif and special cheese, different from Hatay kunefe. A secret address for dessert lovers with crispy exterior, stretchy cheese, and light syrup."
    },
    "Mahallebaşı": {
        "description": "Modern atmosferde geleneksel Antep tatlıları sunan, genç kitleye hitap eden çağdaş tatlıcı. Klasik lezzetlerin yeniden yorumlandığı ve Instagram'a uygun sunumlarla sergilendiği trendy mekan.",
        "description_en": "A contemporary dessert shop serving traditional Antep desserts in modern atmosphere, appealing to young crowds. A trendy venue where classic flavors are reinterpreted and presented Instagram-ready."
    },
    "Helva Evi": {
        "description": "Çeşitli helva türleri, tahin ürünleri ve pekmezlerin satıldığı geleneksel dükkân. Antep fıstıklı, cevizli ve sade helvaların yanı sıra, el yapımı tahin ve üzüm pekmezi de bulunuyor.",
        "description_en": "A traditional shop selling various types of halva, tahini products, and molasses. Along with pistachio, walnut, and plain halvas, handmade tahini and grape molasses are also available."
    },
    "Şire Han": {
        "description": "Tarihi handa üzüm şırası, geleneksel içecekler ve hafif atıştırmalıklar sunan atmosferik mekan. Taş duvarlar, avlu düzenlemesi ve Osmanlı dönemi ambiyansıyla, dinlenme ve sohbet için ideal.",
        "description_en": "An atmospheric venue in a historic han serving grape must, traditional drinks, and light snacks. Ideal for rest and conversation with stone walls, courtyard setting, and Ottoman-era ambiance."
    },
    "Antep Çay Evi": {
        "description": "Yerel halkın tavla, okey ve sohbet için buluştuğu geleneksel çay evi. Demlik çay, menengiç kahvesi ve günlük yaşamın nabzını tutabileceğiniz otantik Antep atmosferi.",
        "description_en": "A traditional tea house where locals meet for backgammon, okey, and conversation. Teapot tea, menengiç coffee, and authentic Antep atmosphere where you can feel the pulse of daily life."
    },
    "Kahve Durağı": {
        "description": "Modern kahve zinciri konseptiyle çalışan, wifi ve çalışma ortamı sunan şehirdeki kafe seçeneği. Espresso bazlı içecekler, tatlılar ve rahat oturma alanlarıyla, dijital göçebeler için uygun.",
        "description_en": "A cafe option in the city working with modern coffee chain concept, offering wifi and work environment. Suitable for digital nomads with espresso-based drinks, desserts, and comfortable seating areas."
    },
    "Antep Evleri Çay Bahçesi": {
        "description": "Restore edilmiş geleneksel Antep evlerinin avlusunda kurulan, nostaljik atmosferli çay bahçesi. Ahşap sedir minderler, bakır semaver çay ve tarihi dokuyla iç içe huzurlu mola deneyimi.",
        "description_en": "A nostalgic tea garden set up in the courtyard of restored traditional Antep houses. A peaceful break experience intertwined with wooden cedar cushions, copper samovar tea, and historic texture."
    },
    "Café 37": {
        "description": "Şehrin dışında modern dekorasyonu, geniş menüsü ve brunch seçenekleriyle dikkat çeken kafe. Genç kitleye hitap eden, Instagram'a uygun sunumları ve rahat ortamıyla popüler mekan.",
        "description_en": "A cafe outside the city notable for modern decor, wide menu, and brunch options. A popular venue appealing to young crowds with Instagram-ready presentations and comfortable environment."
    },
    "Menengiç Kahvecisi": {
        "description": "Sadece Antep'e özgü menengiç kahvesine odaklanan, bu nadir içeceğin en kaliteli halini sunan butik mekan. Kafeinsiz, fıstık aromalı ve geleneksel tarifle hazırlanan benzersiz kahve deneyimi.",
        "description_en": "A boutique venue focusing only on menengiç coffee unique to Antep, offering the highest quality version of this rare drink. A unique coffee experience caffeine-free, pistachio-flavored, and prepared with traditional recipe."
    },
    "Arkeoloji Müzesi": {
        "description": "Zeugma Mozaik Müzesi dışındaki arkeolojik eserleri sergileyen, bölgenin zengin tarihine ışık tutan kapsamlı müze. Hitit, Roma ve Bizans dönemlerinden kalıntılar ve günlük yaşam objeleri.",
        "description_en": "A comprehensive museum exhibiting archaeological artifacts outside Zeugma Mosaic Museum, shedding light on the region's rich history. Remains and daily life objects from Hittite, Roman, and Byzantine periods."
    },
    "Kent Müzesi": {
        "description": "Gaziantep'in tarihini, ekonomisini, kültürünü ve geleneklerini interaktif sergilerle anlatan modern şehir müzesi. Fıstık üretiminden savunma sanayine, şehrin çok yönlü kimliğini keşfedin.",
        "description_en": "A modern city museum explaining Gaziantep's history, economy, culture, and traditions with interactive exhibitions. Discover the city's multifaceted identity from pistachio production to defense industry."
    },
    "Kurtuluş Camii": {
        "description": "Eski bir Ermeni kilisesinden camiye dönüştürülmüş, şehrin çok kültürlü geçmişine tanıklık eden tarihi yapı. Mimari detayları ve dönüşüm hikayesiyle, Anadolu'nun karmaşık tarihinin yansıması.",
        "description_en": "A historic structure converted from an old Armenian church to mosque, witnessing the city's multicultural past. A reflection of Anatolia's complex history with architectural details and transformation story."
    },
    "Şahinbey Milli Mücadele Müzesi": {
        "description": "Kurtuluş Savaşı'nda şehrin kahramanlığını ve direniş hikayesini anlatan anlamlı müze. Şehit Şahinbey'in ve Antep halkının cesaret dolu mücadelesini belgeleyen, tarihi fotoğraflar ve objeler.",
        "description_en": "A meaningful museum telling the city's heroism and resistance story during the War of Independence. Historic photos and objects documenting the courageous struggle of Martyr Şahinbey and Antep people."
    },
    "Yazılı Kayalar": {
        "description": "Hitit döneminden kalma, kayalara oyulmuş antik yazıtlar ve rölyefler içeren arkeolojik alan. Binlerce yıllık tarihin taşlara kazındığı bu açık hava müzesi, antik uygarlıklara pencere açıyor.",
        "description_en": "An archaeological site containing ancient inscriptions and reliefs carved into rocks from the Hittite period. This open-air museum where thousands of years of history are carved into stones opens a window to ancient civilizations."
    },
    "Karkamış Antik Kenti": {
        "description": "Suriye sınırında konumlanan, Hitit İmparatorluğu'nun en önemli şehirlerinden biri olan antik kent kalıntıları. Arkeolojik kazılar, anıtsal kapılar ve tarih öncesi uygarlık izleriyle önemli bir miras alanı.",
        "description_en": "Ancient city remains of one of the most important cities of the Hittite Empire, located at the Syrian border. An important heritage site with archaeological excavations, monumental gates, and traces of prehistoric civilization."
    },
    "Burç Ormanı": {
        "description": "Şehrin bunaltıcı sıcağından kaçış için ideal geniş ormanlık piknik ve rekreasyon alanı. Yaz aylarında açık hava etkinlikleri, mangal alanları ve doğa yürüyüşleriyle, ailelerin favorisi.",
        "description_en": "An extensive forested picnic and recreation area ideal for escaping the city's oppressive heat. A family favorite with outdoor events, barbecue areas, and nature walks in summer months."
    },
    "Halfeti Tekne Turu": {
        "description": "Birecik Barajı'nın suları altında kalan tarihi Halfeti şehrini tekneyle keşfetme turu. Batık cami minareleri, su altı evleri ve dramatik manzarasıyla, Türkiye'nin en sıra dışı deneyimlerinden.",
        "description_en": "A boat tour to discover the historic town of Halfeti submerged under Birecik Dam waters. One of Turkey's most extraordinary experiences with sunken mosque minarets, underwater houses, and dramatic scenery."
    },
    "Fırat Nehri Kıyısı": {
        "description": "Tarihi Fırat Nehri kenarında yürüyüş, piknik ve manzara keyfi için ideal sahil alanı. Mezopotamya uygarlıklarını besleyen bu efsanevi nehrin kenarında, tarihe dokunma deneyimi.",
        "description_en": "An ideal shore area for walking, picnicking, and enjoying views by the historic Euphrates River. An experience of touching history by this legendary river that nourished Mesopotamian civilizations."
    },
    "Zeugma Cam Terası": {
        "description": "Zeugma arkeolojik alanının üzerinde inşa edilen, antik kalıntılara kuşbakışı bakış sunan modern cam platform. Arkeologların çalışmalarını ve kazı alanını canlı olarak izleyebileceğiniz benzersiz deneyim.",
        "description_en": "A modern glass platform built over the Zeugma archaeological site offering a bird's eye view of ancient remains. A unique experience where you can watch archaeologists work and excavation site live."
    },
    "Birecik Kelaynak Üretim İstasyonu": {
        "description": "Dünyada nesli tükenmekte olan kelaynak kuşlarının korunduğu ve üretildiği önemli doğa koruma merkezi. Bu nadir kuşları yakından görebileceğiniz, ekolojik bilinci artıran eğitici ziyaret.",
        "description_en": "An important nature conservation center where endangered bald ibis birds are protected and bred. An educational visit raising ecological awareness where you can see these rare birds up close."
    },
    "Gaziantep Üniversitesi Botanik Parkı": {
        "description": "Üniversite kampüsü içinde nadir bitki türleri, kaktüs koleksiyonu ve doğa eğitim alanları bulunan yeşil vaha. Öğrenciler ve doğa meraklıları için açık hava laboratuvarı niteliğinde.",
        "description_en": "A green oasis within the university campus containing rare plant species, cactus collection, and nature education areas. Like an open-air laboratory for students and nature enthusiasts."
    },
    "Antep Fıstığı Fabrika Turu": {
        "description": "Fıstık işleme fabrikasını gezerek, hasattan kavurmaya tüm süreci öğrenebileceğiniz endüstriyel tur. Taze kavrulmuş sıcak fıstık tadımı ve şehrin ekonomik kalbine yakından bakış.",
        "description_en": "An industrial tour where you can learn the entire process from harvest to roasting by touring a pistachio processing factory. A close look at the city's economic heart with fresh roasted warm pistachio tasting."
    },
    "Gaziantep Kebap Atölyesi": {
        "description": "Profesyonel şeflerden Antep kebabı, lahmacun ve baklava yapımı öğrenebileceğiniz interaktif mutfak dersleri. Tarifi yanınızda götürün, ülkenizde de Antep lezzetlerini yapabilin.",
        "description_en": "Interactive cooking classes where you can learn to make Antep kebab, lahmacun, and baklava from professional chefs. Take the recipe with you and make Antep flavors in your country too."
    },
    "Nakış Atölyesi": {
        "description": "Geleneksel Antep nakışı ve yöresel el sanatlarını öğrenebileceğiniz, yaşayan zanaatkarların çalıştığı atölye. Kendi nakış örneğinizi yaparak, yüzyıllık geleneğe katılma fırsatı.",
        "description_en": "A workshop where you can learn traditional Antep embroidery and regional handicrafts, with living artisans working. An opportunity to join centuries-old tradition by making your own embroidery sample."
    },
    "Sanko Park AVM": {
        "description": "Şehrin en büyük modern alışveriş merkezi, yerli ve uluslararası markalar, sinema ve yeme-içme alanlarıyla. Sıcak yaz günlerinde klimalı ortamda alışveriş ve eğlence için pratik adres.",
        "description_en": "The city's largest modern shopping mall with domestic and international brands, cinema, and dining areas. A practical address for shopping and entertainment in air-conditioned environment on hot summer days."
    },
    "Prime Mall AVM": {
        "description": "Lüks markalar, kaliteli restoranlar ve modern eğlence seçenekleriyle şehrin prestijli alışveriş merkezi. Geniş otopark, family-friendly ortam ve çeşitli aktivite alanlarıyla aileler için uygun.",
        "description_en": "The city's prestigious shopping center with luxury brands, quality restaurants, and modern entertainment options. Suitable for families with large parking, family-friendly environment, and various activity areas."
    },
    "Yerel Pazar (Perşembe Pazarı)": {
        "description": "Her Perşembe kurulan, taze sebze, meyve, baharat ve yerel ürünlerin satıldığı geleneksel açık pazar. Antep'in tarım zenginliğini, yerel yaşamı ve pazarlık kültürünü deneyimleyebileceğiniz yer.",
        "description_en": "A traditional open market set up every Thursday selling fresh vegetables, fruits, spices, and local products. A place to experience Antep's agricultural richness, local life, and bargaining culture."
    },
    "Salça Çarşısı": {
        "description": "Ev yapımı domates ve biber salçalarının toptan ve perakende satıldığı, Antep mutfağının vazgeçilmez malzemelerini bulabileceğiniz özel çarşı. Yöresel tarifler ve kalite garantili ürünler.",
        "description_en": "A special market where homemade tomato and pepper pastes are sold wholesale and retail, where you can find indispensable ingredients of Antep cuisine. Regional recipes and quality-guaranteed products."
    },
    "Şehitkamil Kebapçısı": {
        "description": "Mahalle kebapçısı olarak turist görmemiş, gerçek yerel halkın gittiği otantik kebap lokali. Ucuz fiyatlar, büyük porsiyonlar ve hilesiz Antep usulü kebaplarla, hakiki yerel deneyim.",
        "description_en": "An authentic kebab locale as a neighborhood kebab house that hasn't seen tourists, where real locals go. A genuine local experience with cheap prices, large portions, and unadulterated Antep-style kebabs."
    }
}

filepath = 'assets/cities/gaziantep.json'
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

print(f"\n✅ Manually enriched {count} items (Gaziantep Batch 1).")
