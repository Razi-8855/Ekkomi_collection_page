import os
from PIL import Image

curiosity_shots = ['BEN03124', 'BEN03136', 'BEN03137', 'BEN03166', 'BEN03202', 'BEN03212']

for s in curiosity_shots:
    # check full thumbnail in scratch/inspect_all_35
    p = f"scratch/inspect_all_35/{s}_full.jpg"
    with Image.open(p) as im:
        w, h = im.size
        # let's sample the head area (top 30%)
        # and sample background
        bg = im.getpixel((10, 10))
        center_head = im.getpixel((w//2, int(h * 0.15)))
        center_torso = im.getpixel((w//2, int(h * 0.5)))
        print(f"{s:10} | size=({w},{h}) | bg={bg} | head={center_head} | torso={center_torso}")

