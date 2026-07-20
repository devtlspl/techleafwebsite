from PIL import Image

# Paths
bg1_path = r"C:\Users\DELL\.gemini\antigravity\brain\30d0c7bb-5a0a-4ece-9fba-724d64719881\simple_sketch_1_1784118980877.png"
bg2_path = r"C:\Users\DELL\.gemini\antigravity\brain\30d0c7bb-5a0a-4ece-9fba-724d64719881\simple_sketch_2_1784118990829.png"
logo_path = r"assets\img\logo_cropped.png"
out1_path = r"C:\Users\DELL\.gemini\antigravity\brain\30d0c7bb-5a0a-4ece-9fba-724d64719881\mini_logo_post_1.png"
out2_path = r"C:\Users\DELL\.gemini\antigravity\brain\30d0c7bb-5a0a-4ece-9fba-724d64719881\mini_logo_post_2.png"

logo = Image.open(logo_path).convert("RGBA")

def composite_mini_logo(bg_path, out_path):
    bg = Image.open(bg_path).convert("RGBA")
    
    # Make the logo much smaller! E.g. 25% of the background width
    target_logo_width = int(bg.width * 0.25)
    logo_aspect = logo.width / logo.height
    target_logo_height = int(target_logo_width / logo_aspect)
    
    logo_resized = logo.resize((target_logo_width, target_logo_height), Image.Resampling.LANCZOS)
    
    # Position: Centered horizontally, at the top (with a small margin)
    x = (bg.width - target_logo_width) // 2
    y = int(bg.height * 0.05) # 5% from the top
    
    combined = bg.copy()
    combined.paste(logo_resized, (x, y), mask=logo_resized)
    combined.save(out_path, format="PNG")
    print(f"Saved {out_path}")

composite_mini_logo(bg1_path, out1_path)
composite_mini_logo(bg2_path, out2_path)
