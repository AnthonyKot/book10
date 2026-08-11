import re

with open('resources/bo-2024-texto-aprendizaje-4to.txt', 'r', encoding='utf-8') as f:
    source_text = f.read()

def norm(s):
    s = re.sub(r'[^\w\s]', ' ', s.lower())
    return ' '.join(s.split())

source_norm = norm(source_text)

items = [
    ("LA VENTA DE ESTE DOCUMENTO ESTÁ PROHIBIDA", 2),
    ("un elemento dinamizador del aprendizaje, que siempre puede ampliarse, profundizarse y contextualizarse desde la experiencia y la realidad de cada contexto cultural, social y educativo", 5),
    ("de acuerdo con los Planes y Programas establecidos para cada nivel educativo", 5),
    ("PROMOCIÓN DE LA EQUIDAD DE GÉNERO EN ARMONÍA CON LA MADRE TIERRA EN EL ESTUDIO DE LAS CORRIENTES LITERARIAS", 24),
    ("el conjunto de obras literarias de similares características tanto en el estilo, temas e ideologías que expresan el espíritu de una determinada época", 24),
    ("Realismo y naturalismo", 27),
    ("Obras emblemáticas y Autores representativos", 25),
    ("Inspirados en el estudio de las corrientes literarias, realicemos una dramatización corta acerca de una de ellas… En la dramatización presentar a un autor y su producción literaria", 29),
    ("Destaca entre las demás porque nació por primera vez en América y no es una imitación de ninguna otra corriente. Por el contrario, este movimiento influyó desde América hasta Europa.", 29),
    ("Con expresividad leemos en clase y el siguiente fragmento, el cual es uno de los textos más conocidos en la historia del teatro universal", 30),
    ("¿Has escuchado hablar de William Shakespeare?", 30),
    ("¿Te resulta triste o cómica la situación que se plantea?", 30),
    ("LA IMPORTANCIA DE LOS MEDIOS RADIOFÓNICOS EN LA LUCHA CONTRA LA DESIGUALDAD SOCIAL", 36),
    ("Para estos jefes, los micrófonos eran cañones que disparaban ideas… Triste confusión de planos. Porque en el terreno militar se vence. Pero en el terreno de las ideas se convence.", 36),
    ("nos bombardean a diario con noticias que desinforman… Hacen terrorismo mediático. Pero nosotros no podemos ni queremos jugar ese mismo juego, aunque sea al revés. Por ética", 36),
    ("¿Cómo contribuiríamos a resolver / aportar soluciones a través de la literatura de dicha corriente?", 29),
    ("siempre puede ampliarse", 5)
]

for txt, pg in items:
    # search in source_text
    t_clean = txt.replace("…", "").strip()
    words = t_clean.split()
    found = False
    if norm(t_clean) in source_norm:
        found = True
    else:
        # try 3-4 word chunk
        for i in range(len(words)-2):
            chk = norm(" ".join(words[i:i+3]))
            if chk in source_norm:
                found = True
                break
    print(f"Page {pg}: Verified={found} | Quote: '{txt[:50]}...'")

