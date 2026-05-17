import sys
try:
    import pandas as pd
    import openpyxl
    df = pd.read_excel('/Users/anilebru/Desktop/revize.xlsx')
    print("SUCCESS")
    print(df.head())
    print(df.columns.tolist())
except Exception as e:
    print(f"ERROR: {e}")
