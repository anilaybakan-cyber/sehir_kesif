import json
import os

new_budapest_batch2 = [
    {
        "name": "Mazel Tov",
        "name_en": "Mazel Tov",
        "area": "Yahudi Mahallesi",
        "category": "Restoran",
        "tags": ["ortadoğu", "ruin bar", "şık", "canlı müzik"],
        "distanceFromCenter": 0.8,
        "lat": 47.4994,
        "lng": 19.0658,
        "price": "medium",
        "rating": 4.7,
        "description": "Ruin bar estetiğini şık bir restoran deneyimiyle birleştiren, ağaçlarla çevrili iç avlusu ve harika Ortadoğu mutfağıyla ünlü popüler mekan.",
        "description_en": "A popular venue combining ruin bar aesthetics with a chic restaurant experience, featuring a tree-lined inner courtyard and great Middle Eastern cuisine.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Genelde canlı müzik olur, hafta sonu akşamları için önceden rezervasyon yaptırın.",
        "tips_en": "There's often live music; book in advance for weekend evenings."
    },
    {
        "name": "Dobrumba",
        "name_en": "Dobrumba",
        "area": "Yahudi Mahallesi",
        "category": "Restoran",
        "tags": ["akdeniz", "meze", "popüler", "モダン"],
        "distanceFromCenter": 0.5,
        "lat": 47.4994,
        "lng": 19.0639,
        "price": "medium",
        "rating": 4.8,
        "description": "Orta Doğu ve Akdeniz mutfaklarından seçkin mezeler sunan, her zaman kalabalık ve enerjik bir atmosfere sahip gurme noktası.",
        "description_en": "A gourmet spot with a bustling and energetic atmosphere, serving exquisite mezes from Middle Eastern and Mediterranean cuisines.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Öğle veya Akşam",
        "bestTime_en": "Noon or Evening",
        "tips": "Paylaşımlı tabaklar (Humus, Muhammara) denemek için idealdir.",
        "tips_en": "Ideal for trying shared platters (Hummus, Muhammara)."
    },
    {
        "name": "360 Bar",
        "name_en": "360 Bar",
        "area": "Andrássy",
        "category": "Bar",
        "tags": ["rooftop", "manzara", "kokteyl", "iglo"],
        "distanceFromCenter": 1.2,
        "lat": 47.5061,
        "lng": 19.0617,
        "price": "high",
        "rating": 4.6,
        "description": "Andrássy Bulvarı üzerinde yer alan, Budapeşte'nin 360 derecelik panoramik manzarasını sunan en popüler çatı barı.",
        "description_en": "The most popular rooftop bar in Budapest, located on Andrássy Avenue, offering 360-degree panoramic views of the city.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Kışın çatıda kurulan şeffaf iglolarda ısınarak manzaranın tadını çıkarabilirsiniz.",
        "tips_en": "In winter, you can enjoy the view while staying warm in transparent igloos set up on the roof."
    },
    {
        "name": "Gelarto Rosa",
        "name_en": "Gelarto Rosa",
        "area": "Pest",
        "category": "Kafe",
        "tags": ["dondurma", "gül", "tatlı", "fotojenik"],
        "distanceFromCenter": 0.5,
        "lat": 47.5008,
        "lng": 19.0539,
        "price": "low",
        "rating": 4.7,
        "description": "Aziz İştvan Bazilikası'nın hemen yanında bulunan, dondurmaları gül şeklinde külaha dizmeleriyle ünlü sanat eseri tadında bir dondurmacı.",
        "description_en": "An artisan ice cream shop next to St. Stephen's Basilica, famous for serving ice cream shaped like edible roses on a cone.",
        "imageUrl": "https://images.unsplash.com/photo-1501446529957-6226bd447c46?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Farklı renklerdeki dondurmalarla en güzel gül formunu oluşturun.",
        "tips_en": "Combine different colored ice creams to create the most beautiful rose form."
    },
    {
        "name": "Várkert Bazár",
        "name_en": "Castle Garden Bazaar",
        "area": "Buda",
        "category": "Tarihi",
        "tags": ["mimari", "nehir", "bahçe", "kültür"],
        "distanceFromCenter": 0.8,
        "lat": 47.4950,
        "lng": 19.0394,
        "price": "free",
        "rating": 4.8,
        "description": "Buda Kalesi'nin eteklerinde, nehir kıyısında yer alan Neo-Rönesans tarzı muhteşem bir yapı ve bahçeler kompleksi.",
        "description_en": "A magnificent Neo-Renaissance structure and garden complex located at the foot of Buda Castle along the riverbank.",
        "imageUrl": "https://images.unsplash.com/photo-1551867633-194f125bddfa?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Buradaki yürüyen merdivenlerle kolayca Buda Kalesi'ne çıkabilirsiniz.",
        "tips_en": "You can easily reach Buda Castle using the escalators located here."
    },
    {
        "name": "Bors GasztroBár",
        "name_en": "Bors GasztroBar",
        "area": "Yahudi Mahallesi",
        "category": "Restoran",
        "tags": ["çorba", "sandviç", "hızlı yemek", "gurme"],
        "distanceFromCenter": 0.5,
        "lat": 47.4972,
        "lng": 19.0631,
        "price": "low",
        "rating": 4.9,
        "description": "Yaratıcı çorbaları ve gurme baget sandviçleriyle Budapeşte'nin en sevilen ve en özgün sokak lezzeti duraklarından biri.",
        "description_en": "One of Budapest's most beloved and unique street food spots, known for creative soups and gourmet baguette sandwiches.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Öğle",
        "bestTime_en": "Noon",
        "tips": "Menüleri günlük değişir, Star Wars temalı sandviçlerine denk gelebilirsiniz.",
        "tips_en": "Their menu changes daily; you might come across Star Wars-themed sandwiches."
    },
    {
        "name": "High Note SkyBar",
        "name_en": "High Note SkyBar",
        "area": "Pest",
        "category": "Bar",
        "tags": ["rooftop", "lüks", "bazilika manzarası", "kokteyl"],
        "distanceFromCenter": 0.5,
        "lat": 47.5008,
        "lng": 19.0539,
        "price": "high",
        "rating": 4.8,
        "description": "Aria Hotel'in çatısında yer alan ve Aziz İştvan Bazilikası'nın dev kubbesine neredeyse dokunacak kadar yakın olan inanılmaz manzaralı bir bar.",
        "description_en": "A bar on the roof of Aria Hotel with incredible views, located so close you can almost touch the giant dome of St. Stephen's Basilica.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Gün batımı veya Gece",
        "bestTime_en": "Sunset or Night",
        "tips": "Şehrin en şık barıdır, kıyafetinize özen göstermeyi unutmayın.",
        "tips_en": "It's the city's most elegant bar; don't forget to dress for the occasion."
    },
    {
        "name": "Zsinagóga Garden (Holokost Anıtı)",
        "name_en": "Raoul Wallenberg Memorial Park",
        "area": "Yahudi Mahallesi",
        "category": "Tarihi",
        "tags": ["anıt", "ağaç", "holokost", "tarih"],
        "distanceFromCenter": 0.5,
        "lat": 47.4958,
        "lng": 19.0609,
        "price": "low",
        "rating": 4.8,
        "description": "Büyük Sinagog'un bahçesinde bulunan, yapraklarında Holokost kurbanlarının isimlerinin yazılı olduğu metalik 'Hayat Ağacı' (Emanuel Tree) anıtı.",
        "description_en": "The metallic 'Tree of Life' (Emanuel Tree) memorial in the Great Synagogue courtyard, with victims' names inscribed on its silver leaves.",
        "imageUrl": "https://images.unsplash.com/photo-1590429408077-440232231f42?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Gözyaşı döken bir salkım söğüt ağacını andıran bu anıt çok duygusaldır.",
        "tips_en": "The memorial resembling a weeping willow tree is very moving."
    },
    {
        "name": "Szabadság tér",
        "name_en": "Liberty Square",
        "area": "Pest",
        "category": "Park",
        "tags": ["park", "siyaset", "tarih", "mimari"],
        "distanceFromCenter": 0.5,
        "lat": 47.5036,
        "lng": 19.0506,
        "price": "free",
        "rating": 4.6,
        "description": "Pest yakasının en büyük ve en güzel parklarından biri. Etrafında ABD Büyükelçiliği, Macaristan Merkez Bankası ve tartışmalı anıtlar bulunur.",
        "description_en": "One of the largest and most beautiful squares on the Pest side, surrounded by the US Embassy, the Hungarian National Bank, and controversial monuments.",
        "imageUrl": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Parkın kuzeyindeki Sovyet Savaş Anıtı Budapeşte'de kalan son komünist anıtlardan biridir.",
        "tips_en": "The Soviet War Memorial at the north end is one of the last communist monuments remaining in Budapest."
    },
    {
        "name": "Citadella",
        "name_en": "Citadella",
        "area": "Gellért Tepesi",
        "category": "Tarihi",
        "tags": ["kale", "manzara", "avusturya", "tarihi"],
        "distanceFromCenter": 1.5,
        "lat": 47.4866,
        "lng": 19.0481,
        "price": "free",
        "rating": 4.5,
        "description": "Gellért Tepesi'nin en tepesinde yer alan, 1851 yılında Avusturya İmparatorluğu tarafından inşa edilmiş olan devasa kale.",
        "description_en": "The massive fortress atop Gellért Hill, built by the Austrian Empire in 1851.",
        "imageUrl": "https://images.unsplash.com/photo-1551867633-194f125bddfa?w=800",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Buradan çekilen gece fotoğrafları Budapeşte'nin en ikonik kareleridir.",
        "tips_en": "Night photos taken from here are the most iconic shots of Budapest."
    }
]

def enrich_budapest_batch2():
    filepath = 'assets/cities/budapeste.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'] for h in data.get('highlights', []))
    for new_h in new_budapest_batch2:
        if new_h['name'] not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_budapest_batch2()
print(f"Budapest now has {count} highlights.")
