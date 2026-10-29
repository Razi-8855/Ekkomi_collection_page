# Let's inspect the 6 curiosity shots
# We can print ASCII representation or analyze the key regions
from PIL import Image

curiosity = ['BEN03124', 'BEN03136', 'BEN03137', 'BEN03166', 'BEN03202', 'BEN03212']

for c in curiosity:
    p = f"scratch/inspect_all_35/{c}_full.jpg"
    im = Image.open(p)
    print(f"\n--- {c} ---")
    # Let's check aspect ratio and description
    w, h = im.size
    print(f"Size: {w}x{h}")
    # Let's check skin tones:
    # where is the face located?
    # Let's check y from 0 to h//2
    # In BEN03136, we know: male model front (lips, chin, silver cuban chain, chest)
    # In BEN03137, we know: male model back view (EKKOMI embroidery on back, buzzcut back of head)
    # What about BEN03124? What is in BEN03124?
    # What about BEN03166? What is in BEN03166?
    # What about BEN03202? What is in BEN03202?
    # What about BEN03212? What is in BEN03212?

