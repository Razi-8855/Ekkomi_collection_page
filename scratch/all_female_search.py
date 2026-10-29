import os
from PIL import Image

female_face = Image.open('jackets_original/BEN04068.jpg')
fw, fh = female_face.size
f_crop = female_face.crop((int(fw*0.35), int(fh*0.2), int(fw*0.65), int(fh*0.5))).resize((100, 100)).convert('RGB')

shots = sorted([f.replace('_full.jpg', '') for f in os.listdir('scratch/inspect_all_35') if f.endswith('_full.jpg')])

results = []
for s in shots:
    im = Image.open(f"scratch/inspect_all_35/{s}_full.jpg")
    w, h = im.size
    # let's crop head
    head = im.crop((int(w*0.2), 0, int(w*0.8), int(h*0.45))).resize((100, 100)).convert('RGB')
    diff_f = sum(abs(head.getpixel((x, y))[i] - f_crop.getpixel((x, y))[i]) for y in range(100) for x in range(100) for i in range(3))
    results.append((diff_f, s))

results.sort()
print("Top 15 closest shots to the female model face (BEN04068):")
for diff, s in results[:15]:
    print(f"{diff:10d} | {s}")

