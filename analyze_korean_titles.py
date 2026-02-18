
import json
import re

def has_korean(text):
    if not text:
        return False
    # Check for Hangul Syllables and Jamo
    return bool(re.search(r'[\uAC00-\uD7A3\u1100-\u11FF]', text))

def main():
    file_path = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/seul.json"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        highlights = data.get('highlights', [])
        korean_names_tr = [] # Korean in 'name' (TR target)
        korean_names_en = [] # Korean in 'name_en' (EN target)
        
        print(f"Scanning {len(highlights)} places in Seul...")
        
        for place in highlights:
            name = place.get('name', '')
            name_en = place.get('name_en', '')
            
            if has_korean(name):
                korean_names_tr.append(name)
                
            if has_korean(name_en):
                korean_names_en.append(name_en)
                
        print(f"\nAnalysis Results:")
        print(f"Places with Korean in 'name' (TR field): {len(korean_names_tr)}")
        if korean_names_tr:
            print(f"Example: {korean_names_tr[0]}")
            
        print(f"Places with Korean in 'name_en' (EN field): {len(korean_names_en)}")
        if korean_names_en:
            print(f"Example: {korean_names_en[0]}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
