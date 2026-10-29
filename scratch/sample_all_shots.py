import os
from PIL import Image

shots = sorted([f.replace('_full.jpg', '') for f in os.listdir('scratch/inspect_all_35') if f.endswith('_full.jpg')])

for s in shots:
    p = f"scratch/inspect_all_35/{s}_full.jpg"
    with Image.open(p) as im:
        w, h = im.size
        # sample 5 points across the image:
        # head (0.5*w, 0.15*h), chest (0.5*w, 0.4*h), abdomen (0.5*w, 0.6*h), legs (0.5*w, 0.85*h), background (0.1*w, 0.1*h)
        bg = im.getpixel((int(w*0.1), int(h*0.1)))
        head = im.getpixel((int(w*0.5), int(h*0.15)))
        chest = im.getpixel((int(w*0.5), int(h*0.4)))
        ab = im.getpixel((int(w*0.5), int(h*0.6)))
        legs = im.getpixel((int(w*0.5), int(h*0.85)))
        print(f"{s:10} | bg={bg} | head={head} | chest={chest} | ab={ab} | legs={legs}")

