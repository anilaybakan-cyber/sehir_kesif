#!/usr/bin/env python3
"""
Tüm şehir JSON dosyalarını tarar ve 'price' alanının String olduğundan emin olur.
Eğer int gelmişse (0-4), String karşılığına ("free", "low"...) çevirir.
"""

import json
from pathlib import Path

CITIES_DIR = Path("assets/cities")

PRICE_MAP = {
    0: "free",
    1: "low",
    2: "medium",
    3: "high",
    4: "expensive"
}

def fix_price(val):
    if isinstance(val, int):
        return PRICE_MAP.get(val, "medium")
    if isinstance(val, str):
        # Zaten string ise dokunma (belki "low" yazıyordur)
        # Ama bazen "3" string olarak gelmiş olabilir
        if val.isdigit():
            return PRICE_MAP.get(int(val), "medium")
        return val
    return "medium"

def process_city(json_path: Path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    highlights = data.get("highlights", [])
    updated_count = 0
    
    for place in highlights:
        old_price = place.get("price")
        # Eğer price int ise veya digit-string ise
        if isinstance(old_price, int) or (isinstance(old_price, str) and old_price.isdigit()):
            new_price = fix_price(old_price)
            if old_price != new_price:
                place["price"] = new_price
                updated_count += 1
                
    if updated_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    print(f"  🔧 {json_path.stem}: {updated_count} price düzeltildi.")
    return updated_count

def main():
    print("💰 FİYAT TİPİ DÜZELTME BAŞLADI...")
    total = 0
    for p in sorted(list(CITIES_DIR.glob("*.json"))):
        total += process_city(p)
    print(f"✅ TOPLAM {total} 'price' alanı düzeltildi.")

if __name__ == "__main__":
    main()
