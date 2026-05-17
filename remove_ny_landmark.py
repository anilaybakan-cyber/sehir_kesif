import json
import os

def remove_landmark(city_file, landmark_name):
    if not os.path.exists(city_file): return
    with open(city_file, 'r') as f:
        data = json.load(f)
    
    changed = False
    highlights = data if isinstance(data, list) else data.get('highlights', [])
    
    # Filter out the landmark
    new_highlights = [h for h in highlights if h.get('name') != landmark_name]
    
    if len(new_highlights) < len(highlights):
        if isinstance(data, list):
            data = new_highlights
        else:
            data['highlights'] = new_highlights
        changed = True
            
    if changed:
        with open(city_file, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Removed {landmark_name} from {city_file}")

remove_landmark('assets/cities/newyork.json', 'Elevated Acre')
