import firebase_admin
from firebase_admin import credentials, storage

SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"

def main():
    print("Initializing Firebase Admin...")
    cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
    firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    
    bucket = storage.bucket()
    
    print("Fetching blobs in cities/barcelona/ prefix...")
    blobs = list(bucket.list_blobs(prefix="cities/barcelona/"))
    print(f"Found {len(blobs)} files.")
    
    public_count = 0
    for i, blob in enumerate(blobs):
        try:
            blob.make_public()
            public_count += 1
            if i % 10 == 0:
                print(f"Processed {i}/{len(blobs)}...")
        except Exception as e:
            print(f"Error making {blob.name} public: {e}")
            
    print(f"\nDone! Successfully made {public_count} files public in Barcelona.")
    
if __name__ == "__main__":
    main()
