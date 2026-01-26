import json
import os

new_budapest_highlights = [
    {
        "name": "Bálna Budapest",
        "name_en": "Bálna Budapest",
        "area": "Pest",
        "category": "Deneyim",
        "tags": ["mimari", "kültür", "alışveriş", "manzara"],
        "distanceFromCenter": 1.2,
        "lat": 47.4828,
        "lng": 19.0602,
        "price": "low",
        "rating": 4.5,
        "description": "Tuna kıyısında dev bir balığı andıran cam ve çelik konstrüksiyonlu modern yapı. İçinde sanat galerileri, dükkanlar ve nehre nazır harika kafeler bulunur.",
        "description_en": "A modern glass and steel structure on the Danube bank shaped like a whale. It houses art galleries, shops, and wonderful riverside cafes.",
        "imageUrl": "https://images.unsplash.com/photo-1551867633-194f125bddfa?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Terasındaki barlar gün batımı için mükemmeldir.",
        "tips_en": "The terrace bars are perfect for sunset."
    },
    {
        "name": "Gül Baba Türbesi",
        "name_en": "Tomb of Gül Baba",
        "area": "Buda",
        "category": "Tarihi",
        "tags": ["osmanlı", "türbe", "tarihi", "manzara"],
        "distanceFromCenter": 1.8,
        "lat": 47.5160,
        "lng": 19.0349,
        "price": "free",
        "rating": 4.6,
        "description": "Osmanlı döneminden kalma bu türbe, sadece bir anıt değil, aynı zamanda harika gül bahçeleri ve huzurlu bir seyir terası sunan gizli bir mücevherdir.",
        "description_en": "This tomb from the Ottoman era is not just a monument but a hidden gem offering beautiful rose gardens and a peaceful viewing terrace.",
        "imageUrl": "https://images.unsplash.com/photo-1551867633-194f125bddfa?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Türbeye çıkan dik Arnavut kaldırımlı sokak (Gül Baba utca) çok fotojeniktir.",
        "tips_en": "The steep cobblestone street (Gül Baba utca) leading to the tomb is very photogenic."
    },
    {
        "name": "Magyar Zene Háza",
        "name_en": "House of Music Hungary",
        "area": "Városliget",
        "category": "Müze",
        "tags": ["modern mimari", "müzik", "interaktif", "park"],
        "distanceFromCenter": 2.8,
        "lat": 47.5130,
        "lng": 19.0792,
        "price": "medium",
        "rating": 4.9,
        "description": "Sou Fujimoto tarafından tasarlanan ödüllü bina. Doğayla iç içe, çatısı delikli bu modern sanat eseri, müziğin evrimini interaktif sergilerle sunar.",
        "description_en": "An award-winning building designed by Sou Fujimoto. This modern masterpiece with its perforated roof offers an interactive journey through the evolution of music.",
        "imageUrl": "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=1200",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Binanın içindeki 'Ses Küresi' deneyimini mutlaka yaşayın.",
        "tips_en": "Be sure to experience the 'Sound Dome' inside the building."
    },
    {
        "name": "Pálvölgyi Cave",
        "name_en": "Palvolgyi Cave",
        "area": "Buda",
        "category": "Deneyim",
        "tags": ["mağara", "doğa", "macera"],
        "distanceFromCenter": 4.5,
        "lat": 47.5323,
        "lng": 19.0162,
        "price": "medium",
        "rating": 4.7,
        "description": "Budapeşte'nin altındaki devasa mağara ağının bir parçası. Muhteşem damlataş oluşumları ve macera dolu yollarıyla doğa severler için eşsiz.",
        "description_en": "Part of the massive cave network beneath Budapest. Unique for nature lovers with its magnificent dripstone formations and adventurous paths.",
        "imageUrl": "https://images.unsplash.com/photo-1551867633-194f125bddfa?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Mağara içindeki sıcaklık her zaman 11 derecedir, yanınıza hırka alın.",
        "tips_en": "The temperature inside the cave is always 11 degrees; bring a cardigan."
    },
    {
        "name": "Elisabeth Bridge",
        "name_en": "Elisabeth Bridge",
        "area": "Merkez",
        "category": "Manzara",
        "tags": ["köprü", "beyaz", "manzara", "ikonik"],
        "distanceFromCenter": 0.5,
        "lat": 47.4911,
        "lng": 19.0494,
        "price": "free",
        "rating": 4.5,
        "description": "Tuna Nehri üzerindeki en zarif köprülerden biri. Bembeyaz rengi ve modern kablolu yapısıyla Buda ve Pest yakalarını birleştirir.",
        "description_en": "One of the most elegant bridges on the Danube. It connects the Buda and Pest sides with its pure white color and modern cable structure.",
        "imageUrl": "https://images.unsplash.com/photo-1551867633-194f125bddfa?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Buda tarafındaki ayağından Gellért Tepesi'ne çıkan şelaleli yolu takip edebilirsiniz.",
        "tips_en": "You can follow the waterfall path leading up to Gellért Hill from the Buda side of the bridge."
    }
]

