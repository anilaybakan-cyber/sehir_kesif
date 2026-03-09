import json
import os
import shutil
import pandas as pd

PRAG_ASSET = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/prag.json'
PRAG_OTA = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack/cities/prag.json'
EXCEL_FILE = '/Users/anilebru/Desktop/Tum_Sehirler_V4_Final_Kategorili.xlsx'

# Update JSON
with open(PRAG_ASSET, 'r', encoding='utf-8') as f:
    data = json.load(f)

updated = False
for hl in data.get('highlights', []):
    if hl.get('id') == 'mexicka' or hl.get('name', '').lower() == 'mexická':
        if hl.get('category') == 'Meksika':
            hl['category'] = 'Yeme-İçme'
            updated = True
            print("Fixed JSON category for Mexicka")

if updated:
    with open(PRAG_ASSET, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    shutil.copy2(PRAG_ASSET, PRAG_OTA)
    print("Saved pragmatic JSONs")

# Update Excel
df = pd.read_excel(EXCEL_FILE)
mask = (df['Şehir'] == 'Prag') & (df['Kategori'] == 'Meksika')
if mask.any():
    df.loc[mask, 'Kategori'] = 'Yeme-İçme'
    df.to_excel(EXCEL_FILE, index=False)
    print(f"Fixed {mask.sum()} rows in Excel")
