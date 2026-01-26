import json
import os

new_budapest_final = [
    {
        "name": "Hungarian National Gallery (Magyar Nemzeti Galéria)",
        "name_en": "Hungarian National Gallery",
        "area": "Buda Kalesi",
        "category": "Müze",
        "tags": ["sanat", "macar sanatçılar", "saray", "manzara"],
        "distanceFromCenter": 1.2,
        "lat": 47.4961,
        "lng": 19.0400,
        "price": "medium",
        "rating": 4.7,
        "description": "Buda Kalesi'nin görkemli binalarında yer alan, Orta Çağ'dan günümüze Macar sanatının en kapsamlı koleksiyonunu barındıran müze.",
        "description_en": "Located within the magnificent buildings of Buda Castle, this museum houses the most comprehensive collection of Hungarian art from the Middle Ages to the present.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Müzenin kubbe kısmından şehrin en güzel panoramik manzaralarından birini izleyebilirsiniz.",
        "tips_en": "You can enjoy one of the city's most beautiful panoramic views from the museum's dome."
    },
    {
        "name": "Mai Manó Ház",
        "name_en": "Mai Mano House",
        "area": "Andrássy",
        "category": "Müze",
        "tags": ["fotoğraf", "tarihi bina", "stüdyo", "sanat"],
        "distanceFromCenter": 0.8,
        "lat": 47.5036,
        "lng": 19.0619,
        "price": "medium",
        "rating": 4.6,
        "description": "1894 yılından kalma, aslen bir fotoğraf stüdyosu olarak inşa edilmiş sekiz katlı muhteşem bir Neo-Rönesans bina ve şimdi bir fotoğraf galerisi.",
        "description_en": "A magnificent eight-story Neo-Renaissance building from 1894, originally built as a photography studio and now serving as a photography gallery.",
        "imageUrl": "https://images.unsplash.com/photo-1499781350541-7783f6c6a0c8?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Binanın dış cephesindeki seramik süslemeler ve içindeki 'Güneş Işığı Stüdyosu' (Sunlight Studio) eşsizdir.",
        "tips_en": "The ceramic decorations on the building's exterior and the 'Sunlight Studio' inside are unique."
    }
]

def enrich_budapest_final():
    filepath = 'assets/cities/budapeste.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'] for h in data.get('highlights', []))
    for new_h in new_budapest_final:
        if new_h['name'] not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_budapest_final()
print(f"Budapest reached its target with {count} highlights.")
