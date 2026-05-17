#!/usr/bin/env python3
import os

TARGET_FILE = "lib/services/city_blog_content.dart"

# AMALFI
AMA_TR = r"""
  // AMALFI
  static const _amalfiTR = '''
# Amalfi Sahili: Limon Kokulu Dikey Cennet

**Hızlı Bakış:** Amalfi Sahili, dik yamaçlara tutunmuş pastel renkli evleri, turkuaz denizi ve devasa limon bahçeleriyle dünyanın en büyüleyici rotalarından biridir. Positano'nun dikey sokaklarından Amalfi'nin tarihi meydanına, Ravello'nun nefes kesen bahçelerinden masmavi koylara kadar burası bir yeryüzü cennetidir. UNESCO mirasındaki bu sahil şeridi, İtalyan "La Dolce Vita" (Tatlı Hayat) ruhunun en somut halidir.

**📝 Gitmeden Önce:**
- **Ulaşım:** Sahil yolu (Statale 163) çok dar ve virajlıdır. Araç kiralamak yerine "Sita" otobüslerini veya deniz yoluyla ulaşımı (feribot) tercih etmek çok daha keyifli ve az streslidir.
- **Yürüyüş:** Positano ve Amalfi çok fazla basamak ve dik yokuş barındırır. Rahat ayakkabılar hayati önem taşır.
- **Limon Ürünleri:** Burası limonun anavatanıdır. Limoncello ve limonlu dondurma denemeden dönmeyin.

## 📅 Takviminizi Ayarlayın

- **İlkbahar (Mayıs-Haziran):** Çiçeklerin açtığı, havanın ılıman ve kalabalığın henüz makul olduğu en güzel dönem.
- **Yaz (Temmuz-Ağustos):** Sahilin en kalabalık ve en pahalı dönemi. Rezervasyonlar aylar öncesinden yapılmalı.
- **Sonbahar (Eylül):** Denizin en sıcak, kalabalığın azalmaya başladığı "sarı yaz" dönemi.
- **Kış:** Çoğu otel ve restoranın kapalı olduğu, sahilin tamamen sessizliğe büründüğü dönem.

## 🏠 Nerede Kalmalı

- **Positano:** Adriyatik'in en fotojenik, en lüks ve en dikey kasabası.
- **Amalfi:** Sahilin ana merkezi, ulaşım ağının kalbi ve tarihi dokusuyla ünlü.
- **Ravello:** Tepede, denizden uzak ama en muazzam manzaralara ve huzura sahip kasaba.
- **Maiori / Minori:** Daha düz ayak, aileler için uygun ve nispeten daha ekonomik seçenekler.

## 🚲 Şehir İçi Ulaşım

- **Feribot:** Kasabalar arası en hızlı ve en manzaralı ulaşım yolu.
- **Otobüs (Sita Bus):** Ekonomik ama yazın çok kalabalık ve virajlar nedeniyle yavaş olabilir.
- **Vespa:** Gerçek bir İtalyan gibi hissetmek için popüler ama deneyim gerektiren bir seçenek.

## 🏛️ İkonik Duraklar

1. **Amalfi Katedrali (Duomo di Amalfi):** 9. yüzyıldan kalma, devasa merdivenleri ve Arap-Normann mimarisiyle büyüleyici merkez.
2. **Villa Cimbrone ve Villa Rufolo (Ravello):** Dünyanın en güzel bahçeleri ve "Sonsuzluk Terası" (Terrazza dell'Infinito).
3. **Tanrıların Yolu (Sentiero degli Dei):** Agerola'dan Nocelle'ye uzanan, dünyanın en iyi yürüyüş rotalarından biri.
4. **Grotta dello Smeraldo (Zümrüt Mağarası):** Denizin içindeki zümrüt yeşili ışık oyunlarıyla meşhur mağara.
5. **Fiordo di Furore:** İki dev kaya arasındaki gizli bir plaj ve köprü ile sahilin en gizemli noktası.
6. **Positano Sahili:** Şemsiyeleri ve dik yamaç manzarasıyla İtalya'nın en meşhur fotoğraf karesi.

## 🍽️ Lezzet Haritası

- **Sabah:** Bir İtalyan barında "Cornetto" ve "Cappuccino".
- **Öğle:** Deniz kenarında "Scialatielli ai Frutti di Mare" (deniz mahsüllü taze makarna).
- **Akşam:** Limon ağaçları altında "Limonlu Risotto".
- **Tatlı:** Meşhur "Delizia al Limone" (limon rüyası tatlısı).

## 🔍 Lokal Sırlar

- **Atrani:** Amalfi'nin hemen yanındaki, turistlerin keşfetmediği en küçük ve en otantik İtalyan köyü.
- **Valle delle Ferriere:** Amalfi'nin arkasındaki vadide, şelaleler ve eski kağıt değirmenleri arasındaki serin yürüyüş yolu.
- **Limon Bahçesi Turu:** Yerel çiftçilerin bahçelerinde gerçek "Sfusato Amalfitano" limonlarını dalından toplayın.
''';
"""

