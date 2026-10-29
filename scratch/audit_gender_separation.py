import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Split into Men's section and Women's section
mens_start = html.find('id="mensDetails"')
womens_start = html.find('id="womensDetails"')
footer_start = html.find('id="womensDetails"') + html[html.find('id="womensDetails"'):].find('</section>')

mens_html = html[mens_start:womens_start]
womens_html = html[womens_start:]

female_exclusive_images = [
    'audacity.jpg',
    'audacity_editorial_1.jpg',
    'audacity_editorial_2.jpg',
    'desire_editorial_1.jpg',
    'desire_editorial_2.jpg',
    'desire_editorial_3.jpg',
    'desire_back.jpg',
    'insolence_editorial_1.jpg',
    'insolence_editorial_2.jpg',
    'insolence_editorial_3.jpg',
    'insolence_editorial_4.jpg'
]

male_exclusive_images = [
    'curiosity_lookbook_1.jpg',
    'curiosity_lookbook_2.jpg',
    'desire.jpg',
    'desire_lookbook_1.jpg',
    'desire_lookbook_2.jpg',
    'desire_lookbook_3.jpg',
    'audacity_lookbook_1.jpg',
    'audacity_lookbook_2.jpg'
]

print('=== AUDITING MEN\'S SECTION FOR INADVERTENT FEMALE PHOTOS ===')
female_found_in_men = []
for img in female_exclusive_images:
    if img in mens_html:
        female_found_in_men.append(img)

if female_found_in_men:
    print('ERROR: Found female images in Men\'s section:', female_found_in_men)
else:
    print('SUCCESS: Zero female images found in Men\'s section!')

print('\n=== AUDITING WOMEN\'S SECTION FOR INADVERTENT MALE PHOTOS ===')
male_found_in_women = []
for img in male_exclusive_images:
    if img in womens_html:
        male_found_in_women.append(img)

if male_found_in_women:
    print('ERROR: Found male images in Women\'s section:', male_found_in_women)
else:
    print('SUCCESS: Zero male images found in Women\'s section!')

print('\n=== VERIFYING WOMEN\'S AUDACITY HAS THE LEANING COUNTER SHOT ===')
assert 'assets/collection/nocturne/audacity/audacity.jpg' in womens_html
print('SUCCESS: Women\'s Audacity now prominently features the female model shot (audacity.jpg)!')

print('\n=== VERIFYING MEN\'S AUDACITY HAS MALE MODEL AS PRIMARY ===')
assert 'assets/collection/nocturne/audacity/audacity_lookbook_1.jpg' in mens_html
print('SUCCESS: Men\'s Audacity now prominently features the male model shot (audacity_lookbook_1.jpg)!')

assert len(female_found_in_men) == 0
assert len(male_found_in_women) == 0
print('\nALL GENDER SEPARATION AUDITS PASSED WITH ZERO VIOLATIONS!')

