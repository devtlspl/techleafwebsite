import os
import re

page_map = [
    'laptop-rentals-chennai.html',
    'server-storage-rentals.html',
    'remote-dba-support.html',
    'network-design-implementation.html',
    'it-amc-fms-services.html',
    'it-hardware-consumables.html'
]

for html_file in page_map:
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find the injected image tag
        img_pattern = re.compile(r'(\s*<img src="assets/img/service-[a-z]+\.png"[^>]+>)\s*')
        img_match = img_pattern.search(content)

        if img_match:
            img_tag = img_match.group(1)
            # Remove the image from its current location
            content = content[:img_match.start()] + '\n' + content[img_match.end():]
            
            # Now find the first </p> after the col-lg-8 start
            # To be safe, we'll find col-lg-8, then find the first </p> after it
            col_idx = content.find('<div class="col-lg-8"')
            if col_idx != -1:
                p_end_idx = content.find('</p>', col_idx)
                if p_end_idx != -1:
                    p_end_idx += 4 # move past </p>
                    
                    # Also add a little margin to the top of the image so it doesn't touch the text
                    new_img_tag = img_tag.replace('margin-bottom: 2rem;', 'margin: 2.5rem 0;')
                    
                    content = content[:p_end_idx] + new_img_tag + content[p_end_idx:]
                    
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Moved image in {html_file}")
                else:
                    print(f"Could not find </p> in {html_file}")
            else:
                print(f"Could not find col-lg-8 in {html_file}")
        else:
            print(f"Could not find image tag in {html_file}")
    else:
        print(f"File not found: {html_file}")
