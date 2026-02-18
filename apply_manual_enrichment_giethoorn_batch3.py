import json

# Manual enrichment data (Giethoorn Batch 3 FINAL: 25 items)
updates = {
    "Bezoekerscentrum De Wieden Water Tower": {
        "description": "Tarihi su kulesinde konumlanan ziyaretçi merkezi, Weerribben-Wieden hakkında bilgi ve sergiler. Doğa parkı haritaları, rehberli turlar ve ekolojik eğitim.",
        "description_en": "A visitor center in historic water tower with information and exhibitions about Weerribben-Wieden. Nature park maps, guided tours, and ecological education."
    },
    "Pantropica": {
        "description": "Tropik bitkileri ve egzotik hayvanları barındıran kapalı bahçe. Kelebekler, papağanlar ve tropikal bitkilerle, yağmurlu günlerde ideal aktivite.",
        "description_en": "An indoor garden housing tropical plants and exotic animals. Ideal activity on rainy days with butterflies, parrots, and tropical plants."
    },
    "Netl de Wildste Tuin": {
        "description": "Yaban hayatı ve doğal tarımı harmanlayan, sürdürülebilir yaşam konseptli alternatif bahçe. Permakültür, organik tarım ve ekolojik atölyeler.",
        "description_en": "An alternative garden blending wildlife and natural farming with sustainable living concept. Permaculture, organic farming, and ecological workshops."
    },
    "Schokland": {
        "description": "UNESCO Dünya Mirası listesinde, eski Zuiderzee'de yükselen tarihi ada-köy. Deniz seviyesinin altında yaşam mücadelesini anlatan müze ve kalıntılar.",
        "description_en": "A historic island-village on UNESCO World Heritage list rising in old Zuiderzee. Museum and remains telling the struggle of life below sea level."
    },
    "Museum Schokland": {
        "description": "Schokland'ın tarihi ve Zuiderzee'nin kapanışını anlatan arkeoloji ve tarih müzesi. Eski yaşam kalıntıları, balıkçı kültürü ve Hollanda su mücadelesi.",
        "description_en": "An archaeology and history museum telling Schokland's history and closure of Zuiderzee. Old life remains, fishing culture, and Dutch water struggle."
    },
    "Vuurtoren van Urk": {
        "description": "Urk balıkçı kasabasının ikonik feneri, deniz tarihi ve manzara noktası. Eski balıkçı köyünün simgesi, panoramik IJsselmeer manzarası.",
        "description_en": "Iconic lighthouse of Urk fishing town, maritime history and viewpoint. Symbol of old fishing village, panoramic IJsselmeer views."
    },
    "Lemmer": {
        "description": "Friesland'daki tarihi su sporları kasabası, yelken yarışları ve marina kültürüyle. Hollanda su sporları başkenti, Ir. D.F. Wouda gemisi.",
        "description_en": "A historic water sports town in Friesland with sailing races and marina culture. Dutch water sports capital, Ir. D.F. Wouda pumping station."
    },
    "Ir. D.F. Woudagemaal": {
        "description": "UNESCO Dünya Mirası listesindeki dünyanın en büyük buhar tahrikli pompa istasyonu. 1920'lerden kalma endüstriyel miras ve mühendislik harikası.",
        "description_en": "World's largest steam-powered pumping station on UNESCO World Heritage list. Industrial heritage from 1920s and engineering marvel."
    },
    "Meppel": {
        "description": "Drenthe'nin kanallar üzerine kurulu şirin kasabası, hafta pazarı ve tarihi merkeziyle. Hollanda kırsalında alışveriş ve kültür durağı.",
        "description_en": "A charming town in Drenthe built on canals with weekly market and historic center. Shopping and culture stop in Dutch countryside."
    },
    "Drukkerijmuseum Meppel": {
        "description": "Eski baskı makinelerini ve matbaacılık tarihini sergileyen endüstriyel müze. Antik baskı teknikleri, el yazmaları ve kağıt üretimi.",
        "description_en": "An industrial museum exhibiting old printing machines and printing history. Antique printing techniques, manuscripts, and paper production."
    },
    "Molen De Vlijt": {
        "description": "Meppel yakınındaki tarihi yel değirmeni, hâlâ çalışır durumda ve ziyarete açık. Hollanda değirmencilik geleneği, tahıl öğütme gösterisi.",
        "description_en": "A historic windmill near Meppel, still operational and open to visitors. Dutch milling tradition, grain grinding demonstration."
    },
    "Havelte": {
        "description": "Tarihi hunebedleri (megalitik mezarları) barındıran küçük köy. Neolitik dönem kalıntıları, arkeolojik turlar ve antik tarih.",
        "description_en": "A small village housing historic hunebeds (megalithic tombs). Neolithic period remains, archaeological tours, and ancient history."
    },
    "Hunebed D53": {
        "description": "Hollanda'nın en büyük ve en iyi korunmuş hunebedi, 5000 yıllık megalitik mezar anıtı. Prehistorik miras, taş yapılar ve gizemli geçmiş.",
        "description_en": "The Netherlands' largest and best-preserved hunebed, 5000-year-old megalithic tomb monument. Prehistoric heritage, stone structures, and mysterious past."
    },
    "Kamp Westerbork": {
        "description": "İkinci Dünya Savaşı sırasında transit kampı olan, şimdi anıt müze olarak hizmet veren yer. Holokost anıları, Anne Frank'ın son durağı, tarihi farkındalık.",
        "description_en": "A location that was a transit camp during World War II, now serving as memorial museum. Holocaust memories, Anne Frank's last stop, historical awareness."
    },
    "Dwingelderveld National Park": {
        "description": "Batı Avrupa'nın en büyük ıslak çayır alanlarından biri, nadir flora ve fauna ile. Fundalıklar, göletler ve doğa yürüyüşleri.",
        "description_en": "One of Western Europe's largest wet meadow areas with rare flora and fauna. Heathlands, ponds, and nature walks."
    },
    "Planetron": {
        "description": "Dwingeloo'daki radyo teleskop ve astronomi merkezi, uzay bilimi ve gökyüzü gözlemi. Planetaryum gösterileri, yıldız gözleme geceleri.",
        "description_en": "Radio telescope and astronomy center in Dwingeloo, space science and sky observation. Planetarium shows, stargazing nights."
    },
    "Vlinderparadijs Papiliorama": {
        "description": "Tropik kelebekler ve egzotik böcekleri barındıran kapalı bahçe. Rengarenk türler, yaşam döngüleri ve doğa eğitimi.",
        "description_en": "An indoor garden housing tropical butterflies and exotic insects. Colorful species, life cycles, and nature education."
    },
    "Kasteel Coevorden": {
        "description": "Coevorden kasabasındaki ortaçağ kalesi, tarihi surları ve müzesiyle. Hollanda savunma mimarisi, yerel tarih ve kale turları.",
        "description_en": "A medieval castle in Coevorden town with historic walls and museum. Dutch defense architecture, local history, and castle tours."
    },
    "Wildlands Adventure Zoo Emmen": {
        "description": "Tema parklı modern hayvanat bahçesi, Afrika, Asya ve Kutup bölümlerle. Safari deneyimi, tropikal orman ve buz dünyası.",
        "description_en": "A modern zoo with theme park, featuring Africa, Asia, and Polar sections. Safari experience, tropical jungle, and ice world."
    },
    "Dolmen Center Borger": {
        "description": "Hollanda'nın hunebed başkentinde, megalitik kültürü anlatan arkeoloji müzesi. Gerçek boyutlu modeller, interaktif sergiler ve prehistorik yaşam.",
        "description_en": "An archaeology museum in the Netherlands' hunebed capital explaining megalithic culture. Full-scale models, interactive exhibitions, and prehistoric life."
    },
    "Klimbos Avontuurlijk Paasloo": {
        "description": "Ağaçlar arasında macera parkuru, tırmanma ve zip-line aktiviteleriyle. Aileler için eğlence, adrenalin ve doğa sporları.",
        "description_en": "An adventure course among trees with climbing and zip-line activities. Entertainment for families, adrenaline, and nature sports."
    },
    "De Zwieseborg": {
        "description": "Drenthe'deki ortaçağ şato kalıntıları, tarihi bahçeleri ve restorasyonuyla. Romantik manzara, tarihi turlar ve fotoğraf için ideal.",
        "description_en": "Medieval castle remains in Drenthe with historic gardens and restoration. Romantic scenery, historic tours, and ideal for photography."
    },
    "Waanders In de Broeren": {
        "description": "Zwolle'de eski kiliseye dönüştürülmüş muhteşem kitapçı ve kafe. Gotik mimari içinde kitap keşfi, kahve ve kültürel atmosfer.",
        "description_en": "A magnificent bookstore and cafe converted from old church in Zwolle. Book discovery within Gothic architecture, coffee, and cultural atmosphere."
    },
    "Dinouk": {
        "description": "Urk'taki interaktif dinozor parkı ve eğlence merkezi. Gerçek boyutlu dinozor replikleri, çocuklar için eğitici aktiviteler.",
        "description_en": "Interactive dinosaur park and entertainment center in Urk. Life-size dinosaur replicas, educational activities for children."
    },
    "Taman Indonesia Restaurant": {
        "description": "Endonezya mutfağı sunan, otantik rijsttafel deneyimi için ideal restoran. Baharat zenginliği, egzotik lezzetler ve sömürge dönemi tarihi.",
        "description_en": "A restaurant serving Indonesian cuisine, ideal for authentic rijsttafel experience. Spice richness, exotic flavors, and colonial era history."
    }
}

filepath = 'assets/cities/giethoorn.json'
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

print(f"\n✅ Manually enriched {count} items (Giethoorn Batch 3 FINAL).")
