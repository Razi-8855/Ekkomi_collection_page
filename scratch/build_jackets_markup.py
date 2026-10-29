import os

jackets = [
    {
        'id': 'curiosity',
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
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/curiosity/curiosity.jpg', 'alt': 'Dark Navy jacket — Curiosity Front Silhouette'},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/curiosity/curiosity_detail.jpg', 'alt': 'Dark Navy jacket — Curiosity Tone-on-Tone Embroidery Detail'},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/curiosity/curiosity_back.jpg', 'alt': 'Dark Navy jacket — Curiosity Back Construction'},
            {'label': 'Illustrated Lining', 'src': 'assets/collection/nocturne/curiosity/curiosity_lining.jpg', 'alt': 'Dark Navy jacket — Curiosity Illustrated Silk Lining'},
            {'label': 'Lookbook Portrait', 'src': 'assets/collection/nocturne/curiosity/curiosity_lookbook_1.jpg', 'alt': 'Dark Navy jacket — Curiosity Studio Portrait'},
            {'label': 'Lookbook Profile', 'src': 'assets/collection/nocturne/curiosity/curiosity_lookbook_2.jpg', 'alt': 'Dark Navy jacket — Curiosity Profile View'}
        ]
    },
    {
        'id': 'temptation',
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
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/temptation/temptation.jpg', 'alt': 'Forest Green jacket — Temptation Front Full Body'},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/temptation/temptation_detail.jpg', 'alt': 'Forest Green jacket — Temptation Lapel and Embroidery Detail'},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/temptation/temptation_back.jpg', 'alt': 'Forest Green jacket — Temptation Back Collar Embroidery'},
            {'label': 'Lookbook Seated', 'src': 'assets/collection/nocturne/temptation/temptation_lookbook_1.jpg', 'alt': 'Forest Green jacket — Temptation Seated Lookbook'},
            {'label': 'Lookbook Armchair', 'src': 'assets/collection/nocturne/temptation/temptation_lookbook_2.jpg', 'alt': 'Forest Green jacket — Temptation Armchair Editorial'}
        ]
    },
    {
        'id': 'desire',
        'number': '03',
        'impulse': 'Desire',
        'colour': 'Deep Red',
        'hex': '#662225',
        'headline': 'Wanting more is not always greed. Sometimes it is vision.',
        'narrative': 'Desire is the instinct that refuses to be satisfied by what is already there. It begins with recognition — of what could be, of what is missing, of what feels worth moving toward — and turns that recognition into intent. There is nothing passive about it. Rendered in deep red suede, the jacket carries that tension between restraint and appetite. Tone-on-tone embroidery moves through the surface in shifting fragments, revealing itself gradually as light catches the garment and then recedes again. Sensual without spectacle. Expressive without surrendering restraint.',
        'material': 'Deeply dyed suede gives the jacket its richness, structure and tactile presence.',
        'embroidery': 'Tone-on-tone embroidery is integrated into the surface of the garment, allowing pattern and texture to emerge gradually as the light changes.',
        'innerWorld': 'A richly illustrated lining sits in deliberate contrast to the controlled exterior. Because desire does not have to announce itself to be felt.',
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/desire/desire.jpg', 'alt': 'Deep Red jacket — Desire Front Seated Silhouette'},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/desire/desire_detail.jpg', 'alt': 'Deep Red jacket — Desire Back Tonal Embroidery Detail'},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/desire/desire_back.jpg', 'alt': 'Deep Red jacket — Desire Back Embroidery'},
            {'label': 'Illustrated Lining', 'src': 'assets/collection/nocturne/desire/desire_lining.jpg', 'alt': 'Deep Red jacket — Desire Illustrated Silk Lining'},
            {'label': 'Lookbook Standing', 'src': 'assets/collection/nocturne/desire/desire_lookbook_1.jpg', 'alt': 'Deep Red jacket — Desire Full Standing'},
            {'label': 'Lookbook Profile', 'src': 'assets/collection/nocturne/desire/desire_lookbook_2.jpg', 'alt': 'Deep Red jacket — Desire Side Angle'},
            {'label': 'Lookbook Lounge', 'src': 'assets/collection/nocturne/desire/desire_lookbook_3.jpg', 'alt': 'Deep Red jacket — Desire Lounge Chair'},
            {'label': 'Editorial Evening', 'src': 'assets/collection/nocturne/desire/desire_editorial_1.jpg', 'alt': 'Deep Red jacket — Desire Editorial Sofa'},
            {'label': 'Editorial Detail', 'src': 'assets/collection/nocturne/desire/desire_editorial_2.jpg', 'alt': 'Deep Red jacket — Desire Editorial Close-up'},
            {'label': 'Editorial Silhouette', 'src': 'assets/collection/nocturne/desire/desire_editorial_3.jpg', 'alt': 'Deep Red jacket — Desire Editorial Standing Portrait'}
        ]
    },
    {
        'id': 'audacity',
        'number': '04',
        'impulse': 'Audacity',
        'colour': 'Deep Mustard',
        'hex': '#8c6b24',
        'headline': 'Audacity is confidence before permission arrives.',
        'narrative': 'Audacity is the willingness to move before the world has decided you may. To take the unexpected route, occupy the space available to you — and occasionally the space that was not. The deep mustard suede refuses anonymity, while tonal embroidery tempers its boldness with intricacy and restraint. A piece that stands apart without turning difference into performance.',
        'material': 'Dyed suede gives the saturated mustard tone both richness and weight, balancing expressive colour with a structured silhouette.',
        'embroidery': 'Tone-on-tone embroidery adds complexity without competing with the strength of the colour, revealing itself through texture and light.',
        'innerWorld': 'The illustrated lining continues the jacket\'s confidence inward — a private flourish beneath the more controlled surface. Because audacity does not end where other people stop looking.',
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/audacity/audacity.jpg', 'alt': 'Deep Mustard jacket — Audacity Front View'},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/audacity/audacity_detail.jpg', 'alt': 'Deep Mustard jacket — Audacity Chest Embroidery Detail'},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/audacity/audacity_back.jpg', 'alt': 'Deep Mustard jacket — Audacity Back View'},
            {'label': 'Editorial Seated', 'src': 'assets/collection/nocturne/audacity/audacity_editorial_1.jpg', 'alt': 'Deep Mustard jacket — Audacity Seated Study'},
            {'label': 'Editorial Street', 'src': 'assets/collection/nocturne/audacity/audacity_editorial_2.jpg', 'alt': 'Deep Mustard jacket — Audacity Nocturne Street Scene'},
            {'label': 'Lookbook Styled', 'src': 'assets/collection/nocturne/audacity/audacity_lookbook_1.jpg', 'alt': 'Deep Mustard jacket — Audacity Styled with Scarf'},
            {'label': 'Lookbook Texture', 'src': 'assets/collection/nocturne/audacity/audacity_lookbook_2.jpg', 'alt': 'Deep Mustard jacket — Audacity Front Texture'}
        ]
    },
    {
        'id': 'insolence',
        'number': '05',
        'impulse': 'Insolence',
        'colour': 'Black',
        'hex': '#1a1716',
        'headline': 'Respect the rule. Question its right to rule you.',
        'narrative': 'Insolence begins with discernment. Not the rejection of convention for its own sake, but the confidence to decide which traditions deserve respect — and which have simply become habits of obedience. Rendered in black suede, near-concealed tonal embroidery turns restraint into something more subversive: detail that exists without demanding recognition. Refined, controlled and entirely capable of disobedience.',
        'material': 'Black dyed suede gives the jacket weight, texture and an understated depth that rewards proximity.',
        'embroidery': 'Dark tonal embroidery sits almost within the surface itself, becoming visible through shifts in light rather than contrast.',
        'innerWorld': 'The illustrated lining disrupts the restraint of the exterior with a world known most intimately by the wearer. Because what is hidden can still have character.',
        'views': [
            {'label': 'Front Silhouette', 'src': 'assets/collection/nocturne/insolence/insolence.jpg', 'alt': 'Black jacket — Insolence Front Silhouette'},
            {'label': 'Embroidery Detail', 'src': 'assets/collection/nocturne/insolence/insolence_detail.jpg', 'alt': 'Black jacket — Insolence Subversive Embroidery Detail'},
            {'label': 'Back Tailoring', 'src': 'assets/collection/nocturne/insolence/insolence_back.jpg', 'alt': 'Black jacket — Insolence Back Shoulder Seams'},
            {'label': 'Editorial Full', 'src': 'assets/collection/nocturne/insolence/insolence_editorial_1.jpg', 'alt': 'Black jacket — Insolence Standing Editorial'},
            {'label': 'Editorial Chair', 'src': 'assets/collection/nocturne/insolence/insolence_editorial_2.jpg', 'alt': 'Black jacket — Insolence Sculptural Chair Portrait'},
            {'label': 'Editorial Profile', 'src': 'assets/collection/nocturne/insolence/insolence_editorial_3.jpg', 'alt': 'Black jacket — Insolence Side Profile Study'},
            {'label': 'Editorial Close-up', 'src': 'assets/collection/nocturne/insolence/insolence_editorial_4.jpg', 'alt': 'Black jacket — Insolence Intimate Close-up'}
        ]
    }
]

