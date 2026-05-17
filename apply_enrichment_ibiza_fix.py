import json
import os

all_updates = {
    "Ibiza": {
        "Dalt Vila": {
            "description": "Ibiza'nın UNESCO Dünya Mirası listesindeki Dalt Vila, kentin labirentimsi sokakları ve devasa taş surlarıyla tarihe açılan kapısıdır. Fenikelilerden Romalılara kadar pek çok medeniyetin izini taşıyan bu kale-kent, her köşesinde Akdeniz'in masmavi sonsuzluğuna bakan stratejik burçlar barındırır.",
            "description_en": "Ibiza's UNESCO World Heritage site, Dalt Vila, is the city's gateway to history with its labyrinthine streets and massive stone walls. Carrying traces of civilizations from Phoenicians to Romans, this fortified city houses strategic bastions overlooking the endless blue Mediterranean at every corner.",
            "tips": "Surların en tepesine çıkmak için rahat ayakkabılar giyin; gün batımında kalenin üzerinden kentin ve limanın manzarası büyüleyicidir.",
            "tips_en": "Wear comfortable shoes to climb to the very top of the walls; the view of the city and harbor from the castle at sunset is magical.",
            "category": "Tarihi"
        },
        "Es Vedrà": {
            "description": "Ibiza'nın en mistik ve büyüleyici noktası olan Es Vedra, denizin ortasından aniden yükselen 400 metrelik devasa bir kireçtaşı kayasıdır. Kentin efsanelerine konu olan bu manyetik nokta, özellikle gün batımında gökyüzünün büründüğü renklerle uhrevi bir atmosfer sunar.",
            "description_en": "Ibiza's most mystical and captivating spot, Es Vedra, is a massive 400-meter limestone rock rising suddenly from the sea. Subject to many city legends, this magnetic point offers an ethereal atmosphere, especially with the colors of the sky at sunset.",
            "tips": "Gözlem noktasına giden toprak yol biraz bozuktur, dikkatli sürün; yanınıza şarabınızı ve atıştırmalıklarınızı alıp bu sessiz şölenin tadını çıkarın.",
            "tips_en": "The dirt road leading to the viewpoint is a bit rough, drive carefully; bring your wine and snacks to enjoy this silent spectacle.",
            "category": "Manzara"
        },
        "Pacha": {
            "description": "1973'ten beri kentin gece hayatının kalbi olan Pacha, dünya çapında bir ikon ve İbiza'nın en eski kulübüdür. İkonik kiraz logosuyla tanınan mekan, kentsel eğlence kültürünü lüks, şıklık ve en iyi DJ performanslarıyla birleştirerek unutulmaz bir deneyim sunar.",
            "description_en": "The heart of the city's nightlife since 1973, Pacha is a global icon and Ibiza's oldest club. Known for its iconic cherry logo, the venue combines urban entertainment culture with luxury, elegance, and the best DJ performances to offer an unforgettable experience.",
            "tips": "Kapıda kıyafet kuralı (dress code) oldukça katıdır, şık olun; VIP masalar için aylar öncesinden rezervasyon gerekebilir.",
            "tips_en": "The dress code at the door is quite strict, be stylish; VIP tables may require reservations months in advance.",
            "category": "Sosyal"
        },
        "Cala Comte": {
            "description": "Ibiza'nın en ikonik plajlarından biri olan Cala Comte, kristal berraklığındaki turkuaz suları ve ufuktaki küçük adacıklarıyla kentin doğal mücevheridir. Beyaz kumları ve sığ deniziyle kentsel koşturmacadan uzaklaşıp, adanın vahşi güzelliğini en saf haliyle deneyimleyebileceğiniz bir cennettir.",
            "description_en": "One of Ibiza's most iconic beaches, Cala Comte is a natural jewel of the city with crystal clear turquoise waters and small islets on the horizon. With its white sands and shallow sea, it's a paradise where you can escape urban hustle and experience the island's wild beauty in its purest form.",
            "tips": "Adanın en ünlü gün batımı noktalarından biridir; yer bulmak için erken gelin veya meşhur Sunset Ashram'da önceden rezervasyon yapın.",
            "tips_en": "One of the island's most famous sunset spots; arrive early for a spot or pre-book at the renowned Sunset Ashram.",
            "category": "Doğa"
        }
    }
}

def apply_updates(city_file, city_updates):
    if not os.path.exists(city_file): return
    with open(city_file, 'r') as f:
        data = json.load(f)
    
    changed = False
    highlights = []
    if isinstance(data, list):
        highlights = data
    else:
        highlights = data.get('highlights', [])
        
    for h in highlights:
        name = h.get('name')
        if name in city_updates:
            upd = city_updates[name]
            h['description'] = upd['description']
            h['description_en'] = upd['description_en']
            h['tips'] = upd['tips']
            h['tips_en'] = upd['tips_en']
            h['category'] = upd['category']
            changed = True
            
    if changed:
        with open(city_file, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {city_file}")

# Apply Ibiza update
apply_updates('assets/cities/ibiza.json', all_updates['Ibiza'])
