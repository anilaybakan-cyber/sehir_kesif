import os
import json
import re
from pathlib import Path
import subprocess

# Ensure pandas and openpyxl are installed
try:
    import pandas as pd
except ImportError:
    print("Installing pandas and openpyxl...")
    subprocess.check_call(["pip3", "install", "pandas", "openpyxl"])
    import pandas as pd

# Paths
ASSETS_DIR = Path('assets/cities')
OTA_DIR = Path('ota_data_pack/cities')
BLOG_DART_FILE = Path('lib/services/city_blog_content.dart')
OUTPUT_XLSX_DESKTOP = Path.home() / 'Desktop' / 'Tum_Icerik_Kaynaklari.xlsx'

# Output data list
all_data = []

def add_entry(source, entry_type, city_id, name_tr, name_en, category, content_tr, content_en):
    all_data.append({
        'Kaynak (Source)': source,
        'Tip (Type)': entry_type,
        'Şehir (City)': city_id,
        'Mekan/Başlık Adı TR': name_tr,
        'Mekan/Başlık Adı EN': name_en,
        'Kategori': category,
        'İçerik TR': content_tr,
        'İçerik EN': content_en
    })

def process_json_dir(directory, source_name):
    if not directory.exists():
        return
    for json_file in directory.glob('*.json'):
        city_id = json_file.stem
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # City Guide (General)
            add_entry(
                source=source_name,
                entry_type="City Summary (Şehir Özeti)",
                city_id=city_id,
                name_tr=data.get('city', city_id).title(),
                name_en=data.get('city_en', city_id).title(),
                category="Genel / General",
                content_tr=data.get('description', ''),
                content_en=data.get('description_en', '')
            )
            
            # Highlights
            for hl in data.get('highlights', []):
                add_entry(
                    source=source_name,
                    entry_type="Highlight (Mekan/Yer)",
                    city_id=city_id,
                    name_tr=hl.get('name', ''),
                    name_en=hl.get('name_en', hl.get('name', '')),
                    category=hl.get('category', ''),
                    content_tr=hl.get('description', ''),
                    content_en=hl.get('description_en', '')
                )
        except Exception as e:
            print(f"Error reading {json_file}: {e}")

def process_dart_blogs():
    if not BLOG_DART_FILE.exists():
        return
    
    with open(BLOG_DART_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all variables like: static const _romaTR = '''...''';
    pattern = re.compile(r'static\s+const\s+_([a-zA-Z]+)(TR|EN)\s*=\s*(r?[\'"]{3}.*?[\'"]{3}|r?["\'].*?["\']);', re.DOTALL)
    
    blog_data = {}
    for match in pattern.finditer(content):
        city_id = match.group(1).lower()
        lang = match.group(2)
        val = match.group(3).strip()
        
        # strip quotes
        if val.startswith("r'''") or val.startswith('r"""'):
            val = val[4:-3]
        elif val.startswith("'''") or val.startswith('"""'):
            val = val[3:-3]
        elif val.startswith("r'") or val.startswith('r"'):
            val = val[2:-1]
        else:
            val = val[1:-1]
            
        if city_id not in blog_data:
            blog_data[city_id] = {'TR': '', 'EN': ''}
        blog_data[city_id][lang] = val
        
    for city_id, langs in blog_data.items():
        add_entry(
            source="Hardcoded (CityBlogContent.dart)",
            entry_type="Blog Article / Detaylı Rehber",
            city_id=city_id,
            name_tr=f"{city_id.title()} Rehberi",
            name_en=f"{city_id.title()} Guide",
            category="Blog",
            content_tr=langs.get('TR', ''),
            content_en=langs.get('EN', '')
        )

def main():
    print("Processing assets/cities (Local App Data)...")
    process_json_dir(ASSETS_DIR, "assets/cities (Local)")
    
    print("Processing ota_data_pack/cities (GitHub/OTA Data)...")
    process_json_dir(OTA_DIR, "ota_data_pack (GitHub/OTA)")
    
    print("Processing CityBlogContent.dart (Hardcoded Blogs)...")
    process_dart_blogs()
    
    print(f"Creating Excel file with {len(all_data)} rows...")
    df = pd.DataFrame(all_data)
    
    # Save to Excel
    df.to_excel(OUTPUT_XLSX_DESKTOP, index=False, engine='openpyxl')
    print(f"✅ Excel dosyası başarıyla Masaüstüne kaydedildi: {OUTPUT_XLSX_DESKTOP}")

if __name__ == "__main__":
    main()