AMA_EN = r"""  static const _amalfiEN = '''
# Amalfi Coast: A Vertical Paradise Scented with Lemons

**Quick Glimpse:** The Amalfi Coast is one of the world's most fascinating routes, with pastel-colored houses clinging to steep slopes, turquoise seas, and massive lemon groves. From the vertical streets of Positano to the historic square of Amalfi, and from the breathtaking gardens of Ravello to the deep blue coves, it is an earthly paradise. This coastline, a UNESCO heritage site, is the most tangible form of the Italian "La Dolce Vita" (Sweet Life) spirit.

**📝 Before You Go:**
- **Transport:** The coastal road (Statale 163) is very narrow and winding. Instead of renting a car, opting for "Sita" buses or transport by sea (ferry) is much more enjoyable and less stressful.
- **Walking:** Positano and Amalfi contain a lot of steps and steep slopes. Comfortable shoes are vital.
- **Lemon Products:** This is the homeland of lemons. Don't return without trying Limoncello and lemon ice cream.

## 📅 Set Your Calendar

- **Spring (May-June):** The most beautiful period when flowers bloom, the weather is mild, and the crowds are still reasonable.
- **Summer (July-August):** The most crowded and expensive period of the coast. Reservations should be made months in advance.
- **Autumn (September):** The "golden summer" period when the sea is warmest and the crowds begin to decrease.
- **Winter:** The period when most hotels and restaurants are closed, and the coast falls into complete silence.

## 🏠 Where to Stay

- **Positano:** The most photogenic, luxurious, and vertical town of the Adriatic.
- **Amalfi:** The main center of the coast, the heart of the transport network, and famous for its historical texture.
- **Ravello:** A town on the hill, far from the sea but with the most magnificent views and peace.
- **Maiori / Minori:** Flatter, suitable for families, and relatively more affordable options.

## 🚲 Getting Around

- **Ferry:** The fastest and most scenic way to travel between towns.
- **Bus (Sita Bus):** Economical but can be very crowded in summer and slow due to bends.
- **Vespa:** A popular but experience-requiring option to feel like a real Italian.

## 🏛️ Iconic Stops

1. **Amalfi Cathedral (Duomo di Amalfi):** A fascinating 9th-century center with massive stairs and Arab-Norman architecture.
2. **Villa Cimbrone and Villa Rufolo (Ravello):** The world's most beautiful gardens and the "Infinity Terrace" (Terrazza dell'Infinito).
3. **Path of the Gods (Sentiero degli Dei):** One of the world's best hiking routes, stretching from Agerola to Nocelle.
4. **Emerald Grotto (Grotta dello Smeraldo):** A cave famous for its emerald green light games inside the sea.
5. **Fiordo di Furore:** The most mysterious point of the coast with a hidden beach and bridge between two giant rocks.
6. **Positano Beach:** Italy's most famous photograph with its umbrellas and steep slope view.

## 🍽️ Flavor Map

- **Morning:** "Cornetto" and "Cappuccino" in an Italian bar.
- **Lunch:** "Scialatielli ai Frutti di Mare" (fresh seafood pasta) by the sea.
- **Evening:** "Lemon Risotto" under lemon trees.
- **Sweet:** The famous "Delizia al Limone" (lemon dream dessert).

## 🔍 Local Secrets

- **Atrani:** The smallest and most authentic Italian village right next to Amalfi, undiscovered by tourists.
- **Valle delle Ferriere:** A cool walking path between waterfalls and old paper mills in the valley behind Amalfi.
- **Lemon Grove Tour:** Pick real "Sfusato Amalfitano" lemons from the branch in the gardens of local farmers.
''';
"""

