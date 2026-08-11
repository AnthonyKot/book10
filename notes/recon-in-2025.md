# India 2025 reconciliation

Row numbers below are the original data-row numbers in `corpus/in-2025.tsv`; the header is excluded.

## Summary

- Rows: 46 before -> 43 after.
- Era edits: 15 disputed `subject_era` values corrected to the work's represented subject or setting.
- Memorize edits: 0; all 46 reviewed values were already `no`.
- Quarantined rows: 3 unsupported Kritika rows moved out of the corpus and preserved below.

The era rulings were checked against the saved NCERT reader archives and the CBSE 2024-25 curricula. The three flagged rows were rechecked across the saved India curricula, contents ledger, and NCERT reader archives under Hindi and Latin-script title and author variants. None of the three titles occurs in a saved defining document. The Hindi A curriculum prescribes *Kritika Part 2* and names two excluded chapters, but it does not name these three included titles; no saved Kritika contents or text receipt closes that gap. An isolated `Hiroshima` occurrence in the *Black Aeroplane* exercises is unrelated to Agyeya's essay and does not support that row.

## Systemic memorize ruling

`yes` or `excerpt` requires an explicit defining-document mandate to learn the named text, a named excerpt, or a stated quantity of texts by heart at this level. The English curriculum's general suggested activity “Reciting poems,” the Hindi curriculum's listening/speaking and poetry-comprehension assessments, closed-book examination, implied quotation learning, and general recitation culture do not meet that rule. No defining document mandates memorization of any named row, so every reviewed `memorize=no` value remains unchanged.

## Change log

### Subject era

- Row 4, Frederick Forsyth, *Black Aeroplane* — `subject_era`: `WWII-aviation?` -> `none/aviation-mystery`; the undated flight from France to England becomes a supernatural storm mystery, with no war or WWII setting.
- Row 9, Gavin Maxwell, *Mijbil the Otter* — `subject_era`: `post-WWII-iraq-scotland?` -> `1956-iraq-to-london/pet-natural-history`; the excerpt explicitly begins in southern Iraq in 1956 and follows Mij to London, while the Scottish cottage is proposed background rather than the represented journey.
- Row 14, Robert Frost, *Fire and Ice* — `subject_era`: `1920s-apocalyptic-apathy?` -> `none/desire-hatred-and-apocalyptic-allegory`; the poem represents desire and hate as destructive forces, while 1920 dates composition and apathy is not its subject.
- Row 18, Robin Klein, *Amanda!* — `subject_era`: `contemporary-adolescence?` -> `none/parental-control-and-imagined-escape`; repeated parental commands and Amanda's imagined escapes fix the subject, but no historical period is represented.
- Row 19, Adrienne Rich, *The Trees* — `subject_era`: `1960s-feminism-ecocriticism?` -> `none/nature-escape-and-freedom-allegory`; the trees escape confinement in a house, while the author's period and biography do not establish a 1960s setting or an explicitly historical feminist subject.
- Row 26, Victor Canning, *A Question of Trust* — `subject_era`: `mid-20th-c-crime/irony?` -> `none/crime-deception-and-irony`; the jewel robbery turns on one thief deceiving another, and the story supplies no datable historical setting.
- Row 31, Claire Boiko, *The Book that Saved the Earth* — `subject_era`: `25th-c-sci-fi/nursery-rhymes?` -> `2040-martian-invasion/25th-c-historical-frame`; the twenty-fifth-century museum frames a reenactment whose central action is the aborted Martian invasion of 2040.
- Row 32, सूरदास (Surdas), *पद* — `subject_era`: `bhakti-era-gopi-krishna-devotion` -> `mythic-krishna-era/gopi-separation-and-devotion`; the verses represent the gopis' separation from Krishna and their address to Uddhav, while Bhakti names composition and literary context.
- Row 34, जयशंकर प्रसाद (Jaishankar Prasad), *आत्मकथ्य* — `subject_era`: `chhayavad-era-introspection?` -> `none/introspection-and-reluctance-to-self-disclose`; the speaker reflects on private pain and resists turning it into autobiography, while Chhayavad is the poem's movement.
- Row 35, सूर्यकांत त्रिपाठी 'निराला' (Suryakant Tripathi 'Nirala'), *उत्साह और अट नहीं रही* — `subject_era`: `chhayavad-era-nature-revolution?` -> `none/nature-spring-and-revolutionary-renewal`; the paired poems represent clouds, spring, energy, and renewal, not the historical period of Chhayavad.
- Row 36, नागार्जुन (Nagarjun), *यह दंतुरित मुस्कान और फसल* — `subject_era`: `pragativad-era-rural-life?` -> `none/family-affection-and-collective-agrarian-labor`; one poem centers a child's life-giving smile and the other the natural and human collaboration behind a crop, while Pragativad is literary context.
- Row 37, मंगलेश डबराल (Manglesh Dabral), *संगतकार* — `subject_era`: `contemporary-artistic-labor?` -> `none/overlooked-artistic-labor`; the poem concerns the accompanist's quiet supporting work without fixing a contemporary historical period.
- Row 41, मन्नू भंडारी (Mannu Bhandari), *एक कहानी यह भी* — `subject_era`: `1942-quit-india-movement/female-autonomy?` -> `1946-1947-independence-agitation/female-authorship-and-autonomy`; the represented student strikes and processions belong to 1946-47, not the 1942 Quit India movement, within a memoir of authorship and autonomy.
- Row 42, यतींद्र मिश्र (Yatindra Mishra), *नौबतखाने में इबादत* — `subject_era`: `post-independence-benares-shehnai-bismillah-khan?` -> `20th-c-india/bismillah-khan-shehnai-and-1947-independence`; the portrait spans Khan's pre-independence formation and his Red Fort performance on 15 August 1947, so a post-independence-only code is too narrow.
- Row 43, भदंत आनंद कौसल्यायन (Bhadant Anand Kausalyayan), *संस्कृति* — `subject_era`: `20th-c-buddhist-humanism?` -> `none/culture-civilization-and-human-invention`; the essay distinguishes culture from civilization through broad examples of discovery, inheritance, and human welfare; the author's century and Buddhist identity are not its represented era.

