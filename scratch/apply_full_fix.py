import os
import re

# =====================================================================
# 1. DEFINE JACKETS DATA
# =====================================================================

mens_jackets = [
    {
        'id': 'men-curiosity',
        'key': 'curiosity',
        'gender': 'men',
        'collection_label': "Men's Collection",
        'number': '01',
        'impulse': 'Curiosity',
        'colour': 'Dark Navy',
        'hex': '#1c2838',
        'headline': 'They told you curiosity was dangerous. It is also how every new world is found.',
        'narrative': 'Curiosity refuses the comfort of the already known. It looks twice, asks another question, follows the detail others might pass by. Rendered in deep navy suede, intricate tone-on-tone embroidery rewards that same instinct — receding into the surface at first glance, then revealing more as light moves across it. A piece made for those who would rather discover than simply be shown.',
        'material': 'Dyed suede gives the jacket its depth, structure and tactile character.',
        'embroidery': 'Tone-on-tone embroidery moves quietly across the surface, designed to reward a closer look rather than reveal itself all at once.',
        'innerWorld': 'A richly illustrated lining creates an unexpected counterpoint to the restrained exterior. Because some things are better discovered than displayed.',
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/curiosity/curiosity.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Front Silhouette (Male Model)"},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/curiosity/curiosity_detail.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Tone-on-Tone Embroidery Detail (Male Model)"},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/curiosity/curiosity_back.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Back Construction (Male Model)"},
            {'label': 'Illustrated Lining', 'src': 'assets/collection/nocturne/curiosity/curiosity_lining.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Illustrated Silk Lining (Male Model)"},
            {'label': 'Lookbook Portrait', 'src': 'assets/collection/nocturne/curiosity/curiosity_lookbook_1.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Lookbook Studio Portrait (Male Model)"},
            {'label': 'Lookbook Profile', 'src': 'assets/collection/nocturne/curiosity/curiosity_lookbook_2.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Lookbook Profile View (Male Model)"}
        ]
    },
    {
        'id': 'men-temptation',
        'key': 'temptation',
        'gender': 'men',
        'collection_label': "Men's Collection",
        'number': '02',
        'impulse': 'Temptation',
        'colour': 'Forest Green',
        'hex': '#27382b',
        'headline': 'Not every temptation is a weakness. Sometimes it is recognition.',
        'narrative': 'Temptation begins with the awareness that something else is possible — a pull toward what lies just beyond the choices already made for us. In deep forest green suede, tone-on-tone embroidery moves between shadow and visibility, creating a surface that reveals itself gradually rather than giving everything away. A piece for the possibility that becomes increasingly difficult to ignore.',
        'material': 'Richly dyed suede gives the jacket its depth of colour, softness and structure.',
        'embroidery': 'Intricate tonal embroidery sits close to the colour of the leather, appearing and disappearing with movement and changing light.',
        'innerWorld': 'Inside, the illustrated lining offers a more expressive world than the exterior first suggests. Because restraint does not require the absence of temptation.',
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/temptation/temptation.jpg', 'alt': "Forest Green jacket — Men's Temptation Front Full Body (Male Model)"},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/temptation/temptation_detail.jpg', 'alt': "Forest Green jacket — Men's Temptation Lapel and Embroidery Detail (Male Model)"},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/temptation/temptation_back.jpg', 'alt': "Forest Green jacket — Men's Temptation Back Collar Embroidery"},
            {'label': 'Lookbook Seated', 'src': 'assets/collection/nocturne/temptation/temptation_lookbook_1.jpg', 'alt': "Forest Green jacket — Men's Temptation Seated Lookbook (Male Model)"},
            {'label': 'Lookbook Armchair', 'src': 'assets/collection/nocturne/temptation/temptation_lookbook_2.jpg', 'alt': "Forest Green jacket — Men's Temptation Armchair Editorial (Male Model)"}
        ]
    },
    {
        'id': 'men-desire',
        'key': 'desire',
        'gender': 'men',
        'collection_label': "Men's Collection",
        'number': '03',
        'impulse': 'Desire',
        'colour': 'Deep Red',
        'hex': '#662225',
        'headline': 'Wanting more is not always greed. Sometimes it is vision.',
        'narrative': 'Desire is the instinct that refuses to be satisfied by what is already there. It begins with recognition — of what could be, of what is missing, of what feels worth moving toward — and turns that recognition into intent. Rendered in deep red suede, the jacket carries that tension between restraint and appetite. Tone-on-tone embroidery moves through the surface in shifting fragments, revealing itself gradually as light catches the garment and then recedes again.',
        'material': 'Deeply dyed suede gives the jacket its richness, structure and tactile presence.',
        'embroidery': 'Tone-on-tone embroidery is integrated into the surface of the garment, allowing pattern and texture to emerge gradually as the light changes.',
        'innerWorld': 'A richly illustrated lining sits in deliberate contrast to the controlled exterior. Because desire does not have to announce itself to be felt.',
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/desire/desire.jpg', 'alt': "Deep Red jacket — Men's Desire Front Seated (Male Model)"},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/desire/desire_detail.jpg', 'alt': "Deep Red jacket — Men's Desire Back Tonal Embroidery (Male Model)"},
            {'label': 'Illustrated Lining', 'src': 'assets/collection/nocturne/desire/desire_lining.jpg', 'alt': "Deep Red jacket — Men's Desire Illustrated Silk Lining"},
            {'label': 'Lookbook Standing', 'src': 'assets/collection/nocturne/desire/desire_lookbook_1.jpg', 'alt': "Deep Red jacket — Men's Desire Full Standing (Male Model)"},
            {'label': 'Lookbook Profile', 'src': 'assets/collection/nocturne/desire/desire_lookbook_2.jpg', 'alt': "Deep Red jacket — Men's Desire Side Angle (Male Model)"},
            {'label': 'Lookbook Lounge', 'src': 'assets/collection/nocturne/desire/desire_lookbook_3.jpg', 'alt': "Deep Red jacket — Men's Desire Lounge Chair (Male Model)"}
        ]
    },
    {
        'id': 'men-audacity',
        'key': 'audacity',
        'gender': 'men',
        'collection_label': "Men's Collection",
        'number': '04',
        'impulse': 'Audacity',
        'colour': 'Deep Mustard',
        'hex': '#8c6b24',
        'headline': 'Audacity is confidence before permission arrives.',
        'narrative': 'Audacity is the willingness to move before the world has decided you may. To take the unexpected route, occupy the space available to you — and occasionally the space that was not. The deep mustard suede refuses anonymity, while tonal embroidery tempers its boldness with intricacy and restraint. A piece that stands apart without turning difference into performance.',
        'material': 'Dyed suede gives the saturated mustard tone both richness and weight, balancing expressive colour with a structured silhouette.',
        'embroidery': 'Tone-on-tone embroidery adds complexity without competing with the strength of the colour, revealing itself through texture and light.',
        'innerWorld': "The illustrated lining continues the jacket's confidence inward — a private flourish beneath the more controlled surface. Because audacity does not end where other people stop looking.",
        # 100% MALE MODEL PHOTOS FOR MEN'S AUDACITY (ZERO FEMALE)
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/audacity/audacity_lookbook_1.jpg', 'alt': "Deep Mustard jacket — Men's Audacity Styled with Scarf (Male Model BEN03893)"},
            {'label': 'Chest Embroidery', 'src': 'assets/collection/nocturne/audacity/audacity_lookbook_2.jpg', 'alt': "Deep Mustard jacket — Men's Audacity Front Texture (Male Model)"},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/audacity/audacity_detail.jpg', 'alt': "Deep Mustard jacket — Men's Audacity Chest Embroidery (Male Model)"},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/audacity/audacity_back.jpg', 'alt': "Deep Mustard jacket — Men's Audacity Back View (Male Model)"}
        ]
    },
    {
        'id': 'men-insolence',
        'key': 'insolence',
        'gender': 'men',
        'collection_label': "Men's Collection",
        'number': '05',
        'impulse': 'Insolence',
        'colour': 'Black',
        'hex': '#1a1716',
        'headline': 'Respect the rule. Question its right to rule you.',
        'narrative': 'Insolence begins with discernment. Not the rejection of convention for its own sake, but the confidence to decide which traditions deserve respect — and which have simply become habits of obedience. Rendered in black suede, near-concealed tonal embroidery turns restraint into something more subversive: detail that exists without demanding recognition. Refined, controlled and entirely capable of disobedience.',
        'material': 'Black dyed suede gives the jacket weight, texture and an understated depth that rewards proximity.',
        'embroidery': 'Dark tonal embroidery sits almost within the surface itself, becoming visible through shifts in light rather than contrast.',
        'innerWorld': 'The illustrated lining disrupts the restraint of the exterior with a world known most intimately by the wearer. Because what is hidden can still have character.',
        # 100% MALE MODEL PHOTOS FOR MEN'S INSOLENCE (ZERO FEMALE)
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/insolence/insolence.jpg', 'alt': "Black jacket — Men's Insolence Front Silhouette (Male Model Seated)"},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/insolence/insolence_detail.jpg', 'alt': "Black jacket — Men's Insolence Subversive Embroidery Detail (Male Model)"},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/insolence/insolence_back.jpg', 'alt': "Black jacket — Men's Insolence Back Shoulder Seams (Male Model)"}
        ]
    }
]

