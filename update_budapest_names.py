import json
import glob
import os

files_to_check = [
    "assets/cities/budapeste.json",
]

translations = {
    "kahramanlar meydanı": "Heroes' Square",
    "kahramanlar square": "Heroes' Square",
    "parlamento": "Hungarian Parliament",
    "parlamento binası": "Hungarian Parliament Building"
}

total_updated = 0

for file_path in files_to_check:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    highlights = data.get('highlights', [])
    updated_in_file = 0
    
    for h in highlights:
        # Check name_en
        name_en = (h.get('name_en') or "").lower().strip()
        name = (h.get('name') or "").lower().strip()
        
        if name_en in translations:
            h['name_en'] = translations[name_en]
            updated_in_file += 1
            total_updated += 1
        elif name in translations and h.get('name_en') != translations[name]:
            h['name_en'] = translations[name]
            updated_in_file += 1
            total_updated += 1
            
    if updated_in_file > 0:
        data['highlights'] = highlights
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated {updated_in_file} names in {file_path}")

print(f"Total updated: {total_updated}")
