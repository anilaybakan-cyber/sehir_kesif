#!/usr/bin/env python3
import os

TARGET_FILE = "lib/services/city_blog_content.dart"

BODRUM_TR = r"""
  // BODRUM
  static const _bodrumTR = '''
# Bodrum: Mavi ve Beyazın Dansı, Ege'nin İncisi

**Hızlı Bakış:** Bodrum, antik Halikarnassos'un mirasçısı olarak hem tarihin hem de modern lüksün en zarif buluşma noktasıdır. Mavi pencereli beyaz evleri, her köşeden fışkıran begonvilleri ve dünyanın yedi harikasından birine ev sahipliği yapan topraklarıyla burası sadece bir tatil beldesi değil, bir yaşam tarzıdır. Bodrum Kalesi'nin heybetli silueti limanı selamlarken, Yalıkavak Marina'nın ışıltısı ve Gümüşlük'ün bohem gün batımları, yarımadanın her köşesinde farklı bir hikaye anlatır.

**📝 Gitmeden Önce:**
- **Ulaşım Esnekliği:** Yarımada oldukça geniştir; Bodrum merkezden Yalıkavak veya Gümüşlük'e gitmek araçla 30-40 dakika sürebilir. Araç kiralamak en konforlu seçenek olsa da, her yöne giden düzenli dolmuş ağını da kullanabilirsiniz.
- **Kıyafet Seçimi:** Bodrum akşamları bile bazen rüzgarlı olabilir; yanınızda ince bir şal bulundurmak iyi bir fikirdir. Ayrıca antik tiyatro ve kale gezileri için rahat ayakkabılar şarttır.
- **Rezervasyon Şart:** Özellikle Temmuz ve Ağustos aylarında popüler restoranlar ve beach clublar haftalar öncesinden dolabilir.

## 📅 Takviminizi Ayarlayın

- **İlkbahar (Nisan-Mayıs):** Doğanın uyandığı, begonvillerin ilk renklerini verdiği dönem. Kalabalıktan uzak, huzurlu bir keşif için idealdir.
- **Yaz (Haziran-Ağustos):** Bodrum'un en enerjik, en hareketli ve en sıcak dönemi. Gece hayatı ve beach partilerinin zirve noktası.
- **Sonbahar (Eylül-Ekim):** Denizin en sıcak, güneşin ise daha yumuşak olduğu "sarı yaz" dönemi. Lokallerin en sevdiği zamandır.
- **Kış (Kasım-Mart):** Şehrin kendi kabuğuna çekildiği, şömine başında balık yemenin keyfinin çıktığı sakin dönem.

## 🏠 Nerede Kalmalı

- **Bodrum Merkez:** Tarihe ve çarşıya yakın olmak isteyenler için.
- **Yalıkavak:** Lüks, modernite ve dünya standartlarında marina deneyimi arayanlar için.
- **Gümüşlük:** Bohem bir atmosfer ve balıkçı masalarında huzur arayanlar için.
- **Türkbükü:** Bodrum'un "Cemiyet" hayatının kalbinde, şık iskelelerde vakit geçirmek isteyenler için.

## 🚲 Şehir İçi Ulaşım

- **Dolmuş:** Bodrum Otogarı'ndan yarımadanın her koyuna (Bitez, Ortakent, Turgutreis, Yalıkavak vb.) giden dolmuşlar en ekonomik yoldur.
- **Taksi:** Şehir içinde yaygındır ancak uzun mesafelerde fiyatlar yükselebilir.
- **Araç Kiralama:** Yarımadayı özgürce keşfetmek için en iyi yöntemdir.

## 🏛️ İkonik Duraklar

1. **Bodrum Kalesi ve Sualtı Arkeoloji Müzesi:** Şehrin sembolü, dünyanın en önemli sualtı müzelerinden biri.
2. **Halikarnas Mozolesi:** Antik dünyanın yedi harikasından biri olan devasa anıt mezarın kalıntıları.
3. **Bodrum Antik Tiyatrosu:** Harika bir liman manzarasına karşı konserlerin ve tarihin buluşma noktası.
4. **Zeki Müren Sanat Müzesi:** "Sanat Güneşi"nin Bodrum'daki son yıllarını geçirdiği ve ruhunu bıraktığı evi.
5. **Yalıkavak Marina:** Mega yatlar ve dünyaca ünlü markalarla Bodrum'un lüks yüzü.
6. **Gümüşlük Limanı:** Denizin içinde yürüyerek Tavşan Adası'na geçebileceğiniz, balıkçılarıyla ünlü antik Myndos limanı.

## 🍽️ Lezzet Haritası

- **Sabah:** Bitez'in mandalina bahçeleri arasında yerel bir kahvaltı.
- **Öğle:** Bodrum merkezdeki şirin sokaklarda "Bodrum Döneri" (sebzeli döner).
- **Akşam:** Gümüşlük'te gün batımına karşı taze Ege mezeleri ve deniz ürünleri.
- **Tatlı:** Bodrum'un meşhur mandalina dondurması veya lokumları.

## 🔍 Lokal Sırlar

- **Karakaya Köyü:** Gümüşlük tepelerinde saklı, terk edilmiş bir Rum köyü olan Karakaya'da sessizliğin sesini dinleyin.
- **Pedasa Antik Kenti:** Orman içinde yürüyüş yaparak ulaşabileceğiniz, turistlerden uzak saklı bir tarih rotası.
- **Mandalina Bahçeleri:** Ocak-Şubat aylarında giderseniz Bodrum mandalinasının kokusunu her yerde hissedebilirsiniz.
''';
"""

