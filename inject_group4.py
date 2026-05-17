#!/usr/bin/env python3
import os

TARGET_FILE = "lib/services/city_blog_content.dart"

# CANNES
CAN_TR = r"""
  // CANNES
  static const _cannesTR = '''
# Cannes: Sinemanın ve İhtişamın Fransız Başkenti

**Hızlı Bakış:** Cannes, Fransız Rivierası'nın (Côte d'Azur) en ışıltılı, en prestijli ve en karizmatik şehridir. Sadece bir liman kenti değil, dünya sinemasının kalbinin attığı, kırmızı halıların ve mega yatların merkezidir. Palmiye ağaçlarıyla bezeli La Croisette bulvarı, lüks otelleri ve eski şehrin (Le Suquet) dar sokaklarıyla Cannes, hem aristokrat bir asalet hem de modern bir şıklık sunar.

**📝 Gitmeden Önce:**
- **Festival Zamanı:** Mayıs ayındaki Film Festivali sırasında şehir aşırı kalabalık ve fiyatlar tavan noktadadır. Sakinlik arıyorsanız bu dönemden kaçının.
- **Plajlar:** La Croisette üzerindeki plajların çoğu özeldir ve giriş ücretlidir. Halk plajları için Palais des Festivals'in hemen yanındaki veya şehrin biraz dışındaki alanları tercih edebilirsiniz.
- **Le Suquet:** Modern Cannes'dan sıkılırsanız tepedeki eski şehir bölgesine çıkıp gerçek Fransız dokusunu hissedin.

## 📅 Takviminizi Ayarlayın

- **İlkbahar:** Film Festivali heyecanı ve çiçek açan Riviera doğası.
- **Yaz:** Güneşin, denizin ve gece hayatının en canlı olduğu, jet-set'in şehre akın ettiği dönem.
- **Sonbahar:** Kalabalığın çekildiği ama havanın hala yumuşak olduğu, alışveriş ve yürüyüş için en iyi zaman.
- **Kış:** Cannes Film Pazarı ve diğer etkinliklerle şehrin ticari ama yine de şık olduğu dönem.

## 🏠 Nerede Kalmalı

- **La Croisette:** Şehrin tam kalbinde, lüksün ve denizin yanı başında olmak isteyenler için.
- **Le Suquet (Eski Şehir):** Daha otantik, dar sokaklı ve yerel bir atmosfer arayanlar için.
- **La Bocca:** Şehir merkezinin biraz dışında, daha ekonomik ve aileler için uygun bölge.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Cannes merkezi oldukça kompakttır, her yere yürüyerek ulaşılabilir.
- **Otobüs:** Şehir içi ve çevre kasabalara (Nice, Antibes) giden düzenli hatlar mevcuttur.
- **Tren:** Nice, Monaco ve Marsilya'ya gitmek için en hızlı ve manzaralı yol (Gare de Cannes).
- **Tekne:** Iles de Lérins adalarına gitmek için tek yol.

## 🏛️ İkonik Duraklar

1. **Boulevard de la Croisette:** Dünyanın en meşhur sahil bulvarlarından biri. Palmiyeler, lüks butikler ve oteller.
2. **Palais des Festivals:** Film Festivali'nin yapıldığı ve ünlülerin el izlerinin olduğu bina.
3. **Le Suquet:** Şehrin en eski mahallesi, kalesi ve dar taş sokakları.
4. **Iles de Lérins:** Şehrin hemen karşısındaki, huzur ve tarih kokan iki küçük ada (Sainte-Marguerite ve Saint-Honorat).
5. **Marché Forville:** Şehrin en taze yerel ürünlerinin, peynirlerin ve çiçeklerin satıldığı tarihi pazar.
6. **Port Vieux (Eski Liman):** Klasik yelkenlilerin ve lüks teknelerin yan yana durduğu kartpostallık liman.

## 🍽️ Lezzet Haritası

- **Sabah:** Marché Forville'de taze meyve ve yerel Fransız hamur işleri.
- **Öğle:** Eski liman yakınındaki küçük bistrolarda "Salade Niçoise".
- **Akşam:** Le Suquet'nin dar sokakundaki restoranlarda taze deniz ürünleri ve Provence şarapları.
- **Tatlı:** Fransız makaronları ve el yapımı çikolatalar.

## 🔍 Lokal Sırlar

- **Saint-Honorat Adası:** Adadaki rahiplerin kendi ürettikleri şarapları ve likörleri mutlaka deneyin.
- **Bel Air Tepesi:** Şehri ve denizi en yüksekten görebileceğiniz, turistlerin pek bilmediği manzara noktası.
- **Rue Meynadier:** Lüks mağazalardan ziyade yerel peynircilerin, kasapların ve butik dükkanların olduğu daha gerçek bir alışveriş sokağı.
''';
"""

