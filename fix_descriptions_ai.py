import json
import os
import requests
import time

# Manual API Key Loading from .env
API_KEY = None
if os.path.exists('.env'):
    with open('.env', 'r') as f:
        for line in f:
            if line.startswith('GEMINI_API_KEY='):
                API_KEY = line.split('=')[1].strip()
                break

if not API_KEY:
    print("HATA: .env dosyasında GEMINI_API_KEY bulunamadı!")
    exit(1)

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def call_gemini(prompt):
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2}
    }
    try:
        response = requests.post(GEMINI_API_URL, json=payload)
        data = response.json()
        if 'candidates' in data:
            return data['candidates'][0]['content']['parts'][0]['text'].strip()
        else:
            print("Beklenmeyen yanıt:", data)
            if "error" in data and data["error"].get("code") == 429:
                print("Rate limit aşıldı, 30 saniye bekleniyor...", flush=True)
                time.sleep(30)
            return None
    except Exception as e:
        print("API Hatası:", e, flush=True)
        return None

def fix_city_data(city_file):
    with open(city_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not isinstance(data, dict):
        print(f"⚠️ {os.path.basename(city_file)} atlanıyor: Beklenen JSON formatında değil (dict değil).", flush=True)
        return
        
    highlights = data.get('highlights', [])
    city_name = data.get('name', 'Şehir')
    city_filename = os.path.basename(city_file)
    
    print(f"\n[{city_filename}] Toplam {len(highlights)} mekan kontrol edilecek ({city_name})...", flush=True)
    
    mismatches_fixed = 0
    
    for i, place in enumerate(highlights):
        name = place.get('name')
        desc = place.get('description', '')
        category = place.get('category', '')
        
        # 1. Aşama: Uyuşmazlık Tespiti
        check_prompt = f"""
Sen bir turizm rehberisin. {city_name} şehrindeki "{name}" (Kategori: {category}) adlı mekanın açıklaması aşağıda verilmiştir:
"{desc}"

Bu açıklama bu mekana ait değilse (Örneğin bir kafe için tarihi eser/katedral açıklaması varsa, veya tamamen alakasızsa) sadece "YANLIŞ" yaz.
Eğer açıklama mekana uygunsa sadece "DOĞRU" yaz. Başka hiçbir şey yazma.
"""
        result = None
        while result is None:
            result = call_gemini(check_prompt)
            if result is None:
                time.sleep(5) # Retry delay
                
        if result and "YANLIŞ" in result.upper():
            print(f"  [{i+1}/{len(highlights)}] UYUŞMAZLIK BULUNDU: {name}", flush=True)
            
            # 2. Aşama: Gerçek İçerik Üretimi
            gen_prompt = f"""
Sen profesyonel bir turizm yazarı ve yerel bir rehbersin. {city_name} şehrinde bulunan "{name}" (Kategori: {category}) adlı mekan için 
tamamen GERÇEK, kanıtlanmış ve cezbedici bir açıklama yazmalısın. Hallucinate yapma.

Format olarak SADECE aşağıdaki gibi geçerli bir JSON dönmelisin (başka metin ekleme, markdown kodu kullanma):
{{
  "description": "Türkçe açıklama (maks 160 karakter, tarihi ve gerçek bilgi içermeli)",
  "description_en": "İngilizce çevirisi",
  "tips": "Mekanla ilgili kısa ve gerçekçi bir ipucu (örn: En iyi x'i burada yenir, veya şu saatte gidin)",
  "tips_en": "İpucu İngilizce çevirisi",
  "category": "Doğru kategori (SADECE şunlardan biri olmalı: Yeme-İçme, Kafe, Müze, Park, Bar, Tarihi, Manzara, Deneyim, Alışveriş, Plaj)"
}}
"""
            new_data_str = None
            while new_data_str is None:
                new_data_str = call_gemini(gen_prompt)
                if new_data_str is None:
                    time.sleep(5)
            
            try:
                # Markdown kalıntıları varsa temizle
                new_data_str = new_data_str.replace("```json", "").replace("```", "").strip()
                new_data = json.loads(new_data_str)
                
                place['description'] = new_data['description']
                place['description_en'] = new_data['description_en']
                place['tips'] = new_data['tips']
                place['tips_en'] = new_data['tips_en']
                place['category'] = new_data['category']
                
                print(f"  -> DÜZELTİLDİ: {place['description']}", flush=True)
                mismatches_fixed += 1
            except Exception as e:
                print(f"  -> JSON ayrıştırma hatası: {e}", flush=True)
            
            # API Rate limit'e takılmamak için kısa bekleme
            time.sleep(2)
        else:
            pass #print(f"[{i+1}/{len(highlights)}] {name} - OK", flush=True)
            
        # Her 20 mekanda bir kaydet
        if i % 20 == 0:
            with open(city_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

    # Son kaydetme
    with open(city_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"[{city_filename}] İşlem tamamlandı! Toplam {mismatches_fixed} hatalı içerik GERÇEK bilgilerle düzeltildi.", flush=True)


if __name__ == "__main__":
    cities_dir = "assets/cities"
    files = [f for f in os.listdir(cities_dir) if f.endswith(".json")]
    print(f"🚀 Toplam {len(files)} şehir taranacak...", flush=True)
    
    for filename in files:
        try:
            fix_city_data(os.path.join(cities_dir, filename))
        except Exception as e:
            print(f"❌ {filename} işlenirken KRİTİK HATA oluştu, bu şehir atlanıyor: {e}", flush=True)
            continue
            
    print("\n✅ TÜM ŞEHİRLER TARANDI!", flush=True)

