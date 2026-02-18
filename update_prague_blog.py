
import csv
import json
import os

# --- PATHS ---
CSV_PATH = '/Users/anilebru/Desktop/prag_yeni_mekan_onerileri_full.csv'
OUTPUT_DIR = 'ota_data_pack/guides'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'prag.json')

# --- EXISTING CONTENT (Copied from CityBlogContent.dart) ---
PRAG_TR = """# Prag: Zamanın Dokunmaya Kıyamadığı Şehir

**Hızlı Bakış:** Avrupa’nın tam kalbinde, masallardan fırlamış gotik kulelerin ve tarihin sisli puslu havasının içine hoş geldin. Prag için boşuna "Yüz Kuleli Şehir" ya da "Altın Şehir" denmiyor. Vltava Nehri’nin iki yakasına yayılan bu şehir, II. Dünya Savaşı’ndan neredeyse hiç zarar görmeden kurtulduğu için Avrupa’nın en iyi korunmuş tarihi merkezlerinden birine sahip. Gotik, Barok ve Rönesans mimarisinin iç içe geçtiği sokaklarda yürürken kendinizi bir film setinde gibi hissetmeniz çok normal. Prag sadece mimari değil, aynı zamanda Franz Kafka’nın melankolisi, Mozart’ın müziği ve dünyanın en iyi bira kültürüyle harmanlanmış bir karakterdir.

Gitmeden Önce Küçük Bir Not: Prag AB üyesi olsa da Euro kullanmıyor, resmi para birimi Çek Korunası (CZK). Euro ile ödeme yapmaya çalıştığınızda büyük kur farklarıyla karşılaşmanız muhtemel. Sokaklardaki döviz bürolarına da biraz temkinli yaklaşmakta fayda var; "komisyonsuz" tabelalarına rağmen gizli ücretlerle karşılaşabilirsiniz. Neyse ki Prag kart kullanımı konusunda oldukça uygun bir şehir; güvenilir banka ATM’leri veya doğrudan kartla ödeme yapmak en zahmetsiz yol olacaktır.

Lezzetli Bir Yanılgı: Prag sokaklarında her köşe başında göreceğiniz o meşhur Trdelník (makara tatlısı) aslında sanıldığı gibi kadim bir Çek geleneği değildir; 2000'lerin başında popülerleşmiş bir "modern klasik"tir. Gerçek Prag deneyimi için rotayı Astronomik Saat’in önündeki kalabalıktan biraz saptırıp, Vinohrady veya Letná gibi mahallelerin yerel meyhanelerine kırmalısınız. Şunu da unutmayın: Prag’da bira suyla yarışır; bazen sudan daha ucuzdur ve kesinlikle en sevilen milli içecektir.

## 📅 Takviminizi Ayarlayın: Hangi Mevsim Sizin?
Prag her mevsimde farklı bir kostüm giyen, ruh hali değişen ama cazibesini asla kaybetmeyen bir şehir. Hava durumuyla birlikte karakteri tamamen değişen bu şehirde, kalabalıkları mı, kış masalını mı yoksa altın sarısı yaprakları mı sevdiğine karar verme vakti.

- **Bahar (Nisan - Haziran)**: Şehrin uyanışıdır. Petřín Tepesi'nde kiraz çiçekleri açarken Prag, Avrupa'nın en romantik durağına dönüşür. Hava gezmek için idealdir (15-20°C) ve turist kalabalığı henüz zirveye ulaşmamıştır.
- **Yaz (Temmuz - Ağustos)**: Şehrin en canlı ama aynı zamanda en yorucu zamanıdır. Hava sıcaklıkları 30°C’yi zorlayabilir ve [Charles Köprüsü](search:Charles Köprüsü)'nde iğne atsanız yere düşmez. Eğer kalabalık ve bitmeyen yaz akşamlarını seviyorsanız tam sırası.
- **Sonbahar (Eylül - Ekim)**: Prag’ın "Altın Şehir" unvanını gerçekten hak ettiği dönemdir. Vltava Nehri kıyısındaki ağaçlar sarı ve kızıl tonlara bürünürken şehir puslu ve melankolik bir havaya girer. Fotoğraf tutkunları için en iyi ışıktır.
- **Kış (Kasım - Mart)**: Hava gerçekten dondurucudur ancak Aralık ayında kurulan Noel Pazarları şehri gerçek bir masal dünyasına çevirir. Ocak ve Şubat ayları ise en ekonomik dönemdir; turist trafiği azalır, konaklama fiyatları düşer ve Prag'ın o meşhur gotik kuleleri kar altında büyüleyici görünür.

## 🏠Nerede Kalmalı: Mahalle Rehberi
Prag'da konaklama seçimi aslında "Bir turist gibi mi hissetmek istiyorum, yoksa bir Praglı gibi mi?" sorusuna verdiğin cevaba göre değişir. Şehir bölgelere ayrılmıştır (Prague 1, 2, 3...) ve rakam ne kadar küçükse merkeze o kadar yakınsın demektir. Prag’ın mahalleleri ise sadece birer yerleşim alanı değil, her biri farklı bir zaman dilimine açılan kapılardır. Konaklayacağın yer, sabah uyandığında göreceğin manzaranın gotik bir kule mi yoksa modern bir sanat galerisi mi olacağını belirler.

- **Staré Město (Eski Şehir - Prague 1)**: Prag’ın kalbi ve ilk kez gidenlerin favorisidir. Astronomik Saat ve [Eski Şehir Meydanı](search:Eski Şehir Meydanı)’na kapı komşusu olursunuz. Her yere yürüyerek ulaşmak harikadır ancak burası şehrin en kalabalık ve en pahalı bölgesidir.
- **Malá Strana (Lesser Town - Prague 1)**: Vltava’nın diğer yakasında, kalenin hemen altındaki bu bölge Prag’ın en romantik yeridir. Barok binalar, dar sokaklar ve elçiliklerin olduğu bu alan, Eski Şehir’e göre geceleri daha sessiz ve huzurludur.
- **Nové Město (Yeni Şehir - Prague 1/2)**: Adı "yeni" olsa da tarihi 14. yüzyıla dayanır. Wenceslas Meydanı buradadır. Ulaşım ağının merkezidir ve gece hayatı, alışveriş, büyük oteller için en ideal noktadır.
- **Vinohrady (Prague 2)**: "Praglı gibi yaşamak" istiyorsanız rotanız burası olmalı. Art Nouveau binaları, şık kafeleri, dünya mutfağından restoranları ve yeşil parklarıyla şehrin en nezih bölgesidir. Merkeze tramvayla sadece 10 dakika uzaklıktadır.
- **Žižkov (Prague 3)**: Şehrin biraz daha bohem, asi ve ekonomik yüzüdür. Dünyanın metrekare başına en çok meyhane (pub) düşen yerlerinden biri olduğu söylenir. Gece hayatını ve lokal bira kültürünü seven gençler için birebirdir.

## 🚲 A Noktasından B Noktasına: Bir Lokal Gibi Hareket Edin
Prag yürümek için yaratılmış bir şehir olmakla birlikte, labirenti andıran dar sokakları ve Vltava Nehri boyunca uzanan geniş bulvarlarıyla ulaşım açısından da tam bir mühendislik harikasıdır. Şehirde toplu taşıma o kadar dakiktir ki, saatinizi tramvayların varış süresine göre ayarlayabilir, rayların ve nehrin ritmine kendinizi güvenle bırakabilirsiniz.

- **Havalimanından Şehre İlk Adım**: Václav Havel’den Merkeze Ulaşım Prag’a vardığınızda sizi doğrudan merkeze götüren bir metro hattı bulunmasa da, toplu taşıma sistemi bu boşluğu mükemmel bir şekilde doldurur. En ekonomik ve lokal yöntem, Terminal 1 veya 2’den kalkan Trolleybus 59 hattına binmektir. Bu hat sizi hızlıca Metronun A (Yeşil) hattındaki Nádraží Veleslavín istasyonuna ulaştırır ve standart şehir içi biletleriniz burada geçerlidir. Eğer daha konforlu ve aktarmasız bir yol arıyorsanız, ana tren istasyonuna (Hlavní nádraží) giden Airport Express (AE) otobüslerini tercih edebilirsiniz; ancak bu hat için şoförden yaklaşık 100 CZK karşılığında özel bir bilet almanız gerekecektir. Daha modern bir seçenek arayanlar için ise Prag’ın resmî taksi hizmeti Uber üzerinden yürütülür; uygulama üzerinden sabit fiyatla güvenli bir yolculuk yapabilirsiniz.
- **Arnavut Kaldırımlarında Zaman Yolculuğu**: Yürünebilirlik Prag, ruhunu ancak yürüyerek teslim eden şehirlerdendir. Eski Şehir (Staré Město), [Yahudi Mahallesi](search:Yahudi Mahallesi) (Josefov) ve Malá Strana gibi ana duraklar birbirine sadece birkaç dakikalık yürüme mesafesindedir. Ancak bu masalsı yürüyüşün bir bedeli vardır: Prag’ın o meşhur, estetik ama insafsız Arnavut kaldırımları (cobblestones). Şehri keşfederken "stil" yerine kesinlikle "konfor" odaklı bir ayakkabı seçmek, bir turisti lokalden ayıran en büyük farktır. Yürürken başınızı yukarı kaldırmayı unutmayın; çünkü Prag’ın asıl hazineleri binaların çatı katlarında ve pencere pervazlarındaki detaylarda saklıdır.
 - **Rayların ve Yerin Altındaki Hız**: Tramvay ve Metro Sistemi Şehrin asıl damarları olan tramvaylar, Prag’ın karakterini yansıtır. Özellikle 22 numaralı tramvay, sıradan bir ulaşım aracından ziyade "en ucuz şehir turu" gibidir; sizi nehir kıyısından alıp Prag Kalesi’nin dik yamaçlarına kadar panoramik bir manzara eşliğinde çıkarır. Gece yarısından sonra ise 90-99 arası hatlar devreye girerek sizi şehrin her noktasına güvenle taşır. Eğer zamanınız kısıtlıysa ve daha hızlı hareket etmeniz gerekiyorsa, A, B ve C hatlarından oluşan metro sistemi imdadınıza yetişir. Dünyanın en derin istasyonlarından biri olan Náměstí Míru gibi duraklarda devasa yürüyen merdivenlerle yerin altına inerken, Prag’ın modern yüzüyle tanışırsınız.
-  **Bütçenizi ve Rotanızı Yönetin**: Biletler ve Visitor Pass Prag’da ulaşım sistemi mesafeye değil, zamana dayalıdır. Bu, biletinizin geçerli olduğu süre boyunca sınırsız aktarma yapabileceğiniz anlamına gelir. Kısa mesafeler için 30 dakikalık bilet (30 CZK), daha kapsamlı bir yolculuk için ise 90 dakikalık bilet (40 CZK) idealdir. Eğer şehri 2-3 gün boyunca yoğun bir şekilde gezecekseniz, 24 saatlik (120 CZK) veya 72 saatlik (330 CZK) kartlar büyük bir konfor sağlar. Ancak Prag’ı tam anlamıyla fethetmek isterseniz, Barselona Card'ın buradaki karşılığı olan Prague Visitor Pass en iyi dostunuz olacaktır. Bu kart sadece sınırsız ulaşımı (havalimanı dahil) kapsamakla kalmaz, aynı zamanda Prag Kalesi, Astronomik Saat Kulesi ve Yahudi Müzesi gibi 60’tan fazla önemli noktaya ücretsiz giriş imkânı sunar.
- **Alternatif Yollar**: Nehir, Tepe ve Pedallar Prag’ın en keyifli ulaşım yöntemlerinden biri, Malá Strana’dan kalkıp şehre tepeden bakmanızı sağlayan Petřín Füniküleri’dir. Eğer 24 saatlik veya daha uzun süreli bir ulaşım kartınız varsa, bu nostaljik yolculuk tamamen ücretsizdir. Vltava Nehri’nin tadını çıkarmak isterseniz, toplu taşıma sistemine dahil olan küçük nehir feribotlarını kullanarak iki yaka arasında kısa bir su turu yapabilirsiniz. Şehir merkezi yaya trafiği ve tramvay rayları nedeniyle bisiklet için biraz riskli olsa da, nehir boyundaki Naplavka hattında Rekola (pembe bisikletler) veya Nextbike uygulamalarıyla bisiklet sürmek lokallerin en sevdiği hafta sonu aktivitelerinden biridir.
- **Lokal Etiket**: Yazısız Ulaşım Kuralları Prag ulaşımında dürüstlük sistemi esastır; metro girişlerinde turnike göremezsiniz. Ancak biletinizi tramvaya bindiğinizde veya metro girişindeki sarı makinelerde mutlaka onaylatmalısınız (validate). Sivil denetçilerle karşılaşma ihtimaliniz yüksektir ve biletiniz cebinizde olsa dahi onaylatılmamışsa ağır cezalarla karşılaşırsınız. Şehrin ritmine uyum sağlamak için metroda yürüyen merdivenlerin her zaman sağında durmalı, sol tarafı acelesi olan lokallere bırakmalısınız. En kritik kural ise şudur: Prag’da tramvayların her zaman mutlak önceliği vardır. Yaya geçidinde olsanız bile bir tramvayın sizin için durmasını beklemeyin; Praglıların dediği gibi, "Tramvay her zaman kazanır!"

## 🏛️ Şehrin Hafızası: Görülmesi Gereken İkonik Duraklar
Prag’ın her bir taşı, binlerce yılın birikimini ve imparatorlukların görkemini sessizce fısıldar. Burası, her adımda Orta Çağ’ın gizemli atmosferine çekileceğiniz, zamanın farklı katmanlarının iç içe geçtiği yaşayan bir açık hava sahnesidir.

- **Prag Kalesi (Pražský hrad)**: Dünyanın en büyük antik kale kompleksi olarak kabul edilir. Şehrin siluetine hükmeden bu devasa yapının içinde, Gotik mimarinin zirvesi olan Aziz Vitus Katedrali'ni mutlaka görülmeli. Girişteki güvenlik ve bilet kuyrukları zaman zaman uzayabiliyor; bu nedenle biletinizi önceden online almak ve sabah erken saatleri tercih etmek ziyaretinizi oldukça rahatlatır.
- **Altın Yol (Zlatá ulička)**: Kale kompleksinin içinde yer alan Altın Yol, rengârenk minik evleriyle sizi 16. yüzyıla götürür. Bir dönem simyacıların yaşadığına inanılan bu sokakta, 22 numaralı ev, Franz Kafka’nın en sakin eserlerini kaleme aldığı yer olarak bilinir.
- [Charles Köprüsü (Karlův most)](search:Charles Köprüsü): Vltava Nehri üzerindeki [Charles Köprüsü](search:Charles Köprüsü), üzerindeki 30 Barok heykelle Prag’ın en güçlü simgelerinden biridir. Eski Şehir ile Malá Strana’yı birbirine bağlayan köprü, aynı zamanda açık havada kurulmuş bir sanat galerisi hissi verir. Gün doğumu ve gün batımı saatleri, köprüyü daha sakin görmek için ideal zamanlardır.
- **Lennon Duvarı (Lennonova zeď)**: [Charles Köprüsü](search:Charles Köprüsü)’nün hemen bitiminde yer alan Lennon Duvarı, barış ve özgürlüğün sembolü haline gelmiş bir durak. 1980’lerden bu yana sürekli değişen grafitilerle kaplı bu alan, Prag’ın modern hafızasında direnişin ve ifade özgürlüğünün en renkli yansımalarından biri olarak görülür.
- [Eski Şehir Meydanı](search:Eski Şehir Meydanı) ve Astronomik Saat (Orloj): Gotik ve Barok binalarla çevrili [Eski Şehir Meydanı](search:Eski Şehir Meydanı), Avrupa’nın en etkileyici meydanlarından biridir. Meydandaki Astronomik Saat, hâlâ çalışan dünyanın en eski astronomik saati olarak bilinir. Saat başı yapılan kısa gösteri ilgi çekse de, beklentiyi çok yükseltmek yerine saatin üzerindeki o inanılmaz detaylara ve sembolleri incelemeye odaklanmak çok daha keyifli bir deneyim sunar. 
- **Klementinum Kütüphanesi (Klementinum)**: "Dünyanın en güzel kütüphanesi" unvanını hak eden bu Barok şaheser, sizi devasa küreler ve el yazmaları arasında büyüleyici bir sessizliğe davet eder. Gitmeden önce bilmenizde fayda var ki Klementinum sadece rehberli turlarla gezilebilir ve kontenjanlar oldukça sınırlı. Mağdur olmamak için mutlaka birkaç gün önceden online rezervasyon yaptırmanız faydalı olacaktır.
- [Belediye Binası (Obecní dům)](search:Obecní Dům): Barut Kapısı’nın hemen yanında yükselen bu yapı, Prag’daki Art Nouveau (Genç Üslup) akımının en görkemli temsilcilerinden biridir. Cephesindeki devasa mozaikleriyle şehirdeki sanatsal canlılığın kalbidir.
- [Yahudi Mahallesi (Josefov)](search:Yahudi Mahallesi): Avrupa’nın en iyi korunmuş Yahudi yerleşimlerinden biridir. Altı sinagog ve o meşhur Eski Yahudi Mezarlığı burada yer alır. Tüm sinagogları ve mezarlıkları ziyaret etmeyi planlıyorsanız, kombine bilet almak hem daha pratik hem de daha ekonomik bir seçenek sunacaktır. Biletinizi mahalledeki gişelerden ya da online olarak alabilirsiniz. 
- [Dans Eden Ev (Tančící dům)](search:Dans Eden Ev): Prag sadece Orta Çağ’dan ibaret değildir. Nehir kenarındaki bu modern yapı, şehrin tarihi dokusu içinde aykırı ama büyüleyici bir kontrast yaratır.
- [Vyšehrad](search:Vyšehrad): Prag Kalesi’nin kalabalığından kaçmak isteyenler için "şehrin doğum yeri" kabul edilen bu kale, muazzam bir nehir manzarası ve huzurlu bir park alanı sunar.

## 🍴 Şehrin Lezzet Haritası: Et, Hamur ve Bira Kültürü
Prag mutfağı, Orta Avrupa’nın kalbinde yer almanın getirdiği o "rahatlatıcı" (comfort food) karakteri en iyi yansıtan yerlerden biridir. Burada her tabak, sizi soğuk bir kış gününde şömine başında ağırlayan eski bir dost gibidir.

- **Vepřo-knedlo-zelo (Ulusal Bir Gurur)**: Prag mutfağının sarsılmaz temelidir. Yavaş yavaş fırınlanmış, lokum kıvamındaki domuz eti, yanındaki meşhur knedlíky (ekmek topları) ve karamelize edilmiş ekşi-tatlı lahana turşusu (zelí) ile servis edilir. Bu üçlü, Çeklerin "kutsal kasesi" gibidir; etin ağırlığı lahananın ekşiliğiyle, sosun yoğunluğu ise ekmek toplarıyla kusursuz bir dengeye ulaşır.
- **Svíčková na smetaně (İmparatorluk Zarafeti)**: Çek mutfağının en sofistike yemeğidir. Sığır eti, tam 24 saat boyunca kök sebzeler ve baharatlarla marine edilir. Ortaya çıkan o yoğun, kremamsı havuç ve kök sebze sosu, bir kaşık yaban mersini reçeli ve taze çırpılmış krema ile tamamlanır. Bir tabakta hem tatlıyı hem tuzluyu bu kadar asilce birleştiren başka bir lezzet bulmak zordur.
- **Pilsner (Tekutý Chléb - Sıvı Ekmek)**: Prag’da bira sadece bir içecek değil, hayatın kendisidir; onlara göre ise "sıvı ekmek". Dünyanın ilk altın sarısı pilsnerinin doğduğu bu topraklarda bira, özel musluk teknikleriyle doldurulur. Bardağın üçte birini kaplayan o ıslak, yoğun ve kadifemsi köpük (Hladinka), biranın tazeliğinin ve zanaatın imzasıdır.
- **Guláš (Çek Gulaşı)**: Macar kuzeninden farklı olarak daha koyu bir kıvama ve daha az sebzeye sahiptir. Bol soğan, kimyon ve bazen bir miktar bira ile ağır ateşte pişirilen bu sığır eti yahnisi, yanındaki çiğ soğan halkaları ve taze dumplings ile Prag kışlarının en sıcak sığınağıdır.
- **Trdelník (Sokakların Tarçınlı Ruhu)**: Prag’ın o meşhur Orta Çağ sokaklarında yürürken burnunuza gelen tarçın kokusunun kaynağıdır. Ateş üzerinde dönen rulo hamurların üzerine serpilen şeker ve ceviz, karamelize bir kabuk oluşturur. İster sade, ister içi çikolatayla kaplı olsun; bu tatlı Prag’ın masalsı atmosferinin ayrılmaz bir parçasıdır.
- **Smažený Sýr (Altın Renkli Suçlu Zevk)**: Prag birahanelerinin en sevilen "atıştırmalığıdır". Kalın bir dilim Edam veya Hermelín peynirinin panelenip dışı çıtır, içi ise akışkan olana kadar kızartılmasıyla yapılır. Yanındaki tartar sos ve haşlanmış patatesle, basitliğin ne kadar lezzetli olabileceğinin kanıtıdır.
- **Nakládaný Hermelín (Birahane Klasiği)**: Gerçek bir Praglı gibi hissetmek istiyorsanız denemeniz gereken o meşhur meze. Cam kavanozlarda günlerce yağ, sarımsak, acı biber ve baharatlarla bekletilen yumuşak peynir, taze Çek ekmeğinin üzerine sürülerek yenir. Biranın en sadık eşlikçisidir.
- **Chlebíčky (Görsel Bir Şölen)**: Prag’ın hızlı yaşamına ayak uyduran ama estetiğinden ödün vermeyen açık sandviçleridir. Patates salatası tabanının üzerine bir sanatçı titizliğiyle yerleştirilen şarküteri ürünleri, turşu ve yumurta dilimleri; yerel şarküterilerin (Lahůdky) vitrinlerini süsleyen renkli birer mücevher gibidir.
- **Kulajda (Orman ve Çiftlik Buluşması)**: Dereotu, mantar ve kremanın muazzam birlikteliği. İçine saklanan bir adet poşe yumurta ile sunulan bu yoğun çorba, Bohemya ormanlarının o nemli ve taze kokusunu tabağınıza taşır. Ekşi ve kremsi dokusuyla damağınızda derin bir iz bırakır.
- **Becherovka (13. Şifalı Kaynak)**: Karlovy Vary’nin 20’den fazla gizli bitkiyle hazırlanan efsanevi likörü. Çekler için bu içecek, sindirimi kolaylaştıran bir "ilaç" hükmündedir. Yemek sonrası bir kadehte sunulan bu baharatlı ve keskin içecek, Prag lezzet turunuzun en şık kapanışıdır.

**💡 Lokal Tavsiyesi:** Meydanlardaki "Tourist Menu" yazan yerlerden kaçın. Ara sokaklarda, camları buğulu, içeriden kahkahaların ve kadeh seslerinin yükseldiği, tabelası bile olmayan kapılardan içeri dalın. En iyi Svíčková ve en taze Pilsner sizi her zaman o izbe görünümlü ama ruhu olan birahanelerde bekliyor olacak.

Yazısız Kurallar:
- **Sonsuz Bira Akışı**: Geleneksel bir birahanede (Hospoda) bardağınızı bitirdiğiniz an garson sormadan yenisini getirir. Eğer durmak istiyorsanız, bardak altlığını bardağın üzerine kapatmalısınız. Aksi takdirde sabaha kadar bira içmeye devam edebilirsiniz!
- **Hesap Çetelesi**: Masadaki küçük kağıt sizin tek belgenizdir. Her çizik bir birayı temsil eder. O kağıdı sakın kaybetmeyin veya karalamayın; hesap öderken garson o çizikleri sayacaktır.
- **Sadece Ekmek ve Simit**: Masada gördüğünüz sepet içindeki ekmekler veya büyük simitler (Pretzel) genellikle ücretsiz değildir. Yediğiniz her parça hesabınıza eklenir; istemiyorsanız dokunmamanız en iyisidir.
- **Ortak Masa Kültürü**: Popüler birahanelerde boş yer yoksa, bir masada oturanların yanına "Je tu volno?" (Burası boş mu?) diyerek oturmak çok doğaldır. Prag’da masayı paylaşmak sosyalleşmenin kuralıdır.
- **Bahşiş (Yuvarlama Usulü)**: Çekya’da bahşiş genellikle %10 olarak beklenir ancak bunu masaya bırakmak yerine, hesabı öderken miktarı yukarı yuvarlayarak garsona söylersiniz. (Örneğin hesap 182 Koruna ise, garsona "200" diyerek parayı uzatmak lokal bir davranıştır.)
- **Nakit (Hotovost)**: Prag’ın en iyi lokal birahanelerinin birçoğu hâlâ "Sadece Nakit" (Cash Only) çalışır. Cebinizde her zaman bir miktar Çek Korunası bulundurmak hayat kurtarır.

## 🤫 Şehrin Fısıldadıkları: Lokal Sırlar
Prag, sadece haritalarda işaretlenen kulelerden ibaret değildir; o, ana caddelerin arkasına gizlenmiş avlularda, isyankar heykellerde ve zamanın unutulduğu yeraltı laboratuvarlarında asıl şarkısını söyler. Eğer kalabalıkların uğultusundan sıyrılıp Prag’ın gerçek fısıltısını duymak isterseniz, rotanızı şu gizli duraklara çevirim:

- [Speculum Alchemiae](search:Speculum Alchemiae) (Simyacıların İzinde): Eski Şehir’in kalbinde, 2002 yılındaki büyük sel felaketinden sonra tesadüfen keşfedilen bu yeraltı laboratuvarı, Prag’ın "Büyücüler Şehri" olduğu günlerin en gerçek kanıtıdır. İmparator II. Rudolf’un gizli simyacılarının ölümsüzlük iksirini aradığı bu tozlu tüneller, sizi modern dünyadan koparıp kadim bir gizemin içine çeker.
- [Nový Svět](search:Nový Svět) (Yeni Dünya): Prag Kalesi’nin hemen dibinde ama bir o kadar da uzakta hissettiren bu mahalle, 17. yüzyıldan kalma minik evleriyle Prag’ın en mahrem sığınağıdır. Bir zamanlar simyacıların ve fakir sanatçıların yaşadığı bu sessiz sokaklarda, sadece kendi ayak seslerinizi duyarsınız.
- **Paternoster Asansörleri (Asla Durmayan Döngü)**: Şehirdeki bazı eski devlet binalarında ve Lucerna Pasajı'nda hâlâ çalışan bu "asla durmayan" ahşap asansörler, Prag’ın yaşayan tarihidir. Kapısı olmayan ve sürekli bir döngü halinde hareket eden bu kabinlere binmek, zamanın içinde bir döngüye girmek gibidir.
- **Lucerna Pasajı ve Ters At**: Aziz Wenceslas’ın ölü ve ters asılmış bir atın üzerinde durduğu bu heykel, David Černý’nin otoriteyle dalga geçen meşhur eseridir. Prag’ın o ciddi Gotik yüzüne atılmış kışkırtıcı bir kahkaha gibidir.
- **Vinárna Čertovka (Trafik Işıklı Daracık Sokak)**: Malá Strana’da iki bina arasına sıkışmış, o kadar dar bir geçit vardır ki iki kişinin aynı anda geçmesi imkânsızdır. Bu yüzden her iki ucuna yerleştirilen trafik ışıkları, Prag’ın mimari sürprizlerinin en eğlenceli örneğidir.
- **David Černý’nin Kışkırtıcı İzleri**: Sadece ters atla kalmayın; Kampa Parkı’ndaki yüzleri olmayan devasa Bronz Bebekler veya Kafka Müzesi önündeki interaktif heykeller, Prag’ın isyankar ruhunu okumanın en iyi yoludur.
- [Vrtba Bahçesi](search:Vrtba Bahçesi) (Vrtbovská zahrada): Sıradan bir kapının arkasında saklı bu Barok cennet, kat kat yükselen teraslarıyla Prag’ın o meşhur kırmızı çatılarını en romantik açıdan izleyebileceğiniz, şehrin en iyi korunan sırrıdır.
- **[Letná Parkı](search:Letná Parkı) ve Beş Köprü Manzarası**: Lokallerin gün batımını izlemek için toplandığı bu tepe, Vltava üzerindeki beş köprünün ([Charles Köprüsü](search:Charles Köprüsü) dahil) art arda dizildiği o ikonik kareyi yakalayabileceğiniz tek noktadır.
- **Strahov Manastırı ve St. Norbert Birası**: Kütüphanesinden çok, çevresindeki patikalarda yürümek ve keşişlerin yüzyıllardır aynı tarifle ürettiği özel birayı manastırın kendi avlusunda içmek gerçek bir Bohemya deneyimidir.
- **Belediye Kütüphanesi ve Sonsuzluk Kulesi (Idiom)**: Kütüphanenin girişinde yer alan binlerce kitaptan yapılmış "sonsuzluk tüneli", içindeki aynalar sayesinde size bilginin sonu olmadığını gösteren büyüleyici bir optik illüzyon sunar.

## ✅ Mutlaka Yapmadan Dönme: Prag Checklist
- **[Charles Köprüsü](search:Charles Köprüsü)'nde Güne Merhaba Deyin**: Kalabalıklar şehre doluşmadan hemen önce, şafak vaktinde köprüye gidin. Vltava üzerindeki pusun arasından yükselen Barok heykellerle baş başa kalmak, Prag’ın o mistik ruhuna dokunmanın tek yoludur.
- **Prag Kalesi’nde Gotik’in Zirvesine Çıkın**: Dünyanın en büyük kale kompleksinin avlularında kaybolun ve Aziz Vitus Katedrali'nin o göğe yükselen sivri kulelerine bakarken mimarinin gücünü hissedin.
- **Bir Birahanede "Sıvı Ekmek" Ritüeline Katılın**: Yerel bir birahaneye (Hospoda) girin ve masadaki o meşhur çeteleye ilk çiziğinizi attırın. Bardak altlığını bardağın üzerine kapatana kadar devam eden o sonsuz bira akışını deneyimlemeden Prag’ı anlamış sayılmazsınız.
- **Astronomik Saat’in Detaylarında Kaybolun**: Saat başı yapılan gösteriyi izlemek bir turist klasiğidir; ancak siz gösteriden ziyade saatin üzerindeki o karmaşık sembollerin, burçların ve zamanın felsefesinin tadını çıkarın.
- **Kafka’nın İzinde "Kafkaesk" Bir Yolculuk**: [Franz Kafka Müzesi](search:Franz Kafka Müzesi)’ni ziyaret edin ve hemen dışındaki devasa, dönen metal Kafka büstünün karşısında durun. Yazarı anlamak, Prag'ın o hüzünlü ve labirentvari sokaklarının neden onun eserlerine ilham verdiğini kavramaktır.
- **Vinárna Čertovka’da Yeşil Işığı Bekleyin**: Şehrin en dar sokağında, karşıdan gelenle sıkışıp kalmamak için trafik ışığının yeşil yanmasını bekleyin. Bu minik ve absürt an, Prag mimarisinin size sunduğu en eğlenceli sürprizlerden biridir.
- **Paternoster Asansörü ile Zaman Döngüsüne Girin**: Şehirdeki eski binalardan birinde, kapısı olmayan ve hiç durmadan dönen o ahşap kabinlere atlayın. Bu nostaljik "hiç bitmeyen döngü", Prag’ın yaşayan tarihinin en eğlenceli parçasıdır.
- **Svíčková ile Bohemya Mutfağının Şahikasına Ulaşın**: O yoğun kremalı sosun, yumuşacık sığır etinin ve yaban mersini reçelinin birleştiği o tabağı bitirmeden ve o sosu ekmek toplarıyla (dumplings) sıyırmadan Prag mutfağından geçtim demeyin.
- **David Černý’nin Kışkırtıcı İzini Sürün**: Şehrin dört bir yanına dağılmış o "tuhaf" heykelleri (Ters At, Bebekler, İşeyen Heykeller) bulun. Bu eserler, Prag’ın o ağırbaşlı Gotik yüzünün ardındaki isyankar Çek mizahının anahtarıdır.
- **Vltava Nehri’nde Prag’a Aşağıdan Bakın**: İster küçük bir feribotla karşıya geçin, ister bir deniz bisikleti kiralayıp nehrin ortasına açılın. Prag’ın siluetini suyun üzerinden izlemek, şehre bambaşka bir perspektif kazandırır.
- **[Vrtba Bahçesi](search:Vrtba Bahçesi)’nde Sessizliğin Tadını Çıkarın**: Malá Strana’nın gürültüsünden sadece bir kapı uzaklaşın ve o Barok teraslarda Prag’ın kırmızı çatılarına karşı derin bir nefes alın. Burası şehrin en güzel "gizli" seyir terasıdır.
- **[Letná Parkı](search:Letná Parkı)'nda Gün Batımı**: Lokaller gibi biranızı kapıp tepedeki banklara kurulun. Nehrin üzerindeki tüm köprülerin art arda dizildiği o meşhur kareyi hafızanıza kazıyın.
- **Trdelník Kokularını Takip Edin**: Her ne kadar lokaller "tam olarak bize ait değil" dese de, sokakları saran o tarçınlı ve şekerli kokuya teslim olun. Sıcak bir rulo tatlıyla Prag’ın dar sokaklarında kaybolmak, bu masalsı yolculuğun en tatlı finalidir.
"""

