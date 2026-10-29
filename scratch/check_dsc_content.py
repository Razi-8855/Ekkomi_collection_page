from PIL import Image

im = Image.open('jackets_original/DSC04253.jpg')
w, h = im.size

# Check colors in the center
# Is it a person?
print("DSC04253 info:")
# Let's check skin pixels
skin = 0
for y in range(0, h, 10):
    for x in range(0, w, 10):
        r, g, b = im.getpixel((x, y))
        if r > 100 and g > 60 and b > 40 and r > g and g > b and (r-g)>15:
            skin += 1

print(f"Skin sample count: {skin}")

# What colors are in the center?
center_colors = []
for y in range(int(h*0.3), int(h*0.7), 20):
    for x in range(int(w*0.3), int(w*0.7), 20):
        center_colors.append(im.getpixel((x, y)))

avg_r = sum(c[0] for c in center_colors)/len(center_colors)
avg_g = sum(c[1] for c in center_colors)/len(center_colors)
avg_b = sum(c[2] for c in center_colors)/len(center_colors)
print(f"Torso avg: ({avg_r:.1f}, {avg_g:.1f}, {avg_b:.1f})")

