import re, json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections_raw = re.split(r'(?=<section class="jacket-detail-section" id="jacket-)', html)
print(f"Total chunks: {len(sections_raw)}")

jackets_info = {}
for chunk in sections_raw[1:]:
    m_id = re.search(r'id="(jacket-[a-z-]+)"', chunk)
    if not m_id:
        continue
    jid = m_id.group(1).replace('jacket-', '')
    
    m_headline = re.search(r'<p class="jacket-headline">(.*?)</p>', chunk, re.DOTALL)
    m_narrative = re.search(r'<p class="jacket-narrative">(.*?)</p>', chunk, re.DOTALL)
    
    craft_pairs = re.findall(r'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', chunk, re.DOTALL)
    
    jackets_info[jid] = {
        'headline': m_headline.group(1).strip() if m_headline else '',
        'narrative': m_narrative.group(1).strip() if m_narrative else '',
        'craft': [{'title': c[0].strip(), 'desc': c[1].strip()} for c in craft_pairs]
    }

with open('scratch/jackets_editorial_data.json', 'w', encoding='utf-8') as f:
    json.dump(jackets_info, f, indent=2, ensure_ascii=False)

print(f"Extracted info for {len(jackets_info)} jackets:")
for k, v in jackets_info.items():
    print(f"- {k}: {len(v['headline'])} chars headline, {len(v['craft'])} craft items")
