import os
import glob
import re
from PIL import Image

# 1. Generate images
try:
    # Social Preview
    if os.path.exists('assets/img/fisrt it company.webp'):
        img = Image.open('assets/img/fisrt it company.webp').convert('RGB')
        img.save('assets/img/social-preview.jpg', 'JPEG', quality=85)
        print("Generated social-preview.jpg")
    else:
        print("Could not find social preview source image")

    # Favicons
    if os.path.exists('assets/img/logo.webp'):
        logo = Image.open('assets/img/logo.webp')
        # Generate PNG
        logo_png = logo.resize((512, 512), Image.Resampling.LANCZOS)
        logo_png.save('assets/img/favicon.png', 'PNG')
        print("Generated favicon.png")
        
        # Generate ICO
        logo_ico = logo.resize((32, 32), Image.Resampling.LANCZOS)
        logo_ico.save('favicon.ico', format='ICO')
        print("Generated favicon.ico")
    else:
        print("Could not find logo.webp")
except Exception as e:
    print(f"Error generating images: {e}")

# 2. Update all HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update social tags
    content = re.sub(r'content="[^"]*\.webp"', lambda m: m.group(0).replace('.webp', '.jpg').replace('fisrt%20it%20company', 'social-preview').replace('team-collage', 'social-preview'), content)
    
    # Update favicon
    # <link rel="icon" type="image/png" href="assets/img/logo.webp" />
    content = re.sub(r'<link rel="icon"[^>]+href="[^"]+"[^>]*>', '<link rel="icon" type="image/png" href="assets/img/favicon.png" />\n  <link rel="icon" type="image/x-icon" href="favicon.ico" />', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML files updated with proper meta tags and favicons.")
