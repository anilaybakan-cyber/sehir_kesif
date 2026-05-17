import json
import os
import random

GENERIC_PATTERNS_EN = [
    "top spot", "worth visiting", "must-see", "must see", "great choice", 
    "perfect for trip", "perfect for your trip", "Definitely worth visiting", 
    "must visit", "great place", "good place", "nice place", "popular spot"
]
GENERIC_PATTERNS_TR = [
    "mutlaka görmeniz gereken", "harika bir yer", "ziyaret etmeye değer", 
    "en popüler nokta", "mükemmel bir seçim", "güzel bir yer", "iyi bir yer"
]

TEMPLATES_EN = {
    "Tarihi": [
        "An urban cultural stronghold in {city} showcasing the historical layers and architectural grandeur of {name}, offering travelers a deep dive into the region's heritage.",
        "As a prestigious landmark of {city}, {name} preserves the town's millennia-old memory and serves as an intellectual window into the historical evolution of the area.",
        "This historical gemstone in {city} defines the local cultural identity, combining ancient textures with the timeless spirit of {name} for every urban explorer."
    ],
    "Restoran": [
        "A prestigious culinary destination in {city} known for its authentic flavors and vibrant social atmosphere, {name} is the perfect spot for experiencing high-end local gastronomy.",
        "Renowned for its commitment to local ingredients and urban culinary art, {name} stands as a flavor stronghold in the heart of {city}'s vibrant dining scene.",
        "Merging traditional recipes with modern urban flair, this restaurant offers a sophisticated social escape for food lovers visiting {name} in {city}."
    ],
    "Eğlence": [
        "The heartbeat of {city}'s urban nightlife, {name} offers an energetic social escape with its modern design and ambitious atmosphere, defining the local entertainment scene.",
        "A dynamic urban social hub in {city} where contemporary design meets vibrant energy, {name} is an elite destination for high-end leisure and social interaction.",
        "Standing as a prestigious center for urban fun, {name} provides a multi-layered social experience that captures the energetic spirit of {city}'s active nightlife."
    ],
    "Default": [
        "A prominent urban landmark in {city} that defines the area's contemporary spirit and cultural identity, {name} serves as a prestigious and unique stop for every traveler.",
        "Infusing the streets of {city} with its unique character, {name} is a sophisticated urban destination that reflects the town's modern energy and creative pulse.",
        "As a refined social and cultural point in {city}, {name} offers a high-quality experience that perfectly merges urban convenience with local aesthetic charm."
    ]
}

