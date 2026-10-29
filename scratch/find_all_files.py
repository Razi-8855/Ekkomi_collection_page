import os

# Let's inspect which image is in desire and curiosity
all_files = [f for f in os.listdir('jackets_original') if not f.startswith(('resized_', 'compressed_'))]

print(f"Total original files: {len(all_files)}")
for f in sorted(all_files):
    print(f)

