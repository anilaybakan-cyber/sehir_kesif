from enrich_venues import enrich_venues

# BATCH 4: BUDAPESTE FIX - PART 2
# (Correcting names to match JSON keys exactly)

budapeste_updates = {
    "Parlamento Binası": {
        "desc_tr": "Tuna kıyısında yükselen bu Gotik Revival şaheseri, kentin en ikonik yapısıdır. 691 odası ve devasa kubbesiyle dünyanın en büyük parlamento binalarından biri olan yapı, geceleri kentin üzerine altın bir taç gibi çöker.",
        "desc_en": "Rising from the banks of the Danube, this Gothic Revival masterpiece is the city's crown jewel. With its 691 rooms and dominant dome, it is one of the world's largest parliaments, shining like a golden crown over Budapest at night."
    },
    "Széchenyi Termal Hamamı": {
        "desc_tr": "Avrupa'nın en büyük termal kompleksi olan Széchenyi, Neo-Barok mimarisiyle bir sarayda banyo yapma hissi verir. Buharlı açık hava havuzlarında satranç oynayan yaşlıları izlemek, Budapeşte'nin en otantik ve huzurlu deneyimidir.",
        "desc_en": "As Europe's largest thermal complex, Széchenyi's stunning Neo-Baroque architecture makes bathing feel like a royal experience. Watching locals play chess in the steaming outdoor pools is Budapest's most authentic and peaceful ritual."
    },
    "Matthias Kilisesi": {
        "desc_tr": "Balıkçı Kalesi'nin yanında yer alan bu renkli çatılı kilise, Gotik zarafetin zirvesidir. Osmanlı döneminde cami olarak da kullanılan yapı, bugün zengin süslemeleri ve tarihiyle Buda Tepesi'nin en fotografik noktasıdır.",
        "desc_en": "Located next to the Fisherman's Bastion, this church with its colorful tiled roof is a Gothic masterpiece. Having served as a mosque during Ottoman rule, it is now the most photogenic landmark on Castle Hill, full of rich legends."
    }
}

# EXECUTE UPDATES
print("🚀 Fixing Batch 4 Enrichment: Budapeşte...")
enrich_venues("budapeste", budapeste_updates)
print("✨ Batch 4 Enrichment - Budapeşte Fix Complete.")
