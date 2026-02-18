import json
import os

def cleanup_kopenhag():
    filepath = 'assets/cities/kopenhag.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    seen_names = set()
    unique_highlights = []
    
    for h in data.get('highlights', []):
        name = h['name'].lower().strip()
        # Normalization
        if "nyhavn" in name: name = "nyhavn"
        if "tivoli" in name: name = "tivoli gardens"
        if "christiania" in name: name = "christiania"
        if "little mermaid" in name or "deniz kızı" in name: name = "little mermaid"
        if "strøget" in name: name = "strøget"
        if "torvehallerne" in name: name = "torvehallerne"
        if "rosenborg" in name: name = "rosenborg castle"
        if "christianshavn" in name and "church" not in name: name = "christianshavn"
        if "our saviour" in name or "frelsers" in name: name = "church of our saviour"
        if "kastellet" in name: name = "kastellet"
        if "designmuseum" in name: name = "designmuseum danmark"
        if "amalienborg" in name: name = "amalienborg palace"
        if "reffen" in name or "street food" in name: name = "reffen street food"
        if "nørrebro" in name: name = "nørrebro"
        if "glyptotek" in name: name = "ny carlsberg glyptotek"
        if "rundetårn" in name or "round tower" in name: name = "rundetårn"
        if "aamanns" in name: name = "aamanns 1921"
        if "louisiana" in name: name = "louisiana museum"
        if "mikkeller" in name: name = "mikkeller bar"
        if "copenhill" in name or "amager bakke" in name: name = "copenhill"
        if "botanical garden" in name or "botanisk have" in name: name = "botanical garden"
        if "superkilen" in name: name = "superkilen"
        if "meatpacking" in name or "kødbyen" in name: name = "meatpacking district"
        if "smk" in name or "statens museum" in name: name = "smk"
        if "black diamond" in name or "royal library" in name or "kraliyet kütüphanesi" in name: name = "the black diamond"
        if "grundtvig" in name: name = "grundtvig's church"
        if "cisternerne" in name: name = "cisternerne"
        if "blå planet" in name or "aquarium" in name: name = "den blå planet"
        if "bakken" in name: name = "bakken"
        if "kronborg" in name: name = "kronborg castle"
        if "malmö" in name: name = "malmö"
        if "frederiksborg" in name: name = "frederiksborg castle"
        if "marmorkirken" in name or "marble church" in name: name = "marmorkirken"
        if "børsen" in name or "stock exchange" in name: name = "børsen"
        
        if name not in seen_names:
            seen_names.add(name)
            unique_highlights.append(h)
    
    data['highlights'] = unique_highlights
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = cleanup_kopenhag()
print(f"Kopenhag now has {count} cleaned unique highlights.")
