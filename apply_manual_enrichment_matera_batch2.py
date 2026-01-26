import json

# Manual enrichment data (Matera Batch 2 FINAL: 19 items)
updates = {
    "La Focaccia della Mattina": {
        "description": "Taze pişmiş focaccia ve kahvaltı lezzetleri sunan sabah fırını. Yerel malzemeler, ev yapımı hamur işleri ve sabah enerjisi.",
        "description_en": "Morning bakery serving freshly baked focaccia and breakfast treats. Local ingredients, homemade pastries, and morning energy."
    },
    "Gelateria Belfiore": {
        "description": "Artisan dondurma ve sorbe sunan geleneksel gelateria. Taze meyve tatları, İtalyan gelato sanatı ve yaz serinliği.",
        "description_en": "Traditional gelateria serving artisan ice cream and sorbet. Fresh fruit flavors, Italian gelato art, and summer coolness."
    },
    "Shibuya": {
        "description": "Japon mutfağı ve sushi sunan modern restoran. Uzak Doğu lezzetleri, fusion yorumlar ve şık atmosfer.",
        "description_en": "Modern restaurant serving Japanese cuisine and sushi. Far East flavors, fusion interpretations, and stylish atmosphere."
    },
    "Nadi": {
        "description": "Vejetaryen ve sağlıklı yemek seçenekleri sunan modern kafe. Organik malzemeler, smoothie ve hafif öğle yemeği.",
        "description_en": "Modern cafe serving vegetarian and healthy food options. Organic ingredients, smoothies, and light lunch."
    },
    "Taverna La Focagna": {
        "description": "Geleneksel Basilicata mutfağını sunan otantik taverna. Ev yapımı makarna, yerel şaraplar ve köy atmosferi.",
        "description_en": "Authentic taverna serving traditional Basilicata cuisine. Homemade pasta, local wines, and village atmosphere."
    },
    "Le Bubbole": {
        "description": "Yerel bira ve aperitivo sunan rahat bar. Craft bira seçkisi, atıştırmalıklar ve sosyal ortam.",
        "description_en": "Relaxed bar serving local beer and aperitivo. Craft beer selection, snacks, and social setting."
    },
    "L'Arturo": {
        "description": "Deniz ürünleri ve balık yemekleriyle ünlü şık restoran. Taze malzemeler, Akdeniz lezzetleri ve fine-dining.",
        "description_en": "Elegant restaurant famous for seafood and fish dishes. Fresh ingredients, Mediterranean flavors, and fine-dining."
    },
    "Enoteca Vino & Dintorni": {
        "description": "Basilicata ve Puglia şaraplarına odaklanan şarap barı. Aglianico, Primitivo ve yerel peynirler eşliğinde tadım.",
        "description_en": "Wine bar focusing on Basilicata and Puglia wines. Tasting with Aglianico, Primitivo, and local cheeses."
    },
    "Pietrapertosa": {
        "description": "Basilicata'nın en yüksek köyü, kayalık manzara ve tırmanış. Dolomiti Lucane içinde, macera ve fotoğrafçılık.",
        "description_en": "Basilicata's highest village with rocky scenery and climbing. Within Lucanian Dolomites, adventure, and photography."
    },
    "Church of San Domenico": {
        "description": "Gotik ve Romanesk mimarinin harmanlandığı ortaçağ kilisesi. Dini sanat, fresk kalıntıları ve tarihi atmosfer.",
        "description_en": "Medieval church blending Gothic and Romanesque architecture. Religious art, fresco remains, and historic atmosphere."
    },
    "Sassula": {
        "description": "Mağara ortamında yaratıcı kokteyller sunan bar. Sassi atmosferi, yerel içecekler ve gece hayatı.",
        "description_en": "Bar serving creative cocktails in cave setting. Sassi atmosphere, local drinks, and nightlife."
    },
    "5 Lire": {
        "description": "Nostaljik dekorasyonlu bar ve restoran, İtalyan retro atmosferi. Uygun fiyat, sosyal mekan ve yerli favorisi.",
        "description_en": "Bar and restaurant with nostalgic decor, Italian retro atmosphere. Affordable, social venue, and local favorite."
    },
    "Enoteca Il Buco": {
        "description": "Küçük ve samimi şarap barı, yerel şaraplar ve antipasti. Romantik atmosfer, bilgili personel ve tadım.",
        "description_en": "Small and intimate wine bar with local wines and antipasti. Romantic atmosphere, knowledgeable staff, and tasting."
    },
    "Bar Ridola": {
        "description": "Piazza Ridola'daki popüler kafe-bar, espresso ve aperitivo. Meydan manzarası, tarihi konum ve sosyal sahne.",
        "description_en": "Popular cafe-bar in Piazza Ridola with espresso and aperitivo. Square views, historic location, and social scene."
    },
    "Bar Sottozero": {
        "description": "Dondurma ve taze içecekler sunan yaz mekanı. Granita, meyveli içecekler ve serinletici mola.",
        "description_en": "Summer venue serving ice cream and fresh drinks. Granita, fruit drinks, and refreshing break."
    },
    "Mercato Ortofrutticolo": {
        "description": "Yerel meyve ve sebzelerin satıldığı pazar. Taze ürünler, Basilicata tarımı ve yerel yaşam.",
        "description_en": "Market selling local fruits and vegetables. Fresh produce, Basilicata agriculture, and local life."
    },
    "Parco Giovanni Paolo II": {
        "description": "Şehir parkı, yürüyüş yolları ve dinlenme alanları. Aileler için yeşil alan, piknik ve açık hava.",
        "description_en": "City park with walking paths and rest areas. Green area for families, picnic, and outdoors."
    },
    "Chiesa di Santa Maria di Costantinopoli": {
        "description": "Bizans etkili tarihi kilise, ikonalar ve dini miras. Doğu Hristiyanlığı izleri ve kültürel önem.",
        "description_en": "Historic church with Byzantine influence, icons, and religious heritage. Eastern Christian traces and cultural importance."
    },
    "Stadio XXI Settembre": {
        "description": "Matera'nın futbol stadyumu, yerel maçlar ve spor etkinlikleri. Calcio kültürü ve şehir gururu.",
        "description_en": "Matera's football stadium for local matches and sports events. Calcio culture and city pride."
    }
}

filepath = 'assets/cities/matera.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data['highlights']:
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        print(f"Enriched: {name}")
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Manually enriched {count} items (Matera Batch 2 FINAL).")
