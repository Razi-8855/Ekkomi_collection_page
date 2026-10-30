'use strict';

// Graceful GSAP fallback shim (guarantees accordion works offline, on weak mobile connections, or if CDN blocked)
if (typeof window !== 'undefined' && typeof window.gsap === 'undefined') {
  window.gsap = {
    timeline: function() {
      return {
        to: function(targets, vars) {
          const list = Array.isArray(targets) ? targets : [targets];
          list.forEach(el => {
            if (!el || !el.style) return;
            if (vars.flexGrow !== undefined) el.style.flexGrow = vars.flexGrow;
            if (vars.opacity !== undefined) el.style.opacity = vars.opacity;
            if (vars['--ag-gray'] !== undefined) el.style.setProperty('--ag-gray', vars['--ag-gray']);
            if (vars['--ag-dim'] !== undefined) el.style.setProperty('--ag-dim', vars['--ag-dim']);
            if (vars.rotateY !== undefined || vars.rotateX !== undefined) {
              const rx = vars.rotateX || 0;
              const ry = vars.rotateY || 0;
              el.style.transform = `perspective(1000px) rotateX(${rx}deg) rotateY(${ry}deg)`;
            }
            if (vars.xPercent !== undefined || vars.yPercent !== undefined || vars.x !== undefined || vars.y !== undefined) {
              const xp = vars.xPercent !== undefined ? vars.xPercent : 0;
              const yp = vars.yPercent !== undefined ? vars.yPercent : 0;
              const x = vars.x || 0;
              const y = vars.y || 0;
              el.style.transform = `translate(calc(${xp}% + ${x}px), calc(${yp}% + ${y}px))`;
            }
          });
          return this;
        },
        kill: function() {}
      };
    }
  };
}

/* ===================================================================
   EKKOMI — NOCTURNE COLLECTION
   Data & Interaction Logic: Department Tabs + Dynamic Showcase
   =================================================================== */

const IMAGE_BASE = 'assets/collection/nocturne';
const IMG_V = '?v=curiosity_female_v1';
const imgPath = (folder, file) => `${IMAGE_BASE}/${folder}/${file}${IMG_V}`;

/* -------------------------------------------------------------------
   MEN'S COLLECTION DATA (5 JACKETS — 100% MALE / STILL GARMENT)
   ------------------------------------------------------------------- */

