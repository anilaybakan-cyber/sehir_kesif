import json
import os
from pathlib import Path

cities_dir = Path("assets/cities")
list_files = ["amsterdam.json", "antalya.json", "atina.json", "bangkok.json", "barcelona.json", 
              "bari_unique_1.json", "bari_unique_2.json", "bari_unique_3.json", "belgrad.json", 
              "berlin.json", "bodrum.json", "bologna.json", "catania_batch_1.json", 
              "catania_batch_2.json", "catania_batch_3.json", "catania_batch_4.json", 
              "catania_batch_5.json", "catania_batch_6.json", "madrid.json"]

for filename in list_files:
    filepath = cities_dir / filename
    if not filepath.exists():
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        print(f"Converting {filename} to dict format...")
        new_data = {
            "name": filename.replace(".json", "").capitalize(),
            "highlights": data
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)
    else:
        print(f"{filename} is already a dict.")
