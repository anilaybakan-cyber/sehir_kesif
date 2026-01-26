import json
import os

# Data for all remaining cities
cleanup_data = {
    "zermatt": {
        "Riffelalp Resort 2222m": {
            "description": "Avrupa'nın en yüksek rakımlı 5 yıldızlı oteli (2222m). Tam Matterhorn manzarası, kayak pisti erişimi ve lüks spa.",
            "description_en": "Europe's highest altitude 5-star hotel (2222m). Full Matterhorn view, ski slope access, and luxury spa."
        },
        "3100 Kulmhotel Gornergrat": {
            "description": "İsviçre Alpleri'nin en yüksek oteli, rasathane ve planetaryum içerir. Yıldızları izlemek ve buzulların üzerinde uyumak için eşsiz.",
            "description_en": "Highest hotel in Swiss Alps, includes observatory and planetarium. Unique for stargazing and sleeping above glaciers."
        },
        "BaseCamp Hotel": {
            "description": "Dağcılar için tasarlanmış modern bir 'basecamp'. Tırmanış temalı dekorasyon, rahat atmosfer ve merkezi konum.",
            "description_en": "Modern 'basecamp' designed for mountaineers. Climbing themed decoration, relaxed atmosphere, and central location."
        },
        "Carina": {
            "description": "Zermatt'ın klasik ve şık restoranlarından, İtalyan ve İsviçre mutfağı. Ahşap dekor ve sıcak atmosfer.",
            "description_en": "One of Zermatt's classic and chic restaurants, Italian and Swiss cuisine. Wooden decor and warm atmosphere."
        },
        "Golden India": {
            "description": "Alplerde otantik Hint mutfağı. Soğuk havada sıcak köri ve tandır lezzetleri, baharatlı ve doyurucu.",
            "description_en": "Authentic Indian cuisine in the Alps. Hot curry and tandoor flavors in cold weather, spicy and filling."
        },
        "Slalom Sport": {
            "description": "Kayak ve snowboard kiralama, spor giyim mağazası. Uzman tavsiyeleri ve kaliteli ekipman servisi.",
            "description_en": "Ski and snowboard rental, sportswear shop. Expert advice and quality equipment service."
        },
        "Yosemite Zermatt": {
            "description": "Outdoor giyim ve ekipman mağazası. Tırmanış ve yürüyüş için teknik kıyafetler ve dağcılık aksesuarları.",
            "description_en": "Outdoor clothing and equipment store. Technical clothes for climbing and hiking, mountaineering accessories."
        }
    },
    "saraybosna": {
        "Sebil (Sebilj Brunnen)": {
            "description": "Başçarşı'nın kalbinde 18. yüzyıl Osmanlı ahşap çeşmesi. Şehrin buluşma noktası ve güvercinleriyle meşhur simge.",
            "description_en": "18th-century Ottoman wooden fountain in heart of Baščaršija. City's meeting point and symbol famous for pigeons."
        },
        "Zlatna Ribica": {
            "description": "Antikalarla dolu, müze gibi bir kafe-bar. Caz müzik, nostaljik dekor ve şehrin en ilginç tuvaleti.",
            "description_en": "Cafe-bar filled with antiques, like a museum. Jazz music, nostalgic decor, and city's most interesting toilet."
        },
        "Kafana Ribica": {
            "description": "Nehir kenarında geleneksel Bosna balık restoranı. Taze alabalık ve huzurlu Miljacka manzarası.",
            "description_en": "Traditional Bosnian fish restaurant by the river. Fresh trout and peaceful Miljacka views."
        },
        "Çobanija Köprüsü": {
            "description": "Osmanlı döneminden kalma tarihi taş köprü, 'Şeytan Köprüsü' olarak da bilinir. Miljacka üzerinde yürüyüş.",
            "description_en": "Historic stone bridge from Ottoman era, also known as 'Devil's Bridge'. Walk over Miljacka."
        },
        "Jarčedoli": {
            "description": "Saraybosna'ya tepeden bakan mesire yeri. Doğa yürüyüşü, piknik ve panoramik şehir manzarası.",
            "description_en": "Recreation area overlooking Sarajevo. Nature hiking, picnic, and panoramic city views."
        },
        "Kamerni Teatar 55": {
            "description": "Şehrin en prestijli oda tiyatrosu. Savaş sırasında bile perdelerini kapatmayan sanat direnişinin simgesi.",
            "description_en": "City's most prestigious chamber theater. Symbol of art resistance that didn't close curtains even during war."
        }
    },
    "bruksel": {
        "Royal Greenhouses of Laeken": {
            "description": "Sadece baharda kısa süreliğine açılan Art Nouveau şaheseri kraliyet seraları. Nadir bitkiler ve cam mimari.",
            "description_en": "Art Nouveau masterpiece royal greenhouses opening briefly only in spring. Rare plants and glass architecture."
        },
        "Laurent Gerbaud Chocolatier": {
            "description": "Brüksel'in en iyi çikolatacılarından, meyve ve baharat eşleşmeleriyle ünlü. Atölye ve tadım imkanı.",
            "description_en": "One of Brussels' best chocolatiers, famous for fruit and spice pairings. Workshop and tasting opportunity."
        }
    },
    "barcelona": {
        "Museu Nacional d'Art de Catalunya (MNAC)": {
            "description": "Montjuïc Sarayı'nda Katalan sanatı müzesi. Dünyanın en iyi Romanesk fresk koleksiyonu ve şehir manzarası.",
            "description_en": "Catalan art museum in Montjuïc Palace. World's best Romanesque fresco collection and city views."
        },
        "Recinte Modernista de Sant Pau": {
            "description": "Lluís Domènech i Montaner tasarımı eski hastane kompleksi. Art Nouveau mimarisi, bahçeler ve mozaikler.",
            "description_en": "Former hospital complex designed by Lluís Domènech i Montaner. Art Nouveau architecture, gardens, and mosaics."
        }
    },
    "budapeste": {
        "Memento Park": {
            "description": "Komünist dönem heykellerinin toplandığı açık hava müzesi. Lenin, Stalin çizmeleri ve soğuk savaş tarihi.",
            "description_en": "Open-air museum where Communist era statues are gathered. Lenin, Stalin's boots, and Cold War history."
        }
    },
    "santorini": {
        "Black Beach": {
            "description": "Volkanik siyah kum ve çakıl taşlarıyla kaplı eşsiz plaj (Perissa/Kamari). Kristal deniz ve sahil barları.",
            "description_en": "Unique beach covered with volcanic black sand and pebbles (Perissa/Kamari). Crystal sea and beach bars."
        }
    },
    "zurih": {
        "Restaurant Trübli": {
            "description": "Zürih eski şehirde geleneksel İsviçre mutfağı. Rösti, Zürcher Geschnetzeltes ve rustik atmosfer.",
            "description_en": "Traditional Swiss cuisine in Zurich old town. Rösti, Zürcher Geschnetzeltes, and rustic atmosphere."
        }
    },
    "marsilya": {
        "Tarlata Café": {
            "description": "Canlı ve renkli bir kafe, yerel sanatçıların uğrak yeri. Akdeniz mezeleri ve samimi ortam.",
            "description_en": "Lively and colorful cafe, haunt of local artists. Mediterranean appetizers and friendly atmosphere."
        }
    },
    "floransa": {
        "Piazza della Repubblica (Tarihi Meydan)": {
            "description": "Floransa'nın Roma dönemi forumu üzerine kurulu büyük meydanı. Tarihi atlı karınca (Giostra) ve şık kafeler.",
            "description_en": "Florence's large square built over Roman forum. Historic carousel (Giostra) and chic cafes."
        }
    },
    "viyana": {
        "Café Sacher": {
            "description": "Orijinal Sacher Torte'nin (çikolatalı kayısılı pasta) evi. Lüks Viyana kafesi atmosferi ve uzun kuyruklar.",
            "description_en": "Home of original Sacher Torte (chocolate apricot cake). Luxury Viennese cafe atmosphere and long queues."
        }
    },
    "atina": {
        "Kerameikos": {
            "description": "Antik Atina'nın mezarlığı ve çömlekçiler semti. Mezar stelleri, müze ve akropol manzaralı sakin arkeolojik alan.",
            "description_en": "Ancient Athens' cemetery and potters' quarter. Grave steles, museum, and quiet archaeological site with Acropolis view."
        }
    },
    "madrid": {
        "Bar \"Menuda History\"": {
            "description": "Madrid tarihine tanıklık etmiş klasik tapas bar. Geleneksel lezzetler, vermut ve nostaljik fotoğraflar.",
            "description_en": "Classic tapas bar witnessing Madrid history. Traditional flavors, vermouth, and nostalgic photos."
        }
    }
}

base_path = 'assets/cities'
total_updates = 0

for city, items in cleanup_data.items():
    filepath = os.path.join(base_path, f'{city}.json')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        city_updates = 0
        for place in data['highlights']:
            name = place.get('name')
            if name in items:
                place['description'] = items[name]['description']
                place['description_en'] = items[name]['description_en']
                print(f"Enriched: {name} in {city}")
                city_updates += 1
                total_updates += 1
        
        if city_updates > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ FINAL CLEANUP COMPLETE: Enriched {total_updates} items across all cities.")
