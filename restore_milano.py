#!/usr/bin/env python3
"""
Yanlışlıkla tüm fotoğrafları değiştirilen Milano dosyasını düzelten script.
Galleria hariç diğerlerini Google Places API'den çeker.
"""

import json
import requests
import time
from pathlib import Path
from typing import Optional

# Google Places API Key
API_KEY = "AIzaSyCMEuzJpyZtG-LPG-8DFiNrSn2-KfKrQp0"
CITY_FILE = Path("assets/cities/milano.json")

USER_GALLERIA_URL = "https://www.lombardia.info/wp-content/uploads/sites/112/milano-galleria-vittorio-emanuele-ii.jpg"

def get_google_photo(place_name: str) -> Optional[str]:
    """Google Places API kullanarak mekan fotoğrafı al."""
    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": f"{place_name} Milano",
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
                photo_ref = candidate["photos"][0]["photo_reference"]
                return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={photo_ref}&key={API_KEY}"
    except Exception as e:
        print(f"  ❌ Hata ({place_name}): {e}")
    return None

def main():
    print("🚑 Milano Fotoğraf Kurtarma Operasyonu...")
    
    with open(CITY_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    highlights = data.get("highlights", [])
    updated_count = 0
    
    for place in highlights:
        name = place.get("name", "")
        
        # Galleria için özel URL
        if name == "Galleria Vittorio Emanuele II":
            print(f"  ⭐ Galleria fotoğrafı kullanıcı isteğiyle güncelleniyor...")
            place["imageUrl"] = USER_GALLERIA_URL
            updated_count += 1
            continue
            
        # Diğerleri için Google Places
        print(f"  🔄 Onarılıyor: {name}...")
        new_url = get_google_photo(name)
        
        if new_url:
            place["imageUrl"] = new_url
            updated_count += 1
            # print(f"    ✅ OK")
        else:
            print(f"    ⚠️ Fotoğraf bulunamadı!")
            
        time.sleep(0.1) # Rate limiting
        
    # Kaydet
    with open(CITY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✅ Operasyon Tamamlandı: {updated_count} mekan güncellendi.")

if __name__ == "__main__":
    main()