CAN_EN = r"""  static const _cannesEN = '''
# Cannes: The French Capital of Cinema and Glamour

**Quick Glimpse:** Cannes is the most sparkling, prestigious, and charismatic city on the French Riviera (Côte d'Azur). It’s not just a port city, but the heart of world cinema, the center of red carpets and mega yachts. With its palm-lined Boulevard de la Croisette, luxury hotels, and the narrow streets of the old town (Le Suquet), Cannes offers both aristocratic nobility and modern elegance.

**📝 Before You Go:**
- **Festival Time:** During the Film Festival in May, the city is extremely crowded and prices peak. Avoid this period if you're seeking peace.
- **Beaches:** Most beaches along La Croisette are private with entry fees. For public beaches, choose areas right next to the Palais des Festivals or slightly outside the city.
- **Le Suquet:** If you tire of modern Cannes, climb to the old town area on the hill to feel the authentic French texture.

## 📅 Set Your Calendar

- **Spring:** Film Festival excitement and the blooming Riviera nature.
- **Summer:** The liveliest period for sun, sea, and nightlife, when the jet-set flocks to the city.
- **Autumn:** The best time for shopping and walking when crowds retreat but the weather is still soft.
- **Winter:** The period when the city is business-like yet elegant with the Cannes Film Market and other events.

## 🏠 Where to Stay

- **La Croisette:** For those who want to be right in the heart of the city, next to luxury and the sea.
- **Le Suquet (Old Town):** For those seeking a more authentic, narrow-streeted, and local atmosphere.
- **La Bocca:** A more economical and family-friendly area slightly outside the city center.

## 🚲 Getting Around

- **Walking:** Cannes center is quite compact; everywhere can be reached on foot.
- **Bus:** Regular lines are available within the city and to surrounding towns (Nice, Antibes).
- **Train:** The fastest and most scenic way to Nice, Monaco, and Marseille (Gare de Cannes).
- **Boat:** The only way to go to the Iles de Lérins.

## 🏛️ Iconic Stops

1. **Boulevard de la Croisette:** One of the most famous coastal boulevards in the world. Palms, luxury boutiques, and hotels.
2. **Palais des Festivals:** The building where the Film Festival is held and features the handprints of celebrities.
3. **Le Suquet:** The city's oldest neighborhood, with its castle and narrow stone streets.
4. **Iles de Lérins:** Two small islands full of peace and history (Sainte-Marguerite and Saint-Honorat) right across from the city.
5. **Marché Forville:** Historic market selling the city's freshest local products, cheeses, and flowers.
6. **Port Vieux (Old Port):** A postcard-perfect harbor where classic sailboats and luxury yachts sit side by side.

## 🍽️ Flavor Map

- **Morning:** Fresh fruit and local French pastries at Marché Forville.
- **Lunch:** "Salade Niçoise" in small bistros near the old port.
- **Evening:** Fresh seafood and Provence wines in restaurants in the narrow streets of Le Suquet.
- **Sweet:** French macarons and handmade chocolates.

## 🔍 Local Secrets

- **Saint-Honorat Island:** Definitely try the wines and liqueurs produced by the monks on the island.
- **Bel Air Hill:** A viewpoint little known by tourists where you can see the city and sea from the highest point.
- **Rue Meynadier:** A more authentic shopping street with local cheesemongers, butchers, and boutique shops rather than luxury stores.
''';
"""

