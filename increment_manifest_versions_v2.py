
import json
import os

MANIFEST_FILE = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/version_manifest_updated.json"

def main():
    if not os.path.exists(MANIFEST_FILE):
        print(f"Manifest not found: {MANIFEST_FILE}")
        return

    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # Increment all city versions
    for city in manifest.keys():
        if city in ['version', 'lastUpdated', 'updateNotes', 'routes', 'guides']:
            continue
        if isinstance(manifest[city], int):
            manifest[city] += 1
            print(f"Incrementing {city} to {manifest[city]}")

    # Update metadata
    from datetime import datetime
    manifest['lastUpdated'] = datetime.now().strftime("%Y-%m-%d")
    manifest['updateNotes'] = "Enriched English descriptions and content refresh."

    with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print("Manifest updated successfully.")

if __name__ == "__main__":
    main()
