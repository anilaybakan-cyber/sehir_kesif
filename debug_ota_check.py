
import requests
import json

URL_IN_CODE = 'https://raw.githubusercontent.com/anilaybakan-cyber/myway-data/refs/heads/main/version_manifest.json'
STANDARD_URL = 'https://raw.githubusercontent.com/anilaybakan-cyber/myway-data/main/version_manifest.json'

def check_url(url, label):
    print(f"Checking {label}: {url}")
    try:
        res = requests.get(url)
        print(f"  Status: {res.status_code}")
        if res.status_code == 200:
            try:
                data = res.json()
                print(f"  Content (Prag Version): {data.get('prag')}")
                return True
            except:
                print("  ❌ Invalid JSON content")
        else:
            print("  ❌ Response not OK")
    except Exception as e:
        print(f"  ❌ Request failed: {e}")
    return False

print("--- OTA Debug ---")
code_ok = check_url(URL_IN_CODE, "URL in Code (refs/heads/)")
std_ok = check_url(STANDARD_URL, "Standard URL (main/)")

if code_ok:
    print("\n✅ The URL in the code works and returns the correct version.")
else:
    print("\n⚠️ The URL in the code FAILS. This is likely the issue.")
