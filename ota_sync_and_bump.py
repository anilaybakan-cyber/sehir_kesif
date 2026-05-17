
import json
import os
import shutil

SOURCE_DIR = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
CONFIG_FILE = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities_list.json'
DEST_REPO = '/Users/anilebru/Desktop/Uygulamalar/myway-data'
DEST_CITIES = os.path.join(DEST_REPO, 'cities')
DEST_MANIFEST = os.path.join(DEST_REPO, 'version_manifest.json')
DEST_CONFIG = os.path.join(DEST_REPO, 'cities_list.json')

def sync_data():
    print("🔄 Syncing sanitized city data...")
    # Ensure dest cities dir exists
    os.makedirs(DEST_CITIES, exist_ok=True)
    
    # Copy all city files
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith('.json'):
            shutil.copy2(os.path.join(SOURCE_DIR, filename), os.path.join(DEST_CITIES, filename))
    
    # Copy cities_list.json
    shutil.copy2(CONFIG_FILE, DEST_CONFIG)
    print("✅ Files synchronized.")

def bump_manifest():
    print("📈 Bumping version manifest...")
    with open(DEST_MANIFEST, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    # 1. Bump top-level city versions
    city_count = 0
    for key, value in list(manifest.items()):
        if isinstance(value, int) and key not in ['paywall_config', 'cities_list']:
            manifest[key] += 1
            city_count += 1
    
    # 2. Add missing cities from SOURCE_DIR if any
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith('.json'):
            city_id = filename.replace('.json', '')
            if city_id not in manifest:
                manifest[city_id] = 1
                print(f"🆕 Added new city to manifest: {city_id}")
    
    # 3. Bump routes and guides if they exist for these cities
    if 'routes' in manifest:
        for city in manifest['routes']:
            manifest['routes'][city] += 1
            
    if 'guides' in manifest:
        for city in manifest['guides']:
            manifest['guides'][city] += 1

    # Bump cities_list version
    manifest['cities_list'] = manifest.get('cities_list', 0) + 1
    
    manifest['lastUpdated'] = "2026-04-19"
    manifest['updateNotes'] = "Global Data Sanitization & Healing. Stripped AI trash fragments, restored Bari data, and synchronized high-quality hero images across all 82 cities."

    with open(DEST_MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Bumped {city_count} city versions in manifest.")

if __name__ == "__main__":
    sync_data()
    bump_manifest()
