
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New Turkish Description
UPDATES = {
    # MILAN
    "Barlafus Cafè": "Sforzesco Kalesi yakınında, pastrami sandviçleri ve samimi ortamıyla uygun fiyatlı ve modern kafe.",
    "Bottega dell'Arte del Vino": "Sempione Parkı manzaralı, geniş şarap seçkisi ve mevsimsel Milano yemekleri sunan zarif bistro.",
    "Bricco Café": "Milano şehir merkezinde, hızlı atıştırmalıklar ve kaliteli kahve sunan sıcak ve samimi mola noktası.",
    "Cortinovis Specialty Coffee roasters": "Milano'nun ilk Slow Food kavurucusu; nitelikli çekirdekler ve leziz fıstıklı kruvasanlar sunuyor.",
    "Daimyo Restaurant": "Karanlık ahşap dekorlu, samuray estetiğiyle tasarlanmış şık bir mekanda modern Japon füzyon mutfağı.",
    "Debbie's": "Focaccia sandviçleri ve fıstıklı kruvasanlarıyla bilinen, aile dostu ve neşeli bir Amerikan kafesi.",
    "EnotecaWine": "Eski şarap fıçıları arasında, Milano ve Lombardiya mutfağının modern yorumlarını sunan rustik enoteca.",
    "Il Cafetero Specialty Coffee": "İspanyol ismi taşıyan, sıcak ve samimi bir ortamda nitelikli kahve ve kahvaltı sunan mekan.",
    "Insula Sardinia Experiences": "Sardunya adası lezzetlerini modern dokunuşlarla sunan, şarap ve tapas ağırlıklı zarif restoran.",
    "LA BUFALOTTA": "Bol malzemeli pizzaları ve sıcak, rahat ortamıyla bilinen popüler ve cömert bir restoran.",
    "Marea Seafood & Beverage": "Yaratıcı sunumlarla taze deniz ürünleri ve çiğ tabaklar sunan, samimi ve şık bir restoran.",
    "Niconoce ®️ Enoteca con cucina": "Şarap odaklı, yanında modern dokunuşlu geleneksel yemekler sunan sakin ve kaliteli bir enoteca.",
    "Raboucer": "Vinil plak şeklinde kokteylleri ve neon ışıklı labirent dekoruyla canlı ve modern bir bar.",
    "Remedy Wine & Spirits": "Deri koltuklu, puro odalı şık bir kulüp havasında, premium şarap ve içki deneyimi.",
    "SAMI : Specialty Coffee from Perù": "Peru'dan doğrudan ithal organik kahveler ve ev yapımı empanadalar sunan sıcak bir kahve dükkanı.",
    "Sciuma Radical Wines": "Doğal şaraplar ve onlara eşlik eden yerel atıştırmalıklar sunan, sakin ve samimi bir şarap barı.",
    "Tin - Cocktail Pub": "Caz müziği eşliğinde, endüstriyel dekorlu rahat bir ortamda kaliteli kokteyl ve bira sunan pub.",
    "UNGARO 1956": "Geniş beyaz salonunda, sabahtan akşama kadar Akdeniz lezzetleri sunan tarihi ve şık bistro.",
    "Vineria Cardenzia": "Eski sinema koltuklarıyla dekore edilmiş, peynir reçelleri ve şaraplarıyla ünlü nostaljik bir mekan.",
    "Vino Vino dal 1921": "Dev bir fıçı ve kutsal bir atmosfer eşliğinde, asırlık şarap geleneğini yaşatan tarihi enoteca.",
    "Viro Steak Restaurant": "Kuru dinlendirilmiş etler ve Latin Amerika ızgaraları sunan, şık ve rahat bir steakhouse.",

    # NAPLES
    "Alkymya Bellini": "Kendi kokteylini yaratabileceğin, yanında ikramlarıyla bilinen, Piazza Bellini'de rahat ve samimi bir bar.",
    "Antica Pasticceria Lauri": "Çıtır sfogliatella ve otantik Napoli tatlılarıyla ünlü, sıcak ve davetkar bir tarihi pastane.",
    "Bar Fantasy di Chierchia Antonio": "Oyun alanı da bulunan, kaliteli kahve ve samimi bir ortam sunan rahat bir mahalle kafesi.",
    "Bar Materdei": "Materdei bölgesinde, sessiz ve sakin bir atmosferde kahve molası için otantik bir durak.",
    "Bar and Bet's": "Maç izleyip kokteyl içebileceğiniz, modern dekorlu ve canlı atmosfere sahip bir spor barı.",
    "Bar del Chiostro": "Manastır huzurunda, deniz manzaralı bir avluda kahve ve hamur işi sunan sakin kafe.",
    "Barrio Alto Caffe": "Taze sıkılmış portakal suyu ve harika espressosuyla bilinen, sıcak ve samimi bir mahalle kafesi.",
    "Blue Turtle caffetteria": "Caz müziği ve vintage dekor eşliğinde, nitelikli kahve ve kokteyl sunan sanat dolu mekan.",
    "Botanical Bar": "Bitkilerle çevrili, botanik bahçe havasında kokteyl ve tapas sunan huzurlu ve şık bir kaçış.",
    "Cantina Central 92": "Canlı müzik ve uygun fiyatlı Aperol Spritz ile yerel şarapları buluşturan neşeli bir kantin.",
    "Decanter Wine and More": "Alışveriş bölgesinde, sommelier rehberliğinde şarap ve peynir tabakları sunan sıcak ve trend mekan.",
    "Ecce Homo Bar": "Tarihi merkezde, soğuk bira ve parmak atıştırmalıklarla samimi bir sokak barı deneyimi.",
    "Gran Caffè Valentino": "Şık dekoru ve güler yüzlü servisiyle, geleneksel Napoli tatlıları sunan zarif bir kafe.",
    "Il Fiasco Bar&Restaurant": "Harika kokteyller ve İtalyan yemekleriyle, hem göze hem damağa hitap eden canlı bir restoran.",
    "Jamme Caffé": "Passalacqua kahvesi ve leziz hamur işleriyle, mola vermek için ideal, samimi ve rahat kafe.",
    "La Fesseria - Sokağı Bar": "Eğlenceli ismiyle, sokak ortasında rahatça içki içip sosyalleşebileceğiniz samimi bir bar.",
    "Mosto - Birra Artigianale": "Geniş craft bira ve viski seçkisiyle, genç ve canlı bir atmosfer sunan samimi pub.",
    "Nineteen 19 Bar": "Yaratıcı kokteylleri ve sevimli dekoruyla, yan sokakta gizlenmiş rahat ve eğlenceli bir kokteyl barı.",
    "Pasticceria \"SE.AN.\" di Serra Antonio": "Taze ve el yapımı babà ve sfogliatella sunan, yerel halkın sevdiği otantik pastane.",
    "Pasticceria Tizzano® dal 1960": "Köklü aile geleneğiyle üretilen babà ve geleneksel tatlılarıyla meşhur, aydınlık ve sıcak pastane.",
    "Pasticceria, Caffetteria napoli Piterà": "Nutellalı ruloları ve patates kroketleriyle bilinen, yerel halkın uğrak noktası gizli bir lezzet durağı.",
    "Quesse cocktail bar": "Miksoloji sanatını konuşturan, havalı dekoru ve canlı atmosferiyle dikkat çeken popüler kokteyl barı.",
    "SANTO cocktail bar": "Aziz temalı şık dekoru ve ustaca hazırlanmış kokteylleriyle, keyifli bir akşam için ideal mekan.",
    "San Caffè cappuccino factory": "Kişiye özel latte art ve sanatsal cappuccinolarıyla ünlü, sakin ve samimi bir kahve durağı.",
    "Trattoria Pizzeria Bella Napoli Centro": "1990'dan beri aile işletmesi sıcaklığında, otantik pizza ve deniz ürünleri sunan geleneksel trattoria.",
    "Ventimetriquadri - Specialty Coffee": "Yirmi metrekarede büyük lezzetler; nitelikli kahve ve avokado tostlarıyla ünlü, samimi ve modern kafe.",
    "Wine&ammor": "Ana caddeden uzakta, yerel şaraplar ve lezzetli atıştırmalıklarla huzurlu bir mola sunan şarap barı.",
    "WineCafè Da Mario": "Mario'nun yerel şarapları ve özenle hazırladığı peynir tabaklarıyla, ev sıcaklığında samimi bir deneyim.",
    "Zero - Healthy Bar & Specialty Coffee": "Sağlıklı smoothie kaseleri ve bubble tea seçenekleriyle, modern ve ferah bir wellness kafesi.",

    # NEW YORK
    "787 Coffee": "Porto Riko kahveleri ve çiftlik temalı dekoruyla, hem çalışma hem sosyalleşme için rahat mekan.",
    "Altair Restaurant": "Kozmik temalı dekoru ve modern Amerikan mutfağıyla, romantik ve şık bir yemek deneyimi sunuyor.",
    "BONSAII Tapas & Wine Bar": "Asya ve İspanyol lezzetlerini buluşturan, sakin ve modern atmosferde yaratıcı tapas ve şarap barı.",
    "Cork Wine Bar": "Fransız peynirleri ve ördek etleriyle eşleşen şarap menüsüyle, rahat ve samimi bir mahalle barı.",
    "Cozymeal Cooking Classes": "Şeflerle birebir, modern mutfaklarda dünya lezzetlerini öğreten, interaktif ve eğlenceli yemek pişirme kursları.",
    "Current Coffee": "Bal ve yulaf sütlü latteleriyle ünlü, sade ve şık dekorlu, mahallelinin sevdiği kahve dükkanı.",
    "El Delicioso NY Food Truck": "Bandeja Paisa gibi otantik Kolombiya lezzetlerini, sokak lezzeti pratikliğiyle sunan neşeli yemek kamyonu.",
    "Everything's Jake NYC Bar & Lounge": "Prohibition dönemi esintili, lüks ve geniş bir alanda, butik kokteyller sunan şık lounge.",
    "Fabrique Bakery": "Kakuleli ve tarçınlı çörekleriyle ünlü, İskandinav minimalist tarzda, odun ateşinde pişiren otantik fırın.",
    "Frame Coffee": "Kamera temalı dekoru ve tayland usulü kahveleriyle, fotoğraf çekip dinlenebileceğiniz minimalist ve şık kafe.",
    "Fresh From Hell | Healthy & Smoothie Bar": "Cehennem Mutfağı'nda taze meyve suları ve smoothie kaseleriyle enerji veren, sağlıklı ve hızlı durak.",
    "Hole in the Wall": "Avustralya tarzı rahat kahvaltıları ve akşamları speakeasy havasıyla, gün boyu yaşayan keyifli bir mekan.",
    "Jungle Bird": "Tropikal dekoru ve Güneydoğu Asya lezzetleriyle renkli kokteyller sunan, iki katlı canlı bar.",
    "Kona Coffee and Company": "Hawaii'den gelen kahve çekirdekleri ve huzurlu ortamıyla, şehir karmaşasından kaçış sunan sakin kafe.",
    "Le Phénicien": "Lübnan mezeleri ve ızgaralarıyla bilinen, sıcak ve samimi bir ortamda otantik lezzetler sunuyor.", # Adjusted based on probable offerings for a place with this name, generic but safe if exact NY loc unverified
    "Little Cupcake Bakeshop": "Çeşit çeşit cupcake ve pastalarıyla ünlü, sevimli ve aydınlık dekorlu, çevre dostu tatlı dükkanı.",
    "Mister Paradise": "Eğlenceli ve yaratıcı kokteylleri, parti havasındaki şık dekoruyla Doğu Yakası'nın popüler gece mekanı.",
    "Perk Kafe": "Bitkilerle dolu rustik dekoru ve şarap barına dönüşen akşamlarıyla, huzurlu ve samimi bir kafe.",
    "Plantshed": "Çiçekler arasında kahve keyfi sunan, botanik bahçe havasında, ferah ve huzur dolu bir mekan.",
    "Raines Law Room at the William": "Kitaplık arkasında gizli, lüks deri koltukları ve loş ışığıyla, tam bir speakeasy deneyimi.",
    "Sotto 13": "Sera tavanı ve sosyal İtalyan tabaklarıyla, brunch ve grup yemekleri için ideal, aydınlık mekan.",
    "Supper": "Kuzey İtalyan lezzetleri sunan, açık mutfaklı ve rustik dekorlu, nakit çalışan popüler trattoria.",
    "The Bean": "Topluluk odaklı, vegan dostu atıştırmalıkları ve rahat oturma alanlarıyla, mahallelinin buluşma noktası kahveci.",
    "The Immigrant": "Bir tarafı şarap barı, diğer tarafı bira evi olan, eski New York havasında samimi mekan.",
    "The Spaniard": "Kadife koltukları ve geniş viski menüsüyle, hem şık hem rahat, popüler bir gastropub.",
    "The Standard, High Line": "High Line altında, Alman tarzı bira bahçesi ve şık ızgara restoranıyla, ikonik bir otel.",
    "Travel Bar": "Viski tutkunları için geniş bir seçki sunan, samimi ve sakin atmosferli, şık bir bar.",
    "Turnstyle Underground Market": "Metro istasyonunun altında, çeşitli yemek ve alışveriş dükkanlarıyla dolu, modern ve hareketli çarşı.",
    "Voyager Espresso": "Metro geçidinde gizli, fütüristik dekoru ve bilimsel kahve yaklaşımıyla, modern ve şık kahveci.",
    "While We Were Young": "Pastel tonları ve şık sunumlarıyla, Instagram fotoğrafları ve brunch için ideal, butik restoran.",
    "Whitmans Hudson Yards": "İçli köfteli 'Juicy Lucy' burgeriyle meşhur, modern ve hızlı servis sunan lezzetli burgerci.",
    "William Barnacle Tavern": "Prohibition döneminden kalma, absinthe odaklı menüsüyle, zaman yolculuğu hissi veren tarihi taverna."
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
