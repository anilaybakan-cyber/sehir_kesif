import json
import os

new_cenevre_final = [
    {
        "name": "Boulangerie Pierre & Jean",
        "name_en": "Pierre & Jean Bakery",
        "area": "Eaux-Vives",
        "category": "Kafe",
        "tags": ["fırın", "pastane", "lokal", "taze"],
        "distanceFromCenter": 1.3,
        "lat": 46.2052,
        "lng": 6.1601,
        "price": "medium",
        "rating": 4.8,
        "description": "Eaux-Vives bölgesinin en iyi fırınlarından biri. Fransız usulü çıtır kruvasanları ve özel yapım ekmekleriyle ünlü.",
        "description_en": "One of the best bakeries in Eaux-Vives, famous for its authentic French-style croissants and seasonal pastry selections.",
        "imageUrl": "https://images.unsplash.com/photo-1506764483492-1813517e5735?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Sabah erken saatlerde gidin, kruvasanlar fırından yeni çıktığında muazzamdır.",
        "tips_en": "Go early in the morning to get the pastries while they are still warm; they often sell out by noon."
    },
    {
        "name": "Le Radar de Poche",
        "name_en": "Le Radar de Poche",
        "area": "Vieille Ville",
        "category": "Deneyim",
        "tags": ["gizli", "kitap", "kafe", "bohem"],
        "distanceFromCenter": 0.1,
        "lat": 46.2005,
        "lng": 6.1485,
        "price": "medium",
        "rating": 4.6,
        "description": "Eski şehrin en dar sokaklarından birinde gizlenmiş, kitaplarla dolu, çok samimi ve bohem bir 'gizli' kafe.",
        "description_en": "A hidden, bohemian 'pocket' cafe tucked away in one of the narrowest alleys of the Old Town, perfect for a quiet read.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Farklı ülkelerden gelen nadir dergileri ve kitapları karıştırırken kahvenizi yudumlayın.",
        "tips_en": "Browse through their collection of rare international magazines while enjoying one of the best espressos in the Old Town."
    },
    {
        "name": "Parc Bertrand",
        "name_en": "Bertrand Park",
        "area": "Champel",
        "category": "Park",
        "tags": ["huzur", "yerel", "geniş", "doğa"],
        "distanceFromCenter": 1.5,
        "lat": 46.1925,
        "lng": 6.1555,
        "price": "free",
        "rating": 4.7,
        "description": "Champel bölgesinde, devasa sekoya ağaçlarıyla dolu, turistlerden uzak ve çok huzurlu bir mahalle parkı.",
        "description_en": "A lush, expansive neighborhood park in Champel, known for its giant redwood trees and serene atmosphere away from the tourist crowds.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Parkın içindeki mini kütüphane ve güneşlenme alanları yerellerin favorisidir.",
        "tips_en": "The internal rose garden and the outdoor children's splash pool make it a favorite for local families in the summer."
    },
    {
        "name": "L'Ilôt Sud",
        "name_en": "L'Ilot Sud",
        "area": "Carouge",
        "category": "Deneyim",
        "tags": ["zanaat", "sanat", "atölye", "gizli bahçe"],
        "distanceFromCenter": 2.3,
        "lat": 46.1825,
        "lng": 6.1398,
        "price": "free",
        "rating": 4.5,
        "description": "Carouge'da zanaatkarların toplandığı, avlu içinde gizli bir sanat ve üretim merkezi.",
        "description_en": "A creative hub in Carouge where local artisans maintain workshops; the internal courtyards are full of surprises and craftsmanship.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Hafta içi",
        "bestTime_en": "Weekdays",
        "tips": "Atölyelerin kapıları genellikle açıktır, sanatçıları çalışırken izlemek için nazikçe başınızı uzatabilirsiniz.",
        "tips_en": "Many artists are happy to show their process if you approach respectfully; it's the soul of the Carouge artisanal spirit."
    },
    {
        "name": "La Caravane Passe",
        "name_en": "La Caravane Passe",
        "area": "Plainpalais",
        "category": "Restoran",
        "tags": ["oryantal", "decor", "samimi", "mezze"],
        "distanceFromCenter": 1.0,
        "lat": 46.1955,
        "lng": 6.1435,
        "price": "medium",
        "rating": 4.6,
        "description": "Orta Doğu mutfağını masalsı bir dekorasyon ve harika lezzetlerle sunan, Cenevre'nin en sevilen egzotik restoranlarından biri.",
        "description_en": "An enchanting Middle Eastern restaurant with vibrant decor and excellent mezze plates, offering a warm escape from the Swiss cold.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "bestTime": "Akşam yemeği",
        "bestTime_en": "Dinner",
        "tips": "Paylaşımlı mezze tabakları denemek için en iyi seçenektir.",
        "tips_en": "Their shared platters are famous; it's a very social and relaxed dining experience in the heart of Plainpalais."
    },
    {
        "name": "Bar des Bergues",
        "name_en": "Bar des Bergues",
        "area": "Göl Kenarı",
        "category": "Bar",
        "tags": ["lüks", "klasik", "piano bar", "şık"],
        "distanceFromCenter": 0.3,
        "lat": 46.2062,
        "lng": 6.1468,
        "price": "high",
        "rating": 4.8,
        "description": "Four Seasons otelinin içinde, kentin en şık ve klasik kokteyllerini sunan, piyano eşliğinde vakit geçirebileceğiniz efsanevi bar.",
        "description_en": "Located in the Four Seasons Hotel, this legendary bar offers world-class service, classic cocktails, and a timeless, elegant atmosphere.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Buradaki sıcak çikolata kış aylarında kentin en iyisidir.",
        "tips_en": "Their afternoon tea and hot chocolate are as famous as their evening cocktails; it's the height of Geneva sophistication."
    },
    {
        "name": "Parc Beau-Séjour",
        "name_en": "Beau-Sejour Park",
        "area": "Champel",
        "category": "Park",
        "tags": ["seyir terası", "nehir manzara", "sessiz", "lokal"],
        "distanceFromCenter": 1.8,
        "lat": 46.1905,
        "lng": 6.1510,
        "price": "free",
        "rating": 4.5,
        "description": "Arve nehrine tepeden bakan, muazzam bir seyir terasına sahip, sessiz ve pek bilinmeyen bir park.",
        "description_en": "A quiet, secluded park with a magnificent viewing platform overlooking the Arve river and the cliffs below.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kitabınızı alıp nehir sesini dinleyerek okumak için şehirdeki en huzurlu yerdir.",
        "tips_en": "One of the best 'secret' spots in town for a quiet afternoon with a book, with only the sound of the river below."
    },
    {
        "name": "Taqueria Los Cuates",
        "name_en": "Los Cuates",
        "area": "Pâquis",
        "category": "Restoran",
        "tags": ["meksika", "taco", "samimi", "renkli"],
        "distanceFromCenter": 0.8,
        "lat": 46.2135,
        "lng": 6.1475,
        "price": "medium",
        "rating": 4.5,
        "description": "Cenevre'de gerçek Meksika lezzetlerini bulabileceğiniz, renkli ve çok samimi bir mahalle restoranı.",
        "description_en": "An authentic and vibrant Mexican eatery in Pâquis, popular for its real tacos and lively, unpretentious atmosphere.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Margaritaları oldukça başarılıdır, taco çeşitleri arasından seçim yapmakta zorlanabilirsiniz.",
        "tips_en": "Their margaritas are some of the strongest and best in the city; try the 'Al Pastor' tacos for a real taste of Mexico."
    },
    {
        "name": "Bourse de Genève (Tarihi Bina)",
        "name_en": "Geneva Stock Exchange",
        "area": "Merkez",
        "category": "Tarihi",
        "tags": ["finans", "mimari", "diplomasi", "heybetli"],
        "distanceFromCenter": 0.5,
        "lat": 46.2025,
        "lng": 6.1425,
        "price": "free",
        "rating": 4.2,
        "description": "Cenevre'nin finans merkezi olduğunu hatırlatan, heybetli mimarisiyle dikkat çeken tarihi borsa binası.",
        "description_en": "The imposing historic Stock Exchange building, a symbol of Geneva's significant role in the global financial and diplomatic history.",
        "imageUrl": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Binanın dış cephesindeki detaylı heykel ve işçilikler fotoğrafçılar için ilgi çekicidir.",
        "tips_en": "The facade features intricate sculptures representing trade and industry; it's a great example of the city's 19th-century boom."
    },
    {
        "name": "Le Scandale",
        "name_en": "Le Scandale",
        "area": "Pâquis",
        "category": "Bar",
        "tags": ["trendy", "gece hayatı", "kokteyl", "enerjik"],
        "distanceFromCenter": 0.7,
        "lat": 46.2095,
        "lng": 6.1485,
        "price": "high",
        "rating": 4.3,
        "description": "Pâquis bölgesinin en trend barlarından biri. Yenilikçi kokteylleri ve geç saatlere kadar süren enerjisiyle ünlü.",
        "description_en": "A trendy and vibrant bar in the Pâquis district, famous for its inventive cocktail list and high-energy weekend nights.",
        "imageUrl": "https://images.unsplash.com/photo-1514525253361-bee1a2399222?w=800",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Hafta sonu oldukça kalabalık olabilir, gitmeden önce programı kontrol edin.",
        "tips_en": "The place gets very busy on Friday and Saturday nights; it's one of the hubs for Geneva's younger professional crowd."
    },
    {
        "name": "Quai Gustave-Ador (Güneşlenme Alanı)",
        "name_en": "Quai Gustave-Ador Rocks",
        "area": "Eaux-Vives",
        "category": "Deneyim",
        "tags": ["güneş", "göl", "lokal", "huzur"],
        "distanceFromCenter": 1.0,
        "lat": 46.2065,
        "lng": 6.1615,
        "price": "free",
        "rating": 4.8,
        "description": "Göl üzerindeki büyük kayalıkların üzerine yerleşip güneşlenen yerellerin favori yaz noktası.",
        "description_en": "A favorite local summer spot where people relax on the large rocks along the lake wall, enjoying the sun and easy access for a swim.",
        "imageUrl": "https://images.unsplash.com/photo-1506764483492-1813517e5735?w=800",
        "bestTime": "Yaz öğleden sonra",
        "bestTime_en": "Summer afternoon",
        "tips": "Kendi havlunuzu ve içeceğinizi alıp gidin, gerçek bir Cenevre yazı deneyimi için idealdir.",
        "tips_en": "Bring your own towel and enjoy the best free view of the Jet d'Eau while getting a tan like a local."
    }
]

def enrich_cenevre_final():
    filepath = 'assets/cities/cenevre.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_cenevre_final:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_cenevre_final()
print(f"Geneva now has {count} highlights.")
