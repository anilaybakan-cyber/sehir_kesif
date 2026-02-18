
import json
import os
import re
import requests
import glob
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Configuration
SERVICE_FILE = "lib/services/curated_routes_service.dart"
CITIES_DIR = "assets/cities"

def parse_param(line):
    # Helper to extract value from key: value lines
    if ':' in line:
        return line.split(':', 1)[1].strip().strip(',').strip('"').strip("'")
    return ""

def extract_routes_from_service():
    """
    Parses curated_routes_service.dart to find:
    City -> [{RouteName, [PlaceNames]}]
    """
    print(f"Reading {SERVICE_FILE}...")
    with open(SERVICE_FILE, 'r') as f:
        lines = f.readlines()

    routes = {}
    current_city = None
    current_route = {}
    in_route = False

    # Regex to find city blocks like: static List<CuratedRoute> _getNewYorkRoutes(bool isEnglish) {
    city_block_regex = re.compile(r'static List<CuratedRoute> _get(\w+)Routes')

    for line in lines:
        line = line.strip()
        
        # Detect City Block
        city_match = city_block_regex.search(line)
        if city_match:
            city_name_raw = city_match.group(1)
            # Normalize camelCase to snake_case or just map known ones
            # For now, let's keep the raw name and map it later
            current_city = city_name_raw
            routes[current_city] = []
            continue

        # Detect Route Start
        if "CuratedRoute(" in line:
            in_route = True
            current_route = {"placeNames": []}
            continue

        # Detect Route Fields
        if in_route:
            if line.startswith("id:"):
                current_route["id"] = parse_param(line)
            elif line.startswith("name:"):
                # Handle ternary (isEnglish ? "A" : "B") -> just take both or simple logic
                # We mainly care about ID/Name for reporting
                current_route["name"] = line  # Raw line for context
            elif line.startswith("placeNames:"):
                # Extract list items
                # Usually: placeNames: ["A", "B", "C"],
                content = line.split("placeNames:", 1)[1].strip()
                # Remove brackets and trailing commas
                content = content.strip("[],")
                # Split by comma but respect quotes
                import csv
                import io
                f = io.StringIO(content)
                reader = csv.reader(f, quotechar='"', skipinitialspace=True)
                places = next(reader, [])
                # Also try single quote and clean up
                places = [p.strip().strip("'").strip('"') for p in places if p]
                current_route["placeNames"] = [p for p in places if p]
            elif line.startswith("),"):
                # End of route
                if current_city and current_route:
                    routes[current_city].append(current_route)
                in_route = False
                current_route = {}

    return routes

def load_city_data():
    """
    Loads all city JSONs into a dict: city_normalized -> {place_name -> place_data}
    """
    city_data = {}
    files = glob.glob(f"{CITIES_DIR}/*.json")
    for f_path in files:
        fname = Path(f_path).stem # e.g. "newyork"
        try:
            with open(f_path, 'r') as f:
                data = json.load(f)
                
            places = {}
            if 'highlights' in data:
                for h in data['highlights']:
                    # Map by name AND English name for robust lookup
                    name = h.get('name', '').strip()
                    name_en = h.get('name_en', '').strip()
                    
                    if name: places[name] = h
                    if name_en: places[name_en] = h # Overwrite is fine, we just need existence
            
            city_data[fname] = places
            # Also map "NewYork" -> "newyork"
            city_data[fname.replace("_", "").lower()] = places
            
        except Exception as e:
            print(f"Error loading {fname}: {e}")
            
    return city_data

def check_url_exists(url):
    try:
        if not url or not url.startswith("http"): return False, "Invalid URL"
        r = requests.head(url, timeout=5)
        return (r.status_code == 200, r.status_code)
    except Exception as e:
        return (False, str(e))

def map_service_city_to_json(service_city):
    # Maps "NewYork" -> "newyork"
    # Maps "Sevilla" -> "sevilla"
    norm = service_city.lower()
    mapping = {
        "newyork": "newyork",
        "istanbul": "istanbul",
        "paris": "paris",
        "london": "londra", # Mismatch!
        "londra": "londra",
        "rome": "roma",
        "roma": "roma",
        "seville": "sevilla",
        "sevilla": "sevilla",
        "barcelona": "barcelona",
        "madrid": "madrid",
        "venice": "venedik",
        "florence": "floransa",
        "athens": "atina",
        "prague": "prag",
        "vienna": "viyana",
        "berlin": "berlin",
        "amsterdam": "amsterdam",
        "tokyo": "tokyo",
        "dubai": "dubai",
        "lisbon": "lizbon",
        "dublin": "dublin",
        "copenhagen": "kopenhag",
        "stockholm": "stockholm",
        "budapest": "budapeste",
        "belgrade": "belgrad",
        "bangkok": "bangkok",
        "hongkong": "hongkong",
        "cappadocia": "kapadokya"
    }
    # Try direct lower, then mapped
    if norm in mapping: return mapping[norm]
    return norm # fallback

def main():
    print("--- VALIDATING ROUTES ---")
    routes_by_city = extract_routes_from_service()
    city_data = load_city_data()
    
    missing_places = []
    missing_images = []
    
    for service_city, routes in routes_by_city.items():
        json_city_key = map_service_city_to_json(service_city)
        
        if json_city_key not in city_data:
            print(f"⚠️ Warning: No JSON found for service city '{service_city}' (Mapped: {json_city_key})")
            continue
            
        places_db = city_data[json_city_key]
        print(f"Checking {service_city} ({len(routes)} routes)...")
        
        for route in routes:
            route_name = route.get('id', 'Unknown')
            for place_name in route.get('placeNames', []):
                # Check Existence
                clean_name = place_name.strip()
                
                # Try finding in DB (exact, then case insensitive)
                found_place = places_db.get(clean_name)
                if not found_place:
                    # Try case insensitive scan
                    for db_name in places_db.keys():
                        if db_name.lower() == clean_name.lower():
                            found_place = places_db[db_name]
                            break
                            
                if not found_place:
                    missing_places.append(f"[{service_city}] Route '{route_name}': Place '{clean_name}' NOT FOUND in JSON.")
                    continue
                
                # Check Image
                img_url = found_place.get('imageUrl')
                if not img_url or "http" not in img_url:
                     missing_images.append(f"[{service_city}] Place '{clean_name}': NO IMAGE URL.")
                # We skip HEAD check for speed unless requested, or we can do it for a sample
                
    print("\n--- REPORT ---")
    if missing_places:
        print(f"❌ FOUND {len(missing_places)} MISSING PLACES IN JSON:")
        for m in missing_places: print(m)
    else:
        print("✅ All route places exist in JSON.")
        
    if missing_images:
        print(f"\n❌ FOUND {len(missing_images)} PLACES WITH NO IMAGE URL:")
        for m in missing_images: print(m)
    else:
        print("\n✅ All found places have image URLs.")

if __name__ == "__main__":
    main()
