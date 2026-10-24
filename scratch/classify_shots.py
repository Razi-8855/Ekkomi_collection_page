import os, colorsys
from PIL import Image

shots = ['BEN03124', 'BEN03136', 'BEN03137', 'BEN03166', 'BEN03202', 'BEN03212', 
         'BEN03307', 'BEN03324', 'BEN03515', 'BEN03619', 'BEN03636', 'BEN03655', 
         'BEN03667', 'BEN03725', 'BEN03767', 'BEN03806', 'BEN03835', 'BEN03870', 
         'BEN03893', 'BEN03898', 'BEN03906', 'BEN03911', 'BEN04004', 'BEN04014', 
         'BEN04015', 'BEN04031', 'BEN04053', 'BEN04058', 'BEN04068', 'BEN04099', 
         'BEN04137', 'BEN04149', 'BEN04159', 'BEN04180', 'DSC04253']

all_files = os.listdir('jackets_original')

def get_shot_file(shot):
    candidates = [f for f in all_files if shot in f and not f.startswith(('resized_', 'compressed_'))]
    if not candidates:
        candidates = [f for f in all_files if shot in f]
    candidates.sort(key=lambda x: (x.endswith('.png'), x.endswith('.webp'), x.endswith('.jpg')))
    return os.path.join('jackets_original', candidates[0])

# Let's inspect the garment color by segmenting the darkest/most saturated pixels that aren't background
# Background in studio photoshoot is typically neutral/grey or warm grey
results = []
for s in shots:
    p = get_shot_file(s)
    with Image.open(p) as img:
        im = img.convert('RGB').resize((120, 180))
        # collect pixels in the jacket area: y from 30% to 80%, x from 20% to 80%
        w, h = im.size
        jacket_pixels = []
        for y in range(int(h * 0.3), int(h * 0.8)):
            for x in range(int(w * 0.25), int(w * 0.75)):
                r, g, b = im.getpixel((x, y))
                # filter out very bright background pixels (r>180, g>180, b>180) or skin highlights
                jacket_pixels.append((r, g, b))
        
        # average
        ar = sum(px[0] for px in jacket_pixels) / len(jacket_pixels)
        ag = sum(px[1] for px in jacket_pixels) / len(jacket_pixels)
        ab = sum(px[2] for px in jacket_pixels) / len(jacket_pixels)
        
        h_val, s_val, v_val = colorsys.rgb_to_hsv(ar/255.0, ag/255.0, ab/255.0)
        h_deg = h_val * 360
        
        results.append((s, os.path.basename(p), (round(ar,1), round(ag,1), round(ab,1)), round(h_deg,1), round(s_val*100,1), round(v_val*100,1)))

for r in results:
    print(f'{r[0]:10} | rgb={str(r[2]):20} | H={r[3]:5.1f} S={r[4]:4.1f}% V={r[5]:4.1f}% | {r[1]}')
