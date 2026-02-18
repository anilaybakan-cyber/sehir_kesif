import pandas as pd
import json

file_path = '/Users/anilebru/Downloads/gpt_excel_processed_v6.xlsx'

try:
    # Read the first sheet
    df = pd.read_excel(file_path)
    print("Columns:", df.columns.tolist())
    print("\nFirst 3 rows:")
    print(df.head(3).to_json(orient='records', force_ascii=False, indent=2))
    
    # Check for unique cities to know what we are dealing with
    if 'City' in df.columns:
        print("\nCities in file:", df['City'].unique().tolist())
    elif 'Sehir' in df.columns:
         print("\nCities in file:", df['Sehir'].unique().tolist())
    elif 'Şehir' in df.columns:
         print("\nCities in file:", df['Şehir'].unique().tolist())

except Exception as e:
    print(f"Error reading Excel: {e}")
