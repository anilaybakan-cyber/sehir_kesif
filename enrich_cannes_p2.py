#!/usr/bin/env python3
import json

updates = {
    "cann_la_villa_archange": {
        "description": "Gizli bir taş avluda iki Michelin yıldızlı şef önderliğinde hizmet veren La Villa Archange, adeta büyüleyici bir orman evini andıran huzurlu yapısıyla dikkat çekiyor. Yöresel malzemeleri sanat eserine dönüştüren zarif tarifleri ve doğayla iç içe samimi atmosferi, rafine damaklar için kusursuz bir gastronomi deneyimi sunuyor.",
        "description_en": "Set in a hidden stone courtyard led by a two-Michelin-starred chef, La Villa Archange stands out with its peaceful atmosphere reminiscent of a charming forest house. Transforming regional ingredients into pure art, its delicate recipes and deeply intimate natural setting offer a flawless gastronomic experience for refined tastes."
    },
    "cann_table_22": {
        "description": "Eski limanın hemen arkasına gizlenmiş bu şık ve samimi restoran, ünlü bir Fransız şefin elinden çıkan yenilikçi, taze ve heyecan verici brasserie lezzetleriyle tanınıyor. Cannes ruhuna uygun klasik lezzetlerin çağdaş yöntemlerle harmanlandığı sıcak ortamında, kendinizi ayrıcalıklı ama çok rahat hissedeceğiniz akşam yemekleri sizi bekliyor.",
        "description_en": "Hidden just behind the old port, this chic and intimate restaurant is renowned for bringing innovative, fresh, and exciting brasserie flavors crafted by a famous French chef. In a warm setting where classic Cannes flavors meet contemporary methods, exclusive yet deeply comfortable dinners perfectly await your arrival."
    },
    "cann_astoux_et_brun": {
        "description": "Deniz mahsulleri dendiğinde Cannes'da akla ilk gelen tarihî mekanlardan olan Astoux et Brun, özellikle taze istiridye tabakları ve devasa karides tepsileriyle meşhur bir adrestir. Yıllardır koruduğu yüksek kalite standartları ve her daim cıvıl cıvıl atmosferiyle tam bir Akdeniz deniz ürünleri şöleni sunuyor.",
        "description_en": "As a historical local institution when it comes to seafood in Cannes, Astoux et Brun is a famous address especially legendary for its fresh oyster platters and massive shrimp trays. Promising consistently high quality and an always vibrant atmosphere, it delivers a spectacular and authentic Mediterranean seafood feast."
    },
    "cann_la_petite_maison_cannes": {
        "description": "Yerel pazarlardan günlük olarak seçilen taze ürünlerle hazırlanan zengin menüsü, meşhur trüflü lezzetleri ve Akdeniz samimiyeti sunan canlı ortamıyla ünlü La Petite Maison, misafirlerine evindeymiş gibi hissettiriyor. Provençal misafirperverliğin lüks ile harmanlandığı bu sıcak mekânda her akşam adeta bir kutlama havasında geçer.",
        "description_en": "Famous for its rich seasonal menu crafted from fresh goods daily selected from local markets, legendary truffle delicacies, and lively Mediterranean sincerity, La Petite Maison makes guests feel right at home. In this warm venue fusing Provençal hospitality with luxury, every evening gracefully feels like an intimate celebration."
    },
    "cann_le_fouquet_s": {
        "description": "Efsanevi Majestic Barrière oteli bünyesinde yer alan şık Fransız brasserie efsanesi Le Fouquet's, zamansız Paris tarzını Akdeniz kenarına muazzam bir zarafetle taşıyor. Kırmızı tenteleri ve klasik ahşap sandalyeleriyle misafirlerini karşılarken, gurme Fransız spesiyalitelerinden oluşan kaliteli menüsüyle eşsiz bir mutfak geleneğini sürdürüyor.",
        "description_en": "Located inside the legendary Majestic Barrière hotel, the stylish French brasserie legend Le Fouquet's elegantly transports timeless Parisian charm right to the Mediterranean shore. Welcoming guests with its iconic red awnings, pristine wooden chairs, and gourmet French specialties, it flawlessly sustains a truly unique culinary tradition."
    },
    "cann_baoli_cannes": {
        "description": "Gösterişli ve egzotik bitkilerle çevrili görkemli bir avluda yer alan Baoli, muhteşem Asya füzyon mutfağını gece ilerledikçe şehrin en lüks ve prestijli kulübüne dönüştürüyor. Lüks arabaların dizildiği girişinden başlayarak sabahın ilk ışıklarına kadar süren dünyaca ünlü partileriyle şöhretini sonuna kadar hak ediyor.",
        "description_en": "Set in a magnificent courtyard surrounded by flashy exotic plants, Baoli masterfully transforms its superb Asian fusion dining into the city's most luxurious and prestigious vibrant night club. From its supercar-lined entrance right to the world-famous parties lasting till dawn, it perfectly justifies its incredible international fame."
    },
    "cann_l_affable": {
        "description": "Ara sokakta sessiz sedasız parlayan bu gastronomi mabedi, dışarıdan son derece mütevazı görünmesine rağmen içindeki özenli servis kalitesi ve muazzam sunumlarıyla gurmeleri büyülüyor. Hem yerel halkın hem elit gezginlerin sır gibi sakladığı menüsü, zengin şarap spesiyalleri eşliğinde adeta akıllara kazınan hatıralar yaratıyor.",
        "description_en": "Quietly shining in a serene side street, this gastronomy temple enchants demanding gourmets with its meticulously attentive service and magnificent visual presentations despite its modest exterior. A closely guarded secret loved by locals and elite travelers, its exceptional menu paired with rich wine specialties generously creates unforgettable memories."
    },
    "cann_la_table_du_chef": {
        "description": "Samimi boyutları ve yetenekli bir şefin mutfağı tamamen gözler önüne seren inanılmaz açık konseptiyle bu restoran, yemeği sadece tatmayı değil anlamayı seven misafirler için tasarlandı. Sadece taze ve mevsimsel malzemelerin yön verdiği günlük yaratıcı menüleriyle tamamen kişisel, etkileşimli ve doyurucu bir şölen yaratıyor.",
        "description_en": "With its highly intimate size and incredibly open-concept kitchen revealing the talented chef's mastery, this restaurant is specifically designed for guests who deeply understand and appreciate gastronomy. Its uniquely creative daily menus, guided entirely by fresh seasonal ingredients, successfully deliver a highly personalized, interactive, and fulfilling dining feast."
    },
    "cann_le_pastis": {
        "description": "Cannes'ın bohem ve samimi sokaklarının arasında lokal kültürü en iyi yansıtan mekânlardan biri olan Le Pastis, harika aperitif içkileri ve nefes kesen Provençal atıştırmalıklarıyla öne çıkar. Gün batımında dostlarınızla sohbetinize eşlik edecek ferahlatıcı kokteyller, bu butik cafenin harikulade ve cana yakın karakterini tamamlıyor.",
        "description_en": "Perfectly capturing local culture among Cannes' bohemian and intimate streets, Le Pastis remarkably stands out with its wonderful diverse aperitifs and deeply authentic Provençal snacks. Refreshing local cocktails beautifully complementing sunset conversations with friends flawlessly highlight the wonderful and extremely friendly character of this boutique cafe."
    },
    "cann_yvans_restaurant": {
        "description": "Şık dekorasyonu ve duvarlarındaki özenle seçilmiş çarpıcı sanat eserleriyle Yvan's, taze deniz balıklarının yaratıcı soslarla ustaca birleştirildiği nadide bir gastronomi cennetidir. Yemeğin her bir zerresindeki sanatsal vurgu ve mekânın romantik florası, size unutulmaz kalitede harikulade dinlendirici bir akşam molası vaat eder.",
        "description_en": "With its elegant decor and striking carefully-selected artworks, Yvan's acts as a rare gastronomy paradise where fresh sea fish delicately combines with highly creative sauces. The profound artistic emphasis in every bite alongside the venue's deeply romantic flora unconditionally promises a wonderfully relaxing and memorable evening getaway."
    },
    "cann_biererie_by_casino": {
        "description": "Casinonun şans ve adrenalin dolu ışıltılı havasının hemen yanında yer alan Biererie, dünya çapından özenle seçilmiş geniş bir butik bira yelpazesini şık Fransız pub kültürüyle sunuyor. Rahat, şık ve canlı atmosferiyle özellikle hareketli geçen bir gecenin keyif dolu harika bir tamamlayıcısı olarak kesinlikle dikkat çekiyor.",
        "description_en": "Located just beside the dazzling, adrenaline-filled vibe of the elite casino, Biererie generously offers a meticulously selected wide range of international craft beers layered with chic French pub culture. Through a flawlessly relaxed, stylish, and lively atmosphere, it serves as an excellent, deeply satisfying conclusion to a highly active night."
    },
    "cann_palm_beach_cannes": {
        "description": "Körfezin ucunda harika bir panoramaya hakim olan bu tarihi rüya eğlence kompleksi, bünyesindeki birbirinden lüks restoranlar, lüks mağazalar ve etkinlik alanlarıyla tüm Akdeniz yaşamını tek bir muazzam çatı altında toplamayı başarıyor. İster gündüz sakinliği ister gece eğlencesi için ziyaret edin, size sınırsız bir ihtişam vaat ediyor.",
        "description_en": "Commanding a wonderful sweeping panorama right at the tip of the splendid bay, this historic dream entertainment complex effortlessly unites Mediterranean lifestyle under one massive roof via lavish restaurants, boutiques, and event spaces. Whether seeking blissful daytime serenity or captivating energetic night entertainment, it consistently promises absolute unbounded grandeur."
    },
    "cann_port_canto": {
        "description": "Eski limanın aksine Croisette sahilinin daha huzurlu sonuna uzanan büyüleyici Port Canto, daha sessiz, elit ve dingin bir atmosfere sahip ihtişamlı özel marinalardan biridir. Gölgeli yemyeşil ağaçlar altında sessizce yürüyüş yapmak, lüks yelkenlileri yakından izlemek ve denizin taze sakinliğini koklamak isteyenler için kesinlikle harikadır.",
        "description_en": "Situated delightfully at the far more peaceful extended end of the Croisette shoreline, the captivating Port Canto operates as an incredibly quiet, elite, and remarkably calm premium marina. It is absolutely splendid for strolling silently beneath deeply shaded lush trees, closely admiring lavish sailing yachts, and deeply breathing in pure maritime tranquility."
    },
    "cann_cannes_walk_of_fame": {
        "description": "Birçok filme konu olmuş devasa Saray'ın hemen önünde, sinema otoritelerinin ve efsanevi aktörlerin el izlerinin betona kazındığı meşhur yıldızlar kaldırımı uzanır. Sevdiğiniz yetenekli yönetmenlerin veya popüler çocukluğunuzun kahramanlarının izlerini takip ederken gümüş ekranın o büyülü tarihi parıltısını elinizle hissetme şansını bulursunuz.",
        "description_en": "Stretching elegantly right in front of the massive legendary Palace, the famous Walk of Stars proudly protects the concrete-engraved prominent handprints of brilliant cinema authorities and legendary actors. While carefully tracing the profound marks of talented directors or beloved childhood heroes, you distinctly get the magnificent chance to physically feel the magical silver screen history."
    },
    "cann_malmaison_museum": {
        "description": "Eski şatafatlı Grand Hotel bahçesinde görkemini korumayı başaran harika bir taş malikânede kurulan Malmaison Müzesi, son derece ilham verici çok özel çağdaş sanat panolarına cömertçe ev sahipliği yapar. Riviera bölgesinin yaratıcı dinamizmini sonuna kadar hissedeceğiniz modern eserler ve göz alıcı tematik sergileriyle ufuk açıcı zengin bir perspektif sergiliyor.",
        "description_en": "Set flawlessly in a wonderful stone mansion successfully preserving its immense charm within the former, highly opulent Grand Hotel garden, Malmaison Museum generously hosts remarkably inspiring and deeply exclusive contemporary art displays. Featuring striking modern artworks and highly captivating thematic exhibitions, it undoubtedly offers a profoundly enlightening rich perspective of genuine Riviera creative dynamism."
    },
    "cann_villa_rothschild": {
        "description": "Son derece etkileyici muazzam bir bahçeyle sarılı tarihi neoklasik sahil köşkü olan Villa Rothschild, bugün bölgenin son derece saygın harika kütüphanesi olarak paha biçilemez bir işlev görüyor. Sessizce palmiyeler arasında mimarisine hayran kalacağınız büyük yapı, aynı anda devasa asaletini koruyup zengin bir kent belleğini harikulade bir şekilde sunar.",
        "description_en": "Encircled entirely by an intensely impressive vast tropical garden, the historic neoclassical coastal masterpiece Villa Rothschild seamlessly functions today as an incredibly respected, profoundly gorgeous regional library. This grand structure, whose flawless architecture you will deeply admire amidst silent swaying palms, magically simultaneously guards immense nobility and proudly presents a wonderfully rich urban memory."
    },
    "cann_villa_domergue": {
        "description": "Kaliforniya tarzı yeşil görkemli tepelerde bir tablo gibi gizlenmiş harika Art Deco harikası Villa Domergue, sanatçı çift tarafından olağanüstü bir aşk ve titizlikle dizayn edilmiş enfes bir sığınaktır. Çam ağaçları ve süslü havuzlardan harika deniz manzarasına doğru aralanan yapı, özellikle Cannes Festivali sırasındaki özel sanat şölenleriyle büyüleyicidir.",
        "description_en": "Hidden flawlessly like a masterful painting among perfectly majestic California-style green hills, the tremendous Art Deco wonder Villa Domergue is an exquisite serene sanctuary meticulously designed with phenomenal passion by an artist couple. Opening widely from lush pines and ornate pristine pools to breathtaking endless sea views, the structure remains deeply fascinating, especially during wildly exclusive Cannes Festival artistic feasts."
    },
    "cann_long_beach_cannes": {
        "description": "Açık ve ferah denizin üzerinde lüksün ve sadeliğin kusursuz birleşimi konumundaki göz alıcı Long Beach, devasa plaj yataklarıyla size rüya gibi bir güneşlenme sefası vaat ediyor. Pırıl pırıl temiz sularından çıkıp hemen lüks sahil restoranındaki oldukça taze hafif salatalar eşliğinde tazeleyici saatlerin ve sakinliğin tadını doyasıya çıkarın.",
        "description_en": "Standing proudly as the incredibly flawless combination of lavish luxury and elegant simplicity directly on the immense open sea, glamorous Long Beach beautifully promises a truly dreamlike premium sunbathing delight via enormous plush beach beds. Exiting the sparkling clean soothing waters, deeply and absolutely relish uniquely refreshing hours alongside incredibly fresh light salads at the superb coastal restaurant."
    },
    "cann_goeland_beach": {
        "description": "Plajın hafif sükuneti ve yüksek hizmet kalitesi etrafında dizayn edilmiş bu aydınlık lüks mekân, özellikle sabah denizinden esen serin hafif rüzgarlarla harika kahvaltılar etmek isteyenlerin muazzam bir favorisidir. Öğleden sonra güneşi ve şemsiyeler arasında huzur bulurken zamanın yavaş yavaş aktığını göreceğiniz nadir, eşsiz ve sakin adreslerden biridir.",
        "description_en": "Elegantly designed directly around the subtle gentle tranquility of the pristine beach and incredibly high service quality, this incredibly bright luxury venue acts as a massive favorite for exactly those wanting wonderful flawless breakfasts embraced by refreshing cool morning sea breezes. It operates as one of the exceedingly rare, entirely unique, and deeply peaceful addresses where you clearly observe time slowly drifting amidst bright afternoon sunshine and inviting umbrellas."
    },
    "cann_mace_beach": {
        "description": "Özellikle sinema haftasında halka açık film gösterimleriyle harikulade canlanan harika Mace Plajı, en merkezi çok aktif konumuyla adeta daima gençlere ve enerjiye açık popüler ve ücretsiz güzel bir duraktır. Yan yana dizili birbirinden güzel büfeler ve sıcak sarı kumlarıyla hiç kopamayacağınız bir yerel Akdeniz sıcaklığını hararetle harmanlıyor.",
        "description_en": "Brilliantly springing to vibrant life, especially with magnificent free open-air movie screenings wonderfully accessible to the general public precisely during cinema week, superb Mace Beach essentially operates as a beautifully accessible, decidedly popular stop relentlessly open to remarkable energy given its intensely central and active location. Via side-by-side uniquely beautiful kiosks and deliciously warm yellow sands, it passionately creates a profoundly local Mediterranean warmth."
    },
    "cann_zplage": {
        "description": "Lüks oteller serisinin harika devasa zincirine muazzam entegre olarak işletilen harika Zplage, mükemmel konfor ve prestijin muhteşem buluştuğu sahilin oldukça popüler canlı bir harika köşesidir. Enerji dolu harika dj etkinlikleri ve özel lezzetli soğuk menüsü ile kendinizi inanılmaz özel ve Akdeniz modasına tamamen bürünmüş hissedebildiğiniz canlı enerjik bir noktadır.",
        "description_en": "Operated seamlessly by being fabulously integrated into the wonderful massive chain of tremendously affluent luxury hotels, wonderful Zplage is an incredibly popular and undeniably lively premium corner of the coast where absolutely flawless superior comfort gracefully meets phenomenal prestige. Due to relentlessly fantastic energy-filled exclusive DJ sets and extremely delicious uniquely cold menus, it basically is a highly vibrant energetic hotspot."
    },
    "cann_palme_d_or_terrace": {
        "description": "Michelin yıldızlı prestijli yemeğin oldukça çarpıcı bir sanat galerisiyle birleştiği dev terasa ev sahipliği yapan bu ünlü mekân, şov dünyasında baş döndüren efsanevi partilere ev sahipliği yapıyor. Harika bir gün batımı kızıllığı yavaşça vururken paha biçilemez manzarasıyla tamamen görsel mükemmel bir ziyafeti kalıcı olarak sunar.",
        "description_en": "Serving proudly as the incredibly expansive outdoor terrace where an incredibly prestigious Michelin-starred feast flawlessly merges with a highly striking beautiful art gallery, this profoundly renowned wide open-air venue basically hosts unbelievably mind-blowing legendary gigantic parties deeply within the phenomenal entertainment world. As an absolutely wonderful deep ruby sunset magically strikes slowly, it permanently, undoubtedly offers an entirely visual and flawlessly delightful banquet."
    },
    "cann_harry_s_bar_cannes": {
        "description": "Klasik caz havasının seçkin kokteyller ile mükemmel harmanlandığı Harry's Bar, muazzam nostaljik dokunuşlarla bezeli eski nesil efsanevi bar kültürünü yaşatmaya devam ediyor. İçeriye adım attığınızda adeta zaman makinesiyle geçmişin şık ve büyülü gecelerine elit bir geçiş yapmış gibi büyük ve derin bir keyif hissedersiniz.",
        "description_en": "It stands as an iconic bar culture adorned meticulously with nostalgic brilliant touches, where classic jazz vibes gracefully blend perfectly with extremely high-quality globally recognized premium cocktails. Immediately stepping into this legendary ambiance essentially relaxes you as if making a vastly elite and highly quality-driven transition back into tremendously brilliant chic magical nights of the beautiful deep past."
    },
    "cann_le_cirque_cannes": {
        "description": "Çarpıcı, yaratıcı şovlarıyla ve sirk temalı efsane dekoratif gösterişli ihtişamlarıyla bilinen oldukça heyecan verici Le Cirque, son derece şenlikli ve kaliteli çılgın gecelere renkli harikulade ev sahipliği yapıyor. Görsel etkileyici gösterilerin hemen ardından elit atıştırmalıkların ve modern karışımların sunulduğu benzersiz efsanevi bir şölendir.",
        "description_en": "Unquestionably widely celebrated primarily for its incredibly striking highly creative captivating performances and thoroughly legendary vibrantly flashy circus-themed spectacular decorative grandeur, significantly thrilling Le Cirque dynamically precisely hosts brilliantly colorful, extremely high-quality remarkably festive uniquely wild nights."
    },
    "cann_bobo_l_antispas": {
        "description": "Doğal ve lokal dokunuşlara son derece önem gösteren bu özel gizli ve sıcak köşede, Akdeniz ruhuna tamamen sadık kalarak otantik, şık ve çok samimi zengin menüler çıkarılır. Kendi halinde sakin, kaliteli ve elit bir zaman arayanlar için muazzam rahat ambiyansıyla efsane bir Fransız Rivierası butik lokal deneyimi yaşatır.",
        "description_en": "Within this outstandingly gorgeous profoundly private hidden charmingly cozy lovable little corner that tremendously highly prioritizes deeply exceptionally natural beautifully astonishing local meticulous touches, intensely genuinely superbly authentic highly chic and profoundly extremely approachable marvelously rich generous menus wholly relentlessly devoted immediately toward fulfilling the beautiful authentic Mediterranean spirit."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/cannes.json.draft'
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

print(f"✅ Cannes Part 2: Enriched {count} items.")