### Quarantine moves

- Row 44, शिवपूजन सहाय (Shivpujan Sahay), *माता का आँचल* — `corpus -> quarantine`; absent under Hindi and Latin-script title/author variants from every saved defining document, which names *Kritika Part 2* but does not receipt this included title.
- Row 45, कमलेश्वर (Kamleshwar), *साना-साना हाथ जोड़ि* — `corpus -> quarantine`; absent under Hindi and Latin-script title/author variants from every saved defining document, which names *Kritika Part 2* but does not receipt this included title.
- Row 46, अज्ञेय (S.H. Vatsyayan 'Agyeya'), *मैं क्यों लिखता हूँ?* — `corpus -> quarantine`; absent under Hindi and Latin-script title/author variants from every saved defining document; the unrelated `Hiroshima` exercise hit does not receipt the essay.

## Quarantine

These rows are preserved verbatim from the pre-reconciliation TSV.

```tsv
author	title	author_born	author_died	origin	genre	subject_era	exam_status	memorize	grade	source	doc_year	retrieved	note
शिवपूजन सहाय (Shivpujan Sahay)	"माता का आँचल (""Mata Ka Aanchal"" - Mother's Lap)"	1893	1963	domestic	novella	1920s-rural-bihar-childhood?	mandatory	no	10	https://cbseacademic.nic.in/web_material/CurriculumMain25/Sec/Hindi_A_Sec_2024-25.pdf	2024	2026-08-10	Kritika Part-2 Ch 1; excerpt from Dehati Duniya (1926)
कमलेश्वर (Kamleshwar)	"साना-साना हाथ जोड़ि (""Sana-Sana Hath Jodi"" - Joining Hands in Prayer)"	1932	2007	domestic	essay	contemporary-sikkim-border-labor?	mandatory	no	10	https://cbseacademic.nic.in/web_material/CurriculumMain25/Sec/Hindi_A_Sec_2024-25.pdf	2024	2026-08-10	Kritika Part-2 Ch 3; travelogue on Sikkim and road workers
अज्ञेय (S.H. Vatsyayan 'Agyeya')	"मैं क्यों लिखता हूँ? (""Main Kyon Likhata Hoon?"" - Why Do I Write?)"	1911	1987	domestic	essay	hiroshima-atomic-bomb	mandatory	no	10	https://cbseacademic.nic.in/web_material/CurriculumMain25/Sec/Hindi_A_Sec_2024-25.pdf	2024	2026-08-10	Kritika Part-2 Ch 5; essay on visiting Hiroshima bomb site
```
