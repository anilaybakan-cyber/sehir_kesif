import json
import csv
import os

# Paths
csv_path = '/Users/anilebru/Desktop/city_highlights_export.csv'
json_path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/cenevre.json'
output_path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/cenevre.json'

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_geneva():
    print(f"Loading JSON from {json_path}...")
    city_data = load_json(json_path)
    
    # Create a lookup map for existing highlights by name
    existing_highlights = {h['name']: h for h in city_data.get('highlights', [])}
    
    print(f"Loading CSV from {csv_path}...")
    updated_count = 0
    new_count = 0
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Filter for Cenevre
            if row['City'] != 'Cenevre':
                continue
                
            name = row['Title (TR)']
            name_en = row['Title (EN)']
            
            # Prepare content from CSV
            update_data = {
                'name': name,
                'name_en': name_en,
                'category': row['Category'],
                'area': row['Area'],
                'description': row['Description (TR)'],
                'description_en': row['Description (EN)'],
                'price': row['Price'],
                'imageUrl': row['Image URL']
            }
            
            # Handle numeric fields
            try:
                update_data['rating'] = float(row['Rating'])
            except ValueError:
                pass
                
            try:
                update_data['reviewCount'] = int(row['Review Count'])
            except ValueError:
                pass

            # Update existing or create new
            if name in existing_highlights:
                # Update existing (preserving other keys like id, lat, lng)
                print(f"Updating: {name}")
                original = existing_highlights[name]
                for k, v in update_data.items():
                    if v: # Only update if value exists in CSV
                        original[k] = v
                updated_count += 1
            else:
                # Create new (will lack lat/lng)
                print(f"Adding New: {name}")
                # Add default tags if missing
                if 'tags' not in update_data:
                    update_data['tags'] = ['keşfet', 'popüler'] 
                
                # Check distance? Default to 0?
                update_data['distanceFromCenter'] = 0.0
                
                city_data['highlights'].append(update_data)
                # Add to map so we don't duplicate if CSV has duplicates
                existing_highlights[name] = update_data 
                new_count += 1

    print(f"Updated {updated_count} items.")
    print(f"Added {new_count} items.")
    
    save_json(city_data, output_path)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    update_geneva()
