import json
import os
import shutil
import subprocess

SRC_DIR = "assets/cities"
DEST_DIR = "/Users/anilebru/Desktop/Uygulamalar/myway-data/cities"
MANIFEST_PATH = "/Users/anilebru/Desktop/Uygulamalar/myway-data/version_manifest.json"
REPO_PATH = "/Users/anilebru/Desktop/Uygulamalar/myway-data"

def run_git_cmd(args):
    result = subprocess.run(
        ['git'] + args,
        cwd=REPO_PATH,
        capture_output=True,
        text=True,
        check=False
    )
    return result

def main():
    if not os.path.exists(DEST_DIR):
        print(f"Dest dir not found: {DEST_DIR}")
        return

    # 1. Sync files
    files = [f for f in os.listdir(SRC_DIR) if f.endswith(".json")]
    print(f"Syncing {len(files)} files to {DEST_DIR}...")
    for f in files:
        shutil.copy2(os.path.join(SRC_DIR, f), os.path.join(DEST_DIR, f))

    # 2. Update Manifest
    with open(MANIFEST_PATH, "r", encoding="utf-8") as j:
        manifest = json.load(j)

    # Add/Update city versions
    for f in files:
        city_id = f.replace(".json", "")
        # Bump the version. If new, start at 10 (matching bari/catania style) or 1.
        current_ver = manifest.get(city_id, 0)
        manifest[city_id] = current_ver + 1
        
        # Also update routes/guides versions
        if "routes" not in manifest: manifest["routes"] = {}
        if "guides" not in manifest: manifest["guides"] = {}
        
        manifest["routes"][city_id] = manifest["routes"].get(city_id, 0) + 1
        manifest["guides"][city_id] = manifest["guides"].get(city_id, 0) + 1

    manifest["lastUpdated"] = "2026-05-17 20:50:00"
    manifest["updateNotes"] = "Global OTA Update: 38 premium venues translated, 169 duplicate cards deduplicated."

    with open(MANIFEST_PATH, "w", encoding="utf-8") as j:
        json.dump(manifest, j, indent=4, ensure_ascii=False)
    
    print("Manifest updated.")

    # 3. Git Push
    print("Deploying to GitHub...")
    run_git_cmd(['add', '.'])
    run_git_cmd(['commit', '-m', "feat: Global Content Cleanup & OTA Deployment (3600+ venues)"])
    res = run_git_cmd(['push'])
    
    if res.returncode == 0:
        print("✅ OTA Deployment successful!")
    else:
        print(f"❌ Deploy failed: {res.stderr}")

if __name__ == "__main__":
    main()
