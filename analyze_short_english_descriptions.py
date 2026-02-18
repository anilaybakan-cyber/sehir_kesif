
import json
import os
import glob
import re

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    count_5 = 0
    count_6 = 0
    count_7 = 0
    
    examples_5 = []
    
    print(f"Scanning {len(json_files)} city files for SHORT ENGLISH descriptions...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            
            for place in highlights:
                # Focus on description_en this time
                desc_en = place.get('description_en', '')
                if not desc_en:
                    # Treat empty as 0 words
                    word_count = 0
                else:
                    # Simple word count similar to previous script
                    word_count = len(re.sub(r'[^\w\s]', '', desc_en).split())
                
                if word_count <= 5:
                    count_5 += 1
                    if len(examples_5) < 10:
                        examples_5.append(f"{city_name} - {place.get('name', '')}: {desc_en}")
                
                if word_count <= 6:
                    count_6 += 1
                    
                if word_count <= 7:
                    count_7 += 1
                    
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nAnalysis Results for ENGLISH Descriptions:")
    print(f"5 words or fewer: {count_5}")
    print(f"6 words or fewer: {count_6}")
    print(f"7 words or fewer: {count_7}")
    
    print(f"\nExamples (<= 5 words):")
    for ex in examples_5:
        print(f" - {ex}")

if __name__ == "__main__":
    main()