# SAINT-TROPEZ
TRO_TR = r"""
  // SAINT-TROPEZ
  static const _saint_tropezTR = '''
# Saint-Tropez: Balıkçı Köyünden Dünya Jet-Setine

**Hızlı Bakış:** Saint-Tropez, Fransız Rivierası'nın en efsanevi, en bohem ve en lüks destinasyonudur. 1950'lerde Brigitte Bardot ile başlayan şöhreti, bugün hala dünyanın en zenginlerinin ve ünlülerin uğrak noktası olmasıyla devam eder. Pastel renkli binaları, bembeyaz kumlu plajları ve limandaki mega yatlarıyla burası, bir yanda köklü bir Provençal geleneklerini, diğer yanda ise uçsuz bucaksız bir ihtişamı yaşatır.

**📝 Gitmeden Önce:**
- **Ulaşım Zorluğu:** Saint-Tropez'e giden tek bir ana yol vardır ve yazın bu yol aşırı trafikli olabilir. Nice veya Cannes'dan kalkan feribotlar en hızlı ve keyifli ulaşım yoludur.
- **Pampelonne Plajı:** Şehrin merkezinde değil, 5 km uzağındadır. Buradaki meşhur beach clublara (Le Club 55 gibi) gitmek için araç veya taksi gerekir.
- **Kıyafet:** Şık ama rahat "Riviera stili" buranın vazgeçilmezidir.

## 📅 Takviminizi Ayarlayın

- **Haziran / Eylül:** Şehrin en şık ve havanın en güzel olduğu, kalabalığın nispeten daha kabul edilebilir olduğu dönem.
- **Temmuz-Ağustos:** Şehrin tam anlamıyla "patladığı", lüksün ve partilerin doruk noktasına ulaştığı dönem.
- **Ekim (Les Voiles de Saint-Tropez):** Dünyanın en güzel klasik yelkenlilerinin yarıştığı muazzam festival dönemi.
- **Kış:** Şehrin tamamen sessizleştiği, sadece yerel halkın kaldığı huzurlu dönem.

## 🏠 Nerede Kalmalı

- **Liman Çevresi (Vieux Port):** Aksiyonun tam kalbinde olmak isteyenler için.
- **Pampelonne:** Plajlara ve doğaya daha yakın, lüks villaların ve resortların olduğu bölge.
- **Ramatuelle:** Tepede yer alan, daha huzurlu ve muazzam manzaralı tarihi köy bölgesi.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Şehir merkezi oldukça küçüktür, yürüyerek keşfetmek en iyisidir.
- **Scooter:** Yaz trafiğinden kurtulmanın ve plajlara gitmenin en popüler yolu.
- **Tekne:** Civar koyları ve sahilleri keşfetmek için.

## 🏛️ İkonik Duraklar

1. **Vieux Port (Eski Liman):** Dev yatların ve rengarenk kafelerin (Senequier gibi) olduğu şehrin kalbi.
2. **Citadelle de Saint-Tropez:** Şehre tepeden bakan 17. yüzyıl kalesi ve denizcilik müzesi.
3. **Place des Lices:** Yerlilerin kumda "Pétanque" oynadığı, çınar ağaçları altındaki tarihi meydan ve pazar alanı.
4. **Pampelonne Plajı:** 5 km uzunluğundaki bembeyaz kumları ve dünyaca ünlü plaj kulüpleri.
5. **Eglise de Saint-Tropez:** Şehrin simgesi olan sarı ve kırmızı renkli tarihi çan kulesi.
6. **Musée de l'Annonciade:** Fransız Rivierası'nın en iyi modern sanat koleksiyonlarından birine ev sahipliği yapan müze.

## 🍽️ Lezzet Haritası

- **Sabah:** Sénéquier'de limana karşı bir kahve ve brioche.
- **Öğle:** Pampelonne plajında taze ızgara balık ve buz gibi bir Provence Roze şarabı.
- **Akşam:** Eski şehrin dar sokakundaki restoranlarda yerel "Bouillabaisse" (balık çorbası).
- **Tatlı:** Meşhur "Tarte Tropézienne" (krema dolgulu brioche keki).

## 🔍 Lokal Sırlar

- **Sentier des Douaniers:** Sahil boyunca uzanan, gizli koylara ve muazzam manzaralara çıkan eski gümrük memurları yürüyüş yolu.
- **Grimaud Köyü:** Saint-Tropez'in hemen arkasında yer alan, "Küçük Venedik" olarak bilinen kanallı ve çiçekli köy.
- **Sabah Pazarı:** Salı ve Cumartesi günleri Place des Lices'teki pazarda yerel peynir ve zeytinleri tadın.
''';
"""

