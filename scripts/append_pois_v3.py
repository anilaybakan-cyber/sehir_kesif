
import json
import os

cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"

additions = {
    "budapeste.json": [
        {
            "name": "Vajdahunyad Castle",
            "area": "City Park",
            "category": "Tarihi",
            "tags": ["kale", "park", "masalsı"],
            "distanceFromCenter": 2.5,
            "lat": 47.515,
            "lng": 19.082,
            "price": "free",
            "rating": 4.6,
            "description": "Şehir Parkı içindeki masalsı kale complexi. Farklı mimari stillerin karışımı.",
            "description_en": "Fairytale castle complex in City Park. Mixture of different architectural styles.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Gündüz",
            "bestTime_en": "Daytime",
            "tips": "Bahçesi ücretsizdir. Kışın önünde buz pateni pisti kurulur."
        }
    ],
    "viyana.json": [
        {
            "name": "Spanish Riding School",
            "area": "Hofburg",
            "category": "Kültür",
            "tags": ["at", "gösteri", "barok"],
            "distanceFromCenter": 0.0,
            "lat": 48.207,
            "lng": 16.366,
            "price": "high",
            "rating": 4.6,
            "description": "Dünyaca ünlü Lipizzaner atlarının Barok salondaki dansı. UNESCO listesinde.",
            "description_en": "World famous Lipizzaner horses dancing in Baroque hall. On UNESCO list.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Sabah",
            "bestTime_en": "Morning",
            "tips": "Sabah antrenmanlarını izlemek daha ucuzdur."
        }
    ]
}

def append_pois():
    for filename, new_pois in additions.items():
        filepath = os.path.join(cities_dir, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            existing_names = {poi['name'] for poi in data['highlights']}
            added_count = 0
            
            for poi in new_pois:
                if poi['name'] not in existing_names:
                    data['highlights'].append(poi)
                    added_count += 1
            
            if added_count > 0:
                with open(filepath, 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"{filename}: Added {added_count} new POIs. Total: {len(data['highlights'])}")
            else:
                print(f"{filename}: No new POIs added.")
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    append_pois()
