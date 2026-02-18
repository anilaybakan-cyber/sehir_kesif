import os
import json
from difflib import SequenceMatcher

CITIES_DIR = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"

TURKISH_SUFFIXES = [
    "müzesi", "plajı", "sarayı", "kulesi", "camii", "meydanı", 
    "parkı", "caddesi", "kilisesi", "çarşısı", "tepesi", 
    "akvaryum", "şelalesi", "mahallesi", "limanı"
]

ENGLISH_SUFFIXES = [
    "museum", "beach", "palace", "tower", "mosque", "square", 
    "park", "street", "church", "bazaar", "hill", 
    "aquarium", "waterfall", "neighborhood", "port", "castle"
]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def has_turkish_suffix(name):
    lower = name.lower()
    return any(lower.endswith(s) or f" {s} " in f" {lower} " for s in TURKISH_SUFFIXES)

def is_likely_english(name):
    lower = name.lower()
    return any(lower.endswith(s) or f" {s} " in f" {lower} " for s in ENGLISH_SUFFIXES)

def merge_places(p1, p2):
    # Dtermie which is primary (Turkish name preferred for 'name' field)
    p1_is_tr = has_turkish_suffix(p1['name'])
    p2_is_tr = has_turkish_suffix(p2['name'])
    
    primary, secondary = p1, p2
    
    # If p2 is definitely Turkish and p1 is not, swap
    if p2_is_tr and not p1_is_tr:
        primary, secondary = p2, p1
    # If p1 is definitely English and p2 is not, swap (assume p2 might be local)
    elif is_likely_english(p1['name']) and not is_likely_english(p2['name']):
        primary, secondary = p2, p1
        
    print(f"Merging: KEEP '{primary['name']}' ({primary.get('name_en', 'No EN')}) + DROP '{secondary['name']}'")

    # 1. Name_En Logic
    if not primary.get('name_en'):
        # If secondary has name_en, take it
        if secondary.get('name_en'):
            primary['name_en'] = secondary['name_en']
        # If secondary name looks different and not Turkish, use it as EN name (e.g. Barcelona Aquarium)
        elif secondary['name'] != primary['name']:
             primary['name_en'] = secondary['name']

    # 2. Description (Keep longest)
    d1 = primary.get('description', '') or ''
    d2 = secondary.get('description', '') or ''
    if len(d2) > len(d1):
        primary['description'] = d2
        
    d1_en = primary.get('description_en', '') or ''
    d2_en = secondary.get('description_en', '') or ''
    if len(d2_en) > len(d1_en):
        primary['description_en'] = d2_en
        
    # 3. Tags (Merge unique)
    tags = set(primary.get('tags', []))
    tags.update(secondary.get('tags', []))
    primary['tags'] = list(tags)

    # 4. Rating/Review (Take best/max)
    r1 = primary.get('reviewCount', 0) or 0
    r2 = secondary.get('reviewCount', 0) or 0
    if r2 > r1:
        primary['reviewCount'] = r2
        if secondary.get('rating'):
            primary['rating'] = secondary['rating']
            
    # 5. Missing Fields
    for key in ['imageUrl', 'source', 'tips', 'tips_en', 'bestTime', 'price', 'lat', 'lng', 'area', 'category', 'subcategory']:
        if key not in primary and key in secondary:
            primary[key] = secondary[key]

    return primary

def process_city(filename):
    filepath = os.path.join(CITIES_DIR, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        return

    highlights = data.get("highlights", [])
    if not highlights:
        return

    # Find duplicates
    to_remove_indices = set()
    merged_indices = set() # To avoid merging A with B, then B with C separately
    
    # We iterate and find pairs. Modifying list in-place is tricky, 
    # so we will build a new list or mark indices.
    
    # Let's group by "canonical" match
    # Since we need to merge, it's iterative.
    
    new_highlights = []
    skipped_indices = set()
    
    # Use a while loop to handle merges dynamically? 
    # Actually, simpler: Iterate pairs, if match found, merge into the first, mark second as removed.
    
    # To handle transitive merges (A=B, B=C -> A=B=C), we should do multiple passes or careful management.
    # For now, single pass greedy merge is likely sufficient for these duplicates.
    
    for i in range(len(highlights)):
        if i in skipped_indices:
            continue
            
        current = highlights[i]
        
        # Look ahead for duplicates
        for j in range(i + 1, len(highlights)):
            if j in skipped_indices:
                continue
                
            candidate = highlights[j]
            
            name1 = current.get("name", "").strip()
            name2 = candidate.get("name", "").strip()
            name_en1 = current.get("name_en", "").strip()
            name_en2 = candidate.get("name_en", "").strip()
            
            is_match = False
            
            # 1. Exact Name
            if name1.lower() == name2.lower():
                is_match = True
            # 2. Name matches Name_En
            elif name_en1 and name_en1.lower() == name2.lower():
                is_match = True
            elif name_en2 and name_en2.lower() == name1.lower():
                is_match = True
            # 3. Fuzzy match (High confidence)
            elif similar(name1.lower(), name2.lower()) > 0.85:
                is_match = True
                
            if is_match:
                # MERGE i and j into i
                current = merge_places(current, candidate)
                skipped_indices.add(j)
                highlights[i] = current # Update current in list with merged data

    # Rebuild list
    final_list = []
    for i in range(len(highlights)):
        if i not in skipped_indices:
            final_list.append(highlights[i])
            
    if len(final_list) < len(highlights):
        print(f"Reduced {filename} from {len(highlights)} to {len(final_list)} places.")
        data['highlights'] = final_list
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

for filename in sorted(os.listdir(CITIES_DIR)):
    if filename.endswith(".json"):
        process_city(filename)
