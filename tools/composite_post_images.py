from PIL import Image
import os

# Paths to the generated backgrounds and the logo
bg1_path = r"C:\Users\DELL\.gemini\antigravity\brain\30d0c7bb-5a0a-4ece-9fba-724d64719881\launch_bg_1_1784118723602.png"
bg2_path = r"C:\Users\DELL\.gemini\antigravity\brain\30d0c7bb-5a0a-4ece-9fba-724d64719881\launch_bg_2_1784118735315.png"
logo_path = r"assets\img\logo_cropped.png"
out1_path = r"C:\Users\DELL\.gemini\antigravity\brain\30d0c7bb-5a0a-4ece-9fba-724d64719881\final_post_image_1.png"
out2_path = r"C:\Users\DELL\.gemini\antigravity\brain\30d0c7bb-5a0a-4ece-9fba-724d64719881\final_post_image_2.png"

# Load the logo
logo = Image.open(logo_path).convert("RGBA")

def composite_image(bg_path, out_path, logo_scale=0.6, y_offset=0):
    bg = Image.open(bg_path).convert("RGBA")
    
    # Calculate target width for logo (e.g., 60% of background width)
    target_logo_width = int(bg.width * logo_scale)
    logo_aspect = logo.width / logo.height
    target_logo_height = int(target_logo_width / logo_aspect)
    
    logo_resized = logo.resize((target_logo_width, target_logo_height), Image.Resampling.LANCZOS)
    
    # Calculate position to center the logo
    x = (bg.width - target_logo_width) // 2
    y = (bg.height - target_logo_height) // 2 + y_offset
    
    # Create a copy of bg to paste onto
    combined = bg.copy()
    combined.paste(logo_resized, (x, y), mask=logo_resized)
    
    # Save as PNG
    combined.save(out_path, format="PNG")
    print(f"Saved {out_path}")

# Composite first image (centered)
composite_image(bg1_path, out1_path, logo_scale=0.55, y_offset=0)

# Composite second image (slightly higher up)
composite_image(bg2_path, out2_path, logo_scale=0.55, y_offset=-50)
