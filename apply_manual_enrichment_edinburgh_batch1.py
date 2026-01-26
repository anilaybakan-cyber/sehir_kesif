import json

# Manual enrichment data (Edinburgh - ALL 9 items)
updates = {
    "St Cecilia's Hall": {
        "description": "İskoçya'nın en eski konser salonu ve müzik müzesi. Tarihi enstrümanlar, zarif iç mekan ve canlı performanslar.",
        "description_en": "Scotland's oldest concert hall and music museum. Historic instruments, elegant interior, and live performances."
    },
    "Greyfriars Bobby Statue": {
        "description": "Sahibinin mezarını 14 yıl bekleyen sadık Skye Terrier köpeğinin heykeli. Burnunu ovmanın şans getirdiğine inanılır.",
        "description_en": "Statue of loyal Skye Terrier dog who waited by his master's grave for 14 years. Rubbing its nose is believed to bring luck."
    },
    "Grassmarket Gallows": {
        "description": "Tarihi idam noktası, şimdi canlı publar bölgesi. Covenanters anıtı, Maggie Dickson'ın hikayesi ve karanlık tarih.",
        "description_en": "Historic execution spot, now lively pub area. Covenanters memorial, story of Maggie Dickson, and dark history."
    },
    "Usher Hall": {
        "description": "Edinburgh'un beş yıldızlı konser salonu, muhteşem akustik. Klasik, caz ve rock konserlerine ev sahipliği yapar.",
        "description_en": "Edinburgh's five-star concert hall, magnificent acoustics. Hosts classical, jazz, and rock concerts."
    },
    "The Stand Comedy Club": {
        "description": "Dünyaca ünlü komedi kulübü, Fringe Festivali'nin kalbi. Stand-up şovları, yeni yetenekler ve samimi bodrum katı.",
        "description_en": "World-famous comedy club, heart of Fringe Festival. Stand-up shows, new talents, and intimate basement."
    },
    "Dugald Stewart Monument": {
        "description": "Calton Hill üzerinde ikonik anıt, Atina mimarisi esintili. Şehrin en popüler gün batımı ve kale manzarası noktası.",
        "description_en": "Iconic monument on Calton Hill, inspired by Athenian architecture. City's most popular sunset and castle view spot."
    },
    "Falkirk Wheel": {
        "description": "Mühendislik harikası döner tekne asansörü. Union ve Forth kanallarını birbirine bağlayan fütüristik yapı.",
        "description_en": "Engineering marvel rotating boat lift. Futuristic structure connecting Union and Forth canals."
    },
    "Water of Leith Visitor Centre": {
        "description": "Şehri boydan boya geçen nehir yolu hakkında bilgi merkezi. Yürüyüş rotaları, yaban hayatı ve interaktif sergiler.",
        "description_en": "Information center about river walkway traversing the city. Walking routes, wildlife, and interactive exhibitions."
    },
    "Beecraigs Country Park": {
        "description": "Linlithgow yakınlarında geniş orman parkı. Geyik çiftliği, göl yürüyüşü, macera parkuru ve barbekü alanları.",
        "description_en": "Large forest park near Linlithgow. Deer farm, lake walk, adventure course, and BBQ areas."
    }
}

filepath = 'assets/cities/edinburgh.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data['highlights']:
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        print(f"Enriched: {name}")
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Manually enriched {count} items (Edinburgh - COMPLETE).")
