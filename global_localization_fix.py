import json
import os
from pathlib import Path

CITIES_DIR = Path("assets/cities")

# Translation mappings
TR_TO_EN = {
    " Kalesi": " Castle",
    " Sarayı": " Palace",
    " Müzesi": " Museum",
    " Camii": " Mosque",
    " Köprüsü": " Bridge",
    " Meydanı": " Square",
    " Çarşısı": " Bazaar",
    " Çarşı": " Bazaar",
    " Plajı": " Beach",
    " Koyu": " Bay",
    " Kilisesi": " Church",
    " Tiyatrosu": " Theater",
    " Limanı": " Harbor",
    " Sokağı": " Street",
    " Caddesi": " Street",
    " Parkı": " Park",
    " Bahçesi": " Garden",
    " Şelalesi": " Waterfall",
    " Mağarası": " Cave",
    " Adası": " Island",
    " Tepesi": " Hill",
    " Vadisi": " Valley",
    " Kütüphanesi": " Library",
    " Üniversitesi": " University",
    " Hastanesi": " Hospital",
    " İş Merkezi": " Business Center",
    " Havalimanı": " Airport",
    " İstasyonu": " Station",
    " Otogarı": " Bus Station",
    " Feribot İskelesi": " Ferry Pier",
}

IT_TO_EN = {
    "Castello ": "Castle ",
    "Palazzo ": "Palace ",
    "Basilica di ": "Basilica of ",
    "Cattedrale di ": "Cathedral of ",
    "Chiesa di ": "Church of ",
    "Chiesa della ": "Church of ",
    "Piazza ": "Square ",
    "Ponte ": "Bridge ",
    "Museo ": "Museum ",
    "Teatro ": "Theater ",
    "Porto ": "Port ",
    "Giardino ": "Garden ",
    "Fontana ": "Fountain ",
    "Galleria ": "Gallery ",
    "Duomo di ": "Cathedral of ",
}

FR_TO_EN = {
    "Château de ": "Castle of ",
    "Château ": "Castle ",
    "Palais ": "Palace ",
    "Cathédrale ": "Cathedral ",
    "Basilique ": "Basilica ",
    "Église ": "Church ",
    "Place ": "Square ",
    "Pont ": "Bridge ",
    "Musée ": "Museum ",
    "Théâtre ": "Theater ",
    "Port ": "Harbor ",
    "Jardin ": "Garden ",
    "Fontaine ": "Fountain ",
    "Galerie ": "Gallery ",
    "Avenue ": "Avenue ",
    "Boulevard ": "Boulevard ",
    "Rue ": "Street ",
}

def translate_text(text):
    if not text or not isinstance(text, str): return text
    new_text = text
    # Apply Turkish mappings (suffixes mostly)
    for k, v in TR_TO_EN.items():
        if k in new_text:
            new_text = new_text.replace(k, v)
    # Apply Italian & French (prefixes mostly)
    all_prefixes = {**IT_TO_EN, **FR_TO_EN}
    for k, v in all_prefixes.items():
        if new_text.startswith(k):
            new_text = v + new_text[len(k):]
        elif " " + k in new_text:
             new_text = new_text.replace(" " + k, " " + v)
            
    return new_text

def process_city(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"⚠️ Error loading {file_path.name}: {e}")
            return 0
    
    if not isinstance(data, dict):
        return 0
        
    updates = 0
    
    # Check top level city/country
    city_val = data.get("city")
    if city_val and isinstance(city_val, str):
        if "city_en" not in data or data["city_en"] == city_val:
            new_city_en = translate_text(city_val)
            if new_city_en != city_val:
                data["city_en"] = new_city_en
                updates += 1
            
    # Check highlights
    for h in data.get("highlights", []):
        if not isinstance(h, dict): continue
        name = h.get("name", "")
        name_en = h.get("name_en", "")
        
        # If name_en is missing or same as name but name contains keywords
        if not name_en or name_en == name:
            suggested_en = translate_text(name)
            if suggested_en != name:
                h["name_en"] = suggested_en
                updates += 1
        else:
            # Check if name_en was a copy but still has Turkish artifacts
            suggested_en = translate_text(name_en)
            if suggested_en != name_en:
                h["name_en"] = suggested_en
                updates += 1
                
    if updates > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    return updates

def main():
    total_files = 0
    total_updates = 0
    for json_file in sorted(CITIES_DIR.glob("*.json")):
        try:
            u = process_city(json_file)
            if u > 0:
                total_files += 1
                total_updates += u
                print(f"✅ Updated {json_file.name}: {u} changes")
        except Exception as e:
            print(f"❌ Failed to process {json_file.name}: {e}")
            
    print(f"\n🚀 Global Translation Complete!")
    print(f"Files Modified: {total_files}")
    print(f"Total Names Updated: {total_updates}")

if __name__ == "__main__":
    main()
