import json

# Manual enrichment data (Strasbourg - ALL 18 items)
updates = {
    "Place Saint-Étienne": {
        "description": "Öğrenci meydanı olarak bilinen canlı ve tarihi meydan. Ihlamur ağaçları, kafeler ve huzurlu çeşme sesi.",
        "description_en": "Lively and historic square known as student square. Lime trees, cafes, and peaceful fountain sound."
    },
    "Grenier d'Abondance": {
        "description": "15. yüzyıldan kalma tarihi tahıl ambarı, şimdi kültürel mekan. Çatısında 100'den fazla pencere, devasa kiremit çatı.",
        "description_en": "Historic granary from 15th century, now cultural venue. Over 100 windows on roof, massive tiled roof."
    },
    "Statue Gutenberg": {
        "description": "Matbaanın mucidi Johannes Gutenberg'in heykeli. Elinde 'Ve ışık oldu' yazılı İncil sayfası, Strazburg tarihinin parçası.",
        "description_en": "Statue of printing press inventor Johannes Gutenberg. Holding Bible page saying 'And there was light', part of Strasbourg history."
    },
    "Église du Temple-Neuf": {
        "description": "Grande Île'in kalbinde, neogotik Protestan kilisesi. Konserler, org müziği ve huzurlu ibadet ortamı.",
        "description_en": "Neo-Gothic Protestant church in heart of Grande Île. Concerts, organ music, and peaceful worship environment."
    },
    "Cabinet des Estampes et des Dessins": {
        "description": "Rohan Sarayı'nda grafik sanatlar koleksiyonu. Dürer ve Goya gibi ustaların gravürleri ve çizimleri.",
        "description_en": "Graphic arts collection in Rohan Palace. Engravings and drawings by masters like Dürer and Goya."
    },
    "Bibliothèque Nationale et Universitaire": {
        "description": "Alman İmparatorluğu döneminden kalma görkemli kütüphane binası. İtalyan Rönesans stili kubbe ve öğrenci merkezi.",
        "description_en": "Magnificent library building from German Empire era. Italian Renaissance style dome and student center."
    },
    "Préfecture du Bas-Rhin": {
        "description": "Eski Alman imparatorluk mimarisinin güzel bir örneği (Kaiserplatz). Heybetli taş bina ve idari merkez.",
        "description_en": "Beautiful example of former German imperial architecture (Kaiserplatz). Imposing stone building and administrative center."
    },
    "Tribunal de Grande Instance": {
        "description": "Neustadt bölgesinde neobarok adliye sarayı. Adalet terazisi heykelleri, mermer merdivenler ve hukuki tarih.",
        "description_en": "Neo-Baroque courthouse in Neustadt district. Scales of justice statues, marble stairs, and legal history."
    },
    "Sainte-Aurélie Church": {
        "description": "Gare (İstasyon) bölgesinde barok iç mekanlı Lutheran kilisesi. Eşsiz org ve yerel cemaat merkezi.",
        "description_en": "Lutheran church with baroque interior in Gare (Station) area. Unique organ and local community center."
    },
    "Arte TV Headquarters": {
        "description": "Fransız-Alman kültür kanalı Arte'nin girişindeki dev zürafa heykeli. Avrupa Parlamentosu yakınında modern simge.",
        "description_en": "Giant giraffe statue at entrance of French-German culture channel Arte. Modern symbol near European Parliament."
    },
    "La Taverne Française": {
        "description": "Yerel halkın ve sanatçıların buluştuğu bohem bar. Ucuz şarap, entelektüel sohbetler ve eski Strasbourg havası.",
        "description_en": "Bohemian bar where locals and artists meet. Cheap wine, intellectual conversations, and old Strasbourg vibe."
    },
    "Le Rafiot": {
        "description": "Ill Nehri üzerinde yüzen gece kulübü ve bar teknesi. Elektronik müzik, terasta kokteyl ve nehir manzarası.",
        "description_en": "Nightclub and bar boat floating on Ill River. Electronic music, terrace cocktails, and river views."
    },
    "Jeannette et les Cycleux": {
        "description": "Bisiklet ve retro 50'ler temalı renkli bistro. Kırmızı dekor, vintage eşyalar ve samimi kahve molası.",
        "description_en": "Colorful bistro with bicycle and retro 50s theme. Red decor, vintage items, and friendly coffee break."
    },
    "La Victoire": {
        "description": "Üniversite bölgesinde efsanevi öğrenci barı. Ucuz bira, rock müzik ve her daim kalabalık teras.",
        "description_en": "Legendary student bar in university area. Cheap beer, rock music, and always crowded terrace."
    },
    "Marché de Noël Place de la Cathédrale": {
        "description": "Katedral önündeki ana Noel pazarı. Sıcak şarap kokusu, ışıklandırılmış katedral ve büyülü atmosfer.",
        "description_en": "Main Christmas market in front of Cathedral. Smell of mulled wine, illuminated cathedral, and magical atmosphere."
    },
    "Marché de Noël du Village de Noël": {
        "description": "Noel'in başkenti Strazburg'da kurulan tematik pazar köyleri. El sanatları, bredele kurabiyeleri ve ışıklar.",
        "description_en": "Thematic market villages set up in Strasbourg, capital of Christmas. Crafts, bredele cookies, and lights."
    },
    "TNS - Théâtre National de Strasbourg (Maillon)": {
        "description": "Fransa'nın taşradaki tek ulusal tiyatrosu. Modern oyunlar, etkileyici sahne tasarımı ve kültür merkezi.",
        "description_en": "France's only national theater outside Paris. Modern plays, impressive stage design, and cultural center."
    },
    "Route des Vins d'Alsace": {
        "description": "Strazburg'dan başlayan ünlü Alsas Şarap Yolu. Bağlar, ortaçağ köyleri ve Riesling tadımları.",
        "description_en": "Famous Alsace Wine Route starting from Strasbourg. Vineyards, medieval villages, and Riesling tastings."
    }
}

filepath = 'assets/cities/strazburg.json'
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

print(f"\n✅ Manually enriched {count} items (Strasbourg - COMPLETE).")
