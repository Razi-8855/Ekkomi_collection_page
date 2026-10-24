'use strict';

/* ===================================================================
   EKKOMI — NOCTURNE COLLECTION
   Data & Interaction Logic
   =================================================================== */

/* -------------------------------------------------------------------
   ROOT CAUSE — BLANK JACKET IMAGE PANEL (documented per amendment 1)

   The original selectJacket() set img.src then immediately removed the
   `.is-changing` class (which held opacity:0). The CSS opacity transition
   therefore ran while the browser was still fetching / decoding the new
   JPG → the panel showed blank/white for the entire download time.

   Fix: after swapping img.src, call await img.decode(). This Promise
   resolves only once the browser has the pixel data ready to paint.
   The fade-in transition is triggered AFTER decode completes, so the
   image is never briefly invisible.
   ------------------------------------------------------------------- */

/* -------------------------------------------------------------------
   IMAGE PATHS — swap these when production photos arrive.

   Current files (all distinct):
     assets/collection/nocturne/curiosity/curiosity.jpg   — Dark Navy
     assets/collection/nocturne/temptation/temptation.jpg — Forest Green
     assets/collection/nocturne/desire/desire.jpg         — Deep Red
     assets/collection/nocturne/audacity/audacity.jpg     — Deep Mustard
     assets/collection/nocturne/insolence/insolence.jpg   — Black

   Recommended spec: 4:5 portrait, ~1200 × 1500 px, JPG ≤ 400 KB.
   ------------------------------------------------------------------- */

const IMAGE_BASE = 'assets/collection/nocturne';
const IMG_V = '?v=original';
const imgPath = (folder, file) => `${IMAGE_BASE}/${folder}/${file}${IMG_V}`;

