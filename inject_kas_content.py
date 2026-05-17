#!/usr/bin/env python3
# inject_kas_content.py — Adds _kasTR and _kasEN before the closing brace of the class

KAS_TR = r"""
  // KAŞ
  static const _kasTR = '''
# Kaş: Lykia'nın Gizli Kalmış Kıyı Şehri

**Hızlı Bakış:** Kaş, Akdeniz kıyısında durdurulan zamandır. Karşısında Yunan adası Meis'in silueti, ayaklarının altında Likya'dan kalma taş lahitler ve sokaklarında begonvillerin sardığı cumbalı evleri olan bu kasaba, kalabalık tatil beldelerinin tam tersidir. Ne büyük oteller ne de plaj şezlong sıraları; bunun yerine dalış tüpleri, yelkenciler ve masaya oturup yıllar önce çizilen haritaları kaybetmiş kaşifler var. Kekova'nın sular altındaki antik şehri, Kaputaş'ın kanyon ağzındaki turkuaz cenneti ve Antiphellos tiyatrosundan seyredilen gün batımı; Kaş'ı Türkiye'nin en özgün sahil deneyimine dönüştüren bu üç şey, başka hiçbir yerde bu kadar kompakt ve el değmemiş bir arada bulunmuyor.

**📝 Gitmeden Önce Bilmenizde Fayda Var:**
- **Küçük ama İşlevsel:** Kaş'ın merkezi yürüyerek gezilebilecek kadar kompakttır; otelden plaja, tiyatroya ve çarşıya her yön için 10-20 dakika yeterlidir. Araç kiralama ihtiyacı yalnızca Patara veya Saklıkent gibi çevre gezileri için ortaya çıkar.
- **Nakit Bulundurun:** Büyük restoranlar ve oteller kart kabul etse de, çarşı dükkanları, dolmuşlar ve yerel esnaf genellikle nakit tercih eder. ATM'ler çarşı meydanında mevcuttur ancak yoğun sezonda kuyruğa girebilirsiniz.
- **Sezon Farkı Belirgindir:** Haziran-Eylül arası kasaba dolup taşar, fiyatlar zirveye çıkar. Nisan-Mayıs ve Ekim ayları hem deniz sıcaklığının yeterli olduğu hem de kalabalıkların azaldığı altın dönemdir. Kış aylarında şehir yerel bir ritme bürünür; birçok işletme kapalıdır.
- **Dalış Noktaları Dünyaca Ünlüdür:** Kaş, Türkiye'nin en iyi dalış merkezi unvanını taşır. Caretta Wall, Uçak Enkazı ve çevresindeki koylar, hem yeni başlayanlar hem de ileri seviye dalgıçlar için istisnai koşullar sunar.

## 📅 Takviminizi Ayarlayın: Hangi Mevsim Sizin?

Kaş, yılın farklı yüzlerini kimseye şikayet etmeden taşır. Hangi mevsim seçilirse seçilsin, şehir kendi karakterini korur.

- **İlkbahar (Nisan-Mayıs):** Yılın en dengeli zamanıdır. Deniz suyu Nisan ortasından itibaren 18-20°C'ye ulaşır; yüzme keyfi başlar. Kasaba henüz dolmamıştır, her restoranın masasında yer bulunur. Likya Yolu yürüyüşleri için en uygun hava koşullarıdır; yollar çiçeklerle kaplıdır. Kaputaş'ta sabah erken saatte neredeyse yalnız kalırsınız.
- **Yaz (Haziran-Ağustos):** Kasabanın en hareketli ve en pahalı dönemidir. Sıcaklıklar 35-40°C'ye çıkabilir; Kaputaş'a inen 187 basamak öğle sıcağında zahmetli olabilir. Sabah erken veya akşamüstü gezileri her şeyi değiştirir. Kekova tekne turları için sabah kalkışı şarttır. Gece hayatı en canlı haliyle yaşanır.
- **Sonbahar (Eylül-Ekim):** Gizli sezon. Deniz en sıcak haliyle (26-28°C) yüzmeye hazırdır, hava ise yazın yorgunluğundan arınmıştır. Ekim ayında mevsim kısalmaya başlasa da şehir hala canlıdır. Dalgıçlar için yılın en şeffaf su koşulları bu dönemdedir.
- **Kış (Kasım-Mart):** Kasaba lokalin eline geçer. Birçok turist işletmesi kapanır, ama balıkçı meyhaneleri ve birkaç kafe hala açıktır. Likya mezarlarına ve Antiphellos tiyatrosuna kalabalıksız ulaşırsınız. Fiyatlar minimuma iner. Gerçek bir yerel deneyimi yaşamak isteyenler için ideal.

## 🏠 Nerede Kalmalı: Mahalle Rehberi

Kaş küçüktür ama konum farkı, tatil deneyimini köklü biçimde değiştirir.

- **Kasaba Merkezi (Uzun Çarşı ve Çevresi):** Her şeye yürüme mesafesinde olmak isteyenler için biçilmiş kaftandır. Sabah kahvaltısını Meis Adası manzarasıyla yapmak, çarşıyı keşfetmek ve akşam Küçük Çakıl'a iki dakikada inmek bu konumun ayrıcalıklarıdır. Boutique otel ve pansiyonlar yoğunlaşmıştır; Hotel Sonne ve Seatown gibi seçenekler Meis'e bakan odalara sahiptir.
- **Çukurbağ Yarımadası:** Merkeze birkaç kilometre mesafede, sessizlik isteyenler için doğru adrestir. Amphora Hotel bu yarımadanın en prestijli konaklamasıdır; kendi plaj platformu, büyük havuzu ve şehre hakim gün batımı manzarasıyla lüks arayanların tercihi. Şehre ulaşım için araç ya da dolmuş gerekir.
- **Büyükçakıl Çevresi:** Merkezden 10 dakika yürüme mesafesinde, denize yakın konaklamak isteyenler için idealdir. Plajın kıyısındaki restoranlar akşam dekorlarıyla bambaşka bir atmosfer sunar. Küçük pansiyonlar ve aile işletmeleri ağırlıktadır.

## 🚲 A Noktasından B Noktasına: Bir Lokal Gibi Hareket Edin

Kaş küçük ama çevre gezileri mesafe gerektirir. Doğru ulaşım seçimi günü kurtarır.

- **Antalya'dan Kaş'a Ulaşım:** Antalya Otogarı'ndan Kaş'a doğrudan otobüs seferleri yaklaşık 4 saat sürer (Pamukkale, Kamil Koç gibi firmalar). Araçla Antalya-Kaş arası 3 saattir ve kıyı yolu boyunca nefes kesen manzaralar sunar. Fethiye tarafından gelenler için ise mesafe yaklaşık 2 saattir.
- **Şehir İçi Ulaşım (Yürümek):** Kasaba merkezini ziyaret için en iyi araç kendi ayaklarınızdır. Küçük Çakıl'dan Antiphellos tiyatrosuna, Uzun Çarşı'ya ve Atatürk Meydanı'na hepsi 5-15 dakika yürüme mesafesindedir.
- **Dolmuşlar:** Kaş-Kaputaş-Kalkan hattında düzenli dolmuş seferleri mevcuttur. Kaputaş'a gitmek için en pratik yol budur; araç kiralamanıza gerek kalmaz. Patara ve çevre plajlara da dolmuşla ulaşabilirsiniz.
- **Araç Kiralama:** Kekova, Saklıkent Kanyonu, Patara gibi çevre noktaları için araç kiralamak en esnek seçenektir. Kasabada birkaç yerel kiralık araç ofisi mevcuttur; sezon içinde önceden rezervasyon önerilir.
- **Tekne:** Kekova turu için Kaş limanından kalkan tekne turlarına katılmak hem en pratik hem de en keyifli yoldur. Yarım gün veya tam gün seçenekleri mevcuttur. Kaptan Ergun gibi köklü yerel şirketler güvenilir ve lezzetli öğle yemekleriyle ünlüdür.

## 🏛️ Şehrin Hafızası: Görülmesi Gereken İkonik Duraklar

1. **Kaputaş Plajı:** Kaş ile Kalkan arasında bir kanyon ağzında saklı bu plaj, 187 basamak inerken giderek açılan turkuaz manzarasıyla Türkiye'nin en ikonik noktalarından biridir. Deniz aniden derinleşir; çocuklu aileler için rüzgarlı günlerde dikkatli olmak gerekir. Sabah 08:00'den önce gelin; hem park yeri hem de plaj neredeyse bomboştur.
2. **Kekova Adası ve Batık Şehir:** Tekneyle ulaşılan bu doğa harikasında, bölgeye 2. yüzyılda vuran depremler sonrası sular altında kalan antik kentin merdivenleri ve duvarları camdan bakılır gibi kristal suyun dibinde görülebilir. Kekova'yı en az bir defa sabah kalkışlı turla, öğleden önce ziyaret edin; öğleden sonra rüzgar artar.
3. **Antiphellos Antik Tiyatrosu:** Denize bakan ender antik yapılardan biri olan bu Helenistik tiyatro, Kaş merkezinin hemen üzerindedir ve 10 dakika yürüyüşle çıkılır. Gün batımında sahneden Meis Adası'na uzanan manzara, kasabaya dair en güçlü hatıralardan biri olur.
4. **Uzun Çarşı (Öğütçü Sokak):** Begonvillerle ve cumbalı evlerle süslü bu cadde, Kaş'ın bohem ruhunu barındırır. Sonunda Aslanlı Likya lahdi, antik mirasın modern alışveriş dükkanlarıyla nasıl iç içe geçebildiğini gösterir. El yapımı takılar, liken boyalı kumaşlar ve yerel seramikler en özgün hediye seçenekleridir.
5. **Likya Kaya Mezarları:** Kaş'ın ana caddesine ve meydanına hakim konumdaki bu Dor tipi kaya mezarları, tarihin günlük yaşamla bu denli iç içe geçtiğini başka az yerde göreceğiniz nadir örneklerdir. Lokallerin hemen yanı başında, herhangi bir giriş ücreti olmadan ziyaret edilebilir.
6. **Küçük Çakıl Plajı:** Merkezin hemen altındaki bu küçük ama ikonik koyun sırrı, deniz tabanından fışkıran tatlı su kaynaklarıdır. Akdeniz'in ortasında buz gibi serinliği bu şekilde yaşamak gerçekten tuhaf ve harika bir deneyimdir. Sabah 08:00-10:00 arası kalabalık minimumda olur.

## 🍽️ Lezzet Haritası: Sofra Rehberi

- **Sabah Kahvaltısı:** Kaş'ta kahvaltı kültürü, otel lobilerindeki standart bölünmelerin çok üzerindedir. Büyükçakıl'ın kıyısındaki restoranlarda, denize bakarak servis edilen serpme kahvaltılar kasabanın günü başlatma ritüelidir. Pide ekmekleri, yerel zeytinler ve taze bal kombinasyonu bölgenin imzasıdır.
- **Öğle Yemeği:** Küçük Çakıl ya da Büyükçakıl üzerindeki lokal balık restoranlarında öğle yemeği yemek, denizden çıkıp doğruca masaya oturmak kadar doğal bir Kaş deneyimidir. Meze kültürü burada güçlüdür; balık çorbası ve taş fırın ekmeğiyle başlamak en doğru girişdir.
- **Akşam Yemeği:** Uzun Çarşı çevresindeki butik restoranlar, Meis Adası'na bakan teras manzarasıyla akşamın en güzel dekorunu sunar. Hideaway Hotel'in restoranı ve Amphora Otel'in terasındaki gün batımı yemekleri önceden rezervasyon gerektirir.
- **Kafe Durağı:** Manzara Kafe, Kaş tepesinde panoramik bir bakış açısı sunar; gün batımı için en az 45 dakika öncesinden gelip köşe masayı kapmak gerekir. Çarşı içindeki küçük kafeler ise serin bir dondurma molası için klasik tercihtir.

## 🔍 Lokal Sırlar: Az Bilinen Kaş

- **Meis Adası Günübirlik Feri:** Kaş'tan her sabah kalkan feribot sizi Yunanistan'ın Meis (Kastellorizo) Adası'na götürür. Pasaportunuzu alın, kahvaltıyı teknede yapın ve tarihteki bu küçük ama etkileyici adada bir öğleden sonra geçirin.
- **Dalış Kursları:** Kaş'ın dalış altyapısı Türkiye'nin en kapsamlısıdır. Hiç dalış deneyimi olmayan biri bile güvenli intro-dive programlarıyla başlayabilir. Uçak Enkazı noktası ileri dalgıçlar için unutulmaz bir deneyimdir.
- **Likya Yolu:** Türkiye'nin en prestijli uzun mesafe yürüyüş rotası olan Likya Yolu, Kaş üzerinden geçer. Kasabadan başlayarak kıyı boyunca birkaç saatlik ya da günlük bölümler yürünebilir.
- **Çevre Gezileri:** Patara Antik Kenti ve Türkiye'nin en uzun plajı (18 km), Saklıkent Kanyonu'nda buz gibi dağ suyunda yürüyüş ve Kınık'taki Xanthos antik kenti; bunların hepsi Kaş'tan yarım günlük mesafededir.
- **Begonvil Fotoğrafı için Doğru Adres:** Uzun Çarşı'nın başlangıcındaki taş evlerin üstüne sarkan pembe begonvil sarmaşıklarının yanı sıra, Türk Evi Sokağı'nda sabah güneşini yakalamak en ikonik Kaş fotoğrafını verir.
''';

"""

