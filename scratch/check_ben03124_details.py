from PIL import Image

im = Image.open('jackets_original/BEN03124 (1).jpg')
w, h = im.size
print(f"BEN03124: {w}x{h}")
# What is the person wearing?
# Let's inspect torso
torso = im.crop((int(w * 0.3), int(h * 0.3), int(w * 0.7), int(h * 0.7)))
# Let's save a clear view
torso.resize((400, 400)).save('scratch/ben03124_torso_clear.jpg')
print("Saved ben03124_torso_clear.jpg")

