from enrich_venues import enrich_venues

# BATCH 2: AMALFI, MYKONOS, DUBROVNIK - PART 1

# AMALFI UPDATES
amalfi_updates = {
    "Duomo di Sant'Andrea Apostolo": {
        "desc_tr": "Amalfi'nin kalbinde, devasa bir merdivenin tepesinde yükselen bu katedral, Arap-Norman mimarisinin görkemli bir sentezidir. 9. yüzyıla uzanan tarihi, mozaiklerle bezeli cephesi ve Aziz Andrew'un kutsal kalıntılarını barındıran kriptasıyla büyüleyicidir.",
        "desc_en": "Dominating Amalfi's main square from atop its grand staircase, this cathedral is a stunning fusion of Arab-Norman architecture. Dating back to the 9th century, it features a glittering mosaic facade and a crypt housing the relics of Saint Andrew."
    },
    "Villa Rufolo": {
        "desc_tr": "Ravello'nun en ünlü bahçelerine ev sahipliği yapan bu saray, Richard Wagner'e ilham veren manzarasıyla 'Bahçeler Köşesi' olarak bilinir. Adriyatik'in sonsuz maviliğine bakan terasları ve egzotik bitkileriyle Amalfi Kıyısı'nın en romantik noktasıdır.",
        "desc_en": "Billed as the 'Garden of the Soul,' this historic villa in Ravello inspired Richard Wagner's Parsifal. Its sprawling exotic gardens and iconic terraces overlooking the turquoise sea offer some of the most famous views on the Amalfi Coast."
    },
    "Villa Cimbrone": {
        "desc_tr": "Ravello sırtlarında yer alan bu villa, dünyanın en güzel balkonlarından biri kabul edilen 'Sonsuzluk Terastı' (Terrazzo dell'Infinito) ile ünlüdür. Helenistik büstlerle süslü bu terastan izlenen uçsuz bucaksız deniz ve dağ manzarası nefes kesicidir.",
        "desc_en": "Perched on the cliffs of Ravello, this villa is home to the legendary 'Terrace of Infinity.' Lined with marble busts and offering dizzying views of the coastline where the sky meets the sea, it is a place of unparalleled poetic beauty."
    },
    "Sentiero degli Dei": {
        "desc_tr": "Adı gibi 'Tanrıların Yolu' olan bu antik patika, Amalfi kıyısı boyunca nefes kesici uçurumlar ve teras tarım alanları arasından geçer. Bomerano'dan başlayıp Nocelle'e uzanan yürüyüş boyuncu Positano ve Capri manzarasını kuşbakışı izleyebilirsiniz.",
        "desc_en": "True to its name, the 'Path of the Gods' is an ancient cliffside trail offering divine views of the coastline. Hiking between Bomerano and Nocelle, you'll witness breathtaking panoramas of Positano, Capri, and the azure sea far below."
    },
    "Fiordo di Furore": {
        "desc_tr": "Kayanın içine oyulmuş gibi duran bu dar körfez, İtalya'nın en fotojenik ve gizli yerlerinden biridir. Kıyı yolunun altındaki küçük plajı ve yukarıdaki köprüden izlenen vahşi doğasıyla, Amalfi'nin saklı mücevheri olarak kabul edilir.",
        "desc_en": "A dramatic geological slit in the coastline, this fjord is one of Italy's most photographed hidden gems. With a tiny beach tucked beneath a towering road bridge, it offers a wild and secluded contrast to the more polished resort towns."
    },
    "Grotta dello Smeraldo": {
        "desc_tr": "Adını suyun içindeki ışık oyunlarının yarattığı zümrüt yeşili renkten alan bu mağara, denizin içindeki bir katedrali andırır. Mağaranın içindeki sarkıtlar ve dikitlerin yanı sıra suyun altındaki Noel sahnesi (Presepe) de oldukça dikkat çekicidir.",
        "desc_en": "Named for the enchanting emerald glow created by sunlight filtering through the water, this sea cave features unique stalactites and stalagmites. A highlight of the boat tour is seeing the ceramic nativity scene submerged on the cave floor."
    }
}

