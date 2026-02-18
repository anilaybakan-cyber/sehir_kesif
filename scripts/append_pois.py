
import json
import os

cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"

additions = {
    "madrid.json": [
        {
            "name": "Taberna La Bola",
            "area": "Centro",
            "category": "Yeme-İçme",
            "tags": ["cocido", "tarihi", "geleneksel"],
            "distanceFromCenter": 0.5,
            "lat": 40.419,
            "lng": -3.710,
            "price": "medium",
            "rating": 4.6,
            "description": "1870'den beri kömür ateşinde pişen 'Cocido Madrileño' (nohut yemeği) yapan efsane mekan.",
            "description_en": "Legendary place serving 'Cocido Madrileño' (chickpea stew) cooked on charcoal since 1870.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Öğle yemeği",
            "bestTime_en": "Lunch",
            "tips": "Cocido porsiyonu çok büyüktür, aç gidin. Rezervasyon şart."
        },
        {
            "name": "Cerro del Tío Pío",
            "area": "Vallecas",
            "category": "Manzara",
            "tags": ["manzara", "gün batımı", "tepe"],
            "distanceFromCenter": 5.0,
            "lat": 40.395,
            "lng": -3.655,
            "price": "free",
            "rating": 4.7,
            "description": "'Yedi Memeli Park' olarak bilinir. Madrid'in en güzel gün batımı manzarası buradadır.",
            "description_en": "Known as 'Seven Tits Park'. Best sunset view of Madrid is here.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Gün batımı",
            "bestTime_en": "Sunset",
            "tips": "Turistlerden uzak, yerel halkla piknik yapmak için harika."
        },
        {
            "name": "Museo Sorolla",
            "area": "Chamberí",
            "category": "Müze",
            "tags": ["sanat", "bahçe", "ışık"],
            "distanceFromCenter": 2.0,
            "lat": 40.435,
            "lng": -3.692,
            "price": "low",
            "rating": 4.8,
            "description": "Ressam Joaquín Sorolla'nın evi ve atölyesi. Endülüs tarzı bahçesiyle bir vaha.",
            "description_en": "Painter Joaquín Sorolla's house and studio. An oasis with its Andalusian style garden.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Sabah",
            "bestTime_en": "Morning",
            "tips": "Bahçesindeki çeşme sesleri eşliğinde dinlenin."
        }
    ],
    "kopenhag.json": [
        {
            "name": "CopenHill",
            "area": "Amager",
            "category": "Aktivite",
            "tags": ["kayak", "mimari", "manzara"],
            "distanceFromCenter": 3.0,
            "lat": 55.671,
            "lng": 12.617,
            "price": "free",
            "rating": 4.7,
            "description": "Çöp yakma tesisi üzerinde kayak pisti! Çatısında kamp yapabilir veya manzara izleyebilirsiniz.",
            "description_en": "Ski slope on top of waste-to-energy plant! Can hike or enjoy view from roof.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Gündüz",
            "bestTime_en": "Daytime",
            "tips": "Kayak yapmasanız bile çatıya çıkmak ücretsiz. Dünyanın en yüksek tırmanma duvarı burada."
        },
        {
            "name": "Reffen Street Food",
            "area": "Refshaleøen",
            "category": "Yeme-İçme",
            "tags": ["sokak yemeği", "konteyner", "açık hava"],
            "distanceFromCenter": 3.5,
            "lat": 55.693,
            "lng": 12.610,
            "price": "medium",
            "rating": 4.6,
            "description": "İskandinavya'nın en büyük sokak yemeği pazarı. Eski endüstriyel alanda konteynerler.",
            "description_en": "Scandinavia's largest street food market. Containers in old industrial area.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Akşam",
            "bestTime_en": "Evening",
            "tips": "Liman otobüsü (Havnebus) ile denizden gidin. Gün batımı partileri meşhur."
        }
    ],
    "dubai.json": [
        {
            "name": "Alserkal Avenue",
            "area": "Al Quoz",
            "category": "Kültür",
            "tags": ["sanat", "galeri", "hip"],
            "distanceFromCenter": 10.0,
            "lat": 25.141,
            "lng": 55.234,
            "price": "free",
            "rating": 4.6,
            "description": "Dubai'nin sanat bölgesi. Eski depolar galeriye ve hipster kafelere dönüşmüş.",
            "description_en": "Dubai's art district. Old warehouses turned into galleries and hipster cafes.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Öğleden sonra",
            "bestTime_en": "Afternoon",
            "tips": "Mirzam Chocolate Factory'de çikolata yapımını izleyin."
        },
        {
            "name": "Museum of the Future",
            "area": "Trade Centre",
            "category": "Müze",
            "tags": ["gelecek", "teknoloji", "mimari"],
            "distanceFromCenter": 3.0,
            "lat": 25.219,
            "lng": 55.281,
            "price": "high",
            "rating": 4.5,
            "description": "Dünyanın en güzel binalarından biri. Geleceğin teknolojilerini deneyimleyin.",
            "description_en": "One of the most beautiful buildings in the world. Experience future technologies.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Hafta içi",
            "bestTime_en": "Weekday",
            "tips": "Biletler haftalar önceden tükenir, çok önceden alın! Dışarıdan fotoğraf çekmek bedava."
        }
    ],
    "hongkong.json": [
        {
            "name": "M+ Museum",
            "area": "West Kowloon",
            "category": "Müze",
            "tags": ["sanat", "modern", "kültür"],
            "distanceFromCenter": 2.0,
            "lat": 22.301,
            "lng": 114.160,
            "price": "medium",
            "rating": 4.7,
            "description": "Asya'nın ilk küresel görsel kültür müzesi. Devasa LED cephesiyle ünlü.",
            "description_en": "Asia's first global visual culture museum. Famous for huge LED facade.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Öğleden sonra",
            "bestTime_en": "Afternoon",
            "tips": "Terasından Hong Kong silüeti manzarası harika."
        },
        {
            "name": "Tai O Fishing Village",
            "area": "Lantau",
            "category": "Köy",
            "tags": ["balıkçı", "geleneksel", "kazık evler"],
            "distanceFromCenter": 30.0,
            "lat": 22.253,
            "lng": 113.863,
            "price": "free",
            "rating": 4.5,
            "description": "Hong Kong'un Venedik'i. Su üzerindeki kazık evler (pang uk) ve geleneksel yaşam.",
            "description_en": "Venice of Hong Kong. Stilt houses (pang uk) over water and traditional life.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Gündüz",
            "bestTime_en": "Daytime",
            "tips": "Pembe yunusları görmek için tekne turu yapın. Kurutulmuş deniz ürünleri deneyin."
        }
    ],
    "budapeste.json": [
        {
            "name": "Memento Park",
            "area": "Buda",
            "category": "Müze",
            "tags": ["komünizm", "heykel", "tarih"],
            "distanceFromCenter": 10.0,
            "lat": 47.426,
            "lng": 18.998,
            "price": "medium",
            "rating": 4.4,
            "description": "Komünist dönemden kalan devasa heykellerin toplandığı açık hava müzesi.",
            "description_en": "Open air museum displaying gigantic statues from Communist era.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Gündüz",
            "bestTime_en": "Daytime",
            "tips": "Şehir merkezinden günde bir kez direkt otobüs kalkar."
        }
    ],
    "singapur.json": [
        {
            "name": "Pulau Ubin",
            "area": "Ubin",
            "category": "Doğa",
            "tags": ["ada", "kampong", "doğa"],
            "distanceFromCenter": 15.0,
            "lat": 1.412,
            "lng": 103.957,
            "price": "low",
            "rating": 4.7,
            "description": "Singapur'un son geleneksel köyü (kampong). Gökdelenlerden uzak, zaman yolculuğu.",
            "description_en": "Singapore's last traditional village (kampong). Time travel away from skyscrapers.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Sabah erken",
            "bestTime_en": "Early morning",
            "tips": "Changi Point'ten bumboats (tekne) ile geçin. Bisiklet kiralayıp gezin."
        }
    ],
    "viyana.json": [
        {
            "name": "Zentralfriedhof",
            "area": "Simmering",
            "category": "Tarihi",
            "tags": ["mezarlık", "beethoven", "huzur"],
            "distanceFromCenter": 6.0,
            "lat": 48.150,
            "lng": 16.442,
            "price": "free",
            "rating": 4.6,
            "description": "Avrupa'nın en büyük mezarlıklarından biri. Beethoven, Schubert, Strauss ve Brahms burada yatıyor.",
            "description_en": "One of Europe's largest cemeteries. Beethoven, Schubert, Strauss and Brahms rest here.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Gündüz",
            "bestTime_en": "Daytime",
            "tips": "Müzisyenler bölümü (Ehrengräber) 32A grubundadır."
        }
    ]
}

def append_pois():
    for filename, new_pois in additions.items():
        filepath = os.path.join(cities_dir, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            # Check if POIs already exist by name
            existing_names = {poi['name'] for poi in data['highlights']}
            added_count = 0
            
            for poi in new_pois:
                if poi['name'] not in existing_names:
                    data['highlights'].append(poi)
                    added_count += 1
            
            if added_count > 0:
                with open(filepath, 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"{filename}: Added {added_count} new POIs. Total: {len(data['highlights'])}")
            else:
                print(f"{filename}: No new POIs added (already exist).")
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    append_pois()
