import csv

def inspect_geneva():
    with open('rehber_guncelle.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        print(f"Headers: {headers}")
        
        geneva_rows = []
        for row in reader:
            if row[0].strip() == 'Cenevre':
                geneva_rows.append(row)
                
        print(f"Found {len(geneva_rows)} rows for Cenevre.")
        for row in geneva_rows:
            print(f"Index: {row[1]}, Content Length: {len(row[3])}")
            if row[3]:
                print(f"Start: {row[3][:50]}...")

if __name__ == "__main__":
    inspect_geneva()
