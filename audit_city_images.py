import json
import requests
from concurrent.futures import ThreadPoolExecutor

def check_url(url):
    try:
        r = requests.head(url, timeout=5)
        return url, r.status_code
    except:
        return url, -1

def audit_city(city_file):
    with open(f'assets/cities/{city_file}', 'r') as f:
        data = json.load(f)
    
    urls = [h.get('imageUrl') for h in data.get('highlights', []) if h.get('imageUrl')]
    
    print(f"Checking {len(urls)} images for {city_file}...")
    
    broken = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(check_url, urls))
        for url, status in results:
            if status != 200:
                broken.append((url, status))
    
    print(f"Found {len(broken)} broken images in {city_file}")
    for url, status in broken[:10]:
        print(f"  - {status}: {url}")

if __name__ == "__main__":
    audit_city('berlin.json')
    audit_city('istanbul.json')
