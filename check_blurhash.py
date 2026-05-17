import json
import glob

missing = 0
total = 0

for file in glob.glob("assets/cities/*.json"):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for place in data.get('highlights', []):
            total += 1
            if not place.get('blurHash'):
                missing += 1

print(f"Total places: {total}")
print(f"Missing blurHash: {missing}")
