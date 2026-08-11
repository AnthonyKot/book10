# Mexico 2024 reconciliation

## Summary

- Rows before/after: 13/9.
- Era edits: 3 disputed `subject_era` values corrected to the work's represented subject or setting.
- Memorize edits: 0.
- Quarantined rows: 4 unsupported rows moved out of the corpus and preserved below.

The renewed receipt search covered every saved defining document using Spanish names and titles plus accentless, alternate-spelling, Indigenous-language, romanized, numeric, and English variants. None of the four claimed Mexican selections was found. The only `ceiba` hit was an unrelated passage from Cristina García's *Dreaming in Cuban* in the U.S. Common Core appendix; it does not support the Mexican row.

## Systemic memorize ruling

`yes` or `excerpt` requires an explicit defining-document mandate to learn the named text, a named excerpt, or a stated quantity of texts *naizust*, by heart, or `암기` at this level. Closed-book examinations, implied quote-learning, and general recitation culture do not qualify. The Mexican defining program contains no such mandate for any retained row, so all nine retained values remain `no`.

## Change log

- Data row 1, *Textos literarios escritos en español o traducidos* — `subject_era`: `contemporary-and-historical-literature?` -> `various/no-single-era (open choice)`; the Grade 9 program leaves both literary genre and theme to the student's choice, so it fixes no represented historical era.
- Data row 7, *Creaciones literarias tradicionales y contemporáneas en lenguas indígenas* — `subject_era`: `indigenous-languages-and-territory?` -> `traditional-and-contemporary/no-single-era (open creation)`; the assigned creations can be traditional or contemporary and real or fictional, while territory is a separate content row.
- Data row 9, *Creaciones artísticas y colectivas basadas en textos literarios* — `subject_era`: `artistic-interdisciplinary-adaptation?` -> `various/no-single-era (chosen source text)`; adaptation is the activity, not a represented period, and the source text is unrestricted.
- Data row 10, *Leyenda de Nanahuatzin / El día que Nanahuatzin se convirtió en el Sol* — `corpus -> quarantine`; absent under `Nanahuatzin`, `Nanauatzin`, `Nanahuatl`, and close Spanish/English title variants from every saved defining document.
- Data row 11, *Ueuehtlahtol: La palabra de los ancestros* — `corpus -> quarantine`; absent under `Ueuehtlahtol`, `Huehuehtlahtolli`, `Huehuetlahtolli`, and close title variants from every saved defining document.
- Data row 12, *El árbol sagrado: La ceiba* — `corpus -> quarantine`; absent under `ceiba`, `seiba`, `yaxché`, and Spanish/English title variants from every saved Mexican defining document; the sole cross-resource `ceiba` hit is unrelated.
- Data row 13, *Ñuhu: descendientes de 9 Lagarto y 5 Viento son espíritus de la Tierra* — `corpus -> quarantine`; absent under `Ñuhu`, `Nuhu`, `Nyuhu`, `Hñähñu`, `Otomí`, numeral/word forms of 9 Lagarto and 5 Viento, and English title variants from every saved defining document.

## Quarantine

These rows preserve every pre-reconciliation field.

```tsv
author	title	author_born	author_died	origin	genre	subject_era	exam_status	memorize	grade	source	doc_year	retrieved	note
Anónimo (Tradición Oral Mexica) (Anonymous (Mexica Oral Tradition))	"Leyenda de Nanahuatzin / ""El día que Nanahuatzin se convirtió en el Sol"" (""Legend of Nanahuatzin / The Day Nanahuatzin Became the Sun"")"	traditional	traditional	domestic	short-story	pre-hispanic-mythology?	anthology-only	no	9	https://libros.conaliteg.gob.mx/	2023	2026-08-10	Eponymous foundational indigenous text in CONALITEG Colección Nanahuatzin 3er grado (SEP)
Autores y cultores del Ueuehtlahtol (Ancestral Nahua Orators)	"Ueuehtlahtol: La palabra de los ancestros (""Huehuehtlahtolli: The Ancient Word / Advice of the Elders"")"	traditional	traditional	domestic	essay	pre-hispanic-indigenous-philosophy?	anthology-only	no	9	https://libros.conaliteg.gob.mx/	2023	2026-08-10	Prescribed indigenous ancestral text unit in CONALITEG Nuestro libro de proyectos 3er grado (SEP)
Autores de la ceiba sagrada (Maya Oral Tradition)	"El árbol sagrado: La ceiba (""The Sacred Tree: The Ceiba"")"	traditional	traditional	domestic	short-story	maya-cosmovision?	anthology-only	no	9	https://libros.conaliteg.gob.mx/	2023	2026-08-10	Prescribed indigenous cosmovision text in CONALITEG Múltiples Lenguajes 3er grado (SEP, p. 36)
Autores Ñuhu (Otomí Oral Tradition)	"Ñuhu: descendientes de 9 Lagarto y 5 Viento son espíritus de la Tierra (""Ñuhu: Descendants of 9 Lizard and 5 Wind, Spirits of the Earth"")"	traditional	traditional	domestic	short-story	indigenous-otomi-cosmovision?	anthology-only	no	9	https://libros.conaliteg.gob.mx/	2023	2026-08-10	Prescribed Otomí mythic text selection in CONALITEG Múltiples Lenguajes 3er grado (SEP, p. 23)
```
