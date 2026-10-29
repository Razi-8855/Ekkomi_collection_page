import re

# 1. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Replace scrollToShowcase to always align cleanly
old_scroll_fn = """function scrollToShowcase(smooth = true) {
  const showcase = document.getElementById('productShowcase');
  if (!showcase) return;
  const rect = showcase.getBoundingClientRect();
  const header = document.querySelector('.site-header');
  const navBar = document.querySelector('.collection-nav-bar');
  const offset = (header ? header.offsetHeight : 82) + (navBar ? navBar.offsetHeight : 50) + 16;

  // Only scroll if showcase top is not already comfortably visible in the upper viewport
  const isVisible = rect.top >= offset - 60 && rect.top <= window.innerHeight * 0.45;
  if (!isVisible) {
    const targetTop = rect.top + window.pageYOffset - offset;
    window.scrollTo({
      top: Math.max(0, targetTop),
      behavior: (smooth && !isReducedMotion()) ? 'smooth' : 'auto'
    });
  }
}"""

new_scroll_fn = """function scrollToShowcase(smooth = true) {
  const showcase = document.getElementById('productShowcase');
  if (!showcase) return;
  const header = document.querySelector('.site-header');
  const navBar = document.querySelector('.collection-nav-bar');
  const offset = (header ? header.offsetHeight : 82) + (navBar ? navBar.offsetHeight : 50) + 16;
  const targetTop = showcase.getBoundingClientRect().top + window.pageYOffset - offset;

  window.scrollTo({
    top: Math.max(0, targetTop),
    behavior: (smooth && !isReducedMotion()) ? 'smooth' : 'auto'
  });
}"""

assert old_scroll_fn in app_js, "Could not find old_scroll_fn in app.js"
app_js = app_js.replace(old_scroll_fn, new_scroll_fn, 1)

# In renderShowcase, add quick navigation header row
old_meta_col = """          <div class="jacket-meta-column">
            <div class="jacket-collection-eyebrow">
              <span class="eyebrow-prefix">${departmentTitle}</span>
              <span class="eyebrow-sep">/</span>
              <span class="eyebrow-num">${jacket.number}</span>
            </div>
            <h3 class="jacket-name" id="showcaseJacketTitle">${jacket.impulse}</h3>"""

new_meta_col = """          <div class="jacket-meta-column">
            <div class="jacket-meta-header-row">
              <div class="jacket-collection-eyebrow">
                <span class="eyebrow-prefix">${departmentTitle}</span>
                <span class="eyebrow-sep">/</span>
                <span class="eyebrow-num">${jacket.number}</span>
              </div>
              <div class="jacket-quick-nav">
                <button type="button" class="quick-nav-btn prev-quick-btn" id="prevQuickBtn" aria-label="Previous: ${prevJacket.impulse}" title="Previous jacket">
                  <span aria-hidden="true">&larr;</span>
                </button>
                <span class="quick-nav-counter">${jacket.number} / ${String(currentList.length).padStart(2, '0')}</span>
                <button type="button" class="quick-nav-btn next-quick-btn" id="nextQuickBtn" aria-label="Next: ${nextJacket.impulse}" title="Next jacket">
                  <span aria-hidden="true">&rarr;</span>
                </button>
              </div>
            </div>
            <h3 class="jacket-name" id="showcaseJacketTitle">${jacket.impulse}</h3>"""

assert old_meta_col in app_js, "Could not find old_meta_col in app.js"
app_js = app_js.replace(old_meta_col, new_meta_col, 1)

# Update prevBtn and nextBtn listeners to scroll: true, and wire up quick buttons
old_btn_listeners = """    // Bind Previous / Next Navigation
    const prevBtn = document.getElementById('prevJacketBtn');
    const nextBtn = document.getElementById('nextJacketBtn');

    if (prevBtn) {
      prevBtn.addEventListener('click', (e) => {
        e.preventDefault();
        selectJacket(prevJacket.id, { scroll: false });
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', (e) => {
        e.preventDefault();
        selectJacket(nextJacket.id, { scroll: false });
      });
    }"""

