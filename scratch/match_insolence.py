import os
from PIL import Image

for f in ['insolence_editorial_1.jpg', 'insolence_editorial_2.jpg', 'insolence_editorial_3.jpg', 'insolence_editorial_4.jpg']:
    p = os.path.join('assets/collection/nocturne/insolence', f)
    im = Image.open(p)
    print(f, im.size)
    # let's match with jackets_original
    for of in os.listdir('jackets_original'):
        if not of.startswith(('resized_', 'compressed_')):
            op = os.path.join('jackets_original', of)
            try:
                oim = Image.open(op)
                if oim.size[1] / oim.size[0] == im.size[1] / im.size[0]:
                    pass
            except:
                pass

