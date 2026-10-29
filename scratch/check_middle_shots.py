from PIL import Image

for s in ['BEN03307', 'BEN03324', 'BEN03515', 'BEN03619', 'BEN03636', 'BEN03655', 'BEN03667', 'BEN03725', 'BEN03767']:
    p = f"scratch/inspect_all_35/{s}_full.jpg"
    im = Image.open(p)
    w, h = im.size
    face = im.crop((int(w * 0.25), int(h * 0.05), int(w * 0.75), int(h * 0.45)))
    face.resize((200, 200)).save(f"scratch/face_{s}.jpg")

print("Saved faces for 3307 to 3767.")

