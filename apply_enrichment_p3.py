import json
import os

updates = {
    "Rhodes": {
        "RONDA - Resto | Beach-Bar": {
            "description": "Rodos'un kentsel silüetinde modern bir vaha olan RONDA, Elli Plajı'nın kalbinde sofistike bir 'beach-club' deneyimi sunuyor. Yerel Ege lezzetlerini dünya mutfağıyla harmanlayan mutfağı ve günün her saati değişen dinamik atmosferiyle kentin en prestijli buluşma noktasıdır.",
            "description_en": "A modern oasis in Rhodes' urban silhouette, RONDA offers a sophisticated 'beach-club' experience in the heart of Elli Beach. Blending local Aegean flavors with international cuisine, it is the city's most prestigious meeting point with its dynamic atmosphere that evolves throughout the day.",
            "tips": "Özellikle gün batımı kokteylleri ve suşi mönüsü çok popülerdir; ön sıralarda şezlong için erken gelin.",
            "tips_en": "The sunset cocktails and sushi menu are particularly popular; arrive early for front-row sun loungers.",
            "category": "Sosyal"
        },
        "Bee Museum of Rhodes": {
            "description": "Rodos'un binlerce yıllık arıcılık geleneğine açılan bu müze, balın doğadaki serüveninden sofralara gelişine kadar olan süreci interaktif bir şekilde sunuyor. Arıların gizemli dünyasını keşfederken, bölgenin eşsiz florasından elde edilen şifalı ürünlerin tadımını yapma fırsatı bulursunuz.",
            "description_en": "Opening a window into Rhodes' millennia-old beekeeping tradition, this museum interactively presents the journey of honey from nature to the table. While discovering the mysterious world of bees, you have the opportunity to taste medicinal products derived from the region's unique flora.",
            "tips": "Müze dükkanındaki yerel 'Melekouni' tatlısını mutlaka deneyin; çocuklar için harika bir eğitici duraktır.",
            "tips_en": "Be sure to try the local 'Melekouni' sweet in the museum shop; it's a great educational stop for children.",
            "category": "Müze"
        }
    },
    "Valencia": {
        "Palau de Cervelló": {
            "description": "Valencia'nın tarihi merkezinde yer alan bu görkemli saray, 19. yüzyılda kralların konakladığı bir aristokrasi merkezidir. Kentin siyasi tarihine ışık tutan zengin kütüphanesi ve dönem mobilyalarıyla dekore edilmiş salonlarıyla, Valensiya'nın asil geçmişine entelektüel bir yolculuk sunar.",
            "description_en": "Located in Valencia's historical center, this magnificent palace was an aristocratic hub where kings stayed in the 19th century. With its rich library shedding light on the city's political history and halls decorated with period furniture, it offers an intellectual journey into Valencia's noble past.",
            "tips": "Sarayın iç avlusu fotoğraf çekimi için çok estetiktir; giriş ücreti oldukça makuldür.",
            "tips_en": "The palace's inner courtyard is very aesthetic for photography; the entrance fee is quite reasonable.",
            "category": "Kültür"
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
apply_updates('assets/cities/rhodes.json', updates['Rhodes'])
apply_updates('assets/cities/valencia.json', updates['Valencia'])
