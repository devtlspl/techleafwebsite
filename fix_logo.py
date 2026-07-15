import glob

# 1. Update HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(
        '<div class="logo-name">TechLeaf Systems Private Limited</div>',
        '<div class="logo-name">TechLeaf Systems<span class="pvt-ltd">Private Limited</span></div>'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update CSS
css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

pvt_ltd_css = """
.pvt-ltd { 
    display: block; 
    font-size: 0.55em; 
    color: var(--gray-500); 
    line-height: 1; 
    margin-top: 0px; 
}
.footer-brand .pvt-ltd { 
    color: rgba(255,255,255,0.7); 
}
"""

if '.pvt-ltd' not in css_content:
    css_content += pvt_ltd_css
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

print("HTML and CSS updated successfully.")
