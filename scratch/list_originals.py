import os
from PIL import Image

# List all original files
files = [f for f in os.listdir('jackets_original') if not f.startswith(('resized_', 'compressed_'))]

print(f"Total original files: {len(files)}")
for f in sorted(files):
    fp = os.path.join('jackets_original', f)
    with Image.open(fp) as im:
        print(f"{f:25} | format={im.format:5} | size={str(im.size):12}")

