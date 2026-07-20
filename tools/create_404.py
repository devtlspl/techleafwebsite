import re

with open('404.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = re.sub(r'<title>.*?</title>', '<title>404 - Page Not Found | TechLeaf Systems</title>', content)

# Replace "Thank You!" heading
content = re.sub(r'<h1>.*?</h1>', '<h1>404</h1>', content)

# Replace text
content = re.sub(r'<p class="thank-you-subtitle">.*?</p>', '<p class="thank-you-subtitle">Oops! The page you are looking for does not exist or has been moved.</p>', content)

# Add a button back to home
button_html = '<a href="index.html" class="btn btn-primary" style="margin-top:20px; display:inline-block;">Return to Homepage</a>'
content = content.replace('</p>', f'</p>\n          {button_html}', 1)

with open('404.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("404.html created.")
