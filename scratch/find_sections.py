with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l for k in ['mens-department', 'womens-department', 'mensDetails', 'womensDetails', 'jacket-men-curiosity', 'jacket-women-audacity', 'department-separator']):
        print(f'{i}: {l.strip()[:100]}')

