import os
from PIL import Image

shots = {}
for f in os.listdir('jackets_original'):
    if f.startswith(('resized_', 'compressed_')):
        continue
    # extract shot key
    name = f.split('.')[0].replace(' (1)', '')
    shots[name] = f

print("All shot IDs:")
for k in sorted(shots.keys()):
    print(k, "->", shots[k])