const collectionData = [
  {
    id: 'curiosity',
    number: '01',
    impulse: 'Curiosity',
    colour: 'Dark Navy',
    image: imgPath('curiosity', 'curiosity.jpg'),
    views: [
      { label: 'Front',      src: imgPath('curiosity', 'curiosity.jpg'),            alt: 'Dark Navy jacket — Curiosity Front' },
      { label: 'Detail',     src: imgPath('curiosity', 'curiosity_detail.jpg'),     alt: 'Dark Navy jacket — Curiosity Embroidery Detail' },
      { label: 'Back',       src: imgPath('curiosity', 'curiosity_back.jpg'),       alt: 'Dark Navy jacket — Curiosity Back' },
      { label: 'Lining',     src: imgPath('curiosity', 'curiosity_lining.jpg'),     alt: 'Dark Navy jacket — Curiosity Illustrated Lining' },
      { label: 'Lookbook 1', src: imgPath('curiosity', 'curiosity_lookbook_1.jpg'), alt: 'Dark Navy jacket — Curiosity Male Model Lookbook' },
      { label: 'Lookbook 2', src: imgPath('curiosity', 'curiosity_lookbook_2.jpg'), alt: 'Dark Navy jacket — Curiosity Male Model Side Profile' }
    ],
    headline: 'They told you curiosity was dangerous. It is also how every new world is found.',
    narrative: 'Curiosity refuses the comfort of the already known. It looks twice, asks another question, follows the detail others might pass by. Rendered in deep navy suede, intricate tone-on-tone embroidery rewards that same instinct — receding into the surface at first glance, then revealing more as light moves across it. A piece made for those who would rather discover than simply be shown.',
    material: 'Dyed suede gives the jacket its depth, structure and tactile character.',
    embroidery: 'Tone-on-tone embroidery moves quietly across the surface, designed to reward a closer look rather than reveal itself all at once.',
    innerWorld: 'A richly illustrated lining creates an unexpected counterpoint to the restrained exterior. Because some things are better discovered than displayed.',
    construction: null,   /* ⚠ PENDING — supply construction copy for Curiosity */
    productLink: '#collection'
  },
  {
    id: 'temptation',
    number: '02',
    impulse: 'Temptation',
    colour: 'Forest Green',
    image: imgPath('temptation', 'temptation.jpg'),
    views: [
      { label: 'Front',      src: imgPath('temptation', 'temptation.jpg'),            alt: 'Forest Green jacket — Temptation Front Full Body' },
      { label: 'Detail',     src: imgPath('temptation', 'temptation_detail.jpg'),     alt: 'Forest Green jacket — Temptation Side Embroidery Detail' },
      { label: 'Back',       src: imgPath('temptation', 'temptation_back.jpg'),       alt: 'Forest Green jacket — Temptation Back Lapel Embroidery' },
      { label: 'Lookbook 1', src: imgPath('temptation', 'temptation_lookbook_1.jpg'), alt: 'Forest Green jacket — Temptation Male Model Seated' },
      { label: 'Lookbook 2', src: imgPath('temptation', 'temptation_lookbook_2.jpg'), alt: 'Forest Green jacket — Temptation Male Model Armchair' }
    ],
    headline: 'Not every temptation is a weakness. Sometimes it is recognition.',
    narrative: 'Temptation begins with the awareness that something else is possible — a pull toward what lies just beyond the choices already made for us. In deep forest green suede, tone-on-tone embroidery moves between shadow and visibility, creating a surface that reveals itself gradually rather than giving everything away. A piece for the possibility that becomes increasingly difficult to ignore.',
    material: 'Richly dyed suede gives the jacket its depth of colour, softness and structure.',
    embroidery: 'Intricate tonal embroidery sits close to the colour of the leather, appearing and disappearing with movement and changing light.',
    innerWorld: 'Inside, the illustrated lining offers a more expressive world than the exterior first suggests. Because restraint does not require the absence of temptation.',
    construction: null,   /* ⚠ PENDING — supply construction copy for Temptation */
    productLink: '#collection'
  },
  {
    id: 'desire',
    number: '03',
    impulse: 'Desire',
    colour: 'Deep Red',
    image: imgPath('desire', 'desire.jpg'),
    views: [
      { label: 'Front',       src: imgPath('desire', 'desire.jpg'),             alt: 'Deep Red jacket — Desire Front Seated' },
      { label: 'Detail',      src: imgPath('desire', 'desire_detail.jpg'),      alt: 'Deep Red jacket — Desire Male Back Embroidery Detail' },
      { label: 'Back',        src: imgPath('desire', 'desire_back.jpg'),        alt: 'Deep Red jacket — Desire Female Back Embroidery' },
      { label: 'Lining',      src: imgPath('desire', 'desire_lining.jpg'),      alt: 'Deep Red jacket — Desire Illustrated Inner Lining' },
      { label: 'Lookbook 1',  src: imgPath('desire', 'desire_lookbook_1.jpg'),  alt: 'Deep Red jacket — Desire Male Model Standing' },
      { label: 'Lookbook 2',  src: imgPath('desire', 'desire_lookbook_2.jpg'),  alt: 'Deep Red jacket — Desire Male Model Side Angle' },
      { label: 'Lookbook 3',  src: imgPath('desire', 'desire_lookbook_3.jpg'),  alt: 'Deep Red jacket — Desire Male Model Lounge Chair' },
      { label: 'Editorial 1', src: imgPath('desire', 'desire_editorial_1.jpg'), alt: 'Deep Red jacket — Desire Female Model Sofa' },
      { label: 'Editorial 2', src: imgPath('desire', 'desire_editorial_2.jpg'), alt: 'Deep Red jacket — Desire Female Model Close-up' },
      { label: 'Editorial 3', src: imgPath('desire', 'desire_editorial_3.jpg'), alt: 'Deep Red jacket — Desire Female Model Standing' }
    ],
    headline: 'Wanting more is not always greed. Sometimes it is vision.',
    narrative: 'Desire is the instinct that refuses to be satisfied by what is already there. It begins with recognition — of what could be, of what is missing, of what feels worth moving toward — and turns that recognition into intent. There is nothing passive about it. Rendered in deep red suede, the jacket carries that tension between restraint and appetite. Tone-on-tone embroidery moves through the surface in shifting fragments, revealing itself gradually as light catches the garment and then recedes again. Sensual without spectacle. Expressive without surrendering restraint.',
    material: 'Deeply dyed suede gives the jacket its richness, structure and tactile presence.',
    embroidery: 'Tone-on-tone embroidery is integrated into the surface of the garment, allowing pattern and texture to emerge gradually as the light changes.',
    innerWorld: 'A richly illustrated lining sits in deliberate contrast to the controlled exterior. Because desire does not have to announce itself to be felt.',
    construction: null,   /* ⚠ PENDING — supply construction copy for Desire */
    productLink: '#collection'
  },
  {
    id: 'audacity',
    number: '04',
    impulse: 'Audacity',
    colour: 'Deep Mustard',
    image: imgPath('audacity', 'audacity.jpg'),
    views: [
      { label: 'Front',       src: imgPath('audacity', 'audacity.jpg'),             alt: 'Deep Mustard jacket — Audacity Front View' },
      { label: 'Detail',      src: imgPath('audacity', 'audacity_detail.jpg'),      alt: 'Deep Mustard jacket — Audacity Embroidery Detail' },
      { label: 'Back',        src: imgPath('audacity', 'audacity_back.jpg'),        alt: 'Deep Mustard jacket — Audacity Back View' },
      { label: 'Editorial 1', src: imgPath('audacity', 'audacity_editorial_1.jpg'), alt: 'Deep Mustard jacket — Audacity Female Model Seated Portrait' },
      { label: 'Editorial 2', src: imgPath('audacity', 'audacity_editorial_2.jpg'), alt: 'Deep Mustard jacket — Audacity Female Model with Street Lamp' },
      { label: 'Lookbook 1',  src: imgPath('audacity', 'audacity_lookbook_1.jpg'),  alt: 'Deep Mustard jacket — Audacity Male Model with Scarf' },
      { label: 'Lookbook 2',  src: imgPath('audacity', 'audacity_lookbook_2.jpg'),  alt: 'Deep Mustard jacket — Audacity Male Model Front Embroidery' }
    ],
    headline: 'Audacity is confidence before permission arrives.',
    narrative: 'Audacity is the willingness to move before the world has decided you may. To take the unexpected route, occupy the space available to you — and occasionally the space that was not. The deep mustard suede refuses anonymity, while tonal embroidery tempers its boldness with intricacy and restraint. A piece that stands apart without turning difference into performance.',
    material: 'Dyed suede gives the saturated mustard tone both richness and weight, balancing expressive colour with a structured silhouette.',
    embroidery: 'Tone-on-tone embroidery adds complexity without competing with the strength of the colour, revealing itself through texture and light.',
    innerWorld: "The illustrated lining continues the jacket's confidence inward — a private flourish beneath the more controlled surface. Because audacity does not end where other people stop looking.",
    construction: null,   /* ⚠ PENDING — supply construction copy for Audacity */
    productLink: '#collection'
  },
  {
    id: 'insolence',
    number: '05',
    impulse: 'Insolence',
    colour: 'Black',
    image: imgPath('insolence', 'insolence.jpg'),
    views: [
      { label: 'Front',       src: imgPath('insolence', 'insolence.jpg'),             alt: 'Black jacket — Insolence Male Model Seated' },
      { label: 'Detail',      src: imgPath('insolence', 'insolence_detail.jpg'),      alt: 'Black jacket — Insolence Male Model Floor Angle' },
      { label: 'Back',        src: imgPath('insolence', 'insolence_back.jpg'),        alt: 'Black jacket — Insolence Back Shoulder Embroidery' },
      { label: 'Editorial 1', src: imgPath('insolence', 'insolence_editorial_1.jpg'), alt: 'Black jacket — Insolence Female Model Standing Full-Body' },
      { label: 'Editorial 2', src: imgPath('insolence', 'insolence_editorial_2.jpg'), alt: 'Black jacket — Insolence Female Model Seated Chair' },
      { label: 'Editorial 3', src: imgPath('insolence', 'insolence_editorial_3.jpg'), alt: 'Black jacket — Insolence Female Model Side Chair' },
      { label: 'Editorial 4', src: imgPath('insolence', 'insolence_editorial_4.jpg'), alt: 'Black jacket — Insolence Female Model Front Close-up' }
    ],
    headline: 'Respect the rule. Question its right to rule you.',
    narrative: 'Insolence begins with discernment. Not the rejection of convention for its own sake, but the confidence to decide which traditions deserve respect — and which have simply become habits of obedience. Rendered in black suede, near-concealed tonal embroidery turns restraint into something more subversive: detail that exists without demanding recognition. Refined, controlled and entirely capable of disobedience.',
    material: 'Black dyed suede gives the jacket weight, texture and an understated depth that rewards proximity.',
    embroidery: 'Dark tonal embroidery sits almost within the surface itself, becoming visible through shifts in light rather than contrast.',
    innerWorld: 'The illustrated lining disrupts the restraint of the exterior with a world known most intimately by the wearer. Because what is hidden can still have character.',
    construction: null,   /* ⚠ PENDING — supply construction copy for Insolence */
    productLink: '#collection'
  }
];


