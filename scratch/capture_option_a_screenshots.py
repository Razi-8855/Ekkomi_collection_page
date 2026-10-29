import subprocess, os
from PIL import Image

profile_dir = r'C:\Users\razi7\OneDrive\Desktop\Documents\ChatGPT\ekkomi\scratch\chrome_prof'
out_dir = r'C:\Users\razi7\OneDrive\Desktop\Documents\ChatGPT\ekkomi\scratch\mobile_check'
os.makedirs(out_dir, exist_ok=True)

# 1. Desktop view (1280x900)
cmd_desktop = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-web-security',
    '--allow-file-access-from-files',
    '--enable-local-file-accesses',
    f'--user-data-dir={profile_dir}',
    '--window-size=1280,1800',
    '--virtual-time-budget=4000',
    '--hide-scrollbars',
    '--screenshot=' + os.path.join(out_dir, 'option_a_desktop.png'),
    r'file:///C:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/index.html'
]
subprocess.run(cmd_desktop, capture_output=True, text=True)

# 2. Mobile view (390x2400)
cmd_mobile = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-web-security',
    '--allow-file-access-from-files',
    '--enable-local-file-accesses',
    f'--user-data-dir={profile_dir}',
    '--window-size=390,2600',
    '--virtual-time-budget=4000',
    '--hide-scrollbars',
    '--screenshot=' + os.path.join(out_dir, 'option_a_mobile.png'),
    r'file:///C:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/index.html'
]
subprocess.run(cmd_mobile, capture_output=True, text=True)

print("Captured option_a_desktop.png and option_a_mobile.png")

