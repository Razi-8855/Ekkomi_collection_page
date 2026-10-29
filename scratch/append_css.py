css_addition = """

/* Accordion Gallery Showcase Section */
.accordion-section {
  position: relative;
  z-index: 10;
  padding: 80px 5vw 100px;
  background: #0a0a08;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.accordion-section__header {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 48px;
}

.accordion-section__title {
  font-family: "Cormorant Garamond", serif;
  font-size: clamp(32px, 4.5vw, 56px);
  font-weight: 400;
  letter-spacing: 0.12em;
  color: #eee9df;
  margin: 8px 0 14px;
}

.accordion-section__sub {
  font-size: 13px;
  color: #aaa39a;
  letter-spacing: 0.06em;
  font-weight: 300;
}

.accordion-section__wrapper {
  max-width: 1400px;
  margin: 0 auto;
}
"""

with open(r'F:\ekkomi-carousel\src\App.css', 'a', encoding='utf-8') as f:
    f.write(css_addition)

print("Appended accordion styles to F:\\ekkomi-carousel\\src\\App.css")
