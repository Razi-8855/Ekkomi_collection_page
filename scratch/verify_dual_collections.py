import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

print('=== 1. CHECKING DEPARTMENT ELEMENTS ===')
assert 'id="mens-collection"' in html, "Missing #mens-collection"
assert 'id="womens-collection"' in html, "Missing #womens-collection"
assert 'id="accordionGalleryMen"' in html, "Missing #accordionGalleryMen"
assert 'id="accordionGalleryWomen"' in html, "Missing #accordionGalleryWomen"
assert 'id="mensDetails"' in html, "Missing #mensDetails"
assert 'id="womensDetails"' in html, "Missing #womensDetails"
print('Department root elements: OK')

print('\n=== 2. CHECKING MEN\'S JACKETS (5 TOTAL) ===')
mens_expected = ['curiosity', 'temptation', 'desire', 'audacity', 'insolence']
for k in mens_expected:
    sec_id = f'jacket-men-{k}'
    assert f'id="{sec_id}"' in html, f"Missing section {sec_id}"
    assert f'id="stage-img-men-{k}"' in html, f"Missing stage img for men-{k}"
    print(f'  Men\'s {k:12} section: FOUND')

print('\n=== 3. CHECKING WOMEN\'S JACKETS (3 TOTAL) ===')
womens_expected = ['curiosity', 'desire', 'audacity']
for k in womens_expected:
    sec_id = f'jacket-women-{k}'
    assert f'id="{sec_id}"' in html, f"Missing section {sec_id}"
    assert f'id="stage-img-women-{k}"' in html, f"Missing stage img for women-{k}"
    print(f'  Women\'s {k:10} section: FOUND')

print('\n=== 4. CONFIRMING EXCLUDED STYLES IN WOMEN\'S ===')
assert 'jacket-women-temptation' not in html, "Error: Temptation should not be in Women's"
assert 'jacket-women-insolence' not in html, "Error: Insolence should not be in Women's"
print('  Temptation & Insolence correctly omitted from Women\'s: OK')

print('\n=== 5. CHECKING WOMEN\'S MODEL ACCURACY ===')
# Women's Desire must contain the female editorial shots
assert 'desire_editorial_3.jpg' in html, "Women's desire should have standing female portrait"
assert 'desire_editorial_1.jpg' in html, "Women's desire should have sofa female portrait"
# Women's Audacity must contain female editorial shots
assert 'audacity_editorial_1.jpg' in html, "Women's audacity should have seated female portrait"
# Women's Curiosity must not use male lookbook shots
womens_curiosity_match = re.search(r'id="jacket-women-curiosity".*?</section>', html, re.DOTALL)
assert womens_curiosity_match, "Women's curiosity section not found"
wc_text = womens_curiosity_match.group(0)
assert 'curiosity_lookbook_1.jpg' not in wc_text, "Male lookbook should not be in Women's Curiosity"
assert 'curiosity_lookbook_2.jpg' not in wc_text, "Male lookbook should not be in Women's Curiosity"
assert 'photography in production' in wc_text.lower(), "Production note should be in Women's Curiosity"
print('  Women\'s model accuracy & photography separation: OK')

print('\n=== 6. CHECKING IMAGE ASSETS EXISTENCE ON DISK ===')
all_images = re.findall(r'src="([^"]+\.(?:jpg|png|webp))"', html)
missing = []
for img_path in all_images:
    # clean query string if any
    clean_path = img_path.split('?')[0]
    if not os.path.exists(clean_path):
        missing.append(img_path)

print(f'  Checked {len(all_images)} total image instances in index.html.')
if missing:
    print('  MISSING IMAGES:', missing)
    raise AssertionError(f'Missing images: {missing}')
else:
    print('  All images exist on disk without 404s: OK')

print('\n=== ALL DUAL COLLECTION VALIDATIONS PASSED! ===')

