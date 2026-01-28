
import json
import os
import requests
import re
import firebase_admin
from firebase_admin import credentials, storage
from pathlib import Path

# --- CONFIGURATION ---
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")
DOWNLOAD_DIR = Path("temp_migration_photos")
FIREBASE_PREFIX = "https://storage.googleapis.com/myway-3fe75.firebasestorage.app"

def slugify(text):
    if not text: return ""
    text = text.lower()
    text = text.replace('ö','o').replace('ü','u').replace('ğ','g').replace('ş','s').replace('ç','c').replace('ı','i')
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '_', text)
    return text.strip('_')[:50]

def download_image(url, filename, city_slug):
    city_dir = DOWNLOAD_DIR / city_slug
    city_dir.mkdir(parents=True, exist_ok=True)
    filepath = city_dir / filename
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return filepath
        else:
            print(f"  ❌ Failed to download {url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"  ❌ Error downloading {url}: {e}")
        return None

def upload_to_firebase(local_path, city_slug, filename, bucket):
    blob_path = f"cities/{city_slug}/{filename}"
    blob = bucket.blob(blob_path)
    try:
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"  ❌ Firebase upload error: {e}")
        return None

def main():
    print("Starting migration of non-Firebase images...")
    
    # Initialize Firebase
    if not firebase_admin._apps:
        try:
            cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
            firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
        except Exception as e:
            print(f"FATAL: Could not initialize Firebase: {e}")
            return
            
    bucket = storage.bucket()
    
    total_found = 0
    migrated = 0
    failed = 0
    skipped = 0
    
    # Iterate over all JSON files
    for json_file in CITIES_DIR.glob("*.json"):
        city_slug = json_file.stem
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            modified = False
            highlights = data.get('highlights', [])
            
            for place in highlights:
                image_url = place.get('imageUrl')
                place_name = place.get('name')
                
                if not image_url:
                    continue
                    
                # Check if it's already on Firebase
                if image_url.startswith(FIREBASE_PREFIX):
                    continue
                    
                print(f"Processing: {city_slug} -> {place_name}")
                print(f"  Url: {image_url}")
                total_found += 1
                
                # Download
                filename = f"{slugify(place_name)}.jpg"
                import time
                time.sleep(2) # Avoid 429
                local_path = download_image(image_url, filename, city_slug)
                
                if not local_path:
                    failed += 1
                    continue
                    
                # Upload
                new_url = upload_to_firebase(local_path, city_slug, filename, bucket)
                
                if new_url:
                    place['imageUrl'] = new_url
                    place['source'] = 'firebase'
                    modified = True
                    migrated += 1
                    print(f"  ✓ Migrated -> {new_url}")
                else:
                    failed += 1
            
            if modified:
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"Saved updates to {json_file.name}")
                
        except Exception as e:
            print(f"Error processing {json_file}: {e}")

    print("\n" + "="*30)
    print("Migration Summary")
    print(f"Total External Images Found: {total_found}")
    print(f"Successfully Migrated: {migrated}")
    print(f"Failed: {failed}")
    print("="*30)

if __name__ == "__main__":
    main()