TRO_EN = r"""  static const _saint_tropezEN = '''
# Saint-Tropez: From a Fishing Village to the World Jet-Set

**Quick Glimpse:** Saint-Tropez is the most legendary, bohemian, and luxurious destination on the French Riviera. Its fame, which began with Brigitte Bardot in the 1950s, continues today as a haunt for the world's wealthiest and most famous. With its pastel-colored buildings, white sandy beaches, and mega yachts in the harbor, it offers deep-rooted Provençal traditions on one hand and boundless glamour on the other.

**📝 Before You Go:**
- **Transport Difficulty:** There is only one main road to Saint-Tropez, which can be extremely congested in summer. Ferries from Nice or Cannes are the fastest and most enjoyable way.
- **Pampelonne Beach:** It's not in the city center but 5 km away. A car or taxi is needed to reach famous beach clubs (like Le Club 55) there.
- **Dress Code:** Chic yet casual "Riviera style" is a must here.

## 📅 Set Your Calendar

- **June / September:** The period when the city is most stylish, weather is beautiful, and crowds are relatively more acceptable.
- **July-August:** When the city literally "explodes," and luxury and parties reach their peak.
- **October (Les Voiles de Saint-Tropez):** A massive festival period where the world's most beautiful classic sailboats race.
- **Winter:** A quiet period when the city falls completely silent and only locals remain.

## 🏠 Where to Stay

- **Harbor Area (Vieux Port):** For those who want to be right in the heart of the action.
- **Pampelonne:** An area closer to beaches and nature, with luxury villas and resorts.
- **Ramatuelle:** A historic hilltop village area, more peaceful and with magnificent views.

## 🚲 Getting Around

- **Walking:** The city center is quite small; it's best to explore on foot.
- **Scooter:** The most popular way to escape summer traffic and reach the beaches.
- **Boat:** To explore nearby coves and shores.

## 🏛️ Iconic Stops

1. **Vieux Port:** The heart of the city with giant yachts and colorful cafes (like Sénéquier).
2. **Citadelle de Saint-Tropez:** A 17th-century fortress and maritime museum overlooking the city.
3. **Place des Lices:** A historic square and market area under plane trees where locals play "Pétanque" in the sand.
4. **Pampelonne Beach:** Famous for its 5 km of white sands and world-renowned beach clubs.
5. **Eglise de Saint-Tropez:** The historic yellow and red bell tower, the symbol of the city.
6. **Musée de l'Annonciade:** A museum housing one of the French Riviera's best modern art collections.

## 🍽️ Flavor Map

- **Morning:** A coffee and brioche at Sénéquier facing the harbor.
- **Lunch:** Fresh grilled fish and ice-cold Provence Rosé wine at Pampelonne beach.
- **Evening:** Local "Bouillabaisse" (fish soup) in boutique restaurants in the narrow streets of the old town.
- **Sweet:** The famous "Tarte Tropézienne" (cream-filled brioche cake).

## 🔍 Local Secrets

- **Sentier des Douaniers:** An old customs officers' path along the coast leading to hidden coves and magnificent views.
- **Grimaud Village:** A flowered village with canals known as "Little Venice," located just behind Saint-Tropez.
- **Morning Market:** Taste local cheeses and olives at the market in Place des Lices on Tuesdays and Saturdays.
''';
"""

