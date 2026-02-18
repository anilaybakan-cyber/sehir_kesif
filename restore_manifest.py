import json
import os

# Base URL for Firebase Storage
BASE_URL = "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/ota_data_pack/cities/"

# Path to local files
CITIES_DIR = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack/cities"
MANIFEST_PATH = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack/version_manifest.json"

def restore_manifest():
    manifest = {}
    
    # List all json files
    for filename in os.listdir(CITIES_DIR):
        if not filename.endswith(".json"):
            continue
            
        city_id = filename.replace(".json", "")
        file_path = os.path.join(CITIES_DIR, filename)
        file_size = os.path.getsize(file_path)
        
        # Construct the detailed entry
        manifest[city_id] = {
            "version": 1,
            "url": f"{BASE_URL}{filename}",
            "size": file_size
        }
        
    # Sort by city key
    sorted_manifest = dict(sorted(manifest.items()))
    
    # Write to file
    with open(MANIFEST_PATH, "w") as f:
        json.dump(sorted_manifest, f, indent=2)
        
    print(f"✅ Restored manifest with {len(sorted_manifest)} cities.")

if __name__ == "__main__":
    restore_manifest()
