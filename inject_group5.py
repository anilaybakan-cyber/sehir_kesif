#!/usr/bin/env python3
import os

TARGET_FILE = "lib/services/city_blog_content.dart"

# BUDVA
BUD_TR = r"""
  // BUDVA
  static const _budvaTR = '''
# Budva: Adriyatik'in Orta Çağ Masalı ve Gece Hayatı

**Hızlı Bakış:** Budva, Karadağ'ın (Montenegro) en popüler ve en hareketli sahil kentidir. 2.500 yıllık geçmişiyle Adriyatik'in en eski yerleşimlerinden biri olan Eski Şehri (Stari Grad), masalsı dar sokakları ve tarihi surlarıyla büyüleyicidir. Gündüzleri bembeyaz kumsallarda güneşlenip kristal sularda yüzerken, geceleri Balkanlar'ın en ünlü gece hayatına tanıklık edebileceğiniz dinamik bir şehirdir.

**📝 Gitmeden Önce:**
- **Plaj Seçimi:** Eski şehir yakınındaki Mogren Plajı en popüler olandır ancak biraz daha sakinlik arıyorsanız tekneyle Sveti Nikola adasına geçebilirsiniz.
- **Sveti Stefan:** Budva'nın 15 dakika uzağındaki bu ikonik ada-otel sadece dışarıdan görülebilir (veya restoran rezervasyonuyla girilebilir), ancak gün batımı fotoğrafı için mutlaka durulması gereken bir noktadır.
- **Nakit Para:** Küçük işletmelerde ve taksilerde nakit (Euro) kullanımı yaygındır.

## 📅 Takviminizi Ayarlayın

- **Haziran:** Denizin ısındığı, kalabalığın henüz makul olduğu en keyifli ay.
- **Temmuz-Ağustos:** Adriyatik'in her yerinden gelen turistlerle şehrin "patladığı" en hareketli dönem. Gece hayatı tutkunları için ideal.
- **Eylül:** "Sarı yaz" dönemi. Deniz sıcak, hava yumuşak ve fiyatlar daha uygun.
- **Bahar:** Karadağ'ın doğasını keşfetmek ve eski şehri kalabalıksız gezmek için harika bir zaman.

## 🏠 Nerede Kalmalı

- **Stari Grad (Eski Şehir):** Tarihin tam kalbinde, her yere yürüme mesafesinde butik bir deneyim için.
- **Budva Merkez:** Plajlara, restoranlara ve alışverişe yakın, hareketli bölge.
- **Becici:** Geniş kumsalları ve büyük resort otelleriyle aileler için ideal bölge.
- **Sveti Stefan Çevresi:** Daha lüks, huzurlu ve muazzam manzaralı konaklama için.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Eski şehir ve ana plajlar arası en iyi ulaşım yolu.
- **Otobüs:** Budva'dan Kotor, Tivat ve Cetinje gibi şehirlere düzenli seferler mevcuttur.
- **Tekne:** Civar koylara ve Sveti Nikola adasına gitmek için popüler yol.

## 🏛️ İkonik Duraklar

1. **Stari Grad (Eski Şehir):** Labirent gibi sokakları, kiliseleri ve denize açılan kapılarıyla Orta Çağ atmosferi.
2. **Budva Dans Eden Kız Heykeli:** Mogren yolunda, şehri simgeleyen en meşhur fotoğraf noktası.
3. **Citadela (Hisar):** Eski şehrin en yüksek noktası, deniz ve kiremit çatı manzarası sunan tarihi kale.
4. **Mogren Plajı:** Kayalıkların arasından geçilerek ulaşılan, Budva'nın en güzel halk plajı.
5. **Sveti Nikola Adası (Hawaii):** Budva'nın hemen karşısındaki vahşi doğa ve plaj adası.
6. **Sveti Stefan:** Karadağ'ın kartpostallarını süsleyen efsanevi ada-kasaba.

## 🍽️ Lezzet Haritası

- **Sokak Lezzeti:** Yerel Balkan börekleri (Burek) ve "Cevapi".
- **Deniz Ürünü:** Adriyatik'den taze çıkan kalamar dolma ve siyah risotto.
- **İçecek:** Karadağ'ın meşhur kırmızı şarabı "Vranac" ve yerel birası "Niksicko".
- **Atıştırmalık:** Yerel füme et (Njeguski prsut) ve peynirler.

## 🔍 Lokal Sırlar

- **Kotor Körfezi:** Budva'dan sadece 30 dakika uzaklıktaki bu doğa harikasını mutlaka günübirlik ziyaret edin.
- **Rustovo Manastırı:** Budva tepelerinde, sessiz ve muazzam manzaralı saklı bir ruhani durak.
- **Jaz Plajı:** Şehrin biraz dışındaki, Karadağ'ın en uzun ve festival alanına dönüşen meşhur plajı.
''';
"""

