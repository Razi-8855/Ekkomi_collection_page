import os
from PIL import Image

p = 'assets/collection/nocturne/desire'
for f in os.listdir(p):
    if f.endswith(('.jpg', '.png')):
        fp = os.path.join(p, f)
        with Image.open(fp) as im:
            print(f"{f:25} | {im.size}")

