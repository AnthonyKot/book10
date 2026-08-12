# Cross-country instruments — reconciled corpus, 2026-08-11

This memo reads the 17 populated country files. Belgium, Switzerland, and Norway contain headers only and are not treated as programs returning zero. The unit is the row in the named document, not an equivalent quantity of classroom reading: one row may be a work, a work bundle, an author menu, a national-literature quota, or an open formula. All quarantined material recorded in `notes/recon-*.md` is already outside the TSVs and outside every count below.

## 1. THE ADMISSION MATRIX — foreign-coded works/authors by country

**Counting rule.** A foreign row is a current TSV row whose `origin`, case-insensitively, begins `translated:`. Rows beginning `choice:domestic/translated` are reported separately, because they authorize a foreign choice without naming one. The row fraction uses all data rows in that file as its denominator. “Named people” deduplicates a person within a country, splits an explicitly joint author cell, and counts each country at most once for a person; unknown, anonymous, collective, and open-category keys are shown separately. Russia's single omnibus row is one row but explicitly names four examples, so Homer, Cervantes, Shakespeare, and Molière count as four named people. This is a judgment call; the unbounded “et al.” does not become an author.

| admitting file | foreign-coded rows | named people after identity merge | non-person/open author keys | force of the foreign rows |
|---|---:|---:|---:|---|
| Australia (NSW) | 85 of 140 | 74 | 0 | 85 choice-list |
| Bolivia | 25 of 29 | 23 | 1 unknown-author key | 25 anthology-only |
| Brazil | 20 of 57 | 18 | 1 anonymous-tradition key | 2 mandatory; 18 choice-list |
| Belarus | 39 of 82 | 16 | 1 unknown-author and 1 open-poets key | 35 mandatory; 4 choice-list |
| China | 4 of 69 | 4 | 0 | 4 choice-list |
| Germany (Bavaria) | 0 of 10 | 0 | 0 | 3 additional mixed domestic/translated open rows |
| India | 24 of 43 | 23 | 0 | 24 mandatory |
| Italy | 5 of 10 | 2 | 3 classical author-group keys | 4 mandatory; 1 choice-list |
| Japan | 2 of 15 | 2 | 0 | 2 mandatory |
| Kazakhstan | 27 of 62 | 21 | 0 | 13 mandatory; 14 choice-list |
| Mongolia | 1 of 14 | 1 | 0 | 1 anthology-only |
| Mexico | 0 of 9 | 0 | 0 | 6 additional mixed domestic/translated open rows |
| Russia | 1 of 48 | 4 named examples | 1 open remainder (“et al.”) | 1 choice-list |
| Ukraine | 39 of 57 | 39 | 0 | 13 mandatory; 26 choice-list |
| UK (AQA) | 0 of 73 | 0 | 0 | no foreign-coded row |
| United States | 22 of 63 | 21 | 0 | 22 choice-list |
| Vietnam | 29 of 107 | 20 | 1 Greek-myth tradition and 8 national-literature author groups | 29 choice-list |

These are row descriptions, not a ranking of windows. In particular, 85 NSW options, 25 anthology entries, 24 mandatory Indian reader entries, and one Russian omnibus option are unlike objects.

**Identity merge.** I preferred the Latin transliteration in parentheses, case-folded it, removed initials and punctuation for matching, and reversed surname-first Latin forms. I then manually joined transliteration variants only where the birth/death fields and names made the identity unambiguous. The merges that affect the cross-country leaders are: `Shakespeare, William` / `William Shakespeare` / `W. Shakespeare` / `У. Шекспир` / `Вільям Шекспір`; `Nikolai` / `Nikolay Gogol` and their Cyrillic forms; `Homer` / `Omero` / `Гомер`; the Cyrillic and Latin forms of Isaac Asimov, Ray Bradbury, Anton Chekhov, Robert Frost, Henrik Ibsen, and Jonathan Swift. Within Kazakhstan I also merged `Ч. Айтматов` and `Ч.Т. Айтматов` as Chingiz Aitmatov, and `Alexander` / `Aleksandr Kuprin`; those are the same people, not extra admissions. I did not merge merely similar surnames, author groups, or an unattributed work into a famous conventional author.

