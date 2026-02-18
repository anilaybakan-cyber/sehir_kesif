import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor

def check_url(url):
    try:
        # Use a real browser-like User-Agent to avoid simple blocks
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        r = requests.head(url, timeout=5, headers=headers, allow_redirects=True)
        return url, r.status_code
    except:
        return url, -1

def audit_hero_images():
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    city_files = [f for f in os.listdir(assets_dir) if f.endswith('.json')]
    
    hero_urls = []
    for city_file in city_files:
        with open(os.path.join(assets_dir, city_file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            url = data.get('heroImage')
            if url:
                hero_urls.append((city_file, url))
    
    print(f"Checking {len(hero_urls)} hero images...")
    
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_url, url): city for city, url in hero_urls}
        for future in futures:
            city = futures[future]
            url, status = future.result()
            if status != 200:
                results.append((city, url, status))
    
    print(f"\n--- HERO IMAGE AUDIT REPORT ---")
    if not results:
        print("All hero images returned 200 OK.")
    else:
        print(f"Found {len(results)} broken/invalid hero links:")
        for city, url, status in results:
            print(f"- {city}: {status} ({url})")

if __name__ == "__main__":
    audit_hero_images()
