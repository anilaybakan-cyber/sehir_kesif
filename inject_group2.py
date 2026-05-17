#!/usr/bin/env python3
import os

TARGET_FILE = "lib/services/city_blog_content.dart"

# DUBROVNIK
DUB_TR = r"""
  // DUBROVNIK
  static const _dubrovnikTR = '''
# Dubrovnik: Adriyatik'in İncisi, Taşın ve Mavinin Şehri

**Hızlı Bakış:** Dubrovnik, Orta Çağ'ın ruhunu günümüze taşıyan, surlarla çevrili bir masal şehridir. "Game of Thrones"un King's Landing'i olarak da bilinen bu şehir, kiremit kırmızısı çatıları ve Adriyatik'in kristal mavisi sularıyla büyüleyicidir. Stradun caddesinin pürüzsüz taşlarında yürürken tarihin fısıltılarını duyabilir, surların üzerinden şehri izlerken dünyanın en güzel manzaralarından birine tanıklık edebilirsiniz.

**📝 Gitmeden Önce:**
- **Merdivenlere Hazırlanın:** Dubrovnik, özellikle eski şehir (Old Town) bölgesi çok fazla merdiven barındırır. Rahat bir ayakkabı olmazsa olmazdır.
- **Kredi Kartı Yaygın:** Şehirde kredi kartı kullanımı oldukça yaygındır ancak küçük kafelerde veya hediyelik eşyacılarda nakit (Euro) gerekebilir.
- **Kalabalık Kontrolü:** Kruvaziyer gemilerinin yanaştığı saatlerde şehir çok kalabalık olabilir. Mümkünse erken sabah veya geç akşam saatlerini keşif için ayırın.

## 📅 Takviminizi Ayarlayın

- **İlkbahar (Mayıs-Haziran):** Hava ılıman, doğa yemyeşil ve kalabalık henüz zirveye ulaşmamıştır. En keyifli zamandır.
- **Yaz (Temmuz-Ağustos):** Şehrin en canlı ve en sıcak dönemi. Yaz Festivali ile sanat her köşe başındadır.
- **Sonbahar (Eylül-Ekim):** Denizin hala girilebilir sıcaklıkta olduğu ve turist yoğunluğunun azaldığı dönem.
- **Kış (Kasım-Nisan):** Şehrin yerellere kaldığı, rüzgarlı ve melankolik bir dönem. Noel zamanı ışıklandırmalar harikadır.

## 🏠 Nerede Kalmalı

- **Old Town (Eski Şehir):** Tarihin tam kalbinde, her yere yürüme mesafesinde olmak isteyenler için.
- **Ploce:** Eski şehrin hemen dışında, muazzam kale ve deniz manzaralı lüks otellerin olduğu bölge.
- **Lapad:** Daha modern, plajlara yakın ve aileler için ideal, sakin bölge.
- **Babin Kuk:** Geniş otel komplekslerinin ve yeşil alanların olduğu lüks yarımada.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Eski şehir içinde araç trafiği yoktur, keşfetmenin tek yolu yürümektir.
- **Otobüs:** Şehir içi ulaşım ağı (Libertas) oldukça düzenlidir ve her yere ulaşım sağlar.
- **Teleferik:** Srd Dağı'na çıkıp şehri tepeden izlemek için tek seçenek.
- **Tekne:** Lokrum Adası'na veya Elafiti Adaları'na gitmek için limandan kalkan tekneler.

## 🏛️ İkonik Duraklar

1. **Şehir Surları:** Şehri 2 km boyunca çevreleyen, Adriyatik'in en görkemli savunma hattı.
2. **Stradun (Placa):** Eski şehri boydan boya kat eden, cilalı taşlarıyla meşhur ana cadde.
3. **Lovrijenac Kalesi:** Şehrin hemen dışında, kayalıkların üzerine kurulu "Dubrovnik'in Cebelitarık'ı".
4. **Rektör Sarayı:** Gotik-Rönesans mimarisinin en güzel örneği, eski yönetim merkezi.
5. **Lokrum Adası:** Eski şehirden 10 dakikalık tekne yolculuğu mesafesinde, tavus kuşlarının ve botanik bahçelerin olduğu huzur adası.
6. **Srd Dağı:** Teleferikle çıkılan, Dubrovnik silüetini en iyi görebileceğiniz tepe nokta.

## 🍽️ Lezzet Haritası

- **Sabah:** Yerel fırınlardan (Pekara) taze börekler veya şık kafelerde kahve.
- **Öğle:** Deniz kıyısındaki restoranlarda "Black Risotto" (mürekkep balıklı pilav).
- **Akşam:** Eski şehrin dar sokaklarında taze deniz ürünleri ve yerel Hırvat şarapları.
- **Tatlı:** Dubrovnik'in meşhur sütlü tatlısı "Rozata".

## 🔍 Lokal Sırlar

- **Buza Bar:** Surların dışındaki kayalıklara kurulmuş, kapısı duvarda gizli, denize karşı bir kadeh bira için en iyi nokta.
- **Pasjaca Plajı:** Şehrin biraz dışında, kayaların içinden geçilerek ulaşılan gizli ve muhteşem bir plaj.
- **Mağara Bar (Cave Bar More):** Lapad bölgesinde doğal bir mağaranın içinde kokteyl yudumlayın.
''';
"""

