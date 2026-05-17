import asyncio
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY_HERE")
API_URL = "https://api.openai.com/v1/chat/completions"

SOURCE_FILE = "/Users/anilebru/Desktop/Tum_Sehirler_Cok_Detayli_Liste.xlsx"
TARGET_FILE = "/Users/anilebru/Desktop/Yepyeni_Tum_Sehirler_Detayli_Liste.xlsx"

async def fetch_enrichment(session, idx, city, name, category, sem, retries=10):
    async with sem:
        for attempt in range(retries):
            try:
                prompt = f"""You are a local city expert outputting real facts for '{name}' located in '{city}' (Category: {category}).
Focus on what to eat/drink if it's a restaurant/bar (e.g. signature dish, unique atmosphere), or quick historical/cultural facts if it's an attraction/museum. Do NOT use generic fluff like "one of the best places" or "a must-visit". Try to include the exact year built, the chef's name, or a specific flavor.

Respond ONLY with valid JSON exactly in this format:
{{
  "desc_tr": "15-20 word rich Turkish description with highly specific facts.",
  "desc_en": "English translation of the 15-20 word description.",
  "tip_tr": "7-12 word realistic local tip in Turkish. (e.g. 'Reserve early for sunset views', 'Try the truffle risotto')",
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
                        # Rate limit hit, backoff heavily
                        await asyncio.sleep(5 + (2 ** attempt))
                    else:
                        text = await resp.text()
                        print(f"Error {resp.status} for {name}: {text}")
                        await asyncio.sleep(5)
            except Exception as e:
                print(f"Exception for {name}: {e}")
                await asyncio.sleep(5)
        print(f"Failed to fetch for {name} after {retries} retries.")
        return idx, None

async def main():
    print(f"Reading {SOURCE_FILE}...")
    
    # Load or resume
    if os.path.exists(TARGET_FILE):
        print(f"Resuming from {TARGET_FILE}...")
        df = pd.read_excel(TARGET_FILE)
    else:
        df = pd.read_excel(SOURCE_FILE)
        # Add a column to track completion so we can resume
        if "Enriched" not in df.columns:
            df["Enriched"] = False

    tasks = []
    # Concurrency of 10 keeps us at ~300-400 RPM, well within Tier 1 limits of 500 RPM.
    sem = asyncio.Semaphore(10) 
    
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for idx, row in df.iterrows():
            if row.get("Enriched") == True:
                continue # Skip already processed
                
            city = row.get("Şehir", "")
            name = row.get("Yer Adı (TR)", "")
            cat = row.get("Kategori", "")
            if not isinstance(name, str) or not name.strip():
                continue
            tasks.append(fetch_enrichment(session, idx, city, name, cat, sem))
            
        total_tasks = len(tasks)
        print(f"Starting {total_tasks} remaining enrichment tasks...")
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
    print("Done! File completely enriched.")

if __name__ == "__main__":
    asyncio.run(main())
