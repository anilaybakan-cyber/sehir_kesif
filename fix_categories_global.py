#!/usr/bin/env python3
"""
1. Duomo di Milano fotoğrafını günceller.
2. 'Son Akşam Yemeği' kategorisini 'Restoran'dan 'Müze'ye çevirir.
3. Tüm şehirlerdeki bariz kategori hatalarını (İsminde Museum geçen Restoranlar vb.) tarar ve düzeltir.
"""

import json
from pathlib import Path

# Kullanıcı İstekleri
DUOMO_URL = "https://www.turistafaidate.it/wp-content/uploads/2020/03/duomo-milano-194644012015.jpg"
CITIES_DIR = Path("assets/cities")

# Kategori Düzeltme Kuralları (İsimde geçen kelime -> Hedef Kategori)
# Sadece mevcut kategori bariz yanlışsa uygulanır (örn: Restoran kategorisinde 'Museum' varsa)
FIX_RULES = {
    "museum": "Müze",
    "museo": "Müze",
    "gallery": "Sanat Galerisi",
    "galerie": "Sanat Galerisi",
    "galleria": "Sanat Galerisi", # Galleria Vittorio hariç (alışveriş)
    "cathedral": "Tarihi",
    "church": "Tarihi",
    "basilica": "Tarihi",
    "duomo": "Tarihi",
    "castle": "Tarihi",
    "palace": "Tarihi",
    "park": "Park",
    "garden": "Park",
    "cafe": "Kafe",
    "coffee": "Kafe",
    "kafe": "Kafe",
    "restaurant": "Restoran",
    "osteria": "Restoran",
    "trattoria": "Restoran",
    "bar": "Bar",
    "pub": "Bar"
}

# Restoran/Kafe olmaması gerekenler (Eğer kategori Restoran/Kafe ise ve isimde bunlar varsa -> Müze/Tarihi yap)
NOT_FOOD_KEYWORDS = ["museum", "museo", "gallery", "church", "cathedral", "basilica", "castle", "palace", "tower", "bridge", "park", "garden"]

# Gezilecek Yer olmaması gerekenler (Eğer kategori Müze/Tarihi ise ve isimde bunlar varsa -> Restoran/Kafe yap)
FOOD_KEYWORDS = ["restaurant", "osteria", "trattoria", "cafe", "coffee", "bistro", "bar", "pub", "pizza", "burger"]

def fix_city(json_path: Path):
    city_name = json_path.stem
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    highlights = data.get("highlights", [])
    updated_count = 0
    
    for place in highlights:
        name = place.get("name", "")
        name_lower = name.lower()
        category = place.get("category", "Gezilecek Yer")
        
        # 1. Özel İstekler (Milano)
        if city_name == "milano":
            if name == "Duomo di Milano":
                place["imageUrl"] = DUOMO_URL
                print(f"  ✅ Milano: Duomo fotoğrafı güncellendi.")
                updated_count += 1
                continue
                
            if "Son Akşam Yemeği" in name or "L'Ultima Cena" in name:
                place["category"] = "Müze" # Veya Tarihi
                print(f"  ✅ Milano: '{name}' kategorisi Restoran -> Müze yapıldı!")
                updated_count += 1
                continue

        # 2. Otomatik Kategori Düzeltme
        
        # A) Kategori "Restoran" veya "Kafe" veya "Yeme İçme" ise ama isimde Müze/Park vb geçiyorsa
        if category in ["Restoran", "Kafe", "Yeme İçme", "Bar"]:
            for kw in NOT_FOOD_KEYWORDS:
                if kw in name_lower and "cafe" not in name_lower and "restaurant" not in name_lower: 
                    # Dikkat: "Museum Cafe" olabilir, onu elleme. Ama sadece "British Museum" ise düzelt.
                    # Galleria Vittorio Emanuele II bir AVM (Alışveriş), Müze değil.
                    if name == "Galleria Vittorio Emanuele II":
                        place["category"] = "Alışveriş"
                    else:
                        target = "Müze" if "museum" in kw or "museo" in kw or "gallery" in kw else "Tarihi"
                        if "park" in kw or "garden" in kw: target = "Park"
                        
                        place["category"] = target
                        print(f"  🔧 {city_name}: '{name}' ({category}) -> {target} (Otomatik)")
                        updated_count += 1
                        break
        
        # B) Kategori "Müze", "Tarihi", "Gezilecek Yer" ise ama isimde Cafe/Restoran vb geçiyorsa
        if category in ["Müze", "Tarihi", "Gezilecek Yer", "Anıt", "Park"]:
            for kw in FOOD_KEYWORDS:
                if kw in name_lower:
                    # "Hard Rock Cafe" -> Kafe/Restoran
                    target = "Restoran" if kw in ["restaurant", "osteria", "trattoria", "pizza", "burger"] else "Kafe"
                    if kw in ["bar", "pub"]: target = "Bar"
                    
                    place["category"] = target
                    print(f"  🔧 {city_name}: '{name}' ({category}) -> {target} (Otomatik)")
                    updated_count += 1
                    break
                    
    if updated_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    return updated_count

def main():
    print("🧹 KATEGORİ VE FOTOĞRAF DÜZELTME BAŞLADI")
    print("="*60)
    
    total_fixes = 0
    for json_path in sorted(list(CITIES_DIR.glob("*.json"))):
        total_fixes += fix_city(json_path)
        
    print("="*60)
    print(f"✅ TOPLAM {total_fixes} DÜZELTME YAPILDI.")

if __name__ == "__main__":
    main()