DUB_EN = r"""  static const _dubrovnikEN = '''
# Dubrovnik: The Pearl of the Adriatic, A City of Stone and Blue

**Quick Glimpse:** Dubrovnik is a walled fairytale city that carries the spirit of the Middle Ages to the present day. Also known as King's Landing from "Game of Thrones," this city is mesmerizing with its terracotta roofs and the crystal blue waters of the Adriatic. While walking on the smooth stones of Stradun Street, you can hear the whispers of history, and while watching the city from the walls, you can witness one of the most beautiful views in the world.

**📝 Before You Go:**
- **Prepare for Stairs:** Dubrovnik, especially the Old Town area, contains a lot of stairs. Comfortable shoes are a must.
- **Credit Cards Widely Accepted:** Credit card use is common, but cash (Euro) may be needed in small cafes or souvenir shops.
- **Crowd Control:** The city can get very crowded when cruise ships dock. If possible, reserve early morning or late evening hours for exploration.

## 📅 Set Your Calendar

- **Spring (May-June):** The weather is mild, nature is green, and the crowds haven't reached their peak. The most enjoyable time.
- **Summer (July-August):** The liveliest and hottest period of the city. Art is at every corner with the Summer Festival.
- **Autumn (September-October):** The period when the sea is still warm enough for swimming and the tourist density decreases.
- **Winter (November-April):** A windy and melancholic period when the city belongs to locals. The lights at Christmas are wonderful.

## 🏠 Where to Stay

- **Old Town:** For those who want to be in the heart of history, within walking distance of everywhere.
- **Ploce:** The area just outside the old city with luxury hotels offering magnificent castle and sea views.
- **Lapad:** A more modern, quiet area close to beaches and ideal for families.
- **Babin Kuk:** A luxury peninsula with large hotel complexes and green areas.

## 🚲 Getting Around

- **Walking:** There is no vehicle traffic in the old city; walking is the only way to explore.
- **Bus:** The urban transport network (Libertas) is very organized and provides access everywhere.
- **Cable Car:** The only option to go up Mount Srd and watch the city from above.
- **Boat:** Boats departing from the harbor to go to Lokrum Island or the Elafiti Islands.

## 🏛️ Iconic Stops

1. **City Walls:** The most magnificent defense line of the Adriatic, surrounding the city for 2 km.
2. **Stradun (Placa):** The main street famous for its polished stones, crossing the old city from end to end.
3. **Lovrijenac Fortress:** "Dubrovnik's Gibraltar," built on the rocks just outside the city.
4. **Rector's Palace:** The best example of Gothic-Renaissance architecture, the old administrative center.
5. **Lokrum Island:** A peaceful island with peacocks and botanical gardens, 10 minutes by boat from the old city.
6. **Mount Srd:** The peak point where you can see the Dubrovnik silhouette best, accessible by cable car.

## 🍽️ Flavor Map

- **Morning:** Fresh pastries from local bakeries (Pekara) or coffee in chic cafes.
- **Lunch:** "Black Risotto" (cuttlefish rice) in seaside restaurants.
- **Evening:** Fresh seafood and local Croatian wines in the narrow streets of the old city.
- **Sweet:** "Rozata," Dubrovnik's famous custard dessert.

## 🔍 Local Secrets

- **Buza Bar:** Built on the rocks outside the walls, with its door hidden in the wall; the best spot for a glass of beer against the sea.
- **Pasjaca Beach:** A hidden and magnificent beach accessible through the rocks, slightly outside the city.
- **Cave Bar More:** Sip a cocktail inside a natural cave in the Lapad area.
''';
"""

