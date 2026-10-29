import os
from PIL import Image

for s in ['BEN03124', 'BEN03136', 'BEN03137', 'BEN03166', 'BEN03202', 'BEN03212']:
    p1 = f"jackets_original/{s} (1).jpg"
    p2 = f"jackets_original/{s}.jpg"
    p3 = f"jackets_original/{s}.webp"
    p4 = f"jackets_original/{s}.png"
    target = p1 if os.path.exists(p1) else p2 if os.path.exists(p2) else p3 if os.path.exists(p3) else p4
    im = Image.open(target)
    w, h = im.size
    print(f"{s}: file={target}, size={w}x{h}")
    face = im.crop((int(w * 0.3), int(h * 0.15), int(w * 0.7), int(h * 0.55)))
    face.resize((300, 300)).save(f"scratch/face_{s}.jpg")

print("Saved face crops for all 6 curiosity shots.")
