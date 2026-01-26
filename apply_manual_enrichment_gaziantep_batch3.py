import json

# Manual enrichment data (Gaziantep Batch 3 FINAL: 40 items)
updates = {
    "Ciğer Sarayı": {
        "description": "Antep usulü acılı ve baharatlı ciğer kebabının en meşhur adreslerinden biri. Taze kuzu ciğeri, kırmızı biber ve özel karışımlarla mangalda pişirilen, cesur damaklar için lezzet şöleni.",
        "description_en": "One of the most famous addresses for Antep-style spicy and seasoned liver kebab. A flavor feast for brave palates, grilled with fresh lamb liver, red pepper, and special blends."
    },
    "Etçi Mehmet": {
        "description": "Kaliteli et seçimi ve ustalıkla pişirmesiyle tanınan, şehrin popüler et restoranlarından. Kuzu pirzola, biftek ve geleneksel kebaplar, damak zevkinize göre pişirilir.",
        "description_en": "One of the city's popular meat restaurants known for quality meat selection and skillful cooking. Lamb chops, steak, and traditional kebabs cooked to your taste."
    },
    "Ocakbaşı Ali Usta": {
        "description": "Misafirlerin ocağın çevresinde oturup şefi izlediği, interaktif Antep kebap deneyimi. Taze kıyma, usta eli ve kömür ateşiyle, otantik ocakbaşı atmosferi.",
        "description_en": "An interactive Antep kebab experience where guests sit around the fire and watch the chef. Authentic ocakbaşı atmosphere with fresh minced meat, master's hand, and charcoal fire."
    },
    "Kaburga Dolma Evi": {
        "description": "Kuzu göğüs kemiğinin içine pirinç ve baharatlar doldurulan geleneksel Antep yemeği kaburga dolmanın en iyi yapıldığı yer. Yavaş pişirme ve özel tarifle, unutulmaz lezzet.",
        "description_en": "The place where kaburga dolma, a traditional Antep dish of lamb rib stuffed with rice and spices, is made best. Unforgettable flavor with slow cooking and special recipe."
    },
    "Pide Salonu": {
        "description": "Antep usulü açık pide ve kapalı pidenin çeşitli dolgularla sunulduğu geleneksel fırın-lokanta. Kıymalı, peynirli ve karışık pideler, odun fırınında pişirilir.",
        "description_en": "A traditional bakery-restaurant serving Antep-style open and closed pide with various fillings. Meat, cheese, and mixed pides baked in wood-fired oven."
    },
    "Tantuni Durağı": {
        "description": "Hızlı ve lezzetli tantuni için şehirdeki popüler durak. Dana etinin ince ince doğranıp saç tavasında pişirildiği, dürüm veya ekmek arası servis edilen sokak lezzeti.",
        "description_en": "A popular stop in the city for fast and delicious tantuni. Street food served as wrap or sandwich with beef finely chopped and cooked on flat griddle."
    },
    "Ana Lokantası": {
        "description": "Ev yemekleri, geleneksel sulu yemekler ve anne eli lezzetler sunan samimi aile lokantası. Günlük taze pişirilen menü, uygun fiyat ve doyurucu porsiyonlar.",
        "description_en": "An intimate family restaurant serving home cooking, traditional stews, and mother's hand flavors. Daily fresh-cooked menu, affordable prices, and satisfying portions."
    },
    "Esnaf Lokantası": {
        "description": "İş insanlarının ve yerel halkın öğle yemeği için tercih ettiği ekonomik lokanta. Hızlı servis, çeşitli sulu yemekler ve günlük menüyle pratik öğlen molası.",
        "description_en": "An economical restaurant preferred by businesspeople and locals for lunch. A practical lunch break with fast service, various stews, and daily menu."
    },
    "Ekşili Köfte Evi": {
        "description": "Antep'e özgü ekşili köfte yemeğinin en lezzetli halini sunan özel mekan. Bulgur köftesi, nar ekşisi ve sebzelerle pişirilen bu geleneksel tarif, vejetaryenler için de uygun.",
        "description_en": "A special venue serving the most delicious version of sour meatball dish unique to Antep. This traditional recipe cooked with bulgur meatballs, pomegranate syrup, and vegetables is also suitable for vegetarians."
    },
    "Analı Kızlı Lokantası": {
        "description": "İsmini meşhur Antep yemeğinden alan, köfte ve nohut topu birleşiminin en iyi yapıldığı restoran. Geleneksel tarif, zengin içerik ve otantik sunum.",
        "description_en": "A restaurant named after the famous Antep dish, where the combination of meatballs and chickpea balls is made best. Traditional recipe, rich content, and authentic presentation."
    },
    "Firik Pilavı Evi": {
        "description": "Yeşil buğdaydan yapılan geleneksel firik pilavının en otantik halinde sunulduğu mekan. Kuzu eti veya tavukla servis edilen bu antik tahıl, Antep mutfağının gizli hazinesi.",
        "description_en": "A venue serving traditional firik pilaf made from green wheat in its most authentic form. This ancient grain served with lamb or chicken is a hidden treasure of Antep cuisine."
    },
    "Oruk Evi": {
        "description": "Antep'in meşhur içli köftesinin farklı bir versiyonu olan oruğun en lezzetli örneklerini sunan butik mekan. Kızartılmış veya ızgara seçenekleriyle, bulgur ustası.",
        "description_en": "A boutique venue serving the most delicious examples of oruk, a different version of Antep's famous içli köfte. Bulgur master with fried or grilled options."
    },
    "Rooftop Bar": {
        "description": "Şehrin panoramik manzarasını sunan çatı katı bar, kokteyl ve özel içecekleri manzara eşliğinde sunuyor. Gece ışıkları, müzik ve sofistike atmosferle akşam keyfi.",
        "description_en": "A rooftop bar offering panoramic city views, serving cocktails and special drinks with scenery. Evening enjoyment with night lights, music, and sophisticated atmosphere."
    },
    "Bira Evi": {
        "description": "Yerel ve ithal biralar sunan, rahat ortamıyla dikkat çeken bira odaklı mekan. Arkadaşlarla buluşma, maç izleme ve soğuk bira keyfi için samimi adres.",
        "description_en": "A beer-focused venue serving local and imported beers, notable for its comfortable atmosphere. An intimate address for meeting friends, watching games, and enjoying cold beer."
    },
    "Specialty Coffee": {
        "description": "Üçüncü dalga kahve kültürünü Gaziantep'e taşıyan, özel kavurma ve demleme yöntemlerini kullanan modern kafe. Latte art, pour over ve espresso bazlı içecekler.",
        "description_en": "A modern cafe bringing third-wave coffee culture to Gaziantep, using special roasting and brewing methods. Latte art, pour over, and espresso-based drinks."
    },
    "Kitap Kafe": {
        "description": "Kitaplarla çevrili, okuma ve kahve içme keyfini birleştiren huzurlu mekan. Yerel yazarların eserlerinin satıldığı köşe, sakin atmosfer ve kaliteli içecekler.",
        "description_en": "A peaceful venue surrounded by books, combining reading and coffee enjoyment. A corner selling local authors' works, calm atmosphere, and quality drinks."
    },
    "Çikolata Evi": {
        "description": "El yapımı çikolatalar, pralinler ve kakaolu tatlıların satıldığı butik dükkan. Özel hediye paketleri ve Antep fıstıklı çikolata kreasyonlarıyla tatlı severler için cennet.",
        "description_en": "A boutique shop selling handmade chocolates, pralines, and cocoa desserts. A paradise for sweet lovers with special gift packages and Antep pistachio chocolate creations."
    },
    "Boyacı Camii": {
        "description": "16. yüzyıldan kalma tarihi cami, boyacılar loncasının desteklediği dini yapı. Taş işçiliği, minare detayları ve korunmuş atmosferiyle, şehrin dini mirasından önemli örnek.",
        "description_en": "A 16th-century historic mosque, a religious structure supported by the dyers' guild. An important example of the city's religious heritage with stone work, minaret details, and preserved atmosphere."
    },
    "Ömer Ersoy Camii": {
        "description": "Modern mimari anlayışla tasarlanmış çağdaş cami, geleneksel İslami öğelerle modern estetiği harmanlıyor. Şehrin yeni dini yapıları arasında dikkat çeken tasarım.",
        "description_en": "A contemporary mosque designed with modern architectural approach, blending traditional Islamic elements with modern aesthetics. A notable design among the city's new religious buildings."
    },
    "Tahta Kahve Camii": {
        "description": "Ahşap elemanları ve özgün iç mekanıyla dikkat çeken tarihi cami. Ahşap mimberi ve tavanıyla, Anadolu camii geleneğinin nadir örneklerinden.",
        "description_en": "A historic mosque notable for wooden elements and unique interior. One of the rare examples of Anatolian mosque tradition with its wooden pulpit and ceiling."
    },
    "Naib Hamamı": {
        "description": "Yüzyıllardır hizmet veren tarihi Osmanlı hamamı, geleneksel mimari ve hamam kültürünün canlı örneği. Sıcak mermer, kubbe ve tarihi atmosferde wellness deneyimi.",
        "description_en": "A historic Ottoman hammam serving for centuries, a living example of traditional architecture and bath culture. Wellness experience with hot marble, dome, and historic atmosphere."
    },
    "Kendirci Camii": {
        "description": "Dokumacılar mahallesi ile ilişkili tarihi cami, lonca sisteminin dini yaşamla kesiştiğini gösteren örnek. Mütevazı mimarisi ve yerel tarihi önemiyle dikkat çekici.",
        "description_en": "A historic mosque associated with the weavers' quarter, an example showing intersection of guild system with religious life. Notable for modest architecture and local historical significance."
    },
    "Şehitlik Tepesi": {
        "description": "Kurtuluş Savaşı'nda şehit düşenlerin anısına düzenlenen anıt alan ve park. Şehir manzarası, tarihi anıtlar ve milli duygularla dolu anlamlı ziyaret noktası.",
        "description_en": "A memorial area and park arranged in memory of martyrs in the War of Independence. A meaningful visit point with city views, historical monuments, and national sentiments."
    },
    "Panorama 25 Aralık Müzesi": {
        "description": "Gaziantep'in kurtuluş mücadelesini dramatik panoramik görsellerle anlatan modern müze. 25 Aralık 1921 zaferini 360 derece projeksiyonlarla yaşatan interaktif deneyim.",
        "description_en": "A modern museum telling Gaziantep's liberation struggle with dramatic panoramic visuals. An interactive experience bringing the December 25, 1921 victory to life with 360-degree projections."
    },
    "Astronomi Müzesi": {
        "description": "Gökyüzü bilimi, uzay keşfi ve astronomi tarihini interaktif sergilerle anlatan eğitici müze. Teleskop gözlemleri, planetaryum gösterileri ve çocuklar için aktiviteler.",
        "description_en": "An educational museum explaining astronomy science, space exploration, and astronomy history with interactive exhibitions. Telescope observations, planetarium shows, and activities for children."
    },
    "Savaş Araçları Müzesi": {
        "description": "Askeri araçlar, uçaklar ve savunma sistemlerinin sergilendiği açık hava müzesi. Türk savunma sanayinin güçlü olduğu Gaziantep'te, askeri teknoloji koleksiyonu.",
        "description_en": "An open-air museum exhibiting military vehicles, aircraft, and defense systems. Military technology collection in Gaziantep where Turkish defense industry is strong."
    },
    "Halfeti Sular Altı Köyü": {
        "description": "Birecik Barajı'nın suları altında kalan tarihi Halfeti'nin batık yapılarını tekneyle keşfedin. Minare kalıntıları, su altı evleri ve dramatik manzarayla sıra dışı deneyim.",
        "description_en": "Discover the sunken structures of historic Halfeti submerged under Birecik Dam waters by boat. An extraordinary experience with minaret remains, underwater houses, and dramatic scenery."
    },
    "Kara Gül Bahçesi": {
        "description": "Halfeti'ye özgü nadir siyah güllerin yetiştirildiği botanik bahçe. Bu benzersiz çiçeği görmek, fotoğraflamak ve satın almak için Türkiye'nin tek adresi.",
        "description_en": "A botanical garden where rare black roses unique to Halfeti are grown. Turkey's only address to see, photograph, and purchase this unique flower."
    },
    "Kuruyemişçi Çarşısı": {
        "description": "Antep fıstığı, badem, ceviz ve çeşitli kuruyemişlerin toptan ve perakende satıldığı geleneksel çarşı. Taze kavrulmuş fıstık tadımı ve uygun fiyatlarla alışveriş.",
        "description_en": "A traditional bazaar selling Antep pistachios, almonds, walnuts, and various nuts wholesale and retail. Shopping with fresh roasted pistachio tasting and affordable prices."
    },
    "Baharatçı": {
        "description": "Rengarenk baharatlar, biber salçaları ve geleneksel tatlandırıcıların satıldığı aromatik dükkan. Antep mutfağının gizli silahlarını keşfedin ve eve götürün.",
        "description_en": "An aromatic shop selling colorful spices, pepper pastes, and traditional seasonings. Discover the secret weapons of Antep cuisine and take them home."
    },
    "Hediyelik Eşya Dükkanı": {
        "description": "Antep'e özgü hediyelikler, bakır ürünler, seramikler ve yerel sanatçıların eserlerinin satıldığı butik. Orijinal hatıralar ve el yapımı ürünler.",
        "description_en": "A boutique selling souvenirs unique to Antep, copper products, ceramics, and works of local artists. Original keepsakes and handmade products."
    },
    "Dokumacılar Çarşısı": {
        "description": "Geleneksel el dokuma kumaşları, kilimleri ve yöresel tekstil ürünlerinin satıldığı tarihi çarşı. Zanaatkarların çalışmasını izleyebileceğiniz, canlı ve otantik ortam.",
        "description_en": "A historic bazaar selling traditional handwoven fabrics, kilims, and regional textile products. A lively and authentic environment where you can watch artisans work."
    },
    "Altın Çarşısı": {
        "description": "Kuyumcu dükkanlarının sıralandığı, altın takılar ve mücevherlerin satıldığı geleneksel çarşı. Düğün alışverişi, hediye seçimi ve el işçiliği takılar için adres.",
        "description_en": "A traditional bazaar where jewelry shops are lined up, selling gold jewelry and gems. An address for wedding shopping, gift selection, and handcrafted jewelry."
    },
    "Tirit Lokantası": {
        "description": "Bayat ekmeğin et suyu ve yoğurtla canlandırıldığı geleneksel Antep yemeği tirit'in en iyi yapıldığı yer. Sade görünüşü, zengin tadı ve doyurucu yapısıyla şaşırtıcı lezzet.",
        "description_en": "The place where tirit, a traditional Antep dish where stale bread is revived with meat broth and yogurt, is made best. Surprising flavor with simple appearance, rich taste, and filling nature."
    },
    "Kelle Paça": {
        "description": "Kuzu kellesi ve ayaklarından yapılan geleneksel çorbanın sabahın erken saatlerinde sunulduğu meşhur lokanta. Gece eğlencesi sonrası veya kuvvetli kahvaltı için tercih.",
        "description_en": "A famous restaurant serving traditional soup made from lamb head and feet in early morning hours. Preferred after night entertainment or for a strong breakfast."
    },
    "Mumbar Dolma Evi": {
        "description": "Kuzu bağırsağının pirinç ve baharatlarla doldurulduğu geleneksel Antep lezzeti mumbar dolmanın en iyi yapıldığı yer. Cesur gurmelerin mutlaka denemesi gereken otantik tat.",
        "description_en": "The place where mumbar dolma, a traditional Antep flavor of lamb intestine stuffed with rice and spices, is made best. An authentic taste brave gourmets must try."
    },
    "Şıllık Tatlıcısı": {
        "description": "Antep'e özgü, uzun ince hamur şeritlerinin şerbete batırılarak hazırlandığı geleneksel tatlı şıllık'ın en iyi yapıldığı mekan. Hafif, lezzetli ve farklı bir tatlı deneyimi.",
        "description_en": "The venue where şıllık, a traditional dessert unique to Antep made with long thin dough strips dipped in syrup, is made best. A light, delicious, and different dessert experience."
    },
    "Sac Kavurma": {
        "description": "Saç tavada yüksek ateşte kavrulmuş kuzu etinin en lezzetli halinde sunulduğu geleneksel kebapçı. Yanında közlenmiş sebzeler ve lavash ekmek ile servis.",
        "description_en": "A traditional kebab house serving lamb meat sautéed at high heat on flat griddle in its most delicious form. Served with charred vegetables and lavash bread on the side."
    },
    "Çiğ Köfte Ustası": {
        "description": "Antep'in acılı ve baharatlı çiğ köftesinin en otantik halini sunan usta. Taze bulgur, özel baharat karışımı ve el yoğurmasıyla hazırlanan, vejetaryen versiyonu da mevcut.",
        "description_en": "A master serving the most authentic version of Antep's spicy and seasoned raw meatballs. Prepared with fresh bulgur, special spice mix, and hand kneading, vegetarian version also available."
    },
    "Patlıcan Kebabı Evi": {
        "description": "Antep'in ikonik patlıcan kebabının en lezzetli versiyonunu sunan özel restoran. Közde patlıcan, mükemmel kıyma ve özel sosla, şehrin gurme mutfağının zirvesi.",
        "description_en": "A special restaurant serving the most delicious version of Antep's iconic eggplant kebab. The pinnacle of the city's gourmet cuisine with charred eggplant, perfect minced meat, and special sauce."
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

print(f"\n✅ Manually enriched {count} items (Gaziantep Batch 3 FINAL).")
