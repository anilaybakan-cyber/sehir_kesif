#!/usr/bin/env python3
"""
Upload Prague venue photos to Firebase Storage
"""
import os
import csv
import firebase_admin
from firebase_admin import credentials, storage

# Constants
BUCKET_NAME = 'myway-3fe75.firebasestorage.app'
PHOTOS_DIR = 'prag_venue_photos'
CITY = 'prag'

def init_firebase():
    """Initialize Firebase if not already done"""
    if not firebase_admin._apps:
        cred = credentials.Certificate('service_account.json')
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    return storage.bucket()

def sanitize_filename(name):
    """Create safe filename from venue name"""
    safe_name = name.lower().replace(" ", "_").replace("'", "").replace('"', "")
    safe_name = ''.join(c for c in safe_name if c.isalnum() or c == '_' or c == 'á' or c == 'é' or c == 'í' or c == 'ó' or c == 'ú' or c == 'ý' or c == 'č' or c == 'ď' or c == 'ě' or c == 'ň' or c == 'ř' or c == 'š' or c == 'ť' or c == 'ů' or c == 'ž')
    return safe_name

def upload_photos():
    """Upload all photos to Firebase and return URL mapping"""
    bucket = init_firebase()
    results = []
    
    # Get list of photos
    photos = [f for f in os.listdir(PHOTOS_DIR) if f.endswith('.jpg')]
    print(f"Found {len(photos)} photos to upload...")
    
    for i, photo in enumerate(photos):
        local_path = os.path.join(PHOTOS_DIR, photo)
        
        # Firebase path - normalize filename for URL compatibility
        firebase_name = photo.replace('á', 'a').replace('é', 'e').replace('í', 'i')
        firebase_name = firebase_name.replace('ó', 'o').replace('ú', 'u').replace('ý', 'y')
        firebase_name = firebase_name.replace('č', 'c').replace('ď', 'd').replace('ě', 'e')
        firebase_name = firebase_name.replace('ň', 'n').replace('ř', 'r').replace('š', 's')
        firebase_name = firebase_name.replace('ť', 't').replace('ů', 'u').replace('ž', 'z')
        firebase_name = firebase_name.replace('ô', 'o')
        
        blob_path = f"cities/{CITY}/{firebase_name}"
        
        print(f"[{i+1}/{len(photos)}] Uploading {photo} -> {blob_path}")
        
        try:
            blob = bucket.blob(blob_path)
            blob.upload_from_filename(local_path)
            blob.make_public()
            public_url = blob.public_url
            
            print(f"  ✅ {public_url}")
            results.append({
                "original_file": photo,
                "firebase_path": blob_path,
                "public_url": public_url
            })
        except Exception as e:
            print(f"  ❌ Error: {e}")
            results.append({
                "original_file": photo,
                "firebase_path": "",
                "public_url": ""
            })
    
    # Save results
    with open("prag_firebase_upload_results.csv", 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["original_file", "firebase_path", "public_url"])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"\n✅ Done! {len([r for r in results if r['public_url']])} photos uploaded.")
    print("Results saved to prag_firebase_upload_results.csv")
    
    return results

if __name__ == "__main__":
    upload_photos()
