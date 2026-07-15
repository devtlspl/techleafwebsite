import re

with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the desktop grid rows larger
# .hero-bento-16 { ... grid-template-rows: repeat(29, 25px); ... }
css = re.sub(r'grid-template-rows:\s*repeat\(29,\s*25px\);', 'grid-template-rows: repeat(29, 40px);', css)

# Make the mobile grid items larger
# .hero-bento-16 .bento-item { flex: 1 1 40%; height: 150px; }
css = re.sub(r'\.hero-bento-16 \.bento-item \{\s*flex: 1 1 40%;\s*height: 150px;\s*\}', '.hero-bento-16 .bento-item { flex: 1 1 40%; height: 280px; }', css)

with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS grid resized")
