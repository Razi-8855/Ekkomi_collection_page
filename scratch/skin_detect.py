import os
from PIL import Image

curiosity_shots = ['BEN03124', 'BEN03136', 'BEN03137', 'BEN03166', 'BEN03202', 'BEN03212']

for c in curiosity_shots:
    p = f"scratch/inspect_all_35/{c}_full.jpg"
    im = Image.open(p)
    w, h = im.size
    print(f"\n=================== {c} ===================")
    
    # Let's inspect where skin is located:
    skin_pixels = []
    for y in range(h):
        for x in range(w):
            r, g, b = im.getpixel((x, y))
            # Typical human skin in RGB
            if r > 60 and g > 40 and b > 20 and r > g and g > b and (r - g) >= 15:
                skin_pixels.append((x, y, r, g, b))
    
    print(f"Total skin pixels: {len(skin_pixels)}")
    if skin_pixels:
        ys = [p[1] for p in skin_pixels]
        xs = [p[0] for p in skin_pixels]
        print(f"Skin Y range: {min(ys)} - {max(ys)} (h={h})")
        print(f"Skin X range: {min(xs)} - {max(xs)} (w={w})")