womens_jackets = [
    {
        'id': 'women-curiosity',
        'key': 'curiosity',
        'gender': 'women',
        'collection_label': "Women's Collection",
        'number': '01',
        'impulse': 'Curiosity',
        'colour': 'Dark Navy',
        'hex': '#1c2838',
        'headline': 'They told you curiosity was dangerous. It is also how every new world is found.',
        'narrative': 'Curiosity refuses the comfort of the already known. Reimagined for the women\'s silhouette in deep navy suede, tone-on-tone embroidery moves quietly across tailored lines — subtle, restrained, and rewarding a closer look. A piece made for those who would rather discover than simply be shown.',
        'material': 'Dyed navy suede selected for its softness, lightweight drape and refined structure.',
        'embroidery': 'Tone-on-tone embroidery contoured across the yoke and collar, catching the light with natural movement.',
        'innerWorld': 'A richly illustrated lining creates an unexpected counterpoint to the restrained exterior.',
        'is_pending': True,
        'pending_title': "Women's Curiosity Campaign Photography",
        'pending_desc': "Client photoshoot for the women's tailored Curiosity jacket in Dark Navy is currently scheduled. In accordance with brand curation standards, men's photoshoot imagery has been excluded from this section.",
        'required_shots': [
            '01 / Front Silhouette — Women’s Tailored Fit (Required)',
            '02 / Embroidery Detail — Collar & Yoke (Required)',
            '03 / Back Construction — Silhouette (Required)',
            '04 / Illustrated Silk Lining (Required)'
        ],
        'views': []
    },
    {
        'id': 'women-desire',
        'key': 'desire',
        'gender': 'women',
        'collection_label': "Women's Collection",
        'number': '02',
        'impulse': 'Desire',
        'colour': 'Deep Red',
        'hex': '#662225',
        'headline': 'Wanting more is not always greed. Sometimes it is vision.',
        'narrative': 'Desire is the instinct that refuses to be satisfied by what is already there. Rendered in deep red suede and cut with fluid feminine tailoring, the jacket carries that essential tension between restraint and appetite. Tonal embroidery shifts across the surface, catching the light with movement. Sensual without spectacle. Expressive without surrendering restraint.',
        'material': 'Deeply dyed suede provides richness, supple hand-feel and elegant architectural drape.',
        'embroidery': 'Tone-on-tone embroidery integrated across the back and shoulders, emerging gradually as light changes.',
        'innerWorld': 'A richly illustrated lining sits in deliberate contrast to the controlled exterior.',
        # 100% FEMALE MODEL PHOTOS (ZERO MALE — BEN03806 PURGED)
        'views': [
            {'label': 'Standing Silhouette', 'src': 'assets/collection/nocturne/desire/desire_editorial_3.jpg', 'alt': "Deep Red jacket — Women's Desire Standing Portrait (Female Model BEN04159)"},
            {'label': 'Back Embroidery', 'src': 'assets/collection/nocturne/desire/desire_back.jpg', 'alt': "Deep Red jacket — Women's Desire Back Embroidery Detail (Female Model BEN04180)"},
            {'label': 'Evening Lounge', 'src': 'assets/collection/nocturne/desire/desire_editorial_1.jpg', 'alt': "Deep Red jacket — Women's Desire Editorial on Sofa (Female Model BEN04137)"},
            {'label': 'Close Profile', 'src': 'assets/collection/nocturne/desire/desire_editorial_2.jpg', 'alt': "Deep Red jacket — Women's Desire Intimate Close-up (Female Model BEN04149)"}
        ]
    },
    {
        'id': 'women-audacity',
        'key': 'audacity',
        'gender': 'women',
        'collection_label': "Women's Collection",
        'number': '03',
        'impulse': 'Audacity',
        'colour': 'Deep Mustard',
        'hex': '#8c6b24',
        'headline': 'Audacity is confidence before permission arrives.',
        'narrative': 'Audacity is the willingness to move before the world has decided you may. The deep mustard suede refuses anonymity, while tonal embroidery tempers its boldness with intricate restraint. Tailored for feminine form, the silhouette stands apart with quiet authority rather than performance.',
        'material': 'Dyed mustard suede balancing saturated warmth with a supple, sculptural silhouette.',
        'embroidery': 'Tonal embroidery contours the upper bodice, revealing intricate texture without competing with the colour.',
        'innerWorld': "The illustrated lining continues the jacket's confidence inward — a private flourish beneath the controlled surface.",
        # 100% FEMALE MODEL PHOTOS FOR WOMEN'S AUDACITY (ZERO MALE)
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/audacity/audacity.jpg', 'alt': "Deep Mustard jacket — Women's Audacity Front Leaning Silhouette (Female Model BEN04068)"},
            {'label': 'Seated Portrait', 'src': 'assets/collection/nocturne/audacity/audacity_editorial_1.jpg', 'alt': "Deep Mustard jacket — Women's Audacity Seated Portrait (Female Model BEN04058)"},
            {'label': 'Nocturne Scene', 'src': 'assets/collection/nocturne/audacity/audacity_editorial_2.jpg', 'alt': "Deep Mustard jacket — Women's Audacity with Street Lamp (Female Model BEN04099)"}
        ]
    }
]

