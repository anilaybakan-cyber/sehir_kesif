#!/usr/bin/env python3
import json

updates = {
    "Ryans Ibiza Apartments": {
        "description": "Figueretas plajının hemen yanında modern ve enerjik bir konaklama deneyimi sunan Ryans, genç ve dinamik gezginlerin uğrak noktasıdır. Sosyal alanları, havuz partileri ve kentin eğlence merkezlerine yakınlığıyla İbiza'nın kozmopolit ruhunu doyasıya hissetmek için mükemmel bir tercihtir.",
        "description_en": "Offering a modern and energetic accommodation experience right next to Figueretas beach, Ryans is a frequent spot for young and dynamic travelers. With its social areas, pool parties, and proximity to the city's entertainment centers, it is a perfect choice to fully feel Ibiza's cosmopolitan spirit."
    },
    "Can Lluc Boutique Country Hotel & Villas": {
        "description": "Adanın kalbinde, zeytin ve çam ormanları arasına gizlenmiş bu butik otel, İbiza'nın huzurlu kırsal yaşamını lüksle buluşturuyor. Geleneksel mimarisi ve sessiz atmosferiyle, kentin gürültüsünden uzaklaşıp doğayla baş başa kalmak isteyenler için saklı bir cennet niteliğindedir.",
        "description_en": "Hidden among olive and pine forests in the heart of the island, this boutique hotel brings Ibiza's peaceful rural life together with luxury. With its traditional architecture and quiet atmosphere, it is a hidden paradise for those wanting to escape city noise and stay alone with nature."
    },
    "Sud Ibiza Suites - Apartamentos de Lujo en Ibiza": {
        "description": "Figueretas sahilinde denize sıfır konumu ve minimalist şıklığıyla öne çıkan bu lüks süitler, modern konforu Akdeniz manzarasıyla birleştiriyor. Panaromik terası ve kentin merkezine yürüme mesafesindeki konumuyla, İbiza'da stil sahibi bir tatil arayanlar için muazzam bir seçimdir.",
        "description_en": "Standing out with its seafront location on the Figueretas coast and minimalist elegance, these luxury suites combine modern comfort with Mediterranean views. With its panoramic terrace and walking distance to the city center, it is a magnificent choice for those seeking a stylish holiday in Ibiza."
    },
    "Apartamentos Llevant": {
        "description": "Şehrin hareketli noktalarına yakın, samimi ve ferah konaklama birimlerinden oluşan bu tesis, uygun fiyatlı ve kaliteli bir İbiza tatili vadediyor. Plaja yakınlığı ve çevresindeki şık kafeleriyle, kentin ritmini hissetmek ve güneşin tadını çıkarmak için pratik bir konaklama durağıdır.",
        "description_en": "Consisting of sincere and spacious accommodation units near the city's vibrant spots, this facility promises an affordable and high-quality Ibiza holiday. With its proximity to the beach and surrounding chic cafes, it is a practical accommodation stop to feel the city's rhythm and enjoy the sun."
    },
    "Pura Vida": {
        "description": "Playa Niu Blau'nun kristal sularına karşı kurulan bu şık beach club, 'saf hayat' felsefesini her detayında hissettiriyor. Taze deniz ürünleri, tazeleyici kokteylleri ve gün boyu süren huzurlu atmosferiyle, kalabalıktan uzak, kaliteli bir İbiza deniz sefası için en iyi adreslerden biridir.",
        "description_en": "Set against the crystal waters of Playa Niu Blau, this chic beach club makes you feel the 'pure life' philosophy in every detail. With fresh seafood, refreshing cocktails, and a peaceful atmosphere throughout the day, it's one of the best addresses for a high-quality Ibiza seaside delight away from crowds."
    },
    "Amante Ibiza": {
        "description": "Sarp kayalıkların arasına gizlenmiş, masmavi deniz manzaralı bu prestijli mekan, adanın en romantik gastronomi duraklarından biri kabul edilir. Şık tasarımı ve kaliteli mönüsüyle bildiğimiz bu yer, özellikle ay ışığı altındaki akşam yemekleri için İbiza'nın en seçkin adreslerinden biridir.",
        "description_en": "Hidden among steep cliffs with deep blue sea views, this prestigious venue is considered one of the island's most romantic gastronomy stops. Known for its chic design and quality menu, it is one of Ibiza's most elite addresses especially for moonlight dinners."
    },
    "El Bucanero": {
        "description": "İbiza kenti kıyılarında geleneksel bir sahil tavernasını andıran bu mekan, taze balıkları ve yerel İspanyol mezeleriyle (tapas) tanınır. Denize sıfır masaları ve dalga sesleri eşliğinde sunduğu samimi servis anlayışıyla, adanın gerçek lezzet mirasını deneyimlemek isteyenlerin uğrak yeridir.",
        "description_en": "Reminiscent of a traditional seaside taverna on the shores of Ibiza city, this venue is known for its fresh fish and local Spanish mezes (tapas). With its seafront tables and sincere service provided accompanied by the sound of waves, it is a frequent spot for those wanting to experience the island's true flavor heritage."
    },
    "El Chiringuito Ibiza": {
        "description": "Es Cavallet plajının şık ve doğal atmosferinde yer alan El Chiringuito, sofistike rahatlığı ve gurme mönüsüyle ünlüdür. Beyaz kumlar üzerinde, Akdeniz güneşinin tadını çıkarırken kaliteli müzik ve ferahlatıcı içecekler eşliğinde İbiza yazını en üst seviyede yaşatan ikonik bir plaj restoranıdır.",
        "description_en": "Located in the chic and natural atmosphere of Es Cavallet beach, El Chiringuito is famous for its sophisticated comfort and gourmet menu. It's an iconic beach restaurant that makes you live the Ibiza summer at the highest level on white sands, while enjoying the Mediterranean sun accompanied by quality music and refreshing drinks."
    },
    "Bora Bora Eivissa": {
        "description": "Playa d'en Bossa'nın eğlence tarihinde bir efsane olan Bora Bora, kumsalın hemen üzerindeki dev partileri ve enerjik atmosferiyle tanınır. Dünyaca ünlü DJ'lerin performans sergilediği bu mekan, İbiza'nın özgür ruhunu ve bitmek bilmeyen parti enerjisini en saf haliyle temsil eden bir sahil kulübüdür.",
        "description_en": "A legend in the entertainment history of Playa d'en Bossa, Bora Bora is known for its giant parties right on the beach and its energetic atmosphere. This venue where world-famous DJs perform is a beach club representing Ibiza's free spirit and never-ending party energy in its purest form."
    },
    "Ryans La Marina": {
        "description": "İbiza'nın tarihi limanında yer alan bu şık butik otel, Art Deco mimarisi ve marinaya hakim manzarasıyla nostaljik bir şıklık sunuyor. Şehrin alışveriş ve eğlence merkezlerine yürüme mesafesinde olmasıyla büyük avantaj sağlayan tesis, adanın kozmopolit lüksünü hissetmek isteyenler için ideal bir duraktır.",
        "description_en": "Located in Ibiza's historic harbor, this chic boutique hotel offers nostalgic elegance with its Art Deco architecture and commanding view of the marina. Providing a great advantage with its walking distance to the city's shopping and entertainment centers, the facility is an ideal stop for those wanting to feel the island's cosmopolitan luxury."
    },
    "Es Repòs": {
        "description": "İbiza'nın dar taş sokakları arasında yer alan bu samimi kafe-restoran, geleneksel Ege ve Akdeniz lezzetlerini samimi bir atmosferde sunar. Yöresel ürünlerle hazırlanan hafif öğle yemekleri ve taze kahveleriyle, şehir turuna huzurlu bir mola vermek isteyen gezginlerin en çok tercih ettiği yerel noktalardan biridir.",
        "description_en": "Located among Ibiza's narrow stone streets, this sincere cafe-restaurant offers traditional Aegean and Mediterranean flavors in an intimate atmosphere. With light lunches prepared with local products and fresh coffees, it's one of the most preferred local spots for travelers wanting a peaceful break from the city tour."
    },
    "Es Tap Nou": {
        "description": "Tazeliğin ve yerel üretimin merkezi olan bu mekan, hem geniş taze meyve-sebze pazarı hem de içindeki samimi tapas barıyla ünlüdür. Adanın tarlalarından sofraya gelen lezzetleri tadabileceğiniz bu otantik durak, İbiza'nın gerçek gastronomi ruhunu keşfetmek isteyenler için paha biçilemez bir keşiftir.",
        "description_en": "The center of freshness and local production, this venue is famous for both its wide fresh fruit-vegetable market and its sincere tapas bar. This authentic stop where you can taste flavors coming from the island's fields to the table is a priceless discovery for those wanting to explore Ibiza's true gastronomic spirit."
    },
    "Vila Café": {
        "description": "Eski kentin tarihi meydanına komşu olan Vila Café, nostaljik dekoru ve sokağa taşan masalarıyla kentin nabzını tutan keyifli bir duraktır. Sabah güneşinde kahvenizi içip Dalt Vila'nın görkemli silüetini izlemek ve taze hamur işlerinin tadına bakmak için kentin en samimi adreslerinden biridir.",
        "description_en": "Adjacent to the old town's historic square, Vila Café is a pleasant stop catching the city's pulse with its nostalgic decor and tables spilling onto the street. It is one of the city's most sincere addresses to have your coffee in the morning sun, watch Dalt Vila's grand silhouette, and taste fresh pastries."
    },
    "Pastelería Figueretas": {
        "description": "Onlarca yıllık geçmişiyle İbiza'nın en köklü pastanelerinden biri olan bu dükkan, geleneksel İspanyol tatlıları ve ev yapımı kurabiyeleriyle bilinir. Figueretas bölgesinin vazgeçilmez bir parçası olan pastane, sokağa yayılan mis gibi kokularıyla hem yerlileri hem de tatlı tutkunu gezginleri mest eder.",
        "description_en": "One of Ibiza's most established bakeries with decades of history, this shop is known for traditional Spanish desserts and homemade cookies. An indispensable part of the Figueretas region, the bakery enchants both locals and dessert-loving travelers with the delightful scents spreading into the street."
    },
    "Harinus Forn Artesà": {
        "description": "Geleneksel ekmek yapım sanatını modern fırıncılıkla birleştiren Harinus, çıtır taze ekmekleri, tuzlu atıştırmalıkları ve leziz kahveleriyle bilinir. Şehrin farklı noktalarında yer alan bu popüler durak, günün her saati taze bir mola vermek ve İbiza'nın fırın kültürünü deneyimlemek için idealdir.",
        "description_en": "Combining the traditional art of bread-making with modern baking, Harinus is known for its crispy fresh breads, savory snacks, and delicious coffees. This popular stop located at various points in the city is ideal for taking a fresh break at any hour and experiencing Ibiza's bakery culture."
    },
    "Barocco Nicolau": {
        "description": "İbiza çarşısı içerisinde kendine has dekorasyonu ve samimi atmosferiyle dikkat çeken Barocco Nicolau, kentin en neşeli ve karakteristik barlarındandır. Kokteyl sanatı ve kaliteli müzik eşliğinde geçen akşamüstü sohbetleri için yerel halkın ve gezginlerin popüler buluşma noktalarından biridir.",
        "description_en": "Attracting attention with its unique decoration and sincere atmosphere within the Ibiza market, Barocco Nicolau is one of the city me's most cheerful and characteristic bars. It is one of the popular meeting points for locals and travelers for late afternoon chats spent with cocktail art and quality music."
    },
    "Can Moreta": {
        "description": "Eski İbiza evlerinin otantik dokusunu taşıyan bu mekan, adanın en iyi ev yapımı yemeklerini ve yöresel tatlarını sunar. Samimi bir aile işletmesi havasıyla, turist kalabalığından uzaklaşıp İbiza'nın geleneksel mutfak mirasını keşfetmek ve gerçek bir ada öğünü yemek için harika bir tercihtir.",
        "description_en": "Carrying the authentic texture of old Ibiza houses, this venue offers the island's best homemade food and local tastes. With a sincere family-run feel, it's a great choice to move away from tourist crowds, explore Ibiza's traditional culinary heritage, and have a real island meal."
    },
    "Gelato Ibiza": {
        "description": "İbiza kenti limanında yer alan bu şık dondurmacı, doğal malzemelerle hazırlanan ve onlarca farklı aromaya sahip İtalyan usulü dondurmalarıyla ünlüdür. Sıcak yaz akşamlarında liman yürüyüşü yaparken ferahlatıcı bir mola vermek ve kaliteyi tatmak isteyenlerin ilk adresidir.",
        "description_en": "Located at the harbor of Ibiza city, this chic ice cream parlor is famous for its Italian-style ice creams prepared with natural ingredients and having dozens of different flavors. It is the first address for those wanting to take a refreshing break and taste quality while taking a harbor walk on hot summer evenings."
    },
    "Peter Pan Eivissa": {
        "description": "Çocuklu aileler için İbiza'nın en renkli ve eğlenceli duraklarından biri olan Peter Pan, güvenli oyun alanları ve çocuklara özel menüleriyle bilinir. Şehrin merkezine yakın konumuyla, ebeveynler kahvelerini yudumlarken çocukların neşe içinde vakit geçirebileceği samimi ve kaliteli bir mekandır.",
        "description_en": "One of Ibiza's most colorful and fun stops for families with children, Peter Pan is known for its safe play areas and special menus for kids. With its location near the city center, it is a sincere and quality venue where children can spend time in joy while parents sip their coffees."
    },
    "Ushuaïa Ibiza": {
        "description": "Dünyanın en ünlü açık hava kulübü olan Ushuaïa, Playa d'en Bossa sahilinde devasa sahne şovları ve efsanevi DJ performanslarıyla eğlencenin zirvesidir. Lüks ve eğlenceyi havalimanı manzarasıyla birleştiren bu ikonik otel-kulüp, İbiza'yı dünya partilerinin merkezi yapan en önemli duraklardan biridir.",
        "description_en": "The world's most famous open-air club, Ushuaïa is the pinnacle of entertainment on the Playa d'en Bossa coast with giant stage shows and legendary DJ performances. This iconic hotel-club combining luxury and fun with airport views is one of the most important stops making Ibiza the center of world parties."
    },
    "Lolas Club": {
        "description": "İbiza kenti dar sokaklarında gizlenmiş bu şık ve egzotik gece kulübü, kentin bohem gece hayatına modern bir soluk getiriyor. Etkileyici dekorasyonu ve seçkin müzik mönüsüyle bildiğimiz mekan, kentin kozmopolit enerjisini daha samimi ve iddialı bir atmosferde yaşamak isteyenlerin favorisidir.",
        "description_en": "Hidden in the narrow streets of Ibiza city, this chic and exotic night club brings a modern breath to the city's bohemian nightlife. Known for its impressive decoration and exclusive music menu, the venue is a favorite for those wanting to experience the city's cosmopolitan energy in a more intimate and ambitious atmosphere."
    },
    "Space Beach Club S.A.": {
        "description": "İbiza gece hayatı tarihinde bir efsane olan bu ünlü isim, adanın en hit elektronik müzik şölenlerine ve sabahın ilk ışıklarına kadar süren partilerine ev sahipliği yapmıştır. Markanın mirası bugün bile adanın eğlence kültürüne yön vermekte ve dans tutkunları için unutulmaz bir sembol olma özelliğini korumaktadır.",
        "description_en": "A legend in Ibiza nightlife history, this famous name has hosted the island's hit electronic music festivals and parties lasting until the first light of morning. The brand's heritage continues to guide the island's entertainment culture today and remains an unforgettable symbol for dance enthusiasts."
    },
    "BCB Tango": {
        "description": "Arjantin mutfağının en seçkin örneklerini İbiza'nın kalbine taşıyan bu restoran, kaliteli et mönüsü ve şık barıyla gurme gezginlerin favorisidir. Modern tasarımı ve loş atmosferiyle kentin merkezinde elit bir akşam yemeği deneyimi sunan mekan, gastronomi ve stilin harika bir birleşimidir.",
        "description_en": "Bringing elite examples of Argentine cuisine to the heart of Ibiza, this restaurant is a favorite for gourmet travelers with its high-quality meat menu and chic bar. Offering an elite dining experience in the city center with its modern design and dim atmosphere, the venue is a wonderful combination of gastronomy and style."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/ibiza.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data.get('highlights', []):
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Ibiza Part 3: Enriched {count} items.")