# IBIZA
IBI_TR = r"""
  // IBIZA
  static const _ibizaTR = '''
# İbiza: Partiden Çok Daha Fazlası, Beyaz Ada

**Hızlı Bakış:** İbiza, dünyada sadece "gece hayatı" ile anılsa da, aslında UNESCO mirasındaki kalesi, bohem ruhu ve turkuaz koylarıyla çok daha fazlasıdır. "La Isla Blanca" (Beyaz Ada) olarak bilinen bu İspanyol adası, bir yanda dünyanın en ünlü kulüplerine ev sahipliği yaparken, diğer yanda sessiz çam ormanları, hippi pazarları ve el değmemiş plajlarıyla huzur arayanları karşılar.

**📝 Gitmeden Önce:**
- **Kulüp Biletleri:** Popüler partiler için biletleri önceden internetten almak hem daha ucuzdur hem de girişi garanti eder.
- **Ulaşım:** Taksi bulmak zordur; adayı tam anlamıyla keşfetmek ve gizli koylara gitmek için araç veya scooter kiralama şarttır.
- **İki Yüzlü Ada:** Adanın güneyi daha hareketli ve parti odaklıyken, kuzeyi sessiz, bohem ve aileler için daha uygundur.

## 📅 Takviminizi Ayarlayın

- **Mayıs-Haziran başı:** Sezonun açılış partileri dönemi. Hava güzel, kalabalık henüz zirve yapmamıştır.
- **Temmuz-Ağustos:** Adanın en sıcak ve en çılgın dönemi. Fiyatlar en yüksek seviyededir.
- **Eylül-Ekim:** Kapanış partileri dönemi. Denizin en sıcak ve adanın en keyifli olduğu zaman.
- **Kış:** Adanın tamamen yerellere kaldığı, "hippi" ruhunun en saf hissedildiği sakin dönem.

## 🏠 Nerede Kalmalı

- **Eivissa (Ibiza Town):** Tarihi Dalt Vila'ya yakın, alışveriş ve liman atmosferi isteyenler için.
- **Playa d'en Bossa:** En büyük kulüplere ve en uzun kumsala yürüme mesafesinde olmak isteyenler için.
- **San Antonio:** Muazzam gün batımı ve daha ekonomik konaklama seçenekleri için.
- **Santa Eulalia:** Daha sakin, aileler için uygun ve gastronomik odaklı bölge.

## 🚲 Şehir İçi Ulaşım

- **Discobus:** Gece boyunca kulüpler arası ulaşımı sağlayan ekonomik otobüs ağı.
- **Araç Kiralama:** Gizli koylar (Cala Comte, Cala d'Hort) için en iyi seçenek.
- **Feribot:** Formentera adasına gitmek için limandan kalkan tekneler.

## 🏛️ İkonik Duraklar

1. **Dalt Vila:** Surlarla çevrili, labirent sokaklı UNESCO mirasındaki eski şehir ve katedrali.
2. **Es Vedrà:** Adanın batısında yükselen, manyetik enerjisi ve efsaneleriyle ünlü devasa kaya adası.
3. **Cala Comte:** Kristal suyuyla adanın en güzel gün batımı ve deniz noktalarından biri.
4. **Hippy Markets (Las Dalias / Es Canar):** Adanın 60'lardan gelen bohem ruhunu yaşatan renkli pazarlar.
5. **Cafe del Mar / Mambo:** San Antonio'da müzik eşliğinde gün batımının dünya çapındaki merkezi.
6. **Ses Salines:** Adanın güneyindeki tuz gölleri ve muazzam sahil şeridi.

## 🍽️ Lezzet Haritası

- **Sabah:** Yerel fırınlardan "Ensaimada" (tatlı çörek).
- **Öğle:** Deniz kenarında İspanyol klasiği "Paella" veya "Fideuà".
- **Akşam:** Santa Gertrudis gibi iç kesimlerdeki köylerde yerel tapaslar ve İspanyol şarapları.
- **Tatlı:** İbiza'nın geleneksel peynir keki "Flaó".

## 🔍 Lokal Sırlar

- **Formentera:** İbiza'dan 30 dakikalık feribotla ulaşabileceğiniz, Avrupa'nın Maldivleri olarak bilinen komşu ada.
- **Atlantis (Sa Pedrera):** Eski taş ocaklarından oluşmuş, ulaşımı zor ama mistik bir doğal havuz alanı.
- **Santa Gertrudis Köyü:** Adanın tam ortasında, sanat galerileri ve şık kafeleriyle en "lokal" hissettiren köy.
''';
"""

