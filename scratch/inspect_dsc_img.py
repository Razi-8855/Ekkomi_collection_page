from PIL import Image

im = Image.open('jackets_original/DSC04253.jpg')
w, h = im.size
print(f"DSC04253 size: {w}x{h}")
# What is DSC04253?
# Let's save crops of DSC04253
im.crop((0, 0, w, int(h*0.4))).resize((200, 200)).save('scratch/dsc_head.jpg')
im.crop((0, int(h*0.2), w, int(h*0.8))).resize((200, 200)).save('scratch/dsc_torso.jpg')
print("Saved dsc crops")

