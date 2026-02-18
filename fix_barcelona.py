import json
import os

barcelona_fillers_fix = {
    "Gothic Quarter": {
        "description": "Roma temelleri üzerine kurulu, dar Orta Çağ sokakları, görkemli katedrali ve gizli meydanlarıyla şehrin tarihi kalbi.",
        "description_en": "Built on Roman foundations, the city's historic heart with narrow medieval streets, a grand cathedral, and hidden squares."
    },
    "La Boqueria": {
        "description": "Dünyanın en ünlü kapalı pazarlarından biri. Taze deniz ürünleri, meyveler, İspanyol jambonları ve yerel tapas duraklarıyla bir lezzet festivali.",
        "description_en": "One of the world's most famous covered markets. A feast of fresh seafood, fruit, Spanish hams, and local tapas stalls."
    },
    "Barceloneta Beach": {
        "description": "Şehir merkezine en yakın ve en canlı plaj. Akdeniz güneşinin, sahil yürüyüşlerinin ve 'chiringuito' adı verilen plaj barlarının keyfini sürün.",
        "description_en": "The liveliest beach closest to the city center. Enjoy the Mediterranean sun, seaside walks, and beach bars called 'chiringuitos'."
    },
    "El Born": {
        "description": "Orta Çağ mimarisinin modern butikler ve havalı gece hayatıyla buluştuğu, Picasso Müzesi'ne de ev sahipliği yapan bohem ve şık semt.",
        "description_en": "A chic bohemian district where medieval architecture meets modern boutiques and cool nightlife, also home to the Picasso Museum."
    },
    "Parc de la Ciutadella": {
        "description": "Barcelona'nın ana akciğeri. 19. yüzyıldan kalma dev şelalesi, göleti, heykelleri ve içindeki hayvanat bahçesiyle şehrin en popüler yeşil alanı.",
        "description_en": "Barcelona's main green lung. The city's most popular green space with its 19th-century giant waterfall, pond, statues, and onsite zoo."
    },
    "Palau de la Música Catalana": {
        "description": "Lluís Domènech i Montaner tarafından tasarlanan modernizm şaheseri. Renkli vitray tavanı ve görkemli süslemeleriyle dünyanın en güzel konser salonlarından biri.",
        "description_en": "A modernism masterpiece designed by Lluís Domènech i Montaner. One of the world's most beautiful concert halls with its stained-glass ceiling."
    },
    "MNAC": {
        "description": "Katalan Ulusal Sanat Müzesi. Romanesk kilise fresklerinden modern sanata kadar uzanan dev koleksiyonu ve saray gibi binasıyla büyüleyicidir.",
        "description_en": "Catalonia's National Art Museum. Enchanting with its vast collection from Romanesque church frescoes to modern art, all set in a majestic palace."
    },
    "Magic Fountain of Montjuïc": {
        "description": "Işık, müzik ve suyun senkronize dansı. Montjuïc Tepesi'nin eteklerinde yer alan bu görsel şölen, Barcelona akşamlarının vazgeçilmezidir.",
        "description_en": "A synchronized dance of light, music, and water. This spectacular show at the foot of Montjuïc is an essential Barcelona evening experience."
    },
    "Barceloneta Mahallesi": {
        "description": "Eski balıkçı mahallesi. İnce dar sokakları, balkonlardan sarkan çamaşırları ve şehrin en iyi deniz ürünleri restoranlarıyla çok karakteristiktir.",
        "description_en": "The old fisherman's quarter. Extremely characteristic with its narrow streets, laundry hanging from balconies, and the city's best seafood."
    },
    "Plaça Reial": {
        "description": "La Rambla'nın hemen yanında, Gaudi tasarımı fenerleri, palmiye ağaçları ve çevresindeki restoranlarla şehrin en zarif meydanlarından biri.",
        "description_en": "One of the city's most elegant squares next to La Rambla, featuring Gaudi-designed lampposts, palm trees, and many restaurants."
    }
}

def fix_barcelona_fillers():
    filepath = 'assets/cities/barcelona.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for h in data.get('highlights', []):
        if h['name'] in barcelona_fillers_fix:
            fix = barcelona_fillers_fix[h['name']]
            h['description'] = fix['description']
            h['description_en'] = fix['description_en']

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("Barcelona fillers fixed.")

fix_barcelona_fillers()