With the same foreign-row filter, William Shakespeare is the most widely admitted named person: Australia, Bolivia, Kazakhstan, Russia, Ukraine, the United States, and Vietnam — seven of the 17 populated files. Russia counts because its one foreign row names him as an example; without example-splitting he is in six of 17. Homer and Nikolai Gogol are each admitted by four of the 17: Homer by Italy, Russia, the United States, and Vietnam; Gogol by Belarus, Kazakhstan, Ukraine, and the United States. Isaac Asimov, Ray Bradbury, Anton Chekhov, Robert Frost, Henrik Ibsen, and Jonathan Swift are each admitted by three of the 17.

## 2. THE SHARED SHELF vs THE NATIONAL-POET SLOT

**Counting rule.** For the shared shelf, an author is counted once per country under the Section 1 identity rule. A work is counted once per country when the title or English gloss identifies the same work; a bundled or `OR` option counts as admission but is flagged below, and generic “sonnets,” “Homeric epics,” or unnamed oeuvre rows are not forced into a specific-work match. For the national-poet test, only `origin` beginning `domestic` is inspected. A clear occupant requires the table itself to distinguish one named author from domestic peers by repeated rows, a uniquely large named bundle, or repeated rows explicitly centered on that author. This operational test identifies a table slot; it does not declare anyone the country's true national poet.

There is a small shared shelf, but these files do not produce a de-facto world canon common to them. Shakespeare reaches seven of 17 files as an author, yet the objects differ: six NSW plays, Bolivian *Hamlet*, Kazakh sonnets and *Romeo and Juliet*, a Russian open example, Ukrainian sonnet choice, U.S. *Macbeth* and “Sonnet 73,” and Vietnamese *Romeo and Juliet*. No unambiguous work reaches more than three of the 17. The three-work shelf at that count is:

- *A Doll's House*: Australia, Ukraine, and the United States — three of 17.
- *Gulliver's Travels*: Australia, Bolivia, and Ukraine — three of 17; Ukraine prescribes Part I.
- *The Overcoat*: Belarus, Kazakhstan, and Ukraine — three of 17; in Ukraine it is one side of a Gogol `OR` choice.

The “exactly one non-exportable national poet” proposition does not survive the tables. The country-by-country result is:

| file | table-supported occupant? | what the domestic rows actually support |
|---|---|---|
| Australia (NSW) | none singled out | Oodgeroo Noonuccal, Tim Winton, and Helen Garner each occupy two of 55 domestic rows. |
| Bolivia | none singled out | each of the four domestic author keys occupies one of four domestic rows. |
| Brazil | none singled out | Machado de Assis, Graciliano Ramos, Carlos Drummond de Andrade, and João Guimarães Rosa each occupy two of 37 domestic rows. |
| Belarus | **Yanka Kupala** | six of 43 domestic rows, more than any other named domestic author; one of the six is on the explicit memorization list. |
| China | none singled out | anonymous works occupy five of 65 domestic rows; Du Fu and Su Shi each occupy three; Lu Xun occupies one. Calling Lu Xun the slot would come from outside this table. |
| Germany (Bavaria) | none singled out | the literary selections are open formulas; the two named domestic people are communication theorists. |
| India | none singled out | every named domestic author occupies one row in the 19-row domestic shelf. |
| Italy | none singled out | Dante is absent from the Italian file. Manzoni is its only named modern domestic individual, but that alone does not establish a national-poet office. |
| Japan | none singled out | every domestic author key occupies one of the 13 domestic rows; Bashō has one. |
| Kazakhstan | **Abai, with a judgment flag** | one row is by Abai, while *On Abai's Land*, *Path of Abai*, and *Great Poet of Kazakhs* make four of 35 domestic rows directly about his work or legacy. This is thematic centering, not a four-row authorship count. |
| Mongolia | none singled out | Mongolian oral tradition has two rows; every named person has one. |
| Mexico | none singled out | the three domestic rows are unnamed author/tradition formulas. |
| Russia | **Alexander Pushkin** | five of 47 domestic rows, ahead of Lermontov's four and Gogol's three. |
| Ukraine | **Taras Shevchenko, with a bundle flag** | one of 18 domestic rows bundles five Shevchenko works. The row is the largest clear single-author domestic bundle, but row counting alone does not distinguish him because every named domestic author has one row. |
| UK (AQA) | **William Shakespeare** | six of 73 domestic rows, ahead of Shelley's three. |
| United States | none singled out | Lincoln and Martin Luther King Jr. each have two of 41 domestic rows; every other author key has one. |
| Vietnam | none singled out | Nguyễn Trãi, Nguyễn Đình Chiểu, and Nam Cao each have three domestic rows; Nguyễn Du has two. |

