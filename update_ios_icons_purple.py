import os
import json
from PIL import Image, ImageOps

# Configuration
CONFIG = {
    "source_logo": "assets/images/splash_logo.png",
    "target_dir": "ios/Runner/Assets.xcassets/AppIcon.appiconset",
    "bg_color": "#8C88F5",
    "logo_padding_ratio": 0.15,  # 15% padding on each side (logo occupies 70% width)
}

def create_master_icon(source_path, size=1024):
    """Creates the master 1024x1024 icon with purple background and centered logo."""
    # Create base image
    master = Image.new("RGBA", (size, size), CONFIG["bg_color"])
    
    # Load and resize logo
    try:
        logo = Image.open(source_path).convert("RGBA")
    except FileNotFoundError:
        print(f"Error: Source logo not found at {source_path}")
        return None

    # Calculate logo size maintaining aspect ratio
    target_width = int(size * (1 - CONFIG["logo_padding_ratio"] * 2))
    aspect_ratio = logo.height / logo.width
    target_height = int(target_width * aspect_ratio)

    logo_resized = logo.resize((target_width, target_height), Image.Resampling.LANCZOS)

    # Center placement
    x = (size - target_width) // 2
    y = (size - target_height) // 2

    # Paste logo onto background (using logo as mask for transparency)
    master.paste(logo_resized, (x, y), logo_resized)
    return master

def main():
    # Verify paths
    current_dir = os.getcwd()
    source_path = os.path.join(current_dir, CONFIG["source_logo"])
    target_dir = os.path.join(current_dir, CONFIG["target_dir"])
    contents_json_path = os.path.join(target_dir, "Contents.json")

    print(f"Source: {source_path}")
    print(f"Target: {target_dir}")

    # Generate master icon
    print("Generating master icon...")
    master_icon = create_master_icon(source_path)
    if not master_icon:
        return

    # Read Contents.json to get required sizes
    try:
        with open(contents_json_path, 'r') as f:
            contents = json.load(f)
    except FileNotFoundError:
        print(f"Error: Contents.json not found at {contents_json_path}")
        return

    # Process each image entry
    print("Processing icon sizes...")
    for entry in contents["images"]:
        filename = entry["filename"]
        size_str = entry["size"]
        scale_str = entry["scale"]

        # Parse size (e.g., "20x20")
        width, height = map(float, size_str.split('x'))
        
        # Parse scale (e.g., "2x", "3x")
        scale = float(scale_str.replace('x', ''))

        # Calculate final pixel dimensions
        final_width = int(width * scale)
        final_height = int(height * scale)

        print(f"  Generating {filename} ({final_width}x{final_height})...")

        # Resize master icon
        resized_icon = master_icon.resize((final_width, final_height), Image.Resampling.LANCZOS)
        
        # Save to file (no alpha channel needed for iOS icons usually, but kept for safety if needed)
        # iOS icons officially shouldn't have transparency, so we can convert to RGB
        resized_icon_rgb = resized_icon.convert("RGB")
        save_path = os.path.join(target_dir, filename)
        resized_icon_rgb.save(save_path)

    print("Success! All iOS icons updated independently.")

if __name__ == "__main__":
    main()
