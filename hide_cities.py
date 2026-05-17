import os
import shutil

CITIES_TO_REVERT = [
    "cannes", "selanik", "dubrovnik", "mykonos", "bodrum",
    "cesme", "kas", "amalfi", "ibiza", "mallorca",
    "valencia", "palermo", "catania", "bari", "sardinya",
    "budva", "ksamil", "rhodes", "saint_tropez", "midilli"
]

def map_city_name(c):
    if c == "çeşme": return "cesme"
    if c == "kaş": return "kas"
    if c == "saint-tropez": return "saint_tropez"
    if c == "Valencia": return "valencia"
    return c

def main():
    modified = 0
    for original_city in CITIES_TO_REVERT:
        city = map_city_name(original_city)
        src = f"assets/cities/{city}.json"
        dest = f"assets/cities/{city}.json.draft"
        if os.path.exists(src):
            os.rename(src, dest)
            print(f"Renamed {src} to {dest}")
            modified += 1
        elif os.path.exists(dest):
            print(f"Already hidden: {dest}")
        else:
            print(f"Not found: {src}")
            
    print(f"Total hidden: {modified}")

if __name__ == "__main__":
    main()
