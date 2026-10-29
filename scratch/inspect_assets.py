import os, glob

folders = ['curiosity', 'temptation', 'desire', 'audacity', 'insolence']
for fld in folders:
    p = os.path.join('assets', 'collection', 'nocturne', fld)
    if os.path.exists(p):
        files = os.listdir(p)
        print(f"\nFolder: assets/collection/nocturne/{fld}")
        for f in files:
            print("  ", f)

print("\nFiles in jackets_original:")
for f in os.listdir('jackets_original'):
    print("  ", f)

