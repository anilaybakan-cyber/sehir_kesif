import firebase_admin
from firebase_admin import credentials, storage
import time

SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"

def main():
    print("🚀 Starting mass public ACL update...")
    cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
    firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()
    
    print("Listing all blobs in cities/...")
    blobs = list(bucket.list_blobs(prefix="cities/"))
    total = len(blobs)
    print(f"Found {total} blobs.")
    
    success_count = 0
    error_count = 0
    
    for i, blob in enumerate(blobs):
        try:
            # We only care about images
            if blob.name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                blob.make_public()
                success_count += 1
            if i % 50 == 0:
                print(f"Processed {i}/{total}... (Success: {success_count}, Errors: {error_count})")
        except Exception as e:
            error_count += 1
            print(f"❌ Error on {blob.name}: {e}")
            
    print(f"\n✅ Finished! Made {success_count} images public. Errors: {error_count}")

if __name__ == "__main__":
    main()
