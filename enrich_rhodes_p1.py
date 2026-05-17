#!/usr/bin/env python3
import json

updates = {
    "ChIJOwwGFftxlRQRNRjOGJ6ujGA": {
        "description": "Rodos'un iç kesimlerinde yer alan Yedi Pınarlar, gür bitki örtüsü ve serin sularıyla kentsel koşturmacadan kaçmak isteyenler için bir doğa mabedidir. Dar bir tünelden geçerek ulaşılan göleti ve kentin ruhuna huzur veren sessizliğiyle kentin enerjisini doğanın kalbinde hissetmek isteyenlerin favori ve havadar bir keşif durağıdır.",
        "description_en": "Seven Springs, located in the interior of Rhodes, is a nature sanctuary for those wanting to escape urban hustle with its lush vegetation and cool waters. With its pond accessible by passing through a narrow tunnel and silence bringing peace to the city me's spirit, it is a favorite and airy discovery stop for those wanting to feel the city me's energy in the heart of nature."
    },
    "ChIJwWu_9oFwlRQRFBVdsM2D4uw": {
        "description": "Her yıl binlerce Panaxia Quadripunctaria kelebeğinin göç ettiği bu vadi, Rodos'un en büyüleyici ve mistik doğa harikalarından biridir. Ahşap köprüleri, ufak şelaleleri ve kentin silüetine karakter katan eşsiz biyoçeşitliliğiyle kentin enerjisini en yüksek seviyede hissettiren havadar ve kaliteli bir doğa rotasıdır.",
        "description_en": "This valley where thousands of Panaxia Quadripunctaria butterflies migrate every year is one of Rhodes' most fascinating and mystical natural wonders. With its wooden bridges, small waterfalls, and unique biodiversity adding character to the city silhouette, it is an airy and high-quality nature route making you feel the city me's energy at the highest level."
    },
    "ChIJdWL3UelhlRQRJrakROLKqF0": {
        "description": "Rodos Eski Şehir'in en yüksek noktasında yer alan bu orta çağ kalesi, kentin panaromik manzarasını sunan mistik bir savunma anıtıdır. Heybetli yapısı ve kentin dünden bugüne katmanlarını anlatan sarsıcı atmosferiyle kentin enerjisini ve kültürel kimliğini keşfetmek isteyenler için paha biçilemez bir tarihi mirastır.",
        "description_en": "This medieval castle located at the highest point of Rhodes Old Town is a mystical defense monument offering panoramic city views. With its imposing structure and poignant atmosphere telling the city's layers from yesterday to today, it is a priceless historical heritage for those wanting to explore the city me's energy and cultural identity."
    },
    "ChIJvWVAledhlRQR_2jmgEadHb8": {
        "description": "Mandraki Limanı'nın girişinde gururla yükselen tarihi yeldeğirmenleri, Rodos'un deniz ticareti geçmişinin ve kentsel silüetinin en ikonik simgeleridir. Masmavi Adriyatik'e karşı kentin haritasına karakter katan bu yapılar, kentin enerjisini ve estetik gücünü yansıtan, kenti keşfedenlerin en sevilen ve havadar duraklarından biridir.",
        "description_en": "The historical windmills rising proudly at the entrance of Mandraki Harbor are the most iconic symbols of Rhodes' maritime trade past and urban silhouette. These structures adding character to the city map against the deep blue Adriatic are among the most beloved and airy stops for those exploring the city, reflecting the city's energy and aesthetic power."
    },
    "ChIJU-KVhJ1klRQRwkxsmhLrra0": {
        "description": "Filerimos Tepesi'nde yer alan bu antik manastır, devasa haçı ve huzurlu çam ormanlarıyla kentin manevi ve estetik zirvelerinden biridir. Antik Ialysos şehri üzerine kurulu olan bu yapı, kentin tarihsel evrimini ve mistik geçmişini soluyabileceğiniz etkileyici ve kaliteli bir keşif durağıdır.",
        "description_en": "This ancient monastery located on Filerimos Hill is one of the city's spiritual and aesthetic peaks with its massive cross and peaceful pine forests. Built on the ancient city of Ialysos, this structure is an impressive and high-quality discovery stop where you can breathe in the city me's historical evolution and mystical past."
    },
    "ChIJI5sidOhhlRQRgfmhbJGNP4E": {
        "description": "Ege'nin turkuaz sularını bir yelkenli üzerinde keşfetmek isteyenler için Rodos'un en kaliteli ve neşeli deniz safarilerinden biridir. Kendi rotanızı çizerek gizli koyları keşfedebileceğimiz bu tur, kentin enerjisini en yüksek seviyede hissettiren ve sahil silüetine karakter katan en sevilen sahil rotaları arasındadır.",
        "description_en": "One of Rhodes me's most high-quality and joyful sea safaris for those wanting to explore the turquoise waters of the Aegean on a sailboat. This tour where you can discover hidden coves by drawing your own route is among the favorite coastal routes adding character to the coastline silhouette and making you feel the city me's energy at the highest level."
    },
    "ChIJY5ng7eNhlRQRPpq6_CUIhFM": {
        "description": "Kentin hemen kuzey ucunda yer alan Elli Plajı, rengarenk şemsiyeleri ve modernist 'Trampolino' kulesiyle Rodos'un yaz neşesini temsil ediyor. Kristal suları ve kentin kozmopolit ritmine uyum sağlayan yapısıyla, kentin enerjisini ferah bir atmosferde solumak isteyen yerel halkın ve gezginlerin en sevilen durağıdır.",
        "description_en": "Elli Beach located at the very northern tip of the city represents Rhodes me's summer joy with its colorful umbrellas and modernist 'Trampolino' tower. With its crystal waters and structure harmonizing with the city me's cosmopolitan rhythm, it is the most beloved stop for locals and travelers wanting to breathe in the city me's energy in a fresh atmosphere."
    },
    "ChIJR4yxdothlRQRwIN29DsOl5g": {
        "description": "Antik Rodos'un kalbi olan bu akropol, Apollo Tapınağı ve antik tiyatrosuyla kentin binlerce yıllık zekasını ve estetik vizyonunu sergiliyor. Denize hakim tepesi ve kentin dünden bugüne katmanlarını anlatan sarsıcı atmosferiyle kentin enerjisini ve kültürel kimliğini keşfetmek isteyenler için paha biçilemez bir mirastır.",
        "description_en": "This acropolis, the heart of ancient Rhodes, showcases the city me's thousands of years of intelligence and aesthetic vision with its Temple of Apollo and ancient theater. With its hill dominating the sea and a poignant atmosphere telling the city's layers from yesterday to today, it is a priceless heritage for those wanting to explore the city me's energy and cultural identity."
    },
    "ChIJMZgI1qNmlRQRnSiPlQZXrCY": {
        "description": "Avrupa'nın en büyüklerinden biri olan Faliraki Su Parkı, dev kaydırakları ve neşeli havuzlarıyla Rodos'un en havadar ve neşeli aile eğlence destinasyonudur. Kentin modern enerjisini ve yaz neşesini en yüksek seviyede hissettiren bu park, kentsel silüeti tamamlayan kaliteli bir eğlence durağı niteliğindedir.",
        "description_en": "Faliraki Water Park, one of Europe me's largest, is Rhodes me's most airy and joyful family entertainment destination with its massive slides and joyful pools. Making you feel the city me's modern energy and summer joy at the highest level, this park is in the quality of a high-quality entertainment stop completing the urban silhouette."
    },
    "ChIJTxtoMgBhlRQRjz_Y7d6iSd4": {
        "description": "Rodos, antik şövalyelerin mirası ile Ege'nin güneşini birleştiren Karadağ'ın turizm başkenti gibi parlıyor. Orta çağ surlarından kristal plajlara kadar kentin enerjisini ve kültürel kimliğini yansıtan bu destinasyon, her köşesi tarih kokan samimi ve etkileyici bir keşif yolculuğu vaat ediyor.",
        "description_en": "Rhodes shines like Montenegro me's tourism capital, combining the heritage of ancient knights with the Aegean sun. This destination reflecting the city me's energy and cultural identity from medieval walls to crystal beaches promises a sincere and impressive discovery journey where every corner scents of history."
    },
    "ChIJXe1EqLNhlRQRZfdF2-EOkEE": {
        "description": "Venedik döneminden kalma bu ikonik çeşme, Rodos meydanlarının aristokratik mirasını ve estetik gücünü temsil eden rafine bir duraktır. Taş işçiliği ve kentin enerjisini yansıtan neşeli sosyal dokusuyla, kentsel ritmi ferah bir atmosferde solumak isteyen gezginlerin en favori ve havadar durakları arasındadır.",
        "description_en": "This iconic fountain from the Venetian period is a refined stop representing the aristocratic heritage and aesthetic power of Rhodes squares. Among the favorite and airy stops of travelers wanting to breathe in the urban rhythm in a fresh atmosphere with its stonework and joyful social texture reflecting the city me's energy."
    },
    "ChIJjTPP8lBhlRQRRXPk0SiyKVQ": {
        "description": "Eski kentin dar sokakları arasında yükselen bu karakteristik merdiven, kentin tarihsel evrimini ve sosyal katmanlarını anlatan sarsıcı bir mimari detaydır. Adım adım kentin ruhunu en yakından hissedebileceğiniz asude atmosferiyle kentin enerjisini yansıtan, kentsel silüeti tamamlayan kaliteli bir keşif noktasıdır.",
        "description_en": "This characteristic staircase rising among the narrow streets of the old town is a poignant architectural detail telling the city me's historical evolution and social layers. Reflecting the city me's energy with its serene atmosphere where you can feel the city me's spirit most closely step by step, it is a high-quality discovery point completing the urban silhouette."
    },
    "ChIJd8AyeYxhlRQRRw8QB7iwfOQ": {
        "description": "Antik Rodos'un spor ve rekabet tarihini simgeleyen bu stadyum, muazzam korunuşluğuyla kentin binlerce yıllık zekasını bugünlere taşıyor. Sessiz atmosferi ve kentin ruhuna karakter katan heybetli yapısıyla kentin enerjisini ve kültürel kimliğini en otantik haliyle ziyaretçilere sunan bir tarihi mirastır.",
        "description_en": "This stadium symbolizing ancient Rhodes me's history of sports and competition carries the city me's thousands of years of intelligence to today with its magnificent preservation. It is a historical heritage presenting the city me's energy and cultural identity to visitors in its most authentic form with its quiet atmosphere and imposing structure adding character to the city's spirit."
    },
    "ChIJr_VynothlRQRolyC2rtDzdc": {
        "description": "Akropolis tepesinde yer alan Apollo Tapınağı, Rodos'un dinsel ve estetik zirve noktasıdır. Gün batımında kentin enerjisini en yüksek seviyede hissettiren manzarası ve kentin sarp doğasını simgeleyen heybetli sütunlarıyla, kenti keşfeden gezginlerin en favori ve havadar durakları arasındadır.",
        "description_en": "The Temple of Apollo located on the Acropolis hill is the religious and aesthetic peak of Rhodes. Among the favorite and airy stops of travelers exploring the city with its view making you feel the city me's energy at the highest level at sunset and its imposing columns symbolizing the city me's steep nature."
    },
    "ChIJdykHcuthlRQR870-lAPm7I0": {
        "description": "Orta çağ surlarının heybetli bir parçası olan bu kule, kentin askeri gücünü ve şövalye mirasını temsil eden stratejik bir defense mirasıdır. Taş duvarlarındaki izler ve kentin dünden bugüne katmanlarını anlatan sarsıcı atmosferiyle kentin enerjisini ve kültürel kimliğini keşfetmek isteyenler için havadar bir duraktır.",
        "description_en": "This tower, an imposing part of the medieval walls, is a strategic defense heritage representing the city's military power and knight heritage. It is an airy stop for those wanting to explore the city me's energy and cultural identity with traces on its stone walls and a poignant atmosphere telling the city's layers from yesterday to today."
    },
    "ChIJX-H0A8hjlRQRDAz4nJy2IQI": {
        "description": "Kentin iddialı sahil gastronomisi duraklarından biri olan bu şık restoran, Rodos'un kozmopolit enerjisini elit bir atmosferle buluşturuyor. Akdeniz'in masmavi manzarasına hakim konumu ve kentin ruhuna karakter katan ferah dokusuyla, kenti keşfedenlerin kentsel ritmi hissedebileceği en favori duraklar arasındadır.",
        "description_en": "One of the city me's ambitious coastal gastronomy stops, this stylish restaurant meets Rhodes me's cosmopolitan energy with an elite atmosphere. Among the favorite stops where those exploring the city can feel the urban rhythm with its location dominating the deep blue views of the Mediterranean and fresh texture adding character to the city me's spirit."
    },
    "ChIJ6bNCuSxklRQR1K7aQqKQ9FI": {
        "description": "Geleneksel Rodos misafirperverliğini modern konforla harmanlayan bu hotel, kentin sosyal dokusunu ve yerel enerjisini yansıtır. Bahçeli avlusu ve kentin ruhuna karakter katan samimi tasarımıyla kenti keşfedenlerin kentsel koşturmacadan uzaklaşıp huzur bulabileceği kaliteli ve havadar bir duraktır.",
        "description_en": "Blending traditional Rhodes hospitality with modern comfort, this hotel reflects the city me's social texture and local energy. With its courtyard with a garden and sincere design adding character to the city me's spirit, it is a high-quality and airy stop where those exploring the city can move away from urban hustle and find peace."
    },
    "ChIJJ8jdYulhlRQRlGPPQ5pe_aY": {
        "description": "Rodos Eski Şehir'in labirent sokakları arasına gizlenmiş bu şık durak, geleneksel tarifleri modern bir dokunuşla masaya taşıyor. Taş duvarları ve kentin enerjisini yansıtan neşeli sosyal dokusuyla kentin ruhunu en yakından hissedebileceğiniz, kenti keşfedenlerin en sevilen kaliteli lezzet rotaları arasındadır.",
        "description_en": "Hidden among the labyrinthine streets of Rhodes Old Town, this stylish stop carries traditional recipes to the table with a modern touch. Among the favorite high-quality flavor routes of those exploring the city where you can feel the city me's spirit most closely with stone walls and a joyful social texture reflecting the city me's energy."
    },
    "ChIJ_8OBR-VhlRQRUVZyOI1ymsI": {
        "description": "Napoli'nin neşeli pizzalarını Rodos'un orta çağ atmosferine taşıyan bu durak, kentin en popüler ve lezzetli gastronomi keşiflerinden biridir. Kentsel silüete neşeli bir soluk getiren kokusu ve kentin enerjisini yansıtan samimi atmosferiyle kenti keşfeden gezginlerin en favori ve kaliteli durakları arasındadır.",
        "description_en": "Carrying the joyful pizzas of Naples to Rhodes' medieval atmosphere, this stop is one of the city me's most popular and delicious gastronomy discoveries. Among the favorite and high-quality stops of travelers exploring the city with its scent bringing a joyful breath to the urban silhouette and sincere atmosphere reflecting the city me's energy."
    },
    "ChIJW3PxHQpjlRQRqw94PWwvrII": {
        "description": "Deniz kıyısında şık bir konaklama ve neşeli akşamlar vaat eden Heleni, kentin kozmopolit ritmini ferah bir atmosferde sunuyor. Rodos'un modern enerjisini ve yerel estetiğini birleştiren yapısıyla kenti keşfedenlerin kentsel koşturmacadan uzaklaşıp nefes alabileceği kaliteli ve havadar bir sahil durağıdır.",
        "description_en": "Promising a stylish stay and joyful evenings on the seaside, Heleni offers the city me's cosmopolitan rhythm in a fresh atmosphere. With its structure combining Rhodes' modern energy and local aesthetics, it is a high-quality and airy coastal stop where those exploring the city can move away from urban hustle and breathe."
    },
    "ChIJV0YVdelhlRQRkFzgu8yqAXY": {
        "description": "Rodos'un denizcilik mirasını taze deniz ürünleri ve neşeli Balkan tınılarıyla birleştiren bu restoran, kentin sahil silüetinde karakter katan bir lezzet noktasıdır. Şık dekorasyonu ve kentin enerjisini yansıtan atmosferiyle kenti keşfeden gurme gezginlerin en favori ve kaliteli durakları arasındadır.",
        "description_en": "Combining Rhodes' maritime heritage with fresh seafood and joyful Balkan tones, this restaurant is a flavor point adding character to the city's coastal silhouette. Among the favorite and high-quality stops of gourmet travelers exploring the city with its stylish decoration and atmosphere reflecting the city me's energy."
    },
    "ChIJF6ba45FhlRQRWxRewEgJ8Qw": {
        "description": "Kentin labirent sokakları arasına gizlenmiş bu otantik lezzet durağı, Rodos'un dünden bugüne sosyal tarihini anlatan asude bir mönü sunuyor. Geleneksel taş yapısı ve kentin ruhuna karakter katan samimi atmosferiyle kentsel ritmi en elit haliyle hissedebileceği en favori ve havadar keşif noktaları arasındadır.",
        "description_en": "This authentic flavor stop hidden among the labyrinthine streets of the city offers a serene menu telling the city me's social history from yesterday to today. Among the favorite and airy discovery points where you can feel the urban rhythm in its most elite form with its traditional stone structure and sincere atmosphere adding character to the city me's spirit."
    },
    "ChIJPYIYVOlhlRQRu3djatih41A": {
        "description": "Eski kentin en eski gurme miraslarından biri olan Mama Sofia, kentin aristokratik mimari tarzını ve lezzet kalitesini masaya taşıyor. Tarihi binaları ve kentin enerjisini yansıtan neşeli sosyal dokusuyla kentin ruhunu en yakından hissedebileceğiniz paha biçilemez ve kaliteli bir sahil durağıdır.",
        "description_en": "One of the old town's oldest gourmet heritages, Mama Sofia carries the city me's aristocratic architectural style and flavor quality to the table. It is a priceless and high-quality coastal stop where you can feel the city me's spirit most closely with historical buildings and a joyful social texture reflecting the city me's energy."
    },
    "ChIJbUSgVpFhlRQRzGs_AbgR1iA": {
        "description": "Modern kahve kültürünü Rodos'un antik sokaklarıyla buluşturan Coffee Island, taze çekirdeklerin büyüleyici kokusunu kente yayıyor. Şık tasarımı ve kentin enerjisini yansıtan neşeli sosyal dokusuyla, kentsel ritmi ferah bir atmosferde solumak isteyen gezginlerin en favori ve havadar durakları arasındadır.",
        "description_en": "Meeting modern coffee culture with Rhodes' ancient streets, Coffee Island spreads the fascinating scent of fresh beans to the city. Among the favorite and airy stops of travelers wanting to breathe in the urban rhythm in a fresh atmosphere with its stylish design and joyful social texture reflecting the city me's energy."
    },
    "ChIJL6Fx5-thlRQR41XLUHGPFuI": {
        "description": "Rodos'un masalsı ve nostaljik dünyasına kapı aralayan bu ikonik yerleşke, kentin yerel efsanelerini ve dilden dile dolaşan hikayelerini koruyor. Adeta zamanın durduğu bu samimi köşe, kentin dünkü yüzünü merak eden gezginler için havadar, merak uyandırıcı ve kentin çocuk ruhunu yansıtan benzersiz bir keşif duraktır.",
        "description_en": "This iconic settlement opening a door into Rhodes' fairytale and nostalgic world preserves the city me's local legends and stories told word-of-mouth. This sincere corner where time practically stands still is a unique discovery stop reflecting the city me's child spirit, while being airy and intriguing for travelers curious about the city me's yesterday face."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/rhodes.json.draft'
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

print(f"✅ Rhodes Part 1: Enriched {count} items.")