# BARI
BAR_TR = r"""
  // BARI
  static const _bariTR = '''
# Bari: Puglia'nın Giriş Kapısı, Otantik İtalya

**Hızlı Bakış:** Bari, İtalya'nın çizmesinin topuğunda, Puglia bölgesinin kalbinde yer alan canlı bir liman kentidir. Bir yanda daracık sokaklarında kadınların kapı önünde makarna (orecchiette) açtığı "Bari Vecchia" (Eski Bari), diğer yanda geniş caddeleri ve şık butikleriyle modern Murat bölgesi... Bari, gerçek İtalyan ruhunu, deniz kokusunu ve gastronomi tutkusunu en samimi haliyle sunan bir şehirdir.

**📝 Gitmeden Önce:**
- **Siesta Zamanı:** Bari'de dükkanlar öğlen 13:30 ile 16:30 arası genellikle kapalıdır. Planınızı buna göre yapın.
- **Bari Vecchia'da Kaybolun:** Haritayı bir kenara bırakın ve eski şehrin labirent sokaklarında kaybolun; her sokak ucu bir bazilikaya veya taze ekmek kokusuna çıkar.
- **Güvenlik:** Genel olarak güvenli olsa da, kalabalık yerlerde çantanıza dikkat etmeniz her İtalyan şehri gibi önerilir.

## 📅 Takviminizi Ayarlayın

- **Bahar:** Puglia'nın en güzel zamanı. Ne çok sıcak ne çok kalabalık.
- **Yaz:** Plajların (özellikle Polignano a Mare gibi yakın yerlerin) dolup taştığı, akşamüstü gezintilerinin (passeggiata) en keyifli olduğu zaman.
- **Sonbahar:** Hasat mevsimi. Zeytinyağı ve şarap tadımları için en iyi dönem.
- **Kış:** Noel pazarları ve yerel festivallerle şehrin daha sakin ve otantik olduğu zaman.

## 🏠 Nerede Kalmalı

- **Bari Vecchia (Eski Şehir):** Geleneksel bir deneyim ve tarihin içinde uyanmak isteyenler için.
- **Murat Bölgesi:** Alışveriş caddelerine yakın, modern otellerin bulunduğu merkezi bölge.
- **Lungomare:** Deniz manzaralı, yürüyüş yoluna yakın şık konaklama seçenekleri.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Eski Bari'yi keşfetmenin en iyi ve tek yolu.
- **Bisiklet:** Sahil şeridinde (Lungomare) bisiklet sürmek oldukça popüler.
- **Tren:** Polignano a Mare, Monopoli ve Alberobello gibi çevre kasabalara gitmek için en pratik yöntem (Bari Centrale istasyonu).

## 🏛️ İkonik Duraklar

1. **San Nicola Bazilikası:** Noel Baba olarak bilinen Aziz Nikolaos'un kemiklerine ev sahipliği yapan görkemli hac merkezi.
2. **San Sabino Katedrali:** Puglia Romanesk mimarisinin zarif ve beyaz taşlı örneği.
3. **Castello Svevo:** Şehri koruyan heybetli Norman-Swabian kalesi.
4. **Lungomare Nazario Sauro:** İtalya'nın en uzun ve en güzel sahil yürüyüş yollarından biri.
5. **Arco Basso (Makarna Sokağı):** Kadınların sokakta elleriyle orecchiette makarnası yaptığı ikonik sokak.
6. **Petruzzelli Tiyatrosu:** İtalya'nın en büyük ve en prestijli opera binalarından biri.

## 🍽️ Lezzet Haritası

- **Sokak Lezzeti:** "Focaccia Barese" (domatesli ve zeytinli taze ekmek) ve "Sgagliozze" (kızarmış mısır unu dilimleri).
- **Ana Yemek:** "Orecchiette con cime di rapa" (şalgam yapraklı kulakçık makarnası).
- **Deniz Ürünü:** Bari'nin yerel adeti olan "Crudo di mare" (çiğ deniz ürünleri tabağı).
- **İçecek:** Bölgenin meşhur kırmızı şarabı "Primitivo".

## 🔍 Lokal Sırlar

- **N'derr a la Lanz:** Balıkçıların sabah tuttuğu taze balıkları sattığı ve çiğ balık tadımı yapabileceğiniz liman noktası.
- **Panificio Fiore:** Eski bir kilisenin kalıntıları üzerine kurulu, şehrin en iyi focaccia'sını yapan fırın.
- **Via Sparano:** İtalya'nın en şık lüks markalarının bir arada olduğu araç trafiğine kapalı alışveriş caddesi.
''';
"""

BAR_EN = r"""  static const _bariEN = '''
# Bari: The Gateway to Puglia, Authentic Italy

**Quick Glimpse:** Bari is a vibrant port city in the heart of the Puglia region, at the heel of Italy's boot. On one side is "Bari Vecchia" (Old Bari), where women open pasta (orecchiette) at their doorsteps in narrow alleys; on the other, the modern Murat district with wide avenues and chic boutiques... Bari is a city that offers real Italian spirit, the scent of the sea, and a passion for gastronomy in its most sincere form.

**📝 Before You Go:**
- **Siesta Time:** Shops in Bari are usually closed between 1:30 PM and 4:30 PM. Plan accordingly.
- **Get Lost in Bari Vecchia:** Put the map aside and get lost in the labyrinthine streets of the old city; every street end leads to a basilica or the smell of fresh bread.
- **Security:** While generally safe, it's recommended to watch your bag in crowded places, like in any Italian city.

## 📅 Set Your Calendar

- **Spring:** The best time for Puglia. Neither too hot nor too crowded.
- **Summer:** The time when beaches (especially nearby places like Polignano a Mare) overflow and afternoon strolls (passeggiata) are most enjoyable.
- **Autumn:** Harvest season. The best time for olive oil and wine tastings.
- **Winter:** When the city is calmer and more authentic with Christmas markets and local festivals.

## 🏠 Where to Stay

- **Bari Vecchia:** For those who want a traditional experience and to wake up within history.
- **Murat District:** A central area with modern hotels, close to shopping streets.
- **Lungomare:** Stylish accommodation options with sea views, close to the walking path.

## 🚲 Getting Around

- **Walking:** The best and only way to explore Old Bari.
- **Bicycle:** Cycling on the coastline (Lungomare) is quite popular.
- **Train:** The most practical way to travel to surrounding towns like Polignano a Mare, Monopoli, and Alberobello (Bari Centrale station).

## 🏛️ Iconic Stops

1. **Basilica of Saint Nicholas:** A magnificent pilgrimage center housing the relics of Saint Nicholas, known as Santa Claus.
2. **Cathedral of San Sabino:** An elegant and white-stone example of Puglia Romanesque architecture.
3. **Castello Svevo:** An imposing Norman-Swabian castle protecting the city.
4. **Lungomare Nazario Sauro:** One of Italy's longest and most beautiful coastal walking paths.
5. **Arco Basso (Pasta Street):** An iconic street where women hand-make orecchiette pasta outdoors.
6. **Petruzzelli Theater:** One of Italy's largest and most prestigious opera houses.

## 🍽️ Flavor Map

- **Street Food:** "Focaccia Barese" (fresh bread with tomatoes and olives) and "Sgagliozze" (fried cornmeal slices).
- **Main Dish:** "Orecchiette con cime di rapa" (ear-shaped pasta with turnip greens).
- **Seafood:** Bari's local custom, "Crudo di mare" (raw seafood platter).
- **Drink:** The region's famous red wine, "Primitivo."

## 🔍 Local Secrets

- **N'derr a la Lanz:** The harbor point where fishermen sell fresh fish caught in the morning and where you can taste raw fish.
- **Panificio Fiore:** A bakery built on the remains of an old church, making the city's best focaccia.
- **Via Sparano:** A pedestrian-only shopping street featuring Italy's most stylish luxury brands.
''';
"""