Belgium, Switzerland, and Norway cannot be tested from header-only files. Nor is “non-exportable” a stable description: Pushkin is foreign-coded in Belarus and Kazakhstan; Shakespeare in seven files; Lu Xun in Japan and Vietnam; and Dante in Ukraine. Conversely, absence elsewhere is not proof of non-exportability when several documents leave authors unnamed.

## 3. THE ENEMY SHELF

**Counting rule.** This section uses only current rows whose `origin` is exactly the relevant source-language code: `translated:Russian (doc-marked)` in Ukraine and `translated:russian` in Kazakhstan. It reports titles, document status, and table notes. “Adversary” is the question supplied to the instrument, not a motive inferred from a row.

**Ukraine.** Two of Ukraine's 39 foreign-coded rows are Russian-coded, and both are choice-list rows: Gogol's *The Government Inspector* **or** *The Overcoat*, and Bulgakov's *Heart of a Dog*. The Gogol note states “retained Russian-language work due to author's Ukrainian origin.” The Bulgakov note states “retained Russian-language work due to author's Kyivan birth and anti-totalitarian satire.” Thus the post-2022 slice shows two retained options on the table's stated Ukraine-connection grounds. It does not, by itself, show which other works were removed.

**Kazakhstan.** Twenty-one of Kazakhstan's 62 rows are Russian-coded; they are 21 of its 27 foreign-coded rows. Twelve of the 21 are mandatory and nine are choice-list. The 21 rows name 17 normalized authors: Pavel Vasilyev; Alexander Pushkin; Ivan Turgenev; Aleksandr Kuprin; Nikolai Gogol; Fyodor Dostoevsky; Leo Tolstoy; Alexander Griboyedov; Anton Chekhov; Nikolai Leskov; Konstantin Paustovsky; Mikhail Svetlov; Maxim Gorky; Viktor Astafyev; Mikhail Lermontov; Yevgeny Yevtushenko; and Vasily Yan. That is what the file shows. The table supplies no motive for the shelf.

No broader enemy-shelf inventory is claimed. Political-adversary status is not a TSV field, and the other Russian-language admissions in Belarus, China, India, the United States, and Vietnam are not converted into geopolitical cases by this instrument.

## 4. WINDOW ASYMMETRY

**Counting rule.** The direction `A → B` means: A has at least one foreign-coded named author assigned to B, while B has no foreign-coded named author assigned to A. It does **not** mean that no classroom in B can read A. The test uses only the 17 populated files, excludes source countries outside that set, counts a named author once, and treats mixed/open formulas as unnamed rather than as zero permission. Country assignment is not a TSV column, so each pair below gives a witness. I used the author's primary national-literature association where it is unambiguous and explicit national-literature quotas where the row supplies one; I did not equate source language mechanically with country.

