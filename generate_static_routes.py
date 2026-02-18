import re
import json
import os
import requests
import time
from pathlib import Path

# Ayarlar
PROJECT_ROOT = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif"
SERVICES_FILE = os.path.join(PROJECT_ROOT, "lib/services/curated_routes_service.dart")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets/cities")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets/routes")
API_KEY_FILE = os.path.join(PROJECT_ROOT, "lib/secrets.dart")

def get_api_key():
    """Secrets dosyasından API key'i bul"""
    try:
        with open(API_KEY_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'googleMapsApiKey\s*=\s*["\']([^"\']+)["\']', content)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"API Key okunamadı: {e}")
    return None

def load_city_data(city_name):
    """Şehir JSON dosyasından mekan verilerini yükle"""
    # Şehir ismi mapping (kod -> dosya)
    # create_routes_service içindeki switch case'den tahmin edilebilir veya standart isimlendirme
    # Basitçe lowercase ve türkçe karakter düzeltmesi deneyelim
    normalized = city_name.lower().replace('istanbul', 'istanbul').replace('İstanbul', 'istanbul') # Örnek
    
    # Dosya adını bulmaya çalış
    json_path = os.path.join(ASSETS_DIR, f"{normalized}.json")
    if not os.path.exists(json_path):
        # Belki 'londra' yerine 'london' dır?
        # Şimdilik listedeki şehir isimlerini varsayalım
        pass
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def find_coordinates(place_name, city_data):
    """Mekan isminden koordinat bul"""
    if not city_data: return None
    
    for place in city_data.get('highlights', []):
        if place['name'] == place_name:
            return f"{place['lat']},{place['lng']}"
    return None

def parse_routes_from_dart():
    """Dart dosyasından rota tanımlarını çıkar"""
    with open(SERVICES_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex ile CuratedRoute tanımlarını bul
    # Bu basit bir regex, karmaşık yapıları kaçırabilir ama format temiz görünüyor
    # id: "...", ... placeNames: ["...", "..."],
    
    routes = []
    
    # _get*Routes fonksiyonlarını bul
    # Her fonksiyon bir şehre ait
    city_blocks = re.split(r'static List<CuratedRoute> _get', content)
    
    for block in city_blocks[1:]: # İlki importlar vs
        # Şehir ismini bul
        city_match = re.match(r'([A-Za-z]+)Routes', block)
        if not city_match: continue
        
        city_name = city_match.group(1).lower()
        if city_name == "generic": continue
        
        # Türkçe isim düzeltmeleri (dosya adıyla eşleşmesi için)
        city_map = {
            'istanbul': 'istanbul', 'barcelona': 'barcelona', 'paris': 'paris', 
            'rome': 'roma', 'london': 'londra', 'berlin': 'berlin', 
            'amsterdam': 'amsterdam', 'newyork': 'newyork', 'tokyo': 'tokyo',
            'seville': 'sevilla', 'madrid': 'madrid', 'lisbon': 'lizbon',
            'porto': 'porto', 'naples': 'napoli', 'milan': 'milano',
            'venice': 'venedik', 'florence': 'floransa', 'athens': 'atina',
            'vienna': 'viyana', 'prague': 'prag', 'budapest': 'budapeste',
            'zurich': 'zurih', 'geneva': 'cenevre', 'lucerne': 'lucerne',
            'copenhagen': 'kopenhag', 'stockholm': 'stockholm', 'dubai': 'dubai',
            'marrakech': 'marakes', 'bangkok': 'bangkok', 'hongkong': 'hongkong',
            'singapore': 'singapur', 'seoul': 'seul', 'nice': 'nice',
            'lyon': 'lyon', 'marseille': 'marsilya', 'dublin': 'dublin'
        }
        
        target_city = city_map.get(city_name, city_name)
        
        # Rotaları bul
        route_matches = re.finditer(r'id:\s*"([^"]+)"[\s\S]*?placeNames:\s*\[(.*?)\]', block)
        
        for rm in route_matches:
            route_id = rm.group(1)
            places_str = rm.group(2)
            
            # Mekan listesini temizle
            places = [p.strip().strip('"').strip("'") for p in places_str.split(',')]
            places = [p for p in places if p] # Boşları at
            
            routes.append({
                'id': route_id,
                'city': target_city,
                'places': places
            })
            
    return routes

# Tüm travel modları
TRAVEL_MODES = ['walking', 'bicycling', 'transit', 'driving']

def fetch_directions(route, api_key, mode='walking'):
    """Google Directions API'den rota çek (belirtilen mode için)"""
    # Şehir verisini yükle
    city_data = load_city_data(route['city'])
    if not city_data:
        print(f"  [ERROR] Şehir verisi bulunamadı: {route['city']}")
        return None
        
    # Waypoint koordinatlarını bul
    coords = []
    for place_name in route['places']:
        coord = find_coordinates(place_name, city_data)
        if coord:
            coords.append(coord)
        else:
            print(f"  [WARN] Mekan koordinatı bulunamadı: {place_name} ({route['city']})")
    
    if len(coords) < 2:
        print(f"  [ERROR] Yeterli koordinat yok: {route['id']}")
        return None
        
    origin = coords[0]
    destination = coords[-1]
    waypoints = coords[1:-1]
    
    # API İsteği
    base_url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        'origin': origin,
        'destination': destination,
        'mode': mode,  # Dinamik mode
        'key': api_key
    }
    
    # Transit mode waypoint kabul etmiyor
    if waypoints and mode != 'transit':
        params['waypoints'] = 'optimize:true|' + '|'.join(waypoints)
        
    print(f"  [API] {mode.upper()} - {route['id']} ({len(coords)} nokta)...")
    try:
        resp = requests.get(base_url, params=params)
        data = resp.json()
        
        if data['status'] == 'OK':
            return data
        elif data['status'] == 'ZERO_RESULTS':
            print(f"  [WARN] {mode} için rota bulunamadı (normal)")
            return None
        else:
            print(f"  [API ERROR] {data['status']}: {data.get('error_message')}")
            return None
    except Exception as e:
        print(f"  [REQ ERROR] {e}")
        return None

