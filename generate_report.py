
import json
import csv
import glob
import os

def generate_report():
    # Define the directory containing JSON files
    cities_dir = os.path.join('assets', 'cities')
    output_file = os.path.join(os.path.expanduser('~'), 'Desktop', 'City_Data_Report.csv')
    
    # Get all JSON files
    json_files = glob.glob(os.path.join(cities_dir, '*.json'))
    
    print(f"Found {len(json_files)} city files.")
    
    # Define CSV headers
    headers = [
        'City',
        'Place Name (TR)',
        'Place Name (EN)',
        'Category',
        'Area',
        'Rating',
        'Description (TR)',
        'Description (EN)',
        'Tips (TR)',
        'Tips (EN)',
        'Image URL',
        'Latitude',
        'Longitude',
        'Tags'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        count = 0
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                city_name = data.get('city', 'Unknown')
                highlights = data.get('highlights', [])
                
                for place in highlights:
                    # Extract fields with safe defaults
                    name_tr = place.get('name', '')
                    name_en = place.get('name_en', '')
                    category = place.get('category', '')
                    area = place.get('area', '')
                    rating = place.get('rating', '')
                    
                    desc_tr = place.get('description', '')
                    desc_en = place.get('description_en', '')
                    
                    tips_tr = place.get('tips', '')
                    tips_en = place.get('tips_en', '')
                    
                    image_url = place.get('imageUrl', '')
                    lat = place.get('lat', '')
                    lng = place.get('lng', '')
                    
                    tags = ", ".join(place.get('tags', []))
                    
                    writer.writerow([
                        city_name,
                        name_tr,
                        name_en,
                        category,
                        area,
                        rating,
                        desc_tr,
                        desc_en,
                        tips_tr,
                        tips_en,
                        image_url,
                        lat,
                        lng,
                        tags
                    ])
                    count += 1
                    
            except Exception as e:
                print(f"Error processing {json_file}: {e}")
                
    print(f"Successfully wrote {count} places to {output_file}")

if __name__ == "__main__":
    generate_report()
