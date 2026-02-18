import os
import json
import requests
import random
from concurrent.futures import ThreadPoolExecutor

def check_url(url):
    try:
        r = requests.head(url, timeout=5)
        return url, r.status_code
    except:
        return url, -1

def audit_urls():
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    city_files = [f for f in os.listdir(assets_dir) if f.endswith('.json')]
    
    all_urls = []
    for city_file in city_files:
        with open(os.path.join(assets_dir, city_file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            for h in data.get('highlights', []):
                if h.get('imageUrl'):
                    all_urls.append((city_file, h.get('name'), h.get('imageUrl')))
    
    # Sample 100 URLs to check
    sample_size = min(100, len(all_urls))
    sample = random.sample(all_urls, sample_size)
    
    print(f"Checking {sample_size} random images for 404s...")
    
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_url, url): (city, name) for city, name, url in sample}
        for future in futures:
            city, name = futures[future]
            url, status = future.result()
            if status != 200:
                results.append((city, name, url, status))
    
    print(f"\n--- URL CHECK REPORT (Sample of {sample_size}) ---")
    if not results:
        print("All sampled URLs returned 200 OK.")
    else:
        print(f"Found {len(results)} broken/invalid links in sample:")
        for city, name, url, status in results[:10]:
            print(f"- {city}: {name} -> {status} ({url})")
            
    # Also check for suspected mismatched names (e.g. shibuya in berlin)
    mismatches = []
    for city, name, url in all_urls:
        city_slug = city.replace('.json', '')
        if f"/{city_slug}/" not in url.lower() and "firebasestorage" in url:
            mismatches.append((city, name, url))
            
    if mismatches:
        print(f"\n--- POTENTIAL PATH MISMATCHES ({len(mismatches)} total) ---")
        for city, name, url in mismatches[:10]:
            print(f"- {city}: {name} -> {url}")

if __name__ == "__main__":
    audit_urls()
