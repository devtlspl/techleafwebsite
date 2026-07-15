import re

css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace logo.png with logo_cropped.png
css_content = css_content.replace("url('../img/logo.png')", "url('../img/logo_cropped.png')")

# The cropped logo is wider than tall, let's adjust width to 110px and height to 60px
# The aspect ratio is approx 2:1 or so.
css_content = re.sub(
    r'\.logo-mark\s*\{[^}]+\}',
    '.logo-mark { width: 110px; height: 50px; background: transparent; display: block; padding: 0; min-width: 110px; margin-right: 15px; }',
    css_content
)

# For the footer, let's add a filter to make the logo white so it's visible on the dark background
# We can add a class or selector for the footer logo
css_content += "\n.footer-brand .logo-mark::before { filter: brightness(0) invert(1); }\n"

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated CSS to use cropped logo.")
