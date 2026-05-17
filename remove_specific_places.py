import json
import glob
import os

target_names = [
    "5m migros mall", "5m migros avm",
    "derviş cafe 2", "dervis cafe 2",
    "galataport i̇stanbul", "galataport istanbul"
]

def sanitize(s):
    return s.lower().strip() if s else ""

directories = ["assets/cities", "ota_data_pack/cities"]
total_removed = 0

for base_dir in directories:
    if not os.path.exists(base_dir):
        continue
    
    for file_path in glob.glob(os.path.join(base_dir, "*.json")):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
            
        highlights = data.get('highlights', [])
        new_highlights = []
        
        removed_in_file = 0
        for h in highlights:
            name_tr = sanitize(h.get('name', ''))
            name_en = sanitize(h.get('name_en', ''))
            
            is_target = False
            for t in target_names:
                if t == name_tr or t == name_en or t in name_tr or t in name_en:
                    is_target = True
                    break
            
            if is_target:
                removed_in_file += 1
                total_removed += 1
            else:
                new_highlights.append(h)
                
        if removed_in_file > 0:
            data['highlights'] = new_highlights
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Removed {removed_in_file} specific places in {file_path}")

print(f"Total specific places removed: {total_removed}")
