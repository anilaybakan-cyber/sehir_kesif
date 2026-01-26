import json
import os

new_rome_highlights = [
    {
        "name": "Musei Capitolini",
        "name_en": "Capitoline Museums",
        "area": "Campidoglio",
        "category": "Müze",
        "tags": ["antik", "heykel", "tarih", "manzara"],
        "distanceFromCenter": 0.5,
        "lat": 41.8931,
        "lng": 12.4831,
        "price": "medium",
        "rating": 4.8,
        "description": "Dünyanın en eski halka açık müzesi. Michelangelo tarafından tasarlanan piazza üzerinde yer alan bu kompleks, Roma'nın en önemli antik heykellerine ev sahipliği yapar.",
        "description_en": "The world's oldest public museum. Located on the piazza designed by Michelangelo, this complex houses Rome's most important ancient sculptures.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Müzelerden foruma bakan manzara balkonuna mutlaka çıkın (Tabularium).",
        "tips_en": "Be sure to go out to the balcony overlooking the forum (Tabularium)."
    },
    {
        "name": "Circo Massimo",
        "name_en": "Circus Maximus",
        "area": "Aventino",
        "category": "Tarihi",
        "tags": ["antik", "arena", "yarış", "park"],
        "distanceFromCenter": 1.5,
        "lat": 41.8859,
        "lng": 12.4853,
        "price": "free",
        "rating": 4.5,
        "description": "Antik Roma'nın devasa at arabası yarışı stadyumu. Bugün halka açık bir park olan bu alan, bir zamanlar 150.000 seyirciyi ağırlayabiliyordu.",
        "description_en": "Ancient Rome's massive chariot racing stadium. Now a public park, this area could once accommodate 150,000 spectators.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Palatine Tepesi'nin harabelerini buradan izlemek çok etkileyicidir.",
        "tips_en": "Watching the ruins of Palatine Hill from here is very impressive."
    },
    {
        "name": "Vittoriano (Altare della Patria)",
        "name_en": "Altar of the Fatherland",
        "area": "Piazza Venezia",
        "category": "Tarihi",
        "tags": ["anıt", "manzara", "beyaz mermer"],
        "distanceFromCenter": 0.0,
        "lat": 41.8946,
        "lng": 12.4828,
        "price": "low",
        "rating": 4.7,
        "description": "Birleşmiş İtalya'nın ilk kralı II. Vittorio Emanuele onuruna yapılmış devasa beyaz mermer anıt. Roma siluetinin en belirgin yapılarından biridir.",
        "description_en": "A massive white marble monument built in honor of Victor Emmanuel II, the first king of unified Italy. One of the most prominent features of the Roman skyline.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Anıtın arkasındaki cam asansörle (Roma dal Cielo) terasa çıkıp şehrin en iyi manzarasını izleyebilirsiniz.",
        "tips_en": "Take the glass elevator at the back (Roma dal Cielo) to the terrace for the city's best views."
    },
    {
        "name": "Via Appia Antica",
        "name_en": "Ancient Appian Way",
        "area": "Appio Latino",
        "category": "Tarihi",
        "tags": ["antik yol", "mezarlar", "doğa", "bisiklet"],
        "distanceFromCenter": 5.0,
        "lat": 41.8547,
        "lng": 12.5228,
        "price": "free",
        "rating": 4.8,
        "description": "Roma'nın en eski ve en önemli yollarından biri. 2300 yıllık orijinal taşlar üzerinde yürüyüp antik mezarlar ve kalıntılar arasından geçebilirsiniz.",
        "description_en": "One of Rome's oldest and most important roads. Walk on 2300-year-old original stones through ancient tombs and ruins.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Pazar",
        "bestTime_en": "Sunday",
        "tips": "Pazar günleri araç trafiğine kapalıdır, bisiklet kiralayıp gezmek için mükemmeldir.",
        "tips_en": "Closed to car traffic on Sundays, perfect for renting a bike and exploring."
    },
    {
        "name": "Galleria Borghese",
        "name_en": "Borghese Gallery",
        "area": "Villa Borghese",
        "category": "Müze",
        "tags": ["sanat", "rönesans", "heykel", "barok"],
        "distanceFromCenter": 2.5,
        "lat": 41.9131,
        "lng": 12.4922,
        "price": "high",
        "rating": 4.9,
        "description": "Dünyanın en seçkin özel sanat koleksiyonlarından biri. Bernini'nin heykelleri, Caravaggio'nun tabloları ve Canova'nın eserleriyle doludur.",
        "description_en": "One of the world's most elite private art collections, filled with Bernini sculptures, Caravaggio paintings, and Canova works.",
        "imageUrl": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        "bestTime": "Öğle",
        "bestTime_en": "Noon",
        "tips": "Biletler haftalar öncesinden tükenir, MUTLAKA önceden online rezervasyon yaptırın.",
        "tips_en": "Tickets sell out weeks in advance; MUST book online ahead of time."
    }
]

# Filler fixes for Rome
rome_fillers_fix = {
    "Roma Forumu": {
        "description": "Antik Roma dünyasının politik, ticari ve dini merkezi. Sezar'ın yürüdüğü taşlara basabilir, görkemli tapınak kalıntılarını görebilirsiniz.",
        "description_en": "The political, commercial, and religious center of the ancient Roman world. Walk the same stones as Caesar and see grand temple ruins."
    },
    "Campo de' Fiori": {
        "description": "Gündüzleri taze meyve-sebze ve baharat pazarı, geceleri ise şehrin en canlı bar ve restoran bölgelerinden biri olan tarihi meydan.",
        "description_en": "A historic square featuring a fresh produce and spice market by day and one of the city's liveliest bar and restaurant districts by night."
    },
    "Giardino degli Aranci": {
        "description": "Aventino Tepesi'nde yer alan 'Turunçgil Bahçesi'. Şehrin en huzurlu parklarından biri olup nehre ve Vatikan'a bakan muhteşem bir manzaraya sahiptir.",
        "description_en": "The 'Orange Garden' on Aventine Hill. One of the city's most peaceful parks with magnificent views of the river and the Vatican."
    },
    "Quartiere Coppedè": {
        "description": "Gino Coppedè tarafından tasarlanan sürreal ve eklektik mimari harikası. Peri kemerleri ve mitolojik figürlerle bezeli binalarıyla masalsı bir atmosfer sunar.",
        "description_en": "A surreal and eclectic architectural wonder designed by Gino Coppedè. Offers a fairytale atmosphere with buildings adorned with fairy arches and mythological figures."
    }
}

def enrich_rome():
    filepath = 'assets/cities/roma.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Update fillers
    for h in data.get('highlights', []):
        if h['name'] in rome_fillers_fix:
            fix = rome_fillers_fix[h['name']]
            h['description'] = fix['description']
            h['description_en'] = fix['description_en']

    # Add new ones
    existing_names = set(h['name'] for h in data.get('highlights', []))
    for new_h in new_rome_highlights:
        if new_h['name'] not in existing_names:
            data['highlights'].append(new_h)

    # Note: I'll add more in a bigger batch next.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_rome()
print(f"Rome now has {count} highlights.")
