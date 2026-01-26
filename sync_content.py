import os
import json
import shutil
import sys
from datetime import datetime

# CONFIGURATION
SOURCE_DIR = "assets/cities"
# Default assumption: myway-data is a sibling directory
TARGET_REPO_NAME = "myway-data"
TARGET_REPO_PATH = os.path.abspath(os.path.join(os.getcwd(), "..", TARGET_REPO_NAME))

def main():
    print(f"🚀 Content Sync Script Started")
    print(f"📍 Source: {os.path.abspath(SOURCE_DIR)}")
    print(f"📍 Target: {TARGET_REPO_PATH}")

    if not os.path.exists(TARGET_REPO_PATH):
        print(f"❌ Target repo not found at {TARGET_REPO_PATH}")
        print(f"Please clone 'myway-data' repo to the parent directory or update TARGET_REPO_PATH in the script.")
        return

    target_cities_dir = os.path.join(TARGET_REPO_PATH, "cities")
    manifest_path = os.path.join(TARGET_REPO_PATH, "version_manifest.json")

    if not os.path.exists(target_cities_dir):
        os.makedirs(target_cities_dir)

    # Load Manifest
    manifest = {}
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
        except Exception as e:
            print(f"⚠️ Error reading manifest: {e}")

    updated_cities = []
    
    # Process Cities
    for filename in os.listdir(SOURCE_DIR):
        if not filename.endswith(".json"):
            continue
            
        city_id = filename.replace(".json", "")
        source_file = os.path.join(SOURCE_DIR, filename)
        target_file = os.path.join(target_cities_dir, filename)
        
        # Read contents
        with open(source_file, 'r', encoding='utf-8') as f:
            source_content = f.read()
            
        target_content = ""
        if os.path.exists(target_file):
            with open(target_file, 'r', encoding='utf-8') as f:
                target_content = f.read()

        # Compare (ignoring whitespace might be safer, but direct string compare is okay for now)
        if source_content != target_content:
            print(f"🔄 Updating {filename}...")
            
            # Copy file
            shutil.copy2(source_file, target_file)
            
            # Increment Version
            current_ver = manifest.get(city_id, 0)
            new_ver = current_ver + 1
            manifest[city_id] = new_ver
            updated_cities.append(f"{city_id} (v{new_ver})")
        else:
            # print(f"✅ {filename} is up to date.")
            pass

    # Update Manifest Metadata
    if updated_cities:
        manifest["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")
        manifest["updateNotes"] = f"Auto-sync update: {', '.join(updated_cities)}"
        
        # Save Manifest
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            
        print(f"\n✅ Synced {len(updated_cities)} cities.")
        print(f"📝 Manifest updated.")
        print(f"\n👉 Now run these commands in '{TARGET_REPO_PATH}':")
        print(f"   cd {TARGET_REPO_PATH}")
        print(f"   git add .")
        print(f"   git commit -m 'Update content: {', '.join(updated_cities)}'")
        print(f"   git push origin main")
    else:
        print("\n✨ No changes detected. Everything is in sync.")

if __name__ == "__main__":
    main()