BODRUM_EN = r"""  static const _bodrumEN = '''
# Bodrum: The Aegean Pearl, A Dance of Blue and White

**Quick Glimpse:** As the heir to ancient Halicarnassus, Bodrum is the most elegant meeting point of history and modern luxury. With its white houses adorned with blue shutters, bougainvilleas bursting from every corner, and lands hosting one of the seven wonders of the world, it’s not just a holiday resort but a way of life. While the imposing silhouette of Bodrum Castle greets the harbor, the shimmer of Yalıkavak Marina and the bohemian sunsets of Gümüşlük tell a different story at every corner of the peninsula.

**📝 Before You Go:**
- **Transport Flexibility:** The peninsula is quite large; traveling from Bodrum center to Yalıkavak or Gümüşlük can take 30-40 minutes by car. While renting a car is the most comfortable option, you can also use the regular minibus (dolmuş) network.
- **Dress Code:** Bodrum evenings can be breezy even in summer; bringing a light wrap is a good idea. Also, comfortable shoes are a must for exploring the ancient theater and castle.
- **Booking is Essential:** Especially in July and August, popular restaurants and beach clubs can be fully booked weeks in advance.

## 📅 Set Your Calendar

- **Spring (April-May):** When nature awakens and bougainvilleas give their first colors. Ideal for a peaceful exploration away from crowds.
- **Summer (June-August):** Bodrum's most energetic, vibrant, and hottest period. The peak for nightlife and beach parties.
- **Autumn (September-October):** The "golden summer" when the sea is warmest and the sun is softer. A favorite time for locals.
- **Winter (November-March):** A quiet period when the city retreats into its shell, perfect for enjoying fish by the fireplace.

## 🏠 Where to Stay

- **Bodrum Center:** For those who want to be close to history and the bazaar.
- **Yalıkavak:** For those seeking luxury, modernity, and a world-class marina experience.
- **Gümüşlük:** For those looking for a bohemian atmosphere and peace at fishermen's tables.
- **Türkbükü:** For those who want to spend time on chic piers at the heart of Bodrum's high society.

## 🚲 Getting Around

- **Dolmuş:** Minibuses from Bodrum Bus Station to every cove on the peninsula (Bitez, Ortakent, Turgutreis, Yalıkavak, etc.) are the most economical way.
- **Taxi:** Widely available but prices can rise for long distances.
- **Car Rental:** The best way to explore the peninsula freely.

## 🏛️ Iconic Stops

1. **Bodrum Castle and Underwater Archaeology Museum:** The symbol of the city, one of the most important underwater museums in the world.
2. **Mausoleum at Halicarnassus:** Remains of the massive monumental tomb, one of the seven wonders of the ancient world.
3. **Bodrum Ancient Theater:** A meeting point for concerts and history against a great harbor view.
4. **Zeki Müren Art Museum:** The house where the famous singer Zeki Müren spent his last years and left his spirit.
5. **Yalıkavak Marina:** The luxury face of Bodrum with mega yachts and world-famous brands.
6. **Gümüşlük Harbor:** The ancient Myndos harbor where you can walk through the sea to Rabbit Island.

## 🍽️ Flavor Map

- **Morning:** A local breakfast among Bitez's tangerine groves.
- **Lunch:** "Bodrum Döner" (vegetable döner) in the charming streets of the center.
- **Evening:** Fresh Aegean appetizers and seafood against the sunset in Gümüşlük.
- **Sweet:** Bodrum's famous tangerine ice cream or Turkish delights.

## 🔍 Local Secrets

- **Karakaya Village:** Listen to the sound of silence in Karakaya, an abandoned Greek village hidden in the hills of Gümüşlük.
- **Pedasa Ancient City:** A hidden historical route away from tourists, accessible by a walk through the forest.
- **Tangerine Groves:** If you visit in January or February, you can smell Bodrum tangerines everywhere.
''';
"""

