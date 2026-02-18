#!/usr/bin/env python3
"""
Kafe Kurtarma Scripti.
İsminde Cafe/Coffee/Bakery geçen ama Restoran olarak etiketlenen yerleri Kafe'ye çevirir.
"""

import json
from pathlib import Path

CITIES_DIR = Path("assets/cities")

# Kafe olması gereken anahtar kelimeler (case-insensitive)
CAFE_KEYWORDS = [
    "cafe", "café", "coffee", "kafe", "kahve",
    "bakery", "pastry", "patisserie", "pâtisserie",
    "roastery", "brew", "espresso", "latte",
    "dessert", "gelato", "ice cream", "dondurma",
    "cake", "cupcake", "tatlı", "pastane"
]

def rescue_cafes(json_path: Path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    highlights = data.get("highlights", [])
    fixed = 0
    
    for place in highlights:
        name = place.get("name", "").lower()
        category = place.get("category", "")
        
        # Eğer kategori Restoran ise ve isimde cafe keyword'ü varsa
        if category == "Restoran":
            for kw in CAFE_KEYWORDS:
                if kw in name:
                    place["category"] = "Kafe"
                    fixed += 1
                    print(f"  ☕ {place['name']}: Restoran -> Kafe")
                    break
                    
    if fixed > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    return fixed

def main():
    print("☕ KAFE KURTARMA OPERASYONU")
    total = 0
    for p in sorted(CITIES_DIR.glob("*.json")):
        print(f"\n📍 {p.stem.upper()}")
        total += rescue_cafes(p)
    print(f"\n✅ TOPLAM {total} KAFE KURTARILDI.")

if __name__ == "__main__":
    main()