| admitting A | B for which the reverse named admission is absent | witness in A's foreign rows |
|---|---|---|
| Australia | Italy; UK | Italo Calvino; William Shakespeare |
| Bolivia | Germany; Russia; UK; United States | Goethe; Dostoevsky; Shakespeare; Poe |
| Belarus | Russia; United States† | Pushkin; Isaac Asimov |
| China | Russia; UK; United States | Nikolai Ostrovsky; Charlotte Brontë; Edgar Snow |
| India | Mexico; Russia; UK; United States | Gregorio López y Fuentes; Chekhov; Frederick Forsyth; Robert Frost |
| Japan | China | Lu Xun |
| Kazakhstan | Russia; UK; United States | Pushkin; Shakespeare; Ray Bradbury |
| Mongolia | India† | Kalidasa |
| Russia | UK | Shakespeare, named inside the omnibus example row |
| Ukraine | Australia; Germany; Italy; Japan; Russia‡; UK; United States | Markus Zusak; Goethe; Dante; Akutagawa; the two Russian-coded rows; Shakespeare; Bradbury |
| United States | Russia; UK | Gogol; Shakespeare |
| Vietnam | China; India; Japan; Russia; UK; United States | Lu Xun/Chinese-literature quota; Indian-literature quota; Kawabata/Japanese-literature quota; Chekhov/Russian-literature quota; Shakespeare/English-literature quota; Frost/American-literature quota |

Australia–India and Australia–United States are reciprocal under this rule: Australia names Aravind Adiga and U.S. authors; India names Australian Robin Klein; and the United States names Australian Markus Zusak. They are therefore not in the directed list.

Judgment flags: † assigns the Russian-born, English-language American writer Asimov to the United States and the premodern Sanskrit dramatist Kalidasa to Indian literature. Dropping either assignment drops only that marked pair. ‡ uses Ukraine's own `translated:Russian` coding for Gogol and Bulgakov while preserving the table's Ukraine-connection notes; it is a source-shelf assignment, not a verdict on either author's identity. I excluded Australia → Germany: its two `translated:german` rows are Kafka and Fritz Lang, for whom turning language into present-day country would decide a transnational identity question. The same conservative rule excludes premodern Greek and Roman authors from modern-country dyads. Open German, Italian, and Mexican formulas mean “no named reverse admission,” not “no possible reverse reading.”

## 5. THE MEMORIZATION INVENTORY

**Counting rule.** Select every current TSV row with `memorize` exactly `yes` or `excerpt`; do not infer memorization from `mandatory`, a closed-book exam, quotation use, recitation culture, or an aggregate outcome that names no work. Apply the filter after reconciliation and quarantine. It returns 23 rows, all in three of the 20 country files.

### Belarus — six rows

| value | side | author | row title |
|---|---|---|---|
| yes | domestic | Yanka Kupala | *Sycamore and Guelder-Rose* |
| excerpt | domestic | Yakub Kolas | *New Land* — “The Forester's Place” excerpt |
| yes | domestic | Maksim Tank | *You Are Still Only a Hint of a Human...* |
| yes | domestic | Yauheniya Yanishchyts | *Call Me. Summon Me...* |
| excerpt | Russian-coded foreign | Alexander Griboyedov | *Woe from Wit* — Famusov or Chatsky monologue |
| excerpt | Russian-coded foreign | Alexander Pushkin | *Eugene Onegin* — three excerpts |

Four of Belarus's six work-specific memorization rows are domestic and two of six are foreign-coded.

### Kazakhstan — twelve rows

| value | side | author | row title |
|---|---|---|---|
| excerpt | English-coded foreign | William Shakespeare | *Sonnets* |
| excerpt | Russian-coded foreign | Pavel Vasilyev | *And Your Name...* and other poems |
| excerpt | Russian-coded foreign | Alexander Pushkin | lyric poetry and *The Gypsies* |
| excerpt | Russian-coded foreign | Ivan Turgenev | *Asya* |
| excerpt | Russian-coded foreign | Aleksandr Kuprin | *Olesya* |
| excerpt | Russian-coded foreign | Nikolai Gogol | *The Overcoat* |
| excerpt | Russian-coded foreign | Fyodor Dostoevsky | *Poor Folk* |
| excerpt | Russian-coded foreign | Leo Tolstoy | *After the Ball* |
| excerpt | Russian-coded foreign | Aleksandr Kuprin | *The Garnet Bracelet* |
| excerpt | Russian-coded foreign | Alexander Pushkin | *The Queen of Spades* |
| excerpt | Russian-coded foreign | Anton Chekhov | *Ionych* or *The Man in the Case* |
| excerpt | Russian-coded foreign | Nikolai Leskov | *The Pearl Necklace* |

