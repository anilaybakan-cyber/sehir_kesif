import json

def enrich_bodrum():
    with open("assets/cities/bodrum.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    enrichments = {
        "ChIJYw5gNEJsvhQRcRzUhvXx1Cs": {
            "tr": "15. yüzyılda Saint Jean Şövalyeleri tarafından inşa edilen bu görkemli kale, dünyanın en önemli su altı arkeoloji müzelerinden birine ev sahipliği yapar. Antik batıklardan çıkan paha biçilemez eserleri görebilir ve kalenin burçlarından muazzam deniz manzarasını seyredebilirsiniz.",
            "en": "Built by the Knights of St. John in the 15th century, this iconic castle houses a world-class underwater archaeology museum. You can explore ancient shipwrecks and enjoy breathtaking Aegean views from its towers."
        },
        "ChIJlwmXEkdsvhQR0fktlJphpF4": {
            "tr": "Antik dünyanın yedi harikasından biri olan bu devasa anıt mezarın kalıntıları, Karya kralı Mausolus için inşa edilmiştir. Günümüze sadece temelleri kalmış olsa da, tarihin en büyük mimari eserlerinden birinin izlerini sürmek büyüleyici bir deneyimdir.",
            "en": "Once one of the Seven Wonders of the Ancient World, the remains of this grand tomb were built for King Mausolus. Although mostly in ruins today, it remains a site of immense historical and architectural significance."
        },
        "ChIJv9W_9UdsvhQR2r-WmkBy9K4": {
            "tr": "Klasik Helen döneminden günümüze ulaşan bu muazzam tiyatro, Bodrum'un en eski yapılarından biridir. Sadece tarihi dokusuyla değil, aynı zamanda yaz aylarında düzenlenen konserler ve Bodrum Kalesi'ne bakan panoramik manzarasıyla da mutlaka görülmelidir.",
            "en": "Dating back to the 4th century BC, this ancient theater is one of Bodrum's best-preserved historical sites. It offers panoramic harbor views and still hosts world-class concerts during summer nights."
        },
        "ChIJa74LinVtvhQRBjZuPM4x-bw": {
            "tr": "Halikarnassos Antik Kenti'nin giriş kapısı olan Myndos Kapısı, Büyük İskender'in şehri kuşattığı tarihi noktadır. Restorasyon çalışmalarının ardından ziyarete açılan kapı, antik kentin surlarıyla birlikte tarihin derinliklerini yansıtır.",
            "en": "The Myndos Gate was the main entrance to the ancient city of Halicarnassus and the site of Alexander the Great's famous siege. Today, its restored towers offer a glimpse into the city's heroic past."
        },
        "ChIJSxsWkUdtvhQREXRy5x1VJck": {
            "tr": "Bodrum Yarımadası'nın en rüzgarlı tepelerinden birinde yer alan bu tarihi yel değirmenleri, hem Bodrum hem de Gümbet koylarını kuşbakışı gören efsanevi bir manzaraya sahiptir. Özellikle gün doğumu ve gün batımında fotoğraf tutkunları için vazgeçilmezdir.",
            "en": "Perched on a windy hill overlooking both Bodrum and Gumbet bays, these historic windmills offer some of the best panoramic views on the peninsula. They are especially stunning during sunrise and sunset."
        },
        "ChIJ_1Ko1EFsvhQR3P9pZBJXqZ4": {
            "tr": "Eski bir belediye binasında yer alan bu butik müze, Bodrum'un süngercilik ve tekne yapım tarihini belgeler. Müzede sergilenen devasa deniz kabuğu koleksiyonu ve maket tekneler, kentin denizci ruhunu mükemmel bir şekilde yansıtır.",
            "en": "Housed in a charming old building, this boutique museum documents Bodrum's sponge diving and boat-building heritage. It features an impressive seashell collection and intricate scale models of traditional vessels."
        },
        "ChIJBQsjnm5svhQRJz_yDJJmtw0": {
            "tr": "Türkiye'nin sanat güneşi Zeki Müren'in Bodrum'da hayatının son yıllarını geçirdiği evi, şimdilerde bir müze olarak hizmet vermektedir. Müzede sanatçının sahne kostümleri, tabloları ve kişisel eşyaları sergilenerek onun anısı yaşatılmaktadır.",
            "en": "The final home of Turkey's legendary artist Zeki Müren has been converted into a museum dedicated to his life and career. Visitors can see his iconic stage costumes, paintings, and personal memorabilia."
        },
        "ChIJKSkfloRuvhQRo7OVs9aIrj8": {
            "tr": "Leleg uygarlığının başkenti olan Pedasa, zeytin ağaçları arasındaki patikalardan yürüyerek ulaşılan gizli bir antik kenttir. Doğa yürüyüşü ve tarih meraklıları için, sur duvarları ve kule kalıntıları arasında sessiz bir keşif imkanı sunar.",
            "en": "The capital of the Leleg civilization, Pedasa is a hidden ancient city accessible via scenic trails through olive groves. It is a perfect spot for hikers looking to explore silent ruins, city walls, and burial mounds."
        },
        "ChIJYeiNdDlyvhQRtOAzFXdvYgw": {
            "tr": "Geleneksel mimariyle modern sanatı birleştiren bu kültür ve sanat köyü, yıl boyu süren sergileri, atölyeleri ve restoranıyla çok şık bir komplekstir. Akşamları düzenlenen açık hava konserleri ve film gösterimleri buraya ayrı bir ruh katar.",
            "en": "Blending traditional architecture with modern art, this cultural village is an upscale complex featuring galleries, boutiques, and gourmet dining. Its open-air concerts and cinema nights are a summer highlight."
        },
        "ChIJ_759OOxxvhQRXZc1KZwApPw": {
            "tr": "Dünyanın en lüks yat limanlarından biri olan Yalıkavak Marina, uluslararası tasarım ödülleriyle tescillenmiş bir komplekstir. Dünya çapında ünlü lüks markaların mağazaları ve Michelin yıldızlı kalitesinde restoranlarıyla Bodrum'un jet sosyete noktasıdır.",
            "en": "As one of the world's most luxurious marinas, Yalıkavak is an award-winning hub for mega-yachts and elite travelers. It hosts high-end designer boutiques and world-class dining destinations."
        },
        "ChIJS6IGGndtvhQRmh_4muCldt8": {
            "tr": "Mandalina bahçeleriyle çevrili Bitez Plajı, özellikle rüzgar sörfü tutkunları ve sığ deniziyle çocuklu aileler için ideal bir noktadır. Sahil boyunca uzanan kafe ve restoranlarda taze deniz mahsullerinin tadına bakabilirsiniz.",
            "en": "Famed for its mandarin groves and shallow waters, Bitez Beach is perfect for windsurfing and family outings. The beach is lined with cozy cafes and seafood restaurants that offer a relaxed Bodrum vibe."
        },
        "ChIJ47Rqu_p0vhQRei2H38xNHuI": {
            "tr": "Bohem atmosferi ve denizin içindeki masalarıyla ünlü Gümüşlük, Bodrum Yarımadası'nın en romantik köşesidir. Tavşan Adası'na sığ sudan yürüyerek geçebilir ve akşamları sahil kenarındaki balıkçılarda taze balık yiyebilirsiniz.",
            "en": "Known for its bohemian charm and seaside tables, Gümüşlük is the peninsula's most romantic corner. You can walk through shallow waters to Rabbit Island and enjoy world-class fish dinners at sunset."
        },
        "ChIJUQN2bBVyvhQROyp0NzOXui8": {
            "tr": "Ortakent'te yer alan Yahşi Plajı, kristal netliğindeki denizi ve geniş kum sahiliyle bilinir. 'Mavi Bayraklı' olan bu plaj, uzun yürüyüş yolu ve her bütçeye uygun mekan seçenekleriyle Bodrum'un en tercih edilen sahillerindendir.",
            "en": "Located in Ortakent, Yahşi Beach is famous for its crystal-clear Blue Flag waters and long sandy shore. It offers a great promenade and a wide variety of beach clubs and local eateries for all budgets."
        },
        "ChIJVVK9K_YMvhQRuLKlILDC-Uo": {
            "tr": "Akyarlar'da bulunan Karaincir, incecik altın sarısı kumu ve rüzgara kapalı, durgun deniziyle adeta bir havuzu andırır. Suyun serinliği ve sahilin sakinliği, huzurlu bir deniz günü arayanlar için Karaincir'i eşsiz kılar.",
            "en": "Karaincir Beach in Akyarlar feels like a natural swimming pool with its fine golden sand and calm, sheltered bay. Known for its cool waters, it is the perfect escape for those seeking peace and tranquility."
        },
        "ChIJV4CT2fhtvhQRmuYDm_i3S5M": {
            "tr": "Adını suyunun cam berraklığından alan Akvaryum Koyu, sadece tekne turlarıyla ulaşılabilen bakir bir doğa harikasıdır. Şnorkelle dalış yaparken balıkları çıplak gözle görebileceğiniz bu koy, Bodrum'un en özel duraklarından biridir.",
            "en": "Named for its crystal-clear waters, Aquarium Bay is a pristine natural wonder accessible only by boat. It is a top spot for snorkeling, where you can swim with schools of fish in impossibly blue water."
        }
    }
    
    for item in data["highlights"]:
        pid = item.get("id")
        if pid in enrichments:
            item["description"] = enrichments[pid]["tr"]
            item["description_en"] = enrichments[pid]["en"]
            
    with open("assets/cities/bodrum.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    enrich_bodrum()
