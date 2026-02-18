import os
import json
import math
from difflib import SequenceMatcher

CITIES_DIR = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"

def get_distance(lat1, lon1, lat2, lon2):
    if lat1 is None or lon1 is None or lat2 is None or lon2 is None:
        return float('inf')
    R = 6371e3 # Earth radius in meters
    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi / 180
    delta_phi = (lat2 - lat1) * math.pi / 180
    delta_lambda = (lon2 - lon1) * math.pi / 180
    
    a = math.sin(delta_phi/2) * math.sin(delta_phi/2) + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    return R * c

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

report = "# Potential Duplicate Places Report\n\n"

for filename in sorted(os.listdir(CITIES_DIR)):
    if not filename.endswith(".json"):
        continue
    
    filepath = os.path.join(CITIES_DIR, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        continue
        
    city_name = data.get("city", filename)
    highlights = data.get("highlights", [])
    
    duplicates = []
    
    # Compare every pair
    for i in range(len(highlights)):
        for j in range(i + 1, len(highlights)):
            p1 = highlights[i]
            p2 = highlights[j]
            
            name1 = p1.get("name", "").strip()
            name2 = p2.get("name", "").strip()
            name_en1 = p1.get("name_en", "").strip()
            name_en2 = p2.get("name_en", "").strip()
            
            # 1. Exact Name/Name_en Match
            match_type = ""
            if name1.lower() == name2.lower():
                match_type = "Exact Name Match"
            elif name_en1 and name_en1.lower() == name_en2.lower():
                match_type = "Exact English Name Match"
            elif name_en1 and name_en1.lower() == name2.lower():
                 match_type = "Name_En matches Name"
            elif name_en2 and name_en2.lower() == name1.lower():
                 match_type = "Name matches Name_En"
            
            # 2. Coordinate Match (< 20m)
            dist = get_distance(p1.get("lat"), p1.get("lng"), p2.get("lat"), p2.get("lng"))
            if dist < 50: # 50 meters tolerance
                 if match_type:
                     match_type += " + Coordinates Match"
                 else:
                     match_type = f"Coordinates Match ({int(dist)}m)"

            # 3. Fuzzy Name Match
            if not match_type:
                sim_ratio = similar(name1.lower(), name2.lower())
                if sim_ratio > 0.85:
                    match_type = f"Fuzzy Name Match ({sim_ratio:.2f})"
            
            if match_type:
                duplicates.append({
                    "p1": name1,
                    "p2": name2,
                    "reason": match_type,
                    "file": filename
                })

    if duplicates:
        report += f"## {city_name} ({filename})\n"
        for d in duplicates:
            report += f"- **{d['p1']}** vs **{d['p2']}**\n  - Reason: {d['reason']}\n"
        report += "\n"

print(report)
with open("duplicate_report.md", "w", encoding="utf-8") as f:
    f.write(report)
