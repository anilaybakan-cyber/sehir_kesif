import asyncio
import aiohttp
import pandas as pd
import json
import os

GEMINI_API_KEY = "AIzaSyAQfHjXTs1B1I8M-2C2wEaD4iF_GWkP2ME"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

SOURCE_FILE = "/Users/anilebru/Desktop/Yepyeni_Tum_Sehirler_Detayli_Liste_V2.xlsx"
TARGET_FILE = "/Users/anilebru/Desktop/Yepyeni_Tum_Sehirler_Detayli_Liste_V3.xlsx"

TARGET_CATEGORIES = ["Tarihi", "Müze", "Deneyim"]

async def fetch_enrichment(session, idx, city, name, category, sem, retries=10):
    async with sem:
        for attempt in range(retries):
            try:
                # The user explicitly asked to change the tone to be very informative, historical, structural.
                # Example given for Park Guell: "Gaudí'nin doğadan ilham alan mozaikleri, kertenkele heykeli ve Barselona manzaralı ikonik terasıyla dünyaca ünlü, masalsı ve büyüleyici bir sanat parkıdır."
                
                prompt = f"""You are a master historian and architectural guide creating premium content for '{name}' located in '{city}' (Category: {category}).

CRITICAL INSTRUCTIONS:
1. The description MUST be exactly between 20 to 25 words. No less, no more.
2. Focus entirely on the historical facts, architectural brilliance, what it houses, and its significance.
3. Be EXTREMELY informative and impressive so the user knows exactly what they will see.
4. Examples of the tone:
   - "Etnografik eserler ve dünya kültürlerine odaklanan sergileriyle bilinen, etkileyici mimariye sahip devasa bir dünya müzesidir."
   - "Gaudí'nin doğadan ilham alan mozaikleri, kertenkele heykeli ve Barselona manzaralı ikonik terasıyla dünyaca ünlü, masalsı ve büyüleyici bir sanat parkıdır."
5. Do NOT just say "it is a historical place". Give the specific facts (who built it, what is inside, architectural style).

Respond ONLY with valid JSON exactly in this format:
{{
  "desc_tr": "20-25 word highly detailed, historically profound Turkish description.",
  "desc_en": "English translation of the 20-25 word description.",
  "tip_tr": "7-12 word realistic local tip in Turkish.",
  "tip_en": "English translation of the local tip."
}}"""
                headers = {
                    "Content-Type": "application/json"
                }
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }],
                    "generationConfig": {
                        "responseMimeType": "application/json"
                    }
                }
                
                async with session.post(API_URL, headers=headers, json=payload) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        content = data['candidates'][0]['content']['parts'][0]['text']
                        parsed = json.loads(content)
                        return idx, parsed
                    elif resp.status == 429:
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
    print(f"Reading source file...")
    
    if os.path.exists(TARGET_FILE):
        print(f"Resuming from {TARGET_FILE}...")
        df = pd.read_excel(TARGET_FILE)
    else:
        df = pd.read_excel(SOURCE_FILE)
        df["V4_Enriched"] = False

    tasks = []
    sem = asyncio.Semaphore(10) 
    
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for idx, row in df.iterrows():
            if row.get("V4_Enriched") == True:
                continue 
                
            cat = row.get("Kategori", "")
            if cat not in TARGET_CATEGORIES:
                # Mark as enriched implicitly so we don't process it, we only care about Tarihi, Müze, Deneyim
                df.at[idx, "V4_Enriched"] = True
                continue
                
            city = row.get("Şehir", "")
            name = row.get("Yer Adı (TR)", "")
            
            if not isinstance(name, str) or not name.strip():
                continue
            tasks.append(fetch_enrichment(session, idx, city, name, cat, sem))
            
        total_tasks = len(tasks)
        print(f"Starting {total_tasks} remaining enrichment tasks for V4 (Gemini Historical)...")
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
                df.at[idx, "V4_Enriched"] = True
            
            if completed % 10 == 0:
                print(f"Completed {completed}/{total_tasks} ({(completed/total_tasks)*100:.2f}%)")
                
            if completed % 50 == 0:
                print(f"Saving checkpoint at {completed}...")
                df.to_excel(TARGET_FILE, index=False)
                
    print("Saving final Excel file...")
    df.to_excel(TARGET_FILE, index=False)
    print("Done! File completely enriched with V4 Historical Prompts.")

if __name__ == "__main__":
    asyncio.run(main())
