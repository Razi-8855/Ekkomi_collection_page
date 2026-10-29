import json, re

with open('scratch/jackets_editorial_data.json', 'r', encoding='utf-8') as f:
    editorial = json.load(f)

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Verify that all 8 jacket IDs are in editorial data
expected_ids = [
    'men-curiosity', 'men-temptation', 'men-desire', 'men-audacity', 'men-insolence',
    'women-curiosity', 'women-desire', 'women-audacity'
]

for jid in expected_ids:
    assert jid in editorial, f"Missing {jid} in editorial data"
    ed = editorial[jid]
    assert len(ed['headline']) > 0, f"Empty headline for {jid}"
    assert len(ed['narrative']) > 0, f"Empty narrative for {jid}"
    assert len(ed['craft']) == 3, f"Expected 3 craft items for {jid}, got {len(ed['craft'])}"

print("All 8 jackets have 100% verified editorial data!")

