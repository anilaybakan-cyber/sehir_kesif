import json
import os
import re

def normalize_name(name):
    name = re.sub(r'\(.*?\)', '', name)
    name = name.lower().strip()
    name = name.replace('basilica di', '').replace('basilica', '')
    name = name.replace('piazza della', '').replace('piazza', '')
    name = name.replace('museo nazionale del', '').replace('museo', '')
    name = name.replace('galleria degli', '').replace('galleria', '')
    name = name.replace('köprüsü', 'bridge').replace('bridge', '')
    name = name.replace('meydanı', 'square').replace('square', '')
    name = name.replace('katedrali', 'cathedral').replace('cathedral', '')
    name = name.replace('sarayı', 'palace').replace('palace', '')
    name = name.replace('bahçeleri', 'gardens').replace('gardens', '')
    return name.strip()

def cleanup_floransa():
    filepath = 'assets/cities/floransa.json'
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

count = cleanup_floransa()
print(f"Floransa cleaned. Final unique count: {count}")
