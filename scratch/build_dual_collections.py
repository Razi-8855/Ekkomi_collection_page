import os

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
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/curiosity/curiosity.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Front Silhouette"},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/curiosity/curiosity_detail.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Tone-on-Tone Embroidery Detail"},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/curiosity/curiosity_back.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Back Construction"},
            {'label': 'Illustrated Lining', 'src': 'assets/collection/nocturne/curiosity/curiosity_lining.jpg', 'alt': "Dark Navy jacket — Men's Curiosity Illustrated Silk Lining"},
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
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/temptation/temptation.jpg', 'alt': "Forest Green jacket — Men's Temptation Front Full Body"},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/temptation/temptation_detail.jpg', 'alt': "Forest Green jacket — Men's Temptation Lapel and Embroidery Detail"},
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
        # ALL MALE MODEL SHOTS FOR MEN'S AUDACITY (NO WOMEN)
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/audacity/audacity_lookbook_1.jpg', 'alt': "Deep Mustard jacket — Men's Audacity Styled with Scarf (Male Model)"},
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
        # ALL MALE MODEL SHOTS FOR MEN'S INSOLENCE (NO WOMEN)
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
        'note': "Women's editorial photography in production · Garment craft perspectives displayed",
        # PURE STILL GARMENT VIEWS (NO MALE MODEL)
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/curiosity/curiosity.jpg', 'alt': "Dark Navy jacket — Women's Curiosity Front Silhouette"},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/curiosity/curiosity_detail.jpg', 'alt': "Dark Navy jacket — Women's Curiosity Tone-on-Tone Embroidery Detail"},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/curiosity/curiosity_back.jpg', 'alt': "Dark Navy jacket — Women's Curiosity Back Construction"},
            {'label': 'Illustrated Lining', 'src': 'assets/collection/nocturne/curiosity/curiosity_lining.jpg', 'alt': "Dark Navy jacket — Women's Curiosity Illustrated Silk Lining"}
        ]
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
        # ALL GENUINE FEMALE MODEL PHOTOSHOOT SHOTS + CRAFT
        'views': [
            {'label': 'Standing Silhouette', 'src': 'assets/collection/nocturne/desire/desire_editorial_3.jpg', 'alt': "Deep Red jacket — Women's Desire Standing Portrait (Female Model)"},
            {'label': 'Back Embroidery', 'src': 'assets/collection/nocturne/desire/desire_back.jpg', 'alt': "Deep Red jacket — Women's Desire Back Embroidery Detail (Female Model)"},
            {'label': 'Evening Lounge', 'src': 'assets/collection/nocturne/desire/desire_editorial_1.jpg', 'alt': "Deep Red jacket — Women's Desire Editorial on Sofa (Female Model)"},
            {'label': 'Close Profile', 'src': 'assets/collection/nocturne/desire/desire_editorial_2.jpg', 'alt': "Deep Red jacket — Women's Desire Intimate Close-up (Female Model)"},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/desire/desire_detail.jpg', 'alt': "Deep Red jacket — Women's Desire Embroidery Macro"},
            {'label': 'Illustrated Lining', 'src': 'assets/collection/nocturne/desire/desire_lining.jpg', 'alt': "Deep Red jacket — Women's Desire Illustrated Silk Lining"}
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
        # ALL GENUINE FEMALE MODEL PHOTOSHOOT SHOTS + CRAFT
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/audacity/audacity.jpg', 'alt': "Deep Mustard jacket — Women's Audacity Front Leaning Silhouette (Female Model)"},
            {'label': 'Seated Portrait', 'src': 'assets/collection/nocturne/audacity/audacity_editorial_1.jpg', 'alt': "Deep Mustard jacket — Women's Audacity Seated Portrait (Female Model)"},
            {'label': 'Nocturne Scene', 'src': 'assets/collection/nocturne/audacity/audacity_editorial_2.jpg', 'alt': "Deep Mustard jacket — Women's Audacity with Street Lamp (Female Model)"},
            {'label': 'Chest Embroidery', 'src': 'assets/collection/nocturne/audacity/audacity_detail.jpg', 'alt': "Deep Mustard jacket — Women's Audacity Chest Embroidery"},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/audacity/audacity_back.jpg', 'alt': "Deep Mustard jacket — Women's Audacity Back Tailoring"}
        ]
    }
]

def render_jacket_section(j):
    views = j['views']
    main_view = views[0]
    total_views = len(views)
    is_women = j['gender'] == 'women'
    back_target = '#accordionGalleryWomen' if is_women else '#accordionGalleryMen'
    back_label = "Back to Women's Collection" if is_women else "Back to Men's Collection"
    note_html = ''
    if j.get('note'):
        note_html = f'''            <div class="gallery-production-note">
              <span class="note-dot"></span>
              <span>{j['note']}</span>
            </div>'''
    
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
            <span class="gallery-counter-tag">{total_views} Perspectives</span>
          </div>
{note_html}
          <div class="jacket-gallery-editorial">
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
          </div>
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

with open('scratch/dual_collection_markup.html', 'w', encoding='utf-8') as f:
    f.write(full_collection_block)

print('Generated updated scratch/dual_collection_markup.html successfully! Length:', len(full_collection_block))
