from enrich_venues import enrich_venues

# BATCH 4: BARI, SARDINYA, BUDVA, KSAMIL, RHODES, BUDAPESTE - PART 1

# BARI UPDATES
bari_updates = {
    "Cathedral of Saint Sabinus": {
        "desc_tr": "Bari'nin daha az bilinen ama en az Aziz Nikola kadar etkileyici olan bu 12. yüzyıl katedrali, Puglia Romanesk mimarisinin zarif bir örneğidir. Alt katındaki antik kalıntılar ve beyaz kireçtaşından cephesiyle kentin ruhani duraklarından biridir.",
        "desc_en": "This 12th-century cathedral, less famous but equally impressive as St. Nicholas, is a prime example of Apulian Romanesque beauty. With its ancient ruins in the crypt and radiant white limestone facade, it is a spiritual anchor of the city."
    },
    "Castello Svevo di Bari": {
        "desc_tr": "Deniz kıyısında yükselen bu heybetli Norman kalesi, Bari Vecchia'nın girişini korur. Tarih boyunca saray, hapishane ve kışla olarak kullanılan kale, günümüzde kentin savunma tarihini anlatan sergiler ve eşsiz deniz manzaraları sunmaktadır.",
        "desc_en": "Standing guard over the entrance to Bari Vecchia, this imposing Norman-Swabian fortress is an architectural chronicle of the city. Once a royal palace and a prison, it now hosts historical exhibitions and offers superb views over the Adriatic coast."
    },
    "Teatro Petruzzelli": {
        "desc_tr": "İtalya'nın en görkemli dördüncü opera binası olan Petruzzelli, kırmızı kadife koltukları ve altın varaklı süslemeleriyle büyüleyicidir. Yangından sonra küllerinden doğan bu tiyatro, Bari'nin sanat ve prestij sembolü olarak dünyaca ünlü performanslara ev sahipliği yapar.",
        "desc_en": "The fourth largest opera house in Italy, Petruzzelli is a marvel of red velvet and gilded ornamentation. Having risen from the ashes after a major fire, it stands as Bari's ultimate symbol of cultural prestige, hosting world-class performances."
    }
}

# SARDINYA UPDATES
sardinya_updates = {
    "La Maddalena": {
        "desc_tr": "Sardinya'nın kuzeyindeki bu takımada, pembe granit kayaları ve zümrüt yeşili deniziyle bir doğa koruma alanıdır. Milli park statüsündeki adalar, tekne turları için Akdeniz'in en kristal netliğindeki duraklarını sunar.",
        "desc_en": "This northern archipelago is a pristine sanctuary of pink granite rocks and emerald-green waters. As a national park, these islands offer some of the Mediterranean's most crystal-clear spots for sailing and snorkeling."
    },
    "Cattedrale di Santa Maria Assunta e Santa Cecilia": {
        "desc_tr": "Cagliari'nin kalesi üzerinde yükselen bu 13. yüzyıl katedrali, Pisan-Gotik ve Barok tarzların görkemli bir karışımıdır. İçindeki mermer vaiz kürsüsü ve yeraltı kriptasındaki kraliyet mezarlarıyla kentin tarihi kalbidir.",
        "desc_en": "Perched on Cagliari's 'Castello' hill, this 13th-century cathedral is a stunning mix of Pisan-Gothic and Baroque styles. Its intricate marble interior and the royal tombs within the sanctuary crypt make it the historic heart of the city."
    },
    "Su Nuraxi di Barumini": {
        "desc_tr": "Sardinya'ya özgü gizemli Nurajik medeniyetinden kalan bu devasa taş yapı kompleksi, UNESCO Dünya Mirası listesindedir. M.Ö. 1500 yılına kadar uzanan bu antik savunma kuleleri, adanın vahşi ve kadim tarihine ışık tutar.",
        "desc_en": "A UNESCO-listed marvel of the mysterious Nuragic civilization, this massive stone complex is unique to Sardinia. Dating back to 1500 BC, these ancient defensive towers offer an unparalleled glimpse into the island's wild and prehistoric past."
    }
}

# BUDVA UPDATES
budva_updates = {
    "Citadela Budva": {
        "desc_tr": "Eski Şehir'in en yüksek noktasında yer alan bu tarihi kale, Adriyatik'in sonsuz maviliğine bakmaktadır. Kütüphanesi, müzesi ve panoramik seyir terasıyla Budva'nın denizcilik ve askeri tarihini hissetmek için en doğru noktadır.",
        "desc_en": "Perched at the highest point of the Old Town, this historic fortress offers sweeping views of the endless Adriatic blue. With its ancient library and museum, it is the best place to feel the pulse of Budva’s maritime and military heritage."
    },
    "Mogren beach": {
        "desc_tr": "Old Town'dan kayalıklar boyunca uzanan dar bir patikayla ulaşılan Mogren, Budva'nın en romantik plajıdır. İki küçük koyun birleştiği bu plaj, falezlerle çevrili olmasıyla rüzgardan korunur ve tertemiz sularıyla bilinir.",
        "desc_en": "Reached via a scenic path carved through the cliffs from the Old Town, Mogren is Budva's most romantic beach. Comprised of two golden coves protected by towering rock faces, it offers secluded, crystal-clear swimming."
    }
}

