with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('site-container showcase-container', 'showcase-container')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html showcase-container class successfully!")

