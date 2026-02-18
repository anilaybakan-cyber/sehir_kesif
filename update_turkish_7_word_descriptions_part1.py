
import json
import os
import glob
import re

# Dictionary of updates: Key = Place Name, Value = New Turkish Description
UPDATES = {
    # DUBLIN
    "The Wine Pair": "Butik şarap barı, peynir ve şarküteri tabaklarıyla samimi bir tadım ortamı sunuyor.",
    
    # FLORANSA
    "FLUID - Specialty Coffee & Sharing": "Modern kahve dükkanı, geniş demleme seçenekleri ve rahat çalışma ortamıyla öne çıkıyor.",
    "Osteria Vecchio Cancello": "Geleneksel Toskana mutfağı sunan, antika dekorlu şık ve otantik bir restoran.",
    "Osteria dei Leoni Firenze": "Floransa bifteği ve yerel şarapları, 15. yüzyıldan kalma tarihi bir ahırda sunuyor.",
    "Pasticceria Buonamici": "1949'dan beri hizmet veren aile pastanesi, meşhur fıstıklı cantucci'siyle tanınıyor.",
    "Ristorante La Gioia Toscana": "Geleneksel Toskana lezzetleri ve mükemmel tiramisusuyla misafirperver bir İtalyan restoranı.",
    "RivaReno Gelato Firenze": "Taze ve doğal malzemelerle hazırlanan, yoğun kıvamlı ve ödüllü dondurma çeşitleri.",
    "Sbrino": "Çiftlikten taze sütle yapılan, yaratıcı ve doğal aromalı artizan dondurma dükkanı.",
    "Taverna Dei Servi Firenze": "Tarihi atmosferde trüflü makarna ve Floransa bifteği sunan klasik Toskana tavernası.",
    "Wine Lab - vino sfuso": "Kendi şarabını kendin doldur konseptiyle çalışan, geniş seçenekli samimi şarap butiği.",
    
    # GIETHOORN
    "Chinees Indisch Restaurant 'Lotus'": "Hollanda'da popüler olan Çin-Endonezya mutfağını sunan, sıcak ve samimi bir restoran.",
    
    # HONG KONG
    "Embla": "İskandinav ve Asya lezzetlerini harmanlayan, mevsimsel ve zarif bir fine-dining restoranı.",
    "FRANCIS west": "Kuzey Afrika ve Orta Doğu lezzetlerini modern bir dokunuşla sunan canlı mekan.",
    "Islet Coffee Lab (Central)": "Minimalist dekoru ve huzurlu ortamıyla şehrin kaosundan kaçabileceğiniz özel kahve durağı.",
    "The Mansion, Wyndham St": "Kabare bar konseptli, sanatsal kokteyller ve canlı müzikle eğlenceli bir gece mekanı.",
    "The Savory Project": "Tuzlu ve umami notalara odaklanan, deneysel ve sofistike kokteyller sunan bar.",
    "Urban Coffee Roaster SOHO": "Endüstriyel şık tasarımı ve ödüllü kahveleriyle popüler bir brunch ve kahve noktası.",
    "WAKARAN": "Japon ve Çin lezzetlerini batı teknikleriyle birleştiren, sanat dolu füzyon restoranı.",
    "ztoryhome": "Kitapçı, galeri ve kafe konseptini birleştiren, huzurlu ve hikaye dolu bir mekan.",
    
    # İSTANBUL
    "Kronotrop": "Nitelikli kahve akımının öncüsü, ödüllü kavrumları ve zengin demleme çeşitleriyle ünlü.",
    
    # LİZBON
    "Black Pavilion Restaurant": "Modern ve şık atmosferde, muhteşem şehir manzarası eşliğinde çağdaş Portekiz mutfağı.",
    "Fusion Grill": "Akdeniz ve dünya mutfağından ızgara lezzetleri sunan, samimi ve rahat bir restoran.",
    "Häagen-Dazs": "Dünyaca ünlü dondurma markasının Lizbon şubesi, klasik ve özel tatlar sunuyor.",
    "Listambul": "Türk ve Portekiz lezzetlerini buluşturan, baklava ve köfte gibi klasikler sunan mekan.",
    "Love Lisbon": "Canlı müzik eşliğinde otantik Nepal yemekleri sunan, enerjik ve samimi bir restoran.",
    "Matoli Gelato": "Sürekli değişen yaratıcı çeşitleriyle, taze ve doğal malzemeli artizan dondurma dükkanı.",
    "Novo Mundo": "Taze ve yerel malzemelerle hazırlanan, rafine Portekiz lezzetleri sunan şık restoran.",
    "O Tapas": "Geleneksel Portekiz tapaları ve deniz ürünleri sunan, sıcak ve misafirperver bir mekan.",
    "PUT IT ON LISBON": "Glutensiz tatlıları ve sağlıklı içecekleriyle öne çıkan, sevimli ve rahat kafe.",
    "Prova O Melhor Tapas": "İtalyan ve Portekiz mutfağını harmanlayan, seçkin şaraplar eşliğinde lezzetli tapalar.",
    "romana. specialty coffee": "Nitelikli kahvelerinin yanı sıra vegan ve glutensiz tatlılarıyla sevilen rahat kafe.",
    
    # LONDRA
    "Filo": "Canlı müzik eşliğinde otantik Brezilya mutfağı ve kokteylleri sunan keyifli mekan.",
    "Osteria Fiorentina": "Toskana aile sofrası sıcaklığında, el yapımı makarna ve biftek sunan restoran.",
    
    # LUCERNE
    "Aux Merveilleux de Fred": "Bulut gibi hafif bezeleri ve çikolatalı brioche'larıyla ünlü Fransız pastanesi.",
    "Bar bei Miguel": "İsviçre ve İspanyol mutfağını birleştiren, geniş bira seçeneğine sahip canlı gastropub.",
    "Bebié Konditorei Confiserie GmbH": "Geleneksel İsviçre pastaları, pralinler ve taze hamur işleri sunan şirin pastane.",
    "Bäckerei Macchi": "Taze sandviçler, salatalar ve fırın ürünleri sunan, istasyona yakın pratik fırın.",
    "Dal Mattino": "İtalyan kahvaltısı, kruvasanlar ve özel kahveleriyle güne başlamak için harika bir kafe.",
    "Glutenfreie Brotwerkstatt": "Çölyak dostu, %100 glutensiz ekmek ve hamur işleri üreten özel bir fırın.",
    "Restaurant Don Feri": "İspanyol ve İtalyan esintili Akdeniz yemekleri sunan, aile dostu samimi restoran.",
    "Restaurant Scala": "Göl ve dağ manzaralı, Art Deco tarzında şık ve romantik fine-dining restoranı.",
    
    # MARAKEŞ
    "HESPERIS Coffee Factory": "Barista akademisi ve restoranı birleştiren, şık tasarımlı nitelikli kahve mekanı.",
    "Kesh cup Marrakech": "Medina'da taze smoothie ve özel baharatlı kahve molası için sıcak bir durak.",
    "Mandala Society - Koutoubia - Marrakech": "Yerel ve organik malzemelerle hazırlanan sağlıklı, etik ve vejetaryen dostu mutfak.",
    
    # MARSİLYA
    "Absolem Marseille": "Latin esintili dekoru ve DJ performanslarıyla, kokteyl ve shotlarıyla ünlü canlı bar.",
    "Carry Nation": "Marsilya'nın gizli speakeasy barı, 1920'ler atmosferinde özel kokteyller sunuyor.",
    "Aslan Kadaifs Pâtisserie": "Geleneksel Türk tatlıları, künefe ve baklavayı Marsilya'ya taşıyan aile pastanesi.",
    
    # MİLANO
    "Cafezal Specialty Coffee - Magenta": "1920'lerin şıklığını yansıtan, Brezilya çekirdekleriyle hazırlanan nitelikli kahve ve brunch mekanı.",
    "Zizania via Celestino | Cocktail bar Milano": "Botanik temalı dekoru ve yenilikçi imza kokteylleriyle öne çıkan popüler bar.",
    
    # NAPOLİ
    "AZZUPPA Restaurant": "Geleneksel İtalyan çorba ve yemeklerini modern dokunuşlarla sunan, retro tarzlı mekan.",
    "Lento Hi-Fi Bar": "Yüksek kaliteli ses sistemi ve vinyl plaklar eşliğinde kokteyl sunan dinleme barı."
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
