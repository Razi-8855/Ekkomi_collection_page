from PIL import Image

for s in ['BEN03124', 'BEN03166', 'BEN03202', 'BEN03212']:
    p = f"scratch/inspect_all_35/{s}_full.jpg"
    im = Image.open(p)
    w, h = im.size
    print(f"\n=================== {s} ===================")
    # Check upper half:
    upper = im.crop((0, 0, w, int(h*0.5)))
    # save upper
    upper.resize((200, 200)).save(f"scratch/upper_{s}.jpg")
    # let's inspect the ascii of upper
    small = upper.resize((40, 25)).convert('L')
    ascii_chars = "@%#*+=-:. "
    for y in range(25):
        row = ""
        for x in range(40):
            val = small.getpixel((x, y))
            row += ascii_chars[val * (len(ascii_chars) - 1) // 255]
        print(row)

