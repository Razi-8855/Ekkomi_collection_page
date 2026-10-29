from PIL import Image

female_face = Image.open('scratch/inspect_all_35/BEN04068_head.jpg').resize((100, 100)).convert('RGB')
male_face = Image.open('scratch/inspect_all_35/BEN03136_head.jpg').resize((100, 100)).convert('RGB')

for s in ['BEN03307', 'BEN03324', 'BEN03515', 'BEN03619', 'BEN03636', 'BEN03655', 'BEN03667', 'BEN03725', 'BEN03767']:
    f = Image.open(f"scratch/face_{s}.jpg").resize((100, 100)).convert('RGB')
    diff_f = sum(abs(f.getpixel((x, y))[i] - female_face.getpixel((x, y))[i]) for y in range(100) for x in range(100) for i in range(3))
    diff_m = sum(abs(f.getpixel((x, y))[i] - male_face.getpixel((x, y))[i]) for y in range(100) for x in range(100) for i in range(3))
    print(f"{s}: diff_female={diff_f}, diff_male={diff_m}")

