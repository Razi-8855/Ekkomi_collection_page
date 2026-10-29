from PIL import Image

shots = ['BEN03307', 'BEN03515', 'BEN03619', 'BEN03636', 'BEN03655', 'BEN03667', 'BEN03725', 'BEN03767',
         'BEN03835', 'BEN03870', 'BEN03893', 'BEN03898', 'BEN03906', 'BEN03911',
         'BEN04004', 'BEN04014', 'BEN04015', 'BEN04031', 'BEN04053', 'DSC04253']

for s in shots:
    im = Image.open(f"scratch/inspect_all_35/{s}_full.jpg")
    w, h = im.size
    head = im.crop((int(w*0.2), 0, int(w*0.8), int(h*0.45)))
    small = head.resize((30, 20)).convert('L')
    ascii_chars = "@%#*+=-:. "
    print(f"\n=================== {s} ({w}x{h}) ===================")
    for y in range(20):
        row = ""
        for x in range(30):
            val = small.getpixel((x, y))
            row += ascii_chars[val * (len(ascii_chars) - 1) // 255]
        print(row)

