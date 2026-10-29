import os
from PIL import Image

# We will inspect all 35 shots in scratch/inspect_all_35
# Each shot has:
# - prefix_full.jpg
# - prefix_head.jpg
# - prefix_torso.jpg

shots = sorted([f.replace('_full.jpg', '') for f in os.listdir('scratch/inspect_all_35') if f.endswith('_full.jpg')])

print(f"Total shots to classify: {len(shots)}")

# Let's inspect each shot:
# We know the female model has distinct features:
# - dark hair pulled back into a high bun (visible above the head)
# - bold red lipstick
# - female facial structure
# - white top / cream knit top or bare collarbone
# - wearing either Mustard, Red, or Black

for s in shots:
    p_full = f"scratch/inspect_all_35/{s}_full.jpg"
    p_head = f"scratch/inspect_all_35/{s}_head.jpg"
    p_torso = f"scratch/inspect_all_35/{s}_torso.jpg"
    
    im_full = Image.open(p_full)
    im_head = Image.open(p_head)
    im_torso = Image.open(p_torso)
    
    # Check red lips in head crop (y in lower half of head crop, x in center)
    hw, hh = im_head.size
    red_lips = 0
    for y in range(int(hh * 0.4), int(hh * 0.85)):
        for x in range(int(hw * 0.3), int(hw * 0.7)):
            r, g, b = im_head.getpixel((x, y))
            # red lipstick condition: high red, much lower green and blue
            if r > 95 and g < 45 and b < 45 and (r - g) > 55:
                red_lips += 1
                
    # Check top bun / updo in head crop (y in top 30% of head crop, x in center)
    # hair is very dark: r < 40, g < 30, b < 25
    bun_pixels = 0
    for y in range(int(hh * 0.05), int(hh * 0.35)):
        for x in range(int(hw * 0.35), int(hw * 0.65)):
            r, g, b = im_head.getpixel((x, y))
            if r < 35 and g < 28 and b < 25:
                bun_pixels += 1
                
    # Torso dominant color
    tw, th = im_torso.size
    torso_colors = [im_torso.getpixel((x, y)) for y in range(int(th*0.2), int(th*0.8), 4) for x in range(int(tw*0.2), int(tw*0.8), 4)]
    tr = sum(c[0] for c in torso_colors) / len(torso_colors)
    tg = sum(c[1] for c in torso_colors) / len(torso_colors)
    tb = sum(c[2] for c in torso_colors) / len(torso_colors)
    
    print(f"{s:10} | red_lips={red_lips:3d} | bun={bun_pixels:3d} | torso_rgb=({tr:5.1f},{tg:5.1f},{tb:5.1f})")

