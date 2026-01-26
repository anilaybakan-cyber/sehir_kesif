#!/usr/bin/env python3
"""
Translate Antalya Turkish descriptions to English
"""

import json

# Load antalya.json
with open('assets/cities/antalya.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation dictionary - mapping Turkish phrases to English equivalents
TR_TO_EN = {
    "Antalya'nın": "Antalya's",
    "Türkiye'nin": "Turkey's",
    "İlk": "First",
    "büyük": "large",
    "alışveriş merkezi": "shopping mall",
    "şehir": "city",
    "merkez": "center",
    "sahil": "beach/coast",
    "deniz": "sea",
    "manzara": "view",
    "restoran": "restaurant",
    "kafe": "cafe",
    "tarihi": "historic",
    "antik": "ancient",
    "müze": "museum",
    "park": "park",
    "liman": "harbor",
    "çarşı": "bazaar/market",
    "sokak": "street",
    "camii": "mosque",
    "kilise": "church",
    "kale": "castle/fortress",
    "köprü": "bridge",
    "meydan": "square",
    "bahçe": "garden",
    "orman": "forest",
    "dağ": "mountain",
    "göl": "lake",
    "şelale": "waterfall",
    "plaj": "beach",
    "koy": "bay/cove",
    "ada": "island",
    "yarımada": "peninsula",
    "teleferik": "cable car",
    "teras": "terrace",
    "çatı": "rooftop",
    "yerel": "local",
    "mutfak": "cuisine",
    "lezzet": "flavor",
    "taze": "fresh",
    "organik": "organic",
    "geleneksel": "traditional",
    "modern": "modern",
    "lüks": "luxury",
    "huzur": "peaceful",
    "sakin": "calm",
    "canlı": "lively",
    "popüler": "popular",
    "ünlü": "famous",
    "gizli": "hidden",
    "benzersiz": "unique",
    "muhteşem": "magnificent",
    "büyüleyici": "enchanting",
    "romantik": "romantic",
    "nostaljik": "nostalgic",
}

def translate_tr_to_en(tr_text):
    """
    Create a proper English translation from Turkish text.
    This is a simplified translation - uses context and keywords.
    """
    if not tr_text:
        return ""
    
    # Common patterns and their English equivalents
    en_text = tr_text
    
    # Replace common Turkish phrases with English
    replacements = [
        ("Antalya'nın", "Antalya's"),
        ("Türkiye'nin", "Turkey's"),
        ("şehrin", "the city's"),
        ("denize", "to the sea"),
        ("denizi", "sea"),
        ("manzarası", "view"),
        ("tarihi", "historic"),
        ("yüzyıl", "century"),
        ("meşhur", "famous"),
        ("popüler", "popular"),
        ("geleneksel", "traditional"),
        ("modern", "modern"),
        ("lüks", "luxury"),
        ("muhteşem", "magnificent"),
        ("büyüleyici", "enchanting"),
        ("huzurlu", "peaceful"),
        ("sakin", "calm"),
        ("lezzetli", "delicious"),
        ("taze", "fresh"),
        ("yerel", "local"),
        ("organik", "organic"),
        ("benzersiz", "unique"),
        ("en iyi", "the best"),
        ("en güzel", "the most beautiful"),
        ("mutlaka", "definitely must"),
        ("görülmesi gereken", "must-see"),
        ("deneyimlenmesi gereken", "must-experience"),
    ]
    
    # This is a placeholder - for production, use Google Translate API
    # For now, return the Turkish text to be translated externally
    return en_text

# Get all entries that need translation
entries_to_translate = []
for h in data.get('highlights', []):
    name = h.get('name', '')
    tr_desc = h.get('description', '')
    entries_to_translate.append({
        'name': name,
        'tr': tr_desc
    })

# Save for external translation
with open('antalya_to_translate.json', 'w', encoding='utf-8') as f:
    json.dump(entries_to_translate, f, ensure_ascii=False, indent=2)

print(f"✅ {len(entries_to_translate)} giriş çeviri için hazırlandı")
print("📁 antalya_to_translate.json dosyasına kaydedildi")
