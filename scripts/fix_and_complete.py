
import json
import os

cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"

def fix_and_complete():
    # 1. Fix Names for Placeholders
    fixes = {
        "atina.json": {
            "description_snippet": "Antik Atina'nın mezarlığı",
            "new_name": "Kerameikos Archaeological Site"
        },
        "marakes.json": {
            "description_snippet": "Toprak yapılı antik köy",
            "new_name": "Ait Benhaddou"
        },
        "milano.json": {
            "description_snippet": "Milano tarzı pizza",
            "new_name": "Pizzeria Spontini Duomo"
        },
        "newyork.json": {
            "description_snippet": "South of Houston",
            "new_name": "SoHo Manhattan"
        },
        "venedik.json": {
            "description_snippet": "Eski gümrük binası",
            "new_name": "Punta della Dogana Museum"
        },
        "lyon.json": {
            "description_snippet": "Çikolata konusunda bir dünya markası",
            "new_name": "Bernachon Chocolats"
        }
    }

    # 2. Add Missing Items
    additions = {
        "singapur.json": {
            "name": "Lau Pa Sat",
            "area": "Downtown",
            "category": "Yeme-İçme",
            "tags": ["satay", "pazar", "tarihi"],
            "distanceFromCenter": 0.5,
            "lat": 1.280,
            "lng": 103.850,
            "price": "medium",
            "rating": 4.5,
            "description": "Şehrin göbeğinde tarihi hawker merkezi. Akşamları sokak trafiğe kapatılır ve satay (çöp şiş) sokağına dönüşür.",
            "description_en": "Historic hawker center in heart of city. Street is closed at night and becomes satay street.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Akşam",
            "bestTime_en": "Evening",
            "tips": "Satay sokağında (Satay Street) karides ve tavuk satay deneyin."
        },
        "viyana.json": {
            "name": "Rathaus (City Hall)",
            "area": "Innere Stadt",
            "category": "Tarihi",
            "tags": ["belediye", "gotik", "etkinlik"],
            "distanceFromCenter": 0.5,
            "lat": 48.210,
            "lng": 16.357,
            "price": "free",
            "rating": 4.7,
            "description": "Viyana Belediye Binası. Neo-Gotik mimarisi büyüleyici. Önündeki meydanda sürekli etkinlikler olur.",
            "description_en": "Vienna City Hall. Neo-Gothic architecture is fascinating. Always events in square in front.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Akşam",
            "bestTime_en": "Evening",
            "tips": "Kışın büyük Noel pazarı, yazın film festivali burada kurulur."
        }
    }

    # Execute Fixes
    for filename, fix in fixes.items():
        filepath = os.path.join(cities_dir, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            updated = False
            for poi in data['highlights']:
                if fix['description_snippet'] in poi['description']:
                    print(f"Fixing {filename}: {poi['name']} -> {fix['new_name']}")
                    poi['name'] = fix['new_name']
                    updated = True
                    break
            
            if updated:
                with open(filepath, 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                print(f"Skipped fixing {filename}: Could not find snippet '{fix['description_snippet']}'")
        
        except Exception as e:
            print(f"Error fixing {filename}: {e}")

    # Execute Additions
    for filename, new_poi in additions.items():
        filepath = os.path.join(cities_dir, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            existing_names = {poi['name'] for poi in data['highlights']}
            if new_poi['name'] not in existing_names:
                data['highlights'].append(new_poi)
                with open(filepath, 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"{filename}: Added {new_poi['name']}. Total: {len(data['highlights'])}")
            else:
                print(f"{filename}: {new_poi['name']} already exists.")
                
        except Exception as e:
            print(f"Error adding to {filename}: {e}")

if __name__ == "__main__":
    fix_and_complete()
