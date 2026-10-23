# EKOMMI — NOCTURNE COLLECTION PAGE
## Complete Implementation, Design & UX Plan

---

# 1. PROJECT CONTEXT

Project: Ekkomi Luxury Fashion Website

Current page being developed:

NOCTURNE — COLLECTION PAGE

The Ekkomi website is planned to contain:

- Story
- Collection
- Craft
- Journal

IMPORTANT:

The Story page is NOT currently available in the project.

Do not assume that a completed Story page exists.

Do not build or recreate the Story page as part of this task.

The current priority is ONLY the Collection page.

The Collection page should be developed in a way that can later integrate naturally with the rest of the Ekkomi website.

---

# 2. CURRENT DEVELOPMENT STATUS

The Collection page is currently in the architecture and design phase.

The client has NOT yet provided:

- Final jacket/product images
- Final jacket photography
- Final embroidery images
- Final lining images
- Final construction details
- Final product URLs
- Final colour palette
- Final typography/font system

Therefore, temporary/sample assets are required during development.

These temporary assets are NOT final brand assets.

The implementation must make it extremely easy to replace:

Temporary image → Final product image

Temporary font → Final Ekkomi font

Temporary colour → Final Ekkomi colour

Temporary copy → Final approved copy

Temporary product URL → Final product URL

The page architecture should NOT need to be rebuilt when the final client assets arrive.

---

# 3. COLLECTION NAME

# NOCTURNE

Nocturne is the first collection from the house of Ekkomi.

The collection explores five impulses that people are traditionally taught to keep in check:

- Curiosity
- Temptation
- Desire
- Audacity
- Insolence

The collection consists of five richly coloured suede jackets.

Each jacket represents one impulse.

---

# 4. COLLECTION CONCEPT

Use the following approved collection narrative:

"The first collection from the house of Ekkomi, Nocturne reconsiders five impulses we have long been taught to keep in check.

Curiosity. Temptation. Desire. Audacity. Insolence.

We are warned against wanting too much, asking too much, straying too far, taking up too much space. Yet these same instincts are often what make us singular.

Curiosity leads us beyond what we know. Temptation reveals possibilities we had not allowed ourselves to consider. Desire gives direction to ambition. Audacity makes room where none was offered. Insolence questions rules that have outlived their purpose.

In a world increasingly inclined toward sameness — where taste is predicted, behaviour is performed and individuality can become another carefully managed aesthetic — Nocturne makes a case for the unruly parts of the self.

Not every instinct needs correcting.

Some deserve following.

Across five richly coloured suede jackets, intricate tone-on-tone embroidery moves between concealment and revelation — receding into the surface, then emerging as light catches it.

Each piece gives form to one of these impulses, transforming an old caution into a contemporary expression of individuality.

Five pieces. Five impulses. Five qualities worth reconsidering."

---

# 5. OVERALL PAGE STRUCTURE

The Collection page should follow this hierarchy:

COLLECTION PAGE

│
├── Collection Introduction
│
│   ├── Eyebrow
│   ├── NOCTURNE title
│   ├── Short narrative
│   └── Five impulse navigation
│
├── Main Jacket Showcase
│
│   ├── Large jacket image
│   ├── Impulse
│   ├── Jacket colour
│   ├── Headline
│   ├── Narrative
│   ├── Material
│   ├── Embroidery
│   ├── Inner World
│   ├── Construction
│   └── View Product CTA
│
└── Other Jackets
    │
    └── Horizontal jacket selector/carousel

---

# 6. COLLECTION INTRO SECTION

The first section should introduce Nocturne as an editorial fashion collection.

Use:

Eyebrow:

THE FIRST COLLECTION

Main title:

NOCTURNE

Short introductory statement:

"Five impulses. Five jackets. A collection that reconsiders what we've been taught to keep in check."

Then display the five impulses:

CURIOSITY

TEMPTATION

DESIRE

AUDACITY

INSOLENCE

These should function as interactive controls.

They should NOT be purely decorative.

Clicking an impulse should select the corresponding jacket.

---

# 7. DEFAULT SELECTED JACKET

The default selected jacket must be:

DESIRE

Colour:

DEEP RED

This means that when the Collection page initially loads, the main showcase should display the Desire jacket.

The default selection should be controlled through data/state.

Do NOT hardcode "Desire" in multiple unrelated components.

