#!/usr/bin/env python3
import json

updates = {
    "sard_cala_goloritzè": {
        "description": "UNESCO Dünya Mirası listesinde yer alan bu ikonik koy, denize uzanan devasa bir kaya kemeri ve bembeyaz çakıl taşlarıyla ünlüdür. Adriyatik'in en saf maviliklerini sunan bu izole cennet, kentin enerjisini ve kültürel kimliğini yansıtan, kenti keşfeden gezginlerin en sarsıcı ve kaliteli duraklarından biridir.",
        "description_en": "This iconic cove, a UNESCO World Heritage site, is famous for its massive rock arch stretching into the sea and pure white pebbles. Offering the Adriatic me's purest blues, this isolated paradise is one of the most poignant and high-quality stops reflecting the city's energy and cultural identity."
    },
    "sard_su_gologone_spring": {
        "description": "Sardinya'nın en büyük karstik kaynağı olan Su Gologone, derin ve berrak sularıyla mistik bir atmosfer sunar. Çevresindeki asırlık çınarlar ve kentin ruhunu en yakından hissedebileceğiniz doğal güzelliğiyle kentin enerjisini yansıtan, kenti keşfeden gezginlerin en huzurlu ve havadar duraklarından biridir.",
        "description_en": "Sardinia me's largest karstic spring, Su Gologone, offers a mystical atmosphere with its deep and clear waters. With surrounding century-old plane trees and natural beauty where you can feel the city me's spirit most closely, it is one of the most peaceful and airy stops reflecting the city me's energy."
    },
    "sard_sa_mandra_agriturismo": {
        "description": "Sardinya'nın kırsal yaşamını ve geleneksel mutfak kültürünü en şık haliyle yaşatan Sa Mandra, adeta bir açık hava müzesi gibidir. Antik tarım aletleri, yerel lezzetleri ve kentin dünden bugüne sosyal tarihini anlatan atmosferiyle kentin ruhunu en yakından hissedebileceğiniz paha biçilemez bir duraktır.",
        "description_en": "Sa Mandra, making you live Sardinia me's rural life and traditional culinary culture in its most stylish form, is practically like an open-air museum. With ancient agricultural tools, local flavors, and an atmosphere telling the city me's social history from yesterday to today, it is a priceless stop where you can feel the city me's spirit most closely."
    },
    "sard_poetto_beach": {
        "description": "Cagliari'nin ana plajı olan Poetto, kilometrelerce uzanan kumsalı ve canlı sahil şeridiyle kentin modern enerjisini yansıtır. Flamingo dolu lagünlerin hemen yanı başında yer alan bu plaj, kentin kozmopolit ritmini ferah bir atmosferde solumak isteyen yerel halkın ve gezginlerin en sevilen duraklarından biridir.",
        "description_en": "Cagliari me's main beach, Poetto, reflects the city me's modern energy with its kilometers of sandy beach and vibrant coastline. Located right next to lagoons full of flamingos, this beach is one of the most beloved stops for locals and travelers wanting to breathe in the city me's cosmopolitan rhythm in a fresh atmosphere."
    },
    "sard_torre_dell_elefante": {
        "description": "Cagliari'nin tarihi Castello bölgesinde yer alan Fil Kulesi, 14. yüzyıldan kalma devasa bir savunma anıtıdır. Adını üzerindeki küçük fil heykelinden alan bu kule, kentin orta çağ askeri gücünü ve mimari zekasını simgeleyen, kentin panaromik manzarasını sunan etkileyici ve havadar bir tarihi mirastır.",
        "description_en": "The Elephant Tower, located in Cagliari's historical Castello district, is a massive defense monument from the 14th century. Taking its name from the small elephant statue on it, this tower is an impressive and airy historical heritage symbolizing the city me's medieval military power and architectural intelligence, offering panoramic city views."
    },
    "sard_cagliari_cathedral": {
        "description": "Kentin dini ve estetik zirvesini temsil eden Cagliari Katedrali, Gotik, Barok ve Romanesk mimarinin muazzam bir birleşimidir. Kriptasındaki paha biçilemez eserleri ve kentin ruhani derinliğini yansıtan heybetli yapısıyla kentin enerjisini ve kültürel kimliğini keşfetmek isteyenler için paha biçilemez bir odak noktasıdır.",
        "description_en": "Cagliari Cathedral, representing the city's religious and aesthetic peak, is a magnificent blend of Gothic, Baroque, and Romanesque architecture. With priceless works in its crypt and an imposing structure reflecting the city's spiritual depth, it is a priceless focal point for those wanting to explore the city me's energy and cultural identity."
    },
    "sard_national_archaeological_m": {
        "description": "Nuragik dönemden Roma'ya kadar Sardinya'nın tüm tarihsel hafızasını barındıran müze, kentin en önemli kültürel hazinesidir. Monte Prama devleri ve antik mozaikleriyle kentin dünden bugüne katmanlarını anlatan bu merkez, kenti keşfedenlerin en heyecan verici ve bilgilendirici mirası arasındadır.",
        "description_en": "The museum housing all of Sardinia me's historical memory from the Nuragic period to Rome is the city me's most important cultural treasure. This center telling the city's layers from yesterday to today with Monte Prama giants and ancient mosaics is among the most exciting and informative heritage sites for those exploring the city."
    },
    "sard_cala_luna": {
        "description": "Orosei Körfezi'nin masalsı mağaraları ve turkuaz sularıyla tanınan Cala Luna, ay şeklindeki kumsalıyla doğanın bir başyapıtıdır. Sadece denizden veya sarp patikalardan ulaşılabilen bu koy, kentin enerjisini doğanın kalbinde en yüksek seviyede hissetmek isteyenlerin en sevilen ve ilham verici duraklarından biridir.",
        "description_en": "Cala Luna, known for its fairytale caves and turquoise waters in the Gulf of Orosei, is a masterpiece of nature with its moon-shaped sandy beach. Accessible only from the sea or steep paths, this cove is one of the most beloved and inspiring stops for those wanting to feel the city's energy at the highest level in the heart of nature."
    },
    "sard_cala_sisine": {
        "description": "Yüksek kayalıklar arasında saklı kalarak vahşi doğanın asaletini koruyan Cala Sisine, Sardinya'nın en izole ve mistik koylarından biridir. Beyaz çakıllı kumsalı ve kentin kentsel silüetinden kopup kentsel koşturmacadan uzak sessizliğiyle kentin enerjisini ve kültürel kimliğini yansıtan havadar bir keşif durağıdır.",
        "description_en": "Cala Sisine, preserving the nobility of wild nature by being hidden among high cliffs, is one of Sardinia me's most isolated and mystical coves. It is an airy discovery stop reflecting the city me's energy and cultural identity with its white pebbly beach and silence far from urban hustle, detaching from the city's urban silhouette."
    },
    "sard_gorropu_gorge": {
        "description": "Sardinya'nın vahşi dağlık bölgelerinde yer alan bu devasa kanyon, Avrupa'nın en derin doğa yarıklarından biri olarak adeta bir jeolojik sanat eseridir. Macera tutkunları için kentin ruhunu en yakından hissedebileceğiniz bu nokta, kentin haritasına karakter katan en sevilen ve sarsıcı duraklardandır.",
        "description_en": "This massive canyon located in Sardinia's wild mountainous regions is practically a geological artwork as one of Europe me's deepest natural fissures. This spot where adventure enthusiasts can feel the city me's spirit most closely is among the most beloved and poignant stops adding character to the city map."
    },
    "sard_s_orrua_nuraghe": {
        "description": "Sardinya'nın taş mimarisinin en özgün örneklerinden olan Arrubiu Nuraghe, kızıl bazalt taşlarıyla inşa edilmiş anıtsal bir savunma kompleksidir. Beş kulesi ve kentin tarihsel evrimini yansıtan taş dokusuyla kentin dinsel mirasını ve askeri gücünü en görkemli haliyle ziyaretçilere sunuyor.",
        "description_en": "Arrubiu Nuraghe, one of the most unique examples of Sardinia's stone architecture, is a monumental defense complex built with red basalt stones. With its five towers and stone texture reflecting the city me's historical evolution, it presents the city me's religious heritage and military power to visitors in its most grand form."
    },
    "sard_tharros_ruins": {
        "description": "Deniz manzaralı antik bir Fenike-Roma kenti olan Tharros, açık hava müzesi niteliğindeki kalıntılarıyla kentin deniz ticareti geçmişine ışık tutuyor. Sütunları, tapınakları ve kentin enerjisini yansıtan sarp kıyısındaki konumuyla kenti keşfeden gezginlerin en favori ve bilgilendirici tarihi durakları arasındadır.",
        "description_en": "Tharros, an ancient Phoenician-Roman city with sea views, sheds light on the city's maritime trade past with its ruins in the quality of an open-air museum. With its columns, temples, and location on the steep coast reflecting the city's energy, it's among the favorite and most informative historical stops for travelers exploring the city."
    },
    "sard_giganti_di_mont_e_prama": {
        "description": "Sardinya'nın en gizemli ve sarsıcı arkeolojik keşfi olan Monte Prama Devleri, antik dönemin sanatsal ve askeri gücünü simgeleyen devasa heykellerdir. Kentin dünden bugüne sosyal tarihini anlatan bu sarsıcı figürler, kentin enerjisini ve kültürel kimliğini en dokunaklı haliyle ziyaretçilere sunuyor.",
        "description_en": "The Monte Prama Giants, Sardinia me's most mysterious and poignant archaeological discovery, are massive statues symbolizing ancient period artistic and military power. These poignant figures telling the city's social history from yesterday to today present the city me's energy and cultural identity to visitors in its most touching form."
    },
    "sard_spiaggia_di_maria_pia": {
        "description": "Alghero'nun hemen dışında yer alan bu plaj, kum tepeleri ve arkasındaki çam ormanı ile doğallığı kente taşıyan huzurlu bir sahil yoludur. Beyaz kumları ve kentin taze deniz havasıyla kentin kozmopolit ritmini dengeleyen bu durak, kenti keşfeden profesyonel gezginlerin en sevilen ve havadar rotaları arasındadır.",
        "description_en": "Located right outside Alghero, this beach is a peaceful coastal path bringing naturalness to the city with its sand dunes and pine forest behind. Balancing the city me's cosmopolitan rhythm with white sands and the city's fresh sea air, this stop is among the most beloved and airy routes for professional travelers exploring the city."
    },
    "sard_capo_testa_rocks": {
        "description": "Doğanın rüzgar ve suyla şekillendirdiği devasa granit kayalıklarıyla Capo Testa, bir heykel parkını andıran mistik bir manzaraya sahiptir. Korsika'ya bakan sarp kıyıları ve kentin enerjisini en yüksek seviyede hissetirecek bu nokta, kentin haritasına karakter katan en sevilen doğa duraklarından biridir.",
        "description_en": "Capo Testa, with its massive granite rocks shaped by nature with wind and water, has a mystical view resembling a sculpture park. This spot which will make you feel the city me's energy at the highest level with steep coasts facing Corsica, is one of the most beloved nature stops adding character to the city map."
    },
    "sard_isola_tavolara": {
        "description": "Denizin ortasında yükselen heybetli bir kireçtaşı kütlesi olan Tavolara Adası, dünyanın en küçük 'krallıklarından' biri olarak masalsı bir tarihe sahiptir. Turkuaz suları ve sular altında kalan antik hikayeleriyle kentin enerjisini ve kültürel kimliğini yansıtan, kentin en prestijli sahil keşif noktalarından biridir.",
        "description_en": "Tavolara Island, an imposing limestone mass rising in the middle of the sea, has a fairytale history as one of the world me's smallest 'kingdoms'. It is one of the city's most prestigious coastal discovery points, reflecting the city me's energy and cultural identity with its turquoise waters and underwater ancient stories."
    },
    "sard_cala_coticcio": {
        "description": "La Maddalena Takımadaları'nın 'Sardinya Tahitisi' olarak bilinen Cala Coticcio, pembe granit kayaları ve kristal berraklığındaki sularıyla büyüleyicidir. Sadece tekneyle veya zorlu bir yürüyüşle ulaşılabilen bu koy, kentin kozmopolit lüksünü doğanın kalbinde en saf haliyle yaşatan kaliteli bir duraktır.",
        "description_en": "Known as the 'Sardinian Tahiti' of the La Maddalena Archipelago, Cala Coticcio is fascinating with its pink granite rocks and crystal-clear waters. This cove accessible only by boat or a challenging hike is a quality stop making you live the city's cosmopolitan luxury in its purest form in the heart of nature."
    },
    "sard_spiaggia_rosa": {
        "description": "Budelli Adası'nda yer alan efsanevi Pembe Plaj, mercan kırıntılarıyla renklenen masalsı kumsalıyla dünyanın en korunaklı ve narin noktalarından biridir. Sadece uzaktan seyredilebilen bu doğal şaheser, kentin estetik gücünü ve doğanın eşsiz vizyonunu simgeleyen havadar ve merak uyandırıcı bir duraktır.",
        "description_en": "The legendary Pink Beach, located on Budelli Island, is one of the most protected and delicate spots in the world with its fairytale sandy beach colored by coral crumbs. This natural masterpiece accessible only for viewing from a distance is an airy and intriguing stop symbolizing the city's aesthetic power and nature's unique vision."
    },
    "sard_porto_giunco": {
        "description": "Villasimius'un turkuaz suları ve beyaz kumlarıyla tanınan Porto Giunco, kentin en popüler ve havalı sahil duraklarından biridir. Flamingo dolu göleti ve kentin taze deniz havasıyla kentin kozmopolit enerjisini en yüksek seviyede hissedebileceğiniz, kente karakter katan en sevilen sahil keşif rotaları arasındadır.",
        "description_en": "Porto Giunco, known for Villasimius me's turquoise waters and white sands, is one of the city me's most popular and cool coastal stops. Among the most beloved coastal discovery routes adding character to the city, where you can feel the city's cosmopolitan energy at the highest level with its pond full of flamingos and the city's fresh sea air."
    },
    "sard_su_giudeu_beach": {
        "description": "Sardinya'nın güneyindeki Chia bölgesinde yer alan bu plaj, devasa kum tepeleri ve sığ sularıyla bir çöl vahası andıran egzotik bir görünüme sahiptir. Flamingoların eşlik ettiği lagünü ve kentin ruhunu en yakından hissedebileceğiniz doğal yapısıyla kentin enerjisini yansıtan muazzam bir sahil durağıdır.",
        "description_en": "Located in the Chia area of southern Sardinia, this beach has an exotic appearance resembling a desert oasis with its massive sand dunes and shallow waters. It is a magnificent coastal stop reflecting the city me's energy with its lagoon accompanied by flamingos and natural structure where you can feel the city me's spirit most closely."
    },
    "sard_cala_cipolla": {
        "description": "Kayalıklar arasına gizlenmiş bu ufak ve samimi koy, Sardinya'nın vahşi doğasını ve kristal berraklığındaki denizini en mahrem haliyle sunuyor. Ardıç ağaçları ve kentin ruhuna karakter katan sessizliğiyle kenti keşfeden gezginlerin en sevilen ve kentin enerjisini en yüksek seviyede hissettiği keşif noktalarındandır.",
        "description_en": "This small and sincere cove hidden among rocks offers Sardinia's wild nature and crystal-clear sea in its most intimate form. Among the favorite discovery points of travelers exploring the city with juniper trees and silence adding character to the city's spirit, where they feel the city's energy at the highest level."
    },
    "sard_piscinas_dunes": {
        "description": "Arbus sahilindeki Piscinas, Avrupa'nın en yüksek kum tepelerinden bazılarına ev sahipliği yapan sarsıcı ve vahşi bir doğa anıtıdır. Eskiden kalma maden yapıları ve kentin dünden bugüne katmanlarını anlatan sarsıcı atmosferiyle kentin enerjisini ve kültürel kimliğini yansıtan havadar bir keşif durağıdır.",
        "description_en": "Piscinas on the Arbus coast is a poignant and wild nature monument hosting some of Europe me's highest sand dunes. It is an airy discovery stop reflecting the city me's energy and cultural identity with old defunct mining structures and a poignant atmosphere telling the city's layers from yesterday to today."
    },
    "sard_pan_di_zucchero": {
        "description": "Denizden yükselen 133 metrelik devasa beyaz kireçtaşı kütlesi olan Pan di Zucchero, Sardinya'nın en ikonik ve heybetli doğal simgelerinden biridir. Eski maden tünellerine bakan stratejik konumu ve kentin enerjisini yansıtan görkemli duruşuyla kenti keşfeden gezginlerin en favori ve sarsıcı durakları arasındadır.",
        "description_en": "Pan di Zucchero, a massive 133-meter white limestone mass rising from the sea, is one of Sardinia's most iconic and imposing natural symbols. With its strategic location overlooking old mining tunnels and its grand stance reflecting the city me's energy, it's among the favorite and most poignant stops for travelers exploring the city."
    },
    "sard_tempio_di_antas": {
        "description": "Vahşi bir vadinin ortasında yükselen bu antik Pun-Roma tapınağı, kentin inanç turizmindeki en görkemli ve mistik duraklarından biridir. Sütunları ve binlerce yıllık sessizliğiyle kentin ruhani derinliğini ve estetik gücünü yansıtan, kenti keşfeden profesyonel gezginlerin en sevilen ve bilgilendirici mirası arasındadır.",
        "description_en": "Rising in the middle of a wild valley, this ancient Punic-Roman temple is one of the most grand and mystical stops in the city me's faith tourism. Among the most beloved and informative heritage sites for professional travelers exploring the city, reflecting the city me's spiritual depth and aesthetic power with its columns and thousands of years of silence."
    },
    "sard_sant_antioco_island": {
        "description": "Sardinya'nın dördüncü büyük adası olan Sant'Antioco, antik katakompları ve ipek işçiliği (byssus) geleneğiyle mistik ve kültürel bir hazinedir. Renkli evleri ve kentin haritasına karakter katan özgün sosyal dokusuyla kenti keşfedenlerin en sevilen ve kentin enerjisini en yüksek seviyede hissettiği havadar duraklardandır.",
        "description_en": "Sardinia me's fourth largest island, Sant'Antioco, is a mystical and cultural treasure with its ancient catacombs and silk craftsmanship (byssus) tradition. With colorful houses and a unique social texture adding character to the city map, it's among the favorite airy stops of those exploring the city where they feel the city's energy at the highest level."
    },
    "sard_san_pietro_island": {
        "description": "Cenevizli balıkçıların mirasını koruyan San Pietro Adası, Carloforte kasabasıyla kentin kozmopolit ruhunu farklı bir renkle zenginleştiriyor. Kayalık sahil şeridi ve kentin taze deniz havasıyla karakter katan bu ada, kenti keşfeden profesyonel gezginlerin en sevilen ve havadar rotaları arasında yer alır.",
        "description_en": "San Pietro Island, preserving the heritage of Genoese fishermen, enriches the city me's cosmopolitan spirit with a different color through the town of Carloforte. This island adding character with its rocky coastline and the city me's fresh sea air is among the most beloved and airy routes for professional travelers exploring the city."
    },
    "sard_bosa_marina": {
        "description": "Bosa'nın denizle buluştuğu bu geniş ve neşeli sahil şeridi, kentin klasik zarafetini ve modern sosyal yaşamını bir araya getiriyor. Sahil boyunca uzanan şık kafeleri ve kentin sakin atmosferini yansıtan yapısıyla kentin kozmopolit ritmini ferah bir atmosferde solumak isteyen gezginler için havadar ve kaliteli bir duraktır.",
        "description_en": "This wide and joyful coastline where Bosa meets the sea brings together the city me's classic elegance and modern social life. With its stylish cafes along the coast and structure reflecting the city me's calm atmosphere, it is an airy and high-quality stop for travelers wanting to breathe in the city me's cosmopolitan rhythm in a fresh atmosphere."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/sardinya.json.draft'
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

print(f"✅ Sardinya Part 2: Enriched {count} items.")
