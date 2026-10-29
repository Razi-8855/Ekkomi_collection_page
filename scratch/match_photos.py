import os

asset_files = {}
for root, dirs, files in os.walk('assets/collection/nocturne'):
    for f in files:
        if f.endswith(('.jpg', '.png', '.webp')):
            fp = os.path.join(root, f)
            asset_files[fp] = os.path.getsize(fp)

orig_files = {}
for f in os.listdir('jackets_original'):
    fp = os.path.join('jackets_original', f)
    orig_files[f] = os.path.getsize(fp)

print("Matching assets to originals:")
for ap, asize in sorted(asset_files.items()):
    matches = [of for of, osize in orig_files.items() if osize == asize]
    print(f"{ap} ({asize}b) -> matches: {matches}")

