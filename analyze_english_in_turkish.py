
import json
import os
import glob
import re

# Common English words that are definitely not Turkish
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

# Words that might be common or loanwords, so we might exclude them to be safe, 
# but strictly English structure words like "the", "is", "with" are the best indicators.

def is_mostly_english(text):
    if not text:
        return False, []
    
    # Clean and tokenize
    cleaned = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned.split()
    
    english_word_count = 0
    matched_words = []
    
    for word in words:
        if word in ENGLISH_WORDS:
            english_word_count += 1
            matched_words.append(word)

    # User criteria: 4 or more English words
    if english_word_count >= 4:
        return True, matched_words
    return False, []

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    detected_places = []
    
    print(f"Scanning {len(json_files)} city files...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            
            for place in highlights:
                desc_tr = place.get('description', '')
                is_en, matches = is_mostly_english(desc_tr)
                
                if is_en:
                    detected_places.append({
                        "city": city_name,
                        "name": place.get('name', 'Unknown'),
                        "desc_tr": desc_tr,
                        "matches": matches
                    })
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    print(f"\nAnalysis Complete.")
    print(f"Total places with suspected English content in 'description' (TR): {len(detected_places)}")
    
    if detected_places:
        print("\nExample:")
        example = detected_places[0]
        print(f"City: {example['city']}")
        print(f"Place: {example['name']}")
        print(f"Current Description (TR): {example['desc_tr']}")
        print(f"Detected English Words: {example['matches']}")

if __name__ == "__main__":
    main()
