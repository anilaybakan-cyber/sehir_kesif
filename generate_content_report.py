import json
import csv
import os
import glob

def generate_report():
    cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    output_file = "/Users/anilebru/Desktop/sehir_kesif_content_report.csv"
    
    # Headers
    headers = [
        "City", "Place Name", "Category", "Subcategory", 
        "Area", "Rating", "Review Count", "Price", 
        "Latitude", "Longitude", "Tags", "Description (TR)", "Description (EN)"
    ]
    
    rows = []
    
    json_files = glob.glob(os.path.join(cities_dir, "*.json"))
    json_files.sort()
    
    print(f"Found {len(json_files)} city files.")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            city_name = data.get("city", os.path.basename(file_path).replace(".json", "").capitalize())
            highlights = data.get("highlights", [])
            
            print(f"Processing {city_name}: {len(highlights)} places")
            
            for place in highlights:
                row = [
                    city_name,
                    place.get("name", ""),
                    place.get("category", ""),
                    place.get("subcategory", ""),
                    place.get("area", ""),
                    place.get("rating", ""),
                    place.get("reviewCount", ""),
                    place.get("price", ""),
                    place.get("lat", ""),
                    place.get("lng", ""),
                    ", ".join(place.get("tags", [])),
                    place.get("description", "").replace("\n", " "),
                    place.get("description_en", "").replace("\n", " ")
                ]
                rows.append(row)
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f"\nReport generated successfully: {output_file}")
    print(f"Total places: {len(rows)}")

if __name__ == "__main__":
    generate_report()
