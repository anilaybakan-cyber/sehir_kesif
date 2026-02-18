
import os
import shutil

SOURCE_DIR = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
TARGET_DIR = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack/cities"

def main():
    if not os.path.exists(TARGET_DIR):
        print(f"Creating target directory: {TARGET_DIR}")
        os.makedirs(TARGET_DIR)

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.json')]
    print(f"Syncing {len(files)} city files to ota_data_pack...")

    for filename in files:
        source_path = os.path.join(SOURCE_DIR, filename)
        target_path = os.path.join(TARGET_DIR, filename)
        
        # We always copy to ensure ota_data_pack is up to date
        shutil.copy2(source_path, target_path)
        # print(f"Synced {filename}")

    print("Sync complete.")

if __name__ == "__main__":
    main()