const mensJackets = [
  {
    id: "men-curiosity",
    key: "curiosity",
    gender: "men",
    number: "01",
    impulse: "Curiosity",
    colour: "Dark Navy",
    hex: "#1c2838",
    inStock: false,
    image: imgPath('curiosity', 'curiosity_lookbook_1.jpg'),
    label: "01 / CURIOSITY",
    sublabel: "",
    headline: "The room was loud. The impulse was quiet. Curiosity doesn’t ask for permission.",
    narrative: "Midnight impulse given architectural form. Suede and Italian lambskin punctuated by hand-guided tonal needlework—balanced between severe restraint and private appetite.",
    craft: [
      { title: "The Material", desc: "Supple suede meeting hand-selected Italian lambskin with a deep matte finish." },
      { title: "The Embroidery", desc: "Tonal needlework along the chest and collar, visible only to those standing close." },
      { title: "The Inner World", desc: "Full interior lined with custom illustrated silk—a private artwork worn against the skin." }
    ],
    views: [
      { label: 'Front Silhouette', src: imgPath('curiosity', 'curiosity_lookbook_1.jpg'), alt: "Curiosity Front Silhouette" },
      { label: 'Profile Silhouette', src: imgPath('curiosity', 'curiosity_lookbook_2.jpg'), alt: "Curiosity Profile Silhouette" },
      { label: 'Interior Silk', src: 'jackets_original/resized_BEN03202.webp', alt: "Curiosity Interior Silk Lining" },
      { label: 'Back Tailoring', src: 'jackets_original/resized_BEN03137.webp', alt: "Curiosity Back Tailoring" },
      { label: 'Embroidery Detail', src: imgPath('curiosity', 'curiosity_detail.jpg'), alt: "Curiosity Embroidery Detail" },
      { label: 'Evening Perspective', src: imgPath('curiosity', 'curiosity.jpg'), alt: "Curiosity Evening Perspective" }
    ]
  },
  {
    id: "men-temptation",
    key: "temptation",
    gender: "men",
    number: "02",
    impulse: "Temptation",
    colour: "Forest Green",
    hex: "#27382b",
    inStock: true,
    image: imgPath('temptation', 'temptation.jpg'),
    label: "02 / TEMPTATION",
    sublabel: "",
    headline: "You knew where the line was. You stepped across it on purpose.",
    narrative: "Supple suede tailored into an irresistible impulse. A jacket designed for rooms that reward presence, cut with a relaxed modern drape and intricate foliage-inspired needlework.",
    craft: [
      { title: "The Material", desc: "Velvety suede offering exceptional drape and depth under evening light." },
      { title: "The Embroidery", desc: "Botanical needlework tracing the shoulders—dense, deliberate, and entirely hand-guided." },
      { title: "The Inner World", desc: "Silk interior carrying the Nocturne motif—a nocturnal garden unseen by the world." }
    ],
    views: [
      { label: 'Front Silhouette', src: imgPath('temptation', 'temptation.jpg'), alt: "Temptation Front Silhouette" },
      { label: 'Embroidery Detail', src: imgPath('temptation', 'temptation_detail.jpg'), alt: "Temptation Embroidery Detail" },
      { label: 'Back Tailoring', src: imgPath('temptation', 'temptation_back.jpg'), alt: "Temptation Back Tailoring" },
      { label: 'Lookbook Perspective', src: imgPath('temptation', 'temptation_lookbook_1.jpg'), alt: "Temptation Lookbook Perspective" },
      { label: 'Editorial Portrait', src: imgPath('temptation', 'temptation_lookbook_2.jpg'), alt: "Temptation Editorial Portrait" },
      { label: 'Texture & Finish', src: 'jackets_original/resized_BEN03655.webp', alt: "Temptation Texture and Finish" }
    ]
  },
  {
    id: "men-desire",
    key: "desire",
    gender: "men",
    number: "03",
    impulse: "Desire",
    colour: "Deep Red",
    hex: "#662225",
    inStock: false,
    image: imgPath('desire', 'desire.jpg'),
    label: "03 / DESIRE",
    sublabel: "",
    headline: "Wanting more is not greed. Sometimes it is vision.",
    narrative: "The instinct that refuses to settle. Rich tactile suede meeting shifting tonal needlework—balanced between severe restraint and private appetite.",
    craft: [
      { title: "The Material", desc: "Rich tactile suede with a brushed nap that catches and deepens the light." },
      { title: "The Embroidery", desc: "Shifting needlework across the upper chest—subtle from a distance, magnetic up close." },
      { title: "The Inner World", desc: "Lined in bespoke Nocturne silk—rich, narrative, and intentionally personal." }
    ],
    views: [
      { label: 'Sitting Silhouette', src: imgPath('desire', 'desire.jpg'), alt: "Desire Sitting Silhouette" },
      { label: 'Standing Portrait', src: 'jackets_original/resized_BEN03515.webp', alt: "Desire Standing Portrait" },
      { label: 'Back Embroidery', src: imgPath('desire', 'desire_back.jpg'), alt: "Desire Back Embroidery" },
      { label: 'Evening Perspective', src: 'jackets_original/resized_BEN03767.webp', alt: "Desire Evening Perspective" },
      { label: 'Tonal Needlework', src: 'jackets_original/resized_BEN03619.webp', alt: "Desire Tonal Needlework" },
      { label: 'Suede Nap & Detail', src: imgPath('desire', 'desire_detail.jpg'), alt: "Desire Suede Nap Detail" }
    ]
  },
  {
    id: "men-audacity",
    key: "audacity",
    gender: "men",
    number: "04",
    impulse: "Audacity",
    colour: "Deep Mustard",
    hex: "#8c6b24",
    inStock: true,
    image: imgPath('audacity', 'audacity_lookbook_1.jpg'),
    label: "04 / AUDACITY",
    sublabel: "",
    headline: "Confidence before permission arrives.",
    narrative: "Confidence before permission arrives. Sculptural suede tailored with authority, balanced by fine tonal needlework that commands attention without raising its voice.",
    craft: [
      { title: "The Material", desc: "Sculptural suede with a rich, velvety hand-feel and distinct presence." },
      { title: "The Embroidery", desc: "High-contrast geometric embroidery across the collar and cuffs." },
      { title: "The Inner World", desc: "A private flourish of illustrated silk concealed within the garment." }
    ],
    views: [
      { label: 'Standing Silhouette', src: imgPath('audacity', 'audacity_lookbook_1.jpg'), alt: "Audacity Standing Silhouette" },
      { label: 'Tailoring & Scarf', src: imgPath('audacity', 'audacity_lookbook_2.jpg'), alt: "Audacity Tailoring and Scarf" },
      { label: 'Lookbook Perspective', src: 'jackets_original/resized_BEN03893.webp', alt: "Audacity Lookbook Perspective" },
      { label: 'Embroidery Detail', src: imgPath('audacity', 'audacity_detail.jpg'), alt: "Audacity Embroidery Detail" },
      { label: 'Back Tailoring', src: imgPath('audacity', 'audacity_back.jpg'), alt: "Audacity Back Tailoring" }
    ]
  },
  {
    id: "men-insolence",
    key: "insolence",
    gender: "men",
    number: "05",
    impulse: "Insolence",
    colour: "Black",
    hex: "#1a1716",
    inStock: false,
    image: imgPath('insolence', 'insolence.jpg'),
    label: "05 / INSOLENCE",
    sublabel: "",
    headline: "The rules were written by people who wanted you to stay quiet.",
    narrative: "Velvety suede cut with unapologetic precision. Heavy embroidery tracing the shoulders—designed to speak only when spoken to, with effortless nocturnal gravity.",
    craft: [
      { title: "The Material", desc: "Velvety suede with a deep matte nap that absorbs ambient light." },
      { title: "The Embroidery", desc: "Tonal obsidian threadwork—sculpted into the suede, tactile to the touch." },
      { title: "The Inner World", desc: "Contrast silk lining with Nocturne illustrated artwork." }
    ],
    views: [
      { label: 'Front Silhouette', src: imgPath('insolence', 'insolence.jpg'), alt: "Insolence Front Silhouette" },
      { label: 'Standing Perspective', src: 'jackets_original/resized_BEN03307.webp', alt: "Insolence Standing Perspective" },
      { label: 'Editorial Portrait', src: 'jackets_original/resized_BEN03324.webp', alt: "Insolence Editorial Portrait" },
      { label: 'Embroidery Detail', src: imgPath('insolence', 'insolence_detail.jpg'), alt: "Insolence Embroidery Detail" },
      { label: 'Back Tailoring', src: imgPath('insolence', 'insolence_back.jpg'), alt: "Insolence Back Tailoring" }
    ]
  }
];

