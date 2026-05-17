import json

def parse_strings(file_path):
    with open(file_path, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    
    # Header is 7 lines
    header = lines[:7]
    data = lines[7:]
    
    entries = []
    for i in range(0, len(data), 7):
        chunk = data[i:i+7]
        if len(chunk) < 7: continue
        
        entry = {
            "city": chunk[0],
            "revize": chunk[1],
            "name": chunk[2],
            "desc_tr": chunk[3],
            "desc_en": chunk[4],
            "tips_tr": chunk[5],
            "tips_en": chunk[6]
        }
        entries.append(entry)
    return entries

entries = parse_strings('revize_strings.txt')
print(f"Total entries: {len(entries)}")

# Group by city
cities = {}
for e in entries:
    c = e['city']
    if c not in cities: cities[c] = []
    cities[c].append(e)

for city, items in cities.items():
    print(f"{city}: {len(items)} items")
