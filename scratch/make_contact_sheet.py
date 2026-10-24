import os
from PIL import Image

shots = ['BEN03124', 'BEN03136', 'BEN03137', 'BEN03166', 'BEN03202', 'BEN03212', 
         'BEN03307', 'BEN03324', 'BEN03515', 'BEN03619', 'BEN03636', 'BEN03655', 
         'BEN03667', 'BEN03725', 'BEN03767', 'BEN03806', 'BEN03835', 'BEN03870', 
         'BEN03893', 'BEN03898', 'BEN03906', 'BEN03911', 'BEN04004', 'BEN04014', 
         'BEN04015', 'BEN04031', 'BEN04053', 'BEN04058', 'BEN04068', 'BEN04099', 
         'BEN04137', 'BEN04149', 'BEN04159', 'BEN04180', 'DSC04253']

all_files = os.listdir('jackets_original')
os.makedirs('scratch/clean_thumbs', exist_ok=True)

def get_shot_file(shot):
    candidates = [f for f in all_files if shot in f and not f.startswith(('resized_', 'compressed_'))]
    if not candidates:
        candidates = [f for f in all_files if shot in f]
    candidates.sort(key=lambda x: (x.endswith('.png'), x.endswith('.webp'), x.endswith('.jpg')))
    return os.path.join('jackets_original', candidates[0])

html_cards = []
for s in shots:
    p = get_shot_file(s)
    thumb_path = f'scratch/clean_thumbs/{s}.jpg'
    if not os.path.exists(thumb_path):
        with Image.open(p) as img:
            im = img.convert('RGB')
            im.thumbnail((300, 450))
            im.save(thumb_path, 'JPEG', quality=85)
    html_cards.append(f'''
    <div style="border:1px solid #333; padding:8px; border-radius:6px; background:#1c1c1c; text-align:center;">
      <img src="clean_thumbs/{s}.jpg" style="width:100%; max-width:200px; height:auto; border-radius:4px; display:block; margin:0 auto;" />
      <div style="font-weight:bold; margin-top:8px; font-family:sans-serif; color:#eee;">{s}</div>
      <div style="font-size:11px; color:#888; font-family:sans-serif; word-break:break-all;">{os.path.basename(p)}</div>
    </div>
    ''')

cards_joined = '\n'.join(html_cards)
html = f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Ekkomi Photoshoot Shots (35 items)</title></head>
<body style="background:#0a0a0a; color:#fff; font-family:sans-serif; padding:24px;">
  <h1 style="margin-bottom:20px;">Ekkomi Photoshoot Shots (35 items in jackets_original)</h1>
  <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(200px, 1fr)); gap:16px;">
    {cards_joined}
  </div>
</body>
</html>'''

with open('scratch/contact_sheet.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Contact sheet generated successfully!')
