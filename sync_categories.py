import json
from pathlib import Path

ASSETS_DIR = Path('assets/cities')
OTA_DIR = Path('ota_data_pack/cities')
updated_files = 0
total_places_updated = 0

for asset_file in ASSETS_DIR.glob('*.json'):
    ota_file = OTA_DIR / asset_file.name
    if not ota_file.exists():
        continue
        
    try:
        with open(asset_file, 'r', encoding='utf-8') as f:
            asset_data = json.load(f)
        with open(ota_file, 'r', encoding='utf-8') as f:
            ota_data = json.load(f)
    except Exception as e:
        print(f"Error loading {asset_file.name}: {e}")
        continue
        
    asset_cats = {}
    for h in asset_data.get('highlights', []):
        # Match by ID first, then fallback to name_en or name
        match_key = h.get('id', h.get('name_en', h.get('name', '')))
        asset_cats[match_key] = {
            'category': h.get('category'),
            'tags': h.get('tags'),
            'subcategory': h.get('subcategory')
        }
        
    updated = False
    for h in ota_data.get('highlights', []):
        match_key = h.get('id', h.get('name_en', h.get('name', '')))
        if match_key in asset_cats:
            cat_info = asset_cats[match_key]
            
            if cat_info['category'] is not None and h.get('category') != cat_info['category']:
                h['category'] = cat_info['category']
                updated = True
                
            if cat_info['tags'] is not None and h.get('tags') != cat_info['tags']:
                h['tags'] = cat_info['tags']
                updated = True
                
            if 'subcategory' in cat_info and cat_info['subcategory'] != h.get('subcategory'):
                if cat_info['subcategory'] is not None:
                    h['subcategory'] = cat_info['subcategory']
                else:
                    h.pop('subcategory', None)
                updated = True
                
    if updated:
        with open(ota_file, 'w', encoding='utf-8') as f:
            json.dump(ota_data, f, ensure_ascii=False, indent=2)
        updated_files += 1

print(f"Synced categories for {updated_files} OTA files.")