# MYKONOS
MYK_TR = r"""
  // MYKONOS
  static const _mykonosTR = '''
# Mykonos: Ege'nin Işıltılı ve Kozmopolit Kalbi

**Hızlı Bakış:** Mykonos, Kyklad mimarisinin en saf haliyle dünya standartlarında eğlenceyi birleştiren eşsiz bir adadır. Labirent gibi uzanan bembeyaz sokakları, deniz üzerine kurulmuş "Küçük Venedik" evleri ve rüzgara meydan okuyan yel değirmenleriyle burası bir görsel şölendir. Gündüzleri turkuaz plajlarda güneşin tadını çıkarırken, geceleri dünyanın en ünlü DJ'lerinin performanslarıyla adanın bitmek bilmeyen enerjisine kapılabilirsiniz.

**📝 Gitmeden Önce:**
- **Rüzgara Dikkat:** Mykonos "Rüzgarların Adası" olarak bilinir. Kuzeyden esen "Meltemi" rüzgarı yazın ferahlatıcı olsa da bazen çok şiddetli olabilir.
- **Fiyat Seviyesi:** Mykonos, Yunan adalarının en pahalısıdır. Özellikle popüler plajlar ve restoranlar için bütçenizi önceden planlayın.
- **Ulaşım:** Adada taksi bulmak oldukça zordur. Araç veya ATV kiralamak en popüler ve pratik yöntemdir.

## 📅 Takviminizi Ayarlayın

- **İlkbahar (Mayıs-Haziran başı):** Adanın en taze zamanı. Kalabalık az, fiyatlar daha makul.
- **Yaz (Temmuz-Ağustos):** Eğlencenin zirve yaptığı, plajların dolup taştığı, adanın hiç uyumadığı dönem.
- **Sonbahar (Eylül-Ekim):** Rüzgarın dindiği, denizin hala sıcak olduğu, huzurlu ve lüks dönem.
- **Kış:** Adanın tamamen sessizliğe büründüğü, çoğu işletmenin kapalı olduğu sakin dönem.

## 🏠 Nerede Kalmalı

- **Chora (Mykonos Town):** Gece hayatına, alışverişe ve restoranlara yakın olmak isteyenler için.
- **Ornos:** Aileler için uygun, sakin plajı ve şık otelleriyle popüler bölge.
- **Platis Gialos:** En iyi plajlara doğrudan erişim sunan, lüks otellerin olduğu sahil şeridi.
- **Ano Mera:** Adanın iç kısımlarında, daha yerel ve ekonomik bir konaklama arayanlar için.

## 🚲 Şehir İçi Ulaşım

- **ATV/Scooter:** Mykonos'un dar yollarında en esnek ve popüler ulaşım şekli.
- **Otobüs:** Fabrika Meydanı'ndan popüler plajlara giden düzenli otobüs seferleri mevcuttur.
- **Su Taksisi:** Plajlar arası ulaşımı sağlayan keyifli deniz motorları.
- **Taksi:** Sınırlı sayıdadır, önceden telefonla çağırmak veya duraklarda beklemek gerekir.

## 🏛️ İkonik Duraklar

1. **Little Venice (Küçük Venedik):** Denize sıfır balkonlu evlerin olduğu, gün batımı kokteyllerinin vazgeçilmez adresi.
2. **Kato Mili (Yel Değirmenleri):** Adanın en çok fotoğraflanan, denize hakim tepedeki tarihi değirmenler.
3. **Panagia Paraportiani:** Eşsiz mimarisiyle bembeyaz bir sanat eseri gibi duran tarihi kilise.
4. **Delos Adası:** UNESCO mirasındaki antik kente günübirlik tekne yolculuğu.
5. **Nammos veya Scorpios:** Dünya çapında ünlü beach club deneyimi.
6. **Armenistis Feneri:** Adanın en kuzey ucunda, ıssız ve muazzam bir manzara sunan tarihi fener.

## 🍽️ Lezzet Haritası

- **Sabah:** Chora'nın ara sokaklarındaki fırınlardan yerel "Amigdalota" (bademli kurabiye).
- **Öğle:** Plajlardaki şık restoranlarda taze kalamar ve Yunan salatası.
- **Akşam:** Küçük Venedik'te taze ıstakozlu makarna veya Ano Mera'da yerel et yemekleri.
- **Meze:** Mykonos'un meşhur acılı peyniri "Kopanisti".

## 🔍 Lokal Sırlar

- **Agios Sostis Plajı:** Hiçbir işletmenin olmadığı, adanın en doğal ve bakir plajlarından biri.
- **Kiki's Tavern:** Elektriğin olmadığı, yemeklerin ızgarada piştiği, sıra beklemenize değecek efsanevi restoran.
- **Kapari Plajı:** Gün batımını kalabalıktan uzak izleyebileceğiniz gizli bir koy.
''';
"""

