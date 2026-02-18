#!/usr/bin/env python3
"""
fix_categories_global.py scriptinin yaptığı bazı yanlış otomatikleştirmeleri düzeltir.
Özellikle 'Bar' kelimesini içeren ama Bar olmayan yerleri (Barcelona, Library vb.) geri alır.
"""

import json
from pathlib import Path

CITIES_DIR = Path("assets/cities")

# Manuel Düzeltme Listesi (İsim -> Doğru Kategori)
RESCUE_MAP = {
    "Barceloneta Beach": "Park",
    "Barceloneta Mahallesi": "Semt",
    "Barcelona Zoo": "Park",
    "Barcelona Aquarium": "Müze",
    "L'Aquarium de Barcelona": "Müze",
    "Barbier-Mueller Museum": "Müze",
    "Coffee Museum": "Müze",
    "Temple Bar": "Semt", # Bölge adı
    "Bargello National Museum": "Müze",
    "Museo Nazionale del Bargello (Donatello David)": "Müze",
    "Bardini Garden (Secret View)": "Park",
    "New York Public Library": "Tarihi",
    "Eleven Madison Park": "Restoran", # Park değil restoran
    "Maxim's Palace": "Restoran", # Saray değil restoran
    "Sky Bar (Lebua State Tower)": "Bar", # Tarihi değil bar
    "Dishoom Covent Garden": "Restoran", # Park değil restoran
    "Park Bar": "Bar", # Park değil bar
    "Clouds (Prime Tower)": "Bar", # Tarihi değil bar
    "Giardini Pubblici Indro Montanelli": "Park", # Bar değil
    "Church of Our Saviour": "Tarihi", # Restoran'dan Tarihi'ye (Doğruydu, koru)
    "Basilica di Santa Maria Novella": "Tarihi", # Doğruydu
    "Museo del Novecento": "Müze" # Doğruydu
}

def rescue_city(json_path: Path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    highlights = data.get("highlights", [])
    updated_count = 0
    
    for place in highlights:
        name = place.get("name", "")
        
        # Rescue Map kontrol
        if name in RESCUE_MAP:
            target = RESCUE_MAP[name]
            if place.get("category") != target:
                place["category"] = target
                updated_count += 1
                
        # Özel bir kontrol: Eğer şehir BARCELONA ise ve kategori BAR yapılmışsa, ve isimde 'Barceloneta' falan geçiyorsa -> Geri al
        if json_path.stem == "barcelona" and place.get("category") == "Bar":
            if "Barcelona" in name or "Barceloneta" in name:
                # Eğer gerçekten Bar değilse (bunu anlamak zor ama Barcelona kelimesi yüzünden Bar olduysa)
                # İsimde "Bar " (boşluklu) yoksa muhtemelen hatadır.
                if "Bar " not in name: 
                    # Eski haline döndürmek zor, "Gezilecek Yer" yapalım veya tahmin edelim
                    if "Beach" in name: place["category"] = "Park"
                    elif "Museum" in name or "Aquarium" in name: place["category"] = "Müze"
                    elif "Zoo" in name: place["category"] = "Park"
                    else: place["category"] = "Gezilecek Yer"
                    updated_count += 1

    if updated_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    return updated_count

def main():
    print("🚑 KATEGORİ KURTARMA OPERASYONU...")
    total = 0
    for p in CITIES_DIR.glob("*.json"):
        total += rescue_city(p)
    print(f"✅ {total} hatalı değişiklik düzeltildi.")

if __name__ == "__main__":
    main()
