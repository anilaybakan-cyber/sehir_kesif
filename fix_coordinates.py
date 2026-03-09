import json
import os
import glob

def fix_coordinate(val, is_lat):
    if val == 0:
        return 0.0
    
    abs_val = abs(val)
    limit = 90.0 if is_lat else 180.0
    
    # If it's already a valid coordinate, return as is
    if abs_val <= limit:
        return float(val)
    
    # Otherwise, it's missing a decimal point. 
    # Example: 52521.0 -> 52.521 (divide by 10 until it's under the limit)
    current_val = float(val)
    while abs(current_val) > limit:
        current_val /= 10.0
        
    # We might need to handle cases where it was e.g. 525.21 etc
    # But essentially division by 10 will shift the decimal point to the correct place
    return round(current_val, 6)

def main():
    files = glob.glob("ota_data_pack/cities/*.json")
    total_fixed = 0
    
    for f in files:
        try:
            with open(f, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            
            fixed_count = 0
            for h in data.get("highlights", []):
                old_lat = h.get("lat", 0.0)
                old_lng = h.get("lng", 0.0)
                
                new_lat = fix_coordinate(old_lat, True)
                new_lng = fix_coordinate(old_lng, False)
                
                if old_lat != new_lat or old_lng != new_lng:
                    h["lat"] = new_lat
                    h["lng"] = new_lng
                    fixed_count += 1
            
            if fixed_count > 0:
                # Save the fixed file
                with open(f, "w", encoding="utf-8") as fh:
                    json.dump(data, fh, ensure_ascii=False, indent=2)
                print(f"Fixed {fixed_count} coordinates in {os.path.basename(f)}")
                total_fixed += fixed_count
                
        except Exception as e:
            print(f"Error processing {f}: {e}")
            
    print(f"\nSuccessfully fixed {total_fixed} broken coordinates across all cities!")

if __name__ == "__main__":
    main()