BUD_EN = r"""  static const _budvaEN = '''
# Budva: A Medieval Adriatic Fairytale and Vibrant Nightlife

**Quick Glimpse:** Budva is the most popular and vibrant coastal city in Montenegro. As one of the oldest settlements in the Adriatic with a 2,500-year history, its Old Town (Stari Grad) is fascinating with its fairytale narrow streets and historic walls. It's a dynamic city where you can sunbathe on white sandy beaches and swim in crystal waters by day, while witnessing the most famous nightlife in the Balkans by night.

**📝 Before You Go:**
- **Beach Choice:** Mogren Beach near the old city is the most popular, but if you're looking for more peace, you can head to Sveti Nikola island by boat.
- **Sveti Stefan:** This iconic island-hotel 15 minutes from Budva can only be seen from the outside (or entered with a restaurant reservation), but it's a must-stop for a sunset photo.
- **Cash:** Use of cash (Euro) is common in small businesses and taxis.

## 📅 Set Your Calendar

- **June:** The most enjoyable month when the sea is warm and the crowds are still reasonable.
- **July-August:** The most active period when the city "explodes" with tourists from all over the Adriatic. Ideal for nightlife enthusiasts.
- **September:** The "golden summer" period. The sea is warm, the weather is soft, and prices are more affordable.
- **Spring:** A great time to explore Montenegro's nature and tour the old city without the crowds.

## 🏠 Where to Stay

- **Stari Grad (Old Town):** For a boutique experience in the heart of history, within walking distance of everywhere.
- **Budva Center:** A lively area close to beaches, restaurants, and shopping.
- **Becici:** An ideal area for families with wide sandy beaches and large resort hotels.
- **Around Sveti Stefan:** For more luxurious, peaceful accommodation with magnificent views.

## 🚲 Getting Around

- **Walking:** The best way to travel between the old city and main beaches.
- **Bus:** Regular services from Budva to cities like Kotor, Tivat, and Cetinje are available.
- **Boat:** A popular way to visit nearby coves and Sveti Nikola island.

## 🏛️ Iconic Stops

1. **Stari Grad:** A medieval atmosphere with labyrinthine streets, churches, and gates opening to the sea.
2. **Budva Dancing Girl Statue:** The most famous photo spot symbolizing the city on the Mogren road.
3. **Citadela (Citadel):** The highest point of the old town, a historic fortress offering sea and tile roof views.
4. **Mogren Beach:** Budva's best public beach, reached by passing through the rocks.
5. **Sveti Nikola Island (Hawaii):** A wild nature and beach island right across from Budva.
6. **Sveti Stefan:** The legendary island-town that adorns Montenegro's postcards.

## 🍽️ Flavor Map

- **Street Food:** Local Balkan pastries (Burek) and "Cevapi."
- **Seafood:** Freshly caught squid stuffing and black risotto from the Adriatic.
- **Drink:** Montenegro's famous red wine "Vranac" and local beer "Niksicko."
- **Snack:** Local smoked meat (Njeguski prsut) and cheeses.

## 🔍 Local Secrets

- **Kotor Bay:** Definitely visit this natural wonder just 30 minutes from Budva for a day trip.
- **Rustovo Monastery:** A hidden spiritual stop on Budva's hills with a quiet and magnificent view.
- **Jaz Beach:** The famous beach slightly outside the city that turns into Montenegro's longest festival area.
''';
"""

