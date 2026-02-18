import re
import requests
from concurrent.futures import ThreadPoolExecutor

def check_url(city, url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.head(url, timeout=5, headers=headers, allow_redirects=True)
        return city, url, r.status_code
    except:
        return city, url, -1

def audit_ai_service_images():
    with open('/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/lib/services/ai_service.dart', 'r') as f:
        content = f.read()
    
    # Extract mappings from _cityImages
    matches = re.findall(r"'(.*?)':\s*'(.*?)'", content)
    
    print(f"Checking {len(matches)} AIService city images...")
    
    broken = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_url, city, url) for city, url in matches]
        for future in futures:
            city, url, status = future.result()
            if status != 200:
                broken.append((city, url, status))
                
    print("\n--- BROKEN AISERVICE IMAGES ---")
    for city, url, status in broken:
        print(f"- {city}: {status} ({url})")

if __name__ == "__main__":
    audit_ai_service_images()
