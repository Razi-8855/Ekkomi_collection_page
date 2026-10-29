import os
from PIL import Image

shots = sorted([f.replace('_full.jpg', '') for f in os.listdir('scratch/inspect_all_35') if f.endswith('_full.jpg')])

female_candidates = []

for s in shots:
    p = f"scratch/inspect_all_35/{s}_full.jpg"
    with Image.open(p) as im:
        w, h = im.size
        # Search for bright red pixels in the upper 40% of the image (lips, makeup)
        red_pixel_count = 0
        for y in range(int(h * 0.05), int(h * 0.4)):
            for x in range(int(w * 0.25), int(w * 0.75)):
                r, g, b = im.getpixel((x, y))
                # Red lips are typically high R, low G, low B (e.g. r > 100, g < 40, b < 40)
                if r > 100 and g < 50 and b < 50:
                    red_pixel_count += 1
        
        print(f"{s:10} | red_lip_pixels={red_pixel_count}")
        if red_pixel_count > 15:
            female_candidates.append(s)

print("\nDetected female shots (with red lips):", female_candidates)