def render_jacket_section(j):
    views = j.get('views', [])
    is_women = j['gender'] == 'women'
    back_target = '#accordionGalleryWomen' if is_women else '#accordionGalleryMen'
    back_label = "Back to Women's Collection" if is_women else "Back to Men's Collection"
    
    if j.get('is_pending'):
        req_list_html = ''.join(f'<span>&bull; {req}</span>\n                  ' for req in j['required_shots'])
        gallery_inner_html = f'''          <div class="gallery-production-note">
            <span class="note-dot"></span>
            <span>Production Notice: Photography in Production</span>
          </div>

          <div class="jacket-gallery-editorial">
            <!-- Large Editorial Placeholder Stage -->
            <div class="gallery-stage gallery-stage--placeholder" id="stage-{j['id']}">
              <div class="gallery-stage__placeholder">
                <img class="stage-placeholder__icon" src="assets/collection/nocturne/curiosity/curiosity_women_preview.svg" alt="Dark Navy jacket — Women's Tailored Cut" width="220" height="293" />
                <span class="stage-placeholder__tag">Photography In Production</span>
                <h4 class="stage-placeholder__title">{j['impulse']} · Women&#8217;s Cut</h4>
                <p class="stage-placeholder__desc">{j['pending_desc']}</p>
                <div class="stage-placeholder__requirements">
                  <strong>Required Deliverables:</strong>
                  {req_list_html}
                </div>
              </div>
            </div>

            <!-- Placeholder Cards for Missing Perspectives -->
            <div class="gallery-views-grid" role="list" aria-label="{j['collection_label']} {j['impulse']} pending assets">
              <div class="gallery-view-card gallery-view-card--placeholder" role="listitem">
                <div class="view-card__frame view-card__frame--placeholder">
                  <img class="view-card__placeholder-icon" src="assets/collection/nocturne/curiosity/curiosity_women_preview.svg" alt="" width="52" height="69" />
                  <span class="view-card__placeholder-tag">01 · Front View</span>
                </div>
                <div class="view-card__info"><span class="view-card__index">01</span><span class="view-card__label">Female Front Cut</span></div>
              </div>

              <div class="gallery-view-card gallery-view-card--placeholder" role="listitem">
                <div class="view-card__frame view-card__frame--placeholder">
                  <img class="view-card__placeholder-icon" src="assets/collection/nocturne/curiosity/curiosity_women_preview.svg" alt="" width="52" height="69" />
                  <span class="view-card__placeholder-tag">02 · Embroidery</span>
                </div>
                <div class="view-card__info"><span class="view-card__index">02</span><span class="view-card__label">Embroidery Detail</span></div>
              </div>

              <div class="gallery-view-card gallery-view-card--placeholder" role="listitem">
                <div class="view-card__frame view-card__frame--placeholder">
                  <img class="view-card__placeholder-icon" src="assets/collection/nocturne/curiosity/curiosity_women_preview.svg" alt="" width="52" height="69" />
                  <span class="view-card__placeholder-tag">03 · Back Cut</span>
                </div>
                <div class="view-card__info"><span class="view-card__index">03</span><span class="view-card__label">Back Tailoring</span></div>
              </div>

              <div class="gallery-view-card gallery-view-card--placeholder" role="listitem">
                <div class="view-card__frame view-card__frame--placeholder">
                  <img class="view-card__placeholder-icon" src="assets/collection/nocturne/curiosity/curiosity_women_preview.svg" alt="" width="52" height="69" />
                  <span class="view-card__placeholder-tag">04 · Lining</span>
                </div>
                <div class="view-card__info"><span class="view-card__index">04</span><span class="view-card__label">Silk Inner Lining</span></div>
              </div>
            </div>
          </div>'''
        total_views_str = "4 Deliverables Pending"
    else:
        main_view = views[0]
        total_views_str = f"{len(views)} Perspectives"
        cards_html = []
        for i, v in enumerate(views):
            active_cls = ' is-active' if i == 0 else ''
            pressed_val = 'true' if i == 0 else 'false'
            idx_str = f"{i+1:02d}"
            cards_html.append(f'''              <button class="gallery-view-card{active_cls}"
                      type="button"
                      role="listitem"
                      aria-label="View {v['label']} for {j['collection_label']} {j['impulse']} jacket"
                      aria-pressed="{pressed_val}"
                      data-jacket-id="{j['id']}"
                      data-view-index="{i}"
                      data-src="{v['src']}"
                      data-alt="{v['alt']}"
                      data-label="{v['label']}">
                <div class="view-card__frame">
                  <img class="view-card__img"
                       src="{v['src']}"
                       alt="{v['alt']}"
                       loading="lazy"
                       width="400"
                       height="600" />
                  <span class="view-card__overlay" aria-hidden="true"></span>
                </div>
                <div class="view-card__info">
                  <span class="view-card__index">{idx_str}</span>
                  <span class="view-card__label">{v['label']}</span>
                </div>
              </button>''')
        cards_rendered = '\n'.join(cards_html)
        gallery_inner_html = f'''          <div class="jacket-gallery-editorial">
            <!-- Prominent Main Stage (Large, 2:3 ratio) -->
            <div class="gallery-stage" id="stage-{j['id']}">
              <div class="gallery-stage__frame">
                <img class="gallery-stage__img"
                     id="stage-img-{j['id']}"
                     src="{main_view['src']}"
                     alt="{main_view['alt']}"
                     loading="lazy"
                     width="1200"
                     height="1800" />
                <div class="gallery-stage__badge">
                  <span class="badge-indicator" aria-hidden="true"></span>
                  <span class="stage-caption" id="stage-caption-{j['id']}">{main_view['label']}</span>
                </div>
              </div>
            </div>

            <!-- Additional Views Grid -->
            <div class="gallery-views-grid" role="list" aria-label="{j['collection_label']} {j['impulse']} jacket views">
{cards_rendered}
            </div>
          </div>'''

    return f'''    <!-- ============================================================
         {j['collection_label'].upper()} — {j['number']} / {j['impulse'].upper()}
         ============================================================ -->
    <section class="jacket-detail-section" id="jacket-{j['id']}" data-jacket="{j['id']}" data-gender="{j['gender']}" data-key="{j['key']}" aria-labelledby="title-{j['id']}">
      <div class="section jacket-detail-inner">

        <!-- Editorial Header: Split Meta & Narrative -->
        <div class="jacket-editorial-header">
          <div class="jacket-meta-column">
            <div class="jacket-collection-eyebrow">
              <span class="eyebrow-prefix">{j['collection_label']}</span>
              <span class="eyebrow-sep">/</span>
              <span class="eyebrow-num">{j['number']}</span>
            </div>
            <h3 class="jacket-name" id="title-{j['id']}">{j['impulse']}</h3>
            <div class="jacket-colour-tag">
              <span class="colour-swatch" style="background-color: {j['hex']};" aria-hidden="true"></span>
              <span class="colour-name">{j['colour']}</span>
            </div>
          </div>

          <div class="jacket-story-column">
            <p class="jacket-headline">{j['headline']}</p>
            <p class="jacket-narrative">{j['narrative']}</p>

            <dl class="jacket-craft-list">
              <div class="craft-item">
                <dt>The Material</dt>
                <dd>{j['material']}</dd>
              </div>
              <div class="craft-item">
                <dt>The Embroidery</dt>
                <dd>{j['embroidery']}</dd>
              </div>
              <div class="craft-item">
                <dt>The Inner World</dt>
                <dd>{j['innerWorld']}</dd>
              </div>
            </dl>
          </div>
        </div>

        <!-- Luxury Product Gallery -->
        <div class="jacket-gallery-container" data-gallery-jacket="{j['id']}">
          <div class="gallery-section-bar">
            <h4 class="gallery-heading">Photographic Perspectives</h4>
            <span class="gallery-counter-tag">{total_views_str}</span>
          </div>
{gallery_inner_html}
        </div>

        <!-- Section Footer Navigation -->
        <div class="jacket-section-nav">
          <a class="nav-back-link" href="{back_target}" aria-label="Return to {j['collection_label']} overview">
            <span class="arrow-up" aria-hidden="true">&uarr;</span> {back_label}
          </a>
        </div>

      </div>
    </section>'''

