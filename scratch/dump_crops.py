import os
from PIL import Image

out_dir = 'scratch/inspect_all_35'
os.makedirs(out_dir, exist_ok=True)

all_files = [f for f in os.listdir('jackets_original') if not f.startswith(('resized_', 'compressed_'))]

# Unique by prefix
unique_files = {}
for f in all_files:
    prefix = f.split('.')[0].replace(' (1)', '')
    if prefix not in unique_files:
        unique_files[prefix] = f
    elif f.endswith('.jpg'):
        unique_files[prefix] = f

print(f"Processing {len(unique_files)} unique shots...")

for prefix, fname in sorted(unique_files.items()):
    fp = os.path.join('jackets_original', fname)
    with Image.open(fp) as im:
        im_rgb = im.convert('RGB')
        w, h = im_rgb.size
        
        # Save full thumbnail
        thumb = im_rgb.resize((300, int(300 * h / w)))
        thumb.save(os.path.join(out_dir, f"{prefix}_full.jpg"), quality=85)
        
        # Save face / head crop (upper 40% center)
        face_crop = im_rgb.crop((int(w * 0.2), int(h * 0.02), int(w * 0.8), int(h * 0.4)))
        face_crop = face_crop.resize((240, 240))
        face_crop.save(os.path.join(out_dir, f"{prefix}_head.jpg"), quality=85)
        
        # Save jacket torso crop (middle 40%)
        torso_crop = im_rgb.crop((int(w * 0.2), int(h * 0.25), int(w * 0.8), int(h * 0.75)))
        torso_crop = torso_crop.resize((240, 240))
        torso_crop.save(os.path.join(out_dir, f"{prefix}_torso.jpg"), quality=85)

print("Saved all crops to scratch/inspect_all_35!")

