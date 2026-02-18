#!/usr/bin/env python3
"""
Unsplash linklerini Firebase Storage linkleriyle değiştiren script.
Tüm curated rotalarındaki Unsplash linklerini bulur ve 
o rotadaki mekanların Firebase Storage linklerini kullanarak değiştirir.
"""

import os
import re
import json
from pathlib import Path

# Paths
DART_FILE = "lib/services/curated_routes_service.dart"
CITIES_DIR = "assets/cities"

def load_all_highlights():
    """Tüm şehirlerdeki mekanları ve imageUrl'lerini yükle."""
    highlights = {}
    cities_path = Path(CITIES_DIR)
    
    for city_file in cities_path.glob("*.json"):
        try:
            with open(city_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                city_name = data.get('city', city_file.stem)
                
                for h in data.get('highlights', []):
                    name = h.get('name', '')
                    image_url = h.get('imageUrl', '')
                    
                    if name and image_url and 'storage.googleapis.com' in image_url:
                        # Hem tam isim hem de normalize edilmiş isimle kaydet
                        highlights[name] = image_url
                        highlights[name.lower()] = image_url
                        
                        # Parantez içi olmadan da kaydet
                        clean_name = re.sub(r'\s*\([^)]*\)', '', name).strip()
                        if clean_name != name:
                            highlights[clean_name] = image_url
                            highlights[clean_name.lower()] = image_url
                            
        except Exception as e:
            print(f"⚠️ Error loading {city_file}: {e}")
    
    print(f"📚 Loaded {len(highlights)} highlights with Firebase Storage URLs")
    return highlights

def find_unsplash_links(content):
    """Dart dosyasındaki tüm Unsplash linklerini bul."""
    # imageUrl: "https://images.unsplash.com/..." pattern
    pattern = r'imageUrl:\s*"(https://images\.unsplash\.com/[^"]+)"'
    matches = re.finditer(pattern, content)
    return [(m.start(), m.end(), m.group(1)) for m in matches]

def find_place_names_for_route(content, unsplash_pos):
    """Belirli bir Unsplash linkinin ait olduğu rotanın placeNames listesini bul."""
    # Geriye doğru git ve CuratedRoute'un başlangıcını bul
    route_start = content.rfind("CuratedRoute(", 0, unsplash_pos)
    if route_start == -1:
        return []
    
    # İleriye doğru git ve placeNames'i bul
    route_end = content.find("),", unsplash_pos)
    if route_end == -1:
        route_end = len(content)
    
    route_section = content[route_start:route_end]
    
    # placeNames listesini çıkar
    place_pattern = r'placeNames:\s*\[(.*?)\]'
    match = re.search(place_pattern, route_section, re.DOTALL)
    
    if match:
        places_str = match.group(1)
        # String listesini parse et
        places = re.findall(r'"([^"]+)"', places_str)
        return places
    
    return []

def find_replacement_url(place_names, highlights):
    """placeNames listesindeki mekanlardan birinin Firebase URL'sini bul."""
    for place in place_names:
        # Tam eşleşme
        if place in highlights:
            return highlights[place]
        
        # Küçük harf eşleşme
        if place.lower() in highlights:
            return highlights[place.lower()]
        
        # Parantez olmadan eşleşme
        clean_place = re.sub(r'\s*\([^)]*\)', '', place).strip()
        if clean_place in highlights:
            return highlights[clean_place]
        if clean_place.lower() in highlights:
            return highlights[clean_place.lower()]
        
        # Kısmi eşleşme (contains)
        for h_name, h_url in highlights.items():
            if isinstance(h_name, str) and isinstance(place, str):
                if place.lower() in h_name.lower() or h_name.lower() in place.lower():
                    return h_url
    
    return None

def main():
    print("🔍 Starting Unsplash link replacement...")
    
    # Mekanları yükle
    highlights = load_all_highlights()
    
    # Dart dosyasını oku
    with open(DART_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Unsplash linklerini bul
    unsplash_links = find_unsplash_links(content)
    print(f"🔗 Found {len(unsplash_links)} Unsplash links to replace")
    
    replaced = 0
    failed = []
    
    # Sondan başa doğru değiştir (pozisyonlar kaymasın diye)
    for start, end, old_url in reversed(unsplash_links):
        place_names = find_place_names_for_route(content, start)
        
        if not place_names:
            failed.append((old_url, "No placeNames found"))
            continue
        
        new_url = find_replacement_url(place_names, highlights)
        
        if new_url:
            # Değiştir
            old_line = f'imageUrl: "{old_url}"'
            new_line = f'imageUrl: "{new_url}"'
            content = content[:start] + content[start:end].replace(old_url, new_url) + content[end:]
            replaced += 1
            print(f"✅ Replaced: {place_names[0] if place_names else 'Unknown'}")
        else:
            failed.append((old_url, f"No Firebase URL found for places: {place_names[:3]}"))
    
    # Dosyayı kaydet
    if replaced > 0:
        with open(DART_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n🎉 Successfully replaced {replaced} Unsplash links!")
    else:
        print("\n❌ No links were replaced.")
    
    if failed:
        print(f"\n⚠️ Failed to replace {len(failed)} links:")
        for url, reason in failed[:10]:  # İlk 10'u göster
            print(f"   - {reason}")

if __name__ == "__main__":
    main()
