import json
import os
from pathlib import Path

CITIES_DIR = Path("assets/cities")
GENERIC_PATTERNS = [
    "top spot", "worth visiting", "must-see", "great choice", "perfect for your trip",
    "definitely worth", "mutlaka görmeniz gereken", "harika bir yer", "is a top spot",
    "top spot in", "great for holidays"
]

def is_generic_or_short(desc, lang="en"):
    if not desc: return True
    desc_lower = desc.lower()
    for p in GENERIC_PATTERNS:
        if p in desc_lower:
            return True
    
    words = desc.split()
    if len(words) < 20:
        return True
    return False

def audit():
    results = {}
    for json_file in CITIES_DIR.glob("*.json"):
        # Skip batch/temp files
        if "_" in json_file.stem and json_file.stem not in ['saint_tropez', 'san_sebastian']:
            continue
            
        with open(json_file, "r") as f:
            try:
                data = json.load(f)
            except:
                continue
            
        dirty_venues = []
        for h in data.get("highlights", []):
            name = h.get("name", "Unknown")
            desc_tr = h.get("description", "")
            desc_en = h.get("description_en", "")
            
            needs_update = False
            reasons = []
            
            if is_generic_or_short(desc_tr, "tr"):
                needs_update = True
                reasons.append("TR generic or short")
            if is_generic_or_short(desc_en, "en"):
                needs_update = True
                reasons.append("EN generic or short")
                
            if needs_update:
                dirty_venues.append({
                    "id": h.get("id"),
                    "name": name,
                    "reasons": reasons,
                    "desc_tr": desc_tr,
                    "desc_en": desc_en
                })
        
        if dirty_venues:
            results[json_file.name] = dirty_venues
            
    with open("audit_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    total_dirty = sum(len(v) for v in results.values())
    print(f"Audit Complete. Found {total_dirty} dirty venues in {len(results)} cities.")

if __name__ == "__main__":
    audit()
