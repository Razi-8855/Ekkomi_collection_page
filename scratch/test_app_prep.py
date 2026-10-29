import json

with open('scratch/jackets_editorial_data.json', 'r', encoding='utf-8') as f:
    editorial = json.load(f)

# Let's inspect men-curiosity combined
print("Sample editorial for men-curiosity:")
print(json.dumps(editorial['men-curiosity'], indent=2))

