
import json
import os

file_path = 'assets/cities/amsterdam.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if "highlights" in data:
        initial_count = len(data["highlights"])
        
        # Remove the card with specific exact name "Red Light Secrets" 
        # (The original is "Red Light Secrets (Fuhuş Müzesi)")
        data["highlights"] = [h for h in data["highlights"] if h.get("name") != "Red Light Secrets"]
        
        final_count = len(data["highlights"])
        removed_count = initial_count - final_count
        
        print(f"Removed {removed_count} duplicate cards.")
        
        if removed_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print("Successfully updated JSON.")
        else:
            print("No duplicates found to remove.")
            
except Exception as e:
    print(f"Error: {e}")
