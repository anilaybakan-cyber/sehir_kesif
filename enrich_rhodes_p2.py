#!/usr/bin/env python3
import json

updates = {
    "ChIJL-6MRgBhlRQRMbetccIlfKM": {
        "description": "Rodos, antik şövalye mirası ve masmavi Ege sularıyla Yunan adalarının en görkemli destinasyonlarından biridir. Orta çağ surları, şık caddeleri ve kentin dünden bugüne katmanlarını anlatan sarsıcı atmosferiyle, her köşesi tarih kokan samimi ve etkileyici bir keşif yolculuğu vaat ediyor.",
        "description_en": "Rhodes is one of the most grand destinations of the Greek islands with its ancient knight heritage and deep blue Aegean waters. With its medieval walls, stylish avenues, and a poignant atmosphere telling the city's layers from yesterday to today, it promises a sincere and impressive discovery journey where every corner scents of history."
    },
    "ChIJC4CSvbZmlRQRQbBbcMUo83Y": {
        "description": "Kentin iddialı konaklama duraklarından biri olan bu şık resort, Rodos'un kozmopolit enerjisini elit bir atmosferle buluşturuyor. Modern tasarımı ve kentin ruhuna karakter katan ferah dokusuyla, kenti keşfedenlerin kentsel ritmi en elit haliyle hissedebileceği en favori ve havadar keşif noktaları arasındadır.",
        "description_en": "One of the city me's ambitious accommodation stops, this stylish resort meets Rhodes' cosmopolitan energy with an elite atmosphere. Among the favorite and airy discovery points where those exploring the city can feel the urban rhythm in its most elite form with its modern design and fresh texture adding character to the city me's spirit."
    },
    "ChIJ_WIYvuhhlRQRgL6EfF4vWmg": {
        "description": "Kentin neşeli sokaklarında taze kahve kokusunu ve yeral atıştırmalıkları takip etmek isteyenler için Gregory's, kentin modern sosyal yüzünü temsil eder. Şık tasarımı ve kentin enerjisini yansıtan neşeli sosyal dokusuyla, kentsel ritmi ferah bir atmosferde solumak isteyenlerin en favori durakları arasındadır.",
        "description_en": "For those wanting to follow the scent of fresh coffee and local snacks in the joyful streets of the city, Gregory's represents the city me's modern social face. Among the favorite stops for those wanting to breathe in the urban rhythm in a fresh atmosphere with its stylish design and joyful social texture reflecting the city me's energy."
    },
    "ChIJ3ZMNee9hlRQRwXrAZ6x5TdE": {
        "description": "Rodos'un neşeli sosyal bağlarını ve bohem akşamlarını yansıtan bu karakteristik köşe, kentin en popüler buluşma noktalarından biridir. Kentin enerjisini en yüksek seviyede hissedebileceğiniz atmosferi ve kente karakter katan samimi yapısıyla kenti keşfeden gezginlerin en favori ve havadar rotaları arasındadır.",
        "description_en": "This characteristic corner reflecting Rhodes' joyful social ties and bohemian evenings is one of the city's most popular meeting points. Among the favorite and airy routes of travelers exploring the city with its atmosphere where you can feel the city me's energy at the highest level and its sincere structure adding character to the city."
    },
    "ChIJ71oK8-lhlRQRkRqL9qsLWF4": {
        "description": "Budva'nın gece hayatına modern ve enerjik bir soluk getiren Gazi Club, kentin kozmopolit ritmini ferah bir atmosferde sunuyor. Şık ışıklandırması ve kentin enerjisini yansıtan neşeli sosyal dokusuyla, kentsel silüeti tamamlayan iddialı ve kaliteli bir akşam keşif rotasıdır.",
        "description_en": "Bringing a modern and energetic breath to Budva's nightlife, Gazi Club offers the city me's cosmopolitan rhythm in a fresh atmosphere. With its stylish lighting and joyful social texture reflecting the city's energy, it is an ambitious and high-quality evening discovery route completing the urban silhouette."
    },
    "ChIJl-02aO9hlRQRPldIViP1Keo": {
        "description": "Kentin labirent sokakları arasına gizlenmiş bu şık bar, yaratıcı kokteylleri ve kentin enerjisini yansıtan neşeli atmosferiyle bilinir. Nostaljik tasarımı ve kenti keşfeden profesyor gezginlerin en sevilen durakları arasındadır, kentin kozmopolit enerjisini elit bir akşamda keşfetmek isteyenler için havadar bir duraktır.",
        "description_en": "This stylish bar hidden among the labyrinthine streets of the city is known for its creative cocktails and joyful atmosphere reflecting the city me's energy. It's among the favorite stops of professional travelers exploring the city, and is an airy stop for those wanting to explore the city me's cosmopolitan energy on an elite evening."
    },
    "ChIJn-anMORhlRQRAcZXff4HvEU": {
        "description": "Rodos'un kozmopolit ruhunu farklı kültürlerle buluşturan bu karakteristik kafe, kentin en neşeli ve samimi sosyal duraklarından biridir. Kentin enerjisinin akşam saatlerinde romantik bir ritme dönüştüğü atmosferiyle kente karakter katan, kentsel ritmi solumak için popüler ve havadar bir keşif durağıdır.",
        "description_en": "This characteristic cafe meeting Rhodes' cosmopolitan spirit with different cultures is one of the city me's most joyful and sincere social stops. It is a popular and airy discovery stop for breathing in the urban rhythm, adding character to the city with its atmosphere where the city me's energy turns into a romantic rhythm in evening hours."
    },
    "ChIJhzeVaAthlRQRpa91Ltcr5QE": {
        "description": "Adriyatik kıyısınca uzanan bu devasa açık hava kulübü, Rodos'un yaz neşesini ve enerjisini en yüksek seviyede temsil ediyor. İkonik DJ şovları ve kentin sahil silüetine karakter katan heybetli yapısıyla, kentsel ritmi ferah bir atmosferde solumak isteyen gezginlerin en favori ve prestijli eğlence durağıdır.",
        "description_en": "This massive open-air club stretching along the Adriatic coast represents Rhodes me's summer joy and energy at the highest level. With iconic DJ shows and its imposing structure adding character to the city's coastal silhouette, it is the most favorite and prestigious entertainment stop for travelers wanting to breathe in the urban rhythm in a fresh atmosphere."
    },
    "ChIJn8HbzfphlRQRv-Wvp6MhlUc": {
        "description": "Modern elektronik müzik tınılarını Rodos'un kalbine taşıyan Kinky, kentin en genç ve dinamik gece hayatı duraklarından biridir. Dijital şovları ve kentin enerjisini en yüksek seviyede hissettiren neşeli atmosferiyle, kentsel silüete sanatsal bir soluk getiren dikkat çekici ve popüler bir eğlence merkezidir.",
        "description_en": "Carrying modern electronic music tones to the heart of Rhodes, Kinky is one of the city me's youngest and most dynamic nightlife stops. It is a remarkable and popular entertainment center bringing an artistic breath to the urban silhouette with its digital shows and joyful atmosphere making you feel the city me's energy at the highest level."
    },
    "ChIJccsIb-lhlRQRpZNdmutWjUo": {
        "description": "Eski Şehir'in göbeğinde saklı kalmış bir vaha olan bu bahçe, Rodos'un tarihi atmosferi içinde asude bir mola durağı niteliğindedir. Çiçek kokuları ve kentin ruhuna karakter katan sessizliğiyle kenti keşfeden gezginlerin kentsel koşturmacadan uzaklaşıp huzur bulabileceği kaliteli ve samimi bir duraktır.",
        "description_en": "This garden, a hidden oasis in the heart of Old Town, is in the quality of a serene break stop within Rhodes' historical atmosphere. With flower scents and silence adding character to the city me's spirit, it is a high-quality and sincere stop where travelers exploring the city can move away from urban hustle and find peace."
    },
    "ChIJ7aEGkulhlRQRA9GWB4VdUzo": {
        "description": "Rodos'un sarsılmaz rock ruhunu ve neşeli sosyal bağlarını yansıtan bu bar, kentin en otantik ve enerjik sosyal duraklarından biridir. Kentin enerjisini en yüksek seviyede hissedebileceğiniz samimi atmosferi ve kente karakter katan yapısıyla kenti keşfedenlerin en favori ve havadar rotaları arasındadır.",
        "description_en": "Reflecting Rhodes' unshakable rock spirit and joyful social ties, this bar is one of the city's most authentic and energetic social stops. Among the favorite and airy routes of those exploring the city with its sincere atmosphere where you can feel the city me's energy at the highest level and its structure adding character to the city."
    },
    "ChIJKas_jh5hlRQR4JZ8fWnO-FM": {
        "description": "Kentin modern eğlence hayatına iddialı bir soluk getiren Vibe, Rodos'un kozmopolit ritmini enerjik ritimlerle buluşturuyor. Şık tasarımı ve kentin enerjisini yansıtan neşeli sosyal dokusuyla, kentsel ritmi ferah bir atmosferde solumak isteyen gezginlerin en favori ve kaliteli durakları arasındadır.",
        "description_en": "Bringing an ambitious breath to the city me's modern entertainment life, Vibe meets Rhodes' cosmopolitan rhythm with energetic rhythms. Among the favorite and high-quality stops of travelers wanting to breathe in the urban rhythm in a fresh atmosphere with its stylish design and joyful social texture reflecting the city me's energy."
    },
    "ChIJF5kdRTJhlRQRPuC1OTJ88FQ": {
        "description": "Rodos sahilinde aristokratik şıklığı ve modern eğlenceyi birleştiren Akanthus, kentin en prestijli ve estetik sahil duraklarından biridir. Masmavi manzarası ve kentin dünden bugüne katmanlarını anlatan sarsıcı atmosferiyle kentin enerjisini elit bir akşamda keşfetmek isteyen seçkin gezginlerin favorisidir.",
        "description_en": "Combining aristocratic chic and modern entertainment on the Rhodes coast, Akanthus is one of the city's most prestigious and aesthetic coastal stops. It is a favorite of elite travelers wanting to explore the city me's energy on an elite evening with its deep blue view and a poignant atmosphere telling the city's layers from yesterday to today."
    },
    "ChIJv_y6FOZhlRQRsFNu0WDMAV4": {
        "description": "Modern kahve kültürünün global bir temsilcisi olan Starbucks, Rodos'un kozmopolit enerjisini kentsel silüetin neşeli bir parçası haline getiriyor. Şık tasarımı ve kentin enerjisini yansıtan ferah dokusuyla, kentsel ritmi kaliteli bir kahve eşliğinde ferah bir atmosferde solumak isteyenlerin favori ve havadar bir durağıdır.",
        "description_en": "A global representative of modern coffee culture, Starbucks makes Rhodes' cosmopolitan energy a joyful part of the urban silhouette. With stylish design and a fresh texture reflecting the city me's energy, it is a favorite and airy stop for those wanting to breathe in the urban rhythm in a fresh atmosphere accompanied by a high-quality coffee."
    },
    "ChIJM208--VhlRQRANPf14K2YTo": {
        "description": "Kentin modern sosyal yüzünü temsil eden bu karakteristik kafe, taze kahveleri ve kentin enerjisini yansıtan neşeli sosyal dokusuyla bilinir. Şık tasarımı ve kente karakter katan samimi yapısıyla kenti keşfeden gezginlerin kentsel koşturmacadan uzaklaşıp nefes alabileceği kaliteli ve havadar bir keşif durağıdır.",
        "description_en": "This characteristic cafe representing the city me's modern social face is known for its fresh coffees and joyful social texture reflecting the city me's energy. With its stylish design and sincere structure adding character to the city, it is a high-quality and airy discovery stop where travelers exploring the city can move away from urban hustle and breathe."
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

print(f"✅ Rhodes Part 2: Enriched {count} items.")
