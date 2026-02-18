import json
import os
import re

def normalize_name(name):
    name = re.sub(r'\(.*?\)', '', name)
    name = name.lower().strip()
    name = name.replace('musée ', '').replace('museum', '').replace('müzesi', '').replace('müze', '')
    name = name.replace('palais ', '').replace('sarayı', '').replace('saray', '')
    name = name.replace('vieux lyon', 'old lyon').replace('eski lyon', 'old lyon')
    name = name.replace('cathédrale ', '').replace('katedrali', '').replace('katedral', '')
    name = name.replace('basilique ', '').replace('bazilikası', '').replace('bazilika', '')
    name = name.replace('parc ', '').replace('parkı', '').replace('park', '')
    name = name.replace('place ', '').replace('meydanı', '').replace('meydan', '')
    return name.strip()

def cleanup_lyon():
    filepath = 'assets/cities/lyon.json'
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

count = cleanup_lyon()
print(f"Lyon cleaned. Final unique count: {count}")
