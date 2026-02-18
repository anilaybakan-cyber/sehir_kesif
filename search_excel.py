import pandas as pd

excel_path = '/Users/anilebru/Desktop/City_Guides_Export.xlsx'

try:
    print(f"Reading {excel_path}...")
    # Read all sheets
    xls = pd.ExcelFile(excel_path)
    print(f"Sheets found: {xls.sheet_names}")
    
    found = False
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        
        # Convert all to string and search
        mask = df.astype(str).apply(lambda x: x.str.contains('Hızlı Bakış|Hızlı bakış', case=False, na=False))
        
        if mask.any().any():
            print(f"\n✅ Found 'Hızlı Bakış' in sheet: {sheet_name}")
            # Get rows where it is found
            rows_with_string = df[mask.any(axis=1)]
            for index, row in rows_with_string.iterrows():
                print(f"Row {index}:")
                # Print only columns that contain the string
                for col in df.columns:
                    val = str(row[col])
                    if 'Hızlı Bakış' in val or 'Hızlı bakış' in val:
                         print(f"  Column '{col}': {val[:100]}...") # Print first 100 chars
            found = True
            
    if not found:
        print("\n❌ 'Hızlı Bakış' not found in any sheet.")

except Exception as e:
    print(f"Error: {e}")
