import json
import os
import csv

def export_contents():
    ota_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack/cities'
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    output_path = '/Users/anilebru/Desktop/icerikler2.csv'
    
    headers = ['Source', 'City', 'Place Name', 'Description (TR)', 'Description (EN)', 'Tips (TR)', 'Tips (EN)']
    
    data_rows = []
    
    # Get unique city keys from both dirs
    ota_files = {f: os.path.join(ota_dir, f) for f in os.listdir(ota_dir) if f.endswith('.json') and not f.endswith('.tmp')}
    assets_files = {f: os.path.join(assets_dir, f) for f in os.listdir(assets_dir) if f.endswith('.json') and not f.endswith('.tmp') and not '.bak.' in f}
    
    # Combine unique keys
    all_city_keys = sorted(list(set(ota_files.keys()) | set(assets_files.keys())))
    
    for filename in all_city_keys:
        # Prioritize Assets if it exists (usually more recent/complete in this repo)
        if filename in assets_files:
            file_path = assets_files[filename]
            source = "Assets"
        else:
            file_path = ota_files[filename]
            source = "OTA"
            
        city_name = filename.replace('.json', '').capitalize()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                city_data = json.load(f)
                highlights = city_data.get('highlights', [])
                
                for h in highlights:
                    data_rows.append([
                        source,
                        city_name,
                        h.get('name', ''),
                        h.get('description', ''),
                        h.get('description_en', ''),
                        h.get('tips', ''),
                        h.get('tips_en', '')
                    ])
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    # Write to CSV with UTF-8 BOM
    with open(output_path, 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data_rows)
    
    print(f"Exported {len(data_rows)} items from {len(all_city_keys)} cities to {output_path}")

if __name__ == "__main__":
    export_contents()
