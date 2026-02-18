import json

# Manual enrichment data (Tromso Batch 2 FINAL: 15 items)
updates = {
    "Ersfjord Beach": {
        "description": "Senja Adası yakınındaki beyaz kumlu otantik kuzey plajı. Arktik okyanus, yürüyüş, fotoğrafçılık ve doğa.",
        "description_en": "Authentic northern beach with white sand near Senja Island. Arctic ocean, hiking, photography, and nature."
    },
    "Finnlandsfjellet": {
        "description": "Tromsø yakınındaki dağ zirvesi, orta düzey yürüyüş ve panorama. Yaz trekkingleri, kış turları ve manzara.",
        "description_en": "Mountain peak near Tromsø for intermediate hiking and panorama. Summer treks, winter tours, and scenery."
    },
    "Brim Explorer": {
        "description": "Elektrikli hibrit tekne turları, balina gözlemi ve fiyort keşfi. Çevre dostu turizm, vahşi yaşam ve arktik deneyim.",
        "description_en": "Electric hybrid boat tours for whale watching and fjord exploration. Eco-friendly tourism, wildlife, and Arctic experience."
    },
    "Hermes II": {
        "description": "Tarihi gemi ile fiyort turları ve balina gözlem seferleri. Deniz macerası, fotografci turları ve gezici restoran.",
        "description_en": "Fjord tours and whale watching voyages on historic ship. Sea adventure, photographer tours, and floating restaurant."
    },
    "Tromsø Outdoor": {
        "description": "Outdoor ekipman mağazası ve macera turları organizatörü. Kamp malzemeleri, kış ekipmanları ve doğa etkinlikleri.",
        "description_en": "Outdoor equipment store and adventure tours organizer. Camping supplies, winter gear, and nature activities."
    },
    "Skittenelv Camping": {
        "description": "Doğa içinde kamp alanı, kulübeler ve karavan parkı. Kuzey Işıkları izleme, huzurlu konaklama ve fiyort kenarı.",
        "description_en": "Campsite in nature with cabins and caravan park. Northern Lights viewing, peaceful accommodation, and fjordside."
    },
    "Sommarøy Arctic Hotel": {
        "description": "Sommarøy Adası'nda arktik otel, deniz manzarası ve aurora turları. Balıkçı köyü atmosferi, rahatlatıcı tatil.",
        "description_en": "Arctic hotel on Sommarøy Island with sea views and aurora tours. Fishing village atmosphere, relaxing vacation."
    },
    "Amfi Pyramiden": {
        "description": "Şehir merkezindeki alışveriş merkezi, Norveç markaları ve restoranlar. Günlük alışveriş, sinema ve pratik konum.",
        "description_en": "Shopping center in city center with Norwegian brands and restaurants. Daily shopping, cinema, and practical location."
    },
    "Posthallen": {
        "description": "Tarihi posta binasında kültür ve alışveriş merkezi. Restoranlar, butikler ve topluluk etkinlikleri.",
        "description_en": "Culture and shopping center in historic post office building. Restaurants, boutiques, and community events."
    },
    "Rødbanken": {
        "description": "Tarihi eski banka binası, şimdi bar ve restoran olarak hizmet veriyor. Art deco mimari, kokteyller ve gece hayatı.",
        "description_en": "Historic old bank building, now serving as bar and restaurant. Art deco architecture, cocktails, and nightlife."
    },
    "Norrøna Concept Store": {
        "description": "Norveç outdoor giyim markasının konsept mağazası. Tırmanış, kayak ve macera ekipmanları.",
        "description_en": "Concept store of Norwegian outdoor clothing brand. Climbing, skiing, and adventure equipment."
    },
    "Fjällräven Store": {
        "description": "İsveç outdoor markasının sırt çantası ve doğa kıyafetleri mağazası. Kanken, yürüyüş ekipmanları ve İskandinav tasarımı.",
        "description_en": "Swedish outdoor brand store for backpacks and nature clothing. Kanken, hiking equipment, and Scandinavian design."
    },
    "Chasing Lights": {
        "description": "Kuzey Işıkları avcılığı turları düzenleyen profesyonel şirket. Aurora safari, fotoğrafçılık rehberliği ve kış deneyimi.",
        "description_en": "Professional company organizing Northern Lights hunting tours. Aurora safari, photography guidance, and winter experience."
    },
    "Wandering Owl": {
        "description": "Kuzey Işıkları ve fiyort turları düzenleyen butik tur operatörü. Küçük gruplar, özel deneyimler ve yerel rehberler.",
        "description_en": "Boutique tour operator organizing Northern Lights and fjord tours. Small groups, private experiences, and local guides."
    },
    "Gifts of Norway": {
        "description": "Norveç hediyelik eşyaları ve yerel ürünler mağazası. Trol figürleri, örme ürünler ve Norveç hatıraları.",
        "description_en": "Norwegian souvenirs and local products shop. Troll figures, knitted products, and Norwegian memorabilia."
    }
}

filepath = 'assets/cities/tromso.json'
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

print(f"\n✅ Manually enriched {count} items (Tromso Batch 2 FINAL).")
