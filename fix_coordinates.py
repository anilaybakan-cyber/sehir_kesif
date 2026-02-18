
import json
import os
import glob

cities_dir = 'assets/cities'

def fix_coordinates():
    files = glob.glob(os.path.join(cities_dir, '*.json'))
    
    for file_path in files:
        print(f"Checking {file_path}...")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            modified = False
            
            if "highlights" in data:
                for place in data["highlights"]:
                    lat = place.get("lat")
                    lng = place.get("lng")
                    
                    if lat is not None and isinstance(lat, (int, float)):
                        original_lat = lat
                        # Fix Latitude
                        while abs(lat) > 90:
                            lat /= 1000.0
                        
                        if lat != original_lat:
                            place["lat"] = lat
                            print(f"  Fixed lat for {place.get('name')}: {original_lat} -> {lat}")
                            modified = True
                            
                    if lng is not None and isinstance(lng, (int, float)):
                        original_lng = lng
                        # Fix Longitude
                        while abs(lng) > 180:
                            lng /= 1000.0
                            
                        if lng != original_lng:
                            place["lng"] = lng
                            print(f"  Fixed lng for {place.get('name')}: {original_lng} -> {lng}")
                            modified = True
            
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Saved updates to {file_path}")
            else:
                print("No changes needed.")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    fix_coordinates()