/* -------------------------------------------------------------------
   WOMENS COLLECTION DATA
   ------------------------------------------------------------------- */

const womensJackets = [
  {
    id: "women-curiosity",
    key: "curiosity",
    gender: "women",
    number: "01",
    impulse: "Curiosity",
    colour: "Dark Navy",
    hex: "#1c2838",
    inStock: false,
    image: imgPath('curiosity', 'curiosity_women_1.jpg'),
    label: "01 / CURIOSITY",
    sublabel: "",
    headline: "The room was loud. The impulse was quiet. Curiosity doesn’t ask for permission.",
    narrative: "Midnight impulse given architectural form. Sculptural Italian lambskin and suede tailored to contour the female form with effortless authority.",
    craft: [
      { title: "The Material", desc: "Supple suede meeting hand-selected Italian lambskin with a deep matte finish." },
      { title: "The Embroidery", desc: "Tonal needlework along the chest and collar, visible only to those standing close." },
      { title: "The Inner World", desc: "Full interior lined with custom illustrated silk—a private artwork worn against the skin." }
    ],
    views: [
      { label: 'Standing Silhouette', src: imgPath('curiosity', 'curiosity_women_1.jpg'), alt: "Curiosity Standing Silhouette" },
      { label: 'Seated Perspective', src: imgPath('curiosity', 'curiosity_women_2.jpg'), alt: "Curiosity Seated Perspective" },
      { label: 'Back Tailoring', src: imgPath('curiosity', 'curiosity_women_3.jpg'), alt: "Curiosity Back Tailoring" },
      { label: 'Tailoring Detail', src: imgPath('curiosity', 'curiosity_women_4.jpg'), alt: "Curiosity Tailoring Detail" },
      { label: 'Editorial Portrait', src: imgPath('curiosity', 'curiosity_women_5.jpg'), alt: "Curiosity Editorial Portrait" }
    ]
  },
  {
    id: "women-desire",
    key: "desire",
    gender: "women",
    number: "02",
    impulse: "Desire",
    colour: "Deep Red",
    hex: "#662225",
    inStock: false,
    image: imgPath('desire', 'desire_editorial_3.jpg'),
    label: "02 / DESIRE",
    sublabel: "",
    headline: "Wanting more is not greed. Sometimes it is vision.",
    narrative: "The instinct that refuses to settle. Rich tactile suede meeting shifting tonal needlework—balanced between severe restraint and private appetite.",
    craft: [
      { title: "The Material", desc: "Rich tactile suede with a brushed nap that catches and deepens the light." },
      { title: "The Embroidery", desc: "Shifting needlework across the upper bodice—subtle from a distance, magnetic up close." },
      { title: "The Inner World", desc: "Lined in bespoke Nocturne silk—rich, narrative, and intentionally personal." }
    ],
    views: [
      { label: 'Standing Silhouette', src: imgPath('desire', 'desire_editorial_3.jpg'), alt: "Desire Standing Silhouette" },
      { label: 'Seated Perspective', src: imgPath('desire', 'desire_editorial_1.jpg'), alt: "Desire Seated Perspective" },
      { label: 'Profile Silhouette', src: imgPath('desire', 'desire_editorial_2.jpg'), alt: "Desire Profile Silhouette" },
      { label: 'Embroidery Detail', src: imgPath('desire', 'desire_detail.jpg'), alt: "Desire Embroidery Detail" }
    ]
  },
  {
    id: "women-audacity",
    key: "audacity",
    gender: "women",
    number: "03",
    impulse: "Audacity",
    colour: "Deep Mustard",
    hex: "#8c6b24",
    inStock: true,
    image: imgPath('audacity', 'audacity.jpg'),
    label: "03 / AUDACITY",
    sublabel: "",
    headline: "Confidence before permission arrives.",
    narrative: "Confidence before permission arrives. Sculptural suede tailored with authority, balanced by fine tonal needlework that commands attention without raising its voice.",
    craft: [
      { title: "The Material", desc: "Sculptural suede with a rich, velvety hand-feel and distinct structure." },
      { title: "The Embroidery", desc: "Bodice tonal embroidery contouring the silhouette without excess." },
      { title: "The Inner World", desc: "A private flourish of illustrated silk concealed within the garment." }
    ],
    views: [
      { label: 'Front Silhouette', src: imgPath('audacity', 'audacity.jpg'), alt: "Audacity Front Silhouette" },
      { label: 'Seated Portrait', src: imgPath('audacity', 'audacity_editorial_1.jpg'), alt: "Audacity Seated Portrait" },
      { label: 'Nocturne Scene', src: imgPath('audacity', 'audacity_editorial_2.jpg'), alt: "Audacity Nocturne Scene" },
      { label: 'Embroidery Detail', src: imgPath('audacity', 'audacity_detail.jpg'), alt: "Audacity Embroidery Detail" }
    ]
  }
];

