#!/usr/bin/env python3
"""Generic metin güncelleyici — batch dosyalarını okuyup JSON'a uygular."""
import json, os, sys

CITIES_DIR = os.path.dirname(os.path.abspath(__file__))
GENERIC_DESC = 'en sevilen noktalarından biri olan bu mekan, yerel dokuyu hissetmek'
GENERIC_TIPS = 'Kameranızı yanınıza almayı'

def apply_batch(city_file, updates):
    """updates: {index: {'d': tr, 'de': en, 't': tr_tips, 'te': en_tips}}"""
    path = os.path.join(CITIES_DIR, city_file)
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    changed = 0
    for idx, vals in updates.items():
        h = data['highlights'][idx]
        if 'd' in vals: h['description'] = vals['d']
        if 'de' in vals: h['description_en'] = vals['de']
        if 't' in vals: h['tips'] = vals['t']
        if 'te' in vals: h['tips_en'] = vals['te']
        changed += 1
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✓ {city_file}: {changed} mekan güncellendi")

def count_generic(city_file):
    path = os.path.join(CITIES_DIR, city_file)
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    d = sum(1 for h in data['highlights'] if GENERIC_DESC in h.get('description',''))
    t = sum(1 for h in data['highlights'] if GENERIC_TIPS in h.get('tips',''))
    print(f"{city_file}: {d} jenerik desc, {t} jenerik tips kaldı")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        count_generic(sys.argv[1])
