import json
import os

new_marseille_final_fix2 = [
    {
        "name": "Musée de la Moto (Eski Değirmen)",
        "name_en": "Motorcycle Museum (Old Mill)",
        "area": "Kuzey Marseille",
        "category": "Müze",
        "tags": ["motosiklet", "tarih", "teknoloji", "koleksiyon"],
        "distanceFromCenter": 7.0,
        "lat": 43.3425,
        "lng": 5.4125,
        "price": "medium",
        "rating": 4.8,
        "description": "Eski bir un değirmeninin içine kurulmuş, her katta farklı bir döneme ait motosikletleri görebileceğiniz büyüleyici bir teknik müze.",
        "description_en": "Housed in a former four-story flour mill, this museum features an incredible collection of over 250 motorcycles dating back to the late 19th century."
    },
    {
        "name": "Parc de la Magalone (Manzara)",
        "name_en": "Magalone Garden View",
        "area": "Güney Marseille",
        "category": "Manzara",
        "tags": ["bahçe", "mimari", "estetik", "meydan"],
        "distanceFromCenter": 5.1,
        "lat": 43.2575,
        "lng": 5.3985,
        "price": "free",
        "rating": 4.6,
        "description": "Kentin güneyindeki bu tarihi bahçenin simetrik yapısı ve heykelleriyle oluşturduğu görsel bütünlük, fotoğrafçılar için eşsiz bir kare sunar.",
        "description_en": "The perfectly symmetrical classical layout of this 18th-century garden provides a stunning visual frame for the historic bastide."
    },
    {
        "name": "Place aux Huiles (Kanal Manzarası)",
        "name_en": "Place aux Huiles Canal View",
        "area": "Vieux-Port",
        "category": "Manzara",
        "tags": ["manzara", "liman", "mimari", "venedik vari"],
        "distanceFromCenter": 0.3,
        "lat": 43.2928,
        "lng": 5.3712,
        "price": "free",
        "rating": 4.7,
        "description": "Limanın bu bölümündeki binaların suya yansıması ve dar geçitler, Marseille'e Venedik vari bir hava katar.",
        "description_en": "The reflections of the historic facades in the canal-like inlet of the Old Port create a unique and timeless Mediterranean scene."
    },
    {
        "name": "Vallon des Auffes (Gizli Geçit)",
        "name_en": "Vallon des Auffes Hidden Passage",
        "area": "Endoume",
        "category": "Deneyim",
        "tags": ["keşif", "gizli", "liman", "yürüyüş"],
        "distanceFromCenter": 2.6,
        "lat": 43.2856,
        "lng": 5.3508,
        "price": "free",
        "rating": 4.8,
        "description": "Limanın içindeki dar binaların arasından denize çıkan gizli merdivenler ve geçitler, mahallenin en otantik keşif rotasıdır.",
        "description_en": "Under the arches of the viaduct lie hidden stairways and tiny passages used by fisherman for centuries to access their boats."
    }
]

def enrich_marseille_final_fix2():
    filepath = 'assets/cities/marsilya.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_marseille_final_fix2:
        if new_h['name'].lower() not in existing_names:
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1549221165-276f7c181342?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    # Current 98 + 4 = 102
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_marseille_final_fix2()
print(f"Marseille now has {count} highlights.")