# CATANIA
CAT_TR = r"""
  // CATANIA
  static const _cataniaTR = '''
# Catania: Etna'nın Gölgesindeki Barok Mücevher

**Hızlı Bakış:** Catania, Sicilya'nın doğu kıyısında, heybetli Etna Yanardağı'nın eteklerinde yükselen, küllerinden yeniden doğmuş bir şehirdir. Siyah volkanik taşlardan inşa edilmiş barok binaları, kaotik ama büyüleyici balık pazarları ve bitmek bilmeyen enerjisiyle Catania, Sicilya ruhunun en gerçek halidir. UNESCO mirasındaki bu şehir, hem tarihin derinliğini hem de Avrupa'nın en aktif yanardağının heyecanını sunar.

**📝 Gitmeden Önce:**
- **Volkanik Taşlar:** Şehrin binaları ve yer döşemeleri Etna'nın lavlarından yapıldığı için karakteristik bir gri-siyah renktedir.
- **Pazar Hareketliliği:** Catania'yı anlamak için sabah erken saatlerde "La Pescheria" balık pazarına mutlaka gidin.
- **Trafik:** Şehir trafiği biraz kaotik olabilir, merkezde yürümek en iyisidir.

## 📅 Takviminizi Ayarlayın

- **Şubat:** Aziz Agatha Festivali dönemi. Dünyanın en büyük dini kutlamalarından biri.
- **Bahar:** Etna'da hala kar varken aşağıda denizin keyfinin sürüldüğü, doğanın uyandığı dönem.
- **Yaz:** Çok sıcak olabilir ama sahil kasabalarına kaçmak için ideal zamandır.
- **Sonbahar:** Bağ bozumu zamanı. Etna şaraplarını tatmak için en iyi dönem.

## 🏠 Nerede Kalmalı

- **Piazza Duomo Çevresi:** Şehrin kalbi, ana cazibe merkezlerine yürüme mesafesinde.
- **Via Etnea:** Alışverişin ve hareketin merkezi olan ana cadde üzerindeki şık oteller.
- **Ognina:** Liman kıyısında, daha sakin ve deniz havası almak isteyenler için.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Tarihi merkezi keşfetmenin en keyifli yolu.
- **Metro:** Küçük ama merkezi noktaları birbirine bağlayan bir hattı mevcuttur.
- **Etna Transport:** Yanardağa ve çevre kasabalara gitmek için düzenli otobüs seferleri.

## 🏛️ İkonik Duraklar

1. **Piazza del Duomo ve Fil Çeşmesi (Fontana dell'Elefante):** Şehrin simgesi olan volkanik taştan fil heykeli.
2. **Catania Katedrali (Duomo di Sant'Agata):** Şehrin koruyucu azizesine adanmış muazzam barok yapı.
3. **Castello Ursino:** Lav akıntılarından mucizevi bir şekilde kurtulmuş orta çağ kalesi.
4. **Teatro Massimo Bellini:** Catania doğumlu ünlü besteci Bellini'ye adanmış görkemli opera binası.
5. **Via Crociferi:** Dünyanın en güzel barok caddelerinden biri olarak kabul edilen, kiliselerle bezeli yol.
6. **Etna Yanardağı:** Şehirden düzenlenen turlarla kraterlerine kadar çıkabileceğiniz devasa güç.

## 🍽️ Lezzet Haritası

- **Ana Yemek:** "Pasta alla Norma" (patlıcanlı ve tuzlu lor peynirli makarna) - Catania'nın milli yemeği.
- **Sokak Lezzeti:** "Arancino" (içi dolu kızarmış pirinç topları). Catania'da ucu sivri yapılır.
- **Kahvaltı:** "Granita e Brioche" (buzlu meyve püresi ve yanında sıcak poğaça).
- **Tatlı:** "Cannoli" ve "Cassata".

## 🔍 Lokal Sırlar

- **San Berillo:** Eski, yıkık dökük bir mahalleden sanatçıların elinde renkli bir sokak sanatı bölgesine dönüşen gizli köşe.
- **Aci Trezza:** Catania'nın hemen yanındaki, denizin içindeki dev kayalarıyla ünlü mitolojik balıkçı kasabası.
- **Sotto il Vulcano:** Yanardağın lav tüplerinin içinde kurulan şarap mahzenlerini ziyaret edin.
''';
"""

