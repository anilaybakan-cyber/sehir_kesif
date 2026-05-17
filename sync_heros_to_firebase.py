import os
import json
import requests
import firebase_admin
from firebase_admin import credentials, storage

def sync_heros():
    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate('service_account.json')
        firebase_admin.initialize_app(cred, {'storageBucket': 'myway-3fe75.firebasestorage.app'})
    
    bucket = storage.bucket()
    
    with open("hero_sync_list.json", "r") as f:
        hero_list = json.load(f)
    
    for city_id, url in hero_list.items():
        print(f"--- Syncing Hero for {city_id} ---")
        try:
            # Download
            r = requests.get(url)
            local_filename = f"temp_hero_{city_id}.jpg"
            with open(local_filename, "wb") as f:
                f.write(r.content)
            
            # Upload
            blob = bucket.blob(f"cities/{city_id}/hero.jpg")
            blob.upload_from_filename(local_filename, content_type='image/jpeg')
            blob.make_public()
            print(f"✅ Uploaded: {blob.public_url}")
            
            # Cleanup
            os.remove(local_filename)
        except Exception as e:
            print(f"❌ Error syncing {city_id}: {e}")

if __name__ == "__main__":
    sync_heros()
