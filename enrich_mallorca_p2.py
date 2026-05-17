#!/usr/bin/env python3
import json

updates = {
    "ChIJEQZo3U-SlxIRGIlk5-EXNjQ": {
        "description": "Palma'nın kalbinde yer alan bu şık butik otel, ünlü Cappuccino markasının zarafetini ve Akdeniz yaşam tarzını en üst seviyede sunuyor. Tarihi bir binanın modern sanatla bütünleştiği tesis, katedral manzaralı terası ve sofistike kafesiyle kentin en prestijli konaklama noktalarından biridir.",
        "description_en": "Located in the heart of Palma, this chic boutique hotel offers the elegance of the famous Cappuccino brand and the Mediterranean lifestyle at the highest level. Integrating a historic building with modern art, the facility is one of the city me's most prestigious accommodation points with its cathedral-view terrace and sophisticated cafe."
    },
    "ChIJoegB1USSlxIRY4l-EKhDs9c": {
        "description": "Tarihi bir sarayın içinde, modern lüksün ve konforun zirvesini sunan Can Alomar, Palma'nın en şık alışveriş caddesi üzerinde yer alıyor. Geniş terasları, şık spa alanı ve kişiye özel hizmet anlayışıyla, adanın kozmopolit ruhunu ve asaletini hissetmek isteyen gezginler için muazzam bir seçimdir.",
        "description_en": "Offering the pinnacle of modern luxury and comfort inside a historical palace, Can Alomar is located on Palma's most stylish shopping street. With its wide terraces, chic spa area, and personalized service concept, it's a magnificent choice for travelers wanting to feel the island's cosmopolitan spirit and nobility."
    },
    "ChIJA2USlX2PlxIRJCOeKj1cgUs": {
        "description": "Portals Nous'un seçkin atmosferinde yer alan sadece yetişkinlere özel bu otel, modern tasarımı ve sakin havuz alanıyla huzurlu bir vaha sunuyor. Akdeniz'in masmavi sularına ve marinaya olan yakınlığıyla bildiğimiz tesis, adanın lüks sahil yaşamını deneyimlemek isteyen çiftler ve modern gezginler için idealdir.",
        "description_en": "This adults-only hotel located in the exclusive atmosphere of Portals Nous offers a peaceful oasis with its modern design and quiet pool area. Known for its proximity to the Mediterranean's deep blue waters and the marina, it is ideal for couples and modern travelers wanting to experience the island's luxury coastal life."
    },
    "ChIJy0sW2VqSlxIRVYiQOc_wKYg": {
        "description": "Palma'nın dar sokaklarından birine gizlenmiş olan El Pilón, geleneksel İspanyol tatlarını ve taze deniz ürünlerini otantik bir atmosferde sunuyor. Mağarayı andıran taş duvarları ve güler yüzlü hizmetiyle, kentin gastronomi mirasını en samimi haliyle keşfetmek isteyenlerin yıllardır vazgeçilmez duraklarından biridir.",
        "description_en": "Hidden in one of Palma's narrow streets, El Pilón offers traditional Spanish flavors and fresh seafood in an authentic atmosphere. With its cave-like stone walls and friendly service, it has been one of the indispensable stops for years for those wanting to explore the city me's gastronomic heritage in its most sincere form."
    },
    "ChIJfz378k6SlxIRQgnPvhdBurw": {
        "description": "Eski kentin tarihi surları içerisinde yer alan bu butik hotel ve spa, antik taş yapısı ve modern iç tasarımıyla büyüleyici bir zıtlık yaratıyor. Katedral manzaralı teras barı ve huzur veren spa olanaklarıyla, kentin tarihi dokusunda kendinizi özel hissedeceğiniz romantik ve rafine bir dinlenme noktasıdır.",
        "description_en": "Located within the ancient walls of the old town, this boutique hotel and spa creates a fascinating contrast with its ancient stone structure and modern interior design. With its terrace bar featuring cathedral views and peaceful spa facilities, it is a romantic and refined rest point where you will feel special in the city's historical texture."
    },
    "ChIJa286tk-SlxIR2Cbko3a4S0E": {
        "description": "Palma'nın hareketli meydanlarından birinde yer alan Cafè Plaça, nostaljik atmosferi ve sokağa taşan masalarıyla kentin nabzını tutan keyifli bir duraktır. Yerel halkın ve gezginlerin buluşma noktası olan bu kafe, sabah kahvesi veya akşamüstü tapasları için adanın en samimi ve fotojenik adreslerinden biridir.",
        "description_en": "Located in one of Palma's vibrant squares, Cafè Plaça is a pleasant stop catching the city's pulse with its nostalgic atmosphere and tables spilling onto the street. A meeting point for locals and travelers, this cafe is one of the island's most sincere and photogenic addresses for morning coffee or afternoon tapas."
    },
    "ChIJ149YX12SlxIRpg_GxamF4CE": {
        "description": "Santa Catalina'nın karakteristik mahalle dokusu içinde yer alan bu butik pastane, geleneksel Fransız tekniklerini Mallorca'nın yerel malzemeleriyle birleştiriyor. Taze pişmiş kruvasanları ve sanatsal tatlılarıyla kentin gastronomi dünyasına modern bir soluk getiren, her köşesi ilham dolu samimi bir lezzet durağıdır.",
        "description_en": "Located within the characteristic neighborhood texture of Santa Catalina, this boutique bakery combines traditional French techniques with Mallorca's local ingredients. It's a sincere flavor stop full of inspiration at every corner, bringing a modern breath to the city's gastronomic world with its freshly baked croissants and artistic desserts."
    },
    "ChIJz6NGWUOSlxIRdtjfhGXaR3c": {
        "description": "Palma'nın bohem ve sanatsal ruhunu yansıtan Bar Cafe Coto, renkli duvarları ve antika objeleriyle kentin en karakteristik mekanlarından biridir. Eski kentin tarihi sokaklarında ferahlatıcı bir mola vermek, taze kokteyllerin tadına bakmak ve kentin kozmopolit enerjisini solumak için harika ve havadar bir tercihtir.",
        "description_en": "Reflecting Palma's bohemian and artistic spirit, Bar Cafe Coto is one of the city's most characteristic venues with its colorful walls and antique objects. It's a grand and airy choice for taking a refreshing break in the old town's historical streets, tasting fresh cocktails, and breathing in the city's cosmopolitan energy."
    },
    "ChIJs2r9gVuSlxIRiuG8823VKcY": {
        "description": "1700'lerden beri hizmet veren Can Joan de s'Aigo, Mallorca'nın dondurma ve sıcak çikolata geleneğinin en meşhur temsilcisidir. Antik seramikleri ve nostaljik avizeleriyle zamanın donduğu bu efsanevi pastane, meşhur 'Ensaimada' ve ev yapımı badem dondurmasıyla adanın tatlı mirasını keşfetmek için vazgeçilmezdir.",
        "description_en": "Serving since the 1700s, Can Joan de s'Aigo is the most famous representative of Mallorca's ice cream and hot chocolate traditions. This legendary bakery where time stands still with ancient ceramics and nostalgic chandeliers is indispensable for exploring the island's sweet heritage with its famous 'Ensaimada' and homemade almond ice cream."
    },
    "ChIJYXIphFeSlxIRdTeLTXpq7ZI": {
        "description": "Palma'nın tarihi merkezinde yer alan bu şirin mekan, meşhur İspanyol jambonu 'Jamon Iberico'nun en kaliteli örneklerini taze kahveyle buluşturuyor. Samimi tasarımı ve uzman kesim teknikleriyle adanın en lezzetli gurme duraklarından biri olan bu mini bar, hızlı ve kaliteli bir yerel atıştırmalık deneyimi arayanlar için idealdir.",
        "description_en": "Located in Palma's historical center, this charming venue brings together high-quality examples of the famous Spanish ham 'Jamon Iberico' with fresh coffee. Being one of the most delicious gourmet stops on the island with its sincere design and expert slicing techniques, this mini bar is ideal for those seeking a fast and high-quality local snack experience."
    },
    "ChIJdSOrC5WNlxIR2BIcUl9bmMg": {
        "description": "Mallorca'nın simgesi haline gelen Ensaimada tatlısının en eski ve en ünlü fırınlarından biri olan Forn del Santo Cristo, geleneksel tarifleri nesillerdir yaşatıyor. Şehrin dar sokaklarından birinde yer alan bu ikonik fırın, el yapımı pastaları ve otantik atmosferiyle kentin lezzet hafızasının paha biçilemez bir parçasıdır.",
        "description_en": "One of the oldest and most famous bakeries of the Ensaimada pastry which has become a symbol of Mallorca, Forn del Santo Cristo has been keeping traditional recipes alive for generations. Located in one of the city's narrow streets, this iconic bakery is a priceless part of the city's flavor memory with its handmade pastries and authentic atmosphere."
    },
    "ChIJQ1yZF6-TlxIRpTq_KuF_OGs": {
        "description": "Palma'nın modern ve hareketli yüzünü temsil eden bu sosyal eğlence alanı, spor ve oyun tutkunları için kentin en dinamik noktalarından biridir. Şık tasarımı ve enerjik atmosferiyle kentin yerel ritmini hissettiren bu merkez, arkadaş grupları için neşeli ve kaliteli bir akşam geçirme alternatifi sunuyor.",
        "description_en": "Representing Palma's modern and vibrant face, this social entertainment area is one of the city's most dynamic points for sports and game enthusiasts. Making you feel the city's local rhythm with its chic design and energetic atmosphere, this center offers a joyful and high-quality evening alternative for groups of friends."
    },
    "ChIJ4wxyLVCSlxIR4jUA8RLG6K0": {
        "description": "Palma'nın tarihi merkezinde yer alan Bar Plata, klasik İspanyol meyhanesi ruhunu modern ve şık bir dekorasyonla birleştiriyor. Yerel şarapları ve kaliteli tapas mönüsüyle kentin her daim canlı olan sosyal yaşamının nabzını tutan bu mekan, iş çıkışı buluşmaları ve keyifli sohbetler için kentin en popüler duraklarındandır.",
        "description_en": "Located in Palma's historical center, Bar Plata combines the classic Spanish tavern spirit with modern and chic decoration. Catching the pulse of the city me's always vibrant social life with its local wines and high-quality tapas menu, this venue is one of the city's most popular stops for after-work gatherings and pleasant chats."
    },
    "ChIJT19NmlSSlxIRErYBkYVtVCQ": {
        "description": "İsminin hakkını veren Barok detayları ve nostaljik atmosferiyle bu kafe, kentin sanatsal geçmişine bir saygı duruşu niteliğindedir. Palma'nın dar sokaklarında gizlenmiş bu karakteristik yapı, taze kahvesi ve huzurlu sessizliğiyle hem çalışmak hem de kentin mistik havasını solumak isteyenlerin favori sığınağıdır.",
        "description_en": "With Baroque details living up to its name and a nostalgic atmosphere, this cafe serves as a tribute to the city's artistic past. Hidden in Palma's narrow streets, this characteristic structure is the favorite sanctuary for those wanting to both work and breathe in the city's mystical air with its fresh coffee and peaceful silence."
    },
    "ChIJ9_sQiAuTlxIRRXUPnWKl4DI": {
        "description": "Palma istasyonu yakınlarında yer alan La Parada, kentin kozmopolit enerjisini şık bir gastronomi deneyimiyle buluşturuyor. Modern tasarımı ve dünya mutfağından seçkin örnekler sunan mönüsüyle bildiğimiz bu tesis, kentin hareketli ulaşım ağının ortasında kaliteli ve ferah bir gastronomi durağı olarak hizmet veriyor.",
        "description_en": "Located near Palma station, La Parada brings the city's cosmopolitan energy together with a chic gastronomic experience. Known for its modern design and menu offering exclusive examples from international cuisine, this facility serves as a high-quality and spacious gastronomic stop in the middle of the city's vibrant transport network."
    },
    "ChIJmdMpK1CSlxIRW8qv_4wSWLA": {
        "description": "El yapımı pastaları ve sanatsal dokunuşları olan tatlılarıyla Palma'nın en şık pastanelerinden biri olan Mariola’s, tatlı tutkunları için eşsiz bir vaha niteliğindedir. Her biri usta ellerden çıkan ve adanın renklerini yansıtan bu eserler, kentin yerel sanat ruhunu lezzetle birleştirerek ziyaretçilere unutulmaz bir deneyim sunuyor.",
        "description_en": "One of Palma's most stylish bakeries with handmade cakes and sweets having artistic touches, Mariola’s is a unique oasis for dessert enthusiasts. These works, each emerging from master hands and reflecting the island's colors, offer an unforgettable experience by combining the city's local artistic spirit with flavor."
    },
    "ChIJ4-PvdYiWlxIRV6Oa2P_cKsc": {
        "description": "Playa de Palma sahilinde modern konforu ve enerjik yaz atmosferini bir arada sunan bu otel, denize olan yakınlığı ve şık havuz alanıyla dikkat çekiyor. Güneşin ve Akdeniz melteminin tadını çıkarırken kentin sosyal olanaklarına kolayca ulaşmak isteyen gezginler için ferah ve kaliteli bir konaklama adresidir.",
        "description_en": "Offering modern comfort and an energetic summer atmosphere together on the Playa de Palma coast, this hotel stands out with its proximity to the sea and chic pool area. It's a spacious and high-quality accommodation address for travelers wanting to easily reach city social facilities while enjoying the sun and Mediterranean breeze."
    },
    "ChIJ4a3aTKaWlxIRswFN7GZDDhk": {
        "description": "Palma körfezine hakim bir yarımada üzerinde yer alan Purobeach, adanın en ikonik ve prestijli plaj kulüplerinden biridir. Minimalist beyaz dekorasyonu, muazzam havuzu ve dünya çapındaki DJ performanslarıyla İbiza atmosferini Mallorca'ya taşıyan mekan, lüks ve eğlenceyi en rafine haliyle sunuyor.",
        "description_en": "Located on a peninsula dominating the Palma bay, Purobeach is one of the island's most iconic and prestigious beach clubs. Bringing the Ibiza atmosphere to Mallorca with its minimalist white decoration, magnificent pool, and world-class DJ performances, the venue offers luxury and fun in its most refined form."
    },
    "ChIJm-bKyUSSlxIRAc3vwHrCeb0": {
        "description": "Eski bir malikanede yer alan ve dünyanın en ünlü barlarından biri kabul edilen Abaco, taze meyveler, çiçekler ve klasik müzikle bezeli masalsı atmosferiyle tanınır. İçeri adım attığınızda zamanın durduğu bu mistik mekan, heybetli avlusu ve tarihi dekoruyla kentin en büyüleyici ve romantik keşif duraklarından biridir.",
        "description_en": "Located in an old manor and considered one of the world's most famous bars, Abaco is known for its fairytale atmosphere adorned with fresh fruits, flowers, and classical music. This mystical venue where time stands still as you step inside is one of the city's most charming and romantic discovery stops with its grand courtyard and historical decor."
    },
    "ChIJNTC2BlGSlxIRh7YQEZ_poSo": {
        "description": "Palma'nın en havalı mahallelerinden birinde yer alan Mari lin, bohem şıklığı ve modern gastronomiyi birleştiren seçkin bir kafe-loungetır. Gün boyu süren ferah atmosferi, şık sunumları ve adanın yaratıcı kitlesini bir araya getiren sosyal dokusuyla kentin modern yaşam tarzını solumak için mükemmel bir duraktır.",
        "description_en": "Located in one of Palma's coolest neighborhoods, Mari lin is an exclusive cafe-lounge combining bohemian chic and modern gastronomy. With its spacious atmosphere lasting all day, stylish presentations, and social texture bringing together the island's creative crowd, it is a perfect stop to breathe in the city's modern lifestyle."
    },
    "ChIJmSc8EHKSlxIRrza9gS5ISXY": {
        "description": "Palma gece hayatının en iddialı ve şık adreslerinden biri olan Zar Society, etkileyici dijital tasarımları ve elit atmosferiyle öne çıkıyor. Dünyaca ünlü DJ'lerin ve özel şovların sahne aldığı bu kulüp, kentin kozmopolit enerjisini en yüksek seviyede deneyimlemek isteyen seçkin bir kitleyi ağırlıyor.",
        "description_en": "One of Palma's most ambitious and stylish nightlife addresses, Zar Society stands out with its impressive digital designs and elite atmosphere. Hosting world-famous DJs and special shows, this club welcomes an elite crowd wanting to experience the city's cosmopolitan energy at its highest level."
    },
    "ChIJL-I8bGiSlxIRSmsYYdjVObw": {
        "description": "Santa Catalina'nın kalbinde yer alan Sabotage, endüstriyel şıklığı ve alternatif müzik kültürüyle kentin en neşeli barlarından biridir. Kaliteli kokteylleri ve yerel halkla gezginleri buluşturan samimi atmosferiyle, kentin özgün gece hayatını ve bohem ruhunu keşfetmek için harika bir duraktır.",
        "description_en": "Located in the heart of Santa Catalina, Sabotage is one of the city's most cheerful bars with industrial elegance and alternative music culture. With high-quality cocktails and a sincere atmosphere bringing together locals and travelers, it's a great stop for exploring the city me's authentic nightlife and bohemian spirit."
    },
    "ChIJbwO1AVaSlxIRP3Ra41LMG4U": {
        "description": "Palma'nın merkezinde yer alan bu neşeli ve renkli mekan, kentin kapsayıcı ve enerjik yüzünü temsil ediyor. Modern tasarımı ve kaliteli müzik seçkisiyle bildiğimiz bar, özellikle akşamüstü buluşmaları ve gecenin ilk ışıklarına kadar süren kaliteli sohbetler için adanın en samimi ve havadar duraklarından biridir.",
        "description_en": "Located in Palma's center, this cheerful and colorful venue represents the city's inclusive and energetic face. Known for its modern design and high-quality music selection, the bar is one of the island's most sincere and airy stops especially for late afternoon gatherings and quality chats lasting until the first light of night."
    },
    "ChIJVbFWM2-SlxIRnFh3yK106qc": {
        "description": "İngiliz pub kültürünü Akdeniz güneşiyle buluşturan Three Lions, neşeli atmosferi ve geniş bira seçkisiyle kentin sosyal yaşamının önemli bir parçasıdır. Özellikle canlı spor yayınları ve samimi bar sohbetleri için tercih edilen mekan, kentin kozmopolit dokusunda kendinizi evinizde hissedeceğiniz keyifli bir duraktır.",
        "description_en": "Bringing English pub culture together with the Mediterranean sun, Three Lions is an important part of the city's social life with its cheerful atmosphere and wide beer selection. Favored especially for live sports broadcasts and sincere bar chats, the venue is a pleasant stop where you'll feel at home in the city's cosmopolitan texture."
    },
    "ChIJnR4733GSlxIRapBFlZuE-H0": {
        "description": "Palma'nın ağaçlıklı ve ferah ana caddelerinden biri üzerinde yer alan bu durak, kentin gündelik ritmini ve alışveriş kültürünü solumak için idealdir. Çevresindeki tarihi binalar ve şık vitrinlerle kentin klasik zarafetini yansıtan bölge, hem yürüyüş yapmak hem de yerel kafelerde mola vermek için havadar bir seçenektir.",
        "description_en": "Located on one of Palma's tree-lined and spacious main streets, this stop is ideal for breathing in the city's daily rhythm and shopping culture. Reflecting the city me's classic elegance with surrounding historical buildings and stylish shop windows, the area is an airy option for both walking and taking breaks at local cafes."
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

print(f"✅ Mallorca Part 2: Enriched {count} items.")