# KSAMIL
KSA_TR = r"""
  // KSAMIL
  static const _ksamilTR = '''
# Ksamil: Arnavutluk'un "Maldivler"i ve Saklı İncisi

**Hızlı Bakış:** Ksamil, Arnavutluk Rivierası'nın güney ucunda, turkuazın en açık tonlarına sahip denizi ve bembeyaz kumlu adalarıyla Avrupa'nın son yıllardaki en popüler keşif noktalarından biridir. Karşısındaki Korfu adasına el sallayan konumu, taptaze deniz ürünleri ve bütçe dostu tatil anlayışıyla Ksamil, Akdeniz'in o eski, samimi ve doğal halini hala yaşatmaktadır.

**📝 Gitmeden Önce:**
- **Nakit Para:** Arnavutluk'ta "Lek" kullanılsa da turistik yerlerde Euro geçerlidir; ancak çoğu yerde kredi kartı geçmez, mutlaka nakit bulundurun.
- **Erken Gelin:** Ksamil'in ana plajları yazın çok kalabalık olabilir; şezlong bulmak için sabah 09:00 öncesi plajda olun.
- **Butrint Antik Kenti:** Ksamil'e sadece 10 dakika uzaklıktaki bu UNESCO mirasını mutlaka görün.

## 📅 Takviminizi Ayarlayın

- **Haziran / Eylül:** Denizin harika, kalabalığın makul ve fiyatların en iyi olduğu dönem.
- **Temmuz-Ağustos:** Adriyatik'in en yoğun ve en sıcak dönemi. Enerji yüksek ama plajlar çok dolu.
- **Bahar:** Doğa yürüyüşleri ve kalabalıksız antik kent gezileri için ideal.
- **Kış:** Şehrin tamamen uykuya daldığı, çoğu tesisin kapalı olduğu dönem.

## 🏠 Nerede Kalmalı

- **Ksamil Merkez:** Plajlara yürüme mesafesinde, butik aile işletmeleri ve otellerin olduğu bölge.
- **Saranda:** Ksamil'e 15 dakika mesafede, daha gelişmiş, gece hayatı ve limanı olan ana şehir.
- **Butrint Çevresi:** Daha sakin ve doğa ile iç içe konaklama arayanlar için.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Ksamil içinde her yer yürüme mesafesindedir.
- **Otobüs:** Saranda'dan Ksamil ve Butrint'e her 30 dakikada bir düzenli otobüs seferleri vardır.
- **Tekne:** Plajın hemen karşısındaki 3 adaya gitmek için kiralanan botlar veya deniz bisikletleri.
- **Araç Kiralama:** Diğer Riviera köylerini (Himara, Dhermi) keşfetmek için önerilir.

## 🏛️ İkonik Duraklar

1. **Ksamil Adaları:** Kıyıdan kolayca ulaşılabilen, kristal sulu 3 küçük doğa harikası ada.
2. **Butrint Antik Kenti:** UNESCO listesindeki, orman içinde saklı devasa Yunan-Roma harabeleri.
3. **Mavi Göz (Syri i Kalter):** Ksamil'e 30 dakika mesafede, yerin altından fışkıran buz gibi, masmavi doğal su kaynağı.
4. **Lekuresi Kalesi:** Saranda tepesinde, gün batımı ve tüm körfez manzarasını izleyebileceğiniz kale.
5. **Mirror Beach (Plazhi i Pasqyrave):** Ksamil yakınında, suyun yansımasıyla meşhur daha sakin bir koy.
6. **Korfu Manzarası:** Sahilden çıplak gözle görülebilen Yunan adası manzarası.

## 🍽️ Lezzet Haritası

- **Deniz Ürünü:** Taptaze "Mussels" (midye) - Butrint gölünden gelir ve Ksamil'in simgesidir.
- **Sokak Lezzeti:** Arnavut böreği olan "Byrek" ve "Qofte" (köfte).
- **Akşam Yemeği:** Deniz kenarındaki tavernalarda ızgara deniz ürünleri ve yerel beyaz şarap.
- **İçecek:** Yerel Arnavut rakısı.

## 🔍 Lokal Sırlar

- **Pulëbardha Plajı:** Turistlerin çoğunun kaçırdığı, sarp kayalıklar altındaki muazzam berrak plaj.
- **Borsh Köyü:** Avrupa'nın en uzun plajlarından birine ve şelale içindeki kafelere sahip yakındaki köy.
- **Zeytinyağı:** Bölgenin taze zeytinyağlarını yerel pazarlardan almayı unutmayın.
''';
"""

