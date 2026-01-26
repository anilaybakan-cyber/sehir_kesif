import re
import csv
import sys

def parse_dart_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all city blocks: static List<CuratedRoute> _get[City]Routes
    city_pattern = re.compile(r'static List<CuratedRoute> _get(\w+)Routes\(bool isEnglish\) \{(.*?)\}', re.DOTALL)
    
    routes_data = []

    for city_match in city_pattern.finditer(content):
        city_name = city_match.group(1)
        city_block = city_match.group(2)
        
        # Find all CuratedRoute objects inside the block
        # We assume structure: CuratedRoute( ... )
        # We need to be careful with nested parentheses, but typically code is well formatted here.
        # Let's split by 'CuratedRoute(' and process each chunk
        
        chunks = city_block.split('CuratedRoute(')[1:] # Skip first empty chunk
        
        for chunk in chunks:
            # Basic parsing of fields
            
            # Extract Name
            # Pattern 1: name: isEnglish ? "EN" : "TR",
            # Pattern 2: name: "Static",
            name_tr = ""
            name_en = ""
            
            name_ternary = re.search(r'name:\s*isEnglish\s*\?\s*"(.*?)"\s*:\s*"(.*?)"', chunk)
            if name_ternary:
                name_en = name_ternary.group(1)
                name_tr = name_ternary.group(2)
            else:
                name_static = re.search(r'name:\s*"(.*?)"', chunk)
                if name_static:
                    name_en = name_static.group(1)
                    name_tr = name_static.group(1)
            
            # Extract Place Names
            # placeNames: ["A", "B", ...]
            places = []
            places_match = re.search(r'placeNames:\s*\[(.*?)\]', chunk, re.DOTALL)
            if places_match:
                # Remove quotes and split
                raw_places = places_match.group(1)
                # Handle ternary in list? e.g. [isEnglish ? "A" : "B", "C"]
                # This is hard to regex perfectly. 
                # Let's simple split by comma, strip quotes.
                # If there are ternaries, this simple parser might break or return raw code.
                # Looking at file, placeNames are mostly static strings "Name" or "Name (Desc)".
                # Let's just extract string literals.
                
                # Find all "string" literals inside the brackets
                literals = re.findall(r'"(.*?)"', raw_places)
                places = literals
            
            if name_en and name_tr:
                routes_data.append({
                    'city': city_name,
                    'name_tr': name_tr,
                    'name_en': name_en,
                    'places': places
                })

    return routes_data

def generate_csv(routes, output_file):
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # Header
        writer.writerow(['Language', 'City', 'Route Name', 'Stop Count', 'Places'])
        
        for route in routes:
            # TR Row
            places_str = ", ".join(route['places'])
            writer.writerow(['Turkish', route['city'], route['name_tr'], len(route['places']), places_str])
            
            # EN Row
            writer.writerow(['English', route['city'], route['name_en'], len(route['places']), places_str])

if __name__ == "__main__":
    dart_file = 'lib/services/curated_routes_service.dart'
    output_csv = 'curated_routes_export.csv'
    
    try:
        data = parse_dart_file(dart_file)
        generate_csv(data, output_csv)
        print(f"Successfully exported {len(data)*2} rows to {output_csv}")
    except Exception as e:
        print(f"Error: {e}")
