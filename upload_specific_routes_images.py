
import requests
import firebase_admin
from firebase_admin import credentials, storage
import json

def upload_specific_images():
    # Headers to mimic browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    # Files to process
    targets = [
        {
            "city": "rovaniemi",
            "file": "assets/cities/rovaniemi.json",
            "place_name": "Northern Lights Tour Point",
            "image_url": "https://wildaboutlapland.com/wp-content/uploads/2024/10/Northern-Lights-Wilderness-Tour-with-Professional-Camera-1-scaled.jpg",
            "firebase_name": "northern_lights_tour_point.jpg"
        },
        {
            "city": "zermatt",
            "file": "assets/cities/zermatt.json",
            "place_name": "Monte Rosa Hütte",
            "image_url": "https://cdn.media.amplience.net/i/zermatt/5152eca4-2f38-444a-b0d0-5156cadfbd48_main?fmt=auto&w=1470&h=1102&sm=c",
            "firebase_name": "monte_rosa_hutte_hut.jpg"
        }
    ]

    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate('service_account.json')
        firebase_admin.initialize_app(cred, {'storageBucket': 'myway-3fe75.firebasestorage.app'})

    bucket = storage.bucket()

    print("--- Starting Specific Image Upload ---")

    for target in targets:
        city = target['city']
        print(f"\nProcessing {city} -> {target['place_name']}")
        
        # 1. Download
        print(f"Downloading from {target['image_url']}...")
        try:
            resp = requests.get(target['image_url'], headers=headers, stream=True)
            if resp.status_code != 200:
                print(f"❌ Failed to download! Status: {resp.status_code}")
                continue
        except Exception as e:
            print(f"❌ Download Error: {e}")
            continue

        local_path = f"temp_{target['firebase_name']}"
        with open(local_path, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)

        # 2. Upload to Firebase
        blob_path = f"cities/{city}/{target['firebase_name']}"
        print(f"Uploading to {blob_path}...")
        blob = bucket.blob(blob_path)
        blob.upload_from_filename(local_path)
        blob.make_public()
        public_url = blob.public_url
        print(f"✅ Uploaded: {public_url}")

        # 3. Update JSON
        json_path = target['file']
        print(f"Updating {json_path}...")
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
            
            found = False
            if 'highlights' in data:
                for h in data['highlights']:
                    if h.get('name') == target['place_name']:
                        h['imageUrl'] = public_url
                        found = True
                        print(f"Updated imageUrl for '{target['place_name']}'")
                        break
            
            if found:
                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print("JSON saved.")
            else:
                print(f"⚠️ Place '{target['place_name']}' NOT FOUND in JSON!")

        except Exception as e:
            print(f"❌ JSON Update Error: {e}")

    print("\n--- Done ---")

if __name__ == "__main__":
    upload_specific_images()
