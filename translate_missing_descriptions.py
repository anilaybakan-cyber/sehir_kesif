
import json
import os
import glob
import time
from deep_translator import GoogleTranslator

def translate_text(text):
    if not text:
        return ""
    try:
        # Retry logic
        for i in range(3):
            try:
                return GoogleTranslator(source='tr', target='en').translate(text)
            except Exception:
                time.sleep(1)
        return GoogleTranslator(source='tr', target='en').translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return ""

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    total_updated = 0
    
    print(f"Scanning {len(json_files)} city files in {source_dir}...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            file_updated = False
            
            for place in highlights:
                # Check if description_en is missing or empty
                desc_en = place.get('description_en', '').strip()
                desc_tr = place.get('description', '').strip()
                
                if not desc_en and desc_tr:
                    print(f"Translating for {city_name} - {place.get('name', 'Unknown')}")
                    
                    translated = translate_text(desc_tr)
                    
                    if translated:
                        place['description_en'] = translated
                        file_updated = True
                        total_updated += 1
                        print(f"  -> {translated[:50]}...")
            
            if file_updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Saved updates to {city_name}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nTotal descriptions updated: {total_updated}")

if __name__ == "__main__":
    main()
