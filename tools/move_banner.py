import re

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(\s*<!-- Services banner -->\s*<div class="services-hero services-hero-fullbleed">.*?</div>\s*</div>\s*</div>\s*)', re.DOTALL)
match = pattern.search(content)

if match:
    block = match.group(1)
    content = content[:match.start()] + content[match.end():]
    
    # Use regex to find <!-- CTA -->
    cta_pattern = re.compile(r'(\s*<!-- CTA -->)')
    cta_match = cta_pattern.search(content)
    
    if cta_match:
        content = content[:cta_match.start()] + block + content[cta_match.start():]
        with open('services.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Successfully moved the banner.')
    else:
        print('Could not find CTA section')
else:
    print('Could not find the banner block')
