
import json
import re
import time
from deep_translator import GoogleTranslator

def clean_mixed_title(text):
    # Remove Korean characters
    text = re.sub(r'[\uAC00-\uD7A3\u1100-\u11FF]+', '', text)
    # Remove empty parenthesis () or [] or |
    text = re.sub(r'\(\s*\)', '', text)
    text = re.sub(r'\[\s*\]', '', text)
    text = re.sub(r'\|\s*\|', '', text)
    # Remove trailing/leading pipes or special chars often used as separators
    text = re.sub(r'^[|\s]+|[|\s]+$', '', text)
    # Clean multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def has_latin(text):
    return bool(re.search(r'[a-zA-Z]', text))

def has_korean(text):
    if not text:
        return False
    return bool(re.search(r'[\uAC00-\uD7A3\u1100-\u11FF]', text))

def translate_korean(text):
    try:
        # Translate to English as the standard international name
        translated = GoogleTranslator(source='ko', target='en').translate(text)
        return translated
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def main():
    file_path = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/seul.json"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        highlights = data.get('highlights', [])
        updated_count = 0
        
        print("Processing Seul titles...")
        
        for place in highlights:
            original_name = place.get('name', '')
            original_name_en = place.get('name_en', '')
            
            # Check and fix 'name' (TR/Display)
            if has_korean(original_name):
                print(f"Processing: {original_name}")
                if has_latin(original_name):
                    # Mixed content - strip Korean
                    new_name = clean_mixed_title(original_name)
                    print(f"  -> Cleaned (Latin kept): {new_name}")
                else:
                    # Pure Korean - Translate
                    new_name = translate_korean(original_name)
                    time.sleep(0.5) # rate limit
                    print(f"  -> Translated: {new_name}")
                
                place['name'] = new_name
                updated_count += 1
            
            # Check and fix 'name_en'
            # Usually we want name_en to be same as name if name was fixed to English/Latin
            # But let's check explicitly
            if has_korean(original_name_en):
                if has_latin(original_name_en):
                    new_name_en = clean_mixed_title(original_name_en)
                else:
                    new_name_en = translate_korean(original_name_en)
                    time.sleep(0.5)
                place['name_en'] = new_name_en

        if updated_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"\nSuccessfully updated {updated_count} places in seul.json")
        else:
            print("No changes made.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
