#!/usr/bin/env python3
import json

updates = {
    "ChIJtaO8wQEPWxMRa9Z5FU1XI0s": {
        "description": "Arnavutluk'un güneyindeki dağların eteğinden fışkıran bu büyüleyici doğal su kaynağı, merkezden dışa doğru koyulaşan masmavi rengiyle bir 'Mavi Göz'ü andırır. Buz gibi suları ve kentin ruhuna huzur veren mistik enerjisiyle, doğanın yaratıcı gücünü keşfetmek isteyen gezginlerin en favori ve havadar duraklarından biridir.",
        "description_en": "This fascinating natural spring gushing from the foot of the mountains in southern Albania resembles a 'Blue Eye' with its deep blue color darkening from the center outward. With its icy waters and mystical energy bringing peace to the city me's spirit, it is one of the favorite and airy stops for travelers wanting to explore nature's creative power."
    },
    "ChIJX4chYABrWxMREQL9C4wDDQU": {
        "description": "Ksamil'in en merkezi ve neşeli noktalarından biri olan Public Beach, masmavi bir denize karşı uzanan bembeyaz kumsalıyla kentin yaz ruhunu yansıtır. Karşıdaki adaları seyrederek güneşin tadını çıkarabileceğiniz bu alan, kentin enerjisini ve kültürel kimliğini en samimi haliyle ziyaretçilere sunan popüler bir duraktır.",
        "description_en": "One of Ksamil me's most central and joyful points, Public Beach reflects the city me's summer spirit with its pure white sandy beach stretched against a deep blue sea. This area where you can enjoy the sun while watching the islands opposite is a popular stop presenting the city me's energy and cultural identity to visitors in its most sincere form."
    },
    "ChIJTV2KEtJrWxMRqF563Qkr-4k": {
        "description": "Bölgeye has taze deniz ürünlerini ve Balkan mezelerini modern bir sunumla buluşturan Restuarant Momento, kentin lezzet hafızasında önemli bir yer tutar. Şık dekorasyonu ve kentin kozmopolit ritmini dengeleyen asude atmosferiyle, kenti keşfeden gurme gezginlerin en sevilen ve kaliteli lezzet rotaları arasındadır.",
        "description_en": "Meeting local fresh seafood and Balkan appetizers with a modern presentation, Restaurant Momento holds an important place in the city me's flavor memory. With its stylish decoration and serene atmosphere balancing the city me's cosmopolitan rhythm, it is among the favorite and high-quality flavor routes of gourmet travelers exploring the city."
    },
    "ChIJdcIYPtJrWxMRO45MJod-fAI": {
        "description": "Deniz kıyısında yer alan ve taze balık mönüsüyle tanınan Joni Restaurant, Ksamil'in sahil şıkliğini ve yerel gastronomisini temsil ediyor. Gün batımında kentin enerjisini en yüksek seviyede hissettiren manzarası ve kente karakter katan profesyonel servisiyle, kenti keşfedenlerin en heyecan verici ve kaliteli duraklarından biridir.",
        "description_en": "Located on the seaside and known for its fresh fish menu, Joni Restaurant represents Ksamil me's coastal chic and local gastronomy. With its view making you feel the city me's energy at the highest level at sunset and professional service adding character to the city, it is one of the most exciting and high-quality stops for those exploring the city."
    },
    "ChIJwRJWXsdrWxMRFd9V0cpnmR8": {
        "description": "Mavi Göz kaynağının hemen yanı başında yer alan bu kafe, doğanın kalbinde huzurlu bir mola durağı niteliğindedir. Suyun tınısı ve kentin ruhuna karakter katan sessizliğiyle kenti keşfeden gezginlerin en sevilen ve kentsel koşturmacadan uzak dinlenme noktalarından biridir.",
        "description_en": "Located right next to the Blue Eye spring, this cafe is in the quality of a peaceful break stop in the heart of nature. Among the favorite rest points of travelers exploring the city, away from urban hustle, with the rhythm of water and silence adding character to the city me's spirit."
    },
    "ChIJOYuROqVrWxMRd4j1BoZOnL8": {
        "description": "Butrint Gölü kıyısındaki bu özel mekan, Ksamil'in ünlü midye yetiştiriciliği mirasını sofralara taşıyan eşsiz bir deneyim sunar. Göl manzarası ve kentin tarihsel evrimini yansıtan otantik yapısıyla kentin enerjisini ve kültürel kimliğini lezzetle harmanlayan paha biçilemez bir gastronomi durağıdır.",
        "description_en": "This special venue on the shores of Lake Butrint offers a unique experience bringing Ksamil me's famous mussel farming heritage to the table. It's a priceless gastronomy stop blending the city me's energy and cultural identity with flavor, with its lake view and authentic structure reflecting the city's historical evolution."
    },
    "ChIJUf5fAwBrWxMR8nUYCl0wa2E": {
        "description": "Ksamil'in neşeli sokaklarında taze kahve kokusunu takip etmek isteyenler için Coffee Time, kentin modern sosyal yüzünü temsil eder. Şık tasarımı ve kentin enerjisini yansıtan neşeli sosyal dokusuyla, kentsel ritmi ferah bir atmosferde solumak isteyen gezginlerin en favori ve havadar durakları arasındadır.",
        "description_en": "For those wanting to follow the scent of fresh coffee in the joyful streets of Ksamil, Coffee Time represents the city me's modern social face. Among the favorite and airy stops of travelers wanting to breathe in the urban rhythm in a fresh atmosphere with its stylish design and joyful social texture reflecting the city me's energy."
    },
    "ChIJnarQ1h9rWxMRR45wXOZyox4": {
        "description": "Ksamil'in en tatlı köşelerinden biri olan Sweet Corner, el yapımı tatlıları ve neşeli atmosferiyle kente karakter katan bir duraktır. Geleneksel pastane tariflerini modern bir dokunuşla harmanlayan mekan, kenti keşfeden profesyor gezginlerin en sevilen ve kentin enerjisini en yüksek seviyede hissettiği keşif noktalarındandır.",
        "description_en": "One of the sweetest corners of Ksamil, Sweet Corner is a stop adding character to the city with its handmade sweets and joyful atmosphere. The venue blending traditional bakery recipes with a modern touch is among the favorite discovery points of professional travelers exploring the city where they feel the city's energy at the highest level."
    },
    "ChIJw-6ERQBrWxMRC2CCZu9ugEk": {
        "description": "Ksamil'in ışıltılı akşamlarında şık kokteylleri ve modern müzik tınılarını buluşturan Muzg Lounge, kentin kozmopolit enerjisini temsil ediyor. Modern tasarımı ve kentin haritasına karakter katan elit atmosferiyle kenti keşfedenlerin kentsel koşturmacadan uzaklaşıp eğlenebileceği kaliteli ve havadar bir duraktır.",
        "description_en": "Meeting stylish cocktails and modern music tones on the glittering evenings of Ksamil, Muzg Lounge represents the city me's cosmopolitan energy. With its modern design and elite atmosphere adding character to the city map, it is a high-quality and airy stop where those exploring the city can move away from urban hustle and have fun."
    },
    "ChIJU0o8BzVrWxMRGJ88-gK6tQE": {
        "description": "Masmavi bir denize ve karşıdaki üç adaya hakim konumuyla 3 Island Lounge, kentin en prestijli ve estetik duraklarından biridir. Panaromik manzarası ve kentin enerjisini elit bir akşamla birleştiren yapısıyla kentin estetik gücünü soluyabileceğiniz iddialı ve havadar bir keşif noktasıdır.",
        "description_en": "With its location dominating a deep blue sea and the three islands opposite, 3 Island Lounge is one of the city's most prestigious and aesthetic stops. It is an ambitious and airy discovery point where you can breathe in the city's aesthetic power with its panoramic view and structure combining the city's energy with an elite evening."
    },
    "ChIJY_4bYDBrWxMRHZtknMeJ6RI": {
        "description": "Adından da anlaşılacağı gibi Ksamil'in en asude ve rahatlatıcı duraklarından olan Chill Out, kentsel dinamizmi huzurlu bir tempoya çekiyor. Bohem tasarımı ve kentin ruhuna karakter katan misafirperverliğiyle kenti keşfedenlerin en favori ve enerjisi en yüksek hissettiren havadar rotaları arasındadır.",
        "description_en": "As the name suggests, being one of the most serene and relaxing stops of Ksamil, Chill Out pulls urban dynamism into a peaceful tempo. Among the favorite and airy routes of those exploring the city making them feel the energy at the highest, with its bohemian design and hospitality adding character to the city me's spirit."
    },
    "ChIJm9oeSzxrWxMRRTzH9rFlcwY": {
        "description": "Ksamil gece hayatına modern ve sofistike bir soluk getiren Noctura, kentin kozmopolit ritmini ferah bir atmosferde sunuyor. Şık ışıklandırması ve kentin enerjisini yansıtan neşeli sosyal dokusuyla, kentsel silüeti tamamlayan iddialı ve kaliteli bir akşam rotasıdır.",
        "description_en": "Bringing a modern and sophisticated breath to Ksamil nightlife, Noctura offers the city me's cosmopolitan rhythm in a fresh atmosphere. With its stylish lighting and joyful social texture reflecting the city's energy, it is an ambitious and high-quality evening route completing the urban silhouette."
    },
    "ChIJgWTbf5JrWxMRQuHLSzooeN8": {
        "description": "Ksamil'in sahil şeridindeki en yaratıcı kokteyllere imza atan Vamos Bar, kentin enerjisini ve neşesini her bardağa taşıyor. Modern tasarımı ve kentin haritasına karakter katan popüler atmosferiyle kenti keşfeden gezginlerin en sevilen ve kentsel koşturmacadan uzak eğlence durakları arasındadır.",
        "description_en": "Creating the most creative cocktails on Ksamil's coastline, Vamos Bar carries the city's energy and joy to every glass. Among the favorite entertainment stops of travelers exploring the city, away from urban hustle, with modern design and popular atmosphere adding character to the city map."
    },
    "ChIJw5YU8i5rWxMRrz6ZZO6G10c": {
        "description": "Deniz tınıları ve modern konforu birleştiren Foga Lounge, Ksamil'in sahil silüetine estetik bir soluk getiriyor. Şık terası ve kentin ruhuna karakter katan ferah dokusuyla kenti keşfedenlerin kentsel ritmi en elit haliyle hissedebileceği en favori ve havadar keşif noktaları arasındadır.",
        "description_en": "Combining sea tones and modern comfort, Foga Lounge brings an aesthetic breath to Ksamil's coastal silhouette. Among the favorite and airy discovery points where those exploring the city can feel the urban rhythm in its most elite form with its stylish terrace and fresh texture adding character to the city me's spirit."
    },
    "ChIJJxW01jtrWxMR_Q7Ca24CkJ8": {
        "description": "Uzak Doğu lezzetlerini Balkan sahilinin şıklığıyla harmanlayan Dips Lounge, Ksamil'de kentin kozmopolit enerjisini temsil ediyor. Minimalist tasarımı ve kentin enerjisini elit bir atmosferle birleştiren yapısıyla kentin estetik gücünü soluyabileceğiniz iddialı ve prestijli bir kentsel duraktır.",
        "description_en": "Blending Far East flavors with the chic of the Balkan coast, Dips Lounge represents the city's cosmopolitan energy in Ksamil. It is an ambitious and prestigious urban stop where you can breathe in the city's aesthetic power with its minimalist design and structure combining the city me's energy with an elite atmosphere."
    },
    "ChIJgyp80cFrWxMRFpRpERV7OLw": {
        "description": "Ksamil'in modern yüzünü ve neşeli genç enerjisini yansıtan Bliss Lounge, kentin en popüler ve havalı sosyal duraklarından biridir. Şık tasarımı ve kentin dünden bugüne sosyal tarihine modern bir ekleme yapan yapısıyla kenti keşfeden gezginlerin en sevilen ve kaliteli rotaları arasındadır.",
        "description_en": "Reflecting Ksamil me's modern face and joyful young energy, Bliss Lounge is one of the city's most popular and cool social stops. Among the favorite and high-quality routes of travelers exploring the city, with its stylish design and structure making a modern addition to the city's social history from yesterday to today."
    },
    "ChIJbdErbQBrWxMRtNsq6z4RYH4": {
        "description": "Möhteşem gün batımı manzaralarıyla ünlü olan bu sahil barı, kentin enerjisinin akşam saatlerinde romantik bir ritme dönüştüğü noktadır. Kumların üzerindeki rahat atmosferi ve kentin taze deniz havasıyla kentsel koşturmacadan uzaklaşıp huzur bulabileceğiniz samimi ve havadar bir keşif durağıdır.",
        "description_en": "This beach bar famous for magnificent sunset views is the point where the city me's energy turns into a romantic rhythm in evening hours. It is a sincere and airy discovery stop where you can move away from urban hustle and find peace with its relaxed atmosphere on the sands and the city me's fresh sea air."
    },
    "ChIJ6cuOQwBrWxMRzM-8ogXyZD0": {
        "description": "Lüks ve doğallığı sahil şeridinde birleştiren Orion, Ksamil'in en prestijli ve kaliteli sahil duraklarından biridir. Turkuaz denize hakim konumu ve kentin ruhuna karakter katan ferah dokusuyla kenti keşfeden profesyor gezginlerin en favori ve enerjisi en yüksek hissettiren duraklardandır.",
        "description_en": "Combining luxury and naturalness on the coastline, Orion is one of Ksamil me's most prestigious and high-quality coastal stops. Among the favorite stops of professional travelers exploring the city making them feel the energy at the highest, with its position dominating the turquoise sea and fresh texture adding character to the city me's spirit."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/ksamil.json.draft'
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

print(f"✅ Ksamil: Enriched {count} items.")
