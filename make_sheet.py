import os
from PIL import Image, ImageDraw, ImageFont
import math

dest_dir = 'imgs/nuevas'
images = [f for f in os.listdir(dest_dir) if f.startswith('cat_') and f.endswith('.jpg')]
images.sort()

# Create a contact sheet
cols = 10
rows = math.ceil(len(images) / cols)
thumb_w, thumb_h = 200, 200

contact_sheet = Image.new('RGB', (cols * thumb_w, rows * thumb_h), 'white')
draw = ImageDraw.Draw(contact_sheet)

for i, img_name in enumerate(images):
    img_path = os.path.join(dest_dir, img_name)
    try:
        img = Image.open(img_path)
        img.thumbnail((thumb_w, thumb_h))
        # paste centered
        x = (i % cols) * thumb_w
        y = (i // cols) * thumb_h
        
        # paste image
        contact_sheet.paste(img, (x, y))
        
        # draw text
        draw.text((x + 10, y + 10), str(i), fill='red')
    except Exception as e:
        print(f"Error processing {img_name}: {e}")

contact_sheet.save('contact_sheet.jpg')
print("Saved contact_sheet.jpg")
