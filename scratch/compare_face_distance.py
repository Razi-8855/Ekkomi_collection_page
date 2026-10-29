from PIL import Image

# Compare face crops with the known female model crop (BEN04068, BEN04159)
# and with the known male model crop (BEN03136)

female_face = Image.open('jackets_original/BEN04068.jpg')
fw, fh = female_face.size
# crop female head
f_crop = female_face.crop((int(fw*0.35), int(fh*0.2), int(fw*0.65), int(fh*0.5))).resize((100, 100)).convert('RGB')

male_face = Image.open('jackets_original/BEN03136 (1).jpg')
mw, mh = male_face.size
m_crop = male_face.crop((int(mw*0.2), int(mh*0.0), int(mw*0.8), int(mh*0.4))).resize((100, 100)).convert('RGB')

for s in ['BEN03124', 'BEN03136', 'BEN03137', 'BEN03166', 'BEN03202', 'BEN03212']:
    c_img = Image.open(f"scratch/face_{s}.jpg").resize((100, 100)).convert('RGB')
    
    # compare distance to female vs male
    diff_f = sum(abs(c_img.getpixel((x, y))[i] - f_crop.getpixel((x, y))[i]) for y in range(100) for x in range(100) for i in range(3))
    diff_m = sum(abs(c_img.getpixel((x, y))[i] - m_crop.getpixel((x, y))[i]) for y in range(100) for x in range(100) for i in range(3))
    
    print(f"{s}: dist_to_female={diff_f}, dist_to_male={diff_m}")