const allCollectionJackets = [...mensJackets, ...womensJackets];

/* -------------------------------------------------------------------
   STATE & UTILITIES
   ------------------------------------------------------------------- */

const isReducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

let selectedJacketId = 'men-desire';
let activeDepartment = 'men';

// Expose state for external consumers (e.g. registration modal, telemetry)
window.currentSelectedJacket = mensJackets[2];
window.currentSelectedDepartment = 'men';

/* -------------------------------------------------------------------
   SMOOTH SCROLLING
   ------------------------------------------------------------------- */

function scrollToShowcase(smooth = true) {
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
}

function scrollToDepartmentHeader(dept, smooth = true) {
  const targetId = dept === 'men' ? 'mens-department' : 'womens-department';
  const target = document.getElementById(targetId);
  if (!target) return;
  const header = document.querySelector('.site-header');
  const navBar = document.querySelector('.collection-nav-bar');
  const offset = (header ? header.offsetHeight : 82) + (navBar ? navBar.offsetHeight : 50) + 12;
  const targetTop = target.getBoundingClientRect().top + window.pageYOffset - offset;
  window.scrollTo({
    top: Math.max(0, targetTop),
    behavior: (smooth && !isReducedMotion()) ? 'smooth' : 'auto'
  });
}

/* -------------------------------------------------------------------
   DEPARTMENT TABS (MEN vs WOMEN SEPARATE SECTIONS)
   ------------------------------------------------------------------- */

function switchDepartment(dept, { syncJacket = true, scroll = false } = {}) {
  if (dept !== 'men' && dept !== 'women') return;
  activeDepartment = dept;
  window.currentSelectedDepartment = dept;
  document.body.dataset.activeDepartment = dept;

  const tabMen = document.getElementById('tab-gender-men');
  const tabWomen = document.getElementById('tab-gender-women');
  if (tabMen) {
    tabMen.classList.toggle('is-active', dept === 'men');
    tabMen.setAttribute('aria-selected', dept === 'men' ? 'true' : 'false');
  }
  if (tabWomen) {
    tabWomen.classList.toggle('is-active', dept === 'women');
    tabWomen.setAttribute('aria-selected', dept === 'women' ? 'true' : 'false');
  }

  const mensBlock = document.getElementById('mens-department');
  const womensBlock = document.getElementById('womens-department');

  if (dept === 'men') {
    if (womensBlock) {
      womensBlock.classList.remove('is-active');
      womensBlock.classList.add('is-hidden');
      womensBlock.style.display = 'none';
    }
    if (mensBlock) {
      mensBlock.style.display = 'block';
      mensBlock.classList.remove('is-hidden');
      mensBlock.classList.add('is-active');
      window.accordionMenAPI?.measure();
    }
  } else {
    if (mensBlock) {
      mensBlock.classList.remove('is-active');
      mensBlock.classList.add('is-hidden');
      mensBlock.style.display = 'none';
    }
    if (womensBlock) {
      womensBlock.style.display = 'block';
      womensBlock.classList.remove('is-hidden');
      womensBlock.classList.add('is-active');
      window.accordionWomenAPI?.measure();
    }
  }

  if (syncJacket) {
    // Pick the default/active jacket for this department
    const targetId = dept === 'men' ? 'men-desire' : 'women-desire';
    selectJacket(targetId, { scroll, fromDepartmentSwitch: true });
  }

  if (scroll) {
    scrollToDepartmentHeader(dept);
  }
}

/* -------------------------------------------------------------------
   DYNAMIC PRODUCT SHOWCASE (UPDATES IN-PLACE WITHOUT LONG SCROLLING)
   ------------------------------------------------------------------- */

