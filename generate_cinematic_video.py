
import os
import random
import PIL.Image

# Monkey patch for Pillow 10+ where ANTIALIAS was removed
if not hasattr(PIL.Image, 'ANTIALIAS'):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

from moviepy.editor import ImageClip, concatenate_videoclips, vfx, CompositeVideoClip
from moviepy.video.fx.all import crop, resize

# Configuration
# App Store Portrait Resolution: 886 x 1920 (approx 9:16 for consistency)
TARGET_WIDTH = 886
TARGET_HEIGHT = 1920
RESOLUTION = (TARGET_WIDTH, TARGET_HEIGHT)

DURATION_PER_CLIP = 4.0  # Seconds per city
TRANSITION_DURATION = 0.8 # Generic crossfade

# Paths
ASSETS_DIR = 'assets/badges' # Using your badge images as source
OUTPUT_FILE = 'app_store_preview_vertical.mp4'

def get_image_files(directory):
    """Returns a list of image paths from the directory, excluding system badges."""
    valid_extensions = ('.png', '.jpg', '.jpeg')
    return [os.path.join(directory, f) for f in os.listdir(directory) 
            if f.lower().endswith(valid_extensions) 
            and not f.startswith('.') 
            and not f.startswith('badge_')] # Exclude badge_first_visit etc.

def create_cinematic_clip(image_path, duration):
    """
    Creates a detailed vertical video clip from an image with Ken Burns effect.
    """
    # Load image
    img = ImageClip(image_path)
    
    # ROBUST KEN BURNS: PAN SCAN VIA COMPOSITE
    # This method creates a larger clip and moves it across the screen window.
    # It avoids complex crop lambda errors.
    
    # 1. Resize image to be larger than target resolution
    # Let's make it cover the screen + 15% extra for panning room
    
    # Calculate scale needed to cover screen fully
    scale_w = (TARGET_WIDTH * 1.15) / img.w 
    scale_h = (TARGET_HEIGHT * 1.15) / img.h
    scale = max(scale_w, scale_h) 
    
    # Create the large moving clip
    moving_clip = img.resize(scale * 1.2) # Make it big enough
    cw, ch = moving_clip.size
    
    # Define start and end positions (Top Left coordinates)
    # We want to center the movement roughly
    
    # Center of image aligns with center of screen:
    # x = (TARGET_WIDTH - cw) / 2
    # y = (TARGET_HEIGHT - ch) / 2
    
    center_x = (TARGET_WIDTH - cw) / 2
    center_y = (TARGET_HEIGHT - ch) / 2
    
    # Random movement offset
    pan_x = random.choice([-80, 80, -50, 50])
    pan_y = random.choice([-80, 80, -50, 50])
    
    start_pos_x = center_x - (pan_x / 2)
    start_pos_y = center_y - (pan_y / 2)
    
    end_pos_x = center_x + (pan_x / 2)
    end_pos_y = center_y + (pan_y / 2)
    
    # Position function: (x(t), y(t))
    pos_func = lambda t: (
        start_pos_x + (end_pos_x - start_pos_x) * (t / duration),
        start_pos_y + (end_pos_y - start_pos_y) * (t / duration)
    )
    
    moving_clip = moving_clip.set_position(pos_func).set_duration(duration)
    
    # Composite it into a fixed resolution window
    # We use a dummy clip to set the size, or just pass size to CompositeVideoClip
    
    final_clip = CompositeVideoClip([moving_clip], size=RESOLUTION)
    final_clip = final_clip.set_duration(duration)
    
    return final_clip

def main():
    print("🎬 Initializing Cinematic Video Generator...")
    
    images = get_image_files(ASSETS_DIR)
    
    if not images:
        print(f"❌ No images found in {ASSETS_DIR}")
        return

    print(f"📸 Found {len(images)} images. Selecting random 6 for preview.")
    selected_images = random.sample(images, min(6, len(images)))
    
    clips = []
    
    for idx, img_path in enumerate(selected_images):
        print(f"   Processing clip {idx+1}: {os.path.basename(img_path)}")
        try:
            clip = create_cinematic_clip(img_path, DURATION_PER_CLIP)
            
            # Fade in/out logic
            # Use crossfadein for all except first?
            # clips logic in concatenate with method='compose' handles overlaps
            
            clip = clip.crossfadein(TRANSITION_DURATION)
            clips.append(clip)
        except Exception as e:
            print(f"   ⚠️ Error processing {img_path}: {e}")

    if not clips:
        print("❌ No clips created.")
        return

    print("🎞️  Concatenating clips with transitions...")
    # padding=-TRANSITION_DURATION makes them overlap for the crossfade
    final_video = concatenate_videoclips(clips, method="compose", padding=-TRANSITION_DURATION)
    
    print(f"💾 Render started: {OUTPUT_FILE}")
    # Low preset for faster preview generation during this chat
    final_video.write_videofile(OUTPUT_FILE, fps=24, codec='libx264', preset='medium', audio=False)
    print("✅ Video generation complete!")

if __name__ == "__main__":
    main()
