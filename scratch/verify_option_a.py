import subprocess, os, json

profile_dir = r'C:\Users\razi7\OneDrive\Desktop\Documents\ChatGPT\ekkomi\scratch\chrome_prof'

html_test = """<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body>
<iframe id="f" src="../index.html" style="width:1200px; height:900px; border:none;"></iframe>
<script>
window.onload = async () => {
  const log = (msg) => console.log('VERIFY_TEST: ' + msg);
  
  await new Promise(r => setTimeout(r, 1200));
  const doc = document.getElementById('f').contentDocument;
  const win = document.getElementById('f').contentWindow;

  // 1. Initial State Check (Men active)
  const tabMen = doc.getElementById('tab-gender-men');
  const tabWomen = doc.getElementById('tab-gender-women');
  const mensDept = doc.getElementById('mens-department');
  const womensDept = doc.getElementById('womens-department');
  const showcase = doc.getElementById('productShowcase');

  log('tabMen exists: ' + !!tabMen + ', isActive: ' + tabMen.classList.contains('is-active'));
  log('tabWomen exists: ' + !!tabWomen + ', isActive: ' + tabWomen.classList.contains('is-active'));
  log('mensDept display: ' + win.getComputedStyle(mensDept).display);
  log('womensDept display: ' + win.getComputedStyle(womensDept).display);

  // 2. Check Accordion Panels in Men
  const menPanels = doc.querySelectorAll('#accordionGalleryMen .ag-panel');
  log('Men accordion panel count: ' + menPanels.length);
  const menLabels = Array.from(menPanels).map(p => p.querySelector('.ag-label-title')?.textContent.trim());
  log('Men accordion labels: ' + JSON.stringify(menLabels));

  // 3. Check Initial Showcase (Desire)
  const titleEl = doc.getElementById('showcaseJacketTitle');
  log('Initial showcase title: ' + (titleEl ? titleEl.textContent : 'none'));
  const stageImg = doc.getElementById('showcaseStageImg');
  log('Initial showcase stage img: ' + (stageImg ? stageImg.src.split('/').slice(-2).join('/') : 'none'));
  const cards = doc.querySelectorAll('#productShowcase .gallery-view-card');
  log('Initial showcase thumbnail cards count: ' + cards.length);

  // 4. Test Navigation Buttons (Next Jacket)
  const nextBtn = doc.getElementById('nextJacketBtn');
  log('Next button exists: ' + !!nextBtn);
  if (nextBtn) {
    nextBtn.click();
    await new Promise(r => setTimeout(r, 400));
    const newTitle = doc.getElementById('showcaseJacketTitle')?.textContent;
    log('Showcase title after Next: ' + newTitle);
  }

  // 5. Test Department Switch to WOMEN
  log('Clicking Women tab...');
  tabWomen.click();
  await new Promise(r => setTimeout(r, 600));

  log('After Women switch:');
  log('tabMen isActive: ' + tabMen.classList.contains('is-active'));
  log('tabWomen isActive: ' + tabWomen.classList.contains('is-active'));
  log('mensDept display: ' + win.getComputedStyle(mensDept).display);
  log('womensDept display: ' + win.getComputedStyle(womensDept).display);

  const womenPanels = doc.querySelectorAll('#accordionGalleryWomen .ag-panel');
  log('Women accordion panel count: ' + womenPanels.length);
  const womenLabels = Array.from(womenPanels).map(p => p.querySelector('.ag-label-title')?.textContent.trim());
  log('Women accordion labels: ' + JSON.stringify(womenLabels));

  const womenTitle = doc.getElementById('showcaseJacketTitle')?.textContent;
  log('Women showcase title: ' + womenTitle);
  const womenStageImg = doc.getElementById('showcaseStageImg')?.src.split('/').slice(-2).join('/');
  log('Women showcase stage img: ' + womenStageImg);
  const womenCards = doc.querySelectorAll('#productShowcase .gallery-view-card');
  log('Women showcase thumbnail cards count: ' + womenCards.length);

  // 6. Test Switching to Curiosity in Women
  const curiosityPanel = doc.querySelector('#accordionGalleryWomen .ag-panel[data-jacket="women-curiosity"]');
  log('Women Curiosity panel exists: ' + !!curiosityPanel);
  if (curiosityPanel) {
    curiosityPanel.click();
    await new Promise(r => setTimeout(r, 400));
    const curTitle = doc.getElementById('showcaseJacketTitle')?.textContent;
    log('Showcase title after clicking Curiosity: ' + curTitle);
    const curCards = doc.querySelectorAll('#productShowcase .gallery-view-card');
    log('Women Curiosity cards count: ' + curCards.length);
    const curImgSrcs = Array.from(curCards).map(c => c.querySelector('img')?.src.split('/').slice(-1)[0]);
    log('Women Curiosity card image filenames: ' + JSON.stringify(curImgSrcs));
  }

  log('ALL_VERIFY_TESTS_COMPLETED');
};
</script>
</body>
</html>
"""

with open('scratch/test_runner_option_a.html', 'w', encoding='utf-8') as f:
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
    '--virtual-time-budget=10000',
    r'file:///C:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/scratch/test_runner_option_a.html'
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
for l in res.stderr.splitlines():
    if 'VERIFY_TEST:' in l:
        print(l.split('VERIFY_TEST:')[-1].strip())

