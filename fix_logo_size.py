import re

css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Make the logo container rectangular so the image doesn't get squished
css_content = re.sub(
    r'\.logo-mark\s*\{[^}]+\}',
    '.logo-mark { width: 220px; height: 65px; background: transparent; display: block; padding: 0; min-width: 220px; }',
    css_content
)

# The image is background-size: contain, so it will fill the 220x65 box perfectly.
# Hide the HTML text so it doesn't duplicate the text inside the image.
if '.logo-text { display: none !important; }' not in css_content:
    css_content += '\n.logo-text { display: none !important; }\n'

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("styles.css updated for rectangular logo.")
