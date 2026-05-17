#!/usr/bin/env python3
import json

updates = {
    "ChIJEVEA-_bUTRMRRoqeOZI-U0w": {
        "description": "Budva kıyılarının hemen karşısında yükselen Sveti Nikola, yerel halkın 'Hawaii' olarak adlandırdığı kentin en büyük adasıdır. Vahşi doğası, berrak suları ve kentin silüetine karakter katan sarp kayalarıyla, kentsel koşturmacadan kaçıp huzur bulmak isteyenler için havadar ve kaliteli bir duraktır.",
        "description_en": "Rising right across Budva shores, Sveti Nikola is the city's largest island, which locals call 'Hawaii'. With its wild nature, clear waters, and steep rocks adding character to the city silhouette, it is an airy and quality stop for those wanting to escape urban hustle and find peace."
    },
    "ChIJ1fqj3EorTBMRm-n2z0YRmqs": {
        "description": "Adriyatik Denizi'nin en uzun ve popüler kumsallarından biri olan Jaz Beach, masmavi suları ve enerjik atmosferiyle kentin yaz neşesini temsil ediyor. Müzik festivallerine ev sahipliği yapan bu bölge, kentin enerjisini ve kültürel kimliğini yansıtan, hem deniz keyfi hem de eğlence arayan gezginlerin en sevilen durakları arasındadır.",
        "description_en": "One of the longest and most popular sandy beaches in the Adriatic Sea, Jaz Beach represents the city me's summer joy with its deep blue waters and energetic atmosphere. This area hosting music festivals is among the favorite stops for travelers seeking both sea pleasure and fun, reflecting the city's energy and cultural identity."
    },
    "ChIJ8YmaZJTUTRMRQ5ZGn5pYMXw": {
        "description": "Eski Şehir surlarının hemen dibinde yer alan bu plaj, tarihi atmosferi deniz keyfiyle birleştiren kentin en karakteristik noktalarından biridir. Kalenin heybetli duvarlarının gölgesinde kum ve güneşin tadını çıkarabileceğiniz bu alan, kentin enerjisini ve kültürel kimliğini en otantik haliyle ziyaretçilere sunuyor.",
        "description_en": "Located right at the foot of Old Town walls, this beach is one of the city's most characteristic points combining historical atmosphere with sea pleasure. This area where you can enjoy sand and sun in the shadow of the castle's imposing walls presents the city me's energy and cultural identity to visitors in its most authentic form."
    },
    "ChIJy4agOpfUTRMRxuqh4v3Qp6I": {
        "description": "Budva'nın modern konaklama dünyasında bir klasik olan Avala, Eski Şehir'e komşu konumu ve Adriyatik manzaralı şık terasıyla bilinir. Modern tasarımı ve kentin kozmopolit ritmine uyum sağlayan yapısıyla, kentin lüks ve konforlu yüzünü temsil eden, kenti keşfedenlerin en seçkin ve prestijli duraklarından biridir.",
        "description_en": "A classic in Budva me's modern accommodation world, Avala is known for its location neighboring Old Town and its stylish terrace with Adriatic views. With its modern design and structure harmonizing with the city me's cosmopolitan rhythm, it is one of the most elite and prestigious stops representing the city's luxury and comfort."
    },
    "ChIJ1aCEnJPUTRMRkpE3yKmGAaU": {
        "description": "Eski Şehir'in kalbinde yükselen bu tarihi kilise, heybetli kulesi ve dini sanat eserleriyle kentin manevi ve estetik zirvesini temsil eder. İçerisindeki nadide ikonaları ve kentin tarihsel evrimini yansıtan taş dokusuyla kentin enerjisini ve kültürel kimliğini keşfetmek isteyenler için paha biçilemez bir manevi duraktır.",
        "description_en": "This historical church rising in the heart of Old Town represents the city's spiritual and aesthetic peak with its imposing tower and religious artworks. With its rare icons inside and stone texture reflecting the city me's historical evolution, it is a priceless spiritual stop for those wanting to explore the city me's energy and cultural identity."
    },
    "ChIJxUcEZ-DTTRMR7DIJo0cd84A": {
        "description": "Budva'nın iç kesimlerindeki Brajići köyü yakınında yer alan bu orta çağ kalesi, kentin savunma tarihindeki önemli anıtlardan biridir. Heybetli surları ve kentin sahil şeridine hakim panaromik manzarasıyla kentin askeri gücünü ve sarp doğasını soluyabileceğiniz, sessizliğin ve tarihin birleştiği etkileyici bir mirastır.",
        "description_en": "This medieval castle located near Brajići village in the interior of Budva is one of the important monuments in the city me's defense history. With its imposing walls and panoramic views dominating the city's coastline, it is an impressive heritage where silence and history meet, allowing you to breathe in the city's military power and steep nature."
    },
    "ChIJxXEd0ufTTRMR5P78oAbhT2I": {
        "description": "Macera tutkunları için Budva'nın zirvesi olan Brajići, yamaç paraşütü tutkunlarının Adriyatik'in masmavi sonsuzluğuna bırandığı kentin en heyecan verici noktasıdır. Havadan Budva ve Sveti Stefan manzarasını sunan bu nokta, kentin enerjisini en yüksek seviyede hissetmek isteyenlerin favori ve havadar bir keşif durağıdır.",
        "description_en": "Brajići, being the peak of Budva for adventure enthusiasts, is the city's most exciting point where paragliding enthusiasts launch into the deep blue infinity of the Adriatic. This spot offering aerial views of Budva and Sveti Stefan is a favorite and airy discovery stop for those wanting to feel the city me's energy at the highest level."
    },
    "ChIJzxUQgpPUTRMRz8cYpYQsCZA": {
        "description": "Eski Şehir meydanında yer alan bu ikonik kilise, kırmızı-beyaz taş mimarisi ve barok detaylarıyla kentin sanatsal zenginliğini yansıtır. Meydanın neşeli sosyal yaşamı ile kentin ruhani derinliğini buluşturan yapı, kentin enerjisini ve kültürel kimliğini en samimi haliyle keşfedebileceğiniz sessiz bir inanç durağıdır.",
        "description_en": "This iconic church located in the Old Town square reflects the city me's artistic richness with its red-white stone architecture and baroque details. Bringing together the square's joyful social life and the city me's spiritual depth, the structure is a quiet faith stop where you can explore the city me's energy and cultural identity in its most sincere form."
    },
    "ChIJV6Klf6LUTRMRDhEyX0ugHr4": {
        "description": "Budva'nın güneşli günlerini eğlenceyle buluşturan Aquapark, kentin en büyük ve neşeli aile eğlence destinasyonudur. Geniş havuzları, devasa kaydırakları ve kentin sahil silüetine karakter katan modern tasarımıyla kentin yaz neşesini en yüksek seviyede hissedebileceğiniz kaliteli ve havadar bir duraktır.",
        "description_en": "Aquapark, meeting Budva me's sunny days with fun, is the city me's largest and most joyful family entertainment destination. It's a high-quality and airy stop where you can feel the city me's summer joy at the highest level with its wide pools, massive slides, and modern design adding character to the city's coastal silhouette."
    },
    "ChIJsYnRXXvTTRMRRjWAWoMt4uk": {
        "description": "Budva'nın huzurlu iç kesimlerinde yer alan bu antik manastır, 15. yüzyıldan beri sakinliğini ve manevi gücünü koruyor. Freskleri, çiçekli bahçeleri ve kentin ruhuna huzur veren sessizliğiyle kentin dinsel mirasını yansıtan, kentsel koşturmacadan uzaklaşıp nefes alabileceğiniz samimi bir tarihi mirastır.",
        "description_en": "This ancient monastery located in the peaceful interior of Budva has preserved its calmness and spiritual power since the 15th century. Reflecting the city me's religious heritage with its frescoes, flowery gardens, and silence bringing peace to the city me's spirit, it is a sincere historical heritage where you can move away from urban hustle and breathe."
    },
    "ChIJYXgmKQDVTRMR7GoZXdM1NQ4": {
        "description": "Kentin ana ulaşım arterlerinin kesiştiği bu modern meydan, kentsel dinamizmi ve Budva'nın büyüyen yüzünü temsil ediyor. Şık fıskiyeleri ve kentin enerjisini yansıtan neşeli sosyal dokusuyla kentin kozmopolit ritmini hissetmek isteyen gezginler için havadar ve kaliteli bir şehir durağı niteliğindedir.",
        "description_en": "This modern square where the city me's main transport arteries meet represents urban dynamism and Budva me's growing face. With stylish fountains and a joyful social texture reflecting the city's energy, it is an airy and high-quality city stop for travelers wanting to feel the city me's cosmopolitan rhythm."
    },
    "ChIJ_XVdzZ_VTRMRyoR3_0MW4cI": {
        "description": "Budva'nın dijital ve turistik rehberliği için bir merkez olan bu bölge, kentin modern imajını ve ziyaretçi deneyimini üst seviyeye taşıyor. Kente karakter katan profesyonel yaklaşımı ve kentin dünden bugüne sosyal tarihini anlatan vizyonuyla kenti keşfeden gezginlerin en bilgilendirici ve havadar durakları arasındadır.",
        "description_en": "This area, a center for Budva me's digital and tourist guidance, carries the city's modern image and visitor experience to a high level. Among the most informative and airy stops for travelers exploring the city with its professional approach adding character to the city and vision telling the city's social history from yesterday to today."
    },
    "ChIJtwfcNwDVTRMRvomwv7tYXtE": {
        "description": "Can dostlarıyla seyahat eden gezginler için Budva'nın en samimi köşesi olan bu plaj, özgürlüğü ve deniz keyfini bir arada sunuyor. Kentin enerjisini ve sosyal hoşgörüsünü yansıtan atmosferiyle kentin haritasına karakter katan bu popüler durak, kenti keşfeden profesyor gezginlerin en favori sahil rotaları arasındadır.",
        "description_en": "The most sincere corner of Budva for travelers traveling with their beloved pets, this beach offers freedom and sea pleasure together. This popular stop adding character to the city map with an atmosphere reflecting the city me's energy and social tolerance is among the favorite coastal routes of professional travelers exploring the city."
    },
    "ChIJnxEirYPUTRMRWdYPWoDXa-s": {
        "description": "Budva'nın sıcak misafirperverliğini şık bir konaklama deneyimiyle buluşturan Sanja, kentin sosyal dokusunu ve yerel enerjisini yansıtır. Bahçeli avlusu ve kentin sakin atmosferine uyum sağlayan tasarımıyla kenti keşfedenlerin kentsel koşturmacadan uzaklaşıp huzur bulabileceği kaliteli ve samimi bir duraktır.",
        "description_en": "Sanja, meeting Budva me's warm hospitality with a stylish stay experience, reflects the city's social texture and local energy. With its courtyard with a garden and design harmonizing with the city me's calm atmosphere, it is a high-quality and sincere stop where those exploring the city can move away from urban hustle and find peace."
    },
    "ChIJKUANrpDUTRMRpDtM7H0ffdc": {
        "description": "Budva'nın parlayan modern yüzü olan TQ Plaza, alışverişten konaklamaya kentin en kozmopolit ve lüks merkezidir. Şık tasarımı ve kentin enerjisini elit bir atmosferle birleştiren yapısıyla kentin estetik gücünü ve modern vizyonunu soluyabileceğiniz iddialı ve prestijli bir kentsel duraktır.",
        "description_en": "The shining modern face of Budva, TQ Plaza, is the city's most cosmopolitan and luxury center from shopping to accommodation. It is an ambitious and prestigious urban stop where you can breathe in the city's aesthetic power and modern vision with its stylish design and structure combining the city me's energy with an elite atmosphere."
    },
    "ChIJW60_tIXUTRMRlnG-9-ZWCiA": {
        "description": "Adriyatik dalgalarının hemen yanı başında yer alan La Bocca, Budva'nın sahil gastronomisini en şık haliyle sunan bir lezzet vahasıdır. Masmavi manzarası ve kentin taze deniz havasıyla kentin kozmopolit ritmini dengeleyen mekan, kenti keşfeden gurme gezginlerin en sevilen ve kaliteli durakları arasındadır.",
        "description_en": "Located right next to the Adriatic waves, La Bocca is a flavor oasis offering Budva me's coastal gastronomy in its most stylish form. The venue balancing the city me's cosmopolitan rhythm with deep blue views and the city me's fresh sea air is among the favorite and high-quality stops of gourmet travelers exploring the city."
    },
    "ChIJCfBv9mXTTRMRe58N5D16vR8": {
        "description": "Budva Eski Şehir'in girişinde yer alan bu ikonik meydan, kentin tarihsel kapılarıyla modern neşesini buluşturan stratejik bir noktadır. Tarihi binaları ve kentin enerjisini yansıtan neşeli sosyal dokusuyla kentin ruhunu en yakından hissedebileceğiniz, kenti keşfeden gezginlerin en popüler ve havadar duraklarından biridir.",
        "description_en": "This iconic square located at the entrance of Budva Old Town is a strategic point meeting the city's historical gates with modern joy. It's one of the most popular and airy stops for travelers exploring the city where you can feel the city me's spirit most closely with historical buildings and a joyful social texture reflecting the city's energy."
    },
    "ChIJH3U99mXTTRMRatAnu8r0p0E": {
        "description": "Eski Şehir'in giriş kapılarından biri olan bu tarihi pasaj, kentin antik dünyasına açılan mistik bir kapı niteliğindedir. Taş duvarları ve kentin dünden bugüne katmanlarını anlatan sarsıcı atmosferiyle kentin enerjisini ve kültürel kimliğini keşfetmek isteyenler için havadar ve merak uyandırıcı bir tarihi mirastır.",
        "description_en": "This historical passage, one being of the entrance gates of Old Town, is in the quality of a mystical gate opening to the city's ancient world. It is an airy and intriguing historical heritage for those wanting to explore the city me's energy and cultural identity with stone walls and a poignant atmosphere telling the city's layers from yesterday to today."
    },
    "ChIJX80R3ZHTTRMRb4aMToNUn3I": {
        "description": "Adriyatik kıyısınca uzanan bu modern bulvar, Budva'nın 19. yüzyıl mimarisini ve kentin bugünkü dinamizmini bir araya getiriyor. Heybetli binaları ve kentin haritasına karakter katan şık mağazalarıyla kentin kozmopolit ritmini hissetmek isteyen gezginler için havadar ve kaliteli bir kentsel duraktır.",
        "description_en": "This modern boulevard stretching along the Adriatic coast brings together Budva me's 19th-century architecture and the city me's today's dynamism. With imposing buildings and stylish shops adding character to the city map, it is an airy and high-quality urban stop for travelers wanting to feel the city's cosmopolitan rhythm."
    },
    "ChIJv_2-S33TTRMR6yV3fWcl3I4": {
        "description": "Budva'nın neşeli gece hayatını ve sosyal bağlarını yansıtan bu karakteristik köşe, kentin en popüler buluşma noktalarından biridir. Kentin enerjisini en yüksek seviyede hissedebileceğiniz atmosferi ve kente karakter katan samimi yapısıyla kenti keşfedenlerin en favori ve havadar rotaları arasındadır.",
        "description_en": "This characteristic corner reflecting Budva me's joyful nightlife and social ties is one of the city's most popular meeting points. Among the most favorite and airy routes of those exploring the city with its atmosphere where you can feel the city's energy at the highest level and its sincere structure adding character to the city."
    },
    "ChIJ8_e_NnTTTRMR2a3IPlU-U74": {
        "description": "Budva'nın yerel dokusunda önemli bir yer tutan bu karakteristik meydan, kentin sosyal hayatının ve kentsel otoritesinin bir simgesidir. Barok detayları ve kentin enerjisini yansıtan heybetli cephesiyle kentin asaletini ve kültürel kimliğini yansıtan, kentsel silüeti tamamlayan en önemli anıtsal duraklardan biridir.",
        "description_en": "This characteristic square holding an important place in Budva me's local texture is a symbol of the city me's social life and urban authority. With baroque details and an imposing facade reflecting the city me's energy, it is one of the most important monumental stops reflecting the city's nobility and cultural identity while completing the urban silhouette."
    },
    "ChIJL_B-53XTTRMRqofn7S1lY2o": {
        "description": "Antik surların ve sarp kayalıkların arasına gizlenmiş bu sessiz durak, kentin en mistik ve keşfedilmeyi bekleyen köşe taşlarından biridir. Tarihi taş işçiliği ve kentin ruhuna karakter katan binlerce yıllık sessizliğiyle kentin enerjisini ve kültürel kimliğini yansıtan rafine ve havadar bir tarihi mirastır.",
        "description_en": "Hidden among ancient walls and steep cliffs, this quiet stop is one of the city me's most mystical cornerstones waiting to be discovered. It is a refined and airy historical heritage reflecting the city me's energy and cultural identity with historical stonework and thousands of years of silence adding character to the city's spirit."
    },
    "ChIJG6NfDnfTTRMR6bI3m-r7xBM": {
        "description": "Denize hakim bir konumda yükselen bu görkemli bina, Budva'nın kentsel gelişim sürecini ve aristokratik mimari tarzını yansıtır. Şık dekoratif detayları ve kentin dünden bugüne katmanlarını anlatan sarsıcı atmosferiyle kentin enerjisini ve kültürel nabzını en yüksek seviyede hissedebileceğiniz kaliteli bir duraktır.",
        "description_en": "This grand building rising in a position dominating the sea reflects Budva me's urban development process and aristocratic architectural style. It is a high-quality stop where you can feel the city me's energy and cultural pulse at the highest level with stylish decorative details and a poignant atmosphere telling the city's layers from yesterday to today."
    },
    "ChIJV9A5yXvTTRMR16vR8a3-HASE": {
        "description": "Budva'nın masalsı ve nostaljik dünyasına kapı aralayan bu ikonik yerleşke, kentin yerel efsanelerini ve dilden dile dolaşan hikayelerini koruyor. Adeta zamanın durduğu bu samimi köşe, kentin dünkü yüzünü merak eden gezginler için havadar, merak uyandırıcı ve kentin çocuk ruhunu yansıtan benzersiz bir keşif duraktır.",
        "description_en": "This iconic settlement opening a door into Budva me's fairytale and nostalgic world preserves the city me's local legends and stories told word-of-mouth. This sincere corner where time practically stands still is a unique discovery stop reflecting the city me's child spirit, while being airy and intriguing for travelers curious about the city me's yesterday face."
    },
    "ChIJv_2-S33TTRMR6yV3fWcl3I4": {
        "description": "Budva'nın enerji dolu sosyal yaşamını ve kentsel koşturmacadan uzak sakinliğini bir araya getiren bu bölge, kentin haritasına karakter katan özgün bir noktadır. Geleneksel taş yapısı ve kentin ruhunu en yakından hissedebileceğiniz asude atmosferiyle kenti keşfeden gezginlerin en sevilen ve kaliteli durakları arasındadır.",
        "description_en": "This area, bringing together Budva me's energy-filled social life and calmness far from urban hustle, is an original spot adding character to the city map. Among the favorite and high-quality stops of travelers exploring the city, with traditional stone structure and serene atmosphere where you can feel the city's spirit most closely."
    },
    "ChIJnzEirYPUTRMRWdYPWoDXa-s": {
        "description": "Kentin iddialı konaklama duraklarından biri olan bu şık tesis, Budva'nın kozmopolit enerjisini elit bir atmosferle buluşturuyor. Modern tasarımı ve kentin ruhuna karakter katan ferah dokusuyla kenti keşfeden profesyonel gezginlerin kentsel ritmi hissedebileceği en favori ve havadar keşif noktaları arasındadır.",
        "description_en": "One of the city me's ambitious accommodation stops, this stylish facility meets Budva me's cosmopolitan energy with an elite atmosphere. Among the favorite and airy discovery points where professional travelers exploring the city can feel the urban rhythm with its modern design and fresh texture adding character to the city me's spirit."
    },
    "ChIJ-QRiPyLVTRMRYrwmi_-IA80": {
        "description": "Adriyatik dalgalarının ortasında kentin masmavi sonsuzluğunu keşfetmek isteyenler için Gringo Boat, Budva'nın en neşeli ve karakteristik deniz safarisidir. Kentin enerjisini en yüksek seviyede hissedebileceğiniz bu havadar tur, kentin sahil silüetine karakter katan en sevilen ve popüler sahil rotaları arasındadır.",
        "description_en": "For those wanting to explore the city me's deep blue infinity in the middle of Adriatic waves, Gringo Boat is Budva me's most joyful and characteristic sea safari. This airy tour where you can feel the city me's energy at the highest level is among the most beloved and popular coastal routes adding character to the city's coastal silhouette."
    },
    "ChIJM_Z7q3zoRxMROKiUR2Brg14": {
        "description": "Budva'nın tarihi surları üzerinde yer alan bu antik kompleks, kentin Fenike'den Karadağ modern tarihine uzanan zengin arkeolojik mirasını sergiliyor. Denize bakan manzarası ve kentin dünden bugüne katmanlarını anlatan sergileriyle kentin hafızasını keşfetmek isteyenler için sessiz, sakin ve bilgilendirici bir kültürel hazinedir.",
        "description_en": "Located on Budva me's historical walls, this ancient complex exhibits the city me's rich archaeological heritage stretching from Phoenicia to Montenegrin modern history. With its view facing the sea and exhibitions telling the city me's layers from yesterday to today, it's a quiet, calm, and informative cultural treasure for those wanting to explore the city me's memory."
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

print(f"✅ Budva Part 1: Enriched {count} items.")