KSA_EN = r"""  static const _ksamilEN = '''
# Ksamil: Albania's "Maldives" and a Hidden Gem

**Quick Glimpse:** Ksamil is one of Europe's most popular recent discoveries, located at the southern tip of the Albanian Riviera, with its turquoise-clear waters and white sandy islands. With its location waving across to the island of Corfu, its fresh seafood, and budget-friendly holiday approach, Ksamil still keeps that old, intimate, and natural spirit of the Mediterranean alive.

**📝 Before You Go:**
- **Cash:** While the "Lek" is used in Albania, Euros are accepted in tourist spots; however, credit cards are not accepted in many places, so definitely keep cash.
- **Arrive Early:** Main beaches in Ksamil can be very crowded in summer; be on the beach before 9 AM to find a sun lounger.
- **Butrint Ancient City:** Definitely see this UNESCO heritage site just 10 minutes from Ksamil.

## 📅 Set Your Calendar

- **June / September:** The period when the sea is great, crowds are reasonable, and prices are best.
- **July-August:** The busiest and hottest period in the Adriatic. High energy but very full beaches.
- **Spring:** Ideal for nature walks and touring ancient cities without the crowds.
- **Winter:** The period when the town falls completely asleep and most facilities are closed.

## 🏠 Where to Stay

- **Ksamil Center:** An area with boutique family businesses and hotels within walking distance of the beaches.
- **Saranda:** The main city 15 minutes from Ksamil, with a more developed nightlife and harbor.
- **Around Butrint:** For those seeking quieter accommodation in touch with nature.

## 🚲 Getting Around

- **Walking:** Everywhere in Ksamil is within walking distance.
- **Bus:** Regular buses run every 30 minutes from Saranda to Ksamil and Butrint.
- **Boat:** Boats or pedalos rented to go to the 3 islands right across the beach.
- **Car Rental:** Recommended for exploring other Riviera villages (Himara, Dhermi).

## 🏛️ Iconic Stops

1. **Ksamil Islands:** 3 small natural wonder islands with crystal waters easily reached from the shore.
2. **Butrint Ancient City:** Massive Greco-Roman ruins hidden in the forest, on the UNESCO list.
3. **Blue Eye (Syri i Kalter):** An ice-cold, deep blue natural water spring bubbling from underground, 30 minutes from Ksamil.
4. **Lekuresi Castle:** A fortress on Saranda's hill where you can watch the sunset and the entire bay panorama.
5. **Mirror Beach (Plazhi i Pasqyrave):** A quieter bay near Ksamil famous for the reflection of the water.
6. **Corfu View:** The view of the Greek island visible to the naked eye from the shore.

## 🍽️ Flavor Map

- **Seafood:** Fresh "Mussels"—they come from Butrint Lake and are the symbol of Ksamil.
- **Street Food:** Albanian pie "Byrek" and "Qofte" (meatballs).
- **Dinner:** Grilled seafood and local white wine at seaside tavernas.
- **Drink:** Local Albanian raki.

## 🔍 Local Secrets

- **Pulëbardha Beach:** A magnificent clear beach under steep cliffs that most tourists miss.
- **Borsh Village:** A nearby village with one of Europe's longest beaches and cafes inside waterfalls.
- **Olive Oil:** Don't forget to buy the region's fresh olive oils from local markets.
''';
"""

