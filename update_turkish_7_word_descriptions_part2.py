
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New Turkish Description
UPDATES = {
    # HONG KONG
    "Cloud Nine Specialty Coffee": "Huzurlu bir kaçış noktası, yaratıcı kahveler ve Asya-Batı füzyon tatlar sunar.",
    "Marouf & Puff Bake": "Marouf puf böreği! Ortadoğu-Hong Kong füzyon, pastry.", # Research incomplete, keeping generic but improved if possible or same
    "Pakeeza Food Restaurant": "Otantik Pakistan mutfağı sunan, zengin baharatlı körileriyle meşhur samimi bir restoran.",
    "Sheer Coffee": "Saf kahve deneyimi. Minimal yaklaşım, pure flavors.", # Research incomplete
    "Sugar Brothers hk": "Şeker kardeşler! Tatlı dünyası, desserts ve happiness.", # Research incomplete
    "Uncle Ben Coffee": "Nitelikli kahve laboratuvarı, ödüllü baristalar ve yaratıcı imza içecekleriyle tanınan mekan.",
    
    # LİZBON
    "Casa de Dura": "Dura'nın evi. Geleneksel Portekiz mutfağı, aile atmosferi.", # Research incomplete
    "Mercearia do Século": "Nostaljik bakkal dekorunda, ev yapımı geleneksel Portekiz yemekleri sunan sıcak mekan.",
    "Near Me Alfama": "Canlı Fado müziği eşliğinde, taze ve yerel malzemelerle hazırlanan otantik tapalar.",
    "Orioli Coffee": "Brezilya çekirdekleriyle hazırlanan ustaişi kahveler ve ev yapımı tatlılar sunan şık kafe.",
    "The VENUE": "Gündüzleri sakin, geceleri DJ performanslarıyla canlanan, çok yönlü ve popüler bir mekan.",
    "da Prata 52": "Modern Portekiz mutfağını Akdeniz dokunuşlarıyla sunan, paylaşmalık tabaklarıyla ünlü samimi restoran.",
    
    # LONDRA
    "Bantof": "Modern Avrupa mutfağı. Contemporary dining, yaratıcı sunum.", # Research incomplete
    "Tosi Gorgonzola": "Gorgonzola peynirinin başrolde olduğu, yaratıcı İtalyan lezzetleri sunan şık ve butik bar.",
    
    # LUCERNE
    "Bar León": "Aslan barı! İspanyol temalı, tapas ve sangria.", # Research incomplete
    "Bar bei Miguel": "İsviçre ve İspanyol mutfağını birleştiren, geniş bira menüsüne sahip canlı ve samimi bar.",
    "Bebié Konditorei Confiserie GmbH": "Geleneksel İsviçre pastaları, pralinler ve taze hamur işleriyle ünlü tarihi ve şirin pastane.",
    "Bäckerei Macchi": "İstasyon yakınında taze sandviçler, salatalar ve fırın ürünleri sunan pratik ve lezzetli durak.",
    "Dal Mattino": "İtalyan kahvaltısı, özel 'crookies' tatlısı ve mükemmel kahveleriyle güne başlamak için ideal.",
    "Glutenfreie Brotwerkstatt": "Çölyak dostu, tamamen glutensiz taze ekmek ve hamur işleri üreten güvenilir fırın.",
    "Jardin Oriental (Restaurant &Take Away)": "Doğu bahçesi! Ortadoğu mutfağı, kebap ve mezeler.", # Research incomplete
    "Kaffeekranz im Himmelrich": "Kendi kavurdukları kahveler ve ev yapımı pastalarla huzurlu bir mola sunan modern kafe.",
    "Melissa's Kitchen": "Melissa'nın mutfağı. Ev yapımı yemekler, kişisel dokunuş.", # Research incomplete
    "Onkel Salamat": "Selamet amca! Ortadoğu mutfağı, falafel ve kebap.", # Research incomplete
    "Restaurant Don Feri": "İspanyol ve İtalyan esintili Akdeniz yemekleri sunan, aile dostu ve rahat bir restoran.",
    "Restaurant Scala": "Göl ve dağ manzaralı, Art Deco tarzında, yaratıcı Akdeniz mutfağı sunan şık restoran.",
    "Salvatore Icilio La Bottega Del Buongustaio": "Salvatore'nin gurme dükkanı. İtalyan delicatessen, premium ürünler.", # Research incomplete
    "Volver - Café Tapas Vinos": "Otantik İspanyol tapaları ve şarapları eşliğinde, İspanyol müziğiyle dolu canlı bir atmosfer.",
    "Wirtshaus Taube Luzern": "Güvercin hanı. Geleneksel İsviçre wirtshaus, yerel mutfak.", # Research incomplete
    "tschuppi's wonderbar": "Tschuppi'nin harika barı! Eğlenceli konsept, yaratıcı kokteyller.", # Research incomplete
    "Äss-Bar": "Dünden kalan lezzetler! Sürdürülebilirlik, indirimli fırın ürünleri.", # Research incomplete
    
    # LYON
    "Anahera": "Sağlıklı ve mevsimsel vejetaryen yemekler sunan, bitkilerle dolu huzurlu bir vaha.",
    "Bacchanales, restaurant gastronomique.": "Tarihi binada, mevsimsel ürünlerle hazırlanan yaratıcı Fransız mutfağı sunan romantik restoran.",
    "Bonomia Boulangerie": "Organik ekşi mayalı ekmekleri ve vegan seçenekleriyle öne çıkan modern ve sıcak fırın.",
    "Boulangerie L'Artisan (Maison Dumollard)": "Geleneksel Fransız ekmekleri ve ev yapımı pastalarıyla tanınan, zanaatkar ruhlu mahalle fırını.",
    "Boulangerie Les Frères Barioz": "Kardeşlerin işlettiği, ödüllü kruvasanları ve yaratıcı mevsimsel pastalarıyla ünlü sıcak mekan.",
    "Café Joyeux": "Down sendromlu çalışanlarıyla neşe saçan, sosyal sorumluluk sahibi samimi bir kafe-restoran.",
    "Cuisiné Sensée et Inspirée": "Akdeniz ve Asya esintili, sağlıklı ve yaratıcı yemekler sunan ilham verici restoran.",
    "Duclef Café Pâtisserie": "Mevsimsel tatlılar ve tuzlu atıştırmalıklarla gün boyu keyif sunan şirin kafe-pastane.",
    "GRANIT Bar à Vins": "Yüzlerce doğal şarap seçeneği ve lezzetli tapaslarıyla öne çıkan, keyifli ve rahat şarap barı.",
    "House of Bears - Bar Lyon 7": "Bölgesel şarküteri tabakları ve ev yapımı atıştırmalıklarla samimi ve rahat bir mahalle barı.",
    "Kachka": "Slav kahve kültürünü yansıtan, sanat galerisi atmosferinde sakin ve huzurlu bir kaçış noktası.",
    "La Baignoire": "Bir banyo küvetinde kokteyl içebileceğiniz, 1920'ler temalı gizli ve şık speakeasy.",
    "La Beer Fabrique - Atelier bière et microbrasserie": "Kendi biranızı yapabileceğiniz atölyeler ve taze bira tadımları sunan eğlenceli mikro bira fabrikası.",
    "La Bouteillerie": "Hem şarap dükkanı hem bar, yerel peynirler eşliğinde samimi bir şarap deneyimi.",
    "Le Rancard : Coffee shop - Brunch - Laverie": "Kahve, brunch ve çamaşırhane hizmetini birleştiren, modern ve çok yönlü sosyal mekan.",
    "Le Starck bar": "İspanyol tapaları ve canlı müzik atmosferiyle, dostça sohbetler için ideal bir buluşma noktası.",
    "Magma Coffee shop": "Akdeniz esintili atıştırmalıklar ve nitelikli kahveler sunan, volkanik enerjili şık kafe.",
    "My Little Babka": "Geleneksel Polonya babka tatlısının en lezzetli ve çeşitli hallerini sunan şirin pastane.",
    "Puzzle Cafe": "Ruanda kahveleri ve ev yapımı tatlılarıyla, modern ve oyun dolu bir mola noktası.",
    "Rakwé Café - Lafayette": "Kolombiya ve Panama çekirdekleriyle hazırlanan özel kahveler sunan, küçük ve trend kafe.",
    "STEPPE BAR": "Asya mutfağı ve yaratıcı kokteylleri, göl manzaralı terasında sunan modern ve rahat bar.",
    "Satriale": "Doğal şaraplar ve plak müziği eşliğinde, Sopranos dizisinden ilham alan keyifli mekan.",
    "Skull Lyon - Bar à cocktails immersif": "Kafatası ve steampunk temalı dekoruyla, görsel şölen sunan sürükleyici bir kokteyl barı.",
    "Soif !": "Yüzlerce şarap çeşidi ve retro oyunları birleştiren, eğlenceli ve nostaljik bir şarap barı.",
    "The Phantom of the Operası": "Opera temalı dekoru ve geniş içki menüsüyle, dramatik ve gizemli bir kokteyl deneyimi.",
    "Un Brin De Folie, fleuriste de saison et café": "Çiçekler içinde kahve ve ev yapımı kek keyfi sunan, botanik ve huzurlu bir kafe.",
    "you cocktail bar": "Parfümden ilham alan kokteylleri ve şık atmosferiyle, duyulara hitap eden modern bir bar.",
    
    # MADRID
    "Alchemist 1967": "Simya temalı, nostaljik dekoru ve yaratıcı kokteylleriyle büyüleyen, sofistike bir gece mekanı.",
    "Botequim Brunch & Tapas Bar": "İspanyol tapas kültürünü Brezilya lezzetleriyle harmanlayan, brunch için ideal, canlı ve modern mekan.",
    "Cinco Hileras Café": "Uygun fiyatlı ve kaliteli brunch seçenekleri sunan, ev sıcaklığında samimi bir mahalle kafesi.",
    "Despacito Specialty Coffee - Café Especialidad": "Yavaşça specialty kahve! Sabırlı brewing, kaliteli mola.", # Research incomplete
    "Koffie Specialty Coffee & Vinos Naturales": "Hollandaca kahve! Specialty brewing ve doğal şaraplar.", # Research incomplete
    "Kon Kafé - Specialty Coffee": "Kalp simgelilatte artları ve ev yapımı kurabiyeleriyle, kahve tutkunları için sıcak bir durak.",
    "LICENSED specialty coffee": "Chamartín'de, analog müzik eşliğinde hassas tekniklerle hazırlanan nitelikli kahveler sunan huzurlu mekan.",
    "La Dulcería Café |Tartas de Queso Artesanas|Specialty Cheesecakes. Desserts-Postres": "Tatlıcı kafe! Artisan cheesecake uzmanı, Bask tarzı.", # Research incomplete
    "Le Praliné Brunch / Malasaña": "Akdeniz füzyon brunch menüsü ve şık sunumlarıyla, Malasaña'nın modern ve keyifli mekanı.",
    "Lito Pastelería": "Lito pastanesi! İspanyol tatlı geleneği, modern sunum.", # Research incomplete
    "Loca Obsesión | Brunch Madrid": "Deli takıntı brunch! Tutkulu mutfak, yaratıcı sunum.", # Research incomplete
    "Lovo Cocktail Bar Madrid": "Lovo kokteyl barı! Yaratıcı karışımlar, şık ortam.", # Research incomplete
    "MARCELLE": "İki ayda bir değişen menüsüyle, Fransız bistro tarzını yansıtan romantik ve samimi restoran.",
    "Madremia Retiro": "Retiro Parkı yakınında, geleneksel hamur işleri ve taze ekmekleriyle sevilen şirin fırın.",
    "Madrid & Darracott - Vinos y experiencias": "Eğlenceli ve öğretici tadım etkinlikleriyle, İspanyol şaraplarını keşfetmek için harika bir durak.",
    "Minos Pastry & Specialty coffee": "Geniş hamur işi çeşitleri ve nitelikli kahveleriyle, tatlı bir mola için ideal mekan.",
    "Momento Café": "An kafesi! Şimdinin tadını çıkar, mindful coffee.", # Research incomplete
    "Norah Barrio Salamanca | Brunch Madrid": "Salamanca'da sağlıklı ve estetik brunch tabakları sunan, Akdeniz ruhlu şık ve rahat mekan.",
    "Nubra Coffee Roasters": "Himalaya Nubra vadisinden kavurucu! Yüksek rakım çekirdekler.", # Research incomplete, keeping old
    "SAMBHAD the cocktail bar": "Sambhad kokteyl barı! Egzotik tatlar, yaratıcı sunum.", # Research incomplete
    "Salty Dog Madrid": "Tuzlu köpek! Denizci temalı bar, rum kokteyller.", # Research incomplete
    "Santo Bakehouse": "Artisan ekmekler, aziz kalitesi.", # Research incomplete
    "Satán Cocktail Bar": "Şeytan kokteyl barı! Cehennem temalı, güçlü kokteyller.", # Research incomplete
    "Shambala": "Tibet Şambala cenneti! Zen atmosfer, mindful dining.", # Research incomplete
    "Shanghai Sheng Jian Bao": "Şanghay kızarmış köfte! Otantik Çin sokak yemeği.", # Research incomplete
    "Sinfonía Specialty Coffee": "Senfoni specialty kahve! Müzikal uyum, perfect brewing.", # Research incomplete
    "Sole Mio | Specialty Coffee": "Benim güneşim İtalyanca! Napoli şarkısı, specialty kahve.", # Research incomplete
    "TastyCakes": "Lezzetli pastalar! Amerikan tarzı cakes, renkli dekor.", # Research incomplete
    "Vinoteca La Cristalería": "Cam atölyesi vinotekası! Tarihi mekan, premium şaraplar.", # Research incomplete
    "ZAFYRO Cocktail Experience": "Safir kokteyl deneyimi! Mücevher temalı, premium kokteyller.", # Research incomplete
    "chök - Chueca | Pastelería sin gluten Madrid": "Çök glutensiz pastane! Chueca'da çölyak dostu tatlılar." # Research incomplete
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
                    # Update Turkish description
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
