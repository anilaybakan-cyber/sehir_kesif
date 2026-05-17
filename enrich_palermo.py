#!/usr/bin/env python3
import json

updates = {
    "ChIJRT-UYGTvGRMRxSv7Jhaj7HE": {
        "description": "Avrupa'nın en eski kraliyet sarayı olan Palazzo dei Normanni, Arap-Normal-Bizans mimarisinin muazzam bir birleşimidir. İçerisindeki göz alıcı Palatine Şapeli ve asırlık mozaikleriyle kentin görkemli geçmişine ve kültürel çeşitliliğine tanıklık edebileceğiniz, paha biçilemez bir tarihi simgedir.",
        "description_en": "The oldest royal palace in Europe, Palazzo dei Normanni is a magnificent blend of Arab-Norman-Byzantine architecture. With its stunning Palatine Chapel and centuries-old mosaics, it is a priceless historical symbol where you can witness the city's grand past and cultural diversity."
    },
    "ChIJAbBCq2XvGRMRdn8cRrtvzUc": {
        "description": "Dünyanın en sarsıcı ve gizemli yerlerinden biri olan bu katakomplar, yüzyıllar boyunca mumyalanmış binlerce bedene ev sahipliği yapıyor. Rahiplerden aristokratlara kadar farklı sosyal sınıfların giysileriyle sergilendiği bu alan, kentin ölüm ve yaşam algısına dair derin ve mistik bir yolculuk sunuyor.",
        "description_en": "One of the most poignant and mysterious places in the world, these catacombs house thousands of bodies mummified over centuries. Exhibiting different social classes from priests to aristocrats in their clothes, this area offers a deep and mystical journey into the city me's perception of life and death."
    },
    "ChIJgRiIFZPlGRMRdETtrp3lnFk": {
        "description": "Palermo'nun yeşil vahası olan bu botanik bahçesi, 18. yüzyıldan beri dünyanın dört bir yanından gelen egzotik bitkilere ev sahipliği yapıyor. Dev kaktüsleri, su zambakları ve neoklasik seralarıyla kentin koşturmacasından kaçıp doğanın huzuruyla buluşmak için kentin en havadar ve bilimsel duraklarından biridir.",
        "description_en": "The green oasis of Palermo, this botanical garden has been home to exotic plants from all over the world since the 18th century. With its giant cacti, water lilies, and neoclassical greenhouses, it's one of the city's most airy and scientific stops to escape the hustle and find nature's peace."
    },
    "ChIJx6dblGjvGRMRAQF-0AWBCrs": {
        "description": "Kuzey Afrika ve İslam mimarisinin Sicilya'daki en zarif örneklerinden biri olan Zisa Sarayı, kentin 'cennet bahçesi' olarak inşa edilmiştir. İnovatif havalandırma sistemi ve etkileyici mozaikleriyle kentin Arap etkisindeki ihtişamlı dönemini ve estetik zenginliğini anlamak için büyüleyici bir tarihi mirastır.",
        "description_en": "One of the most elegant examples of North African and Islamic architecture in Sicily, Zisa Palace was built as the city's 'paradise garden'. With its innovative ventilation system and impressive mosaics, it is a fascinating historical heritage to understand the city me's Arab-influenced grand era and aesthetic richness."
    },
    "ChIJ7QutmfLlGRMR9yogB-r7xBM": {
        "description": "Palermo limanına hakim bir konumda yükselen bu heybetli saray, Orta Çağ'ın güçlü Chiaramonte ailesinin konutu ve bir dönem Engizisyon hapishanesi olarak hizmet vermiştir. Duvarlarındaki mahkum yazıları ve kentin sosyal tarihine ışık tutan sergileriyle, kentin hafızasında derin izler bırakmış sarsıcı bir duraktır.",
        "description_en": "Rising dominantly over Palermo harbor, this imposing palace served as the residence of the powerful medieval Chiaramonte family and for a time as an Inquisition prison. With prisoner inscriptions on its walls and exhibitions shedding light on the city's social history, it is a poignant stop that left deep marks in the city's memory."
    },
    "ChIJZyhJN_TlGRMRq45_m-kIhZI": {
        "description": "Palermo'nun kültürel kalbinde yer alan Palazzo Branciforte, kentin en önemli sanat ve nümismatik koleksiyonlarına ev sahipliği yapıyor. Gae Aulenti tarafından restore edilen modern tasarımı ve tarihi kütüphanesiyle kentin geleneksel dokusunu çağdaş bir vizyonla buluşturan paha biçilemez bir sanat merkezidir.",
        "description_en": "Located in the cultural heart of Palermo, Palazzo Branciforte hosts the city's most important art and numismatic collections. It is a priceless art center bringing the city's traditional texture together with a contemporary vision through its modern design restored by Gae Aulenti and its historical library."
    },
    "ChIJx0nhgu3lGRMRXpGbOLuKCp8": {
        "description": "Deniz manzaralı bu görkemli saray, Palermo'nun aristokratik yaşamını ve modern sanat vizyonunu bir araya getiriyor. Geniş koleksiyonları, aslına uygun restore edilmiş salonları ve kentin silüetini tamamlayan heybetli cephesiyle, kentin hem dünkü hem de bugünkü kültürel gücünü yansıtan rafine bir duraktır.",
        "description_en": "This grand palace with sea views brings together Palermo's aristocratic life and modern art vision. With its wide collections, faithfully restored halls, and imposing facade completing the city silhouette, it is a refined stop reflecting both the yesterday's and today's cultural power of the city."
    },
    "ChIJve2AJlLvGRMRGxGT5xHWufI": {
        "description": "Palermo'nun modern mahallelerinden birinde yer alan villa, Sicilya'nın en önemli resim koleksiyonlarından birini barındırıyor. 18. yüzyıldan günümüze uzanan sanatsal gelişimi izleyebileceğiniz bu galeri, kentin sanata olan tutkusunu ve estetik birikimini keşfetmek isteyenler için havadar ve kaliteli bir duraktır.",
        "description_en": "Located in one of Palermo me's modern neighborhoods, the villa houses one of Sicily me's most important painting collections. This gallery where you can trace artistic development from the 18th century to today is an airy and high-quality stop for those wanting to explore the city me's passion for art and aesthetic accumulation."
    },
    "ChIJwdYMXorlGRMRTUdJoNw1MpE": {
        "description": "Palermo'nun en işlek meydanlarından biri olan Quattro Canti'nin hemen yanında yer alan bu saray, kentin asaletini ve sanatsal zenginliğini sergiliyor. Barok odaları ve nadide sanat eserleriyle kentin kozmopolit ruhunu ve estetik derinliğini kucaklayan, tarihin sessiz tanıklığını yapan muazzam bir keşif noktasıdır.",
        "description_en": "Located right next to Quattro Canti, one of Palermo me's busiest squares, this palace showcases the city me's nobility and artistic richness. It is a magnificent discovery point silently watching history, embracing the city me's cosmopolitan spirit and aesthetic depth with its Baroque rooms and rare artworks."
    },
    "ChIJ9cscy_LlGRMR0Maz86dHzxI": {
        "description": "Aristokrat Mirto ailesinin yüzyıllardır değişmeden kalan eşyalarıyla döşeli bu ev müze, kentin geçmişteki aristokratik gündelik yaşamına ışık tutuyor. Şık kristal avizeleri ve antika mobilyalarıyla kentin dünkü yüzünü en canlı haliyle görebileceğiniz, tarihin içinde donmuş gibi duran samimi bir duraktır.",
        "description_en": "Furnished with items of the aristocratic Mirto family that have remained unchanged for centuries, this house museum sheds light on the city's past aristocratic daily life. With chic crystal chandeliers and antique furniture, it is a sincere stop where you can see the city's yesterday face in its most vivid form, standing as if frozen in history."
    },
    "ChIJXXrHAxHmGRMR3Z1c7cLYjBY": {
        "description": "Palermo gece hayatının modern ve şık yüzünü temsil eden White, kentin kozmopolit enerjisini elit bir atmosferle buluşturuyor. Şık barı ve kaliteli müzik seçkisiyle bildiğimiz mekan, kentin kargaşasından uzaklaşmak ve şık bir kokteyl eşliğinde neşeli bir akşam geçirmek isteyen seçkin gezginlerin favori adresidir.",
        "description_en": "Representing the modern and stylish face of Palermo nightlife, White brings together the city me's cosmopolitan energy with an elite atmosphere. Known for its stylish bar and high-quality music selection, the venue is a favorite address for elite travelers wanting to move away from the city's chaos and spend a joyful evening accompanied by a chic cocktail."
    },
    "ChIJbfr54TvvGRMRwYr9CRd4bsE": {
        "description": "Kentin dinamik ve neşeli kulüp kültürüne yön veren Migò, etkileyici dijital tasarımları ve enerjik atmosferiyle öne çıkıyor. Dünyaca ünlü DJ'lerin ve yerel sanatçıların performanslarına ev sahipliği yapan kulüp, kentin kozmopolit enerjisini en yüksek seviyede hissetmek isteyenlerin vazgeçilmez eğlence durağıdır.",
        "description_en": "Guiding the city me's dynamic and joyful club culture, Migò stands out with its impressive digital designs and energetic atmosphere. Hosting performances by world-famous DJs and local artists, the club is an indispensable entertainment stop for those wanting to feel the city's cosmopolitan energy at its highest level."
    },
    "ChIJJ36-PGrvGRMR91Lyzp6MTDM": {
        "description": "Eski bir fabrika yerleşkesinin devasa bir kültür merkezine dönüştürülmesiyle hayata geçen bu alan, Palermo'nun sanatsal ve yaratıcı kalbi kabul ediliyor. Sinemadan tiyatroya, sergilerden atölyelere kadar kentin bohem ruhunu ve modern sanat vizyonunu en özgür haliyle soluyabileceğiniz ilham verici bir duraktır.",
        "description_en": "Brought to life by transforming an old factory complex into a massive cultural center, this area is considered the artistic and creative heart of Palermo. From cinema to theatre, exhibitions to workshops, it is an inspiring stop where you can breathe in the city's bohemian spirit and modern art vision in its freest form."
    },
    "ChIJRT-UYGTvGRMR47yr7zq9rbA": {
        "description": "Normandiya Sarayı kompleksi içinde yer alan Palatine Şapeli, altın sarısı mozaikleri ve ahşap oyma tavanıyla bir sanat şaheseridir. Hristiyan ve İslam sanatının eşsiz bir uyumunu sergileyen bu kutsal alan, kentin dinsel hoşgörüsünü ve estetik gücünü en görkemli haliyle ziyaretçilere sunuyor.",
        "description_en": "The Palatine Chapel, located within the Norman Palace complex, is an art masterpiece with its golden mosaics and wood-carved ceiling. Showcasing a unique harmony of Christian and Islamic art, this sacred space presents the city's religious tolerance and aesthetic power to its visitors in its most grand form."
    },
    "ChIJR_CcdmHvGRMRTd_ZZI9iVBA": {
        "description": "Katedralin hemen yanında yer alan bu müze, kentin dini tarihine ait paha biçilemez sanat eserlerini ve kutsal emanetleri sergiliyor. Yüzyıllara meydan okuyan klasik tabloları ve dini objeleriyle, kentin manevi ve estetik derinliğini yansıtan, sessiz ve keşfedilmeyi bekleyen bir kültürel hazinedir.",
        "description_en": "Located right next to the cathedral, this museum exhibits priceless artworks and sacred relics from the city's religious history. With classical paintings and religious objects defying centuries, it is a quiet cultural treasure waiting to be discovered, reflecting the city me's spiritual and aesthetic depth."
    },
    "ChIJnywWfKPlGRMRznBTrPXZdos": {
        "description": "Palermo'nun sanatsal mirasını modern bir bakış açısıyla sürdüren bu atölye-galeri, bronz ve mermer işçiliğinin şık örneklerini sunuyor. Yerel zanaatkarların usta ellerinden çıkan heykellerle kentin yaratıcı enerjisini hissedebileceğiniz bu mekan, kentin köklü sanat ruhunu evinize taşımak için ilham verici bir duraktır.",
        "description_en": "Sustaining Palermo's artistic heritage with a modern perspective, this workshop-gallery offers stylish examples of bronze and marble craftsmanship. This venue where you can feel the city me's creative energy with sculptures from master hands of local artisans is an inspiring stop to carry the city's deep-rooted artistic spirit home."
    },
    "ChIJs5alDWHvGRMRkJLUidllG2s": {
        "description": "Palermo Katedrali yakınındaki bu tarihi yapı, zarif sundurması ve mistik atmosferiyle kentin Orta Çağ mimarisinin önemli bir parçasıdır. Geleneksel taş işçiliği ve dini detaylarıyla kentin asude geçmişine tanıklık edebileceğiniz, kentin kozmopolit kalabalığından uzaklaşıp huzur bulabileceğiniz samimi bir tarihi duraktır.",
        "description_en": "This historical structure near Palermo Cathedral is an important part of the city me's medieval architecture with its elegant loggia and mystical atmosphere. With traditional stonework and religious details, it's a sincere historical stop where you can witness the city's serene past and find peace away from the cosmopolitan crowds."
    },
    "ChIJSWUHeZHlGRMRXKNASnI_w5E": {
        "description": "Palermo Üniversitesi bünyesinde yer alan Mineraloji Müzesi, dünyanın dört bir yanından gelen nadir taş ve kristal koleksiyonlarıyla bilim tutkunlarını bekliyor. Kükürt örneklerinden değerli taşlara kadar kentin yer altı zenginliğini ve doğanın geometrik sanatını keşfetmek isteyenler için havadar ve öğretici bir duraktır.",
        "description_en": "Located within the University of Palermo, the Mineralogy Museum awaits science enthusiasts with its rare stone and crystal collections from all over the world. It is an airy and educational stop for those wanting to explore the city me's underground richness and nature's geometric art, from sulfur samples to gemstones."
    },
    "ChIJu6MPD4vlGRMRcHsCY2PorY0": {
        "description": "Palermo Belediye Sarayı (Kartallı Saray), kentin siyasi tarihini ve idari gücünü temsil eden heybetli bir idari merkezdir. Barok mimarisi ve kentin simgesi olan kartal figürleriyle süslü cephesiyle kentin asaletini ve kentsel otoritesini yansıtan kentin en önemli anıtsal yapılarından biridir.",
        "description_en": "Palermo City Hall (Palace of the Eagles) is an imposing administrative center representing the city's political history and administrative power. With its Baroque architecture and facade decorated with the city me's symbolic eagle figures, it is one of the city me's most important monumental structures reflecting its nobility and urban authority."
    },
    "ChIJzaihqfLlGRMREqGvuMvbSdI": {
        "description": "Sicilya'nın köklü tarım tarihini ve şarap üretim kültürünü anlatan bu müze, kentin kırsal mirasını samimi bir koleksiyonla sunuyor. Antik tarım aletleri ve yerel üretim hikayeleriyle kentin sadece bir saraylar kenti değil, aynı zamanda bereketli toprakların birleşimi olduğunu gösteren bilgilendirici bir duraktır.",
        "description_en": "Telling Sicily me's deep-rooted agricultural history and wine production culture, this museum presents the city me's rural heritage with a sincere collection. It's an informative stop showing that the city is not just a city of palaces but also a combination of fertile lands with ancient agricultural tools and local production stories."
    },
    "ChIJedJCaWfvGRMRGuhexryhG-c": {
        "description": "Eski kentin tarihi dokusu içerisinde yer alan bu şık malikane, kentin kentsel gelişim sürecini ve aristokratik mimari tarzını yansıtan zarif dekoratif detaylarıyla bilinir. Taş duvarları ve nostaljik atmosferiyle kentin sosyal tarihini ve eski şehir yaşamının kalitesini hissetmek isteyenler için saklı ve havadar bir köşedir.",
        "description_en": "Located within the old town's historical texture, this stylish mansion is known for its elegant decorative details reflecting the city me's urban development process and aristocratic architectural style. With stone walls and a nostalgic atmosphere, it is a hidden and airy corner for those wanting to feel the city's social history and the quality of old town life."
    },
    "ChIJbYeXTu3lGRMRZQjz9O7I80k": {
        "description": "Sicilya Bölgesel Sanat Galerisi'ne ev sahipliği yapan bu Gotik-Katalan sarayı, adanın en önemli resim ve heykel hazinelerini barındırır. Francesco Laurana'nın büstlerinden antik triptik tablolarına kadar kentin estetik gücünü ve yüksek sanat vizyonunu soluyabileceğiniz, her köşesi tarih dolu bir sanat tapınağıdır.",
        "description_en": "Hosting the Regional Gallery of Sicily, this Gothic-Catalan palace houses the island's most important painting and sculpture treasures. From Francesco Laurana's busts to ancient triptych paintings, it is an art temple full of history at every corner where you can breathe in the city me's aesthetic power and high art vision."
    },
    "ChIJA9tkHGfvGRMRX5GpD2m4Sgw": {
        "description": "Kentin yer altı dünyasına açılan bu antik kapı ve katakomplar, kentin ilk Hristiyanlık dönemlerine ait mistik bir yolculuk vaat ediyor. Dar geçitleri ve tarihin tozunu taşıyan taşlarıyla kentin görünmeyen hafızasını ve inanç temellerini keşfetmek isteyenler için heyecan verici ve huzurlu bir arkeolojik duraktır.",
        "description_en": "This ancient gate and catacombs opening to the city me's underworld promise a mystical journey into its earliest Christian periods. With narrow passages and stones carrying the dust of history, it is an exciting and peaceful archaeological stop for those wanting to explore the city me's invisible memory and foundations of faith."
    },
    "ChIJRyFINAfmGRMRl9SucteKRu0": {
        "description": "Palermo'nun modern bilimle buluştuğu Planetario, gökyüzünün masalsı dünyasını kentin merkezinde ziyaretçilere sunuyor. Astronomi meraklıları ve aileler için harika bir keşif noktası olan merkez, evrenin derinliklerini teknolojik ve görsel bir şovla anlatarak visitörlere kentin havadar bir perspektifini kazandırıyor.",
        "description_en": "Planetario, where Palermo meets modern science, presents the fairytale world of the sky to its visitors in the city center. A great discovery point for astronomy enthusiasts and families, the center explains the depths of the universe with a technological and visual show, giving visitors an airy perspective of the city."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/palermo.json.draft'
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

print(f"✅ Palermo enriched {count} items.")