# SELANIK
SEL_TR = r"""
  // SELANIK
  static const _selanikTR = '''
# Selanik: Ege'nin Kuzey Yıldızı, Tarih ve Gastronomi Şehri

**Hızlı Bakış:** Selanik (Thessaloniki), Yunanistan'ın ikinci büyük şehri olmasının ötesinde, binlerce yıllık çok kültürlü mirasıyla Ege'nin en ruhlu kentidir. Osmanlı, Bizans ve Roma izlerinin birbirine karıştığı sokakları, hiç uyumayan sahil şeridi ve Balkanlar'ın en zengin mutfak kültürüyle burası bir keşif cennetidir. Atatürk'ün doğduğu evden görkemli Beyaz Kule'ye kadar Selanik, her adımda tarihin ve dostluğun hissedildiği bir şehirdir.

**📝 Gitmeden Önce:**
- **Yürüyüş Rotası:** Selanik bir sahil şehridir. Aristotelous Meydanı'ndan Beyaz Kule'ye kadar olan deniz yolu (Paralia) şehrin kalbidir.
- **Pazar Günleri:** Çoğu dükkan ve bazı müzeler pazar günü kapalı olabilir, planınızı buna göre yapın.
- **Yeme-İçme:** Selanik, Yunanistan'ın gastronomi başkenti kabul edilir. Ladadika bölgesinde yemek yemeden dönmeyin.

## 📅 Takviminizi Ayarlayın

- **Bahar:** Şehrin en keyifli, yürüyerek keşfetmek için ideal sıcaklıkta olduğu dönem.
- **Sonbahar (Ekim-Kasım):** Selanik Uluslararası Film Festivali dönemi. Şehrin en entelektüel ve canlı zamanı.
- **Yaz:** Şehir merkezi sıcak olabilir ama 1 saat mesafedeki Halkidiki plajları için en iyi zaman.
- **Kış:** Noel pazarları ve hareketli gece hayatıyla şehrin daha lokal ve samimi olduğu dönem.

## 🏠 Nerede Kalmalı

- **Aristotelous Meydanı Çevresi:** Şehrin tam merkezi, her yere yürüme mesafesinde olmak isteyenler için.
- **Ladadika:** Tarihi doku, restoranlar ve gece hayatına en yakın olmak isteyenler için.
- **Ano Poli (Eski Şehir):** Tepede, deniz manzaralı, dar sokaklı ve daha otantik konaklama için.
- **Tsimiski / Egnatia:** Alışveriş ve iş merkezlerine yakın, modern otellerin olduğu bölge.

## 🚲 Şehir İçi Ulaşım

- **Yürümek:** Merkez oldukça kompakttır, keşfetmenin en iyi yolu yürümektir.
- **Otobüs:** Şehir içi ulaşım ağı oldukça geniştir (OASTH).
- **Bisiklet:** Sahil şeridi boyunca bisiklet sürmek oldukça keyifli ve yaygındır.
- **Taksi:** Şehirde oldukça fazla ve uygun fiyatlı taksi mevcuttur.

## 🏛️ İkonik Duraklar

1. **Beyaz Kule:** Şehrin sembolü, Osmanlı mirası olan tarihi kule ve müze.
2. **Atatürk Evi Müzesi:** Mustafa Kemal Atatürk'ün doğduğu ve çocukluğunun geçtiği tarihi bina.
3. **Aristotelous Meydanı:** Şehrin ana buluşma noktası, denize açılan devasa meydan.
4. **Ano Poli (Yukarı Şehir):** Şehrin yangından kurtulan en eski mahallesi, Bizans surları ve muazzam körfez manzarası.
5. **Agios Dimitrios Kilisesi:** Şehrin koruyucusuna adanmış, muazzam mozaikleriyle UNESCO mirasındaki kilise.
6. **Rotunda ve Galerius Kemeri:** Roma döneminden kalma, şehrin en görkemli antik anıtları.

## 🍽️ Lezzet Haritası

- **Kahvaltı:** Meşhur "Selanik Gevreği" (Koulouri) veya kremalı "Bougatsa".
- **Öğle:** Kapani veya Modiano pazarlarında taze ve yerel atıştırmalıklar.
- **Akşam:** Ladadika'da uzo eşliğinde deniz ürünleri veya "Soutzoukakia" (İzmir köfte).
- **Tatlı:** Meşhur "Trigona" (şerbetli üçgen tatlı) veya "Selanik çöreği" (Tsoureki).

## 🔍 Lokal Sırlar

- **Halkidiki:** Selanik'e 1-2 saat mesafedeki, turkuaz sularıyla meşhur üç parmaklı yarımadayı mutlaka ziyaret edin.
- **Bit Bazaar:** Eski eşyaların satıldığı, akşamları ise öğrencilerin doldurduğu tavernalara dönüşen gizli avlu.
- **Seih Sou Ormanı:** Şehre tepeden bakan, doğa yürüyüşü ve temiz hava için lokallerin kaçış noktası.
''';
"""

