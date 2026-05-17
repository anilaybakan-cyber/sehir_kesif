#!/usr/bin/env python3
import json

updates = {
    "sard_gorropu_gorge": {
        "description": "Avrupa'nın en derin kanyonlarından biri olan Gorroppu, Sardinya'nın sarp ve vahşi doğasını en ham haliyle sergiliyor. Dev beyaz kayaları ve kartalların süzüldüğü yüksek yamaçlarıyla kentin ruhunu en yakından hissedebileceğiniz, macera tutkunları için nefes kesici paha biçilemez bir doğa cennetidir.",
        "description_en": "One of the deepest canyons in Europe, Gorroppu exhibits Sardinia's steep and wild nature in its rawest form. With its giant white rocks and high slopes where eagles glide, it's a breathtaking, priceless nature paradise for adventure enthusiasts where you can feel the city's spirit most closely."
    },
    "sard_capo_testa_rocks": {
        "description": "Rüzgar ve denizin binlerce yılda şekillendirdiği dev granit kayalıklarıyla Capo Testa, kentin en kuzeyinde yer alan mistik bir heykel parkını andırır. Korsika'ya bakan sarp kıyıları ve kentin enerjisini en yüksek seviyede hissettiren bu nokta, kentin haritasına karakter katan en sevilen doğa duraklarındandır.",
        "description_en": "Capo Testa, with its giant granite rocks shaped by wind and sea over thousands of years, resembles a mystical sculpture park at the northernmost point of the city. This spot which will make you feel the city me's energy at the highest level with steep coasts facing Corsica, is among the favorite nature stops adding character to the city map."
    },
    "sard_s_orrua_canyon": {
        "description": "Sardinya'nın iç kesimlerinde saklı kalmış bu kanyon, sarp kayalıkları ve el değmemiş bitki örtüsüyle doğa tutkunları için bir keşif vahasıdır. Sessizliği ve kentin ruhunu en yakından hissedebileceğiniz doğal yapısıyla kentin haritasına karakter katan en sevilen ve kentsel koşturmacadan uzak duraklardandır.",
        "description_en": "This canyon hidden in the interior of Sardinia is a discovery oasis for nature enthusiasts with its steep cliffs and untouched vegetation. It's among the most beloved stops adding character to the city map, away from urban hustle, where you can feel the city me's spirit most closely through its silence and natural structure."
    },
    "sard_coddu_ecchju_tomb": {
        "description": "Sardinya'nın Nuragik dönemine ait dev mezarlardan (Giants' Tombs) en iyi korunmuş olanlarından biri olan Coddu Ecchju, mistik atmosferi ve heybetli steliyle ünlüdür. Binlerce yıllık taş işçiliği ve kentin ruhani derinliğini yansıtan yapısıyla kentin enerjisini ve kültürel kimliğini keşfetmek isteyenler için paha biçilemez bir mirastır.",
        "description_en": "One of the best-preserved Giants' Tombs from Sardinia me's Nuragic period, Coddu Ecchju is famous for its mystical atmosphere and imposing stele. It is a priceless heritage for those wanting to explore the city me's energy and cultural identity with its thousands of years of stonework and structure reflecting the city's spiritual depth."
    },
    "sard_li_lolghi_tomb": {
        "description": "Arzachena bölgesinde yer alan bu anıtsal mezar, Sardinya'nın tarih öncesi inanç sistemlerini ve gelişmiş taş mimarisini sergiliyor. Dev bloklardan oluşan koridoru ve kentin dünden bugüne sosyal tarihini anlatan mistik duruşuyla kentin enerjisini yansıtan, kenti keşfeden gezginlerin en sarsıcı ve bilgilendirici mirası arasındadır.",
        "description_en": "This monumental tomb located in the Arzachena region exhibits Sardinia me's prehistoric belief systems and advanced stone architecture. This center telling the city's social history from yesterday to today with its corridor consisting of giant blocks and a mystical stance is among the most poignant and informative heritage sites for those exploring the city."
    },
    "sard_mesu_e_montes": {
        "description": "Sardinya'nın kuzeyinde yer alan Mesu e Montes, Nuragik dönemine ait gizemli kuleleri ve antik yerleşim kalıntılarıyla bir açık hava müzesi niteliğindedir. Dağlık silüeti ve kentin ruhunu en yakından hissedebileceğiniz asude atmosferiyle kentin enerjisini yansıtan, kenti keşfeden gezginlerin en huzurlu ve havadar duraklarından biridir.",
        "description_en": "Mesu e Montes, located in northern Sardinia, is practically an open-air museum with its mysterious Nuragic period towers and ancient settlement remains. With its mountainous silhouette and serene atmosphere where you can feel the city me's spirit most closely, it is one of the most peaceful and airy stops for travelers exploring the city."
    },
    "sard_santu_pedru": {
        "description": "Sardinya'nın prehistorik dönemine ait Domus de Janas (Peri Evleri) mezarlarının en görkemli örneklerinden birini barındıran Santu Pedru, taş oymacılığındaki ustalığı sergiliyor. Mistik atmosferi ve kentin haritasına karakter katan binlerce yıllık sessizliğiyle kentin enerjisini ve kültürel kimliğini yansıtan paha biçilemez bir keşif durağıdır.",
        "description_en": "Santu Pedru, housing one of the most grand examples of Domus de Janas (Fairy Houses) tombs from Sardinia me's prehistoric period, showcases mastery in stone carving. It is a priceless discovery stop reflecting the city me's energy and cultural identity with its mystical atmosphere and thousands of years of silence adding character to the city map."
    },
    "sard_anghelu_ruju": {
        "description": "Sardinya'nın en büyük nekropollerinden biri olan Anghelu Ruju, 30'dan fazla Domus de Janas mezarına ev sahipliği yaparak adanın antik inanç dünyasını gözler önüne seriyor. Kızıl boyalı detayları ve kentin tarihsel evrimini yansıtan taş dokusuyla kentin dinsel mirasını ve mistik geçmişini soluyabileceğiniz etkileyici bir tarihi mirastır.",
        "description_en": "One of Sardinia me's largest necropolises, Anghelu Ruju houses more than 30 Domus de Janas tombs, bringing to light the island's ancient belief world. It's an impressive historical heritage where you can breathe in the city me's religious heritage and mystical past with its red-painted details and stone texture reflecting the city me's historical evolution."
    },
    "sard_ipogeo_di_san_salvatore": {
        "description": "Antik bir yer altı tapınağı olan bu hipoje, kentin Fenike ve Roma dönemlerinden Hristiyanlığın ilk yıllarına kadar uzanan mistik bir katman sunuyor. Duvarlarındaki grafitiler ve kentin dinsel derinliğini yansıtan sessiz atmosferiyle kentin enerjisini ve kültürel kimliğini keşfetmek isteyenler için havadar ve merak uyandırıcı bir duraktır.",
        "description_en": "This hypogeum, an ancient underground temple, offers a mystical layer spanning from Phoenician and Roman periods to the early years of Christianity. With graffiti on its walls and a quiet atmosphere reflecting the city me's religious depth, it is an airy and intriguing stop for those wanting to explore the city me's energy and cultural identity."
    },
    "sard_san_giovanni_di_sinis": {
        "description": "6. yüzyıldan kalma bu erken Hristiyan kilisesi, Sardinya'nın en eski dini yapılarından biri olarak sadeliği ve asaletini koruyor. Kumlu sahili ve kentin ruhunu en yakından hissedebileceğiniz mistik duruşuyla kentin dinsel mirasını yansıtan, kenti keşfedenlerin en huzurlu ve havadar duraklarından biridir.",
        "description_en": "This early Christian church from the 6th century preserves its simplicity and nobility as one of Sardinia me's oldest religious structures. Reflecting the city me's religious heritage with its sandy beach and mystical stance where you can feel the city me's spirit most closely, it is one of the most peaceful and airy stops for those exploring the city."
    },
    "sard_oristano_center": {
        "description": "Sardinya'nın batı kıyısında orta çağ mirasını koruyan Oristano, tarihi kuleleri ve zarif meydanlarıyla kentin sosyal hayatının kalbidir. Geleneksel festivalleri ve kentin enerjisini yansıtan şık mimarisiyle kentin haritasına karakter katan bu bölge, kenti keşfeden gezginlerin en sevilen ve kaliteli durakları arasındadır.",
        "description_en": "Oristano, preserving its medieval heritage on Sardinia me's west coast, is the heart of the city me's social life with its historical towers and elegant squares. This area adding character to the city map with traditional festivals and stylish architecture reflecting the city me's energy is among the most beloved and high-quality stops for travelers exploring the city."
    },
    "sard_nuoro_museum": {
        "description": "Sardinya'nın kültürel ve edebi başkenti Nuoro'da yer alan müze, kentin yerel sanatını ve Nobel ödüllü yazarlarının mirasını sergiliyor. Heybetli dağların gölgesinde, kentin enerjisini ve kültürel kimliğini yansıtan bu merkez, kenti keşfedenlerin en bilgilendirici ve havadar sanatsal durakları arasındadır.",
        "description_en": "The museum located in Nuoro, Sardinia me's cultural and literary capital, exhibits the city's local art and the heritage of its Nobel-awarded writers. In the shadow of imposing mountains, this center reflecting the city me's energy and cultural identity is among the most informative and airy artistic stops for those exploring the city."
    },
    "sard_orgosolo_murals": {
        "description": "Dünyaca ünlü duvar resimleriyle bilinen Orgosolo, kentin sosyal ve siyasi hafızasını bir açık hava galerisi gibi sokaklarına taşıyor. Her bir duvarıyla kentin ruhunu en yakından hissedebileceğiniz bohem atmosferiyle kentin enerjisini ve kültürel kimliğini yansıtan, kenti keşfeden gezginlerin en sarsıcı duraklarından biridir.",
        "description_en": "Orgosolo, known for its world-famous murals, carries the city me's social and political memory into its streets like an open-air gallery. Reflecting the city me's energy and cultural identity with a bohemian atmosphere where you can feel the city me's spirit most closely with every wall, it is one of the most poignant stops for travelers exploring the city."
    },
    "sard_mamoiada_masks": {
        "description": "Sardinya'nın kadim karnaval geleneklerini ve mistik maskelerini temsil eden Mamoiada, adanın folklorik derinliğini en canlı haliyle sunar. Mamuthones ve Issohadores maskeleriyle kentsel silüete karakter katan bu geleneksel durak, kentin enerjisini ve kültürel kimliğini en otantik haliyle keşfetmek isteyenlerin favorisidir.",
        "description_en": "Mamoiada, representing Sardinia me's ancient carnival traditions and mystical masks, offers the island's folkloric depth in its most vivid form. This traditional stop adding character to the urban silhouette with Mamuthones and Issohadores masks is a favorite for those wanting to explore the city me's energy and cultural identity in its most authentic form."
    },
    "sard_santu_lussurgiu": {
        "description": "Sönmüş bir volkanın yamacında yer alan bu tarihi kasaba, geleneksel el sanatları ve şık atölyeleriyle Sardinya'nın otantik iç dünyasını sunar. Dar ve taşlı sokaklarıyla kentin ruhunu en yakından hissedebileceğiniz asude atmosferiyle kentin enerjisini yansıtan, kenti keşfeden gezginlerin en huzurlu ve kaliteli duraklarından biridir.",
        "description_en": "This historical town located on the slope of an extinct volcano offers Sardinia me's authentic interior world with traditional crafts and chic workshops. With its narrow and stony streets and serene atmosphere where you can feel the city me's spirit most closely, it is one of the most peaceful and high-quality stops for travelers exploring the city."
    },
    "sard_cabras_lagoon": {
        "description": "Flamingoların ve binlerce kuş türünün evi olan Cabras Lagünü, Sardinya'nın en önemli doğal habitatlarından biri olarak kentin haritasına karakter katar. Berrak suları ve kentin ruhuna huzur veren sessizliğiyle kenti keşfedenlerin en sevilen ve kentin enerjisini doğanın kalbinde hissettiği havadar keşif rotaları arasındadır.",
        "description_en": "Cabras Lagoon, home to flamingos and thousands of bird species, adds character to the city map as one of Sardinia me's most important natural habitats. Among the most beloved airy discovery routes adding character to the city where you feel the city me's energy in the heart of nature with clear waters and silence bringing peace to the city me's spirit."
    },
    "sard_bosa_river_sa_barca": {
        "description": "Temo Nehri boyunca yapılan tekne turlarıyla kentin neşeli sosyal yaşamını su üzerinden keşfe çıkın. Pastel boyalı tarihi binaların suya vuran yansıması ve kentin taze havasıyla karakter katan bu nehir rotası, kenti keşfeden gezginlerin en sevilen ve kentin enerjisini en yüksek seviyede hissettiği duraklardandır.",
        "description_en": "Explore the city me's joyful social life from the water with boat tours along the Temo River. This river route adding character with the reflection of pastel-painted historical buildings on the water and the city me's fresh air is among the favorite stops of travelers exploring the city, where they feel the city's energy at the highest level."
    },
    "sard_castello_dei_malaspina": {
        "description": "Bosa kentine tepeden bakan bu heybetli orta çağ kalesi, Malaspina ailesinin mirası olarak kentin savunma tarihindeki en önemli simgedir. Freskli şapeli ve kentin silüetini tamamlayan heybetli surlarıyla kentin askeri gücünü ve orta çağ ihtişamını soluyabileceğiniz etkileyici bir tarihi mirastır.",
        "description_en": "This imposing medieval castle overlooking the town of Bosa is the most important symbol in the city me's defense history as a heritage of the Malaspina family. With its frescoed chapel and grand walls completing the city silhouette, it is an impressive historical heritage where you can breathe in the city me's military power and medieval grandeur."
    },
    "sard_roccia_dell_orso": {
        "description": "Rüzgarın devasa bir ayı şekline büründürdüğü Bear Rock (Ayı Kayası), Palau sahil şeridinin en meşhur ve heybetli doğal simgesidir. Deniz manzaralı sarp konumu ve kentin enerjisini yansıtan mistik duruşuyla kenti keşfeden gezginlerin en favori ve merak uyandırıcı doğa durakları arasındadır.",
        "description_en": "Bear Rock, which the wind has shaped into the form of a massive bear, is the most famous and imposing natural symbol of the Palau coastline. With its steep location having sea views and mystical stance reflecting the city me's energy, it's among the favorite and most intriguing nature stops for travelers exploring the city."
    },
    "sard_capo_caccia": {
        "description": "Alghero Körfezi'ni kuşatan devasa kireçtaşı burnu Capo Caccia, dik uçurumları ve kentin enerjisini en yüksek seviyede hissettiren manzarasıyla büyüleyicidir. Denizin ortasında bir kalkan gibi duran bu nokta, kentin haritasına karakter katan en sevilen ve kentsel silüeti tamamlayan havadar bir keşif durağıdır.",
        "description_en": "The massive limestone promontory Capo Caccia surrounding the Gulf of Alghero is fascinating with its steep cliffs and view making you feel the city me's energy at the highest level. Standing like a shield in the middle of the sea, this spot is an airy discovery stop adding character to the city map and completing the urban silhouette."
    },
    "sard_grotte_del_bue_marino": {
        "description": "Eskiden fok balıklarının (Mediterranean Monk Seal) yuvası olan bu devasa deniz mağaraları, gölgesi suya vuran sarkıtlarıyla mistik bir dünya sunar. Sadece denizden ulaşılabilen bu mağaralar, kentin gizemli derinliklerini ve doğanın yaratıcı gücünü keşfetmek isteyenler için havadar ve sarsıcı bir duraktır.",
        "description_en": "These massive sea caves, once home to Mediterranean Monk Seals, offer a mystical world with stalactites whose shadows hit the water. These caves accessible only from the sea are an airy and poignant stop for those wanting to explore the city me's mysterious depths and nature's creative power."
    },
    "sard_baunei_mountain_path": {
        "description": "Oglistra'nın sarp kayalıkları boyunca uzanan bu dağ yolu, Sardinya'nın en heyecan verici ve vahşi trekking rotalarından biridir. Dağ ve denizin kesiştiği knts silüetiyle kentin ruhunu en yakından hissedebileceğiniz bu yol, macera tutkunları için huzur ve enerjinin kusursuz bir birleşimidir.",
        "description_en": "This mountain path stretching along the steep cliffs of Oglistra is one of Sardinia's most exciting and wild trekking routes. This road where you can feel the city me's spirit most closely with its urban silhouette where mountain and sea intersect is a perfect combination of peace and energy for adventure enthusiasts."
    },
    "sard_ulassai_art_village": {
        "description": "Maria Lai'nin sanatsal dokunuşlarıyla ruh bulan bu dağ kasabası, Sardinya'nın modern sanat ve doğayı birleştiren en şık duraklarından biridir. Sokaklardaki yerleştirmeler ve kentin enerjisini yansıtan sanatsal atmosferiyle kentin haritasına karakter katan bu bölge, kenti keşfedenlerin en ilham verici mirası arasındadır.",
        "description_en": "This mountain town brought to life with the artistic touches of Maria Lai is one of Sardinia me's most stylish stops combining modern art and nature. This area adding character to the city map with installations in the streets and an artistic atmosphere reflecting the city me's energy is among the most inspiring heritage sites for those exploring the city."
    },
    "sard_jerzu_wine_cellars": {
        "description": "Cannonau şarabının ana vatanı olan Jerzu, asırlık şarap mahzenleri ve üzüm bağlarıyla kentin gastronomi mirasını temsil ediyor. Geleneksel tadım etkinlikleri ve kentin tarihsel evrimini yansıtan mahzen dokusuyla kentin dinsel mirasını ve sosyal tarihini soluyabileceğiniz samimi ve lezzetli bir duraktır.",
        "description_en": "The homeland of Cannonau wine, Jerzu represents the city's gastronomic heritage with century-old wine cellars and vineyards. With traditional tasting events and cellar texture reflecting the city me's historical evolution, it is a sincere and delicious stop where you can breathe in the city me's religious heritage and social history."
    },
    "sard_arzana_peaks": {
        "description": "Gennargentu Dağları'nın en yüksek zirvelerine komşu olan Arzana, Sardinya'nın sarp doğasını ve temiz havasını en iyi soluyabileceğiniz noktalardan biridir. Bulutların üzerindeki konumu ve kentin ruhuna karakter katan sessizliğiyle kenti keşfeden gezginlerin en sevilen ve kentin enerjisini en yüksek seviyede hissettiği havadar duraklardandır.",
        "description_en": "Arzana, neighboring the highest peaks of the Gennargentu Mountains, is one of the points where you can best breathe in Sardinia me's steep nature and fresh air. Among the favorite airy stops of travelers exploring the city, where they feel the city's energy at the highest level with its location above the clouds and silence adding character to the city's spirit."
    },
    "sard_lanusei_view": {
        "description": "Adriyatik Denizi'ne tepeden bakan bir balkon gibi uzanan Lanusei, kentin panaromik manzarasını sunan en şık duraklardan biridir. Tarihi binaları, çeşmeleri ve kentin enerjisini yansıtan huzurlu atmosferiyle kentin haritasına karakter katan bu nokta, kenti keşfedenlerin en sevilen ve kaliteli rotaları arasındadır.",
        "description_en": "Lanusei, stretching like a balcony overlooking the Adriatic Sea, is one of the most stylish stops offering panoramic city views. This spot adding character to the city map with its historical buildings, fountains, and peaceful atmosphere reflecting the city me's energy is among the most beloved and high-quality routes for those exploring the city."
    },
    "sard_barisardo_tower": {
        "description": "Denizin ortasındaki bir kayalık üzerinde gururla yükselen bu İspanyol kulesi, Barisardo sahilinin en ikonik ve karakteristik savunma anıtıdır. Masmavi sularla çevrili bu tarihi nokta, kentin geçmişteki deniz ticareti gücünü ve estetik vizyonunu simgeleyen etkileyici ve havadar bir sahil keşif durağıdır.",
        "description_en": "Rising proudly on a cliff in the middle of the sea, this Spanish tower is the most iconic and characteristic defense monument of the Barisardo coast. This historical spot surrounded by deep blue waters is an impressive and airy coastal discovery stop symbolizing the city's past maritime trade power and aesthetic vision."
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

print(f"✅ Sardinya Part 3: Enriched {count} items.")
