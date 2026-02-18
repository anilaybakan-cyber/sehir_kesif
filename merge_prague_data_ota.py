
import csv
import json
import os
import shutil
from datetime import date

# --- CONFIGURATION ---
CSV_INPUT = '/Users/anilebru/Desktop/prag_yeni_mekan_onerileri_final.csv'
JSON_ASSET_PATH = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/prag.json'
OTA_REPO_PATH = '/Users/anilebru/Desktop/Uygulamalar/myway-data' # Assuming this is where the repo is
OTA_PACK_LOCAL = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack' # Local staging if repo not found

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    print("🚀 Starting OTA preparation for Prague...")

    # 1. Read New Venues from CSV
    new_venues = []
    try:
        with open(CSV_INPUT, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            new_venues = list(reader)
        print(f"✅ Loaded {len(new_venues)} new venues from CSV.")
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return

    # 2. Read Existing JSON
    try:
        city_data = load_json(JSON_ASSET_PATH)
        print(f"✅ Loaded existing prag.json with {len(city_data.get('highlights', []))} highlights.")
    except Exception as e:
        print(f"❌ Error reading JSON: {e}")
        return

    # 3. Merge Data
    existing_ids = {h['id'] for h in city_data['highlights'] if 'id' in h}
    added_count = 0

    for venue in new_venues:
        if venue['id'] in existing_ids:
            # print(f"  ⚠️ Skipping duplicate: {venue['name']} ({venue['id']})")
            continue
        
        # Convert CSV strings to correct JSON types
        new_highlight = {
            "name": venue['name'],
            "name_en": venue['name_en'],
            "area": venue['area'],
            "category": venue['category'],
            "tags": [t.strip() for t in venue['tags'].split(',')] if venue['tags'] else [],
            "distanceFromCenter": 0.0, # Placeholder, app calculates or existing logic
            "lat": float(venue['lat']),
            "lng": float(venue['lng']),
            "price": venue['price'],
            "rating": float(venue['rating']),
            "description": venue['description'],
            "description_en": venue['description_en'],
            "bestTime": venue['bestTime'],
            "bestTime_en": venue['bestTime_en'],
            "imageUrl": venue['imageUrl'],
            "id": venue['id'],
            "tips": venue['tips'],
            "tips_en": venue['tips_en'],
            "source": "firebase_ota" # Mark as OTA added
        }
        
        city_data['highlights'].append(new_highlight)
        added_count += 1

    print(f"✨ Merged {added_count} new venues. Total: {len(city_data['highlights'])}")

    # 4. Save to Asset (Development Source)
    save_json(JSON_ASSET_PATH, city_data)
    print(f"✅ Updated {JSON_ASSET_PATH}")

    # 5. Handle OTA Deployment
    # Check if 'myway-data' repo exists nearby, otherwise check 'ota_data_pack' logic
    
    # Try typical paths for the repo
    possible_repo_paths = [
        '/Users/anilebru/Desktop/Uygulamalar/myway-data',
        '/Users/anilebru/Desktop/myway-data',
        '/Users/anilebru/Documents/myway-data',
        '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack' # Maybe this IS the repo?
    ]
    
    repo_path = None
    for p in possible_repo_paths:
        if os.path.exists(os.path.join(p, '.git')) or os.path.exists(os.path.join(p, 'version_manifest.json')):
            repo_path = p
            break
            
    if not repo_path:
        print("⚠️ Could not find 'myway-data' repository automatically.")
        print("   Please verify where you clone the 'myway-data' repo.")
        # Fallback: Just update local ota_data_pack so user can manually push
        repo_path = OTA_PACK_LOCAL
        if not os.path.exists(repo_path):
            os.makedirs(repo_path)
            
    print(f"📂 Using Update Path: {repo_path}")

    # Paths within repo
    target_city_json = os.path.join(repo_path, 'cities', 'prag.json')
    target_manifest = os.path.join(repo_path, 'version_manifest.json')
    
    # Ensure dirs exist
    os.makedirs(os.path.dirname(target_city_json), exist_ok=True)

    # 5.1 Copy updated prag.json to repo
    shutil.copy2(JSON_ASSET_PATH, target_city_json)
    print(f"✅ Copied prag.json to {target_city_json}")

    # 5.2 Update Manifest
    if os.path.exists(target_manifest):
        manifest = load_json(target_manifest)
        current_ver = manifest.get('prag', 10)
        new_ver = current_ver + 1
        manifest['prag'] = new_ver
        manifest['lastUpdated'] = str(date.today())
        manifest['updateNotes'] = f"Updated Prague with {added_count} new venues via OTA."
        
        save_json(target_manifest, manifest)
        print(f"🆙 Bumped Prague version to {new_ver} in {target_manifest}")
    else:
        print(f"❌ Manifest not found at {target_manifest}. Creating new...")
        manifest = {
            "prag": 11,
            "version": "1.0.4",
            "lastUpdated": str(date.today())
        }
        save_json(target_manifest, manifest)

    print("\n🎉 OTA Preparation Complete!")
    print(f"   You can now cd to '{repo_path}' and push to GitHub.")

if __name__ == "__main__":
    main()
