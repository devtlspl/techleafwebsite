import re

css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# 1. Bring back the text (remove the display: none !important that I added)
css_content = css_content.replace('.logo-text { display: none !important; }', '')

# 2. Fix the logo mark width. 
# Previously it was 220px, which is too wide to fit NEXT to the text.
# Let's make it 120px wide by 60px high so it renders clearly without being squished, 
# while leaving plenty of room for the HTML text next to it.
css_content = re.sub(
    r'\.logo-mark\s*\{[^}]+\}',
    '.logo-mark { width: 120px; height: 60px; background: transparent; display: block; padding: 0; min-width: 120px; }',
    css_content
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("styles.css updated to restore text and fix image size.")
