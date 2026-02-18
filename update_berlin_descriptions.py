
import json
import os

UPDATES = {
    "Bloom's Bar Berlin": {
        "tr": "Şık dekorasyonu, uzman kokteylleri ve samimi atmosferiyle tanınan, Charlottenburg'da keyifli bir bar.",
        "en": "An intimate and stylish bar in Charlottenburg known for its fancy decor, expert cocktails, and welcoming atmosphere."
    },
    "Bodega Iberica": {
        "tr": "Otantik İspanyol ve Portekiz lezzetleri, tapas ve şaraplarıyla sıcak, romantik bir ortam sunar.",
        "en": "Offers authentic Spanish and Portuguese flavors, tapas, and wines in a warm, romantic setting."
    },
    "Bottega Alimentare Portamivia": {
        "tr": "Kreuzberg'de kaliteli İtalyan ürünleri ve şarapları sunan, uygun fiyatlı ve samimi bir bistro.",
        "en": "A friendly bistro in Kreuzberg offering quality Italian products and wines with an authentic touch."
    },
    "Burger Turm Berlin": {
        "tr": "Mitte'de ferah atmosferi, el yapımı burgerleri ve taze malzemeleriyle ünlü Amerikan tarzı restoran.",
        "en": "An American-style restaurant in Mitte famous for its handcrafted burgers, fresh ingredients, and spacious atmosphere."
    },
    "Burger Turm": {
        "tr": "Mitte'de ferah atmosferi, el yapımı burgerleri ve taze malzemeleriyle ünlü Amerikan tarzı restoran.",
        "en": "An American-style restaurant in Mitte famous for its handcrafted burgers, fresh ingredients, and spacious atmosphere."
    },
    "CEBE COFFEE ROASTERS": {
        "tr": "Friedrichshain'da minimalist tasarımı, etik kahve çekirdekleri ve rahat çalışma ortamıyla öne çıkan kafe.",
        "en": "A modern specialty coffee shop in Friedrichshain known for its minimalist design, ethical beans, and cozy workspace."
    },
    "CEBE COFFEE ROASTERS specialty coffee": {
        "tr": "Friedrichshain'da minimalist tasarımı, etik kahve çekirdekleri ve rahat çalışma ortamıyla öne çıkan kafe.",
        "en": "A modern specialty coffee shop in Friedrichshain known for its minimalist design, ethical beans, and cozy workspace."
    },
    "Café Modo": {
        "tr": "Hip-hop temalı dekoru, harika bagel menüsü ve samimi servisiyle sevilen popüler bir brunch noktası.",
        "en": "A popular brunch spot loved for its hip-hop themed decor, great bagel menu, and friendly service."
    },
    "Champagner Bar": {
        "tr": "Şampanya çeşitleri ve özenli servis anlayışıyla lüks ama rahat bir deneyim sunan sofistike bir mekan.",
        "en": "A sophisticated venue offering a luxurious yet relaxed experience with a variety of champagnes and attentive service."
    },
    "Chestnut Coffee": {
        "tr": "Prenzlauer Berg'de özellikle fıstıklı kruvasanları ve kaliteli kahvesiyle bilinen şirin bir mahalle kafesi.",
        "en": "A charming neighborhood cafe in Prenzlauer Berg known for its pistachio croissants and quality coffee."
    },
    "Chill & Spice": {
        "tr": "Hint ve Singapur mutfağının egzotik lezzetlerini modern bir sunumla birleştiren lezzet odaklı restoran.",
        "en": "A flavor-focused restaurant combining exotic tastes of Indian and Singaporean cuisine with modern presentation."
    },
    "Ciuk - Winebar & Tapas": {
        "tr": "Özenle seçilmiş şarap koleksiyonu ve lezzetli tapas tabaklarıyla keyifli akşamlar için ideal bir şarap barı.",
        "en": "An ideal wine bar for pleasant evenings with a carefully curated wine collection and delicious tapas plates."
    },
    "Classic - Specialty Coffee": {
        "tr": "Kreuzberg'de minimalist tarzı, mükemmel espressosu ve matcha seçenekleriyle kahve severlerin uğrak noktası.",
        "en": "A minimalist stop in Kreuzberg for coffee lovers, featuring excellent espresso and matcha options."
    },
    "Coffee Karros": {
        "tr": "Friedrichshain'da Portekiz usulü Pastel de Nata ve kaliteli kahveleriyle sıcak bir mola yeri.",
        "en": "A warm stop in Friedrichshain offering Portuguese-style Pastel de Nata and quality coffees."
    },
    "CoooL Music Bar": {
        "tr": "Kulüp karmaşasından uzak, iyi müzik ve kokteyllerle rahatlayabileceğiniz samimi bir 'chill' mekanı.",
        "en": "An intimate 'chill' spot where you can relax with good music and cocktails away from the club chaos."
    },
    "Dopamine Bench (Singaporean and Indian Fusion Restaurant & Cocktail Bar)": {
         "tr": "Asya füzyon mutfağı, yaratıcı kokteylleri ve 'bağlantı kurma' temalı dekoruyla canlı bir Friedrichshain mekanı.",
        "en": "A vibrant Friedrichshain venue with Asian fusion cuisine, creative cocktails, and 'connection' themed decor."
    },
    "Dopamine Bench": {
         "tr": "Asya füzyon mutfağı, yaratıcı kokteylleri ve 'bağlantı kurma' temalı dekoruyla canlı bir Friedrichshain mekanı.",
        "en": "A vibrant Friedrichshain venue with Asian fusion cuisine, creative cocktails, and 'connection' themed decor."
    },
    "Dot Tea Bar (一点茶寮)": {
        "tr": "Geleneksel Çin çay seremonisi (Gongfu) ve dim sum çeşitleriyle huzurlu bir mola sunan çay evi.",
        "en": "A peaceful tea house offering traditional Chinese tea ceremony (Gongfu) and dim sum varieties."
    },
    "Dot Tea Bar": {
        "tr": "Geleneksel Çin çay seremonisi (Gongfu) ve dim sum çeşitleriyle huzurlu bir mola sunan çay evi.",
        "en": "A peaceful tea house offering traditional Chinese tea ceremony (Gongfu) and dim sum varieties."
    },
    "Espressomania Coffee Roastery": {
        "tr": "İtalyan cazibesini yansıtan, hem kavurma atölyesi hem de lezzetli panini'leriyle ünlü rahat bir kafe.",
        "en": "A cozy cafe reflecting Italian charm, known as both a roasting workshop and for its delicious paninis."
    },
    "Ewig Freunde": {
        "tr": "Prenzlauer Berg'de şık detayları, organik kahvaltıları ve aile dostu ortamıyla sevilen bir kafe.",
        "en": "A beloved cafe in Prenzlauer Berg with stylish details, organic breakfasts, and a family-friendly atmosphere."
    },
    "Flying Roasters": {
        "tr": "Wedding'de doğrudan ticaret (direct trade) kahveleri ve atölyeleriyle bilinen, endüstriyel şık bir kavurma evi.",
        "en": "An industrial-chic roastery in Wedding known for its direct trade coffees and workshops."
    },
    "GEM Bar": {
        "tr": "Lüks dekoru, karaoke geceleri ve misafirperver personeliyle Schöneberg'in enerjik kokteyl barı.",
        "en": "An energetic cocktail bar in Schöneberg with luxury decor, karaoke nights, and hospitable staff."
    },
    "GLASWEISE Weinbar": {
        "tr": "Ahşap dekoru, doğal şarapları ve nostaljik müzikleriyle sohbet odaklı, sıcak bir şarap barı.",
        "en": "A warm, conversation-focused wine bar with wood decor, natural wines, and nostalgic music."
    },
    "Garçon de Café - Specialty coffee shop - Kaffee": {
        "tr": "Mitte'de Fransız bistrosu havasında, bol ışıklı ve şık bir ortamda nitelikli kahve sunan mekan.",
        "en": "A chic, light-filled venue in Mitte offering specialty coffee with a French bistro vibe."
    },
    "Garçon de Café": {
        "tr": "Mitte'de Fransız bistrosu havasında, bol ışıklı ve şık bir ortamda nitelikli kahve sunan mekan.",
        "en": "A chic, light-filled venue in Mitte offering specialty coffee with a French bistro vibe."
    },
    "GioMecca Pastry": {
        "tr": "İtalyan pasta şefinin elinden çıkan mini tatlıları ve otantik lezzetleriyle ünlü butik bir pastane.",
        "en": "A boutique patisserie famous for mini desserts and authentic flavors created by an Italian pastry chef."
    },
    "Green Wall Coffee": {
        "tr": "Lichtenberg'de saf aromalara odaklanan, kendi kavurduğu çekirdekleri sunan küçük ve samimi bir kahve dükkanı.",
        "en": "A small, intimate coffee shop in Lichtenberg roasting its own beans with a focus on pure flavors."
    },
    "Jane & the Jam": {
        "tr": "Sanatsal atmosferi, şarap-peynir eşleşmeleri ve rahat 'oturma odası' havasıyla trend bir şarap barı.",
        "en": "A trendy wine bar with an artistic atmosphere, wine-cheese pairings, and a relaxed 'living room' vibe."
    },
    "Kaffee Momente Berlin - Café Berlin": {
        "tr": "Pankow'da bagel çeşitleri, cheesecake'i ve sıcak servisiyle mahalle sakinlerinin favorisi olan kafe.",
        "en": "A neighborhood favorite in Pankow known for its bagel varieties, cheesecake, and warm service."
    },
    "Kaffee Momente Berlin": {
        "tr": "Pankow'da bagel çeşitleri, cheesecake'i ve sıcak servisiyle mahalle sakinlerinin favorisi olan kafe.",
        "en": "A neighborhood favorite in Pankow known for its bagel varieties, cheesecake, and warm service."
    },
    "Kerala Amma Mess": {
        "tr": "Güney Hindistan'ın Kerala bölgesine özgü baharatlı ve otantik ev yemekleri sunan mütevazı restoran.",
        "en": "A modest restaurant offering spicy and authentic home-style dishes from the Kerala region of South India. "
    },
    "Kírkē": {
        "tr": "Atina havasını taşıyan, doğal şaraplar ve modern Yunan lezzetleri sunan Graefekiez'deki deli/bar.",
        "en": "A deli/bar in Graefekiez with Athens vibes, offering natural wines and modern Greek flavors."
    },
    "L'apéro Bar": {
        "tr": "Fransız aperitif kültürünü Kreuzberg'e taşıyan, peynir tabakları ve akşamüstü içkileriyle ünlü mekan.",
        "en": "A venue bringing French aperitif culture to Kreuzberg, famous for cheese boards and evening drinks."
    },
    "LETA Patisserie": {
        "tr": "Sanat eseri niteliğinde Fransız tartları ve kişiye özel tatlı tasarımlarıyla öne çıkan üst düzey pastane.",
        "en": "High-end patisserie standing out with artistic French tarts and personalized dessert designs."
    },
    "LOUMI": {
        "tr": "Michelin yıldızlı, yaratıcı menüsü ve rahat ama şık atmosferiyle sıra dışı bir fine-dining deneyimi.",
        "en": "An extraordinary fine-dining experience with a Michelin star, creative menu, and casual yet stylish atmosphere."
    },
    "Pâtisserie Sarina (preorder online only)": {
         "tr": "Detaylara verdiği önem ve 'çok lezzetli' küçük pastalarıyla (Törtchen) bilinen yaratıcı bir pastane.",
        "en": "A creative patisserie known for its attention to detail and 'very delicious' small cakes (Törtchen)."
    },
    "Pâtisserie Sarina": {
         "tr": "Detaylara verdiği önem ve 'çok lezzetli' küçük pastalarıyla (Törtchen) bilinen yaratıcı bir pastane.",
        "en": "A creative patisserie known for its attention to detail and 'very delicious' small cakes (Törtchen)."
    },
    "The Coffee Club SPECIALTY COFFEE": {
        "tr": "Charlottenburg'da tüm gün kahvaltı, modern ortam ve aile dostu yapısıyla rahat bir kafe.",
        "en": "A relaxed cafe in Charlottenburg with all-day breakfast, modern setting, and family-friendly vibe."
    },
    "Cafè Nook Berlin": {
        "tr": "Prenzlauer Berg'de ev yapımı kekleri, doyurucu kahvaltıları ve sessiz ortamıyla huzurlu bir köşe.",
        "en": "A peaceful corner in Prenzlauer Berg with homemade cakes, hearty breakfasts, and a quiet atmosphere."
    },
    "Café Dreizehn": {
        "tr": "Wedding'de sevimli dekorasyonu, pastel de nata'sı ve uygun fiyatlarıyla sevilen mahalle kafesi.",
        "en": "A beloved neighborhood cafe in Wedding with cute decor, pastel de nata, and reasonable prices."
    },
    "Café Libre Berlin": {
        "tr": "Berlin Duvarı Anıtı yanında, organik atıştırmalıkları ve sakin müzikleriyle 'transgender safe space' olan kafe.",
        "en": "A cafe next to the Berlin Wall Memorial, a 'transgender safe space' with organic snacks and calm music."
    },
    "Café Minouche": {
        "tr": "Budapester Straße'de caz müzik eşliğinde kahve ve taze hamur işleri sunan sıcak, davetkar bir kafe.",
        "en": "A warm, inviting cafe on Budapester Straße serving coffee and fresh pastries accompanied by jazz music."
    }
}

def main():
    file_path = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/berlin.json"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated_count = 0
        highlights = data.get('highlights', [])
        
        for place in highlights:
            name = place.get('name', '')
            if name in UPDATES:
                place['description'] = UPDATES[name]['tr']
                place['description_en'] = UPDATES[name]['en']
                updated_count += 1
                
        if updated_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Successfully updated {updated_count} places in berlin.json")
        else:
            print("No places were updated.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
