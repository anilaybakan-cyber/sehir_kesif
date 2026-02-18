import json

# Manual enrichment data (Batch 7 - Final Sintra items)
updates = {
    "Ursa Beach": {
        "description": "Avrupa'nın en güzel vahşi plajlarından biri olarak kabul edilen, devasa kayalık oluşumlarıyla çevrili nefes kesici bir kumsal. Dik ve zorlu bir patikadan inerek ulaşılan bu cennet, Ayı kayası (Ursa rock) ve Tüy kayası (Escada de Penedo) ile doğanın muhteşem bir heykeli gibi.",
        "description_en": "A breathtaking beach surrounded by giant rock formations, considered one of the most beautiful wild beaches in Europe. This paradise reached by descending a steep and challenging path is like a magnificent sculpture of nature with Bear rock (Ursa rock) and Escada de Penedo."
    },
    "Azenhas do Mar Viewpoint": {
        "description": "Portekiz'in en çok Instagram'lanan görüntülerinden birine ev sahipliği yapan ikonik seyir noktası. Beyaz badanalı evlerin uçurumun kenarından okyanusa doğru döküldüğü Azenhas do Mar köyünün postallık manzarasını buradan en iyi şekilde yakalayabilirsiniz.",
        "description_en": "An iconic viewpoint housing one of the most Instagrammed images of Portugal. You can best capture the postcard view of Azenhas do Mar village, where whitewashed houses spill from the edge of the cliff towards the ocean."
    },
    "Praia do Magoito": {
        "description": "Portekiz'e özgü sertleşmiş fosil kumullarıyla (duna consolidada) ünlü, yüksek iyot oranıyla sağlık turizmine de hitap eden geniş kumsal. Altın renkli kumsalı, güçlü dalgaları ve doğal havuzlarıyla hem yüzücüleri hem de sörf tutkunlarını cezbediyor.",
        "description_en": "A wide beach famous for Portugal's unique consolidated fossil dunes (duna consolidada), also catering to health tourism with its high iodine content. Its golden sand, strong waves, and natural pools attract both swimmers and surf enthusiasts."
    },
    "Curral dos Caprinos": {
        "description": "Sintra'nın geleneksel ve meşhur oğlak eti yemeği 'Cabrito Assado' (fırında oğlak) için bölgenin en saygın adresi. Taş fırında saatlerce pişirilen bu lezzet, yerel şarapları eşliğinde Portekiz köy mutfağının en otantik halini deneyimlemek isteyenler için kaçırılmamalı.",
        "description_en": "The region's most respected address for Sintra's traditional and famous goat meat dish 'Cabrito Assado' (roast kid). This flavor slowly cooked in a stone oven for hours is not to be missed for those wanting to experience the most authentic Portuguese village cuisine with local wines."
    },
    "Apeadeiro": {
        "description": "Sintra tren istasyonunun yakınında, yerel halkın düzenli olarak uğradığı, gösterişsiz ama lezzetli geleneksel Portekiz lokantası. Günün menüsü (prato do dia), ev yapımı çorbaları ve cömert porsiyonlarıyla, turist fiyatlarından uzak otantik bir öğle yemeği deneyimi sunuyor.",
        "description_en": "A traditional Portuguese restaurant near Sintra train station frequented regularly by locals, unpretentious but delicious. With its daily menu (prato do dia), homemade soups, and generous portions, it offers an authentic lunch experience away from tourist prices."
    },
    "Café Saudade": {
        "description": "Sintra'nın tarihi bir binasında, nostaljik vintage dekorasyonu ve ev yapımı muhteşem tatlılarıyla ün yapmış butik kafe. Portekiz'in meşhur 'Pastel de Nata'sı, yerel peynirli tart 'Queijada' ve aromatik kahveleriyle, kahve molası için mükemmel bir durak.",
        "description_en": "A boutique cafe in a historic Sintra building, famous for its nostalgic vintage decor and magnificent homemade desserts. A perfect stop for a coffee break with Portugal's famous 'Pastel de Nata', local cheese tart 'Queijada', and aromatic coffees."
    },
    "Bar do Fundo": {
        "description": "Praia Grande plajının sonunda, okyanusa bakan konumuyla gün batımına karşı şık akşam yemekleri sunan atmosferik restoran ve bar. Taze deniz ürünleri, soğuk içkiler ve romantik manzarasıyla, sahil gününü taçlandırmak için ideal bir mekan.",
        "description_en": "An atmospheric restaurant and bar at the end of Praia Grande beach, offering stylish dinners against the sunset with its ocean-facing position. An ideal venue to crown a beach day with fresh seafood, cold drinks, and romantic views."
    },
    "News Museum": {
        "description": "Sintra'da medya, gazetecilik ve iletişim tarihine adanmış modern ve interaktif bir müze. Matbaanın icadından dijital çağa uzanan sergileri, uygulamalı etkinlikleri ve tarihi basın arşivleriyle, her yaştan ziyaretçiye eğlenceli ve öğretici bir deneyim sunuyor.",
        "description_en": "A modern and interactive museum in Sintra dedicated to the history of media, journalism, and communication. With exhibitions spanning from the invention of printing to the digital age, hands-on activities, and historic press archives, it offers a fun and educational experience for visitors of all ages."
    },
    "Fonte da Sabuga": {
        "description": "Sintra'nın en eski ve en meşhur tarihi çeşmelerinden biri, geleneksel mavi-beyaz azulejo çinileriyle süslü zarif yapısıyla dikkat çekiyor. Efsaneye göre suyu içenler tekrar Sintra'ya dönecek; bu büyüleyici şehre veda ederken uğramadan geçilmemeli.",
        "description_en": "One of Sintra's oldest and most famous historic fountains, notable for its elegant structure decorated with traditional blue-white azulejo tiles. According to legend, those who drink its water will return to Sintra again; not to be passed by when saying goodbye to this enchanting city."
    }
}

filepath = 'assets/cities/sintra.json'
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

print(f"\n✅ Manually enriched {count} items (Batch 7 - Sintra Complete).")
