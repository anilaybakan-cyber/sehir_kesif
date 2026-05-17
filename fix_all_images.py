#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()
"""
Tüm şehir JSON dosyalarındaki eksik veya Unsplash fotoğraflarını
Google Places API ile güncelleyen script.
"""

import json
import os
import time
import requests
from pathlib import Path

# Google Places API Key
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Klasör yolu
CITIES_DIR = Path("assets/cities")

from typing import Optional

def get_google_photo(place_name: str, city_name: str) -> Optional[str]:
    """Google Places API kullanarak mekan fotoğrafı al."""
    
    # 1. Place ID bul
    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": f"{place_name} {city_name}",
        "inputtype": "textquery",
        "fields": "place_id,photos",
        "key": API_KEY
    }
    
    try:
        resp = requests.get(search_url, params=params, timeout=10)
        data = resp.json()
        
        if data.get("status") != "OK" or not data.get("candidates"):
            print(f"  ⚠️ Bulunamadı: {place_name}")
            return None
        
        candidate = data["candidates"][0]
        
        # Fotoğraf varsa
        if "photos" in candidate and candidate["photos"]:
            photo_ref = candidate["photos"][0].get("photo_reference")
            if photo_ref:
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={photo_ref}&key={API_KEY}"
                return photo_url
        
        # Fotoğraf yoksa Place Details dene
        place_id = candidate.get("place_id")
        if place_id:
            details_url = "https://maps.googleapis.com/maps/api/place/details/json"
            details_params = {
                "place_id": place_id,
                "fields": "photos",
                "key": API_KEY
            }
            details_resp = requests.get(details_url, params=details_params, timeout=10)
            details_data = details_resp.json()
            
            if details_data.get("status") == "OK" and details_data.get("result", {}).get("photos"):
                photo_ref = details_data["result"]["photos"][0].get("photo_reference")
                if photo_ref:
                    photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={photo_ref}&key={API_KEY}"
                    return photo_url
        
        print(f"  ⚠️ Fotoğraf yok: {place_name}")
        return None
        
    except Exception as e:
        print(f"  ❌ Hata: {place_name} - {e}")
        return None


def needs_update(image_url: Optional[str]) -> bool:
    """Fotoğrafın güncellenmesi gerekip gerekmediğini kontrol et."""
    if not image_url:
        return True
    if "unsplash" in image_url.lower():
        return True
    if image_url.strip() == "":
        return True
    return False


def process_city(json_path: Path) -> int:
    """Bir şehir dosyasını işle ve güncellenen mekan sayısını döndür."""
    
    city_name = json_path.stem  # Dosya adından şehir ismi
    print(f"\n📍 {city_name.upper()} işleniyor...")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated_count = 0
    highlights = data.get("highlights", [])
    
    for i, place in enumerate(highlights):
        image_url = place.get("imageUrl")
        place_name = place.get("name", "Unknown")
        
        if needs_update(image_url):
            print(f"  🔄 [{i+1}/{len(highlights)}] {place_name}...")
            
            new_url = get_google_photo(place_name, city_name)
            if new_url:
                place["imageUrl"] = new_url
                updated_count += 1
                print(f"  ✅ Güncellendi: {place_name}")
            
            # Rate limiting
            time.sleep(0.1)
    
    # Dosyayı kaydet
    if updated_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  💾 {updated_count} mekan güncellendi ve kaydedildi.")
    else:
        print(f"  ✓ Güncelleme gerekmiyor.")
    
    return updated_count


def main():
    """Ana fonksiyon."""
    print("=" * 60)
    print("🖼️  FOTOĞRAF GÜNCELLEME SCRIPTİ")
    print("=" * 60)
    
    # Önce hangi dosyalarda sorun var kontrol et
    json_files = list(CITIES_DIR.glob("*.json"))
    print(f"\n📂 Toplam {len(json_files)} şehir dosyası bulundu.")
    
    # Sorunlu dosyaları bul
    files_to_process = []
    for json_path in sorted(json_files):
        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "unsplash" in content.lower() or '""' in content or "null" in content:
            files_to_process.append(json_path)
    
    print(f"🔧 {len(files_to_process)} dosyada güncelleme gerekiyor.")
    
    total_updated = 0
    for json_path in files_to_process:
        updated = process_city(json_path)
        total_updated += updated
    
    print("\n" + "=" * 60)
    print(f"✅ TAMAMLANDI: Toplam {total_updated} mekan güncellendi.")
    print("=" * 60)


if __name__ == "__main__":
    main()
