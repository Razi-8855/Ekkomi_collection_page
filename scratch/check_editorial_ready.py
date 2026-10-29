import json, re

with open('scratch/jackets_editorial_data.json', 'r', encoding='utf-8') as f:
    editorial = json.load(f)

# Let's inspect all fields of editorial
for k, v in editorial.items():
    print(k, "craft count:", len(v['craft']))

