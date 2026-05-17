#!/usr/bin/env python3
import json

routes = [
    {
        "id": "cannes_red_carpet_tour",
        "title": "Kırmızı Halı ve İkonik Cannes",
        "title_en": "Red Carpet & Iconic Cannes",
        "description": "Film festivalinin ihtişamını ve Croisette Bulvarı'nın efsanevi duraklarını keşfedin.",
        "description_en": "Discover the glamour of the film festival and the legendary stops of Boulevard de la Croisette.",
        "places": [
            "cann_palais_des_festivals",
            "cann_cannes_walk_of_fame",
            "cann_boulevard_de_la_croisette",
            "cann_carlton_beach_club"
        ]
    },
    {
        "id": "cannes_old_town_discovery",
        "title": "Tarihi Le Suquet Tepesi",
        "title_en": "Historic Le Suquet Hill",
        "description": "Cannes'ın eski balıkçı köyü ruhunu dar sokaklarda ve tarihi yapılarda gezin.",
        "description_en": "Stroll through the narrow streets and historical buildings reflecting Cannes' ancient fishing village spirit.",
        "places": [
            "cann_marché_forville",
            "cann_le_suquet_old_town",
            "cann_musée_de_la_castre",
            "cann_église_notre-dame_de_l_es"
        ]
    },
    {
        "id": "cannes_island_escape",
        "title": "Lérins Adaları Kaçamağı",
        "title_en": "Lérins Islands Escape",
        "description": "Şehrin kalabalığından uzaklaşıp doğa, deniz ve tarihle iç içe huzurlu bir ada turu.",
        "description_en": "A peaceful island tour intertwined with nature, sea, and history, away from the city crowds.",
        "places": [
            "cann_lérins_islands_ferry",
            "cann_île_sainte-marguerite",
            "cann_la_guérite",
            "cann_île_saint-honorat"
        ]
    },
    {
        "id": "cannes_luxury_shopping",
        "title": "Riviera Lüks Alışverişi",
        "title_en": "Riviera Luxury Shopping",
        "description": "Dünyaca ünlü butiklerde, lüks cadde ve sokaklarda elit bir alışveriş deneyimi yaşayın.",
        "description_en": "Experience elite shopping on luxury streets and world-renowned boutiques.",
        "places": [
            "cann_rue_d_antibes_shopping",
            "cann_boulevard_de_la_croisette",
            "cann_palm_beach_cannes",
            "cann_harry_s_bar_cannes"
        ]
    },
    {
        "id": "cannes_gastronomy_excellence",
        "title": "Michelin Yıldızlı Gastronomi",
        "title_en": "Michelin-Starred Gastronomy",
        "description": "Damaklarınızı şenlendirecek en özel ve lüks Cannes restoranlarında gurme bir gün.",
        "description_en": "A gourmet day at the most exclusive luxury Cannes restaurants to delight your palate.",
        "places": [
            "cann_astoux_et_brun",
            "cann_la_petite_maison_cannes",
            "cann_la_palme_d_or",
            "cann_la_villa_archange"
        ]
    },
    {
        "id": "cannes_beach_relaxation",
        "title": "Özel Plajlarda Dinginlik",
        "title_en": "Serenity at Private Beaches",
        "description": "Akdeniz güneşinin, yumuşak kumların ve yüksek kaliteli şezlongların tadını çıkarın.",
        "description_en": "Enjoy the Mediterranean sun, soft sands, and high-quality sun loungers.",
        "places": [
            "cann_miramar_plage",
            "cann_plage_du_festival",
            "cann_ondine_plage",
            "cann_long_beach_cannes"
        ]
    },
    {
        "id": "cannes_vibrant_nightlife",
        "title": "Riviera Gece Hayatı",
        "title_en": "Riviera Nightlife",
        "description": "Dj performansları, şampanyalar ve efsanevi kulüplerle Cannes gecelerinin ritmini yakalayın.",
        "description_en": "Catch the rhythm of Cannes nights with DJ performances, champagnes, and legendary clubs.",
        "places": [
            "cann_barrière_beach",
            "cann_baoli_cannes",
            "cann_le_cirque_cannes",
            "cann_biererie_by_casino"
        ]
    },
    {
        "id": "cannes_art_and_museums",
        "title": "Sanat ve Kültür Keşfi",
        "title_en": "Art and Culture Discovery",
        "description": "Tarihi villalardan modern sanat galerilerine kadar ufuk açıcı bir sergi ve müze rotası.",
        "description_en": "An eye-opening exhibition and museum route ranging from historical villas to modern art galleries.",
        "places": [
            "cann_malmaison_museum",
            "cann_villa_domergue",
            "cann_villa_rothschild",
            "cann_musée_de_la_castre"
        ]
    },
    {
        "id": "cannes_marina_promenade",
        "title": "Sakin Marina Yürüyüşü",
        "title_en": "Quiet Marina Promenade",
        "description": "Lüks yatların süzüldüğü ve deniz melteminin eşlik ettiği harika bir marin gezintisi.",
        "description_en": "A wonderful marina stroll accompanied by gliding luxury yachts and sea breezes.",
        "places": [
            "cann_vieux_port_cannes",
            "cann_port_canto",
            "cann_boulevard_de_la_croisette",
            "cann_cannes_bay_sunset_point"
        ]
    },
    {
        "id": "cannes_family_fun",
        "title": "Çocuklu Aileler İçin Plaj Günü",
        "title_en": "Beach Day for Families",
        "description": "Çocuklar için güvenli kumsallar, dondurma durakları ve eğlenceli açık hava sinemaları.",
        "description_en": "Safe sandy beaches for children, ice cream stops, and fun open-air cinemas.",
        "places": [
            "cann_vegaluna",
            "cann_mace_beach",
            "cann_marché_forville",
            "cann_palm_beach_cannes"
        ]
    },
    {
        "id": "cannes_romantic_getaway",
        "title": "Çiftlere Romantik Akşam",
        "title_en": "Romantic Evening for Couples",
        "description": "Şık bir akşam yemeği, gün batımında kokteyl ve romantik caz esintili rahat bir kaçamak.",
        "description_en": "A chic dinner, sunset cocktails, and a cozy getaway with romantic jazz breezes.",
        "places": [
            "cann_le_pastis",
            "cann_yvans_restaurant",
            "cann_harry_s_bar_cannes",
            "cann_rado_plage"
        ]
    },
    {
        "id": "cannes_bohemian_chic",
        "title": "Bohem Riviera Deneyimi",
        "title_en": "Bohemian Riviera Experience",
        "description": "Egzotik dekorasyonlar, tropikal lezzetler ve daha samimi, renkli bir eğlence arayanlar için.",
        "description_en": "For those seeking exotic decorations, tropical flavors, and a more intimate, colorful entertainment.",
        "places": [
            "cann_mademoiselle_gray",
            "cann_copal_beach",
            "cann_lucia_cannes",
            "cann_bobo_l_antispas"
        ]
    },
    {
        "id": "cannes_mediterranean_classic",
        "title": "Akdeniz'in Klasikleri",
        "title_en": "Classics of the Mediterranean",
        "description": "Bölgenin meşhur brasserie kültürü ve şık otel teraslarında geçmişin asaletini deneyimleyin.",
        "description_en": "Experience the nobility of the past in the region's famous brasserie culture and elegant hotel terraces.",
        "places": [
            "cann_table_22",
            "cann_le_fouquet_s",
            "cann_palme_d_or_terrace",
            "cann_l_affable"
        ]
    },
    {
        "id": "cannes_chic_beach_clubs",
        "title": "VIP Plaj Kulüpleri",
        "title_en": "VIP Beach Clubs",
        "description": "Özel misafirlerin ağırlandığı, müzik ve lüksün ön planda olduğu popüler güneşlenme tesisleri.",
        "description_en": "Popular sunbathing facilities where special guests are hosted, emphasizing music and luxury.",
        "places": [
            "cann_carlton_beach_club",
            "cann_la_plage_du_martinez",
            "cann_la_môme_plage",
            "cann_zplage"
        ]
    },
    {
        "id": "cannes_coastal_nature",
        "title": "Sahil, Doğa ve Manzara",
        "title_en": "Coast, Nature and View",
        "description": "Limandan adalara, oradan da tarihi tepeye kadar şehrin en fotojenik doğal noktaları.",
        "description_en": "The most photogenic natural spots of the city, from the port to the islands, and then to the historic hill.",
        "places": [
            "cann_vieux_port_cannes",
            "cann_lérins_islands_ferry",
            "cann_île_sainte-marguerite",
            "cann_le_suquet_old_town"
        ]
    }
]

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/cannes.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)
    if isinstance(data, list):
        highlights = data
    else:
        highlights = data.get("highlights", [])

data['curated_routes'] = routes

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Generated and injected 15 routes into {filepath}")
