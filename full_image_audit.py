import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor

def check_url(city, name, url):
    try:
        # Use a user agent to avoid common blocks (like Wikipedia)
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.head(url, timeout=5, headers=headers, allow_redirects=True)
        return city, name, url, r.status_code
    except:
        return city, name, url, -1

def audit_all_cities():
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    city_files = [f for f in os.listdir(assets_dir) if f.endswith('.json')]
    
    all_tasks = []
    for city_file in city_files:
        with open(os.path.join(assets_dir, city_file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Check hero image
            hero = data.get('heroImage')
            if hero:
                all_tasks.append((city_file, "[HERO]", hero))
            # Check highlights
            for h in data.get('highlights', []):
                url = h.get('imageUrl')
                if url:
                    all_tasks.append((city_file, h.get('name'), url))
    
    print(f"Auditing {len(all_tasks)} images across {len(city_files)} cities...")
    
    broken = []
    # Using more workers for speed
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(check_url, city, name, url) for city, name, url in all_tasks]
        for i, future in enumerate(futures):
            city, name, url, status = future.result()
            if status != 200:
                broken.append({
                    "city": city,
                    "name": name,
                    "url": url,
                    "status": status
                })
            if (i + 1) % 500 == 0:
                print(f"Processed {i+1}/{len(all_tasks)}...")

    print(f"\n--- FULL IMAGE AUDIT REPORT ---")
    print(f"Total Broken/Blocked: {len(broken)}")
    
    # Group by status
    stats = {}
    for b in broken:
        stats[b['status']] = stats.get(b['status'], 0) + 1
    
    print("\nSummary by status:")
    for status, count in stats.items():
        print(f"- {status}: {count}")
    
    # Save to file
    with open('broken_images_full.json', 'w', encoding='utf-8') as f:
        json.dump(broken, f, ensure_ascii=False, indent=2)
    
    print(f"\nDetailed report saved to 'broken_images_full.json'")
    
    # Print top 10 broken
    print("\nSamples of broken images:")
    for b in broken[:20]:
        print(f"- {b['city']} | {b['name']} | Status {b['status']} | {b['url']}")

if __name__ == "__main__":
    audit_all_cities()
