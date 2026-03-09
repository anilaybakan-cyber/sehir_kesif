import asyncio
import aiohttp
import pandas as pd
import json
import os
import random

API_KEY = "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"
API_URL = "https://api.openai.com/v1/chat/completions"

SOURCE_FILE = "/Users/anilebru/Desktop/Tum_Sehirler_Cok_Detayli_Liste.xlsx"
TARGET_FILE = "/Users/anilebru/Desktop/Yepyeni_Tum_Sehirler_Detayli_Liste_V2.xlsx"

STYLES = [
    "Focus primarily on the atmospheric feeling, the unique visual aspects, and the local vibe. Make it sound poetic but factual.",
    "Start by highlighting an interesting historical trivia, legend, or cultural significance without leading with a boring date.",
    "Describe the energetic mood, the types of locals who go there, and what makes it feel alive.",
    "If it's food/drink, talk about the exact flavor profile, ingredients, or preparation of their signature dish. If it's a sight, focus on the sounds, textures, and first impressions.",
    "Focus on the architecture, design, or natural beauty, describing specific colors, materials, or breathtaking viewpoints.",
    "Write a short, engaging description that focuses on why an insider would secretly love this specific place, avoiding cliché tourist words.",
    "Emphasize the unique contrast of the place—like modern vs old, quiet vs chaotic, or sweet vs savory.",
    "Frame the description entirely around the specific sensory details (the smell of coffee, the echo of footsteps, the chill of the breeze)."
]

async def fetch_enrichment(session, idx, city, name, category, sem, retries=10):
    async with sem:
        for attempt in range(retries):
            try:
                style = random.choice(STYLES)
                prompt = f"""You are a master local travel writer creating real, specific content for '{name}' located in '{city}' (Category: {category}).

YOUR STYLE INSTRUCTION FOR THIS ONE: {style}

CRITICAL RULES:
1. NEVER start the sentence with a date (e.g., DO NOT SAY "Built in 1898...").
2. DO NOT use generic filler words like "one of the best", "must-visit", "amazing", or "unforgettable".
3. Provide objective, highly specific facts woven into an engaging, varying sentence structure. 
4. Ensure the descriptions feel completely different in grammar and flow from other typical encyclopedia entries.

Respond ONLY with valid JSON exactly in this format:
{{
  "desc_tr": "15-30 word rich, vibrant Turkish description strictly following the rules above. Feel free to be descriptive.",
  "desc_en": "English translation of the 15-30 word description.",
  "tip_tr": "7-12 word realistic and highly specific local tip in Turkish. (e.g. 'Sip the lavender latte by the window', 'Go at 4 PM to avoid the shadow')",
  "tip_en": "English translation of the local tip."
}}"""
                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "gpt-4o-mini",
                    "messages": [{"role": "user", "content": prompt}],
                    "response_format": { "type": "json_object" }
                }
                
                async with session.post(API_URL, headers=headers, json=payload) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        content = data['choices'][0]['message']['content']
                        parsed = json.loads(content)
                        return idx, parsed
                    elif resp.status == 429:
                        resp_json = await resp.json()
                        error_msg = resp_json.get("error", {}).get("message", "429 Rate Limit")
                        if "quota" in error_msg.lower():
                            print(f"QUOTA EXCEEDED! Stopping attempt for {name}.")
                            return idx, None
                        
                        sleep_time = min(30, 5 + (2 ** attempt))
                        await asyncio.sleep(sleep_time)
                    else:
                        text = await resp.text()
                        print(f"Error {resp.status} for {name}: {text}")
                        await asyncio.sleep(10)
            except Exception as e:
                print(f"Exception for {name}: {e}")
                await asyncio.sleep(5)
        print(f"Failed to fetch for {name} after {retries} retries.")
        return idx, None

async def main():
    print(f"Reading {SOURCE_FILE}...")
    
    if os.path.exists(TARGET_FILE):
        print(f"Resuming from {TARGET_FILE}...")
        df = pd.read_excel(TARGET_FILE)
    else:
        df = pd.read_excel(SOURCE_FILE)
        if "Enriched" not in df.columns:
            df["Enriched"] = False

    tasks = []
    sem = asyncio.Semaphore(15) 
    
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for idx, row in df.iterrows():
            if row.get("Enriched") == True:
                continue 
                
            city = row.get("Şehir", "")
            name = row.get("Yer Adı (TR)", "")
            cat = row.get("Kategori", "")
            if not isinstance(name, str) or not name.strip():
                continue
            tasks.append(fetch_enrichment(session, idx, city, name, cat, sem))
            
        total_tasks = len(tasks)
        print(f"Starting {total_tasks} remaining enrichment tasks for V2...")
        if total_tasks == 0:
            print("Everything is completed!")
            return

        completed = 0
        for f in asyncio.as_completed(tasks):
            idx, res = await f
            completed += 1
            if res:
                df.at[idx, "Açıklama (TR)"] = res.get("desc_tr", df.at[idx, "Açıklama (TR)"])
                df.at[idx, "Açıklama (EN)"] = res.get("desc_en", df.at[idx, "Açıklama (EN)"])
                df.at[idx, "Yerel İpucu (TR)"] = res.get("tip_tr", df.at[idx, "Yerel İpucu (TR)"])
                df.at[idx, "Yerel İpucu (EN)"] = res.get("tip_en", df.at[idx, "Yerel İpucu (EN)"])
                df.at[idx, "Enriched"] = True
            
            if completed % 10 == 0:
                print(f"Completed {completed}/{total_tasks} ({(completed/total_tasks)*100:.2f}%)")
                
            if completed % 100 == 0:
                print(f"Saving checkpoint at {completed}...")
                df.to_excel(TARGET_FILE, index=False)
                
    print("Saving final Excel file...")
    df.to_excel(TARGET_FILE, index=False)
    print("Done! File completely enriched with V2 Prompts.")

if __name__ == "__main__":
    asyncio.run(main())
