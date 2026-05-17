#!/usr/bin/env python3
import json

updates = {
    "ChIJL7M2CJfUTRMRXgc6ncMVbjA": {
        "description": "Adriyatik'in masmavi sularını özgürce keşfetmek isteyenler için Budva'nın en popüler tekne kiralama servislerinden biridir. Kendi rotanızı çizerek gizli koyları ve Sveti Nikola adasını denizden keşfedebileceğiniz, kentin enerjisini en yüksek seviyede hissettiren havadar bir deniz durağıdır.",
        "description_en": "One of Budva me's most popular boat rental services for those wanting to freely explore the deep blue waters of the Adriatic. It is an airy sea stop making you feel the city me's energy at the highest level, where you can discover hidden coves and Sveti Nikola island from the sea by drawing your own route."
    },
    "ChIJ3Sv1bwDVTRMRYxzhq1EtZEE": {
        "description": "Budva kıyılarında geleneksel bir balıkçı teknesiyle nostaljik bir yolculuğa çıkın. Nenov Brod, kentin sahil silüetine karakter katan samimi atmosferi ve denizle iç içe olan yapısıyla, kenti bir yerel gibi hissetmek isteyen gezginler için havadar ve kaliteli bir deniz rotasıdır.",
        "description_en": "Go on a nostalgic journey along the shores of Budva with a traditional fishing boat. Nenov Brod is an airy and quality sea route for travelers wanting to feel like a local, with its sincere atmosphere adding character to the city's coastal silhouette and its structure intertwined with the sea."
    },
    "ChIJ41oDvhHVTRMR3j1BCYY5zHg": {
        "description": "Eski Şehir surlarının hemen yanındaki bu tarihi rıhtım, Budva'nın denizle olan kopmaz bağının ve deniz ticaretinin merkezidir. Balıkçı tekneleri, lüks yatlar ve kentin taze deniz havasıyla kentsel silüeti tamamlayan bu nokta, kentin neşeli sosyal dokusunu solumak için ideal ve samimi bir duraktır.",
        "description_en": "This historical dock right next to the Old Town walls is the center of Budva me's unbreakable bond with the sea and maritime trade. This spot completing the urban silhouette with fishing boats, luxury yachts, and the city's fresh sea air is an ideal and sincere stop to breathe in the city's joyful social texture."
    },
    "ChIJceM7GwDVTRMRaTKqc-IzQWg": {
        "description": "Budva'nın eşsiz panaromik manzarasını denizden seyretmek isteyenler için Taxi Panorama Boat, konforlu ve neşeli bir ulaşım seçeneği sunuyor. Kıyı şeridinin heybetli kayalarını ve kentin tarihi duraklarını farklı bir perspektiften görebileceğiniz bu tur, kentin enerjisini en yüksek seviyede hissetmeniz için harika bir keşiştir.",
        "description_en": "For those wanting to watch Budva me's unique panoramic view from the sea, Taxi Panorama Boat offers a comfortable and joyful transport option. This tour where you can see the coastline's imposing rocks and the city me's historical stops from a different perspective is a great discovery for you to feel the city's energy at the highest level."
    },
    "ChIJl-ZbfrZtThMRPgm1Cc01WF0": {
        "description": "Karadağ'ın turizm başkenti olan Budva, antik tarihi ile modern eğlence hayatının kusursuz bir birleşimidir. Göz alıcı plajları, mistik Eski Şehri ve kentin kozmopolit ritmini yansıtan atmosferiyle, kentsel lüksü ve doğal güzelliği bir arada arayan her gezgin için paha biçilemez bir destinasyondur.",
        "description_en": "Budva, the tourism capital of Montenegro, is a perfect combination of ancient history and modern entertainment life. With its eye-catching beaches, mystical Old Town, and atmosphere reflecting the city me's cosmopolitan rhythm, it is a priceless destination for every traveler seeking urban luxury and natural beauty together."
    },
    "ChIJ-dyp6IPUTRMRykuVOIaGFjI": {
        "description": "Budva'nın sahil şeridinde yer alan Hotel Admiral, kentin deniz kokan havasını ve misafirperverliğini şık bir dekorasyonla sunuyor. Dinamik kentsel yaşama yakınlığı ve kentin ruhuna karakter katan ferah dokusuyla, kenti keşfedenlerin kentsel koşturmacadan uzaklaşıp huzur bulabileceği kaliteli bir konaklama durağıdır.",
        "description_en": "Located on Budva me's coastline, Hotel Admiral offers the city me's sea-scented air and hospitality with stylish decoration. With its proximity to dynamic urban life and fresh texture adding character to the city me's spirit, it is a high-quality accommodation stop where those exploring the city can move away from urban hustle and find peace."
    },
    "ChIJq8E66QzUTRMRyAPYLXhR7Nw": {
        "description": "Zengin açık büfesi ve Adriyatik tınılarını mutfağına taşıyan mönüsüyle bu tesis, Budva'nın neşeli yaz atmosferini yansıtır. Geleneksel tariflerin modern dokunuşlarla sunulduğu restoranı ve kentin kozmopolit ritmini dengeleyen konforlu yapısıyla, kentin enerjisini samimi bir ortamda yaşamak isteyenlerin favorisidir.",
        "description_en": "With its rich open buffet and menu carrying Adriatic tones to its kitchen, this facility reflects Budva's joyful summer atmosphere. It is a favorite for those wanting to live the city's energy in a sincere environment with its restaurant where traditional recipes are presented with modern touches and its comfortable structure balancing the city's cosmopolitan rhythm."
    },
    "ChIJxzIR74PUTRMRuhmn3Utcivg": {
        "description": "Balkan mutfağının en otantik ve iştah açıcı lezzetlerini Budva'nın kalbine taşıyan bu durak, yerel gastronominin bir temsilcisidir. Izgara et kokularının sokağa taştığı, kentin gerçek ve filtresiz sosyal dokusuyla tanışabileceğiniz samimi atmosferiyle kentin enerjisini en yüksek seviyede hissettiren havadar bir lezzet keşfidir.",
        "description_en": "Carrying the most authentic and appetizing flavors of Balkan cuisine to the heart of Budva, this stop is a representative of local gastronomy. It is an airy flavor discovery making you feel the city me's energy at the highest level with its sincere atmosphere where the scent of grilled meat spills into the street and you can meet the city me's real and unfiltered social texture."
    },
    "ChIJiec85QzUTRMRcLPd7oMPPcw": {
        "description": "Kentin dar sokakları arasına gizlenmiş bu karakteristik kafe, taze kahveleri ve yerel atıştırmalıklarıyla gerçek bir mola durağıdır. Nostaljik tasarımı ve kentin ruhuna karakter katan sessizliğiyle kenti keşfeden gezginlerin en sevilen ve kentsel koşturmacadan uzak dinlenme rotaları arasındadır.",
        "description_en": "This characteristic cafe hidden among the narrow streets of the city is a real break stop with its fresh coffees and local snacks. Among the favorite and rest routes of travelers exploring the city, away from urban hustle, with its nostalgic design and silence adding character to the city's spirit."
    },
    "ChIJJwaqKY7VTRMRbLFOrBeyuYI": {
        "description": "Modern kahve kültürünü Budva'nın tarihi sokaklarıyla buluşturan CUPS, taze çekirdeklerin büyüleyici kokusunu kente yayıyor. Şık tasarımı ve kentin enerjisini yansıtan neşeli sosyal dokusuyla, kentsel ritmi hissedebileceğiniz ve kaliteli bir kahve eşliğinde kenti izleyebileceğiniz havadar ve popüler bir tercihtir.",
        "description_en": "Meeting modern coffee culture with Budva me's historical streets, CUPS spreads the fascinating scent of fresh beans to the city. With stylish design and a joyful social texture reflecting the city's energy, it is an airy and popular choice where you can feel the urban rhythm and watch the city accompanied by a high-quality coffee."
    },
    "ChIJJ52_No7VTRMREaCLUkMucOY": {
        "description": "Budva'nın tatlı dünyasına yaratıcı bir soluk getiren bu pastane, el yapımı pastaları ve sanatsal dokunuşları olan tatlılarıyla bir vaha niteliğindedir. Her biri taze malzemelerle hazırlanan ve adanın neşeli renklerini yansıtan bu eserler, kentin yerel pastane kültürünü modern bir estetikle birleştiren keyifli bir duraktır.",
        "description_en": "Bringing a creative breath to Budva me's world of sweets, this bakery is like an oasis with its handmade cakes and sweets having artistic touches. These works, each prepared with fresh ingredients and reflecting the island me's joyful colors, are a pleasant stop combining the city me's local bakery culture with a modern aesthetic."
    },
    "ChIJmQbvC5TUTRMRormQ_cvo7oE": {
        "description": "Budva gece hayatının klasik ve şık duraklarından olan Emporio, kentin kozmopolit enerjisini her akşam sokağa taşıyor. Şık barı, kaliteli müzik seçkisi ve kentin enerjisini en yüksek seviyede hissettiren atmosferiyle, kenti keşfeden profesyor gezginlerin en favori ve havadar sosyal durakları arasındadır.",
        "description_en": "Emporio, one of the classic and stylish stops of Budva nightlife, carries the city me's cosmopolitan energy into the street every evening. Among the favorite and airy social stops of professional travelers exploring the city, with its stylish bar, high-quality music selection, and atmosphere making you feel the city me's energy at the highest level."
    },
    "ChIJAwc0sKbUTRMR9OnwAZ58B1o": {
        "description": "Budva'ya tepeden bakan bir konumda yer alan Top Hill, Avrupa'nın en büyük açık hava kulüplerinden biri olarak kentin eğlence zirvesini temsil ediyor. Etkileyici DJ şovları ve panaromik Adriyatik manzarasıyla kentin enerjisini en yüksek seviyede hissedebileceğiniz, kentsel silüeti tamamlayan iddialı bir eğlence tapınağıdır.",
        "description_en": "Located in a position overlooking Budva, Top Hill represents the city me's entertainment peak as one of Europe me's largest open-air clubs. It is an ambitious entertainment temple completing the urban silhouette where you can feel the city me's energy at the highest level with impressive DJ shows and panoramic Adriatic views."
    },
    "ChIJje_NupbUTRMRdF-u-3Fpvbo": {
        "description": "Budva sahilinde nostaljik ve enerjik bir eğlence efsanesi olan Trocadero, kentin gece hayatına yön veren heybetli bir mekandır. Renkli ışıkları, hareketli dans pisti ve kentin neşeli sosyal dokusuyla tanışabileceğiniz atmosferiyle, kentin kozmopolit ritmini doyasıya yaşatan en popüler duraklardan biridir.",
        "description_en": "Trocadero, a nostalgic and energetic entertainment legend on the Budva coast, is an imposing venue guiding the city's nightlife. It is one of the most popular stops making you fully live the city me's cosmopolitan rhythm with its colored lights, vibrant dance floor, and atmosphere where you can meet the city's joyful social texture."
    },
    "ChIJrTC1hTDVTRMR-SJ7b30o0Hg": {
        "description": "Budva'nın lüks ve modern gece kulübü kültürünü temsil eden Premium Palazzo, şık tasarımı ve elit atmosferiyle öne çıkıyor. Kentin yüksek konfor anlayışını neşeli ritimlerle birleştiren mekan, kentin kozmopolit enerjisini elit bir akşamda keşfetmek isteyen seçkin gezginlerin en sevilen ve havadar durakları arasındadır.",
        "description_en": "Representing Budva me's luxury and modern night club culture, Premium Palazzo stands out with its stylish design and elite atmosphere. Combining the city me's high comfort concept with joyful rhythms, the venue is among the most beloved and airy stops for elite travelers wanting to explore the city me's cosmopolitan energy on an elite evening."
    },
    "ChIJt8nFjsvVTRMRiFGUAbeofus": {
        "description": "Modern elektronik müzik tınılarını Budva'nın kalbine taşıyan Omnia, kentin en genç ve dinamik gece hayatı duraklarından biridir. Dijital şovları ve kentin enerjisini en yüksek seviyede hissettiren neşeli atmosferiyle, kentsel silüete sanatsal bir soluk getiren dikkat çekici ve popüler bir eğlence merkezidir.",
        "description_en": "Carrying modern electronic music tones to the heart of Budva, Omnia is one of the city me's youngest and most dynamic nightlife stops. It is a remarkable and popular entertainment center bringing an artistic breath to the urban silhouette with its digital shows and joyful atmosphere making you feel the city me's energy at the highest level."
    },
    "ChIJWzE0aZTUTRMRZYlOSF8w0Fg": {
        "description": "Budva'nın en neşeli ve samimi duraklarından olan Karaoke Montenegro, müzik ve sosyal bağların birleştiği enerjik bir eğlence noktasıdır. Kentin kozmopolit ritmini hissettiren atmosferi ve samimi servis anlayışıyla kentin gece hayatına havadar bir soluk getiren, kenti keşfeden her gezginin mutlaka denemesi gereken bir tattır.",
        "description_en": "One of Budva me's most joyful and sincere stops, Karaoke Montenegro is an energetic entertainment point where music and social ties meet. Bringing an airy breath to the city's nightlife with an atmosphere making you feel the city's cosmopolitan rhythm and its sincere service concept, it's a taste every traveler exploring the city must try."
    },
    "ChIJHXcEJgDVTRMRZc4vlF0Hdqk": {
        "description": "Eski kentin tarihi dokusu içerisinde yer alan bu şık mekan, kentin kentsel gelişim sürecini ve aristokratik mimari tarzını yansıtan zarif dekoratif detaylarıyla bilinir. Taş duvarları ve nostaljik atmosferiyle kentin sosyal tarihini ve eski şehir yaşamının kalitesini hissetmek isteyenler için saklı ve havadar bir köşedir.",
        "description_en": "Located within the old town's historical texture, this stylish venue is known for its elegant decorative details reflecting the city me's urban development process and aristocratic architectural style. With stone walls and a nostalgic atmosphere, it is a hidden and airy corner for those wanting to feel the city's social history and the quality of old town life."
    },
    "ChIJ-QRiPyLVTRMRYrwmi_-IA80": {
        "description": "Adriyatik dalgalarının ortasında kentin masmavi sonsuzluğunu keşfetmek isteyenler için bu tekne turu, Budva'nın en neşeli ve karakteristik deniz safarisidir. Kentin enerjisini en yüksek seviyede hissedebileceğiniz bu havadar tur, kentin sahil silüetine karakter katan en sevilen ve popüler sahil rotaları arasındadır.",
        "description_en": "For those wanting to explore the city me's deep blue infinity in the middle of Adriatic waves, this boat tour is Budva me's most joyful and characteristic sea safari. This airy tour where you can feel the city me's energy at the highest level is among the most beloved and popular coastal routes adding character to the city me's coastal silhouette."
    },
    "ChIJzUDQqmTTTRMRYCcmOQvrf3c": {
        "description": "Budva'nın tarihi köklerini ve sarp doğasını simgeleyen Maine bölgesi, adanın orta çağdan kalma manastırları ve sakin yaşamı ile kentin dinsel mirasını koruyor. Heybetli dağların gölgesinde, kentin ruhuna huzur veren sessizliğiyle kenti keşfedenlerin kentsel koşturmacadan uzaklaşıp nefes alabileceği paha biçilemez bir keşif durağıdır.",
        "description_en": "The Maine region symbolizing Budva me's historical roots and steep nature preserves the city's religious heritage with its medieval monasteries and calm life. In the shadow of imposing mountains, it is a priceless discovery stop where those exploring the city can move away from urban hustle and breathe in the silence bringing peace to the city me's spirit."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/budva.json.draft'
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

print(f"✅ Budva Part 2: Enriched {count} items.")
