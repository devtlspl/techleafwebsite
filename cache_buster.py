import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace any styles.min.css and styles.min.css?v=XX with styles.min.css?v=39
    content = re.sub(r'styles\.min\.css(?:\?v=\d+)?', 'styles.min.css?v=39', content)
    
    # Replace any main.min.js and main.min.js?v=XX with main.min.js?v=39
    content = re.sub(r'main\.min\.js(?:\?v=\d+)?', 'main.min.js?v=39', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cache busters updated globally.")
