import json
import os
import re

CITIES_DIR = 'assets/cities'

# High-Premium Image Mappings (Unsplash)
PREMIUM_IMAGES = {
    'cannes': 'https://images.unsplash.com/photo-1510414842594-a61c69b5ae57?w=1200',
    'saint_tropez': 'https://images.unsplash.com/photo-1541416410405-b77874f63116?w=1200',
    'bari': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bari/hero.jpg',
    'sardinya': 'https://images.unsplash.com/photo-1543783207-ec64e405a760?w=1200',
    'catania': 'https://images.unsplash.com/photo-1533105079780-92b9be482077?w=1200',
    'palermo': 'https://images.unsplash.com/photo-1525438160292-a5a860951216?w=1200',
    'dubrovnik': 'https://images.unsplash.com/photo-1555990540-3482390f7773?w=1200',
    'amalfi': 'https://images.unsplash.com/photo-1533903345306-15d1c30952de?w=1200',
    'ibiza': 'https://images.unsplash.com/photo-1516690561799-46d8f74f90f6?w=1200',
    'mallorca': 'https://images.unsplash.com/photo-1536431311719-398b6704d4cc?w=1200',
    'mykonos': 'https://images.unsplash.com/photo-1601581875309-fad3c438769b?w=1200',
    'santorini': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=1200',
    'rhodes': 'https://images.unsplash.com/photo-1558284534-192776c5b96a?w=1200',
    'bodrum': 'https://images.unsplash.com/photo-1582234375003-8d63a890db7a?w=1200',
    'cesme': 'https://images.unsplash.com/photo-1570940333200-a232fd33ff36?w=1200',
    'kas': 'https://images.unsplash.com/photo-1524230572899-a752b3835840?w=1200',
    'atina': 'https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=1200',
    'dublin': 'https://images.unsplash.com/photo-1549918864-48ac978761a4?w=1200',
    'lucerne': 'https://images.unsplash.com/photo-1510414442767-73934301904e?w=1200',
    'lyon': 'https://images.unsplash.com/photo-1520106212299-d99c443e4568?w=1200',
    'marakes': 'https://images.unsplash.com/photo-1548013146-72479768bada?w=1200',
    'selanik': 'https://images.unsplash.com/photo-1562608460-f97577579893?w=1200',
}

# Detection Patterns for Fake Names
FAKE_PATTERNS = [
    r'^Spot \d+$',
    r'^Point \d+$',
    r'Point of Interest',
    r'Info Hub',
    r'Trip Link',
    r'Gateway',
    r'Guide$',
    r'Viewpoint$',
]
RE_FAKE = re.compile('|'.join(FAKE_PATTERNS), re.IGNORECASE)

# Trash fragments to strip from descriptions
TRASH_FRAGMENTS = [
    "kentsel", 
    "prestij noktası", 
    "sosyal durak kalesidir", 
    "kaza kale",
    "kentsel dinamiz",
    "sosyal hayatı birleştiren",
    "kentsel haritasına karakter katan",
    "en sevilen ve tatlı kentsel duraklardan birisi olan",
    "sofistike bir kentsel sosyal durak",
    "kentsel bir vizyon alanıdır",
    "kentsel bir dinlenme alanı sunar",
    "kentsel estetiğini en zarif haliyle yansıtan",
    "kentsel dokunuş katan",
]
RE_BACKUP_LEAK = re.compile(r'\w+\.bak\.\d+_\d+')

def heal_description(desc):
    if not desc: return desc
    # Remove backup leaks
    desc = RE_BACKUP_LEAK.sub('', desc)
    # Remove trash fragments
    for frag in TRASH_FRAGMENTS:
        desc = desc.replace(frag, "").replace("  ", " ").strip()
    return desc

def is_fake(venue, descriptions_count):
    name = venue.get('name', '')
    desc = venue.get('description', '')
    
    # 1. Name matches generic pattern
    if RE_FAKE.search(name):
        return True
    
    # 2. Description is part of a cluster (template-based)
    if descriptions_count.get(desc, 0) > 3:
        # If the description itself is pure garbage
        for frag in TRASH_FRAGMENTS:
            if frag in desc:
                return True
    return False

def get_latest_valid_backup(city_id):
    path = os.path.join(CITIES_DIR)
    backups = [f for f in os.listdir(path) if f.startswith(city_id) and '.bak' in f]
    if not backups: return None
    # Sort by date suffix (latest first)
    backups.sort(reverse=True)
    return os.path.join(CITIES_DIR, backups[0])

def process():
    total_removed = 0
    total_healed = 0
    total_restored = 0
    affected_cities = set()

    files = sorted([f for f in os.listdir(CITIES_DIR) if f.endswith('.json') and not f.count('.bak')])
    
    for filename in files:
        path = os.path.join(CITIES_DIR, filename)
        city_id = filename.replace('.json', '')
        
        with open(path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except: continue
        
        if not isinstance(data, dict) or 'city' not in data:
            continue
            
        # --- 1. RESTORATION ---
        if not data.get('highlights'):
            backup_path = get_latest_valid_backup(city_id)
            if backup_path:
                print(f"🔄 Restoring {city_id} from {backup_path}")
                with open(backup_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                total_restored += 1
                affected_cities.add(city_id)

        venues = data.get('highlights', [])
        if not venues: continue

        # Count descriptions to identify clones
        descriptions_count = {}
        for v in venues:
            d = v.get('description', '')
            descriptions_count[d] = descriptions_count.get(d, 0) + 1
            
        # --- 2. FILTERING & HEALING ---
        original_count = len(venues)
        cleaned_venues = []
        
        for v in venues:
            if is_fake(v, descriptions_count):
                continue
            
            # Heal description
            old_tr = v.get('description', '')
            old_en = v.get('description_en', '')
            
            v['description'] = heal_description(old_tr)
            v['description_en'] = heal_description(old_en)
            
            if v['description'] != old_tr or v['description_en'] != old_en:
                total_healed += 1
            
            cleaned_venues.append(v)
        
        removed_in_city = original_count - len(cleaned_venues)
        
        # --- 3. HERO IMAGE UPDATE ---
        hero = data.get('heroImage', '')
        if 'storage.googleapis.com' in hero or not hero or 'unsplash.com' not in hero:
            if city_id in PREMIUM_IMAGES:
                data['heroImage'] = PREMIUM_IMAGES[city_id]
        
        if removed_in_city > 0 or total_healed > 0 or total_restored > 0 or data.get('heroImage') != hero:
            data['highlights'] = cleaned_venues
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            total_removed += removed_in_city
            affected_cities.add(city_id)
            
    print(f"\n🚀 CLEANUP COMPLETE")
    print(f"   - Cities Affected: {len(affected_cities)}")
    print(f"   - Venues Removed: {total_removed}")
    print(f"   - Venues Healed: {total_healed}")
    print(f"   - Cities Restored: {total_restored}")

if __name__ == "__main__":
    process()
