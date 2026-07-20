import os
import glob
import re

# 1. Rename images
img_dir = 'assets/img'
patterns = {
    'service_rentals_*.png': 'service-rentals.png',
    'service_networking_*.png': 'service-networking.png',
    'service_repair_*.png': 'service-repair.png',
    'service_backup_*.png': 'service-backup.png',
    'service_consulting_*.png': 'service-consulting.png',
    'service_support_*.png': 'service-support.png'
}

for pattern, new_name in patterns.items():
    matches = glob.glob(os.path.join(img_dir, pattern))
    if matches:
        old_path = matches[0]
        new_path = os.path.join(img_dir, new_name)
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")

# 2. Inject images into HTML pages
page_map = {
    'laptop-rentals-chennai.html': 'service-rentals.png',
    'server-storage-rentals.html': 'service-backup.png',
    'remote-dba-support.html': 'service-consulting.png',
    'network-design-implementation.html': 'service-networking.png',
    'it-amc-fms-services.html': 'service-repair.png',
    'it-hardware-consumables.html': 'service-support.png'
}

for html_file, img_name in page_map.items():
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already injected
        if img_name in content:
            print(f"Image already in {html_file}")
            continue

        target_div = '<div class="col-lg-8" style="flex: 1; min-width: 300px;">'
        img_tag = f'\n        <img src="assets/img/{img_name}" alt="TechLeaf Service" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: var(--shadow-md); display: block;">'
        
        # Insert right after the target div
        if target_div in content:
            content = content.replace(target_div, target_div + img_tag, 1)
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {html_file}")
        else:
            print(f"Target div not found in {html_file}")
    else:
        print(f"File not found: {html_file}")
