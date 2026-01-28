
import json
import csv
import glob
import os

def export_google_links():
    # Define the directory containing JSON files
    cities_dir = os.path.join('assets', 'cities')
    output_file = os.path.join(os.path.expanduser('~'), 'Desktop', 'Google_API_Links_Report.csv')
    
    # Get all JSON files
    json_files = glob.glob(os.path.join(cities_dir, '*.json'))
    
    print(f"Scanning {len(json_files)} city files for Google API links...")
    
    # Define CSV headers
    headers = [
        'City',
        'Place Name',
        'Place ID',
        'Current Image URL'
    ]
    
    total_found = 0
    
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                city_name = data.get('city', 'Unknown')
                highlights = data.get('highlights', [])
                
                city_found_count = 0
                for place in highlights:
                    image_url = place.get('imageUrl', '')
                    
                    if 'maps.googleapis.com' in image_url:
                        writer.writerow([
                            city_name,
                            place.get('name', 'Unknown'),
                            place.get('id', ''),
                            image_url
                        ])
                        city_found_count += 1
                        total_found += 1
                
                if city_found_count > 0:
                    print(f"  - {city_name}: Found {city_found_count} expensive links")
                    
            except Exception as e:
                print(f"Error processing {json_file}: {e}")
                
    print(f"\nScan complete.")
    print(f"Found a total of {total_found} expensive Google API links.")
    print(f"Report saved to: {output_file}")

if __name__ == "__main__":
    export_google_links()
