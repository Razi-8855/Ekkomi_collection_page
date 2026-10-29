with open('scratch/update_app_js_clean.py', 'r', encoding='utf-8') as f:
    code = f.read()

old_desire_js = """  {
    id: 'women-desire',
    key: 'desire',
    gender: 'women',
    number: '02',
    impulse: 'Desire',
    colour: 'Deep Red',
    hex: '#662225',
    // 100% Female model standing portrait (BEN04159)
    image: imgPath('desire', 'desire_editorial_3.jpg'),
    label: '02 / DESIRE',
    sublabel: 'DEEP RED · WOMEN',
    views: [
      { label: 'Standing Silhouette', src: imgPath('desire', 'desire_editorial_3.jpg'), alt: "Deep Red jacket — Women's Desire Standing Portrait (Female Model BEN04159)" },
      { label: 'Back Embroidery', src: imgPath('desire', 'desire_back.jpg'), alt: "Deep Red jacket — Women's Desire Back Embroidery Detail (Female Model BEN04180)" },
      { label: 'Evening Lounge', src: imgPath('desire', 'desire_editorial_1.jpg'), alt: "Deep Red jacket — Women's Desire Editorial on Sofa (Female Model BEN04137)" },
      { label: 'Close Profile', src: imgPath('desire', 'desire_editorial_2.jpg'), alt: "Deep Red jacket — Women's Desire Intimate Close-up (Female Model BEN04149)" },
      { label: 'Illustrated Lining', src: imgPath('desire', 'desire_lining.jpg'), alt: "Deep Red jacket — Women's Desire Illustrated Silk Lining (Garment Detail BEN03806)" }
    ]
  },"""

new_desire_js = """  {
    id: 'women-desire',
    key: 'desire',
    gender: 'women',
    number: '02',
    impulse: 'Desire',
    colour: 'Deep Red',
    hex: '#662225',
    // 100% Female model standing portrait (BEN04159)
    image: imgPath('desire', 'desire_editorial_3.jpg'),
    label: '02 / DESIRE',
    sublabel: 'DEEP RED · WOMEN',
    views: [
      { label: 'Standing Silhouette', src: imgPath('desire', 'desire_editorial_3.jpg'), alt: "Deep Red jacket — Women's Desire Standing Portrait (Female Model BEN04159)" },
      { label: 'Back Embroidery', src: imgPath('desire', 'desire_back.jpg'), alt: "Deep Red jacket — Women's Desire Back Embroidery Detail (Female Model BEN04180)" },
      { label: 'Evening Lounge', src: imgPath('desire', 'desire_editorial_1.jpg'), alt: "Deep Red jacket — Women's Desire Editorial on Sofa (Female Model BEN04137)" },
      { label: 'Close Profile', src: imgPath('desire', 'desire_editorial_2.jpg'), alt: "Deep Red jacket — Women's Desire Intimate Close-up (Female Model BEN04149)" }
    ]
  },"""

assert old_desire_js in code, "old_desire_js not found in update_app_js_clean.py"
code = code.replace(old_desire_js, new_desire_js)

with open('scratch/update_app_js_clean.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated scratch/update_app_js_clean.py with 4 female views for Women's Desire!")

