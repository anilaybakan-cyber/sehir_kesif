import firebase_admin
from firebase_admin import credentials, storage

SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"

def main():
    print("Initializing Firebase Admin...")
    cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
    firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    
    bucket = storage.bucket()
    
    print("Listing files in cities/barcelona/...")
    blobs = list(bucket.list_blobs(prefix="cities/barcelona/", max_results=20))
    for blob in blobs:
        print(f" - {blob.name} (Public: {blob.public_url is not None})")

if __name__ == "__main__":
    main()
