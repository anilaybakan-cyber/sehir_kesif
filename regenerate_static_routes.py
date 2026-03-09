import os
import json
import re
import asyncio
import aiohttp
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY") or os.environ.get("GOOGLE_DIRECTIONS_API_KEY") or os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    print("WARNING: GOOGLE_MAPS_API_KEY not found in .env")

# 1. Parse curated routes
DART_FILE = "lib/services/curated_routes_service.dart"
with open(DART_FILE, "r", encoding="utf-8") as f:
    dart_content = f.read()

# Regex to find id: "something", ... placeNames: ["A", "B", ...]
route_pattern = re.compile(r'id:\s*["\']([^"\']+)["\'].*?placeNames:\s*\[(.*?)\]', re.DOTALL)
matches = route_pattern.findall(dart_content)

routes_to_places = {}
for route_id, places_str in matches:
    places = [p.strip().strip('"').strip("'") for p in places_str.split(',') if p.strip()]
    routes_to_places[route_id] = places

print(f"Loaded {len(routes_to_places)} hardcoded routes from Dart file.")

# 2. Parse all city JSONs to get coordinates
CITIES_DIR = "assets/cities"
place_coords = {} # name (lowercase) -> {"lat": X, "lng": Y}

for filename in os.listdir(CITIES_DIR):
    if not filename.endswith(".json"):
        continue
    with open(os.path.join(CITIES_DIR, filename), "r", encoding="utf-8") as f:
        try:
            city_data = json.load(f)
            for hl in city_data.get("highlights", []):
                name = hl.get("name", "").lower().strip()
                name_en = hl.get("name_en", "").lower().strip()
                
                # Check multiple possible keys
                lat = hl.get("lat") or hl.get("latitude")
                lng = hl.get("lng") or hl.get("longitude")
                
                if lat is not None and lng is not None:
                    # Handle scaled coordinates (e.g., 41034.0 -> 41.034)
                    if abs(lat) > 1000: lat /= 1000.0
                    if abs(lng) > 1000: lng /= 1000.0
                    
                    coord = {"lat": lat, "lng": lng}
                    if name: place_coords[name] = coord
                    if name_en: place_coords[name_en] = coord
        except Exception as e:
            print(f"Error reading {filename}: {e}")

# 3. Scan assets/routes to see exactly which files need regeneration
ROUTES_DIR = "assets/routes"
files_to_regenerate = []

for filename in os.listdir(ROUTES_DIR):
    if not filename.endswith(".json"):
        continue
    # e.g. ist_historic_walking.json -> routeId=ist_historic, mode=walking
    # Be careful, some routeIds have underscores. e.g. ist_historic.
    # The mode is the LAST split part before .json
    base = filename.replace(".json", "")
    parts = base.split("_")
    mode = parts[-1]
    route_id = "_".join(parts[:-1])
    
    if route_id in routes_to_places:
        files_to_regenerate.append({
            "filename": filename,
            "route_id": route_id,
            "mode": mode,
            "place_names": routes_to_places[route_id]
        })
    else:
        # print(f"Warning: {filename} uses unknown routeId {route_id}")
        pass

print(f"Found {len(files_to_regenerate)} JSON files to regenerate based on valid route definitions.")

async def fetch_directions(session, origin, destination, waypoints, mode):
    # Mimic Dart logic:
    # optimize:true for non-transit, and proper URLs
    base_url = "https://maps.googleapis.com/maps/api/directions/json"
    
    params = {
        "origin": f"{origin['lat']},{origin['lng']}",
        "destination": f"{destination['lat']},{destination['lng']}",
        "mode": mode,
        "key": API_KEY,
        "alternatives": "false"
    }

    if mode == "transit":
        params["departure_time"] = "now"
    
    if waypoints:
        wp_list = [f"{wp['lat']},{wp['lng']}" for wp in waypoints]
        if mode != "transit":
            wp_str = "optimize:true|" + "|".join(wp_list)
            params["waypoints"] = wp_str

    if mode == "transit" and waypoints:
        # For transit + waypoints, the Dart code chunks it sequentially.
        # But for static routes, we never actually drew transit static maps properly before!
        # wait! Did transit static routes exist with waypoints? Yes!
        # If we just do simple sequential calls and merge them, we recreate what the app does.
        # Let's write the chunking logic for transit!
        all_steps = []
        total_dist = 0
        total_dur = 0
        all_polyline = []
        waypoint_order = list(range(len(waypoints)))
        
        full_path = [origin] + waypoints + [destination]
        
        for i in range(len(full_path)-1):
            o = full_path[i]
            d = full_path[i+1]
            chunk_params = {
                "origin": f"{o['lat']},{o['lng']}",
                "destination": f"{d['lat']},{d['lng']}",
                "mode": "transit",
                "key": API_KEY,
                "alternatives": "false",
                "departure_time": "now"
            }
            async with session.get(base_url, params=chunk_params) as resp:
                data = await resp.json()
                if data.get("status") == "OK":
                    leg = data["routes"][0]["legs"][0]
                    total_dist += leg.get("distance", {}).get("value", 0)
                    total_dur += leg.get("duration", {}).get("value", 0)
                    for step in leg.get("steps", []):
                        step["chunk_origin_index"] = i
                        step["chunk_dest_index"] = i + 1
                        all_steps.append(step)
                        # We don't bother extracting detailed polyline points here because the app just uses the step polylines
                else:
                    return None
        
        # Craft a fake combined response that the Dart parser understands
        # _parseResponse in Dart expects: steps, distance_value, duration_seconds, waypoint_order
        return {
            "routes": [
                {
                    "legs": [
                        {
                            "steps": all_steps,
                            "distance": {"value": total_dist},
                            "duration": {"value": total_dur},
                        }
                    ],
                    "waypoint_order": waypoint_order
                }
            ],
            "status": "OK"
        }
    else:
        # Standard request
        async with session.get(base_url, params=params) as resp:
            return await resp.json()

async def worker(queue, session):
    while True:
        task = await queue.get()
        if task is None:
            break
        
        filename = task["filename"]
        place_names = task["place_names"]
        mode = task["mode"]
        
        # Resolve coords
        coords = []
        missing = []
        for name in place_names:
            c = place_coords.get(name.lower())
            if c:
                coords.append(c)
            else:
                missing.append(name)
        
        if len(coords) < 2:
            print(f"Skipping {filename}: Not enough coordinates. Missing: {missing}")
            queue.task_done()
            continue
            
        origin = coords[0]
        destination = coords[-1]
        waypoints = coords[1:-1]
        
        try:
            data = await fetch_directions(session, origin, destination, waypoints, mode)
            if data and data.get("status") == "OK":
                with open(os.path.join(ROUTES_DIR, filename), "w", encoding="utf-8") as f:
                    json.dump(data, f, separators=(',', ':')) # Minify the output to save space
                print(f"  [OK] {filename}")
            else:
                print(f"  [ERROR] {filename} API response: {data.get('status') if data else 'Unknown'}")
        except Exception as e:
            print(f"  [EXCEPTION] {filename}: {e}")
            
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    for item in files_to_regenerate:
         queue.put_nowait(item)
         
    async with aiohttp.ClientSession() as session:
         workers = [asyncio.create_task(worker(queue, session)) for _ in range(10)] # 10 parallel requests
         await queue.join()
         for _ in range(10):
             queue.put_nowait(None)
         await asyncio.gather(*workers)

if __name__ == "__main__":
    if API_KEY:
        asyncio.run(main())
    else:
        print("Please provide API Key.")
