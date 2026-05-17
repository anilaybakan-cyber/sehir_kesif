import csv

input_file = '/Users/anilebru/Desktop/revize_gerçek_içerikler.csv'
output_file = '/Users/anilebru/Desktop/revize_özet.csv'

rows = []
with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows.append(header)
    for row in reader:
        # Check if generic or just updated
        if "GÜNCELLENDİ" in row[6] or "JENERİK" in row[6]:
            rows.append(row)

# Limit to top 500 or just ones that matter
with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Summary CSV created with {len(rows)-1} items.")
