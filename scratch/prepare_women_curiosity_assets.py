import os
from PIL import Image

uploaded = {
    'stand': 'C:/Users/razi7/.gemini/antigravity/brain/ca9db15d-74e4-425d-899e-b554016f82b2/.user_uploaded/media_1793208837468_8f46ee57.jpg',
    'profile': 'C:/Users/razi7/.gemini/antigravity/brain/ca9db15d-74e4-425d-899e-b554016f82b2/.user_uploaded/media_1793208847591_736303a5.webp',
    'down': 'C:/Users/razi7/.gemini/antigravity/brain/ca9db15d-74e4-425d-899e-b554016f82b2/.user_uploaded/media_1793208852982_351aaef0.jpg',
    'portrait': 'C:/Users/razi7/.gemini/antigravity/brain/ca9db15d-74e4-425d-899e-b554016f82b2/.user_uploaded/media_1793208864022_8a5f20f3.jpg',
    'back': 'C:/Users/razi7/.gemini/antigravity/brain/ca9db15d-74e4-425d-899e-b554016f82b2/.user_uploaded/media_1793208870021_40228d14.jpg'
}

existing_highres = {
    'stand': 'assets/collection/nocturne/insolence/insolence_editorial_1.jpg',
    'profile': 'assets/collection/nocturne/insolence/insolence_editorial_2.jpg',
    'down': 'assets/collection/nocturne/insolence/insolence_editorial_3.jpg',
    'portrait': 'assets/collection/nocturne/insolence/insolence_editorial_4.jpg'
}

dest_dir = 'assets/collection/nocturne/curiosity'
os.makedirs(dest_dir, exist_ok=True)

# 1. Standing silhouette (Upload 1 / High-res 1200x1800)
im_stand = Image.open(existing_highres['stand']).convert('RGB')
im_stand.save(os.path.join(dest_dir, 'curiosity_women_1.jpg'), quality=95)
print("Saved curiosity_women_1.jpg (Standing Silhouette) - 1200x1800")

# 2. Embroidery detail / Close portrait (Upload 4 / High-res 1200x1800)
im_portrait = Image.open(existing_highres['portrait']).convert('RGB')
im_portrait.save(os.path.join(dest_dir, 'curiosity_women_2.jpg'), quality=95)
print("Saved curiosity_women_2.jpg (Embroidery Detail) - 1200x1800")

# 3. Back tailoring (Upload 5 - 682x1024 -> 1200x1800 high quality)
im_back = Image.open(uploaded['back']).convert('RGB')
im_back_1800 = im_back.resize((1200, 1800), Image.Resampling.LANCZOS)
im_back_1800.save(os.path.join(dest_dir, 'curiosity_women_3.jpg'), quality=95)
print("Saved curiosity_women_3.jpg (Back Tailoring) - 1200x1800")

# 4. Studio profile (Upload 2 / High-res 1200x1800)
im_profile = Image.open(existing_highres['profile']).convert('RGB')
im_profile.save(os.path.join(dest_dir, 'curiosity_women_4.jpg'), quality=95)
print("Saved curiosity_women_4.jpg (Studio Profile) - 1200x1800")

# 5. Editorial seated (Upload 3 / High-res 1200x1800)
im_down = Image.open(existing_highres['down']).convert('RGB')
im_down.save(os.path.join(dest_dir, 'curiosity_women_5.jpg'), quality=95)
print("Saved curiosity_women_5.jpg (Editorial Seated) - 1200x1800")

print("\nAll 5 Women's Curiosity images generated successfully in assets/collection/nocturne/curiosity/!")

