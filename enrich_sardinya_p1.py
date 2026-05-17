#!/usr/bin/env python3
import json

updates = {
    "sard_alghero_old_town": {
        "description": "Katalan etkileri taşıyan dar sokakları ve sarı taşlı surlarıyla Alghero Eski Kent, Sardinya'nın en romantik ve karakteristik köşelerinden biridir. Denize hakim surları üzerinde yürüyüş yaparken kentin asude tarihini soluyabileceğiniz, her köşesi tarih ve deniz kokan samimi bir duraktır.",
        "description_en": "With its narrow streets bearing Catalan influences and yellow stone walls, Alghero Old Town is one of Sardinia's most romantic and characteristic corners. It is a sincere stop full of history and the scent of the sea where you can breathe in the city me's serene history while walking on its walls dominating the sea."
    },
    "sard_la_pelosa_beach": {
        "description": "Sardinya'nın kuzeybatı ucunda yer alan La Pelosa, sığ turkuaz suları ve bembeyaz kumlarıyla bir tropikal cenneti andırır. Karşısındaki tarihi kule manzarasıyla bildiğimiz bu plaj, Akdeniz'in en berrak sularında yüzmek ve doğanın eşsiz renklerine tanıklık etmek için kentin en prestijli sahil duraklarından biridir.",
        "description_en": "Located at the northwestern tip of Sardinia, La Pelosa resembles a tropical paradise with its shallow turquoise waters and pure white sands. Known for its historical tower view opposite, this beach is one of the city's most prestigious coastal stops for swimming in the Mediterranean's clearest waters and witnessing nature's unique colors."
    },
    "sard_castelsardo_hilltop": {
        "description": "Denize dimdik inen bir kayalık üzerinde kurulu bu orta çağ kasabası, kentin heybetli kalesi ve renkli evleriyle büyüleyici bir silüet sunuyor. El sanatları ve zengin tarihiyle kentin ruhunu en yakından hissedebileceğiniz bu hilltop noktası, kentin kozmopolit enerjisinden uzaklaşıp adanın otantik yüzünü keşfetmek için idealdir.",
        "description_en": "This medieval town, built on a cliff dropping steeply into the sea, offers a fascinating silhouette with the city's grand castle and colorful houses. This hilltop spot where you can feel the city me's spirit most closely with crafts and rich history is ideal for escaping the city's cosmopolitan energy and exploring the island's authentic face."
    },
    "sard_santa_teresa_gallura_port": {
        "description": "Sardinya'nın en kuzey noktasında yer alan bu liman şehri, granit kayalıkları ve Korsika'ya bakan panaromik manzarasıyla ünlüdür. Hareketli limanı, şık kafeleri ve kentin taze deniz havasıyla karakter katan bu bölge, kenti keşfeden gezginlerin en sevilen ve havadar duraklarından biridir.",
        "description_en": "This port city at the northernmost point of Sardinia is famous for its granite cliffs and panoramic views facing Corsica. This area adding character with its vibrant harbor, stylish cafes, and fresh sea air is one of the most beloved and airy stops for travelers exploring the city."
    },
    "sard_porto_cervo_marina": {
        "description": "Lüks ve ihtişamın merkezi olan Porto Cervo Marina, Sardinya'nın en prestijli yat limanlarından biri olarak kentin ekonomik ve sosyal elitini bir araya getirir. Modern tasarımı, şık butikleri ve pırıltılı Akdeniz akşamlarıyla kentin kozmopolit enerjisini ve kültürel nabzını en yüksek seviyede hissedebileceğiniz bir duraktır.",
        "description_en": "The center of luxury and grandeur, Porto Cervo Marina gathers the city's economic and social elite as one of Sardinia's most prestigious yacht harbors. It is a stop where you can feel the city's cosmopolitan energy and cultural pulse at the highest level with modern design, stylish boutiques, and sparkling Mediterranean evenings."
    },
    "sard_san_teodoro_coast": {
        "description": "Kristal suları ve geniş kumsallarıyla tanınan bu sahil kasabası, Sardinya'nın en hareketli ve neşeli yaz merkezlerinden biridir. Pembe flamingoların görülebileceği lagünü ve bembeyaz kumlu plajlarıyla kentin haritasına karakter katan bu nokta, hem huzur hem de eğlence arayanlar için muazzam bir seçimdir.",
        "description_en": "Known for its crystal waters and wide sandy beaches, this coastal town is one of Sardinia's most vibrant and joyful summer centers. This spot adding character to the city map with its lagoon where pink flamingos can be seen and its pure white sandy beaches is a magnificent choice for those seeking both peace and fun."
    },
    "sard_orosei_historic_center": {
        "description": "Tarihi taş binaları ve dar sokaklarıyla Orosei, Sardinya'nın otantik iç kesim yaşantısını şık bir atmosferde sunuyor. Kiliseleri, yerel sanat galerileri ve kentin dünden bugüne sosyal tarihini anlatan sergileriyle kentin ruhunu en yakından hissedebileceğiniz, kentin enerjisini ve kültürel kimliğini yansıtan sessiz bir mirastır.",
        "description_en": "With its historical stone buildings and narrow streets, Orosei offers Sardinia's authentic interior life in a stylish atmosphere. It is a quiet heritage reflecting the city me's energy and cultural identity where you can feel the city me's spirit most closely with churches, local art galleries, and exhibitions telling the city's social history from yesterday to today."
    },
    "sard_cala_gonone_bay": {
        "description": "Sarp kayalıkların ve zümrüt yeşili denizin buluştuğu bu körfez, Sardinya'nın en vahşi ve büyüleyici doğa harikalarından biridir. Sadece tekneyle ulaşılabilen gizli koyları ve etkileyici mağaralarıyla kentin enerjisini ve kültürel kimliğini yansıtan, kenti keşfeden gezginlerin en sevilen ve ilham verici duraklarından biridir.",
        "description_en": "This bay where steep cliffs and emerald green sea meet is one of Sardinia's wildest and most fascinating natural wonders. With hidden coves and impressive caves accessible only by boat, it is one of the most beloved and inspiring stops reflecting the city's energy and cultural identity."
    },
    "sard_bosa_colorful_streets": {
        "description": "Temo Nehri kıyısında pastel renkli evleriyle masalsı bir görüntü sunan Bosa, Sardinya'nın en karakteristik ve sanatsal kasabalarından biridir. Sarp yokuşları, tarihi kalesi ve kentin ruhunu en yakından hissedebileceğiniz bohem atmosferiyle kentin enerjisini ve kültürel kimliğini yansıtan rafine bir duraktır.",
        "description_en": "Offering a fairytale image with pastel-colored houses on the banks of the Temo River, Bosa is one of Sardinia's most characteristic and artistic towns. It is a refined stop reflecting the city me's energy and cultural identity with steep slopes, its historical castle, and a bohemian atmosphere where you can feel the city's spirit most closely."
    },
    "sard_carloforte_island": {
        "description": "San Pietro Adası üzerinde yer alan bu kasaba, Ceneviz kökenli sakinleri ve kendine has mimarisiyle Sardinya içinde adeta bir başka dünyadır. Renkli sokakları ve kentin haritasına karakter katan özgün kültürüyle kenti keşfeden gezginlerin en sevilen ve kentin enerjisini en yüksek seviyede hissettiği havadar duraklardandır.",
        "description_en": "Located on San Pietro Island, this town is practically another world within Sardinia with its Genoese-origin residents and unique architecture. It's among the favorite airy stops of travelers exploring the city with its colorful streets and unique culture adding character to the city map, where they feel the city me's energy at the highest level."
    },
    "sard_nora_archaeological_area": {
        "description": "Denizin hemen kıyısında yer alan bu antik kent, Sardinya'nın Fenike ve Roma dönemlerine ait paha biçilemez katmanlarını sergiliyor. Sular altında kalan antik limanı, mozaikleri ve kentin bir dönemine damga vuran tiyatrosuyla kentin geçmişteki deniz ticareti gücünü ve estetik vizyonunu simgeleyen etkileyici bir mirastır.",
        "description_en": "This ancient city located right on the seaside exhibits Sardinia's priceless layers from Phoenician and Roman periods. With its underwater ancient harbor, mosaics, and theater that marked an era, it is an impressive heritage symbolizing the city's past maritime trade power and aesthetic vision."
    },
    "sard_villasimius_turquoise": {
        "description": "Sardinya'nın güneydoğu kıyısında yer alan Villasimius, turkuaz suları ve granit kayalıklarıyla kentin en havalı yaz duraklarından biridir. Deniz rezervleri ve zengin su altı dünyasıyla kentin haritasına karakter katan bu bölge, kenti keşfeden gezginlerin en sevilen ve kaliteli sahil rotaları arasındadır.",
        "description_en": "Located on Sardinia me's southeastern coast, Villasimius is one of the city's coolest summer stops with its turquoise waters and granite cliffs. This area adding character to the city map with marine reserves and a rich underwater world is among the most beloved and high-quality coastal routes for travelers exploring the city."
    },
    "sard_cagliari_castello": {
        "description": "Kentin ana tepesinde yükselen tarihi Castello bölgesi, heybetli surları ve orta çağdan kalma kuleleriyle kentin idari ve tarihi kalbidir. Katedrali, dar sokakları ve kentin panaromik manzarasını sunan teraslarıyla kentin enerjisini ve kültürel kimliğini yansıtan, kenti keşfedenlerin en heyecan verici duraklarından biridir.",
        "description_en": "The historical Castello district rising on the city's main hill is the administrative and historical heart of the city with its imposing walls and medieval towers. With its cathedral, narrow streets, and terraces offering panoramic city views, it's one of the most exciting stops reflecting the city me's energy and cultural identity."
    },
    "sard_su_nuraxi_di_barumini": {
        "description": "UNESCO Dünya Mirası listesinde yer alan bu devasa Nuragik kompleksi, Sardinya'nın tarih öncesi mühendislik dehasının en görkemli kanıtıdır. Mistik taş yapıları ve binlerce yıllık sessizliğiyle adanın gizemli köklerini ve kültürel gücünü keşfetmek isteyenler için havadar, sakin ve bilgilendirici bir paha biçilemez hazinedir.",
        "description_en": "This massive Nuragic complex, a UNESCO World Heritage site, is the grandest proof of Sardinia's prehistoric engineering genius. With mystical stone structures and thousands of years of silence, it is an airy, quiet, and informative priceless treasure for those wanting to explore the island's mysterious roots and cultural power."
    },
    "sard_nuraghe_santu_antine": {
        "description": "Sardinya'nın en heybetli Nuragik yapılarından biri olan Santu Antine, 'Nuragik Saray' olarak da bilinir ve mimari detaylarıyla hayranlık uyandırır. Görkemli taş kulesi ve sofistike tasarım anlayışıyla adanın antik askeri gücünü ve estetik vizyonunu simgeleyen, tarihin derinliklerini keşfedenlerin favori duraklarından biridir.",
        "description_en": "One of Sardinia's most imposing Nuragic structures, Santu Antine is also known as the 'Nuragic Palace' and inspires admiration with its architectural details. Symbolizing the island's ancient military power and aesthetic vision with its grand stone tower and sophisticated design concept, it's one of the favorite stops for those exploring the depths of history."
    },
    "sard_nuraghe_palmavera": {
        "description": "Alghero yakınlarında yer alan bu antik yerleşke, Sardinya'nın yerli halklarının binlerce yıl önceki sosyal hayatına ve mimari dehasına ışık tutuyor. Geleneksel yapısı ve kentin dünden bugüne sosyal tarihini anlatan sergileriyle kentin ruhunu en yakından hissedebileceğiniz, kentin enerjisini yansıtan samimi bir arkeolojik duraktır.",
        "description_en": "Located near Alghero, this ancient settlement sheds light on the social life and architectural genius of Sardinia's indigenous people thousands of years ago. It is a sincere archaeological stop reflecting the city me's energy where you can feel the city's spirit most closely with its traditional structure and exhibitions telling the city's social history from yesterday to today."
    },
    "sard_nuraghe_arrubiu": {
        "description": "Bölgedeki tek beş kuleli Nuragik yapı olan Arrubiu, kızıl taşlarıyla bilinen ve adanın en büyük antik komplekslerinden biridir. Heybetli yapısı ve kentin tarihsel evrimini yansıtan taş dokusuyla kentin askeri tarihine ve mistik geçmişine tanıklık edebileceğiniz, keşfedilmeyi bekleyen bir kültürel hazinedir.",
        "description_en": "Arrubiu, the only five-towered Nuragic structure in the region, is known for its reddish stones and is one of the island's largest ancient complexes. It is a cultural treasure waiting to be discovered, where you can witness the city's military history and mystical past with its imposing structure and stone texture reflecting the city's historical evolution."
    },
    "sard_nuraghe_losa": {
        "description": "Mükemmel korunmuş bazalt yapısıyla Nuraghe Losa, Sardinya'nın tarih öncesi dönemlerdeki savunma stratejilerini ve kentsel otoritesini yansıtan bir başyapıttır. Sessiz atmosferi ve görkemli duruşuyla kentin kozmopolit kalabalığından uzaklaşıp tarihin fısıltılarını soluyabileceğiniz paha biçilemez ve kutsal bir keşif durağıdır.",
        "description_en": "With its perfectly preserved basalt structure, Nuraghe Losa is a masterpiece reflecting Sardinia's defense strategies and urban authority in prehistoric periods. It is a priceless and sacred discovery stop where you can move away from the cosmopolitan crowds and breathe in the whispers of history with its quiet atmosphere and grand stance."
    },
    "sard_nuraghe_la_prisgiona": {
        "description": "Gallura bölgesinin kalbinde yer alan bu antik köy, Sardinya'nın Nuragik dönemindeki toplumsal yapısını ve tarım kültürünü en canlı haliyle sergiliyor. Geleneksel taş işçiliği ve kentin enerji dolu geçmişiyle kentin haritasına karakter katan bu bölge, kenti keşfedenlerin en sevilen ve bilgilendirici mirası arasındadır.",
        "description_en": "Located in the heart of the Gallura region, this ancient village exhibits Sardinia's social structure and agricultural culture during the Nuragic period in its most vivid form. This area adding character to the city map with traditional stonework and the city's energy-filled past is among the most beloved and informative heritage sites for those exploring the city."
    },
    "sard_sanctuary_of_santa_cristi": {
        "description": "Dünyanın en iyi korunmuş antik su tapınaklarından biri olan Santa Cristina, kusursuz geometrisi ve mistik atmosferiyle kentin inanç turizmindeki en önemli duraklarından biridir. Binlerce yıllık sessizliği ve matematiksel dehasıyla kentin ruhani derinliğini ve estetik gücünü yansıtan rafine ve havadar bir keşif noktasıdır.",
        "description_en": "One of the best-preserved ancient water temples in the world, Santa Cristina is one of the most important stops in the city me's faith tourism with its flawless geometry and mystical atmosphere. It is a refined and airy discovery point reflecting the city's spiritual depth and aesthetic power with its thousands of years of silence and mathematical genius."
    },
    "sard_costa_smeralda_luxury": {
        "description": "Zümrüt yeşili denizi ve şık villalarıyla Costa Smeralda, Sardinya'nın dünya jet sosyetesini ağırlayan en ışıltılı ve prestijli sahil şerididir. Modern tasarımı, lüks butikleri ve kentin kozmopolit lüksünü en üst seviyede yaşatan atmosferiyle kentin enerjisini ve kültürel nabzını hissedebileceğiniz iddialı bir duraktır.",
        "description_en": "With its emerald green sea and chic villas, Costa Smeralda is Sardinia's most glittering and prestigious coastline welcoming the world's jet set. It is an ambitious stop where you can feel the city me's energy and cultural pulse with an atmosphere that makes you experience the city's cosmopolitan luxury at the highest level with modern design and luxury boutiques."
    },
    "sard_la_maddalena_archipelago": {
        "description": "Sardinya'nın kuzeyinde bir dizi el değmemiş adadan oluşan La Maddalena, kristal berraklığındaki suları ve pembe kumlarıyla bir doğa harikasıdır. Sadece tekneyle keşfedilebilen gizli koyları ve adanın bakir ruhunu temsil eden atmosferiyle kenti keşfeden gezginlerin en favori ve ilham verici doğa rotasıdır.",
        "description_en": "Consisting of a series of untouched islands in northern Sardinia, La Maddalena is a natural wonder with its crystal-clear waters and pink sands. It is the favorite and most inspiring nature route for travelers exploring the city, with hidden coves accessible only by boat and an atmosphere representing the island's virgin spirit."
    },
    "sard_neptunes_grotto": {
        "description": "Deniz seviyesindeki heybetli sarkıt ve dikitleriyle Neptün Mağarası, Sardinya'nın yer altındaki en görkemli sanat galerisidir. Dalgaların dövdüğü sarp kayalıkların içindeki bu mistik dünya, kentin masalsı derinliklerini ve doğanın yaratıcı gücünü keşfetmek isteyenler için havadar ve merak uyandırıcı bir duraktır.",
        "description_en": "With imposing stalactites and stalagmites at sea level, Neptune's Grotto is Sardinia's most grand underground art gallery. This mystical world inside steep cliffs beaten by waves is an airy and intriguing stop for those wanting to explore the city me's fairytale depths and nature's creative power."
    },
    "sard_gorroppu_canyon": {
        "description": "Avrupa'nın en derin kanyonlarından biri olan Gorroppu, Sardinya'nın vahşi ve sarp doğasını en ham haliyle sergiliyor. Dev beyaz kayaları ve kartalların süzüldüğü yüksek yamaçlarıyla kentin ruhunu en yakından hissedebileceğiniz, macera tutkunları için hem nefes kesici hem de huzurlu bir doğa mabedidir.",
        "description_en": "One of the deepest canyons in Europe, Gorroppu exhibits Sardinia's wild and steep nature in its rawest form. With giant white rocks and high slopes where eagles glide, it is a natural temple both breathtaking and peaceful for adventure enthusiasts where you can feel the city's spirit most closely."
    },
    "sard_spiaggia_del_principe": {
        "description": "Costa Smeralda'nın pırlantası olan bu plaj, bir prensin keşfiyle ünlenmiş ve adını bu mirastan almıştır. Masmavi denizi ve granit kayalıklarla çevrili mahremiyetiyle kentin haritasına karakter katan bu nokta, kentin kozmopolit lüksünü doğallıkla birleştiren havadar ve popüler bir sahil rotasıdır.",
        "description_en": "The diamond of Costa Smeralda, this beach was made famous by a prince's discovery and takes its name from this heritage. This spot adding character to the city map with its deep blue sea and privacy surrounded by granite cliffs is an airy and popular coastal route combining the city's cosmopolitan luxury with naturalness."
    },
    "sard_cala_brandinchi": {
        "description": "Sığ ve süt beyazı sularıyla 'Küçük Tahiti' olarak anılan Cala Brandinchi, Sardinya'nın en fotojenik ve neşeli sahil duraklarından biridir. Çam ağaçlarının gölgesinde uzatılan bu masmavi sahil, kenti keşfeden profesyonel gezginlerin en sevilen ve kentin enerjisini en yüksek seviyede hissettiği duraklardandır.",
        "description_en": "Known as 'Little Tahiti' with its shallow and milk-white waters, Cala Brandinchi is one of Sardinia's most photogenic and joyful coastal stops. This deep blue shore stretched in the shadow of pine trees is among the favorite stops of professional travelers, where they feel the city me's energy at the highest level."
    },
    "sard_cala_mariolu": {
        "description": "Orosei Körfezi'nin incisi olan Cala Mariolu, beyaz çakıl taşları ve akvaryumu andıran sularıyla bir doğa şaheseridir. Sadece denizden ulaşılabilen bu izole cennet, kentin kentsel silüetinden tamamen kopup kentin enerjisini doğanın kalbinde hissetmek isteyenler için havadar ve kaliteli bir kaçış durağıdır.",
        "description_en": "The pearl of the Gulf of Orosei, Cala Mariolu is a natural masterpiece with white pebbles and waters resembling an aquarium. This isolated paradise accessible only from the sea is an airy and high-quality escape stop for those wanting to detach completely from the city's urban silhouette and feel the city me's energy in the heart of nature."
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

print(f"✅ Sardinya Part 1: Enriched {count} items.")
