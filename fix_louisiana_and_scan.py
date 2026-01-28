
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
DOWNLOAD_DIR = Path("temp_fix_photos")

# Specific fix for Louisiana
LOUISIANA_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Louisiana_Museum_of_Modern_Art_2016.jpg/1280px-Louisiana_Museum_of_Modern_Art_2016.jpg"
LOUISIANA_NAME = "Louisiana Modern Sanat Müzesi"
LOUISIANA_SLUG = "louisiana_modern_sanat_muzesi" # clean slug

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def upload_from_url(url, city_slug, blob_name, bucket):
    print(f"Downloading {url}...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 ...'}
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code != 200:
            print(f"Failed to download: {response.status_code}")
            return None
            
        blob_path = f"cities/{city_slug}/{blob_name}"
        blob = bucket.blob(blob_path)
        blob.upload_from_string(response.content, content_type='image/jpeg')
        blob.make_public()
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"Error uploading: {e}")
        return None

def main():
    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()

    # 1. FIX LOUISIANA
    print("\n--- Fixing Louisiana Museum ---")
    kopenhag_path = CITIES_DIR / "kopenhag.json"
    if kopenhag_path.exists():
        with open(kopenhag_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        found = False
        for place in data.get('highlights', []):
            if place.get('name') == LOUISIANA_NAME:
                print(f"Found {LOUISIANA_NAME}")
                new_url = upload_from_url(LOUISIANA_URL, 'kopenhag', f"{LOUISIANA_SLUG}.jpg", bucket)
                if new_url:
                    place['imageUrl'] = new_url
                    place['source'] = 'firebase'
                    found = True
                    print(f"Updated to: {new_url}")
        
        if found:
            with open(kopenhag_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("Saved kopenhag.json")
    else:
        print("kopenhag.json not found")

    # 2. SCAN FOR NON-ASCII URLS
    print("\n--- Scanning for Non-ASCII URLs ---")
    issues = 0
    for json_file in CITIES_DIR.glob("*.json"):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for place in data.get('highlights', []):
            url = place.get('imageUrl', '')
            if not url: continue
            
            if not is_ascii(url):
                print(f"NON-ASCII URL in {json_file.name}: {place.get('name')}")
                print(f"  Url: {url}")
                issues += 1
                
    if issues == 0:
        print("No other non-ASCII URLs found.")
    else:
        print(f"Found {issues} other issues.")

if __name__ == "__main__":
    main()
