#!/usr/bin/env python3
"""
Google Places Fotoğraf İndirme Scripti
Tüm şehir JSON dosyalarından Google Places API fotoğraflarını indirir.
"""

import os
import json
import requests
import time
import hashlib
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import re

# Konfigürasyon
CITIES_DIR = "assets/cities"
OUTPUT_DIR = "downloaded_images"
LOG_FILE = "download_log.json"
MAX_RETRIES = 3
DELAY_BETWEEN_REQUESTS = 0.1  # saniye

def sanitize_filename(name):
    """Dosya adı için güvenli karakter dönüşümü"""
    # Türkçe karakterleri değiştir
    tr_chars = {
        'ş': 's', 'Ş': 'S', 'ı': 'i', 'İ': 'I', 'ğ': 'g', 'Ğ': 'G',
        'ü': 'u', 'Ü': 'U', 'ö': 'o', 'Ö': 'O', 'ç': 'c', 'Ç': 'C',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'à': 'a', 'â': 'a',
        'ô': 'o', 'û': 'u', 'ù': 'u', 'î': 'i', 'ï': 'i', 'ñ': 'n',
        'ß': 'ss', 'ä': 'a', 'á': 'a', 'í': 'i', 'ó': 'o', 'ú': 'u',
        ' ': '_', '-': '_', "'": '', '"': '', '(': '', ')': '',
        '/': '_', '\\': '_', ':': '', ',': '', '.': '_', '&': 'and',
    }
    result = name.lower()
    for old, new in tr_chars.items():
        result = result.replace(old, new)
    # Sadece alfanumerik ve alt çizgi bırak
    result = re.sub(r'[^a-z0-9_]', '', result)
    # Birden fazla alt çizgiyi teke indir
    result = re.sub(r'_+', '_', result)
    return result.strip('_')[:50]  # Max 50 karakter

def is_google_places_url(url):
    """URL'nin Google Places API'den olup olmadığını kontrol et"""
    return url and 'maps.googleapis.com/maps/api/place/photo' in url

def download_image(url, output_path, retries=MAX_RETRIES):
    """Görseli indir ve kaydet"""
    for attempt in range(retries):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
            
            if response.status_code == 200:
                # Dosya uzantısını belirle
                content_type = response.headers.get('content-type', 'image/jpeg')
                if 'png' in content_type:
                    ext = '.png'
                elif 'webp' in content_type:
                    ext = '.webp'
                else:
                    ext = '.jpg'
                
                # Dosya adını güncelle
                final_path = output_path.with_suffix(ext)
                
                # Kaydet
                with open(final_path, 'wb') as f:
                    f.write(response.content)
                
                return {
                    'success': True,
                    'path': str(final_path),
                    'size': len(response.content),
                    'extension': ext
                }
            elif response.status_code == 403:
                return {
                    'success': False,
                    'error': f'403 Forbidden - API key sorunu',
                    'status_code': 403
                }
            else:
                if attempt < retries - 1:
                    time.sleep(1)
                    continue
                return {
                    'success': False,
                    'error': f'HTTP {response.status_code}',
                    'status_code': response.status_code
                }
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(1)
                continue
            return {
                'success': False,
                'error': str(e)
            }
    return {'success': False, 'error': 'Max retries exceeded'}