function renderShowcase(jacket) {
  const showcase = document.getElementById('productShowcase');
  if (!showcase) return;

  // Subtle luxury fade transition
  showcase.classList.add('is-updating');

  setTimeout(() => {
    const currentList = jacket.gender === 'men' ? mensJackets : womensJackets;
    const currentIndex = currentList.findIndex(j => j.id === jacket.id);
    const prevIndex = (currentIndex - 1 + currentList.length) % currentList.length;
    const nextIndex = (currentIndex + 1) % currentList.length;
    const prevJacket = currentList[prevIndex];
    const nextJacket = currentList[nextIndex];

    const departmentTitle = jacket.gender === 'men' ? "Men's Collection" : "Women's Collection";
    const carouselId = jacket.gender === 'men' ? 'accordionGalleryMen' : 'accordionGalleryWomen';

    const craftHtml = jacket.craft.map(c => `
      <div class="craft-item">
        <dt>${c.title}</dt>
        <dd>${c.desc}</dd>
      </div>
    `).join('');

    const firstView = jacket.views[0] || { src: jacket.image, alt: jacket.impulse, label: 'Front Silhouette' };

    const viewsHtml = jacket.views.map((v, i) => `
      <button class="gallery-view-card${i === 0 ? ' is-active' : ''}"
              type="button"
              role="listitem"
              aria-label="View ${v.label} for ${jacket.impulse}"
              aria-pressed="${i === 0 ? 'true' : 'false'}"
              data-jacket-id="${jacket.id}"
              data-view-index="${i}"
              data-src="${v.src}"
              data-alt="${v.alt}"
              data-label="${v.label}">
        <div class="view-card__frame">
          <img class="view-card__img"
               src="${v.src}"
               alt="${v.alt}"
               loading="lazy"
               decoding="async"
               width="400"
               height="600" />
          <span class="view-card__overlay" aria-hidden="true"></span>
        </div>
        <div class="view-card__info">
          <span class="view-card__index">${String(i + 1).padStart(2, '0')}</span>
          <span class="view-card__label">${v.label}</span>
        </div>
      </button>
    `).join('');

    showcase.innerHTML = `
      <div class="section jacket-detail-inner">
        <div class="showcase-unified-grid">
          <!-- Left Column: Sticky Hero Stage Gallery -->
          <div class="showcase-stage-col">
            <div class="gallery-stage" id="showcaseStage">
              <div class="gallery-stage__frame">
                <img class="gallery-stage__img"
                     id="showcaseStageImg"
                     src="${firstView.src}"
                     alt="${firstView.alt}"
                     loading="eager"
                     decoding="async"
                     fetchpriority="high"
                     width="1200"
                     height="1800" />
                <div class="gallery-stage__badge">
                  <span class="badge-indicator" aria-hidden="true"></span>
                  <span class="stage-caption" id="showcaseStageCaption">${firstView.label}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column: Unified Story, Perspectives & Craftsmanship -->
          <div class="showcase-narrative-col">
            <!-- Meta Bar: Eyebrow + Quick Nav -->
            <div class="showcase-meta-bar">
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

            <!-- Jacket Title Row -->
            <div class="jacket-title-row">
              <h3 class="jacket-name" id="showcaseJacketTitle">${jacket.impulse}</h3>
              ${jacket.inStock === false ? '<span class="jacket-stock-badge is-oos">OUT OF STOCK</span>' : ''}
            </div>


            <!-- Poetic Script Headline Quote -->
            <p class="jacket-headline">${jacket.headline}</p>

            <!-- Narrative Story Paragraph -->
            <p class="jacket-narrative">${jacket.narrative}</p>

            

            <!-- Photographic Perspectives Gallery -->
            <div class="jacket-perspectives-block" data-gallery-jacket="${jacket.id}">
              <div class="gallery-section-bar">
                <h4 class="gallery-heading">Photographic Perspectives</h4>
                <span class="gallery-counter-tag">${jacket.views.length} Perspectives</span>
              </div>
              <div class="gallery-views-grid" role="list" aria-label="${departmentTitle} ${jacket.impulse} jacket views">
                ${viewsHtml}
              </div>
            </div>

            <!-- Craftsmanship Specifications -->
            <dl class="jacket-craft-list">
              ${craftHtml}
            </dl>

            <!-- Waitlist CTA inside Showcase (Positioned after craftsmanship specs) -->
            <div class="showcase-cta-wrap">
              <button type="button" class="showcase-waitlist-btn btn-join-waitlist" id="showcaseWaitlistBtn" data-open-waitlist>
                ${jacket.inStock === false ? 'OUT OF STOCK &mdash; JOIN THE WAITING LIST' : 'JOIN THE WAITING LIST'}
              </button>
            </div>
          </div>
        </div>

        <!-- Understated Product Navigation Bar -->
        <nav class="showcase-bottom-nav" aria-label="Jacket navigation">
          <button type="button" class="showcase-nav-btn prev-jacket-btn" id="prevJacketBtn" aria-label="Previous jacket: ${prevJacket.number} ${prevJacket.impulse}">
            <span class="nav-arrow" aria-hidden="true">&larr;</span>
            <span class="nav-label-wrap">
              <span class="nav-sub">Previous Jacket</span>
              <span class="nav-jacket-name">${prevJacket.number} &middot; ${prevJacket.impulse}</span>
            </span>
          </button>

          <a class="nav-back-link" id="backToCarouselLink" href="#${carouselId}" aria-label="Return to ${departmentTitle} carousel">
            <span class="arrow-up" aria-hidden="true">&uarr;</span> Back to Carousel
          </a>

          <button type="button" class="showcase-nav-btn next-jacket-btn" id="nextJacketBtn" aria-label="Next jacket: ${nextJacket.number} ${nextJacket.impulse}">
            <span class="nav-label-wrap">
              <span class="nav-sub">Next Jacket</span>
              <span class="nav-jacket-name">${nextJacket.number} &middot; ${nextJacket.impulse}</span>
            </span>
            <span class="nav-arrow" aria-hidden="true">&rarr;</span>
          </button>
        </nav>
      </div>    `;

    // Bind thumbnail click events for main stage swapping
    const stage = document.getElementById('showcaseStage');
    const stageImg = document.getElementById('showcaseStageImg');
    const stageCaption = document.getElementById('showcaseStageCaption');
    const cards = showcase.querySelectorAll('.gallery-view-card');

    cards.forEach(card => {
      card.addEventListener('click', (e) => {
        e.preventDefault();
        const src = card.dataset.src;
        const alt = card.dataset.alt;
        const label = card.dataset.label;

        cards.forEach(c => {
          c.classList.remove('is-active');
          c.setAttribute('aria-pressed', 'false');
        });
        card.classList.add('is-active');
        card.setAttribute('aria-pressed', 'true');

        if (stage && stageImg) {
          stage.classList.add('is-switching');
          setTimeout(() => {
            stageImg.src = src;
            stageImg.alt = alt;
            if (stageCaption) stageCaption.textContent = label;
            stage.classList.remove('is-switching');
          }, 140);
        }
      });
    });

    // Bind Previous / Next Navigation (Both bottom buttons & top quick buttons)
    const prevBtn = document.getElementById('prevJacketBtn');
    const nextBtn = document.getElementById('nextJacketBtn');
    const prevQuick = document.getElementById('prevQuickBtn');
    const nextQuick = document.getElementById('nextQuickBtn');

    const handlePrev = (e) => {
      e.preventDefault();
      selectJacket(prevJacket.id, { scroll: true, userInitiated: true });
    };

    const handleNext = (e) => {
      e.preventDefault();
      selectJacket(nextJacket.id, { scroll: true, userInitiated: true });
    };

    if (prevBtn) prevBtn.addEventListener('click', handlePrev);
    if (nextBtn) nextBtn.addEventListener('click', handleNext);
    if (prevQuick) prevQuick.addEventListener('click', handlePrev);
    if (nextQuick) nextQuick.addEventListener('click', handleNext);

    // Bind Back to Carousel Link
    const backLink = document.getElementById('backToCarouselLink');
    if (backLink) {
      backLink.addEventListener('click', (e) => {
        e.preventDefault();
        scrollToDepartmentHeader(jacket.gender);
      });
    }

    // Reveal with subtle fade in
    showcase.classList.remove('is-updating');
  }, 160);
}

