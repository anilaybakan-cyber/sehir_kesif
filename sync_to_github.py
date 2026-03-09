import os
import json
import shutil

source_dir = "assets/cities"
target_dir = "../myway-data/cities"
manifest_path = "../myway-data/version_manifest.json"

# Read existing manifest
if os.path.exists(manifest_path):
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
else:
    manifest = {}

os.makedirs(target_dir, exist_ok=True)

# Process all json files in source_dir
updated_count = 0
for filename in os.listdir(source_dir):
    if filename.endswith(".json"):
        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(target_dir, filename)
        
        # Check if contents are different to verify if update needed
        needs_update = True
        if os.path.exists(target_path):
            with open(source_path, 'rb') as sf, open(target_path, 'rb') as tf:
                if sf.read() == tf.read():
                    needs_update = False
        
        if needs_update:
            shutil.copy2(source_path, target_path)
            city_key = filename[:-5] # remove .json
            
            # Increment version
            if city_key in manifest and isinstance(manifest[city_key], int):
                manifest[city_key] += 1
            else:
                manifest[city_key] = 1
                
            updated_count += 1
            print(f"Updated {filename} -> Version {manifest[city_key]}")

# Save manifest
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=4, ensure_ascii=False)

print(f"Total files updated: {updated_count}")