def main():
    print("="*60)
    print("STATİK ROTA OLUŞTURUCU - TÜM MODLAR")
    print("="*60)
    
    # 1. API Key
    api_key = get_api_key()
    if not api_key:
        print("API Key bulunamadı!")
        return
    print(f"API Key: {api_key[:5]}...")
    
    # 2. Çıktı klasörü
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 3. Rotaları Pars Et
    print("\n[1/3] Rotalar analiz ediliyor...")
    routes = parse_routes_from_dart()
    print(f"Toplam {len(routes)} rota bulundu.")
    print(f"Modlar: {', '.join(TRAVEL_MODES)}")
    print(f"Toplam dosya sayısı: {len(routes)} × {len(TRAVEL_MODES)} = {len(routes) * len(TRAVEL_MODES)}")
    
    # 4. API Çağrıları ve Kayıt (Her rota için her mod)
    print("\n[2/3] Google Directions API çağrılıyor...")
    success_count = 0
    skip_count = 0
    fail_count = 0
    
    for i, route in enumerate(routes):
        print(f"\n[{i+1}/{len(routes)}] {route['id']} ({route['city']})")
        
        for mode in TRAVEL_MODES:
            # Yeni dosya adı: {id}_{mode}.json
            file_path = os.path.join(OUTPUT_DIR, f"{route['id']}_{mode}.json")
            
            # Zaten varsa atla (para tasarrufu)
            if os.path.exists(file_path):
                print(f"  ✓ {mode}: zaten var")
                skip_count += 1
                continue
            
            data = fetch_directions(route, api_key, mode)
            if data:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f)
                print(f"  ✓ {mode}: kaydedildi")
                success_count += 1
            else:
                print(f"  ✗ {mode}: başarısız")
                fail_count += 1
            
            # Rate limit önlemi
            time.sleep(0.3)
    
    print("\n" + "="*60)
    print(f"TAMAMLANDI!")
    print(f"  Yeni oluşturulan: {success_count}")
    print(f"  Zaten var (atlandı): {skip_count}")
    print(f"  Başarısız: {fail_count}")
    print("="*60)

if __name__ == "__main__":
    main()

