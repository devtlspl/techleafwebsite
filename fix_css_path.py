import re

css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Fix the broken path!
css_content = css_content.replace(
    "background-image: url('../../assets/img/favicon.png');",
    "background-image: url('../img/favicon.png');"
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("styles.css path fixed.")
