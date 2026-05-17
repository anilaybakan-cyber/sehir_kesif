#!/usr/bin/env python3
import json

updates = {
    "cann_boulevard_de_la_croisette": {
        "description": "Cannes'ın Akdeniz'e kucak açan dünyaca ünlü sahil şeridi Boulevard de la Croisette, lüks butikleri, görkemli palmiye ağaçları ve göz alıcı özel plajlarıyla Fransız Rivierası'nın kalbini oluşturur. Akşamüstü uzun yürüyüşler yaparken şehrin lüks ve gösterişli atmosferini en saf haliyle hissedebileceğiniz benzersiz bir alandır.",
        "description_en": "The world-famous Boulevard de la Croisette embraces the Mediterranean with its luxury boutiques, magnificent palm trees, and glamorous private beaches, forming the true heart of the French Riviera. A sunset stroll here allows you to deeply feel the city's opulent and sophisticated atmosphere."
    },
    "cann_palais_des_festivals": {
        "description": "Her yıl Cannes Film Festivali'ne ev sahipliği yapan bu efsanevi saray, sinema dünyasının en büyük yıldızlarının yürüdüğü ikonik kırmızı halısıyla ziyaretçilerin akınına uğrar. Kültürel prestijin merkezi olan merdivenlerde, sanki bir film galasındaymış gibi fotoğraf çektirmek şehrin en büyük ritüelidir.",
        "description_en": "Hosting the annual Cannes Film Festival, this legendary venue is flocked by visitors eager to see the iconic red carpet where cinema's biggest stars walk. Taking a photo on these steps, feeling like a movie star at a premiere, is an essential cultural ritual."
    },
    "cann_le_suquet_old_town": {
        "description": "Cannes'ın ışıltılı sahilinden sıyrılıp tarihsel yüzüne şahit olacağınız Le Suquet, dik ve labirent gibi daracık sokakları, eski taş evleri ve pastel tonlarıyla eski balıkçı köyü ruhunu yaşatır. Tepeye tırmandığınızda tüm şehri ve limanı ayaklarınızın altına seren manzarasıyla tarifsiz bir huzur sunar.",
        "description_en": "Stepping away from the glamorous shoreline, Le Suquet reflects the city's historical face with its steep, labyrinthine narrow streets, ancient stone houses, and pastel tones preserving the former fishing village spirit. Reaching the hilltop rewards you with breathtaking panoramic views over the harbor."
    },
    "cann_marché_forville": {
        "description": "Şehrin gastronomi kalbinin attığı Marché Forville, taze deniz ürünleri, yerel peynirler, zeytinler ve renkli meyvelerle dolu tezgâhlarıyla gerçek bir Provençal pazar deneyimi sunuyor. Yerel halkın günlük alışveriş ritüeline karışmak ve en taze yöresel lezzetleri sabah saatlerinde keşfetmek isteyenler için biçilmiş kaftan.",
        "description_en": "As the gastronomic heart of the city, Marché Forville offers a genuine Provençal market experience with stalls brimming with fresh seafood, local cheeses, olives, and colorful fruits. It is perfectly tailored for those wanting to mingle with locals and discover fresh regional flavors in the morning."
    },
    "cann_lérins_islands_ferry": {
        "description": "Cannes'ın hemen karşısında uzanan ve yemyeşil doğasıyla dikkat çeken dev Lérins Adaları'na açılan bu feribot hattı, şehrin kalabalığından uzakta sakin bir sığınağa doğru serin bir yolculuk başlatıyor. Günübirlik ada maceraları, temiz Akdeniz havası ve çam kokuları arasında benzersiz bir rota sunar.",
        "description_en": "Departing to the stunning Lérins Islands positioned just off the coast, this ferry ride initiates a tranquil blue journey away from the city's lively crowds. It offers a unique route for a daily island adventure surrounded by pristine Mediterranean air and the refreshing scent of pine trees."
    },
    "cann_île_sainte-marguerite": {
        "description": "Lérins Adaları'nın en büyüğü olan Île Sainte-Marguerite, efsanevi Demir Maskeli Adam'ın hapsedildiği eski kalesi ve asırlık okaliptüs ormanlarıyla tarih ve doğayı kusursuz birleştiriyor. Gizli koylarında yüzebilir, çam ağaçlarının gölgesinde piknik yaparak şehrin koşturmacasını ardınızda bırakabilirsiniz.",
        "description_en": "The largest of the Lérins Islands, Île Sainte-Marguerite perfectly blends nature and history, featuring the ancient fortress where the Man in the Iron Mask was imprisoned. You can swim in its hidden coves and picnic under the eucalyptus trees, leaving the city hustle behind."
    },
    "cann_île_saint-honorat": {
        "description": "Sadece rahiplerin yaşadığı bu huzur dolu ada, beşinci yüzyıldan beri aktif olan bir manastıra ve yemyeşil antik bağlara ev sahipliği yapmaktadır. Ada sessizliği kucaklayan atmosferiyle ruhu dinlendirirken, bölgenin tarihi manastırında üretilen ödüllü yöresel şarapların tadımını yapma fırsatı sunuyor.",
        "description_en": "This peaceful island, inhabited solely by monks, hosts an active monastery dating back to the 5th century along with ancient green vineyards. Embracing an atmosphere of utter silence, it offers a deeply restful experience and the rare opportunity to taste award-winning monastic wines."
    },
    "cann_musée_de_la_castre": {
        "description": "Antik bir Orta Çağ kalesinin içerisine konumlanan Musée de la Castre, antik medeniyetlere, Okyanusya sanatına ve Doğu kökenli antikalara kadar uzanan zengin bir koleksiyona sahiptir. Kulenin spiral merdivenlerini tırmandıktan sonra Cannes Körfezi'nin eşsiz panaromik manzarası ile karşılaşacaksınız.",
        "description_en": "Housed within a medieval castle, Musée de la Castre boasts a rich collection ranging from ancient civilizations to Oceanian art and Oriental antiquities. Climbing the spiral staircase of the old tower rewards you with an unmatched, breathtaking panoramic view of the entire Bay of Cannes."
    },
    "cann_rue_d_antibes_shopping": {
        "description": "Moda ve alışveriş tutkunlarının Cannes'daki vazgeçilmez rotası olan Rue d'Antibes, lüks markalardan butik tasarımcılara kadar geniş yelpazede birçok ünlü mağazaya ev sahipliği yapıyor. Harika pastaneleri, zarif kafeleri ve renkli vitrinleriyle sadece alışveriş değil tam bir Fransız yaşam tarzı deneyimidir.",
        "description_en": "An indispensable route for fashion enthusiasts, Rue d'Antibes is home to a wide spectrum of stores ranging from luxury brands to boutique designers. With its delightful pastry shops, elegant local cafes, and vibrant window displays, it offers a complete French lifestyle experience beyond just shopping."
    },
    "cann_vieux_port_cannes": {
        "description": "Şehrin en eski kısmının eteğinde uzanan bu muazzam Eski Liman, gösterişli süper yatların yan yana dizildiği ve geleneksel ahşap balıkçı teknelerinin ahenkle sallandığı büyüleyici bir marinadır. Akşamüstü güneşinin altın rengine boyadığı sular izlerken romantik ve unutulmaz anlar yakalayabilirsiniz.",
        "description_en": "Stretching at the foot of the old town, this magnificent Old Port is a fascinating marina where glamorous superyachts line up next to gently swaying traditional fishing boats. Watching the sunset cast a golden hue across the water creates truly romantic and unforgettable seaside moments."
    },
    "cann_église_notre-dame_de_l_es": {
        "description": "Le Suquet tepesinde tüm görkemiyle şehri kucaklayan ve on altıncı yüzyılda inşa edilmiş olan Notre-Dame de l’Espérance Kilisesi, muazzam gotik mimarisi ve devasa çan kulesiyle öne çıkıyor. Klasik müzik konserlerine ev sahipliği yapan mistik sahanlığı sayesinde yaz gecelerine tarihi bir ahenk katıyor.",
        "description_en": "Crowning the Le Suquet hill in its full glory, the 16th-century Church of Notre-Dame de l’Espérance stands out with its magnificent Gothic architecture and massive bell tower. Hosting classical music concerts in its mystical courtyard, it adds historical harmony to romantic summer nights."
    },
    "cann_carlton_beach_club": {
        "description": "Efsanevi Carlton Oteli'ne bağlı bu ultra prestijli kulüp, altın kumsalların şezlonglarla donatıldığı, sinema yıldızlarının tercih ettiği muhteşem bir sahil dinlenme tesisidir. Birinci sınıf hizmet kalitesi ve sofistike Fransız kokteylleri ile Riviera yaşamının lüks standartlarına doğrudan adım atmanızı sağlar.",
        "description_en": "Attached to the legendary Carlton Hotel, this ultra-prestigious beach club features golden sands equipped with sun loungers favored by movie stars. Providing first-class service and sophisticated French cocktails, it allows you to directly step into the luxurious standards of the Riviera lifestyle."
    },
    "cann_la_plage_du_martinez": {
        "description": "Croisette bulvarının incisi sayılan Martinez plajı, su sporlarından sakin bir güneşlenme kaçamağına kadar çeşitli rahatlama olanaklarıyla ünlüdür. Okyanus hissi veren açık mavi suları seyrederken özenli şeflerin hazırladığı deniz ürünleriyle hem gözünüzü hem de enfes mutfağıyla damaklarınızı şenlendirir.",
        "description_en": "Considered the pearl of the Croisette boulevard, Martinez beach is famous for offering diverse relaxation options from water sports to tranquil sunbathing escapes. While watching the ocean-blue waters, the carefully crafted seafood delights prepared by executive chefs will pamper your sophisticated palate."
    },
    "cann_la_guérite": {
        "description": "Sainte-Marguerite Adası'nın sarp kayalıkları üzerinde yer alan La Guérite, taze ızgara ıstakoz ve eşsiz DJ performanslarının unutulmaz birleşimini misafirlerine cömertçe sunuyor. Adaya özel ulaşım sağlayan sürat tekneleriyle ulaşılan mekân, Cannes eğlence hayatının en gizli ve özel cevherlerinden biridir.",
        "description_en": "Perched on the rocky outcrops of Sainte-Marguerite Island, La Guérite generously offers a memorable combination of fresh grilled lobster and outstanding live DJ performances. Accessed exclusively via private speedboats, this venue stands as one of the most secluded and exclusive gems of Cannes nightlife."
    },
    "cann_barrière_beach": {
        "description": "Cannes'ın sofistike eğlence noktalarından Barrière Beach, özel iskelesi ve konforlu alanlarıyla şık bir sahil şöleni vadeder. Gün boyu güneşin tadını çıkarıp ardından etkileyici şampanya menüsü eşliğinde canlı Dj setleriyle hareketli bir Fransız akşamına sorunsuzca geçiş yapabileceğiniz nadir mekânlardandır.",
        "description_en": "As a sophisticated entertainment hub, Barrière Beach promises a stylish coastal feast with its private pier and comfortable lounging areas. It is a rare venue where you can smoothly transition from daytime sunbathing to a lively French evening fueled by an impressive champagne menu and dynamic DJ sets."
    },
    "cann_mademoiselle_gray": {
        "description": "Bohem ve şık konseptiyle dikkat çeken Mademoiselle Gray, lüks şezlongları ve sıcak kumların üzerindeki büyüleyici ortamıyla gündüz deniz, akşam ise kaliteli eğlencenin merkezidir. Lübnan mutfağından ilham alan yenilikçi lezzetleri ve Akdeniz rüzgarları eşliğinde eşsiz bir gastronomi yolculuğu vadediyor.",
        "description_en": "Standing out with its bohemian and chic concept, Mademoiselle Gray acts as a daytime beach and an evening entertainment hub right on the warm sands. It promises a unique gastronomic journey accompanied by gentle Mediterranean winds and highly innovative culinary flavors inspired by Lebanese cuisine."
    },
    "cann_la_môme_plage": {
        "description": "Zarif lacivert şemsiyeleri, İtalyan Riviera tarzındaki tasarımı ve şık ambiyansıyla La Môme Plage, canlı piyano ezgileri eşliğinde güneşlenip kokteyl yudumlayabileceğiniz nezih bir adrestir. Burada La Dolce Vita (Tatlı Hayat) konseptini en ince ayrıntılarına kadar yaşarken yüksek kaliteli hizmetin tadını çıkarırsınız.",
        "description_en": "With its elegant navy blue umbrellas, Italian Riviera-style design, and chic ambiance, La Môme Plage is an exclusive address to sunbathe and sip cocktails to live piano tunes. Here you can truly experience the La Dolce Vita concept down to the finest details while enjoying high-quality upscale service."
    },
    "cann_copal_beach": {
        "description": "Güney Amerika ruhunu ve mistik Amazon havasını Akdeniz kıyısına taşıyan Copal Beach, egzotik ahşap detaylarla örülü renkli ve sıcak bir tasarıma sahiptir. Odun ateşinde pişen özel tatlar ve Latin ezgileriyle donatılmış dinamik atmosferi, Cannes sahillerine canlandırıcı bir farklılık ile egzotik ritim katar.",
        "description_en": "Bringing the spirit of South America and mystical Amazon flair to the Mediterranean coast, Copal Beach features a colorful and warm design laced with exotic wood details. Its dynamic atmosphere with wood-fired special tastes and Latin rhythms adds a refreshing difference and exotic pulse to the Cannes shores."
    },
    "cann_lucia_cannes": {
        "description": "Canlı portakal ağaçları ve göz alıcı renk paletiyle dekore edilmiş Lucia, Akdeniz güneşini kucaklayan sıcak ve pozitif enerjisiyle konuklarına benzersiz bir sahil stili sunar. Lezzetli tapas tabakları ve paylaşmalık Akdeniz tatları, günün her saati dostlarla keyifli anılar yaratmak için büyüleyici bir seçenek oluşturur.",
        "description_en": "Decorated with vibrant orange trees and an eye-catching color palette, Lucia offers an unequivocally warm and positive coastal style that embraces the Mediterranean sun. Its delicious tapas platters and shareable Mediterranean flavors provide a charming setting for creating joyful memories with friends at any hour."
    },
    "cann_vegaluna": {
        "description": "Özellikle çocuklu ailelerin rahat bir plaj günü geçirmesi için tüm ince detayların düşünüldüğü Vegaluna, sığ ve ince kumlu özel çocuk oyun alanlarıyla ebeveynlerin kurtarıcısıdır. Şezlonglarda huzurla Akdeniz güneşinin tadını çıkarırken, ailenizin güvende ve keyifli olmasının rahatlığını doya doya yaşayabilirsiniz.",
        "description_en": "Where every small detail is considered for families with children to enjoy a relaxed beach day, Vegaluna acts as a true lifesaver with shallow waters and private sandy playgrounds. While peacefully soaking up the Mediterranean sun on loungers, you can fully relish the comfort of your family's safety and joy."
    },
    "cann_ondine_plage": {
        "description": "Kusursuz Fransız zarafetini sahil rahatlığıyla mükemmel dengede tutan Ondine Plage, şık hasır mobilyaları ve deniz mahsullerindeki rakipsiz ustalıklarıyla tanınır. Taze yakalanmış nefis istiridyeleri tadarken dalgaların hemen dibinde olduğunuzu hissettiren konumunda huzur dolu bir öğleden sonrasına imza atın.",
        "description_en": "Perfectly balancing flawless French elegance with coastal comfort, Ondine Plage is well-known for its stylish wicker furniture and unrivaled mastery in fresh seafood. Enjoy a famously tranquil afternoon sampling freshly caught delicious oysters in a prime location that makes you feel intimately close to the soothing waves."
    },
    "cann_plage_du_festival": {
        "description": "Adını ünlü film festivalinden alan ve kırmızı halı şıklığını sahil dokusuna yansıtan plaj, modern mimarisi ve devasa güneşlenme teraslarıyla film yıldızlarının çekim alanıdır. Göz yormayan minimalist detaylar eşliğinde, şehrin tam merkezinde ama gürültüden uzak dinlendirici bir kaçamak şansı sağlar.",
        "description_en": "Named after the renowned film festival and reflecting red carpet elegance into its coastal texture, this beach attracts movie stars with its modern architecture and substantial sunbathing terraces. Surrounded by soothing minimalist details, it provides a relaxing, star-quality getaway right in the city center yet away from the noise."
    },
    "cann_rado_plage": {
        "description": "Bölgenin en uzun soluklu ve köklü işletmelerinden olan Rado Plage, geleneksel ile modern Fransız mutfağını samimi misafirperverlik anlayışıyla, harika bir deniz fonunda birleştiriyor. Müdavimlerinin asla vazgeçemediği sıcak ortamında, ince kumlar üzerinde şampanyanızı yudumlayarak gün batımını keyifle bekleyebilirsiniz.",
        "description_en": "As one of the longest-running and well-established venues in the area, Rado Plage seamlessly combines traditional and modern French cuisine with sincere hospitality against a stunning ocean backdrop. In its warm atmosphere cherished by regulars, you can delightfully await the golden sunset while sipping your refined champagne."
    },
    "cann_miramar_plage": {
        "description": "Kalabalık kumsallardan bir nebze sıyrılan butik deneyimi ve sade şıklığıyla Miramar, altın sarısı kumlarında dingin ve kişiselleştirilmiş birinci sınıf bir servis vaat ediyor. Organik malzemeler ağırlıklı menüsü ve dinlendirici müziğiyle, şehirden kopmadan kendinize kaliteli vakit ayırmanın en şık formülüdür.",
        "description_en": "Stepping slightly away from crowded shores with its boutique experience and simple elegance, Miramar guarantees a serene, highly personalized first-class service on its golden sands. With an organic-focused culinary menu and relaxing music, it stands as the most stylish formula for dedicating quality personal time without leaving the city."
    },
    "cann_la_palme_d_or": {
        "description": "İki Michelin yıldızına sahip bu baş döndürücü restoran, yemek yemeyi adeta bir sanat formuna dönüştüren yaratıcı şefin elinden çıkan sürprizlerle dolu tadım menüleri sunar. Zarif sinema temalı göz alıcı dekorasyonu ve panaromik körfez manzarası eşliğinde unutulması imkansız bir gastronomi zirvesi yaşatır.",
        "description_en": "Boasting two prestigious Michelin stars, this dazzling restaurant offers surprise-filled tasting menus by an incredibly creative chef, turning food into pure art. Accompanied by elegant cinema-themed decorations and sweeping panoramic bay views, it delivers an absolutely unforgettable and world-class peak gastronomic experience."
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

print(f"✅ Cannes Part 1: Enriched {count} items.")
