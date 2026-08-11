with open('resources/bo-2024-texto-aprendizaje-4to.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1380, 1405):
    print(f"L{i+1}: {repr(lines[i])}")
