import os

new_app_js = """'use strict';

/* ===================================================================
   EKKOMI — NOCTURNE COLLECTION
   Data & Interaction Logic: Men's & Women's Collections
   =================================================================== */

const IMAGE_BASE = 'assets/collection/nocturne';
const IMG_V = '?v=original';
const imgPath = (folder, file) => `${IMAGE_BASE}/${folder}/${file}${IMG_V}`;

/* -------------------------------------------------------------------
   MEN'S COLLECTION DATA (5 JACKETS — 100% MALE / STILL GARMENT)
   ------------------------------------------------------------------- */

const mensJackets = [
  {
    id: 'men-curiosity',
    key: 'curiosity',
    gender: 'men',
    number: '01',
    impulse: 'Curiosity',
    colour: 'Dark Navy',
    hex: '#1c2838',
    image: 'jackets_original/resized_BEN03137.webp',
    label: '01 / CURIOSITY',
    sublabel: 'DARK NAVY',
    views: [
      { label: 'Front Silhouette', src: imgPath('curiosity', 'curiosity.jpg'), alt: "Dark Navy jacket — Men's Curiosity Front Silhouette" },
      { label: 'Embroidery Detail', src: imgPath('curiosity', 'curiosity_detail.jpg'), alt: "Dark Navy jacket — Men's Curiosity Tone-on-Tone Embroidery Detail" },
      { label: 'Back Tailoring', src: imgPath('curiosity', 'curiosity_back.jpg'), alt: "Dark Navy jacket — Men's Curiosity Back Construction" },
      { label: 'Illustrated Lining', src: imgPath('curiosity', 'curiosity_lining.jpg'), alt: "Dark Navy jacket — Men's Curiosity Illustrated Silk Lining" },
      { label: 'Lookbook Portrait', src: imgPath('curiosity', 'curiosity_lookbook_1.jpg'), alt: "Dark Navy jacket — Men's Curiosity Lookbook Studio Portrait (Male Model)" },
      { label: 'Lookbook Profile', src: imgPath('curiosity', 'curiosity_lookbook_2.jpg'), alt: "Dark Navy jacket — Men's Curiosity Lookbook Profile View (Male Model)" }
    ]
  },
  {
    id: 'men-temptation',
    key: 'temptation',
    gender: 'men',
    number: '02',
    impulse: 'Temptation',
    colour: 'Forest Green',
    hex: '#27382b',
    image: 'jackets_original/resized_BEN03655.webp',
    label: '02 / TEMPTATION',
    sublabel: 'FOREST GREEN',
    views: [
      { label: 'Front Silhouette', src: imgPath('temptation', 'temptation.jpg'), alt: "Forest Green jacket — Men's Temptation Front Full Body" },
      { label: 'Embroidery Detail', src: imgPath('temptation', 'temptation_detail.jpg'), alt: "Forest Green jacket — Men's Temptation Lapel and Embroidery Detail" },
      { label: 'Back Tailoring', src: imgPath('temptation', 'temptation_back.jpg'), alt: "Forest Green jacket — Men's Temptation Back Collar Embroidery" },
      { label: 'Lookbook Seated', src: imgPath('temptation', 'temptation_lookbook_1.jpg'), alt: "Forest Green jacket — Men's Temptation Seated Lookbook (Male Model)" },
      { label: 'Lookbook Armchair', src: imgPath('temptation', 'temptation_lookbook_2.jpg'), alt: "Forest Green jacket — Men's Temptation Armchair Editorial (Male Model)" }
    ]
  },
  {
    id: 'men-desire',
    key: 'desire',
    gender: 'men',
    number: '03',
    impulse: 'Desire',
    colour: 'Deep Red',
    hex: '#662225',
    image: 'jackets_original/resized_BEN03806.webp',
    label: '03 / DESIRE',
    sublabel: 'DEEP RED',
    views: [
      { label: 'Front Silhouette', src: imgPath('desire', 'desire.jpg'), alt: "Deep Red jacket — Men's Desire Front Seated (Male Model)" },
      { label: 'Embroidery Detail', src: imgPath('desire', 'desire_detail.jpg'), alt: "Deep Red jacket — Men's Desire Back Tonal Embroidery (Male Model)" },
      { label: 'Illustrated Lining', src: imgPath('desire', 'desire_lining.jpg'), alt: "Deep Red jacket — Men's Desire Illustrated Silk Lining" },
      { label: 'Lookbook Standing', src: imgPath('desire', 'desire_lookbook_1.jpg'), alt: "Deep Red jacket — Men's Desire Full Standing (Male Model)" },
      { label: 'Lookbook Profile', src: imgPath('desire', 'desire_lookbook_2.jpg'), alt: "Deep Red jacket — Men's Desire Side Angle (Male Model)" },
      { label: 'Lookbook Lounge', src: imgPath('desire', 'desire_lookbook_3.jpg'), alt: "Deep Red jacket — Men's Desire Lounge Chair (Male Model)" }
    ]
  },
  {
    id: 'men-audacity',
    key: 'audacity',
    gender: 'men',
    number: '04',
    impulse: 'Audacity',
    colour: 'Deep Mustard',
    hex: '#8c6b24',
    // Male model standing with scarf (BEN03893)
    image: imgPath('audacity', 'audacity_lookbook_1.jpg'),
    label: '04 / AUDACITY',
    sublabel: 'DEEP MUSTARD',
    views: [
      { label: 'Front Silhouette', src: imgPath('audacity', 'audacity_lookbook_1.jpg'), alt: "Deep Mustard jacket — Men's Audacity Styled with Scarf (Male Model)" },
      { label: 'Chest Embroidery', src: imgPath('audacity', 'audacity_lookbook_2.jpg'), alt: "Deep Mustard jacket — Men's Audacity Front Texture (Male Model)" },
      { label: 'Embroidery Detail', src: imgPath('audacity', 'audacity_detail.jpg'), alt: "Deep Mustard jacket — Men's Audacity Chest Embroidery (Male Model)" },
      { label: 'Back Tailoring', src: imgPath('audacity', 'audacity_back.jpg'), alt: "Deep Mustard jacket — Men's Audacity Back View (Male Model)" }
    ]
  },
  {
    id: 'men-insolence',
    key: 'insolence',
    gender: 'men',
    number: '05',
    impulse: 'Insolence',
    colour: 'Black',
    hex: '#1a1716',
    image: 'jackets_original/resized_BEN03324.webp',
    label: '05 / INSOLENCE',
    sublabel: 'BLACK',
    views: [
      { label: 'Front Silhouette', src: imgPath('insolence', 'insolence.jpg'), alt: "Black jacket — Men's Insolence Front Silhouette (Male Model Seated)" },
      { label: 'Embroidery Detail', src: imgPath('insolence', 'insolence_detail.jpg'), alt: "Black jacket — Men's Insolence Subversive Embroidery Detail (Male Model)" },
      { label: 'Back Tailoring', src: imgPath('insolence', 'insolence_back.jpg'), alt: "Black jacket — Men's Insolence Back Shoulder Seams (Male Model)" }
    ]
  }
];

/* -------------------------------------------------------------------
   WOMEN'S COLLECTION DATA (3 JACKETS — 100% FEMALE / STILL GARMENT)
   ------------------------------------------------------------------- */

const womensJackets = [
  {
    id: 'women-curiosity',
    key: 'curiosity',
    gender: 'women',
    number: '01',
    impulse: 'Curiosity',
    colour: 'Dark Navy',
    hex: '#1c2838',
    image: imgPath('curiosity', 'curiosity.jpg'),
    label: '01 / CURIOSITY',
    sublabel: 'DARK NAVY',
    views: [
      { label: 'Front Silhouette', src: imgPath('curiosity', 'curiosity.jpg'), alt: "Dark Navy jacket — Women's Curiosity Front Silhouette" },
      { label: 'Embroidery Detail', src: imgPath('curiosity', 'curiosity_detail.jpg'), alt: "Dark Navy jacket — Women's Curiosity Tone-on-Tone Embroidery Detail" },
      { label: 'Back Tailoring', src: imgPath('curiosity', 'curiosity_back.jpg'), alt: "Dark Navy jacket — Women's Curiosity Back Construction" },
      { label: 'Illustrated Lining', src: imgPath('curiosity', 'curiosity_lining.jpg'), alt: "Dark Navy jacket — Women's Curiosity Illustrated Silk Lining" }
    ]
  },
  {
    id: 'women-desire',
    key: 'desire',
    gender: 'women',
    number: '02',
    impulse: 'Desire',
    colour: 'Deep Red',
    hex: '#662225',
    image: imgPath('desire', 'desire_editorial_3.jpg'),
    label: '02 / DESIRE',
    sublabel: 'DEEP RED',
    views: [
      { label: 'Standing Silhouette', src: imgPath('desire', 'desire_editorial_3.jpg'), alt: "Deep Red jacket — Women's Desire Standing Portrait (Female Model)" },
      { label: 'Back Embroidery', src: imgPath('desire', 'desire_back.jpg'), alt: "Deep Red jacket — Women's Desire Back Embroidery Detail (Female Model)" },
      { label: 'Evening Lounge', src: imgPath('desire', 'desire_editorial_1.jpg'), alt: "Deep Red jacket — Women's Desire Editorial on Sofa (Female Model)" },
      { label: 'Close Profile', src: imgPath('desire', 'desire_editorial_2.jpg'), alt: "Deep Red jacket — Women's Desire Intimate Close-up (Female Model)" },
      { label: 'Embroidery Detail', src: imgPath('desire', 'desire_detail.jpg'), alt: "Deep Red jacket — Women's Desire Embroidery Macro" },
      { label: 'Illustrated Lining', src: imgPath('desire', 'desire_lining.jpg'), alt: "Deep Red jacket — Women's Desire Illustrated Silk Lining" }
    ]
  },
  {
    id: 'women-audacity',
    key: 'audacity',
    gender: 'women',
    number: '03',
    impulse: 'Audacity',
    colour: 'Deep Mustard',
    hex: '#8c6b24',
    // Female model leaning on counter (BEN04068)
    image: imgPath('audacity', 'audacity.jpg'),
    label: '03 / AUDACITY',
    sublabel: 'DEEP MUSTARD',
    views: [
      { label: 'Front Silhouette', src: imgPath('audacity', 'audacity.jpg'), alt: "Deep Mustard jacket — Women's Audacity Front Leaning Silhouette (Female Model)" },
      { label: 'Seated Portrait', src: imgPath('audacity', 'audacity_editorial_1.jpg'), alt: "Deep Mustard jacket — Women's Audacity Seated Portrait (Female Model)" },
      { label: 'Nocturne Scene', src: imgPath('audacity', 'audacity_editorial_2.jpg'), alt: "Deep Mustard jacket — Women's Audacity with Street Lamp (Female Model)" },
      { label: 'Chest Embroidery', src: imgPath('audacity', 'audacity_detail.jpg'), alt: "Deep Mustard jacket — Women's Audacity Chest Embroidery" },
      { label: 'Back Tailoring', src: imgPath('audacity', 'audacity_back.jpg'), alt: "Deep Mustard jacket — Women's Audacity Back Tailoring" }
    ]
  }
];

const allCollectionJackets = [...mensJackets, ...womensJackets];

/* -------------------------------------------------------------------
   UTILITIES
   ------------------------------------------------------------------- */

const $ = (s) => document.querySelector(s);
const isReducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const delay = (ms) => new Promise(res => setTimeout(res, ms));

let selectedJacketId = 'men-desire';
let activeDepartment = 'men';

/* -------------------------------------------------------------------
   SCROLLING & NAVIGATION
   ------------------------------------------------------------------- */

function scrollToJacket(id, smooth = true) {
  const target = document.getElementById(`jacket-${id}`);
  if (!target) return;
  const header = document.querySelector('.site-header');
  const navBar = document.querySelector('.collection-nav-bar');
  const offset = (header ? header.offsetHeight : 82) + (navBar ? navBar.offsetHeight : 50) + 16;
  const targetTop = target.getBoundingClientRect().top + window.pageYOffset - offset;
  window.scrollTo({
    top: targetTop,
    behavior: (smooth && !isReducedMotion()) ? 'smooth' : 'auto'
  });
}

function scrollToDepartment(deptId, smooth = true) {
  const target = document.getElementById(deptId);
  if (!target) return;
  const header = document.querySelector('.site-header');
  const navBar = document.querySelector('.collection-nav-bar');
  const offset = (header ? header.offsetHeight : 82) + (navBar ? navBar.offsetHeight : 50) + 12;
  const targetTop = target.getBoundingClientRect().top + window.pageYOffset - offset;
  window.scrollTo({
    top: targetTop,
    behavior: (smooth && !isReducedMotion()) ? 'smooth' : 'auto'
  });
}

function updateDepartmentSwitch(gender) {
  activeDepartment = gender;
  document.querySelectorAll('.gender-switch-btn').forEach(btn => {
    const isTarget = btn.dataset.genderTarget === `${gender}s-department`;
    btn.classList.toggle('is-active', isTarget);
    btn.setAttribute('aria-selected', isTarget ? 'true' : 'false');
  });
}

async function selectJacket(id, { scroll = false, fromAccordion = false } = {}) {
  const item = allCollectionJackets.find(j => j.id === id);
  if (!item) return;

  // If clicked again on the same jacket, scroll to its section without duplicating anything
  if (id === selectedJacketId) {
    if (scroll) {
      scrollToJacket(id);
    }
    return;
  }

  selectedJacketId = id;
  const gender = item.gender;
  updateDepartmentSwitch(gender);

  // Sync accordion active panel
  if (!fromAccordion) {
    if (gender === 'men' && window.accordionMenAPI) {
      window.accordionMenAPI.setActiveById(id, false);
    } else if (gender === 'women' && window.accordionWomenAPI) {
      window.accordionWomenAPI.setActiveById(id, false);
    }
  }

  // Highlight active section
  document.querySelectorAll('.jacket-detail-section').forEach(s => {
    s.classList.toggle('is-selected', s.id === `jacket-${id}`);
  });

  if (scroll) {
    scrollToJacket(id);
  }
}

/* -------------------------------------------------------------------
   PRODUCT GALLERY INTERACTIONS (ALL JACKETS)
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

      // Update active state among sibling cards for this jacket
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
   GENERIC ACCORDION GALLERY INITIALIZER (REUSABLE GSAP ACCORDION)
   ------------------------------------------------------------------- */

function createAccordionGallery({
  rootId,
  items,
  defaultIndex = 0,
  expandRatio = 0.52,
  onSelectJacket
}) {
  const root = document.getElementById(rootId);
  if (!root || typeof gsap === 'undefined') return null;

  let activeIndex = defaultIndex >= 0 && defaultIndex < items.length ? defaultIndex : 0;
  const duration = 0.6;
  const ease = 'power3.out';
  const parallax = 0.5;
  const tilt = 8;
  const stagger = 0.06;
  const count = items.length;

  const prefersReduced = () =>
    typeof window !== 'undefined' && window.matchMedia
      ? window.matchMedia('(prefers-reduced-motion: reduce)').matches
      : false;

  root.innerHTML = '';

  const panelEls = [];
  const mediaEls = [];
  const barEls = [];
  const textEls = [];
  let tl = null;
  let firstRun = true;
  let mediaSize = 320;

  items.forEach((item, i) => {
    const isActive = i === activeIndex;
    const panel = document.createElement('div');
    panel.className = `ag-panel${isActive ? ' ag-panel--active' : ''}`;
    panel.tabIndex = 0;
    panel.setAttribute('role', 'listitem');
    panel.setAttribute('aria-label', `${item.impulse} — ${item.colour}`);
    panel.dataset.index = String(i);
    panel.dataset.jacket = item.id;

    const frame = document.createElement('span');
    frame.className = 'ag-panel__frame';

    const media = document.createElement('span');
    media.className = 'ag-panel__media';

    const img = document.createElement('img');
    img.src = item.image;
    img.alt = `${item.colour} jacket — ${item.impulse}`;
    img.draggable = false;
    img.loading = 'lazy';

    media.appendChild(img);
    frame.appendChild(media);

    const overlay = document.createElement('span');
    overlay.className = 'ag-panel__overlay';
    overlay.setAttribute('aria-hidden', 'true');
    frame.appendChild(overlay);

    panel.appendChild(frame);

    const label = document.createElement('span');
    label.className = 'ag-panel__label';
    label.setAttribute('aria-hidden', 'true');

    const bar = document.createElement('span');
    bar.className = 'ag-panel__bar';
    barEls[i] = bar;

    const text = document.createElement('span');
    text.className = 'ag-panel__text';
    text.innerHTML = `<span class="ag-label-title">${item.label}</span><span class="ag-label-sub">${item.sublabel}</span>`;
    textEls[i] = text;

    label.appendChild(bar);
    label.appendChild(text);
    panel.appendChild(label);

    panelEls[i] = panel;
    mediaEls[i] = media;
    root.appendChild(panel);
  });

  function applyLayout(animate = true) {
    if (!panelEls.length) return;
    const isVert = window.innerWidth <= 768;
    root.classList.toggle('accordion-gallery--vertical', isVert);

    const r = Math.min(Math.max(expandRatio, 0.2), 0.9);
    const grow = count > 1 ? (r * (count - 1)) / (1 - r) : 1;

    tl?.kill();
    const dur = animate && !prefersReduced() ? duration : 0;
    tl = gsap.timeline();

    panelEls.forEach((panel, i) => {
      if (!panel) return;
      const isActive = i === activeIndex;
      panel.classList.toggle('ag-panel--active', isActive);
      panel.setAttribute('aria-current', isActive ? 'true' : 'false');

      const media = mediaEls[i];
      const bar = barEls[i];
      const text = textEls[i];

      const rot = isActive ? 0 : i < activeIndex ? tilt : -tilt;
      const rotProp = isVert ? { rotateX: -rot, rotateY: 0 } : { rotateY: rot, rotateX: 0 };

      tl.to(panel, { flexGrow: isActive ? grow : 1, ...rotProp, duration: dur, ease }, 0);

      if (media) {
        const drift = Math.max(-1.5, Math.min(1.5, activeIndex - i));
        const shift = drift * parallax * mediaSize * 0.06;
        const gray = isActive ? 0 : 1;
        tl.to(
          media,
          {
            xPercent: -50,
            yPercent: -50,
            x: isVert ? 0 : (isActive ? 0 : shift),
            y: isVert ? (isActive ? 0 : shift) : 0,
            '--ag-gray': gray,
            '--ag-dim': isActive ? 0 : 0.35,
            duration: dur,
            ease
          },
          0
        );
      }

      if (bar && text) {
        if (isActive) {
          tl.to([bar, text], { opacity: 1, x: 0, duration: dur, ease, stagger: prefersReduced() ? 0 : stagger }, 0);
        } else {
          tl.to([bar, text], { opacity: 0, x: -14, duration: dur * 0.6, ease }, 0);
        }
      }
    });
  }

  const measure = () => {
    const isVert = window.innerWidth <= 768;
    root.classList.toggle('accordion-gallery--vertical', isVert);
    const rect = root.getBoundingClientRect();
    const total = isVert ? rect.height : rect.width;
    const gap = isVert ? 8 : 12;
    const usable = Math.max(total - gap * (count - 1), 120);
    const size = Math.max(140, usable * Math.min(Math.max(expandRatio, 0.2), 0.9) * 1.22);
    mediaSize = size;
    root.style.setProperty('--ag-media-size', `${size}px`);
    applyLayout(!firstRun);
  };

  measure();
  const ro = new ResizeObserver(measure);
  ro.observe(root);
  window.addEventListener('resize', measure);

  applyLayout(!firstRun);
  firstRun = false;

  function setActive(i, triggerScroll = false) {
    if (i >= 0 && i < count) {
      activeIndex = i;
      applyLayout(true);
      if (triggerScroll && onSelectJacket) {
        onSelectJacket(items[i].id);
      }
    }
  }

  // Event Listeners: expand on hover / focus, select on click
  panelEls.forEach((panel, i) => {
    panel.addEventListener('mouseenter', () => setActive(i, false));
    panel.addEventListener('click', (e) => {
      e.preventDefault();
      setActive(i, false);
      if (onSelectJacket) {
        onSelectJacket(items[i].id);
      }
    });
    panel.addEventListener('focus', () => setActive(i, false));
    panel.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        setActive(i, false);
        if (onSelectJacket) {
          onSelectJacket(items[i].id);
        }
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
  });

  return {
    setActiveById: (id, triggerScroll = false) => {
      const idx = items.findIndex(j => j.id === id);
      if (idx >= 0 && idx !== activeIndex) {
        setActive(idx, triggerScroll);
      }
    }
  };
}

/* -------------------------------------------------------------------
   SCROLL SPY & DEPARTMENT SWITCHER
   ------------------------------------------------------------------- */

function initScrollSpy() {
  const mensBlock = document.getElementById('mens-department');
  const womensBlock = document.getElementById('womens-department');

  if (window.IntersectionObserver) {
    const deptObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          if (entry.target.id === 'mens-department') {
            updateDepartmentSwitch('men');
          } else if (entry.target.id === 'womens-department') {
            updateDepartmentSwitch('women');
          }
        }
      });
    }, {
      rootMargin: '-20% 0px -40% 0px',
      threshold: [0.1, 0.4]
    });

    if (mensBlock) deptObserver.observe(mensBlock);
    if (womensBlock) deptObserver.observe(womensBlock);
  }

  document.querySelectorAll('.gender-switch-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = btn.dataset.genderTarget;
      if (targetId) {
        scrollToDepartment(targetId);
      }
    });
  });
}

/* -------------------------------------------------------------------
   3D PERSPECTIVE DRIFT WALL (HERO)
   ------------------------------------------------------------------- */

const wallTiles = [
  { image: 'jackets_original/resized_BEN03137.webp', title: 'Curiosity · Dark Navy Back', jacket: 'men-curiosity' },
  { image: 'jackets_original/resized_BEN03166.webp', title: 'Curiosity · Navy Profile (Men)', jacket: 'men-curiosity' },
  { image: 'jackets_original/resized_BEN03202.webp', title: 'Curiosity · Male Model Navy', jacket: 'men-curiosity' },
  { image: 'jackets_original/resized_BEN03655.webp', title: 'Temptation · Forest Green Suede', jacket: 'men-temptation' },
  { image: 'assets/collection/nocturne/temptation/temptation.jpg', title: 'Temptation · Forest Green (Men)', jacket: 'men-temptation' },
  { image: 'jackets_original/resized_BEN03806.webp', title: 'Desire · Deep Red Suede', jacket: 'men-desire' },
  { image: 'jackets_original/resized_BEN03515.webp', title: 'Desire · Deep Red Male Standing', jacket: 'men-desire' },
  { image: 'jackets_original/resized_BEN03619.webp', title: 'Desire · Red Tonal Embroidery (Men)', jacket: 'men-desire' },
  { image: 'jackets_original/resized_BEN03767.webp', title: 'Desire · Deep Red Portrait (Men)', jacket: 'men-desire' },
  { image: 'assets/collection/nocturne/desire/desire_editorial_3.jpg', title: 'Desire · Women’s Standing Portrait', jacket: 'women-desire' },
  { image: 'assets/collection/nocturne/audacity/audacity_editorial_1.jpg', title: 'Audacity · Women’s Seated Portrait', jacket: 'women-audacity' },
  { image: 'assets/collection/nocturne/audacity/audacity_lookbook_1.jpg', title: 'Audacity · Deep Mustard Suede (Men)', jacket: 'men-audacity' },
  { image: 'jackets_original/resized_BEN04068.webp', title: 'Audacity · Mustard Leaning (Women)', jacket: 'women-audacity' },
  { image: 'jackets_original/resized_BEN03324.webp', title: 'Insolence · Black Suede Seated (Men)', jacket: 'men-insolence' },
  { image: 'assets/collection/nocturne/audacity/audacity_editorial_2.jpg', title: 'Audacity · Women’s Street Scene', jacket: 'women-audacity' },
  { image: 'jackets_original/resized_BEN04053.webp', title: 'Insolence · Black Suede Lookbook (Men)', jacket: 'men-insolence' },
  { image: 'assets/collection/nocturne/insolence/insolence.jpg', title: 'Insolence · Black Armchair (Men)', jacket: 'men-insolence' },
  { image: 'assets/collection/nocturne/curiosity/curiosity.jpg', title: 'Curiosity · Navy Chest Embroidery', jacket: 'men-curiosity' },
  { image: 'assets/collection/nocturne/desire/desire_editorial_1.jpg', title: 'Desire · Women’s Evening Lounge', jacket: 'women-desire' }
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
        tile.dataset.tileId = tileId;
        tile.dataset.col = String(c);
        tile.dataset.jacket = item.jacket;
        tile.style.cursor = 'pointer';
        tile.addEventListener('click', () => {
          selectJacket(item.jacket, { scroll: true });
        });

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

        inner.appendChild(img);
        inner.appendChild(overlay);
        tile.appendChild(inner);
        track.appendChild(tile);
      });
    }

    colEl.appendChild(track);
    plane.appendChild(colEl);
  });

  container.innerHTML = '';
  container.appendChild(root);

  let activeTileEl = null;
  let hoveredCol = -1;
  let wallHovered = false;
  const pointer = { x: 0, y: 0 };
  const pointerDamped = { x: 0, y: 0 };
  let lastTs = null;

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

    requestAnimationFrame(animate);
  }

  requestAnimationFrame(animate);

  const ro = new ResizeObserver(([entry]) => {
    const h = entry.contentRect.height;
    if (h && Math.abs(h - containerHeight) > 30) {
      containerHeight = h;
      columnMeta = columnItems.map(col => getColumnMeta(col));
    }
  });
  ro.observe(container);

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
}

/* -------------------------------------------------------------------
   INIT
   ------------------------------------------------------------------- */

function init() {
  initDriftWall();

  // Initialize Men's Accordion Carousel (5 jackets)
  window.accordionMenAPI = createAccordionGallery({
    rootId: 'accordionGalleryMen',
    items: mensJackets,
    defaultIndex: 2, // Desire
    onSelectJacket: (id) => selectJacket(id, { scroll: true, fromAccordion: true })
  });

  // Initialize Women's Accordion Carousel (3 jackets)
  window.accordionWomenAPI = createAccordionGallery({
    rootId: 'accordionGalleryWomen',
    items: womensJackets,
    defaultIndex: 1, // Desire
    onSelectJacket: (id) => selectJacket(id, { scroll: true, fromAccordion: true })
  });

  setupGalleryInteractions();
  initScrollSpy();

  // Preload primary assets
  allCollectionJackets.forEach(j => {
    const img = new Image();
    img.src = j.image;
    if (j.views && j.views[0]) {
      const vImg = new Image();
      vImg.src = j.views[0].src;
    }
  });
}

init();
"""

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(new_app_js)

print('app.js written with clean model separation! Bytes:', len(new_app_js))
