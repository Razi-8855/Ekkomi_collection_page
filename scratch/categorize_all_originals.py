import os
from PIL import Image

# Let's inspect all unique shots in jackets_original:
# Print shot name, size, dominant colors, and description
shots = sorted([f for f in os.listdir('jackets_original') if not f.startswith(('resized_', 'compressed_'))])

print(f"Total files: {len(shots)}")
for s in shots:
    fp = os.path.join('jackets_original', s)
    with Image.open(fp) as im:
        w, h = im.size
        # sample 100 points in the middle
        colors = [im.getpixel((x, y))[:3] for y in range(int(h*0.3), int(h*0.7), int(h*0.04)) for x in range(int(w*0.3), int(w*0.7), int(w*0.04))]
        r = sum(c[0] for c in colors)/len(colors)
        g = sum(c[1] for c in colors)/len(colors)
        b = sum(c[2] for c in colors)/len(colors)
        
        # Determine dominant tone
        if b > r and b > g and b > 25:
            color_name = "NAVY / BLUE (Curiosity)"
        elif g > r and g > 35:
            color_name = "GREEN (Temptation)"
        elif r > g + 25 and r > b + 25:
            color_name = "RED (Desire)"
        elif r > 80 and g > 60 and b < 50:
            color_name = "MUSTARD (Audacity)"
        elif r < 45 and g < 45 and b < 45:
            color_name = "BLACK / DARK (Insolence / Curiosity / Dark)"
        else:
            color_name = f"OTHER ({r:.0f},{g:.0f},{b:.0f})"
            
        print(f"{s:25} | ({w}x{h}) | {color_name}")