CESME_TR = r"""
  // ÇEŞME
  static const _cesmeTR = '''
# Çeşme: Rüzgarın, Mavinin ve Eğlencenin Kalbi

**Hızlı Bakış:** Çeşme, Ege'nin en dinamik ve sofistike duraklarından biridir. Sakız ağaçlarının kokusu, Alaçatı'nın lavanta renkli taş sokakları ve Ilıca'nın turkuaz sığ sularıyla burası bir yaz rüyasıdır. Ayayorgi'nin dünyaca ünlü beach club'larından Germiyan'ın sakin köy yaşamına, Çeşme Kalesi'nin tarihi nöbetinden sörfçülerin rüzgarla dansına kadar yarımada her zevke hitap eden zengin bir mozaik sunar.

**📝 Gitmeden Önce:**
- **Rüzgara Hazırlıklı Olun:** Çeşme'nin meşhur rüzgarı bazen akşamları üşütebilir, yanınıza hafif bir hırka almayı unutmayın.
- **Beach Club Rezervasyonu:** Ayayorgi gibi popüler koylardaki mekanlar için özellikle hafta sonu rezervasyon şarttır.
- **Alaçatı Akşamları:** Alaçatı Çarşı akşam saatlerinde aşırı kalabalık olabilir; daha sakin bir gezi için sabah veya öğle saatlerini tercih edebilirsiniz.

## 📅 Takviminizi Ayarlayın

- **İlkbahar:** Alaçatı Ot Festivali dönemi (Genelde Nisan). Şehrin en renkli ve lezzetli zamanı.
- **Yaz:** Eğlencenin, güneşin ve denizin zirve yaptığı, enerjinin hiç bitmediği dönem.
- **Sonbahar:** Kalabalıkların çekildiği, denizin hala sıcak olduğu huzurlu dönem.
- **Kış:** Çeşme'nin gerçek yerlilerine kaldığı, rüzgarın sesini dinlemek için en iyi zaman.

## 🏠 Nerede Kalmalı

- **Alaçatı:** Butik taş otellerde romantik ve nostaljik bir atmosfer arayanlar için.
- **Çeşme Merkez:** Marina'ya yakın, daha hareketli bir konum tercih edenler için.
- **Ilıca:** Uzun plajın hemen yanında, deniz odaklı bir tatil isteyener için.
- **Dalyan:** Daha sakin, balıkçı kasabası havasını koruyan bir bölge arayanlar için.

## 🚲 Şehir İçi Ulaşım

- **Dolmuş:** Çeşme merkezden Alaçatı, Ilıca, Altınkum ve Dalyan'a düzenli seferler mevcuttur.
- **Taksi:** Özellikle gece eğlencesi dönüşü yaygındır.
- **Bisiklet:** Alaçatı ve çevresini keşfetmek için keyifli bir seçenek olabilir.

## 🏛️ İkonik Duraklar

1. **Çeşme Kalesi:** II. Bayezid döneminden kalma, muazzam bir manzara sunan görkemli kale.
2. **Alaçatı Çarşı:** Taş evler, begonviller ve tasarım dükkanlarıyla bezeli büyüleyici sokaklar.
3. **Alaçatı Yel Değirmenleri:** Kasabanın en fotojenik ve ikonik simgesi.
4. **Çeşme Marina:** Lüks yatlar ve şık restoranlarla kentin modern yüzü.
5. **Ilıca Plajı:** İncecik kumu ve denizin içinden kaynayan termal sularıyla eşsiz bir sahil.
6. **Erythrai Tiyatrosu (Ildırı):** Muhteşem bir gün batımı manzarasına sahip antik İyon kenti kalıntıları.

## 🍽️ Lezzet Haritası

- **Sabah:** Alaçatı'nın meşhur "Sakız Reçelli" köy kahvaltısı.
- **Öğle:** Çeşme'nin vazgeçilmezi olan bol malzemeli "Çeşme Kumrusu".
- **Akşam:** Dalyan'da taze balık veya Alaçatı'nın saklı bahçelerinde zeytinyağlı Ege mezeleri.
- **Tatlı:** Sakızlı dondurma veya sakızlı kurabiye.

## 🔍 Lokal Sırlar

- **Germiyan Köyü:** Türkiye'nin ilk CittaSlow (Sakin Şehir) köyü. Evlerin duvarlarındaki çiçek resimlerini keşfedin.
- **Delikli Koy:** Doğal kireçtaşı kayalarıyla ünlü, bakir ve huzurlu bir koy.
- **Yıldızburnu:** Denizin içindeki termal su kaynaklarında akşam serinliğinde keyif yapın.
''';
"""

