mens_jackets_code = """const mensJackets = [
  {
    id: 'men-curiosity',
    key: 'curiosity',
    gender: 'men',
    number: '01',
    impulse: 'Curiosity',
    colour: 'Dark Navy',
    hex: '#1c2838',
    image: imgPath('curiosity', 'curiosity.jpg'),
    label: '01 / CURIOSITY',
    sublabel: 'DARK NAVY',
    views: [
      { label: 'Front Silhouette', src: imgPath('curiosity', 'curiosity.jpg'), alt: "Dark Navy jacket — Men's Curiosity Front Silhouette (Male Model)" },
      { label: 'Embroidery Detail', src: imgPath('curiosity', 'curiosity_detail.jpg'), alt: "Dark Navy jacket — Men's Curiosity Tone-on-Tone Embroidery Detail (Male Model)" },
      { label: 'Back Tailoring', src: imgPath('curiosity', 'curiosity_back.jpg'), alt: "Dark Navy jacket — Men's Curiosity Back Construction (Male Model)" },
      { label: 'Illustrated Lining', src: imgPath('curiosity', 'curiosity_lining.jpg'), alt: "Dark Navy jacket — Men's Curiosity Illustrated Silk Lining (Male Model)" },
      { label: 'Lookbook Portrait', src: imgPath('curiosity', 'curiosity_lookbook_1.jpg'), alt: "Dark Navy jacket — Men's Curiosity Lookbook Studio Portrait (Male Model)" },
      { label: 'Lookbook Profile', src: imgPath('curiosity', 'curiosity_lookbook_2.jpg'), alt: "Dark Navy jacket — Men's Curiosity Lookbook Profile View (Male Model)" }
    ]
  },
  {
    id: 'men-temptation',
    key: 'temptation',
    gender: 'men',
    number: '02',
    impulse: 'Temptation',
    colour: 'Forest Green',
    hex: '#27382b',
    image: imgPath('temptation', 'temptation.jpg'),
    label: '02 / TEMPTATION',
    sublabel: 'FOREST GREEN',
    views: [
      { label: 'Front Silhouette', src: imgPath('temptation', 'temptation.jpg'), alt: "Forest Green jacket — Men's Temptation Front Full Body (Male Model)" },
      { label: 'Embroidery Detail', src: imgPath('temptation', 'temptation_detail.jpg'), alt: "Forest Green jacket — Men's Temptation Lapel and Embroidery Detail (Male Model)" },
      { label: 'Back Tailoring', src: imgPath('temptation', 'temptation_back.jpg'), alt: "Forest Green jacket — Men's Temptation Back Collar Embroidery" },
      { label: 'Lookbook Seated', src: imgPath('temptation', 'temptation_lookbook_1.jpg'), alt: "Forest Green jacket — Men's Temptation Seated Lookbook (Male Model)" },
      { label: 'Lookbook Armchair', src: imgPath('temptation', 'temptation_lookbook_2.jpg'), alt: "Forest Green jacket — Men's Temptation Armchair Editorial (Male Model)" }
    ]
  },
  {
    id: 'men-desire',
    key: 'desire',
    gender: 'men',
    number: '03',
    impulse: 'Desire',
    colour: 'Deep Red',
    hex: '#662225',
    image: imgPath('desire', 'desire.jpg'),
    label: '03 / DESIRE',
    sublabel: 'DEEP RED',
    views: [
      { label: 'Front Silhouette', src: imgPath('desire', 'desire.jpg'), alt: "Deep Red jacket — Men's Desire Front Seated (Male Model)" },
      { label: 'Embroidery Detail', src: imgPath('desire', 'desire_detail.jpg'), alt: "Deep Red jacket — Men's Desire Back Tonal Embroidery (Male Model)" },
      { label: 'Illustrated Lining', src: imgPath('desire', 'desire_lining.jpg'), alt: "Deep Red jacket — Men's Desire Illustrated Silk Lining" },
      { label: 'Lookbook Standing', src: imgPath('desire', 'desire_lookbook_1.jpg'), alt: "Deep Red jacket — Men's Desire Full Standing (Male Model)" },
      { label: 'Lookbook Profile', src: imgPath('desire', 'desire_lookbook_2.jpg'), alt: "Deep Red jacket — Men's Desire Side Angle (Male Model)" },
      { label: 'Lookbook Lounge', src: imgPath('desire', 'desire_lookbook_3.jpg'), alt: "Deep Red jacket — Men's Desire Lounge Chair (Male Model)" }
    ]
  },
  {
    id: 'men-audacity',
    key: 'audacity',
    gender: 'men',
    number: '04',
    impulse: 'Audacity',
    colour: 'Deep Mustard',
    hex: '#8c6b24',
    // 100% Male model standing with scarf (BEN03893)
    image: imgPath('audacity', 'audacity_lookbook_1.jpg'),
    label: '04 / AUDACITY',
    sublabel: 'DEEP MUSTARD',
    views: [
      { label: 'Front Silhouette', src: imgPath('audacity', 'audacity_lookbook_1.jpg'), alt: "Deep Mustard jacket — Men's Audacity Styled with Scarf (Male Model)" },
      { label: 'Chest Embroidery', src: imgPath('audacity', 'audacity_lookbook_2.jpg'), alt: "Deep Mustard jacket — Men's Audacity Front Texture (Male Model)" },
      { label: 'Embroidery Detail', src: imgPath('audacity', 'audacity_detail.jpg'), alt: "Deep Mustard jacket — Men's Audacity Chest Embroidery (Male Model)" },
      { label: 'Back Tailoring', src: imgPath('audacity', 'audacity_back.jpg'), alt: "Deep Mustard jacket — Men's Audacity Back View (Male Model)" }
    ]
  },
  {
    id: 'men-insolence',
    key: 'insolence',
    gender: 'men',
    number: '05',
    impulse: 'Insolence',
    colour: 'Black',
    hex: '#1a1716',
    // 100% Male model seated (BEN03324)
    image: imgPath('insolence', 'insolence.jpg'),
    label: '05 / INSOLENCE',
    sublabel: 'BLACK',
    views: [
      { label: 'Front Silhouette', src: imgPath('insolence', 'insolence.jpg'), alt: "Black jacket — Men's Insolence Front Silhouette (Male Model Seated)" },
      { label: 'Embroidery Detail', src: imgPath('insolence', 'insolence_detail.jpg'), alt: "Black jacket — Men's Insolence Subversive Embroidery Detail (Male Model)" },
      { label: 'Back Tailoring', src: imgPath('insolence', 'insolence_back.jpg'), alt: "Black jacket — Men's Insolence Back Shoulder Seams (Male Model)" }
    ]
  }
];

/* -------------------------------------------------------------------
   WOMEN'S COLLECTION DATA (3 JACKETS — 100% FEMALE / CURATED PENDING)
   ------------------------------------------------------------------- */

const womensJackets = [
  {
    id: 'women-curiosity',
    key: 'curiosity',
    gender: 'women',
    number: '01',
    impulse: 'Curiosity',
    colour: 'Dark Navy',
    hex: '#1c2838',
    // Ultra-luxury editorial silhouette preview (ZERO male photography)
    image: 'assets/collection/nocturne/curiosity/curiosity_women_preview.svg',
    label: '01 / CURIOSITY',
    sublabel: 'DARK NAVY · WOMEN',
    isPending: true,
    views: []
  },
  {
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
  },
  {
    id: 'women-audacity',
    key: 'audacity',
    gender: 'women',
    number: '03',
    impulse: 'Audacity',
    colour: 'Deep Mustard',
    hex: '#8c6b24',
    // 100% Female model leaning on counter (BEN04068)
    image: imgPath('audacity', 'audacity.jpg'),
    label: '03 / AUDACITY',
    sublabel: 'MUSTARD · WOMEN',
    views: [
      { label: 'Front Silhouette', src: imgPath('audacity', 'audacity.jpg'), alt: "Deep Mustard jacket — Women's Audacity Front Leaning Silhouette (Female Model BEN04068)" },
      { label: 'Seated Portrait', src: imgPath('audacity', 'audacity_editorial_1.jpg'), alt: "Deep Mustard jacket — Women's Audacity Seated Portrait (Female Model BEN04058)" },
      { label: 'Nocturne Scene', src: imgPath('audacity', 'audacity_editorial_2.jpg'), alt: "Deep Mustard jacket — Women's Audacity with Street Lamp (Female Model BEN04099)" }
    ]
  }
];

"""

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = text.find('const mensJackets = [')
m2 = text.find('const allCollectionJackets =')

if m1 == -1 or m2 == -1:
    raise Exception(f"Cannot find markers in app.js: m1={m1}, m2={m2}")

new_app_js = text[:m1] + mens_jackets_code + text[m2:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(new_app_js)

print("app.js updated successfully with zero cross-gender leaks!")

