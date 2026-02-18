
import json

def fix_title(text):
    if '(' in text and ')' not in text:
        text += ')'
    if '[' in text and ']' not in text:
        text += ']'
    return text

def main():
    file_path = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/seul.json"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        highlights = data.get('highlights', [])
        updated_count = 0
        
        for place in highlights:
            original_name = place.get('name', '')
            new_name = fix_title(original_name)
            
            if new_name != original_name:
                print(f"Fixing: '{original_name}' -> '{new_name}'")
                place['name'] = new_name
                place['name_en'] = new_name
                updated_count += 1

        if updated_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"\nSuccessfully fixed {updated_count} places in seul.json")
        else:
            print("No changes needed.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
