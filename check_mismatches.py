import os
import json

def check_mismatches():
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    city_files = [f for f in os.listdir(assets_dir) if f.endswith('.json')]
    
    mismatches = []
    
    for city_file in city_files:
        city_slug = city_file.replace('.json', '')
        # Normalize city slug for comparison (common mapping)
        slug_norm = city_slug.replace('stokholm', 'stockholm').replace('londra', 'london').replace('roma', 'rome').replace('lizbon', 'lisbon').replace('kopenhag', 'copenhagen')
        
        with open(os.path.join(assets_dir, city_file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            for h in data.get('highlights', []):
                url = h.get('imageUrl', '')
                if "firebasestorage" in url:
                    # Check if the city slug is in the path
                    if f"/{slug_norm}/" not in url.lower() and f"/{city_slug}/" not in url.lower():
                        mismatches.append((city_file, h.get('name'), url))

    print(f"Total Highlights with path mismatches: {len(mismatches)}")
    for city, name, url in mismatches[:20]:
        print(f"- {city}: {name} -> {url}")

if __name__ == "__main__":
    check_mismatches()