All twelve of Kazakhstan's twelve work-specific memorization rows are foreign-coded: eleven are Russian-coded and one is English-coded. None of its 35 domestic rows passes the filter.

### Ukraine — five rows

| value | side | author | row title |
|---|---|---|---|
| yes | German-coded foreign | Heinrich Heine | *Book of Songs* selections |
| yes | Italian-coded foreign | Dante Alighieri | “In Her Eyes She Carries Love” |
| yes | Italian-coded foreign | Francesco Petrarch | Sonnet 61 or 132 |
| yes | English-coded foreign | William Shakespeare | Sonnet 116 or 130 |
| yes | Romanian-coded foreign | Mihai Eminescu | *To Bukovina* |

All five of Ukraine's five work-specific memorization rows are foreign-coded. None of its 18 domestic rows passes the filter.

Russia has no row passing the filter: zero of 48. Its codifier requires expressive reading of at least twelve works or fragments and includes reading by heart, but it identifies neither how many must be memorized nor which named works; the reconciliation therefore leaves all 48 rows at `no`. China, Japan, the UK AQA file, and Vietnam were corrected on the same work-specific principle. No other country file contains `yes` or `excerpt` after reconciliation.

## 6. WHAT THIS CORPUS CANNOT SUPPORT

**Counting rule.** None: this is the refusal register. A claim is refused when it requires comparable exposure, a missing time series, classroom behavior, causal evidence, or a category not encoded in the reconciled rows.

- **No openness ranking or cross-country “window size” metric.** Rows are not commensurate. A named mandate, an anthology TOC entry, a state choice menu, a national-literature quota, and an omnibus/open formula do not measure equal quantities.
- **No claim that a row was actually taught, read in full, memorized in practice, or encountered by a stated number of pupils.** The tables describe document admission, not classroom uptake.
- **No national-system zero from an empty or open file.** Belgium, Switzerland, and Norway are header-only. Germany and Mexico permit translated choices without naming them. AQA is one English board, NSW one Australian state, and the U.S. file an exemplar appendix.
- **No universal de-facto canon, and no proof that every country installs exactly one national poet.** The instrument can group repeated names and table-centered domestic figures; it cannot turn seven Shakespeare admissions or a bundled Shevchenko row into a universal institutional law.
- **No unqualified author-nationality graph.** `origin` codes source language, not citizenship or literary nationality. Gogol, Bulgakov, Asimov, Kafka, Lang, Conrad, Ishiguro, Aitmatov, ancient authors, and diaspora writers expose the mismatch. Section 4 therefore publishes its assignments and exclusions.
- **No political motive from the enemy shelf.** The current rows establish admission and the wording of Ukraine's two retention notes. They do not establish friendship, hostility, coercion, inheritance, approval, resistance, or any other cause.
- **No post-2022 removal count or reform trend.** Ukraine's current slice shows what remains; removals require a prior list and dated revision receipts. One-year files cannot establish direction of change.
- **No memorization comparison beyond named work-level mandates.** Aggregate by-heart outcomes, closed-book assessment, quotation requirements, expressive reading, and anthology presence are different document acts and remain different.
- **No period, genre, wound, gender, correlation, significance, or trend claim from these instruments.** `subject_era` is analyst coding; some rows bundle genres and eras; the documents and grades differ; and the method discipline forbids correlation and derived metrics.
- **No causal “errand” for an imported author from admission alone.** What a work is for requires close reading of the corrected work and the document's teaching language, not an inference from nationality or row count.

## Four-line summary

1. Shakespeare is foreign-admitted by seven of the 17 populated files; Homer and Gogol by four of 17 each.
2. No unambiguous work is foreign-admitted by more than three of 17, and most files do not single out exactly one domestic national-poet occupant.
3. Ukraine retains two Russian-coded choice rows, while Kazakhstan contains 21 Russian-coded rows; the tables establish admission, not motive.
4. The work-specific memorization filter returns six Belarusian, twelve Kazakhstani, and five Ukrainian rows; Russia returns none.

