#!/usr/bin/env python3
import json

updates = {
    "sard_costa_rei_beaches": {
        "description": "Sardinya'nın güneydoğusunda kilometrelerce uzanan beyaz kumları ve berrak sularıyla Costa Rei, kentin en havadar ve huzurlu sahil şerididir. Arkasındaki kaktüsler ve kentin taze deniz havasıyla kentin kozmopolit ritmini en doğal haliyle soluyabileceğiniz, kente karakter katan en sevilen sahil rotaları arasındadır.",
        "description_en": "Costa Rei, stretching for kilometers in southeastern Sardinia with white sands and clear waters, is the city's most airy and peaceful coastline. Among the favorite coastal routes adding character to the city, where you can breathe in the city me's cosmopolitan rhythm in its most natural form with cacti behind and the city's fresh sea air."
    },
    "sard_castiadas_old_prison": {
        "description": "19. yüzyıldan kalma bu tarihi hapishane kompleksi, bugün kentin tarımsal ve sosyal tarihindeki önemli bir dönemi anlatan bir müze niteliğindedir. Heybetli taş yapıları, avluları ve kentin dünden bugüne katmanlarını anlatan sergileriyle kentin ruhunu en yakından hissedebileceğiniz sarsıcı bir mirastır.",
        "description_en": "This historical prison complex from the 19th century serves today as a museum telling of an important period in the city's agricultural and social history. It is a poignant heritage where you can feel the city me's spirit most closely with its imposing stone structures, courtyards, and exhibitions telling the city's layers from yesterday to today."
    },
    "sard_muravera_orange_groves": {
        "description": "Sardinya'nın en bereketli toprakları üzerine kurulu Muravera, uçsuz bucaksız portakal ve narenciye bahçeleriyle ünlüdür. Bahar aylarındaki mis kokulu çiçekleri ve kentin kırsal neşesini yansıtan atmosferiyle kentin enerjisini en saf haliyle keşfetmek isteyenler için havadar ve kaliteli bir duraktır.",
        "description_en": "Built on Sardinia me's most fertile lands, Muravera is famous for its endless orange and citrus groves. With its fragrant flowers in spring months and atmosphere reflecting the city me's rural joy, it is an airy and high-quality stop for those wanting to explore the city me's energy in its purest form."
    },
    "sard_sinis_peninsula": {
        "description": "Vahşi ve el değmemiş doğasıyla Sinis Yarımadası, kentin en bakir ve mistik sahil şeridini sunuyor. Fenike kalıntılarından kristal sulara kadar kentin enerjisini ve kültürel kimliğini yansıtan, kentin haritasına karakter katan en sevilen ve huzurlu keşif rotaları arasındadır.",
        "description_en": "The Sinis Peninsula, with its wild and untouched nature, offers the city's most virgin and mystical coastline. Among the favorite and peaceful discovery routes adding character to the city map, reflecting the city's energy and cultural identity from Phoenician remains to crystal waters."
    },
    "sard_s_archittu_rock_arch": {
        "description": "Denizin üzerinde yükselen devasa ve bembeyaz bir kaya kemeri olan S'Archittu, doğanın Sardinya sahilindeki en ikonik heykellerinden biridir. Gün batımında kentin enerjisini en yüksek seviyede hissettiren bu nokta, kentin haritasına karakter katan en sevilen ve merak uyandırıcı doğa duraklarından biridir.",
        "description_en": "S'Archittu, a massive and pure white rock arch rising over the sea, is one of nature's most iconic sculptures on the Sardinian coast. This spot which will make you feel the city me's energy at the highest level at sunset, is one of the most beloved and intriguing nature stops adding character to the city map."
    },
    "sard_putzu_idu": {
        "description": "Sığ suları ve kuvars kumu kumsallarıyla Putzu Idu, Sardinya'nın en berrak ve havadar sahil duraklarından biridir. Sörf tutkunları ve sükunet arayanlar için kentin enerjisini ve kültürel kimliğini yansıtan, kentsel silüeti tamamlayan kaliteli bir sahil keşif noktasıdır.",
        "description_en": "Putzu Idu, with its shallow waters and quartz sandy beaches, is one of Sardinia's clearest and most airy coastal stops. It is a high-quality coastal discovery point for surf enthusiasts and those seeking tranquility, reflecting the city me's energy and cultural identity while completing the urban silhouette."
    },
    "sard_spiaggia_del_riso": {
        "description": "Villasimius'ta yer alan ve 'Pirinç Plajı' anlamına gelen bu kordon, kumunu andıran pürüzsüz küçük beyaz taşlarıyla ünlüdür. Turkuaz denizi ve kentin taze deniz havasıyla kentin kozmopolit lüksünü dengeleyen bu durak, kenti keşfeden profesyonel gezginlerin en sevilen ve kaliteli rotaları arasındadır.",
        "description_en": "This promenade located in Villasimius and meaning 'Rice Beach' is famous for its smooth small white stones resembling rice. Balancing the city me's cosmopolitan luxury with its turquoise sea and the city's fresh sea air, this stop is among the most beloved and high-quality routes for professional travelers exploring the city."
    },
    "sard_cala_pira": {
        "description": "Eski bir gözetleme kulesinin gölgesinde saklı kalan Cala Pira, sığ turkuaz suları ve bembeyaz kumlarıyla bir akvaryumu andırır. Doğal dokusu ve kentin ruhuna huzur veren sessizliğiyle kentin enerjisini ve kültürel kimliğini yansıtan, kente karakter katan en sevilen sahil kaçış duraklarından biridir.",
        "description_en": "Cala Pira, hidden in the shadow of an old watchtower, resembles an aquarium with its shallow turquoise waters and pure white sands. Reflecting the city me's energy and cultural identity with its natural texture and silence bringing peace to the city me's spirit, it is one of the most beloved coastal escape stops adding character to the city."
    },
    "sard_cala_sinzias": {
        "description": "Uçsuz bucaksız çam ormanlarıyla sahilin birleştiği Cala Sinzias, Sardinya'nın en bakir ve mis kokulu sahil duraklarından biridir. Berrak denizi ve kentin taze havasıyla kentin kozmopolit ritmini dengeleyen bu bölge, kenti keşfeden GEZGİNLERİN en sevilen ve havadar keşif rotaları arasındadır.",
        "description_en": "Cala Sinzias, where endless pine forests meet the coast, is one of Sardinia's most virgin and fragrant coastal stops. This area balancing the city me's cosmopolitan rhythm with its clear sea and the city's fresh air is among the favorite and airy discovery routes of travelers exploring the city."
    },
    "sard_capo_carbonara_marine_are": {
        "description": "Sardinya'nın güneydoğu ucunda yer alan bu koruma altındaki deniz alanı, zengin su altı faunası ve turkuaz sularıyla bir doğa şaheseridir. Granit kayalıkları ve kentin enerjisini en yüksek seviyede hissettiren manzarasıyla kentin haritasına karakter katan en sevilen ve prestijli deniz keşif noktasıdır.",
        "description_en": "This protected marine area located at Sardinia's southeastern tip is a natural masterpiece with its rich underwater fauna and turquoise waters. It is the most beloved and prestigious sea discovery point adding character to the city map with its granite cliffs and view making you feel the city me's energy at the highest level."
    },
    "sard_campulongu_beach": {
        "description": "Hafif eğimli kristal denizi ve beyaz kumuyla Campulongu, kentin en konforlu ve havadar sahil duraklarından biridir. Akdeniz çalılıklarının arasında kalan bu sessiz plaj, kentin enerjisini doğallıkla buluşturmak isteyen yerel halkın ve gezginlerin en sevilen kaliteli rotaları arasındadır.",
        "description_en": "Campulongu, with its gently sloping crystal sea and white sand, is one of the city's most comfortable and airy coastal stops. This quiet beach among Mediterranean bushes is among the most beloved high-quality routes for locals and travelers wanting to meet the city me's energy with naturalness."
    },
    "sard_simius_beach": {
        "description": "Göz alabildiğine uzanan bembeyaz kumsalı ve canlı sahil şeridiyle Simius Plajı, Sardinya'nın modern yaz neşesini temsil ediyor. Flamingo dolu göletleri ve kentin taze deniz havasıyla kentsel silüeti tamamlayan bu nokta, kenti keşfedenlerin en heyecan verici ve popüler sahil durağıdır.",
        "description_en": "Simius Beach, with its stretch of white sandy beach as far as the eye can see and vibrant coastline, represents Sardinia's modern summer joy. Completing the urban silhouette with lagoons full of flamingos and the city me's fresh sea air, this spot is the most exciting and popular coastal stop for those exploring the city."
    },
    "sard_timi_ama_coast": {
        "description": "Turkuaz denizin beyaz kumlarla dans ettiği Timi Ama, kentin en prestijli ve estetik sahil duraklarından biridir. Arkasındaki lagün ve kentin ruhuna huzur veren sessizliğiyle kentin enerjisini ve kültürel kimliğini yansıtan, kentsel koşturmacadan uzak kaliteli bir keşif noktasıdır.",
        "description_en": "Timi Ama, where the turquoise sea dances with white sands, is one of the city me's most prestigious and aesthetic coastal stops. Reflecting the city me's energy and cultural identity with the lagoon behind and silence bringing peace to the city me's spirit, it is a high-quality discovery point away from urban hustle."
    },
    "sard_is_molas_golf": {
        "description": "Deniz manzaralı yeşil sahalarıyla Is Molas Golf, Sardinya'nın en şık ve kozmopolit spor duraklarından biridir. Modern tasarımı ve kentin enerjisini elit bir atmosferle birleştiren yapısıyla kentin estetik gücünü ve yüksek konfor anlayışını yansıtan paha biçilemez bir duraktır.",
        "description_en": "Is Molas Golf, with its green courses having sea views, is one of Sardinia me's most stylish and cosmopolitan sports stops. It is a priceless stop reflecting the city me's aesthetic power and high comfort concept with its modern design and structure combining the city's energy with an elite atmosphere."
    },
    "sard_santa_margherita_di_pula": {
        "description": "Çam ormanlarıyla kaplı bembeyaz sahiliyle Santa Margherita di Pula, Sardinya'nın en havadar ve kaliteli yaz duraklarından biridir. Lüks resortları ve kentin taze deniz havasıyla karakter katan bu bölge, kenti keşfeden profesyonel gezginlerin en sevilen ve prestijli rotaları arasındadır.",
        "description_en": "Santa Margherita di Pula, with its pure white shore covered with pine forests, is one of Sardinia's most airy and high-quality summer stops. This area adding character with its luxury resorts and the city's fresh sea air is among the most beloved and prestigious routes for professional travelers exploring the city."
    },
    "sard_chia_shoreline": {
        "description": "Devasa kum tepeleri ve turkuaz sularıyla Chia Sahili, Sardinya'nın en vahşi ve büyüleyici sahil şeridinden biridir. Flamingo dolu lagünleri ve kentin enerjisini doğanın kalbinde hissettiren atmosferiyle kentin haritasına karakter katan en favori ve sarsıcı duraklardandır.",
        "description_en": "The Chia Shoreline, with its massive sand dunes and turquoise waters, is one of Sardinia's most wild and fascinating coastlines. Among the most favorite and poignant stops adding character to the city map with lagoons full of flamingos and an atmosphere making you feel the city me's energy in the heart of nature."
    },
    "sard_tuerredda_beach": {
        "description": "Karayip adalarını andıran turkuaz suları ve bembeyaz kumuyla Tuerredda, kentin en prestijli ve neşeli sahil duraklarından biridir. Karşısındaki minik adası ve kentin taze deniz havasıyla kentin kozmopolit ritmini doyasıya yaşatan kaliteli ve havadar bir sahil rotasıdır.",
        "description_en": "Tuerredda, with its turquoise waters and pure white sand resembling Caribbean islands, is one of the city me's most prestigious and joyful coastal stops. It is a high-quality and airy coastal route making you fully live the city me's cosmopolitan rhythm with its tiny island opposite and the city's fresh sea air."
    },
    "sard_capo_spartivento": {
        "description": "Sardinya'nın en güney ucunda yükselen Capo Spartivento, tarihi feneri ve sarp kayalıklarıyla kentin en mistik ve heybetli doğal simgelerinden biridir. Denize hakim konumu ve kentin enerjisini en yüksek seviyede hissettiren manzarasıyla kentin haritasına karakter katan en sevilen keşif durağıdır.",
        "description_en": "Capo Spartivento rising at the southernmost tip of Sardinia is one of the city's most mystical and imposing natural symbols with its historical lighthouse and steep cliffs. It is the most beloved discovery stop adding character to the city map with its location dominating the sea and view making you feel the city me's energy at the highest level."
    },
    "sard_domus_de_maria": {
        "description": "Dağlarla denizin buluştuğu bu şık kasaba, Sardinya'nın hem kırsal asaletini hem de sahil şıklığını bir arada sunuyor. Geleneksel yapısı ve kentin dünden bugüne sosyal tarihini anlatan asude atmosferiyle kentin ruhunu en yakından hissedebileceğiniz kaliteli bir duraktır.",
        "description_en": "This stylish town where mountains meet the sea offers both Sardinia me's rural nobility and seaside chic together. It is a high-quality stop where you can feel the city me's spirit most closely with its traditional structure and serene atmosphere telling the city's social history from yesterday to today."
    },
    "sard_teulada_port": {
        "description": "Cagliari'nin güneyindeki bu tarihi liman, sarp kayalıkları ve el değmemiş koylarıyla kentin en bakir deniz rotalarından biridir. Balıkçı tekneleri ve kentin taze deniz havasıyla karakter katan bu bölge, kenti keşfeden gezginlerin en sevilen ve enerjisi en yüksek keşif noktalarındandır.",
        "description_en": "This historical port in southern Cagliari is one of the city's most virgin sea routes with its steep cliffs and untouched coves. This area adding character with fishing boats and the city me's fresh sea air is among the favorite discovery points with highest energy for travelers exploring the city."
    },
    "sard_porto_pino_dunes": {
        "description": "Bembeyaz ve devasa kum tepeleriyle Porto Pino, Sardinya'nın en sarsıcı ve vahşi doğa harikalarından biridir. Çam ormanları ve lagünleriyle kentin ruhuna karakter katan bu nokta, kentin kozmopolit enerjisinden uzaklaşıp doğanın sessizliğini solumak için paha biçilemez bir duraktır.",
        "description_en": "Porto Pino, with its and massive white sand dunes, is one of Sardinia me's most poignant and wild natural wonders. This spot adding character to the city me's spirit with pine forests and lagoons is a priceless stop for escaping the city me's cosmopolitan energy and breathing in nature's silence."
    },
    "sard_sant_anna_arresi": {
        "description": "Kentin silüetinde yer alan antik Nuragelerle çevrili bu kasaba, Sardinya'nın binlerce yıllık tarihini modern yaşamla her gün buluşturuyor. Geleneksel yapısı ve kentin sosyal tarihinde bıraktığı derin izlerle kenti keşfeden gezginlerin en sevilen ve kentin enerjisini en yüksek seviyede hissettiği havadar duraklardandır.",
        "description_en": "This town surrounded by ancient Nuraghes in the city silhouette meets Sardinia me's thousands of years of history with modern life every day. Among the favorite airy stops of travelers exploring the city, where they feel the city me's energy at the highest level with its traditional structure and deep marks left in the city's social history."
    },
    "sard_carbonia_mining_site": {
        "description": "Endüstriyel mirasın en heybetli örneklerinden biri olan bu maden yerleşkesi, Sardinya'nın işçi tarihini ve ekonomik evrimini sarsıcı bir dille anlatıyor. Heybetli kuyuları ve kentin dünden bugüne katmanlarını anlatan müzesiyle kentin enerjisini ve kültürel kimliğini yansıtan bilgilendirici bir mirastır.",
        "description_en": "This mining settlement, one of the most imposing examples of industrial heritage, tells Sardinia's labor history and economic evolution in a poignant language. It is an informative heritage reflecting the city me's energy and cultural identity with its imposing pits and museum telling the city's layers from yesterday to today."
    },
    "sard_iglesias_old_town": {
        "description": "Gümüş madenlerinin zenginliğiyle kurulan Iglesias Eski Kent, orta çağ surları ve şık katedralleriyle kentin aristokratik geçmişini yansıtır. Renkli şemsiyeli sokakları ve kentin enerjisini yansıtan neşeli sosyal yapısıyla kenti keşfedenlerin en heyecan verici ve kaliteli durakları arasındadır.",
        "description_en": "Iglesias Old Town, founded with the wealth of silver mines, reflects the city me's aristocratic past with its medieval walls and chic cathedrals. With colorful umbrella streets and a joyful social structure reflecting the city me's energy, it's among the most exciting and high-quality stops for those exploring the city."
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

print(f"✅ Sardinya Part 4: Enriched {count} items.")
