import json
import os

new_madrid_final = [
    {
        "name": "Calle de Fuencarral",
        "name_en": "Fuencarral Street",
        "area": "Malasaña / Chueca",
        "category": "Alışveriş",
        "tags": ["alışveriş", "moda", "alternatif", "yaya yolu"],
        "distanceFromCenter": 0.5,
        "lat": 40.4245,
        "lng": -3.7015,
        "price": "medium",
        "rating": 4.6,
        "description": "Madrid'in en popüler yaya alışveriş caddelerinden biri. Alternatif markalar, şık mağazalar ve hareketli atmosferiyle kentin nabzını tutar.",
        "description_en": "One of Madrid's trendiest pedestrian shopping streets, connecting Gran Vía to the Chamberí district, filled with popular brand stores and local boutiques."
    },
    {
        "name": "Plaza de San Ildefonso",
        "name_en": "San Ildefonso Square",
        "area": "Malasaña",
        "category": "Manzara",
        "tags": ["meydan", "teras", "lokal", "sosyal"],
        "distanceFromCenter": 0.7,
        "lat": 40.4255,
        "lng": -3.7025,
        "price": "free",
        "rating": 4.7,
        "description": "Malasaña'nın kalbinde yer alan, gençlerin ve yerlilerin teraslarında vakit geçirdiği, kentin en 'cool' ve samimi meydanlarından biri.",
        "description_en": "A small, atmospheric square in Malasaña that serves as the neighborhood's living room, perfect for people-watching from its many terrace bars."
    },
    {
        "name": "Museo de Historia de Madrid",
        "name_en": "Museum of the History of Madrid",
        "area": "Malasaña",
        "category": "Müze",
        "tags": ["tarih", "mimar", "barok", "şehir"],
        "distanceFromCenter": 0.8,
        "lat": 40.4265,
        "lng": -3.7010,
        "price": "free",
        "rating": 4.6,
        "description": "Muazzam barok kapısıyla ünlü bu müze, Madrid'in 1561'den günümüze kadar olan gelişimini haritalar, resimler ve objelerle anlatır.",
        "description_en": "Famed for its spectacular Baroque doorway, this museum chronicles the history of Madrid since it was chosen as the capital in 1561."
    },
    {
        "name": "Casa de América",
        "name_en": "Casa de America",
        "area": "Centro",
        "category": "Deneyim",
        "tags": ["kültür", "saray", "latin amerika", "sergi"],
        "distanceFromCenter": 0.8,
        "lat": 40.4195,
        "lng": -3.6925,
        "price": "low",
        "rating": 4.7,
        "description": "Cibeles Meydanı'ndaki tarihi Linares Sarayı'nda yer alan, İspanya ile Latin Amerika arasındaki kültürel bağları güçlendiren sergi ve etkinlik merkezi.",
        "description_en": "Located in the ornate Linares Palace, this cultural institution hosts art exhibitions and film screenings focused on Latin American culture."
    },
    {
        "name": "Puerta de Toledo",
        "name_en": "Toledo Gate",
        "area": "La Latina",
        "category": "Tarihi",
        "tags": ["kapı", "anıt", "tarih", "granit"],
        "distanceFromCenter": 1.5,
        "lat": 40.4068,
        "lng": -3.7115,
        "price": "free",
        "rating": 4.5,
        "description": "Madrid'in tarihi giriş kapılarından biri olan, 19. yüzyıl başında kral VII. Fernando anısına granitten yapılmış heybetli zafer takı.",
        "description_en": "A monumental granite triumphal arch built in the early 19th century to commemorate the arrival of King Ferdinand VII to Madrid."
    },
    {
        "name": "Atocha Tren İstasyonu (Tropikal Bahçe)",
        "name_en": "Atocha Station Tropical Garden",
        "area": "Arganzuela",
        "category": "Park",
        "tags": ["istasyon", "botanik", "bahçe", "kapalı"],
        "distanceFromCenter": 1.3,
        "lat": 40.4065,
        "lng": -3.6920,
        "price": "free",
        "rating": 4.8,
        "description": "Madrid'in ana tren istasyonunun kalbinde yer alan, 7000'den fazla tropikal bitkinin bulunduğu muazzam bir kapalı bahçe.",
        "description_en": "A lush tropical palm garden located inside the historic concourse of Madrid's main train station, featuring over 7,000 plants and a turtle pond."
    },
    {
        "name": "Museo Nacional de Antropología",
        "name_en": "National Museum of Anthropology",
        "area": "Retiro",
        "category": "Müze",
        "tags": ["antropoloji", "kültür", "etnografya", "dünya"],
        "distanceFromCenter": 1.4,
        "lat": 40.4078,
        "lng": -3.6895,
        "price": "low",
        "rating": 4.4,
        "description": "Beş kıtadan gelen etnografik ve biyolojik koleksiyonlarla insanlık tarihine ve farklı kültürlere ışık tutan İspanya'nın ilk antropoloji müzesi.",
        "description_en": "The first anthropology museum in Spain, offering a fascinating global view of different cultures through ethnographic and biological collections."
    },
    {
        "name": "Calle de Segovia",
        "name_en": "Segovia Street",
        "area": "Centro / La Latina",
        "category": "Tarihi",
        "tags": ["viyadük", "tarihi sokağı", "yürüyüş", "mimari"],
        "distanceFromCenter": 0.8,
        "lat": 40.4135,
        "lng": -3.7125,
        "price": "free",
        "rating": 4.6,
        "description": "Madrid'in en eski ve dik sokaklarından biri. Ünlü Segovia Viyadüğü'nün altından geçer ve kentin ortaçağ dokusunu hissettirir.",
        "description_en": "One of Madrid's oldest and steepest streets, passing under the grand Segovia Viaduct and offering glimpses of the city's medieval heritage."
    },
    {
        "name": "Palacio de Santa Cruz",
        "name_en": "Santa Cruz Palace",
        "area": "Centro",
        "category": "Tarihi",
        "tags": ["mimari", "diplomasi", "tuğla", "saray"],
        "distanceFromCenter": 0.2,
        "lat": 40.4150,
        "lng": -3.7065,
        "price": "free",
        "rating": 4.5,
        "description": "Plaza Mayor yakınındaki bu kırmızı tuğlalı muazzam bina, İspanya Dışişleri Bakanlığı'na ev sahipliği yapan tarihi bir saraydır.",
        "description_en": "A striking Habsburg-era red brick palace located near Plaza Mayor, currently used as the headquarters for the Spanish Ministry of Foreign Affairs."
    },
    {
        "name": "Ermita de San Antonio de la Florida",
        "name_en": "San Antonio de la Florida Chapel",
        "area": "Moncloa",
        "category": "Tarihi",
        "tags": ["goya", "fresk", "sanat", "şapel"],
        "distanceFromCenter": 2.2,
        "lat": 40.4251,
        "lng": -3.7258,
        "price": "free",
        "rating": 4.8,
        "description": "Goya'nın muazzam tavan fresklerini barındıran ve aynı zamanda büyük ressamın mezarının bulunduğu küçük ama sanat dolu bir şapel.",
        "description_en": "A small chapel famous for housing the magnificent ceiling frescoes by Francisco de Goya, who is also buried within the church."
    },
    {
        "name": "Teatro de la Zarzuela",
        "name_en": "Zarzuela Theatre",
        "area": "Centro",
        "category": "Tarihi",
        "tags": ["operet", "müzik", "kültür", "geleneksel"],
        "distanceFromCenter": 0.7,
        "lat": 40.4172,
        "lng": -3.6970,
        "price": "medium",
        "rating": 4.7,
        "description": "İspanya'nın geleneksel lirik tiyatro türü olan Zarzuela'ya adanmış, kentin kalbinde yer alan tarihi ve zarif tiyatro binası.",
        "description_en": "The world's leading home for Zarzuela, the traditional Spanish lyric-dramatic genre that alternates between spoken and sung scenes."
    },
    {
        "name": "Mercado de Maravillas",
        "name_en": "Maravillas Market",
        "area": "Tetuan",
        "category": "Deneyim",
        "tags": ["market", "lokal", "gastronomi", "gerçek"],
        "distanceFromCenter": 3.8,
        "lat": 40.4495,
        "lng": -3.7050,
        "price": "low",
        "rating": 4.8,
        "description": "Avrupa'nın en büyük belediye pazarlarından biri. Turistlerden uzak, Madridlilerin günlük alışverişini yaptığı gerçek bir gastronomi mabedi.",
        "description_en": "One of the largest municipal markets in Europe, offering an authentic, non-touristy slice of Madrid life with over 200 stalls."
    },
    {
        "name": "Plaza del Dos de Mayo",
        "name_en": "Dos de Mayo Square",
        "area": "Malasaña",
        "category": "Manzara",
        "tags": ["meydan", "tarih", "sosyal", "lokal"],
        "distanceFromCenter": 1.2,
        "lat": 40.4278,
        "lng": -3.7042,
        "price": "free",
        "rating": 4.7,
        "description": "Malasaña'nın kalbi dendiğinde akla gelen ilk yer. Çocuk parkları, teraslar ve bağımsızlık savaşının anısını taşıyan heykeliyle hep canlı.",
        "description_en": "The beating heart of Malasaña, a social square legendary for its role in the 1808 uprising and now the city's favorite spot for an outdoor beer."
    },
    {
        "name": "Real Fábrica de Tapices",
        "name_en": "Royal Tapestry Factory",
        "area": "Retiro / Arganzuela",
        "category": "Müze",
        "tags": ["dokuma", "sanat", "tarih", "atölye"],
        "distanceFromCenter": 1.5,
        "lat": 40.4060,
        "lng": -3.6875,
        "price": "medium",
        "rating": 4.6,
        "description": "300 yıldır kraliyet için halı ve duvar kilimi üreten, geleneksel tekniklerin hala kullanıldığı çalışan bir müze ve atölye.",
        "description_en": "A 300-year-old historic institution that continues to produce hand-woven tapestries and rugs using traditional 18th-century techniques."
    },
    {
        "name": "Pasaje de la Caja de Ahorros",
        "name_en": "Pasaje de la Caja de Ahorros",
        "area": "Centro",
        "category": "Tarihi",
        "tags": ["pasaj", "gizli", "mimari", "geçit"],
        "distanceFromCenter": 0.2,
        "lat": 40.4178,
        "lng": -3.7048,
        "price": "free",
        "rating": 4.4,
        "description": "Puerta del Sol'un çok yakınında, Madridlilerin bile bazen gözden kaçırdığı, şık dükkanları ve nostaljik havasıyla saklı bir pasaj.",
        "description_en": "A small and charming hidden passageway in central Madrid, offering a quiet shortcut and a peek into vintage commercial architecture."
    },
    {
        "name": "Museo Naval de Madrid",
        "name_en": "Naval Museum of Madrid",
        "area": "Retiro / Centro",
        "category": "Müze",
        "tags": ["denizcilik", "tarih", "gemi", "harita"],
        "distanceFromCenter": 0.8,
        "lat": 40.4182,
        "lng": -3.6928,
        "price": "low",
        "rating": 4.7,
        "description": "İspanyol denizcilik tarihinin muazzam bir koleksiyonu. Antik haritalar, gemi modelleri ve denizcilik aletleriyle dolu etkileyici bir müze.",
        "description_en": "Chronicling Spain's rich maritime history, this museum features an incredible collection of ship models and the world's oldest map of the Americas."
    },
    {
        "name": "Parque Enrique Tierno Galván",
        "name_en": "Tierno Galvan Park",
        "area": "Arganzuela",
        "category": "Park",
        "tags": ["planeteryum", "modern", "açık hava", "amfitiyatro"],
        "distanceFromCenter": 2.5,
        "lat": 40.3950,
        "lng": -3.6850,
        "price": "free",
        "rating": 4.5,
        "description": "İçinde Madrid planetaryumunu barındıran, geniş yeşil alanları ve amfitiyatrosuyla kentin güneyinde yer alan modern bir park.",
        "description_en": "A modern park home to the Madrid Planetarium, famous for its amphitheater and open spaces that host outdoor movie screenings in the summer."
    },
    {
        "name": "Museo del Romanticismo",
        "name_en": "Museum of Romanticism",
        "area": "Malasaña / Chueca",
        "category": "Müze",
        "tags": ["romantik", "saray", "dekorasyon", "sanat"],
        "distanceFromCenter": 1.0,
        "lat": 40.4260,
        "lng": -3.6985,
        "price": "low",
        "rating": 4.8,
        "description": "19. yüzyılın romantik yaşam tarzını yansıtan, dantele benzer dekorasyonu ve şık bahçesiyle kentin en duygusal ve güzel müzelerinden biri.",
        "description_en": "A beautifully preserved mansion showcasing the art and daily life of the Romantic period in Spain, complete with a charming secret garden cafe."
    },
    {
        "name": "Calle del Arenal",
        "name_en": "Arenal Street",
        "area": "Centro",
        "category": "Alışveriş",
        "tags": ["yaya yolu", "merkezi", "alışveriş", "tarihi"],
        "distanceFromCenter": 0.2,
        "lat": 40.4170,
        "lng": -3.7060,
        "price": "medium",
        "rating": 4.6,
        "description": "Puerta del Sol ile Opera meydanını bağlayan, hep kalabalık ve canlı olan Madrid'in en meşhur yaya ve alışveriş yollarından biri.",
        "description_en": "A main pedestrian artery of the city, lined with shops and historic churches, and famously house to the museum of the Tooth Fairy mouse, Ratoncito Pérez."
    },
    {
        "name": "Plaza del Humilladero",
        "name_en": "Humilladero Square",
        "area": "La Latina",
        "category": "Manzara",
        "tags": ["meydan", "tapas", "lokal", "tarihi"],
        "distanceFromCenter": 0.8,
        "lat": 40.4110,
        "lng": -3.7120,
        "price": "free",
        "rating": 4.6,
        "description": "La Latina mahallesinin girişinde yer alan, pazar günleri Rastro sonrası tapas için Madridlilerin en sevdiği buluşma noktalarından biri.",
        "description_en": "A lively gateway to the La Latina neighborhood, bustling with energy on Sundays when the 'Rastro' market-goers flock here for afternoon drinks."
    }
]

def enrich_madrid_final():
    filepath = 'assets/cities/madrid.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_madrid_final:
        if new_h['name'].lower() not in existing_names:
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1543783232-af412b852fc7?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_madrid_final()
print(f"Madrid now has {count} highlights.")
