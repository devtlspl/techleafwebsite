from PIL import Image

# Open the cropped logo
logo = Image.open('assets/img/logo_cropped.png').convert("RGBA")

# Create a white background image for the social preview (1200x630 is standard for LinkedIn/Facebook)
bg_width, bg_height = 1200, 630
bg = Image.new('RGB', (bg_width, bg_height), (255, 255, 255))

# Calculate size to scale the logo (let's make it 800px wide max, or whatever fits well)
logo_aspect = logo.width / logo.height
new_logo_width = 800
new_logo_height = int(new_logo_width / logo_aspect)

logo_resized = logo.resize((new_logo_width, new_logo_height), Image.Resampling.LANCZOS)

# Calculate position to center the logo
x = (bg_width - new_logo_width) // 2
y = (bg_height - new_logo_height) // 2

# Paste the logo onto the white background using the logo's alpha channel as a mask
bg.paste(logo_resized, (x, y), mask=logo_resized)

# Save as the social preview image
bg.save('assets/img/social-preview.jpg', 'JPEG', quality=90)
print("Successfully generated new social-preview.jpg with the logo!")
