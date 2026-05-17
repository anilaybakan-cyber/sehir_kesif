import json

def find_duplicate_descriptions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    highlights = data.get('highlights', [])
    desc_map = {}
    duplicates = []
    
    for h in highlights:
        desc = h.get('description', '')
        if not desc: continue
        
        if desc in desc_map:
            duplicates.append({
                'name': h.get('name'),
                'duplicate_of': desc_map[desc],
                'description': desc[:50] + "..."
            })
        else:
            desc_map[desc] = h.get('name')
            
    return duplicates

if __name__ == "__main__":
    dupes = find_duplicate_descriptions('/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/istanbul.json')
    if dupes:
        print(f"Found {len(dupes)} duplicate descriptions in Istanbul:")
        for d in dupes:
            print(f"- {d['name']} is a duplicate of {d['duplicate_of']}")
    else:
        print("No duplicate descriptions found in Istanbul.")
