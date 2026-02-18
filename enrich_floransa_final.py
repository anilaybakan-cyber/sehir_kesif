import json
import os

extra_10 = [
    {
        "name": "Mercato delle Cascine",
        "name_en": "Cascine Market",
        "area": "Cascine Park",
        "category": "Alışveriş",
        "tags": ["pazar", "yerel", "ucuz", "giyim"],
        "distanceFromCenter": 2.2,
        "lat": 43.7800,
        "lng": 11.2300,
        "price": "low",
        "rating": 4.1,
        "description": "Her Salı sabahı Cascine Parkı'nda kurulan, Floransa'nın en büyük ve en ucuz yerel pazarı. Giyimden mutfak eşyalarına kadar her şeyi bulabilirsiniz.",
        "description_en": "Florence's largest and cheapest local market, held every Tuesday morning in Cascine Park. Offers everything from clothing to household goods.",
        "imageUrl": "https://images.unsplash.com/photo-1544333346-bf0375179462?w=800",
        "bestTime": "Salı sabah (08:00 - 13:00)",
        "bestTime_en": "Tuesday morning (08:00 - 13:00)",
        "tips": "Gerçekten çok büyüktür, rahat ayakkabı giyin ve kalabalığa hazır olun.",
        "tips_en": "It's enormous; wear comfortable shoes and be prepared for large crowds."
    },
    {
        "name": "Museo Nazionale del Bargello (Donatello David)",
        "name_en": "Bargello - Donatello David",
        "area": "San Firenze",
        "category": "Müze",
        "tags": ["heykel", "david", "rönesans", "tarih"],
        "distanceFromCenter": 0.3,
        "lat": 43.7704,
        "lng": 11.2582,
        "price": "medium",
        "rating": 4.8,
        "description": "Donatello'nun çığır açan bronz 'David' heykelinin evi. Rönesans heykel sanatının en önemli parçalarından biri buradadır.",
        "description_en": "The home of Donatello's groundbreaking bronze 'David', one of the most significant works of early Renaissance sculpture.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Ghiberti ve Brunelleschi'nin katedral kapıları için yaptıkları orjinal yarışma panoları da buradadır.",
        "tips_en": "Contains the original competition panels for the Baptistery doors by Ghiberti and Brunelleschi."
    },
    {
        "name": "Gelateria dei Neri (Via dei Neri)",
        "name_en": "Gelateria dei Neri 2",
        "area": "Santa Croce",
        "category": "Kafe",
        "tags": ["dondurma", "lokal", "favori", "kalite"],
        "distanceFromCenter": 0.4,
        "lat": 43.7686,
        "lng": 11.2612,
        "price": "low",
        "rating": 4.7,
        "description": "Uffizi ve Santa Croce arasında yer alan, hem klasik hem de yenilikçi tatlarıyla (karamel-tuzlu peynir gibi) ün yapmış dondurmacı.",
        "description_en": "A highly popular gelateria between Uffizi and Santa Croce, famous for both traditional and creative artisan flavors.",
        "imageUrl": "https://images.unsplash.com/photo-1506764483492-1813517e5735?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Çikolata çeşitleri ve meyveli sorbeleri oldukça yoğundur, mutlaka deneyin.",
        "tips_en": "Their chocolate selections and fruit sorbets are incredibly intense and delicious."
    },
    {
        "name": "Santo Spirito Pazarı",
        "name_en": "Santo Spirito Market",
        "area": "Oltrarno",
        "category": "Alışveriş",
        "tags": ["pazar", "lokal", "antika", "organik"],
        "distanceFromCenter": 0.6,
        "lat": 43.7672,
        "lng": 11.2482,
        "price": "low",
        "rating": 4.5,
        "description": "Meydanda kurulan, bazen antika bazen de yerel üreticilerin organik ürünlerini sattığı hareketli ve çok renkli bir mahalle pazarı.",
        "description_en": "A vibrant neighborhood market in the square, alternating between antiques and local organic food producers.",
        "imageUrl": "https://images.unsplash.com/photo-1473951574080-01fe45ec8643?w=800",
        "bestTime": "Hafta sonu sabah",
        "bestTime_en": "Weekend morning",
        "tips": "Ayın her Pazar günü farklı bir tema (antika, el sanatları vb.) olabilir, önceden kontrol edin.",
        "tips_en": "Themes change depending on which Sunday of the month it is; check ahead for antiques or crafts."
    },
    {
        "name": "La Terrazza (Hotel Continentale)",
        "name_en": "La Terrazza Rooftop",
        "area": "Centro Storico",
        "category": "Manzara",
        "tags": ["rooftop", "kokteyl", "lüks", "ponte vecchio"],
        "distanceFromCenter": 0.3,
        "lat": 43.7685,
        "lng": 11.2533,
        "price": "high",
        "rating": 4.6,
        "description": "Ponte Vecchio'ya tam tepeden bakan, Orta Çağ kulesi üzerine kurulu, şehrin en şık ve özel rooftop barı.",
        "description_en": "An exclusive rooftop bar on top of a medieval tower, offering direct views down onto the Ponte Vecchio.",
        "imageUrl": "https://images.unsplash.com/photo-1514525253361-bee1a2399222?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Rezervasyon şarttır; akşamüzeri aperitivo için en şık ve manzaralı adrestir.",
        "tips_en": "Reservations are essential; it's the most stylish spot in town for a sunset aperitivo."
    },
    {
        "name": "Biblioteca Medicea Laurenziana",
        "name_en": "Laurentian Library",
        "area": "San Lorenzo",
        "category": "Tarihi",
        "tags": ["michelangelo", "kütüphane", "mimari", "medici"],
        "distanceFromCenter": 0.3,
        "lat": 43.7748,
        "lng": 11.2538,
        "price": "medium",
        "rating": 4.8,
        "description": "Michelangelo tarafından tasarlanan muhteşem merdivenleri ve okuma salonuyla, mimari tarihin en önemli yapılarından biri.",
        "description_en": "Designed by Michelangelo, this library features a revolutionary staircase and reading room that changed the course of architecture.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Merdivenli giriş holündeki (vestibule) oranlar ve tasarım Michelangelo'nun ustalığını yansıtır.",
        "tips_en": "The entrance vestibule is a masterpiece of Mannerist architecture; study the pillars and stairs closely."
    },
    {
        "name": "Gucci Garden Galleria",
        "name_en": "Gucci Galleria",
        "area": "Piazza della Signoria",
        "category": "Müze",
        "tags": ["moda", "sanat", "sergi", "gucci"],
        "distanceFromCenter": 0.2,
        "lat": 43.7697,
        "lng": 11.2568,
        "price": "medium",
        "rating": 4.5,
        "description": "Gucci'nin zengin arşivini modern ve sanatsal bir dille sunan, her odası farklı bir konseptle tasarlanmış galeri.",
        "description_en": "A series of themed rooms presenting a rich archive of Gucci designs in a modern, artistic, and immersive way.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Müze gezinizden sonra alt kattaki butik ve dükkan bölümündeki özel tasarım ürünlere göz atın.",
        "tips_en": "Browse the unique range of objects and accessories in the ground-floor store after your visit."
    },
    {
        "name": "Mercato Nuovo (Hasır Pazarı)",
        "name_en": "Straw Market Loggia",
        "area": "Centro Storico",
        "category": "Alışveriş",
        "tags": ["hasır", "hediyelik", "tarihi", "avlu"],
        "distanceFromCenter": 0.2,
        "lat": 43.7698,
        "lng": 11.2537,
        "price": "medium",
        "rating": 4.2,
        "description": "Geleneksel Floransa hasır şapkalarının ve el sanatlarının satıldığı, tarihi Loggia yapısı içindeki pazar.",
        "description_en": "A historic market loggia where traditional Florentine straw work and local crafts have been sold for centuries.",
        "imageUrl": "https://images.unsplash.com/photo-1544333346-bf0375179462?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Burada satılan ipek eşarplar ve goblen yastık kılıfları güzel birer hediye seçeneğidir.",
        "tips_en": "The silk scarves and tapestry-style bags here make for beautiful and traditional souvenirs."
    },
    {
        "name": "La Rinascente Rooftop",
        "name_en": "La Rinascente Rooftop",
        "area": "Piazza della Repubblica",
        "category": "Manzara",
        "tags": ["rooftop", "manzara", "kafe", "lüks"],
        "distanceFromCenter": 0.1,
        "lat": 43.7712,
        "lng": 11.2541,
        "price": "medium",
        "rating": 4.6,
        "description": "Alışveriş merkezinin en üst katında, Duomo kubbesini neredeyse dokunacak kadar yakın hissedeceğiniz muhteşem bir teras kafe.",
        "description_en": "A rooftop cafe atop the department store offering incredibly close views of the Cathedral dome and the square below.",
        "imageUrl": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800",
        "bestTime": "Gündüz veya Akşamüstü",
        "bestTime_en": "Daytime or late afternoon",
        "tips": "Meydandan asansörle en üst kata çıktığınızda sizi karşılayacak olan panorama büyüleyicidir.",
        "tips_en": "Take the elevator to the top floor for an instant panoramic reward that is hard to beat."
    },
    {
        "name": "Porcellino (Bronz Domuz)",
        "name_en": "Porcellino Bronze Boar",
        "area": "Centro Storico",
        "category": "Tarihi",
        "tags": ["heykel", "gelenek", "ücretsiz", "pazar"],
        "distanceFromCenter": 0.2,
        "lat": 43.7696,
        "lng": 11.2536,
        "price": "free",
        "rating": 4.6,
        "description": "Tüm turistlerin dilek dilemek için burnunu parlattığı, Floransa'nın en meşhur bronz heykellerinden biri.",
        "description_en": "Florence's iconic bronze boar statue; locals and tourists alike rub its snout for a wish and to return to the city.",
        "imageUrl": "https://images.unsplash.com/photo-1544333346-bf0375179462?w=800",
        "bestTime": "Her zaman",
        "bestTime_en": "Anytime",
        "tips": "Heykelin burnu, binlerce dokunuş nedeniyle artık altın gibi parlamaktadır.",
        "tips_en": "The snout is polished to a golden shine after centuries of people rubbing it for good luck."
    }
]

def enrich_floransa_final():
    filepath = 'assets/cities/floransa.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in extra_10:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_floransa_final()
print(f"Floransa reached {count} highlights.")
