
import json
import os
import glob
import re
import time
from deep_translator import GoogleTranslator

# Same English word list for detection
ENGLISH_WORDS = {
    "the", "and", "of", "to", "in", "is", "a", "with", "for", "on", 
    "at", "by", "from", "this", "that", "it", "as", "are", "was", "were",
    "be", "or", "an", "not", "but", "if", "you", "your", "we", "our",
    "has", "have", "had", "will", "can", "one", "all", "so", "up", "out",
    "located", "city", "center", "view", "best", "place", "visit", 
    "enjoy", "famous", "known", "traditional", "delicious", "served", 
    "dishes", "great", "beautiful", "experience", "history", "building", 
    "street", "square", "old", "new", "restaurant", "museum", "garden",
    "park", "bridge", "church", "cathedral", "castle", "palace", "house",
    "shop", "store", "market", "room", "night", "day", "time", "life",
    "world", "local", "during", "offering", "features", "offers", "popular"
}

def is_mostly_english(text):
    if not text:
        return False
    
    cleaned = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned.split()
    
    english_word_count = 0
    
    for word in words:
        if word in ENGLISH_WORDS:
            english_word_count += 1

    if english_word_count >= 4:
        return True
    return False

def translate_to_tr(text):
    if not text:
        return ""
    try:
        for i in range(3):
            try:
                return GoogleTranslator(source='en', target='tr').translate(text)
            except Exception:
                time.sleep(1)
        return GoogleTranslator(source='en', target='tr').translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return ""

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    total_updated = 0
    
    print(f"Scanning {len(json_files)} city files...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            file_updated = False
            
            for place in highlights:
                desc_tr = place.get('description', '')
                
                # Check for English content in Turkish field
                if is_mostly_english(desc_tr):
                    print(f"Translating for {city_name} - {place.get('name', 'Unknown')}")
                    print(f"  Old TR (actually EN): {desc_tr[:50]}...")
                    
                    # Translate from the existing content (which is EN) to TR
                    translated = translate_to_tr(desc_tr)
                    
                    if translated:
                        place['description'] = translated
                        file_updated = True
                        total_updated += 1
                        print(f"  New TR: {translated[:50]}...")
            
            if file_updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Saved updates to {city_name}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nTotal Turkish descriptions corrected: {total_updated}")

if __name__ == "__main__":
    main()
