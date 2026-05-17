#!/usr/bin/env python3
"""
Reads lib/services/city_blog_content.dart, finds unstructured guides (TR/EN),
and uses Gemini 2.5 Flash to generate highly detailed, structured guides.
Updates the dart file automatically.
"""

import os
import re
import sys
import json
import time
import requests

if os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                os.environ["GEMINI_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
                break

GEMINI_KEY = os.environ.get("GEMINI_KEY", "")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
DART_FILE = "lib/services/city_blog_content.dart"
CACHE_FILE = "scratch/guide_cache.json"

PROMPT_TR = """Sen profesyonel bir seyahat yazarı ve rehbersin. Verilen eski rehber metnini, aşağıda belirtilen KESİN formata uygun olarak baştan yazacaksın. Eğer eski metinde bazı alt başlıklar için yeterli bilgi yoksa, kendi seyahat veritabanını ve bilgisini kullanarak bu bölümleri detaylandırıp tamamla. Metin son derece akıcı, detaylı, lokal tavsiyeler içeren "dergi/blog" kalitesinde olmalı. Yorum, yıldız puanı gibi şeylerden asla bahsetme.

HEDEF ŞEHİR/LOKASYON: {city_name}
DİL: Türkçe

FORMAT: (Kesinlikle aşağıdaki Markdown yapısını kullan, başlıkları aynen koru. H1 başlık '# [Şehir Adı]: [Güzel bir slogan]' şeklinde başlasın)

# [Şehir Adı]: [Şehir için çekici bir slogan]

**Hızlı Bakış:** [Şehrin genel ruhunu ve hissini anlatan, okuyucuyu içine çeken 1-2 paragraflık bir giriş. Eski metindeki genel bilgileri kullan.]

**📝 Gitmeden Önce Bilmenizde Fayda Var:**
- **Vize ve Sınırlar:** [bilgi]
- **Priz ve Enerji:** [bilgi]
- **Nakit Paraya Elveda / Nakit Gerekli:** [bilgi]
- **Hava Durumu ve Giyim:** [bilgi]

## 📅 Takviminizi Ayarlayın: Hangi Mevsim Sizin?
[Şehrin 4 mevsimi hakkında detaylı bilgi, her mevsimde neler yapılır, kalabalık durumu vb. Alt alta bullet point ile 4 mevsimi listele]

## 🏠Nerede Kalmalı: Mahalle Rehberi
[Şehirdeki 4-5 farklı mahallenin/bölgenin karakteristiği. Aileler, gençler, bohemler veya bütçe dostu vs. olarak sınıflandırıp liste yapın.]

## 🚲 A Noktasından B Noktasına: Bir Lokal Gibi Hareket Edin
[Havalimanından merkeze ulaşım, metro/otobüs detayları, ulaşım kartları, taksi/uber durumu ve lokal ulaşım tüyoları.]

## 🏛️ Şehrin Hafızası: Görülmesi Gereken İkonik Duraklar
[Şehrin en ikonik 8-10 yerini detaylıca listele. Turistik yerlere dair küçük püf noktaları (hangi saatte gidilmeli, biletler vb.) ekle.]

## 🍴 Şehrin Lezzet Haritası: Lokal Lezzetler
[Şehrin en ünlü yerel yemekleri, sokak lezzetleri, kahve kültürü vb. En az 6-8 yemek ve deneyim.]

## 🤫 Şehrin Fısıldadıkları: Lokal Sırlar
[Turistlerin pek bilmediği, lokallerin takıldığı gizli bahçeler, ilginç mimari noktalar, efsaneler veya az bilinen kafeler. 6-8 adet gizli sır.]

## ✅ Mutlaka Yapmadan Dönme: [Şehir Adı] Checklist
[Seyahati özetleyen, hap niteliğinde en az 10 maddelik "yapılacaklar" listesi.]

---
ESKİ REHBER METNİ (Buradaki spesifik bilgileri korumaya özen göster, yetersizse kendi bilginle tamamla):
{old_text}
"""

PROMPT_EN = """You are a professional travel writer and guide. Rewrite the provided old guide text into the STRICT format specified below. If the old text lacks sufficient information for some subsections, use your own travel database and knowledge to expand and complete those sections. The text must be highly fluent, detailed, and of "magazine/blog" quality with local tips. Never mention ratings, stars, or review counts.

TARGET CITY/LOCATION: {city_name}
LANGUAGE: English

FORMAT: (Use exactly the following Markdown structure, keep the headings exactly as shown. Start with H1 as '# [City Name]: [Catchy slogan]')

# [City Name]: [A catchy slogan for the city]

**Quick Glimpse:** [A 1-2 paragraph introduction capturing the city's general spirit and vibe, drawing the reader in.]

**📝 Good to Know Before You Go:**
- **Visa and Borders:** [info]
- **Plugs and Power:** [info]
- **Cash or Card:** [info]
- **Weather and Clothing:** [info]

## 📅 Timing is Everything: Which Season is Yours?
[Detailed info on the 4 seasons, what to do in each, crowd levels, etc. Use bullet points for the 4 seasons]

## 🏠 Where to Stay: Neighborhood Guide
[Characteristics of 4-5 different neighborhoods/areas. Categorize them for families, youth, bohemians, budget, etc. with bullet points.]

## 🚲 Getting from A to B: Move Like a Local
[Transport from airport to center, metro/bus details, transport cards, taxi/uber situation, and local transport tips.]

## 🏛️ The City's Memory: Iconic Landmarks Must-See
[Detailed list of the top 8-10 iconic places. Add small tips (best time to go, tickets, etc.).]

## 🍴 A Taste of the City: Local Flavors
[The city's most famous local dishes, street food, coffee culture, etc. At least 6-8 dishes and experiences.]

## 🤫 Whispers of the City: Local Secrets
[Hidden gardens, interesting architectural spots, legends, or lesser-known cafes that tourists rarely know but locals frequent. 6-8 hidden secrets.]

## ✅ The [City Name] Checklist: Don't Leave Without Doing These
[A bite-sized, bulleted checklist of at least 10 "must-dos" summarizing the trip.]

---
OLD GUIDE TEXT (Make sure to preserve specific info from here, expand with your knowledge if insufficient):
{old_text}
"""

def call_gemini(prompt: str) -> str:
    try:
        r = requests.post(
            f"{GEMINI_URL}?key={GEMINI_KEY}",
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.4,
                    "maxOutputTokens": 6000,
                },
            },
            timeout=120,
        )
        data = r.json()
        if "candidates" not in data:
            print("ERROR from Gemini:", data)
            return ""
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print("EXCEPTION from Gemini:", e)
        return ""

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def main():
    if not GEMINI_KEY:
        print("HATA: GEMINI_KEY env variable is required.")
        sys.exit(1)

    with open(DART_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all var blocks
    # static const _cityTR = '''...''';
    pattern = re.compile(r"(static const _(\w+?)(TR|EN) = ''')(.*?)(''';)", re.DOTALL)
    matches = pattern.findall(content)

    cache = load_cache()
    
    modified_content = content
    
    # Pre-flight check to see how many need processing
    needs_processing = []
    for match in matches:
        prefix, city_base, lang, old_text, suffix = match
        var_name = f"{city_base}{lang}"
        is_tr = (lang == 'TR')
        
        # Check if already processed
        if "Hızlı Bakış:" in old_text or "Quick Glimpse:" in old_text:
            continue
            
        needs_processing.append((match, var_name, is_tr, old_text))
        
    print(f"Total targets to rewrite: {len(needs_processing)}")

    for i, item in enumerate(needs_processing, 1):
        match, var_name, is_tr, old_text = item
        city_name = match[1]
        
        if var_name in cache:
            new_text = cache[var_name]
            print(f"[{i}/{len(needs_processing)}] {var_name} (loaded from cache)")
        else:
            print(f"[{i}/{len(needs_processing)}] Generating {var_name}...")
            prompt = PROMPT_TR.format(city_name=city_name, old_text=old_text) if is_tr else PROMPT_EN.format(city_name=city_name, old_text=old_text)
            
            new_text = call_gemini(prompt)
            if not new_text:
                print(f"  Failed to generate {var_name}")
                continue
                
            cache[var_name] = new_text
            save_cache(cache)
            time.sleep(4.5) # respect rate limit

        # Escape any $ signs in the generated text as it's for a Dart string
        new_text_escaped = new_text.replace('$', '\\$')
        
        # Replace in content
        full_old_block = "".join(match)
        full_new_block = f"{match[0]}\n{new_text_escaped}\n{match[4]}"
        
        modified_content = modified_content.replace(full_old_block, full_new_block)

    # Save dart file
    with open(DART_FILE, 'w', encoding='utf-8') as f:
        f.write(modified_content)

    print("\nDONE! Updated dart file.")

if __name__ == "__main__":
    main()
