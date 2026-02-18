
import subprocess
import os
import re

REPO_PATH = '/Users/anilebru/Desktop/Uygulamalar/myway-data'
MANIFEST_PATH = os.path.join(REPO_PATH, 'version_manifest.json')

def run_git_cmd(args):
    result = subprocess.run(
        ['git'] + args,
        cwd=REPO_PATH,
        capture_output=True,
        text=True,
        check=False
    )
    return result

def solve_conflict():
    print("⚠️ Attempting to resolve content conflict in version_manifest.json...")
    
    try:
        with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simple conflict solver: take the remote content but update 'prag' version manually to 11
        # Conflicts look like <<<<<<< HEAD ... ======= ... >>>>>>>
        
        # Actually, let's just make sure it's valid JSON with prag: 11. 
        # But parsing conflict markers as JSON is impossible.
        # We'll try to checkout 'theirs' (remote), then apply our prag update.
        
        run_git_cmd(['checkout', '--theirs', 'version_manifest.json'])
        run_git_cmd(['add', 'version_manifest.json'])
        
        # Now read it and force prag: 11
        import json
        with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        data['prag'] = 11
        data['updateNotes'] = "Updated Prague with new venues via Routes OTA"
        
        # Add routes version bump
        if 'routes' not in data:
            data['routes'] = {}
        
        current_route_ver = data['routes'].get('prag', 0)
        data['routes']['prag'] = current_route_ver + 1
        print(f"✅ Bumped Prague ROUTE version to {current_route_ver + 1}")

        # Add guides version bump
        if 'guides' not in data:
            data['guides'] = {}
        
        data['guides']['prag'] = 2
        print(f"✅ Forced Prague GUIDE version to 2")
        
        with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        run_git_cmd(['add', 'version_manifest.json'])
        print("✅ Resolved conflict by forcing prag: 11 on top of remote.")
        return True
        
    except Exception as e:
        print(f"❌ Failed to resolve conflict: {e}")
        return False

def main():
    if not os.path.exists(REPO_PATH):
        print(f"Repo path not found: {REPO_PATH}")
        return

    print(f"🔄 Starting deployment in {REPO_PATH}...")

    # 0. Commit local changes first
    print("--- Staging and Committing changes ---")
    run_git_cmd(['add', '.'])
    run_git_cmd(['commit', '-m', "feat: Update Prague Guide v2 (Text OTA)"])

    # 1. Abort any pending rebase from previous attempt
    run_git_cmd(['rebase', '--abort'])
    
    # 2. Pull with merge (not rebase) to allow conflict handling
    print("\n--- Pulling changes (Merge strategy) ---")
    res = run_git_cmd(['pull', '--no-rebase'])
    
    if res.returncode != 0:
        print("⚠️ Git pull halted. Checking for conflicts...")
        if "CONFLICT" in res.stdout or "CONFLICT" in res.stderr:
            if solve_conflict():
                # Commit the resolution
                run_git_cmd(['commit', '--no-edit'])
            else:
                print("❌ Could not resolve conflicts automatically.")
                return
        else:
            print(f"❌ Git pull failed with unknown error:\n{res.stderr}")
            return

    # 3. Push changes
    print("\n--- Pushing changes ---")
    res = run_git_cmd(['push'])
    
    if res.returncode == 0:
        print("\n✅ Successfully pushed changes to GitHub!")
    else:
        print(f"\n❌ Git push failed:\n{res.stderr}")

if __name__ == "__main__":
    main()
