import json
import os

new_kopenhag_batch1 = [
    {
        "name": "The Round Tower (Rundetårn)",
        "name_en": "The Round Tower",
        "area": "Centrum",
        "category": "Tarihi",
        "tags": ["gözlemevi", "manzara", "17. yüzyıl", "mimari"],
        "distanceFromCenter": 0.3,
        "lat": 55.6814,
        "lng": 12.5756,
        "price": "low",
        "rating": 4.5,
        "description": "17. yüzyıldan kalma, Avrupa'nın çalışan en eski gözlemevi. İçindeki basamaksız spiral rampa, eskiden atlı arabaların yukarı çıkabilmesi için tasarlanmıştır.",
        "description_en": "A 17th-century tower and the oldest functioning observatory in Europe. Its unique spiral horse ramp was designed for horse-drawn carriages to reach the top.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Rampayı tırmanırken cam bölmelerden eski kütüphane salonunu görebilirsiniz.",
        "tips_en": "You can see the former library hall through glass partitions as you climb the ramp."
    },
    {
        "name": "Vor Frelsers Kirke (Kurtarıcı Kilisesi)",
        "name_en": "Church of Our Saviour",
        "area": "Christianshavn",
        "category": "Tarihi",
        "tags": ["kilise", "spiral kule", "manzara", "barok"],
        "distanceFromCenter": 1.2,
        "lat": 55.6729,
        "lng": 12.5942,
        "price": "low",
        "rating": 4.7,
        "description": "Dışarıdan dolanarak yükselen altın spiral kulesiyle ünlü barok kilise. Kuleye tırmanmak Kopenhag'ın en iyi panoramik manzarasını sunar.",
        "description_en": "A Baroque church famous for its helix spire with an external staircase. Climbing to the top provides one of the best panoramic views of Copenhagen.",
        "imageUrl": "https://images.unsplash.com/photo-1548678906-f80e9a6572e2?w=800",
        "bestTime": "Gündüz (rüzgarsız)",
        "bestTime_en": "Daytime (not windy)",
        "tips": "En üstteki basamaklar oldukça dardır, yükseklik korkusu olanlar dikkat etmeli.",
        "tips_en": "The topmost steps are quite narrow; those with a fear of heights should be cautious."
    },
    {
        "name": "Marmorkirken (Mermer Kilise)",
        "name_en": "The Marble Church",
        "area": "Centrum",
        "category": "Tarihi",
        "tags": ["kilise", "kubbe", "mermer", "saray yakın"],
        "distanceFromCenter": 1.0,
        "lat": 55.6853,
        "lng": 12.5897,
        "price": "free",
        "rating": 4.8,
        "description": "İskandinavya'nın en büyük kilise kubbesine sahip olan muhteşem Frederiks Kilisesi. Roma'daki Aziz Petrus Bazilikası'ndan esinlenmiştir.",
        "description_en": "The magnificent Frederik's Church, boasting the largest church dome in Scandinavia. It was inspired by St. Peter's Basilica in Rome.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Amalienborg Sarayı ile aynı eksen üzerindedir, ikisi arasındaki meydanda harika fotoğraflar çekilir.",
        "tips_en": "It sits on the same axis as Amalienborg Palace; the square between them target is great for photos."
    },
    {
        "name": "Glyptoteket (Ny Carlsberg Glyptotek)",
        "name_en": "Glyptoteket",
        "area": "Vesterbro",
        "category": "Müze",
        "tags": ["sanat", "heykel", "kış bahçesi", "antika"],
        "distanceFromCenter": 0.5,
        "lat": 55.6729,
        "lng": 12.5724,
        "price": "medium",
        "rating": 4.8,
        "description": "Carlsberg biralarının kurucusu tarafından kurulan sanat müzesi. Özellikle antik heykelleri ve içindeki palmiyeli kış bahçesiyle ünlüdür.",
        "description_en": "An art museum founded by the creator of Carlsberg beer. It is particularly famous for its ancient sculptures and stunning palm-filled winter garden.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Müze içindeki kafe, Kopenhag'ın en şık dinlenme noktalarından biridir.",
        "tips_en": "The museum's cafe is one of the most elegant spots in Copenhagen to take a break."
    },
    {
        "name": "National Aquarium Denmark (Den Blå Planet)",
        "name_en": "National Aquarium Denmark",
        "area": "Kastrup",
        "category": "Deneyim",
        "tags": ["akvaryum", "modern", "mimari", "aile"],
        "distanceFromCenter": 7.0,
        "lat": 55.6379,
        "lng": 12.6565,
        "price": "high",
        "rating": 4.4,
        "description": "Kuzey Avrupa'nın en büyük ve modern akvaryumu. Bina tasarımı havadan bakıldığında dev bir su anaforunu andırır.",
        "description_en": "The largest and most modern aquarium in Northern Europe. From the air, the building's design resembles a giant whirlpool.",
        "imageUrl": "https://images.unsplash.com/photo-1503431128566-66abc0cf0464?w=800",
        "bestTime": "Sabah (açılış saati)",
        "bestTime_en": "Morning (at opening)",
        "tips": "Havaalanına çok yakın olduğu için uçuş öncesi veya sonrası ziyaret edilebilir.",
        "tips_en": "Its proximity to the airport makes it perfect for a visit before or after your flight."
    },
    {
        "name": "Reffen - Street Food Market",
        "name_en": "Reffen",
        "area": "Refshaleøen",
        "category": "Deneyim",
        "tags": ["sokak yemeği", "liman", "alternatif", "gün batımı"],
        "distanceFromCenter": 3.0,
        "lat": 55.6931,
        "lng": 12.6097,
        "price": "low",
        "rating": 4.6,
        "description": "Eski endüstriyel liman bölgesinde yer alan devasa açık hava sokak yemeği pazarı. Her damak tadına uygun dünya mutfaklarından örnekler sunar.",
        "description_en": "A massive open-air street food market located in a former industrial harbor area. Offers cuisines from around the world catering to all tastes.",
        "imageUrl": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Liman otobüsü (havnebus) ile deniz yoluyla gitmek çok daha keyiflidir.",
        "tips_en": "Taking the harbor bus (havnebus) is a much more enjoyable way to reach the site by sea."
    },
    {
        "name": "CopenHill (Amager Bakke)",
        "name_en": "CopenHill",
        "area": "Amager",
        "category": "Deneyim",
        "tags": ["kayak", "mimari", "çevre", "manzara"],
        "distanceFromCenter": 3.5,
        "lat": 55.6846,
        "lng": 12.6199,
        "price": "free",
        "rating": 4.7,
        "description": "Bir geri dönüşüm tesisinin çatısına inşa edilmiş yapay kayak pisti ve yürüyüş parkuru. Modern mimari ile sürdürülebilirliğin harika bir birleşimi.",
        "description_en": "An artificial ski slope and hiking trail built atop an energy-from-waste plant. A brilliant combination of modern architecture and sustainability.",
        "imageUrl": "https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kayak yapmasanız bile asansörle tepeye ücretsiz çıkıp liman manzarasını izleyebilirsiniz.",
        "tips_en": "Even if you don't ski, you can take the elevator to the top for free to enjoy harbor views."
    },
    {
        "name": "Torvehallerne KBH",
        "name_en": "Torvehallerne",
        "area": "Nørreport",
        "category": "Deneyim",
        "tags": ["gurme", "yiyecek pazarı", "lokal", "smørrebrød"],
        "distanceFromCenter": 0.8,
        "lat": 55.6837,
        "lng": 12.5696,
        "price": "medium",
        "rating": 4.6,
        "description": "Kopenhag'ın en ünlü kapalı yemek pazarı. Taze deniz ürünlerinden Smørrebrød'lara kadar en kaliteli Danimarka lezzetlerini burada bulabilirsiniz.",
        "description_en": "Copenhagen's most famous indoor food market. You'll find top-quality Danish delicacies here, from fresh seafood to Smørrebrød.",
        "imageUrl": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800",
        "bestTime": "Öğle yemeği",
        "bestTime_en": "Lunch",
        "tips": "Hallernes Smørrebrød'da geleneksel açık sandviçleri mutlaka deneyin.",
        "tips_en": "Be sure to try traditional open-faced sandwiches at Hallernes Smørrebrød."
    },
    {
        "name": "Botanisk Have (Botanik Bahçesi)",
        "name_en": "Botanical Garden",
        "area": "Centrum",
        "category": "Park",
        "tags": ["doğa", "sera", "palmiye evi", "fotojenik"],
        "distanceFromCenter": 0.7,
        "lat": 55.6869,
        "lng": 12.5739,
        "price": "free",
        "rating": 4.6,
        "description": "Kopenhag'ın merkezindeki huzurlu botanik bahçesi. 19. yüzyıldan kalma camdan Palmiye Evi (Palm House) görülmesi gereken en şık yapılardan biridir.",
        "description_en": "A peaceful botanical garden in the heart of Copenhagen. The 19th-century glass Palm House is one of must-see landmarks.",
        "imageUrl": "https://images.unsplash.com/photo-1548678906-f80e9a6572e2?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Bahçeye giriş ücretsizdir ancak Palmiye Evi ve Kelebek Evi için ayrı bilet almanız gerekir.",
        "tips_en": "Entrance to the garden is free, but you need separate tickets for the Palm House and Butterfly House."
    },
    {
        "name": "Kastellet (Yıldız Kale)",
        "name_en": "Kastellet",
        "area": "Østerbro",
        "category": "Tarihi",
        "tags": ["kale", "yürüyüş", "tarih", "yel değirmeni"],
        "distanceFromCenter": 1.8,
        "lat": 55.6913,
        "lng": 12.5942,
        "price": "free",
        "rating": 4.6,
        "description": "Kopenhag'ın yıldız şeklindeki savunma kalesi. Kırmızı binaları, yel değirmeni ve üzerindeki yürüyüş parkuruyla şehrin en sevilen açık hava alanlarından biridir.",
        "description_en": "Copenhagen's star-shaped fortress. With its red buildings, windmill, and walking paths atop the ramparts, it's one of the city's most beloved outdoor spaces.",
        "imageUrl": "https://images.unsplash.com/photo-1473951574080-01fe45ec8643?w=800",
        "bestTime": "Sabah yürüyüşü",
        "bestTime_en": "Morning walk",
        "tips": "Denizkızı heykelinden sadece 5 dakikalık yürüyüş mesafesindedir.",
        "tips_en": "It is only a 5-minute walk from the Little Mermaid statue."
    },
    {
        "name": "The Black Diamond (Kraliyet Kütüphanesi)",
        "name_en": "The Black Diamond",
        "area": "Slotsholmen",
        "category": "Tarihi",
        "tags": ["kütüphane", "modern mimari", "kanal manzara", "kültür"],
        "distanceFromCenter": 0.8,
        "lat": 55.6735,
        "lng": 12.5826,
        "price": "free",
        "rating": 4.7,
        "description": "Adını parlayan siyah granit dış cephesinden alan kütüphanenin ek binası. Modern mimarisi ile kanal kıyısında ihtişamla yükselir.",
        "description_en": "The modern extension of the Royal Library, named for its shimmering black granite exterior. It rises majestically along the canal.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Kütüphanenin içindeki devasa cam atriumdan kanala bakmak büyüleyicidir.",
        "tips_en": "The view of the canal from within the library's massive glass atrium is enchanting."
    },
    {
        "name": "Designmuseum Danmark",
        "name_en": "Designmuseum Denmark",
        "area": "Fredriksstaden",
        "category": "Müze",
        "tags": ["tasarım", "mobilya", "daniş", "sanat"],
        "distanceFromCenter": 1.1,
        "lat": 55.6865,
        "lng": 12.5928,
        "price": "medium",
        "rating": 4.5,
        "description": "Danimarka ve uluslararası tasarımın ev sahibi. Jacobsen ve Wegner gibi efsanevi tasarımcıların ikonik ürünlerini burada görebilirsiniz.",
        "description_en": "Showcasing Danish and international design. You can see iconic works by legendary designers like Jacobsen and Wegner here.",
        "imageUrl": "https://images.unsplash.com/photo-1499781350541-7783f6c6a0c8?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Müzenin avlusundaki bahçe ve kafe tasarımı da oldukça ilham vericidir.",
        "tips_en": "The garden and cafe design in the museum's courtyard are also highly inspiring."
    },
    {
        "name": "Grundtvig's Kirke",
        "name_en": "Grundtvig's Church",
        "area": "Bispebjerg",
        "category": "Tarihi",
        "tags": ["mimari", "kilise", "ekspresyonizm", "dev devasa"],
        "distanceFromCenter": 5.0,
        "lat": 55.7165,
        "lng": 12.5336,
        "price": "free",
        "rating": 4.8,
        "description": "Dev bir kilise orgunu andıran mimarisiyle dünyanın en ilginç ekspresyonist kiliselerinden biri. İçi sarımsı-krem rengi tuğla dokusuyla büyüleyicidir.",
        "description_en": "One of the world's most unique expressionist churches, with architecture resembling a giant church organ. The interior's yellowish-cream brickwork is captivating.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Şehir merkezine biraz mesafededir, otobüsle Bispebjerg durağında inerek ulaşabilirsiniz.",
        "tips_en": "A bit of a distance from the city center; reach it by taking a bus and getting off at the Bispebjerg stop."
    },
    {
        "name": "Børsen (Eski Borsa Binası)",
        "name_en": "Børsen",
        "area": "Slotsholmen",
        "category": "Tarihi",
        "tags": ["mimari", "kraliyet", "tarihi bina", "ikonik"],
        "distanceFromCenter": 0.7,
        "lat": 55.6755,
        "lng": 12.5839,
        "price": "low",
        "rating": 4.7,
        "description": "Birbirine dolanmış dört ejderha kuyruğu şeklindeki karakteristik kulesiyle Kopenhag'ın en eski yapılarından ve Hollanda Rönesansı'nın başyapıtlarından.",
        "description_en": "One of Copenhagen's oldest structures and a masterpiece of Dutch Renaissance, featuring a characteristic spire formed by four intertwined dragon tails.",
        "imageUrl": "https://images.unsplash.com/photo-1473951574080-01fe45ec8643?w=800",
        "bestTime": "Dışarıdan izlemek için her zaman",
        "bestTime_en": "Always great for exterior views",
        "tips": "İçerisi halka açık olmasa da önünden geçerken kulesine mutlaka detaylı bakın.",
        "tips_en": "While the interior isn't open to the public, be sure to take a close look at the spire as you pass by."
    },
    {
        "name": "Louisiana Museum of Modern Art",
        "name_en": "Louisiana Museum of Modern Art",
        "area": "Humlebæk (Günübirlik)",
        "category": "Müze",
        "tags": ["modern sanat", "doğa", "heykel bahçesi", "deniz manzarası"],
        "distanceFromCenter": 35.0,
        "lat": 55.9522,
        "lng": 12.3789,
        "price": "high",
        "rating": 4.9,
        "description": "Dünyanın en güzel konumlu sanat müzelerinden biri. Sanat, mimari ve doğanın iç içe geçtiği müze, Oresund Boğazı manzarasına sahiptir.",
        "description_en": "One of the most beautifully situated art museums in the world. Merging art, architecture, and nature, it offers stunning views of the Oresund Strait.",
        "imageUrl": "https://images.unsplash.com/photo-1499781350541-7783f6c6a0c8?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Kopenhag merkezden trenle 35 dakikada ulaşılabilir, bir tam gün ayırmak gerekir.",
        "tips_en": "Accessible in 35 minutes by train from central Copenhagen; plan for a full-day trip."
    }
]

def enrich_kopenhag_batch1():
    filepath = 'assets/cities/kopenhag.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # First, cleanup fillers in existing highlights
    for h in data.get('highlights', []):
        if "dikkat çekici bir nokta" in h['description']:
             if h['name'] == "Tivoli Gardens":
                 h['description'] = "Dünyanın en eski ikinci lunaparkı ve Walt Disney'e ilham veren masalsı bahçe. Sadece oyuncaklarıyla değil, akşamları binlerce lambayla aydınlanan atmosferiyle büyüler."
                 h['description_en'] = "The world's second-oldest amusement park and the magical garden that inspired Walt Disney. It charms not only with its rides but with its evening atmosphere lit by thousands of lamps."
             if h['name'] == "Strøget":
                 h['description'] = "Kopenhag'ın kalbinde uzanan, Avrupa'nın en uzun yaya caddelerinden biri. Mağazaları, sokak sanatçıları ve tarihi meydanlarıyla alışverişin merkezi."
                 h['description_en'] = "One of Europe's longest pedestrian streets stretching through the heart of Copenhagen. A hub for shopping with its stores, street performers, and historic squares."

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_kopenhag_batch1:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_kopenhag_batch1()
print(f"Kopenhag now has {count} highlights.")
