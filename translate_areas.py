
import os
import json
import glob
import re

# Configuration
CITIES_DIR = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'

def translate_area(area, city_name):
    # Paris/Lyon specific: "1. Bölge" -> "1st Arr."
    if city_name.lower() in ['paris', 'lyon']:
        match = re.match(r'(\d+)\.\s*Bölge', area)
        if match:
            num = int(match.group(1))
            suffix = 'th'
            if num == 1: suffix = 'st'
            elif num == 2: suffix = 'nd'
            elif num == 3: suffix = 'rd'
            return f"{num}{suffix} Arr."
    
    # General "Bölge" -> "District" / "Zone"
    # "Sanayi Bölgesi" -> "Industrial District"
    if "Sanayi Bölgesi" in area:
        return area.replace("Sanayi Bölgesi", "Industrial District")
    
    # "X Bölgesi" -> "X District"
    if "Bölgesi" in area:
        return area.replace("Bölgesi", " District")
        
    # "X. Bölge" (Generic fallback) -> "District X"
    match = re.match(r'(\d+)\.\s*Bölge', area)
    if match:
        return f"District {match.group(1)}"
        
    # "X Bölge" -> "X District"
    if "Bölge" in area:
        return area.replace("Bölge", "District")
        
    return area # Return original if no translation found (or maybe simpler to keep same if proper name)

def process_files():
    print(f"Scanning directory: {CITIES_DIR}")
    json_files = glob.glob(os.path.join(CITIES_DIR, '*.json'))
    
    total_updates = 0
    files_changed = 0

    for file_path in sorted(json_files):
        if file_path.endswith('.tmp') or file_path.endswith('.DS_Store'):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            
            modified = False
            
            for place in highlights:
                area = place.get('area', '')
                area_en = place.get('area_en', '')
                
                # Check if area needs translation and area_en is missing or same as Turkish
                if area and ("Bölge" in area):
                    if not area_en or area_en == area:
                        new_area_en = translate_area(area, city_name)
                        if new_area_en != area:
                            place['area_en'] = new_area_en
                            print(f"[{city_name}] Added area_en: '{area}' -> '{new_area_en}' ({place.get('name')})")
                            modified = True
                            total_updates += 1
            
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                files_changed += 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\n✅ Area Translation Completed")
    print(f"Files Changed: {files_changed}")
    print(f"Total Updates: {total_updates}")

if __name__ == "__main__":
    process_files()
