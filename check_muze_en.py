import pandas as pd

file_path = '/Users/anilebru/Downloads/gpt_excel_processed_v6.xlsx'
df = pd.read_excel(file_path, header=0)
df.columns = ['City', 'Name_TR', 'Name_EN', 'Category', 'Description_TR', 'Description_EN', 'Tips_TR', 'Tips_EN', 'Lat', 'Lng']
df = df.iloc[1:].reset_index(drop=True)

# Check for "Müze" in Name_EN columns
muze_in_en = df[df['Name_EN'].str.contains('Müze', na=False)]
print(f"Found {len(muze_in_en)} entries where Name_EN contains 'Müze'")
if not muze_in_en.empty:
    print(muze_in_en[['Name_TR', 'Name_EN']].head(10).to_string())
