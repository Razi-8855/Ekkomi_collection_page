from PIL import Image

im_dsc = Image.open('jackets_original/DSC04253.jpg')
im_female = Image.open('jackets_original/BEN04068.jpg')

# Let's inspect DSC04253 head region
# DSC04253 size is (2000, 3000)
# Let's crop head
w, h = im_dsc.size
# Find skin coordinates in DSC04253
skin_pts = []
for y in range(0, h, 20):
    for x in range(0, w, 20):
        r, g, b = im_dsc.getpixel((x, y))
        if r > 120 and g > 70 and b > 50 and r > g and g > b and (r-g)>20:
            skin_pts.append((x, y))

if skin_pts:
    min_y = min(p[1] for p in skin_pts)
    max_y = max(p[1] for p in skin_pts)
    min_x = min(p[0] for p in skin_pts)
    max_x = max(p[0] for p in skin_pts)
    print(f"DSC04253 Skin bounds: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
    
    # Let's crop around face
    face = im_dsc.crop((min_x, min_y, max_x, min_y + int((max_y-min_y)*0.4)))
    face.resize((150, 150)).save('scratch/dsc_face.jpg')
    print("Saved scratch/dsc_face.jpg")

