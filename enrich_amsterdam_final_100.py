import json
import os

extra_10 = [
    {
        "name": "Hans Egstorf (Bakery)",
        "name_en": "Hans Egstorf",
        "area": "Centrum",
        "category": "Deneyim",
        "tags": ["stroopwafel", "fırın", "tarihi", "tatlı"],
        "distanceFromCenter": 0.5,
        "lat": 52.3688,
        "lng": 4.8897,
        "price": "low",
        "rating": 4.8,
        "description": "1898'den beri hizmet veren Amsterdam'ın en eski fırınlarından biri. İnanılmaz stroopwafelleri ve taze hamur işleriyle tanınır.",
        "description_en": "One of Amsterdam's oldest bakeries, serving since 1898. Renowned for its incredible stroopwafels and fresh pastries.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Taze yapılmış sıcak stroopwafellerini mutlaka deneyin, fabrika yapımı olanlardan çok farklıdır.",
        "tips_en": "Be sure to try their freshly made hot stroopwafels, which are vastly different from factory-made ones."
    },
    {
        "name": "Gassan Diamonds",
        "name_en": "Gassan Diamonds",
        "area": "Centrum",
        "category": "Deneyim",
        "tags": ["elmas", "tazminat", "tarih", "lüks"],
        "distanceFromCenter": 0.8,
        "lat": 52.3705,
        "lng": 4.9038,
        "price": "free",
        "rating": 4.6,
        "description": "Tarihi bir buharlı elmas fabrikasında yer alan, dünyanın en ünlü elmas kesim ve mücevher merkezlerinden biri.",
        "description_en": "One of the world's most famous diamond cutting and jewelry centers, located in a historic steam-powered diamond factory.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Ücretsiz rehberli turlar sayesinde elmasların nasıl işlendiğini öğrenebilirsiniz.",
        "tips_en": "You can learn about diamond processing through free guided tours."
    },
    {
        "name": "Verzetsmuseum (Direniş Müzesi)",
        "name_en": "Resistance Museum",
        "area": "Plantage",
        "category": "Müze",
        "tags": ["tarih", "ikinci dünya savaşı", "direniş", "hollanda"],
        "distanceFromCenter": 1.5,
        "lat": 52.3667,
        "lng": 4.9125,
        "price": "medium",
        "rating": 4.7,
        "description": "İkinci Dünya Savaşı sırasında Hollanda Direnişi'ni ve işgal altındaki yaşamı anlatan, ödüllü ve çok etkileyici bir tarih müzesi.",
        "description_en": "An award-winning and very moving history museum telling the story of the Dutch Resistance and life under occupation during WWII.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kişisel hikayeler üzerinden ilerleyen sergiler, dönemin atmosferini çok iyi yansıtır.",
        "tips_en": "The exhibitions, which progress through personal stories, capture the atmosphere of the period very well."
    },
    {
        "name": "Joods Museum (Yahudi Müzesi)",
        "name_en": "Jewish Museum",
        "area": "Jewish Cultural Quarter",
        "category": "Müze",
        "tags": ["tarih", "yahudi kültürü", "din", "gelenek"],
        "distanceFromCenter": 1.0,
        "lat": 52.3670,
        "lng": 4.9031,
        "price": "medium",
        "rating": 4.6,
        "description": "Dört tarihi sinagogun içinde yer alan, Hollanda'daki Yahudi tarihi, dini ve kültürüne adanmış kapsamlı müze.",
        "description_en": "A comprehensive museum dedicated to Jewish history, religion, and culture in the Netherlands, housed within four historic synagogues.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Çocuk Müzesi bölümü, Yahudi geleneklerini interaktif bir şekilde öğrenmek için harikadır.",
        "tips_en": "The Jewish Museum junior section is great for learning about Jewish traditions interactively."
    },
    {
        "name": "Embassy of the Free Mind",
        "name_en": "Embassy of the Free Mind",
        "area": "Centrum",
        "category": "Müze",
        "tags": ["felsefe", "tarih", "kütüphane", "bilgelik"],
        "distanceFromCenter": 0.8,
        "lat": 52.3758,
        "lng": 4.8856,
        "price": "medium",
        "rating": 4.8,
        "description": "Tarihi bir kanal evinde yer alan, felsefe, astronomi ve mistisizm gibi nadir konulara odaklanan benzersiz bir kütüphane ve müze.",
        "description_en": "A unique library and museum focusing on rare subjects like philosophy, astronomy, and mysticism, housed in a historic canal house.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Binanın iç mimarisi ve eski el yazmaları koleksiyonu görenleri büyüler.",
        "tips_en": "The building's interior architecture and collection of ancient manuscripts are enchanting."
    },
    {
        "name": "Hollandsche Schouwburg (Ulusal Holokost Anıtı)",
        "name_en": "National Holocaust Memorial",
        "area": "Plantage",
        "category": "Tarihi",
        "tags": ["holokost", "anıt", "tarih", "2. dünya savaşı"],
        "distanceFromCenter": 1.5,
        "lat": 52.3661,
        "lng": 4.9103,
        "price": "free",
        "rating": 4.7,
        "description": "Eski bir tiyatro binası olan bu mekan, savaş sırasında Yahudilerin toplandığı bir merkezdi, bugün ise bir anıt ve müze olarak hizmet veriyor.",
        "description_en": "Formerly a theater, this venue served as a collection center for Jews during the war; today it serves as a memorials and museum.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Sessiz ve saygılı bir ziyaret gerektiren duygusal bir mekandır.",
        "tips_en": "A poignant and moving site that requires a quiet and respectful visit."
    },
    {
        "name": "Fashion for Good Museum",
        "name_en": "Fashion for Good Museum",
        "area": "Centrum",
        "category": "Müze",
        "tags": ["moda", "sürdürülebilirlik", "teknoloji", "inovasyon"],
        "distanceFromCenter": 0.5,
        "lat": 52.3703,
        "lng": 4.8914,
        "price": "medium",
        "rating": 4.5,
        "description": "Sürdürülebilir moda ve tekstil inovasyonuna adanmış dünyanın ilk interaktif müzesi.",
        "description_en": "The world's first interactive museum dedicated to sustainable fashion and textile innovation.",
        "imageUrl": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kendi sürdürülebilir alışveriş rehberinizi oluşturmak için interaktif bilekliklerden kullanın.",
        "tips_en": "Use the interactive bracelets to create your own sustainable shopping guide."
    },
    {
        "name": "Nam Kee (Çin Mutfağı)",
        "name_en": "Nam Kee",
        "area": "Zeedijk (Chinatown)",
        "category": "Restoran",
        "tags": ["çin yemeği", "istiridye", "tarihi", "lezzetli"],
        "distanceFromCenter": 0.5,
        "lat": 52.3745,
        "lng": 4.9002,
        "price": "medium",
        "rating": 4.4,
        "description": "Amsterdam'ın Chinatown bölgesindeki efsanevi Çin restoranı. Özellikle 'Nam Kee'nin İstiridyeleri' yemeğiyle dünya çapında ünlüdür.",
        "description_en": "Legendary Chinese restaurant in Amsterdam's Chinatown. World-famous especially for its dish 'Oysters at Nam Kee'.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "bestTime": "Öğle veya Akşam",
        "bestTime_en": "Lunch or Dinner",
        "tips": "Burası aynı isimli Hollanda romanı ve filmine de ilham vermiştir.",
        "tips_en": "This place inspired a Dutch novel and film of the same name."
    },
    {
        "name": "Albert Heijn Museum (Zaanse Schans)",
        "name_en": "Albert Heijn Museum Shop",
        "area": "Zaanse Schans",
        "category": "Tarihi",
        "tags": ["market", "tarih", "alışveriş", "nostalji"],
        "distanceFromCenter": 15.0,
        "lat": 52.4731,
        "lng": 4.8197,
        "price": "free",
        "rating": 4.5,
        "description": "Hollanda'nın ünlü market zinciri Albert Heijn'in 1887'deki ilk dükkanının rekonstrüksiyonu. Nostaljik bir alışveriş deneyimi sunar.",
        "description_en": "A reconstruction of the first shop opened in 1887 by the famous Dutch supermarket chain Albert Heijn. Offers a nostalgic shopping experience.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Eski usul şekerlemeler ve kahve kavurma aletlerini görebilirsiniz.",
        "tips_en": "You can see old-fashioned candies and coffee roasting equipment."
    },
    {
        "name": "This is Holland (Uçuş Deneyimi)",
        "name_en": "This is Holland",
        "area": "Noord",
        "category": "Deneyim",
        "tags": ["simülasyon", "hollanda turu", "4D", "eğlenceli"],
        "distanceFromCenter": 1.5,
        "lat": 52.3845,
        "lng": 4.9023,
        "price": "high",
        "rating": 4.7,
        "description": "Hollanda'nın simge yapıları üzerinde uçuyormuşsunuz hissi veren muazzam bir 4D uçuş simülasyonu deneyimi.",
        "description_en": "A magnificent 4D flight simulation experience that gives you the sensation of flying over the Netherlands' iconic landmarks.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "A'DAM Lookout'un hemen yanındadır, iki deneyimi birleştirebilirsiniz.",
        "tips_en": "Located right next to A'DAM Lookout; you can combine both experiences."
    }
]

def enrich_amsterdam_final_100():
    filepath = 'assets/cities/amsterdam.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in extra_10:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_amsterdam_final_100()
print(f"Amsterdam final count: {count}")