CAT_EN = r"""  static const _cataniaEN = '''
# Catania: The Baroque Jewel in Etna's Shadow

**Quick Glimpse:** Catania is a city reborn from its ashes, rising at the foot of the majestic Mount Etna on Sicily's eastern coast. With its baroque buildings constructed from black volcanic stone, chaotic but fascinating fish markets, and endless energy, Catania is the truest form of the Sicilian spirit. This UNESCO heritage city offers both the depth of history and the excitement of Europe's most active volcano.

**📝 Before You Go:**
- **Volcanic Stones:** The city's buildings and pavements are made from Etna's lava, giving them a characteristic grey-black color.
- **Market Vibrancy:** To understand Catania, definitely visit the "La Pescheria" fish market in the early morning.
- **Traffic:** City traffic can be a bit chaotic; walking in the center is best.

## 📅 Set Your Calendar

- **February:** Saint Agatha Festival period. One of the world's largest religious celebrations.
- **Spring:** A period when nature awakens, and you can still enjoy the sea while there is snow on Etna.
- **Summer:** Can be very hot, but it's an ideal time to escape to coastal towns.
- **Autumn:** Harvest time. The best period to taste Etna wines.

## 🏠 Where to Stay

- **Piazza Duomo Surroundings:** The heart of the city, within walking distance of main attractions.
- **Via Etnea:** Stylish hotels on the main street, the center of shopping and movement.
- **Ognina:** For those who want a calmer seaside atmosphere by the harbor.

## 🚲 Getting Around

- **Walking:** The most enjoyable way to explore the historic center.
- **Metro:** A small line connecting central points is available.
- **Etna Transport:** Regular bus services to the volcano and surrounding towns.

## 🏛️ Iconic Stops

1. **Piazza del Duomo and Elephant Fountain:** The symbol of the city, a volcanic stone elephant statue.
2. **Catania Cathedral:** A magnificent baroque structure dedicated to the city's patron saint.
3. **Castello Ursino:** A medieval castle that miraculously survived lava flows.
4. **Teatro Massimo Bellini:** A grand opera house dedicated to the famous Catania-born composer Bellini.
5. **Via Crociferi:** A road lined with churches, considered one of the most beautiful baroque streets in the world.
6. **Mount Etna:** The massive power where you can go up to the craters with tours organized from the city.

## 🍽️ Flavor Map

- **Main Dish:** "Pasta alla Norma" (pasta with eggplant and salted ricotta cheese) - Catania's national dish.
- **Street Food:** "Arancino" (stuffed fried rice balls). In Catania, they are pointed at the top.
- **Breakfast:** "Granita e Brioche" (iced fruit puree with a warm bun).
- **Sweet:** "Cannoli" and "Cassata."

## 🔍 Local Secrets

- **San Berillo:** A hidden corner transformed from an old, dilapidated neighborhood into a colorful street art district by artists.
- **Aci Trezza:** A mythological fishing village next to Catania, famous for its giant rocks in the sea.
- **Sotto il Vulcano:** Visit the wine cellars established inside the lava tubes of the volcano.
''';
"""

