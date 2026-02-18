import json
import os

def sanitize_cities():
    city_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    sanitized_count = 0
    highlight_fixed_count = 0
    
    for file in os.listdir(city_dir):
        if file.endswith(".json"):
            path = os.path.join(city_dir, file)
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except:
                    continue
            
            city_coords = data.get("coordinates", {})
            city_lat = city_coords.get("lat")
            city_lng = city_coords.get("lng")
            
            if city_lat is None or city_lng is None:
                # Try to find city center from first highlight that has coords
                for h in data.get("highlights", []):
                    if "lat" in h and "lng" in h:
                        city_lat = h["lat"]
                        city_lng = h["lng"]
                        break
            
            if city_lat is None:
                print(f"⚠️ Skipping {file}: No city center found.")
                continue

            changed = False
            for h in data.get("highlights", []):
                if "lat" not in h or "lng" not in h or (h.get("lat") == 0 and h.get("lng") == 0):
                    h["lat"] = city_lat
                    h["lng"] = city_lng
                    highlight_fixed_count += 1
                    changed = True
            
            if changed:
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                sanitized_count += 1
                print(f"✅ Sanitized {file}")

    print(f"\nSanitized {sanitized_count} files, fixed {highlight_fixed_count} highlights.")

if __name__ == "__main__":
    sanitize_cities()
