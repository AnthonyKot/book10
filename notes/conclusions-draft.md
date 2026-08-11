# Conclusions draft — what the present shelf can honestly bear

This is a reading of twenty country files, not a ranking of twenty school systems. Three files — Belgium, Switzerland, and Norway — contain only the header. The populated files mix a national codifier, a state prescription, an exam-board specification, an anthology table of contents, open curricular formulas, and suggested reading. They also cover different grades. A row therefore proves only that the named document gives a work or a category the stated place. It does not prove how often a book was taught, how many pupils read it, or that two rows in two systems carry equal force.

The generated window report needs one further warning. Its “253 distinct foreign authors/works” are author keys, not distinct works. It collapses several works by one author, retains only one title per author-country pair, and can split `Shakespeare, William` from `William Shakespeare`. Its period is the author's birth period, not the work's setting, and it assigns only one of an author's genres to the grouped display. The grouped shelf is useful as an index for reading; those totals and placements are not publication-ready findings.

## 1. What the grouped shelf shows, by instrument

### Window size

The tables show radically different *forms* of window, but their row counts are not a common measure of openness.

- Australia's NSW file has 85 foreign-origin rows, all on choice lists. Ukraine has 39: 13 mandatory and 26 choice-list rows. Vietnam has 29 choice-list rows. Kazakhstan has 27: 13 mandatory and 14 choice-list rows.
- Bolivia has 25 foreign-origin rows, all anthology-only. India has 24, all marked mandatory. The United States file has 22, all choices in a Common Core exemplar appendix rather than a national set-text mandate. Brazil has 20: two mandatory and 18 choices, all from the Portuguese-speaking world.
- China has five named foreign works, all marked mandatory. Italy has five named foreign rows, four mandatory and one open classical choice. Mongolia has one anthology row. Russia has one omnibus choice row for foreign literature, with Homer, Cervantes, Shakespeare, and Molière given as examples.
- Germany and Mexico contain open formulas that permit domestic or translated selections; because those rows are coded `choice:domestic/translated`, they do not enter the generated foreign shelf. The AQA file contains 73 rows and no row coded foreign. Belgium, Switzerland, and Norway have no data rows.

The honest reading is administrative: some documents name books, some name traditions, some offer menus, and some leave the selection open. “One row” can mean one work, several works bundled together, a whole national literature, or an unrestricted slot.

### The shared shelf

The shelf shares authors more readily than it shares works. A manual merge of name-order variants finds Shakespeare in seven files: Australia, Bolivia, Belarus, Kazakhstan, Ukraine, the United States, and Vietnam. Those files offer different objects: six plays in the NSW menu; *Hamlet* in Bolivia; *Hamlet* or sonnets in Belarus; sonnets and *Romeo and Juliet* in Kazakhstan; a choice of two sonnets in Ukraine; *Macbeth* and “Sonnet 73” in the United States appendix; and *Romeo and Juliet* in Vietnam. The Belarus confirmation pass flags its Shakespeare row as unsupported by the saved defining document.

The report's next recurrent names reach only three displayed country columns: Goethe, Chekhov, Homer, and Gogol. Even these are not uniform admissions. Goethe's Belarus row is flagged; Russia puts Homer inside one omnibus option; and the works, status, grades, and document types differ. This is evidence for a small zone of name recognition, not yet for a single enforceable world reading list.

### The enemy shelf

The present rows expose strong essay questions but do not support a general enemy-shelf verdict.

- Ukraine's foreign-literature rows retain two Russian-language choices: Gogol's *The Government Inspector* or *The Overcoat*, and Bulgakov's *Heart of a Dog*. Their table notes explain the retention through Gogol's Ukrainian origin and Bulgakov's Kyiv birth and anti-totalitarian satire. Russia's table contains no row coded as translated from Ukrainian; its one foreign row is an omnibus choice.
- Belarus contains two Ukrainian admissions: Shevchenko is mandatory and Lesya Ukrainka is a choice. Its claimed block of ten Russian admissions is not safe to use: the confirmation pass says those rows are absent from the saved Belarus documents and largely mirror the Russian OGE codifier.
- Kazakhstan contains 21 rows coded as translated from Russian, alongside six other foreign-origin rows. That is a plain shelf fact. Calling the shelf friendly, hostile, colonial, or post-colonial would require historical and institutional evidence outside this one file.
- Vietnam requires choice from Russian literature and also names Aitmatov and Chekhov; China mandates Ostrovsky; India mandates Chekhov. None of those admissions by itself identifies a present-day political relation.

The asymmetry visible in a slice may be described, but it cannot yet be narrated as refusal, reconciliation, or reform.

### The errand

