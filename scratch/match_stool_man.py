import os
from PIL import Image

screenshot = Image.open('C:/Users/razi7/.gemini/antigravity/brain/ca9db15d-74e4-425d-899e-b554016f82b2/.user_uploaded/media_1793206230264_af48ba0b.png')
print("Screenshot size:", screenshot.size)

# The man on the wooden stool is in the bottom right quadrant
# Let's crop the bottom right quadrant
w, h = screenshot.size
# stool shot is roughly x from 0.48*w to 0.87*w, y from 0.45*h to 0.98*h
crop_man = screenshot.crop((int(w * 0.48), int(h * 0.45), int(w * 0.87), int(h * 0.98)))
crop_man = crop_man.resize((100, 150)).convert('RGB')

# Now let's compare crop_man with each file in assets/collection/nocturne/desire and jackets_original
scores = []
for p in ['assets/collection/nocturne/desire', 'jackets_original']:
    for f in os.listdir(p):
        if f.endswith(('.jpg', '.png', '.webp')) and not f.startswith(('resized_', 'compressed_')):
            fp = os.path.join(p, f)
            try:
                with Image.open(fp) as im:
                    im_thumb = im.convert('RGB').resize((100, 150))
                    # Mean squared difference
                    diff = 0
                    for y in range(150):
                        for x in range(100):
                            p1 = crop_man.getpixel((x, y))
                            p2 = im_thumb.getpixel((x, y))
                            diff += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
                    scores.append((diff, fp))
            except Exception as e:
                pass

scores.sort()
print("\nTop 10 matches for the man on the wooden stool in the user's screenshot:")
for s, fp in scores[:10]:
    print(f"Score: {s} | {fp}")

