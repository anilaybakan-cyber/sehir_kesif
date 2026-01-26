import json
import os

extra_5 = [
    {
        "name": "Wat Suthat",
        "name_en": "Wat Suthat",
        "area": "Old City",
        "category": "Tarihi",
        "tags": ["tapınak", "dev salıncak", "mural", "sessiz"],
        "distanceFromCenter": 1.2,
        "lat": 13.7511,
        "lng": 100.5011,
        "price": "low",
        "rating": 4.6,
        "description": "28 adet devasa sütunu ve muhteşem duvar resimleriyle ünlü, Bangkok'un en zarif ve huzurlu tapınaklarından biri.",
        "description_en": "One of the most elegant and tranquil temples in Bangkok, famous for its 28 massive pillars and exquisite 19th-century murals.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Tapınağın hemen dışındaki 'Dev Salıncak' (Giant Swing) Bangkok'un en çok fotoğraflanan noktalarından biridir.",
        "tips_en": "The landmark Giant Swing is located just outside the temple gates, a perfect photo opportunity."
    },
    {
        "name": "Jim Thompson Art Center",
        "name_en": "Jim Thompson Art Center",
        "area": "Pathum Wan",
        "category": "Müze",
        "tags": ["sanat", "çağdaş", "mimari", "kültür"],
        "distanceFromCenter": 3.0,
        "lat": 13.7428,
        "lng": 100.5238,
        "price": "medium",
        "rating": 4.6,
        "description": "Jim Thompson evinin hemen yanında yer alan, çağdaş sanat sergilerine ve kültürel etkinliklere ev sahipliği yapan modern bir sanat merkezi.",
        "description_en": "A state-of-the-art facility next to the historic Jim Thompson House, hosting cutting-edge contemporary art exhibitions and film screenings.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Binanın mimarisi ve teras katındaki manzara şehir fotoğrafçıları için harikadır.",
        "tips_en": "The building's brutalist-inspired architecture and the roof terrace views are phenomenal."
    },
    {
        "name": "Queen Sirikit Museum of Textiles",
        "name_en": "textile Museum",
        "area": "Grand Palace",
        "category": "Müze",
        "tags": ["tekstil", "kıyafet", "ipek", "saray"],
        "distanceFromCenter": 0.1,
        "lat": 13.7515,
        "lng": 100.4915,
        "price": "medium",
        "rating": 4.7,
        "description": "Kraliçe Sirikit'e adanmış, Tayland'ın zengin dokuma mirasını ve kraliyet giysilerini sunan şık bir müze.",
        "description_en": "Located within the Grand Palace grounds, this museum showcases the stunning collection of royal Thai textiles and Queen Sirikit's iconic dresses.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Öğleden önce",
        "bestTime_en": "Late morning",
        "tips": "Old City'nin sıcağından kaçmak için harika, klimalı ve çok modern bir müzedir.",
        "tips_en": "A great place to escape the heat of the Grand Palace as it is fully air-conditioned and highly immersive."
    },
    {
        "name": "Maha Rat Riverside Walkway",
        "name_en": "Maha Rat Walkway",
        "area": "Old City",
        "category": "Manzara",
        "tags": ["nehir yürüyüşü", "gün batımı", "kafe", "dinlenme"],
        "distanceFromCenter": 0.5,
        "lat": 13.7540,
        "lng": 100.4890,
        "price": "free",
        "rating": 4.5,
        "description": "Nehir kıyısı boyunca uzanan, tapınak manzaraları eşliğinde yürüyebileceğiniz ve şık butik kafelere sahip keyifli kordon boyu.",
        "description_en": "A scenic riverside boardwalk offering great views of Wat Arun across the water and filled with trendy cafes and artisanal shops.",
        "imageUrl": "https://images.unsplash.com/photo-1473951574080-01fe45ec8643?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Tha Maharaj terminalindeki kafelerden birinde oturup nehrin manzarasını izlemek paha biçilemezdir.",
        "tips_en": "Perfect for a coffee at Tha Maharaj mall while watching the busy boat traffic on the Chao Phraya."
    },
    {
        "name": "King Power Mahanakhon (Observation Deck)",
        "name_en": "Mahanakhon Deck",
        "area": "Sathorn",
        "category": "Manzara",
        "tags": ["gökdelen", "lüks", "şehir ışıkları", "rooftop"],
        "distanceFromCenter": 4.0,
        "lat": 13.7243,
        "lng": 100.5296,
        "price": "high",
        "rating": 4.5,
        "description": "Şehrin en yüksek noktasında, modern mimarisiyle dikkat çeken King Power Mahanakhon'un manzara terası.",
        "description_en": "The iconic pixelated building of Bangkok, featuring a world-class observation deck and a thrilling glass skywalk.",
        "imageUrl": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Asansördeki 50 saniyelik dijital şovu kaçırmayın, gerçekten etkileyicidir.",
        "tips_en": "The 50-second elevator ride features an immersive digital show that starts the experience on a high note."
    }
]

def enrich_bangkok_final():
    filepath = 'assets/cities/bangkok.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in extra_5:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_bangkok_final()
print(f"Bangkok reached {count} highlights.")
