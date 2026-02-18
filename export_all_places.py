
import json
import os
import csv
from pathlib import Path

# Configuration
ASSETS_DIR = Path("assets/cities")
OUTPUT_CSV = os.path.expanduser("~/Desktop/tum_mekanlar_fotograflar.csv")

def main():
    print(f"Reading JSON files from {ASSETS_DIR}...")
    
    all_data = []
    
    # Iterate over all JSON files
    for json_file in ASSETS_DIR.glob("*.json"):
        city_slug = json_file.stem
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            city_name = data.get('city', city_slug.title())
            highlights = data.get('highlights', [])
            
            for place in highlights:
                name = place.get('name', '')
                image_url = place.get('imageUrl', '')
                
                all_data.append({
                    'City': city_name,
                    'Place Name': name,
                    'Image URL': image_url
                })
                
        except Exception as e:
            print(f"Error reading {json_file}: {e}")

    print(f"Found {len(all_data)} places.")
    
    # Sort by City then Place Name
    all_data.sort(key=lambda x: (x['City'], x['Place Name']))
    
    # Write to CSV
    print(f"Writing to {OUTPUT_CSV}...")
    with open(OUTPUT_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['City', 'Place Name', 'Image URL'], delimiter=';')
        writer.writeheader()
        writer.writerows(all_data)
        
    print("Done!")

if __name__ == "__main__":
    main()
