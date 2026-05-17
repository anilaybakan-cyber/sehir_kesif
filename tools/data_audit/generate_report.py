import json

# Verdicts dosyasını oku
with open('gemini_verdicts.json', 'r', encoding='utf-8') as f:
    verdicts = json.load(f)

# Mismatch ve wrong_city vakalarını filtrele
mismatches = []
wrong_cities = []

for place_id, data in verdicts.items():
    if data.get('verdict') == 'mismatch':
        mismatches.append({
            'place_id': place_id,
            'name': data.get('name', ''),
            'city': data.get('city', ''),
            'category': data.get('category', ''),
            'reason': data.get('reason', '')
        })
    elif data.get('verdict') == 'wrong_city':
        wrong_cities.append({
            'place_id': place_id,
            'name': data.get('name', ''),
            'city': data.get('city', ''),
            'category': data.get('category', ''),
            'reason': data.get('reason', '')
        })

# Raporu yaz
print(f"=== MISMATCH RAPORU ({len(mismatches)} vaka) ===")
for i, m in enumerate(mismatches, 1):
    print(f"{i}. {m['name']} ({m['city']}) - {m['category']}")
    print(f"   Reason: {m['reason']}")
    print(f"   Place ID: {m['place_id']}")
    print()

print(f"\n=== WRONG_CITY RAPORU ({len(wrong_cities)} vaka) ===")
for i, w in enumerate(wrong_cities, 1):
    print(f"{i}. {w['name']} ({w['city']}) - {w['category']}")
    print(f"   Reason: {w['reason']}")
    print(f"   Place ID: {w['place_id']}")
    print()

# JSON olarak da kaydet
with open('mismatch_report.json', 'w', encoding='utf-8') as f:
    json.dump(mismatches, f, ensure_ascii=False, indent=2)

with open('wrong_city_report.json', 'w', encoding='utf-8') as f:
    json.dump(wrong_cities, f, ensure_ascii=False, indent=2)

print(f"✅ Raporlar oluşturuldu: mismatch_report.json ({len(mismatches)}), wrong_city_report.json ({len(wrong_cities)})")
