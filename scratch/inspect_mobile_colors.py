import os
from PIL import Image

p = 'scratch/mobile_check'
for f in os.listdir(p):
    fp = os.path.join(p, f)
    im = Image.open(fp)
    w, h = im.size
    # let's sample colors down the vertical axis to see what sections are visible
    print(f"\n=================== {f} ===================")
    for y in range(0, h, 80):
        row_colors = [im.getpixel((x, y))[:3] for x in range(0, w, 20)]
        avg = (sum(c[0] for c in row_colors)//len(row_colors),
               sum(c[1] for c in row_colors)//len(row_colors),
               sum(c[2] for c in row_colors)//len(row_colors))
        print(f"y={y:3d}: avg RGB={avg}")