PRAG_EN = """# Prague: The City Time Refused to Touch

Quick Glance: Welcome to the heart of Europe, to the midst of Gothic spires and the misty atmosphere of history. There’s a reason Prague is called "The City of a Hundred Spires" or "The Golden City." Spreading across both banks of the Vltava River, the city boasts one of Europe’s best-preserved historic centers, having emerged from WWII almost unscathed. As you walk through streets where Gothic, Baroque, and Renaissance architecture intertwine, it's perfectly normal to feel like you're on a film set. Prague is not just about architecture; it's a character blended with the melancholy of Franz Kafka, the music of Mozart, and the world's finest beer culture.

A Friendly Note Before You Go: Although Prague is in the EU, it doesn’t use the Euro; the official currency is the Czech Koruna (CZK). Paying in Euros might result in significant exchange losses. Be cautious with street exchange offices as well; despite "no commission" signs, hidden fees are common. Fortunately, Prague is a very card-friendly city, so using reliable bank ATMs or simply paying by card is your most seamless and effortless option.

A Tasty Misconception: That famous Trdelník (chimney cake) you see on every corner is actually not an ancient Czech tradition; it's a "modern classic" that became popular in the early 2000s. For an authentic Prague experience, steer away from the crowds in front of the [Astronomical Clock](search:Astronomical Clock) and head to the local pubs in neighborhoods like Vinohrady or Letná. Also, remember: in Prague, beer competes with water; it is often cheaper and definitely the most beloved national beverage.

## 📅 Timing is Everything: Which Season is Yours?
Prague is a city that wears a different costume every season, changing its mood but never losing its charm. Since its character shifts entirely with the weather, it's time to decide whether you prefer lively crowds, a winter fairytale, or golden autumn leaves.

- **Spring (April - June)**: This is the city's awakening. As cherry blossoms bloom on Petřín Hill, Prague transforms into Europe’s most romantic destination. The weather is ideal for exploring (15-20°C), and the tourist crowds have yet to reach their peak.
- **Summer (July - August)**: The most vibrant but also the most exhausting time. Temperatures can push 30°C, and [Charles Bridge](search:Charles Köprüsü) becomes incredibly packed. If you love energy and endless summer evenings, this is the perfect time for you.
- **Autumn (September - October)**: The period when Prague truly earns its "Golden City" title. As the trees along the Vltava River turn shades of yellow and crimson, the city takes on a misty, melancholic atmosphere. It offers the best light for photography enthusiasts.
- **Winter (November - March)**: The weather is truly freezing, but the Christmas Markets in December turn the city into a real-life fairytale. January and February are the most economical months; tourist traffic thins out, accommodation prices drop, and Prague’s famous Gothic towers look enchanting under the snow.

## 🏠 Where to Stay: Neighborhood Guide
Choosing where to stay in Prague really depends on your answer to the question: "Do I want to feel like a tourist or a local?" The city is divided into districts (Prague 1, 2, 3...), and the lower the number, the closer you are to the heart of the city. Prague’s neighborhoods are more than just residential areas; each is a gateway to a different era. Your choice determines whether your morning view will be a Gothic spire or a modern art gallery.

- **Staré Město (Old Town - Prague 1)**: The heart of Prague and a favorite for first-timers. You’ll be neighbors with the [Astronomical Clock](search:Astronomical Clock) and [Old Town Square](search:Old Town Meydanı). Being within walking distance of everything is fantastic, but keep in mind that this is the busiest and most expensive area of the city.
- **Malá Strana (Lesser Town - Prague 1)**: Located on the other side of the Vltava, right beneath the Castle, this is the most romantic spot in Prague. With its Baroque buildings, narrow alleys, and embassies, this area is much quieter and more peaceful at night compared to the Old Town.
- **Nové Město (New Town - Prague 1/2)**: Although it's called "New," its history dates back to the 14th century. [Wenceslas Square](search:Wenceslas Meydanı (Václavské náměstí)) is located here. It is the hub of the transport network and the ideal spot for nightlife, shopping, and major hotels.
- **Vinohrady (Prague 2)**: If you want to "live like a local," this should be your destination. With its Art Nouveau buildings, chic cafes, international restaurants, and green parks, it’s the city’s most sophisticated district. It is only 10 minutes away from the center by tram.
- **Žižkov (Prague 3)**: The bohemian, edgy, and more budget-friendly side of the city. It is said to have one of the highest numbers of pubs per square meter in the world. It’s perfect for younger travelers who love nightlife and local beer culture.

## 🚲 Getting from A to B: Move Like a Local
While Prague is a city essentially designed for walking, its labyrinthine alleys and wide boulevards stretching along the Vltava River make it a true engineering masterpiece of transportation. Public transit here is so punctual that you can set your watch by the tram arrivals, allowing you to immerse yourself in the rhythm of the rails and the river with complete confidence.

- **First Steps**: Getting from Václav Havel Airport to the City Center Upon arriving in Prague, you will find that while there is no direct metro line from the airport, the public transport system fills this gap perfectly. The most economical and "local" method is to hop on Trolleybus 59 from Terminal 1 or 2. This line whisked you quickly to the Nádraží Veleslavín station on Metro Line A (Green), where standard city tickets are valid. For those seeking more comfort without transfers, the Airport Express (AE) bus runs directly to the main train station (Hlavní nádraží); however, this requires a special ticket purchased from the driver for approximately 100 CZK. For a more modern alternative, Prague’s official taxi service is integrated with Uber, providing safe journeys at fixed prices via the app.
- **Time Travel on Cobblestones**: Walkability Prague is a city that only truly reveals its soul to those who explore it on foot. Main hubs like the Old Town (Staré Město), the Jewish Quarter (Josefov), and Malá Strana are all within a few minutes' walk of each other. However, this fairytale stroll comes with a price: Prague’s famous, aesthetic, yet merciless cobblestones. When exploring the city, choosing shoes focused on "comfort" rather than "style" is the biggest detail that sets a local apart from a tourist. Don't forget to look up while walking; Prague’s true treasures are often hidden in the details of the attics and window sills.
- **Speed on Rails and Underground**: The Tram and Metro System Trams are the true arteries of the city, reflecting Prague’s unique character. Tram 22, in particular, acts more like the "cheapest city tour" than a mere transport vehicle, taking you from the riverbanks up the steep slopes of [Prague Castle](search:Prague Kalesi) with panoramic views. After midnight, the "Night Trams" (lines 90-99) take over, ensuring you reach any point in the city safely. If you are short on time, the metro system—comprising lines A, B, and C—is your best bet. Descending into the earth via massive escalators at stations like Náměstí Míru (one of the deepest in the world) offers a glimpse into the modern face of Prague.
- **Manage Your Budget and Route**: Tickets and the Visitor Pass Transportation in Prague is based on time rather than distance. This means your ticket allows for unlimited transfers (metro, tram, bus, funicular) within its validity period. A 30-minute ticket (30 CZK) is ideal for short hops, while the 90-minute ticket (40 CZK) is better for comprehensive journeys. If you plan to explore intensively for 2-3 days, the 24-hour (120 CZK) or 72-hour (330 CZK) passes offer great convenience. For the ultimate experience, the Prague Visitor Pass is your best ally. Similar to the Barcelona Card, it covers unlimited transport (including the airport) and provides free entry to over 60 top attractions like [Prague Castle](search:Prague Kalesi) and the [Astronomical Clock](search:Astronomical Clock) Tower.
- **Alternative Paths**: The River, the Hill, and the Pedals One of the most delightful ways to see the city is the Petřín Funicular, which climbs from Malá Strana to offer a bird’s-eye view of the spires. If you have a 24-hour or longer transport pass, this nostalgic journey is entirely free. To enjoy the Vltava River, you can use the small river ferries included in the public transport system for a quick cross-river water tour. While the city center can be risky for cycling due to pedestrian traffic and tram tracks, biking along the Náplavka riverbank using the Rekola (pink bikes) or Nextbike apps is a favorite weekend activity for locals.
- **Local Etiquette**: The Unwritten Rules of Transit The "honesty system" is fundamental to Prague’s transit; you won't find turnstiles at metro entrances. However, you must validate your ticket in the yellow machines upon boarding a tram or entering the metro area. Plainclothes inspectors frequently conduct checks, and having a ticket in your pocket that hasn't been validated will result in a heavy fine—no excuses accepted. To blend in, always stand on the right on escalators, leaving the left side open for locals in a hurry. The most critical rule? Trams always have absolute priority. Even at a pedestrian crossing, never expect a tram to stop for you. As the locals say, "The tram always wins!"

## 🏛️ The City's Memory: Iconic Landmarks Must-See
Every stone in Prague whispers the heritage of a thousand years and the grandeur of empires. It is a living, open-air stage where every step draws you into the mystical atmosphere of the Middle Ages, and where different layers of time seamlessly intertwine.

- [Prague Castle (Pražský hrad)](search:Prague Kalesi)): Recognized as the largest ancient castle complex in the world. Dominating the city’s skyline, this massive structure houses [St. Vitus Cathedral](search:St. Vitus Katedrali), the true pinnacle of Gothic architecture. Practical Note: Security and ticket queues can get quite long. To ensure a comfortable visit, it is highly recommended to purchase your tickets online in advance and arrive early in the morning.
- [Golden Lane (Zlatá ulička)](search:Golden Lane): Located within the castle complex, [Golden Lane](search:Golden Lane) transports you back to the 16th century with its vibrant, tiny houses. Once believed to be the home of alchemists, House No. 22 is famous as the sanctuary where Franz Kafka penned some of his most introspective works.
- [Charles Bridge (Karlův most)](search:Charles Köprüsü)): Adorned with 30 Baroque statues, [Charles Bridge](search:Charles Köprüsü) is one of Prague’s most powerful symbols spanning the Vltava River. Connecting the Old Town with Malá Strana, the bridge feels like an open-air art gallery. To experience its most serene state, aim for sunrise or sunset.
- [Lennon Wall (Lennonova zeď)](search:Lennon Wall): Situated just past [Charles Bridge](search:Charles Köprüsü), the [Lennon Wall](search:Lennon Wall) has become a global symbol of peace and freedom. Since the 1980s, this ever-changing canvas of graffiti has stood as a vibrant reflection of resistance and freedom of expression in Prague’s modern memory.
- [Old Town Square](search:Eski Şehir Meydanı) and the [Astronomical Clock (Orloj)](search:Astronomical Clock): Surrounded by Gothic and Baroque architecture, [Old Town Square](search:Old Town Meydanı) is one of Europe’s most breathtaking plazas. Its centerpiece, the [Astronomical Clock](search:Astronomical Clock), is the oldest working clock of its kind. While the brief hourly show is a popular attraction, the real reward lies in examining the clock’s intricate details and profound symbolism.
- [Klementinum Library (Klementinum)](search:Klementinum Kütüphanesi): Deserving of the title "the world’s most beautiful library," this Baroque masterpiece invites you into a mesmerizing silence among ancient manuscripts and massive globes. Important Tip: The Klementinum can only be visited via guided tours, and capacity is strictly limited. To avoid disappointment, make sure to book your reservation online several days in advance.
- [Municipal House (Obecní dům)](search:Belediye Binası): Rising next to the [Powder Tower](search:Powder Kulesi), this building is a magnificent representative of the Art Nouveau (Jugendstil) movement. With its grand mosaics, it remains the heart of the city’s artistic pulse.
- [Jewish Quarter (Josefov)](search:Yahudi Mahallesi): One of the best-preserved Jewish settlements in Europe, housing six synagogues and the historic [Old Jewish Cemetery](search:Old Jewish Cemetery). Pro Tip: If you plan to visit all the synagogues and the cemetery, a combined ticket is both more practical and economical. These can be purchased at local kiosks or online.
- [Dancing House (Tančící dům)](search:Dancing House): Prague is not defined solely by its medieval past. This modern architectural marvel on the riverbank creates a striking yet fascinating contrast within the city’s historical fabric.
- [Vyšehrad](search:Vyšehrad): For those looking to escape the crowds of [Prague Castle](search:Prague Kalesi), this fortress—regarded as the "birthplace of the city"—offers magnificent river views and tranquil parklands. It remains a favorite weekend retreat for locals.

## 🍴 A Taste of the City: Meat, Dough, and Beer
Prague’s cuisine is one of the finest reflections of that "comfort food" character at the heart of Central Europe. Here, every dish feels like an old friend welcoming you by the fireplace on a cold winter day.

- **Vepřo-knedlo-zelo (A National Pride)**: The unshakeable foundation of Prague’s culinary identity. It features slow-roasted, tender pork served alongside the famous knedlíky (bread dumplings) and caramelized sweet-and-sour sauerkraut (zelí). This trio is considered the "Holy Grail" of Czech cuisine; the richness of the meat finds a perfect balance in the acidity of the cabbage and the density of the dumplings.
- **Svíčková na smetaně (Imperial Elegance)**: The most sophisticated dish in the Czech repertoire. Beef sirloin is marinated for a full 24 hours with root vegetables and spices. The resulting thick, creamy vegetable sauce is finished with a spoonful of cranberry jam and a dollop of fresh whipped cream. It is rare to find another dish that blends sweet and savory with such noble grace.
- **Pilsner (Tekutý Chléb – "Liquid Bread")**: In Prague, beer is not just a beverage; it is life itself. To the locals, it is "liquid bread." In the land where the world’s first golden pilsner was born, beer is poured using specialized tap techniques. The Hladinka—a thick, wet, and velvety head of foam occupying a third of the glass—is the signature of freshness and craftsmanship.
- **Guláš (Czech Goulash)**: Distinct from its Hungarian cousin, the Czech version is darker, denser, and contains fewer vegetables. Braised over a slow flame with plenty of onions, cumin, and occasionally a splash of beer, this beef stew served with raw onion rings and fresh dumplings is the warmest sanctuary during a Prague winter.
- **Trdelník (The Cinnamon Soul of the Streets)**: The source of that enchanting cinnamon scent that greets you as you wander through Prague’s medieval alleys. Dough spirals are roasted over an open flame and dusted with sugar and walnuts to create a caramelized crust. Whether plain or filled with chocolate, this pastry is an inseparable part of Prague’s fairytale atmosphere.
- **Smažený Sýr (Golden Guilty Pleasure)**: The most beloved "snack" found in Prague’s pubs. A thick slice of Edam or Hermelín cheese is breaded and fried until the exterior is crispy and the interior is molten. Served with tartar sauce and boiled potatoes, it is proof of how delicious simplicity can be.
- **Nakládaný Hermelín (The Pub Classic)**: If you want to feel like a true local, this is the legendary appetizer you must try. Soft cheese is marinated in jars for days with oil, garlic, chili peppers, and spices. Served with fresh Czech bread, it is the most loyal companion to a cold beer.
- **Chlebíčky (A Visual Feast)**: These are open-faced sandwiches that keep pace with Prague’s fast life without sacrificing aesthetics. Toppings like potato salad, cured meats, pickles, and egg slices are arranged with artistic precision on small slices of bread; they look like colorful jewels decorating the windows of local delicatessens (Lahůdky).
- **Kulajda (Forest Meets Farm)**: A magnificent union of dill, mushrooms, and cream. Often served with a poached egg hidden inside, this dense soup brings the damp, fresh scent of Bohemian forests to your plate. Its sour and creamy texture leaves a deep impression on the palate.
- **Becherovka (The 13th Spring)**: A legendary herbal liqueur from Karlovy Vary, crafted with over 20 secret herbs. To the Czechs, this drink is practically a "medicine" that aids digestion. Served in a small glass after a meal, this spicy and sharp spirit is the most elegant way to conclude your Prague flavor tour.

**💡 Local Advice:** Avoid places with "Tourist Menu" signs in the main squares. Instead, dive into the side streets and look for the unmarked doors with steamed-up windows, where laughter and the clinking of glasses echo from within. The best Svíčková and the freshest Pilsner are always waiting for you in those dimly lit but soulful pubs.

Local Wisdom and Unwritten Rules: To eat like a local and avoid the "tourist traps," keep these insider rules in mind:
- **The Endless Flow**: In a traditional pub (Hospoda), the moment you finish your beer, the waiter will bring a fresh, frothy replacement without asking. If you want to stop the cycle, place your coaster on top of your glass. Otherwise, the beer will keep coming until dawn!
- **The Tally Slip**: The small slip of paper on your table is your only official document. Every stroke represents one beer. Do not lose or scribble on that paper; the waiter will count those marks to calculate your bill.
- **The Bread and Pretzel Trap**: The baskets of bread or large pretzels you see on the table are usually not free. Every piece you eat will be added to your tab; if you don't want them, it’s best not to touch them.
- **Shared Table Culture**: In popular pubs, if there are no empty tables, it is perfectly normal to ask those already seated, "Je tu volno?" (Is this spot free?). Sharing a table is a social rule in Prague.
- **Tipping (The Round-Up)**: A 10% tip is generally expected in Czechia. However, rather than leaving it on the table, you tell the waiter the total amount you want to pay as you hand over the money. (e.g., if the bill is 182 Koruna, saying "200" to the waiter is the local way to tip).
- **Cash (Hotovost)**: Many of Prague’s best local pubs still operate on a "Cash Only" basis. Keeping a supply of Czech Koruna in your pocket is a lifesaver.

## 🤫 Whispers of the City: Local Secrets
Prague is more than the towers marked on a map; its true song is sung in courtyards tucked behind main streets, through rebellious sculptures, and within underground laboratories where time has been forgotten. If you wish to escape the hum of the crowds and hear the city’s genuine whisper, turn your path toward these ten hidden stops:

- [Speculum Alchemiae](search:Speculum Alchemiae) (In the Footsteps of Alchemists): Located in the heart of the Old Town, this underground laboratory was discovered by chance following the Great Flood of 2002. It serves as the most authentic proof of Prague’s days as the "City of Mages." These dusty tunnels, where Emperor Rudolf II’s secret alchemists once sought the elixir of immortality, pull you away from the modern world and into an ancient mystery.
- [Nový Svět](search:Nový Svět) (The [New World](search:Nový Svět)): Nestled right at the foot of [Prague Castle](search:Prague Kalesi) yet feeling worlds away, this neighborhood is the city’s most intimate sanctuary. With its tiny houses dating back to the 17th century, it was once a refuge for poor artists and alchemists. Today, in these quiet, cobblestone streets, the only sound you’ll hear is your own footsteps.
- **Paternoster Elevators (The Never-Ending Loop)**: Still operating in some of the city's older government buildings and the Lucerna Palace, these "doorless" wooden elevators are a piece of living history. Stepping into these cabins, which move in a continuous, rhythmic cycle, feels like entering a loop within time itself.
- **[Lucerna Passage](search:Lucerna Passage) and the Upside-Down Horse**: This sculpture of St. Wenceslas sitting atop a dead, inverted horse is David Černý’s famous mockery of authority. It stands as a provocative laugh directed at Prague’s solemn Gothic facade.
- **Vinárna Čertovka (The [Narrowest Street](search:Vinarna Certovka (Narrowest Sokağı)) with a Traffic Light)**: Tucked between two buildings in Malá Strana is a passage so narrow that it is impossible for İwo people to pass at once. Because of this, traffic lights have been placed at both ends—making it perhaps the most amusing example of Prague’s architectural quirks.
- **The Provocative Traces of David Černý**: Don’t stop at the upside-down horse; seek out the faceless, giant Bronze Babies in Kampa Park or the interactive sculptures in front of the Kafka Museum. Following Černý’s trail is the best way to decode the rebellious soul of Prague.
- [Vrtba Garden](search:Vrtba Bahçesi) (Vrtbovská zahrada): Hidden behind an ordinary door, this Baroque paradise rises in terraced layers, offering the most romantic views of Prague’s iconic red rooftops. It remains the city’s best-kept secret.
- **[Letná Park](search:Letná Parkı) and the Five-Bridge View**: While tourists flock to [Charles Bridge](search:Charles Köprüsü), locals gather on this hill to watch the sunset. This is the only spot where you can capture the iconic frame of five bridges—including [Charles Bridge](search:Charles Köprüsü)—aligned perfectly along the Vltava.
- **Strahov Monastery and St. Norbert Beer**: Far beyond its world-famous library, the true Bohemian experience lies in walking the surrounding trails and tasting the craft beer brewed by monks using the same recipe for centuries, served in the monastery’s own courtyard.
- **The Municipal Library and the Infinity Tower (Idiom)**: Located at the entrance of the library, this "tunnel of infinity" made from thousands of books uses mirrors to create a mesmerizing optical illusion, reminding every visitor that there is truly no end to knowledge.

## ✅ The Prague Checklist: Don't Leave Without Doing These
- **Greet the Dawn on [Charles Bridge](search:Charles Köprüsü)**: Visit before the crowds descend, right at daybreak. Watching the Baroque statues emerge from the Vltava mist is the only way to touch the city's mystical soul.
- **Ascend the Heights of Gothic at [Prague Castle](search:Prague Kalesi)**: Wander the courtyards of the world’s largest castle complex and feel the sheer power of architecture while gazing at the soaring spires of [St. Vitus Cathedral](search:St. Vitus Katedrali).
- **Join the "Liquid Bread" Ritual in a Pub**: Step into a traditional hospoda and get that first stroke on your tally slip. You haven't truly understood Prague until you've experienced the endless flow of beer that only stops when you place your coaster on top of your glass.
- **Lose Yourself in the Details of the [Astronomical Clock](search:Astronomical Clock)**: While the hourly show is a tourist classic, you should look deeper. Savor the intricate symbols, the zodiac signs, and the profound philosophy of time etched into its legendary face.
- **A "Kafkaesque" Journey in the Footsteps of Kafka**: Visit the [Franz Kafka Museum](search:Franz Kafka Müzesi) and stand before the giant, rotating metal bust of the author. Understanding Kafka is the key to comprehending why Prague’s melancholic and maze-like streets inspired his genius.
- **Wait for the Green Light at Vinárna Čertovka**: In the city’s narrowest street, don't forget to wait for the traffic light to turn green so you don't get stuck. This tiny, absurd moment is one of the most charming architectural surprises Prague offers.
- **Enter a Time Loop with the Paternoster Elevator**: Find one of these doorless, wooden, never-stopping elevators in an old government building. This nostalgic "never-ending loop" is a whimsical piece of Prague’s living history.
- **Reach the Pinnacle of Bohemian Cuisine with Svíčková**: You cannot say you’ve tasted Prague until you’ve finished that plate of rich cream sauce, tender beef, and cranberry jam—mopping up every last drop with your bread dumplings.
- **Trace the Provocative Trail of David Černý**: Seek out the "weird" sculptures scattered across the city (the Upside-Down Horse, the Babies, the Pissing Statues). These works are the key to the rebellious Czech wit hidden behind Prague’s solemn Gothic facade.
- **Look at Prague from Below on the Vltava River**: Whether by a small ferry or a rented pedal boat, viewing the city’s skyline from the water offers a serene and romantic perspective that you simply cannot get on land.
- **Find Peace in the [Vrtba Garden](search:Vrtba Bahçesi)**: Escape the hustle of Malá Strana through a hidden door into this Baroque paradise. Climb its terraces for a deep breath and the most enchanting view of Prague’s iconic red-tiled roofs.
- **Sunset at [Letná Park](search:Letná Parkı)**: Join the locals with a drink in hand on the hills of Letná. Capture the iconic frame of five bridges—including [Charles Bridge](search:Charles Köprüsü)—aligned perfectly along the Vltava as the sun dips below the horizon.
- **Follow the Scent of Trdelník**: Even if locals say it’s not "entirely" Czech, surrender to the cinnamon and sugar aroma wafting through the medieval alleys. Getting lost in the cobblestone streets with a warm pastry is the quintessential fairytale ending to your journey.
"""

