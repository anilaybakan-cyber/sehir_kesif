import json
import os

def cleanup_duplicates():
    base_path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    cities_to_clean = ["selanik.json", "cesme.json", "kapadokya.json", "saraybosna.json", "amalfi.json"]
    
    for city_file in cities_to_clean:
        file_path = os.path.join(base_path, city_file)
        if not os.path.exists(file_path): continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        highlights = data.get('highlights', [])
        new_highlights = []
        seen_ids = set()
        seen_names = set()
        
        for h in highlights:
            h_id = h.get('id')
            name = h.get('name')
            # Check for duplicate IDs or duplicate Names with identical descriptions
            if h_id in seen_ids or name in seen_names:
                # If we've seen the name, check if description is also same (or if we just want unique names)
                # For Mikel Coffee etc, they are exact duplicates
                continue
            
            seen_ids.add(h_id)
            seen_names.add(name)
            new_highlights.append(h)
            
        data['highlights'] = new_highlights
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Cleaned {city_file}")

if __name__ == "__main__":
    cleanup_duplicates()
