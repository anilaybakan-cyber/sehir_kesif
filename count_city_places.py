
import json
import glob
import os

def count_places():
    assets_dir = 'assets/cities'
    json_files = glob.glob(os.path.join(assets_dir, '*.json'))
    
    city_counts = []
    
    print(f"{'City':<20} | {'Place Count':<10}")
    print("-" * 35)
    
    for json_file in json_files:
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                
            city_name = os.path.splitext(os.path.basename(json_file))[0]
            # Some files might use 'places' instead of 'highlights', check both or just highlights as per previous scripts
            highlights = data.get('highlights', [])
            count = len(highlights)
            
            city_counts.append((city_name, count))
        except Exception as e:
            print(f"Error reading {json_file}: {e}")

    # Sort by count ascending
    city_counts.sort(key=lambda x: x[1])
    
    for city, count in city_counts:
        print(f"{city:<20} | {count:<10}")
        
    print("-" * 35)
    print(f"Total Cities: {len(city_counts)}")

if __name__ == "__main__":
    count_places()
