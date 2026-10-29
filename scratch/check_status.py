import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Jacket sections in index.html:")
for m in re.finditer(r'id="(jacket-[^"]+)"', html):
    print(" - ", m.group(1))

# Check what images are in each section in index.html
sections = re.findall(r'<section class="jacket-detail-section" id="(jacket-[^"]+)".*?</section>', html, re.DOTALL)
for s_id, s_html in [(m.group(1), m.group(0)) for m in re.finditer(r'<section class="jacket-detail-section" id="(jacket-[^"]+)".*?</section>', html, re.DOTALL)]:
    imgs = re.findall(r'src="([^"]+)"', s_html)
    print(f"\n{s_id} has {len(imgs)} img tags:")
    for img in imgs:
        print(f"   {img}")

