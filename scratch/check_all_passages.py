import re

with open('drafts/bo.md', 'r', encoding='utf-8') as f:
    essay_text = f.read()

with open('resources/bo-2024-texto-aprendizaje-4to.txt', 'r', encoding='utf-8') as f:
    source_text = f.read()

def norm(s):
    # remove punctuation, lower case, normalize spaces
    s = re.sub(r'[^\w\s]', ' ', s.lower())
    return ' '.join(s.split())

source_norm = norm(source_text)

# Let's define all potential quoted non-English passages found in bo.md
passages = [
    {
        "id": 1,
        "location": "p. 2 (line 12)",
        "original": "LA VENTA DE ESTE DOCUMENTO ESTÁ PROHIBIDA",
        "essay_rendering": "the sale of this document is prohibited",
    },
    {
        "id": 2,
        "location": "p. 5 (line 22-26)",
        "original": "un elemento dinamizador del aprendizaje, que siempre puede ampliarse, profundizarse y contextualizarse desde la experiencia y la realidad de cada contexto cultural, social y educativo",
        "essay_rendering": "an element that energizes learning, one that can always be widened, deepened and put in context from the experience and reality of each cultural, social and educational setting",
    },
    {
        "id": 3,
        "location": "p. 5 (line 28-29)",
        "original": "de acuerdo con los Planes y Programas establecidos para cada nivel educativo",
        "essay_rendering": "in accordance with the Plans and Programs established for each educational level",
    },
    {
        "id": 4,
        "location": "p. 24 (line 38-40)",
        "original": "PROMOCIÓN DE LA EQUIDAD DE GÉNERO EN ARMONÍA CON LA MADRE TIERRA EN EL ESTUDIO DE LAS CORRIENTES LITERARIAS",
        "essay_rendering": "promotion of gender equity in harmony with Mother Earth in the study of literary currents",
    },
    {
        "id": 5,
        "location": "p. 24 (line 40-44)",
        "original": "el conjunto de obras literarias de similares características tanto en el estilo, temas e ideologías que expresan el espíritu de una determinada época",
        "essay_rendering": "the set of literary works of similar characteristics in style, themes and ideologies, which express the spirit of a given epoch",
    },
    {
        "id": 6,
        "location": "p. 25 (line 52-53)",
        "original": "Obras emblemáticas y Autores representativos",
        "essay_rendering": "Emblematic works and representative authors",
    },
    {
        "id": 7,
        "location": "p. 29 (line 75-79)",
        "original": "Inspirados en el estudio de las corrientes literarias, realicemos una dramatización corta acerca de una de ellas… En la dramatización presentar a un autor y su producción literaria",
        "essay_rendering": "let us stage a short dramatization about one of the currents; present an author and his literary production",
    },
    {
        "id": 8,
        "location": "p. 29 (line 109-113)",
        "original": "Destaca entre las demás porque nació por primera vez en América y no es una imitación de ninguna otra corriente. Por el contrario, este movimiento influyó desde América hasta Europa.",
        "essay_rendering": "It stands out from the rest because it was born for the first time in America and is not an imitation of any other current. On the contrary, this movement influenced from America as far as Europe.",
    },
    {
        "id": 9,
        "location": "p. 30 (line 148-151)",
        "original": "Con expresividad leemos en clase y el siguiente fragmento, el cual es uno de los textos más conocidos en la historia del teatro universal",
        "essay_rendering": "with expressiveness we read in class the following fragment, one of the best-known texts in the history of world theatre",
    },
    {
        "id": 10,
        "location": "p. 30 (line 154-155)",
        "original": "¿Has escuchado hablar de William Shakespeare?",
        "essay_rendering": "have you heard of Shakespeare",
    },
    {
        "id": 11,
        "location": "p. 30 (line 154-155)",
        "original": "¿Te resulta triste o cómica la situación que se plantea?",
        "essay_rendering": "do you find the situation sad or funny",
    },
    {
        "id": 12,
        "location": "p. 36 (line 163-165)",
        "original": "LA IMPORTANCIA DE LOS MEDIOS RADIOFÓNICOS EN LA LUCHA CONTRA LA DESIGUALDAD SOCIAL",
        "essay_rendering": "the importance of radio media in the struggle against social inequality",
    },
    {
        "id": 13,
        "location": "p. 36 (line 170-174)",
        "original": "Para estos jefes, los micrófonos eran cañones que disparaban ideas… Triste confusión de planos. Porque en el terreno militar se vence. Pero en el terreno de las ideas se convence.",
        "essay_rendering": "For these chiefs, microphones were cannons firing ideas… A sad confusion of registers. Because on military ground one conquers. But on the ground of ideas one convinces.",
    },
    {
        "id": 14,
        "location": "p. 36 (line 176-180)",
        "original": "nos bombardean a diario con noticias que desinforman… Hacen terrorismo mediático. Pero nosotros no podemos ni queremos jugar ese mismo juego, aunque sea al revés. Por ética",
        "essay_rendering": "they bombard us daily with news that misinforms… They practise media terrorism. But we cannot and do not want to play that same game, even in reverse. Out of ethics",
    },
    {
        "id": 15,
        "location": "p. 29 (line 184-186)",
        "original": "¿Cómo contribuiríamos a resolver / aportar soluciones a través de la literatura de dicha corriente?",
        "essay_rendering": "how would we contribute to solving, or offer solutions, through the literature of that current",
    },
    {
        "id": 16,
        "location": "p. 5 (line 199)",
        "original": "siempre puede ampliarse",
        "essay_rendering": "that it can always be widened",
    }
]

print("=== VERIFYING IN SOURCE DOCUMENT ===")
for p in passages:
    orig = p["original"].replace("…", " ")
    # split into smaller fragments if needed
    frags = [f for f in orig.split() if len(f) > 3]
    # check exact norm match first
    norm_orig = norm(orig)
    if norm_orig in source_norm:
        found = True
        match_type = "exact"
    else:
        # check fragment matching
        # try 4-5 word chunk
        words = orig.split()
        found = False
        for start in range(len(words)-3):
            chunk = norm(' '.join(words[start:start+4]))
            if chunk in source_norm:
                found = True
                match_type = f"chunk: {' '.join(words[start:start+4])}"
                break
    p["source_verified"] = found
    p["match_type"] = match_type if found else "NOT FOUND"
    print(f"[{p['id']}] Verified: {found} ({p['match_type']}) - '{p['original'][:40]}...'")

