import os
import re

print("=================================================================")
print("STRICT GENDER SEPARATION AUDIT & ASSET VERIFICATION")
print("=================================================================\n")

# Load index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Load app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Identify all female images from the photoshoot
female_images = [
    'audacity.jpg',
    'audacity_editorial_1.jpg',
    'audacity_editorial_2.jpg',
    'desire_editorial_1.jpg',
    'desire_editorial_2.jpg',
    'desire_editorial_3.jpg',
    'desire_back.jpg',
    'insolence_editorial_1.jpg',
    'insolence_editorial_2.jpg',
    'insolence_editorial_3.jpg',
    'insolence_editorial_4.jpg'
]

# Identify all male images from the photoshoot
male_images = [
    'curiosity.jpg',
    'curiosity_detail.jpg',
    'curiosity_back.jpg',
    'curiosity_lining.jpg',
    'curiosity_lookbook_1.jpg',
    'curiosity_lookbook_2.jpg',
    'temptation.jpg',
    'temptation_detail.jpg',
    'temptation_back.jpg',
    'temptation_lookbook_1.jpg',
    'temptation_lookbook_2.jpg',
    'desire.jpg',
    'desire_detail.jpg',
    'desire_lookbook_1.jpg',
    'desire_lookbook_2.jpg',
    'desire_lookbook_3.jpg',
    'audacity_lookbook_1.jpg',
    'audacity_lookbook_2.jpg',
    'audacity_detail.jpg',
    'audacity_back.jpg',
    'insolence.jpg',
    'insolence_detail.jpg',
    'insolence_back.jpg'
]

# 1. Parse Men's and Women's blocks in index.html
mens_dept_m = re.search(r'<div class="collection-department-block" id="mens-department">.*?</div>\s*<!-- Refined Luxury Divider', html, re.DOTALL)
womens_dept_m = re.search(r'<div class="collection-department-block" id="womens-department">.*?</section>\s*(?=\s*</main>)', html, re.DOTALL)

assert mens_dept_m, "Could not find mens-department in index.html"
assert womens_dept_m, "Could not find womens-department in index.html"

mens_html = mens_dept_m.group(0)
womens_html = womens_dept_m.group(0)

# Audit Men's section in index.html
print("1. Auditing index.html: Men's Department (id='mens-department')...")
mens_violations = []
for f_img in female_images:
    if f_img in mens_html:
        mens_violations.append(f_img)

if mens_violations:
    print(f"[FAIL]: Found female image(s) in Men's department: {mens_violations}")
else:
    print("[PASS]: 0 female images found in Men's department.")

# Audit Women's section in index.html
print("\n2. Auditing index.html: Women's Department (id='womens-department')...")
womens_violations = []
for m_img in male_images:
    if m_img in womens_html:
        womens_violations.append(m_img)

if womens_violations:
    print(f"[FAIL]: Found male image(s) in Women's department: {womens_violations}")
else:
    print("[PASS]: 0 male images found in Women's department.")

# 2. Parse and audit app.js
print("\n3. Auditing app.js: mensJackets and womensJackets data...")
mens_js_m = re.search(r'const mensJackets = \[(.*?)\];\s*/\*', js, re.DOTALL)
womens_js_m = re.search(r'const womensJackets = \[(.*?)\];', js, re.DOTALL)

assert mens_js_m, "Could not find mensJackets in app.js"
assert womens_js_m, "Could not find womensJackets in app.js"

mens_js = mens_js_m.group(1)
womens_js = womens_js_m.group(1)

mens_js_violations = [f for f in female_images if f in mens_js]
womens_js_violations = [m for m in male_images if m in womens_js]

if mens_js_violations:
    print(f"[FAIL]: Found female image(s) in mensJackets in app.js: {mens_js_violations}")
else:
    print("[PASS]: 0 female images found in mensJackets in app.js.")

if womens_js_violations:
    print(f"[FAIL]: Found male image(s) in womensJackets in app.js: {womens_js_violations}")
else:
    print("[PASS]: 0 male images found in womensJackets in app.js.")

# 3. Verify all image files exist on disk
print("\n4. Verifying existence of all referenced assets on disk...")
all_html_srcs = re.findall(r'src="([^"]+)"', html)
missing_assets = []
for s in set(all_html_srcs):
    if s.startswith(('http://', 'https://')):
        continue
    # Strip cachebusters or query strings
    clean_path = s.split('?')[0]
    if not os.path.exists(clean_path):
        missing_assets.append(clean_path)

if missing_assets:
    print(f"[FAIL]: Missing files on disk: {missing_assets}")
else:
    print(f"[PASS]: All {len(set(all_html_srcs))} unique assets in index.html exist on disk.")

# Final Assertion
assert len(mens_violations) == 0
assert len(womens_violations) == 0
assert len(mens_js_violations) == 0
assert len(womens_js_violations) == 0
assert len(missing_assets) == 0

print("\n=================================================================")
print("ALL STRICT GENDER SEPARATION AUDITS PASSED WITH ZERO LEAKS!")
print("=================================================================")
