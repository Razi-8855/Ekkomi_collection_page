import subprocess, os, re

# We can test layout overflow by creating a test runner html that loads index.html in an iframe or evaluates it
html_test = """
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body>
<iframe id="testFrame" src="index.html" style="border:none;"></iframe>
<script>
async function runTest(width) {
  const frame = document.getElementById('testFrame');
  frame.style.width = width + 'px';
  frame.style.height = '844px';
  await new Promise(r => setTimeout(r, 1000));
  
  const doc = frame.contentDocument;
  const win = frame.contentWindow;
  
  const scrollW = doc.documentElement.scrollWidth;
  const clientW = doc.documentElement.clientWidth;
  const bodyScrollW = doc.body.scrollWidth;
  
  // Find overflowing elements if any
  const overflowing = [];
  const all = doc.querySelectorAll('*');
  for (let el of all) {
    const rect = el.getBoundingClientRect();
    if (rect.right > width + 1) {
      overflowing.push({
        tag: el.tagName,
        cls: el.className,
        id: el.id,
        right: Math.round(rect.right),
        width: Math.round(rect.width)
      });
    }
  }
  
  console.log('WIDTH_' + width + ': clientW=' + clientW + ', scrollW=' + scrollW + ', bodyScrollW=' + bodyScrollW + ', hasOverflow=' + (scrollW > clientW));
  if (overflowing.length > 0) {
    console.log('OVERFLOW_ELEMENTS_' + width + ':', JSON.stringify(overflowing.slice(0, 10)));
  }
}

window.onload = async () => {
  for (let w of [320, 360, 375, 390, 414, 430]) {
    await runTest(w);
  }
  console.log('ALL_TESTS_DONE');
};
</script>
</body>
</html>
"""

with open('scratch/test_iframe_overflow.html', 'w', encoding='utf-8') as f:
    f.write(html_test)

print("Saved scratch/test_iframe_overflow.html")

