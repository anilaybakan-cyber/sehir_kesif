
#!/usr/bin/env python3
"""
Report Failed Photos Script
Checks which places from 'eksikler.csv' still don't have a Firebase URL.
"""

import csv
import json
import os

# --- CONFIGURATION ---
CSV_PATH = os.path.expanduser('~/Desktop/eksikler.csv')
REPORT_PATH = os.path.expanduser('~/Desktop/failed_photos.csv')

def get_image_url(city, place_name):
    """Gets the current image URL for a place from the city JSON"""
    city_slug = city.lower().replace('ö','o').replace('ü','u').replace('ğ','g').replace('ş','s').replace('ç','c').replace('ı','i')
    # Special case mappings or fuzzy find
    json_path = f"assets/cities/{city_slug}.json"
    
    if not os.path.exists(json_path):
        import glob
        files = glob.glob(f"assets/cities/*.json")
        for f in files:
            if city_slug in f:
                json_path = f
                break
        
    if not os.path.exists(json_path):
        return None
        
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for place in data.get('highlights', []):
            if place.get('name') == place_name:
                return place.get('imageUrl', '')
            
    except Exception as e:
        pass
        
    return None

def main():
    print(f"Reading {CSV_PATH}...")
    
    failed_places = []
    
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        
        try:
            header = next(reader)
        except StopIteration:
            print("Empty CSV file")
            return

        city_idx = 0
        name_idx = 2
        
        if 'City' in header:
            city_idx = header.index('City')
        if 'Place Name (TR)' in header:
            name_idx = header.index('Place Name (TR)')
            
        for row in reader:
            if len(row) > name_idx:
                city = row[city_idx].strip()
                place_name = row[name_idx].strip()
                
                if place_name and city:
                    current_url = get_image_url(city, place_name)
                    
                    # If URL is missing, or not from firebase/storage, it's a fail
                    if not current_url or 'firebasestorage' not in current_url:
                        failed_places.append([city, place_name, current_url if current_url else "MISSING"])

    print(f"Found {len(failed_places)} failed places.")
    
    # Write report
    with open(REPORT_PATH, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['City', 'Place Name', 'Current URL Status'])
        writer.writerows(failed_places)
        
    print(f"Report saved to: {REPORT_PATH}")
    
    # Print list to console for immediate visibility
    print("\n--- Failed Places ---")
    for place in failed_places:
        print(f"- {place[0]}: {place[1]}")

if __name__ == "__main__":
    main()
