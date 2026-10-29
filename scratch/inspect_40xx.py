from PIL import Image

shots = ['BEN04004', 'BEN04014', 'BEN04015', 'BEN04031', 'BEN04053']

for s in shots:
    p = f"scratch/inspect_all_35/{s}_full.jpg"
    im = Image.open(p)
    w, h = im.size
    print(f"\n=================== {s} ===================")
    # let's sample the jacket color:
    # y from 0.35 to 0.65
    pixels = []
    for y in range(int(h*0.35), int(h*0.65), 5):
        for x in range(int(w*0.3), int(w*0.7), 5):
            pixels.append(im.getpixel((x, y)))
    
    ar = sum(p[0] for p in pixels)/len(pixels)
    ag = sum(p[1] for p in pixels)/len(pixels)
    ab = sum(p[2] for p in pixels)/len(pixels)
    print(f"Jacket avg RGB: ({ar:.1f}, {ag:.1f}, {ab:.1f})")
    
    # Check if there is red lips or female features
    # Check head
    head = im.crop((int(w*0.25), 0, int(w*0.75), int(h*0.4)))
    # print head dimensions
    print(f"Head crop: {head.size}")

