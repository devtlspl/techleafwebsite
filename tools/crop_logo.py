from PIL import Image

# Open the logo image
img = Image.open('assets/img/logo.png').convert("RGBA")

# Get bounding box of non-transparent pixels
# First we need to get the alpha channel
alpha = img.split()[-1]
bbox = alpha.getbbox()

if bbox:
    # Crop the image to the bounding box
    img_cropped = img.crop(bbox)
    img_cropped.save('assets/img/logo_cropped.png')
    print("Successfully cropped the logo and saved to logo_cropped.png")
else:
    print("Could not find a bounding box, image might be completely transparent.")
