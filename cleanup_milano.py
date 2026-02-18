import json
import os
import re

def normalize_name(name):
    name = re.sub(r'\(.*?\)', '', name)
    name = name.lower().strip()
    name = name.replace('duomo di ', '').replace('basilica di ', '').replace('chiesa di ', '')
    name = name.replace('pasticceria ', '').replace('pizzeria ', '').replace('bar ', '')
    name = name.replace('museum', '').replace('müzesi', '').replace('müze', '')
    name = name.replace('gallery', '').replace('galleria', '').replace('galeri', '')
    name = name.replace('parkı', '').replace('park', '').replace('parco ', '')
    name = name.replace('district', '').replace('bölgesi', '')
    return name.strip()

def cleanup_milano():
    filepath = 'assets/cities/milano.json'
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    highlights = data.get('highlights', [])
    seen_normalized = {}
    unique_highlights = []

    for h in highlights:
        norm = normalize_name(h['name'])
        if norm not in seen_normalized:
            seen_normalized[norm] = h
            unique_highlights.append(h)
        else:
            existing_h = seen_normalized[norm]
            if len(h['description']) > len(existing_h['description']):
                 idx = unique_highlights.index(existing_h)
                 unique_highlights[idx] = h
                 seen_normalized[norm] = h

    data['highlights'] = unique_highlights

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = cleanup_milano()
print(f"Milan cleaned. Final unique count: {count}")
