from dotenv import load_dotenv
load_dotenv()
import os
#!/usr/bin/env python3
"""
Belirli bir mekan için Google Places API'den en iyi fotoğrafı bulup güncelleyen script.
"""

import json
import requests
from pathlib import Path

# Google Places API Key
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Hedef
TARGET_CITY_FILE = Path("assets/cities/milano.json")
TARGET_PLACE_NAME = "Galleria Vittorio Emanuele II"

def update_photo():
    # 1. Fotoğraf URL'i bul
    print(f"🔍 {TARGET_PLACE_NAME} için fotoğraf aranıyor...")
    
    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": f"{TARGET_PLACE_NAME} Milano",
        "inputtype": "textquery",
        "fields": "photos",
        "key": API_KEY
    }
    
    try:
        resp = requests.get(search_url, params=params)
        data = resp.json()
        
        if data.get("status") == "OK" and data.get("candidates"):
            candidate = data["candidates"][0]
            if "photos" in candidate:
                # İlk fotoğrafı değil, biraz daha ileridekini alalım (belki daha iyidir)
                # Genelde ilk fotoğraf en popüler olandır ama API sırası değişkendir.
                # Kullanıcı "harika fotoğrafı olmalı" dediği için en geniş olanı (maxwidth) isteyelim.
                photo_ref = candidate["photos"][0]["photo_reference"]
                
                # Varsa 2. fotoğrafı deneyelim (bazen ilki standart dış cephe oluyor, iç mekan daha etkileyici olabilir)
                if len(candidate["photos"]) > 1:
                    print(f"📸 {len(candidate['photos'])} fotoğraf bulundu. İlkini kullanıyoruz.")
                
                new_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1600&photo_reference={photo_ref}&key={API_KEY}"
                print(f"✅ Yeni URL oluşturuldu.")
                
                # 2. JSON güncelle
                with open(TARGET_CITY_FILE, 'r', encoding='utf-8') as f:
                    city_data = json.load(f)
                
                updated = False
                for place in city_data.get("highlights", []):
                    if place.get("name") == TARGET_PLACE_NAME:
                        place["imageUrl"] = new_url
                        updated = True
                        print("📝 JSON güncellendi.")
                        break
                
                if updated:
                    with open(TARGET_CITY_FILE, 'w', encoding='utf-8') as f:
                        json.dump(city_data, f, ensure_ascii=False, indent=2)
                    print("💾 Dosya kaydedildi.")
                else:
                    print("❌ Mekan JSON içinde bulunamadı.")
            else:
                print("❌ Mekan için fotoğraf bulunamadı.")
        else:
            print(f"❌ API Hatası: {data.get('status')}")
            
    except Exception as e:
        print(f"❌ Hata: {e}")

if __name__ == "__main__":
    update_photo()
