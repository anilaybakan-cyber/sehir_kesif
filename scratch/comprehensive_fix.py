import json
import os

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def fix_catania():
    path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/catania.json'
    data = load_json(path)
    highlights = data.get('highlights', [])
    
    updates = {
        "Anfiteatro Romano": {
            "id": "cat_anfiteatro_romano",
            "category": "Tarihi",
            "desc": "Catania'nın kalbinde yer alan bu antik Roma amfitiyatrosu, bir zamanlar 15.000 seyirci kapasitesine sahipti. Lav taşından inşa edilen yapı, Roma İmparatorluğu'nun Sicilya'daki ihtişamını ve kentin köklü tarihini yansıtan en önemli anıtlardan biridir.",
            "desc_en": "Located in the heart of Catania, this ancient Roman amphitheater once had a capacity of 15,000 spectators. Built from lava stone, it is one of the most important monuments reflecting the grandeur of the Roman Empire in Sicily and the city's deep-rooted history."
        },
        "Piazza Carlo Alberto": {
            "id": "cat_piazza_carlo_alberto",
            "category": "Deneyim",
            "desc": "Catania'nın en büyük ve en renkli açık hava pazarlarından biri olan 'A Fera 'o Luni'ye ev sahipliği yapar. Yerel meyve, sebze ve tekstil ürünlerinin satıldığı pazar, kentin otantik yaşamını ve canlı ruhunu gözlemlemek için mükemmeldir.",
            "desc_en": "Home to 'A Fera 'o Luni', one of Catania's largest and most colorful open-air markets. Selling local fruits, vegetables, and textiles, the market is perfect for observing the city's authentic life and vibrant spirit."
        },
        "Viale Regina Margherita": {
            "id": "cat_viale_regina_margherita",
            "category": "Deneyim",
            "desc": "Şehrin en geniş ve ağaçlıklı bulvarlarından biridir. Tarihi villaları ve huzurlu atmosferiyle bilinir; akşam yürüyüşleri ve Catania'nın zarif mimarisini keşfetmek için ideal bir rotadır.",
            "desc_en": "One of the city's widest and most tree-lined boulevards. Known for its historic villas and peaceful atmosphere, it's an ideal route for evening walks and exploring Catania's elegant architecture."
        },
        "Chiosco Giammona": {
            "id": "cat_chiosco_giammona",
            "category": "Deneyim",
            "desc": "Catania'nın geleneksel 'kiosk' kültürünün en meşhur temsilcilerinden biridir. Özellikle meşhur maden suyu ve limonlu içecekleriyle ferahlamak isteyen yerellerin ve turistlerin uğrak noktasıdır.",
            "desc_en": "One of the most famous representatives of Catania's traditional 'kiosk' culture. It's a popular spot for locals and tourists alike to refresh with famous mineral water and lemon drinks."
        },
        "Sikulo": {
            "id": "cat_sikulo",
            "category": "Restoran",
            "desc": "Geleneksel Sicilya mutfağını modern bir dokunuşla sunan popüler bir restorandır. Taze deniz ürünleri ve yöresel malzemelerle hazırlanan menüsüyle Catania'da gurme bir lezzet durağıdır.",
            "desc_en": "A popular restaurant offering traditional Sicilian cuisine with a modern touch. It's a gourmet food destination in Catania with its menu prepared with fresh seafood and local ingredients."
        },
        "Toscano Palace": {
            "id": "cat_toscano_palace",
            "category": "Tarihi",
            "desc": "Catania'nın tarihi merkezinde yer alan görkemli bir yapıdır. Barok mimarinin izlerini taşıyan saray, şehrin zengin kültürel mirasını ve soylu geçmişini yansıtan önemli binalardan biridir.",
            "desc_en": "A magnificent building located in the historic center of Catania. The palace, bearing traces of Baroque architecture, is one of the important buildings reflecting the city's rich cultural heritage and noble past."
        }
    }
    
    seen_names = set()
    new_highlights = []
    for h in highlights:
        name = h.get('name')
        if name in updates:
            upd = updates[name]
            h['id'] = upd['id']
            h['category'] = upd['category']
            h['description'] = upd['desc']
            h['description_en'] = upd['desc_en']
        new_highlights.append(h)
    
    data['highlights'] = new_highlights
    save_json(path, data)
    print("Fixed Catania mismatches and IDs.")

