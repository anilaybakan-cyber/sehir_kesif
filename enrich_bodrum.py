#!/usr/bin/env python3
import json

updates = {
    "ChIJYw5gNEJsvhQRcRzUhvXx1Cs": {
        "description": "Bodrum'un en görkemli simgesi olan bu kale, 15. yüzyılda St. Jean Şövalyeleri tarafından inşa edilmiştir. İçerisinde dünyanın en önemli sualtı arkeoloji müzelerinden birini barındıran kale, kuleleri ve surlarıyla hem tarihin hem de Ege'nin masmavi manzarasının en iyi izlendiği noktadır.",
        "description_en": "Bodrum's most magnificent symbol, this castle was built in the 15th century by the Knights of St. John. Housing one of the world's most significant underwater archaeology museums, the castle and its towers offer the best vistas of both history and the deep blue Aegean."
    },
    "ChIJlwmXEkdsvhQR0fktlJphpF4": {
        "description": "Antik Dünyanın Yedi Harikası'ndan biri kabul edilen bu devasa anıt mezar, Karya Kralı Mausolos için inşa edilmiştir. Bugün açık hava müzesi olarak hizmet veren alan, 'Mozole' kelimesine ismini veren yapının kalıntılarıyla tarihin ihtişamlı bir dönemine tanıklık etmenizi sağlar.",
        "description_en": "Considered one of the Seven Wonders of the Ancient World, this massive tomb was built for the Carian King Mausolus. Functioning as an open-air museum today, the site allows you to witness a grand era of history with the remains of the structure that gave the word 'Mausoleum' its name."
    },
    "ChIJ_1Ko1EFsvhQR3P9pZBJXqZ4": {
        "description": "Bodrum'un denizcilik mirasını ve tekne yapım geleneğini sergileyen bu müze, kentin ruhunu anlamak için mükemmel bir duraktır. Antik çapalar, maket tekneler ve nadir deniz kabukları koleksiyonuyla Ege'nin mavi sularıyla olan köklü bağını ziyaretçilere etkileyici bir şekilde sunar.",
        "description_en": "Showcasing Bodrum's maritime heritage and boat-building traditions, this museum is a perfect stop for understanding the city's spirit. With its collection of ancient anchors, model boats, and rare seashells, it impressively presents the city's deep-rooted bond with the blue waters of the Aegean."
    },
    "ChIJBQsjnm5svhQRJz_yDJJmtw0": {
        "description": "Ünlü sanatçı Zeki Müren'in Bodrum'da yaşadığı ve son günlerini geçirdiği evi, bugün müzeye dönüştürülmüştür. Sanatçının şahsi eşyaları, ödülleri ve sahne kıyafetlerinin sergilendiği bu müze, 'Sanat Güneşi'nin Bodrum tutkusunu ve zengin sanat yaşamını yakından tanıma fırsatı sunar.",
        "description_en": "The house where the famous artist Zeki Müren lived and spent his final days in Bodrum has been converted into a museum today. Exhibiting the artist's personal items, awards, and stage costumes, this museum offers an opportunity to closely discover the 'Sun of Art's' passion for Bodrum and his rich artistic life."
    },
    "ChIJd9_mLEBsvhQR6pGYjxFgJ0o": {
        "description": "Bodrum'un kalbi sayılan tarihi Çarşı, el yapımı sandaletleri, renkli takıları ve yöresel dokumalarıyla cıvıl cıvıl bir alışveriş merkezidir. Dar sokakları, begonvillerle süslü duvarları ve otantik ambiyansıyla, kentin hem yerel hem de kozmopolit enerjisini bir arada hissetmek isteyenler için idealdir.",
        "description_en": "Bodrum's historic Bazaar, considered the heart of the city, is a vibrant shopping center with handmade sandals, colorful jewelry, and local textiles. With its narrow streets, bougainvillaea-decorated walls, and authentic ambiance, it's ideal for those wanting to feel both the local and cosmopolitan energy of the city together."
    },
    "ChIJsWAj8kFsvhQRHj1S9yF8C6Q": {
        "description": "Bodrum'un sembolü olan mandalina bahçeleri arasında yer alan bu popüler eğlence durağı, lezzetli kokteylleri ve canlı müzik performanslarıyla bilinir. Kentin sosyal yaşamının en enerjik noktalarından biri olarak, Bodrum gecelerini neşeli ve samimi bir atmosferde geçirmek isteyenlerin favorisidir.",
        "description_en": "Located among Bodrum's symbolic mandarin orchards, this popular entertainment spot is known for its delicious cocktails and live music performances. As one of the most energetic points of city social life, it's a favorite for those wanting to spend Bodrum nights in a joyful and sincere atmosphere."
    },
    "ChIJqdSVl0FsvhQRRE021bxW1MU": {
        "description": "Bodrum Kalesi içerisinde yer alan bu eşsiz müze, antik batıklardan çıkarılan paha biçilemez buluntularla dünyanın en iyilerinden biri kabul edilir. Uluburun batığı ve Doğu Roma batığı gibi tarihi eserlerle denizin derinliklerindeki binlerce yıllık ticaret ve denizcilik tarihine büyüleyici bir pencere açar.",
        "description_en": "Considered one of the best in the world, this unique museum located inside Bodrum Castle features priceless findings recovered from ancient shipwrecks. With artifacts like the Uluburun and East Roman wrecks, it opens a fascinating window into thousands of years of trade and maritime history from the depths of the sea."
    },
    "ChIJN7yup2xsvhQRj0PfOGHNJMA": {
        "description": "Bodrum'un en eski ve en otantik yapılarından biri olan tarihi Bardakçı Hamamı, yüzyıllardır süregelen Türk hamamı geleneğini modern ziyaretçilere sunuyor. Mistik atmosferi, tarihi kubbesi ve geleneksel kese-masaj hizmetiyle, gün yorgunluğunu atmak ve kültürel bir ritüeli deneyimlemek için harika bir duraktır.",
        "description_en": "One of Bodrum's oldest and most authentic structures, the historic Bardakçı Bath offers the centuries-old Turkish bath tradition to modern visitors. With its mystical atmosphere, historic dome, and traditional scrubbing-massage services, it is a great stop to relieve the day's fatigue and experience a cultural ritual."
    },
    "ChIJ6WDdOgxtvhQROLTz96uMpno": {
        "description": "Zamanın durduğu yer olarak bilinen Gümüşlük, denizin içine doğru uzanan taşları ve deniz kenarındaki meşhur balıkçılarıyla ün kazanmıştır. Antik Myndos kentinin kalıntıları üzerine kurulu olan bu balıkçı kasabası, gün batımı manzaraları ve bohem atmosferiyle adanın en huzurlu köşelerinden biridir.",
        "description_en": "Known as the place where time stands still, Gümüşlük has earned fame for its stones stretching into the sea and its renowned seaside fish restaurants. Built atop the ruins of the ancient city of Myndos, this fishing town is one of the island's most peaceful corners with its sunset views and bohemian atmosphere."
    },
    "ChIJn5ieK1FtvhQR1q1iWNs91P4": {
        "description": "Şık tasarımı ve enerjik plaj atmosferiyle tanınan bu mekan, kaliteli kokteylleri ve etkileyici DJ performanslarıyla Bodrum yazlarını renklendiriyor. Güneşin ve denizin tadını çıkarırken akşamüstü partilerine katılmak isteyen genç ve dinamik kitlenin vazgeçilmez buluşma noktalarından biridir.",
        "description_en": "Known for its chic design and energetic beach atmosphere, this venue colors Bodrum summers with quality cocktails and impressive DJ performances. It is one of the indispensable meeting points for the young and dynamic crowd wanting to enjoy the sun and sea while joining late afternoon parties."
    },
    "ChIJ89XFAVdsvhQRGo3VxmBp7SU": {
        "description": "Bodrum gece hayatının nabzını tutan bu popüler kulüp, etkileyici ses sistemleri ve özel sahne şovlarıyla eğlenceyi sabaha kadar sürdürüyor. Modern tasarımı ve dünyaca ünlü DJ performanslarıyla kentin kozmopolit enerjisini en yüksek seviyede hissedebileceğiniz iddialı bir eğlence mekanıdır.",
        "description_en": "Catching the pulse of Bodrum nightlife, this popular club continues the fun until morning with impressive sound systems and special stage shows. It is an ambitious entertainment venue where you can feel the city's cosmopolitan energy at its highest level with modern design and world-famous DJ performances."
    },
    "ChIJKYS03kVsvhQRTFlwnRjb6jo": {
        "description": "Bodrum'un denizcilik geçmişine saygı duruşu niteliğindeki bu tarihi tersane, bugün sergiler düzenlenen etkileyici bir sanat galerisine dönüşmüştür. Antik surlar altındaki mistik atmosferi ve denizle iç içe konumuyla, sanatseverlere tarihin gölgesinde ilham verici bir kültürel deneyim sunar.",
        "description_en": "A tribute to Bodrum's maritime past, this historic shipyard has today transformed into an impressive art gallery hosting exhibitions. With its mystical atmosphere under ancient walls and its location intertwined with the sea, it offers art lovers an inspiring cultural experience in the shadow of history."
    },
    "ChIJR7ZX9rRtvhQRVqh04PgpmjQ": {
        "description": "Cevat Şakir Kabaağaçlı nam-ı diğer Halikarnas Balıkçısı'na adanan bu müze, yazarın Bodrum'a olan tutkusunu ve kentin bugünkü kimliğine katkılarını sergiliyor. Şahsi eşyaları ve edebi eserleriyle Balıkçı'nın hatırasını yaşatan müze, Bodrum'un entelektüel tarihini merak edenler için mutlaka görülmesi gereken bir duraktır.",
        "description_en": "Dedicated to Cevat Şakir Kabaağaçlı, known as the Fisherman of Halicarnassus, this museum showcases the writer's passion for Bodrum and his contributions to the city's current identity. Preserving the Fisherman's memory with personal items and literary works, it is a must-see stop for those curious about its intellectual history."
    },
    "ChIJzVtejwBtvhQR9boP_8ap388": {
        "description": "Bodrum Yarımadası'nın en uç noktalarından biri olan Akyarlar, turkuaz renkli denizi ve meşhur rüzgarıyla bilinir. Karşısındaki İstanköy (Kos) adasına en yakın nokta olmasıyla bilinen bu bölge, huzurlu koyları, sörf alanları ve şirin balıkçı lokantalarıyla sakin bir Ege tatili vaat eder.",
        "description_en": "One of the farthest points of the Bodrum Peninsula, Akyarlar is known for its turquoise sea and famous winds. Being the closest point to the opposite island of Kos, this region promises a peaceful Aegean holiday with its tranquil bays, surfing areas, and charming fish restaurants."
    },
    "ChIJp7D-tZ1tvhQRMgtX5CaW6As": {
        "description": "Bodrum Müzesi'nin en etkileyici seksiyonlarından biri olan bu sergi, antik dönemden kalma gerçek bir gemi batığı üzerinden binlerce yıllık ticaret yollarını canlandırıyor. Sergilenen cam eşyalar ve antik amphoralarla deniz altı arkeolojisinin büyüleyici dünyasını ziyaretçilere derinden hissettiren kültürel bir yolculuktur.",
        "description_en": "One of the most impressive sections of the Bodrum Museum, this exhibition brings to life thousands of years of trade routes through an actual ancient shipwreck. It's a cultural journey that makes visitors deeply feel the fascinating world of submarine archaeology through exhibited glass items and ancient amphorae."
    },
    "ChIJY6eHGgBtvhQR1izXZIIzH14": {
        "description": "Bodrum Kalesi'nin görkemli ana girişi, ziyaretçileri kentin en önemli tarihi anıtına bağlayan bilet ve karşılama noktasıdır. Surların arasından geçerek tarihe ilk adımınızı attığınız bu alan, hem kentin tarihi dokusunu hem de modern biletleme konforunu bir arada sunan profesyonel bir karşılama merkezidir.",
        "description_en": "The grand main entrance of Bodrum Castle is the ticket and welcoming point connecting visitors to the city's most important historical monument. This area, where you take your first step into history by passing through the walls, is a professional welcoming center offering both historical texture and modern ticketing comfort."
    },
    "ChIJ3xrHykNsvhQRe4JG9zohK_8": {
        "description": "Karya Prensesi Ada'nın altın takıları ve lahitinin sergilendiği bu özel salon, antik Karya'nın ihtişamını gözler önüne seriyor. Bodrum Kalesi içindeki en gizemli duraklardan biri kabul edilen müze, tarihin derinliklerinden gelen kraliyet zarafetiyle ziyaretçileri eski çağların aristokratik dünyasına götürür.",
        "description_en": "Exhibiting the golden jewelry and sarcophagus of the Carian Princess Ada, this special hall brings the grandeur of ancient Caria to light. Considered one of the most mysterious stops within Bodrum Castle, the museum takes visitors into the aristocratic world of ancient times with royal elegance from the depths of history."
    },
    "ChIJXzLCWmpsvhQRqbRDZHqZIVA": {
        "description": "Bodrum'un yerel yaşamına, sosyal tarihine ve geleneksel mesleklerine ışık tutan Kent Müzesi, kentin değişim sürecini etkileyici bir koleksiyonla sergiliyor. Eski fotoğraflar, geleneksel kıyafetler ve yerel objelerle Bodrum'un bir balıkçı kasabasından dünya kentine dönüşüm hikayesine tanıklık edebilirsiniz.",
        "description_en": "City Museum, shedding light on Bodrum's local life, social history, and traditional professions, showcases the city's transformation process with an impressive collection. You can witness Bodrum's transformation story from a fishing town to a world city through old photographs, traditional costumes, and local objects."
    },
    "ChIJ3X7RgdNtvhQR3b-hCXmqRFo": {
        "description": "Antik Halikarnas'ın en kutsal yapılarından biri olan Mars Tapınağı, bugün kalıntılarıyla bile tarihin mistik gücünü hissettiren bir arkeolojik alandır. Zeytin ağaçları arasındaki sessiz konumuyla, antik çağların dini mimarisini ve kentin köklü geçmişini keşfetmek isteyenler için dingin bir duraktır.",
        "description_en": "One of ancient Halicarnassus's most sacred structures, the Temple of Mars is an archaeological site that makes you feel history's mystical power even through its remains. With its quiet location among olive trees, it is a serene stop for those wanting to explore ancient religious architecture and the city's deep-rooted past."
    },
    "ChIJs8QDpfBtvhQRsVN0gf_QnTg": {
        "description": "Bodrum'un Osmanlı döneminden kalan tarihi izlerinden biri olan bu türbe, kentin manevi ve askeri geçmişine dair önemli bir simgedir. Kale yakınlarındaki konumu ve huzurlu avlusuyla, tarihin sessiz tanıklıklarını merak eden ve kentin eski sahiplerine saygı sunmak isteyen ziyaretçiler için anlamlı bir duraktır.",
        "description_en": "One of Bodrum's historical traces from the Ottoman period, this tomb is an important symbol of the city's spiritual and military past. With its location near the castle and its peaceful courtyard, it is a meaningful stop for visitors curious about history's silent witnesses and wanting to pay respects to the city's past owners."
    },
    "ChIJoZxPh3dtvhQRiI3eN0OEs8Y": {
        "description": "Bodrum yarımadasının zengin kültürel ve tarihi mirasını farklı temalarla sunan bu butik müze, kentin yerel sanatçılarını ve arkeolojik buluntularını bir araya getiriyor. Modern sergileme teknikleriyle kentin hafızasını canlı tutan müze, Bodrum gezinize derinlik katan sessiz ve kaliteli bir eğitim durağıdır.",
        "description_en": "Presenting the Bodrum peninsula's rich cultural and historical heritage through different themes, this boutique museum brings together the city's local artists and archaeological findings. Keeping the city's memory alive with modern display techniques, it is a quiet and quality educational stop that adds depth to your Bodrum trip."
    },
    "ChIJXaB5XPVtvhQR4SoW9PBy4RI": {
        "description": "Antik Halikarnas'ın estetik mirasını modern sanatla birleştiren bu platform, Bodrum'un yaratıcı yüzünü sergileyen en şık galerilerden biridir. Yerel ve uluslararası sanatçıların eserlerine ev sahipliği yapan galeri, kentin kozmopolit ruhunu sanatın evrensel diliyle ziyaretçilere etkileyici bir şekilde sunar.",
        "description_en": "Combining ancient Halicarnassus's aesthetic heritage with modern art, this platform is one of the chicest galleries showcasing Bodrum's creative face. Hosting works by local and international artists, the gallery impressively presents the city's cosmopolitan spirit through the universal language of art to visitors."
    },
    "ChIJ03th5PVtvhQRPKhQHbpeQWc": {
        "description": "Bodrum'un dik yamaçlarına oyulmuş olan bu antik kaya mezarları, Karya döneminin ölü gömme geleneklerini ve kentin köklü nekropol geçmişini yansıtır. Tarihin sessiz ve vakur bekçileri gibi yükselen bu mezarlar, antik kentin sınırlarını ve eski çağların saygınlık anlayışını keşfetmek için benzersiz bir noktadır.",
        "description_en": "These ancient rock tombs carved into Bodrum's steep slopes reflect the Carian period's burial traditions and the city's deep-rooted necropolis past. Rising like silent and dignified guardians of history, these tombs are a unique point for exploring the boundaries of the ancient city and the ancient world's sense of dignity."
    },
    "ChIJ4WVjYlttvhQRctLEnHWMBos": {
        "description": "Bodrum ve Gümbet koylarını birbirinden ayıran tepede gururla yükselen bu tarihi yel değirmenleri, kentin en fotojenik manzaralarını sunuyor. Yel değirmenlerinin arasından batan güneşi izlemek ve harika panoramik fotoğraflar çekmek için kentin en havadar ve huzurlu noktalarından biridir.",
        "description_en": "Proudly rising on the hill separating the bays of Bodrum and Gümbet, these historical windmills offer the city's most photogenic views. It's one of the city me's most airy and peaceful spots for watching the sunset among the windmills and taking great panoramic photos."
    },
    "ChIJCzyhazJsvhQRzI8CRd-TFAs": {
        "description": "Ünlü ressam Kadir Akorak'ın Bodrum'un otantik dokusunda yer alan çalışma alanı, sanatın en doğal ve samimi hallerine tanıklık etme fırsatı sunuyor. Sanatçının özgün üslubunu yansıtan eserlerin yaratım sürecini görebileceğiniz bu atölye, kentin bohem ruhunu ve yaratıcı enerjisini hissetmek isteyenler için ilham vericidir.",
        "description_en": "The workspace of famous painter Kadir Akorak, located in Bodrum's authentic texture, offers an opportunity to witness art in its most natural and sincere forms. This workshop, where you can see the creation process of works reflecting the artist's unique style, is inspiring for those wanting to feel the city's bohemian spirit and creative energy."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/bodrum.json.draft'
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

print(f"✅ Bodrum enriched {count} items.")
