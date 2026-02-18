
import os
import json
import csv
import glob

# Set the path to the cities directory
CITIES_DIR = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
OUTPUT_FILE = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/City_Content_Export_v3.csv'

def main():
    print(f"Scanning directory: {CITIES_DIR}")
    
    json_files = glob.glob(os.path.join(CITIES_DIR, '*.json'))
    print(f"Found {len(json_files)} city files.")

    # CSV Headers
    headers = [
        'City',
        'Place Name (TR)',
        'Place Name (EN)', 
        'Area',
        'Category',
        'Description (TR)',
        'Description (EN)',
        'Tips (TR)',
        'Tips (EN)',
        'Best Time (TR)',
        'Best Time (EN)',
        'Review Count',
        'Rating',
        'Latitude',
        'Longitude',
        'Image URL'
    ]

    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        count = 0
        
        for file_path in sorted(json_files):
            # Skip temporary or system files
            if file_path.endswith('.tmp') or file_path.endswith('.DS_Store'):
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                city_name = data.get('city', 'Unknown')
                highlights = data.get('highlights', [])
                
                print(f"Processing {city_name} ({len(highlights)} places)...")
                
                for place in highlights:
                    count += 1
                    writer.writerow([
                        city_name,
                        place.get('name', ''),
                        place.get('name_en', ''),
                        place.get('area', ''),
                        place.get('category', ''),
                        place.get('description', ''),
                        place.get('description_en', ''),
                        place.get('tips', ''),
                        place.get('tips_en', ''),
                        place.get('bestTime', ''),
                        place.get('bestTime_en', ''),
                        place.get('reviewCount', ''),
                        place.get('rating', ''),
                        place.get('lat', ''),
                        place.get('lng', ''),
                        place.get('imageUrl', '')
                    ])
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    print(f"\n✅ Export completed successfully!")
    print(f"Total places exported: {count}")
    print(f"File saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
