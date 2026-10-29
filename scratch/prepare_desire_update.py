import os
import re

# =====================================================================
# 1. UPDATE INDEX.HTML & APP.JS FOR WOMEN'S DESIRE (PURGE BEN03806 / desire_lining.jpg)
# =====================================================================

# Load apply_full_fix.py
with open('scratch/apply_full_fix.py', 'r', encoding='utf-8') as f:
    code = f.read()

# In womens_jackets in apply_full_fix.py:
# Make sure desire only has 4 female views (NO desire_lining.jpg)
old_desire_views = """        # 100% FEMALE MODEL & GARMENT DETAIL PHOTOS (ZERO MALE)
        'views': [
            {'label': 'Standing Silhouette', 'src': 'assets/collection/nocturne/desire/desire_editorial_3.jpg', 'alt': "Deep Red jacket — Women's Desire Standing Portrait (Female Model BEN04159)"},
            {'label': 'Back Embroidery', 'src': 'assets/collection/nocturne/desire/desire_back.jpg', 'alt': "Deep Red jacket — Women's Desire Back Embroidery Detail (Female Model BEN04180)"},
            {'label': 'Evening Lounge', 'src': 'assets/collection/nocturne/desire/desire_editorial_1.jpg', 'alt': "Deep Red jacket — Women's Desire Editorial on Sofa (Female Model BEN04137)"},
            {'label': 'Close Profile', 'src': 'assets/collection/nocturne/desire/desire_editorial_2.jpg', 'alt': "Deep Red jacket — Women's Desire Intimate Close-up (Female Model BEN04149)"},
            {'label': 'Illustrated Lining', 'src': 'assets/collection/nocturne/desire/desire_lining.jpg', 'alt': "Deep Red jacket — Women's Desire Illustrated Silk Lining (Garment Detail BEN03806)"}
        ]"""

new_desire_views = """        # 100% FEMALE MODEL PHOTOS (ZERO MALE — BEN03806 PURGED)
        'views': [
            {'label': 'Standing Silhouette', 'src': 'assets/collection/nocturne/desire/desire_editorial_3.jpg', 'alt': "Deep Red jacket — Women's Desire Standing Portrait (Female Model BEN04159)"},
            {'label': 'Back Embroidery', 'src': 'assets/collection/nocturne/desire/desire_back.jpg', 'alt': "Deep Red jacket — Women's Desire Back Embroidery Detail (Female Model BEN04180)"},
            {'label': 'Evening Lounge', 'src': 'assets/collection/nocturne/desire/desire_editorial_1.jpg', 'alt': "Deep Red jacket — Women's Desire Editorial on Sofa (Female Model BEN04137)"},
            {'label': 'Close Profile', 'src': 'assets/collection/nocturne/desire/desire_editorial_2.jpg', 'alt': "Deep Red jacket — Women's Desire Intimate Close-up (Female Model BEN04149)"}
        ]"""

assert old_desire_views in code, "old_desire_views not found in apply_full_fix.py"
code = code.replace(old_desire_views, new_desire_views)

with open('scratch/apply_full_fix.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated scratch/apply_full_fix.py with 4 female views for Women's Desire!")

