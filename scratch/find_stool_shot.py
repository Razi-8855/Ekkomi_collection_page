import os
from PIL import Image

# Let's inspect all files in jackets_original related to red jacket or all BEN files
files = [f for f in os.listdir('jackets_original') if not f.startswith(('resized_', 'compressed_'))]

for f in sorted(files):
    fp = os.path.join('jackets_original', f)
    # let's check size and see
    try:
        with Image.open(fp) as im:
            print(f"{f:25} | format={im.format:5} | size={str(im.size):12}")
    except Exception as e:
        print(f"Error {f}: {e}")

