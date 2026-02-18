import pandas as pd

try:
    df = pd.read_excel('/Users/anilebru/Desktop/City_Guides_Export.xlsx')
    
    # Amsterdam satırlarını filtrele
    amsterdam_rows = df[df.astype(str).apply(lambda x: x.str.contains('Amsterdam', case=False, na=False)).any(axis=1)]
    
    if amsterdam_rows.empty:
        print("No Amsterdam rows found.")
    else:
        # Tüm sütunları ve satırları yazdır (truncate etmeden)
        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.max_rows', None)
        
        # Sadece ilgili sütunları alalım (Header ve Content)
        # Sütun isimlerini önceki çıktıdan biliyoruz: 
        # ['City', 'Index', 'Header (TR)', 'Content (TR)', 'Header (EN)', 'Content (EN)']
        
        # Temiz çıktı için iterasyon
        for index, row in amsterdam_rows.iterrows():
            print("-" * 50)
            print(f"INDEX: {row['Index']}")
            print(f"TR_HEADER: {row['Header (TR)']}")
            print(f"TR_CONTENT: {row['Content (TR)']}")
            print(f"EN_HEADER: {row['Header (EN)']}")
            print(f"EN_CONTENT: {row['Content (EN)']}")
            print("-" * 50)

except Exception as e:
    print(f"Error reading excel: {e}")
