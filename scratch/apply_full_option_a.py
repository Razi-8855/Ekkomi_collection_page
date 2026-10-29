import json, re

# 1. Load editorial data
with open('scratch/jackets_editorial_data.json', 'r', encoding='utf-8') as f:
    editorial = json.load(f)

# 2. Build the complete new app.js
app_js_content = '''\'use strict\';

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
    id: 'men-curiosity',
    key: 'curiosity',
    gender: 'men',
    number: '01',
    impulse: 'Curiosity',
    colour: 'Dark Navy',
    hex: '#1c2838',
    image: imgPath('curiosity', 'curiosity.jpg'),
    label: '01 / CURIOSITY',
    sublabel: 'DARK NAVY',
    headline: "They told you curiosity was dangerous. It is also how every new world is found.",
    narrative: "Curiosity refuses the comfort of the already known. It looks twice, asks another question, follows the detail others might pass by. Rendered in deep navy suede, intricate tone-on-tone embroidery rewards that same instinct — receding into the surface at first glance, then revealing more as light moves across it. A piece made for those who would rather discover than simply be shown.",
    craft: [
      { title: "The Material", desc: "Dyed suede gives the jacket its depth, structure and tactile character." },
      { title: "The Embroidery", desc: "Tone-on-tone embroidery moves quietly across the surface, designed to reward a closer look rather than reveal itself all at once." },
      { title: "The Inner World", desc: "A richly illustrated lining creates an unexpected counterpoint to the restrained exterior. Because some things are better discovered than displayed." }
    ],
    views: [
      { label: 'Front Silhouette', src: imgPath('curiosity', 'curiosity.jpg'), alt: "Dark Navy jacket — Men's Curiosity Front Silhouette (Male Model)" },
      { label: 'Embroidery Detail', src: imgPath('curiosity', 'curiosity_detail.jpg'), alt: "Dark Navy jacket — Men's Curiosity Tone-on-Tone Embroidery Detail (Male Model)" },
      { label: 'Back Tailoring', src: imgPath('curiosity', 'curiosity_back.jpg'), alt: "Dark Navy jacket — Men's Curiosity Back Construction (Male Model)" },
      { label: 'Illustrated Lining', src: imgPath('curiosity', 'curiosity_lining.jpg'), alt: "Dark Navy jacket — Men's Curiosity Illustrated Silk Lining (Male Model)" },
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
    image: imgPath('temptation', 'temptation.jpg'),
    label: '02 / TEMPTATION',
    sublabel: 'FOREST GREEN',
    headline: "Not every temptation is a weakness. Sometimes it is recognition.",
    narrative: "Temptation begins with the awareness that something else is possible — a pull toward what lies just beyond the choices already made for us. In deep forest green suede, tone-on-tone embroidery moves between shadow and visibility, creating a surface that reveals itself gradually rather than giving everything away. A piece for the possibility that becomes increasingly difficult to ignore.",
    craft: [
      { title: "The Material", desc: "Richly dyed suede gives the jacket its depth of colour, softness and structure." },
      { title: "The Embroidery", desc: "Intricate tonal embroidery sits close to the colour of the leather, appearing and disappearing with movement and changing light." },
      { title: "The Inner World", desc: "Inside, the illustrated lining offers a more expressive world than the exterior first suggests. Because restraint does not require the absence of temptation." }
    ],
    views: [
      { label: 'Front Silhouette', src: imgPath('temptation', 'temptation.jpg'), alt: "Forest Green jacket — Men's Temptation Front Full Body (Male Model)" },
      { label: 'Embroidery Detail', src: imgPath('temptation', 'temptation_detail.jpg'), alt: "Forest Green jacket — Men's Temptation Lapel and Embroidery Detail (Male Model)" },
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
    image: imgPath('desire', 'desire.jpg'),
    label: '03 / DESIRE',
    sublabel: 'DEEP RED',
    headline: "Wanting more is not always greed. Sometimes it is vision.",
    narrative: "Desire is the instinct that refuses to be satisfied by what is already there. It begins with recognition — of what could be, of what is missing, of what feels worth moving toward — and turns that recognition into intent. Rendered in deep red suede, the jacket carries that tension between restraint and appetite. Tone-on-tone embroidery moves through the surface in shifting fragments, revealing itself gradually as light catches the garment and then recedes again.",
    craft: [
      { title: "The Material", desc: "Deeply dyed suede gives the jacket its richness, structure and tactile presence." },
      { title: "The Embroidery", desc: "Tone-on-tone embroidery is integrated into the surface of the garment, allowing pattern and texture to emerge gradually as the light changes." },
      { title: "The Inner World", desc: "A richly illustrated lining sits in deliberate contrast to the controlled exterior. Because desire does not have to announce itself to be felt." }
    ],
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
    image: imgPath('audacity', 'audacity_lookbook_1.jpg'),
    label: '04 / AUDACITY',
    sublabel: 'DEEP MUSTARD',
    headline: "Audacity is confidence before permission arrives.",
    narrative: "Audacity is the willingness to move before the world has decided you may. To take the unexpected route, occupy the space available to you — and occasionally the space that was not. The deep mustard suede refuses anonymity, while tonal embroidery tempers its boldness with intricacy and restraint. A piece that stands apart without turning difference into performance.",
    craft: [
      { title: "The Material", desc: "Dyed suede gives the saturated mustard tone both richness and weight, balancing expressive colour with a structured silhouette." },
      { title: "The Embroidery", desc: "Tone-on-tone embroidery adds complexity without competing with the strength of the colour, revealing itself through texture and light." },
      { title: "The Inner World", desc: "The illustrated lining continues the jacket's confidence inward — a private flourish beneath the more controlled surface. Because audacity does not end where other people stop looking." }
    ],
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
    image: imgPath('insolence', 'insolence.jpg'),
    label: '05 / INSOLENCE',
    sublabel: 'BLACK',
    headline: "Respect the rule. Question its right to rule you.",
    narrative: "Insolence begins with discernment. Not the rejection of convention for its own sake, but the confidence to decide which traditions deserve respect — and which have simply become habits of obedience. Rendered in black suede, near-concealed tonal embroidery turns restraint into something more subversive: detail that exists without demanding recognition. Refined, controlled and entirely capable of disobedience.",
    craft: [
      { title: "The Material", desc: "Black dyed suede gives the jacket weight, texture and an understated depth that rewards proximity." },
      { title: "The Embroidery", desc: "Dark tonal embroidery sits almost within the surface itself, becoming visible through shifts in light rather than contrast." },
      { title: "The Inner World", desc: "The illustrated lining disrupts the restraint of the exterior with a world known most intimately by the wearer. Because what is hidden can still have character." }
    ],
    views: [
      { label: 'Front Silhouette', src: imgPath('insolence', 'insolence.jpg'), alt: "Black jacket — Men's Insolence Front Silhouette (Male Model Seated)" },
      { label: 'Embroidery Detail', src: imgPath('insolence', 'insolence_detail.jpg'), alt: "Black jacket — Men's Insolence Subversive Embroidery Detail (Male Model)" },
      { label: 'Back Tailoring', src: imgPath('insolence', 'insolence_back.jpg'), alt: "Black jacket — Men's Insolence Back Shoulder Seams (Male Model)" }
    ]
  }
];

/* -------------------------------------------------------------------
   WOMEN'S COLLECTION DATA (3 JACKETS — 100% FEMALE PHOTOGRAPHY)
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
    image: imgPath('curiosity', 'curiosity_women_1.jpg'),
    label: '01 / CURIOSITY',
    sublabel: 'DARK NAVY · WOMEN',
    headline: "They told you curiosity was dangerous. It is also how every new world is found.",
    narrative: "Curiosity refuses the comfort of the already known. Reimagined for the women's silhouette in deep navy suede, intricate tone-on-tone embroidery moves quietly across tailored lines — subtle, restrained, and rewarding a closer look. A piece made for those who would rather discover than simply be shown.",
    craft: [
      { title: "The Material", desc: "Dyed navy suede selected for its softness, lightweight drape and refined structure." },
      { title: "The Embroidery", desc: "Tone-on-tone diamond and floral embroidery contoured across the yoke and collar, catching the light with natural movement." },
      { title: "The Inner World", desc: "A richly illustrated lining creates an unexpected counterpoint to the restrained exterior. Because some things are better discovered than displayed." }
    ],
    views: [
      { label: 'Standing Silhouette', src: imgPath('curiosity', 'curiosity_women_1.jpg'), alt: "Dark Navy jacket — Women's Curiosity Standing Silhouette (Female Model)" },
      { label: 'Embroidery Detail', src: imgPath('curiosity', 'curiosity_women_2.jpg'), alt: "Dark Navy jacket — Women's Curiosity Tone-on-Tone Embroidery Portrait (Female Model)" },
      { label: 'Back Tailoring', src: imgPath('curiosity', 'curiosity_women_3.jpg'), alt: "Dark Navy jacket — Women's Curiosity EKKOMI Back Collar Embroidery (Female Model)" },
      { label: 'Studio Profile', src: imgPath('curiosity', 'curiosity_women_4.jpg'), alt: "Dark Navy jacket — Women's Curiosity Studio Profile on Chair (Female Model)" },
      { label: 'Editorial Seated', src: imgPath('curiosity', 'curiosity_women_5.jpg'), alt: "Dark Navy jacket — Women's Curiosity Studio Editorial (Female Model)" }
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
    sublabel: 'DEEP RED · WOMEN',
    headline: "Wanting more is not always greed. Sometimes it is vision.",
    narrative: "Desire is the instinct that refuses to be satisfied by what is already there. Rendered in deep red suede and cut with fluid feminine tailoring, the jacket carries that essential tension between restraint and appetite. Tonal embroidery shifts across the surface, catching the light with movement. Sensual without spectacle. Expressive without surrendering restraint.",
    craft: [
      { title: "The Material", desc: "Deeply dyed suede provides richness, supple hand-feel and elegant architectural drape." },
      { title: "The Embroidery", desc: "Tone-on-tone embroidery integrated across the back and shoulders, emerging gradually as light changes." },
      { title: "The Inner World", desc: "A richly illustrated lining sits in deliberate contrast to the controlled exterior." }
    ],
    views: [
      { label: 'Standing Silhouette', src: imgPath('desire', 'desire_editorial_3.jpg'), alt: "Deep Red jacket — Women's Desire Standing Portrait (Female Model BEN04159)" },
      { label: 'Back Embroidery', src: imgPath('desire', 'desire_back.jpg'), alt: "Deep Red jacket — Women's Desire Back Embroidery Detail (Female Model BEN04180)" },
      { label: 'Evening Lounge', src: imgPath('desire', 'desire_editorial_1.jpg'), alt: "Deep Red jacket — Women's Desire Editorial on Sofa (Female Model BEN04137)" },
      { label: 'Close Profile', src: imgPath('desire', 'desire_editorial_2.jpg'), alt: "Deep Red jacket — Women's Desire Intimate Close-up (Female Model BEN04149)" }
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
    image: imgPath('audacity', 'audacity.jpg'),
    label: '03 / AUDACITY',
    sublabel: 'MUSTARD · WOMEN',
    headline: "Audacity is confidence before permission arrives.",
    narrative: "Audacity is the willingness to move before the world has decided you may. The deep mustard suede refuses anonymity, while tonal embroidery tempers its boldness with intricate restraint. Tailored for feminine form, the silhouette stands apart with quiet authority rather than performance.",
    craft: [
      { title: "The Material", desc: "Dyed mustard suede balancing saturated warmth with a supple, sculptural silhouette." },
      { title: "The Embroidery", desc: "Tonal embroidery contours the upper bodice, revealing intricate texture without competing with the colour." },
      { title: "The Inner World", desc: "The illustrated lining continues the jacket's confidence inward — a private flourish beneath the controlled surface." }
    ],
    views: [
      { label: 'Front Silhouette', src: imgPath('audacity', 'audacity.jpg'), alt: "Deep Mustard jacket — Women's Audacity Front Leaning Silhouette (Female Model BEN04068)" },
      { label: 'Seated Portrait', src: imgPath('audacity', 'audacity_editorial_1.jpg'), alt: "Deep Mustard jacket — Women's Audacity Seated Portrait (Female Model BEN04058)" },
      { label: 'Nocturne Scene', src: imgPath('audacity', 'audacity_editorial_2.jpg'), alt: "Deep Mustard jacket — Women's Audacity with Street Lamp (Female Model BEN04099)" }
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
        <!-- Editorial Header: Split Meta & Narrative -->
        <div class="jacket-editorial-header">
          <div class="jacket-meta-column">
            <div class="jacket-collection-eyebrow">
              <span class="eyebrow-prefix">${departmentTitle}</span>
              <span class="eyebrow-sep">/</span>
              <span class="eyebrow-num">${jacket.number}</span>
            </div>
            <h3 class="jacket-name" id="showcaseJacketTitle">${jacket.impulse}</h3>
            <div class="jacket-colour-tag">
              <span class="colour-swatch" style="background-color: ${jacket.hex};" aria-hidden="true"></span>
              <span class="colour-name">${jacket.colour}</span>
            </div>
          </div>

          <div class="jacket-story-column">
            <p class="jacket-headline">${jacket.headline}</p>
            <p class="jacket-narrative">${jacket.narrative}</p>

            <dl class="jacket-craft-list">
              ${craftHtml}
            </dl>
          </div>
        </div>

        <!-- Luxury Product Gallery -->
        <div class="jacket-gallery-container" data-gallery-jacket="${jacket.id}">
          <div class="gallery-section-bar">
            <h4 class="gallery-heading">Photographic Perspectives</h4>
            <span class="gallery-counter-tag">${jacket.views.length} Perspectives</span>
          </div>
          <div class="jacket-gallery-editorial">
            <!-- Prominent Main Stage (Large, 2:3 ratio) -->
            <div class="gallery-stage" id="showcaseStage">
              <div class="gallery-stage__frame">
                <img class="gallery-stage__img"
                     id="showcaseStageImg"
                     src="${firstView.src}"
                     alt="${firstView.alt}"
                     loading="eager"
                     width="1200"
                     height="1800" />
                <div class="gallery-stage__badge">
                  <span class="badge-indicator" aria-hidden="true"></span>
                  <span class="stage-caption" id="showcaseStageCaption">${firstView.label}</span>
                </div>
              </div>
            </div>

            <!-- Additional Views Grid -->
            <div class="gallery-views-grid" role="list" aria-label="${departmentTitle} ${jacket.impulse} jacket views">
              ${viewsHtml}
            </div>
          </div>
        </div>

        <!-- Understated Product Navigation (Previous / Next & Carousel Return) -->
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
      </div>
    `;

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

    // Bind Previous / Next Navigation
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
    }

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

function selectJacket(id, { scroll = false, fromAccordion = false, fromDepartmentSwitch = false } = {}) {
  const item = allCollectionJackets.find(j => j.id === id);
  if (!item) return;

  if (item.gender !== activeDepartment) {
    switchDepartment(item.gender, { syncJacket: false });
  }

  selectedJacketId = id;
  window.currentSelectedJacket = item;
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
  { image: 'jackets_original/resized_BEN03893.webp', title: 'Audacity · Deep Mustard with Scarf', jacket: 'men-audacity' },
  { image: 'jackets_original/resized_BEN03307.webp', title: 'Insolence · Black Suede (Men)', jacket: 'men-insolence' },
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
    requestAnimationFrame(animateWall);
  }

  requestAnimationFrame(animateWall);

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
    onSelectJacket: (id) => selectJacket(id, { scroll: true, fromAccordion: true })
  });

  // Initialize Women's Accordion Carousel (3 jackets)
  window.accordionWomenAPI = createAccordionGallery({
    rootId: 'accordionGalleryWomen',
    items: womensJackets,
    defaultIndex: 1, // Desire
    onSelectJacket: (id) => selectJacket(id, { scroll: true, fromAccordion: true })
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
'''

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js_content)

print("Updated app.js successfully, size:", len(app_js_content))