/* -------------------------------------------------------------------
   UTILITY
   ------------------------------------------------------------------- */

const $ = (s) => document.querySelector(s);

const isReducedMotion = () =>
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const delay = (ms) => new Promise(res => setTimeout(res, ms));


/* -------------------------------------------------------------------
   STATE
   ------------------------------------------------------------------- */

let selectedJacketId    = null;
let isTransitioning     = false;
let currentViewIndex    = 0;
let isViewTransitioning = false;


/* -------------------------------------------------------------------
   URL SYNC
   ------------------------------------------------------------------- */

function getJacketFromURL() {
  const p = new URLSearchParams(window.location.search).get('jacket');
  return (p && collectionData.some(j => j.id === p)) ? p : null;
}

function syncURL(id) {
  const u = new URL(window.location.href);
  u.searchParams.set('jacket', id);
  history.replaceState({ jacket: id }, '', u);
}


/* -------------------------------------------------------------------
   IMAGE PRELOADING
   ------------------------------------------------------------------- */

function preloadSrc(src) {
  const img = new Image();
  img.src = src;
}

function preloadAdjacent(id) {
  const i   = collectionData.findIndex(j => j.id === id);
  const len = collectionData.length;
  preloadSrc(collectionData[(i - 1 + len) % len].image);
  preloadSrc(collectionData[(i + 1) % len].image);
}

/* Preload based on URL param so initial load is instant (amendment 9) */
function preloadFromURL() {
  const id   = getJacketFromURL() || 'desire';
  const item = collectionData.find(j => j.id === id);
  if (item) {
    preloadSrc(item.image);
    preloadViews(item);
  }
}


/* -------------------------------------------------------------------
   GALLERY HELPERS (VIEWS / ANGLES FOR ACTIVE JACKET)
   ------------------------------------------------------------------- */

