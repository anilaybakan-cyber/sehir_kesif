#!/usr/bin/env python3
import json

updates = {
    "ChIJA1Fe26DWlxIRN0Vzy9Fe7Co": {
        "description": "Mallorca'nın kuzeyindeki bu şirin kasaba, dar taş sokakları, tarihi meydanı ve Pön dönemi kalıntılarıyla adanın en fotonejik yerlerinden biridir. Roman köprüsü ve asırlık kalesiyle kentin zengin geçmişini yansıtan Pollença, hem yerel kültürü solumak hem de huzurlu bir akşam geçirmek için mükemmeldir.",
        "description_en": "This charming town in northern Mallorca is one of the island's most photogenic places with its narrow stone streets, historical square, and Punic era remains. Reflecting the city's rich past with its Roman bridge and century-old castle, Pollença is perfect for both soaking in local culture or having a peaceful evening."
    },
    "ChIJ0aPV-5yWlxIRM0tN163W2is": {
        "description": "Avrupa'nın en büyük köpekbalığı tanklarından birine sahip olan Palma Aquarium, deniz altı dünyasının tüm gizemini ziyaretçilerine açıyor. Mercan resifleri, tropikal balıklar ve devasa kumsallara yakın konumuyla aileler için harika bir durak olan bu akvaryum, deniz ekosistemini koruma bilincini de aşılayan eğitici bir merkezdir.",
        "description_en": "Featuring one of Europe's largest shark tanks, Palma Aquarium opens all mysteries of the underwater world to its visitors. A great stop for families with coral reefs, tropical fish, and its location near massive beaches, this aquarium is an educational center that also instills awareness of preserving marine ecosystems."
    },
    "ChIJJffYU5iOlxIRllj1RLrewsU": {
        "description": "Mallorca'nın en popüler eğlence parklarından biri olan Marineland, büyüleyici yunus ve deniz aslanı şovlarıyla tanınır. Çocuklu aileler için eğlence dolu bir gün vadeden parkta, egzotik kuşlardan sürüngenlere kadar birçok canlıyı yakından görme ve deniz yaşamının eğlenceli yanını keşfetme şansı bulabilirsiniz.",
        "description_en": "One of Mallorca's most popular entertainment parks, Marineland is known for its fascinating dolphin and sea lion shows. In the park promising a fun-filled day for families with children, you can find the chance to see many creatures from exotic birds to reptiles and explore the fun side of marine life."
    },
    "ChIJpflxoFaSlxIRTW9HTELbRic": {
        "description": "Tarihi Sóller Tren İstasyonu, Palma ve Sóller arasında bir asırdır süzülen ikonik ahşap trenin başlangıç noktasıdır. Nostaljik atmosferi ve çevresindeki şık kafeleriyle bu istasyon, kentin modern yüzünden ayrılıp adanın dik yamaçlarına ve zeytin bahçelerine uzanan masalsı bir yolculuğun kapısıdır.",
        "description_en": "The historic Sóller Train Station is the starting point of the iconic wooden train that has been gliding between Palma and Sóller for a century. With its nostalgic atmosphere and surrounding chic cafes, this station is the gateway to a fairytale journey stretching from the city's modern face to the island's steep slopes and olive groves."
    },
    "ChIJWRWcWlGSlxIRDoi8jn_f9sw": {
        "description": "Mallorca Müzesi, kentin Gotik mahallesindeki görkemli bir malikanede yer alır ve adanın tarihöncesi dönemden günümüze kadar uzanan zengin mirasını sergiler. Arkeolojik buluntular, klasik sanat eserleri ve geleneksel el sanatlarıyla kentin kimliğini ve kültürel derinliğini keşfetmek isteyenler için paha biçilemez bir hazinedir.",
        "description_en": "The Museum of Mallorca is located in a grand manor in the city's Gothic quarter and exhibits the island's rich heritage stretching from prehistoric periods to the present. It is a priceless treasure for those wanting to explore the city me's identity and cultural depth with archaeological finds, classical artworks, and traditional crafts."
    },
    "ChIJYXZ5tk-SlxIR7EHzc09Lx90": {
        "description": "Eski kentin dar sokakları arasında saklanmış karakteristik bir yapı olan Can Amorós, Mallorca'nın aristokratik konut mimarisinin zarif bir örneğidir. Tarihi avlusu ve detaylı işlenmiş cephesiyle kentin sessiz tanıklığını yapan bu bina, geçmişin asaletini ve kentin otantik dokusunu solumak için ideal bir duraktır.",
        "description_en": "A characteristic structure hidden among the narrow streets of the old town, Can Amorós is an elegant example of Mallorca's aristocratic residential architecture. Watching the city silently with its historical courtyard and detailed facade, this building is an ideal stop for breathing in the past's nobility and the city's authentic texture."
    },
    "ChIJbffZvU-SlxIRxOphTumLpnc": {
        "description": "Mallorca'nın kırsal mirasını ve zeytinyağı üretim kültürünü temsil eden bu tarihi malikane, kentin dik yamaçlarındaki tarım geçmişini yansıtır. Geleneksel yapısı ve huzur veren bahçeleriyle İspanyol aristokrasisinin yerel yaşamla nasıl bütünleştiğini gösteren kentin en samimi ve fotojenik miras noktalarından biridir.",
        "description_en": "Representing Mallorca's rural heritage and olive oil production culture, this historic manor reflects the agricultural past on the city's steep slopes. With its traditional structure and peaceful gardens, it is one of the city's most sincere and photogenic heritage spots showing how Spanish aristocracy integrated with local life."
    },
    "ChIJa42YNU6SlxIRE5J0CLPCi9g": {
        "description": "Palma'nın merkezindeki tarihi evlerden biri olan Can March, kentin mimari değişim sürecini yansıtan zarif dekoratif detaylarıyla bilinir. Yüzyıllara meydan okuyan taş duvarları ve nostaljik atmosferiyle bu bölge, kentin sosyal tarihini ve eski şehir yaşamının huzurunu hissetmek isteyenler için saklı bir köşedir.",
        "description_en": "One of the historic houses in Palma's center, Can March is known for its elegant decorative details reflecting the city's architectural transformation process. With stone walls defying centuries and a nostalgic atmosphere, this area is a hidden corner for those wanting to feel the city's social history and the peace of old town life."
    },
    "ChIJZ0N_pU-SlxIRksaeC7Ryzwc": {
        "description": "Mallorca'nın en prestijli malikanelerinden biri olan Can Oleza, büyüleyici 'Mallorcan' tarzı avlusu ve heybetli mermer sütunlarıyla tanınır. İtalyan Rönesansı etkilerini taşıyan mimarisiyle kentin zengin ticaret geçmişini ve asaletini simgeleyen bu yapı, eski kentin en çok hayranlık uyandıran tarihi simgelerinden biridir.",
        "description_en": "One of Mallorca's most prestigious manors, Can Oleza is known for its fascinating 'Mallorcan' style courtyard and imposing marble columns. Representing the city me's rich trade history and nobility with its Italian Renaissance-influenced architecture, this structure is one of the most admired historical symbols of the old town."
    },
    "ChIJRQvciU-SlxIRYuZ7zWyvRno": {
        "description": "Kentin labirent gibi sokakları içinde yer alan Can Alemany, geleneksel ile modernin harika bir birleşimidir. Restore edilmiş tarihi dokusu ve samimi iç avlusuyla, kentin kozmopolit havasından uzaklaşıp adanın asude geçmişine tanıklık edebileceğiniz, mimari detaylarıyla büyüleyen huzurlu bir duraktır.",
        "description_en": "Located within the city's labyrinthine streets, Can Alemany is a wonderful combination of traditional and modern. With its restored historical texture and intimate inner courtyard, it's a peaceful stop fascinating with architectural details where you can witness the island's serene past away from the city's cosmopolitan air."
    },
    "ChIJlzT0QVCSlxIRhpU6VPrT1nQ": {
        "description": "Modernist kentin kalbinde yer alan CaixaForum Palma, görkemli bir otelin sanat merkezine dönüştürülmesiyle hayat bulmuştur. Modern sanatın öncü sergilerine, konserlere ve kültürel etkinliklere ev sahipliği yapan bu ikonik bina, şık tasarımıyla kentin yaratıcı ruhunu ve estetik zenginliğini temsil eder.",
        "description_en": "Located in the heart of the modernist city, CaixaForum Palma was brought to life by transforming a grand hotel into an art center. Hosting pioneering modern art exhibitions, concerts, and cultural events, this iconic building represents the city me's creative spirit and aesthetic richness with its chic design."
    },
    "ChIJx3sqB3eOlxIRzY_BRZ-4IoQ": {
        "description": "Kentin hemen dışında, turkuaz suların sarp kayalıklarla buluştuğu Roc Illetas plajı, hem güneşin hem de sükunetin tadını çıkarmak isteyenler için idealdir. Konforlu locaları ve masmavi deniz manzarasıyla bildiğimiz bu bölge, Akdeniz meltemi eşliğinde huzur dolu bir plaj günü vaat ediyor.",
        "description_en": "Just outside the city, where turquoise waters meet steep cliffs, Roc Illetas beach is ideal for those wanting to enjoy both sun and serenity. Known for its comfortable booths and deep blue sea views, this area promises a peaceful beach day accompanied by the Mediterranean breeze."
    },
    "ChIJf3wSntiNlxIRo8CCeZSw4Ts": {
        "description": "Dikey mimarisi ve denize basamaklarla inen bahçeleriyle ünlü olan bu lüks otel, Mallorca konukseverliğinin en şık adreslerinden biridir. Şehir kalabalığından korunmuş saklı koyu ve kaliteli spa hizmetiyle, hem dinlenmek hem de adanın eşsiz kıyılarını keşfetmek isteyen seçkin gezginlerin favorisidir.",
        "description_en": "Famous for its vertical architecture and gardens descending to the sea in steps, this luxury hotel is one of the most elegant addresses for Mallorca hospitality. With its hidden bay protected from city crowds and high-quality spa service, it is a favorite for elite travelers wanting to both relax and explore the island's unique shores."
    },
    "ChIJJwHxZ4OOlxIRW-BAHEzC04E": {
        "description": "Portals Nous bölgesinde yer alan bu prestijli tesis, modern konforu Akdeniz güneşiyle buluşturuyor. Şık havuz alanı ve kentin en popüler yat limanlarına olan yakınlığıyla dikkat çeken otel, adanın kozmopolit lüksünü ve neşeli sahil yaşamını doyasıya hissettiren kaliteli bir konaklama durağıdır.",
        "description_en": "Located in the Portals Nous area, this prestigious facility brings modern comfort together with the Mediterranean sun. Standing out with its chic pool area and proximity to the city's most popular yacht harbors, the hotel is a high-quality accommodation stop that makes you fully feel the island's cosmopolitan luxury and joyous seaside life."
    },
    "ChIJRXqd3USSlxIRt5DCbb2ob40": {
        "description": "Palma'nın merkezindeki tarihi bir binada hizmet veren Petit Palace Hotel Tres, endüstriyel şıklığı ve modern tasarımı birleştiriyor. Katedral manzaralı terası ve her biri sanatsal bir dokunuş taşıyan odalarıyla, kentin kalbinde hem stil hem de huzur arayan modern gezginlerin adresi haline gelmiştir.",
        "description_en": "Operating in a historic building in the center of Palma, Petit Palace Hotel Tres combines industrial elegance and modern design. With its terrace featuring cathedral views and rooms each carrying an artistic touch, it has become the address for modern travelers seeking both style and peace in the heart of the city."
    },
    "ChIJ_fP5iQmSlxIRpckX1ae_f4Y": {
        "description": "Körfeze tepeden bakan görkemli konumuyla Valparaiso Palace, adanın en büyük ve prestijli spa-resort merkezlerinden biridir. Yemyeşil bahçeleri, panaromik şehir manzarası ve yüksek standartlardaki konforuyla, kendinizi Mallorca'nın asaletine bırakacağınız elit bir tatil rotasıdır.",
        "description_en": "With its grand position overlooking the bay, Valparaiso Palace is one of the island's largest and most prestigious spa-resort centers. Featuring lush gardens, panoramic city views, and high-standard comfort, it is an elite holiday route where you'll surrender yourself to Mallorca's nobility."
    },
    "ChIJ030lTNyNlxIRkoTe_M1QLsU": {
        "description": "Denizin hemen kıyısında, tarihi bir malikanenin modern zarafetle bütünleştiği bu otel, kentin en özel ve sessiz konaklama noktalarından biridir. Ünlü deniz kenarı terasındaki şık kahvaltıları ve gün boyu süren ferah atmosferiyle, Akdeniz güneşini en rafine haliyle kucaklayan prestijli bir adrestir.",
        "description_en": "Situated right at the seaside, this hotel where a historic manor integrates with modern elegance is one of the city me's most exclusive and quiet accommodation points. With its chic breakfasts on the famous seaside terrace and a refreshed atmosphere lasting all day, it is a prestigious address embracing the Mediterranean sun in its most refined form."
    },
    "ChIJzVKOAU6SlxIR1Gq7Vsd1bGU": {
        "description": "Eski bir Gotik malikanenin aslına sadık kalınarak restore edilmesiyle hayata geçen Posada Terra Santa, tarihin fısıltılarını modern lüksle birleştiriyor. Sessiz avlusu, antik taş duvarları ve kentin katedraline olan yakınlığıyla, kendinizi tarihin korunaklı kucağında hissedeceğiniz romantik bir sığınaktır.",
        "description_en": "Brought to life by restoring an old Gothic manor staying faithful to its original, Posada Terra Santa combines the whispers of history with modern luxury. With its quiet courtyard, ancient stone walls, and proximity to the city's cathedral, it is a romantic sanctuary where you'll feel in the protected lap of history."
    },
    "ChIJJUJc_WeSlxIR8TjWsA9o7Kw": {
        "description": "Palma'nın ikonik Art Nouveau binalarından birinde yer alan Hotel Hostal Cuba, kentin liman kültürünü ve modern şıklığını temsil eder. Ünlü çatı terasındaki eşsiz gün batımı manzarası ve kaliteli kokteylleriyle, geceye hareketli bir başlangıç yapmak isteyen seçkin kitlenin favori buluşma noktasıdır.",
        "description_en": "Located in one of Palma's iconic Art Nouveau buildings, Hotel Hostal Cuba represents the city's harbor culture and modern elegance. With its unique sunset view on the famous roof terrace and quality cocktails, it is the favorite meeting point for the elite crowd wanting a lively start to the night."
    },
    "ChIJx9-bd32OlxIRpvyZeGOMoZc": {
        "description": "Sarp kayaların üzerine kurulu masmavi bir koyda yer alan Bendinat, klasik İspanyol stilini ve deniz sefasını en samimi haliyle sunuyor. Adını çevresindeki antik surlardan alan bu tesis, hem doğa yürüyüşleri hem de berrak sularda serinlemek isteyenler için kentin en huzurlu sahil duraklarından biridir.",
        "description_en": "Located in a deep blue bay built on steep rocks, Bendinat offers classic Spanish style and seaside delight in its most sincere form. Taking its name from the surrounding ancient walls, this facility is one of the city's most peaceful coastal stops for those wanting both nature walks and to cool off in clear waters."
    },
    "ChIJB5NZmWOWlxIRHYVyowelens": {
        "description": "Playa de Palma'nın enerjik atmosferinde yer alan bu modern otel, sadece yetişkinlere özel konseptiyle huzur ve eğlenceyi bir arada sunuyor. Şık havuz alanı ve denize olan yakınlığıyla dikkat çeken tesis, adanın neşeli yaz ruhunu kaliteli bir hizmet anlayışıyla keşfetmek isteyenlerin adresidir.",
        "description_en": "Located in the energetic atmosphere of Playa de Palma, this modern hotel offers peace and fun together with its adults-only concept. Standing out with its chic pool area and proximity to the sea, the facility is the address for those wanting to explore the island's joyful summer spirit with a high-quality service concept."
    },
    "ChIJjcao54eWlxIRxW_PkmeY-kI": {
        "description": "Palma havalimanına ve popüler plajlara yakın konumuyla bu tesis, modern konforu pratik bir yaklaşımla sunuyor. Ferah odaları ve geniş sosyal alanlarıyla kentin kozmopolit kalabalığından kaçıp kaliteli bir dinlenme molası vermek isteyen gezginlerin favori bölgesel durakları arasındadır.",
        "description_en": "With its location near Palma airport and popular beaches, this facility offers modern comfort with a practical approach. With its spacious rooms and wide social areas, it is among the favorite regional stops for travelers wanting to escape the city's cosmopolitan crowds and have a quality rest break."
    },
    "ChIJ3-nnOGKWlxIR--EVaejOzcw": {
        "description": "Playa de Palma'nın merkezinde taze ve genç bir enerji sunan bu otel, minimal tasarımı ve sosyal odaklı konseptiyle bilinir. Güneşin ve denizin tadını çıkarırken bir yandan da kentin hareketli gece hayatına yakın olmak isteyen gezginler için havadar ve kaliteli bir konaklama alternatifidir.",
        "description_en": "Offering fresh and young energy in the center of Playa de Palma, this hotel is known for its minimal design and social-oriented concept. It's an airy and quality accommodation alternative for travelers wanting to enjoy the sun and sea while also being close to the city's vibrant nightlife."
    },
    "ChIJw-8BdmKWlxIR0Bqw4gMtD_Q": {
        "description": "Dünyaca ünlü Iberostar kalitesini Akdeniz'in en uzun plajında sunan bu tesis, lüks ve konforun buluşma noktasıdır. Geniş gurme mönüleri, şık spa olanakları ve denize sıfır konumuyla, adanın kozmopolit lüksünü ve yaz neşesini en üst seviyede hissetmek isteyenler için muazzam bir seçimdir.",
        "description_en": "Offering world-famous Iberostar quality on the Mediterranean's longest beach, this facility is the meeting point of luxury and comfort. With its wide gourmet menus, chic spa facilities, and seafront location, it is a magnificent choice for those wanting to feel the island's cosmopolitan luxury and summer joy at the highest level."
    },
    "ChIJe1rp-FOSlxIRIA-Jj1Pzacc": {
        "description": "Eski kentin tarihi dokusunda yer alan bu şık mekan, Mallorca'nın yerel lezzetlerini ev yapımı samimiyetiyle sunuyor. Adanın en taze ürünleriyle hazırlanan mönüsü ve bitki-baharat kokulu atmosferiyle, kentin gastronomi mirasını keşfetmek ve sakin bir akşam yemeği yemek için kentin en doğal adreslerinden biridir.",
        "description_en": "Located in the historical texture of the old town, this chic venue offers Mallorca's local flavors with homemade sincerity. With its menu prepared with the island's freshest products and an atmosphere smelling of herbs and spices, it is one of the city me's most natural addresses for exploring the gastronomic heritage and having a quiet dinner."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/mallorca.json.draft'
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

print(f"✅ Mallorca Part 1: Enriched {count} items.")