def render_section(j):
    views = j['views']
    main_view = views[0]
    total_views = len(views)
    
    cards_html = []
    for i, v in enumerate(views):
        active_cls = ' is-active' if i == 0 else ''
        pressed_val = 'true' if i == 0 else 'false'
        idx_str = f"{i+1:02d}"
        cards_html.append(f'''              <button class="gallery-view-card{active_cls}"
                      type="button"
                      role="listitem"
                      aria-label="View {v['label']} for {j['impulse']} jacket"
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
         {j['number']} / {j['impulse'].upper()} PRODUCT DETAIL SECTION
         ============================================================ -->
    <section class="jacket-detail-section" id="jacket-{j['id']}" data-jacket="{j['id']}" aria-labelledby="title-{j['id']}">
      <div class="section jacket-detail-inner">

        <!-- Editorial Header: Split Meta & Narrative -->
        <div class="jacket-editorial-header">
          <div class="jacket-meta-column">
            <div class="jacket-collection-eyebrow">
              <span class="eyebrow-prefix">Nocturne</span>
              <span class="eyebrow-sep">/</span>
              <span class="eyebrow-num">{j['number']}</span>
            </div>
            <h2 class="jacket-name" id="title-{j['id']}">{j['impulse']}</h2>
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
            <h3 class="gallery-heading">Photographic Perspectives</h3>
            <span class="gallery-counter-tag">{total_views} Perspectives</span>
          </div>

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
            <div class="gallery-views-grid" role="list" aria-label="{j['impulse']} jacket photographic angles">
{cards_rendered}
            </div>
          </div>
        </div>

        <!-- Section Footer Navigation -->
        <div class="jacket-section-nav">
          <a class="nav-back-link" href="#accordionGallery" aria-label="Return to Nocturne collection overview">
            <span class="arrow-up" aria-hidden="true">&uarr;</span> Back to Nocturne Collection
          </a>
        </div>

      </div>
    </section>'''

all_sections = '\n\n'.join(render_section(j) for j in jackets)

full_block = f'''      <!-- ============================================================
           DEDICATED PRODUCT DETAILS & GALLERIES FOR ALL 5 JACKETS
           Each jacket has its own dedicated editorial section & gallery
           ============================================================ -->
      <div class="jackets-collection-details" id="jacketsDetails">
{all_sections}
      </div>'''

with open('scratch/jackets_sections.html', 'w', encoding='utf-8') as f:
    f.write(full_block)

print('Generated scratch/jackets_sections.html successfully! Length:', len(full_block))

