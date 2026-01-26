#!/usr/bin/env python3
"""
Google Places API ile photo_reference güncelleyici.
Her mekan için Places Text Search API'ye sorgu atar ve photo_reference alır.
"""

import json
import time
import urllib.request
import urllib.parse
import sys
import os

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

def get_photo_reference(place_name: str, city: str) -> str:
    """Mekan için photo_reference al"""
    query = f"{place_name} {city}"
    encoded_query = urllib.parse.quote(query)
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={encoded_query}&key={API_KEY}"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        if data.get("status") == "OK" and data.get("results"):
            photos = data["results"][0].get("photos", [])
            if photos:
                photo_ref = photos[0].get("photo_reference", "")
                return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={photo_ref}&key={API_KEY}"
    except Exception as e:
        print(f"  ❌ Hata: {e}")
    
    return ""


def update_city_photos(json_path: str):
    """Şehir JSON dosyasındaki tüm mekanların fotoğraflarını güncelle"""
    print(f"\n📍 İşleniyor: {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    city_name = data.get("city_en", data.get("city", ""))
    highlights = data.get("highlights", [])
    updated_count = 0
    
    for i, place in enumerate(highlights):
        place_name = place.get("name", "")
        current_url = place.get("imageUrl", "")
        
        # Zaten Google API URL'si varsa atla
        if "maps.googleapis.com" in current_url:
            print(f"  ✓ [{i+1}/{len(highlights)}] {place_name} - zaten Google API")
            continue
        
        print(f"  🔍 [{i+1}/{len(highlights)}] {place_name}...", end=" ", flush=True)
        
        new_url = get_photo_reference(place_name, city_name)
        
        if new_url:
            place["imageUrl"] = new_url
            updated_count += 1
            print("✅")
        else:
            print("⚠️ bulunamadı")
        
        # Rate limiting - API çok hızlı çağırılmasın
        time.sleep(0.3)
    
    # Dosyayı kaydet
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"  📊 Güncellenen: {updated_count}/{len(highlights)}")
    return updated_count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python3 update_photos.py <sehir1> <sehir2> ...")
        print("Örnek: python3 update_photos.py atina dublin assets/cities/viyana.json")
        sys.exit(1)
    
    cities_dir = os.path.join(os.path.dirname(__file__), '../assets/cities')
    total_updated = 0
    
    for arg in sys.argv[1:]:
        # Eğer tam yol verilmişse kullan, değilse assets/cities altında ara
        if arg.endswith('.json'):
            if os.path.exists(arg):
                json_path = arg
            elif os.path.exists(os.path.join(cities_dir, arg)):
                json_path = os.path.join(cities_dir, arg)
            else:
                json_path = arg # Hata verdirmek için olduğu gibi bırak
        else:
            json_path = os.path.join(cities_dir, f"{arg}.json")
            
        if not os.path.exists(json_path):
            print(f"❌ Dosya bulunamadı: {json_path}")
            continue
            
        total_updated += update_city_photos(json_path)
        
    print(f"\n✅ Tüm şehirler tamamlandı. Toplam {total_updated} fotoğraf güncellendi.")
