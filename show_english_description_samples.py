
import json
import os
import glob
import re

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    tier_5 = [] # <= 5
    tier_6 = [] # == 6
    tier_7 = [] # == 7
    
    print(f"Scanning {len(json_files)} city files...")
    
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
                    
                # Clean counting
                original_desc = desc_en
                # Remove punctuation for counting
                cleaned = re.sub(r'[^\w\s]', '', desc_en)
                word_count = len(cleaned.split())
                
                entry = f"[{city_name}] {place.get('name', '')}: \"{original_desc}\""
                
                if word_count <= 5:
                    tier_5.append(entry)
                elif word_count == 6:
                    tier_6.append(entry)
                elif word_count == 7:
                    tier_7.append(entry)
                    
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nSTATS:")
    print(f"<= 5 words: {len(tier_5)}")
    print(f"== 6 words: {len(tier_6)}")
    print(f"== 7 words: {len(tier_7)}")
    print(f"Total <= 7 words: {len(tier_5) + len(tier_6) + len(tier_7)}")
    
    print(f"\n=== SAMPLE DESCRIPTIONS (<= 5 words) ===")
    for item in tier_5:
        print(item)
        
    print(f"\n=== SAMPLE DESCRIPTIONS (== 6 words) (First 10) ===")
    for item in tier_6[:10]:
        print(item)

    print(f"\n=== SAMPLE DESCRIPTIONS (== 7 words) (First 10) ===")
    for item in tier_7[:10]:
        print(item)

if __name__ == "__main__":
    main()
