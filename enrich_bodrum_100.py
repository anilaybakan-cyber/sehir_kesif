from enrich_venues import enrich_venues

# FINAL SWEEP: BODRUM 100%

bodrum_last_fix = {
    "Yalcin Sivrikaya plaji": {
        "desc_tr": "Yalıkavak'ın doğal kalmış sahil şeridinde yer alan bu plaj, kentsel karmaşadan uzaklaşmak isteyenler için huzurlu bir duraktır. Turkuaz denizi ve sakin atmosferiyle, Bodrum'un yerel ve bakir dokusunu en iyi yansıtan gizli köşelerindendir.",
        "desc_en": "Located along Yalıkavak's naturally preserved coastline, this beach is a peaceful retreat for those looking to escape the urban rush. With its turquoise sea and quiet vibe, it is one of the hidden gems reflecting Bodrum's authentic and untouched fabric."
    }
}

enrich_venues("bodrum", bodrum_last_fix)
print("✅ Bodrum is now 100% complete.")
