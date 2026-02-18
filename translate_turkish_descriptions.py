
import json
import os
import glob
import re
import time
from deep_translator import GoogleTranslator

TURKISH_WORDS = {
    "ve", "bir", "ile", "için", "olarak", "olan", "bu", "şu", "o", 
    "ama", "fakat", "ancak", "çünkü", "eğer", "ki", "mi", "mu", "mı", 
    "mü", "da", "de", "ne", "nasıl", "neden", "niçin", "kim", "hangi", 
    "her", "şey", "çok", "daha", "kadar", "en", "gibi", "sadece", 
    "tüm", "bütün", "aynı", "yeni", "eski", "büyük", "küçük", "yer", 
    "zaman", "gün", "yıl", "ay", "saat", "sonra", "önce", "kendi",
    "kendine", "tarafından", "arasında", "üzerinde", "altında", "içinde",
    "dışında", "birlikte", "karşı", "rağmen", "bilgi", "hakkında",
    "tarihi", "şehrin", "manzara", "keyifli", "lezzetli", "güzel",
    "yetişen", "hazırlanan", "edildiği", "servis", "mekan", "ünlü"
}

def is_mostly_turkish(text):
    if not text:
        return False
    
    cleaned = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned.split()
    
    turkish_word_count = 0
    
    for word in words:
        if word in TURKISH_WORDS:
            turkish_word_count += 1
        elif 'ı' in word or 'ğ' in word or 'ş' in word:
             turkish_word_count += 1

    if turkish_word_count >= 4:
        return True
    return False

def translate_text(text):
    if not text:
        return ""
    try:
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
    
    print(f"Scanning {len(json_files)} city files...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            file_updated = False
            
            for place in highlights:
                desc_en = place.get('description_en', '')
                desc_tr = place.get('description', '')
                
                # Check for Turkish content in English field
                if is_mostly_turkish(desc_en):
                    print(f"Translating for {city_name} - {place.get('name', 'Unknown')}")
                    print(f"  Old EN: {desc_en[:50]}...")
                    
                    # Translate from the TR description source
                    translated = translate_text(desc_tr)
                    
                    if translated:
                        place['description_en'] = translated
                        file_updated = True
                        total_updated += 1
                        print(f"  New EN: {translated[:50]}...")
            
            if file_updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Saved updates to {city_name}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nTotal descriptions corrected: {total_updated}")

if __name__ == "__main__":
    main()