Conceptually:

selectedJacket = "desire"

---

# 8. THE FIVE NOCTURNE JACKETS

The five products are:

1. Curiosity — Dark Navy
2. Temptation — Forest Green
3. Desire — Deep Red
4. Audacity — Deep Mustard
5. Insolence — Black

Each jacket should be represented as a data object.

---

# 9. DATA-DRIVEN ARCHITECTURE

Product content must be separated from UI.

Create one central collection data structure.

Conceptually:

collectionData = [

  {
    id: "curiosity",
    impulse: "Curiosity",
    colour: "Dark Navy",
    image: "...",
    headline: "...",
    narrative: "...",
    material: "...",
    embroidery: "...",
    innerWorld: "...",
    construction: "...",
    productLink: "..."
  },

  {
    id: "temptation",
    impulse: "Temptation",
    colour: "Forest Green",
    ...
  },

  {
    id: "desire",
    impulse: "Desire",
    colour: "Deep Red",
    ...
  },

  {
    id: "audacity",
    impulse: "Audacity",
    colour: "Deep Mustard",
    ...
  },

  {
    id: "insolence",
    impulse: "Insolence",
    colour: "Black",
    ...
  }

]

The exact implementation should follow the existing project's technology and coding conventions.

---

# 10. SINGLE SELECTED-JACKET STATE

The page should use ONE central selected-jacket state.

Conceptually:

selectedJacket

This state controls:

- Main jacket image
- Impulse
- Colour
- Headline
- Narrative
- Material
- Embroidery
- Inner World
- Construction
- Product URL
- Active jacket in carousel
- Active impulse

The architecture should be:

collectionData
        ↓
selectedJacket
        ↓
Main Showcase
        +
Impulse Navigation
        +
Other Jackets Carousel

There should NOT be separate independent selection states for each section.

---

# 11. MAIN JACKET SHOWCASE

The main showcase is the most important section of the page.

It should use ONE reusable showcase component.

Do NOT create five separate showcase layouts.

Conceptually:

JacketShowcase(selectedJacket)

The showcase should contain:

- Large jacket image
- Impulse
- Colour
- Editorial headline
- Narrative
- Material
- Embroidery
- Inner World
- Construction
- View Product CTA

---

# 12. MAIN SHOWCASE LAYOUT

Desktop direction:

┌──────────────────────────┬──────────────────────────┐
│                          │ IMPULSE                  │
│                          │                          │
│                          │ COLOUR                   │
│                          │                          │
│       LARGE JACKET       │ HEADLINE                 │
│          IMAGE           │                          │
│                          │ NARRATIVE                │
│                          │                          │
│                          │ MATERIAL                 │
│                          │ EMBROIDERY               │
│                          │ INNER WORLD              │
│                          │ CONSTRUCTION             │
│                          │                          │
│                          │ VIEW PRODUCT →           │
└──────────────────────────┴──────────────────────────┘

The jacket image should be visually dominant.

The text should remain editorial and refined.

---

# 13. JACKET NAVIGATION

Provide navigation controls around the showcase where appropriate.

Possible controls:

Previous jacket

Next jacket

The controls should update selectedJacket.

They should NOT cause a page reload.

The active jacket should remain synchronized across:

- Impulse navigation
- Main showcase
- Other Jackets carousel

---

# 14. CURIOSITY CONTENT

Impulse:

CURIOSITY

Colour:

DARK NAVY

Headline:

"They told you curiosity was dangerous. It is also how every new world is found."

Narrative:

"Curiosity refuses the comfort of the already known. It looks twice, asks another question, follows the detail others might pass by.

Rendered in deep navy suede, intricate tone-on-tone embroidery rewards that same instinct — receding into the surface at first glance, then revealing more as light moves across it.

A piece made for those who would rather discover than simply be shown."

Material:

"Dyed suede gives the jacket its depth, structure and tactile character."

Embroidery:

"Tone-on-tone embroidery moves quietly across the surface, designed to reward a closer look rather than reveal itself all at once."

Inner World:

"A richly illustrated lining creates an unexpected counterpoint to the restrained exterior.

Because some things are better discovered than displayed."

Construction:

"Construction details to be added after production sample approval."

---

# 15. TEMPTATION CONTENT

Impulse:

TEMPTATION

Colour:

FOREST GREEN

