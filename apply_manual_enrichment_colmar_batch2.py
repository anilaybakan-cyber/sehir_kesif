import json

# Manual enrichment data (Colmar Batch 2 FINAL: 20 items)
updates = {
    "Le 3": {
        "description": "Modern Alsace mutfağını yaratıcı bir şekilde sunan contemporary restoran. Mevsimlik menü, yerel malzemeler ve şık atmosfer.",
        "description_en": "Contemporary restaurant creatively serving modern Alsace cuisine. Seasonal menu, local ingredients, and stylish atmosphere."
    },
    "Confiserie Bruntz": {
        "description": "Geleneksel Alsace şekerleme ve kurabiyelerinin satıldığı aile işletmesi. Bredele, bonbon ve Noel spesiyalleri.",
        "description_en": "Family business selling traditional Alsace confectionery and cookies. Bredele, bonbons, and Christmas specials."
    },
    "L'Arpège": {
        "description": "Klasik Fransız mutfağını Alsace esintisiyle sunan fine-dining restoran. Foie gras, balık ve özenli sunum.",
        "description_en": "Fine-dining restaurant serving classic French cuisine with Alsace influence. Foie gras, fish, and careful presentation."
    },
    "Caveau Saint-Jean": {
        "description": "Tarihi şarap mahzeninde yer alan şarap barı ve restoran. Alsace şarap tadımları, flammkuchen ve romantik atmosfer.",
        "description_en": "Wine bar and restaurant in historic wine cellar. Alsace wine tastings, flammkuchen, and romantic atmosphere."
    },
    "Mont Donon": {
        "description": "Vosges Dağları'ndaki tarihi zirve, Kelt ve Roma kalıntıları. Panoramik manzara, yürüyüş rotaları ve arkeolojik alan.",
        "description_en": "Historic peak in Vosges Mountains with Celtic and Roman remains. Panoramic views, hiking trails, and archaeological site."
    },
    "Château de Saint-Ulrich": {
        "description": "Ribeauvillé yakınındaki ortaçağ kale kalıntıları, tırmanış ve manzara. Üç kale rotasının bir parçası, gotik mimari.",
        "description_en": "Medieval castle ruins near Ribeauvillé for climbing and views. Part of three castles route, Gothic architecture."
    },
    "Château du Haut-Ribeaupierre": {
        "description": "Ribeauvillé üzerindeki yüksek kalelerden biri, zorlu tırmanış ve ödüllendirici manzara. Kale kalıntıları ve orman yürüyüşü.",
        "description_en": "One of high castles above Ribeauvillé for challenging climb and rewarding views. Castle ruins and forest hiking."
    },
    "Kaysersberg Castle": {
        "description": "Kaysersberg köyünü koruyan ortaçağ kalesi, dönjon ve şehir panoraması. Tırmanış, fotoğrafçılık ve tarihi keşif.",
        "description_en": "Medieval castle protecting Kaysersberg village with donjon and town panorama. Climbing, photography, and historic exploration."
    },
    "Grand Ballon Luge d'été": {
        "description": "Vosges'un en yüksek zirvesinde yaz kızağı pisti. Adrenalin, dağ manzarası ve aile eğlencesi.",
        "description_en": "Summer toboggan run at highest peak of Vosges. Adrenaline, mountain views, and family fun."
    },
    "Lac de Kruth-Wildenstein": {
        "description": "Vosges Dağları'ndaki yapay göl, su sporları ve yürüyüş. Kano, yüzme ve doğa kaçışı.",
        "description_en": "Artificial lake in Vosges Mountains for water sports and hiking. Canoeing, swimming, and nature escape."
    },
    "Eau-de-Vie Museum": {
        "description": "Alsace damıtılmış içkilerin tarihini ve üretimini anlatan müze. Kirsch, mirabelle ve tadım deneyimi.",
        "description_en": "Museum telling history and production of Alsace distilled spirits. Kirsch, mirabelle, and tasting experience."
    },
    "Fort de Schoenenbourg": {
        "description": "Maginot Hattı'nın en iyi korunan kalelerinden biri, yeraltı turları. Savaş tarihi, askeri mühendislik ve eğitim.",
        "description_en": "One of best-preserved fortresses of Maginot Line with underground tours. War history, military engineering, and education."
    },
    "Four à Chaux": {
        "description": "Eski kireç ocağı kalıntısı, endüstriyel miras ve doğa yürüyüşü. Yerel tarih, arkeoloji ve keşif.",
        "description_en": "Old lime kiln remains, industrial heritage and nature walking. Local history, archaeology, and discovery."
    },
    "Plan Incliné de Saint-Louis-Arzviller": {
        "description": "Dünyanın en büyük eğimli kanal asansörü, tekne turları ve mühendislik harikası. Endüstriyel turizm ve ulaşım tarihi.",
        "description_en": "World's largest inclined canal lift with boat tours and engineering marvel. Industrial tourism and transport history."
    },
    "Grotte Saint-Vit": {
        "description": "Ortaçağ'dan beri hac yeri olan doğal mağara, dini önemi ve doğa. Sessiz mola, manevi atmosfer ve orman.",
        "description_en": "Natural cave serving as pilgrimage site since medieval times. Quiet break, spiritual atmosphere, and forest."
    },
    "Cascades du Tendon": {
        "description": "Vosges'daki şelaleler, doğa yürüyüşü ve fotoğrafçılık. Orman patikası, serinlik ve hafta sonu kaçışı.",
        "description_en": "Waterfalls in Vosges for nature hiking and photography. Forest trail, coolness, and weekend escape."
    },
    "Lac de Longemer": {
        "description": "Vosges'un en güzel göllerinden biri, yüzme, kano ve kamp. Dağ manzarası, plaj alanı ve açık hava.",
        "description_en": "One of Vosges's most beautiful lakes for swimming, canoeing, and camping. Mountain views, beach area, and outdoors."
    },
    "Saboterie des Lacs": {
        "description": "Geleneksel tahta takunya (sabot) atölyesi, üretimi izleme ve satın alma. Alsace zanaatı, hediyelik ve folklor.",
        "description_en": "Traditional wooden clog (sabot) workshop, watching production and buying. Alsace craftsmanship, souvenirs, and folklore."
    },
    "Source de la Moselle": {
        "description": "Mosel Nehri'nin kaynağı, Vosges Dağları'nda doğa yürüyüşü noktası. Coğrafya merakı, orman ve taze hava.",
        "description_en": "Source of Moselle River, nature hiking point in Vosges Mountains. Geography curiosity, forest, and fresh air."
    },
    "Musée du Pain d'Epices": {
        "description": "Alsace zencefilli ekmeğinin tarihini ve yapımını anlatan müze. Tadım, atölye ve geleneksel lezzetler.",
        "description_en": "Museum telling history and making of Alsace gingerbread. Tasting, workshop, and traditional flavors."
    }
}

filepath = 'assets/cities/colmar.json'
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

print(f"\n✅ Manually enriched {count} items (Colmar Batch 2 FINAL).")
