with open('resources/bo-2024-texto-aprendizaje-4to.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Remove all line breaks and spaces between words
text_single_line = ' '.join(text.split())

for q in ["Obras emblemáticas y Autores representativos", "Obras emblemáticas y autores representativos"]:
    clean_q = ' '.join(q.split())
    if clean_q.lower() in text_single_line.lower():
        print(f"FOUND: '{q}'")
    else:
        print(f"NOT FOUND: '{q}'")
