
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New Turkish Description
UPDATES = {
    # HONG KONG
    "Mu": "Tsim Sha Tsui'de, şefin önünüzde hazırladığı özel suşi ve sashimi sunan interaktif Japon restoranı.",
    "Sugar Brothers hk": "Tatlı krizleri için harika bir durak, çeşitli tatlılar ve atıştırmalıklar sunan keyifli mekan.",

    # LUCERNE
    "Bar León": "İspanyol tapasları, deniz ürünleri ve chorizo eşliğinde keyifli bir akşam yemeği için ideal mekan.",
    "Jardin Oriental (Restaurant &Take Away)": "Geleneksel Türk kebapları ve baklava çeşitleriyle, sıcak ve samimi atmosferde Doğu lezzetleri sunan restoran.",
    "Melissa's Kitchen": "Harika pazar brunchları, ev yapımı kekler ve vejetaryen seçenekler sunan sıcak ve samimi kafe.",
    "Onkel Salamat": "Taze falafel, tavuk dürüm ve sandviçleriyle bilinen, hızlı ve doyurucu bir lezzet durağı.",
    "Salvatore Icilio La Bottega Del Buongustaio": "Eski Şehir'de, taze makarna ve Sicilya spesiyalleri sunan otantik İtalyan şarküteri ve restoranı.",
    "Wirtshaus Taube Luzern": "Nehir kenarında, geleneksel İsviçre fondüsü ve rösti sunan rustik ve tarihi taverna.",
    "tschuppi's wonderbar": "Canlı müzik ve geniş içki menüsüyle gece hayatının nabzını tutan eğlenceli ve hareketli bar.",
    "Äss-Bar": "Gıda israfını önlemek için fırınlardan kalan taze ürünleri indirimli sunan sürdürülebilir kafe.",

    # MADRID
    "Despacito Specialty Coffee - Café Especialidad": "Nitelikli kahveleri ve sürpriz unlu mamul paketleriyle bilinen, kahve tutkunları için özel bir durak.",
    "Lito Pastelería": "Geleneksel İspanyol tatlılarını modern sunumlarla birleştiren, lezzetli atıştırmalıklar bulabileceğiniz şık pastane.",
    "Momento Café": "Şehrin kalabalığından uzaklaşıp anın tadını çıkarabileceğiniz, kahve ve huzur dolu bir mekan.",
    "Nubra Coffee Roasters": "Yüksek rakımlı bölgelerden gelen özel çekirdekleri kavuran, kahve severler için nitelikli bir deneyim.",
    "Salty Dog Madrid": "Denizci temasıyla dekore edilmiş, rom bazlı kokteyller ve canlı müzik sunan eğlenceli bar.",
    "Satán Cocktail Bar": "Karanlık ve gizemli dekorasyonuyla dikkat çeken, yaratıcı kokteyller ve vegan atıştırmalıklar sunan bar.",
    "Sole Mio | Specialty Coffee": "İtalyan esintileri taşıyan, Napoli şarkıları eşliğinde nitelikli kahve sunan sıcak ve samimi mekan.",
    "TastyCakes": "Özellikle red velvet pastasıyla ünlü, renkli ve lezzetli özel tasarım pastalar sunan butik fırın.",
    "Vinoteca La Cristalería": "Geniş şarap kavı ve gurme tadım etkinlikleriyle, şarap severler için tarihi bir buluşma noktası.",
    "ZAFYRO Cocktail Experience": "Disney müzikalleri temasında hazırlanan yaratıcı kokteylleri ve büyülü atmosferiyle eşsiz bir deneyim.",
    "chök - Chueca | Pastelería sin gluten Madrid": "Çikolata odaklı, glutensiz kronut ve hamur işleri sunan, tatlı krizleri için ideal mekan.",

    # MILAN (Leftover)
    "Goccetto": "İtalyan şarapları ve yanında sunulan peynir tabaklarıyla, samimi ve sıcak bir şarap barı.",
    "Grappo Lambro": "Özenle seçilmiş şaraplar, soğuk mezeler ve neşeli atmosferiyle bilinen keyifli bir enoteca.",

    # MARSEILLE
    "Address Ateliers De Pâtisserie": "Yetişkinler ve çocuklar için pasta yapım atölyeleri düzenleyen, ellerinizi una bulayabileceğiniz yaratıcı alan.",
    "Bar de L Est": "Canlı atmosferi, lezzetli atıştırmalık tabakları ve geniş içki menüsüyle popüler bir buluşma noktası.",
    "Chicoulon caviste restaurant": "Hem şarap kavı hem restoran olarak hizmet veren, mevsimsel ve yerel lezzetler sunan şık bistro.",
    "Glacier Marseille Scooter And Shop - La Mignonne": "Mevsim meyveleri ve kaliteli malzemelerle hazırlanan el yapımı dondurmalarıyla ünlü seyyar ve sabit dondurmacı.",
    "Josie café": "Tüm gün kahvaltı, özel kahveler ve taze meyve sularıyla aydınlık ve ferah bir kafe.",
    "KRM café galerie": "Sanat ve kahve tutkunlarını buluşturan, sergiler eşliğinde kahve keyfi sunan galeri kafe.",
    "Le Balagan": "Organik, glütensiz ve bitkisel bazlı sağlıklı yemekleriyle öne çıkan, sürdürülebilir mutfak anlayışına sahip restoran.",
    "Mostera Concept Store": "Tasarım ürünleri incelerken kahvenizi yudumlayabileceğiniz, yaşam tarzı ve kafe konseptini birleştiren mekan.",
    "Risette – Torréfacteur & Coffee Shop": "Kendi kavurdukları kahve çekirdekleri ve Japon matcha çeşitleriyle, kahvaltı ve öğle yemeği için ideal.",

    # MARRAKESH
    "Azalai Şehir Çarşısı": "Geleneksel Fas lezzetlerini modern dokunuşlarla yeniden yorumlayan, şık ve büyüleyici bir şehir restoranı.",
    "Bidaya Rooftop Restaurant Bar by Almaha": "Medina ve Atlas Dağları manzaralı, bohem dekorlu terasında uluslararası ve Fas yemekleri sunan restoran.",
    "Cocktail La Poterne": "Gizli bir girişin ardında, özel kokteyller ve samimi bir atmosfer sunan speakeasy tarzı bar.",
    "Coffee Houmti ️ قهوة حومتي": "Akdeniz ve Fas mutfağından lezzetler sunan, modern dekorlu ve rahat bir mahalle kafesi.",
    "FOLK MARRAKECH": "Geleneksel Fas kültürünü modern bir sunumla birleştiren, yerel lezzetler ve kültürel bir atmosfer sunan mekan.",
    "HeiBai Speciality Coffee 黑白": "Japon füzyon dekoru ve sakin atmosferiyle, dijital göçebeler ve kahve severler için huzurlu bir kafe.",
    "LE MECANO": "Endüstriyel dekorasyonu ve yaratıcı kokteylleriyle dikkat çeken, mekanik temalı özgün bir bar.",
    "La Cueva restaurant bar à tapas": "İspanyol tapasları, canlı müzik ve festivale dönüşen atmosferiyle enerjik bir restoran ve bar.",
    "La Pergola & Le bistro Arabe": "Riad Monceau'nun terasında, caz müzik eşliğinde Fas tapasları ve kokteylleri sunan yeşil çatı bahçesi.",
    "La Table Berbère": "Atlas Dağları'nın otantik atmosferini yaşatan, geleneksel Berber yemekleri ve misafirperverliği sunan sıcak mekan.",
    "Le Slimana Restaurant & Rooftop": "Geleneksel Fas gastronomisinin en iyi örneklerini panoramik şehir manzarası eşliğinde sunan çatı restoranı.",
    "Luna Glacier Marrakech": "Gece geç saatlere kadar açık, Atlas Dağları manzarası eşliğinde dondurma keyfi sunan mekan.",
    "MK ROOFTOP Marrakech - FOOD & COCKTAILS": "Koutoubia Camii manzaralı, Fransız ve Fas mutfağı sunan, şık ve kozmopolit bir çatı barı.",
    "Manso Bar": "Havuz manzaralı, caz müzik eşliğinde kokteyl ve tapas sunan, şık ve samimi bir bar.",
    "Moroccan Teahouse Restaurant - 1112 Marrakech": "Unutulmuş tariflerle hazırlanan bölgesel Fas yemekleri ve bitki çayları sunan sakin ve aydınlık restoran.",
    "Naranj Libanese": "Lübnan ve Suriye mutfağının en iyi örneklerini, güzel bir terasta sunan samimi aile işletmesi.",
    "Nola By Ari - Votre Restaurant à Marrakech": "New Orleans esintili menüsü ve canlı caz müziğiyle, Gueliz'de modern ve şık bir deneyim.",
    "Oban": "İskoç viskileri ve premium içkiler sunan, şık atmosferiyle viski severler için ideal bir bar.",
    "Petanque Social Club": "Eski bir petank salonunda, Akdeniz yemekleri ve retro dekoruyla hizmet veren gizli bahçe restoranı.",
    "Restaurant - Le 68 Bar à Vin Marrakech": "Geniş şarap kavı ve Fransız zarafetiyle, şarap severler için sofistike bir buluşma noktası.",
    "Restaurant Chez Fatima - Gastronomie marocaine et internationale - Restaurant marocain Marrakech": "Renkli ve geleneksel dekoruyla, hem Fas hem de uluslararası yemekler sunan sıcak aile restoranı.",
    "Restaurant Chouf L'Or": "Altın detaylı lüks dekorasyonu ve Fas gastronomisinin seçkin lezzetleriyle premium bir yemek deneyimi.",
    "Restaurant Granada Marrakech": "Baharat kokulari eşliğinde, geleneksel tagine ve kuskus yemekleri sunan canlı ve otantik restoran.",
    "Rooftop Restaurant El Kennaria": "Medina'nın kalbinde, geleneksel Fas yemeklerini çatı katı ferahlığında sunan keyifli bir restoran.",
    "SAVOR Coffee Shop": "Özenle seçilmiş kahve çekirdekleri ve sağlıklı atıştırmalıklarıyla, minimalist ve modern bir kahve dükkanı.",
    "Simple specialty coffee": "Medina'da, özenle hazırlanan espresso ve matcha çeşitleri sunan küçük ve sevimli bir kahve durağı.",
    "Sky Bar Wow": "Şehrin üzerinde, panoramik manzaralar eşliğinde premium kokteyller ve keyifli bir akşam sunan bar.",
    "So Lounge Marrakech": "Canlı şovlar, Asya füzyon mutfağı ve şık bahçesiyle, gece hayatının nabzını tutan trend mekan.",
    "Sweet & Sook - Glacier à L'orientale - Mouassine": "Fas'a özgü baharatlar ve meyvelerle hazırlanan artisanal dondurmalarıyla ünlü, Medina'daki tatlı durağı.",
    "Tanjia secrets": "Ağır ateşte pişen meşhur Tanjia yemeği ve samimi misafirperverliğiyle bilinen gizli lezzet noktası.",
    "Wall Marrakech": "Şehrin tarihi surları boyunca yürüyüş yaparken mola verebileceğiniz, sokak sanatı temalı modern bar."
}

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    total_updated = 0
    print(f"Applying updates to {len(json_files)} city files...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            file_changed = False
            
            for place in highlights:
                name = place.get('name', '').strip()
                
                # Check exact name match first
                if name in UPDATES:
                    place['description'] = UPDATES[name]
                    file_changed = True
                    total_updated += 1
                
            if file_changed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Saved updates to {city_name}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nTotal Turkish descriptions updated: {total_updated}")

if __name__ == "__main__":
    main()