def process_city(city_file, output_base_dir, log):
    """Bir şehrin tüm fotoğraflarını indir"""
    city_name = city_file.stem  # Dosya adından şehir adı
    print(f"\n{'='*60}")
    print(f"📍 İşleniyor: {city_name}")
    print(f"{'='*60}")
    
    # Şehir için klasör oluştur
    city_output_dir = output_base_dir / city_name
    city_output_dir.mkdir(parents=True, exist_ok=True)
    
    # JSON'u oku
    with open(city_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    highlights = data.get('highlights', [])
    city_stats = {'total': 0, 'success': 0, 'failed': 0, 'skipped': 0}
    
    for i, place in enumerate(highlights):
        image_url = place.get('imageUrl', '')
        place_name = place.get('name', f'unknown_{i}')
        
        city_stats['total'] += 1
        
        # Google Places URL değilse atla
        if not is_google_places_url(image_url):
            city_stats['skipped'] += 1
            continue
        
        # Dosya adı oluştur
        safe_name = sanitize_filename(place_name)
        output_path = city_output_dir / safe_name
        
        # Zaten indirilmiş mi kontrol et
        existing_files = list(city_output_dir.glob(f"{safe_name}.*"))
        if existing_files:
            print(f"  ⏭️  Zaten var: {place_name[:40]}")
            city_stats['success'] += 1
            
            # Log'a ekle
            log_key = f"{city_name}/{safe_name}"
            if log_key not in log:
                log[log_key] = {
                    'original_url': image_url,
                    'local_path': str(existing_files[0]),
                    'place_name': place_name,
                    'status': 'exists'
                }
            continue
        
        # İndir
        print(f"  ⬇️  İndiriliyor: {place_name[:40]}...", end=' ', flush=True)
        result = download_image(image_url, output_path)
        
        if result['success']:
            print(f"✅ ({result['size']//1024}KB)")
            city_stats['success'] += 1
            
            # Log'a ekle
            log_key = f"{city_name}/{safe_name}"
            log[log_key] = {
                'original_url': image_url,
                'local_path': result['path'],
                'place_name': place_name,
                'status': 'downloaded'
            }
        else:
            print(f"❌ {result.get('error', 'Unknown error')}")
            city_stats['failed'] += 1
            
            # Hatalı log
            log_key = f"{city_name}/{safe_name}"
            log[log_key] = {
                'original_url': image_url,
                'place_name': place_name,
                'status': 'failed',
                'error': result.get('error', 'Unknown')
            }
        
        # Rate limiting
        time.sleep(DELAY_BETWEEN_REQUESTS)
    
    print(f"\n📊 {city_name} Özet:")
    print(f"   Toplam: {city_stats['total']}, Başarılı: {city_stats['success']}, "
          f"Başarısız: {city_stats['failed']}, Atlandı: {city_stats['skipped']}")
    
    return city_stats

def main():
    print("🚀 Google Places Fotoğraf İndirme Scripti")
    print("=" * 60)
    
    # Çıktı klasörü
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(exist_ok=True)
    
    # Log dosyası
    log_path = output_dir / LOG_FILE
    if log_path.exists():
        with open(log_path, 'r', encoding='utf-8') as f:
            log = json.load(f)
        print(f"📋 Mevcut log yüklendi: {len(log)} kayıt")
    else:
        log = {}
    
    # Şehir dosyalarını bul
    cities_path = Path(CITIES_DIR)
    city_files = sorted(cities_path.glob("*.json"))
    print(f"📁 Bulunan şehir dosyası: {len(city_files)}")
    
    # İstatistikler
    total_stats = {'total': 0, 'success': 0, 'failed': 0, 'skipped': 0}
    
    # Her şehri işle
    for city_file in city_files:
        try:
            stats = process_city(city_file, output_dir, log)
            for key in total_stats:
                total_stats[key] += stats[key]
            
            # Her şehirden sonra log'u kaydet
            with open(log_path, 'w', encoding='utf-8') as f:
                json.dump(log, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            print(f"❌ Hata ({city_file.name}): {e}")
    
    # Final özet
    print("\n" + "=" * 60)
    print("🏁 GENEL ÖZET")
    print("=" * 60)
    print(f"Toplam fotoğraf: {total_stats['total']}")
    print(f"Başarılı: {total_stats['success']}")
    print(f"Başarısız: {total_stats['failed']}")
    print(f"Atlandı (Google dışı): {total_stats['skipped']}")
    print(f"\n📁 Fotoğraflar: {output_dir.absolute()}")
    print(f"📋 Log dosyası: {log_path.absolute()}")

if __name__ == "__main__":
    main()
