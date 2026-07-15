import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add theme color and apple touch icon if not present
    if 'theme-color' not in content:
        insert_code = '  <meta name="theme-color" content="#1b5a3f" />\n  <link rel="apple-touch-icon" href="assets/img/favicon.png" />\n'
        content = content.replace('<head>', f'<head>\n{insert_code}', 1)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Mobile UI metadata injected.")
