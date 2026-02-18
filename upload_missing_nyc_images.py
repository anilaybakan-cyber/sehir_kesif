
import requests
import firebase_admin
from firebase_admin import credentials, storage
import os

def upload_missing_images():
    # Headers to avoid 403 blocks from Wikimedia/Unsplash
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    # Target Images with robust public URLs
    images = {
        # Pebble Beach: Direct view via Special:FilePath
        "pebble_beach.jpg": "https://commons.wikimedia.org/wiki/Special:FilePath/Pebble_Beach_(46549148).jpeg",
        
        # Time Out Market: DUMBO view (best proxy for the market experience) (Already Success)
        # "timeout_market.jpg": "https://images.unsplash.com/photo-1534270804882-6b5048b1c1fc?w=1200",
        
        # Grimaldi's: The actual pizzeria via Special:FilePath
        "grimaldis.jpg": "https://commons.wikimedia.org/wiki/Special:FilePath/Grimaldi's.JPG"
    }

    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate('service_account.json')
        firebase_admin.initialize_app(cred, {'storageBucket': 'myway-3fe75.firebasestorage.app'})

    bucket = storage.bucket()
    base_path = "cities/newyork/"

    print("--- Starting Upload for Missing NYC Images ---")

    for filename, url in images.items():
        blob_path = f"{base_path}{filename}"
        print(f"\nProcessing: {filename}")
        print(f"Source: {url}")
        
        try:
            # 1. Download
            print("Downloading...")
            resp = requests.get(url, headers=headers, stream=True)
            if resp.status_code != 200:
                print(f"❌ Failed to download! Status: {resp.status_code}")
                continue
                
            # 2. Upload
            print(f"Uploading to {blob_path}...")
            blob = bucket.blob(blob_path)
            blob.upload_from_string(resp.content, content_type="image/jpeg")
            blob.make_public()
            
            print(f"✅ Success! Public URL: {blob.public_url}")
            
        except Exception as e:
            print(f"❌ Error: {e}")

    print("\n--- Done ---")

if __name__ == "__main__":
    upload_missing_images()
