import os
from PIL import Image

desire_female_candidates = ['BEN04137', 'BEN04149', 'BEN04159', 'BEN04180']
for c in desire_female_candidates:
    # find file
    matches = [f for f in os.listdir('jackets_original') if c in f and not f.startswith(('resized_', 'compressed_'))]
    print(c, matches)

