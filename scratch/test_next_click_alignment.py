import subprocess, os
from PIL import Image

profile_dir = r'C:\Users\razi7\OneDrive\Desktop\Documents\ChatGPT\ekkomi\scratch\chrome_prof'
out_dir = r'C:\Users\razi7\OneDrive\Desktop\Documents\ChatGPT\ekkomi\scratch\mobile_check'
os.makedirs(out_dir, exist_ok=True)

html_test = """<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="margin:0; padding:0;">
<iframe id="f" src="../index.html" style="width:1280px; height:800px; border:none;"></iframe>
<script>
window.onload = async () => {
  const f = document.getElementById('f');
  const doc = f.contentDocument;
  const win = f.contentWindow;

  await new Promise(r => setTimeout(r, 1200));

  // 1. Check initial scroll and state
  console.log('INIT_JACKET: ' + doc.getElementById('showcaseJacketTitle')?.textContent);

  // 2. Click Next Jacket at the bottom
  const nextBtn = doc.getElementById('nextJacketBtn');
  console.log('NEXT_BTN_EXISTS: ' + !!nextBtn);
  if (nextBtn) {
    // Scroll window down to bottom so button is clicked
    win.scrollTo(0, 2000);
    await new Promise(r => setTimeout(r, 400));
    console.log('SCROLLED_TO_BOTTOM: ' + win.pageYOffset);

    // Click Next
    nextBtn.click();
    await new Promise(r => setTimeout(r, 800));

    const newTitle = doc.getElementById('showcaseJacketTitle')?.textContent;
    const scrollYAfter = win.pageYOffset;
    const showcaseRect = doc.getElementById('productShowcase')?.getBoundingClientRect();

    console.log('AFTER_NEXT_TITLE: ' + newTitle);
    console.log('AFTER_NEXT_SCROLL_Y: ' + scrollYAfter);
    console.log('SHOWCASE_TOP_RECT: ' + showcaseRect.top);
  }
};
</script>
</body>
</html>
"""

with open('scratch/test_next_scroll.html', 'w', encoding='utf-8') as f:
    f.write(html_test)

cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-web-security',
    '--allow-file-access-from-files',
    '--enable-local-file-accesses',
    f'--user-data-dir={profile_dir}',
    '--enable-logging=stderr',
    '--log-level=0',
    '--virtual-time-budget=6000',
    r'file:///C:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/scratch/test_next_scroll.html'
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
for l in res.stderr.splitlines():
    if any(k in l for k in ['INIT_JACKET', 'SCROLLED_TO', 'AFTER_NEXT', 'SHOWCASE_TOP']):
        print(l)