IBI_EN = r"""  static const _ibizaEN = '''
# Ibiza: Much More Than Just Parties, The White Island

**Quick Glimpse:** Although Ibiza is often associated only with "nightlife," it is much more with its UNESCO-listed fortress, bohemian spirit, and turquoise coves. Known as "La Isla Blanca" (The White Island), this Spanish destination hosts the world's most famous clubs on one hand, while welcoming peace-seekers with quiet pine forests, hippy markets, and untouched beaches on the other.

**📝 Before You Go:**
- **Club Tickets:** Buying tickets for popular parties online in advance is both cheaper and guarantees entry.
- **Transport:** Taxis are hard to find; renting a car or scooter is essential to fully explore the island and reach hidden coves.
- **Two-Sided Island:** The south of the island is more active and party-oriented, while the north is quiet, bohemian, and more suitable for families.

## 📅 Set Your Calendar

- **May-Early June:** Opening party season. Weather is nice, crowds haven't peaked yet.
- **July-August:** The hottest and craziest period of the island. Prices are at their highest.
- **September-October:** Closing party season. The time when the sea is warmest and the island is most enjoyable.
- **Winter:** A quiet period when the island belongs to locals and the "hippy" spirit is felt at its purest.

## 🏠 Where to Stay

- **Eivissa (Ibiza Town):** For those who want to be near historic Dalt Vila, shopping, and the harbor atmosphere.
- **Playa d'en Bossa:** For those who want to be within walking distance of the biggest clubs and the longest beach.
- **San Antonio:** For magnificent sunsets and more economical accommodation options.
- **Santa Eulalia:** A more peaceful, family-friendly, and gastronomically focused area.

## 🚲 Getting Around

- **Discobus:** An economical bus network providing transport between clubs throughout the night.
- **Car Rental:** The best option for hidden coves (Cala Comte, Cala d'Hort).
- **Ferry:** Boats departing from the harbor to Formentera island.

## 🏛️ Iconic Stops

1. **Dalt Vila:** The walled, labyrinthine UNESCO-listed old town and its cathedral.
2. **Es Vedrà:** A giant rocky island rising in the west of the island, famous for its magnetic energy and legends.
3. **Cala Comte:** One of the island's best sunset and swimming spots with crystal water.
4. **Hippy Markets (Las Dalias / Es Canar):** Colorful markets that keep the island's 60s bohemian spirit alive.
5. **Cafe del Mar / Mambo:** The global center of sunsets accompanied by music in San Antonio.
6. **Ses Salines:** Salt lakes in the south and an impressive coastline.

## 🍽️ Flavor Map

- **Morning:** "Ensaimada" (sweet pastry) from local bakeries.
- **Lunch:** Spanish classic "Paella" or "Fideuà" by the sea.
- **Evening:** Local tapas and Spanish wines in inland villages like Santa Gertrudis.
- **Sweet:** Ibiza's traditional cheesecake "Flaó".

## 🔍 Local Secrets

- **Formentera:** The neighbor island known as Europe's Maldives, accessible by a 30-minute ferry from Ibiza.
- **Atlantis (Sa Pedrera):** An area of old stone quarries, difficult to reach but with mystical natural pools.
- **Santa Gertrudis Village:** The village in the exact center of the island that feels most "local" with its art galleries and chic cafes.
''';
"""

