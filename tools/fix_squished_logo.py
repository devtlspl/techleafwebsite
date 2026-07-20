import urllib.request
import re

url = "https://techleafassets.blob.core.windows.net/assets/TechLeafLogoPNG.png"
logo_file = "assets/img/logo.png"

# 1. Download the un-squished logo directly
urllib.request.urlretrieve(url, logo_file)
print(f"Downloaded un-squished logo to {logo_file}")

# 2. Update styles.css to use logo.png instead of favicon.png for the header/footer
css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace the background image
css_content = css_content.replace("url('../img/favicon.png')", "url('../img/logo.png')")

# Update logo-mark width to accommodate the wide logo nicely next to the text
css_content = re.sub(
    r'\.logo-mark\s*\{[^}]+\}',
    '.logo-mark { width: 140px; height: 60px; background: transparent; display: block; padding: 0; min-width: 140px; margin-right: 15px; }',
    css_content
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated styles.css to use logo.png and fixed sizing.")