Headline:

"Not every temptation is a weakness. Sometimes it is recognition."

Narrative:

"Temptation begins with the awareness that something else is possible — a pull toward what lies just beyond the choices already made for us.

In deep forest green suede, tone-on-tone embroidery moves between shadow and visibility, creating a surface that reveals itself gradually rather than giving everything away.

A piece for the possibility that becomes increasingly difficult to ignore."

Material:

"Richly dyed suede gives the jacket its depth of colour, softness and structure."

Embroidery:

"Intricate tonal embroidery sits close to the colour of the leather, appearing and disappearing with movement and changing light."

Inner World:

"Inside, the illustrated lining offers a more expressive world than the exterior first suggests.

Because restraint does not require the absence of temptation."

Construction:

"Construction details to be added after production sample approval."

---

# 16. DESIRE CONTENT

Impulse:

DESIRE

Colour:

DEEP RED

Headline:

"Wanting more is not always greed. Sometimes it is vision."

Narrative:

"Desire is the instinct that refuses to be satisfied by what is already there. It begins with recognition - of what could be, of what is missing, of what feels worth moving toward - and turns that recognition into intent. There is nothing passive about it.

Rendered in deep red suede, the jacket carries that tension between restraint and appetite. Tone-on-tone embroidery moves through the surface in shifting fragments, revealing itself gradually as light catches the garment and then receding again.

Sensual without spectacle. Expressive without surrendering restraint."

Material:

"Deeply dyed suede gives the jacket its richness, structure and tactile presence."

Embroidery:

"Tone-on-tone embroidery is integrated into the surface of the garment, allowing pattern and texture to emerge gradually as the light changes."

Inner World:

"A richly illustrated lining sits in deliberate contrast to the controlled exterior.

Because desire does not have to announce itself to be felt."

Construction:

"Construction details to be added after production sample approval."

---

# 17. AUDACITY CONTENT

Impulse:

AUDACITY

Colour:

DEEP MUSTARD

Headline:

"Audacity is confidence before permission arrives."

Narrative:

"Audacity is the willingness to move before the world has decided you may. To take the unexpected route, occupy the space available to you — and occasionally the space that was not.

The deep mustard suede refuses anonymity, while tonal embroidery tempers its boldness with intricacy and restraint.

A piece that stands apart without turning difference into performance."

Material:

"Dyed suede gives the saturated mustard tone both richness and weight, balancing expressive colour with a structured silhouette."

Embroidery:

"Tone-on-tone embroidery adds complexity without competing with the strength of the colour, revealing itself through texture and light."

Inner World:

"The illustrated lining continues the jacket's confidence inward — a private flourish beneath the more controlled surface.

Because audacity does not end where other people stop looking."

Construction:

"Construction details to be added after production sample approval."

---

# 18. INSOLENCE CONTENT

Impulse:

INSOLENCE

Colour:

BLACK

Headline:

"Respect the rule. Question its right to rule you."

Narrative:

"Insolence begins with discernment. Not the rejection of convention for its own sake, but the confidence to decide which traditions deserve respect — and which have simply become habits of obedience.

Rendered in black suede, near-concealed tonal embroidery turns restraint into something more subversive: detail that exists without demanding recognition.

Refined, controlled and entirely capable of disobedience."

Material:

"Black dyed suede gives the jacket weight, texture and an understated depth that rewards proximity."

Embroidery:

"Dark tonal embroidery sits almost within the surface itself, becoming visible through shifts in light rather than contrast."

Inner World:

"The illustrated lining disrupts the restraint of the exterior with a world known most intimately by the wearer.

Because what is hidden can still have character."

Construction:

"Construction details to be added after production sample approval."

---

# 19. VIEW PRODUCT CTA

CTA:

VIEW PRODUCT →

The CTA should be stored as part of the jacket data.

Example:

productLink

Do not hardcode product links into the UI.

Final product pages may not exist yet.

Until they exist, use a safe placeholder route or non-destructive placeholder behaviour.

Do not invent real URLs.

---

# 20. OTHER JACKETS SECTION

After the main showcase, create:

OTHER JACKETS

Supporting copy:

"Five impulses. Five expressions."

This section should provide a horizontal visual selector for all five jackets.

Each item should contain:

- Jacket image
- Impulse
- Colour

The selected jacket should be visually emphasized.

