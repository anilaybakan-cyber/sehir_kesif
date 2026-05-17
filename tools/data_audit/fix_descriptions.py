#!/usr/bin/env python3
"""
Faz 3 — Description düzeltme (Gemini 2.5 Flash).

Gemini_verdicts.json'dan mismatch ve wrong_city vakalarını alır,
Gemini ile doğru Türkçe ve İngilizce description üretir,
city JSON dosyalarına uygular (.bak backup ile).
"""

import json
import os
import time
import requests
from pathlib import Path

# .env dosyasını manuel yükle (önce yapmalıyız)
env_file = Path("/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/.env")
if env_file.exists():
    with open(env_file, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()

# Konfigürasyon
CITIES_DIR = Path("/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities")
OUT_DIR = Path("/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/tools/data_audit")
VERDICTS_FILE = OUT_DIR / "gemini_verdicts.json"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

# Rate limiting
RPM = 10
BATCH_SIZE = 5  # Description generation daha ağır, batch küçük tut


def load_verdicts():
    """Gemini verdicts cache'ini yükle."""
    with open(VERDICTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_city_json(city_name):
    """Şehir JSON dosyasını yükle."""
    city_file = CITIES_DIR / f"{city_name}.json"
    with open(city_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Highlights key'i yoksa direkt list
    if isinstance(data, list):
        return data, city_file
    else:
        return data.get("highlights", []), city_file


def get_problematic_places(verdicts):
    """mismatch ve wrong_city vakalarını filtrele."""
    problematic = []
    for place_id, info in verdicts.items():
        if info.get("verdict") in ["mismatch", "wrong_city"]:
            problematic.append({
                "place_id": place_id,
                "name": info["name"],
                "city": info["city"],
                "category": info["category"],
                "verdict": info["verdict"],
                "reason": info["reason"]
            })
    return problematic


def generate_description_batch(places):
    """Gemini ile batch description üret."""
    places_info = []
    for p in places:
        places_info.append(
            f"- ID: {p['place_id']}, İsim: {p['name']}, Şehir: {p['city']}, Kategori: {p['category']}"
        )
    
    prompt = f"""Aşağıdaki mekanlar için doğru Türkçe ve İngilizce açıklama üret.

Her mekan için:
1. Mekanın gerçek doğasını (kategori, şehir) yansıtan kısa ama bilgilendirici bir açıklama yaz.
2. Türkçe ve İngilizce versiyon üret.
3. JSON formatında döndür: {{"place_id": "...", "tr": "...", "en": "..."}}

Mekanlar:
{chr(10).join(places_info)}

Lütfen sadece JSON array döndür, başka açıklama ekleme."""

    try:
        response = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=30
        )
        response.raise_for_status()
        
        result = response.json()
        text = result["candidates"][0]["content"]["parts"][0]["text"]
        
        # Debug: raw response
        print(f"  📝 Raw response preview: {text[:200]}...")
        
        # JSON kısmını extract et
        text = text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
        
        descriptions = json.loads(text)
        print(f"  📝 Parsed {len(descriptions)} descriptions")
        return descriptions
    except json.JSONDecodeError as e:
        print(f"❌ JSON parse error: {e}")
        print(f"  Full response: {text[:500]}...")
        return None
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return None


def apply_fixes(fixes, dry_run=True):
    """Description düzeltmelerini city JSON dosyalarına uygula."""
    # Şehir bazında grupla
    by_city = {}
    for fix in fixes:
        city = fix["city"]
        if city not in by_city:
            by_city[city] = []
        by_city[city].append(fix)
    
    for city, city_fixes in by_city.items():
        print(f"\n📍 Şehir: {city} ({len(city_fixes)} düzeltme)")
        
        highlights, city_file = load_city_json(city)
        
        # Backup oluştur
        if not dry_run:
            backup_file = city_file.with_suffix(".json.bak")
            with open(backup_file, "w", encoding="utf-8") as f:
                json.dump(highlights, f, ensure_ascii=False, indent=2)
            print(f"  💾 Backup: {backup_file}")
        
        # Highlights güncelle
        updated_count = 0
        for fix in city_fixes:
            place_id = fix["place_id"]
            tr_desc = fix["tr"]
            en_desc = fix["en"]
            
            for highlight in highlights:
                if highlight.get("place_id") == place_id:
                    if dry_run:
                        print(f"  [DRY-RUN] {highlight['name']}:")
                        print(f"    TR: {tr_desc[:60]}...")
                        print(f"    EN: {en_desc[:60]}...")
                    else:
                        old_tr = highlight.get("about", "")
                        old_en = highlight.get("about_en", "")
                        highlight["about"] = tr_desc
                        highlight["about_en"] = en_desc
                        print(f"  ✅ {highlight['name']}: güncellendi")
                        print(f"     Eski TR: {old_tr[:40]}...")
                        print(f"     Yeni TR: {tr_desc[:40]}...")
                    updated_count += 1
                    break
        
        # Dosyaya yaz
        if not dry_run and updated_count > 0:
            with open(city_file, "w", encoding="utf-8") as f:
                json.dump(highlights, f, ensure_ascii=False, indent=2)
            print(f"  💾 {city_file} güncellendi ({updated_count} mekan)")


def main():
    print("🔧 Faz 3 — Description düzeltme")
    
    if not GEMINI_API_KEY:
        print("❌ GEMINI_API_KEY bulunamadı (.env dosyasını kontrol et)")
        return
    
    # Verdicts yükle
    verdicts = load_verdicts()
    print(f"📊 {len(verdicts)} verdict yüklendi")
    
    # Problemli yerleri filtrele
    problematic = get_problematic_places(verdicts)
    print(f"⚠️ {len(problematic)} problemli mekan (mismatch + wrong_city)")
    
    if not problematic:
        print("✅ Düzeltilecek mekan yok")
        return
    
    # Dry-run göster
    print("\n🔍 İlk 10 örnek:")
    for p in problematic[:10]:
        print(f"  {p['city']} | {p['name']} | {p['verdict']}")
    
    # Onay al
    response = input(f"\n{len(problematic)} mekan için Gemini'den description üret ve uygula? (yes/no): ")
    if response.lower() != "yes":
        print("❌ İptal edildi")
        return
    
    # Batch bazlı üret
    all_fixes = []
    for i in range(0, len(problematic), BATCH_SIZE):
        batch = problematic[i:i+BATCH_SIZE]
        print(f"\n📝 Batch {i//BATCH_SIZE + 1}/{(len(problematic)-1)//BATCH_SIZE + 1} ({len(batch)} mekan)")
        
        descriptions = generate_description_batch(batch)
        if descriptions:
            for desc in descriptions:
                place_id = desc["place_id"]
                # Orijinal bilgilerle birleştir
                orig = next((p for p in problematic if p["place_id"] == place_id), None)
                if orig:
                    all_fixes.append({
                        "place_id": place_id,
                        "name": orig["name"],
                        "city": orig["city"],
                        "category": orig["category"],
                        "tr": desc["tr"],
                        "en": desc["en"]
                    })
                    print(f"  ✅ {orig['name']}: description üretildi")
                else:
                    print(f"  ⚠️ place_id {place_id} bulunamadı, atlanıyor")
        else:
            print(f"  ❌ Batch başarısız")
        
        # Rate limit
        if i + BATCH_SIZE < len(problematic):
            time.sleep(60 / RPM)
    
    print(f"\n✅ {len(all_fixes)} description üretildi")
    
    # Dry-run göster
    print("\n🔍 Dry-run önizleme:")
    apply_fixes(all_fixes, dry_run=True)
    
    # Onay al ve uygula
    response = input(f"\nDeğişiklikleri uygula? (yes/no): ")
    if response.lower() == "yes":
        apply_fixes(all_fixes, dry_run=False)
        print("\n✅ Tüm değişiklikler uygulandı")
    else:
        print("❌ İptal edildi")


if __name__ == "__main__":
    main()
