import json
import os

new_rome_target = [
    {
        "name": "Parco degli Acquedotti",
        "name_en": "Park of the Aqueducts",
        "area": "Appio Claudio",
        "category": "Park",
        "tags": ["antik", "su kemeri", "doğa", "manzara"],
        "distanceFromCenter": 8.0,
        "lat": 41.8483,
        "lng": 12.5617,
        "price": "free",
        "rating": 4.8,
        "description": "Antik Roma'nın devasa su kemerlerinin yeşil bir park içinde yükseldiği, gün batımında büyüleyici bir atmosfere bürünen gizli bir cennet.",
        "description_en": "A hidden paradise where massive ancient Roman aqueducts rise within a green park, taking on an enchanting atmosphere at sunset.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Şehir gürültüsünden kaçıp gerçek antik Roma manzarasını hissetmek için en iyi yerdir.",
        "tips_en": "The best place to escape city noise and feel the true atmosphere of ancient Rome."
    },
    {
        "name": "Garbatella",
        "name_en": "Garbatella",
        "area": "Ostiense",
        "category": "Tarihi",
        "tags": ["mimari", "lokal", "avlu", "karakteristik"],
        "distanceFromCenter": 3.5,
        "lat": 41.8617,
        "lng": 12.4883,
        "price": "free",
        "rating": 4.6,
        "description": "1920'lerde 'bahçe şehir' modeliyle kurulan, kendine özgü mimarisi ve huzurlu iç avlularıyla Roma'nın en karakteristik mahallelerinden biri.",
        "description_en": "One of Rome's most characteristic neighborhoods, established in the 1920s as a 'garden city' with unique architecture and peaceful inner courtyards.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Piazza Benedetto Brin'den başlayarak labirent gibi sokaklarında kaybolun.",
        "tips_en": "Start from Piazza Benedetto Brin and get lost in its labyrinthine streets."
    },
    {
        "name": "Sant'Ivo alla Sapienza",
        "name_en": "Sant'Ivo alla Sapienza",
        "area": "Centro Storico",
        "category": "Tarihi",
        "tags": ["borromini", "barok", "spiral kubbe", "mimari"],
        "distanceFromCenter": 0.3,
        "lat": 41.8981,
        "lng": 12.4747,
        "price": "free",
        "rating": 4.7,
        "description": "Borromini'nin en dahi eserlerinden biri. Helisel (spiral) kubbe yapısıyla barok mimarinin sınırlarını zorlayan eşsiz bir kilise.",
        "description_en": "One of Borromini's most brilliant works. A unique church that pushes the boundaries of Baroque architecture with its helical (spiral) dome structure.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Pazar sabahı (ayinde)",
        "bestTime_en": "Sunday morning (during mass)",
        "tips": "Genellikle sadece Pazar sabahları ziyarete açıktır, planınızı ona göre yapın.",
        "tips_en": "Usually only open to visitors on Sunday mornings; plan accordingly."
    },
    {
        "name": "San Paolo Fuori le Mura (Surların Dışındaki Aziz Pavlus)",
        "name_en": "St. Paul Outside the Walls",
        "area": "Ostiense",
        "category": "Tarihi",
        "tags": ["bazilika", "mozaik", "papalık", "muazzam"],
        "distanceFromCenter": 4.5,
        "lat": 41.8586,
        "lng": 12.4764,
        "price": "free",
        "rating": 4.9,
        "description": "Roma'nın dört büyük papalık bazilikasından biri. İçerideki tüm papaların portreleri ve muazzam revaklı avlusu ile büyüleyicidir.",
        "description_en": "One of Rome's four great papal basilicas. Enchanting with its portraits of all past Popes and its magnificent cloistered courtyard.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kilisenin altındaki Aziz Pavlus'un mezarını ziyaret edebilirsiniz.",
        "tips_en": "You can visit the tomb of Saint Paul located beneath the church."
    },
    {
        "name": "Gianicolo Top Atışı (Il Cannone del Gianicolo)",
        "name_en": "Janiculum Cannon",
        "area": "Gianicolo",
        "category": "Deneyim",
        "tags": ["gelenek", "manzara", "ses", "ücretsiz"],
        "distanceFromCenter": 2.2,
        "lat": 41.8917,
        "lng": 12.4614,
        "price": "free",
        "rating": 4.7,
        "description": "1847'den beri her gün öğle saat 12:00'de patlatılan geleneksel top. Tüm Roma'nın saatini buna göre ayarladığı bir şehir ritüelidir.",
        "description_en": "A traditional cannon fired every day at noon since 1847. A city ritual by which all of Rome once synchronized its time.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Öğle 12:00",
        "bestTime_en": "Noon 12:00",
        "tips": "Tam 12'den birkaç dakika önce orada olun, topun patlama anındaki sarsıntıyı hissedeceksiniz.",
        "tips_en": "Be there a few minutes before 12; you'll feel the shockwave as the cannon fires."
    },
    {
        "name": "Palazzo Colonna",
        "name_en": "Colonna Palace",
        "area": "Piazza Venezia",
        "category": "Müze",
        "tags": ["barok galeri", "saray", "lüks", "sanat"],
        "distanceFromCenter": 0.5,
        "lat": 41.8978,
        "lng": 12.4842,
        "price": "high",
        "rating": 4.9,
        "description": "Roma'nın en büyük ve en görkemli özel saraylarından biri. İçindeki 'Büyük Galeri' barok ihtişamının dünyadaki en yüksek noktasıdır.",
        "description_en": "One of Rome's largest and most magnificent private palaces. The 'Great Gallery' inside is a pinnacle of Baroque splendor.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Cumartesi sabah",
        "bestTime_en": "Saturday morning",
        "tips": "Genellikle sadece Cumartesi sabahları halka açıktır, biletinizi önceden ayırtın.",
        "tips_en": "Usually only open to the public on Saturday mornings; book your tickets in advance."
    }
]

def enrich_rome_target():
    filepath = 'assets/cities/roma.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'] for h in data.get('highlights', []))
    for new_h in new_rome_target:
        if new_h['name'] not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_rome_target()
print(f"Rome reached its target with {count} highlights.")
