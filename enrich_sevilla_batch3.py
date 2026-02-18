import json
import os

new_highlights_batch3 = [
    {
        "name": "Plaza de la Alfalfa",
        "name_en": "Alfalfa Square",
        "area": "Centro",
        "category": "Tarihi",
        "tags": ["meydan", "lokal", "aile"],
        "distanceFromCenter": 0.4,
        "lat": 37.391,
        "lng": -5.99,
        "price": "free",
        "rating": 4.5,
        "description": "Sevilla'nın en otantik meydanlarından biri. Çocuk parkı, kafeleri ve her daim canlı mahalle atmosferiyle gerçek bir Sevilla klasiği.",
        "description_en": "One of Seville's most authentic squares. A classic spot with a playground, cafes, and a constantly lively neighborhood atmosphere.",
        "imageUrl": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=800",
        "bestTime": "Akşamüstü",
        "bestTime_en": "Late afternoon",
        "tips": "Meydandaki küçük barlarda tapas yerken mahalle hayatını izleyin.",
        "tips_en": "Watch neighborhood life while enjoying tapas at the small bars in the square."
    },
    {
        "name": "Pabellón de Marruecos",
        "name_en": "Moroccan Pavilion",
        "area": "Cartuja",
        "category": "Müze",
        "tags": ["sanat", "kültür", "oriental"],
        "distanceFromCenter": 1.7,
        "lat": 37.4,
        "lng": -6.0,
        "price": "low",
        "rating": 4.7,
        "description": "Üç Kültür Vakfı'na ev sahipliği yapan ve Fas mimarisinin en zarif örneklerini sunan bina. Sevilla'nın oryantalist yüzü.",
        "description_en": "The building housing the Foundation of Three Cultures, showcasing the most elegant examples of Moroccan architecture in Seville.",
        "imageUrl": "https://images.unsplash.com/photo-1598449419142-2d1033069315?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "İçerideki ahşap oymaları ve mozaikleri mutlaka görün.",
        "tips_en": "Be sure to see the wood carvings and mosaics inside."
    },
    {
        "name": "Puente de la Barqueta",
        "name_en": "Barqueta Bridge",
        "area": "Macarena / Cartuja",
        "category": "Manzara",
        "tags": ["köprü", "mimari", "nehir"],
        "distanceFromCenter": 1.5,
        "lat": 37.404,
        "lng": -6.0,
        "price": "free",
        "rating": 4.3,
        "description": "Expo '92 için tasarlanan bir diğer estetik köprü. Modern tasarımı ile nehir üzerinde asılı duran dev bir yay gibi görünür.",
        "description_en": "Another aesthetic bridge designed for Expo '92. With its modern design, it looks like a giant bow suspended over the river.",
        "imageUrl": "https://images.unsplash.com/photo-1550522433-281b37494cc1?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Altındaki yolda yürüyüş yaparak köprünün açısını yakalayabilirsiniz.",
        "tips_en": "Walk along the path beneath to catch the best angles of the bridge."
    },
    {
        "name": "Jeronimó",
        "name_en": "Jeronimo",
        "area": "Centro",
        "category": "Kafe",
        "tags": ["fırın", "pastane", "kahvaltı"],
        "distanceFromCenter": 0.5,
        "lat": 37.389,
        "lng": -5.991,
        "price": "low",
        "rating": 4.7,
        "description": "Geleneksel Sevilla tatlılarını modern bir dokunuşla sunan butik pastane ve kafe. Kruvasanları ve yerel hamur işleri meşhurdur.",
        "description_en": "A boutique bakery and cafe offering traditional Sevillian sweets with a modern twist, famous for its croissants and local pastries.",
        "imageUrl": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Hafta sonları kapısında uzun kuyruklar olabilir, erken gitmekte fayda var.",
        "tips_en": "Expect long queues on weekends, so it's best to go early."
    },
    {
        "name": "Mercado de San Jorge",
        "name_en": "San Jorge Market",
        "area": "Triana",
        "category": "Alışveriş",
        "tags": ["pazar", "lezzet", "triana"],
        "distanceFromCenter": 1.0,
        "lat": 37.385,
        "lng": -6.003,
        "price": "low",
        "rating": 4.4,
        "description": "Triana Köprüsü'nün hemen yanında, yerel ürünlerin ve taze deniz ürünlerinin bulunduğu otantik pazar yeri.",
        "description_en": "An authentic marketplace next to the Triana Bridge, featuring local produce and fresh seafood.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Pazarın içindeki küçük barlarda taze balık tapaslarını deneyin.",
        "tips_en": "Try the fresh fish tapas at the small bars inside the market."
    },
    {
        "name": "Prado de San Sebastián",
        "name_en": "Prado de San Sebastian",
        "area": "Centro",
        "category": "Park",
        "tags": ["park", "etkinlik", "meydan"],
        "distanceFromCenter": 0.7,
        "lat": 37.379,
        "lng": -5.989,
        "price": "free",
        "rating": 4.3,
        "description": "Otobüs terminalinin yanında yer alan ve yıl boyu festivallere, buz pateni pistlerine (kışın) ev sahipliği yapan geniş park alanı.",
        "description_en": "A wide park area next to the bus terminal that hosts festivals and ice rinks (in winter) throughout the year.",
        "imageUrl": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=800",
        "bestTime": "Her zaman",
        "bestTime_en": "Anytime",
        "tips": "Feria de Abril zamanı burası şehrin kalbinin attığı yerdir.",
        "tips_en": "During the Feria de Abril, this is where the heart of the city beats."
    },
    {
        "name": "Parque de los Príncipes",
        "name_en": "Princes Park",
        "area": "Los Remedios",
        "category": "Park",
        "tags": ["park", "spor", "göl"],
        "distanceFromCenter": 1.5,
        "lat": 37.375,
        "lng": -6.002,
        "price": "free",
        "rating": 4.4,
        "description": "Los Remedios mahallesinde yer alan, büyük göleti ve spor alanlarıyla bilinen huzurlu yerel park.",
        "description_en": "A peaceful local park in the Los Remedios neighborhood, known for its large pond and sports areas.",
        "imageUrl": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=800",
        "bestTime": "Hafta sonu",
        "bestTime_en": "Weekend",
        "tips": "Ördekleri izlemek ve yerel halkla birlikte koşu yapmak için harika bir yer.",
        "tips_en": "A great place for birdwatching or going for a run with the locals."
    },
    {
        "name": "Jardines del Valle",
        "name_en": "Valle Gardens",
        "area": "Centro",
        "category": "Park",
        "tags": ["gizli", "bahçe", "sur"],
        "distanceFromCenter": 0.8,
        "lat": 37.394,
        "lng": -5.985,
        "price": "free",
        "rating": 4.5,
        "description": "Eski şehir surlarının kalıntılarını içinde barındıran, turistler tarafından az bilinen çok huzurlu bir gizli bahçe.",
        "description_en": "A peaceful hidden garden containing ruins of the old city walls, little known by tourists.",
        "imageUrl": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Sur kalıntıları boyunca yürüyüp sessizliğin tadını çıkarın.",
        "tips_en": "Walk along the wall ruins and enjoy the silence."
    },
    {
        "name": "Puente de San Telmo",
        "name_en": "San Telmo Bridge",
        "area": "Centro / Triana",
        "category": "Manzara",
        "tags": ["köprü", "manzara", "nehir"],
        "distanceFromCenter": 0.6,
        "lat": 37.382,
        "lng": -5.994,
        "price": "free",
        "rating": 4.6,
        "description": "Torre del Oro ile Triana'yı birbirine bağlayan, nehrin en güzel perspektiflerinden birini sunan köprü.",
        "description_en": "The bridge connecting Torre del Oro and Triana, offering one of the best perspectives of the river.",
        "imageUrl": "https://images.unsplash.com/photo-1550522433-281b37494cc1?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Köprü üzerinden Giralda ve Torre del Oro'nun aynı kareye sığdığı fotoğraflar çekebilirsiniz.",
        "tips_en": "From the bridge, you can snap photos that frame both the Giralda and Torre del Oro."
    },
    {
        "name": "Bar El Garlochi",
        "name_en": "Bar El Garlochi",
        "area": "Centro",
        "category": "Bar",
        "tags": ["dini", "kokteyl", "deneyim"],
        "distanceFromCenter": 0.7,
        "lat": 37.391,
        "lng": -5.989,
        "price": "medium",
        "rating": 4.6,
        "description": "Kutsal Hafta temalı kitsch dekorasyonuyla meşhur, Sevilla'nın en ikonik ve 'garip' barlarından biri.",
        "description_en": "One of Seville's most iconic and 'quirky' bars, famous for its Holy Week-themed kitsch decor.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "'Sangre de Cristo' kokteylini içmeden Sevilla'dan ayrılmayın.",
        "tips_en": "Don't leave Seville without trying the 'Sangre de Cristo' cocktail."
    }
]

def enrich_city_batch3(city_file):
    filepath = os.path.join('assets/cities', city_file)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'] for h in data.get('highlights', []))
    for new_h in new_highlights_batch3:
        if new_h['name'] not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

new_count = enrich_city_batch3('sevilla.json')
print(f"Sevilla now has {new_count} highlights.")
