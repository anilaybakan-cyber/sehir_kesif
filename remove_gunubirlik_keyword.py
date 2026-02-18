
import json
import os
import glob
import re

SOURCE_DIR = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
KEYWORD = "Günübirlik"

def clean_text(text):
    if not isinstance(text, str):
        return text
    
    # Remove the keyword (case insensitive and with potential trailing/leading whitespace)
    # Using regex to handle word boundaries and multiple spaces
    pattern = re.compile(rf'\b{re.escape(KEYWORD)}\b', re.IGNORECASE)
    cleaned = pattern.sub('', text)
    
    # Clean up double spaces and leading/trailing whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    
    return cleaned

def process_city_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        changed = False
        
        # Process highlights
        if 'highlights' in data:
            for place in data['highlights']:
                for field in ['name', 'name_en', 'description', 'description_en', 'area', 'area_en']:
                    if field in place and place[field]:
                        original = place[field]
                        cleaned = clean_text(original)
                        if original != cleaned:
                            place[field] = cleaned
                            changed = True
        
        # Process other sections if needed (e.g., guide chapters)
        if 'chapters' in data:
             for chapter in data['chapters']:
                 for field in ['title', 'title_en', 'content', 'description', 'description_en']:
                     if field in chapter and chapter[field]:
                         original = chapter[field]
                         cleaned = clean_text(original)
                         if original != cleaned:
                             chapter[field] = cleaned
                             changed = True

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    
    return False

def main():
    json_files = glob.glob(os.path.join(SOURCE_DIR, "*.json"))
    print(f"Found {len(json_files)} city files.")
    
    updated_count = 0
    for filepath in json_files:
        if process_city_file(filepath):
            print(f"✓ Updated: {os.path.basename(filepath)}")
            updated_count += 1
            
    print(f"\nCleanup complete. {updated_count} files modified.")

if __name__ == "__main__":
    main()
