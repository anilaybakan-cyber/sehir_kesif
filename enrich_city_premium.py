import json
import os
import sys
from openai import OpenAI

# Mocking the AI call since the model handles text generation
# In a real script, this would call the API. Here I will use the model to generate the batch.

def enrich_city(city_file):
    with open(city_file, "r") as f:
        data = json.load(f)
    
    print(f"Enriching {city_file}...")
    # Logic to identify dirty venues and output them for the model to process
    dirty = []
    for h in data.get("highlights", []):
        desc = h.get("description_en", "")
        if "top spot" in desc.lower() or "worth visiting" in desc.lower() or len(desc.split()) < 20:
            dirty.append(h)
            
    print(f"Found {len(dirty)} dirty venues in {city_file}")
    # The actual generation will be done by the model in the next step
    return dirty

if __name__ == "__main__":
    enrich_city(sys.argv[1])