MYK_EN = r"""  static const _mykonosEN = '''
# Mykonos: The Radiant and Cosmopolitan Heart of the Aegean

**Quick Glimpse:** Mykonos is a unique island that combines the purest Cycladic architecture with world-class entertainment. Its labyrinthine white streets, "Little Venice" houses built over the sea, and windmills defying the wind are a visual feast. While enjoying the turquoise beaches by day, you can lose yourself in the island's endless energy with performances by the world's most famous DJs at night.

**📝 Before You Go:**
- **Beware of Wind:** Known as the "Island of the Winds," the "Meltemi" wind from the north is refreshing in summer but can sometimes be very strong.
- **Price Level:** Mykonos is the most expensive of the Greek islands. Plan your budget in advance, especially for popular beaches and restaurants.
- **Transport:** Taxis are very scarce. Renting a car or ATV is the most popular and practical method.

## 📅 Set Your Calendar

- **Spring (May-early June):** The island's freshest time. Fewer crowds, more reasonable prices.
- **Summer (July-August):** The peak of fun, when beaches overflow and the island never sleeps.
- **Autumn (September-October):** The peaceful and luxurious period when the wind dies down and the sea is still warm.
- **Winter:** A quiet period when the island falls completely silent and most businesses are closed.

## 🏠 Where to Stay

- **Chora (Mykonos Town):** For those who want to be close to nightlife, shopping, and restaurants.
- **Ornos:** A popular area for families, with its calm beach and chic hotels.
- **Platis Gialos:** A coastline with luxury hotels offering direct access to the best beaches.
- **Ano Mera:** For those seeking more local and affordable accommodation in the inland parts of the island.

## 🚲 Getting Around

- **ATV/Scooter:** The most flexible and popular way of transport in Mykonos' narrow roads.
- **Bus:** Regular bus services are available from Fabrika Square to popular beaches.
- **Water Taxi:** Pleasant sea boats providing transport between beaches.
- **Taxi:** Limited in number; you need to call by phone or wait at stands.

## 🏛️ Iconic Stops

1. **Little Venice:** The indispensable address for sunset cocktails, with its seafront balcony houses.
2. **Kato Mili (Windmills):** The island's most photographed historical mills on the hill overlooking the sea.
3. **Panagia Paraportiani:** A historic church standing like a pure white work of art with its unique architecture.
4. **Delos Island:** A day boat trip to the UNESCO heritage ancient city.
5. **Nammos or Scorpios:** A world-renowned beach club experience.
6. **Armenistis Lighthouse:** A historic lighthouse at the northernmost tip of the island, offering a desolate and magnificent view.

## 🍽️ Flavor Map

- **Morning:** Local "Amigdalota" (almond cookies) from bakeries in Chora's side streets.
- **Lunch:** Fresh squid and Greek salad in chic seaside restaurants.
- **Evening:** Fresh lobster pasta in Little Venice or local meat dishes in Ano Mera.
- **Appetizer:** Mykonos' famous spicy cheese "Kopanisti."

## 🔍 Local Secrets

- **Agios Sostis Beach:** One of the island's most natural and pristine beaches with no facilities.
- **Kiki's Tavern:** A legendary restaurant where there is no electricity and food is cooked on the grill; it's worth the wait.
- **Kapari Beach:** A hidden bay where you can watch the sunset away from the crowds.
''';
"""