SEL_EN = r"""  static const _selanikEN = '''
# Thessaloniki: The North Star of the Aegean, City of History and Gastronomy

**Quick Glimpse:** Beyond being Greece's second-largest city, Thessaloniki is the most soulful city of the Aegean with its thousands of years of multicultural heritage. Its streets, where Ottoman, Byzantine, and Roman traces mix, its never-sleeping coastline, and the richest culinary culture of the Balkans make it a paradise for discovery. From the house where Atatürk was born to the majestic White Tower, Thessaloniki is a city where history and friendship are felt at every step.

**📝 Before You Go:**
- **Walking Route:** Thessaloniki is a coastal city. The sea path (Paralia) from Aristotelous Square to the White Tower is the heart of the city.
- **Sundays:** Most shops and some museums may be closed on Sundays, so plan accordingly.
- **Eating & Drinking:** Thessaloniki is considered the gastronomic capital of Greece. Don't return without eating in the Ladadika area.

## 📅 Set Your Calendar

- **Spring:** The city's most enjoyable time, with temperatures ideal for exploring on foot.
- **Autumn (October-November):** Thessaloniki International Film Festival period. The most intellectual and vibrant time of the city.
- **Summer:** The city center can be hot, but it's the best time for the Halkidiki beaches just 1 hour away.
- **Winter:** The period when the city is more local and intimate with Christmas markets and a lively nightlife.

## 🏠 Where to Stay

- **Around Aristotelous Square:** The exact center of the city, for those who want to be within walking distance of everywhere.
- **Ladadika:** For those who want to be closest to historical texture, restaurants, and nightlife.
- **Ano Poli (Old Town):** For more authentic accommodation with narrow streets and sea views on the hill.
- **Tsimiski / Egnatia:** A central area with modern hotels, close to shopping and business centers.

## 🚲 Getting Around

- **Walking:** The center is quite compact; walking is the best way to explore.
- **Bus:** The urban transport network is quite extensive (OASTH).
- **Bicycle:** Cycling along the coastline is quite pleasant and common.
- **Taxi:** There are plenty of reasonably priced taxis in the city.

## 🏛️ Iconic Stops

1. **White Tower:** The symbol of the city, a historic tower and museum from the Ottoman heritage.
2. **Atatürk House Museum:** The historic building where Mustafa Kemal Atatürk was born and spent his childhood.
3. **Aristotelous Square:** The city's main meeting point, a massive square opening to the sea.
4. **Ano Poli (Upper Town):** The city's oldest neighborhood that survived the fire, with Byzantine walls and magnificent bay views.
5. **Agios Dimitrios Church:** A church on the UNESCO heritage list dedicated to the city's protector, with magnificent mosaics.
6. **Rotunda and Arch of Galerius:** The most magnificent ancient Roman monuments in the city.

## 🍽️ Flavor Map

- **Breakfast:** Famous "Thessaloniki Bagel" (Koulouri) or custard-filled "Bougatsa."
- **Lunch:** Fresh and local snacks at Kapani or Modiano markets.
- **Evening:** Seafood accompanied by ouzo or "Soutzoukakia" (meatballs) in Ladadika.
- **Sweet:** Famous "Trigona" (triangular syrup-soaked pastry) or "Thessaloniki bun" (Tsoureki).

## 🔍 Local Secrets

- **Halkidiki:** Definitely visit the three-fingered peninsula famous for its turquoise waters, just 1-2 hours from Thessaloniki.
- **Bit Bazaar:** A hidden courtyard where old items are sold and which turns into tavernas filled with students in the evenings.
- **Seih Sou Forest:** A local escape for nature walks and fresh air overlooking the city.
''';
"""

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Add switch cases
CASE_ADDITIONS = """      case 'budva':
        return isEnglish ? _budvaEN : _budvaTR;
      case 'ksamil':
        return isEnglish ? _ksamilEN : _ksamilTR;
      case 'selanik':
      case 'thessaloniki':
        return isEnglish ? _selanikEN : _selanikTR;"""

if "default:" in content:
    content = content.replace("default:", CASE_ADDITIONS + "\n      default:")

# Add variables at the end
if content.strip().endswith("}"):
    insert_pos = content.rfind("}")
    new_vars = BUD_TR + "\n" + BUD_EN + "\n" + KSA_TR + "\n" + KSA_EN + "\n" + SEL_TR + "\n" + SEL_EN + "\n"
    content = content[:insert_pos] + new_vars + content[insert_pos:]

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Group 5 (Budva, Ksamil, Selanik) successfully injected.")
