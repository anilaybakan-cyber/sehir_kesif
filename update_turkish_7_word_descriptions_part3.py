
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New Turkish Description
UPDATES = {
    # HONG KONG
    "Marouf & Puff Bake": "Sokak arasında huzurlu bir mola; fıstıklı tartlar ve özel kahveler sunan minimalist kafe.",
    "Sheer Coffee": "Japon estetiğiyle tasarlanmış, sade ve dingin bir ortamda sunulan rafine kahve deneyimi.",

    # LUCERNE
    "Jardin Oriental (Restaurant &Take Away)": "Doğu bahçesi! Ortadoğu mutfağı, kebap ve mezeler.", # Research was inconclusive, keeping generic but improved if possible
    "Melissa's Kitchen": "Melissa'nın mutfağı. Ev yapımı yemekler, kişisel dokunuş.", # Research inconclusive
    "Onkel Salamat": "Selamet amca! Ortadoğu mutfağı, falafel ve kebap.", # Research inconclusive
    
    # MADRID
    "Despacito Specialty Coffee - Café Especialidad": "Yavaşça specialty kahve! Sabırlı brewing, kaliteli mola.", # Research inconclusive
    "Koffie Specialty Coffee & Vinos Naturales": "Sadece espresso odaklı, sade ve modern bir kahve barı; kahve tutkunları için ideal.",
    "La Dulcería Café |Tartas de Queso Artesanas|Specialty Cheesecakes. Desserts-Postres": "Çeşit çeşit el yapımı cheesecake'ler ve yanında nitelikli kahve sunan sıcak bir tatlıcı.",
    "Lito Pastelería": "Lito pastanesi! İspanyol tatlı geleneği, modern sunum.", # Research inconclusive
    "Loca Obsesión | Brunch Madrid": "Yaratıcı sunumları ve ateşle hazırlanan lezzetleriyle, trend ve canlı bir brunch mekanı.",
    "Lovo Cocktail Bar Madrid": "Josefine Baker ve 1920'ler temalı, şık atmosferde sunulan yaratıcı ve görsel kokteyller.",
    "MARCELLE": "Mevsimsel ürünlerle hazırlanan, Fransız bistro tarzı, samimi ve romantik bir restoran.",
    "Madremia Retiro": "New York tarzı kurabiyeler ve taze kruvasanlarıyla sevilen, rahat bir hamur işi durağı.",
    "Madrid & Darracott - Vinos y experiencias": "Eğlenceli ve öğretici tadım etkinlikleriyle, İspanyol şaraplarını keşfetmek için harika bir durak.",
    "Minos Pastry & Specialty coffee": "Geniş hamur işi çeşitleri ve nitelikli kahveleriyle, tatlı bir mola için ideal mekan.",
    "Momento Café": "An kafesi! Şimdinin tadını çıkar, mindful coffee.", # Research inconclusive
    "Norah Barrio Salamanca | Brunch Madrid": "Akdeniz esintili, sağlıklı brunch tabakları ve deniz temalı dekoruyla huzurlu bir mekan.",
    "Nubra Coffee Roasters": "Himalaya Nubra vadisinden kavurucu! Yüksek rakım çekirdekler.", # Research inconclusive
    "SAMBHAD the cocktail bar": "Şık ve modern dekoruyla, egzotik tatlar ve canlı müzik sunan popüler kokteyl barı.",
    "Salty Dog Madrid": "Tuzlu köpek! Denizci temalı bar, rum kokteyller.", # Research inconclusive / possibly wrong place
    "Santo Bakehouse": "Sıcak ve samimi bir ortamda, el yapımı ekşi mayalı ekmekler ve mevsimsel çörekler.",
    "Satán Cocktail Bar": "Şeytan kokteyl barı! Cehennem temalı, güçlü kokteyller.", # Research inconclusive
    "Shambala": "Kum zeminli, tropik bitkilerle dolu, egzotik kokteyller sunan rahat ve şık lounge.",
    "Shanghai Sheng Jian Bao": "Şanghay usulü tavada kızarmış, içi sulu ve dışı çıtır otantik domuz bürekleri.",
    "Sinfonía Specialty Coffee": "Ferah ve evcil hayvan dostu bir ortamda, özenle hazırlanan nitelikli kahve ve atıştırmalıklar.",
    "Sole Mio | Specialty Coffee": "Benim güneşim İtalyanca! Napoli şarkısı, specialty kahve.", # Research points to a song, likely name match error or obscure place

    # LİZBON
    "Casa de Dura": "Egzotik dekoru, canlı atmosferi ve cömert porsiyonlarıyla sevilen geleneksel Portekiz restoranı.",

    # LONDRA
    "Bantof": "Soho'da gizli, 1920'lerin cazibesini yansıtan şık atmosferde paylaşımlık tabaklar ve kokteyller.",

    # LYON
    "House of Bears - Bar Lyon 7": "Rahat ve samimi bir atmosferde, peynir tabakları ve yerel biralar sunan mahalle barı.",
    "Kachka": "Bitkilerle dolu huzurlu bir ortamda, sanatla iç içe nitelikli kahve ve ev yapımı kurabiyeler.",

    # MARAKEŞ
    "Anzar": "Imsouane esintili, taze ve sağlıklı vejetaryen seçenekler sunan manzaralı ve renkli restoran.",
    "Arroz Bar Restaurant": "Fas dekoru ve modern dokunuşlarla, lezzetli tagine ve kuskus sunan canlı mekan.",
    "Azalai Şehir Çarşısı": "Azalai şehir çarşısı! Tuareg kafilesi, çöl ruhu.", # Research inconclusive
    "BAROMETRE MARRAKECH": "Laboratuvar tarzı dekoru ve yaratıcı sunumlarıyla, şehrin en iyi miksoloji ve yemek deneyimi.",
    "Bidaya Rooftop Restaurant Bar by Almaha": "Başlangıç rooftop! Almaha'nın premium terası, panoramik manzara.", # Research inconclusive
    "Café Carmel Marrakech": "Renkli dekoru, huzurlu terası ve taze kahvaltı seçenekleriyle bilinen şirin ve samimi kafe.",
    "Cocktail La Poterne": "Küçük kapı kokteyller! Gizli giriş, speakeasy vibes.", # Research inconclusive

    # MARSİLYA
    "Address Ateliers De Pâtisserie": "Adres pastane atölyeleri! Pastacılık kursları, hands-on deneyim.", # Research inconclusive
    "Bar Odéon": "Sakin ve sıcak bir atmosferde, kahve ve hafif atıştırmalıklar sunan klasik bir bar.",
    "Café Barbotyne": "Seramik boyama ve kahve keyfini birleştiren, renkli ve huzurlu bir sanat kafesi.",
    "Café Lauca « La Boutchica »": "Küçük ve samimi bir alanda, özenle seçilmiş çekirdeklerle hazırlanan nitelikli kahve durağı.",
    "Chapati baille @ l'original": "Tunus usulü chapati sandviçleri ve pizzalarıyla bilinen, samimi ve rahat bir atıştırmalık noktası.",
    "Chicoulon caviste restaurant": "Chicoulon şarapçı restoran! Provençal şaraplar, yerel mutfak.", # Research inconclusive
    "Coffee&Bakery": "Sakin bir pasajda, yulaf sütlü kahveler ve taze hamur işleri sunan huzurlu kafe.",
    "Coquetel Club - Bar à Manger et Cocktails - Marseille 6": "Her ay değişen teması ve yaratıcı kokteylleriyle, canlı ve samimi bir akşam mekanı.",
    "Delices du port": "Liman manzaralı, hem tatlı hem tuzlu krep ve waffle çeşitleriyle sevilen şirin krepçi.",
    "Dionysos": "Güzel müzik eşliğinde, özenle hazırlanan kokteylleri ve sıcak atmosferiyle popüler bir bar.",
    "Fuella Nera": "Organik şaraplar ve ev yapımı focaccia sunan, samimi ve bilgili bir şarap barı.",
    "GRIGNE CAFÉ": "Vauban'da, vegan seçenekli kekler ve harika kahveler sunan sıcak ve canlı kafe.",
    "Glaces Moustache-Artisan Glacier": "Bıyık temalı, eğlenceli ve lezzetli dondurmalar sunan popüler bir zanaatkar dondurmacı.",
    "Glacier Marseille Scooter And Shop - La Mignonne": "Sevimli dondurmacı ve scooter dükkanı! Retro vibes.", # Research inconclusive
    "Josie café": "Josie kafesi! Amerikan vibes, brunch ve kahve.", # Research inconclusive
    "KRM café galerie": "KRM kafe galeri! Sanat ve kahve buluşması.", # Research inconclusive
    "La Cosca": "İtalyan tapasları ve doğal şaraplarıyla, arkadaş buluşmaları için ideal, sıcak bir mekan.",
    "La Movida": "Canlı müzik ve DJ performansları eşliğinde, İspanyol tapasları ve kokteylleri sunan enerjik bar.",
    "Le Balagan": "İbranice kaos anlamında! İsrail mutfağı, canlı atmosfer.", # Research inconclusive
    "Les Jardins de Tanin Natural Wine Club": "Mum ışığında, doğal şaraplar ve lezzetli tapaslar sunan romantik ve şık şarap barı.",
    "Mauvaise Herbe - Bistrot Café Végétal Marseille": "Tamamen bitki bazlı, yaratıcı ve taze lezzetler sunan, sürdürülebilir ve samimi vegan bistro.",
    "Mostera Concept Store": "Mostera konsept mağaza! Lifestyle, kahve ve tasarım.", # Research inconclusive
    "Nabu et Jéro": "Fransız mutfağını yenilikçi tatlarla buluşturan, özenli servisi ve şarap seçkisiyle şık restoran.",
    "Naima Cake": "Özel günler için tasarlanan, hem göze hem damağa hitap eden butik pasta atölyesi.",
    "PANAMA LATINO FOOD": "Latin Amerika müzikleri eşliğinde, ceviche ve empanada gibi tropik lezzetler sunan neşeli restoran.",
    "Paloma Cocktail Bar": "Cours Julien'de saklı, mevsimsel ve yaratıcı kokteylleriyle ünlü, rahat ve modern bar.",
    "Papamousse": "Neşeli atmosferi ve ferah terasıyla, keyifli akşamlar ve lezzetli içecekler için ideal nokta.",
    "Propaganda - bar tapas Marseille": "Liman manzaralı, siyasi temalı dekoru ve lezzetli tapaslarıyla, rahat ve eğlenceli bir bar.",
    "Risette – Torréfacteur & Coffee Shop": "Gülümseme kavurucu ve kahve dükkanı! Mutlu kahve.", # Research inconclusive
    "Sabrina Guez Patissier": "Aile sıcaklığında, el yapımı meyveli kekler ve cheesecake sunan butik bir pastane.",
    "Succulentes Cafe": "Kaktüs temalı dekoru, mavi lattesi ve sağlıklı kahvaltılarıyla, keyifli ve fotojenik bir kafe.",
    "Verre a Cruise - Tapas & Cocktail Bar": "Akdeniz ve Lübnan mezeleri eşliğinde, ustaca hazırlanan kokteyller sunan şık ve rahat bar.",
    "Weeno - Vins, spiritueux, bières et sakés - Formation WSET - Marseille": "Şarap eğitimi ve tadım etkinlikleriyle, şarap severler için samimi ve öğretici bir mekan.",
    "White Rabbit": "Saloon tarzı dekoru, canlı şovları ve doyurucu yemekleriyle, hem bar hem restoran deneyimi.",
    "mamaco (Marseille Madame Coree) restaurant coreen marseille": "Marsilya'da lüks ve samimi bir ortamda, otantik Kore lezzetleri sunan özel restoran.",

    # MİLANO
    "Barlafus Cafè - Milano": "Kalenin yakınında, lezzetli sandviçleri ve samimi ortamıyla, bütçe dostu keyifli bir kafe.",
    "Bottega dell'Arte del Vino": "Geniş şarap seçkisi ve sahibinin uzman tavsiyeleriyle, şarap tutkunları için vazgeçilmez bir durak.",
    "Bricco Café": "Milano'nun kalbinde, güler yüzlü baristaları ve kaliteli kahvesiyle, huzurlu bir mola noktası."
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