def main():
    print(f"Reading CSV from {CSV_PATH}...")
    
    new_features_tr = ""
    new_features_en = ""
    
    try:
        if not os.path.exists(CSV_PATH):
             print(f"Error: CSV file not found at {CSV_PATH}")
             return

        with open(CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            venues = list(reader)
            
            for venue in venues:
                name = venue.get('name', '').strip()
                desc_tr = venue.get('description_tr', '').strip()
                desc_en = venue.get('description_en', '').strip()
                tips_tr = venue.get('tips_tr', '').strip()
                tips_en = venue.get('tips_en', '').strip()
                
                # TR Format
                new_features_tr += f"- **{name}**: {desc_tr}"
                if tips_tr:
                    new_features_tr += f" _İpucu: {tips_tr}_"
                new_features_tr += "\n"
                
                # EN Format
                new_features_en += f"- **{name}**: {desc_en}"
                if tips_en:
                    new_features_en += f" _Tip: {tips_en}_"
                new_features_en += "\n"
                
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Create structured JSON for AIService
    output_data = {
        "tr": {
            "intro": PRAG_TR,
            "recommendations": new_features_tr,
            "tip": ""
        },
        "en": {
            "intro": PRAG_EN,
            "recommendations": new_features_en,
            "tip": ""
        }
    }
    
    # Ensure directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Write JSON
    print(f"Writing JSON to {OUTPUT_FILE}...")
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        print("✅ Successfully generated Prague Guide JSON.")
    except Exception as e:
        print(f"Error writing JSON: {e}")

if __name__ == "__main__":
    main()
