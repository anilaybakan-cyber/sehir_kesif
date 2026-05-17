# City Pipeline

This folder contains an automation pipeline that prepares new city content (places, routes, blogs, OTA assets) with the exact format used by the app.

```
tools/city_pipeline/
├── README.md
├── config/
│   └── cities.yml               # City definitions (id, radius, themes, etc.)
├── city_pipeline/
│   ├── __init__.py
│   ├── config_loader.py         # Loads and validates cities.yml
│   ├── google_places.py         # Fetches raw place data from Google Places API
│   ├── content_generator.py     # Enriches places with TR/EN descriptions via AI
│   ├── photo_pipeline.py        # Downloads Google photos, uploads to Firebase Storage
│   ├── city_json_builder.py     # Builds assets/cities/<city>.json
│   ├── route_builder.py         # Builds assets/routes/<city>_<theme>_<mode>.json via Directions API
│   ├── blog_builder.py          # Writes OTA blog JSON from markdown templates
│   ├── manifest_updater.py      # Updates cities_list.json + version_manifest.json (OTA)
│   └── utils.py                 # Shared helpers (logging, slugify, filesystem)
└── scripts/
    └── run_pipeline.py          # CLI entrypoint that orchestrates the steps
```

## Quick Start

1. Install dependencies:
   ```bash
   cd tools/city_pipeline
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Copy sample env and fill secrets:
   ```bash
   cp .env.sample .env
   # Fill GOOGLE_PLACES_API_KEY, GOOGLE_DIRECTIONS_API_KEY, FIREBASE_SERVICE_ACCOUNT, OPENAI_API_KEY (or Anthropic)
   ```

3. Define cities in `config/cities.yml`.

4. Run pipeline for a city:
   ```bash
   python scripts/run_pipeline.py --city bodrum --steps places,augment,photos,city_json,routes,blogs,manifest
   ```

The pipeline is modular—each step can re-run independently (results cached in `output/<city>/raw/*.json`).
