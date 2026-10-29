from PIL import Image

im = Image.open('jackets_original/BEN03166.webp')
w, h = im.size
# crop face
face = im.crop((int(w * 0.25), int(h * 0.05), int(w * 0.65), int(h * 0.35)))
face.resize((300, 300)).save('scratch/ben03166_face.jpg')

small = face.resize((50, 40)).convert('L')
ascii_chars = "@%#*+=-:. "
for y in range(40):
    row = ""
    for x in range(50):
        val = small.getpixel((x, y))
        row += ascii_chars[val * (len(ascii_chars) - 1) // 255]
    print(row)

