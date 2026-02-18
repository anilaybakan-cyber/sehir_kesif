import pandas as pd

file_path = '/Users/anilebru/Downloads/gpt_excel_processed_v6.xlsx'
df = pd.read_excel(file_path, header=0)
df.columns = ['City', 'Name_TR', 'Name_EN', 'Category', 'Description_TR', 'Description_EN', 'Tips_TR', 'Tips_EN', 'Lat', 'Lng']
df = df.iloc[1:].reset_index(drop=True)

# Search for Museum Island related row
berlin_data = df[df['City'].str.contains('Berlin', na=False)]
island_row = berlin_data[berlin_data['Name_TR'].str.contains('Müze Adası', na=False) | berlin_data['Name_EN'].str.contains('Museum Island', na=False)]

print(island_row.to_json(orient='records', force_ascii=False, indent=2))
