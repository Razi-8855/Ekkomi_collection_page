from PIL import Image

im = Image.open('scratch/ben03124_face.jpg')
small = im.resize((50, 40)).convert('L')
ascii_chars = "@%#*+=-:. "
for y in range(40):
    row = ""
    for x in range(50):
        val = small.getpixel((x, y))
        row += ascii_chars[val * (len(ascii_chars) - 1) // 255]
    print(row)

