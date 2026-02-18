import json
import time
import google.generativeai as genai
import os

# Gemini API Configuration
GEMINI_API_KEY = "AIzaSyDL3n3joYZ_MwVj1lbXF2xTBAEMQqYprYA"
genai.configure(api_key=GEMINI_API_KEY)
# Using gemini-pro-latest to avoid flash rate limits if possible
model = genai.GenerativeModel('gemini-pro-latest')

CITY_FILE = "assets/cities/brugge.json"
MIN_DESCRIPTION_LENGTH = 80  # Characters
TARGET_DESCRIPTION_LENGTH = 200  # Target ~200 chars
MAX_BATCH_SIZE = 50

def generate_rich_description(place_name, name_en, category, tags, current_desc, city_name="Brugge"):
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
"Orta Çağ atmosferini iliklerinize kadar hissedeceğiniz bu meydan, şehrin kalbinin attığı yerdir. Tarihi çan kulesinin gölgesinde kahvenizi yudumlarken masalsı bir manzaranın keyfini çıkarabilirsiniz."

Şimdi {place_name} için açıklama yaz:"""

    for attempt in range(5):
        try:
            response = model.generate_content(prompt)
            new_desc = response.text.strip().strip('"').strip("'")
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
    
    prompt = f"""Translate this travel description to English. Keep the same guide-style tone.

Turkish: {turkish_desc}

Just return the English translation, nothing else:"""
    
    for attempt in range(5):
        try:
            response = model.generate_content(prompt)
            return response.text.strip().strip('"').strip("'")
        except Exception as e:
            if "429" in str(e):
                print(f"  ⚠ Trans Rate limit hit, waiting 60s... (Attempt {attempt+1}/5)")
                time.sleep(60)
            else:
                print(f"  ⚠ Translation error: {e}")
                time.sleep(5)
    return None

def enrich_descriptions():
    """Main function to enrich short descriptions."""
    
    print(f"Loading {CITY_FILE}...")
    try:
        with open(CITY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {CITY_FILE} not found.")
        return

    highlights = data.get('highlights', [])
    short_count = 0
    enriched_count = 0
    
    # Calculate initial stats
    total_short = sum(1 for p in highlights if len(p.get('description', '')) < MIN_DESCRIPTION_LENGTH)
    print(f"Found {total_short} descriptions shorter than {MIN_DESCRIPTION_LENGTH} chars.")
    
    for i, place in enumerate(highlights):
        desc = place.get('description', '')
        
        if len(desc) < MIN_DESCRIPTION_LENGTH:
            short_count += 1
            place_name = place.get('name', 'Unknown')
            print(f"\n[{short_count}] {place_name} - Current: {len(desc)} chars")
            print(f"    Old: {desc[:60]}...")
            
            # Generate rich description
            new_desc = generate_rich_description(
                place_name=place_name,
                name_en=place.get('name_en', ''),
                category=place.get('category', ''),
                tags=place.get('tags', []),
                current_desc=desc
            )
            
            if new_desc and len(new_desc) > len(desc):
                # Also generate English version
                new_desc_en = generate_english_description(place_name, new_desc)
                
                highlights[i]['description'] = new_desc
                if new_desc_en:
                    highlights[i]['description_en'] = new_desc_en
                
                enriched_count += 1
                print(f"    New: {new_desc[:80]}...")
                print(f"    Length: {len(desc)} → {len(new_desc)} chars ✓")
                
                # Incremental Save
                data['highlights'] = highlights
                with open(CITY_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            
            # Rate limiting
            time.sleep(10)
            
            # Process in batches
            if enriched_count >= MAX_BATCH_SIZE:
                print(f"\n--- Batch complete: {enriched_count} enriched ---")
                break
    
    print(f"\n✅ Enriched {enriched_count} descriptions in {CITY_FILE}")
    return enriched_count

if __name__ == "__main__":
    enrich_descriptions()
