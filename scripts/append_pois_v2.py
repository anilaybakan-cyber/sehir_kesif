
import json
import os

cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"

additions = {
    "madrid.json": [
        {
            "name": "Matadero Madrid",
            "area": "Arganzuela",
            "category": "Kültür",
            "tags": ["sanat", "endüstriyel", "sinema"],
            "distanceFromCenter": 2.5,
            "lat": 40.392,
            "lng": -3.697,
            "price": "free",
            "rating": 4.6,
            "description": "Eski mezbaha, dev bir kültür merkezine dönüştü. Sergiler, sinema ve pazarlar.",
            "description_en": "Old slaughterhouse turned into a giant cultural hub. Exhibitions, cinema and markets.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Öğleden sonra",
            "bestTime_en": "Afternoon",
            "tips": "Her zaman ücretsiz sergiler vardır. Nehir kenarında yürüyüş yapın."
        }
    ],
    "hongkong.json": [
        {
            "name": "Nan Lian Garden",
            "area": "Diamond Hill",
            "category": "Doğa",
            "tags": ["bahçe", "tapınak", "huzur"],
            "distanceFromCenter": 5.0,
            "lat": 22.339,
            "lng": 114.205,
            "price": "free",
            "rating": 4.7,
            "description": "Tang Hanedanlığı tarzında klasik Çin bahçesi. Gökdelenlerin ortasında bir huzur vahası. Altın Köşk muazzam.",
            "description_en": "Classic Chinese garden in Tang Dynasty style. Oasis of peace amidst skyscrapers. Golden Pavilion is magnificent.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Sabah",
            "bestTime_en": "Morning",
            "tips": "Chi Lin Rahibe Manastırı (Chi Lin Nunnery) ile köprüyle bağlantılıdır, ikisini de görün."
        }
    ],
    "dubai.json": [
        {
            "name": "Dubai Miracle Garden",
            "area": "Dubailand",
            "category": "Doğa",
            "tags": ["çiçek", "rekor", "fotoğraf"],
            "distanceFromCenter": 15.0,
            "lat": 25.060,
            "lng": 55.244,
            "price": "medium",
            "rating": 4.6,
            "description": "Dünyanın en büyük doğal çiçek bahçesi. 50 milyon çiçekten yapılan dev heykeller (Uçak, Mickey Mouse).",
            "description_en": "World's largest natural flower garden. Giant sculptures made of 50 million flowers (Plane, Mickey Mouse).",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Kış ayları",
            "bestTime_en": "Winter months",
            "tips": "Sadece kışın (Kasım-Nisan) açıktır. Sıcaktan kaçınmak için akşamüstü gidin."
        }
    ],
    "budapeste.json": [
        {
            "name": "Hospital in the Rock",
            "area": "Buda",
            "category": "Müze",
            "tags": ["sığınak", "tarih", "ilginç"],
            "distanceFromCenter": 0.5,
            "lat": 47.500,
            "lng": 19.034,
            "price": "medium",
            "rating": 4.7,
            "description": "Kale altında doğal mağaralara kurulmuş eski bir gizli hastane ve nükleer sığınak (Sziklakorhaz).",
            "description_en": "Former secret hospital and nuclear bunker built in natural caves under the castle (Sziklakorhaz).",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Tüm gün",
            "bestTime_en": "Full day",
            "tips": "Sadece rehberli turla gezilir. Yazın bile içerisi serindir, hırka alın."
        }
    ],
    "singapur.json": [
        {
            "name": "National Gallery Singapore",
            "area": "City Hall",
            "category": "Müze",
            "tags": ["sanat", "mimari", "tarih"],
            "distanceFromCenter": 0.5,
            "lat": 1.290,
            "lng": 103.851,
            "price": "medium",
            "rating": 4.7,
            "description": "Eski Yüksek Mahkeme ve Belediye Binası'nın birleştirilmesiyle oluşan muazzam sanat müzesi. Güneydoğu Asya sanatı.",
            "description_en": "Magnificent art museum formed by merging old Supreme Court and City Hall. Southeast Asian art.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Öğleden sonra",
            "bestTime_en": "Afternoon",
            "tips": "Çatı terasındaki bahçe (Ng Teng Fong) halka açıktır ve Marina Bay manzaralıdır."
        }
    ],
    "viyana.json": [
        {
            "name": "Kunsthistorisches Museum",
            "area": "Museumsquartier",
            "category": "Müze",
            "tags": ["sanat", "bina", "klasik"],
            "distanceFromCenter": 0.5,
            "lat": 48.203,
            "lng": 16.361,
            "price": "medium",
            "rating": 4.8,
            "description": "Sanat Tarihi Müzesi. Habsburgların devasa koleksiyonu. Binanın kendisi bile bir sanat eseri.",
            "description_en": "Museum of Art History. Huge collection of Habsburgs. Building itself is a work of art.",
            "imageUrl": "PLACEHOLDER",
            "bestTime": "Yağmurlu gün",
            "bestTime_en": "Rainy day",
            "tips": "Müzenin kafesi (Cafe im Kunsthistorisches Museum) dünyanın en şık müze kafesidir."
        }
    ]
}

def append_pois():
    for filename, new_pois in additions.items():
        filepath = os.path.join(cities_dir, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
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
                print(f"{filename}: No new POIs added.")
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    append_pois()
