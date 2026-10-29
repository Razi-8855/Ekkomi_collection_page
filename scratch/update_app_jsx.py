app_jsx = """import DriftWall from "./components/DriftWall";
import AccordionGallery from "./components/AccordionGallery";
import "./App.css";

/* Nocturne jacket shots for the perspective wall */
const wallTiles = [
  { image: "/images/wall/resized_BEN03137.webp", title: "Curiosity I" },
  { image: "/images/wall/resized_BEN03166.webp", title: "Curiosity II" },
  { image: "/images/wall/resized_BEN03202.webp", title: "Curiosity III" },
  { image: "/images/wall/resized_BEN03324.webp", title: "Desire I" },
  { image: "/images/wall/resized_BEN03515.webp", title: "Desire II" },
  { image: "/images/wall/resized_BEN03619.webp", title: "Audacity I" },
  { image: "/images/wall/resized_BEN03655.webp", title: "Audacity II" },
  { image: "/images/wall/resized_BEN03767.webp", title: "Audacity III" },
  { image: "/images/wall/resized_BEN03806.webp", title: "Audacity IV" },
  { image: "/images/wall/resized_BEN04014.webp", title: "Temptation I" },
  { image: "/images/wall/resized_BEN04053.webp", title: "Insolence I" },
  { image: "/images/wall/resized_BEN04058.webp", title: "Insolence II" },
  { image: "/images/wall/resized_BEN04068.webp", title: "Insolence III" },
  { image: "/images/wall/resized_BEN04099.webp", title: "Insolence IV" },
  { image: "/images/wall/resized_DSC04253.webp", title: "Nocturne Detail" },
];

/* Five Nocturne jackets for AccordionGallery */
const nocturneJackets = [
  { image: "/images/wall/resized_BEN03137.webp", label: "01 / Curiosity", link: "#" },
  { image: "/images/wall/resized_BEN04014.webp", label: "02 / Temptation", link: "#" },
  { image: "/images/wall/resized_BEN03324.webp", label: "03 / Desire", link: "#" },
  { image: "/images/wall/resized_BEN03806.webp", label: "04 / Audacity", link: "#" },
  { image: "/images/wall/resized_BEN04053.webp", label: "05 / Insolence", link: "#" }
];

export default function App() {
  return (
    <main className="nocturne-page">
      {/* Header */}
      <header className="nocturne-header">
        <span className="brand">EKKOMI</span>
        <span className="collection-label">THE HOUSE COLLECTION</span>
      </header>

      {/* Hero: perspective drift wall + overlaid intro copy */}
      <section className="hero" aria-labelledby="nocturne-title">
        <div className="hero__wall">
          <DriftWall
            items={wallTiles}
            columns={5}
            tileWidth={220}
            tileHeight={300}
            gap={14}
            radius={6}
            tilt={14}
            turn={-12}
            perspective={1100}
            depth={100}
            speed={28}
            direction="up"
            variance={0.4}
            parallax={0.5}
            lift={72}
            fade={0.55}
            dim={0.45}
            grayscale={false}
            overlayColor="#0a0a08"
          />
        </div>

        <div className="hero__content">
          <p className="eyebrow">THE FIRST COLLECTION</p>
          <h1 id="nocturne-title">NOCTURNE</h1>
          <p className="intro-copy">
            Five impulses. Five jackets. One instinct.
          </p>
        </div>
      </section>

      {/* Accordion Gallery Showcase */}
      <section className="accordion-section">
        <div className="accordion-section__header">
          <p className="eyebrow">THE IMPULSES</p>
          <h2 className="accordion-section__title">THE FIVE SILHOUETTES</h2>
          <p className="accordion-section__sub">Hover across each panel to reveal the craftsmanship and form.</p>
        </div>

        <div className="accordion-section__wrapper">
          <AccordionGallery
            items={nocturneJackets}
            defaultIndex={2}
            expandRatio={0.52}
            trigger="hover"
            height={520}
            radius={14}
            gap={12}
            accentColor="#B89B72"
            overlayColor="#0a0a08"
          />
        </div>
      </section>

      {/* Footer */}
      <footer className="nocturne-footer">
        <span>CRAFTED IN SUEDE</span>
        <span>01 - 05</span>
        <span>AN EXPRESSION OF SELF</span>
      </footer>
    </main>
  );
}
"""

with open(r'F:\ekkomi-carousel\src\App.jsx', 'w', encoding='utf-8') as f:
    f.write(app_jsx)

print("Updated F:\\ekkomi-carousel\\src\\App.jsx")
