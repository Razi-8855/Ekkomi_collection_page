import os
from PIL import Image

# Let's inspect the files BEN03124 - BEN03212
# Are any of them a woman?
for s in ['BEN03124', 'BEN03136', 'BEN03137', 'BEN03166', 'BEN03202', 'BEN03212']:
    im = Image.open(f"scratch/inspect_all_35/{s}_full.jpg")
    w, h = im.size
    print(f"\n{s} ({w}x{h}):")
    # Let's check the face crop:
    # Save a clear 150x150 face thumbnail
    face = im.crop((int(w * 0.25), int(h * 0.05), int(w * 0.75), int(h * 0.45)))
    face.resize((150, 150)).save(f"scratch/face_inspect_{s}.jpg")

print("Saved face inspect images.")

