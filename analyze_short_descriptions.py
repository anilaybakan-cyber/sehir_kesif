
import json
import os
import glob
import re

def count_words(text):
    if not text:
        return 0
    # Simple whitespace split, removing punctuation
    cleaned = re.sub(r'[^\w\s]', '', text)
    return len(cleaned.split())

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    short_desc_places = []
    
    print(f"Scanning {len(json_files)} city files...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            
            for place in highlights:
                desc_tr = place.get('description', '')
                word_count = count_words(desc_tr)
                
                # Check for 10 or fewer words
                # We should also ensure it's not empty, assuming empty ones were handled before?
                # But looking for short content implies non-empty too.
                if 0 < word_count <= 10:
                    short_desc_places.append({
                        "city": city_name,
                        "name": place.get('name', 'Unknown'),
                        "desc_tr": desc_tr,
                        "word_count": word_count
                    })
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    print(f"\nAnalysis Complete.")
    print(f"Total places with 10 or fewer words in 'description' (TR): {len(short_desc_places)}")
    
    if short_desc_places:
        print("\nExample:")
        example = short_desc_places[0]
        print(f"City: {example['city']}")
        print(f"Place: {example['name']}")
        print(f"Current Description (TR): {example['desc_tr']}")
        print(f"Word Count: {example['word_count']}")

if __name__ == "__main__":
    main()
