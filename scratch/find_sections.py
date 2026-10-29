import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "/* Dynamic Showcase Transitions */"
p1 = text.find(start_marker)
print("p1:", p1)

# Find all occurrences of comments with === or --- after p1
pos = p1
while pos != -1 and pos < len(text):
    p = text.find('/*', pos)
    if p == -1:
        break
    comment_end = text.find('*/', p)
    if comment_end != -1:
        c_body = text[p:comment_end+2]
        if '===' in c_body or '---' in c_body:
            print(f"Section at {p}: {c_body[:100].strip()}")
    pos = p + 2
    if len(text) - pos < 50:
        break