# Filler fixes for Budapest
budapest_fillers_fix = {
    "Parlamento": {
        "description": "Dünyanın en görkemli parlamento binalarından biri. 691 odalık Neo-Gotik dev şaheser, Tuna kıyısının tacıdır.",
        "description_en": "One of the world's most magnificent parliament buildings. A 691-room Neo-Gothic masterpiece, crown of the Danube."
    },
    "Széchenyi Termal Hamamı": {
        "description": "Avrupa'nın en büyük termal kompleksi. Sarı neo-barok binası ve kışın bile açık olan açık hava havuzlarıyla ikoniktir.",
        "description_en": "Europe's largest thermal complex. Iconic for its yellow neo-baroque building and outdoor pools open even in winter."
    },
    "Buda Kalesi": {
        "description": "Macar krallarının tarihi saray kompleksi. Şimdi Ulusal Galeri ve Tarih Müzesi'ne ev sahipliği yapan UNESCO miras alanı.",
        "description_en": "The historic palace complex of Hungarian kings. A UNESCO site now housing the National Gallery and History Museum."
    },
    "Balıkçı Kalesi": {
        "description": "Tuna ve Pest yakasının en iyi manzarasını sunan masalsı kuleler. 100 yıl önce balıkçılar loncası tarafından korunmuştur.",
        "description_en": "Dreamy towers offering the best views of the Danube and Pest side, protected by the fishermen's guild 100 years ago."
    },
    "Instant-Fogas Complex": {
        "description": "Budapeşte'nin en ünlü 'ruin bar' kompleksi. Labirenti andıran onlarca oda, farklı müzik türleri ve sürreal dekorasyon.",
        "description_en": "Budapest's most famous ruin bar complex. Labyrinthine rooms, various music genres, and surreal decoration."
    },
    "Zincir Köprüsü": {
        "description": "Buda ve Pest'i birleştiren ilk taş köprü. Girişindeki aslan heykelleriyle şehrin en bilindik sembollerinden biridir.",
        "description_en": "The first stone bridge connecting Buda and Pest. One of the city's most recognizable symbols with its lion statues."
    },
    "St. Stephen's Basilika": {
        "description": "Macaristan'ın en büyük kilisesi. 96 metrelik kubbesinden panoramik şehir manzarası ve içindeki kutsal sağ el emanetiyle ünlü.",
        "description_en": "Hungary's largest church. Famous for its 96-meter dome with panoramic views and the holy right hand relic inside."
    },
    "Gellért Hamamı": {
        "description": "Art Nouveau mimarisinin en güzel örneği. Turkuaz çinilerle kaplı havuzları ve cam tavanıyla sarayda yüzüyormuş hissi verir.",
        "description_en": "A prime example of Art Nouveau architecture. Turquoise-tiled pools and glass ceilings make you feel like swimming in a palace."
    },
    "Andrássy Bulvarı": {
        "description": "Şehrin şanzelizesi. Neo-Rönesans malikaneler, şık butikler ve Opera binası ile 2.5 km boyunca uzanan UNESCO mirası.",
        "description_en": "The city's Champs-Élysées. UNESCO heritage stretching 2.5 km with Neo-Renaissance mansions, chic boutiques, and the Opera."
    },
    "Merkez Pazar": {
        "description": "1897'den kalma devasa kapalı pazar. Taze Macar ürünleri, baharatlar ve üst katında yerel lezzetler sunan tezgahlar bulunur.",
        "description_en": "Massive covered market from 1897. Features fresh Hungarian produce, spices, and stalls serving local dishes on the upper floor."
    }
}

def enrich_budapest():
    filepath = 'assets/cities/budapeste.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Update fillers
    for h in data.get('highlights', []):
        if h['name'] in budapest_fillers_fix:
            fix = budapest_fillers_fix[h['name']]
            h['description'] = fix['description']
            h['description_en'] = fix['description_en']

    # Add new ones
    existing_names = set(h['name'] for h in data.get('highlights', []))
    for new_h in new_budapest_highlights:
        if new_h['name'] not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_budapest()
print(f"Budapest now has {count} highlights.")