# RHODES
RHO_TR = r"""
  // RHODES
  static const _rhodesTR = '''
# Rodos: Şövalyelerin ve Güneşin Adası

**Hızlı Bakış:** Rodos, Orta Çağ atmosferini modern bir tatil anlayışıyla harmanlayan, Ege'nin en büyük adalarından biridir. UNESCO listesindeki surlarla çevrili Eski Şehri (Old Town), adeta bir zaman tüneli gibidir. Bir yanda şövalye kaleleri ve dar taş sokaklar, diğer yanda Lindos'un bembeyaz evleri ve masmavi koyları... Rodos, her köşesinde farklı bir kültürel katman barındıran, güneş tanrısı Helios'un evi olarak anılan büyüleyici bir adadır.

**📝 Gitmeden Önce:**
- **Ayakkabı Seçimi:** Eski Şehrin "Pebble" (çakıl taşı) döşeli yolları topuklu veya ince tabanlı ayakkabılar için uygun değildir.
- **Lindos Ziyareti:** Lindos köyü adanın en popüler noktasıdır. Sıcaklardan ve kalabalıktan kaçmak için sabah çok erken saatlerde gitmelisiniz.
- **Araç Kiralama:** Ada çok büyüktür. Gizli koyları ve dağ köylerini keşfetmek için araç kiralamak en iyi seçenektir.

## 📅 Takviminizi Ayarlayın

- **İlkbahar:** Adanın en yeşil ve çiçekli dönemi. Eski şehir yürüyüşleri için ideal sıcaklık.
- **Yaz:** Plajların ve gece hayatının en canlı olduğu, adanın tam kapasite çalıştığı dönem.
- **Sonbahar (Eylül-Ekim):** Rüzgarın dindiği, denizin ısındığı ve kalabalıkların çekildiği en güzel zaman.
- **Kış:** Adanın yerel hayatına döndüğü, sakin ve otantik dönem.

## 🏠 Nerede Kalmalı

- **Rhodes Town (Eski Şehir):** Orta Çağ atmosferini 24 saat yaşamak isteyen tarih tutkunları için.
- **Lindos:** Beyaz badanalı evlerde konaklayıp, Akropolis manzarasına uyanmak isteyenler için.
- **Faliraki:** Gençler ve eğlence arayanlar için canlı gece hayatı olan bölge.
- **Kolymbia:** Daha huzurlu, aileler ve resort otel sevenler için ideal orta nokta.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Eski şehir içinde ulaşımın tek yolu.
- **Otobüs:** Adanın kuzey ve güney hattına giden iki farklı ana otobüs terminali mevcuttur.
- **Taksi:** Şehir içinde yaygındır ancak köyler arası ulaşımda sabitleştirilmiş fiyatları sormanızda fayda var.
- **Tekne:** Mandraki limanından kalkan teknelerle çevre koylara veya Simi adasına günübirlik turlar.

## 🏛️ İkonik Duraklar

1. **Büyük Üstatlar Sarayı:** Eski şehrin en görkemli yapısı, şövalyelerin yönetim merkezi.
2. **Şövalyeler Caddesi:** Orta Çağ'dan günümüze bozulmadan gelmiş, her ülkenin kendi hanının bulunduğu cadde.
3. **Lindos Akropolü:** Beyaz köyün tepesinde yükselen, muazzam bir manzara sunan antik tapınak.
4. **Mandraki Limanı:** Girişinde eskiden Rodos Heykeli'nin durduğuna inanılan, geyik heykelleriyle ünlü liman.
5. **Kelebekler Vadisi:** Binlerce kelebeğin toplandığı, ağaçlar ve akarsular arasındaki doğa harikası.
6. **Anthony Quinn Koyu:** Filmin çekildiği, turkuaz rengiyle meşhur ikonik koy.

## 🍽️ Lezzet Haritası

- **Sabah:** Eski şehirde taze "Bougatsa" (kremalı börek).
- **Öğle:** Deniz kenarındaki tavernalarda "Grilled Octopus" (ızgara ahtapot).
- **Akşam:** Köy meydanlarında yerel Rodos yemeği olan "Pitaroudia" (nohut köftesi).
- **İçecek:** Rodos'un meşhur şarapları ve "Souma" (yerel içki).

## 🔍 Lokal Sırlar

- **Prasonisi:** Adanın en güney ucunda, Ege ve Akdeniz'in birleştiği, sörfçülerin cenneti olan kum şeridi.
- **Yedi Pınarlar (Epta Piges):** Serinlemek için buz gibi suyun içinden geçen karanlık tünelde yürüme deneyimi.
- **Monolithos Kalesi:** Gün batımını kalabalıktan uzak, sarp bir kayalığın üzerindeki kaleden izleyin.
''';
"""

