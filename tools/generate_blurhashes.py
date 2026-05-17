#!/usr/bin/env python3
"""
Blurhash oluşturma script'i
Mevcut şehir JSON dosyalarındaki fotoğraflar için blurhash string'leri üretir.

Kullanım:
    python tools/generate_blurhashes.py

Gereksinimler:
    pip install Pillow blurhash
"""

import json
import os
import sys
from pathlib import Path
from urllib.request import urlopen
from io import BytesIO

try:
    from PIL import Image
    from blurhash import encode
except ImportError:
    print("❌ Gereksinimler eksik:")
    print("   pip install Pillow blurhash")
    sys.exit(1)


def download_image(url: str) -> Image.Image:
    """URL'den görseli indir ve PIL Image olarak dön."""
    try:
        with urlopen(url) as response:
            img_data = response.read()
        img = Image.open(BytesIO(img_data))
        if img.mode != 'RGB':
            img = img.convert('RGB')
        return img
    except Exception as e:
        print(f"  ⚠️ Görsel indirilemedi: {url} - {e}")
        return None


def generate_blurhash(image_url: str) -> str:
    """Görsel URL'sinden blurhash üret."""
    img = download_image(image_url)
    if img is None:
        return None
    
    # Resize to 32x32 for blurhash (standard size)
    img = img.resize((32, 32), Image.LANCZOS)
    
    # Convert to RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Convert to 2D array of RGB values (required by blurhash library)
    pixels = [[list(img.getpixel((x, y))) for x in range(32)] for y in range(32)]
    
    # Encode blurhash (4 components X, 3 components Y is standard)
    blurhash_str = encode(pixels, 4, 3)
    return blurhash_str


def process_city_json(json_path: Path) -> bool:
    """Bir şehir JSON dosyasını işle ve blurHash alanlarını ekle."""
    print(f"📄 İşleniyor: {json_path.name}")
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"  ❌ JSON okunamadı: {e}")
        return False
    
    highlights = data.get('highlights', [])
    if not highlights:
        print("  ℹ️  Highlight yok")
        return True
    
    updated_count = 0
    for h in highlights:
        image_url = h.get('imageUrl') or h.get('image') or h.get('photo')
        if not image_url:
            continue
        
        # Zaten blurHash var mı?
        if h.get('blurHash') or h.get('blurhash'):
            continue
        
        # Blurhash oluştur
        blurhash_str = generate_blurhash(image_url)
        if blurhash_str:
            h['blurHash'] = blurhash_str
            updated_count += 1
            print(f"  ✓ {h.get('name', 'Unknown')}: {blurhash_str}")
    
    if updated_count > 0:
        # Yedek oluştur
        backup_path = json_path.with_suffix('.json.backup')
        with open(json_path, 'r', encoding='utf-8') as f:
            with open(backup_path, 'w', encoding='utf-8') as bf:
                bf.write(f.read())
        
        # Güncellenmiş JSON'u yaz
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"  ✅ {updated_count} blurhash eklendi (yedek: {backup_path.name})")
    else:
        print("  ℹ️  Yeni blurhash gerekli değil")
    
    return True


def main():
    """Ana fonksiyon."""
    # Proje kök dizini
    root_dir = Path(__file__).parent.parent
    cities_dir = root_dir / 'assets' / 'cities'
    
    if not cities_dir.exists():
        print(f"❌ Şehirler dizini bulunamadı: {cities_dir}")
        sys.exit(1)
    
    # Tüm şehir JSON dosyalarını bul
    json_files = sorted(cities_dir.glob('*.json'))
    
    if not json_files:
        print(f"❌ JSON dosyası bulunamadı: {cities_dir}")
        sys.exit(1)
    
    print(f"🔍 {len(json_files)} şehir dosyası bulundu\n")
    
    success_count = 0
    for json_file in json_files:
        if process_city_json(json_file):
            success_count += 1
    
    print(f"\n✅ {success_count}/{len(json_files)} dosya işlendi")


if __name__ == '__main__':
    main()
