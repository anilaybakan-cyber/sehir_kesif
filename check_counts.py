import json
import os

cities_dir = 'assets/cities'
stats = []

for filename in os.listdir(cities_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(cities_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                count = len(data.get('highlights', []))
                stats.append((filename, count))
        except Exception as e:
            print(f"Error reading {filename}: {e}")

# Sort by count ascending
stats.sort(key=lambda x: x[1])

print(f"{'City File':<30} | {'Highlights':<10}")
print("-" * 45)
for city, count in stats:
    print(f"{city:<30} | {count:<10}")