# VALENCIA
VAL_TR = r"""
  // VALENCIA
  static const _valenciaTR = '''
# Valensiya: Tarihin ve Geleceğin Kusursuz Harmanı

**Hızlı Bakış:** Valensiya, İspanya'nın üçüncü büyük şehri olup hem fütüristik mimarisiyle hem de köklü gelenekleriyle büyüleyen bir Akdeniz kentidir. Paella'nın anavatanı olan bu şehir, daracık orta çağ sokakları, devasa parkları ve dünyanın en modern yapılarından biri olan Bilim ve Sanat Şehri ile her zevke hitap eder. Güneşin hiç eksik olmadığı, hayatın sokaklarda yaşandığı sıcakkanlı ve dinamik bir şehirdir.

**📝 Gitmeden Önce:**
- **Paella Zamanı:** Gerçek Paella Valensiya'da öğle yemeğinde yenir; akşamları restoranlarda Paella bulmak zor olabilir veya turistler için yapılmış olabilir.
- **Turia Bahçeleri:** Şehrin ortasından geçen eski nehir yatağının devasa bir parka dönüştürüldüğünü unutmayın; şehri keşfetmek için bu yeşil yolu kullanın.
- **Las Fallas:** Mart ayında giderseniz şehrin dev kuklalarla ve havai fişeklerle yandığı efsanevi festivale tanıklık edebilirsiniz.

## 📅 Takviminizi Ayarlayın

- **Mart:** Las Fallas Festivali dönemi. Şehrin en çılgın ve en kalabalık zamanı.
- **Bahar (Nisan-Haziran):** Hava mükemmel, parklar yemyeşil ve plaj mevsimi açılmış. En iyi dönem.
- **Yaz:** Oldukça sıcak olabilir ama plajları ve gece festivalleriyle çok canlıdır.
- **Sonbahar (Eylül-Ekim):** Sıcakların dindiği, havanın keşif için en yumuşak olduğu keyifli zaman.

## 🏠 Nerede Kalmalı

- **Ciutat Vella (Eski Şehir):** Tarihin tam ortasında, katedrale ve pazara yakın olmak isteyenler için.
- **Ruzafa:** Şehrin "soho"su. Sanat galerileri, bohem kafeler ve hareketli gece hayatı için.
- **El Cabanyal:** Eski balıkçı mahallesi, denize yakın ve daha lokal bir atmosfer arayanlar için.
- **Extramurs:** Daha modern, sakin ve yerel bir İspanyol mahallesi deneyimi için.

## 🚲 Şehir İçi Ulaşım

- **Bisiklet:** Valensiya dümdüz bir şehirdir ve Turia Bahçeleri sayesinde bisiklet sürmek en keyifli ulaşım yoludur.
- **Metro:** Havalimanı ve plajlar arası ulaşım için çok düzenlidir.
- **Yürümek:** Eski şehir bölgesi yürüyerek keşfedilmeye çok uygundur.

## 🏛️ İkonik Duraklar

1. **Bilim ve Sanat Şehri (Ciudad de las Artes y las Ciencias):** Santiago Calatrava imzalı fütüristik yapılar topluluğu.
2. **Valencia Katedrali:** Kutsal Kase'nin (Holy Grail) burada olduğuna inanılan, Gotik-Barok harikası yapı.
3. **Mercado Central (Merkez Pazar):** Avrupa'nın en büyük ve en güzel taze gıda pazarlarından biri.
4. **La Lonja de la Seda:** İpek Borsası binası, UNESCO mirasındaki muazzam Gotik mimari.
5. **Turia Bahçeleri:** Şehri ikiye bölen 9 km uzunluğundaki devasa yeşil vaha.
6. **Torres de Serranos:** Şehrin eski giriş kapısı olan heybetli ikiz kuleler.

## 🍽️ Lezzet Haritası

- **Ana Yemek:** "Paella Valenciana" (tavşan, tavuk ve taze fasulyeli orijinal tarif).
- **İçecek:** Valensiya'ya özgü "Horchata" (yer bademi sütü) ve "Agua de Valencia" kokteyli.
- **Sokak Lezzeti:** Sıcak çikolataya batırılan taze "Churros" veya "Buñuelos".
- **Atıştırmalık:** Mercado Central'da taze meyveler ve yerel peynirler.

## 🔍 Lokal Sırlar

- **Albufera Gölü:** Şehrin hemen dışındaki bu gölde gün batımında tekne turu yapın; Paella pirincinin yetiştiği yer burasıdır.
- **Plaza Redonda:** Gizli kalmış, dairesel bir meydan; geleneksel el sanatları ve danteller için uğrayın.
- **Gulliver Parkı:** Turia Bahçeleri içinde, dev bir Gulliver heykelinin kaydıraklara dönüştüğü eğlenceli alan.
''';
"""

