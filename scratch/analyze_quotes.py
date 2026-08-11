import re

with open('drafts/bo.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('resources/bo-2024-texto-aprendizaje-4to.txt', 'r', encoding='utf-8') as f:
    source_text = f.read()

# Normalize whitespace function for searching source
def norm_space(s):
    return ' '.join(s.split())

source_norm = norm_space(source_text)

print("=== SEARCHING ALL QUOTES IN BO.MD ===")
# Find all lines with guillemets or quotes
for line_num, line in enumerate(lines, 1):
    if '«' in line or '“' in line or '"' in line:
        # print line if it has potential quote + rendering
        print(f"L{line_num}: {line.strip()}")

