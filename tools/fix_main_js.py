import re

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# 1. Remove initHeroSliderAutoplay call
js_content = re.sub(r'\s*// Auto-rotate hero slider every 7s\s*initHeroSliderAutoplay\(\);', '', js_content)

# 2. Remove initHeroSliderAutoplay function
# The function spans from `function initHeroSliderAutoplay() {` up to `// GA4 Event Tracking`
# Let's use a regex to strip it
pattern_func = r'function initHeroSliderAutoplay\(\)\s*\{.*?\}\s*\}\s*// GA4 Event Tracking'
js_content = re.sub(r'function initHeroSliderAutoplay\(\) \{.*?(?=\n// GA4 Event Tracking)', '', js_content, flags=re.DOTALL)

# Let's make sure it's removed
# Also we need to merge the DOMContentLoaded
# We want to take the contents of the second DOMContentLoaded and put it at the end of the first.
# Wait, it's easier to just strip `});\n\n// GA4 Event Tracking\ndocument.addEventListener('DOMContentLoaded', function () {\n`
merge_pattern = r'\s*\}\);\s*// GA4 Event Tracking\s*document\.addEventListener\(\'DOMContentLoaded\', function \(\) \{'
js_content = re.sub(merge_pattern, '\n\n  // GA4 Event Tracking', js_content)

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Minify JS (Safe method: strip leading/trailing spaces, remove blank lines)
minified_js = []
for line in js_content.split('\n'):
    stripped = line.strip()
    if stripped and not stripped.startswith('//'):
        minified_js.append(stripped)

with open('assets/js/main.min.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(minified_js))

print("Fixed main.js and minified to main.min.js")
