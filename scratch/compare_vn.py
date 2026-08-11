with open('notes/transcheck-vn.md', 'r', encoding='utf-8') as f:
    print("transcheck-vn.md content:")
    print(f.read())

with open('drafts/vn.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find all «...» — ... in vn.md
pairs = re.findall(r'«([^»]+)»\s*—\s*([^(\n]+)', text)
print(f"Found {len(pairs)} «...» — ... pairs in vn.md")
for i, (q, r) in enumerate(pairs, 1):
    print(f"{i}: «{q[:30]}...» -> {r[:30]}...")