# PALERMO
PAL_TR = r"""
  // PALERMO
  static const _palermoTR = '''
# Palermo: Kültürlerin Kavşağında Bir Sicilya Masalı

**Hızlı Bakış:** Palermo, Akdeniz'in en renkli, en gürültülü ve en etkileyici şehirlerinden biridir. Fenikelilerden Araplara, Normanlardan İspanyollara kadar her medeniyetin iz bıraktığı bu şehir, adeta bir açık hava müzesidir. Kaotik pazarları, altın mozaikli katedralleri, görkemli opera binaları ve efsanevi sokak lezzetleriyle Palermo, tüm duyularınızı aynı anda harekete geçiren unutulmaz bir deneyimdir.

**📝 Gitmeden Önce:**
- **Sokak Lezzetlerine Hazır Olun:** Palermo, dünyanın en iyi sokak yemeği şehirlerinden biridir. Cesur olun ve her şeyi deneyin.
- **Öğle Tatili:** Diğer İtalyan şehirleri gibi burada da dükkanlar öğlen kapanır (Siesta).
- **Trafik ve Kalabalık:** Şehir merkezi oldukça yoğun ve hareketlidir; yavaşlamayı ve Palermo'nun ritmine ayak uydurmayı öğrenin.

## 📅 Takviminizi Ayarlayın

- **Bahar:** Şehrin en ferah ve keşif için en uygun sıcaklıkta olduğu dönem.
- **Yaz:** Mondello plajının canlandığı ama şehir merkezinin oldukça sıcak olduğu dönem.
- **Sonbahar:** Festivaller ve gurme etkinliklerin yoğunlaştığı en keyifli zaman.
- **Kış:** Noel ışıklarıyla bezeli, opera sezonunun zirve yaptığı şık dönem.

## 🏠 Nerede Kalmalı

- **Politeama / Libertà:** Şehrin modern, şık ve güvenli yüzü. Lüks butikler ve geniş caddeler.
- **Kalsa:** Tarihi merkezin kalbinde, son yıllarda yenilenen, sanat galerileri ve bohem kafelerin olduğu bölge.
- **Mondello:** Şehir merkezinden uzakta, denize girmek isteyenler için sayfiye bölgesi.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Tarihi aksı (Quattro Canti çevresi) keşfetmek için en iyi yöntem.
- **Otobüs:** Şehir içinde yaygındır ancak saatleri Sicilya usulü biraz esnek olabilir.
- **Fayton:** Turistik ama nostaljik bir şehir turu seçeneği.

## 🏛️ İkonik Duraklar

1. **Palermo Katedrali:** Mimaride Arap, Norman ve Barok sentezinin zirve noktası.
2. **Palazzo dei Normanni ve Cappella Palatina:** Altın mozaikleriyle dünyanın en güzel şapellerinden birine ev sahipliği yapan krallık sarayı.
3. **Teatro Massimo:** İtalya'nın en büyük, Avrupa'nın üçüncü büyük opera binası (The Godfather 3'ün final sahnesinin çekildiği yer).
4. **Quattro Canti:** Şehrin dört eski mahallesinin birleştiği, barok heykellerle bezeli sekizgen meydan.
5. **Martorana Kilisesi:** Bizans mozaikleriyle süslü büyüleyici bir dini yapı.
6. **Catacombe dei Cappuccini:** Tarihin en ilginç ve biraz da ürpertici mumya koleksiyonunun olduğu yer.

## 🍽️ Lezzet Haritası

- **Sokak Lezzeti:** "Panelle" (nohut unu kızartması), "Arancina" ve cesurlar için "Pane con la Milza" (dalaklı sandviç).
- **Ana Yemek:** "Pasta con le sarde" (sardalyalı ve anasonlu makarna).
- **Tatlı:** "Cassata Siciliana" ve gerçek Sicilya "Cannoli"si.
- **İçecek:** Sicilya'nın sert ve karakterli şarapları.

## 🔍 Lokal Sırlar

- **Ballarò ve Vucciria Pazarları:** Şehrin gerçek ruhunun attığı, bağırışların ve renklerin birbirine karıştığı tarihi pazarlar.
- **Orto Botanico:** Şehrin gürültüsünden kaçıp egzotik bitkiler arasında dinlenebileceğiniz devasa botanik bahçesi.
- **Zisa Şatosu:** Norman döneminden kalma, Arap etkileri taşıyan büyüleyici "yazlık" saray.
''';
"""

PAL_EN = r"""  static const _palermoEN = '''
# Palermo: A Sicilian Fairytale at the Crossroads of Cultures

**Quick Glimpse:** Palermo is one of the most colorful, loudest, and most impressive cities in the Mediterranean. As an open-air museum where every civilization from Phoenicians to Arabs, Normans to Spaniards has left its mark. With its chaotic markets, golden-mosaic cathedrals, grand opera houses, and legendary street food, Palermo is an unforgettable experience that stimulates all your senses at once.

**📝 Before You Go:**
- **Be Ready for Street Food:** Palermo is one of the world's best street food cities. Be brave and try everything.
- **Midday Break:** Like other Italian cities, shops close here at noon (Siesta).
- **Traffic and Crowds:** The city center is quite busy and active; learn to slow down and keep pace with Palermo's rhythm.

## 📅 Set Your Calendar

- **Spring:** The period when the city is freshest and at the most suitable temperature for exploration.
- **Summer:** When Mondello beach comes alive but the city center is quite hot.
- **Autumn:** The most enjoyable time when festivals and gourmet events intensify.
- **Winter:** A chic period decorated with Christmas lights, where the opera season peaks.

## 🏠 Where to Stay

- **Politeama / Libertà:** The modern, stylish, and safe face of the city. Luxury boutiques and wide avenues.
- **Kalsa:** In the heart of the historic center, an area recently renovated with art galleries and bohemian cafes.
- **Mondello:** A seaside resort area away from the city center for those who want to swim.

## 🚲 Getting Around

- **Walking:** The best way to explore the historic axis (around Quattro Canti).
- **Bus:** Common in the city, but times can be a bit flexible in the Sicilian style.
- **Horse Carriage:** A touristy but nostalgic city tour option.

## 🏛️ Iconic Stops

1. **Palermo Cathedral:** The peak point of Arab, Norman, and Baroque synthesis in architecture.
2. **Palazzo dei Normanni and Cappella Palatina:** A royal palace housing one of the world's most beautiful chapels with golden mosaics.
3. **Teatro Massimo:** Italy's largest and Europe's third-largest opera house (where the final scene of The Godfather 3 was filmed).
4. **Quattro Canti:** An octagonal square adorned with baroque statues, where the city's four old neighborhoods meet.
5. **Martorana Church:** A fascinating religious building decorated with Byzantine mosaics.
6. **Catacombe dei Cappuccini:** The place with history's most interesting and somewhat creepy collection of mummies.

## 🍽️ Flavor Map

- **Street Food:** "Panelle" (chickpea fritters), "Arancina," and for the brave, "Pane con la Milza" (spleen sandwich).
- **Main Dish:** "Pasta con le sarde" (pasta with sardines and fennel).
- **Sweet:** "Cassata Siciliana" and real Sicilian "Cannoli."
- **Drink:** Sicily's strong and characteristic wines.

## 🔍 Local Secrets

- **Ballarò and Vucciria Markets:** Historic markets where the city's true spirit beats, with shouts and colors mixing.
- **Orto Botanico:** A massive botanical garden where you can escape the city noise and rest among exotic plants.
- **Zisa Castle:** A fascinating "summer" palace from the Norman period with Arab influences.
''';
"""

