
import json
import os
import requests
import re
import urllib.parse
import firebase_admin
from firebase_admin import credentials, storage
from pathlib import Path

# --- CONFIGURATION ---
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")
DOWNLOAD_DIR = Path("temp_ascii_fix_photos")

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def slugify(text):
    if not text: return ""
    text = text.lower()
    text = text.replace('ö','o').replace('ü','u').replace('č','c')\
               .replace('ğ','g').replace('ş','s').replace('ç','c')\
               .replace('ı','i').replace('ä','a').replace('å','a')\
               .replace('é','e').replace('ø','o').replace('ñ','n')\
               .replace('á','a').replace('í','i').replace('ó','o').replace('ú','u')\
               .replace('ý','y').replace('ř','r').replace('ž','z').replace('š','s')
    # Strict fallback for anything else
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_-]+', '_', text)
    return text.strip('_')[:50]

def download_image(url, filename, city_slug):
    city_dir = DOWNLOAD_DIR / city_slug
    city_dir.mkdir(parents=True, exist_ok=True)
    filepath = city_dir / filename
    
    # Try to encode the URL properly
    # If the URL is already fully encoded, this might double encode, be careful.
    # Usually 'https://.../foo_bar.jpg' is fine.
    # 'https://.../foo_bar_ç.jpg' needs encoding.
    
    # Split scheme/netloc and path
    parsed = urllib.parse.urlparse(url)
    
    # Encode path parts (but keep /)
    # We need to unquote first in case it was partially mixed, then quote
    decoded_path = urllib.parse.unquote(parsed.path) 
    encoded_path = urllib.parse.quote(decoded_path, safe='/')
    
    encoded_url = urllib.parse.urlunparse((
        parsed.scheme,
        parsed.netloc,
        encoded_path,
        parsed.params,
        parsed.query,
        parsed.fragment
    ))
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(encoded_url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return filepath
        elif response.status_code == 403 or response.status_code == 404:
             # Try raw url just in case requests handles it
             response = requests.get(url, headers=headers, timeout=30)
             if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                return filepath
                
        print(f"  ❌ Download failed ({response.status_code}): {encoded_url}")
        return None
        
    except Exception as e:
        print(f"  ❌ Error downloading: {e}")
        return None

def upload_to_firebase(local_path, city_slug, filename, bucket):
    blob_path = f"cities/{city_slug}/{filename}"
    blob = bucket.blob(blob_path)
    try:
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"  ❌ Upload error: {e}")
        return None

def main():
    print("Starting NON-ASCII URL Fix...")
    
    # Initialize Firebase
    if not firebase_admin._apps:
        try:
            cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
            firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
        except Exception as e:
            print(f"FATAL: Could not initialize Firebase: {e}")
            return
            
    bucket = storage.bucket()
    
    total_issues = 0
    fixed = 0
    failed = 0
    
    for json_file in CITIES_DIR.glob("*.json"):
        city_slug = json_file.stem
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            modified = False
            highlights = data.get('highlights', [])
            
            for place in highlights:
                image_url = place.get('imageUrl', '')
                if not image_url: continue
                
                # Check for non-ascii
                if not is_ascii(image_url):
                    print(f"Fixing: {city_slug} -> {place.get('name')}")
                    print(f"  Old: {image_url}")
                    total_issues += 1
                    
                    # 1. Download
                    slug_name = slugify(place.get('name'))
                    filename = f"{slug_name}.jpg"
                    local_path = download_image(image_url, filename, city_slug)
                    
                    if not local_path:
                        print("  Skipping (Download failed)")
                        failed += 1
                        continue
                        
                    # 2. Upload
                    new_url = upload_to_firebase(local_path, city_slug, filename, bucket)
                    
                    if new_url:
                        place['imageUrl'] = new_url
                        place['source'] = 'firebase'
                        modified = True
                        fixed += 1
                        print(f"  ✓ Fixed: {new_url}")
                    else:
                        print("  Skipping (Upload failed)")
                        failed += 1
            
            if modified:
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"Saved {json_file.name}")
                
        except Exception as e:
            print(f"Error processing {json_file}: {e}")

    print("\n" + "="*30)
    print("Fix Summary")
    print(f"Total Issues Found: {total_issues}")
    print(f"Fixed: {fixed}")
    print(f"Failed: {failed}")
    print("="*30)

if __name__ == "__main__":
    main()
