import glob
import re

html_files = glob.glob('*.html')
replacements = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace "TECH Leaf Systems" (exact matches usually found in the header logo text)
    content = content.replace("TECH Leaf Systems", "TechLeaf Systems Private Limited")
    
    # Replace "TechLeaf Systems" but ONLY if it's not part of a URL (like techleafsystems.com) 
    # and not already followed by "Private Limited" or "private limited"
    # Negative lookahead for .com and Private Limited
    content = re.sub(r'TechLeaf Systems(?!\.com|\s+Private Limited|\s+private limited)', 'TechLeaf Systems Private Limited', content, flags=re.IGNORECASE)
    
    # Clean up any potential double "Private Limited"
    content = re.sub(r'Private Limited(?:\s+Private Limited)+', 'Private Limited', content, flags=re.IGNORECASE)

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        replacements += 1

print(f"Updated {replacements} HTML files with the new company name.")
