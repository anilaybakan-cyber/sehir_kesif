import firebase_admin
from firebase_admin import credentials, storage
from PIL import Image
import io
import os
import concurrent.futures

import argparse

parser = argparse.ArgumentParser(description='Firebase resimlerini optimize et.')
parser.add_argument('--city', type=str, required=True, help='Optimize edilecek şehrin adı (ör: prag, amalfi, hepsi)')
args = parser.parse_args()

TARGET_CITY = args.city
MAX_WIDTH = 800
MAX_HEIGHT = 800
JPEG_QUALITY = 75

# Firebase Başlat
cred = credentials.Certificate('service_account.json')
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'myway-3fe75.firebasestorage.app'
    })

bucket = storage.bucket()

def process_blob(blob):
    try:
        # Sadece jpg, jpeg, png dosyalarını işle
        if not (blob.name.lower().endswith('.jpg') or blob.name.lower().endswith('.jpeg') or blob.name.lower().endswith('.png')):
            return f"Atlandı (Resim değil): {blob.name}"

        # Sadece seçili şehri işle (test için)
        if TARGET_CITY != 'hepsi' and TARGET_CITY not in blob.name.lower():
            return f"Atlandı (Hedef şehir değil): {blob.name}"

        # Dosyayı indir
        image_bytes = blob.download_as_bytes()
        
        # PIL ile aç
        img = Image.open(io.BytesIO(image_bytes))
        
        # Format dönüşümü (PNG'leri JPEG'e çevirmek için RGB'ye geç)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        # Orijinal boyutları kontrol et
        orig_width, orig_height = img.size
        
        # Eğer zaten küçükse elleme (gereksiz kalite düşmesin)
        if orig_width <= MAX_WIDTH and orig_height <= MAX_HEIGHT:
            return f"Zaten küçük, atlandı: {blob.name} ({orig_width}x{orig_height})"
            
        # Yeniden boyutlandır (En boy oranını koruyarak)
        img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.Resampling.LANCZOS)
        
        # Bellekte JPEG olarak sıkıştır
        output_io = io.BytesIO()
        img.save(output_io, format='JPEG', quality=JPEG_QUALITY, optimize=True)
        compressed_bytes = output_io.getvalue()
        
        # Orijinal ve yeni boyut karşılaştırması
        orig_size_kb = len(image_bytes) / 1024
        new_size_kb = len(compressed_bytes) / 1024
        
        # Dosya boyutu gerçekten küçüldüyse üzerine yaz
        if new_size_kb < orig_size_kb:
            # Üzerine yaz
            new_blob = bucket.blob(blob.name)
            new_blob.upload_from_string(compressed_bytes, content_type='image/jpeg')
            return f"✅ Başarılı: {blob.name} | {orig_size_kb:.1f} KB -> {new_size_kb:.1f} KB"
        else:
            return f"Sıkıştırma fayda sağlamadı, atlandı: {blob.name}"
            
    except Exception as e:
        return f"❌ Hata ({blob.name}): {str(e)}"

def main():
    print(f"[{TARGET_CITY}] şehrindeki resimler taranıyor ve sıkıştırılıyor...")
    prefix = f'cities/{TARGET_CITY}/' if TARGET_CITY != 'hepsi' else 'cities/'
    blobs = list(bucket.list_blobs(prefix=prefix))
    
    print(f"Toplam {len(blobs)} dosya bulundu. İşlem başlıyor (Paralel 10 thread)...")
    
    success_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(process_blob, blobs)
        for result in results:
            print(result)
            if "✅" in result:
                success_count += 1
                
    print(f"\nİşlem Tamamlandı! Toplam {success_count} resim başarıyla optimize edildi.")

if __name__ == '__main__':
    main()
