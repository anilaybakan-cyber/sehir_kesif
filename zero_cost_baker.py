import os
import re
import json
import time
import requests
from pathlib import Path

# Configuration
PROJECT_ROOT = Path("/Users/anilebru/Desktop/Uygulamalar/sehir_kesif")
ROUTES_SERVICE_FILE = PROJECT_ROOT / "lib/services/curated_routes_service.dart"
CITIES_DATA_DIR = PROJECT_ROOT / "assets/cities"
OUTPUT_DIR = PROJECT_ROOT / "assets/routes"
ENV_FILE = PROJECT_ROOT / ".env"

def load_here_api_key():
    """Load HERE API Key from .env file"""
    if not ENV_FILE.exists():
        print("❌ .env file not found!")
        return None
    with open(ENV_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('HERE_API_KEY='):
                return line.split('=')[1].strip()
    return None

def parse_curated_routes():
    """Parse route definitions from Dart service file"""
    print(f"📖 Parsing {ROUTES_SERVICE_FILE.name}...")
    with open(ROUTES_SERVICE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the switch case in getRoutes to map city names to methods
    # Example: case 'istanbul': return _getIstanbulRoutes(isEnglish);
    city_map = {}
    switch_matches = re.finditer(r"case\s+'([^']+)':\s*(?:case\s+'[^']+':\s*)*return\s+(_get\w+Routes)", content)
    for match in switch_matches:
        city_id = match.group(1).lower()
        method_name = match.group(2)
        city_map[method_name] = city_id

    all_routes = []
    # Find all _getCityRoutes methods
    method_blocks = re.finditer(r"static List<CuratedRoute> (_get\w+Routes)\(bool isEnglish\) \{([\s\S]*?)\n  \}", content)
    
    for block in method_blocks:
        method_name = block.group(1)
        body = block.group(2)
        
        city_id = city_map.get(method_name)
        if not city_id:
            # Fallback if not in switch (e.g. generic)
            city_id = method_name.replace('_get', '').replace('Routes', '').lower()

        # Find individual CuratedRoute objects
        route_matches = re.finditer(r'CuratedRoute\([\s\S]*?id:\s*"([^"]+)"[\s\S]*?placeNames:\s*\[([\s\S]*?)\]', body)
        for rm in route_matches:
            route_id = rm.group(1)
            places_raw = rm.group(2)
            # Extract place names
            places = [p.strip().strip('"').strip("'") for p in places_raw.split(',') if p.strip()]
            
            all_routes.append({
                'city_id': city_id,
                'route_id': route_id,
                'places': places
            })

    print(f"✅ Found {len(all_routes)} routes across {len(set(r['city_id'] for r in all_routes))} cities.")
    return all_routes

def resolve_coordinates(city_id, place_names):
    """Load city JSON and resolve coordinates for place names"""
    # Map some mismatching city IDs to file names
    city_file_map = {
        'new york': 'newyork',
        'nyc': 'newyork',
        'hong kong': 'hongkong',
        'san sebastian': 'san_sebastian' # Adjustment based on file list
    }
    
    file_name = city_file_map.get(city_id, city_id)
    json_path = CITIES_DATA_DIR / f"{file_name}.json"
    
    if not json_path.exists():
        # Try some common variations
        for variation in [file_name.replace(' ', ''), file_name.replace(' ', '_'), file_name.replace('_', '')]:
            if (CITIES_DATA_DIR / f"{variation}.json").exists():
                json_path = CITIES_DATA_DIR / f"{variation}.json"
                break
    
    if not json_path.exists():
        print(f"⚠️ City file {file_name}.json not found.")
        return None

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    highlights = data.get('highlights', [])
    coords = []
    
    for name in place_names:
        found = False
        lower_name = name.lower().strip()
        for h in highlights:
            h_name = h.get('name', '').lower().strip()
            h_name_en = h.get('name_en', h.get('nameEn', '')).lower().strip()
            
            if h_name == lower_name or h_name_en == lower_name:
                if 'lat' in h and 'lng' in h:
                    coords.append({'lat': h['lat'], 'lng': h['lng']})
                    found = True
                    break
        
        if not found:
            # Try partial match if exact fails
            for h in highlights:
                h_name = h.get('name', '').lower().strip()
                h_name_en = h.get('name_en', h.get('nameEn', '')).lower().strip()
                if lower_name in h_name or lower_name in h_name_en or h_name in lower_name:
                    if 'lat' in h and 'lng' in h:
                        coords.append({'lat': h['lat'], 'lng': h['lng']})
                        found = True
                        break

        if not found:
            print(f"  ❓ Place '{name}' not found or missing coordinates in {file_name}.json.")
            
    return coords

def fetch_osrm_route(coords):
    """Fetch walking route from OSRM (Zero-Cost)"""
    if len(coords) < 2: return None
    
    coord_str = ";".join([f"{c['lng']},{c['lat']}" for c in coords])
    url = f"http://router.project-osrm.org/route/v1/walking/{coord_str}?overview=full&geometries=polyline&steps=true"
    
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('code') == 'Ok':
                route = data['routes'][0]
                # Map to Google-like structure
                return {
                    "routes": [{
                        "overview_polyline": {"points": route['geometry']},
                        "legs": [{
                            "distance": {"value": route['distance'], "text": f"{route['distance']/1000:.1f} km"},
                            "duration": {"value": route['duration'], "text": f"{int(route['duration']/60)} mins"},
                            "steps": [
                                {
                                    "travel_mode": "WALKING",
                                    "distance": {"value": s['distance']},
                                    "duration": {"value": s['duration']},
                                    "polyline": {"points": s['geometry']},
                                    "html_instructions": s['maneuver']['type'] + " " + (s.get('name', '') or "")
                                }
                                for leg in route['legs'] for s in leg['steps']
                            ]
                        }],
                        "bounds": {"northeast": {"lat": 0, "lng": 0}, "southwest": {"lat": 0, "lng": 0}}
                    }],
                    "status": "OK"
                }
    except Exception as e:
        print(f"  ❌ OSRM Error: {e}")
    return None

def fetch_here_route(coords, api_key):
    """Fetch transit route from HERE Maps (Zero-Cost Tier) leg by leg and merge"""
    if not api_key or len(coords) < 2: return None
    
    all_legs = []
    
    import datetime
    now_iso = datetime.datetime.now().replace(microsecond=0).isoformat()
    
    for i in range(len(coords) - 1):
        origin = coords[i]
        destination = coords[i+1]
        
        # Check if points are identical (HERE 400s on identical points)
        if abs(origin['lat'] - destination['lat']) < 1e-6 and abs(origin['lng'] - destination['lng']) < 1e-6:
            print(f"    ⚠️ Leg {i}->{i+1}: Origin and Destination are identical. Skipping.")
            continue

        # HERE transit requires the 'at' parameter in ISO 8601 format
        url = (f"https://router.hereapi.com/v8/routes?transportMode=publicTransport"
               f"&origin={origin['lat']:.6f},{origin['lng']:.6f}"
               f"&destination={destination['lat']:.6f},{destination['lng']:.6f}"
               f"&at={now_iso}"
               f"&return=polyline,summary,actions,instructions"
               f"&apiKey={api_key}")
        
        try:
            resp = requests.get(url, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                if 'routes' in data and data['routes']:
                    h_route = data['routes'][0]
                    for section in h_route['sections']:
                        all_legs.append({
                            "distance": {"value": section['summary']['length'], "text": f"{section['summary']['length']/1000:.1f} km"},
                            "duration": {"value": section['summary']['duration'], "text": f"{int(section['summary']['duration']/60)} mins"},
                            "steps": [
                                {
                                    "travel_mode": "WALKING" if section['type'] == 'pedestrian' else "TRANSIT",
                                    "distance": {"value": section['summary']['length'] / max(1, len(section.get('actions', [1]))), "text": ""},
                                    "duration": {"value": section['summary']['duration'] / max(1, len(section.get('actions', [1]))), "text": ""},
                                    "polyline": {"points": section['polyline']},
                                    "html_instructions": action.get('instruction', '')
                                }
                                for action in section.get('actions', [])
                            ]
                        })
                else:
                    print(f"    ⚠️ No transit route between stops {i} and {i+1}.")
            else:
                print(f"    ❌ HERE API Error ({resp.status_code}) for leg {i}->{i+1}: {resp.text[:100]}")
        except Exception as e:
            print(f"    ❌ HERE Exception for leg {i}->{i+1}: {e}")
            
        time.sleep(0.2) # Avoid aggressive rate limiting
    
    if not all_legs: return None
    
    return {
        "routes": [{
            "overview_polyline": {"points": all_legs[0]['steps'][0]['polyline'] if all_legs and all_legs[0]['steps'] else ""},
            "legs": all_legs,
            "bounds": {"northeast": {"lat": 0, "lng": 0}, "southwest": {"lat": 0, "lng": 0}}
        }],
        "status": "OK"
    }

def main():
    print("🥯 ZERO-COST ROUTE BAKER 🥯")
    api_key = load_here_api_key()
    if not api_key:
        print("⚠️ HERE_API_KEY not found in .env. Transit baking will be skipped or limited.")
    
    routes = parse_curated_routes()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    success_walking = 0
    success_transit = 0
    
    for i, r in enumerate(routes):
        print(f"[{i+1}/{len(routes)}] {r['route_id']} ({r['city_id']})")
        
        coords = resolve_coordinates(r['city_id'], r['places'])
        if not coords or len(coords) < 2:
            print(f"  ❌ Skipping: Could not resolve enough coordinates.")
            continue
            
        # 1. Walking (OSRM)
        walking_file = OUTPUT_DIR / f"{r['route_id']}_walking.json"
        if not walking_file.exists():
            data = fetch_osrm_route(coords)
            if data:
                with open(walking_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                print(f"  🚶 Walking: Baked ✅")
                success_walking += 1
            else:
                print(f"  🚶 Walking: Failed ❌")
        else:
            print(f"  🚶 Walking: Already exists.")
            
        # 2. Transit (HERE)
        if api_key:
            transit_file = OUTPUT_DIR / f"{r['route_id']}_transit.json"
            if not transit_file.exists():
                data = fetch_here_route(coords, api_key)
                if data:
                    with open(transit_file, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2)
                    print(f"  🚌 Transit: Baked ✅")
                    success_transit += 1
                else:
                    print(f"  🚌 Transit: Failed ❌")
            else:
                print(f"  🚌 Transit: Already exists.")
        
        # Rate limiting preventers
        time.sleep(0.5)

    print("\n" + "="*40)
    print(f"✨ BAKE COMPLETE ✨")
    print(f"🚶 Walking Baked: {success_walking}")
    print(f"🚌 Transit Baked: {success_transit}")
    print("="*40)

if __name__ == "__main__":
    main()
