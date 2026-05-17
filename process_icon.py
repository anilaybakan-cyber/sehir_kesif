from PIL import Image
import os

input_path = '/Users/anilebru/Desktop/gezgin.png'
output_path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/icons/gezgin.png'

# Create output dir if not exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

img = Image.open(input_path)
img = img.convert("RGBA")

datas = img.getdata()

newData = []
for item in datas:
    # If it's very light grey or white, make it transparent
    # The image I saw has a background of roughly (240, 240, 240)
    if item[0] > 220 and item[1] > 220 and item[2] > 220:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save(output_path, "PNG")
print(f"Processed and saved to {output_path}")