new_btn_listeners = """    // Bind Previous / Next Navigation (Both bottom buttons & top quick buttons)
    const prevBtn = document.getElementById('prevJacketBtn');
    const nextBtn = document.getElementById('nextJacketBtn');
    const prevQuick = document.getElementById('prevQuickBtn');
    const nextQuick = document.getElementById('nextQuickBtn');

    const handlePrev = (e) => {
      e.preventDefault();
      selectJacket(prevJacket.id, { scroll: true });
    };

    const handleNext = (e) => {
      e.preventDefault();
      selectJacket(nextJacket.id, { scroll: true });
    };

    if (prevBtn) prevBtn.addEventListener('click', handlePrev);
    if (nextBtn) nextBtn.addEventListener('click', handleNext);
    if (prevQuick) prevQuick.addEventListener('click', handlePrev);
    if (nextQuick) nextQuick.addEventListener('click', handleNext);"""

assert old_btn_listeners in app_js, "Could not find old_btn_listeners in app.js"
app_js = app_js.replace(old_btn_listeners, new_btn_listeners, 1)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Updated app.js with scroll: true and quick nav header!")

# 2. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add styles for showcase sizing, top center object-position, and quick nav
extra_css = """
/* Sizing refinement: prevent 'half-half' cut-off on dynamic showcase */
.showcase-container {
  width: 100%;
  max-width: var(--container-w, 1400px);
  margin: 0 auto;
  padding: 0 clamp(1.25rem, 4vw, 4rem);
  box-sizing: border-box;
}

.dynamic-product-showcase {
  border-top: 1px solid var(--color-border);
  padding: clamp(2rem, 3.5vw, 3rem) 0;
  margin-top: 1rem;
  transition: opacity 0.22s ease, transform 0.22s ease;
  scroll-margin-top: calc(var(--header-h, 82px) + 54px);
  box-sizing: border-box;
  width: 100%;
}

.jacket-meta-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 12px;
}

.jacket-quick-nav {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(64, 48, 44, 0.05);
  border: 1px solid var(--color-border);
  border-radius: 20px;
  padding: 3px 10px;
}

.quick-nav-btn {
  background: transparent;
  border: none;
  color: var(--color-text);
  font-size: 13px;
  cursor: pointer;
  padding: 2px 6px;
  border-radius: 50%;
  transition: color var(--motion), transform var(--motion);
  line-height: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.quick-nav-btn:hover {
  color: var(--color-accent);
}

.quick-nav-counter {
  font-family: var(--font-sans);
  font-size: 10px;
  letter-spacing: 0.12em;
  color: var(--color-muted);
}

.dynamic-product-showcase .jacket-gallery-editorial {
  display: grid;
  grid-template-columns: minmax(280px, 380px) 1fr;
  gap: clamp(1.5rem, 3.5vw, 3rem);
  align-items: start;
}

.dynamic-product-showcase .gallery-stage {
  position: static !important;
  max-width: 380px;
  width: 100%;
  margin: 0 auto;
  border-radius: 6px;
  overflow: hidden;
  background: #14100e;
  box-shadow: 0 16px 40px -12px rgba(64, 48, 44, 0.2);
  border: 1px solid rgba(64, 48, 44, 0.18);
}

.dynamic-product-showcase .gallery-stage__frame {
  position: relative;
  aspect-ratio: 2 / 3;
  max-height: min(65vh, 520px);
  width: 100%;
  overflow: hidden;
  background: #0f0c0a;
}

.dynamic-product-showcase .gallery-stage__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center !important; /* Keep face and jacket tailoring in focus */
  display: block;
}

.dynamic-product-showcase .gallery-views-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
  gap: 12px;
  max-width: 620px;
}

.dynamic-product-showcase .view-card__img {
  object-position: top center !important;
}

@media (max-width: 900px) {
  .dynamic-product-showcase .jacket-gallery-editorial {
    grid-template-columns: 1fr;
    gap: 1.8rem;
  }
  .dynamic-product-showcase .gallery-stage {
    max-width: 360px;
  }
}

@media (max-width: 480px) {
  .dynamic-product-showcase .gallery-views-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
}
"""

css += "\n" + extra_css
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated styles.css with sizing refinements!")

