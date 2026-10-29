import os
from PIL import Image

for i in range(1, 5):
    p = f"assets/collection/nocturne/insolence/insolence_editorial_{i}.jpg"
    im = Image.open(p).resize((60, 90)).convert('RGB')
    
    # find best match in jackets_original
    best_diff = 999999999
    best_f = None
    for f in os.listdir('jackets_original'):
        if not f.startswith(('resized_', 'compressed_')):
            fp = os.path.join('jackets_original', f)
            try:
                oim = Image.open(fp).resize((60, 90)).convert('RGB')
                diff = sum(abs(im.getpixel((x, y))[c] - oim.getpixel((x, y))[c]) for y in range(90) for x in range(60) for c in range(3))
                if diff < best_diff:
                    best_diff = diff
                    best_f = f
            except:
                pass
    print(f"insolence_editorial_{i}.jpg matches: {best_f} (diff={best_diff})")

