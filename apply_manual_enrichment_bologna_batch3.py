import json

# Manual enrichment data (Bologna Batch 3 FINAL: 15 items)
updates = {
    "Botanica Lab": {
        "description": "Bitkisel kokteyller ve botanik temalarla çalışan yaratıcı bar. Doğal malzemeler, yeşillik dekorasyonu ve mixology sanatı.",
        "description_en": "Creative bar working with botanical cocktails and plant themes. Natural ingredients, greenery decor, and mixology art."
    },
    "Galleria Cavour": {
        "description": "Bologna'nın lüks alışveriş pasajı, tasarımcı butikler ve premium markalar. İtalyan modası, elit atmosfer ve şık vitrinler.",
        "description_en": "Bologna's luxury shopping arcade with designer boutiques and premium brands. Italian fashion, elite atmosphere, and stylish window displays."
    },
    "Libreria Coop Ambasciatori": {
        "description": "Tarihi tiyatro binasında kurulan büyük kitapçı, kültürel etkinlikler ve kahve köşesiyle. İtalyan edebiyatı, uluslararası kitaplar ve okuma mekanı.",
        "description_en": "Large bookstore in historic theater building with cultural events and coffee corner. Italian literature, international books, and reading venue."
    },
    "Vicolo dei Ranocchi": {
        "description": "Finestrella'ya yakın gizli geçit, Bologna'nın eski kanallarına dair ipuçları. Romantik sokak, fotoğraf molası ve tarihi keşif.",
        "description_en": "Hidden passage near Finestrella with hints of Bologna's old canals. Romantic street, photo break, and historic discovery."
    },
    "Fresco": {
        "description": "Taze ve sağlıklı öğle yemeği seçenekleri sunan casual restoran. Salatalar, bowlar ve hafif İtalyan lezzetleri.",
        "description_en": "Casual restaurant serving fresh and healthy lunch options. Salads, bowls, and light Italian flavors."
    },
    "Costarena": {
        "description": "Spor etkinlikleri, konserler ve büyük organizasyonlara ev sahipliği yapan çok amaçlı arena. Basketbol, müzik ve gösteri.",
        "description_en": "Multi-purpose arena hosting sports events, concerts, and large organizations. Basketball, music, and shows."
    },
    "DumBO": {
        "description": "Eski endüstriyel bölgede kültür, yeme-içme ve startup hub'ı. Pazarlar, etkinlikler ve yaratıcı topluluk mekanı.",
        "description_en": "Culture, dining, and startup hub in old industrial area. Markets, events, and creative community space."
    },
    "Torre Unipol": {
        "description": "Bologna'nın en yüksek modern gökdeleni, şirket merkezi ve şehir siluetinin yeni simgesi. Çağdaş mimari ve iş dünyası.",
        "description_en": "Bologna's tallest modern skyscraper, corporate headquarters and new symbol of city skyline. Contemporary architecture and business world."
    },
    "Eataly Bologna": {
        "description": "İtalyan gıda marketi ve restoranlar kompleksi, kaliteli ürünler ve taze yemekler. Pasta, peynir, şarap ve gastronomi deneyimi.",
        "description_en": "Italian food market and restaurants complex with quality products and fresh meals. Pasta, cheese, wine, and gastronomy experience."
    },
    "Flying Tiger Copenhagen": {
        "description": "Danimarka tasarım mağazası, renkli ev eşyaları ve hediyelik ürünler. Uygun fiyat, eğlenceli tasarımlar ve pratik aksesuarlar.",
        "description_en": "Danish design store with colorful home items and gift products. Affordable price, fun designs, and practical accessories."
    },
    "Disney Store": {
        "description": "Disney karakterleri ve lisanslı ürünlerin satıldığı resmi mağaza. Oyuncaklar, kıyafetler ve aile alışverişi.",
        "description_en": "Official store selling Disney characters and licensed products. Toys, clothing, and family shopping."
    },
    "Lego Store": {
        "description": "Lego ürünlerinin ve özel setlerin satıldığı resmi mağaza. Yapı oyuncakları, koleksiyon parçaları ve çocuk eğlencesi.",
        "description_en": "Official store selling Lego products and exclusive sets. Building toys, collectibles, and children's entertainment."
    },
    "Victoria's Secret": {
        "description": "Amerikan iç giyim ve güzellik markasının mağazası. Kadın modası, parfümler ve premium iç çamaşırı.",
        "description_en": "Store of American lingerie and beauty brand. Women's fashion, perfumes, and premium underwear."
    },
    "Kiko Milano": {
        "description": "İtalyan kozmetik markasının mağazası, uygun fiyatlı makyaj ve cilt bakımı. Renkli palletler, trend ürünler ve güzellik.",
        "description_en": "Store of Italian cosmetics brand with affordable makeup and skincare. Colorful palettes, trending products, and beauty."
    },
    "Lush": {
        "description": "El yapımı kozmetik ve banyo ürünleri mağazası, doğal malzemeler ve çevre dostu yaklaşım. Banyo bombaları, sabunlar ve aromatik deneyim.",
        "description_en": "Handmade cosmetics and bath products store with natural ingredients and eco-friendly approach. Bath bombs, soaps, and aromatic experience."
    }
}

filepath = 'assets/cities/bologna.json'
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

print(f"\n✅ Manually enriched {count} items (Bologna Batch 3 FINAL).")
