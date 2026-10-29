import os
from PIL import Image

# Let's inspect all 48 files in jackets_original
files = sorted([f for f in os.listdir('jackets_original') if not f.startswith(('resized_', 'compressed_'))])

print("Exhaustive inspection of jackets_original:")
for f in files:
    fp = os.path.join('jackets_original', f)
    # let's check prefix
    prefix = f.split('.')[0].replace(' (1)', '')
    print(f"File: {f:25} -> Shot ID: {prefix}")

