import json
import os

new_milano_final_fix = [
    {
        "name": "Museo Nazionale Scienza e Tecnologia Leonardo da Vinci",
        "name_en": "Leonardo da Vinci Science and Technology Museum",
        "area": "Sant'Ambrogio",
        "category": "Müze",
        "tags": ["da vinci", "teknoloji", "bilim", "denizaltı"],
        "distanceFromCenter": 1.6,
        "lat": 45.4627,
        "lng": 9.1706,
        "price": "medium",
        "rating": 4.6,
        "description": "Leonardo da Vinci'nin makinelerinden denizaltılara kadar uzanan, İtalya'nın en büyük bilim ve teknoloji müzesi.",
        "description_en": "The largest science and technology museum in Italy, featuring a large collection of models based on Leonardo da Vinci's drawings."
    },
    {
        "name": "Piazza San Fedele",
        "name_en": "San Fedele Square",
        "area": "Centro",
        "category": "Tarihi",
        "tags": ["heykel", "kilise", "meydan", "merkezi"],
        "distanceFromCenter": 0.2,
        "lat": 45.4655,
        "lng": 9.1912,
        "price": "free",
        "rating": 4.5,
        "description": "Duomo ile La Scala arasında yer alan, Alessandro Manzoni heykeli ve tarihi kilisesiyle bilinen asil bir meydan.",
        "description_en": "An elegant square between the Duomo and La Scala, home to the statue of Alessandro Manzoni and a beautiful Jesuit church."
    },
    {
        "name": "Teatro alla Scala (Müze)",
        "name_en": "La Scala Museum",
        "area": "Centro",
        "category": "Müze",
        "tags": ["opera", "tiyatro", "kostüm", "tarih"],
        "distanceFromCenter": 0.2,
        "lat": 45.4675,
        "lng": 9.1895,
        "price": "medium",
        "rating": 4.7,
        "description": "Dünyanın en ünlü opera binasının tarihini, kostümlerini ve sahne arkası hikayelerini sergileyen büyüleyici bir müze.",
        "description_en": "A fascinating museum dedicated to the history of the world-famous opera house, showcasing stage costumes and musical artifacts."
    }
]

def enrich_milano_final_fix():
    filepath = 'assets/cities/milano.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_milano_final_fix:
        if new_h['name'].lower() not in existing_names:
             new_h['imageUrl'] = "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800"
             new_h['bestTime'] = "Gündüz"
             new_h['bestTime_en'] = "Daytime"
             new_h['tips'] = "Mutlaka görün."
             new_h['tips_en'] = "A must see."
             data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_milano_final_fix()
print(f"Milan now has {count} highlights.")