## Addendum 2026-08-12 — reconciliation with the RU rebuild (corpus/ru-frp-2024.tsv)

Sections 5 and the four-line summary above were computed while the Russia file was the
ЕГЭ-codifier table, which the reader ruled the wrong document (the exam door, not the
taught door). The replacement table `corpus/ru-frp-2024.tsv` (federal working program,
40 rows, confirmed and reconciled) changes one instrument:

**§5 THE MEMORIZATION INVENTORY — updated result.** Applying the same counting rule
(`memorize` exactly `yes` or `excerpt`, after reconciliation, no inference from
aggregates) to the current tables returns **27 rows in four country files**:

### Russia — four rows (new)

| value | side | author | row title |
|---|---|---|---|
| yes | domestic | Unknown author | «Слово о полку Игореве» |
| yes | domestic | M.V. Lomonosov | Ода на день восшествия… (1747 ode) |
| yes | domestic | A.S. Griboyedov | «Горе от ума» |
| yes | domestic | N.V. Gogol | «Мёртвые души» |

All four of Russia's work-specific memorization rows are domestic. (The program's
separate aggregate recitation floor — poems by heart with no work named — remains
excluded by the counting rule, as all aggregates are.)

**The memorization triangle, corrected.** Sixteen of the twenty country files sign no
named text into memory; four do — Russia (4 of 4 domestic), Kazakhstan (12 of 12
foreign-coded), Ukraine (5 of 5 foreign-coded), Belarus (4 of 6 domestic, 2 of 6
Russian-coded). Summary line 4 above is superseded accordingly; lines 1–3 are
unaffected (the codifier's foreign rows and the FRP's foreign rows do not change the
per-work admission maxima).

## Addendum 2, 2026-08-12 (late) — §2 recount against corpus/ru-frp-2024.tsv

The first addendum asserted that summary lines 1–3 were unaffected by the RU rebuild.
Line 2's work-level maximum WAS affected: the FRP names foreign works that the retired
codifier's single omnibus row did not. Recounted under §2's own rules (work counted
once per country when title or gloss identifies the same work; bundles and OR options
count as admission; generic oeuvre rows not forced into a specific-work match; Russia =
ru-frp-2024.tsv; ru-2025.tsv retired):

- **Author counts unchanged.** Shakespeare 7 of 17 (au bo kz ru ua us vn) — now
  without the example-splitting judgment call: the FRP holds three named Shakespeare
  rows (Sonnets, one-two by choice; *Romeo and Juliet*, fragments, mandatory; *Hamlet*,
  fragments, mandatory). Homer 4 of 17 (it ru us vn; the FRP row is *Iliad*/*Odyssey*
  fragments, mandatory). Gogol foreign-coded 4 of 17 (by kz ua us; domestic in ru).
- **Work-level maximum is now FOUR of 17, not three:** *Gulliver's Travels* —
  Australia (choice-list, whole work), Bolivia (anthology-only), Ukraine (Part 1,
  mandatory, grade 9), Russia (chapters by choice, mandatory, grade 6). No other work
  reaches four. Verified at three of 17 under the same rule: *A Doll's House* (au ua
  us), *The Overcoat* (by kz ua), *Romeo and Juliet* (kz ru vn — the UK AQA row is
  domestic-coded and excluded from the foreign shelf), *Hamlet* (au bo ru), *Robinson
  Crusoe* (bo ru vn), Homer's *Odyssey* (ru fragments, us, vn — Italy's "Homeric
  poems" bundle not forced to the specific work).
- **§2 national-poet Russia row, recomputed on the FRP:** Pushkin 3 domestic rows;
  Lermontov 2; Lomonosov 2. Occupant retained, margin narrowed (the "5 of 47" figure
  belonged to the retired codifier table).
- **Stale-report warning:** `notes/window-report.md` predates both the RU rebuild and
  the BY reconciliation; it still shows a Belarus Hamlet/sonnets row that is no longer
  in `corpus/by-2024.tsv` (0 Shakespeare rows of its current 82) and shows Russia as
  the codifier omnibus. Do not cite it for counts.
