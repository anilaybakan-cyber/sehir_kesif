
import json
import os
import glob
import re

def count_words(text):
    if not text:
        return 0
    cleaned = re.sub(r'[^\w\s]', '', text)
    return len(cleaned.split())

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    count_5_or_less = 0
    count_6_or_less = 0
    count_7_or_less = 0
    
    examples_5 = []
    
    print(f"Scanning {len(json_files)} city files...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            highlights = data.get('highlights', [])
            
            for place in highlights:
                desc_tr = place.get('description', '')
                word_count = count_words(desc_tr)
                
                if 0 < word_count <= 5:
                    count_5_or_less += 1
                    if len(examples_5) < 3:
                        examples_5.append(f"{place.get('name')} ({word_count} kelime): {desc_tr}")
                        
                if 0 < word_count <= 6:
                    count_6_or_less += 1
                    
                if 0 < word_count <= 7:
                    count_7_or_less += 1
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    print(f"\nAnalysis Results:")
    print(f"5 ve altı: {count_5_or_less}")
    print(f"6 ve altı: {count_6_or_less}")
    print(f"7 ve altı: {count_7_or_less}")
    
    print("\n5 ve altı için örnekler:")
    for ex in examples_5:
        print(f"- {ex}")

if __name__ == "__main__":
    main()
