import json
import os

new_lyon_extra2 = [
    {
        "name": "Musée de la Soie (Atölye)",
        "name_en": "Silk Workshop (Maison des Canuts)",
        "area": "Croix-Rousse",
        "category": "Deneyim",
        "tags": ["ipek", "dokuma", "sanat", "zanaat"],
        "distanceFromCenter": 1.4,
        "lat": 45.7766,
        "lng": 4.8341,
        "price": "low",
        "rating": 4.8,
        "description": "Lyon'un ipek mirasını koruyan bu atölyede, devasa ahşap tezgahlarda ipeğin nasıl can bulduğunu canlı olarak izleyebilirsiniz.",
        "description_en": "A living museum where you can watch master weavers operate historic looms and learn about Lyon's 500-year-old silk industry."
    },
    {
        "name": "Saint-Antoine (Gastronomi Yürüyüşü)",
        "name_en": "Saint-Antoine Food Walk",
        "area": "Saône Kıyısı",
        "category": "Deneyim",
        "tags": ["pazar", "nehir", "gurme", "lokal"],
        "distanceFromCenter": 0.4,
        "lat": 45.7612,
        "lng": 4.8318,
        "price": "free",
        "rating": 4.8,
        "description": "Nehir kıyısındaki Saint-Antoine pazarında yerel peynirlerin ve fırınlanmış tavuk kokularının eşliğinde yapılan en 'Lyonvari' sabah yürüyüşü.",
        "description_en": "The ultimate local morning routine: strolling through the riverside market stalls, sampling regional delicacies while overlooking the Saône."
    },
    {
        "name": "Place des Jacobins (Işıklandırma)",
        "name_en": "Jacobins Square Illumination",
        "area": "Presqu'île",
        "category": "Manzara",
        "tags": ["gece", "ışık", "fıskiye", "estetik"],
        "distanceFromCenter": 0.5,
        "lat": 45.7605,
        "lng": 4.8295,
        "price": "free",
        "rating": 4.9,
        "description": "Geceleri bembeyaz ve masalsı bir ışıkla aydınlanan Jacobins fıskiyesi, Lyon'un en zarif ve huzurlu gece manzaralarından birini sunar.",
        "description_en": "At night, the grand marble fountain of Place des Jacobins is beautifully lit, highlighting its intricate sculptures and creating a magical urban atmosphere."
    },
    {
        "name": "Traboule du Boeuf",
        "name_en": "Le Boeuf Traboule",
        "area": "Vieux Lyon",
        "category": "Tarihi",
        "tags": ["traboule", "gizli geçit", "rönesans", "mimari"],
        "distanceFromCenter": 0.6,
        "lat": 45.7625,
        "lng": 4.8270,
        "price": "free",
        "rating": 4.8,
        "description": "Rue du Bœuf üzerinde yer alan ve Vieux Lyon'un en geniş avlularından birine açılan, pembe tonlu taşları ve kemerleriyle ünlü tarihi geçit.",
        "description_en": "One of the most impressive traboules in the Old Town, leading through successive courtyards with elegant Renaissance features."
    }
]

def enrich_lyon_extra2():
    filepath = 'assets/cities/lyon.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_lyon_extra2:
        if new_h['name'].lower() not in existing_names:
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1543783232-af412b852fc7?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    # Current 100 + 3 = 103 (one might be duplicate)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_lyon_extra2()
print(f"Lyon now has {count} highlights.")
