import os
from PIL import Image

p = 'assets/collection/nocturne/insolence'
for f in sorted(os.listdir(p)):
    if f.endswith('.jpg'):
        fp = os.path.join(p, f)
        im = Image.open(fp)
        print(f, im.size)
        # sample colors in the center
        w, h = im.size
        sample = [im.getpixel((x, y)) for y in range(int(h*0.3), int(h*0.7), int(h*0.05)) for x in range(int(w*0.3), int(w*0.7), int(w*0.05))]
        ar = sum(c[0] for c in sample)/len(sample)
        ag = sum(c[1] for c in sample)/len(sample)
        ab = sum(c[2] for c in sample)/len(sample)
        print(f"  avg RGB: ({ar:.1f}, {ag:.1f}, {ab:.1f})")

