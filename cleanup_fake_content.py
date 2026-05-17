#!/usr/bin/env python3
"""
Sahte/Placeholder içerikleri (örn: 'London Spot') ve 
geçerli fotoğrafı olmayan mekanları JSON dosyalarından temizleyen script.
"""

import json
import os
from pathlib import Path

# Klasör yolu
CITIES_DIR = Path("assets/cities")

# Silinecek jenerik terimler (küçük harf)
FAKE_TERMS = [
    "london spot", "paris spot", "berlin spot", "city spot",
    "unknown place", "test place", "sample place",
    "lorem ipsum", "spot 1", "spot 2", "spot 3"
]

def is_fake(name: str) -> bool:
    """İsmin sahte/placeholder olup olmadığını kontrol et."""
    name_lower = name.lower()
    for term in FAKE_TERMS:
        if term in name_lower:
            return True
    
    # "Spot X" formatı kontrolü (regex yerine basit kontrol)
    if "spot" in name_lower and any(c.isdigit() for c in name_lower):
        return True
        
    return False

def has_valid_image(image_url: str) -> bool:
    """Fotoğraf URL'inin geçerli olup olmadığını kontrol et."""
    if not image_url:
        return False
    if image_url == "":
        return False
    # Hala Unsplash ise (Google/Wiki bulunamadıysa) sil
    if "unsplash" in image_url.lower():
        return False
    return True

def process_city(json_path: Path) -> int:
    """Bir şehir dosyasını temizle."""
    
    city_name = json_path.stem.upper()
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        highlights = data
        is_list_root = True
    else:
        highlights = data.get("highlights", [])
        is_list_root = False
    
    original_count = len(highlights)
    
    # Filtreleme
    valid_places = []
    removed_places = []
    
    for place in highlights:
        name = place.get("name", "Unknown")
        image_url = place.get("imageUrl", "")
        
        # 1. Fake isim kontrolü
        if is_fake(name):
            removed_places.append(f"{name} (Fake Name)")
            continue
            
        # 2. Fotoğraf kontrolü (opsiyonel: eğer fotoğrafsız kalsın istemiyorsak)
        # Kullanıcı "fake" lere kızdı, fotoğrafsızlara değil ama 
        # Unsplash olanları da bulamadıysak silelim demiştik.
        if not has_valid_image(image_url):
            removed_places.append(f"{name} (No Image/Unsplash)")
            continue
            
        valid_places.append(place)
    
    # Sadece değişiklik varsa kaydet
    if len(valid_places) < original_count:
        if is_list_root:
            data = valid_places
        else:
            data["highlights"] = valid_places
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"\n📍 {city_name}: {original_count} -> {len(valid_places)} mekan")
        for removed in removed_places:
            print(f"  ❌ Silindi: {removed}")
        
        return len(removed_places)
    
    return 0

def main():
    print("=" * 60)
    print("🧹 SAHTE İÇERİK TEMİZLİĞİ")
    print("=" * 60)
    
    json_files = list(CITIES_DIR.glob("*.json"))
    total_removed = 0
    
    for json_path in sorted(json_files):
        removed = process_city(json_path)
        total_removed += removed
    
    print("\n" + "=" * 60)
    print(f"✅ TAMAMLANDI: Toplam {total_removed} sahte/bozuk mekan silindi.")
    print("=" * 60)

if __name__ == "__main__":
    main()
