from PIL import Image

for s in ['BEN04004', 'BEN04014', 'BEN04015', 'BEN04031', 'BEN04053', 'BEN04058', 'BEN04068']:
    im = Image.open(f"scratch/inspect_all_35/{s}_full.jpg")
    w, h = im.size
    head = im.crop((int(w*0.25), 0, int(w*0.75), int(h*0.4)))
    small = head.resize((30, 20)).convert('L')
    ascii_chars = "@%#*+=-:. "
    print(f"\n=================== {s} ({w}x{h}) ===================")
    for y in range(20):
        row = ""
        for x in range(30):
            val = small.getpixel((x, y))
            row += ascii_chars[val * (len(ascii_chars) - 1) // 255]
        print(row)

