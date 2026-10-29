with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = text.find('const mensJackets = [')
m2 = text.find('const allCollectionJackets =')

print("Before m1:")
print(text[m1-60:m1])

print("\nAround m2:")
print(text[m2-40:m2+50])

