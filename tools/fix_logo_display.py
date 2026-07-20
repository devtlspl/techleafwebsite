import glob
import re

# 1. Update HTML files to add a space and fix the wrapping
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the missing space that caused "SystemsPrivate"
    content = content.replace(
        '<div class="logo-name">TechLeaf Systems<span class="pvt-ltd">Private Limited</span></div>',
        '<div class="logo-name">TechLeaf Systems <span class="pvt-ltd">Private Limited</span></div>'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update CSS to fix the missing logo image and ensure the block formatting works
css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace the missing 'Real tech.png' with the new transparent logo (favicon.png)
css_content = re.sub(
    r"background-image:\s*url\('[^']+'\);",
    "background-image: url('../../assets/img/favicon.png');",
    css_content
)

# Ensure pvt-ltd is properly blocked
if 'display: block;' not in css_content.split('.pvt-ltd')[1][:50]:
    css_content = css_content.replace('.pvt-ltd {', '.pvt-ltd { display: block !important;')

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("HTML and CSS fixed.")