function getViewsForItem(item) {
  if (!item) return [];
  if (Array.isArray(item.views) && item.views.length > 0) return item.views;
  return [{ label: 'Front', src: item.image, alt: `${item.colour} jacket — ${item.impulse}` }];
}

function preloadViews(item) {
  if (!item) return;
  const views = getViewsForItem(item);
  views.forEach(v => preloadSrc(v.src));
}

function updateGalleryUI(item) {
  const views = getViewsForItem(item);
  const counter = $('#galleryCounter');
  const pills = $('#galleryPills');
  const prevBtn = $('#galleryPrevBtn');
  const nextBtn = $('#galleryNextBtn');

  if (views.length <= 1) {
    if (counter) counter.style.display = 'none';
    if (pills) {
      pills.innerHTML = '';
      pills.style.display = 'none';
    }
    if (prevBtn) prevBtn.style.display = 'none';
    if (nextBtn) nextBtn.style.display = 'none';
    return;
  }

  const currentView = views[currentViewIndex] || views[0];

  if (counter) {
    counter.style.display = '';
    const labelStr = currentView && currentView.label ? ` · ${currentView.label}` : '';
    counter.textContent = `· ${String(currentViewIndex + 1).padStart(2, '0')} / ${String(views.length).padStart(2, '0')}${labelStr}`;
  }

  if (prevBtn) {
    prevBtn.style.display = '';
    const prevIdx = (currentViewIndex - 1 + views.length) % views.length;
    prevBtn.setAttribute('aria-label', `Previous view: ${views[prevIdx].label}`);
    prevBtn.title = `Previous: ${views[prevIdx].label}`;
  }

  if (nextBtn) {
    nextBtn.style.display = '';
    const nextIdx = (currentViewIndex + 1) % views.length;
    nextBtn.setAttribute('aria-label', `Next view: ${views[nextIdx].label}`);
    nextBtn.title = `Next: ${views[nextIdx].label}`;
  }

  if (pills) {
    pills.style.display = '';
    pills.innerHTML = views.map((v, i) => `
      <button
        class="gallery-indicator-bar${i === currentViewIndex ? ' is-active' : ''}"
        type="button"
        role="tab"
        aria-selected="${i === currentViewIndex}"
        aria-label="View ${v.label} (${i + 1} of ${views.length})"
        title="${v.label}"
        data-view-index="${i}"
      ><span class="indicator-line" aria-hidden="true"></span><span class="sr-only">${v.label}</span></button>
    `).join('');
  }
}


/* -------------------------------------------------------------------
   CONTROLS RENDERING
   Roving tabindex: active tab has tabindex="0", others "-1" (amendment 7).
   Carousel: original cards + aria-hidden clones (amendment 5).
   ------------------------------------------------------------------- */

function renderControls() {
  const nav = $('#impulseNav');
  if (!nav) return;

  nav.innerHTML = collectionData.map(item =>
    `<button
       class="impulse-button${item.id === selectedJacketId ? ' is-active' : ''}"
       id="tab-${item.id}"
       data-jacket="${item.id}"
       type="button"
       role="tab"
       aria-selected="${item.id === selectedJacketId}"
       aria-controls="collection"
       tabindex="${item.id === selectedJacketId ? '0' : '-1'}"
     >${item.impulse}</button>`
  ).join('');
}



/* -------------------------------------------------------------------
   IMAGE FALLBACK (neutral beige block on error)
   ------------------------------------------------------------------- */

function showFallback(item) {
  const img  = $('#jacketImage');
  const fb   = $('#jacketImgFallback');
  const lbl  = $('#fallbackLabel');
  if (img) img.style.display = 'none';
  if (lbl) lbl.textContent = item.impulse;
  if (fb)  fb.removeAttribute('aria-hidden');
  $('#jacketStage')?.classList.remove('is-loading');
}

function hideFallback() {
  const img = $('#jacketImage');
  const fb  = $('#jacketImgFallback');
  if (img) img.style.display = '';
  if (fb)  fb.setAttribute('aria-hidden', 'true');
}


/* -------------------------------------------------------------------
   TEXT UPDATES
   ------------------------------------------------------------------- */

function setText(id, value) {
  const el = $(id);
  if (el) el.textContent = value ?? '';
}

function updateText(item) {
  const idx = collectionData.indexOf(item);
  setText('#visualNumber',      String(idx + 1).padStart(2, '0'));
  setText('#visualImpulse',     item.impulse);
  setText('#productImpulse',    item.impulse);
  setText('#productColour',     item.colour);
  setText('#productHeadline',   item.headline);
  setText('#productNarrative',  item.narrative);
  setText('#productMaterial',   item.material);
  setText('#productEmbroidery', item.embroidery);
  setText('#productInnerWorld', item.innerWorld);

  /* Construction row: hidden until copy is supplied (amendment 6) */
  const constrRow = $('#constructionRow');
  if (constrRow) {
    constrRow.hidden = !item.construction;
    if (item.construction) setText('#productConstruction', item.construction);
  }

  const link = $('#productLink');
  if (link) {
    link.href = item.productLink || '#collection';
    link.setAttribute('aria-label', `View ${item.impulse} jacket`);
  }

  const img = $('#jacketImage');
  if (img) img.alt = `${item.colour} jacket — ${item.impulse}`;
}