def fix_ibiza():
    path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/ibiza.json'
    data = load_json(path)
    highlights = data.get('highlights', [])
    
    new_highlights = []
    seen_names = set()
    for h in highlights:
        name = h.get('name')
        # Only keep the first occurrence of "Harinus Forn Artesà"
        if name == "Harinus Forn Artesà":
            if name not in seen_names:
                seen_names.add(name)
                new_highlights.append(h)
        else:
            new_highlights.append(h)
            
    data['highlights'] = new_highlights
    save_json(path, data)
    print("Fixed Ibiza duplicates.")

def fix_placeholders():
    base_path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    updates = {
        "cannes.json": {
            "cann_juan-les-pins_beach": {
                "tr": "Cannes'ın en şık sahil bölgelerinden biri olan Juan-les-Pins, geniş kum plajları ve art-deco mimarisiyle ünlüdür. Gece hayatı ve caz festivaliyle tanınan bölge, Riviera'nın enerjisini en iyi yansıtan noktalardan biridir.",
                "en": "One of Cannes' most stylish coastal areas, Juan-les-Pins is famous for its wide sandy beaches and Art Deco architecture. Known for its nightlife and jazz festival, it's a spot that perfectly reflects the energy of the Riviera."
            }
        },
        "dubrovnik.json": {
            "ChIJeVmgMkp1TBMRQmPeT1RAwSQ": {
                "tr": "Dubrovnik'in en popüler aile plajlarından biridir. Çevresindeki yürüyüş yolları, restoranlar ve çocuk oyun alanlarıyla gün boyu konforlu bir vakit geçirme imkanı sunar. Sakin suları yüzmek için oldukça güvenlidir.",
                "en": "One of Dubrovnik's most popular family beaches. With surrounding walking paths, restaurants, and children's playgrounds, it offers a comfortable way to spend the day. Its calm waters are very safe for swimming."
            }
        },
        "sardinya.json": {
            "sard_scivu_beach": {
                "tr": "Sardinya'nın batı kıyısında yer alan Scivu, vahşi ve el değmemiş güzelliğiyle büyüleyicidir. Yüksek kum tepeleri ve kristal berraklığındaki turkuaz deniziyle doğaseverler için gerçek bir gizli cennettir.",
                "en": "Located on Sardinia's western coast, Scivu is enchanting with its wild and untouched beauty. With high sand dunes and crystal-clear turquoise sea, it's a true hidden paradise for nature lovers."
            }
        },
        "amalfi.json": {
            "ChIJN1U5u6KZOxMR9MY8nwnmfd4": {
                "tr": "Positano yakınlarında yer alan bu gizli koy, Amalfi Kıyısı'nın en doğal ve sakin noktalarından biridir. Sadece tekneyle veya zorlu bir patikadan yürüyerek ulaşılabilmesi, buranın huzurlu atmosferini korumasını sağlamıştır.",
                "en": "This hidden bay near Positano is one of the most natural and peaceful spots on the Amalfi Coast. Being accessible only by boat or a challenging hiking path has helped preserve its tranquil atmosphere."
            }
        }
    }
    
    for city_file, data_updates in updates.items():
        file_path = os.path.join(base_path, city_file)
        if not os.path.exists(file_path): continue
        data = load_json(file_path)
        highlights = data.get('highlights', [])
        for h in highlights:
            h_id = h.get('id')
            if h_id in data_updates:
                h['description'] = data_updates[h_id]['tr']
                h['description_en'] = data_updates[h_id]['en']
        save_json(file_path, data)
    print("Fixed remaining placeholders.")

if __name__ == "__main__":
    fix_catania()
    fix_ibiza()
    fix_placeholders()