VAL_EN = r"""  static const _valenciaEN = '''
# Valencia: A Perfect Blend of History and Future

**Quick Glimpse:** Valencia is Spain's third-largest city, a Mediterranean gem that fascinates with both its futuristic architecture and deep-rooted traditions. As the birthplace of Paella, it offers something for everyone with its narrow medieval streets, massive parks, and the City of Arts and Sciences, one of the most modern structures in the world. It is a warm and dynamic city where the sun is never missing and life is lived in the streets.

**📝 Before You Go:**
- **Paella Time:** Real Paella is eaten at lunch in Valencia; it can be hard to find in restaurants in the evening, or it might be made for tourists.
- **Turia Gardens:** Remember that the old riverbed passing through the middle of the city has been converted into a massive park; use this green path to explore the city.
- **Las Fallas:** If you visit in March, you can witness the legendary festival where the city "burns" with giant puppets and fireworks.

## 📅 Set Your Calendar

- **March:** Las Fallas Festival period. The craziest and most crowded time of the city.
- **Spring (April-June):** Perfect weather, green parks, and beach season is open. The best period.
- **Summer:** Can be quite hot, but very lively with beaches and night festivals.
- **Autumn (September-October):** A pleasant time when the heat recedes and the weather is softest for exploration.

## 🏠 Where to Stay

- **Ciutat Vella (Old Town):** For those who want to be right in history, close to the cathedral and the market.
- **Ruzafa:** The city's "Soho." For art galleries, bohemian cafes, and a vibrant nightlife.
- **El Cabanyal:** The old fishing neighborhood, close to the sea and for those seeking a more local atmosphere.
- **Extramurs:** For a more modern, quiet, and local Spanish neighborhood experience.

## 🚲 Getting Around

- **Bicycle:** Valencia is a flat city, and cycling is the most enjoyable way of transport thanks to the Turia Gardens.
- **Metro:** Very organized for transport between the airport and beaches.
- **Walking:** The old town area is very suitable for exploring on foot.

## 🏛️ Iconic Stops

1. **City of Arts and Sciences:** A collection of futuristic structures signed by Santiago Calatrava.
2. **Valencia Cathedral:** A Gothic-Baroque masterpiece believed to house the Holy Grail.
3. **Mercado Central (Central Market):** One of Europe's largest and most beautiful fresh food markets.
4. **La Lonja de la Seda:** The Silk Exchange building, a magnificent example of Gothic architecture on the UNESCO heritage list.
5. **Turia Gardens:** A massive 9 km long green oasis dividing the city in two.
6. **Torres de Serranos:** Imposing twin towers that were the city's old entrance gates.

## 🍽️ Flavor Map

- **Main Dish:** "Paella Valenciana" (the original recipe with rabbit, chicken, and fresh beans).
- **Drink:** Valencia's unique "Horchata" (tigernut milk) and "Agua de Valencia" cocktail.
- **Street Food:** Fresh "Churros" or "Buñuelos" dipped in hot chocolate.
- **Snack:** Fresh fruit and local cheeses at the Mercado Central.

## 🔍 Local Secrets

- **Albufera Lake:** Take a boat trip at sunset in this lake just outside the city; this is where Paella rice is grown.
- **Plaza Redonda:** A hidden, circular square; stop by for traditional crafts and lace.
- **Gulliver Park:** A fun area inside the Turia Gardens where a giant Gulliver statue is transformed into slides.
''';
"""

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Add switch cases
CASE_ADDITIONS = """      case 'cannes':
        return isEnglish ? _cannesEN : _cannesTR;
      case 'saint_tropez':
      case 'st_tropez':
        return isEnglish ? _saint_tropezEN : _saint_tropezTR;
      case 'ibiza':
        return isEnglish ? _ibizaEN : _ibizaTR;
      case 'valencia':
        return isEnglish ? _valenciaEN : _valenciaTR;"""

if "default:" in content:
    content = content.replace("default:", CASE_ADDITIONS + "\n      default:")

# Add variables at the end
if content.strip().endswith("}"):
    insert_pos = content.rfind("}")
    new_vars = CAN_TR + "\n" + CAN_EN + "\n" + TRO_TR + "\n" + TRO_EN + "\n" + IBI_TR + "\n" + IBI_EN + "\n" + VAL_TR + "\n" + VAL_EN + "\n"
    content = content[:insert_pos] + new_vars + content[insert_pos:]

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Group 4 (Cannes, Saint-Tropez, Ibiza, Valencia) successfully injected.")
