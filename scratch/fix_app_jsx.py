path = r'F:\ekkomi-carousel\src\App.jsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """const nocturneJackets = [
  { image: "/images/wall/resized_BEN03137.webp", label: "01 / Curiosity", link: "#" },
  { image: "/images/wall/resized_BEN04014.webp", label: "02 / Temptation", link: "#" },
  { image: "/images/wall/resized_BEN03324.webp", label: "03 / Desire", link: "#" },
  { image: "/images/wall/resized_BEN03806.webp", label: "04 / Audacity", link: "#" },
  { image: "/images/wall/resized_BEN04053.webp", label: "05 / Insolence", link: "#" }
];"""

new_block = """const nocturneJackets = [
  { image: "/images/wall/resized_BEN03137.webp", label: "01 / Curiosity", link: "#" },
  { image: "/images/wall/resized_BEN03655.webp", label: "02 / Temptation", link: "#" },
  { image: "/images/wall/resized_BEN03806.webp", label: "03 / Desire", link: "#" },
  { image: "/images/wall/resized_BEN04068.webp", label: "04 / Audacity", link: "#" },
  { image: "/images/wall/resized_BEN03324.webp", label: "05 / Insolence", link: "#" }
];"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated F:\\ekkomi-carousel\\src\\App.jsx successfully!')
else:
    print('Block not found!')
