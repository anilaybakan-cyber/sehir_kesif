import json
import os

updates = {
    "Ibiza": {
        "Restaurante Pasta Luego de Pescado": {
            "description": "Ibiza Marina'nın en taze deniz ürünlerini İtalyan el yapımı makarnalarıyla birleştiren bu mekan, kentin gastronomi dünyasında 'denizden tabağa' felsefesinin en lezzetli temsilcisidir. Şık tasarımı ve Dalt Vila surlarına bakan manzarasıyla, kentin enerjisini sofistike bir akşam yemeğiyle taçlandırır.",
            "description_en": "Combining the freshest seafood of Ibiza Marina with Italian handmade pastas, this venue is the most delicious representative of the 'sea-to-plate' philosophy in the city's gastronomic world. With its chic design and views of the Dalt Vila walls, it crowns the city's energy with a sophisticated dinner.",
            "tips": "Istakozlu linguine imza yemeğidir; yüksek sezonda marina tarafındaki masalar için mutlaka rezervasyon yapın.",
            "tips_en": "The lobster linguine is the signature dish; be sure to book a table on the marina side during high season.",
            "category": "Restoran"
        },
        "SES Figueres": {
            "description": "Ibiza'nın Figueretas sahilinde, kentsel koşturmacadan uzaklaşıp denizin hemen kıyısında modern Akdeniz lezzetlerini keşfedebileceğiniz asude bir duraktır. Minimalist tasarımı ve kentin taze deniz havasıyla kentsel silüeti tamamlayan bu mekan, hem yerel halkın hem de kenti keşfedenlerin favori mola noktasıdır.",
            "description_en": "A serene stop on Ibiza's Figueretas coast where you can escape the urban hustle and discover modern Mediterranean flavors right by the sea. With its minimalist design and fresh sea air, this venue complements the urban silhouette and is a favorite break point for both locals and travelers exploring the city.",
            "tips": "Günü batırmak için ideal bir noktadır; tapas tabakları paylaşmak için mükemmeldir.",
            "tips_en": "An ideal spot for watching the sunset; their tapas platters are perfect for sharing.",
            "category": "Restoran"
        }
    },
    "Budva": {
        "Restoran Kralj": {
            "description": "Budva Eski Şehir surlarının hemen yanında, Adriyatik'in en taze balıklarını ve Karadağ'ın geleneksel et yemeklerini krallara layık bir sunumla sunan köklü bir lezzet durağıdır. Tarihi dokusu ve kentin enerjisini yansıtan neşeli terasıyla, kentsel ritmi en lezzetli haliyle solumak isteyenlerin favorisidir.",
            "description_en": "A long-established flavor stop right next to the Budva Old Town walls, offering the freshest Adriatic fish and traditional Montenegrin meat dishes with a presentation fit for kings. With its historical texture and joyful terrace reflecting the city's energy, it's a favorite for those wanting to breathe in the urban rhythm in its most delicious form.",
            "tips": "Karadağ'ın meşhur 'Njegusi' peynirini ve füme etini mutlaka deneyin; akşam saatleri canlı müzik eşliğinde çok daha keyiflidir.",
            "tips_en": "Be sure to try Montenegro's famous 'Njegusi' cheese and smoked meat; evening hours are much more enjoyable with live music.",
            "category": "Restoran"
        },
        "Sidro Beach Bar": {
            "description": "Budva'nın neşeli sahil şeridinde, ayağınızın altında kum ve elinizde serinletici bir kokteylle kentin yaz enerjisini en yüksek seviyede hissettiren bir sahil noktasıdır. Salaş ve samimi yapısıyla kentsel koşturmacadan uzaklaşıp Adriyatik güneşinin tadını çıkarmak isteyenlerin vazgeçilmez durağıdır.",
            "description_en": "A seaside spot on Budva's joyful coastline that makes you feel the city's summer energy at the highest level with sand under your feet and a refreshing cocktail in your hand. With its casual and sincere structure, it's an indispensable stop for those wanting to move away from urban hustle and enjoy the Adriatic sun.",
            "tips": "Gündüz şezlong keyfi için erken gelin; akşamüstü DJ performansları kentin en hareketli sahil partilerine dönüşür.",
            "tips_en": "Arrive early for daytime sun loungers; late afternoon DJ performances turn into the city's most vibrant beach parties.",
            "category": "Sosyal"
        }
    },
    "Ksamil": {
        "Savory bistro café & lounge": {
            "description": "Ksamil'in turkuaz sularına yukarıdan bakan bu şık bistro, modern Arnavut mutfağını İtalyan etkileriyle harmanlayan rafine bir mönü sunuyor. Kentin enerjisini yansıtan tasarımı ve havadar terasıyla, kenti keşfeden gezginlerin kentsel koşturmacadan uzaklaşıp nefes alabileceği en kaliteli duraklardan biridir.",
            "description_en": "Overlooking the turquoise waters of Ksamil, this stylish bistro offers a refined menu blending modern Albanian cuisine with Italian influences. With its design reflecting the city's energy and its airy terrace, it is one of the highest quality stops where travelers exploring the city can move away from urban hustle and breathe.",
            "tips": "Özellikle deniz ürünlü risottosu çok başarılıdır; gün batımında yer bulmak için rezervasyon şarttır.",
            "tips_en": "Their seafood risotto is particularly successful; a reservation is essential to find a spot at sunset.",
            "category": "Restoran"
        }
    }
}

def apply_updates(city_file, city_updates):
    if not os.path.exists(city_file): return
    with open(city_file, 'r') as f:
        data = json.load(f)
    
    changed = False
    for h in data.get('highlights', []):
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

# Apply batches
apply_updates('assets/cities/ibiza.json', updates['Ibiza'])
apply_updates('assets/cities/budva.json', updates['Budva'])
apply_updates('assets/cities/ksamil.json', updates['Ksamil'])