# KSAMIL UPDATES
ksamil_updates = {
    "Plazhi Ksamilit": {
        "desc_tr": "Adaları görebileceğiniz bu ana plaj, sığ ve turkuaz deniziyle Ksamil'in kalbidir. Bembeyaz kumu ve çevresindeki ferah deniz ürünleri restoranlarıyla, İyon Denizi kıyısında lüks ve huzurlu bir gün geçirmek isteyenlerin ilk tercihidir.",
        "desc_en": "Facing the three islands, this main beach is the heart of Ksamil with its shallow, turquoise waters. Its brilliant white sand and the surrounding fresh seafood restaurants offer a serene escape on the edge of the Ionian Sea."
    },
    "Butrint National Archaeological Park": {
        "desc_tr": "UNESCO mirası olan bu antik kent, zeytin ağaçları ve sulak alanlar arasında gizlenmiş bir tarih hazinesidir. Roma tiyatrosu, Bizans bazilikası ve Venedik kalesiyle akdeniz medeniyetlerinin katman katman tarihini sunar.",
        "desc_en": "A UNESCO-listed treasure, this ancient city is a historical gem hidden amidst olive groves and wetlands. With its Roman theater and Byzantine basilica, it offers a multi-layered journey through centuries of Mediterranean history."
    }
}

# RHODES UPDATES
rhodes_updates = {
    "Palace of the Grand Master of the Knights of Rhodes": {
        "desc_tr": "Kalenin en yüksek noktasında yer alan bu görkemli yapı, Rodos Şövalyeleri'nin yönetim merkeziydi. Devasa surları, mozaik zeminli salonları ve Orta Çağ ruhunu yansıtan avlusuyla kentin en heybetli anıtıdır.",
        "desc_en": "Dominating the highest point of the fortress, this grand palace was the administrative heart of the Knights of Rhodes. With its massive walls, mosaic floors, and medieval courtyards, it is the city's most imposing monument."
    },
    "Street of the Knights of Rhodes": {
        "desc_tr": "Avrupa'nın en iyi korunmuş Orta Çağ caddelerinden biridir. Yüzyıllar önce şövalyelerin konakladığı hanlarla çevrili bu taş döşeli sokak, sizi doğrudan 14. yüzyılın atmosferine götüren büyüleyici bir tünel gibidir.",
        "desc_en": "One of Europe's best-preserved medieval streets, this cobblestone road is lined with the 'inns' where knights once stayed. Walking here is like entering a time tunnel, leading straight into the heart of the 14th century."
    },
    "Kallithea Springs": {
        "desc_tr": "Art Deco mimarisi ve mozaik süslemeleriyle ünlü bu tarihi kaplıca, Rodos'un en şık noktalarından biridir. Kristal denizi ve romantik bahçeleriyle, hem tarih hem de güneşlenmek için eşsiz bir Ege deneyimi sunar.",
        "desc_en": "Famed for its Art Deco architecture and intricate pebble mosaics, Kallithea is one of Rhodes' most stylish seaside spots. With its crystal-clear bay and romantic gardens, it blends history and leisure in a perfect Aegean setting."
    }
}

# BUDAPESTE UPDATES
budapeste_updates = {
    "Hungarian Parliament Building": {
        "desc_tr": "Tuna kıyısında yükselen bu Gotik Revival şaheseri, kentin en ikonik yapısıdır. 691 odası ve devasa kubbesiyle dünyanın en büyük parlamento binalarından biri olan yapı, geceleri kentin üzerine altın bir taç gibi çöker.",
        "desc_en": "Rising from the banks of the Danube, this Gothic Revival masterpiece is the city's crown jewel. With its 691 rooms and dominant dome, it is one of the world's largest parliaments, shining like a golden crown over Budapest at night."
    },
    "Széchenyi Thermal Bath": {
        "desc_tr": "Avrupa'nın en büyük termal kompleksi olan Széchenyi, Neo-Barok mimarisiyle bir sarayda banyo yapma hissi verir. Buharlı açık hava havuzlarında satranç oynayan yaşlıları izlemek, Budapeşte'nin en otantik ve huzurlu deneyimidir.",
        "desc_en": "As Europe's largest thermal complex, Széchenyi's stunning Neo-Baroque architecture makes bathing feel like a royal experience. Watching locals play chess in the steaming outdoor pools is Budapest's most authentic and peaceful ritual."
    },
    "Matthias Church": {
        "desc_tr": "Balıkçı Kalesi'nin yanında yer alan bu renkli çatılı kilise, Gotik zarafetin zirvesidir. Osmanlı döneminde cami olarak da kullanılan yapı, bugün zengin süslemeleri ve tarihiyle Buda Tepesi'nin en fotografik noktasıdır.",
        "desc_en": "Located next to the Fisherman's Bastion, this church with its colorful tiled roof is a Gothic masterpiece. Having served as a mosque during Ottoman rule, it is now the most photogenic landmark on Castle Hill, full of rich legends."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Batch 4 Enrichment: Bari, Sardinya, Budva, Ksamil, Rhodes, Budapest...")
enrich_venues("bari", bari_updates)
enrich_venues("sardinya", sardinya_updates)
enrich_venues("budva", budva_updates)
enrich_venues("ksamil", ksamil_updates)
enrich_venues("rhodes", rhodes_updates)
enrich_venues("budapeste", budapeste_updates)
print("✨ Batch 4 Enrichment - Part 1 Complete.")
