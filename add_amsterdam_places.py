
import json
import os

file_path = 'assets/cities/amsterdam.json'

new_places = [
    {
        "name": "Poezenboot (Kedi Teknesi)",
        "name_en": "Poezenboot (The Cat Boat)",
        "area": "Centrum",
        "category": "Deneyim",
        "tags": ["kedi", "tekne", "yardım", "barınak"],
        "distanceFromCenter": 0.8,
        "lat": 52.3792,
        "lng": 4.8917,
        "price": "free",
        "description": "1966'dan beri Singel kanalı üzerinde yüzen, dünyanın tek kedi barınağı-teknesi. Kedileri sevebilir, onlarla vakit geçirebilir ve bağışta bulunabilirsiniz.",
        "description_en": "The world's only floating cat shelter, moored on the Singel canal since 1966. You can pet the cats, spend time with them, and verify donations.",
        "imageUrl": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/amsterdam/poezenboot.jpg",
        "tips": "Ziyaret saatleri kısıtlıdır (genelde 13:00-15:00), gitmeden kontrol edin.",
        "tips_en": "Visiting hours are limited (usually 1:00 PM - 3:00 PM), checks before you go.",
        "rating": 4.6,
        "reviewCount": 3500,
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon"
    },
    {
        "name": "Red Light Secrets",
        "name_en": "Red Light Secrets",
        "area": "Red Light District",
        "category": "Müze",
        "tags": ["müze", "tarih", "kültür", "yetişkin"],
        "distanceFromCenter": 0.6,
        "lat": 52.3740,
        "lng": 4.8995,
        "price": "medium",
        "description": "Kırmızı Fener Mahallesi'nin sırlarını keşfedin. Eski bir genelevde yer alan bu müze, seks işçilerinin dünyasına içeriden, saygılı ve eğitici bir bakış sunuyor.",
        "description_en": "Discover the secrets of the Red Light District. Located in a former brothel, this museum offers an insider, respectful, and educational view into the world of sex workers.",
        "imageUrl": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/amsterdam/red_light_secrets.jpg",
        "tips": "Fotoğraf çekmenin serbest olduğu nadir Red Light mekanlarından biridir.",
        "tips_en": "One of the few places in the Red Light District where photography is allowed.",
        "rating": 4.3,
        "reviewCount": 4200,
        "bestTime": "Akşam",
        "bestTime_en": "Evening"
    }
]

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if "highlights" not in data:
        data["highlights"] = []
        
    # Check if they already exist to avoid duplicates (though grep said no)
    existing_names = [h.get("name") for h in data["highlights"]]
    
    added_count = 0
    for place in new_places:
        if place["name"] not in existing_names:
            # Generate a generic ID just in case
            place["id"] = f"gen_added_{place['name'].replace(' ', '_').lower()}"
            data["highlights"].append(place)
            added_count += 1
            print(f"Added: {place['name']}")
    
    if added_count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Successfully added {added_count} places to {file_path}")
    else:
        print("Places already exist.")

except Exception as e:
    print(f"Error: {e}")