Possible active treatment:

- subtle underline
- slight scale increase
- stronger opacity
- slightly stronger typography

Do not over-design the active state.

---

# 21. OTHER JACKETS CAROUSEL

Desktop:

Display multiple jacket cards horizontally.

Tablet:

Reduce visible cards appropriately.

Mobile:

Use horizontal swipe interaction.

The selected jacket should remain visible.

Clicking a card must update:

selectedJacket

This automatically updates the main showcase.

---

# 22. RESPONSIVE DESIGN

The page must be designed for:

- Desktop
- Tablet
- Mobile

Do not simply shrink the desktop layout.

The hierarchy should be intentionally adapted.

---

# 23. DESKTOP EXPERIENCE

Desktop should prioritize:

- Large editorial composition
- Large jacket image
- Strong typography
- Generous whitespace
- Two-column showcase
- Horizontal jacket selector

The product should feel like an editorial fashion presentation rather than a standard product grid.

---

# 24. TABLET EXPERIENCE

Tablet should maintain the same visual hierarchy while adapting:

- image size
- text width
- spacing
- navigation
- carousel visibility

Avoid cramped layouts.

---

# 25. MOBILE EXPERIENCE

Mobile should use a vertical sequence:

IMPULSE

↓

JACKET IMAGE

↓

COLOUR

↓

HEADLINE

↓

NARRATIVE

↓

MATERIAL

↓

EMBROIDERY

↓

INNER WORLD

↓

CONSTRUCTION

↓

VIEW PRODUCT

↓

OTHER JACKETS

The jacket selector should support horizontal touch/swipe interaction.

There must be no unwanted horizontal page overflow.

---

# 26. TEMPORARY IMAGES

Because final jacket assets are not ready, use temporary/sample jacket images.

Preferred characteristics:

- Transparent background
- Front-facing jacket
- Consistent proportions
- Consistent framing
- Neutral presentation
- High quality
- Similar visual treatment across all five products

Do NOT pretend these are the final Ekkomi jackets.

Do NOT invent final embroidery artwork.

---

# 27. ASSET STRUCTURE

Keep collection assets organized.

Preferred conceptual structure:

assets/

collection/

nocturne/

curiosity/

temptation/

desire/

audacity/

insolence/

The actual directory can follow the existing project's conventions.

The important requirement is:

Product assets should be easy to locate and replace.

---

# 28. TEMPORARY DESIGN SYSTEM

The final Ekkomi colour palette has not been provided.

Use a restrained temporary palette.

Suggested direction:

Background:

Warm ivory / off-white

Primary text:

Near black

Secondary text:

Muted neutral

Borders:

Very subtle neutral

Accent:

Minimal

Avoid bright or overly decorative colours.

---

# 29. CENTRALIZED COLOURS

Do not scatter hardcoded colours throughout the project.

Use centralized design tokens/variables.

Conceptually:

--color-background
--color-surface
--color-text
--color-text-muted
--color-border
--color-accent

When the client provides the final palette, these values should be easy to change globally.

---

# 30. TEMPORARY TYPOGRAPHY

The final Ekkomi typography has not been provided.

Use:

Display:

Elegant editorial serif

Body/UI:

Clean modern sans-serif

Centralize the font definitions.

Conceptually:

--font-display
--font-body

Do not hardcode different fonts throughout individual components.

When the final Ekkomi fonts arrive, changing the variables should update the page.

---

# 31. VISUAL LANGUAGE

The page should feel:

- Luxury
- Editorial
- Minimal
- Atmospheric
- Sophisticated
- Contemporary
- Restrained
- Confident
- Slightly rebellious

Use:

- Generous whitespace
- Elegant typography
- Large imagery
- Thin dividers
- Subtle transitions
- Precise alignment
- Strong visual hierarchy

---

# 32. AVOID

Do NOT use:

- Generic e-commerce card layouts
- Excessive rounded corners
- Heavy drop shadows
- Neon colours
- Excessive gradients
- Large glowing effects
- Excessive badges
- Fake reviews
- Fake ratings
- Fake prices
- Fake product specifications
- Fake availability
- Unnecessary UI elements
- SaaS/dashboard styling

The website should feel like a fashion house.

---

# 33. ANIMATION DIRECTION

Use subtle, intentional animation.

When changing jackets:

