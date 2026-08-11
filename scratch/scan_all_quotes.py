import re

with open('drafts/bo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for any non-English string inside quotes/guillemets followed by an English translation
# Patterns: «...» — ..., "..." —, (...) — ...

# Let's find all guillemets
g_matches = re.findall(r'«([^»]+)»([^.\n\n]*)', text)
print(f"Total guillemet matches: {len(g_matches)}")

for i, (q, rest) in enumerate(g_matches, 1):
    # check if rest contains translation indicator like '—', 'or', 'meaning', etc.
    print(f"Match {i}:")
    print(f"  Q: {repr(q)}")
    print(f"  Rest: {repr(rest[:100])}")