The tables provide promising pairs for close reading. They do not yet prove a general theory of what nations “import feelings” to do.

- Shakespeare arrives as tragedy, comedy, history play, and sonnet; the common author does not run one common errand.
- Frost is represented by “Stopping by Woods on a Snowy Evening” in the NSW menu, “Dust of Snow” and “Fire and Ice” in India, and “The Road Not Taken” in Vietnam. Those are three different classroom objects.
- China's five foreign rows put an outsider's account of the Red Army beside adventure, natural history, a Soviet revolutionary novel, and *Jane Eyre*. One of those five, Fabre's *Souvenirs Entomologiques*, lacks a local work-level receipt in the confirmation pass.
- Ukraine's menu places canonical European poetry beside satire, science fiction, young-adult fiction, war fiction, slavery, disability, illness, and fantasy. The table's `subject_era` labels cannot safely carry that interpretation without repair: the confirmation pass corrects, among others, *War Horse* from WWII to WWI and *The Underground Railroad* from serfdom to United States slavery.

The errand should therefore be written work by work from corrected coding and the source document's teaching language, not inferred from author nationality or a broad period bin.

## 2. Conclusions that survive scrutiny

### Conclusion 1: The most durable difference in this corpus is the administrative door through which foreign literature enters, not a rank order of how “open” countries are.

Supporting plain facts:

- Russia represents foreign literature with one omnibus choice row; Germany and Mexico use mixed open formulas; Vietnam reserves at least one choice from each of eight named foreign literary traditions.
- China names five foreign works and marks all five mandatory. Bolivia's 25 foreign rows are anthology-only. Australia's 85 are all choices in a NSW senior prescription. Ukraine divides 39 foreign rows between 13 mandatory and 26 choices.
- Three country files have no rows. The AQA file has no row coded foreign, while the United States file is a suggested appendix and the Australian file belongs to one state.

Caveats that limit the sentence:

- **Data quality:** the confirmation notes flag unsupported rows in Belarus, China, India, Japan, Mexico, and Ukraine. Germany's and Mexico's mixed-origin slots disappear from a report that selects only origins beginning `translated`.
- **One-year slices:** each file captures one named document or document bundle. It supplies no before-and-after evidence.
- **Granularity:** a named work, a bundled oeuvre, a national-literature quota, an anthology item, and an exam-board option each count as one row. Grades also differ, with the NSW file at grades 11–12 and Vietnam spanning grades 6–12 in part of its foreign requirement.

### Conclusion 2: Shakespeare is the nearest thing here to a shared foreign author, but there is no shared Shakespeare assignment.

Supporting plain facts:

- After manually joining surname-first and given-name-first variants, Shakespeare appears in seven country files.
- The seven files name *Hamlet*, *Romeo and Juliet*, *Macbeth*, six different NSW plays, and several different sonnets or sonnet choices.
- No single Shakespeare work is present in all seven files, and the admissions range from anthology-only to mandatory to choice-list.
- The Belarus row is flagged as unsupported; removing that disputed row still leaves Shakespeare in six files.

Caveats that limit the sentence:

- **Data quality:** the generated leaderboard splits `Shakespeare, William` from `William Shakespeare` and overwrites multiple titles within a country. The count above comes from the TSV rows, not the leaderboard. Belarus remains disputed.
- **One-year slices:** recurrence in these files is not permanence and says nothing about earlier or later lists.
- **Granularity:** Australia is a state senior menu, Bolivia an anthology, Ukraine and Kazakhstan program lists, the United States an exemplar appendix, and the others different curricular instruments. Shared naming is not shared obligation or classroom use.

## 3. Claims rejected as not surviving

1. **“The corpus contains 253 distinct foreign works.”** Rejected. The report counts normalized author keys, collapses several works by one author, and can split the same author when names are ordered differently.

2. **“The leaderboard has established a de-facto world canon.”** Rejected. Name normalization is incomplete, one title overwrites another within a country, flagged rows remain in the count, and admissions of unlike force are treated alike.

3. **“Country A has a larger or more open window than Country B because it has more rows.”** Rejected. Eighty-five NSW choices, 25 Bolivian anthology entries, five Chinese mandates, and Russia's one omnibus option are not commensurate units.

4. **“A zero means a closed national window.”** Rejected. Belgium, Switzerland, and Norway are empty files. Germany and Mexico have mixed-origin open slots that the foreign-row filter omits. AQA is one exam board; NSW is one state; the United States table is an exemplar appendix.

5. **“England excludes foreign experience.”** Rejected. The AQA file has no translated-origin row, but it includes British writing about migration, empire, kamikaze, Guyana, and other places. More importantly, one board's origin coding cannot stand for every English classroom.

