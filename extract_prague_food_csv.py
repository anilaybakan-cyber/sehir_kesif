
import json
import csv
import os

# Define paths
input_path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/prag.json'
output_path = '/Users/anilebru/Desktop/prag_mekanlar.csv'

# Categories to extract
target_categories = ['Yeme-İçme', 'Bar', 'Kafe']

# Fields to export
fields = [
    'id', 'name', 'name_en', 'category', 'area', 'area_en', 
    'rating', 'price', 'bestTime', 'bestTime_en', 
    'description', 'description_en', 'tips', 'tips_en', 
    'imageUrl', 'lat', 'lng', 'tags'
]

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

    # Write to CSV file
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        
        for place in filtered_places:
            row = {}
            for field in fields:
                if field == 'tags':
                    # Convert list of tags to comma-separated string
                    tags = place.get('tags', [])
                    row[field] = ', '.join(tags) if isinstance(tags, list) else str(tags)
                else:
                    row[field] = place.get(field, '')
            writer.writerow(row)

    print(f"Successfully extracted {len(filtered_places)} places to {output_path}")

except Exception as e:
    print(f"An error occurred: {e}")
