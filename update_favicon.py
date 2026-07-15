import urllib.request
from PIL import Image
import os

url = "https://techleafassets.blob.core.windows.net/assets/TechLeafLogoPNG.png"
temp_file = "assets/img/temp_logo.png"

try:
    # Download the image
    urllib.request.urlretrieve(url, temp_file)
    print("Downloaded new transparent logo.")

    img = Image.open(temp_file).convert("RGBA")

    # Generate proper favicon.png
    favicon_png = img.resize((512, 512), Image.Resampling.LANCZOS)
    favicon_png.save("assets/img/favicon.png", "PNG")
    print("Updated assets/img/favicon.png")

    # Generate proper favicon.ico
    favicon_ico = img.resize((32, 32), Image.Resampling.LANCZOS)
    favicon_ico.save("favicon.ico", format="ICO")
    print("Updated favicon.ico")

    # Clean up
    os.remove(temp_file)
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
