import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_m = re.search(r'<!--\s*=+\s*NOCTURNE COLLECTION: DUAL EDIT', html)
if start_m:
    print('Found start comment at index:', start_m.start())
    start_pos = start_m.start()
else:
    s2 = html.find('class="collection-showcase-section"')
    print('s2:', s2)
    start_pos = s2

# Find end before </main>
end_m = re.search(r'</section>\s*(?=\s*</main>)', html)
if end_m:
    print('Found end section at index:', end_m.start(), end_m.end())
    end_pos = end_m.end()

print("Substr preview at start:")
print(html[start_pos:start_pos+150])
print("\nSubstr preview at end:")
print(html[end_pos-100:end_pos+100])

