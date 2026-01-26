import json
import os

extra_9 = [
    {
        "name": "Odense (H.C. Andersen'in Doğum Yeri)",
        "name_en": "Odense",
        "area": "Fyn Adası (Günübirlik)",
        "category": "Deneyim",
        "tags": ["h.c. andersen", "masal", "tarihi evler", "müze"],
        "distanceFromCenter": 160.0,
        "lat": 55.4038,
        "lng": 10.3883,
        "price": "high",
        "rating": 4.7,
        "description": "Dünyaca ünlü masal yazarı Hans Christian Andersen'in doğduğu ve çocukluğunun geçtiği büyülü şehir. Yeni açılan devasa H.C. Andersen Müzesi görülmeye değerdir.",
        "description_en": "The magical birthplace and childhood home of world-famous fairytale author Hans Christian Andersen. The newly opened, massive H.C. Andersen Museum is a must-see.",
        "imageUrl": "https://images.unsplash.com/photo-1548678906-f80e9a6572e2?w=800",
        "bestTime": "Tüm gün",
        "bestTime_en": "Full day",
        "tips": "Kopenhag'dan trenle yaklaşık 1.5 saatte ulaşılabilir. Arnavut kaldırımlı eski şehir bölgesinde kaybolun.",
        "tips_en": "Accessible in about 1.5 hours by train from Copenhagen. Get lost in the cobblestoned streets of the old town."
    },
    {
        "name": "Sluseholmen (Kopenhag'ın Venedik'i)",
        "name_en": "Sluseholmen Canal District",
        "area": "Sydhavn",
        "category": "Tarihi",
        "tags": ["kanallar", "modern mimari", "su kıyısı", "ikonik"],
        "distanceFromCenter": 4.0,
        "lat": 55.6444,
        "lng": 12.5539,
        "price": "free",
        "rating": 4.6,
        "description": "Kanalların arasından yükselen modern konutlarıyla ünlü, suyun içinde yaşayan bir mahalle konsepti.",
        "description_en": "A neighborhood concept living 'in the water', famous for its modern residents rising between man-made canals.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Liman otobüsü (havnebus) ile bu bölgeye gelip kanallar arasında yürüyüş yapmak harikadır.",
        "tips_en": "Take the harbor bus (havnebus) to reach this area and enjoy a walk along the canals."
    },
    {
        "name": "Jægersborggade",
        "name_en": "Jægersborggade",
        "area": "Nørrebro",
        "category": "Alışveriş",
        "tags": ["trendy", "sanat", "gastronomi", "bohem"],
        "distanceFromCenter": 2.5,
        "lat": 55.6922,
        "lng": 12.5456,
        "price": "medium",
        "rating": 4.8,
        "description": "Kopenhag'ın en havalı sokaklarından biri. Özel yapım çikolata dükkanları, butik kafeler ve sanat galerileriyle doludur.",
        "description_en": "One of Copenhagen's coolest streets, filled with artisanal chocolate shops, boutique cafes, and art galleries.",
        "imageUrl": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Grød'da yulaf lapası yiyip Coffee Collective'de kahve molası verin.",
        "tips_en": "Have porridge at Grød and take a coffee break at Coffee Collective."
    },
    {
        "name": "Møns Klint (Beyaz Tebeşir Kayalıkları)",
        "name_en": "Møns Klint",
        "area": "Moen (Günübirlik)",
        "category": "Manzara",
        "tags": ["doğa", "jeoloji", "deniz", "yürüyüş"],
        "distanceFromCenter": 130.0,
        "lat": 54.9639,
        "lng": 12.5469,
        "price": "free",
        "rating": 4.9,
        "description": "Deniz kıyısında yükselen 128 metre yüksekliğindeki tebeşir beyazı dev kayalıklar. Danimarka'nın en çarpıcı doğal alanı.",
        "description_en": "128-meter-high chalk-white cliffs rising directly from the sea. Denmark's most striking natural site.",
        "imageUrl": "https://images.unsplash.com/photo-1548678906-f80e9a6572e2?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kayalıklardan denize inmek için oldukça çok sayıda basamak tırmanmanız gerekecek, hazırlıklı olun.",
        "tips_en": "Be prepared for a significant stair climb to reach the beach from the top of the cliffs."
    },
    {
        "name": "Restaurant Barr",
        "name_en": "Restaurant Barr",
        "area": "Christianshavn",
        "category": "Restoran",
        "tags": ["gastronomi", "kuzey denizi mutfağı", "fine dining", "ikonik bina"],
        "distanceFromCenter": 1.2,
        "lat": 55.6781,
        "lng": 12.5936,
        "price": "high",
        "rating": 4.7,
        "description": "Eski Noma restoranının yerinde bulunan, Kuzey Denizi çevresindeki ülkelerin mutfak geleneklerine (bira, ekmek, tuzlu balık) odaklanan harika bir restoran.",
        "description_en": "Located in the original home of Noma, this restaurant focuses on the culinary traditions of countries around the North Sea (beer, bread, salted fish).",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Viyana şnitzelini Danimarka yorumuyla denemenizi öneririz.",
        "tips_en": "We recommend trying the Danish interpretation of Wiener Schnitzel."
    },
    {
        "name": "The Silo Rooftop Restaurant",
        "name_en": "The Silo Rooftop",
        "area": "Nordhavn",
        "category": "Restoran",
        "tags": ["manzara", "fine dining", "mimari", "rooftop"],
        "distanceFromCenter": 3.8,
        "lat": 55.7078,
        "lng": 12.5925,
        "price": "high",
        "rating": 4.6,
        "description": "Eski bir tahıl silonunun dönüştürülmesiyle oluşan binanın en üst katında, muhteşem liman ve şehir manzaralı bir restoran.",
        "description_en": "A restaurant on the top floor of a converted grain silo, offering spectacular harbor and city views.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Binanın kendisi modern mimarinin ödüllü bir örneğidir, dış cephesine mutlaka bakın.",
        "tips_en": "The building itself is an award-winning example of modern architecture; be sure to admire its facade."
    },
    {
        "name": "Admiralgade 26",
        "name_en": "Admiralgade 26",
        "area": "Indre By",
        "category": "Restoran",
        "tags": ["bohem", "şarap", "gastronomi", "tarihi dükkan"],
        "distanceFromCenter": 0.5,
        "lat": 55.6775,
        "lng": 12.5831,
        "price": "medium",
        "rating": 4.5,
        "description": "Kendine has bohem dekorasyonu ve seçkin yiyecekleriyle Kopenhag'ın en şık ama samimi restoranlarından biri.",
        "description_en": "One of Copenhagen's most stylish yet intimate restaurants, known for its unique bohemian decor and exquisite food.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "bestTime": "Akşam yemeği",
        "bestTime_en": "Dinner",
        "tips": "Japon mutfağından esinlenen kahvaltıları hafta sonları çok popülerdir.",
        "tips_en": "Their Japanese-inspired breakfasts are very popular on weekends."
    },
    {
        "name": "Vesterbro'nun Sakin Sokakları (Elmegade)",
        "name_en": "Elmegade",
        "area": "Nørrebro",
        "category": "Alışveriş",
        "tags": ["butik", "genç", "trendy", "lokal"],
        "distanceFromCenter": 2.2,
        "lat": 55.6897,
        "lng": 12.5583,
        "price": "medium",
        "rating": 4.6,
        "description": "Nørrebro bölgesinin kalbinde, tasarım butikleri ve küçük kahveleriyle ünlü, yerel Kopenhag yaşamını en iyi yansıtan sokaklardan biri.",
        "description_en": "One of the streets best reflecting local Copenhagen life in the heart of Nørrebro, famous for its design boutiques and small cafes.",
        "imageUrl": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Laundromat Cafe'de kirli kıyafetlerinizi yıkarken bir kahve içebilirsiniz!",
        "tips_en": "You can have a coffee at Laundromat Cafe while doing your laundry!"
    },
    {
        "name": "Ravnsborggade (Antika Sokağı)",
        "name_en": "Ravnsborggade",
        "area": "Nørrebro",
        "category": "Alışveriş",
        "tags": ["antika", "vintage", "bit pazarı", "dekor"],
        "distanceFromCenter": 2.0,
        "lat": 55.6881,
        "lng": 12.5622,
        "price": "medium",
        "rating": 4.5,
        "description": "Antika dükkanları, vintage mobilya mağazaları ve moda butikleriyle ünlü, tarih kokan bir Nørrebro sokağı.",
        "description_en": "A historic Nørrebro street famous for its antique shops, vintage furniture stores, and fashion boutiques.",
        "imageUrl": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800",
        "bestTime": "Cumartesi öğleden sonra",
        "bestTime_en": "Saturday afternoon",
        "tips": "Yılda birkaç kez sokağın tamamına yayılan devasa bit pazarları düzenlenir.",
        "tips_en": "Huge flea markets that spread across the entire street are held several times a year."
    }
]

def enrich_kopenhag_extra_9():
    filepath = 'assets/cities/kopenhag.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in extra_9:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_kopenhag_extra_9()
print(f"Kopenhag reached final unique highlight count: {count}")
