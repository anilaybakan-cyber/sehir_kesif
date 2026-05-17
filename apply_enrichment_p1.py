import json
import os

updates = {
    "Amalfi": {
        "Amalfi Coast Private Driver": {
            "description": "Amalfi kıyılarının sarp virajlarında, yerel bir şoför eşliğinde Positano'dan Ravello'ya uzanan bu özel yolculuk, kentin en panoramik ve zahmetsiz keşif yöntemidir. Turkuaz denize tepeden bakan gizli duraklarda mola vererek, bölgenin tarihini ve saklı koylarını bir uzmandan dinleme şansı sunar.",
            "description_en": "This private journey with a local driver along the steep curves of the Amalfi Coast, stretching from Positano to Ravello, is the most panoramic and effortless way to explore the region. It offers the chance to stop at hidden viewpoints overlooking the turquoise sea while hearing the history and secrets of the coast from an expert.",
            "tips": "Özellikle gün batımı saatlerinde rezervasyon yapın; fotoğraf molaları için şoförünüzden 'Belvedere' noktalarında durmasını isteyin.",
            "tips_en": "Book for sunset hours; ask your driver to stop at 'Belvedere' points for the best photo opportunities.",
            "category": "Deneyim"
        },
        "Amalfi Lemon Experience": {
            "description": "Amalfi'nin dünyaca ünlü 'Sfusato Amalfitano' limonlarının yetiştiği teraslı bahçelerde, aile işletmesi bir çiftlikte limonun hasadından likör yapımına uzanan sarsıcı bir yolculuk keşfedin. Limon ağaçlarının gölgesinde yapılan tadımlarla kentin tarım mirasını ve mis kokulu ruhunu en otantik haliyle soluyun.",
            "description_en": "Discover a poignant journey from harvest to liqueur making in the terraced gardens of a family-run farm where Amalfi's world-famous 'Sfusato Amalfitano' lemons grow. Breathe in the city's agricultural heritage and fragrant spirit in its most authentic form with tastings under the shade of lemon trees.",
            "tips": "Tadım sonrası taze yapılmış Limoncello almayı unutmayın; bahçeler dik yokuşlu olduğu için rahat ayakkabılar giyin.",
            "tips_en": "Don't forget to buy freshly made Limoncello after the tasting; wear comfortable shoes as the gardens have steep slopes.",
            "category": "Doğa"
        },
        "Auditorium Oscar Niemeyer": {
            "description": "Efsanevi mimar Oscar Niemeyer tarafından tasarlanan bu fütüristik oditoryum, Ravello'nun tarihi dokusu üzerinde bembeyaz bir dalga gibi yükselen modern bir sanat eseridir. Akdeniz'in masmavi sonsuzluğuna bakan devasa penceresiyle, klasik müzik konserlerini kentin en estetik ve havadar atmosferinde sunar.",
            "description_en": "Designed by the legendary architect Oscar Niemeyer, this futuristic auditorium is a modern masterpiece rising like a white wave over Ravello's historical texture. With its massive window overlooking the deep blue Mediterranean, it hosts classical music concerts in the city's most aesthetic and airy atmosphere.",
            "tips": "Konser takvimini önceden kontrol edin; mimari fotoğrafçılık için gün ışığının en yumuşak olduğu akşamüstü saatleri idealdir.",
            "tips_en": "Check the concert schedule in advance; late afternoon hours are ideal for architectural photography when the light is softest.",
            "category": "Kültür"
        }
    },
    "Saint-Tropez": {
        "Sentier des Douaniers": {
            "description": "Saint-Tropez yarımadasını çevreleyen bu eski gümrük yolu, turkuaz koylar ve sarp kayalıklar arasında uzanan kentin en vahşi ve havadar yürüyüş rotasıdır. Lüks villaların arkasından geçerek el değmemiş plajlara ulaşan bu patika, kentin ışıltılı yüzünün ardındaki asıl doğayı keşfetmenizi sağlar.",
            "description_en": "This old customs path encircling the Saint-Tropez peninsula is the city's wildest and airiest hiking route, stretching between turquoise coves and steep cliffs. Passing behind luxury villas to reach untouched beaches, it allows you to discover the true nature behind the city's glamorous facade.",
            "tips": "Pampelonne Plajı'na kadar yürümek yaklaşık 3 saat sürer; yanınıza mutlaka su alın ve güneş kremi kullanın.",
            "tips_en": "Walking to Pampelonne Beach takes about 3 hours; make sure to bring water and wear sunscreen.",
            "category": "Doğa"
        }
    }
}

def apply_updates(city_file, city_updates):
    if not os.path.exists(city_file): return
    with open(city_file, 'r') as f:
        data = json.load(f)
    
    changed = False
    for h in data.get('highlights', []):
        name = h.get('name')
        if name in city_updates:
            upd = city_updates[name]
            h['description'] = upd['description']
            h['description_en'] = upd['description_en']
            h['tips'] = upd['tips']
            h['tips_en'] = upd['tips_en']
            h['category'] = upd['category']
            changed = True
            
    if changed:
        with open(city_file, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {city_file}")

# Apply batches
apply_updates('assets/cities/amalfi.json', updates['Amalfi'])
apply_updates('assets/cities/saint_tropez.json', updates['Saint-Tropez'])
