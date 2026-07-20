import os
import re
from PIL import Image
import urllib.parse

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the hero-bento-16 block
block_match = re.search(r'<div class="hero-bento-16">(.*?)</div>\s*<div class="hero-img-badge"', html, flags=re.DOTALL)
if not block_match:
    print("Could not find hero-bento-16 block")
    exit(1)

block = block_match.group(1)

# Find all src="path" inside the block
srcs = re.findall(r'src="([^"]+)"', block)

new_block = block
converted = 0

for src in srcs:
    if '-thumb.webp' in src:
        continue # already a thumb
        
    # url decode because of spaces like %20
    local_path = urllib.parse.unquote(src)
    
    if os.path.exists(local_path):
        try:
            img = Image.open(local_path)
            # max width 600px
            max_width = 600
            if img.width > max_width:
                wpercent = (max_width / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((max_width, hsize), Image.Resampling.LANCZOS)
            
            thumb_path = os.path.splitext(local_path)[0] + '-thumb.webp'
            img.save(thumb_path, 'webp', quality=80, optimize=True)
            
            # replace in HTML
            new_src = src.replace('.webp', '-thumb.webp')
            new_block = new_block.replace(f'src="{src}"', f'src="{new_src}"')
            
            converted += 1
            print(f"Created thumbnail for {src}")
        except Exception as e:
            print(f"Error processing {local_path}: {e}")
    else:
        print(f"File not found: {local_path}")

html = html.replace(block, new_block)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done! Created {converted} thumbnails and updated index.html.")
