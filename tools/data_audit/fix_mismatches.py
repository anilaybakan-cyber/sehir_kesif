import json
import os
import requests
import time
from pathlib import Path

# API key'i .env dosyasından al
ENV_FILE = Path("../../.env")
if ENV_FILE.exists():
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("GEMINI_API_KEY"):
            _, _, v = line.partition("=")
            API_KEY = v.strip().strip("\"'")
            break
else:
    API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY bulunamadı")
    exit(1)

# Mismatch raporunu oku
with open('mismatch_report.json', 'r', encoding='utf-8') as f:
    mismatches = json.load(f)

# Şehir dosyalarını yükle
city_files = {}
cities_dir = '../../assets/cities'
for filename in os.listdir(cities_dir):
    if filename.endswith('.json') and 'batch' not in filename.lower() and 'unique' not in filename.lower():
        city_id = filename.replace('.json', '')
        with open(os.path.join(cities_dir, filename), 'r', encoding='utf-8') as f:
            city_files[city_id] = json.load(f)

# Gemini API ile gerçek açıklama oluştur
def generate_description(place_name, category, city_name):
    prompt = f"""Write a complete 15-20 word Turkish description for this place:
- Place: {place_name}
- Category: {category}
- City: {city_name}

CRITICAL REQUIREMENTS:
- Must be exactly 15-20 words
- Must be a complete sentence
- Must describe the place specifically
- Must be in Turkish
- Do NOT use just the city name
- Do NOT use colons or incomplete phrases

Example format: "Madriddeki tarihi Menuda History barı, samimi atmosferi ve ödüllü kokteylleriyle ünlüdür."""

    try:
        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",
            params={"key": API_KEY},
            json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 200
                }
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            description = data['candidates'][0]['content']['parts'][0]['text'].strip()
            # Tırnak işaretlerini temizle
            description = description.replace('"', '').replace("'", "")
            return description
        else:
            print(f"⚠️ API Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"⚠️ Error generating description: {e}")
        return None

# Mismatch düzeltme stratejisi:
# 1. Açıklama yanlışsa - Gemini ile gerçek açıklama oluştur
# 2. Kategori yanlışsa - manuel inceleme
# 3. Bölge/mahalle yanlış tanımlanmış - manuel inceleme

fixed_count = 0
manual_review_count = 0

for i, mismatch in enumerate(mismatches, 1):
    place_id = mismatch['place_id']
    city_id = mismatch['city']
    place_name = mismatch['name']
    category = mismatch['category']
    reason = mismatch['reason']
    
    if city_id not in city_files:
        print(f"⚠️ City not found: {city_id}")
        continue
    
    city_data = city_files[city_id]
    
    # city_data dictionary mi kontrol et
    if not isinstance(city_data, dict):
        print(f"⚠️ Invalid city data format for {city_id}")
        continue
    
    highlights = city_data.get('highlights', [])
    
    # Place'ı bul (name'e göre)
    place = None
    for h in highlights:
        if h.get('name') == place_name:
            place = h
            break
    
    if place is None:
        print(f"⚠️ Place not found: {place_name} in {city_id}")
        continue
    
    # Tüm mismatch vakaları için Gemini'den yeni açıklama oluştur
    print(f"[{i}/{len(mismatches)}] Generating description for {place_name} ({city_id})")
    
    city_name_en = city_data.get('city_en', city_id.capitalize())
    new_description = generate_description(place_name, category, city_name_en)
    
    if new_description:
        place['description'] = new_description
        print(f"   ✅ New description: {new_description}")
        fixed_count += 1
        # Rate limiting
        time.sleep(0.5)
    else:
        print(f"   ❌ Failed to generate description")
        manual_review_count += 1

# Değişiklikleri kaydet
for city_id, city_data in city_files.items():
    if fixed_count > 0 or manual_review_count > 0:
        filename = f"{city_id}.json"
        with open(os.path.join(cities_dir, filename), 'w', encoding='utf-8') as f:
            json.dump(city_data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Summary:")
print(f"   Auto-fixed: {fixed_count} (descriptions generated)")
print(f"   Manual review needed: {manual_review_count}")
