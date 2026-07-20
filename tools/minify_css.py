import re

with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Simple minification
# Remove comments
css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
# Remove whitespace around structural characters
css = re.sub(r'\s*([\{\}\:\;\,])\s*', r'\1', css)
# Remove newlines
css = css.replace('\n', '')

with open('assets/css/styles.min.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Minified styles.css to styles.min.css")
