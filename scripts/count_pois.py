
import os
import json

cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
print(f"{'City':<20} | {'Count':<5} | {'Placeholders':<12}")
print("-" * 45)

for filename in sorted(os.listdir(cities_dir)):
    if filename.endswith(".json"):
        filepath = os.path.join(cities_dir, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                highlights = data.get('highlights', [])
                count = len(highlights)
                placeholders = sum(1 for h in highlights if h.get('imageUrl') == 'PLACEHOLDER')
                print(f"{filename.replace('.json', ''):<20} | {count:<5} | {placeholders:<12}")
        except Exception as e:
            print(f"{filename:<20} | ERROR | {str(e)}")
