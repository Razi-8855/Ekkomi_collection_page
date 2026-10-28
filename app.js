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
  renderControls();  /* update active tab immediately */
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
   3D PERSPECTIVE DRIFT WALL
   Replaces the sliding carousel in the hero section.
   Drifts continuous columns of jacket photos from jackets_original,
   lifting tiles on hover with smooth 3D perspective and mouse parallax.
   Clicking a tile selects that jacket in the collection showcase.
   ------------------------------------------------------------------- */

const wallTiles = [
  { image: 'jackets_original/resized_BEN03137.webp', title: 'Curiosity · Dark Navy', jacket: 'curiosity' },
  { image: 'jackets_original/resized_BEN03166.webp', title: 'Curiosity · Angle View', jacket: 'curiosity' },
  { image: 'jackets_original/resized_BEN03202.webp', title: 'Curiosity · Male Model', jacket: 'curiosity' },
  { image: 'jackets_original/resized_BEN04014.webp', title: 'Temptation · Forest Green', jacket: 'temptation' },
  { image: 'assets/collection/nocturne/temptation/temptation_lookbook_1.jpg', title: 'Temptation · Seated', jacket: 'temptation' },
  { image: 'jackets_original/resized_BEN03324.webp', title: 'Desire · Deep Red', jacket: 'desire' },
  { image: 'jackets_original/resized_BEN03515.webp', title: 'Desire · Lounge Chair', jacket: 'desire' },
  { image: 'assets/collection/nocturne/desire/desire_editorial_1.jpg', title: 'Desire · Editorial', jacket: 'desire' },
  { image: 'jackets_original/resized_BEN03619.webp', title: 'Audacity · Deep Mustard', jacket: 'audacity' },
  { image: 'jackets_original/resized_BEN03655.webp', title: 'Audacity · Embroidery Detail', jacket: 'audacity' },
  { image: 'jackets_original/resized_BEN03767.webp', title: 'Audacity · Looking Away', jacket: 'audacity' },
  { image: 'jackets_original/resized_BEN03806.webp', title: 'Audacity · Front View', jacket: 'audacity' },
  { image: 'jackets_original/resized_BEN04053.webp', title: 'Insolence · Black', jacket: 'insolence' },
  { image: 'jackets_original/resized_BEN04058.webp', title: 'Insolence · Sunglasses', jacket: 'insolence' },
  { image: 'jackets_original/resized_BEN04068.webp', title: 'Insolence · Side Profile', jacket: 'insolence' },
  { image: 'jackets_original/resized_BEN04099.webp', title: 'Insolence · Female Model', jacket: 'insolence' },
  { image: 'jackets_original/resized_DSC04253.webp', title: 'Nocturne · Craftsmanship', jacket: 'curiosity' },
  { image: 'assets/collection/nocturne/curiosity/curiosity_lookbook_1.jpg', title: 'Curiosity · Full Body', jacket: 'curiosity' },
  { image: 'assets/collection/nocturne/temptation/temptation_lookbook_2.jpg', title: 'Temptation · Armchair', jacket: 'temptation' },
  { image: 'assets/collection/nocturne/desire/desire_lookbook_2.jpg', title: 'Desire · Side Angle', jacket: 'desire' }
];

