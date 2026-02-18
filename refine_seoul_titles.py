
import json
import re

def refine_title(text):
    # Remove Chinese characters [\u4e00-\u9fff] and Japanese [\u3040-\u30ff\u31f0-\u31ff]
    text = re.sub(r'[\u4e00-\u9fff\u3040-\u30ff\u31f0-\u31ff]+', '', text)
    # Remove Arabic [\u0600-\u06FF]
    text = re.sub(r'[\u0600-\u06FF]+', '', text)
    
    # Remove pipes |, commas ,, specific bad patterns
    text = text.replace('|', ' ')
    
    # Remove any character that is NOT alphanumeric, space, hypen, ampersand, or apostrophe
    # This captures the "(&)" issue or trailing punctuation
    # But we want to be careful not to remove valid ones.
    
    # Fix specific messy detected items
    if "Pasha Kebab" in text:
        return "Pasha Kebab & Burger"
    if "tott seoul" in text:
        return "Bar Tott (Tott Seoul)"
    if "BAR HaNook" in text:
        return "Bar HaNook"
    if "Nanloyeon" in text or "Korean BBQ & Premium Galbi" in text:
        if "Nanloyeon" not in text: # If the name was stripped too much
             return "Nanloyeon Yongsan Main Branch"
    if "Woojujip" in text:
        return "Woojujip Korean BBQ"
    if "Hongdae restaurant" in text:
        return "Saebyeok Hongdae Pub"
    if "Seventeen Birthday" in text:
        return "Seventeen Birthday Pub"
    if "Yanginhwandae" in text or "City Hall Halal" in text:
        return "Yanginhwandae Bukchang"
    if "H. Charles H." in text:
        return "Charles H. Bar"
        
    # General cleanup
    text = re.sub(r'\(\s*&\s*\)', '', text) # Remove (&)
    text = re.sub(r'^\W+|\W+$', '', text) # Strip non-word chars from start/end
    text = re.sub(r'\s+', ' ', text).strip()
    
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
            
            # Apply refinement to previously cleaned names if they look messy
            # Or just check all names for Chinese/Arabic
            
            new_name = refine_title(original_name)
            
            if new_name != original_name:
                print(f"Refining: '{original_name}' -> '{new_name}'")
                place['name'] = new_name
                place['name_en'] = new_name
                updated_count += 1

        if updated_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"\nSuccessfully refined {updated_count} places in seul.json")
        else:
            print("No changes made during refinement.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
