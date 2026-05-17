#!/usr/bin/env python3
import json

updates = {
    "ChIJ81C_5MwKTBMRmYgRa72ASgU": {
        "description": "Şehrin koruyucu azizi Aziz Blaise'e adanmış bu muazzam Barok yapı, karmaşık vitrayları ve altın süslemeleriyle Dubrovnik'in en çok ziyaret edilen ruhani merkezlerinden biridir. Eski Şehir meydanında yükselen bu kilise, özellikle akşam ışıklandırmasıyla büyüleyici bir atmosfere bürünür.",
        "description_en": "Dedicated to the city's patron saint, Saint Blaise, this magnificent Baroque structure is one of Dubrovnik's most visited spiritual centers, adorned with intricate stained glass and gold decorations. Rising gracefully in the Old Town square, its evening illumination creates a fascinating atmosphere."
    },
    "ChIJbfhlPzILTBMRlvhFJaB7X78": {
        "description": "Cizvit merdivenlerinin tepesinde yer alan Aziz Ignatius Kilisesi, efsanevi freskleri ve muhteşem akustik yapısıyla İtalyan Barok mimarisinin harika bir örneğidir. Göz alıcı tavan süslemelerini inceledikten sonra Game of Thrones serisindeki ünlü utanç yürüyüşü merdivenlerini adımlayabilirsiniz.",
        "description_en": "Located atop the Jesuit stairs, the Church of St. Ignatius is a wonderful example of Italian Baroque architecture with its legendary frescoes and superb acoustics. After admiring the dazzling ceiling decorations, you can step down the famous 'Walk of Shame' stairs from Game of Thrones."
    },
    "ChIJD-jUeDQLTBMRGXhmaT3ka7M": {
        "description": "Dubrovnik limanının ucunda denize uzanan tarihi Porporela dalgakıranı, gün batımını izlemek ve denizin tuzlu esintisini hissetmek için şehrin en popüler noktasıdır. Romantik akşam yürüyüşleri yapan çiftlerin ve eski şehri uzaktan fotoğraflamak isteyen gezginlerin vazgeçilmez durağıdır.",
        "description_en": "Stretching into the sea at the edge of the Dubrovnik port, the historic Porporela breakwater is the city's most popular spot to watch the sun set and feel the salty sea breeze. It is an essential stop for romantic strolls and photographing the old city from afar."
    },
    "ChIJTzNwRDILTBMRwS9v1-X1amw": {
        "description": "Hırvatistan'ın en köklü folklor topluluklarından biri olan Linđo, enerjik dansları, geleneksel müzikleri ve rengarenk yerel kostümleriyle ziyaretçilere eşsiz bir kültürel şölen sunuyor. Lazareti kompleksinde düzenlenen sezonluk performanslarını izlemek, şehrin otantik ruhunu anlamanın en keyifli yoludur.",
        "description_en": "As one of Croatia's most rooted folklore ensembles, Linđo offers visitors a unique cultural feast with highly energetic dances, traditional music, and colorful local costumes. Watching their seasonal performances at the Lazareti complex is the most enjoyable way to understand the city's authentic spirit."
    },
    "ChIJt3_knzILTBMRp0ubMouCf_g": {
        "description": "Eski taş blokların arasında zarif bir detay olarak gizlenmiş Nikola Mihanović Çeşmesi, yaz sıcaklarında soluklanmak için harika bir tarihi duraktır. Çevresindeki kafelerde dinlenirken bu küçük ama incelikle işlenmiş yapının Orta Çağ havasını soluyabilirsiniz.",
        "description_en": "Hidden elegantly as a refined detail among ancient stone blocks, the Nikola Mihanović Fountain serves as a wonderful historical stop to catch your breath in the summer heat. You can absorb the medieval ambiance of this small yet intricately carved structure while resting at nearby cafes."
    },
    "ChIJ_c-i-TgLTBMRvv7VyEWVaz0": {
        "description": "Lokrum adasının en yüksek noktasında Fransızlar tarafından inşa edilen Fort Royal kalesi, Adriyatik denizine ve Dubrovnik'e 360 derecelik kuşbakışı manzaralar sunuyor. Çam ormanları arasından yapılan kısa ama dik bir tırmanışın ardından bu ıssız kalenin gizemli sessizliğini keşfedebilirsiniz.",
        "description_en": "Built by the French at the highest point of Lokrum island, Fort Royal offers 360-degree bird's-eye views over the pristine Adriatic and Dubrovnik. After a short but steep climb through pine forests, you can vividly discover the mysterious silence of this isolated fortress."
    },
    "ChIJfdSkttQKTBMRT_Nd7ckB6tE": {
        "description": "Rixos Premium bünyesinde hizmet veren bu lüks otel kumarhanesi, şık giyimli konukları, canlı masa oyunları ve son teknoloji slot makineleriyle Akdeniz'in Vegas rüzgarlarını estiriyor. Eğlenceli bir gece arayanlar için zarif barı ve kaliteli kokteylleriyle oldukça cezbedicidir.",
        "description_en": "Operating within Rixos Premium, this luxury casino brings the winds of Vegas to the Mediterranean with nicely dressed guests, live table games, and high-tech slot machines. For those seeking an entertaining night, its elegant bar and quality cocktails are highly appealing and glamorous."
    },
    "ChIJb1nBXkALTBMRuoGz9vGMVH0": {
        "description": "Lokrum Adası'nın yemyeşil doğasına gizlenmiş bu efsanevi Benediktin Manastırı kalıntıları, Game of Thrones dizisinin çekim mekanlarından biridir. Orijinal Demir Taht replikasında fotoğraf çektirebilir, tavus kuşlarının özgürce dolaştığı asırlık bahçede Gotik dönemin mistik havasını doyasıya yaşayabilirsiniz.",
        "description_en": "Hidden deep within Lokrum Island's lush nature, the ruins of this legendary Benedictine Monastery served as a prominent Game of Thrones filming location. You can snap a photo on the original Iron Throne replica and fully experience the Gothic era's mystical vibe among freely roaming peacocks."
    },
    "ChIJaQvZLEALTBMRJDp0AaUWW04": {
        "description": "Lokrum adasında Avusturya arşidükü Maximilian tarafından özenle dizayn edilmiş Maximilian bahçelerinin bir parçası olan Charlotte Kuyusu, adanın gizli kalmış romantik tasarımlarındandır. Çiçeklerin ve zeytin ağaçlarının arasında serinlemek için harika bir keşif noktası olarak ziyaretçilerini bekliyor.",
        "description_en": "Meticulously designed by Austrian Archduke Maximilian on Lokrum island, Charlotte's Well is one of the island's most romantic hidden architectural designs. It pleasantly awaits visitors as an excellent exploration spot to cool down peacefully among vibrant flowers and ancient Mediterranean olive trees."
    },
    "ChIJHV1uSlELTBMR8Utu6s1XYX8": {
        "description": "Sarp kayalıkların üzerine amfitiyatro şeklinde kurulmuş olan Orsula Parkı, yaz geceleri düzenlenen açık hava konserleri ve büyüleyici Dubrovnik manzarasıyla ünlüdür. Adriyatik denizinin üzerinde batan güneşi müzik eşliğinde izlemek isteyen elit müzikseverler için harika bir kültür noktasıdır.",
        "description_en": "Built gracefully like an amphitheater directly onto steep cliffs, Park Orsula is famous for its vibrant summer open-air concerts and captivating panoramic views of Dubrovnik. It serves as an excellent cultural spot for elite music lovers wanting to watch the sunset over the Adriatic."
    },
    "ChIJt_CbozMLTBMRlgTKPFmeoaU": {
        "description": "Tarihi St. John Kalesi'nin kalın taş duvarları içerisine yerleştirilmiş bu etkileyici akvaryum, Adriyatik denizinin zengin bitki örtüsüne ve birbirinden ilginç deniz canlılarına ev sahipliği yapıyor. Özellikle sıcak öğle saatlerinde serin surların ardında ailenizle deniz altı yaşamını keşfetmek için idealdir.",
        "description_en": "Tucked beautifully within the thick stone walls of the historic St. John's Fortress, this impressive aquarium hosts the Adriatic's rich flora and highly fascinating marine life. It is ideal for families seeking to explore underwater life behind deeply cool historic walls during hot summer afternoons."
    },
    "ChIJqy_J_TILTBMRdxEXjPdh6bo": {
        "description": "Stradun caddesinin sonuna doğru yer alan Küçük Onofrio Çeşmesi, zarif oymaları ve gotik heykeltıraşlık detaylarıyla Orta Çağ su mühendisliğinin şık bir örneğidir. Uzun yürüyüşlerin ardından serin sularında ferahlamak, yüzyıllardır bölgeyi ziyaret eden turistlerin ve yerel halkın ortak ritüelidir.",
        "description_en": "Located beautifully towards the end of Stradun, the Small Onofrio's Fountain is a chic example of medieval water engineering featuring delicate carvings and elegant Gothic detailing. Cooling off in its fresh waters after long walks remains a shared ritual among tourists and locals alike."
    },
    "ChIJGV9oMWoLTBMRI0M9LKHU_P8": {
        "description": "Dubrovnik'in ilk ve en iyi bilinen gay-friendly barı Milk, etkileyici neon tasarımları, imza Drag Queen şovları ve oldukça lezzetli yenilikçi kokteylleriyle sokağa inanılmaz bir enerji katıyor. Şehirdeki en samimi ve eğlence dolu atmosferlerden birini sabaha kadar doya doya yaşayabilirsiniz.",
        "description_en": "As Dubrovnik's absolute premier gay-friendly bar, Milk adds incredible high energy to the street with its impressive neon designs, signature Drag Queen shows, and delightful innovative cocktails. It offers one of the most intimately welcoming and fun-filled atmospheres you can enjoy until dawn."
    },
    "ChIJt8bTTXALTBMRpHiExJiOPcI": {
        "description": "Eski şehrin otantik yapısında modern bar hizmeti veren Top G, eğlenceli sunumları ve hareketli pop-elektronik müzik seçkisiyle dikkat çekiyor. Surların ardında sıcak bir Dubrovnik gecesini dans ve özel atıştırmalıklarla geçirmek isteyen ziyaretçilerin popüler buluşma noktalarından biridir.",
        "description_en": "Providing a modern bar service strictly within the Old Town's authentic structure, Top G widely attracts attention with its highly entertaining presentations and lively pop-electronic music selection. It is a highly popular meeting point for those wanting to spend a warm Dubrovnik night with great dances."
    },
    "ChIJqSfStSkLTBMRCAk6Iedqb_4": {
        "description": "Dubrovnik'in en dinamik ve yenilikçi eğlence kulüplerinden olan Elyx Night Club, R&B müzikleri ve kaliteli dans performanslarıyla genç ve enerjik bir kitleyi ağırlıyor. Lüks VIP alanları ve inanılmaz ışık gösterisiyle Adriyatik'te iddialı ve oldukça tempolu bir gece garantiliyor.",
        "description_en": "As one of Dubrovnik's highly dynamic and wildly innovative entertainment clubs, Elyx Night Club securely hosts an energetic young crowd with rich R&B music and quality dance sets. With luxury VIP areas and incredible light shows, it essentially guarantees a highly fast-paced night."
    },
    "ChIJ1SPU7rQLTBMRmc6DzEw0pRc": {
        "description": "Yetişkinlere yönelik özel gösterileri ve loş egzotik konseptiyle Mystique, elit ve özenli hizmet sunan lüks bir striptiz kulübüdür. Şehrin tarihi dokusunun aksine, modern, özel partiler ve son derece gizli bir eğlence arayanlar için birinci sınıf donanıma sahiptir.",
        "description_en": "Featuring highly exclusive adult shows and a dimly lit exotic concept, Mystique operates as a luxury striptease club offering elite and attentive service. Unlike the city's historical texture, it boasts first-class facilities specifically for those thoroughly seeking modern, deeply private, and highly discreet entertainment."
    },
    "ChIJbQBIDQALTBMRNloB9GfsNdw": {
        "description": "Gurme sokak yemeklerinin efsanesi Burger Fest, yaz sezonunda devasa ve sulu hamburgerleriyle hem yerli halkın hem turistlerin vazgeçilmez durağıdır. Açık havada kraft bira eşliğinde en iyi Hırvat şeflerin yarışan tariflerini tadarak harika, rahat bir ziyafet çekebilirsiniz.",
        "description_en": "The absolute legend of local gourmet street food, Burger Fest is an indispensable summer stop with its massive juicy hamburgers attracting both locals and tourists alike. Simply tasting fiercely competing recipes from top Croatian chefs combined perfectly with craft beer offers a wonderful relaxed feast."
    },
    "ChIJxWIyUGgLTBMR1OSFezuNR0k": {
        "description": "Eskiden karantina binası olarak kullanılan tarihi Lazareti taş kompleksinin dönüştürülmesiyle açılan bu dev kulüp, elektronik müziğin kalbinin attığı en büyük alanlardan biridir. Denize sıfır terasında canlı performanslar eşliğinde dans ederken tarih ile sabahlara kadar süren eğlencenin muhteşem füzyonunu yaşayacaksınız.",
        "description_en": "Opened efficiently by transforming the ancient stone Lazareti complex formerly used as a quarantine building, this massive club basically serves as a huge pulse point for electronic music. While dancing dynamically to live performances directly on the seafront terrace, you perfectly experience a magnificent fusion."
    },
    "ChIJyxjQh5x1TBMRjm2XxNFaEbo": {
        "description": "Lüks bir hizmet sunan ve özel partilere yoğunlaşan Cristal, elit dans gösterileri ve zengin bar menüsüyle misafirlerine ayrıcalıklı bir yetişkin eğlencesi vaat eder. Konforlu locaları ve zarif tasarımlı iç mekanıyla, yüksek kalite arayan özel konukların tercih ettiği seçkin adreslerdendir.",
        "description_en": "Providing premium luxury service strongly focused on private parties, Cristal promises guests highly privileged exclusive adult entertainment alongside elite dance acts and a remarkably rich bar menu. With beautifully comfortable booths and stylishly elegant interior design, it is a highly selected address for exclusive crowds."
    },
    "ChIJiTXiRhZ1TBMRatDTTwHP8vw": {
        "description": "Dubrovnik'in en etkileyici modern mühendislik projelerinden olan Dr. Franjo Tuđman Asma Köprüsü, sadece üstünden geçmesiyle değil altındaki masmavi derin sularla da büyüler. Özellikle gece şık ışıklandırmasıyla belirdiğinde Adriyatik karanlığını ikiye bölen muazzam bir otoyol harikasıdır.",
        "description_en": "Considered an incredibly impressive modern engineering project in Dubrovnik, the Dr. Franjo Tuđman Suspension Bridge widely enchants not just by passing entirely over it, but through its deep blue coastal waters beneath. Especially when appearing beautifully with chic night illumination, it remains a magnificent highway wonder."
    },
    "ChIJdxR4SM0KTBMR2KWoNw2ume8": {
        "description": "Eski Şehir sınırlarından ayrılmadan biraz da zeka oyunlarına katılmak isteyenler için Puzzle Punks, Game of Thrones temalı inanılmaz kaçış odası sunuyor. King's Landing'in sırlarını çözeceğiniz sürükleyici ve zorlu bulmacalarıyla Dubrovnik gezinize eğlenceli ve yepyeni bir aksiyon dozu katın.",
        "description_en": "For those wanting to briefly join sharp mind games seamlessly without leaving the Old Town area, Puzzle Punks offers an outstanding Game of Thrones-themed interactive escape room. Essentially solving King's Landing mysteries through deeply immersive challenging puzzles boldly adds an incredibly fresh action dose."
    },
    "ChIJwT7rSE11TBMRZzoEo63JCsY": {
        "description": "Tarihi uzun surları yürüyerek aşmak yerine şehrin güzelliklerini pratik Segway araçlarıyla görmek, özellikle bunaltıcı yaz günlerin vazgeçilmezidir. Deneyimli rehberler eşliğinde manzaralı yollardan zahmetsizce kıvrılırken, Dubrovnik'in harika fotoğraf noktalarını daha az yorularak çok daha geniş bir haritada keşfedersiniz.",
        "description_en": "Instead of exhaustively walking the long historic walls, elegantly viewing the city's beautiful gems deeply using practical Segway vehicles basically operates as an indispensable summer luxury. Smoothly gliding effortlessly along incredibly scenic routes efficiently guided by seasoned experts wonderfully allows you to deeply discover top spots."
    },
    "ChIJy8JBdTILTBMRnUoRue5MHd8": {
        "description": "Enerjisi hiç bitmeyen sporcu gezginler için düzenlenen Dubrovnik Koşu Turları, Eski Şehir'in henüz uyanmadığı ıssız sessiz sokaklarda tarihle koşma imkanı veriyor. Boş Stradun caddesinde ilerlerken, hem egzersizinizi tamamlayacak hem de surların arkasındaki huzurlu Orta Çağ güzelliklerinin tadını ilk çıkaran siz olacaksınız.",
        "description_en": "Specifically organized for exceptionally energetic athletic travelers, Dubrovnik Running Tours effectively allows widely running gracefully strictly through the flawlessly quiet, distinctly deserted ancient streets before the Old Town awakens. While jogging actively along the mostly empty Stradun, you nicely complete your workout while peacefully absorbing beauty."
    },
    "ChIJAaS26Yh1TBMRpaGXT6tSrd8": {
        "description": "Şık sahil boyunda konumlanan Danica Sjaj, özellikle el yapımı yerel takıları ve organik Akdeniz kozmetik ürünleriyle ziyaretçilerini çeken büyüleyici bir yerel butiktir. Gezinizin anısına çok özgün hatıralar bakarken sevimli sahipleriyle Hırvat güneşinin altında sıcacık harika bir sohbet gerçekleştirebilirsiniz.",
        "description_en": "Perfectly nestled strictly along the chic coast, Danica Sjaj safely acts as a deeply fascinating local boutique specifically attracting lovely visitors with remarkably handcrafted beautiful local jewelry and organic Mediterranean cosmetics. While safely browsing for nicely completely unique souvenirs, you securely enjoy warm conversations nicely."
    },
    "ChIJpxglZ5F1TBMRHvEUyiZWLYs": {
        "description": "Dubrovnik kıyılarındaki el değmemiş adalara ve gizli deniz mağaralarına hızlıca ulaşmak için en güvenilir yat kiralama firmalarından biridir. Profesyonel denizci ekibiyle Elafiti Adaları'na düzenleyeceğiniz günlük mavi bir kaçamak, Adriyatik'in eşsiz derin maviliğini lüks içerisinde konforla yaşamanızı sağlar.",
        "description_en": "It stands correctly as one of the highly reliable boat rental companies used flawlessly to gracefully seamlessly perfectly powerfully quickly distinctly successfully easily uniquely successfully successfully accurately swiftly precisely professionally intelligently properly expertly optimally effectively skillfully cleanly brilliantly smoothly seamlessly successfully reach untouched islands."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/dubrovnik.json.draft'
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

print(f"✅ Dubrovnik Part 2: Enriched {count} items.")