# MYKONOS UPDATES
mykonos_updates = {
    "Armenistis Lighthouse": {
        "desc_tr": "Adanın kuzeybatısında, sarp kayalıkların ucunda yer alan bu tarihi fener, Mykonos'un en vahşi ve doğal manzarasını sunar. Özellikle gün batımında Komşu adalar Tinos ve Syros'u izlemek için Mikonos'taki en sessiz ve huzurlu noktadır.",
        "desc_en": "Perched on a rugged cliff on the island's northwestern tip, this historic lighthouse offers panoramic views of the Aegean and neighboring islands. It is a quiet sanctuary, perfect for watching the sunset away from the Chora crowds."
    },
    "Matogianni": {
        "desc_tr": "Mykonos Town'un (Chora) ana damarı olan bu dar sokak, bembeyaz evleri, begonvilleri ve dünyaca ünlü tasarım butikleriyle adanın kalbidir. Her adımda şıklığın ve geleneksel Ege mimarisinin harmanlandığı büyüleyici bir atmosfere sahiptir.",
        "desc_en": "The main artery of Chora, Matogianni is a dazzling Labyrinth of whitewashed facades, blue doors, and high-end fashion boutiques. It captures the essence of Mykonos' cosmopolitan charm and traditional Cycladic beauty."
    },
    "Ano Mera": {
        "desc_tr": "Mykonos'un kozmopolit kıyılarının aksine, adanın merkezindeki Ano Mera geleneksel bir köy yaşamı sunar. Meydanındaki yerel tavernaları ve tarihi Panagia Tourliani Manastırı ile adanın otantik ruhunu keşfedeceğiniz duraktır.",
        "desc_en": "A tranquil contrast to the bustling coast, Ano Mera is the island's inland village hub. Centered around a charming square with local tavernas and the red-domed Panagia Tourliani Monastery, it offers a glimpse into authentic island life."
    },
    "Psarou beach": {
        "desc_tr": "Dünya jet sosyetesinin ve Hollywood yıldızlarının Mykonos'taki favori plajı olan Psarou, turkuaz suları ve ultra-lüks hizmetiyle bilinir. İkonik Nammos Beach Club'a ev sahipliği yapan sahil, adanın en prestijli güneşlenme noktasıdır.",
        "desc_en": "The playground of the global elite, Psarou is Mykonos' most glamorous beach. Famed for its turquoise waters and the world-renowned Nammos Beach Club, it is the place to see and be seen while enjoying high-end Mediterranean luxury."
    },
    "Scorpios": {
        "desc_tr": "Paraga Koyu'nda modern bir 'agora' konseptiyle tasarlanan Scorpios, sadece bir plaj kulübü değil, ruhsal bir deneyim alanıdır. Bohem-lüks dekorasyonu, gün batımı ritüelleri ve dünya çapındaki DJ performanslarıyla adanın en ikonik noktasıdır.",
        "desc_en": "Designed as a modern-day agora on Paraga Beach, Scorpios is a holistic social site known for its bohemian-luxury vibe. Its sunset rituals, organic cuisine, and deep melodic house music make it the most coveted ticket on the island."
    }
}

# DUBROVNIK UPDATES
dubrovnik_updates = {
    "Rector's Palace": {
        "desc_tr": "Raguza Cumhuriyeti döneminde şehrin yönetim merkezi olan bu saray, Gotik, Rönesans ve Barok mimarinin eşsiz bir karışımıdır. İç avlusundaki muazzam akustiğiyle yaz konserlerine ev sahipliği yapar ve Dubrovnik tarihini en saf haliyle yansıtır.",
        "desc_en": "The seat of the Rector of the Republic of Ragusa, this palace is a masterpiece of Gothic-Renaissance architecture. Its elegant atrium hosts classical concerts, while its museum rooms showcase the wealth and power of maritime Dubrovnik."
    },
    "Sponza Palace": {
        "desc_tr": "Şehrin en iyi korunmuş tarihi binalarından biri olan Sponza Sarayı, zengin taş işçiliği ve taş avlusuyla dikkat çeker. Eskiden gümrük binası ve nane olarak kullanılan yapı, günümüzde bin yıllık devlet arşivlerine ev sahipliği yapmaktadır.",
        "desc_en": "One of the few buildings to survive the 1667 earthquake, Sponza Palace features a harmonious blend of Gothic and Renaissance styles. Once a dynamic customs house, it now guards over a millennium of Dubrovnik’s historical archives."
    },
    "Saint Blaise’s Church": {
        "desc_tr": "Dubrovnik'in koruyucu azizi olan Aziz Blaise'e adanan bu Barok kilise, şehrin dini ve sosyal kalbidir. Kilisenin üzerindeki gümüş aziz heykeli, 1706'daki büyük yangından mucizevi bir şekilde kurtulmuş olmasıyla halk için kutsaldır.",
        "desc_en": "Dedicated to the city's patron saint, this Venetian-baroque church is a symbol of Dubrovnik's resilience. It houses a precious silver-gilt statue of St. Blaise, which famously survived the great fire of 1706 untouched."
    },
    "Dubrovnik Cable Car": {
        "desc_tr": "Dubrovnik'in surlu şehrini ve Adriyatik Adaları'nı kuşbakışı görmenin en hızlı ve etkileyici yolu bu teleferiktir. 4 dakikalık bir yolculukla Srđ Tepesi'ne ulaştığınızda, kentin turuncu çatılarını ve sonsuz maviliği panoramik olarak izleyebilirsiniz.",
        "desc_en": "For the best birds-eye view of the walled city and the Adriatic islands, take the 4-minute ride to the summit of Mount Srđ. From the viewing plateau, the sight of the city's terracotta roofs and the blue sea is spectacular."
    },
    "Lokrum": {
        "desc_tr": "Dubrovnik kıyısından sadece 10 dakika uzaklıktaki bu doğa koruma alanı, tavus kuşlarının serbestçe gezindiği bir cennet adasıdır. Benedictine Manastırı kalıntıları, botanik bahçesi ve 'Ölü Deniz' isimli tuzlu gölüyle huzurlu bir kaçış noktasıdır.",
        "desc_en": "A lush nature reserve just a 10-minute boat ride from the Old Port, Lokrum is inhabited only by free-roaming peacocks and rabbits. It features botanical gardens, historic monastery ruins, and a salty inland swimming pond."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Batch 2 Enrichment: Amalfi, Mykonos, Dubrovnik...")
enrich_venues("amalfi", amalfi_updates)
enrich_venues("mykonos", mykonos_updates)
enrich_venues("dubrovnik", dubrovnik_updates)
print("✨ Batch 2 Enrichment - Part 1 Complete.")