/* -------------------------------------------------------------------
   SELECT JACKET
   ------------------------------------------------------------------- */

function selectJacket(id, { scroll = false, fromAccordion = false, fromDepartmentSwitch = false, userInitiated = false } = {}) {
  const item = allCollectionJackets.find(j => j.id === id);
  if (!item) return;

  if (item.gender !== activeDepartment) {
    switchDepartment(item.gender, { syncJacket: false });
  }

  selectedJacketId = id;
  window.currentSelectedJacket = item;
  if (userInitiated) {
    window.userHasSelectedJacket = true;
  }
  document.body.dataset.selectedJacket = id;

  // Sync accordion active panel
  if (!fromAccordion) {
    if (item.gender === 'men' && window.accordionMenAPI) {
      window.accordionMenAPI.setActiveById(id, false);
    } else if (item.gender === 'women' && window.accordionWomenAPI) {
      window.accordionWomenAPI.setActiveById(id, false);
    }
  }

  // Render into dynamic showcase
  renderShowcase(item);

  if (scroll) {
    scrollToShowcase(true);
  }

  // If user clicked this jacket and it is marked out of stock, trigger waitlist popup with jacket details!
  if (userInitiated && item.inStock === false) {
    setTimeout(() => {
      if (window.EkkomiWaitlist && window.EkkomiWaitlist.open) {
        window.EkkomiWaitlist.open({
          collection: item.gender,
          jacketKey: item.key,
          jacketName: item.impulse,
          jacketNumber: item.number,
          jacketHex: item.hex,
          jacketColour: item.colour,
          outOfStock: true
        });
      }
    }, 320);
  }
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
  if (!root) return null;

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
    panel.setAttribute('aria-label', `${item.impulse} — Ekkomi Nocturne`);
    panel.dataset.index = String(i);
    panel.dataset.jacket = item.id;

    const frame = document.createElement('span');
    frame.className = 'ag-panel__frame';

    const media = document.createElement('span');
    media.className = 'ag-panel__media';

    const img = document.createElement('img');
    img.src = item.image;
    img.alt = `${item.impulse} jacket — Ekkomi Nocturne`;
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
    text.innerHTML = `<span class="ag-label-title">${item.label}</span>`;
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
    const isVert = window.innerWidth <= 640;
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
    const isVert = window.innerWidth <= 640;
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
  if ('ResizeObserver' in window) {
    const ro = new ResizeObserver(measure);
    ro.observe(root);
  } else {
    window.addEventListener('resize', measure, { passive: true });
  }

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
    },
    measure: () => {
      measure();
    }
  };
}

