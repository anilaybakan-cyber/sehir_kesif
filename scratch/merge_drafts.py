import shutil
from pathlib import Path

cities_dir = Path("assets/cities")
drafts = list(cities_dir.glob("*.json.draft"))

for draft in drafts:
    main_file = draft.parent / draft.stem # stem of .json.draft is city.json
    print(f"Merging {draft.name} -> {main_file.name}")
    shutil.copy2(draft, main_file)
    # Optional: remove draft after merge
    # draft.unlink()
