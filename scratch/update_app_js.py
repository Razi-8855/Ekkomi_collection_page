import re

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update selectJacket and add scrollToJacket & setupGalleryInteractions
old_select_pattern = re.compile(
    r'/\* -------------------------------------------------------------------\s*JACKET SELECTION.*?async function selectJacket\(id, \{.*?\}\) \{.*?isTransitioning = false;\s*\}',
    re.DOTALL
)

new_select_code = '''/* -------------------------------------------------------------------
   JACKET SELECTION & SCROLLING

   Clicking any jacket selects it in the accordion/nav and smoothly
   scrolls down to that jacket's dedicated details section below.
   Clicking the already-selected jacket smoothly scrolls to it without
   creating duplicate sections or duplicate content.
   ------------------------------------------------------------------- */

function scrollToJacket(id, smooth = true) {
  const target = document.getElementById(`jacket-${id}`);
  if (!target) return;
  const header = document.querySelector('.site-header');
  const headerH = (header ? header.offsetHeight : 82) + 20;
  const targetTop = target.getBoundingClientRect().top + window.pageYOffset - headerH;
  window.scrollTo({
    top: targetTop,
    behavior: (smooth && !isReducedMotion()) ? 'smooth' : 'auto'
  });
}

async function selectJacket(id, { fromCarousel = false, fromAccordion = false, scroll = false } = {}) {
  const item = collectionData.find(j => j.id === id);
  if (!item) return;

  // If clicked again on the same jacket, scroll to its section without duplicating anything
  if (id === selectedJacketId) {
    if (scroll || fromAccordion || fromCarousel) {
      scrollToJacket(id);
    }
    return;
  }

  selectedJacketId = id;
  currentViewIndex = 0;
  syncURL(id);
  renderControls();  /* update active tab */

  /* Synchronize Accordion Gallery if selection came from outside */
  if (!fromAccordion && window.accordionGalleryAPI) {
    window.accordionGalleryAPI.setActiveById(id, false);
  }

  /* Update active class on jacket detail sections */
  document.querySelectorAll('.jacket-detail-section').forEach(s => {
    s.classList.toggle('is-selected', s.id === `jacket-${id}`);
  });

  preloadAdjacent(id);
  preloadViews(item);

  if (scroll || fromAccordion || fromCarousel) {
    scrollToJacket(id);
  }
}

/* -------------------------------------------------------------------
   PRODUCT GALLERY INTERACTIONS (ALL 5 JACKETS)
   Wires up thumbnail cards to swap views into their main stage
   ------------------------------------------------------------------- */

function setupGalleryInteractions() {
  document.querySelectorAll('.gallery-view-card').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.preventDefault();
      const jacketId = btn.dataset.jacketId;
      const src = btn.dataset.src;
      const alt = btn.dataset.alt;
      const label = btn.dataset.label;
      const stageImg = document.getElementById(`stage-img-${jacketId}`);
      const stageCaption = document.getElementById(`stage-caption-${jacketId}`);
      const stage = document.getElementById(`stage-${jacketId}`);

      // Update active state among sibling thumbnail cards for this jacket
      const siblingCards = document.querySelectorAll(`.gallery-view-card[data-jacket-id="${jacketId}"]`);
      siblingCards.forEach(card => {
        const isActive = card === btn;
        card.classList.toggle('is-active', isActive);
        card.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      });

      if (!stageImg) return;
      if (stageImg.getAttribute('src') === src) return;

      if (isReducedMotion()) {
        stageImg.src = src;
        stageImg.alt = alt;
        if (stageCaption) stageCaption.textContent = label;
        return;
      }

      stage?.classList.add('is-switching');
      await delay(160);

      stageImg.src = src;
      stageImg.alt = alt;
      try {
        await stageImg.decode();
      } catch (_) {}

      if (stageCaption) stageCaption.textContent = label;

      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          stage?.classList.remove('is-switching');
        });
      });
    });
  });
}

/* -------------------------------------------------------------------
   SCROLL SPY (KEEPS NAV & ACCORDION IN SYNC ON MANUAL SCROLL)
   ------------------------------------------------------------------- */

function initScrollSpy() {
  if (!('IntersectionObserver' in window)) return;
  const sections = document.querySelectorAll('.jacket-detail-section');
  if (!sections.length) return;

  const observer = new IntersectionObserver((entries) => {
    const visibleEntries = entries.filter(e => e.isIntersecting);
    if (!visibleEntries.length) return;

    visibleEntries.sort((a, b) => b.intersectionRatio - a.intersectionRatio);
    const mostVisible = visibleEntries[0];
    const jacketId = mostVisible.target.dataset.jacket;

    if (jacketId && jacketId !== selectedJacketId) {
      selectedJacketId = jacketId;
      syncURL(jacketId);
      renderControls();
      if (window.accordionGalleryAPI) {
        window.accordionGalleryAPI.setActiveById(jacketId, false);
      }
      document.querySelectorAll('.jacket-detail-section').forEach(s => {
        s.classList.toggle('is-selected', s.id === `jacket-${jacketId}`);
      });
    }
  }, {
    rootMargin: '-15% 0px -45% 0px',
    threshold: [0.15, 0.4, 0.7]
  });

  sections.forEach(s => observer.observe(s));
}'''

