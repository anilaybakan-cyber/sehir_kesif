import csv
import json
import os
from pathlib import Path

# Paths
CSV_PATH = "city_contents_master_export.csv"
ASSETS_DIR = Path("assets/cities")
OTA_DIR = Path("ota_data_pack/cities")

def load_master_data(csv_path):
    """Loads place highlights from CSV into a nested dictionary."""
    master_data = {}
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Type'] == 'Place/Highlight':
                city_id = row['City ID'].lower().strip()
                place_name_en = row['Title (EN)'].strip()
                
                if city_id not in master_data:
                    master_data[city_id] = {}
                
                master_data[city_id][place_name_en] = {
                    'category': row['Category'],
                    'description': row['Content (TR)'],
                    'description_en': row['Content (EN)']
                }
    return master_data

def update_json_files(target_dir, master_data):
    """Updates JSON files in target_dir with content from master_data."""
    print(f"Updating JSON files in {target_dir}...")
    updated_cities = 0
    total_places_updated = 0
    
    for json_file in target_dir.glob("*.json"):
        city_id = json_file.stem.lower()
        if city_id not in master_data:
            continue
            
        print(f"    Processing {json_file.name}...")
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"    Error reading {json_file}: {e}")
            continue
        
        city_master = master_data[city_id]
        city_updated = False
        
        for highlight in data.get('highlights', []):
            name_en = highlight.get('name', '') # Mostly name is in English or used as key
            
            # Try to match by name
            if name_en in city_master:
                entry = city_master[name_en]
                highlight['description'] = entry['description']
                highlight['description_en'] = entry['description_en']
                city_updated = True
                total_places_updated += 1
        
        if city_updated:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            updated_cities += 1
            print(f"  [v] Updated {city_id}.json")
            
    print(f"Done! Updated {updated_cities} cities and {total_places_updated} total places in {target_dir}.")

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Error: {CSV_PATH} not found.")
        return

    print(f"Loading master data from {CSV_PATH}...")
    master_data = load_master_data(CSV_PATH)
    print(f"Loaded {len(master_data)} cities from master CSV.")
    
    # Update assets
    update_json_files(ASSETS_DIR, master_data)
    
    # Update OTA pack
    update_json_files(OTA_DIR, master_data)

if __name__ == "__main__":
    main()
