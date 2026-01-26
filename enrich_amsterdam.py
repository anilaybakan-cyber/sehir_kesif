import json
import os

new_amsterdam_highlights = [
    {
        "name": "Dam Meydanı (Dam Square)",
        "name_en": "Dam Square",
        "area": "Centrum",
        "category": "Tarihi",
        "tags": ["meydan", "saray", "anıt", "merkez"],
        "distanceFromCenter": 0.0,
        "lat": 52.3731,
        "lng": 4.8923,
        "price": "free",
        "rating": 4.6,
        "description": "Amsterdam'ın kalbi ve en ünlü meydanı. Royal Palace, Nieuwe Kerk ve Ulusal Anıt burada yer alır. Her zaman canlı ve hareketlidir.",
        "description_en": "The heart of Amsterdam and its most famous square. Home to the Royal Palace, Nieuwe Kerk, and the National Monument. Always lively and bustling.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Meydandaki güvercinleri besleyebilir veya merdivenlerde oturup şehri izleyebilirsiniz.",
        "tips_en": "You can feed the pigeons or just sit on the steps and watch the city go by."
    },
    {
        "name": "Koninklijk Paleis (Kraliyet Sarayı)",
        "name_en": "Royal Palace Amsterdam",
        "area": "Dam Square",
        "category": "Tarihi",
        "tags": ["saray", "monarşi", "altın çağ", "mimarisi"],
        "distanceFromCenter": 0.1,
        "lat": 52.3732,
        "lng": 4.8916,
        "price": "medium",
        "rating": 4.7,
        "description": "Dam Meydanı'ndaki ihtişamlı saray. 17. yüzyılda belediye binası olarak inşa edilmiş, bugün ise kraliyet kabul ve törenleri için kullanılmaktadır.",
        "description_en": "The grand palace on Dam Square. Built in the 17th century as a town hall, it is now used for royal receptions and ceremonies.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Kraliyet ailesi orada olmadığında içini gezebilirsiniz, mermer zeminleri ve avizeleri muhteşemdir.",
        "tips_en": "You can tour the interior when the royal family is not in residence; the marble floors and chandeliers are magnificent."
    },
    {
        "name": "Rembrandthuis (Rembrandt Evi Müzesi)",
        "name_en": "Rembrandt House Museum",
        "area": "Centrum",
        "category": "Müze",
        "tags": ["sanat", "rembrandt", "tarihi ev", "atölye"],
        "distanceFromCenter": 0.7,
        "lat": 52.3693,
        "lng": 4.9011,
        "price": "medium",
        "rating": 4.6,
        "description": "Ünlü ressam Rembrandt'ın 1639-1658 yılları arasında yaşadığı ve çalıştığı ev. Sanatçının stüdyosunu ve geniş gravür koleksiyonunu görebilirsiniz.",
        "description_en": "The house where the famous painter Rembrandt lived and worked between 1639 and 1658. You can see the artist's studio and a vast collection of etchings.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Öğleden önce",
        "bestTime_en": "Before noon",
        "tips": "Müzede yapılan gravür ve boya yapım gösterilerini kaçırmayın.",
        "tips_en": "Don't miss the etching and paint-making demonstrations in the museum."
    },
    {
        "name": "NEMO Bilim Müzesi",
        "name_en": "NEMO Science Museum",
        "area": "Oosterdok",
        "category": "Müze",
        "tags": ["bilim", "interaktif", "çocuklar", "mimari"],
        "distanceFromCenter": 1.2,
        "lat": 52.3741,
        "lng": 4.9122,
        "price": "medium",
        "rating": 4.5,
        "description": "Renzo Piano tarafından tasarlanan yeşil bir gemi şeklindeki bina. Her yaştan ziyaretçi için eğlenceli ve interaktif bilim deneyleri sunar.",
        "description_en": "A green ship-shaped building designed by Renzo Piano. Offers fun and interactive science experiments for visitors of all ages.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Müzenin çatısındaki teras ücretsizdir ve harika bir Amsterdam liman manzarasına sahiptir.",
        "tips_en": "The rooftop terrace of the museum is free and offers great views of the Amsterdam harbor."
    },
    {
        "name": "Bloemenmarkt (Yüzen Çiçek Pazarı)",
        "name_en": "Floating Flower Market",
        "area": "Centrum",
        "category": "Deneyim",
        "tags": ["çiçek", "lale", "hediyelik", "kanal"],
        "distanceFromCenter": 0.5,
        "lat": 52.3673,
        "lng": 4.8910,
        "price": "free",
        "rating": 4.2,
        "description": "Singel Kanalı üzerindeki yüzen teknelerde kurulu dünyanın tek yüzen çiçek pazarı. Her mevsim taze çiçekler ve lale soğanları bulabilirsiniz.",
        "description_en": "The world's only floating flower market, set on houseboats along the Singel Canal. You can find fresh flowers and tulip bulbs in every season.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Lale soğanlarını evinize götürmek üzere paketlenmiş halde buradan satın alabilirsiniz.",
        "tips_en": "You can buy tulip bulbs packaged for travel to take home from here."
    }
]