6. **“The enemy shelf proves political friendship or hostility.”** Rejected. Ukraine's two Russian-language choices and Russia's lack of a Ukrainian-coded row are real facts in these files, but author identity is contested, the documents are asymmetric, and there is no historical comparison in the corpus.

7. **“Ukraine's shelf proves a post-2022 removal.”** Rejected for this draft. A 2022 or 2023 source date and two retained Russian-language choices do not establish what was removed. That claim needs a prior list and a dated revision receipt.

8. **“Kazakhstan's 21 Russian rows have one political meaning.”** Rejected. The file establishes admission, not whether it reflects inheritance, language policy, coercion, convenience, esteem, or classroom practice.

9. **“The period-by-genre grouping shows the age or historical interests of each window.”** Rejected. Period is generated from author birth, not work date or represented era; the report keeps only one genre for an author; and many `subject_era` codes confuse composition context with represented subject.

10. **“The wound map or errand can be read directly from `subject_era`.”** Rejected. Confirmation passes record 34 era checks in Belarus, 33 in Vietnam, 28 each in Russia and Kazakhstan, 21 in Australia, and 17 in AQA. Recurrent errors include treating publication period, movement, or author biography as the work's represented wound.

11. **“Memorization can now be compared across systems.”** Rejected. The confirmation passes record disagreements for all 73 AQA rows, 27 Russian rows, 19 Kazakhstan rows, seven each in Belarus and Ukraine, six in Vietnam, and five in Japan. Closed-book examination, excerpt study, aggregate recitation requirements, and work-specific memorization have been conflated.

12. **“Absence from one table proves that a country ignores an author.”** Rejected. Absence is meaningful only against equivalent, complete instruments. Several files are incomplete, open formulas do not name the eventual selection, and the age bands differ.

13. **“The asymmetry graph is ready.”** Rejected. Origin labels themselves use different national and linguistic boundaries: British and American English is foreign in the Australian file, British writing is domestic in AQA, Portuguese writing is foreign in Brazil, and Russian-language writers with Ukrainian ties complicate Ukraine. A graph would harden unresolved coding choices into apparent facts.

14. **Any causal or correlation claim.** Rejected by method and by evidence. These lists can establish admission, omission against a valid baseline, and document form; they cannot establish why a ministry chose a work or what that choice caused.

## 4. Country essays richest to write first

1. **Ukraine, then Russia as the adjacent essay.** Ukraine has a separately legible foreign shelf with 39 rows, a mandatory/choice distinction, two retained Russian-language works, and unusually varied genres. Russia supplies the sharp formal contrast: 47 domestic rows and one omnibus foreign choice. Write the essays separately, but let their neighboring placement expose the unequal instruments. Repair Ukraine's two flagged rows, seven memorization disagreements, and the checked era labels first.

2. **Vietnam.** The national document requires representation from eight foreign literary traditions, while the table also records named textbook choices. That creates a rare view of both the rule and possible contents. Its 33 checked era codes and broad grade span must be corrected or kept out of the prose.

3. **Kazakhstan.** Its 27 foreign-origin rows include 21 Russian rows, two Kyrgyz rows, and four English rows; both mandatory and choice shelves are visible. It is the richest imperial-language and neighbor shelf in the current reliable files. The essay should not use the present memorization coding until the 19 disagreements are resolved.

4. **China.** Five named mandatory foreign books form a compact essay, especially because Edgar Snow's outsider account is about China itself. The confirmation pass locally supports four of the five foreign rows and flags Fabre for want of a work-level receipt. This is a manageable verification job before drafting.

5. **Bolivia.** Its 25 foreign anthology rows make a concrete, readable shelf: European classics, Russian novels, and Latin American writing sit together in one textbook instrument. All rows have local support in the confirmation pass, but anthology presence must not be narrated as an exam mandate.

6. **Brazil.** The shelf admits 20 foreign-origin rows, all from the Portuguese-speaking world; two are mandatory in the 2024 FUVEST list and 18 are choices in the broader syllabus material. That language-bounded window is a strong essay, provided the two source layers remain distinct.

7. **Australia.** The NSW list is large, contemporary, multilingual in source, and multimodal; it offers strong errand comparisons and has no hallucination flags. It is a state list for grades 11–12, however, so it sits outside the book's stated 15–16-year-old national unit and should be framed as an explicit federalism/age exception.

Do not draft Belgium, Switzerland, or Norway from the present corpus. Do not lead with Japan or Belarus: Japan's nineteen rows all lack local work-level receipts in the confirmation pass, and twelve Belarus rows appear imported from the Russian file. India can become rich after its twenty receipt flags are resolved. AQA and the United States are valuable institutional essays, but should be written as “board” and “exemplar appendix” cases rather than as national shelves.
