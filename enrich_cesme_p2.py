#!/usr/bin/env python3
import json

updates = {
    "Dalyan Köşem Restaurant Emin'in Yeri": {
        "description": "Dalyan'ın en sakin ve huzurlu köşelerinden birinde yer alan Emin'in Yeri, taze deniz ürünleri ve meşhur ev yapımı mezeleriyle damaklarda unutulmaz bir tat bırakıyor. Denizin hemen yanı başındaki masalarda, güneşin batışını izlerken Ege'nin en doğal ve otantik gastronomi deneyimlerinden birini yaşayabilirsiniz.",
        "description_en": "Located in one of Dalyan's most peaceful and tranquil corners, Emin'in Yeri leaves an unforgettable taste on the palate with its fresh seafood and famous homemade mezes. At tables right by the sea, you can experience one of the most natural and authentic Aegean culinary delights while watching the sunset."
    },
    "ayşe hatun sofrası": {
        "description": "Çeşme'nin tarihi dokusu içinde, anne eli değmiş gibi özenle hazırlanan ev yemeklerinin adresi olan Ayşe Hatun Sofrası, özellikle zeytinyağlıları ve el açması börekleriyle bilinir. Samimi atmosferi ve geleneksel Ege misafirperverliğiyle, kendinizi evinizde hissedeceğiniz huzurlu bir akşam yemeği noktasıdır.",
        "description_en": "Ayşe Hatun Sofrası, the address for home-cooked meals prepared with care as if by a mother's hand within Cesme's historical texture, is particularly known for its olive oil dishes and handmade pastries. With its sincere atmosphere and traditional Aegean hospitality, it is a peaceful dinner spot where you will feel at home."
    },
    "Dalyan Yelken Restoran Neco’nun Yeri": {
        "description": "Yelkenli teknelerin süzüldüğü Dalyan koyuna hakim konumuyla Neco'nun Yeri, taze ahtapot ızgarası ve yöresel deniz börülcesiyle öne çıkar. Şık ama samimi ambiyansıyla, hem kaliteli servis hem de denizin serinliğini hissetmek isteyen gezginlerin favori balık restoranlarından biridir.",
        "description_en": "Commanding a view of Dalyan bay where sailing boats glide, Neco'nun Yeri stands out with its fresh grilled octopus and local sea beans. With its chic yet sincere ambiance, it is one of the favorite fish restaurants for travelers wanting both quality service and to feel the sea breeze."
    },
    "Edo Balik": {
        "description": "Dalyanköy'ün kalbinde modern bir deniz mahsulleri deneyimi sunan Edo Balık, yaratıcı sunumları ve her gün denizden taze gelen ürünleriyle bilinir. Ege denizinin bereketini sofranıza taşıyan bu mekan, özellikle geniş şarap seçkisi ve dalga sesleri altındaki huzurlu terasıyla romantik akşamların merkezidir.",
        "description_en": "Offering a modern seafood experience in the heart of Dalyankoy, Edo Balik is known for its creative presentations and products appearing fresh from the sea every day. Bringing the abundance of the Aegean to your table, this venue is the center of romantic evenings especially with its wide wine selection and peaceful terrace under the sound of waves."
    },
    "VantuZ Çeşme Dalyanköy": {
        "description": "Dalyan sahilinde modern ve şık bir esinti sunan VantuZ, hem tazeleyici kokteylleri hem de dünya mutfağından seçkin örnekler barındıran mönüsüyle dikkat çeker. Özellikle batan güneşin ışıkları altında, denizle iç içe, kaliteli müzik eşliğinde keyifli bir akşamüstü mola yeridir.",
        "description_en": "Offering a modern and chic breeze on the Dalyan coast, VantuZ stands out with both its refreshing cocktails and a menu featuring elite examples from world cuisine. It is a pleasant late afternoon break spot intertwined with the sea under the light of the setting sun, accompanied by quality music."
    },
    "Arif'in Yeri": {
        "description": "Geleneksel Çeşme mutfağının en samimi temsilcilerinden biri olan Arif'in Yeri, Dalyan'ın huzurlu kıyısında taze balık ve sıcak ot kavurmasıyla ünlüdür. Yıllardır değişmeyen kalitesi ve güler yüzlü servisiyle, adanın yerel halkının da en çok tercih ettiği otantik lezzet noktalarından biridir.",
        "description_en": "One of the most sincere representatives of traditional Cesme cuisine, Arif'in Yeri is famous for fresh fish and warm herb roasts on the peaceful coast of Dalyan. With its unchanging quality and friendly service over the years, it is one of the most preferred authentic flavor spots by the island's local people."
    },
    "Çeşme Bahçelika Kahvaltı - Çeşme": {
        "description": "Zeytin ağaçlarının gölgesinde, kuş sesleri eşliğinde güne başlamak için Bahçelika, adanın en doğal köy kahvaltısı adreslerinden biridir. Kendi bahçelerinden topladıkları domatesler, ev yapımı peynirler ve sıcak pişi çeşitleriyle gerçek bir Ege sabahı deneyimi vaat ediyor.",
        "description_en": "To start the day in the shade of olive trees accompanied by bird sounds, Bahçelika is one of the island's most natural village breakfast addresses. It promises a real Aegean morning experience with tomatoes picked from their own gardens, homemade cheeses, and warm 'pişi' varieties."
    },
    "Bonjour Beach": {
        "description": "Çeşme'nin masmavi sularına sıfır konumuyla Bonjour Beach, konforlu güneşlenme alanları ve kristal berrak deniziyle huzurlu bir gün sunuyor. Şık tasarımı, tazeleyici içecekleri ve serinletici Ege meltemiyle, şehir kalabalığından uzaklaşıp denizin tadını çıkarmak isteyenlerin favorisidir.",
        "description_en": "Situated right at the deep blue waters of Cesme, Bonjour Beach offers a peaceful day with comfortable sunbathing areas and crystal-clear sea. With its chic design, refreshing drinks, and cooling Aegean breeze, it is a favorite for those wanting to escape city crowds and enjoy the sea."
    },
    "West Port Bar Cafe Kahvaltı": {
        "description": "Çeşme Marina'nın enerjik atmosferinde yer alan West Port, sabahları zengin kahvaltı seçenekleri, akşamları ise keyifli kokteylleriyle bilinir. Denize karşı konumu ve modern dekorasyonuyla, günün her saati şehrin nabzını tutabileceğiniz, samimi ve kaliteli bir duraktır.",
        "description_en": "Located in the energetic atmosphere of Cesme Marina, West Port is known for its rich breakfast options in the morning and pleasant cocktails in the evening. With its seafront location and modern decoration, it is a sincere and quality stop where you can catch the city's pulse at any hour of the day."
    },
    "Marina&Cafe&Pub": {
        "description": "Çeşme Marinası'nda yatların gölgesinde yer alan bu çok yönlü mekan, hem sabah kahvenizi içebileceğiniz hem de akşam şık bir pub atmosferinde eğlenebileceğiniz bir buluşma noktasıdır. Geniş içki mönüsü ve marinaya hakim manzarasıyla, kentin en sosyal ve hareketli noktalarından biridir.",
        "description_en": "Located in the shadow of yachts at Cesme Marina, this versatile venue is a meeting point where you can have your morning coffee and have fun in a chic pub atmosphere in the evening. With its wide drink menu and commanding view of the marina, it is one of the city's most social and active spots."
    },
    "Tarçın Kahvaltı & Kafe": {
        "description": "Çeşme'nin dar taş sokaklarında mis gibi kokularla sizi karşılayan Tarçın Kahvaltı, el yapımı reçelleri ve meşhur sakızlı kurabiyeleriyle ünlüdür. Nostaljik mobilyaları ve huzurlu avlusuyla, şehir keşfiniz sırasında sakin bir mola verip adanın tatlı hayatını solumak için mükemmel bir seçimdir.",
        "description_en": "Welcoming you with delightful scents in the narrow stone streets of Cesme, Tarçın Kahvaltı is famous for its homemade jams and renowned mastic cookies. With nostalgic furniture and a peaceful courtyard, it is a perfect choice to take a quiet break during your city discovery and breathe in the island's sweet life."
    },
    "Cava Roof": {
        "description": "Çeşme manzarasına tepeden bakan şık terasıyla Cava Roof, sofistike kokteylleri ve etkileyici müzik seçkisiyle şehrin en seçkin akşamüstü adreslerinden biridir. Modern tasarımı ve batan güneşi kucaklayan konumuyla, geceye elit ve keyifli bir başlangıç yapmak isteyenler için harika bir tercihtir.",
        "description_en": "With its chic terrace overlooking the Cesme view, Cava Roof is one of the city's most elite late afternoon addresses with sophisticated cocktails and an impressive music selection. With its modern design and a location embracing the setting sun, it's a great choice for those wanting an elite and pleasant start to the night."
    },
    "Cozy Time Çeşme": {
        "description": "İsmine yakışır şekilde sıcak ve samimi bir atmosfer sunan Cozy Time, taze demlenmiş kahveleri ve ev yapımı tatlılarıyla bilinir. Şehrin kalbinde küçük bir huzur adası olan bu mekan, kitap okumak veya sevdiklerinizle baş başa sohbet etmek için oldukça sessiz ve kaliteli bir konsept sunuyor.",
        "description_en": "Offering a warm and sincere atmosphere, true to its name, Cozy Time is known for freshly brewed coffees and homemade desserts. Being a small island of peace in the heart of the city, this venue offers a very quiet and quality concept for reading a book or chatting privately with loved ones."
    },
    "Aramızda Kalsın Çeşme - Yeni Nesil Meyhane": {
        "description": "Geleneksel meyhane kültürünü modern müzikler ve yenilikçi mezelerle birleştiren Aramızda Kalsın, Çeşme gecelerine yepyeni bir soluk getiriyor. Şık dekorasyonu ve her masada samimiyeti hissettiren ambiyansıyla, dostlarınızla unutulmaz bir kutlama gecesi yaşamak için adanın en popüler adreslerinden biridir.",
        "description_en": "Combining traditional tavern culture with modern music and innovative mezes, Aramızda Kalsın brings a fresh breath to Cesme nights. With its chic decoration and an ambiance that makes you feel sincerity at every table, it's one of the island's most popular addresses for an unforgettable celebration night with friends."
    },
    "Bizim Ev Kafe Ceshme": {
        "description": "Çeşme sahilinde bir aile evinin samimiyetini sunan Bizim Ev Kafe, taze ev börekleri ve serinletici limonatalarıyla ünlüdür. Denize karşı konforlu koltukları ve huzurlu sessizliğiyle, gün ortasında kendinizi evinizdeymiş gibi hissetmek ve Ege melteminin tadını çıkarmak için ideal bir duraktır.",
        "description_en": "Offering the sincerity of a family home on the Cesme coast, Bizim Ev Kafe is famous for fresh homemade pastries and refreshing lemonades. With comfortable seats against the sea and peaceful silence, it is an ideal stop to feel at home in the middle of the day and enjoy the Aegean breeze."
    },
    "Yaz gülü cafe": {
        "description": "Renkli çiçeklerle süslü bahçesi ve çocuk oyun alanıyla Yaz Gülü Kafe, özellikle ailelerin en sevdiği duraklardan biridir. Taze tıkır tıkır pişen gözlemeleri ve buz gibi ayranıyla, sıcak bir yaz gününde ağaçlar altında mola verip samimi bir Ege öğle yemeği yemek için birebirdir.",
        "description_en": "With its garden decorated with colorful flowers and a children's playground, Yaz Gülü Kafe is one of the favorite stops especially for families. With its freshly cooked 'gözleme' and icy ayran, it's perfect for taking a break under the trees on a hot summer day and eating a sincere Aegean lunch."
    },
    "Deniz kızı beach": {
        "description": "Çeşme'nin masmavi koylarından birine hakim olan Deniz Kızı Beach, kristal berraklığındaki suyu ve sakin atmosferiyle dinlendirici bir kaçış noktasıdır. Konforlu locaları, şık kumsalı ve dalga sesleri eşliğinde sunduğu hafif atıştırmalıklarıyla, tüm gün denizin ve huzurun tadını çıkarmak isteyenlerin favorisidir.",
        "description_en": "Commanding one of Cesme's deep blue bays, Deniz Kızı Beach is a relaxing escape point with crystal-clear water and a calm atmosphere. With its comfortable booths, chic sandy beach, and light snacks offered accompanied by the sound of waves, it's a favorite for those wanting to enjoy the sea and peace all day."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/cesme.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data.get('highlights', []):
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Cesme Part 2: Enriched {count} items.")
