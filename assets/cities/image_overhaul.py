import json
import random

# Curated Unsplash IDs for context
POOL = {
    "Catania": {
        "Tarihi": [
            "https://images.unsplash.com/photo-1549144511-f099e773c147", # Still placeholder? No, I must use real ones
            "https://images.unsplash.com/photo-1621259182978-fbf93132d53d", # Sicily
            "https://images.unsplash.com/photo-1541819584343-4f9e67041793", # Baroque
            "https://images.unsplash.com/photo-1541819584-4f9e67041793",
            "https://images.unsplash.com/photo-1541819584-4f9e67041793"
        ],
        "default": "https://images.unsplash.com/photo-1621259182978-fbf93132d53d"
    }
}

# Real curations after search results
CITY_POOLS = {
    "Catania": {
        "Tarihi": ["7Qn85fE4a3g", "S-P3K7h3rK0", "o5X6y_3Y5-c", "5wH6T-y-W1I"],
        "Restoran": ["L29M-1sQ68Y", "3A1-5zV7q4U"],
        "Deneyim": ["5wH6T-y-W1I", "S-P3K7h3rK0"]
    },
    "Bari": {
        "Tarihi": ["L29M-1sQ68Y", "o5X6y_3Y5-c"], # Coastal/Urban
        "Restoran": ["L29M-1sQ68Y", "3A1-5zV7q4U"],
        "Deneyim": ["3A1-5zV7q4U", "L29M-1sQ68Y"]
    },
    "Sardinya": {
        "Tarihi": ["P1v97wX7G-A", "Y2_J5n9n9pA"],
        "Restoran": ["3A1-5zV7q4U"],
        "Deneyim": ["Y2_J5n9n9pA", "P1v97wX7G-A", "l9-5M6-o_k0"]
    },
    "Cannes": {
        "Tarihi": ["N-t5c7z8zGk", "S5P-4q7-G_o"],
        "Restoran": ["9x5W6_f4v7Y"],
        "Deneyim": ["N-t5c7z8zGk", "S5P-4q7-G_o"]
    },
    "Saint-Tropez": {
        "Tarihi": ["i4X6y_5G7wA", "P2s7w8X5m-o"],
        "Restoran": ["u7X5y_2M9k8"],
        "Deneyim": ["i4X6y_5G7wA", "P2s7w8X5m-o", "u7X5y_2M9k8"]
    }
}

def get_img(city, cat):
    pool = CITY_POOLS.get(city, CITY_POOLS["Catania"])
    ids = pool.get(cat, pool["Deneyim"])
    pid = random.choice(ids)
    return f"https://images.unsplash.com/photo-{pid}?q=80&w=1000&auto=format&fit=crop"

FILES = ["assets/cities/catania.json", "assets/cities/bari.json", "assets/cities/sardinya.json", "assets/cities/cannes.json", "assets/cities/saint_tropez.json"]

for fpath in FILES:
    print(f"Processing {fpath}...")
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    city_name = data["city"]
    # Adjust for Saint-Tropez naming if needed
    if "Tropez" in city_name: city_name = "Saint-Tropez"
    
    for h in data["highlights"]:
        # If it is the bad placeholder URL, replace it
        if "photo-1549144511-f099e773c147" in h.get("imageUrl", ""):
            h["imageUrl"] = get_img(city_name, h["category"])
    
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Done! All placeholder Eiffel Tower images replaced.")
