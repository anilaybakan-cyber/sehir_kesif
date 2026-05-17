import json
import os

def check_all_cities(dir_path):
    results = {}
    for filename in os.listdir(dir_path):
        if filename.endswith('.json'):
            file_path = os.path.join(dir_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                highlights = data.get('highlights', [])
                desc_map = {}
                duplicates = []
                
                for h in highlights:
                    desc = h.get('description', '')
                    if not desc or len(desc) < 20: continue # Ignore empty or very short
                    
                    if desc in desc_map:
                        duplicates.append({
                            'name': h.get('name'),
                            'duplicate_of': desc_map[desc],
                        })
                    else:
                        desc_map[desc] = h.get('name')
                
                if duplicates:
                    results[filename] = duplicates
            except:
                continue
    return results

if __name__ == "__main__":
    all_dupes = check_all_cities('/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
    if all_dupes:
        for city, dupes in all_dupes.items():
            print(f"[{city}] Found {len(dupes)} duplicates:")
            for d in dupes:
                print(f"  - {d['name']} -> {d['duplicate_of']}")
    else:
        print("No duplicate descriptions found in any city.")