KAS_EN = r"""  static const _kasEN = '''
# Kas: The Lycian Coast's Best-Kept Secret

**Quick Glimpse:** Kaş is time frozen on the Mediterranean. With the silhouette of the Greek island Kastellorizo across the water, Lycian rock tombs lining its streets, and bougainvillea-draped historic houses, this small town is the antithesis of the crowded resort strip. No massive hotels, no rows of beach loungers; instead, diving tanks, sailors, and explorers who lost their itineraries years ago. The sunken city at Kekova, the turquoise heaven of Kaputaş canyon mouth, and a sunset watched from the Antiphellos theatre — these three things make Kaş the most authentic coastal experience in Turkey, compact, unspoiled, and utterly unforgettable.

**📝 Before You Go:**
- **Small But Functional:** Kaş's center is compact enough to explore on foot; hotel to beach, theatre, and bazaar are all within 10-20 minutes in any direction. A rental car is only needed for day trips to Patara or Saklıkent.
- **Carry Cash:** Major restaurants and hotels accept cards, but bazaar shops, dolmuş minibuses, and local vendors usually prefer cash. ATMs are available at the town square but can have queues during peak season.
- **Seasonal Difference Is Stark:** June–September, the town is packed and prices peak. April–May and October are the golden window when the sea is warm enough and crowds thin out. Winter turns the town local; most tourist businesses close.
- **World-Class Diving:** Kaş holds Turkey's top diving center title. Caretta Wall, the Airplane Wreck, and surrounding coves offer exceptional conditions for both beginners and advanced divers.

## 📅 When to Go: Find Your Season

Kaş carries its different seasons without complaint. Whatever time you choose, the town stays true to its character.

- **Spring (April–May):** The most balanced time of year. Sea temperature reaches 18–20°C by mid-April; swimming begins. The town hasn't filled up yet, every restaurant has a free table. Ideal conditions for Lycian Way hikes; the trails are blanketed with wildflowers. You can have Kaputaş almost to yourself in the early morning.
- **Summer (June–August):** The busiest and most expensive season. Temperatures can reach 35–40°C; the 187 steps down to Kaputaş become a challenge at midday. Early mornings and late afternoons change everything. Morning departures for Kekova boat tours are essential. Nightlife is at its liveliest.
- **Autumn (September–October):** The hidden season. The sea is at its warmest (26–28°C) and the air has shed summer's fatigue. Divers find the year's clearest water conditions during this period. October remains lively even as the season begins to wind down.
- **Winter (November–March):** The town belongs to locals. Many tourist businesses close, but fishermen's taverns and a few cafés remain open. You can visit the Lycian tombs and Antiphellos theatre with no crowds at all. Prices drop to their lowest. Ideal for those seeking a genuine local experience.

## 🏠 Where to Stay: Neighborhood Guide

Kaş is small, but where you stay meaningfully shapes your holiday experience.

- **Town Center (Uzun Çarşı and surroundings):** Perfect for those who want everything within walking distance. Waking up for breakfast with a view of Meis Island, browsing the bazaar, and walking two minutes down to Küçük Çakıl beach are the privileges of this location. Boutique hotels and guesthouses cluster here; Hotel Sonne and Seatown have rooms facing Meis.
- **Çukurbağ Peninsula:** A few kilometers from the center, the right address for those seeking quiet. Amphora Hotel is the peninsula's most prestigious stay; its private beach platform, large pool, and commanding sunset views over the town make it a luxury traveler's first choice. A vehicle or dolmuş is needed to reach town.
- **Büyükçakıl Area:** Ideal for those wanting to stay close to the sea, a 10-minute walk from the center. Restaurants along the beachfront create a completely different atmosphere in the evenings. Small guesthouses and family-run businesses are the norm here.

## 🚲 Getting Around: Move Like a Local

Kaş is small, but day trips require distance. The right transport choice saves the day.

- **Getting to Kaş from Antalya:** Direct buses from Antalya Otogar to Kaş take about 4 hours (Pamukkale, Kamil Koç and similar companies). By car, the coastal road from Antalya takes about 3 hours and offers breathtaking scenery. From Fethiye, the drive is approximately 2 hours.
- **Getting Around Town (Walking):** For exploring the town center, your own feet are the best tool. From Küçük Çakıl to the Antiphellos theatre, Uzun Çarşı and Atatürk Square are all within 5-15 minutes on foot.
- **Dolmuş Minibuses:** Regular dolmuş services run on the Kaş–Kaputaş–Kalkan route. This is the most practical way to reach Kaputaş without renting a car. Dolmuş also serve Patara and surrounding beaches.
- **Car Rental:** For Kekova, Saklıkent Canyon, Patara and other surrounding points, renting a car is the most flexible option. Several local rental offices operate in town; advance booking is recommended during peak season.
- **Boat:** For Kekova tours, joining boat trips departing from Kaş harbor is both the most practical and the most enjoyable approach. Half-day and full-day options are available. Long-established local operators like Captain Ergun are known for reliable service and delicious on-board lunches.

## 🏛️ Iconic Stops: The Town's Living Memory

1. **Kaputaş Beach:** Hidden at a canyon mouth between Kaş and Kalkan, this beach reveals its turquoise perfection gradually as you descend 187 steps. The sea deepens suddenly; families with children should be cautious on windy days. Arrive before 08:00 — both parking and the beach are nearly empty.
2. **Kekova Island and the Sunken City:** Reachable only by boat, this natural wonder holds the remains of an ancient city submerged by 2nd-century earthquakes. Ancient staircases and house walls are visible through the crystal-clear water as if through glass. Visit with a morning departure tour before the afternoon wind picks up.
3. **Antiphellos Ancient Theatre:** One of the rare ancient structures facing the sea, this Hellenistic theatre sits directly above Kaş town center — a 10-minute walk. The sunset view stretching from the stage to Meis Island becomes one of the most powerful memories of any visit.
4. **Uzun Çarşı (Öğütçü Street):** This bougainvillea-draped, bay-windowed street holds Kaş's bohemian soul. The Lycian Lion Sarcophagus at its end shows how ancient heritage and modern boutique shops can coexist naturally. Handmade jewelry, lichen-dyed fabrics and local ceramics are the most authentic souvenir choices.
5. **Lycian Rock Tombs:** The Doric-style rock tombs commanding Kaş's main street and town square are among the rare examples where history is so completely woven into everyday life. Visible right next to where locals go about their day, and free to visit.
6. **Küçük Çakıl Beach:** The secret of this small but iconic cove just below the center lies in freshwater springs bubbling up from the seabed, making the water ice-cold even in peak Mediterranean summer. The experience of this unexpected chill in the warm sea is genuinely strange and wonderful. Crowds are minimal between 08:00–10:00.

## 🍽️ Flavor Map: Where to Eat

- **Breakfast:** Breakfast culture in Kaş sits far above the standard hotel lobby spread. At restaurants along Büyükçakıl beachfront, a leisurely spread served overlooking the sea is the town's way of starting the day. Local flatbreads, olives and fresh honey are the regional signature.
- **Lunch:** Eating at one of the local fish restaurants above Küçük Çakıl or Büyükçakıl — stepping out of the sea and directly to a table — is as natural a Kaş experience as they come. The meze culture is strong here; fish soup and wood-fired bread make the right opening.
- **Dinner:** Boutique restaurants around Uzun Çarşı offer terrace views toward Meis Island as the finest dinner backdrop in town. Hideaway Hotel's restaurant and Amphora Hotel's terrace sunset dinners require advance reservations.
- **Café Stop:** Manzara Café on Kaş hilltop offers panoramic views; arrive at least 45 minutes before sunset to claim a corner table. Small cafés inside the bazaar are the classic choice for a cool ice cream break.

## 🔍 Local Secrets: The Kaş Few Know

- **Meis Island Day Ferry:** A small ferry departs from Kaş each morning for Kastellorizo (Meis), Greece. Grab your passport, have breakfast on the crossing, and spend an afternoon on this tiny but historically rich Greek island just minutes away.
- **Diving Courses:** Kaş's diving infrastructure is Turkey's most comprehensive. Someone with no prior diving experience can start with safe intro-dive programs. The Airplane Wreck site is an unforgettable experience for advanced divers.
- **Lycian Way:** Turkey's most prestigious long-distance hiking route, the Lycian Way, passes through Kaş. Half-day or day-sections of the coastal path can be walked directly from the town.
- **Day Trips:** Patara Ancient City and Turkey's longest beach (18 km), the ice-cold mountain stream walks in Saklıkent Canyon, and the ancient city of Xanthos at Kınık; all are within half a day's drive from Kaş.
- **The Best Bougainvillea Shot:** Beyond the start of Uzun Çarşı, catching the morning sun on the pink bougainvillea-draped stone houses of Türk Evi Sokağı gives you the most iconic Kaş photograph.
''';
}
"""

TARGET_FILE = "lib/services/city_blog_content.dart"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# The file ends with  '''\n}\n
CLOSING = "''';\n}"
if content.strip().endswith(CLOSING.strip()):
    # Insert _kasTR and _kasEN before the final closing brace
    insert_pos = content.rfind(CLOSING)
    new_content = content[:insert_pos + len(CLOSING) - 1] + "\n" + KAS_TR + "\n" + KAS_EN
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ _kasTR and _kasEN successfully injected into city_blog_content.dart")
else:
    print("❌ Could not find the expected closing pattern. Last 200 chars:")
    print(repr(content[-200:]))
