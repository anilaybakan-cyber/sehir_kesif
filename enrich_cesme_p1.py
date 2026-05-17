#!/usr/bin/env python3
import json

updates = {
    "ChIJD1CASuR7uxQR-g5JH967nrE": {
        "description": "Çeşme Kalesi'nin eteklerinde, marinaya hakim bir konumda yer alan bu dinlenme terasları, Ege'nin serin meltemini hissederek Sakız Adası manzarasını izlemek için mükemmeldir. Modern ve konforlu oturma alanlarıyla şehir gezisine kısa bir mola vermek ve batan güneşi fotoğraflamak için idealdir.",
        "description_en": "Located at the foothills of Cesme Castle with a commanding view of the marina, these rest terraces are perfect for watching the Chios Island view while feeling the cool Aegean breeze. With modern and comfortable seating areas, it's ideal for a short break during a city tour and for photographing the sunset."
    },
    "ChIJx7Lhm997uxQRMYWCz3lwG-0": {
        "description": "Çeşme'nin yerel bir bilgi ve haber portalı olan CesmeCity, bölgenin gizli hazinelerini keşfetmek isteyen gezginler için dijital bir rehber niteliğindedir. Kentin etkinliklerinden, en popüler plajlarına ve restoranlarına kadar güncel tavsiyeler sunan bir platformdur.",
        "description_en": "CesmeCity, a local information and news portal for Cesme, acts as a digital guide for travelers wanting to discover the region's hidden treasures. It's a platform offering up-to-date recommendations ranging from city events to the most popular beaches and restaurants."
    },
    "ChIJK4KBznp7uxQRnSz6EMDJyi4": {
        "description": "Marinaya yakın bir noktada denizin hemen kıyısında yer alan bu güneşlenme terası, kristal berrak sularda serinlemek ve güneşin tadını çıkarmak isteyenler için tasarlanmıştır. Şehrin kalbinde, konforlu şezlonglar ve ferahlatıcı içecekler eşliğinde huzurlu bir gün vaat ediyor.",
        "description_en": "Located right by the sea near the marina, this sunbathing terrace is designed for those wanting to cool off in crystal-clear waters and enjoy the sun. It promises a peaceful day in the heart of the city, accompanied by comfortable loungers and refreshing drinks."
    },
    "ChIJbW-kzjR7uxQRePzi6JUW7lY": {
        "description": "Çeşme Meydanı'nda kentin tarihine ve sanatına vurgu yapan bu heykel, ziyaretçilerin buluşma noktalarından biridir. Sanatsal detaylarıyla dikkat çeken bu anıt, şehrin kültürel kimliğini yansıtırken aynı zamanda harika bir fotoğraf arka planı oluşturur.",
        "description_en": "Emphasizing the city's history and art in Cesme Square, this statue is one of the meeting points for visitors. Standing out with its artistic details, this monument reflects the city's cultural identity while also providing a great photo backdrop."
    },
    "ChIJi-57meV7uxQREbvRJ4aBSsY": {
        "description": "Eski bir Rum evinin özenle restore edilmesiyle hayata geçen Casa ARK, otantik mobilyaları ve huzurlu avlusuyla misafirlerini ağırlıyor. Tarihi dokuyu modern konforla birleştiren bu butik konaklama noktası, Çeşme'nin ruhunu derinden hissetmek isteyenler için eşsizdir.",
        "description_en": "Brought to life by the careful restoration of an old Greek house, Casa ARK welcomes guests with its authentic furniture and peaceful courtyard. This boutique accommodation point, combining historical texture with modern comfort, is unique for those wanting to feel the spirit of Cesme deeply."
    },
    "ChIJtSKg8jZ6uxQR-zI8aUUldIQ": {
        "description": "Sanatsal bir yaklaşımla tasarlanan Sato Design Hotel, her odasında farklı bir hikaye barındıran butik ve modern bir konsept sunuyor. Marinaya yakın konumu ve minimalist şıklığıyla, adada hem stil hem de huzur arayan gezginlerin favori adreslerinden biridir.",
        "description_en": "Designed with an artistic approach, Sato Design Hotel offers a boutique and modern concept with a different story in every room. With its location near the marina and minimalist elegance, it's one of the favorite addresses for travelers seeking both style and peace on the island."
    },
    "ChIJzVHtSBJ6uxQRGdrIz8CHARs": {
        "description": "Güne taze yerel ürünlerle başlamak isteyenler için Çeşme'li Butik Kafe, ev yapımı reçelleri ve meşhur boyozuyla öne çıkar. Samimi aile işletmesi atmosferi ve çiçeklerle süslü bahçesiyle, Ege kahvaltısının en otantik hallerinden birini sunuyor.",
        "description_en": "For those wanting to start the day with fresh local products, Cesme'li Boutique Cafe stands out with its homemade jams and famous boyoz. With a sincere family-run atmosphere and a garden decorated with flowers, it offers one of the most authentic versions of an Aegean breakfast."
    },
    "ChIJz36EWzF6uxQRwwCyKwSHFRg": {
        "description": "Çeşme'nin tarihi sokaklarında nostaljik bir mola yeri olan bu mekan, asırlık dokusu ve samimi atmosferiyle bilinir. Yöresel kahve çeşitleri ve hafif atıştırmalıklarıyla, şehrin tarihine tanıklık ederken gün ortasında dinlenmek için harika bir tercihtir.",
        "description_en": "A nostalgic break spot in the historical streets of Cesme, this venue is known for its century-old texture and intimate atmosphere. With local coffee varieties and light snacks, it's a great choice for resting in the middle of the day while witnessing the city's history."
    },
    "ChIJlYEJnVR7uxQRASQck6a7RKA": {
        "description": "Geleneksel sosyal yaşamın bir parçası olan bu oyun salonu, yerel halkın ve emeklilerin bir araya gelip keyifli vakit geçirdiği samimi bir mekandır. Tavla ve okey sesleri eşliğinde, Çeşme'nin en otantik ve sıcak mahalle kültürüne tanıklık edebilirsiniz.",
        "description_en": "As a part of traditional social life, this gaming hall is an intimate venue where local people and retirees come together to have a pleasant time. Accompanied by the sounds of backgammon and okey, you can witness Cesme's most authentic and warm neighborhood culture."
    },
    "ChIJt85LJQB7uxQR9yY6YmJC8e8": {
        "description": "Halkın çay ve sohbet eşliğinde sosyalleştiği bu oyun salonu, Çeşme'nin gündelik yaşamını gözlemlemek için mükemmel bir noktadır. Samimi personeli ve geleneksel havasıyla, turistlerden uzak, gerçek Ege mahalle kültürünü hissetmek isteyenler için idealdir.",
        "description_en": "This gaming hall, where people socialize with tea and conversation, is a perfect point for observing Cesme's daily life. With its sincere staff and traditional atmosphere, it's ideal for those wanting to feel the real Aegean neighborhood culture away from tourists."
    },
    "ChIJRau5l_x4uxQRzDCQfJjR1tE": {
        "description": "Alaçatı'nın kalabalığından uzak, yeşillikler içinde yer alan bu park, çocuklar için güvenli bir oyun alanı ve yetişkinler için huzurlu bir yürüyüş yolu sunuyor. Palmiye ağaçları altındaki banklarda oturup kitabınızı okuyabilir veya akşamüstü serinliğinin tadını çıkarabilirsiniz.",
        "description_en": "Located in lush greenery away from the crowds of Alacati, this park offers a safe playground for children and a peaceful walking path for adults. You can sit on benches under palm trees to read your book or enjoy the late afternoon coolness."
    },
    "ChIJkdMdP7x5uxQR4dJam-DGEx8": {
        "description": "Alaçatı'nın modern yüzünü yansıtan bu teknoloji noktası, şık tasarımı ve dijital hizmetleriyle özellikle genç gezginlerin uğrak yeridir. Şehir rehberliğinden kesintisiz bağlantıya kadar birçok imkan sunan bu merkez, tatilinizi daha planlı geçirmenize yardımcı olur.",
        "description_en": "Reflecting the modern face of Alacati, this technology point is a frequent spot for young travelers with its chic design and digital services. Offering many facilities from city guidance to uninterrupted connectivity, this center helps you spend your holiday more planned."
    },
    "ChIJD4x5VR15uxQRfYHWDD0Ul-g": {
        "description": "Geniş yeşil alanları ve spor parkurlarıyla bilinen bu park, sabah koşucuları ve doğa severlerin favorisidir. Çocuklar için modern oyun grupları ve aileler için piknik masalarıyla donatılmış olan park, şehrin içinde nefes alabileceğiniz ferah bir vaha niteliğindedir.",
        "description_en": "Known for its wide green areas and sports tracks, this park is a favorite for morning joggers and nature lovers. Equipped with modern playgrounds for children and picnic tables for families, the park serves as a spacious oasis where you can breathe inside the city."
    },
    "ChIJSarypft4uxQRjDy5BLOtjt8": {
        "description": "Su severler için macera dolu bir gün vaat eden Oasis Aquapark, farklı zorluklardaki dev kaydırakları ve geniş havuzlarıyla eğlencenin merkezidir. Aileler için güvenli alanları ve gün boyu süren animasyonlarıyla, yaz sıcağında serinlemek ve keyifli vakit geçirmek için mükemmeldir.",
        "description_en": "Promising an adventurous day for water lovers, Oasis Aquapark is the center of fun with its giant slides of different difficulties and wide pools. With safe areas for families and animations lasting all day, it's perfect for cooling off and having a pleasant time in the summer heat."
    },
    "ChIJk4uYrvl4uxQR1i2Ia24OCFc": {
        "description": "Çeşme Yarımadası'nın kalbinde yer alan bu merkezi nokta, marinası, kalesi ve tarihi çarşısıyla her gezginin rotasında mutlaka yer almalıdır. Kristal berrak koylara, Sakız Adası manzarasına ve Ege'nin en iyi tavernalarına açılan kapınız olan bu bölge, kentin ruhunu temsil eder.",
        "description_en": "Located in the heart of the Cesme Peninsula, this central point must be on every traveler's route with its marina, castle, and historical bazaar. This area, which is your gateway to crystal-clear bays, Chios Island views, and the best tavernas of the Aegean, represents the spirit of the city."
    },
    "ChIJy21xRU15uxQR4fga04JBz7k": {
        "description": "Alaçatı'nın doğal dokusunda, minimalizm ve konforu birleştiren Flu Tiny House, modern bir konaklama deneyimi sunuyor. Zeytin ağaçları ve lavanta kokuları arasındaki bahçesiyle, şehir gürültüsünden uzaklaşmak ve sakin bir Ege tatili yapmak isteyenler için harika bir sığınaktır.",
        "description_en": "In the natural texture of Alacati, Flu Tiny House offers a modern accommodation experience by combining minimalism and comfort. With its garden among olive trees and lavender scents, it is a great sanctuary for those wanting to escape city noise and have a peaceful Aegean holiday."
    },
    "ChIJR-M-vK8LTBMRaZ6m8p9D8Xo": {
        "description": "Alaçatı'nın dar ve Arnavut kaldırımlı sokaklarında yer alan bu şirin kafe, taze kumru çeşitleri ve buz gibi koruk şerbetiyle ünlüdür. Geleneksel mavi-beyaz dekorasyonu ve sokağa taşan masalarıyla, bölgenin otantik havasını solumak için en keyifli mola yerlerinden biridir.",
        "description_en": "Located in the narrow and cobbled streets of Alacati, this charming cafe is famous for its fresh kumru varieties and ice-cold koruk sherbet. With its traditional blue-and-white decoration and tables overflowing into the street, it is one of the most pleasant break spots to breathe in the region's authentic air."
    },
    "ChIJe7JgnOB4uxQRzwtuSSq8kKg": {
        "description": "Alaçatı'nın kalbinde modern ve butik bir kahve deneyimi sunan Alaçatı Cafe, taze aromalı çekirdekleri ve sağlıklı atıştırmalıklarıyla bilinir. Şık ve ferah iç tasarımıyla kitap okumak veya arkadaşlarınızla sohbet etmek için oldukça huzurlu ve kaliteli bir mekandır.",
        "description_en": "Offering a modern and boutique coffee experience in the heart of Alacati, Alacati Cafe is known for its fresh aromatic beans and healthy snacks. With its chic and spacious interior design, it is a very peaceful and quality venue for reading a book or chatting with friends."
    },
    "ChIJpeT84Bh5uxQRMcQA8x1XhxU": {
        "description": "Özellikle akşam saatlerinde canlanan enerjisiyle The Barra, kaliteli kokteylleri ve etkileyici müzik seçkisiyle Alaçatı'nın en popüler bar duraklarından biridir. Şık bar tasarımı ve samimi atmosferiyle, geceye hareketli bir başlangıç yapmak isteyenler için idealdir.",
        "description_en": "With its energy picking up especially in the evening hours, The Barra is one of the most popular bar stops in Alacati with its quality cocktails and impressive music selection. It is ideal for those wanting a lively start to the night with its chic bar design and intimate atmosphere."
    },
    "ChIJ_5y1oYt7uxQRy7SfzAtkdoE": {
        "description": "Alaçatı'nın mistik ve modern sentezini yansıran ZUM, yenilikçi mutfağı ve şık barıyla gurme gezginlerin favorisidir. Özenle seçilmiş yerel malzemelerle hazırlanan mönüsü ve gece boyu süren keyifli ambiyansıyla, özel akşam yemekleri için adanın en seçkin adreslerinden biri haline gelmiştir.",
        "description_en": "Reflecting the mystical and modern synthesis of Alacati, ZUM is a favorite for gourmet travelers with its innovative cuisine and chic bar. With its menu prepared with carefully selected local ingredients and a pleasant ambiance lasting all night, it has become one of the most elite addresses for special dinners."
    },
    "ChIJ_z9Pg2F7uxQRLAuFoYfm_7c": {
        "description": "Çeşme'nin tarihi dokusuna hakim bir noktada yer alan Nezir's Tower, muazzam kale manzarası ve nostaljik mimarisiyle dikkat çekiyor. Marinaya tepeden bakan konumu ve serin esintisiyle, akşamüstü kahvenizi içmek ve gün batımını izlemek için benzersiz bir tarihi kuledir.",
        "description_en": "Located at a point commanding Cesme's historical texture, Nezir's Tower stands out with its magnificent castle view and nostalgic architecture. With its position overlooking the marina from above and its cool breeze, it's a unique historical tower for having your late afternoon coffee and watching the sunset."
    },
    "ChIJrVqbUwB7uxQR5j-kR8POjY8": {
        "description": "Ege'nin en berrak koylarına, beyaz kumsallarına ve rüzgar sörfüne ev sahipliği yapan Çeşme Yarımadası, doğa ve lüksün harika bir birleşimidir. Her köşesinde farklı bir plaj kulübü, tarihi yel değirmenleri ve lezzetli Ege mutfağını barındıran bu bölge, Türkiye'nin en seçkin tatil rotalarından biridir.",
        "description_en": "Hosting the clearest bays of the Aegean, white sandy beaches, and windsurfing, the Cesme Peninsula is a wonderful combination of nature and luxury. Featuring a different beach club at every corner, historical windmills, and delicious Aegean cuisine, this region is one of Turkey's most elite holiday routes."
    },
    "ChIJ9-PKyG17uxQRvyFa-dPGzAs": {
        "description": "Marina'nın hemen yanı başında, modern mimari ve konforlu yaşamın simgesi olan Marinera Residence, şık tasarımıyla dikkat çekiyor. Şehrin merkezinde lüks ve sükuneti arayanlar için muazzam bir yaşam alanı sunan bu tesis, marinaya olan yakınlığıyla deniz severlerin de favorisidir.",
        "description_en": "Located right next to the Marina, Marinera Residence, a symbol of modern architecture and comfortable living, stands out with its chic design. Offering a magnificent living space for those seeking luxury and tranquility in the city center, this facility is also a favorite for sea lovers due to its proximity to the marina."
    },
    "ChIJi0vffNJxuxQRD8UjiPKJWV8": {
        "description": "Çeşme'nin en yüksek noktalarından birinde yer alan bu seyir terası, Sakız Adası ve Ege Denizi'nin 360 derecelik panaromik manzarasını sunuyor. Özellikle gün batımında gökyüzünün büründüğü renkleri izlemek ve şehri kuş bakışı fotoğraflamak isteyenler için mutlaka uğranması gereken bir noktadır.",
        "description_en": "Located at one of the highest points of Cesme, this viewing terrace offers 360-degree panoramic views of Chios Island and the Aegean Sea. It's a must-visit point for those wanting to watch the colors the sky takes especially at sunset and to photograph the city from a bird's eye view."
    },
    "ChIJH74JKQZ6uxQRILYKXds8R00": {
        "description": "Dalyan'ın huzurlu koyunda deniz ürünleri tutkunlarını ağırlayan Levent'in Yeri, taze yakalanmış balıkları ve meşhur sıcak mezeleriyle tanınır. Denize sıfır masaları ve dalga sesleri eşliğinde sunduğu samimi servis anlayışıyla, geleneksel bir Ege akşamı yaşamak isteyenlerin vazgeçilmez durağıdır.",
        "description_en": "Welcoming seafood enthusiasts in the peaceful bay of Dalyan, Levent'in Yeri is known for its freshly caught fish and famous hot mezes. With its seafront tables and sincere service provided accompanied by the sound of waves, it's an indispensable stop for those wanting an authentic Aegean evening."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/cesme.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data.get('highlights', []):
    pid = place.get('id')
    if pid in updates:
        place['description'] = updates[pid]['description']
        place['description_en'] = updates[pid]['description_en']
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Cesme Part 1: Enriched {count} items.")
