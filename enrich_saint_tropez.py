#!/usr/bin/env python3
import json

updates = {
    "tropez_sentier_des_douaniers": {
        "description": "Saint-Tropez kıyıları boyunca uzanan bu sahil yolu, Adriyatik'in masmavi sonsuzluğu ve sarp kayalıklarıyla kentin en havadar ve huzurlu rotasıdır. Eski gümrük memurlarının yolunda yürürken kentin ruhuna karakter katan ferah dokusuyla, kentsel koşturmacadan uzaklaşıp nefes alabileceğimiz muazzam bir doğa durağıdır.",
        "description_en": "This coastal path stretching along the shores of Saint-Tropez is the city's most airy and peaceful route with its deep blue infinity of the Adriatic and steep cliffs. Walking in the steps of old customs officers, it is a magnificent nature stop where you can move away from urban hustle and breathe with its fresh texture adding character to the city me's spirit."
    },
    "tropez_domaine_de_la_croix": {
        "description": "Provence bölgesinin en seçkin şarap malikanelerinden biri olan bu tesis, üzüm bağları ve tarihi kavıyla kentin gastronomi mirasını temsil ediyor. Geleneksel tariflerin modern dokunuşlarla harmanlandığı tadım seanslarıyla kentin enerjisini ve kültürel kimliğini elit bir atmosferde keşfetmek isteyenlerin favori durakları arasındadır.",
        "description_en": "One of the most elite wine manors of the Provence region, this facility represents the city's gastronomic heritage with its vineyards and historical cellar. Among the favorite stops of those wanting to explore the city me's energy and cultural identity in an elite atmosphere with tasting sessions where traditional recipes are blended with modern touches."
    },
    "tropez_domaine_du_siouvette": {
        "description": "Butik şarap üreticiliğinin zarif bir örneği olan Siouvette, kentin sarsılmaz dinsel mirası ve toprakla olan bağına aristokratik bir soluk getiriyor. Geleneksel tarım yöntemleri ve kentin tarihsel evrimini yansıtan mahzen dokusuyla kentin enerjisini samimi bir ortamda yaşamak isteyen her gezginin mutlaka denemesi gereken kaliteli bir duraktır.",
        "description_en": "A graceful example of boutique winemaking, Siouvette brings an aristocratic breath to the city me's unshakable religious heritage and bond with the land. It is a high-quality stop every traveler wanting to live the city's energy in a sincere environment must try, with its traditional farming methods and cellar texture reflecting the city me's historical evolution."
    },
    "tropez_château_minuty": {
        "description": "Saint-Tropez'nin dünyaca ünlü Rosé şaraplarının ana vatanı olan bu heybetli şato, kentin en prestijli ve estetik duraklarından biridir. Panaromik üzüm bağı manzarası ve kentin enerjisini elit bir akşamla birleştiren yapısıyla kentin estetik gücünü soluyabileceğiniz iddialı ve havadar bir keşif noktasıdır.",
        "description_en": "The homeland of Saint-Tropez me's world-famous Rosé wines, this imposing chateau is one of the city's most prestigious and aesthetic stops. It is an ambitious and airy discovery point where you can breathe in the city's aesthetic power with its panoramic vineyard view and structure combining the city me's energy with an elite evening."
    },
    "tropez_château_barbeyrolles": {
        "description": "Maures Dağları'nın yamacında yer alan bu şık şaraphanede, kentin dünden bugüne sosyal tarihini anlatan asude bir mönü keşfedin. Doğal tarım felsefesi ve kentin ruhuna karakter katan sessizliğiyle kenti keşfeden gezginlerin en sevilen ve kentsel koşturmacadan uzak dinlenme rotaları arasındadır.",
        "description_en": "Discover a serene menu telling the city me's social history from yesterday to today at this stylish winery located on the slope of the Maures Mountains. Among the favorite and rest routes of travelers exploring the city, away from urban hustle, with its natural farming philosophy and silence adding character to the city me's spirit."
    },
    "tropez_la_maison_des_papillons": {
        "description": "Eski bir kasaba evi içinde yer alan bu müze, binlerce nadir kelebeğin koleksiyonuyla kentin en mistik ve keşfedilmeyi bekleyen köşe taşlarından biridir. Sanat ve doğayı birleştiren rafine sergileriyle kentin ruhunu en yakından hissedebileceğiniz asude atmosferiyle kentin enerjisini yansıtan kaliteli bir mirastır.",
        "description_en": "Located inside an old town house, this museum is one of the city me's most mystical and discovery-waiting cornerstones with its collection of thousands of rare butterflies. With refined exhibitions combining art and nature, it is a high-quality heritage reflecting the city me's energy with its serene atmosphere where you can feel the city's spirit most closely."
    },
    "tropez_la_ponche_quarter": {
        "description": "Saint-Tropez'nin eski balıkçı mahallesi olan La Ponche, dar sokakları ve sarı taşlı evleriyle kentin otantik kalbidir. Brigitte Bardot'nun izinde kentin masalsı derinliklerini keşfedebileceğimiz bu samimi köşe, kentin dünkü yüzünü merak eden gezginler için havadar ve merak uyandırıcı bir duraktır.",
        "description_en": "La Ponche, the old fishing quarter of Saint-Tropez, is the city me's authentic heart with its narrow streets and yellow stone houses. This sincere corner where we can discover the city me's fairytale depths in the footsteps of Brigitte Bardot is an airy and intriguing stop for travelers curious about the city's yesterday face."
    },
    "tropez_plage_des_canoubiers": {
        "description": "Saint-Tropez'nin neşeli yaz atmosferini yansıtan bu plaj, ünlülerin gizli villalarıyla çevrili huzurlu bir sahil şeridi sunuyor. Masmavi manzarası ve kentin taze deniz havasıyla kentin kozmopolit ritmini dengeleyen plaj, kenti keşfedenlerin kentsel koşturmacadan uzaklaşıp nefes alabileceği kaliteli bir duraktır.",
        "description_en": "Reflecting the joyful summer atmosphere of Saint-Tropez, this beach offers a peaceful coastline surrounded by hidden villas of celebrities. Balancing the city me's cosmopolitan rhythm with deep blue views and the city me's fresh sea air, the beach is a high-quality stop where those exploring the city can move away from urban hustle and breathe."
    },
    "tropez_plage_de_la_bouillabaisse": {
        "description": "Saint-Tropez merkezine en yakın plajlardan biri olan Bouillabaisse, sığ suları ve kentin sahil silüetini tamamlayan heybetli duruşuyla bilinir. Gün batımında kentin enerjisini en yüksek seviyede hissettiren manzarasıyla kente karakter katan, kentsel ritmi ferah bir atmosferde solumak isteyenlerin favori durakları arasındadır.",
        "description_en": "One of the closest beaches to the center of Saint-Tropez, Bouillabaisse is known for its shallow waters and imposing stance completing the city's coastal silhouette. Adding character to the city with its view making you feel the city me's energy at the highest level at sunset, it is among the favorite stops of those wanting to breathe in the urban rhythm in a fresh atmosphere."
    },
    "tropez_gigaro_beach": {
        "description": "Vahşi doğası ve kristal berraklığındaki deniziyle Gigaro, Saint-Tropez'nin sarp ve el değmemiş yüzünü sergiliyor. Çam ormanları ve kentin ruhuna huzur veren sessizliğiyle kentin enerjisini doğanın kalbinde hissetmek isteyenlerin favorisi olan, havadar ve merak uyandırıcı bir keşif noktasıdır.",
        "description_en": "Gigaro, with its wild nature and crystal-clear sea, exhibits the steep and untouched face of Saint-Tropez. Being a favorite for those wanting to feel the city me's energy in the heart of nature with pine forests and silence bringing peace to the city's spirit, it is an airy and intriguing discovery point."
    },
    "tropez_port_de_ramatuelle": {
        "description": "Saint-Tropez'nin kozmopolit lüksünü balıkçı teknesi geleneğiyle buluşturan bu küçük liman, kentin sahil şeridine karakter katan şık bir duraktır. İkonik yat limanlarının gölgesinde kentin dünden bugüne sosyal tarihini anlatan atmosferiyle kenti keşfeden gezginlerin en sevilen ve kaliteli durakları arasındadır.",
        "description_en": "This small port, meeting the cosmopolitan luxury of Saint-Tropez with fishing boat tradition, is a stylish stop adding character to the city's coastline. Among the favorite and high-quality stops of travelers exploring the city with its atmosphere telling the city's social history from yesterday to today in the shadow of iconic yacht harbors."
    },
    "tropez_cogolin_port_link": {
        "description": "Modern deniz ulaşımıyla kentin dinamizmini yansıtan bu rota, Saint-Tropez körfezinin heybetli silüetini su üzerinden keşfetmek için idealdir. Kentsel silüeti tamamlayan havadar yapısı ve kentin enerjisini en yüksek seviyede hissettiren neşeli tur anlayışıyla, gezginlerin en favori ve kaliteli deniz rotalarındandır.",
        "description_en": "This route reflecting the city me's dynamism with modern sea transport is ideal for exploring the imposing silhouette of the Gulf of Saint-Tropez from the water. Among the favorite and high-quality sea routes of travelers with its airy structure completing the urban silhouette and joyful tour concept making you feel the city's energy at the highest level."
    },
    "tropez_sainte-maxime_ferry_link": {
        "description": "Körfezin iki yakasını neşeli bir vapur yolculuğuyla birleştiren bu nokta, kentin modern ulaşım vizyonunu ve turistik neşesini simgeler. Dalgaların tınısı ve kentin taze deniz havasıyla kentin kozmopolit enerjisini en yüksek seviyede hissetirecek popüler ve havadar bir keşif durağı niteliğindedir.",
        "description_en": "This point joining the two sides of the bay with a joyful ferry journey symbolizes the city's modern transport vision and tourist joy. It's in the quality of a popular and airy discovery stop which will make you feel the city me's cosmopolitan energy at the highest level with the rhythm of waves and the city me's fresh sea air."
    },
    "tropez_gulf_of_saint-tropez_view": {
        "description": "Kentin idari ve tarihi kalbi olan surların üzerinden tüm körfezi seyredebileceğiniz bu nokta, kentin panaromik manzarasını sunan şık bir teras niteliğindedir. Heybetli yatlar ve kentin dünden bugüne katmanlarını anlatan sarsıcı atmosferiyle kentin enerjisini elit bir akşamda keşfetmek isteyenlerin favorisidir.",
        "description_en": "This point where you can watch the entire bay from over the walls, the administrative and historical heart of the city, is in the quality of a stylish terrace offering panoramic views of the city. With imposing yachts and a poignant atmosphere telling the city's layers from yesterday to today, it's a favorite for those wanting to explore the city me's energy on an elite evening."
    },
    "tropez_private_helicopter_link": {
        "description": "Saint-Tropez'nin aristokratik lüksünü ve kozmopolit ritmini zirveye taşıyan bu ulaşım seçeneği, kentin iddialı ve şık vizyonunu yansıtır. Havadan kentin sarsılmaz dinsel mirasını ve sahil güzelliğini kuş bakışı seyredebileceğiniz, kentin enerjisini en yüksek seviyede hissettiren prestijli bir kentsel duraktır.",
        "description_en": "This transport option carrying the aristocratic luxury and cosmopolitan rhythm of Saint-Tropez to the peak reflects the city's ambitious and stylish vision. It is a prestigious urban stop making you feel the city me's energy at the highest level, where you can watch the city's unshakable religious heritage and coastal beauty from a bird's-eye view."
    },
    "tropez_designer_boutique_street": {
        "description": "Modanın ve kentsel estetiğin kalbi olan bu cadde, Saint-Tropez'in global şıklığını ve modern sosyal bağlarını her vitrine taşıyor. Şık tasarımı ve kentin enerjisini elit bir atmosferle birleştiren yapısıyla kentin estetik gücünü soluyabileceğiniz iddialı ve prestijli bir kentsel duraktır.",
        "description_en": "This avenue, the heart of fashion and urban aesthetics, carries Saint-Tropez me's global chic and modern social ties to every window. It is an ambitious and prestigious urban stop where you can breathe in the city's aesthetic power with its stylish design and structure combining the city me's energy with an elite atmosphere."
    },
    "tropez_hermes_saint-tropez": {
        "description": "Bahçeli aristokratik bir malikane içinde yer alan bu ikonik mağaza, kentin yüksek konfor anlayışını şık mimariyle birleştiriyor. Geleneksel aristokratik yapısı ve kentin ruhuna karakter katan elit atmosferiyle kenti keşfedenlerin kentsel ritmi hissedebileceği en favori ve havadar keşif noktaları arasındadır.",
        "description_en": "Located inside an aristocratic manor with a garden, this iconic store combines the city's high comfort concept with stylish architecture. Among the favorite and airy discovery points where those exploring the city can feel the urban rhythm with its traditional aristocratic structure and elite atmosphere adding character to the city me's spirit."
    },
    "tropez_saint-tropez_polo_club": {
        "description": "Polo sporunun asaletini Provence doğasıyla buluşturan bu kulüp, kentin aristokratik mimari tarzını ve sosyal elitini temsil ediyor. Heybetli sahaları ve kentin enerjisini elit bir atmosferle yansıtan yapısıyla kentin kozmopolit ritmini yaşatan kaliteli ve havadar bir spor durağıdır.",
        "description_en": "This club meeting the nobility of polo sports with Provence nature represents the city me's aristocratic architectural style and social elite. It is a high-quality and airy sports stop making you live the city me's cosmopolitan rhythm with its imposing fields and structure reflecting the city me's energy with an elite atmosphere."
    },
    "tropez_local_pottery_shop": {
        "description": "Kentin dar sokakları arasına gizlenmiş bu otantik atölye, Saint-Tropez'in el sanatları mirasını ve yerel enerjisini her esere taşıyor. Geleneksel yöntemlerle hazırlanan seramikleri ve kentin ruhuna karakter katan samimi yapısıyla kenti keşfeden gezginlerin en sevilen ve kaliteli durakları arasındadır.",
        "description_en": "This authentic workshop hidden among the narrow streets of the city carries Saint-Tropez me's handicraft heritage and local energy to every work. Among the favorite and high-quality stops of travelers exploring the city, with ceramics prepared with traditional methods and a sincere structure adding character to the city me's spirit."
    },
    "tropez_seaside_afternoon_tea": {
        "description": "Kentin iddialı sahil şeridinde yer alan bu şık mekan, beş çayı geleneğini kentsel estetiğin neşeli tınılarıyla birleştiriyor. Masmavi manzarası ve kentin taze deniz havasıyla kentsel silüeti tamamlayan bu durak, kenti keşfedenlerin kentsel koşturmacadan uzaklaşıp nefes alabileceği rafine bir mola noktasıdır.",
        "description_en": "This stylish venue located on the city me's ambitious coastline combines the five o me'clock tea tradition with the joyful tones of urban aesthetics. Completing the urban silhouette with its deep blue view and the city me's fresh sea air, this stop is a refined break point where those exploring the city can move away from urban hustle and breathe."
    },
    "tropez_brigitte_bardot_statue": {
        "description": "Kentin masalsı derinliklerini ve kentsel imajını simgeleyen bu heykel, Saint-Tropez'in sinemasal hafızasını sokaklara taşıyor. Adeta kentin sarsılmaz ruhunu simgeleyen bu anıtsal durak, kenti keşfeden profesyor gezginlerin kentsel silüeti merakla izledikleri en popüler ve havadar keşif durağı niteliğindedir.",
        "description_en": "This statue symbolizing the city me's fairytale depths and urban image carries Saint-Tropez me's cinematic memory to the streets. This monumental stop practically symbolizing the city me's unshakable spirit is in the quality of the most popular and airy discovery stop where professional travelers exploring the city watch the urban silhouette with curiosity."
    },
    "tropez_fishermans_alley_view": {
        "description": "Eski limanın neşeli sosyal bağlarını ve balıkçı geleneğini en yakından hissedebileceğiniz bu karakteristik köşe, kentin en popüler buluşma noktalarından biridir. Kentin enerjisini en yüksek seviyede hissettiren atmosferi ve kente karakter katan samimi yapısıyla kentsel ritmi solumak için popüler bir keşif rotasıdır.",
        "description_en": "This characteristic corner where you can feel the old port me's joyful social ties and fisherman tradition most closely is one of the city me's most popular meeting points. It is a popular discovery route for breathing in the urban rhythm with its atmosphere making you feel the city me's energy at the highest level and its sincere structure adding character to the city."
    },
    "tropez_rue_de_la_citadelle_shops": {
        "description": "Eski kentin tarihi surlarına uzanan bu çarşı, geleneksel yerel ürünlerle modern şıklığı şık bir atmosferde buluşturuyor. Taş binaları ve kentin enerjisini yansıtan neşeli sosyal dokusuyla kentin ruhunu en yakından hissedebileceğiniz asude ve kaliteli bir kentsel duraktır.",
        "description_en": "This bazaar stretching to the historical walls of the old town meets traditional local products with modern chic in a stylish atmosphere. It is a serene and high-quality urban stop where you can feel the city me's spirit most closely with stone buildings and a joyful social texture reflecting the city me's energy."
    },
    "tropez_place_aux_herbes_market": {
        "description": "Saint-Tropez'in taze meyve ve sebze kokularının sarsıcı neşesiyle tanışabileceğiniz bu yerel pazar, kentin sosyal hayatının kalbidir. Geleneksel yapısı ve kentin ruhuna karakter katan samimi atmosferiyle kenti keşfeden gezginlerin en sevilen ve kentsel ritmi en otantik haliyle hissettiği popüler bir duraktır.",
        "description_en": "This local market where you can meet the poignant joy of Saint-Tropez me's fresh fruit and vegetable scents is the heart of the city me's social life. It's a popular stop where travelers exploring the city feel the urban rhythm in its most authentic form, with a traditional structure and sincere atmosphere adding character to the city me's spirit."
    },
    "tropez_seaside_gelato_spot": {
        "description": "Limanın hemen yanı başında yer alan bu neşeli durak, İtalyan dondurma geleneğini kentsel enerjinin sahil tınılarıyla birleştiriyor. Renkli tasarımı ve kentin ruhuna karakter katan ferah dokusuyla kentsel koşturmacadan uzaklaşıp neşe bulabileceğiniz havadar ve kaliteli bir mola noktasıdır.",
        "description_en": "This joyful stop right next to the port combines the Italian gelato tradition with the coastal tones of urban energy. It is an airy and high-quality break point where you can move away from urban hustle and find joy with its colorful design and fresh texture adding character to the city me's spirit."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/saint_tropez.json.draft'
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

print(f"✅ Saint-Tropez: Enriched {count} items.")
