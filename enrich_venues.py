import json
import os
import shutil
from datetime import datetime

def enrich_venues(city_id, updates):
    """
    Applies venue description updates to a city's JSON file.
    
    city_id: basename of the file (e.g. 'bodrum')
    updates: dict of { venue_id (or name): { 'desc_tr': '...', 'desc_en': '...' } }
    """
    city_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    file_path = os.path.join(city_dir, f"{city_id}.json")
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    # Backup
    backup_path = file_path + f".bak.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    print(f"📦 Backup created: {backup_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    not_found = []

    for highlight in data.get('highlights', []):
        hid = highlight.get('id')
        name = highlight.get('name')
        
        # Try finding by ID first, then by name
        update_info = updates.get(hid) or updates.get(name)
        
        if update_info:
            highlight['description'] = update_info['desc_tr']
            highlight['description_en'] = update_info['desc_en']
            updated_count += 1
        else:
            # Check if it's already "premium" (not generic)
            desc = highlight.get('description', '')
            if "harika bir yer" in desc or not desc:
                not_found.append(name)

    if updated_count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Updated {updated_count} venues in {city_id}.json")
    else:
        print(f"⚠️ No venues updated in {city_id}.json")

    if not_found:
        print(f"🔍 {len(not_found)} venues still need enrichment in {city_id}.")

if __name__ == "__main__":
    # This script will be called with specific data in execution turns
    pass
