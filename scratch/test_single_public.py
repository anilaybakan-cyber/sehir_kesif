import firebase_admin
from firebase_admin import credentials, storage
import requests

SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
TEST_BLOB = "cities/barcelona/7_portes.jpg"

def main():
    print(f"Testing public access for {TEST_BLOB}...")
    cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
    firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()
    blob = bucket.blob(TEST_BLOB)
    
    print("Making public...")
    blob.make_public()
    url = blob.public_url
    print(f"Public URL: {url}")
    
    print("Testing URL with requests...")
    try:
        resp = requests.get(url, timeout=10)
        print(f"Status Code: {resp.status_code}")
        if resp.status_code == 200:
            print("✅ Success! Image is public.")
        else:
            print(f"❌ Failed with status {resp.status_code}")
    except Exception as e:
        print(f"❌ Request error: {e}")

if __name__ == "__main__":
    main()
