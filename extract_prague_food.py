
import json
import os

# Define paths
input_path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/prag.json'
output_path = '/Users/anilebru/Desktop/prag_mekanlar.json'

# Categories to extract
target_categories = ['Yeme-İçme', 'Bar', 'Kafe']

try:
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'highlights' not in data:
        print("Error: 'highlights' key not found in JSON.")
        exit(1)

    filtered_places = []
    
    for place in data['highlights']:
        # Check category (case-insensitive for safety)
        category = place.get('category', '')
        if any(target.lower() == category.lower() for target in target_categories):
            filtered_places.append(place)

    # Write to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(filtered_places, f, ensure_ascii=False, indent=2)

    print(f"Successfully extracted {len(filtered_places)} places to {output_path}")

except Exception as e:
    print(f"An error occurred: {e}")
