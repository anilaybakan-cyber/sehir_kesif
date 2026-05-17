import json
import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# Paths
LOCAL_REPO = Path("/Users/anilebru/Desktop/Uygulamalar/sehir_kesif")
OTA_REPO = Path("/Users/anilebru/Desktop/Uygulamalar/myway-data")
LOCAL_CITIES = LOCAL_REPO / "assets/cities"
OTA_CITIES = OTA_REPO / "cities"
OTA_MANIFEST = OTA_REPO / "version_manifest.json"

NEW_CITIES = ['catania', 'bari', 'sardinya', 'cannes', 'saint_tropez']

def run_cmd(args, cwd):
    result = subprocess.run(args, cwd=str(cwd), capture_output=True, text=True)
    return result

def main():
    print("🚀 Starting Global OTA Sync...")

    # 1. Pull latest from OTA repo
    print("  📥 Pulling latest from OTA repo...")
    run_cmd(['git', 'pull'], OTA_REPO)

    # 2. Identify cities to update
    updated_count = 0
    synced_cities = []
    
    # Read manifest
    with open(OTA_MANIFEST, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # All JSON files in our local assets
    for local_file in LOCAL_CITIES.glob("*.json"):
        city_id = local_file.stem
        # Skip temp/batch files
        if "_" in city_id and city_id not in ['saint_tropez', 'san_sebastian']:
            continue
            
        ota_file = OTA_CITIES / f"{city_id}.json"
        
        # Determine if we should sync
        is_new = city_id in NEW_CITIES
        is_existing = ota_file.exists()
        
        if is_new or is_existing:
            print(f"  📂 Syncing {city_id}...")
            shutil.copy(local_file, ota_file)
            synced_cities.append(city_id)
            updated_count += 1
            
            # Update manifest version
            # Primary version
            if city_id not in manifest:
                manifest[city_id] = 10 # Start at 10 for new cities
            else:
                manifest[city_id] += 1
            
            # Routes/Guides versions (Optional but good for consistency)
            if 'routes' in manifest and city_id in manifest['routes']:
                manifest['routes'][city_id] += 1
            elif 'routes' in manifest:
                manifest['routes'][city_id] = 1
                
            if 'guides' in manifest and city_id in manifest['guides']:
                manifest['guides'][city_id] += 1
            elif 'guides' in manifest:
                manifest['guides'][city_id] = 1

    # 3. Update Manifest Metadata
    manifest['lastUpdated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    manifest['updateNotes'] = "Global Overhaul: 5 New Cities (Premium) & 50+ Localization Fixes with Real Photos."
    
    with open(OTA_MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=4, ensure_ascii=False)

    print(f"  📝 Manifest updated. {updated_count} cities synced.")

    # 4. Git Operations
    print("  ⬆️ Committing and pushing to OTA repo...")
    run_cmd(['git', 'add', '.'], OTA_REPO)
    run_cmd(['git', 'commit', '-m', "feat: Global Premium Content & Localization Update (1000+ Real Photos)"], OTA_REPO)
    push_res = run_cmd(['git', 'push'], OTA_REPO)
    
    if push_res.returncode == 0:
        print("\n✅ OTA Deployment SUCCESSFUL!")
    else:
        print(f"\n❌ OTA Deployment FAILED: {push_res.stderr}")

if __name__ == "__main__":
    main()
