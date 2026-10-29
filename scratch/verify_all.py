import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

jackets = ['curiosity', 'temptation', 'desire', 'audacity', 'insolence']
all_ok = True

for j in jackets:
    if f'id="jacket-{j}"' not in html:
        print(f'FAIL: id="jacket-{j}" not found')
        all_ok = False
        continue
    if f'id="title-{j}"' not in html:
        print(f'FAIL: id="title-{j}" not found')
        all_ok = False
    if f'id="stage-{j}"' not in html:
        print(f'FAIL: id="stage-{j}" not found')
        all_ok = False
    if f'id="stage-img-{j}"' not in html:
        print(f'FAIL: id="stage-img-{j}" not found')
        all_ok = False
        
    # extract all img src for this jacket
    sec_match = re.search(rf'<section[^>]*id="jacket-{j}".*?</section>', html, re.DOTALL)
    if sec_match:
        sec_text = sec_match.group(0)
        img_srcs = re.findall(r'src="([^"]+)"', sec_text)
        print(f'OK: jacket-{j:10} | Found {len(img_srcs)} image elements')
        for s in img_srcs:
            if not os.path.exists(s):
                print(f'  MISSING IMAGE: {s}')
                all_ok = False

# check required root elements
for el_id in ['accordionGallery', 'heroDriftWall', 'impulseNav', 'jacketsDetails']:
    if f'id="{el_id}"' in html:
        print(f'OK: element id="{el_id}" found')
    else:
        print(f'FAIL: element id="{el_id}" NOT found')
        all_ok = False

if all_ok:
    print('\nALL VERIFICATIONS PASSED!')
else:
    print('\nSOME CHECKS FAILED!')