/* -------------------------------------------------------------------
   JACKET SELECTION

   Root cause fix (amendment 1):
   — Fade out: add is-changing, wait 220ms.
   — Swap src + show skeleton.
   — await img.decode() → fade-in ONLY after pixels are ready.
   — Double requestAnimationFrame before removing is-changing so the
     browser completes the repaint before the transition starts.

   Auto-scroll only from carousel card clicks (amendment 8).
   ------------------------------------------------------------------- */

async function selectJacket(id, { fromCarousel = false } = {}) {
  const item = collectionData.find(j => j.id === id);
  if (!item || id === selectedJacketId || isTransitioning) return;

  isTransitioning  = true;
  selectedJacketId = id;
  currentViewIndex = 0;
  syncURL(id);
  renderControls();  /* update active tab + carousel card immediately */
  updateInlineCarouselActive();  /* sync inline product carousel active state */
  scrollInlineCarouselToActive(); /* bring selected card into view */
  updateGalleryUI(item);

  const views = getViewsForItem(item);
  const activeView = views[0] || { src: item.image, alt: `${item.colour} jacket — ${item.impulse}` };

  const reduced = isReducedMotion();
  const img     = $('#jacketImage');
  const stage   = $('#jacketStage');
  const meta    = $('#productMeta');
  const content = $('#showcaseContent');

  /* ── Reduced-motion: instant swap, no animation (amendment 10) ── */
  if (reduced) {
    if (img) {
      img.src = activeView.src;
      img.alt = activeView.alt;
    }
    updateText(item);
    preloadViews(item);
    isTransitioning = false;
    return;
  }

  /* ── Phase 1: fade out ────────────────────────────────────────── */
  stage?.classList.add('is-changing');
  meta?.classList.add('is-changing');
  content?.classList.add('is-changing');
  await delay(220);   /* let opacity reach ~0 before swapping content */

  /* ── Phase 2: swap src + loading skeleton ─────────────────────── */
  hideFallback();
  stage?.classList.add('is-loading');

  if (img) {
    img.src = activeView.src;
    img.alt = activeView.alt;
    try {
      await img.decode();  /* KEY FIX: wait until browser has pixels ready */
    } catch (_) {
      showFallback(item);  /* graceful fallback on load failure */
    }
  }

  stage?.classList.remove('is-loading');
  updateText(item);

  /* ── Phase 3: fade in ─────────────────────────────────────────── */
  /* Double rAF ensures the class removal triggers a new CSS transition
     rather than continuing the interrupted one. */
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      stage?.classList.remove('is-changing');
      meta?.classList.remove('is-changing');
      content?.classList.remove('is-changing');
    });
  });

  /* Preload adjacent jackets and all views for this jacket */
  preloadAdjacent(id);
  preloadViews(item);

  /* Scroll to detail only from carousel, only when not fully in view (amendment 8) */
  if (fromCarousel) scrollToDetailIfNeeded();

  isTransitioning = false;
}


/* -------------------------------------------------------------------
   GALLERY VIEW SELECTION (ANGLE / DETAIL VIEW SWAPPING)
   ------------------------------------------------------------------- */

async function selectView(index) {
  const item = collectionData.find(j => j.id === selectedJacketId);
  if (!item) return;
  const views = getViewsForItem(item);
  if (views.length <= 1 || isViewTransitioning || isTransitioning) return;

  const total = views.length;
  const normalizedIndex = ((index % total) + total) % total;
  if (normalizedIndex === currentViewIndex) return;

  isViewTransitioning = true;
  currentViewIndex = normalizedIndex;
  const view = views[currentViewIndex];

  updateGalleryUI(item);

  const img   = $('#jacketImage');
  const stage = $('#jacketStage');

  if (isReducedMotion()) {
    if (img) {
      img.src = view.src;
      img.alt = view.alt;
    }
    isViewTransitioning = false;
    return;
  }

  /* Fade out current image */
  stage?.classList.add('is-changing');
  await delay(180);

  if (img) {
    img.src = view.src;
    img.alt = view.alt;
    try {
      await img.decode();
    } catch (_) {
      showFallback(item);
    }
  }

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      stage?.classList.remove('is-changing');
      isViewTransitioning = false;
    });
  });
}

function changeView(direction) {
  const item = collectionData.find(j => j.id === selectedJacketId);
  if (!item) return;
  const views = getViewsForItem(item);
  if (views.length <= 1) return;
  selectView(currentViewIndex + direction);
}


/* -------------------------------------------------------------------
   SCROLL HELPER
   ------------------------------------------------------------------- */

