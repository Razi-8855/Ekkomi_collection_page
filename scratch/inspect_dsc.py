import os
from PIL import Image

# Let's inspect DSC04253
im = Image.open("scratch/inspect_all_35/DSC04253_full.jpg")
w, h = im.size
print(f"DSC04253: size={w}x{h}")
# What jacket color is in DSC04253?
# Let's check the jacket pixels (torso)
jacket_px = []
for y in range(int(h*0.3), int(h*0.7)):
    for x in range(int(w*0.3), int(w*0.7)):
        jacket_px.append(im.getpixel((x, y)))

avg_r = sum(p[0] for p in jacket_px)/len(jacket_px)
avg_g = sum(p[1] for p in jacket_px)/len(jacket_px)
avg_b = sum(p[2] for p in jacket_px)/len(jacket_px)
print(f"DSC04253 torso avg RGB: ({avg_r:.1f}, {avg_g:.1f}, {avg_b:.1f})")