function initDriftWall() {
  const container = document.getElementById('heroDriftWall');
  if (!container) return;

  const columns = 5;
  const tileWidth = 220;
  const tileHeight = 300;
  const gap = 16;
  const radius = 8;
  const tilt = 14;
  const turn = -12;
  const roll = 0;
  const perspective = 1100;
  const depth = 100;
  const speed = 28;
  const direction = 'up';
  const variance = 0.4;
  const parallax = 0.5;
  const lift = 72;
  const fade = 0.55;
  const dim = 0.48;
  const overlayColor = '#080706';

  let containerHeight = container.offsetHeight || 640;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Distribute tiles across 5 columns
  const columnItems = Array.from({ length: columns }, () => []);
  wallTiles.forEach((tile, i) => {
    columnItems[i % columns].push(tile);
  });

  const unit = tileHeight + gap;
  const getColumnMeta = (col) => {
    const copyHeight = Math.max(unit, col.length * unit);
    const copies = Math.max(2, Math.ceil((containerHeight * 1.6) / copyHeight) + 1);
    return { copyHeight, copies };
  };

  let columnMeta = columnItems.map(col => getColumnMeta(col));

  const columnFactor = (index, v) => {
    const pseudo = ((index * 0.6180339887 + 0.35) % 1) * 2 - 1;
    return 1 + v * pseudo;
  };

  const dirSign = direction === 'up' ? 1 : -1;
  const baseVelocities = columnItems.map((_, c) => {
    const altSign = c % 2 === 0 ? 1 : -1;
    return speed * columnFactor(c, variance) * dirSign * altSign;
  });

  const offsets = columnMeta.map((meta, c) => meta.copyHeight * ((c * 0.37) % 1));
  const velocities = columnItems.map(() => 0);

  // Build DOM
  const root = document.createElement('div');
  root.className = `drift-wall${reduced ? ' drift-wall--reduced' : ''}`;
  root.style.setProperty('--dw-tile-w', `${tileWidth}px`);
  root.style.setProperty('--dw-tile-h', `${tileHeight}px`);
  root.style.setProperty('--dw-gap', `${gap}px`);
  root.style.setProperty('--dw-radius', `${radius}px`);
  root.style.setProperty('--dw-perspective', `${perspective}px`);
  root.style.setProperty('--dw-lift', `${lift}px`);
  root.style.setProperty('--dw-dim', dim);
  root.style.setProperty('--dw-gray', 0);
  root.style.setProperty('--dw-overlay', overlayColor);
  root.style.setProperty('--dw-edge', `${Math.max(0, (1 - fade) * 100)}%`);

  const plane = document.createElement('div');
  plane.className = 'drift-wall__plane';
  root.appendChild(plane);

  const trackEls = [];

  columnItems.forEach((col, c) => {
    const meta = columnMeta[c];
    const colEl = document.createElement('div');
    colEl.className = 'drift-wall__col';
    colEl.dataset.col = String(c);

    const track = document.createElement('div');
    track.className = 'drift-wall__track';
    trackEls[c] = track;

    for (let copy = 0; copy < meta.copies; copy++) {
      col.forEach((item, itemIdx) => {
        const tileId = `${c}-${copy}-${itemIdx}`;
        const tile = document.createElement('div');
        tile.className = 'drift-wall__tile';
        tile.tabIndex = 0;
        tile.setAttribute('role', 'button');
        tile.setAttribute('aria-label', `${item.title} — view jacket`);
        tile.dataset.tileId = tileId;
        tile.dataset.col = String(c);
        tile.dataset.jacket = item.jacket;

        const inner = document.createElement('span');
        inner.className = 'drift-wall__inner';

        const img = document.createElement('img');
        img.src = item.image;
        img.alt = item.title;
        img.loading = 'lazy';
        img.decoding = 'async';
        img.draggable = false;

        const overlay = document.createElement('span');
        overlay.className = 'drift-wall__overlay';
        overlay.setAttribute('aria-hidden', 'true');

        const badge = document.createElement('span');
        badge.className = 'drift-wall__badge';
        badge.innerHTML = `<span>${item.jacket.toUpperCase()}</span><span>EXPLORE &rarr;</span>`;

        inner.appendChild(img);
        inner.appendChild(overlay);
        inner.appendChild(badge);
        tile.appendChild(inner);
        track.appendChild(tile);
      });
    }

    colEl.appendChild(track);
    plane.appendChild(colEl);
  });

  container.innerHTML = '';
  container.appendChild(root);

  // Dynamic animation and hover interaction
  let activeTileEl = null;
  let hoveredCol = -1;
  let wallHovered = false;
  const pointer = { x: 0, y: 0 };
  const pointerDamped = { x: 0, y: 0 };
  let lastTs = null;
  let rafId = null;

  function applyPlaneTransform(px, py) {
    plane.style.transform =
      `translate(-50%, -50%) scale(1.18) ` +
      `rotateX(${tilt + py}deg) rotateY(${turn + px}deg) rotateZ(${roll}deg) ` +
      `translateZ(${-depth}px)`;
  }
  applyPlaneTransform(0, 0);

  function setActiveTile(tile) {
    if (activeTileEl === tile) return;
    if (activeTileEl) activeTileEl.classList.remove('is-active');
    activeTileEl = tile;
    if (tile) {
      tile.classList.add('is-active');
      hoveredCol = Number(tile.dataset.col);
    } else {
      hoveredCol = -1;
    }
  }

  function releaseActive() {
    if (activeTileEl) {
      activeTileEl.classList.remove('is-active');
      activeTileEl = null;
    }
    hoveredCol = -1;
  }

  function animate(ts) {
    if (lastTs === null) lastTs = ts;
    const dt = Math.min(0.05, Math.max(0, ts - lastTs) / 1000);
    lastTs = ts;

    const maxTilt = parallax * 8;
    const targetX = pointer.x * maxTilt;
    const targetY = -pointer.y * maxTilt;
    const damp = 1 - Math.exp(-dt / 0.12);
    pointerDamped.x += (targetX - pointerDamped.x) * damp;
    pointerDamped.y += (targetY - pointerDamped.y) * damp;
    applyPlaneTransform(pointerDamped.x, pointerDamped.y);

    if (!reduced) {
      for (let c = 0; c < trackEls.length; c++) {
        const meta = columnMeta[c];
        if (!meta) continue;
        const factor = (wallHovered && hoveredCol === c) ? 0 : 1;
        const target = baseVelocities[c] * factor;

        const ease = 1 - Math.exp(-dt / (target === 0 ? 0.16 : 0.28));
        velocities[c] += (target - velocities[c]) * ease;
        let next = offsets[c] + velocities[c] * dt;
        next = ((next % meta.copyHeight) + meta.copyHeight) % meta.copyHeight;
        offsets[c] = next;

        const track = trackEls[c];
        if (track) {
          track.style.transform = `translate3d(0, ${-next}px, 0)`;
        }
      }
    }

    rafId = requestAnimationFrame(animate);
  }

  rafId = requestAnimationFrame(animate);

  // ResizeObserver to adapt copy count seamlessly
  const ro = new ResizeObserver(([entry]) => {
    const h = entry.contentRect.height;
    if (h && Math.abs(h - containerHeight) > 30) {
      containerHeight = h;
      columnMeta = columnItems.map(col => getColumnMeta(col));
    }
  });
  ro.observe(container);

  // Pointer interactions
  root.addEventListener('pointerenter', () => {
    wallHovered = true;
  });

  root.addEventListener('pointermove', (e) => {
    const rect = root.getBoundingClientRect();
    if (parallax > 0 && !reduced) {
      pointer.x = (e.clientX - rect.left) / rect.width - 0.5;
      pointer.y = (e.clientY - rect.top) / rect.height - 0.5;
    }
    const hit = document.elementFromPoint(e.clientX, e.clientY);
    const tile = hit ? hit.closest('.drift-wall__tile') : null;
    if (!tile) {
      releaseActive();
      return;
    }
    setActiveTile(tile);
  });

  root.addEventListener('pointerleave', () => {
    wallHovered = false;
    pointer.x = 0;
    pointer.y = 0;
    releaseActive();
  });

  // Click on tile -> select jacket & scroll to collection
  root.addEventListener('click', (e) => {
    const tile = e.target.closest('.drift-wall__tile');
    if (!tile) return;
    const jId = tile.dataset.jacket;
    if (jId) {
      selectJacket(jId);
      const showcase = document.getElementById('collection');
      if (showcase) {
        showcase.scrollIntoView({ behavior: 'smooth' });
      }
    }
  });

  // Keyboard accessibility
  root.addEventListener('focusin', (e) => {
    const tile = e.target.closest('.drift-wall__tile');
    if (tile) setActiveTile(tile);
  });

  root.addEventListener('focusout', () => {
    releaseActive();
  });

  root.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      const tile = e.target.closest('.drift-wall__tile');
      if (tile && tile.dataset.jacket) {
        e.preventDefault();
        selectJacket(tile.dataset.jacket);
        document.getElementById('collection')?.scrollIntoView({ behavior: 'smooth' });
      }
    }
  });
}

/* -------------------------------------------------------------------
   INIT
   ------------------------------------------------------------------- */

function init() {
  /* Determine starting jacket */
  const startId = getJacketFromURL() || 'desire';
  selectedJacketId = startId;
  currentViewIndex = 0;

  /* Preload the URL-specified jacket immediately */
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

  initDriftWall();
}

init();
