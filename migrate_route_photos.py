#!/usr/bin/env python3
"""
Rota Fotoğraflarını Firebase'e Taşıma Script'i V4 (Robust)
urllib kullanarak parametreleri ayrıştırır.
"""

import re
import os
import requests
import hashlib
import firebase_admin
from firebase_admin import credentials, storage
from urllib.parse import urlparse, parse_qs

# Yapılandırma
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
ROUTES_FOLDER = "routes"
DART_FILE = "lib/services/curated_routes_service.dart"
LOCAL_DOWNLOAD_FOLDER = "migrated_photos_batch4"
# Key'i direkt Dart dosyasındaki URL'den alacağız

def extract_photo_refs(dart_content):
    """Dart dosyasından photo_reference değerlerini ve tam eşleşen stringi çıkarır"""
    full_pattern = r'"(https://maps\.googleapis\.com/maps/api/place/photo\?[^"]+)"'
    matches = re.finditer(full_pattern, dart_content)
    
    results = [] 
    for m in matches:
        full_url = m.group(1)
        parsed = urlparse(full_url)
        params = parse_qs(parsed.query)
        
        if 'photo_reference' in params:
            ref = params['photo_reference'][0]
            key = params.get('key', [None])[0]
            
            results.append({
                'original_url': full_url,
                'reference': ref,
                'key': key
            })
    
    return results

def generate_filename(ref, index):
    short_hash = hashlib.md5(ref.encode()).hexdigest()[:12]
    return f"route_photo_v4_{index}_{short_hash}.jpg"

def download_photo(ref, key, filename, download_folder):
    if not key:
        print(f"  [ERROR] Key bulunamadı: {filename}")
        return None
        
    filepath = os.path.join(download_folder, filename)
    if os.path.exists(filepath):
        # Dosya boş mu kontrol et
        if os.path.getsize(filepath) > 0:
            print(f"  [SKIP DOWNLOAD] Zaten var: {filename}")
            return filepath
    
    clean_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1600&photo_reference={ref}&key={key}"
    
    try:
        response = requests.get(clean_url, timeout=30)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"  [DOWNLOAD OK] {filename}")
            return filepath
        else:
            print(f"  [DOWNLOAD ERROR] HTTP {response.status_code}")
            # print(f"  URL: {clean_url}") 
            return None
    except Exception as e:
        print(f"  [DOWNLOAD EXCEPTION] {e}")
        return None

def upload_to_firebase(local_path, filename, bucket):
    blob_path = f"{ROUTES_FOLDER}/{filename}"
    blob = bucket.blob(blob_path)
    
    if blob.exists():
         return f"https://storage.googleapis.com/{BUCKET_NAME}/{blob_path}"

    try:
        blob.upload_from_filename(local_path)
        blob.make_public()
        return f"https://storage.googleapis.com/{BUCKET_NAME}/{blob_path}"
    except Exception as e:
        print(f"  [UPLOAD ERROR] {e}")
        return None

def main():
    print("=" * 60)
    print("MİGRASYON SCRIPT V4 (URLLIB)")
    print("=" * 60)
    
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()
    
    with open(DART_FILE, 'r', encoding='utf-8') as f:
        dart_content = f.read()
    
    items = extract_photo_refs(dart_content)
    
    # Unique hale getir
    unique_items = []
    seen = set()
    for item in items:
        if item['original_url'] not in seen:
            seen.add(item['original_url'])
            unique_items.append(item)
            
    if not unique_items:
        print("✓ Google Maps URL'si kalmamış.")
        return

    print(f"✓ {len(unique_items)} adet URL bulundu.")
    os.makedirs(LOCAL_DOWNLOAD_FOLDER, exist_ok=True)
    
    url_mapping = {}
    
    for i, item in enumerate(unique_items):
        ref = item['reference']
        key = item['key']
        filename = generate_filename(ref, i)
        
        local_path = download_photo(ref, key, filename, LOCAL_DOWNLOAD_FOLDER)
        
        if local_path:
            firebase_url = upload_to_firebase(local_path, filename, bucket)
            if firebase_url:
                url_mapping[item['original_url']] = firebase_url
                print(f"  -> Mapped: {filename}")

    if url_mapping:
        print(f"\nDosya güncelleniyor ({len(url_mapping)} değişiklik)...")
        updated_content = dart_content
        for old_url, new_url in url_mapping.items():
            updated_content = updated_content.replace(old_url, new_url)
        
        with open(DART_FILE, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("✓ Dart dosyası başarıyla güncellendi!")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
