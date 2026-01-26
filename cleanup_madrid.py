import json
import os
import re

def normalize_name(name):
    name = re.sub(r'\(.*?\)', '', name)
    name = name.lower().strip()
    name = name.replace('museo ', '').replace('museum', '').replace('müzesi', '').replace('müze', '')
    name = name.replace('plaza ', '').replace('meydanı', '').replace('meydan', '')
    name = name.replace('parque ', '').replace('retiro', '').replace('parkı', '').replace('park', '')
    name = name.replace('palacio ', '').replace('sarayı', '').replace('saray', '')
    name = name.replace('mercado ', '').replace('pazarı', '').replace('pazar', '')
    name = name.replace('templo ', '').replace('tapınağı', '').replace('tapınak', '')
    name = name.replace('puerta ', '').replace('kapısı', '').replace('kapı', '')
    return name.strip()

def cleanup_madrid():
    filepath = 'assets/cities/madrid.json'
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

count = cleanup_madrid()
print(f"Madrid cleaned. Final unique count: {count}")
