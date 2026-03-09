import pandas as pd
import json
import os

SOURCE_FILE = '/Users/anilebru/Desktop/Yepyeni_Tum_Sehirler_Detayli_Liste_V3.xlsx'
TARGET_FILE = '/Users/anilebru/Desktop/Tum_Sehirler_V4_Final_Kategorili.xlsx'

category_mapping = {
    # Bar
    'Gece Hayatı': 'Bar', 'Bira Barı': 'Bar', 'Bira Fabrikası': 'Bar', 
    'Şarap Barı': 'Bar', 'Craft Bira': 'Bar', 'Çek Pub': 'Bar', 'Tapas Bar': 'Bar',
    # Yeme-İçme
    'Restoran': 'Yeme-İçme', 'Fine Dining': 'Yeme-İçme', 'Amerikan Lokanta': 'Yeme-İçme', 
    'Slovak Restoran': 'Yeme-İçme', 'Lezzet': 'Yeme-İçme', 'Domuz Eti Restoranı': 'Yeme-İçme', 
    'Geleneksel Çek': 'Yeme-İçme', 'Modern Çek': 'Yeme-İçme', 'İspanyol': 'Yeme-İçme', 
    'Bistro': 'Yeme-İçme', 'Bira Barı-Restoran': 'Yeme-İçme', 'Japon-Peru': 'Yeme-İçme', 
    'Ukrayna Restoran': 'Yeme-İçme', 'Fast Casual': 'Yeme-İçme', 'Pub Restoran': 'Yeme-İçme', 
    'Ukrayna Deniz Ürünleri': 'Yeme-İçme', 'İtalyan': 'Yeme-İçme', 'İtalyan Fine Dining': 'Yeme-İçme', 
    'Steakhouse': 'Yeme-İçme',
    # Kafe
    'Cafe': 'Kafe', 'Brunch': 'Kafe', 'Fransız Brunch': 'Kafe', 
    'Kahvaltı': 'Kafe', 'İngiliz Brunch': 'Kafe',
    # Tarihi
    'Mimari': 'Tarihi', 'Dini': 'Tarihi', 'Kilise': 'Tarihi', 
    'Meydan': 'Tarihi', 'İkonik': 'Tarihi',
    # Deneyim
    'Kültür': 'Deneyim', 'Eğlence': 'Deneyim', 'Sanat': 'Deneyim', 
    'Müzik': 'Deneyim', 'Bilgi': 'Deneyim', 'Bilim': 'Deneyim', 
    'Bölge': 'Deneyim', 'Cadde': 'Deneyim', 'Zanaat': 'Deneyim', 
    'Lokal': 'Deneyim', 'Ulaşım': 'Deneyim', 'Macera': 'Deneyim', 
    'Keşfet': 'Deneyim', 'Ada': 'Deneyim',
    # Park
    'Doğa': 'Park', 'Huzur': 'Park'
}

print("Loading data...")
df = pd.read_excel(SOURCE_FILE)

print("Applying category mapping...")
# Apply mapping, keeping the original category if it's not in the mapping dictionary (e.g., standard categories)
df['Kategori'] = df['Kategori'].apply(lambda x: category_mapping.get(x, x))

print("Saving final normalized Excel file...")
df.to_excel(TARGET_FILE, index=False)
print(f"Saved to {TARGET_FILE}")
