import subprocess, os
from PIL import Image

profile_dir = r'C:\Users\razi7\OneDrive\Desktop\Documents\ChatGPT\ekkomi\scratch\chrome_prof'
out_file = r'C:\Users\razi7\OneDrive\Desktop\Documents\ChatGPT\ekkomi\scratch\mobile_check\desktop_women_curiosity_view.png'

html_scroller = """<!DOCTYPE html>
<html>
<head><style>body,html{margin:0;padding:0;}</style></head>
<body>
<iframe id="f" src="../index.html" style="width:1280px; height:800px; border:none;"></iframe>
<script>
window.onload = async () => {
  await new Promise(r => setTimeout(r, 1200));
  const f = document.getElementById('f');
  const win = f.contentWindow;
  const doc = f.contentDocument;

  // Switch to women and select curiosity
  doc.getElementById('tab-gender-women').click();
  await new Promise(r => setTimeout(r, 400));
  
  const curiosityPanel = doc.querySelector('#accordionGalleryWomen .ag-panel[data-jacket="women-curiosity"]');
  if (curiosityPanel) curiosityPanel.click();
  await new Promise(r => setTimeout(r, 600));

  const gallery = doc.querySelector('.jacket-gallery-container');
  const offset = 82 + 50 + 10;
  const targetTop = gallery.getBoundingClientRect().top + win.pageYOffset - offset;
  win.scrollTo({ top: targetTop, behavior: 'instant' });
};
</script>
</body>
</html>
"""

with open('scratch/view_women_curiosity.html', 'w', encoding='utf-8') as f:
    f.write(html_scroller)

cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-web-security',
    '--allow-file-access-from-files',
    '--enable-local-file-accesses',
    f'--user-data-dir={profile_dir}',
    '--window-size=1280,800',
    '--virtual-time-budget=5000',
    '--hide-scrollbars',
    '--screenshot=' + out_file,
    r'file:///C:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/scratch/view_women_curiosity.html'
]
subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(out_file):
    im = Image.open(out_file)
    print('Captured women curiosity view screenshot:', im.size)

