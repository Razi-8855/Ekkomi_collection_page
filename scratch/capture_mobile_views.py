import subprocess, os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_url = r'file:///C:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/index.html'

# Let's take full page screenshots and section screenshots at 390x844
out_dir = r'C:\Users\razi7\OneDrive\Desktop\Documents\ChatGPT\ekkomi\scratch\mobile_check'
os.makedirs(out_dir, exist_ok=True)

# 1. Full page screenshot at 390px mobile viewport width
cmd_full = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--allow-file-access-from-files',
    '--enable-local-file-accesses',
    '--window-size=390,844',
    '--virtual-time-budget=4000',
    '--default-background-color=0',
    '--hide-scrollbars',
    '--screenshot=' + os.path.join(out_dir, 'phone_viewport_top.png'),
    html_url
]

subprocess.run(cmd_full, capture_output=True, text=True)

# Let's also test deep links to specific sections:
sections = [
    ('collection', '#collection'),
    ('mens_dept', '#mens-department'),
    ('womens_dept', '#womens-department'),
    ('women_curiosity', '#jacket-women-curiosity'),
    ('women_desire', '#jacket-women-desire'),
    ('women_audacity', '#jacket-women-audacity')
]

for name, hash_link in sections:
    out_file = os.path.join(out_dir, f'phone_{name}.png')
    cmd_sec = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        '--allow-file-access-from-files',
        '--enable-local-file-accesses',
        '--window-size=390,844',
        '--virtual-time-budget=3000',
        '--screenshot=' + out_file,
        html_url + hash_link
    ]
    subprocess.run(cmd_sec, capture_output=True, text=True)
    if os.path.exists(out_file):
        im = Image.open(out_file)
        print(f"Captured {name}: {im.size}, {os.path.getsize(out_file)} bytes")

print("Finished capturing mobile screenshots.")

