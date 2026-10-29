import os
from PIL import Image

# Known female shots:
# BEN04058, BEN04068, BEN04099 (Audacity - Mustard)
# BEN04137, BEN04149, BEN04159, BEN04180 (Desire - Red)
# DSC04253 (Insolence - Black)

# Let's inspect all 35 shots!
# Specifically, are there any female shots among BEN03124 - BEN03767 or BEN04014 - BEN04053?
# Let's write an HTML gallery of all 35 shots with their head and torso crops so we can inspect every single one!

html = """<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>All 35 Shots Inspection</title>
<style>
body { background: #111; color: #fff; font-family: sans-serif; padding: 20px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }
.card { background: #222; border: 1px solid #444; border-radius: 8px; padding: 12px; text-align: center; }
.card img { width: 100%; height: auto; border-radius: 4px; margin-bottom: 8px; }
.title { font-weight: bold; font-size: 16px; margin-bottom: 4px; }
.crops { display: flex; gap: 8px; justify-content: center; }
.crops img { width: 120px; height: 120px; object-fit: cover; }
</style>
</head>
<body>
<h1>All 35 Shots in jackets_original</h1>
<div class="grid">
"""

all_files = sorted([f for f in os.listdir('scratch/inspect_all_35') if f.endswith('_full.jpg')])
for f in all_files:
    prefix = f.replace('_full.jpg', '')
    html += f"""
    <div class="card">
        <div class="title">{prefix}</div>
        <img src="{prefix}_full.jpg" alt="{prefix} full">
        <div class="crops">
            <img src="{prefix}_head.jpg" alt="{prefix} head">
            <img src="{prefix}_torso.jpg" alt="{prefix} torso">
        </div>
    </div>
    """

html += """
</div>
</body>
</html>
"""

with open('scratch/inspect_all_35/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated scratch/inspect_all_35/index.html")