# SARDINYA
SAR_TR = r"""
  // SARDINYA
  static const _sardinyaTR = '''
# Sardinya: Akdeniz'in Turkuaz ve Gizemli Adası

**Hızlı Bakış:** Sardinya, sadece bir ada değil, kendi dili, gelenekleri ve vahşi doğasıyla minyatür bir kıtadır. Avrupa'nın en turkuaz sularına sahip Costa Smeralda'nın lüksünden, iç kısımlardaki sarp dağların sessizliğine uzanan bir çeşitlilik sunar. MÖ 1500'lerden kalma gizemli Nurajik kuleleri, bembeyaz kumsalları ve dünyada sadece burada bulabileceğiniz lezzetleriyle Sardinya, Akdeniz'in en asil ve el değmemiş köşesidir.

**📝 Gitmeden Önce:**
- **Mesafe:** Sardinya çok büyük bir adadır. Kuzeyden güneye gitmek 3-4 saat sürebilir. Seyahatinizi bir bölgeye odaklamanız önerilir.
- **Araç Kiralama:** Toplu taşıma sınırlıdır; adayı ve gizli koyları keşfetmek için araç kiralamak şarttır.
- **Rüzgar:** Ada, rüzgarlarıyla (özellikle Mistral) meşhurdur; bu da burayı yelken ve sörf için dünya lideri yapar.

## 📅 Takviminizi Ayarlayın

- **Haziran:** Denizin ısındığı, kalabalığın henüz makul olduğu en güzel ay.
- **Temmuz-Ağustos:** İtalyanların tatil dönemi. Adanın en hareketli, en pahalı ve en sıcak zamanı.
- **Eylül-Ekim:** Sakinlik arayanlar için ideal. Deniz hala sıcak, hava daha yumuşak.
- **Bahar (Nisan-Mayıs):** Doğa yürüyüşleri ve Nurajik alanları keşfetmek için muazzam bir doğa uyanışı.

## 🏠 Nerede Kalmalı

- **Costa Smeralda (Kuzeydoğu):** Lüks oteller, mega yatlar ve turkuazın en açık tonları için. (Porto Cervo)
- **Alghero (Kuzeybatı):** Katalan etkileri, tarihi surlar ve romantik akşamlar için.
- **Cagliari (Güney):** Adanın başkenti, tarihi doku, canlı şehir hayatı ve uzun kumsallar için.
- **Orosei Körfezi (Doğu):** Vahşi doğa, kanyonlar ve sadece tekneyle ulaşılan gizli koylar için.

## 🚲 Şehir İçi Ulaşım

- **Araç Kiralama:** Adadaki tek gerçek özgürlük yöntemi.
- **Tren (Trenino Verde):** Adanın iç kısımlarındaki muazzam manzaraları görmek için nostaljik yeşil tren hattı.
- **Tekne:** La Maddalena Takımadaları'nı keşfetmek için en iyi yol.

## 🏛️ İkonik Duraklar

1. **Costa Smeralda (Zümrüt Sahili):** Dünyanın en berrak sularına sahip lüks kıyı şeridi.
2. **Su Nuraxi di Barumini:** UNESCO mirasındaki, MÖ 1500'lerden kalma devasa nurajik kule kompleksi.
3. **Alghero Eski Şehir:** Katalan mimarisi ve denize nazır sarı taşlı surlar.
4. **Cala Mariolu ve Cala Goloritzé:** Orosei Körfezi'nde, bembeyaz çakılları ve turkuaz suyuyla dünyanın en iyi plajları arasında gösterilen koylar.
5. **La Maddalena Takımadaları:** Kristal denizi ve pembe kumlu plajlarıyla (Spiaggia Rosa) büyüleyici adalar grubu.
6. **Cagliari Kalesi (Castello):** Şehre tepeden bakan, dar sokaklı tarihi bölge.

## 🍽️ Lezzet Haritası

- **Ana Yemek:** "Malloreddus" (safranlı Sardinya makarnası) ve "Culurgiones" (patates ve peynir dolgulu mantı).
- **Et:** Geleneksel "Porceddu" (odun ateşinde pişen süt kuzusu).
- **Tatlı:** İçi peynir dolgulu, üzerinde bal gezdirilen kızarmış "Seadas".
- **İçecek:** Bölgenin meşhur beyaz şarabı "Vermentino" ve likörü "Mirto".

## 🔍 Lokal Sırlar

- **Bosa Köyü:** Adanın batısında, nehir kenarına kurulu rengarenk evleriyle en fotojenik kasaba.
- **Tiscali Köyü:** Bir mağaranın içine saklanmış, yürüyüşle ulaşılan antik yerleşim yeri.
- **Spiaggia di Pelosa:** Stintino'da, bir göl kadar sığ ve berrak, Maldivler'i aratmayan efsanevi plaj.
''';
"""