function scrollToDetailIfNeeded() {
  const section = $('#collection');
  if (!section) return;
  const headerH = ($('.site-header')?.offsetHeight ?? 82) + 12;
  const rect    = section.getBoundingClientRect();
  const fullyVisible = rect.top >= headerH && rect.bottom <= window.innerHeight;
  if (!fullyVisible) {
    window.scrollTo({
      top: section.offsetTop - headerH,
      behavior: 'smooth'
    });
  }
}


/* -------------------------------------------------------------------
   PREV / NEXT (JACKETS)
   ------------------------------------------------------------------- */

function moveSelection(direction) {
  const i   = collectionData.findIndex(j => j.id === selectedJacketId);
  const len = collectionData.length;
  selectJacket(collectionData[(i + direction + len) % len].id);
}

$('#previousButton')?.addEventListener('click', () => moveSelection(-1));
$('#nextButton')?.addEventListener('click',     () => moveSelection(1));


/* -------------------------------------------------------------------
   GALLERY NAVIGATION LISTENERS (VIEWS / ANGLES)
   ------------------------------------------------------------------- */

$('#galleryPrevBtn')?.addEventListener('click', (e) => {
  e.preventDefault();
  changeView(-1);
});

$('#galleryNextBtn')?.addEventListener('click', (e) => {
  e.preventDefault();
  changeView(1);
});

$('#galleryPills')?.addEventListener('click', (e) => {
  const btn = e.target.closest('[data-view-index]');
  if (!btn) return;
  e.preventDefault();
  const idx = parseInt(btn.dataset.viewIndex, 10);
  if (!isNaN(idx)) selectView(idx);
});

/* Touch swipe support on jacket stage */
const stageEl = $('#jacketStage');
if (stageEl) {
  let touchStartX = 0;
  let touchStartY = 0;

  stageEl.addEventListener('touchstart', (e) => {
    if (e.touches.length === 1) {
      touchStartX = e.touches[0].clientX;
      touchStartY = e.touches[0].clientY;
    }
  }, { passive: true });

  stageEl.addEventListener('touchend', (e) => {
    if (e.changedTouches.length === 1) {
      const deltaX = e.changedTouches[0].clientX - touchStartX;
      const deltaY = e.changedTouches[0].clientY - touchStartY;
      if (Math.abs(deltaX) > 40 && Math.abs(deltaX) > Math.abs(deltaY) * 1.5) {
        if (deltaX < 0) {
          changeView(1);
        } else {
          changeView(-1);
        }
      }
    }
  }, { passive: true });
}


/* -------------------------------------------------------------------
   KEYBOARD — SCOPED TO TABLIST, STAGE & DETAIL
   Roving tabindex: ArrowLeft/Right moves between tabs or angles.
   Ignores inputs and elements outside the scoped regions.
   ------------------------------------------------------------------- */

document.addEventListener('keydown', (e) => {
  /* Ignore when focus is in an editable element */
  const tag = document.activeElement?.tagName;
  if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;

  const inStage  = !!document.activeElement?.closest('#jacketStage');
  const inPills  = !!document.activeElement?.closest('#galleryPills');
  const inNav    = !!document.activeElement?.closest('#impulseNav');
  const inDetail = !!document.activeElement?.closest('#collection');
  if (!inStage && !inPills && !inNav && !inDetail) return;

  if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
    e.preventDefault();
    if (inStage || inPills) {
      changeView(e.key === 'ArrowLeft' ? -1 : 1);
    } else {
      moveSelection(e.key === 'ArrowLeft' ? -1 : 1);
      /* After renderControls() rebuilds buttons, focus the new active tab */
      requestAnimationFrame(() => $(`#tab-${selectedJacketId}`)?.focus());
    }
  }
});


/* -------------------------------------------------------------------
   DELEGATED CLICK — tabs + carousel (clones included via delegation)
   ------------------------------------------------------------------- */

document.addEventListener('click', (e) => {
  const ctrl = e.target.closest('[data-jacket]');
  if (!ctrl) return;
  const fromCarousel = !!e.target.closest('#jacketCarousel');
  selectJacket(ctrl.dataset.jacket, { fromCarousel });
});




/* -------------------------------------------------------------------
   INLINE PRODUCT CAROUSEL — rAF-driven marquee + two-way tab sync
   Architecture:
   • Track holds original 5 cards + 5 aria-hidden clones (10 total).
   • JS rAF loop translates the track by icState.speed px/frame.
   • When translateX reaches -halfWidth, it resets to 0 → seamless.
   • Tab click → snap-to-card animation (ease toward target translateX).
   • Two-way sync: every frame calculates the centered original card
     and updates the impulse-nav tab active states (lightweight toggle,
     NOT a full selectJacket() call during auto-scroll).
   • Pause sources: hover, pause button, tab click (4 s auto-resume).
   ------------------------------------------------------------------- */

