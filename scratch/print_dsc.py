from PIL import Image

im = Image.open('jackets_original/DSC04253.jpg')
small = im.resize((60, 40)).convert('L')
ascii_chars = "@%#*+=-:. "
for y in range(40):
    row = ""
    for x in range(60):
        val = small.getpixel((x, y))
        row += ascii_chars[val * (len(ascii_chars) - 1) // 255]
    print(row)