/* -------------------------------------------------------------------
   3D PERSPECTIVE DRIFT WALL (HERO)
   ------------------------------------------------------------------- */

const wallTiles = [
  { image: 'jackets_original/resized_BEN03137.webp', title: 'Curiosity · Back Silhouette', jacket: 'men-curiosity' },
  { image: 'jackets_original/resized_BEN03166.webp', title: 'Curiosity · Profile Silhouette', jacket: 'men-curiosity' },
  { image: 'jackets_original/resized_BEN03202.webp', title: 'Curiosity · Editorial Perspective', jacket: 'men-curiosity' },
  { image: 'jackets_original/resized_BEN03655.webp', title: 'Temptation · Suede Tailoring', jacket: 'men-temptation' },
  { image: 'assets/collection/nocturne/temptation/temptation.jpg', title: 'Temptation · Front Silhouette', jacket: 'men-temptation' },
  { image: 'jackets_original/resized_BEN03806.webp', title: 'Desire · Suede Tailoring', jacket: 'men-desire' },
  { image: 'jackets_original/resized_BEN03515.webp', title: 'Desire · Standing Silhouette', jacket: 'men-desire' },
  { image: 'jackets_original/resized_BEN03619.webp', title: 'Desire · Tonal Embroidery', jacket: 'men-desire' },
  { image: 'jackets_original/resized_BEN03767.webp', title: 'Desire · Portrait Perspective', jacket: 'men-desire' },
  { image: 'assets/collection/nocturne/desire/desire_editorial_3.jpg', title: 'Desire · Women’s Standing Portrait', jacket: 'women-desire' },
  { image: 'assets/collection/nocturne/audacity/audacity_editorial_1.jpg', title: 'Audacity · Women’s Seated Portrait', jacket: 'women-audacity' },
  { image: 'assets/collection/nocturne/audacity/audacity_lookbook_1.jpg', title: 'Audacity · Suede Tailoring', jacket: 'men-audacity' },
  { image: 'jackets_original/resized_BEN03893.webp', title: 'Audacity · Lookbook Styling', jacket: 'men-audacity' },
  { image: 'jackets_original/resized_BEN03307.webp', title: 'Insolence · Suede Tailoring', jacket: 'men-insolence' },
  { image: 'jackets_original/resized_BEN03324.webp', title: 'Insolence · Male Model Seated', jacket: 'men-insolence' }
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
  const autoPlay = true;

  const root = document.createElement('div');
  root.className = 'drift-wall';
  root.style.setProperty('--dw-tile-w', `${tileWidth}px`);
  root.style.setProperty('--dw-tile-h', `${tileHeight}px`);
  root.style.setProperty('--dw-gap', `${gap}px`);
  root.style.setProperty('--dw-radius', `${radius}px`);

  const plane = document.createElement('div');
  plane.className = 'drift-wall__plane';
  root.appendChild(plane);

  const colPools = [];
  const colElements = [];
  const tracks = [];
  const itemHeight = tileHeight + gap;

  for (let c = 0; c < columns; c++) {
    const col = document.createElement('div');
    col.className = 'drift-wall__col';
    const pool = [];
    for (let i = 0; i < wallTiles.length; i++) {
      if ((i + c) % columns === 0 || pool.length < 3) {
        pool.push(wallTiles[(i * 3 + c * 2) % wallTiles.length]);
      }
    }
    colPools.push(pool);

    const track = document.createElement('div');
    track.className = 'drift-wall__track';
    col.appendChild(track);
    plane.appendChild(col);
    colElements.push(col);
    tracks.push(track);
  }

  container.innerHTML = '';
  container.appendChild(root);

  const colOffsets = new Array(columns).fill(0);
  const colSpeeds = [];
  for (let c = 0; c < columns; c++) {
    const mid = (columns - 1) / 2;
    const dist = Math.abs(c - mid) / (mid || 1);
    const mod = 1 - dist * variance;
    colSpeeds.push(speed * Math.max(mod, 0.45));
    colOffsets[c] = (c * itemHeight * 0.45) % (colPools[c].length * itemHeight);
  }

  const trackHeights = new Array(columns).fill(0);
  const activeTileEls = [];

  function fillTracks() {
    const rootH = root.clientHeight || 700;
    const renderH = rootH + itemHeight * 5;

    for (let c = 0; c < columns; c++) {
      const track = tracks[c];
      const pool = colPools[c];
      const curH = trackHeights[c];
      if (curH >= renderH) continue;

      const needed = Math.ceil((renderH - curH) / itemHeight) + 2;
      for (let k = 0; k < needed; k++) {
        const itemIdx = (Math.floor(curH / itemHeight) + k) % pool.length;
        const item = pool[itemIdx];

        const tile = document.createElement('div');
        tile.className = 'drift-wall__tile';
        tile.tabIndex = 0;
        tile.setAttribute('role', 'button');
        tile.setAttribute('aria-label', item.title);
        tile.dataset.jacket = item.jacket;

        const inner = document.createElement('span');
        inner.className = 'drift-wall__inner';

        const img = document.createElement('img');
        img.src = item.image;
        img.alt = item.title;
        img.draggable = false;
        img.loading = 'lazy';

        inner.appendChild(img);
        tile.appendChild(inner);
        track.appendChild(tile);
        activeTileEls.push(tile);
      }
      trackHeights[c] += needed * itemHeight;
    }
  }

  fillTracks();

  let pointer = { x: 0, y: 0 };
  let smoothPointer = { x: 0, y: 0 };
  let targetTilt = tilt;
  let targetTurn = turn;
  let curTilt = tilt;
  let curTurn = turn;
  let wallHovered = false;

  const updatePlaneTransform = () => {
    smoothPointer.x += (pointer.x - smoothPointer.x) * 0.08;
    smoothPointer.y += (pointer.y - smoothPointer.y) * 0.08;

    const mouseTurn = -smoothPointer.x * 6;
    const mouseTilt = smoothPointer.y * 5;

    curTilt += (targetTilt + mouseTilt - curTilt) * 0.08;
    curTurn += (targetTurn + mouseTurn - curTurn) * 0.08;

    plane.style.transform = `perspective(${perspective}px) translateZ(${depth}px) rotateX(${curTilt}deg) rotateY(${curTurn}deg) rotateZ(${roll}deg)`;
  };

  let lastTime = performance.now();

  let wallInView = true;
  let wallRafId = null;

  function animateWall(now) {
    const dt = Math.min((now - lastTime) / 1000, 0.1);
    lastTime = now;

    if (autoPlay && !isReducedMotion()) {
      for (let c = 0; c < columns; c++) {
        const poolH = colPools[c].length * itemHeight;
        const dist = colSpeeds[c] * dt;
        if (direction === 'up') {
          colOffsets[c] = (colOffsets[c] + dist) % poolH;
        } else {
          colOffsets[c] = (colOffsets[c] - dist + poolH) % poolH;
        }
        tracks[c].style.transform = `translate3d(0, ${-colOffsets[c]}px, 0)`;
      }
    }

    updatePlaneTransform();
  }

  function driftLoop(now) {
    if (!wallInView || document.hidden || isReducedMotion()) {
      wallRafId = null;
      return;
    }
    animateWall(now);
    wallRafId = requestAnimationFrame(driftLoop);
  }

  function startDriftLoop() {
    if (!wallRafId && wallInView && !document.hidden && !isReducedMotion()) {
      lastTime = performance.now();
      wallRafId = requestAnimationFrame(driftLoop);
    }
  }

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      wallInView = entries[0].isIntersecting;
      if (wallInView) {
        startDriftLoop();
      }
    }, { threshold: 0.05 });
    observer.observe(container);
  }

  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && wallInView) {
      startDriftLoop();
    }
  }, { passive: true });

  startDriftLoop();

  root.addEventListener('pointermove', (e) => {
    const rect = root.getBoundingClientRect();
    const nx = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    const ny = ((e.clientY - rect.top) / rect.height) * 2 - 1;
    pointer.x = Math.max(-1, Math.min(1, nx));
    pointer.y = Math.max(-1, Math.min(1, ny));
    wallHovered = true;
  });

  root.addEventListener('pointerleave', () => {
    wallHovered = false;
    pointer.x = 0;
    pointer.y = 0;
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
    onSelectJacket: (id) => selectJacket(id, { scroll: true, fromAccordion: true, userInitiated: true })
  });

  // Initialize Women's Accordion Carousel (3 jackets)
  window.accordionWomenAPI = createAccordionGallery({
    rootId: 'accordionGalleryWomen',
    items: womensJackets,
    defaultIndex: 1, // Desire
    onSelectJacket: (id) => selectJacket(id, { scroll: true, fromAccordion: true, userInitiated: true })
  });

  // Department switch button click listeners
  const tabMen = document.getElementById('tab-gender-men');
  const tabWomen = document.getElementById('tab-gender-women');

  if (tabMen) {
    tabMen.addEventListener('click', (e) => {
      e.preventDefault();
      switchDepartment('men', { syncJacket: true, scroll: false });
    });
  }

  if (tabWomen) {
    tabWomen.addEventListener('click', (e) => {
      e.preventDefault();
      switchDepartment('women', { syncJacket: true, scroll: false });
    });
  }

  // Pre-render the default active jacket (Men's Desire) in showcase
  const defaultJacket = mensJackets[2];
  renderShowcase(defaultJacket);

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

// Kick off when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
