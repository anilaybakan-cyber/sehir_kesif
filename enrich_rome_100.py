import json
import os

new_h = {
    "name": "Via Margutta",
    "name_en": "Via Margutta",
    "area": "Centro Storico",
    "category": "Tarihi",
    "tags": ["sanat", "atölye", "sarmaşık", "film mekanı"],
    "distanceFromCenter": 1.0,
    "lat": 41.9086,
    "lng": 12.4797,
    "price": "free",
    "rating": 4.7,
    "description": "Roma'nın en sessiz ve sanat dolu sokaklarından biri. Sarmaşıklarla kaplı binaları ve sanat galerileriyle 'Roman Holiday' filmine de ev sahipliği yapmıştır.",
    "description_en": "One of Rome's quietest and most artistic streets. Home to the film 'Roman Holiday' with its ivy-covered buildings and art galleries.",
    "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
    "bestTime": "Öğleden sonra",
    "bestTime_en": "Afternoon",
    "tips": "Fellini'nin bir zamanlar burada yaşadığı binayı arayın.",
    "tips_en": "Look for the building where Fellini once lived."
}

def enrich_rome_100():
    filepath = 'assets/cities/roma.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_rome_100()
print(f"Rome hit 100 with {count} highlights.")
