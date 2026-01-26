import json
import os

new_rome_batch3 = [
    {
        "name": "Teatro di Marcello",
        "name_en": "Theatre of Marcellus",
        "area": "Jewish Ghetto",
        "category": "Tarihi",
        "tags": ["antik", "tiyatro", "roma", "mimarisi"],
        "distanceFromCenter": 1.0,
        "lat": 41.8919,
        "lng": 12.4797,
        "price": "free",
        "rating": 4.6,
        "description": "Kolezyum'a olan benzerliği nedeniyle 'küçük Kolezyum' olarak da adlandırılan, Sezar tarafından başlatılan ve Augustus tarafından bitirilen antik tiyatro.",
        "description_en": "An ancient open-air theatre, started by Caesar and finished by Augustus, often called the 'mini Colosseum' due to its resemblance.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Üst katlarındaki dairelerde hala insanlar yaşamaktadır, dünyadaki en pahalı konutlardan bazılarıdır.",
        "tips_en": "People still live in the apartments on the top floors, some of the most expensive housing in the world."
    },
    {
        "name": "Ara Pacis Augustae",
        "name_en": "Ara Pacis",
        "area": "Merkez",
        "category": "Müze",
        "tags": ["antik", "barış sunağı", "augustus", "modern bina"],
        "distanceFromCenter": 1.5,
        "lat": 41.9061,
        "lng": 12.4764,
        "price": "medium",
        "rating": 4.7,
        "description": "İmparator Augustus'un Roma'ya getirdiği barış onuruna adanmış antik sunak. Richard Meier tasarımı ultra-modern bir cam binada sergilenir.",
        "description_en": "An ancient altar dedicated to the peace brought to Rome by Emperor Augustus. Exhibited in an ultra-modern glass building designed by Richard Meier.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Binanın dışındaki Augustus'un başarılarını anlatan yazıları (Res Gestae) okuyun.",
        "tips_en": "Read the inscriptions describing Augustus's achievements (Res Gestae) outside the building."
    },
    {
        "name": "Centrale Montemartini",
        "name_en": "Centrale Montemartini",
        "area": "Ostiense",
        "category": "Müze",
        "tags": ["antik heykel", "endüstriyel", "kontrast", "santral"],
        "distanceFromCenter": 3.5,
        "lat": 41.8667,
        "lng": 12.4775,
        "price": "medium",
        "rating": 4.8,
        "description": "Eski bir elektrik santralinde sergilenen antik Roma heykelleri. Devasa motorlar ve makineler ile zarif mermer heykellerin yarattığı kontrast büyüleyicidir.",
        "description_en": "Ancient Roman sculptures exhibited in a former power plant. The contrast between massive engines and machinery and elegant marble statues is fascinating.",
        "imageUrl": "https://images.unsplash.com/photo-1499781350541-7783f6c6a0c8?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Roma'nın en az bilinen ama en etkileyici müzelerinden biridir; sakin bir sanat deneyimi sunar.",
        "tips_en": "One of Rome's least known but most impressive museums; offers a quiet art experience."
    },
    {
        "name": "Santa Maria della Vittoria",
        "name_en": "Santa Maria della Vittoria",
        "area": "Via Veneto",
        "category": "Tarihi",
        "tags": ["barok", "bernini", "heykel", "melek"],
        "distanceFromCenter": 1.2,
        "lat": 41.9047,
        "lng": 12.4942,
        "price": "free",
        "rating": 4.8,
        "description": "Bernini'nin en ünlü ve tartışmalı başyapıtlarından biri olan 'Azize Teresa'nın Vecdi' heykelini barındıran muhteşem barok kilise.",
        "description_en": "A magnificent Baroque church housing one of Bernini's most famous and controversial masterpieces, 'The Ecstasy of Saint Teresa'.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Heykelin üzerindeki gizli pencereden düşen doğal ışığın heykeli nasıl canlandırdığını izleyin.",
        "tips_en": "Watch how the natural light falling from a hidden window above the statue brings it to life."
    },
    {
        "name": "Scala Sancta (Kutsal Merdivenler)",
        "name_en": "Holy Stairs",
        "area": "San Giovanni",
        "category": "Tarihi",
        "tags": ["kutsal", "hac", "merdiven", "dini"],
        "distanceFromCenter": 2.5,
        "lat": 41.8875,
        "lng": 12.5061,
        "price": "free",
        "rating": 4.7,
        "description": "Hz. İsa'nın Pontius Pilatus'un önünde yürürken bastığına inanılan 28 mermer basamak. İnananlar bu merdivenleri sadece dizleri üzerinde çıkarlar.",
        "description_en": "The 28 marble steps believed to have been climbed by Jesus on his way to trial before Pontius Pilate. Pilgrims climb these steps only on their knees.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Merdivenlerin en tepesindeki 'Sancta Sanctorum' (Kutsalların Kutsalı) şapelini mutlaka görün.",
        "tips_en": "Be sure to see the 'Sancta Sanctorum' (Holy of Holies) chapel at the very top of the stairs."
    },
    {
        "name": "Basilica di Santa Maria Sopra Minerva",
        "name_en": "Santa Maria Sopra Minerva",
        "area": "Centro Storico",
        "category": "Tarihi",
        "tags": ["gotik", "kilise", "mavi tavan", "heykel"],
        "distanceFromCenter": 0.3,
        "lat": 41.8978,
        "lng": 12.4781,
        "price": "free",
        "rating": 4.8,
        "description": "Roma'nın tek gotik kilisesi. Büyüleyici mavi yıldızlı tavanı ve Bernini'nin kilise önündeki meşhur fil heykeli (Elefante della Minerva) ile ünlüdür.",
        "description_en": "Rome's only Gothic church. Famous for its enchanting blue starry ceiling and Bernini's famous elephant statue (Elefante della Minerva) in front of the church.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "İçeride Michelangelo'nun nadir bir eseri olan İsa heykelini de görebilirsiniz.",
        "tips_en": "Inside, you can also see a rare statue of Christ by Michelangelo."
    },
    {
        "name": "Villa Doria Pamphilj",
        "name_en": "Villa Doria Pamphilj",
        "area": "Gianicolo",
        "category": "Park",
        "tags": ["park", "koşu", "saray", "doğa"],
        "distanceFromCenter": 3.0,
        "lat": 41.8875,
        "lng": 12.4508,
        "price": "free",
        "rating": 4.7,
        "description": "Roma'nın en büyük halka açık parkı. 17. yüzyıldan kalma sarayı, labirent bahçeleri ve geniş yürüyüş yollarıyla doğa içinde huzurlu bir kaçış sunar.",
        "description_en": "Rome's largest public park. Offers a peaceful escape in nature with its 17th-century palace, labyrinth gardens, and extensive walking paths.",
        "imageUrl": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=800",
        "bestTime": "Hafta sonu sabah",
        "bestTime_en": "Weekend morning",
        "tips": "Hafta sonları Romalı ailelerin piknik yaptığı ve çocukların oynadığı en popüler yerlerden biridir.",
        "tips_en": "It's one of the most popular places where Roman families picnic and children play on weekends."
    },
    {
        "name": "Palazzo Altemps",
        "name_en": "Palazzo Altemps",
        "area": "Centro Storico",
        "category": "Müze",
        "tags": ["antik heykel", "rönesans sarayı", "tarih", "sanat"],
        "distanceFromCenter": 0.5,
        "lat": 41.9008,
        "lng": 12.4735,
        "price": "medium",
        "rating": 4.8,
        "description": "Büyüleyici bir Rönesans sarayı içinde sergilenen muazzam antik heykel koleksiyonu. Ludovisi koleksiyonunun en iyi parçaları buradadır.",
        "description_en": "A magnificent collection of ancient sculptures exhibited in a charming Renaissance palace. The best pieces of the Ludovisi collection are here.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Öğleden önce",
        "bestTime_en": "Before noon",
        "tips": "Piazza Navona'nın hemen arkasındadır, turist kalabalığından kaçmak için harika bir sessiz sığınaktır.",
        "tips_en": "Located just behind Piazza Navona, it's a great quiet sanctuary to escape the tourist crowds."
    },
    {
        "name": "National Roman Museum - Palazzo Massimo alle Terme",
        "name_en": "Palazzo Massimo",
        "area": "Termini",
        "category": "Müze",
        "tags": ["antik", "mozaik", "fresk", "sanat"],
        "distanceFromCenter": 1.2,
        "lat": 41.9015,
        "lng": 12.4983,
        "price": "medium",
        "rating": 4.9,
        "description": "Roma'nın en iyi mozaik ve fresk koleksiyonuna sahip müzesi. Antik Roma villalarından kurtarılan inanılmaz duvar resimleri burada sergilenir.",
        "description_en": "A museum with Rome's best collection of mosaics and frescoes. Incredible wall paintings rescued from ancient Roman villas are exhibited here.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Livia'nın Villası'ndan gelen bahçe temalı freskli odayı (Garden Room) mutlaka görün.",
        "tips_en": "Be sure to see the garden-themed frescoed room (Garden Room) from the Villa of Livia."
    },
    {
        "name": "Via Condotti",
        "name_en": "Via Condotti",
        "area": "Centro Storico",
        "category": "Alışveriş",
        "tags": ["lüks", "moda", "butik", "ikonik"],
        "distanceFromCenter": 0.8,
        "lat": 41.9054,
        "lng": 12.4806,
        "price": "high",
        "rating": 4.4,
        "description": "Dünyanın en ünlü lüks alışveriş caddelerinden biri. İtalyan moda devlerinin (Gucci, Prada, Valentino) amiral gemisi mağazalarıyla ünlüdür.",
        "description_en": "One of the world's most famous luxury shopping streets. Known for the flagship stores of Italian fashion giants like Gucci, Prada, and Valentino.",
        "imageUrl": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Caddenin başındaki tarihi Antico Caffè Greco'da bir kahve içip tarihe tanıklık edin.",
        "tips_en": "Have a coffee at the historic Antico Caffè Greco at the start of the street and witness history."
    }
]

def enrich_rome_batch3():
    filepath = 'assets/cities/roma.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'] for h in data.get('highlights', []))
    for new_h in new_rome_batch3:
        if new_h['name'] not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_rome_batch3()
print(f"Rome now has {count} highlights.")