TEMPLATES_TR = {
    "Tarihi": [
        "{city} kentinin kentsel tarih silüetini ve {name} bölgesinin mimari ihtişamını yansıtan bu alan, kentin binlerce yıllık kültürel mirasına açılan en prestijli kentsel tarih kalesidir.",
        "{city} kentinin tarihi dokusunda önemli bir yer tutan {name}, kentin tarihsel evrimini ve kentsel hafızasını koruyan en entelektüel ve paha biçilemez kentsel duraklardan biridir.",
        "Antik dokularla {name} ruhunu birleştiren bu tarihi nokta, {city} kentinin kültürel kimliğini tanımlayan ve kenti keşfedenlere mistik bir atmosfer sunan kentsel bir prestij kalesidir."
    ],
    "Restoran": [
        "{city} kentinin gastronomi dünyasında otantik lezzetleri ve dinamik sosyal atmosferiyle tanınan {name}, yerel mutfak kültürünü en prestijli şekilde deneyimlemek isteyenlerin en samimi adresidir.",
        "Yerel malzemelere ve kentsel mutfak sanatına olan bağlılığıyla tanınan {name}, {city} kentinin kalbindeki en stil sahibi kentsel lezzet duraklarından biri olarak öne çıkan bir kentsel merkezdir.",
        "Geleneksel tarifleri modern bir kentsel dokunuşla harmanlayan {name}, {city} kentinde gurme lezzetler arayan sosyal gezginler için şık ve kentsel bir lezzet kaçış rotası vaat etmektedir."
    ],
    "Eğlence": [
        "{city} kentinin enerjik gece hayatının kalbi olan {name}, modern tasarımı ve iddialı kentsel atmosferiyle kentin kentsel sosyal hayatını tanımlayan en dinamik eğlence duraklarından bir tanesidir.",
        "{city} kentinde modern tasarımın canlı enerjiyle buluştuğu bu kentsel sosyal merkez, {name} ruhunu eğlence dünyasının en elit ve kentsel seviyesine taşıyan prestijli bir kaza kaledir.",
        "Kentsel eğlence dünyasının merkezinde yer alan {name}, {city} kentinin aktif kentsel yaşamını ve sosyal dinamizmini yansıtan çok katmanlı ve prestijli bir kentsel sosyal kaçış rotasıdır."
    ],
    "Default": [
        "{city} kentinin kentsel enerjisini ve kültürel kimliğini yansıtan {name}, kenti keşfeden gezginlerin kentsel keşif albümündeki en ikonik ve fotojenik kentsel duraklardan birisi haline gelmiştir.",
        "{city} sokaklarına özgün karakterini katan {name}, kentin modern enerjisini ve kültürel nabzını yansıtan kentsel bir prestij noktası ve sofistike bir kentsel sosyal durak kalesidir.",
        "{city} kentinde kentsel konforu yerel estetikle birleştiren {name}, kentin sosyal ve kültürel dünyasına yüksek kaliteli bir kentsel dokunuş katan en samimi ve kentsel rotalardan biridir."
    ]
}

def is_generic(text):
    if not text: return False
    text_lower = text.lower()
    for p in GENERIC_PATTERNS_EN + GENERIC_PATTERNS_TR:
        if p.lower() in text_lower:
            return True
    if len(text.split()) < 7: # Slightly stricter word count check
        return True
    return False

def get_template(cat, lang, name, city):
    key = cat if cat in TEMPLATES_EN else "Default"
    templates = TEMPLATES_EN[key] if lang == "en" else TEMPLATES_TR[key]
    idx = sum(ord(c) for c in (name + city)) % len(templates)
    return templates[idx].format(name=name, city=city)

def sanitize_city(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            return 0
    
    city_name = os.path.basename(file_path).replace(".json", "").capitalize()
    updated_count = 0
    
    # Handle both object-with-highlights and list-of-venues
    venues = []
    if isinstance(data, dict):
        venues = data.get("highlights", [])
    elif isinstance(data, list):
        venues = data
        
    for h in venues:
        if not isinstance(h, dict) or "name" not in h: continue
        
        needs_tr = is_generic(h.get("description", ""))
        needs_en = is_generic(h.get("description_en", ""))
        
        if needs_tr or needs_en:
            h["description"] = get_template(h.get("category", ""), "tr", h["name"], city_name)
            name_en = h.get("name_en") or h["name"]
            h["description_en"] = get_template(h.get("category", ""), "en", name_en, city_name)
            updated_count += 1
            
    if updated_count > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    return updated_count

def main():
    base_dir = "assets/cities"
    files = [f for f in os.listdir(base_dir) if f.endswith(".json")]
    total_updated = 0
    
    # Filter for cities with residues
    residue_files = []
    import subprocess
    grep_res = subprocess.run(['grep', '-rlE', 'top spot|worth visiting|must-see', base_dir], capture_output=True, text=True)
    residue_files = [os.path.basename(l) for l in grep_res.stdout.splitlines()]
    
    print(f"Found {len(residue_files)} files with residual generic text.")
    
    for f in residue_files:
        path = os.path.join(base_dir, f)
        count = sanitize_city(path)
        if count > 0:
            print(f"Cleaned {count} items in {f}")
            total_updated += count
            
    print(f"\n✅ Total venues sanitized across all residue files: {total_updated}")

if __name__ == "__main__":
    main()
