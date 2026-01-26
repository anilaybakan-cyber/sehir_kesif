#!/usr/bin/env python3
"""
Description Enrichment Script using Gemini API
Enriches short place descriptions with detailed, guide-style content.
"""

import json
import time
import google.generativeai as genai

# Gemini API Configuration
GEMINI_API_KEY = "AIzaSyDL3n3joYZ_MwVj1lbXF2xTBAEMQqYprYA"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-flash-latest')

CITY_FILE = "assets/cities/milano.json"
MIN_DESCRIPTION_LENGTH = 80  # Characters
TARGET_DESCRIPTION_LENGTH = 200  # Target ~200 chars

def generate_rich_description(place_name, name_en, category, tags, current_desc, city_name="Milano"):
    """Generate a rich, guide-style description using Gemini."""
    
    prompt = f"""Sen bir profesyonel seyahat rehberisin. Aşağıdaki yer için Türkçe bir açıklama yaz.

Yer: {place_name} ({name_en})
Şehir: {city_name}
Kategori: {category}
Etiketler: {', '.join(tags) if tags else 'Yok'}
Mevcut kısa açıklama: {current_desc}

KURALLAR:
1. Açıklama 150-250 karakter arasında olmalı (2-3 cümle)
2. Rehber tarzında, samimi ve bilgilendirici ol
3. Tarihi/kültürel bağlam ekle
4. Ziyaretçiye pratik değer kat (ne görecek, ne hissedecek)
5. Abartılı sıfatlardan kaçın, gerçekçi ol
6. Sadece açıklama metnini döndür, başka bir şey ekleme

ÖRNEK ÇIKTI:
"Milano'nun kalbindeki Duomo, gotik mimarisi ve altın Madonnina heykeliyle şehrin en görkemli simgesidir. 600 yılda tamamlanan bu katedralin terasına çıkarak şehrin panoramik manzarasını izleyebilir ve dantel gibi işlenmiş mermer detayları yakından görebilirsiniz."

Şimdi {place_name} için açıklama yaz:"""

    for attempt in range(5):
        try:
            response = model.generate_content(prompt)
            new_desc = response.text.strip().strip('"').strip("'")
            # Remove any markdown or extra formatting
            new_desc = new_desc.replace("**", "").replace("*", "")
            return new_desc
        except Exception as e:
            if "429" in str(e):
                print(f"  ⚠ Rate limit hit, waiting 60s... (Attempt {attempt+1}/5)")
                time.sleep(60)
            else:
                print(f"  ⚠ Gemini error for {place_name}: {e}")
                time.sleep(5)
    return None

def generate_english_description(place_name, turkish_desc):
    """Translate Turkish description to English."""
    
    prompt = f"""Translate this Turkish travel description to English. Keep the same guide-style tone.

Turkish: {turkish_desc}

Just return the English translation, nothing else:"""

    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            return response.text.strip().strip('"').strip("'")
        except Exception as e:
            if "429" in str(e):
                print(f"  ⚠ Rate limit hit (translation), waiting 20s...")
                time.sleep(20)
            else:
                print(f"  ⚠ Translation error: {e}")
                return None
    return None

def enrich_descriptions():
    """Main function to enrich short descriptions."""
    
    print(f"Loading {CITY_FILE}...")
    try:
        with open(CITY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {CITY_FILE} not found.")
        return 0
    
    highlights = data.get('highlights', [])
    short_count = 0
    enriched_count = 0
    
    # Find places with short descriptions
    # Process up to 50 items per run (increased batch size since we have incremental save)
    MAX_BATCH_SIZE = 50
    
    for i, place in enumerate(highlights):
        desc = place.get('description', '')
        
        # Check if description is short OR if it's a generic placeholder
        if len(desc) < MIN_DESCRIPTION_LENGTH:
            short_count += 1
            print(f"\n[{short_count}] {place.get('name', 'Unknown')} - Current: {len(desc)} chars")
            print(f"    Old: {desc[:60]}...")
            
            # Generate rich description
            new_desc = generate_rich_description(
                place_name=place.get('name', ''),
                name_en=place.get('name_en', ''),
                category=place.get('category', ''),
                tags=place.get('tags', []),
                current_desc=desc
            )
            
            if new_desc and len(new_desc) > len(desc):
                # Also generate English version
                new_desc_en = generate_english_description(place.get('name', ''), new_desc)
                
                highlights[i]['description'] = new_desc
                if new_desc_en:
                    highlights[i]['description_en'] = new_desc_en
                
                enriched_count += 1
                print(f"    New: {new_desc[:80]}...")
                print(f"    Length: {len(desc)} → {len(new_desc)} chars ✓")
                
                # Save progress incrementally
                data['highlights'] = highlights
                with open(CITY_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            
            # Rate limiting
            time.sleep(30)
            
            # Process in batches
            if enriched_count >= MAX_BATCH_SIZE:
                print(f"\n--- Batch limit reached: {enriched_count} enriched ---")
                break
    
    # Final Save
    data['highlights'] = highlights
    with open(CITY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Enriched {enriched_count} descriptions in {CITY_FILE}")
    print(f"Remaining short descriptions: {short_count - enriched_count} (approx)")
    return enriched_count

if __name__ == "__main__":
    enrich_descriptions()
