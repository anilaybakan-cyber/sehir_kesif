import json
import os

extra_5 = [
    {
        "name": "Riddarholmen Kilisesi",
        "name_en": "Riddarholmen Church",
        "area": "Riddarholmen",
        "category": "Tarihi",
        "tags": ["kilise", "kraliyet mezarlığı", "ortaçağ", "gotik"],
        "distanceFromCenter": 0.5,
        "lat": 59.3251,
        "lng": 18.0642,
        "price": "medium",
        "rating": 4.6,
        "description": "Stockholm'ün en eski binalarından biri ve İsveç krallarının geleneksel mezar yeri. Dantel gibi işlenmiş dökme demir kulesiyle şehrin siluetinde hemen tanınır.",
        "description_en": "One of the oldest buildings in Stockholm and the final resting place of Swedish monarchs. Known for its distinctive openwork cast-iron spire.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kilise sadece yaz aylarında ziyarete açıktır; içindeki kraliyet lahitleri oldukça etkileyicidir.",
        "tips_en": "The church is only open during summer months; the royal sarcophagi inside are very impressive."
    },
    {
        "name": "Storkyrkan (Büyük Kilise)",
        "name_en": "Storkyrkan",
        "area": "Gamla Stan",
        "category": "Tarihi",
        "tags": ["katedral", "kraliyet düğünü", "heykel", "tarih"],
        "distanceFromCenter": 0.1,
        "lat": 59.3258,
        "lng": 18.0706,
        "price": "low",
        "rating": 4.5,
        "description": "Stockholm'ün en eski kilisesi ve katedrali. Kraliyet düğünlerine ev sahipliği yapar ve içindeki 'Aziz George ve Ejderha' heykeli dünyaca ünlüdür.",
        "description_en": "The oldest church in Gamla Stan, often used for royal weddings. Home to the world-famous wooden sculpture of Saint George and the Dragon.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kilisenin tuğla gotik mimarisi ve içindeki devasa tablolar sanatseverler için büyüleyicidir.",
        "tips_en": "The brick Gothic architecture and massive paintings inside are a treat for art lovers."
    },
    {
        "name": "Historiska Museet (Tarih Müzesi)",
        "name_en": "Swedish History Museum",
        "area": "Östermalm",
        "category": "Müze",
        "tags": ["viking", "altın", "ortaçağ", "isveç tarihi"],
        "distanceFromCenter": 1.5,
        "lat": 59.3347,
        "lng": 18.0908,
        "price": "medium",
        "rating": 4.7,
        "description": "İskandinavya'nın en büyük Viking koleksiyonlarından birine ve muhteşem bir 'Altın Oda'ya (Guldrummet) ev sahipliği yapan devasa tarih müzesi.",
        "description_en": "Features one of the world's largest Viking collections and the spectacular Gold Room, housing precious Swedish treasures.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Müze bahçesinde yaz aylarında Viking oyunları ve etkinlikleri düzenlenebilir.",
        "tips_en": "The museum courtyard often hosts Viking games and activities during summer."
    },
    {
        "name": "Hallwyl Müzesi",
        "name_en": "Hallwyl Museum",
        "area": "Norrmalm",
        "category": "Müze",
        "tags": ["saray", "koleksiyon", "sanat", "tarihi ev"],
        "distanceFromCenter": 0.5,
        "lat": 59.3333,
        "lng": 18.0744,
        "price": "medium",
        "rating": 4.6,
        "description": "20. yüzyılın başında dondurulmuş gibi duran, inanılmaz lüks bir kontes evi. Gümüş takımlardan tablolara kadar her şey orijinal yerindedir.",
        "description_en": "An incredibly lavish private palace from the early 20th century, preserved exactly as it was. Every object, from silver to paintings, remains in its place.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Evin içindeki modern teknoloji (o dönem için asansör ve banyo gibi) detaylarına dikkat edin.",
        "tips_en": "Look out for the early 20th-century modern conveniences like the elevator and bathrooms."
    },
    {
        "name": "Grona Lund (Lunapark)",
        "name_en": "Gröna Lund",
        "area": "Djurgården",
        "category": "Deneyim",
        "tags": ["lunapark", "adrenalin", "sahil", "konser"],
        "distanceFromCenter": 2.5,
        "lat": 59.3233,
        "lng": 18.0967,
        "price": "high",
        "rating": 4.4,
        "description": "Deniz kıyısında kurulu, 140 yıllık geçmişe sahip Stockholm'ün en eski ve popüler eğlence parkı.",
        "description_en": "Stockholm's beloved seaside amusement park with a 140-year history, offering thrilling rides and summer concerts.",
        "imageUrl": "https://images.unsplash.com/photo-1561580119-967a112c858e?w=800",
        "bestTime": "Yaz akşamı",
        "bestTime_en": "Summer evening",
        "tips": "Giriş için 'Gröna Kortet' alarak sezon boyu konserlere ücretsiz girebilirsiniz (eğer uzun kalacaksanız).",
        "tips_en": "Consider getting a season pass (Gröna Kortet) if you plan on attending multiple concerts over the summer."
    }
]

def enrich_stockholm_final():
    filepath = 'assets/cities/stockholm.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in extra_5:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_stockholm_final()
print(f"Stockholm reached {count} highlights.")