- Product image transitions smoothly
- Text transitions smoothly
- Active state transitions smoothly

The animation should feel:

- Slow enough to feel premium
- Fast enough to remain responsive

Avoid:

- Flashy transitions
- Excessive parallax
- Large bouncing animations
- Overly complex effects
- Distracting motion

Respect:

prefers-reduced-motion

---

# 34. ACCESSIBILITY

Implement:

- Semantic HTML
- Correct heading hierarchy
- Descriptive image alt text
- Accessible buttons
- Keyboard-accessible controls
- Visible focus states
- Adequate contrast
- Touch-friendly controls
- Reduced-motion support

Carousel controls should be accessible.

---

# 35. PERFORMANCE

Prepare the page for future high-resolution fashion imagery.

Use:

- Optimized images
- Responsive image sizing
- Lazy loading where appropriate
- Efficient rendering
- Minimal dependencies

Do not add large libraries simply to implement basic carousel/state functionality if the existing project can handle it without them.

---

# 36. COMPONENT ARCHITECTURE

Recommended conceptual structure:

CollectionPage

├── CollectionIntro
│   └── ImpulseNavigation
│
├── JacketShowcase
│   ├── JacketVisual
│   ├── JacketNavigation
│   ├── JacketInformation
│   ├── JacketDetails
│   └── ProductCTA
│
└── OtherJackets
    └── JacketCarousel
        └── JacketCard

The exact implementation should follow the existing project architecture.

Do not force a framework structure that does not match the existing codebase.

---

# 37. IMPORTANT ARCHITECTURAL PRINCIPLE

Do NOT build:

Curiosity Showcase

Temptation Showcase

Desire Showcase

Audacity Showcase

Insolence Showcase

as five separate page implementations.

Instead build:

ONE reusable JacketShowcase

powered by:

ONE collectionData structure

and:

ONE selectedJacket state.

This is one of the most important requirements of the project.

---

# 38. PAGE INTERACTION FLOW

The intended experience is:

Visitor enters Collection page

↓

NOCTURNE introduction appears

↓

Five impulses are presented

↓

DESIRE is selected by default

↓

Deep Red jacket appears in main showcase

↓

Visitor reads the Desire story

↓

Visitor clicks another impulse

↓

Selected jacket changes

↓

Main image changes

↓

Product information changes

↓

Active carousel item changes

↓

Visitor can continue exploring

↓

Visitor clicks VIEW PRODUCT

↓

Selected jacket's product destination is used

---

# 39. STATE SYNCHRONIZATION

There should be one source of truth.

Example:

collectionData
        ↓
selectedJacket
        ↓
┌─────────────────────────────┐
│                             │
│ Main Showcase               │
│ Impulse Navigation          │
│ Other Jackets Carousel      │
│ Product CTA                 │
│                             │
└─────────────────────────────┘

Changing selectedJacket must update every relevant UI element.

---

# 40. FUTURE REPLACEMENT SYSTEM

When the client sends the final assets, the following should be replaceable independently:

1. Jacket images
2. Embroidery imagery
3. Lining imagery
4. Final copy
5. Construction information
6. Product links
7. Brand fonts
8. Brand colours
9. Final logo assets

The page architecture should not need to be rebuilt.

---

# 41. IMPLEMENTATION PHASES

## PHASE 1 — PROJECT INSPECTION

Before coding:

- Inspect existing repository
- Inspect index.html
- Inspect existing files
- Identify framework
- Identify routing
- Identify CSS/styling architecture
- Identify reusable components
- Identify current assets
- Identify existing navigation
- Identify existing animations

Do not modify unrelated code.

---

## PHASE 2 — ARCHITECTURE

Implement:

- Collection data
- Five jacket objects
- selectedJacket state
- Default Desire selection
- Reusable showcase
- Reusable jacket card
- Impulse navigation
- Central design tokens
- Central asset references

---

## PHASE 3 — COLLECTION INTRO

Implement:

- THE FIRST COLLECTION
- NOCTURNE
- Intro narrative
- Five impulse navigation items

---

## PHASE 4 — MAIN SHOWCASE

Implement:

- Large jacket image
- Impulse
- Colour
- Headline
- Narrative
- Material
- Embroidery
- Inner World
- Construction
- View Product CTA

---

## PHASE 5 — INTERACTION

Implement:

