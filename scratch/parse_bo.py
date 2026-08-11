import re

with open('drafts/bo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all occurrences of guillemets «...»
guillemets = re.findall(r'«([^»]+)»', text)

print(f"Total guillemet passages found: {len(guillemets)}")
for i, g in enumerate(guillemets, 1):
    print(f"--- {i} ---")
    print(g)
