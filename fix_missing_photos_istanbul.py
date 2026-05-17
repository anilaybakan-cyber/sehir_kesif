from dotenv import load_dotenv
load_dotenv()
import json
import requests
import os
import re
from pathlib import Path
import firebase_admin
from firebase_admin import credentials, storage

# --- Configuration ---
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")
DOWNLOAD_DIR = Path("fixed_istanbul_photos")

LANDMARKS_TO_FIX = [
    "Akmar Pasajı",
    "Mahmutpaşa",
    "Süleymaniye Camii",
    "Süleymaniye",
    "Istanbul Skyline"  # For hero image
]

CITY_ID = "istanbul"

# --- Utility Functions ---

def slugify(text):
    if not text: return ""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '_', text)
    return text.strip('_')[:50]

def find_place_id_and_photo(name):
    """Use Text Search to find the place and get its photo reference"""
    print(f"🔍 Searching API for: {name}")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"{name} Istanbul",
        "key": API_KEY,
        "language": "tr"
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        
        if data.get("status") == "OK" and data.get("results"):
            result = data["results"][0]
            photos = result.get("photos", [])
            if photos:
                return photos[0].get("photo_reference")
    except Exception as e:
        print(f"   ❌ Search API Error: {e}")
    return None

def download_photo(photo_ref, filename):
    DOWNLOAD_DIR.mkdir(exist_ok=True)
    filepath = DOWNLOAD_DIR / filename
    
    url = "https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "maxwidth": 1200,
        "photo_reference": photo_ref,
        "key": API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        if response.status_code == 200 and len(response.content) > 5000:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"   ✅ Downloaded: {filename} ({len(response.content)} bytes)")
            return filepath
        else:
            print(f"   ❌ Download failure: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Download Error: {e}")
    return None

def upload_to_firebase(local_path, filename, bucket):
    blob_path = f"cities/{CITY_ID}/{filename}"
    blob = bucket.blob(blob_path)
    
    try:
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        print(f"   🚀 Uploaded to Firebase: {blob_path}")
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"   ❌ Upload Error: {e}")
    return None

# --- Main Logic ---

def main():
    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()

    json_path = CITIES_DIR / f"{CITY_ID}.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    
    for landmark_name in LANDMARKS_TO_FIX:
        print(f"\n--- Processing: {landmark_name} ---")
        
        # 1. Find the place and get photo ref
        photo_ref = find_place_id_and_photo(landmark_name)
        if not photo_ref:
            print(f"   ⚠️ Could not find photo reference for {landmark_name}")
            continue
            
        # 2. Download photo
        filename = f"{slugify(landmark_name)}.jpg"
        local_path = download_photo(photo_ref, filename)
        if not local_path:
            continue
            
        # 3. Upload to Firebase
        firebase_url = upload_to_firebase(local_path, filename, bucket)
        if not firebase_url:
            continue
            
        # 4. Update JSON
        # Note: We might have multiple hits if names are partial (Süleymaniye)
        found_in_json = False
        for place in data.get('highlights', []):
            if landmark_name.lower() == place.get('name', '').lower() or \
               (landmark_name == "Süleymaniye" and place.get('name') == "Süleymaniye"):
                place['imageUrl'] = firebase_url
                found_in_json = True
                print(f"   📝 Updated {place.get('name')} in JSON")
        
        if found_in_json:
            updated_count += 1

        # Handle heroImage separately
        if landmark_name == "Istanbul Skyline":
            data['heroImage'] = firebase_url
            updated_count += 1
            print(f"   🖼️ Updated heroImage in JSON")

    # Save JSON
    if updated_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ Finished! Updated {updated_count} landmarks in {json_path}")
    else:
        print("\n⚠️ No landmarks were updated in the JSON.")

if __name__ == "__main__":
    main()
