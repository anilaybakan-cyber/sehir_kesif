
import json
import os
import glob
import re

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    targets = []
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            
            for place in highlights:
                desc_en = place.get('description_en', '').strip()
                if not desc_en:
                    continue
                
                # Check word count
                cleaned = re.sub(r'[^\w\s]', '', desc_en)
                word_count = len(cleaned.split())
                
                if word_count <= 7:
                    targets.append({
                        "city": city_name,
                        "name": place.get('name', ''),
                        "current_desc": desc_en
                    })
                    
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Save details to a file for the agent to read
    with open("english_update_targets.json", "w", encoding='utf-8') as f:
        json.dump(targets, f, indent=2, ensure_ascii=False)
        
    print(f"Extracted {len(targets)} targets to english_update_targets.json")

if __name__ == "__main__":
    main()
