import re, json

# 1. Update app.js
with open('scratch/apply_full_option_a.py', 'r', encoding='utf-8') as f:
    exec(f.read())

# 2. Update styles.css with Option A styles
css_addon = """
/* ===================================================================
   OPTION A: DEPARTMENT TABS & DYNAMIC PRODUCT SHOWCASE STYLING
   =================================================================== */

.collection-department-block {
  transition: opacity 0.35s cubic-bezier(0.2, 0.7, 0.2, 1);
}

.collection-department-block.is-hidden {
  display: none !important;
  opacity: 0;
}

.collection-department-block.is-active {
  display: block;
  opacity: 1;
}

/* Dynamic Showcase Transitions */
.dynamic-product-showcase {
  border-top: 1px solid var(--color-border);
  padding-top: clamp(2.5rem, 5vw, 4.5rem);
  margin-top: 1.5rem;
  transition: opacity 0.22s ease, transform 0.22s ease;
  scroll-margin-top: calc(var(--header-h, 82px) + 54px);
  will-change: opacity, transform;
}

.dynamic-product-showcase.is-updating {
  opacity: 0;
  transform: translateY(8px);
}

/* Understated Showcase Bottom Navigation */
.showcase-bottom-nav {
  margin-top: clamp(2.5rem, 5vw, 4.5rem);
  padding-top: clamp(1.5rem, 3vw, 2.5rem);
  border-top: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.showcase-nav-btn {
  background: transparent;
  border: 1px solid var(--color-border);
  border-radius: 30px;
  padding: 10px 22px;
  display: inline-flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  color: var(--color-text);
  font-family: var(--font-sans);
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  transition: all var(--motion);
  outline: none;
  -webkit-tap-highlight-color: transparent;
}

.showcase-nav-btn:hover {
  border-color: var(--color-accent);
  color: var(--color-accent);
  background: rgba(119, 58, 60, 0.04);
}

.showcase-nav-btn .nav-arrow {
  font-size: 14px;
  transition: transform var(--motion);
}

.prev-jacket-btn:hover .nav-arrow {
  transform: translateX(-4px);
}

.next-jacket-btn:hover .nav-arrow {
  transform: translateX(4px);
}

.showcase-nav-btn .nav-label-wrap {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}

.next-jacket-btn .nav-label-wrap {
  align-items: flex-end;
  text-align: right;
}

.nav-sub {
  font-size: 9px;
  color: var(--color-muted);
  letter-spacing: 0.16em;
  line-height: 1.2;
}

.nav-jacket-name {
  font-weight: 500;
  color: var(--color-text);
  line-height: 1.3;
}

.showcase-nav-btn:hover .nav-jacket-name {
  color: var(--color-accent);
}

@media (max-width: 600px) {
  .showcase-bottom-nav {
    flex-direction: column;
    gap: 1rem;
  }
  .showcase-nav-btn {
    width: 100%;
    justify-content: space-between;
    padding: 12px 20px;
  }
  .showcase-bottom-nav .nav-back-link {
    order: -1;
    margin-bottom: 0.5rem;
  }
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if '/* ===================================================================\n   OPTION A: DEPARTMENT TABS & DYNAMIC PRODUCT SHOWCASE STYLING' not in css_content:
    css_content += "\n" + css_addon
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("styles.css updated with Option A styles")

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate from <section class="collection-showcase-section" id="collection" down to </section></main>
sec_start = html.find('<section class="collection-showcase-section" id="collection"')
sec_end = html.find('</section></main>')

assert sec_start != -1 and sec_end != -1, "Could not find collection section boundaries"

new_collection_section = '''<section class="collection-showcase-section" id="collection" role="region" aria-label="Nocturne collection">
      
      <!-- Top Department Switcher Bar -->
      <div class="collection-nav-bar" id="collectionNavBar">
        <div class="section">
          <div class="collection-gender-switch" role="tablist" aria-label="Nocturne collection departments">
            <button class="gender-switch-btn is-active" id="tab-gender-men" type="button" role="tab" aria-selected="true" data-department="men">
              <span class="gender-label">MEN</span>
              <span class="gender-badge">05 Styles</span>
            </button>
            <span class="gender-switch-divider" aria-hidden="true">/</span>
            <button class="gender-switch-btn" id="tab-gender-women" type="button" role="tab" aria-selected="false" data-department="women">
              <span class="gender-label">WOMEN</span>
              <span class="gender-badge">03 Styles</span>
            </button>
          </div>
        </div>
      </div>

      <!-- ============================================================
           1. MEN'S COLLECTION (5 Jackets)
           Curiosity, Temptation, Desire, Audacity, Insolence
           ============================================================ -->
      <div class="collection-department-block is-active" id="mens-department" data-department="men">
        <header class="section collection-department-header" id="mens-collection">
          <div class="department-header-inner">
            <span class="department-eyebrow">The Nocturne Edit</span>
            <h2 class="department-title">Men&#8217;s Collection</h2>
            <p class="department-subtitle">Five expressions of instinct.</p>
          </div>
        </header>

        <!-- Accordion Gallery Container (Men's 5 panels) -->
        <div class="section accordion-gallery-container">
          <div id="accordionGalleryMen" class="accordion-gallery" role="list" aria-label="Men's Nocturne jackets gallery"></div>
        </div>
      </div>

      <!-- ============================================================
           2. WOMEN'S COLLECTION (3 Jackets)
           Curiosity, Desire, Audacity
           ============================================================ -->
      <div class="collection-department-block is-hidden" id="womens-department" data-department="women" style="display: none;">
        <header class="section collection-department-header" id="womens-collection">
          <div class="department-header-inner">
            <span class="department-eyebrow">The Nocturne Edit</span>
            <h2 class="department-title">Women&#8217;s Collection</h2>
            <p class="department-subtitle">Three expressions of instinct.</p>
          </div>
        </header>

        <!-- Accordion Gallery Container (Women's 3 panels) -->
        <div class="section accordion-gallery-container">
          <div id="accordionGalleryWomen" class="accordion-gallery" role="list" aria-label="Women's Nocturne jackets gallery"></div>
        </div>
      </div>

      <!-- ============================================================
           3. DYNAMIC PRODUCT SHOWCASE (Single in-place showcase)
           Directly beneath the carousel, updates dynamically
           ============================================================ -->
      <div class="site-container showcase-container">
        <section class="jacket-detail-section dynamic-product-showcase" id="productShowcase" aria-live="polite">
          <!-- Dynamically populated and transitioned by app.js (Initial state rendered on boot) -->
        </section>
      </div>

    '''

new_html = html[:sec_start] + new_collection_section + html[sec_end:]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("index.html updated successfully! New size:", len(new_html))

