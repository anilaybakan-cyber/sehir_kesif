import json
import os

ASSETS_DIR = 'assets/cities'

def main():
    report = {}
    files = [f for f in os.listdir(ASSETS_DIR) if f.endswith('.json')]
    
    for filename in sorted(files):
        city_name = filename.replace('.json', '')
        path = os.path.join(ASSETS_DIR, filename)
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            places = []
            if 'highlights' in data:
                for h in data['highlights']:
                    places.append(f"{h.get('name', '???')} | {h.get('nameEn', '???')}")
            
            report[city_name] = sorted(places)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    # Print in a readable format
    for city, places in report.items():
        print(f"--- {city.upper()} ---")
        for p in places:
            print(f"  {p}")
        print("")

if __name__ == "__main__":
    main()
