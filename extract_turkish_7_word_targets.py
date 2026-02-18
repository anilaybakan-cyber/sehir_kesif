
import json
import os
import glob
import re

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    targets = []
    
    print(f"Scanning {len(json_files)} city files for 7-word TURKISH descriptions...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            
            for place in highlights:
                desc_tr = place.get('description', '').strip()
                if not desc_tr:
                    continue
                
                # Check word count
                cleaned = re.sub(r'[^\w\s]', '', desc_tr)
                word_count = len(cleaned.split())
                
                if word_count == 7:
                    targets.append({
                        "city": city_name,
                        "name": place.get('name', ''),
                        "current_desc": desc_tr,
                        "current_desc_en": place.get('description_en', '')
                    })
                    
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Save details to a file for the agent to read
    with open("turkish_7_word_targets.json", "w", encoding='utf-8') as f:
        json.dump(targets, f, indent=2, ensure_ascii=False)
        
    print(f"Extracted {len(targets)} targets to turkish_7_word_targets.json")

if __name__ == "__main__":
    main()
