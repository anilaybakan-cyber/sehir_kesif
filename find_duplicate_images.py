import os
import json

def find_duplicate_images():
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    city_files = [f for f in os.listdir(assets_dir) if f.endswith('.json')]
    
    cities_with_dupes = {}
    
    for city_file in city_files:
        with open(os.path.join(assets_dir, city_file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            url_counts = {}
            for h in data.get('highlights', []):
                url = h.get('imageUrl')
                if url:
                    url_counts[url] = url_counts.get(url, 0) + 1
            
            dupes = {url: count for url, count in url_counts.items() if count > 1}
            if dupes:
                cities_with_dupes[city_file] = dupes

    print(f"--- DUPLICATE IMAGE AUDIT ---")
    # Sort cities by total dupe count
    sorted_cities = sorted(cities_with_dupes.items(), key=lambda x: sum(x[1].values()), reverse=True)
    
    for city, dupes in sorted_cities[:15]:
        total_dupes = sum(dupes.values())
        print(f"- {city}: {total_dupes} duplicated URLs (Unique dupes: {len(dupes)})")
        # List some of them
        for url, count in list(dupes.items())[:3]:
            print(f"  * {count}x: {url}")

if __name__ == "__main__":
    find_duplicate_images()
