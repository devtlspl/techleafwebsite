import re

css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Hide logo text in the footer
css_content += "\n.footer-brand .logo-text { display: none !important; }\n"

# Make the footer logo a bit larger since the text is gone
css_content += "\n.footer-brand .logo-mark { width: 160px !important; height: 70px !important; margin: 0 auto 15px 0 !important; }\n"

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated CSS to hide text in footer and enlarge the footer logo.")