/* ── State ──────────────────────────────────────────────────────── */
const icState = {
  translateX:     0,      /* current track offset in px */
  speed:          0.48,   /* px per rAF frame ≈ 29px/s at 60fps */
  paused:         false,  /* hovered or button-paused */
  userPaused:     false,  /* explicit pause-button press */
  snapping:       false,  /* currently easing toward snapTarget */
  snapTarget:     null,   /* target translateX for snap */
  snapTimer:      null,   /* timeout to resume after snap */
  rafId:          null,
  halfWidth:      0,      /* px-width of one full set (5 cards + gaps) */
  cardWidth:      0,
  cardGap:        0,
  padLeft:        0,      /* track padding-left in px */
  lastTabId:      null,   /* last id pushed to tab bar during auto-scroll */
};

/* ── Render ─────────────────────────────────────────────────────── */
function renderInlineCarousel() {
  const track = $('#inlineCarouselTrack');
  if (!track) return;

  const makeCard = (item, clone) => `
    <div
      class="inline-jacket-card${!clone && item.id === selectedJacketId ? ' is-active' : ''}"
      data-jacket="${item.id}"
      role="${clone ? 'presentation' : 'listitem'}"
      ${clone
        ? 'aria-hidden="true" tabindex="-1"'
        : `tabindex="0" aria-label="${item.impulse} — ${item.colour}"`}
    >
      <div class="inline-card-img">
        <img
          src="${item.image}"
          alt="${clone ? '' : `${item.impulse} jacket, ${item.colour}`}"
          loading="lazy"
          width="1200"
          height="1500"
        >
      </div>
      <div class="inline-card-label">
        <span class="ic-label-left">${item.number} / ${item.impulse.toUpperCase()}</span>
        <span class="ic-label-right">${item.colour.toUpperCase()}</span>
      </div>
    </div>`;

  /* Originals first, then aria-hidden clones */
  track.innerHTML =
    collectionData.map(item => makeCard(item, false)).join('') +
    collectionData.map(item => makeCard(item, true)).join('');
}

/* ── Measure card geometry after render ─────────────────────────── */
function icMeasure() {
  const track = $('#inlineCarouselTrack');
  if (!track) return;
  const cards = track.querySelectorAll('.inline-jacket-card');
  if (cards.length < 2) return;
  const c0 = cards[0];
  const c1 = cards[1];
  icState.cardWidth = c0.offsetWidth;
  icState.cardGap   = c1.offsetLeft - c0.offsetLeft - c0.offsetWidth;
  icState.padLeft   = c0.offsetLeft; /* track padding-left reflected here */
  icState.halfWidth = collectionData.length * (icState.cardWidth + icState.cardGap);
}

/* ── Detect which original card is nearest to carousel centre ───── */
function icCenteredId() {
  const carousel = $('#inlineCarousel');
  if (!carousel || icState.halfWidth === 0) return null;
  const viewCentre = carousel.offsetWidth / 2;
  const step = icState.cardWidth + icState.cardGap;
  let bestId = null, minDist = Infinity;
  collectionData.forEach((item, i) => {
    const cardCentre = icState.padLeft + i * step + icState.cardWidth / 2 + icState.translateX;
    const dist = Math.abs(cardCentre - viewCentre);
    if (dist < minDist) { minDist = dist; bestId = item.id; }
  });
  return bestId;
}

/* ── Lightly update impulse-nav tabs (no full re-render) ─────────── */
function icSyncTabs(id) {
  document.querySelectorAll('#impulseNav .impulse-button').forEach(btn => {
    const active = btn.dataset.jacket === id;
    btn.classList.toggle('is-active', active);
    btn.setAttribute('aria-selected', String(active));
    btn.tabIndex = active ? 0 : -1;
  });
}

/* ── Update inline card active state (originals only) ───────────── */
function updateInlineCarouselActive() {
  document.querySelectorAll('.inline-jacket-card:not([aria-hidden])').forEach(card => {
    card.classList.toggle('is-active', card.dataset.jacket === selectedJacketId);
  });
}

/* ── Compute snap target translateX to centre a card ────────────── */
function icSnapTargetFor(id) {
  const carousel = $('#inlineCarousel');
  if (!carousel || icState.halfWidth === 0) return null;
  const idx  = collectionData.findIndex(j => j.id === id);
  if (idx < 0) return null;
  const step = icState.cardWidth + icState.cardGap;
  let target = carousel.offsetWidth / 2
               - (icState.padLeft + idx * step + icState.cardWidth / 2);
  /* Normalise into [-halfWidth, 0] so it corresponds to a real track position */
  while (target > 0)                target -= icState.halfWidth;
  while (target < -icState.halfWidth) target += icState.halfWidth;
  return target;
}

/* ── Trigger a snap-to-card (called on tab click) ───────────────── */
function scrollInlineCarouselToActive() {
  const target = icSnapTargetFor(selectedJacketId);
  if (target === null) return;
  icState.snapTarget = target;
  icState.snapping   = true;
  icState.paused     = true;
  clearTimeout(icState.snapTimer);
  /* Auto-resume after 4 s of no interaction */
  icState.snapTimer = setTimeout(() => {
    if (!icState.userPaused) {
      icState.snapping = false;
      icState.paused   = false;
    }
  }, 4000);
}

