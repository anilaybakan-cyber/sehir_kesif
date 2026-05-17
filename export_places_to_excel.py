import json
import csv
import glob
import os

# Output file path on Desktop
desktop_path = os.path.expanduser("~/Desktop/sehir_kesif_yerler.csv")

# Find all city json files
json_files = glob.glob("assets/cities/*.json")

with open(desktop_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
    # Define columns
    fieldnames = [
        'City', 'City_EN', 'Place_Name_TR', 'Place_Name_EN', 
        'Category_TR', 'Category_EN', 
        'Description_TR', 'Description_EN',
        'Tips_TR', 'Tips_EN',
        'Tags_TR', 'Area'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                city_tr = data.get('city', '')
                city_en = data.get('city_en', city_tr)

                for highlight in data.get('highlights', []):
                    # Category mapping as in the app
                    category_tr = highlight.get('category', '')
                    category_en = ''
                    if category_tr == "Tarihi":
                        category_en = "Historical"
                    elif category_tr == "Yeme-İçme":
                        category_en = "Food & Drink"
                    elif category_tr == "Müze":
                        category_en = "Museum"
                    elif category_tr == "Park":
                        category_en = "Park"
                    elif category_tr == "Deneyim":
                        category_en = "Experience"
                    elif category_tr == "Alışveriş":
                        category_en = "Shopping"
                    elif category_tr == "Manzara":
                        category_en = "Viewpoint"
                    elif category_tr == "Eğlence":
                        category_en = "Entertainment"
                    elif category_tr == "Sanat":
                        category_en = "Art"
                    elif category_tr == "Mimari":
                        category_en = "Architecture"
                    elif category_tr == "Doğa":
                        category_en = "Nature"
                    elif category_tr == "Kafe":
                        category_en = "Cafe"
                    elif category_tr == "Tarih":
                        category_en = "History"
                    elif category_tr == "Sokak":
                        category_en = "Street"
                    elif category_tr == "Bar":
                        category_en = "Bar"
                    elif category_tr == "Kilise":
                        category_en = "Church"
                    elif category_tr == "Meydan":
                        category_en = "Square"
                    elif category_tr == "Restoran":
                        category_en = "Restaurant"
                    else:
                        category_en = category_tr
                        
                    tags = highlight.get('tags', [])
                    tags_tr = ", ".join(tags) if isinstance(tags, list) else str(tags)

                    writer.writerow({
                        'City': city_tr,
                        'City_EN': city_en,
                        'Place_Name_TR': highlight.get('name', ''),
                        'Place_Name_EN': highlight.get('name_en', highlight.get('name', '')),
                        'Category_TR': category_tr,
                        'Category_EN': category_en,
                        'Description_TR': highlight.get('description', ''),
                        'Description_EN': highlight.get('description_en', ''),
                        'Tips_TR': highlight.get('tips', ''),
                        'Tips_EN': highlight.get('tips_en', ''),
                        'Tags_TR': tags_tr,
                        'Area': highlight.get('area', '')
                    })
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print(f"Veriler başarıyla {desktop_path} konumuna aktarıldı.")
