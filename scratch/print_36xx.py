from PIL import Image

for s in ['BEN03515', 'BEN03619', 'BEN03655']:
    im = Image.open(f"scratch/inspect_all_35/{s}_full.jpg")
    small = im.resize((50, 40)).convert('L')
    ascii_chars = "@%#*+=-:. "
    print(f"\n=================== {s} ===================")
    for y in range(40):
        row = ""
        for x in range(50):
            val = small.getpixel((x, y))
            row += ascii_chars[val * (len(ascii_chars) - 1) // 255]
        print(row)