RHO_EN = r"""  static const _rhodesEN = '''
# Rhodes: Island of Knights and the Sun

**Quick Glimpse:** Rhodes is one of the largest islands in the Aegean, blending a medieval atmosphere with a modern holiday approach. Its UNESCO-listed, walled Old Town is like a time tunnel. On one side are knightly castles and narrow stone alleys; on the other, the white houses and deep blue bays of Lindos. Rhodes is a fascinating island hosting different cultural layers at every corner, known as the home of the sun god Helios.

**📝 Before You Go:**
- **Shoe Selection:** The pebble-paved roads of the Old Town are not suitable for heels or thin-soled shoes.
- **Lindos Visit:** Lindos village is the most popular point of the island. You should go in the early morning to avoid the heat and crowds.
- **Car Rental:** The island is very large. Renting a car is the best option to explore hidden bays and mountain villages.

## 📅 Set Your Calendar

- **Spring:** The island's greenest and most flowery period. Ideal temperature for Old Town walks.
- **Summer:** The peak period when beaches and nightlife are liveliest and the island works at full capacity.
- **Autumn (September-October):** The best time when the wind dies down, the sea warms up, and the crowds withdraw.
- **Winter:** A quiet and authentic period when the island returns to its local life.

## 🏠 Where to Stay

- **Rhodes Town (Old Town):** For history buffs who want to live the medieval atmosphere 24 hours a day.
- **Lindos:** For those who want to stay in white-washed houses and wake up to the view of the Acropolis.
- **Faliraki:** A vibrant area for young people and entertainment seekers.
- **Kolymbia:** A more peaceful, ideal midpoint for families and resort hotel lovers.

## 🚲 Getting Around

- **Walking:** The only way to get around in the Old Town.
- **Bus:** There are two different main bus terminals for the north and south lines of the island.
- **Taxi:** Common in the city; however, it's useful to ask for fixed prices for travel between villages.
- **Boat:** Day trips from Mandraki harbor to surrounding bays or Symi island.

## 🏛️ Iconic Stops

1. **Palace of the Grand Master:** The most magnificent structure of the Old Town, the administrative center of the knights.
2. **Street of the Knights:** A street that has come down from the Middle Ages to the present day intact, where each nation had its own inn.
3. **Lindos Acropolis:** An ancient temple rising above the white village, offering a magnificent view.
4. **Mandraki Harbor:** Famous for its deer statues, where the Colossus of Rhodes was believed to have stood.
5. **Valley of the Butterflies:** A natural wonder where thousands of butterflies gather among trees and streams.
6. **Anthony Quinn Bay:** The iconic bay famous for its turquoise color where the movie was filmed.

## 🍽️ Flavor Map

- **Morning:** Fresh "Bougatsa" (custard pastry) in the Old Town.
- **Lunch:** "Grilled Octopus" at seaside tavernas.
- **Evening:** "Pitaroudia" (chickpea fritters), a local Rhodes dish in village squares.
- **Drink:** Famous Rhodes wines and "Souma" (local spirit).

## 🔍 Local Secrets

- **Prasonisi:** A sandbar at the southernmost tip of the island where the Aegean and Mediterranean meet, a paradise for surfers.
- **Seven Springs (Epta Piges):** Walking through a dark tunnel in ice-cold water to cool off.
- **Monolithos Castle:** Watch the sunset from the castle on a steep rock, away from the crowds.
''';
"""

