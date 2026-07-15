import os
import re

def create_pledge_page():
    # Read about.html to use as a template
    with open('about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # We want to keep everything up to the end of the <header> and the nav
    # The first section after header is typically <section class="page-hero"> or similar.
    # Let's find the closing </header> tag.
    header_end = html.find('</header>') + len('</header>')
    
    # Let's find the start of the footer CTA or FOOTER
    footer_start = html.find('<!-- CTA -->')
    if footer_start == -1:
        footer_start = html.find('<footer class="site-footer">')

    header_part = html[:header_end]
    footer_part = html[footer_start:]

    # Fix the active nav link (remove active from About, no active link for pledge)
    header_part = header_part.replace('href="about.html" class="active"', 'href="about.html"')

    # Create the new pledge content
    pledge_content = """
<!-- PAGE HERO -->
<section class="page-hero">
  <div class="container">
    <h1>Environmental Sustainability Pledge</h1>
    <p>Championing the Circular IT Economy through hardware reuse and lifecycle management.</p>
  </div>
</section>

<!-- PLEDGE CONTENT -->
<section class="section">
  <div class="container" style="max-width: 800px; margin: 0 auto; line-height: 1.8; font-size: 1.1rem; color: #4a5568;">
    <h2 style="color: #1a365d; margin-bottom: 1.5rem; font-size: 2rem;">Our Commitment to the Environment</h2>
    <p style="margin-bottom: 1.5rem;">At TechLeaf Systems Private Limited, environmental sustainability is not just an initiative—it is built directly into our core business model. Through our Enterprise IT Hardware Rental and Annual Maintenance Contract (AMC) services, we actively champion the Circular IT Economy.</p>
    
    <h3 style="color: #1a365d; margin-top: 2rem; margin-bottom: 1rem; font-size: 1.5rem;">Reducing Electronic Waste (E-Waste)</h3>
    <p style="margin-bottom: 1.5rem;">By meticulously maintaining, refurbishing, and extending the lifecycle of servers, storage arrays, and network infrastructure, we help businesses drastically reduce electronic waste. Every server we deploy as a rental is a server that didn't need to be newly manufactured, saving significant energy and raw materials.</p>
    
    <h3 style="color: #1a365d; margin-top: 2rem; margin-bottom: 1rem; font-size: 1.5rem;">The Zero-Capex, Low-Carbon Approach</h3>
    <p style="margin-bottom: 1.5rem;">Instead of constantly manufacturing, shipping, and purchasing new equipment, our clients leverage high-performance, perfectly maintained infrastructure on demand. This approach not only optimizes IT budgets but fundamentally reduces the environmental impact and carbon footprint of global enterprise technology.</p>

    <div style="background: #f7fafc; border-left: 4px solid #38a169; padding: 2rem; margin-top: 3rem; border-radius: 0 8px 8px 0;">
      <h4 style="color: #2f855a; margin-bottom: 1rem; font-size: 1.25rem;">Our Core Sustainability Pillars:</h4>
      <ul style="list-style-type: disc; padding-left: 1.5rem; color: #4a5568;">
        <li style="margin-bottom: 0.5rem;"><strong>Hardware Longevity:</strong> Maximizing the useful life of enterprise IT equipment through expert AMC and DBA support.</li>
        <li style="margin-bottom: 0.5rem;"><strong>Circular Economy:</strong> Renting instead of buying to ensure hardware is fully utilized across multiple lifecycles.</li>
        <li style="margin-bottom: 0.5rem;"><strong>Responsible Disposal:</strong> Ensuring end-of-life equipment is recycled responsibly in compliance with all e-waste regulations.</li>
      </ul>
    </div>
  </div>
</section>
"""

    # Combine parts
    full_html = header_part + "\n" + pledge_content + "\n" + footer_part

    # Update document title
    full_html = re.sub(
        r'<title>.*?</title>', 
        '<title>Sustainability Pledge | TechLeaf Systems Private Limited</title>', 
        full_html
    )

    # Write the new file
    with open('pledge.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Created pledge.html")

def add_link_to_footer():
    # We need to add a link to the footer in all HTML files
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it already has the link
        if 'pledge.html' in content:
            continue
            
        # Find the Company links in the footer
        # <li><a href="about.html">About Us</a></li>
        # Let's insert it after About Us
        target = '<li><a href="about.html">About Us</a></li>'
        replacement = '<li><a href="about.html">About Us</a></li>\n        <li><a href="pledge.html">Sustainability Pledge</a></li>'
        
        new_content = content.replace(target, replacement)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    print("Added Sustainability Pledge link to footer in all pages.")

if __name__ == '__main__':
    create_pledge_page()
    add_link_to_footer()