- Impulse selection
- Jacket selection
- Previous/next navigation
- Dynamic content
- Dynamic image
- Dynamic product link
- Active states

No page reload.

---

## PHASE 6 — OTHER JACKETS

Implement:

- Horizontal carousel
- Jacket cards
- Active selection
- Click interaction
- Mobile swipe interaction

---

## PHASE 7 — RESPONSIVE

Test:

- Desktop
- Tablet
- Mobile

Fix:

- Overflow
- Spacing
- Typography
- Image sizing
- Carousel behaviour
- Touch interaction

---

## PHASE 8 — MOTION

Add:

- Image transitions
- Text transitions
- Active-state transitions

Keep motion subtle.

---

## PHASE 9 — VISUAL REFINEMENT

Refine:

- Typography
- Spacing
- Alignment
- Image scale
- Section rhythm
- CTA
- Carousel
- Navigation
- Responsive presentation

---

## PHASE 10 — QA

Verify:

Architecture:

- Product data is separated from UI
- One reusable showcase exists
- selectedJacket is centralized
- Five jackets are represented consistently

Functionality:

- Curiosity works
- Temptation works
- Desire works
- Audacity works
- Insolence works
- Main showcase updates
- Carousel updates
- Active state synchronizes
- CTA updates

Responsive:

- Desktop works
- Tablet works
- Mobile works
- No horizontal overflow

Accessibility:

- Semantic headings
- Alt text
- Keyboard controls
- Focus states
- Reduced motion

Performance:

- No unnecessary dependencies
- Images handled appropriately
- No obvious console/runtime errors

---

# 42. DO NOT MODIFY UNRELATED PROJECT AREAS

The current task is the Nocturne Collection page.

Do NOT unnecessarily modify:

- Story
- Craft
- Journal
- unrelated homepage sections
- unrelated components
- unrelated assets
- unrelated animations
- existing navigation unless necessary for Collection integration

Preserve existing functionality.

---

# 43. EXISTING PROJECT FIRST

Before implementation, inspect the existing project.

The current project location is:

C:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/

The main existing file is currently:

index.html

The implementation must work with the existing project rather than replacing it with an unrelated new architecture.

If the existing project is a static HTML/CSS/JavaScript implementation, continue using that architecture unless there is a strong technical reason not to.

If the project uses another framework, follow its existing conventions.

---

# 44. IMPORTANT — DO NOT ASSUME FINAL BRAND ASSETS

The current visual system is temporary.

Do not make temporary choices difficult to replace.

All temporary:

- colours
- fonts
- images
- copy
- URLs

should be centralized wherever practical.

---

# 45. FINAL DESIGN GOAL

The Collection page should feel like entering the world of Nocturne.

It should NOT feel like:

"Here are five products."

It should feel like:

"Here are five impulses, each given form through a jacket."

The visitor should be encouraged to explore.

The product should remain important, but the editorial story should give the product meaning.

---

# 46. FINAL SUCCESS CRITERIA

The Collection page is considered successful when:

### EXPERIENCE

- It feels like a luxury fashion editorial.
- The collection has a clear identity.
- The five impulses are immediately understandable.
- The visitor can explore all five jackets naturally.

### ARCHITECTURE

- Data is separated from UI.
- One reusable showcase handles all five jackets.
- One selected-jacket state controls the page.
- Assets can easily be replaced.
- Fonts can easily be replaced.
- Colours can easily be replaced.

### INTERACTION

- Impulse navigation works.
- Jacket selector works.
- Main showcase updates.
- Product CTA updates.
- Transitions feel polished.

### RESPONSIVENESS

- Desktop is polished.
- Tablet is polished.
- Mobile is polished.
- No unwanted horizontal overflow.

### FUTURE-PROOFING

When the client sends final assets, the developer should primarily need to replace:

- Images
- Fonts
- Colours
- Copy
- Product links
- Construction details

The core Collection page architecture should remain intact.

---

# 47. IMPLEMENTATION RULE

DO NOT immediately rewrite the existing website.

First inspect.

Then understand.

Then propose architecture.

Then implement.

Then test.

Then refine.

Preserve the existing Ekkomi work wherever possible.

The priority is:

Existing project
→ clean architecture
→ data-driven collection
→ working interactions
→ responsive layout
→ luxury visual refinement
→ easy future replacement of client assets.