mens_rendered = '\n\n'.join(render_jacket_section(j) for j in mens_jackets)
womens_rendered = '\n\n'.join(render_jacket_section(j) for j in womens_jackets)

full_collection_block = f'''    <!-- ============================================================
         NOCTURNE COLLECTION: DUAL EDIT (MEN'S & WOMEN'S)
         ============================================================ -->
    <section class="collection-showcase-section" id="collection" role="region" aria-label="Nocturne collection">
      
      <!-- Top Department Switcher Bar -->
      <div class="collection-nav-bar" id="collectionNavBar">
        <div class="section">
          <div class="collection-gender-switch" role="tablist" aria-label="Nocturne collection departments">
            <button class="gender-switch-btn is-active" id="tab-gender-men" type="button" role="tab" aria-selected="true" data-gender-target="mens-department">
              <span class="gender-label">Men&#8217;s Collection</span>
              <span class="gender-badge">05 Styles</span>
            </button>
            <span class="gender-switch-divider" aria-hidden="true">/</span>
            <button class="gender-switch-btn" id="tab-gender-women" type="button" role="tab" aria-selected="false" data-gender-target="womens-department">
              <span class="gender-label">Women&#8217;s Collection</span>
              <span class="gender-badge">03 Styles</span>
            </button>
          </div>
        </div>
      </div>

      <!-- ============================================================
           1. MEN'S COLLECTION
           Five expressions of instinct
           ============================================================ -->
      <div class="collection-department-block" id="mens-department">
        
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

        <!-- Men's Dedicated Product Detail Sections -->
        <div class="jackets-collection-details" id="mensDetails">
{mens_rendered}
        </div>

      </div>

      <!-- Refined Luxury Divider between Departments -->
      <div class="department-separator" aria-hidden="true">
        <span class="separator-line"></span>
        <span class="separator-emblem">&bull;</span>
        <span class="separator-line"></span>
      </div>

      <!-- ============================================================
           2. WOMEN'S COLLECTION
           Three expressions of instinct
           ============================================================ -->
      <div class="collection-department-block" id="womens-department">
        
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

        <!-- Women's Dedicated Product Detail Sections -->
        <div class="jackets-collection-details" id="womensDetails">
{womens_rendered}
        </div>

      </div>

    </section>'''