# MIDILLI
MID_TR = r"""
  // MIDILLI
  static const _midilliTR = '''
# Midilli (Lesvos): Ege'nin Otantik ve Huzurlu Dev Adası

**Hızlı Bakış:** Midilli, Yunanistan'ın üçüncü büyük adası olmasına rağmen turizmin bozamadığı nadir yerlerden biridir. Uçsuz bucaksız zeytin ormanları, dünyaca ünlü uzo fabrikaları ve taş binalarıyla bezeli köyleriyle burası gerçek bir Ege deneyimi sunar. Molyvos'un kalesi altındaki masalsı sokaklarından Plomari'nin uzo kokulu limanına, Skala Eressos'un özgürlükçü plajlarından Petra'nın kaya üzerindeki kilisesine kadar her köşesinde samimiyet bulursunuz.

**📝 Gitmeden Önce:**
- **Araç Şart:** Ada çok büyüktür. Bir ucundan diğerine gitmek 2-3 saat sürebilir. Keşfetmek için araç kiralamak kaçınılmazdır.
- **Uzo Başkenti:** Dünyanın en iyi uzolarının üretildiği yer burasıdır. Plomari'deki müzeleri ziyaret etmeden dönmeyin.
- **Yollar Virajlı:** Ada dağlık bir yapıya sahiptir, yollar genellikle virajlıdır. Sürüş sırasında dikkatli olunmalı.

## 📅 Takviminizi Ayarlayın

- **İlkbahar:** Zeytin çiçeklerinin kokusu ve yeşilin her tonu. Doğa yürüyüşleri için en iyi zaman.
- **Yaz:** Adanın en canlı dönemi. Her köyde düzenlenen "Panigiri" (yerel festivaller) mutlaka deneyimlenmeli.
- **Sonbahar (Eylül):** Hasat zamanı başlangıcı. Hava hala sıcak, deniz dingin.
- **Kış:** Adanın tamamen kendine döndüğü, uzo ve balıkçı masalarının sıcaklığında geçen dönem.

## 🏠 Nerede Kalmalı

- **Molyvos (Mithymna):** Adanın en ikonik ve turistik köyü. Romantik bir konaklama arayanlar için.
- **Plomari:** Uzo kültürünün kalbinde, deniz kenarında samimi bir atmosfer isteyenler için.
- **Petra:** Molyvos'a yakın, geniş kumsalı ve şirin çarşısıyla popüler nokta.
- **Mytilene (Merkez):** Daha kentsel, alışverişe ve limana yakın olmak isteyenler için.

## 🚲 Şehir İçi Ulaşım

- **Araç Kiralama:** Adada özgürce hareket etmek için tek gerçek seçenek.
- **Otobüs:** Merkezden ana köylere giden otobüsler vardır ancak sefer sayıları sınırlıdır.
- **Taksi:** Kasabalar arası ulaşımda pahalı bir seçenek olabilir.
- **Yürümek:** Köy içlerini keşfetmek için en keyifli yöntem.

## 🏛️ İkonik Duraklar

1. **Molyvos Kalesi ve Sokakları:** Arnavut kaldırımlı, begonvilli sokaklardan tepedeki kaleye uzanan yolculuk.
2. **Plomari Uzo Müzesi (Barbayanni):** Uzun uzo tarihini keşfedebileceğiniz dünyaca ünlü müze.
3. **Taşlaşmış Orman (Sigri):** Milyonlarca yıl öncesinden kalma, dünyada nadir bulunan fosil ormanı.
4. **Petra Kilisesi (Panagia Glykofilousa):** 114 basamakla çıkılan, bir kaya üzerine kurulu efsanevi kilise.
5. **Agiasos Köyü:** Olimpos Dağı eteklerinde, el sanatları ve otantik kahveleriyle ünlü dağ köyü.
6. **Mor Taksi Yarımadası:** Issız ve doğal güzelliğiyle bilinen kuzey kıyıları.

## 🍽️ Lezzet Haritası

- **Sabah:** Agiasos'ta közde pişmiş Yunan kahvesi ve yerel helvalar.
- **Öğle:** Liman tavernalarında güneşte kurutulmuş ızgara ahtapot (Lakerda).
- **Akşam:** Plomari'de uzo eşliğinde yerel peynirler (Ladotyri) ve deniz ürünleri.
- **Meze:** Midilli'nin meşhur "Kalloni Sardalyası".

## 🔍 Lokal Sırlar

- **Eftalou Termal Kaynakları:** Deniz kıyısında, tarihi hamamın içinde veya hemen dışındaki doğal kaynaklarda serinleme.
- **Skala Sikamineas:** Deniz içindeki küçük beyaz kilisesi (Mermaid Madonna) ile adanın en romantik balıkçı köyü.
- **Man 'Atsa Plajı:** Sadece yerlilerin bildiği, sığ ve kristal suyuyla gizli bir koy.
''';
"""

