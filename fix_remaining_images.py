#!/usr/bin/env python3
"""
Kalan Unsplash fotoğraflarını Google Custom Search API veya 
Wikipedia'dan çeken script.
"""

import json
import os
import time
import requests
from pathlib import Path
from typing import Optional

# Google Custom Search API (ücretsiz 100 sorgu/gün)
# https://developers.google.com/custom-search/v1/overview
GOOGLE_API_KEY = "AIzaSyCMEuzJpyZtG-LPG-8DFiNrSn2-KfKrQp0"
GOOGLE_CX = "a6b1c2d3e4f5g6h7i"  # Custom Search Engine ID (oluşturulmalı)

# Klasör yolu
CITIES_DIR = Path("assets/cities")


def get_wikipedia_image(place_name: str, city_name: str) -> Optional[str]:
    """Wikipedia'dan mekan fotoğrafı al."""
    
    # Wikipedia API - arama
    search_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": place_name,
        "prop": "pageimages",
        "pithumbsize": 1200
    }
    
    try:
        resp = requests.get(search_url, params=params, timeout=10)
        data = resp.json()
        
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if "thumbnail" in page_data:
                return page_data["thumbnail"]["source"]
        
        # Şehir adıyla birlikte dene
        params["titles"] = f"{place_name}, {city_name}"
        resp = requests.get(search_url, params=params, timeout=10)
        data = resp.json()
        
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if "thumbnail" in page_data:
                return page_data["thumbnail"]["source"]
                
        return None
        
    except Exception as e:
        print(f"  ❌ Wikipedia hatası: {e}")
        return None


def get_wikimedia_commons_image(place_name: str) -> Optional[str]:
    """Wikimedia Commons'tan fotoğraf al."""
    
    search_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": f"{place_name} filetype:bitmap",
        "srnamespace": "6",  # File namespace
        "srlimit": 1
    }
    
    try:
        resp = requests.get(search_url, params=params, timeout=10)
        data = resp.json()
        
        results = data.get("query", {}).get("search", [])
        if not results:
            return None
            
        file_title = results[0]["title"]
        
        # Dosya URL'ini al
        info_params = {
            "action": "query",
            "format": "json",
            "titles": file_title,
            "prop": "imageinfo",
            "iiprop": "url",
            "iiurlwidth": 1200
        }
        
        info_resp = requests.get(search_url, params=info_params, timeout=10)
        info_data = info_resp.json()
        
        pages = info_data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if "imageinfo" in page_data:
                url = page_data["imageinfo"][0].get("thumburl")
                if url:
                    return url
                    
        return None
        
    except Exception as e:
        print(f"  ❌ Wikimedia hatası: {e}")
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
    """Bir şehir dosyasını işle."""
    
    city_name = json_path.stem
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
            
            # 1. Wikipedia dene
            new_url = get_wikipedia_image(place_name, city_name)
            
            # 2. Wikimedia Commons dene
            if not new_url:
                new_url = get_wikimedia_commons_image(place_name)
            
            if new_url:
                place["imageUrl"] = new_url
                updated_count += 1
                print(f"  ✅ Güncellendi: {place_name}")
            else:
                print(f"  ⚠️ Bulunamadı: {place_name}")
            
            time.sleep(0.2)  # Rate limiting
    
    if updated_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  💾 {updated_count} mekan güncellendi.")
    else:
        print(f"  ✓ Güncelleme gerekmiyor.")
    
    return updated_count


def main():
    print("=" * 60)
    print("🖼️  WİKİPEDİA/WİKİMEDİA FOTOĞRAF SCRIPTİ")
    print("=" * 60)
    
    json_files = list(CITIES_DIR.glob("*.json"))
    print(f"\n📂 {len(json_files)} şehir dosyası taranıyor...")
    
    # Unsplash içeren dosyaları bul
    files_to_process = []
    for json_path in sorted(json_files):
        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if "unsplash" in content.lower():
            files_to_process.append(json_path)
    
    print(f"🔧 {len(files_to_process)} dosyada Unsplash URL'si var.")
    
    total_updated = 0
    for json_path in files_to_process:
        updated = process_city(json_path)
        total_updated += updated
    
    print("\n" + "=" * 60)
    print(f"✅ TAMAMLANDI: {total_updated} mekan güncellendi.")
    print("=" * 60)


if __name__ == "__main__":
    main()