SAR_EN = r"""  static const _sardinyaEN = '''
# Sardinia: The Turquoise and Mysterious Island of the Mediterranean

**Quick Glimpse:** Sardinia is not just an island but a miniature continent with its own language, traditions, and wild nature. From the luxury of the Costa Smeralda, which has the most turquoise waters in Europe, to the silence of the steep mountains in the interior, it offers a great variety. With its mysterious Nuragic towers dating from 1500 BC, white sandy beaches, and flavors you can only find here, Sardinia is the most noble and untouched corner of the Mediterranean.

**📝 Before You Go:**
- **Distance:** Sardinia is a very large island. Traveling from north to south can take 3-4 hours. It is recommended to focus your trip on one region.
- **Car Rental:** Public transport is limited; renting a car is essential for exploring the island and hidden coves.
- **Wind:** The island is famous for its winds (especially the Mistral), making it a world leader for sailing and surfing.

## 📅 Set Your Calendar

- **June:** The most beautiful month when the sea is warm and the crowds are still reasonable.
- **July-August:** Italian holiday period. The island's busiest, most expensive, and hottest time.
- **September-October:** Ideal for those seeking peace. The sea is still warm, the weather is softer.
- **Spring (April-May):** A magnificent awakening of nature for hiking and exploring Nuragic sites.

## 🏠 Where to Stay

- **Costa Smeralda (Northeast):** For luxury hotels, mega yachts, and the clearest shades of turquoise. (Porto Cervo)
- **Alghero (Northwest):** For Catalan influences, historic walls, and romantic evenings.
- **Cagliari (South):** For the island's capital, historic texture, lively city life, and long sandy beaches.
- **Orosei Gulf (East):** For wild nature, canyons, and hidden coves accessible only by boat.

## 🚲 Getting Around

- **Car Rental:** The only true way of freedom on the island.
- **Train (Trenino Verde):** A nostalgic green train line to see the magnificent views in the interior of the island.
- **Boat:** The best way to explore the La Maddalena Archipelago.

## 🏛️ Iconic Stops

1. **Costa Smeralda:** A luxury coastline with the clearest waters in the world.
2. **Su Nuraxi di Barumini:** A massive Nuragic tower complex from 1500 BC, a UNESCO heritage site.
3. **Alghero Old Town:** Catalan architecture and yellow-stone walls overlooking the sea.
4. **Cala Mariolu and Cala Goloritzé:** Coves in the Orosei Gulf shown among the world's best beaches for their white pebbles and turquoise water.
5. **La Maddalena Archipelago:** A fascinating group of islands with crystal seas and pink-sand beaches (Spiaggia Rosa).
6. **Cagliari Castle (Castello):** The historic district with narrow streets overlooking the city.

## 🍽️ Flavor Map

- **Main Dish:** "Malloreddus" (Sardinian pasta with saffron) and "Culurgiones" (dumplings filled with potatoes and cheese).
- **Meat:** Traditional "Porceddu" (suckling pig cooked on a wood fire).
- **Sweet:** Fried "Seadas" stuffed with cheese and drizzled with honey.
- **Drink:** The region's famous white wine "Vermentino" and liqueur "Mirto".

## 🔍 Local Secrets

- **Bosa Village:** The most photogenic town on the west of the island, with colorful houses built by the river.
- **Tiscali Village:** An ancient settlement hidden inside a cave, accessible by hiking.
- **Spiaggia di Pelosa:** A legendary beach in Stintino, shallow and clear as a lake, rivaling the Maldives.
''';
"""

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Add switch cases
CASE_ADDITIONS = """      case 'amalfi':
        return isEnglish ? _amalfiEN : _amalfiTR;
      case 'bari':
        return isEnglish ? _bariEN : _bariTR;
      case 'catania':
        return isEnglish ? _cataniaEN : _cataniaTR;
      case 'palermo':
        return isEnglish ? _palermoEN : _palermoTR;
      case 'sardinya':
      case 'sardinia':
        return isEnglish ? _sardinyaEN : _sardinyaTR;"""

if "default:" in content:
    content = content.replace("default:", CASE_ADDITIONS + "\n      default:")

# Add variables at the end
if content.strip().endswith("}"):
    insert_pos = content.rfind("}")
    new_vars = AMA_TR + "\n" + AMA_EN + "\n" + BAR_TR + "\n" + BAR_EN + "\n" + CAT_TR + "\n" + CAT_EN + "\n" + PAL_TR + "\n" + PAL_EN + "\n" + SAR_TR + "\n" + SAR_EN + "\n"
    content = content[:insert_pos] + new_vars + content[insert_pos:]

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Group 3 (Amalfi, Bari, Catania, Palermo, Sardinya) successfully injected.")
