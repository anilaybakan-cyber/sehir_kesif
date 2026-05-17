import json
import os
import time
import requests
from pathlib import Path
import firebase_admin
from firebase_admin import credentials, storage
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")
DOWNLOAD_DIR = Path("fresh_photos")

def find_place_and_get_photo(name, lat, lng):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": name,
        "key": API_KEY,
        "location": f"{lat},{lng}" if lat and lng else None,
        "radius": 5000 if lat and lng else None
    }
    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        if data.get("status") == "OK" and data.get("results"):
            for result in data["results"]:
                photos = result.get("photos", [])
                if photos:
                    return photos[0].get("photo_reference")
    except Exception as e:
        print(f"    API Error seeking {name}: {e}")
    return None

def download_photo(photo_ref, filename, city_id):
    city_dir = DOWNLOAD_DIR / city_id
    city_dir.mkdir(parents=True, exist_ok=True)
    filepath = city_dir / filename
    url = f"https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "maxwidth": 1600,
        "photo_reference": photo_ref,
        "key": API_KEY
    }
    try:
        response = requests.get(url, params=params, timeout=30)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return filepath
    except Exception as e:
        print(f"    Download Error: {e}")
    return None

def upload_to_firebase(local_path, city_id, filename, bucket):
    blob_path = f"cities/{city_id}/{filename}"
    blob = bucket.blob(blob_path)
    try:
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"    Upload Error: {e}")
        return None

def process_city(city_id, bucket):
    json_path = CITIES_DIR / f"{city_id}.json"
    if not json_path.exists(): return
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\n🏙️ Processing {city_id.upper()}")
    success = 0
    for h in data.get('highlights', []):
        if 'unsplash.com' in str(h.get('imageUrl', '')):
            print(f"  📸 Finding photo for: {h['name']}")
            photo_ref = find_place_and_get_photo(h['name'], h.get('lat'), h.get('lng'))
            if photo_ref:
                filename = f"{h['id']}.jpg"
                local_path = download_photo(photo_ref, filename, city_id)
                if local_path:
                    url = upload_to_firebase(local_path, city_id, filename, bucket)
                    if url:
                        h['imageUrl'] = url
                        success += 1
                        print("    ✅ Success")
            time.sleep(0.1)
    if success > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  Done. Updated {success} photos.")

def main():
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()
    TARGET_CITIES = ['catania', 'bari', 'sardinya', 'cannes', 'saint_tropez']
    for city in TARGET_CITIES:
        process_city(city, bucket)

if __name__ == "__main__":
    main()
