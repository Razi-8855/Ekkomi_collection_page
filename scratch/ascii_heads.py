from PIL import Image

for shot in ['BEN03124', 'BEN03136', 'BEN03137', 'BEN03166', 'BEN03202', 'BEN03212']:
    im = Image.open(f"scratch/inspect_all_35/{shot}_full.jpg")
    w, h = im.size
    print(f"\n=================== {shot} ===================")
    # Let's inspect where skin is and what colors are present around the head/face:
    # Let's crop head region (y from 0 to int(h*0.45), x from int(w*0.2) to int(w*0.8))
    head = im.crop((int(w*0.2), 0, int(w*0.8), int(h*0.45)))
    hw, hh = head.size
    # let's find the brightest skin pixel and darkest hair pixel
    pixels = list(head.getdata())
    # count pixels by color
    print(f"Head region size: {hw}x{hh}")
    # let's save a small ascii art of head
    small = head.resize((40, 30)).convert('L')
    ascii_chars = "@%#*+=-:. "
    for y in range(30):
        row = ""
        for x in range(40):
            val = small.getpixel((x, y))
            row += ascii_chars[val * (len(ascii_chars) - 1) // 255]
        print(row)

