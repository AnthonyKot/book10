import re

with open('resources/bo-2024-texto-aprendizaje-4to.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

print("=== SEARCHING FOR emblemáticas ===")
for i, line in enumerate(lines, 1):
    if 'emblemática' in line.lower() or 'representat' in line.lower():
        print(f"L{i}: {line}")