# Filler fixes for Amsterdam
amsterdam_fillers_fix = {
    "Anne Frank Evi": {
        "description": "İkinci Dünya Savaşı sırasında Anne Frank ve ailesinin iki yıl boyunca Nazi zulmünden saklandığı gizli bölme. Duygusal ve sarsıcı bir deneyim.",
        "description_en": "The secret annex where Anne Frank and her family hid from Nazi persecution for two years during WWII. A moving and poignant experience."
    },
    "Van Gogh Müzesi": {
        "description": "Vincent van Gogh'un dünyanın en büyük koleksiyonuna ev sahipliği yapan müze. 'Günebakanlar' gibi başyapıtları ve sanatçının mektuplarını görebilirsiniz.",
        "description_en": "Home to the world's largest collection of works by Vincent van Gogh. See masterpieces like 'Sunflowers' and the artist's personal letters."
    },
    "Rijksmuseum": {
        "description": "Hollanda'nın ulusal müzesi. Rembrandt'ın 'Gece Devriyesi' ve Vermeer'in eserleri dahil olmak üzere 800 yıllık Hollanda sanat ve tarihini barındırır.",
        "description_en": "The national museum of the Netherlands. Houses 800 years of Dutch art and history, including Rembrandt's 'The Night Watch' and works by Vermeer."
    },
    "Vondelpark": {
        "description": "Amsterdam'ın en büyük ve en ünlü parkı. Koşu yapmak, piknik yapmak veya sadece çimlerde uzanıp güneşin tadını çıkarmak için en popüler yer.",
        "description_en": "Amsterdam's largest and most famous park. The most popular spot for jogging, picnicking, or just lying on the grass and enjoying the sun."
    },
    "Jordaan": {
        "description": "Dar sokakları, şirin kanalları, bağımsız butikleri ve gizli avlularıyla (hofjes) Amsterdam'ın en karakteristik ve fotogejik mahallesi.",
        "description_en": "Amsterdam's most characteristic and photogenic neighborhood, with its narrow streets, quaint canals, independent boutiques, and hidden courtyards (hofjes)."
    }
}

def enrich_amsterdam():
    filepath = 'assets/cities/amsterdam.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Update fillers
    for h in data.get('highlights', []):
        if h['name'] in amsterdam_fillers_fix:
            fix = amsterdam_fillers_fix[h['name']]
            h['description'] = fix['description']
            h['description_en'] = fix['description_en']

    # Add new ones
    existing_names = set(h['name'] for h in data.get('highlights', []))
    for new_h in new_amsterdam_highlights:
        if new_h['name'] not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_amsterdam()
print(f"Amsterdam now has {count} highlights.")
