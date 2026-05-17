import os
import subprocess
from pathlib import Path

scripts = [f for f in os.listdir('.') if f.startswith('generate_routes_') and f.endswith('.py')]
cities_dir = Path("assets/cities")

for script in scripts:
    city = script.replace('generate_routes_', '').replace('.py', '')
    # Special case for tropez -> saint_tropez
    city_filename = city
    if city == "tropez":
        city_filename = "saint_tropez"
    
    json_path = cities_dir / f"{city_filename}.json"
    draft_path = cities_dir / f"{city_filename}.json.draft"
    
    if not json_path.exists():
        print(f"⚠️  City file not found for {city}: {json_path}")
        continue
        
    # Create draft if missing
    if not draft_path.exists():
        print(f"📝 Creating draft for {city}...")
        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(draft_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    # Run script
    print(f"🚀 Running {script}...")
    res = subprocess.run(['python3', script], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"✅ {res.stdout.strip()}")
    else:
        print(f"❌ Error running {script}: {res.stderr}")
