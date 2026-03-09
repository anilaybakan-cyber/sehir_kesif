import json
import glob

counts = []
total = 0
for file in glob.glob("assets/cities/*.json"):
    with open(file, "r") as f:
        data = json.load(f)
        city = data.get("city", "Unknown")
        count = len(data.get("highlights", []))
        counts.append((city, count))
        total += count

counts.sort(key=lambda x: x[1], reverse=True)

print(f"Toplam_Sehir: {len(counts)}")
print(f"Toplam_Mekan: {total}\n")
print("-" * 40)
for city, count in counts:
    print(f"{city.ljust(30)} : {count}")