/* ── Main rAF loop ──────────────────────────────────────────────── */
function icLoop() {
  const track = $('#inlineCarouselTrack');
  if (!track) return;

  if (icState.snapping && icState.snapTarget !== null) {
    /* Ease toward snap target */
    const diff = icState.snapTarget - icState.translateX;
    if (Math.abs(diff) < 0.3) {
      icState.translateX = icState.snapTarget;
    } else {
      icState.translateX += diff * 0.12;
    }
  } else if (!icState.paused) {
    icState.translateX -= icState.speed;
    /* Seamless loop reset */
    if (icState.translateX <= -icState.halfWidth) {
      icState.translateX += icState.halfWidth;
    }
  }

  track.style.transform = `translateX(${icState.translateX}px)`;

  /* Two-way tab sync — update tabs to reflect centred card */
  const centredId = icCenteredId();
  if (centredId && centredId !== icState.lastTabId) {
    icState.lastTabId = centredId;
    /* During auto-scroll: only update visual tab, not the showcase */
    if (!icState.snapping) {
      icSyncTabs(centredId);
    }
  }

  icState.rafId = requestAnimationFrame(icLoop);
}

/* ── Initialise ─────────────────────────────────────────────────── */
function initInlineCarousel() {
  const carousel = $('#inlineCarousel');
  const track    = $('#inlineCarouselTrack');
  const pauseBtn = $('#icPauseBtn');
  if (!carousel || !track) return;

  /* Reduced-motion: render static, skip loop */
  if (isReducedMotion()) {
    renderInlineCarousel();
    updateInlineCarouselActive();
    return;
  }

  renderInlineCarousel();

  /* Measure after two rAF passes (layout is settled) */
  requestAnimationFrame(() => requestAnimationFrame(() => {
    icMeasure();
    /* Snap to active jacket on first load */
    scrollInlineCarouselToActive();
    icState.rafId = requestAnimationFrame(icLoop);
  }));

  /* ── Hover: pause / resume ────────────────────────────────────── */
  carousel.addEventListener('mouseenter', () => {
    if (!icState.userPaused) icState.paused = true;
  });
  carousel.addEventListener('mouseleave', () => {
    if (!icState.userPaused && !icState.snapping) icState.paused = false;
  });

  /* ── Pause button ────────────────────────────────────────────── */
  if (pauseBtn) {
    pauseBtn.addEventListener('click', () => {
      icState.userPaused = !icState.userPaused;
      icState.paused     = icState.userPaused;
      if (!icState.userPaused) icState.snapping = false;
      pauseBtn.setAttribute('aria-pressed', String(icState.userPaused));
    });
  }

  /* ── Click original cards ─────────────────────────────────────── */
  track.addEventListener('click', (e) => {
    const card = e.target.closest('.inline-jacket-card:not([aria-hidden])');
    if (!card) return;
    selectJacket(card.dataset.jacket);
  });

  /* ── Keyboard on original cards ──────────────────────────────── */
  track.addEventListener('keydown', (e) => {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    const card = e.target.closest('.inline-jacket-card:not([aria-hidden])');
    if (!card) return;
    e.preventDefault();
    selectJacket(card.dataset.jacket);
  });

  /* ── Touch: pause while finger is down ──────────────────────── */
  carousel.addEventListener('touchstart',  () => { icState.paused = true; },
    { passive: true });
  carousel.addEventListener('touchend',    () => {
    if (!icState.userPaused && !icState.snapping) icState.paused = false;
  }, { passive: true });
  carousel.addEventListener('touchcancel', () => {
    if (!icState.userPaused && !icState.snapping) icState.paused = false;
  }, { passive: true });
}




/* -------------------------------------------------------------------
   INIT
   ------------------------------------------------------------------- */

function init() {
  /* Determine starting jacket */
  const startId = getJacketFromURL() || 'desire';
  selectedJacketId = startId;
  currentViewIndex = 0;

  /* Preload the URL-specified jacket immediately (amendment 9) */
  preloadFromURL();

  renderControls();

  const startItem = collectionData.find(j => j.id === startId);
  if (startItem) {
    updateText(startItem);
    const views = getViewsForItem(startItem);
    const initialView = views[0] || { src: startItem.image, alt: `${startItem.colour} jacket — ${startItem.impulse}` };
    const initialImg = $('#jacketImage');
    if (initialImg) {
      initialImg.src = initialView.src;
      initialImg.alt = initialView.alt;
    }
    updateGalleryUI(startItem);
    preloadViews(startItem);
    syncURL(startId);
    preloadAdjacent(startId);
  }

  /* Wire up error fallback for the initial image in the HTML */
  const img = $('#jacketImage');
  if (img) {
    img.addEventListener('error', () => {
      const item = collectionData.find(j => j.id === selectedJacketId);
      if (item) showFallback(item);
    });
  }

  initInlineCarousel();
}

init();
