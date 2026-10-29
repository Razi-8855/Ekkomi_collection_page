from PIL import Image

im = Image.open('jackets_original/BEN03124 (1).jpg')
w, h = im.size
print(f"BEN03124 size: {w}x{h}")

# The person is standing
# Let's crop:
# 1. Face
# 2. Torso (jacket)
# 3. Legs/pants

face = im.crop((int(w * 0.4), int(h * 0.15), int(w * 0.6), int(h * 0.3)))
torso = im.crop((int(w * 0.3), int(h * 0.28), int(w * 0.7), int(h * 0.65)))
legs = im.crop((int(w * 0.35), int(h * 0.6), int(w * 0.65), int(h * 0.95)))

face.save('scratch/ben03124_face.jpg')
torso.save('scratch/ben03124_torso.jpg')
legs.save('scratch/ben03124_legs.jpg')

print("Saved BEN03124 crops.")