# =====================================================================
# 2. UPDATE INDEX.HTML
# =====================================================================

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_m = re.search(r'<!--\s*=+\s*NOCTURNE COLLECTION: DUAL EDIT', html)
if not start_m:
    raise Exception("Could not find start marker in index.html")

start_pos = start_m.start()
end_m = re.search(r'</section>\s*(?=\s*</main>)', html)
if not end_m:
    raise Exception("Could not find end marker in index.html")

end_pos = end_m.end()

new_html = html[:start_pos] + full_collection_block + html[end_pos:]

# Update cachebuster on styles and app.js
new_html = re.sub(r'styles\.css\?v=[^\"]+', 'styles.css?v=zero_leak_2', new_html)
new_html = re.sub(r'app\.js\?v=[^\"]+', 'app.js?v=zero_leak_2', new_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("index.html updated successfully!")

# =====================================================================
# 3. UPDATE STYLES.CSS
# =====================================================================

placeholder_css = """
/* ===================================================================
   PRODUCTION PENDING & EDITORIAL PLACEHOLDER (LUXURY CURATION)
   =================================================================== */

.gallery-stage--placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 50% 40%, rgba(28, 40, 56, 0.45) 0%, rgba(10, 14, 20, 0.85) 100%), #0c1219;
  border: 1px solid rgba(184, 155, 114, 0.22);
  border-radius: var(--radius-lg);
  padding: clamp(32px, 5vw, 64px) clamp(24px, 4vw, 48px);
  min-height: 480px;
  text-align: center;
  box-shadow: inset 0 0 60px rgba(0, 0, 0, 0.5);
}

.gallery-stage__placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 540px;
  margin: 0 auto;
}

.stage-placeholder__icon {
  width: clamp(140px, 20vw, 200px);
  height: auto;
  margin-bottom: 24px;
  filter: drop-shadow(0 14px 28px rgba(0, 0, 0, 0.6));
  border-radius: var(--radius-md);
  transition: transform 0.4s var(--ease-out);
}

.stage-placeholder__icon:hover {
  transform: translateY(-4px) scale(1.02);
}

.stage-placeholder__tag {
  display: inline-block;
  font-family: var(--font-sans);
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--color-gold);
  padding: 5px 14px;
  border: 1px solid rgba(184, 155, 114, 0.35);
  border-radius: 999px;
  background: rgba(184, 155, 114, 0.08);
  margin-bottom: 16px;
}

.stage-placeholder__title {
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 2.8vw, 2.2rem);
  font-weight: 300;
  color: var(--color-cream);
  letter-spacing: 0.06em;
  margin: 0 0 12px;
  line-height: 1.2;
}

.stage-placeholder__desc {
  font-family: var(--font-serif);
  font-size: clamp(0.9375rem, 1.2vw, 1.0625rem);
  line-height: 1.6;
  color: rgba(250, 246, 241, 0.72);
  margin: 0 0 24px;
}

.stage-placeholder__requirements {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
  padding: 18px 22px;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(184, 155, 114, 0.15);
  border-radius: var(--radius-md);
  text-align: left;
}

.stage-placeholder__requirements strong {
  font-family: var(--font-sans);
  font-size: 0.6875rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--color-gold);
  margin-bottom: 4px;
}

.stage-placeholder__requirements span {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  color: rgba(250, 246, 241, 0.65);
  letter-spacing: 0.05em;
}

/* Placeholder Cards in View Grid */
.gallery-view-card--placeholder {
  cursor: default;
  opacity: 0.75;
}

.gallery-view-card--placeholder:hover {
  opacity: 0.95;
  transform: none;
}

.view-card__frame--placeholder {
  position: relative;
  aspect-ratio: 2 / 3;
  width: 100%;
  background: radial-gradient(circle at 50% 40%, rgba(28, 40, 56, 0.5) 0%, rgba(10, 14, 20, 0.9) 100%);
  border: 1px dashed rgba(184, 155, 114, 0.3);
  border-radius: var(--radius-md);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 12px;
  gap: 8px;
  overflow: hidden;
}

.view-card__placeholder-icon {
  width: 52px;
  height: auto;
  opacity: 0.85;
}

.view-card__placeholder-tag {
  font-family: var(--font-sans);
  font-size: 0.625rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--color-gold);
  text-align: center;
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.gallery-stage--placeholder' not in css:
    css = css + '\n' + placeholder_css
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("styles.css updated with placeholder CSS!")
else:
    print("styles.css already contains placeholder CSS.")

# =====================================================================
# 4. UPDATE APP.JS DATA
# =====================================================================

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Replace mensJackets and womensJackets definition in app.js
mens_jackets_code = """const mensJackets = [
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
    // 100% Male model standing with scarf (BEN03893)
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
    // 100% Male model seated (BEN03324)
    image: imgPath('insolence', 'insolence.jpg'),
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
   WOMEN'S COLLECTION DATA (3 JACKETS — 100% FEMALE / CURATED PENDING)
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
    // Ultra-luxury editorial silhouette preview (ZERO male photography)
    image: 'assets/collection/nocturne/curiosity/curiosity_women_preview.svg',
    label: '01 / CURIOSITY',
    sublabel: 'DARK NAVY · WOMEN',
    isPending: true,
    views: []
  },
  {
    id: 'women-desire',
    key: 'desire',
    gender: 'women',
    number: '02',
    impulse: 'Desire',
    colour: 'Deep Red',
    hex: '#662225',
    // 100% Female model standing portrait (BEN04159)
    image: imgPath('desire', 'desire_editorial_3.jpg'),
    label: '02 / DESIRE',
    sublabel: 'DEEP RED · WOMEN',
    views: [
      { label: 'Standing Silhouette', src: imgPath('desire', 'desire_editorial_3.jpg'), alt: "Deep Red jacket — Women's Desire Standing Portrait (Female Model BEN04159)" },
      { label: 'Back Embroidery', src: imgPath('desire', 'desire_back.jpg'), alt: "Deep Red jacket — Women's Desire Back Embroidery Detail (Female Model BEN04180)" },
      { label: 'Evening Lounge', src: imgPath('desire', 'desire_editorial_1.jpg'), alt: "Deep Red jacket — Women's Desire Editorial on Sofa (Female Model BEN04137)" },
      { label: 'Close Profile', src: imgPath('desire', 'desire_editorial_2.jpg'), alt: "Deep Red jacket — Women's Desire Intimate Close-up (Female Model BEN04149)" },
      { label: 'Illustrated Lining', src: imgPath('desire', 'desire_lining.jpg'), alt: "Deep Red jacket — Women's Desire Illustrated Silk Lining (Garment Detail BEN03806)" }
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
    // 100% Female model leaning on counter (BEN04068)
    image: imgPath('audacity', 'audacity.jpg'),
    label: '03 / AUDACITY',
    sublabel: 'MUSTARD · WOMEN',
    views: [
      { label: 'Front Silhouette', src: imgPath('audacity', 'audacity.jpg'), alt: "Deep Mustard jacket — Women's Audacity Front Leaning Silhouette (Female Model BEN04068)" },
      { label: 'Seated Portrait', src: imgPath('audacity', 'audacity_editorial_1.jpg'), alt: "Deep Mustard jacket — Women's Audacity Seated Portrait (Female Model BEN04058)" },
      { label: 'Nocturne Scene', src: imgPath('audacity', 'audacity_editorial_2.jpg'), alt: "Deep Mustard jacket — Women's Audacity with Street Lamp (Female Model BEN04099)" }
    ]
  }
];"""

app_js_pattern = re.compile(r'const mensJackets = \[.*?\];\s*const womensJackets = \[.*?\];', re.DOTALL)
if not app_js_pattern.search(app_js):
    raise Exception("Could not find mensJackets / womensJackets block in app.js")

app_js = app_js_pattern.sub(mens_jackets_code, app_js)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("app.js updated successfully!")

