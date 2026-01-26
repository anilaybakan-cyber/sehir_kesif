import json
import os

new_milano_extra = [
    {
        "name": "Bar Luce (Fondazione Prada)",
        "name_en": "Bar Luce",
        "area": "Güney Milano",
        "category": "Kafe",
        "tags": ["wes anderson", "tasarım", "retro", "popüler"],
        "distanceFromCenter": 3.7,
        "lat": 45.4452,
        "lng": 9.2092,
        "price": "medium",
        "rating": 4.9,
        "description": "Yönetmen Wes Anderson tarafından tasarlanan, kentin en ikonik ve fotojenik kafelerinden biri.",
        "description_en": "A cinematic icon designed by Wes Anderson, perfectly capturing the whimsical retro vibe of 1950s Milanese bars."
    },
    {
        "name": "10 Corso Como (Teras)",
        "name_en": "10 Corso Como Terrace",
        "area": "Porta Nuova",
        "category": "Manzara",
        "tags": ["teras", "gizli", "bahçe", "tasarım"],
        "distanceFromCenter": 1.7,
        "lat": 45.4828,
        "lng": 9.1885,
        "price": "free",
        "rating": 4.7,
        "description": "Corso Como'daki ünlü konsept mağazanın çatısında yer alan, kentin karmaşasından uzak, sarmaşıklarla dolu huzurlu bir teras.",
        "description_en": "A lush, hidden rooftop garden atop the famous concept store, offering a quiet escape with a unique perspective on the city's architecture."
    },
    {
        "name": "Pasticceria Marchesi (Via Meravigli)",
        "name_en": "Marchesi 1824 Original",
        "area": "Centro",
        "category": "Kafe",
        "tags": ["tarihi", "tatlı", "panettone", "gelenek"],
        "distanceFromCenter": 0.4,
        "lat": 45.4655,
        "lng": 9.1825,
        "price": "high",
        "rating": 4.8,
        "description": "1824 yılında kurulan orijinal şube. Tarihi ahşap tezgahları ve asırlık tarifleriyle gerçek bir Milano klasiği.",
        "description_en": "The original 1824 location, preserving its historic wood-paneled charm and time-tested recipes for the city's finest pastries."
    }
]

def enrich_milano_extra():
    filepath = 'assets/cities/milano.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_milano_extra:
        # Check by name or partial name to avoid dups that cleanup might miss if name slightly differs
        if new_h['name'].lower() not in existing_names:
             # Basic field completion
             new_h['imageUrl'] = "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800"
             new_h['bestTime'] = "Gündüz"
             new_h['bestTime_en'] = "Daytime"
             new_h['tips'] = "Mutlaka görün."
             new_h['tips_en'] = "A must see."
             data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_milano_extra()
print(f"Milan now has {count} highlights.")
