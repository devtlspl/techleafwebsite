import os
import re
import subprocess

def run_tests():
    print("--- STARTING FINAL QA CHECK ---\n")
    issues = 0

    # 1. Check all JS files for syntax errors
    print("[1/3] Checking Javascript Syntax...")
    js_dir = 'assets/js'
    for f in os.listdir(js_dir):
        if f.endswith('.js'):
            filepath = os.path.join(js_dir, f)
            result = subprocess.run(['node', '-c', filepath], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ Syntax Error in {f}:\n{result.stderr}")
                issues += 1
            else:
                print(f"✅ {f} passed.")

    # 2. Check HTML files for broken links and missing images
    print("\n[2/3] Checking HTML Files...")
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Check for empty hrefs
                if re.search(r'href=""|href="#"', content):
                    print(f"⚠️ Warning: Found empty or '#' links in {f}")
                
                # Check for missing local image files
                images = re.findall(r'src="([^"]+)"', content)
                for img in images:
                    if not img.startswith('http') and not img.startswith('data:'):
                        # Handle potential query params in src (e.g. file.jpg?v=2)
                        img_path = img.split('?')[0]
                        if not os.path.exists(img_path):
                            print(f"❌ Broken Image Link in {f}: {img_path}")
                            issues += 1
                            
                # Check for unclosed tags (very basic heuristic: just counting divs)
                open_divs = len(re.findall(r'<div\b[^>]*>', content))
                close_divs = len(re.findall(r'</div>', content))
                if open_divs != close_divs:
                    print(f"⚠️ Warning: Unmatched <div> tags in {f} (Opened: {open_divs}, Closed: {close_divs})")

    # 3. Check CSS for basic syntax
    print("\n[3/3] Checking CSS Files...")
    css_dir = 'assets/css'
    if os.path.exists(css_dir):
        for f in os.listdir(css_dir):
            if f.endswith('.css'):
                with open(os.path.join(css_dir, f), 'r', encoding='utf-8') as file:
                    content = file.read()
                    if content.count('{') != content.count('}'):
                        print(f"❌ Unmatched braces in {f}")
                        issues += 1
                    else:
                        print(f"✅ {f} passed.")
    
    print(f"\n--- QA COMPLETE: {issues} critical issues found ---")

if __name__ == "__main__":
    run_tests()
