import json

with open('scratch/jackets_editorial_data.json', 'r', encoding='utf-8') as f:
    editorial = json.load(f)

print("Editorial keys:", list(editorial.keys()))

