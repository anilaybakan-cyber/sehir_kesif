import json
import os

new_nice_final_fix = [
    {
        "name": "Eglise Notre-Dame-de-l'Assomption",
        "name_en": "Notre-Dame-de-l'Assomption Church",
        "area": "Vieux Nice",
        "category": "Tarihi",
        "tags": ["kilise", "tarih", "barok", "mimari"],
        "distanceFromCenter": 0.5,
        "lat": 43.6965,
        "lng": 7.2758,
        "price": "free",
        "rating": 4.6,
        "description": "Eski Nice'in kalbinde yer alan, sade dış cephesinin ardında muazzam bir barok zenginlik saklayan tarihi kilise.",
        "description_en": "A historic church in the heart of Old Nice, known for its austere facade hiding a richly decorated Baroque interior."
    },
    {
        "name": "Observatoire de la Côte d'Azur",
        "name_en": "Nice Observatory",
        "area": "Mont Gros",
        "category": "Manzara",
        "tags": ["gözlemevi", "astronomi", "mimari", "panoramik"],
        "distanceFromCenter": 4.0,
        "lat": 43.7275,
        "lng": 7.2995,
        "price": "medium",
        "rating": 4.7,
        "description": "Charles Garnier tarafından tasarlanan muazzam kubbesi ve kenti kucaklayan konumuyla Avrupa'nın en önemli astronomi merkezlerinden biri.",
        "description_en": "One of Europe's top astronomical research centers, featuring a spectacular dome designed by Charles Garnier and panoramic views."
    },
    {
        "name": "Parc d'Estienne d'Orves",
        "name_en": "Estienne d'Orves Park",
        "area": "Batı Nice",
        "category": "Park",
        "tags": ["doğa", "yürüyüş", "zeytin ağacı", "sessiz"],
        "distanceFromCenter": 2.2,
        "lat": 43.6995,
        "lng": 7.2450,
        "price": "free",
        "rating": 4.6,
        "description": "Yüzyıllık zeytin ağaçlarıyla dolu, Nice yerlilerinin yürüyüş ve piknik için tercih ettiği huzurlu bir tepe parkı.",
        "description_en": "A peaceful natural park on a hill filled with ancient olive trees, offering quiet trails and a glimpse into Nice's agricultural past."
    }
]

def enrich_nice_final_fix():
    filepath = 'assets/cities/nice.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_nice_final_fix:
        if new_h['name'].lower() not in existing_names:
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_nice_final_fix()
print(f"Nice now has {count} highlights.")
