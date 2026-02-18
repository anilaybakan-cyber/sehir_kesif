#!/usr/bin/env python3
"""
Script to apply Google Places API photos to city_switcher_screen.dart and explore_screen.dart
"""

import json
import re

# Load the photo URLs
with open("scripts/city_photos_output.json", "r") as f:
    photo_urls = json.load(f)

# Files to update
files_to_update = [
    "lib/screens/city_switcher_screen.dart",
    "lib/screens/explore_screen.dart"
]

def update_dart_file(filepath, photo_urls):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    updated = 0
    for city_id, new_url in photo_urls.items():
        # Pattern for city_switcher: "networkImage": "..." or 'city_id': '...'
        # We need to find and replace URLs for each city
        
        # For city_switcher_screen.dart - networkImage in list
        pattern1 = rf'("id":\s*"{city_id}"[^}}]*"networkImage":\s*")[^"]+(")'
        if re.search(pattern1, content):
            content = re.sub(pattern1, rf'\g<1>{new_url}\g<2>', content)
            updated += 1
        
        # For explore_screen.dart - _cityImages map
        pattern2 = rf"('{city_id}':\s*')[^']+(')"
        if re.search(pattern2, content):
            content = re.sub(pattern2, rf"\g<1>{new_url}\g<2>", content)
            updated += 1
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return updated

total = 0
for filepath in files_to_update:
    count = update_dart_file(filepath, photo_urls)
    print(f"✅ {filepath}: {count} URLs updated")
    total += count

print(f"\nTotal: {total} URLs updated across all files")
