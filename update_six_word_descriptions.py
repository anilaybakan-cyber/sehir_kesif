
import json
import os
import glob
import re

def load_updates():
    updates = {}
    files = [
        "updates_part_1.json",
        "updates_part_2.json",
        "updates_part_3.json",
        "updates_part_4.json",
        "updates_part_5.json"
    ]
    
    base_path = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/"
    
    for file_name in files:
        file_path = os.path.join(base_path, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    # Key by name for easy lookup
                    # We strip whitespace just in case
                    name = item['name'].strip()
                    updates[name] = item
        else:
            print(f"Warning: {file_name} not found.")
            
    return updates

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    
    updates_map = load_updates()
    print(f"Loaded {len(updates_map)} updates to apply.")
    
    total_updated = 0
    updated_places = []
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            file_changed = False
            
            for place in highlights:
                name = place.get('name', '').strip()
                
                if name in updates_map:
                    update_data = updates_map[name]
                    
                    # Apply updates
                    # Only update if the current description is short (<= 6 words) OR if we want to force update
                    # The user goal is to update these SPECIFIC places, so we force update if matched.
                    
                    old_desc = place.get('description', '')
                    new_desc = update_data['tr']
                    new_desc_en = update_data['en']
                    
                    if old_desc != new_desc:
                        place['description'] = new_desc
                        place['description_en'] = new_desc_en
                        file_changed = True
                        total_updated += 1
                        updated_places.append(name)
                        # Remove from map to track what was used
                        # del updates_map[name] # Don't delete while iterating or if we want to debug unused
            
            if file_changed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Updated {city_name}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nTotal places updated: {total_updated}")
    
    # Check for unused updates
    # applied_names = set(updated_places)
    # all_update_names = set(updates_map.keys())
    # missed = all_update_names - applied_names
    # if missed:
    #     print(f"\nWarning: {len(missed)} updates were NOT applied (names didn't match):")
    #     for m in missed:
    #         print(f" - {m} (City: {updates_map[m]['city']})")

if __name__ == "__main__":
    main()