match = old_select_pattern.search(code)
if not match:
    print('Error: old_select_pattern not found!')
    exit(1)

code = code[:match.start()] + new_select_code + code[match.end():]

# 2. Update initAccordionGallery click listeners
old_accordion_listeners = '''  // Event Listeners: expand on hover / focus / click
  panelEls.forEach((panel, i) => {
    if (trigger === 'hover') {
      panel.addEventListener('mouseenter', () => setActive(i, true));
    }
    panel.addEventListener('click', (e) => {
      e.preventDefault();
      setActive(i, true);
    });
    panel.addEventListener('focus', () => setActive(i, true));
    panel.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault();
        const next = (i + 1) % count;
        setActive(next, true);
        panelEls[next]?.focus();
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        const prev = (i - 1 + count) % count;
        setActive(prev, true);
        panelEls[prev]?.focus();
      }
    });
  });'''

new_accordion_listeners = '''  // Event Listeners: expand on hover / focus; navigate and scroll on click
  panelEls.forEach((panel, i) => {
    if (trigger === 'hover') {
      panel.addEventListener('mouseenter', () => setActive(i, false));
    }
    panel.addEventListener('click', (e) => {
      e.preventDefault();
      setActive(i, false);
      selectJacket(items[i].id, { scroll: true, fromAccordion: true });
    });
    panel.addEventListener('focus', () => setActive(i, false));
    panel.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        selectJacket(items[i].id, { scroll: true, fromAccordion: true });
      } else if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault();
        const next = (i + 1) % count;
        setActive(next, false);
        panelEls[next]?.focus();
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        const prev = (i - 1 + count) % count;
        setActive(prev, false);
        panelEls[prev]?.focus();
      }
    });
  });'''

if old_accordion_listeners in code:
    code = code.replace(old_accordion_listeners, new_accordion_listeners)
    print('Replaced accordion listeners successfully!')
else:
    print('Warning: old_accordion_listeners exact match not found!')

# 3. Update drift wall tile creation so clicking a drift wall tile navigates and scrolls
old_tile_creation = '''        const tile = document.createElement('div');
        tile.className = 'drift-wall__tile';
        tile.dataset.tileId = tileId;
        tile.dataset.col = String(c);'''

new_tile_creation = '''        const tile = document.createElement('div');
        tile.className = 'drift-wall__tile';
        tile.dataset.tileId = tileId;
        tile.dataset.col = String(c);
        tile.dataset.jacket = item.jacket;
        tile.style.cursor = 'pointer';
        tile.addEventListener('click', () => {
          selectJacket(item.jacket, { scroll: true });
        });'''

if old_tile_creation in code:
    code = code.replace(old_tile_creation, new_tile_creation)
    print('Replaced drift wall tile creation successfully!')
else:
    print('Warning: old_tile_creation not found!')

# 4. Update delegated click
old_delegated = '''document.addEventListener('click', (e) => {
  const ctrl = e.target.closest('[data-jacket]');
  if (!ctrl) return;
  const fromCarousel = !!e.target.closest('#jacketCarousel');
  selectJacket(ctrl.dataset.jacket, { fromCarousel });
});'''

new_delegated = '''document.addEventListener('click', (e) => {
  const ctrl = e.target.closest('[data-jacket]');
  if (!ctrl) return;
  // If clicked inside accordion, drift wall, or gallery card, those have dedicated listeners
  if (ctrl.closest('#accordionGallery') || ctrl.closest('#heroDriftWall') || ctrl.closest('.gallery-view-card')) return;
  const fromCarousel = !!e.target.closest('#jacketCarousel');
  selectJacket(ctrl.dataset.jacket, { scroll: true, fromCarousel });
});'''

if old_delegated in code:
    code = code.replace(old_delegated, new_delegated)
    print('Replaced delegated click listener successfully!')
else:
    print('Warning: old_delegated not found!')

# 5. Update init() to call setupGalleryInteractions and initScrollSpy
old_init_end = '''  initDriftWall();
  initAccordionGallery();
}'''

new_init_end = '''  initDriftWall();
  initAccordionGallery();
  setupGalleryInteractions();
  initScrollSpy();
}'''

if old_init_end in code:
    code = code.replace(old_init_end, new_init_end)
    print('Replaced init() successfully!')
else:
    print('Warning: old_init_end not found!')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print('app.js updated successfully!')