MID_EN = r"""  static const _midilliEN = '''
# Mytilene (Lesvos): The Authentic and Peaceful Giant of the Aegean

**Quick Glimpse:** Although Lesvos is the third-largest island in Greece, it remains one of the rare places untainted by mass tourism. It offers a true Aegean experience with its vast olive forests, world-famous ouzo factories, and villages adorned with stone buildings. You'll find sincerity at every corner, from the fairytale streets under the castle of Molyvos to the ouzo-scented harbor of Plomari, and from the liberal beaches of Skala Eressos to the legendary church on the rock in Petra.

**📝 Before You Go:**
- **Car is Essential:** The island is very large. Traveling from one end to the other can take 2-3 hours. Renting a car is inevitable for exploring.
- **Ouzo Capital:** This is where the world's best ouzos are produced. Don't return without visiting the museums in Plomari.
- **Roads are Winding:** The island has a mountainous structure, and roads are generally winding. Caution should be exercised while driving.

## 📅 Set Your Calendar

- **Spring:** The scent of olive flowers and every shade of green. The best time for nature walks.
- **Summer:** The liveliest period of the island. "Panigiri" (local festivals) held in every village must be experienced.
- **Autumn (September):** Start of harvest time. The weather is still warm, the sea is calm.
- **Winter:** The period when the island returns completely to its own life, spent in the warmth of ouzo and fish tables.

## 🏠 Where to Stay

- **Molyvos (Mithymna):** The island's most iconic and touristic village. For those seeking a romantic stay.
- **Plomari:** For those who want an intimate atmosphere by the sea, at the heart of ouzo culture.
- **Petra:** A popular spot near Molyvos with a wide sandy beach and a charming bazaar.
- **Mytilene (Center):** For those who want to be closer to shopping and the harbor, more urban.

## 🚲 Getting Around

- **Car Rental:** The only real option for moving freely on the island.
- **Bus:** Buses run from the center to major villages, but service is limited.
- **Taxi:** Can be an expensive option for travel between towns.
- **Walking:** The most enjoyable way to explore the village centers.

## 🏛️ Iconic Stops

1. **Molyvos Castle and Streets:** A journey through cobblestone, bougainvillea-lined streets up to the hilltop castle.
2. **Plomari Ouzo Museum (Barbayanni):** A world-famous museum where you can discover the long history of ouzo.
3. **Petrified Forest (Sigri):** A rare fossil forest from millions of years ago.
4. **Petra Church (Panagia Glykofilousa):** A legendary church built on a rock, accessible by 114 steps.
5. **Agiasos Village:** A mountain village on the slopes of Mount Olympus, famous for its handicrafts and authentic coffees.
6. **Mor Taksi Peninsula:** Northern coasts known for their desolate and natural beauty.

## 🍽️ Flavor Map

- **Morning:** Greek coffee cooked on coals and local halvas in Agiasos.
- **Lunch:** Sun-dried grilled octopus (Lakerda) in harbor tavernas.
- **Evening:** Local cheeses (Ladotyri) and seafood accompanied by ouzo in Plomari.
- **Appetizer:** Lesvos' famous "Kalloni Sardine."

## 🔍 Local Secrets

- **Eftalou Thermal Springs:** Cooling off in natural springs inside or right outside the historic bath on the seaside.
- **Skala Sikamineas:** The most romantic fishing village on the island with its small white church in the sea (Mermaid Madonna).
- **Man 'Atsa Beach:** A hidden bay with shallow and crystal water known only to locals.
''';
"""

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Add switch cases
CASE_ADDITIONS = """      case 'dubrovnik':
        return isEnglish ? _dubrovnikEN : _dubrovnikTR;
      case 'mykonos':
      case 'mikonos':
        return isEnglish ? _mykonosEN : _mykonosTR;
      case 'rhodes':
      case 'rodos':
        return isEnglish ? _rhodesEN : _rhodesTR;
      case 'midilli':
      case 'lesvos':
        return isEnglish ? _midilliEN : _midilliTR;"""

# Insert into switch before default
if "default:" in content:
    content = content.replace("default:", CASE_ADDITIONS + "\n      default:")

# Add variables at the end
if content.strip().endswith("}"):
    insert_pos = content.rfind("}")
    new_vars = DUB_TR + "\n" + DUB_EN + "\n" + MYK_TR + "\n" + MYK_EN + "\n" + RHO_TR + "\n" + RHO_EN + "\n" + MID_TR + "\n" + MID_EN + "\n"
    content = content[:insert_pos] + new_vars + content[insert_pos:]

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Group 2 (Dubrovnik, Mykonos, Rhodes, Midilli) successfully injected.")
