import json
import os

UPDATES = {
    "cannes.json": {
        "cann_juan-les-pins_beach": {
            "tr": "Cannes'ın en şık sahil bölgelerinden biri olan Juan-les-Pins, geniş kum plajları ve art-deco mimarisiyle ünlüdür. Gece hayatı ve caz festivaliyle tanınan bölge, Riviera'nın enerjisini en iyi yansıtan noktalardan biridir.",
            "en": "One of Cannes' most stylish coastal areas, Juan-les-Pins is famous for its wide sandy beaches and Art Deco architecture. Known for its nightlife and jazz festival, it's a spot that perfectly reflects the energy of the Riviera."
        }
    },
    "dubrovnik.json": {
        "ChIJeVmgMkp1TBMRQmPeT1RAwSQ": { # Uvala Lapad
            "tr": "Dubrovnik'in en popüler aile plajlarından biridir. Çevresindeki yürüyüş yolları, restoranlar ve çocuk oyun alanlarıyla gün boyu konforlu bir vakit geçirme imkanı sunar. Sakin suları yüzmek için oldukça güvenlidir.",
            "en": "One of Dubrovnik's most popular family beaches. With surrounding walking paths, restaurants, and children's playgrounds, it offers a comfortable way to spend the day. Its calm waters are very safe for swimming."
        }
    },
    "sardinya.json": {
        "sard_scivu_beach": {
            "tr": "Sardinya'nın batı kıyısında yer alan Scivu, vahşi ve el değmemiş güzelliğiyle büyüleyicidir. Yüksek kum tepeleri ve kristal berraklığındaki turkuaz deniziyle doğaseverler için gerçek bir gizli cennettir.",
            "en": "Located on Sardinia's western coast, Scivu is enchanting with its wild and untouched beauty. With high sand dunes and crystal-clear turquoise sea, it's a true hidden paradise for nature lovers."
        }
    },
    "amalfi.json": {
        "ChIJN1U5u6KZOxMR9MY8nwnmfd4": { # Tordigliano
            "tr": "Positano yakınlarında yer alan bu gizli koy, Amalfi Kıyısı'nın en doğal ve sakin noktalarından biridir. Sadece tekneyle veya zorlu bir patikadan yürüyerek ulaşılabilmesi, buranın huzurlu atmosferini korumasını sağlamıştır.",
            "en": "This hidden bay near Positano is one of the most natural and peaceful spots on the Amalfi Coast. Being accessible only by boat or a challenging hiking path has helped preserve its tranquil atmosphere."
        }
    },
    "catania.json": {
        "cat_cafe_agata_19": { # Catania Beach (La Playa)
            "tr": "Catania'nın güneyinde kilometrelerce uzanan altın kumlu plaj bölgesidir. Etna Yanardağı manzarası eşliğinde denize girmek isteyenlerin tercihidir; çok sayıda plaj kulübü ve sosyal tesis barındırır.",
            "en": "A kilometers-long golden sand beach area south of Catania. Preferred by those who want to swim with a view of Mount Etna, it hosts numerous beach clubs and social facilities."
        },
        "cat_piazza_carlo_alberto": { # Piazza Carlo Alberto
            "tr": "Catania'nın en büyük ve en renkli açık hava pazarlarından biri olan 'A Fera 'o Luni'ye ev sahipliği yapar. Yerel meyve, sebze ve tekstil ürünlerinin satıldığı pazar, şehrin otantik yaşamını gözlemlemek için mükemmeldir.",
            "en": "Home to 'A Fera 'o Luni', one of Catania's largest and most colorful open-air markets. Selling local fruits, vegetables, and textiles, the market is perfect for observing the city's authentic life."
        },
        "cat_viale_regina_margherita": { # Viale Regina Margherita
            "tr": "Şehrin en geniş ve ağaçlıklı bulvarlarından biridir. Tarihi villaları ve huzurlu atmosferiyle bilinir; akşam yürüyüşleri ve Catania'nın zarif mimarisini keşfetmek için ideal bir rotadır.",
            "en": "One of the city's widest and most tree-lined boulevards. Known for its historic villas and peaceful atmosphere, it's an ideal route for evening walks and exploring Catania's elegant architecture."
        },
        "cat_chiosco_giammona": { # Chiosco Giammona
            "tr": "Catania'nın geleneksel 'kiosk' kültürünün en meşhur temsilcilerinden biridir. Özellikle meşhur maden suyu ve limonlu içecekleriyle ferahlamak isteyen yerellerin ve turistlerin uğrak noktasıdır.",
            "en": "One of the most famous representatives of Catania's traditional 'kiosk' culture. It's a popular spot for locals and tourists alike to refresh with famous mineral water and lemon drinks."
        },
        "cat_sikulo": { # Sikulo
            "tr": "Geleneksel Sicilya mutfağını modern bir dokunuşla sunan popüler bir restorandır. Taze deniz ürünleri ve yöresel malzemelerle hazırlanan menüsüyle gurme bir lezzet durağıdır.",
            "en": "A popular restaurant offering traditional Sicilian cuisine with a modern touch. It's a gourmet food destination with its menu prepared with fresh seafood and local ingredients."
        },
        "cat_toscano_palace": { # Toscano Palace
            "tr": "Catania'nın tarihi merkezinde yer alan görkemli bir yapıdır. Barok mimarinin izlerini taşıyan saray, şehrin zengin kültürel mirasını ve soylu geçmişini yansıtan önemli binalardan biridir.",
            "en": "A magnificent building located in the historic center of Catania. The palace, bearing traces of Baroque architecture, is one of the important buildings reflecting the city's rich cultural heritage and noble past."
        }
    }
}

# Mapping IDs for Catania because the script found description matches, need to find the correct IDs in the file.
# I'll check IDs in catania.json first.
