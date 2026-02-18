
import json
import os
import glob
import re

# Common Turkish stopwords/words that rarely appear in English
TURKISH_WORDS = {
    "ve", "bir", "ile", "için", "olarak", "olan", "bu", "şu", "o", 
    "ama", "fakat", "ancak", "çünkü", "eğer", "ki", "mi", "mu", "mı", 
    "mü", "da", "de", "ne", "nasıl", "neden", "niçin", "kim", "hangi", 
    "her", "şey", "çok", "daha", "kadar", "en", "gibi", "sadece", 
    "tüm", "bütün", "aynı", "yeni", "eski", "büyük", "küçük", "yer", 
    "zaman", "gün", "yıl", "ay", "saat", "sonra", "önce", "kendi",
    "kendine", "tarafından", "arasında", "üzerinde", "altında", "içinde",
    "dışında", "birlikte", "karşı", "rağmen", "bilgi", "hakkında",
    "tarihi", "şehrin", "manzara", "keyifli", "lezzetli", "güzel"
}

def is_mostly_turkish(text):
    if not text:
        return False
    
    # Clean and tokenize
    # Remove punctuation
    cleaned = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned.split()
    
    turkish_word_count = 0
    matched_words = []
    
    for word in words:
        if word in TURKISH_WORDS:
            turkish_word_count += 1
            matched_words.append(word)
        # Check for specific Turkish characters not in English (be careful with names)
        # ı, ğ, ş usually indicate Turkish. ü, ö, ç exist in other langs but strong indicator combined.
        elif 'ı' in word or 'ğ' in word or 'ş' in word:
             # Double check it's not a proper name that stays same in English? 
             # But usually description shouldn't contain these unless it's a Turkish word.
             # Let's count them if they are lower case in the map.
             turkish_word_count += 1
             matched_words.append(word)

    # User criteria: 4 or more Turkish words
    if turkish_word_count >= 4:
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
                desc_en = place.get('description_en', '')
                is_tr, matches = is_mostly_turkish(desc_en)
                
                if is_tr:
                    detected_places.append({
                        "city": city_name,
                        "name": place.get('name', 'Unknown'),
                        "desc_en": desc_en,
                        "matches": matches
                    })
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    print(f"\nAnalysis Complete.")
    print(f"Total places with suspected Turkish content in 'description_en': {len(detected_places)}")
    
    if detected_places:
        print("\nExample:")
        example = detected_places[0]
        print(f"City: {example['city']}")
        print(f"Place: {example['name']}")
        print(f"Current Description (EN): {example['desc_en']}")
        print(f"Detected Turkish Words: {example['matches']}")

if __name__ == "__main__":
    main()