CESME_EN = r"""  static const _cesmeEN = '''
# Cesme: The Heart of Wind, Blue, and Entertainment

**Quick Glimpse:** Cesme is one of the most dynamic and sophisticated destinations in the Aegean. With the scent of mastic trees, the lavender-colored stone streets of Alacati, and the shallow turquoise waters of Ilica, it is a summer dream. From the world-famous beach clubs of Ayayorgi to the quiet village life of Germiyan, and from the historical watch of Cesme Castle to the surfers' dance with the wind, the peninsula offers a rich mosaic for every taste.

**📝 Before You Go:**
- **Be Prepared for the Wind:** Cesme's famous wind can sometimes get chilly in the evenings; don't forget to bring a light cardigan.
- **Beach Club Reservations:** Reservations are a must for venues in popular bays like Ayayorgi, especially on weekends.
- **Alacati Evenings:** Alacati Bazaar can get extremely crowded in the evening; choose morning or noon hours for a more peaceful stroll.

## 📅 Set Your Calendar

- **Spring:** Alacati Herb Festival period (Usually April). The most colorful and delicious time of the city.
- **Summer:** The period when fun, sun, and sea peak, and the energy never ends.
- **Autumn:** A peaceful period when the crowds retreat and the sea is still warm.
- **Winter:** The best time to listen to the sound of the wind, when Cesme belongs to its real locals.

## 🏠 Where to Stay

- **Alacati:** For those looking for a romantic and nostalgic atmosphere in boutique stone hotels.
- **Cesme Center:** For those who prefer a more vibrant location close to the Marina.
- **Ilica:** For those who want a sea-oriented holiday right next to the long beach.
- **Dalyan:** For those looking for a quieter area that preserves its fishing village atmosphere.

## 🚲 Getting Around

- **Dolmuş:** Regular services are available from Cesme center to Alacati, Ilica, Altinkum, and Dalyan.
- **Taxi:** Especially common after night entertainment.
- **Bicycle:** Can be a pleasant option to explore Alacati and its surroundings.

## 🏛️ Iconic Stops

1. **Cesme Castle:** A majestic castle from the era of Sultan Bayezid II, offering a magnificent view.
2. **Alacati Bazaar:** Charming streets adorned with stone houses, bougainvilleas, and designer shops.
3. **Alacati Windmills:** The most photogenic and iconic symbol of the town.
4. **Cesme Marina:** The modern face of the city with luxury yachts and chic restaurants.
5. **Ilica Beach:** A unique shore with fine sand and thermal waters bubbling from the seabed.
6. **Erythrai Theater (Ildırı):** Remains of an ancient Ionian city with a spectacular sunset view.

## 🍽️ Flavor Map

- **Morning:** Alacati's famous village breakfast with "Mastic Jam."
- **Lunch:** The indispensable "Cesme Kumru" with plenty of ingredients.
- **Evening:** Fresh fish in Dalyan or Aegean appetizers with olive oil in the hidden gardens of Alacati.
- **Sweet:** Mastic ice cream or mastic cookies.

## 🔍 Local Secrets

- **Germiyan Village:** Turkey's first CittaSlow (Quiet City) village. Discover the flower paintings on the walls of the houses.
- **Delikli Bay:** A pristine and peaceful bay famous for its natural limestone rocks.
- **Yildizburnu:** Enjoy the evening breeze in the thermal springs within the sea.
''';
"""

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Add switch cases
SWITCH_MARKER = "return isEnglish ? _kasEN : _kasTR;"
CASE_ADDITIONS = """      case 'bodrum':
        return isEnglish ? _bodrumEN : _bodrumTR;
      case 'cesme':
      case 'çeşme':
        return isEnglish ? _cesmeEN : _cesmeTR;"""

if SWITCH_MARKER in content:
    content = content.replace(SWITCH_MARKER, SWITCH_MARKER + "\n" + CASE_ADDITIONS)

# Add variables at the end
CLOSING = "}\n"
if content.strip().endswith("}"):
    insert_pos = content.rfind("}")
    new_vars = BODRUM_TR + "\n" + BODRUM_EN + "\n" + CESME_TR + "\n" + CESME_EN + "\n"
    content = content[:insert_pos] + new_vars + content[insert_pos:]

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Group 1 (Bodrum, Cesme) successfully injected.")
