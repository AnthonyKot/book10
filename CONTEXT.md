# Book 10 — CONTEXT (design seed)

**The Window.** (working name; was "The Ministry of Feeling") Every school system opens
a window on the world's literature — and the comparable decision is not the domestic
canon (each country reading its own classics is mere difference) but the FOREIGN slice:
**out of all of world literature, which outsiders does each country admit into its
classroom, and what does the choice say?** (Reader decision 2026-08-10: domestic rows
are context; the window is the subject.)

The pilot already measured the variance: Russia's window at exam level is ONE optional
row ("works of foreign literature, by choice — including Homer, Cervantes, Shakespeare,
Molière et al."); England's GCSE window is closed by the subject's own name ("English
Literature"); Ukraine runs an ENTIRE SEPARATE SUBJECT — «Зарубіжна література» — a
whole ministry program of nothing but foreign works. Window sizes differ by two orders
of magnitude, and that variance is the book.

Core instruments:
- **The admission matrix**: rows = foreign authors, columns = countries. Who is the
  most-admitted author in the world's classrooms? Is there a de-facto world canon, and
  who defines it? (The convergence control of this book.)
- **The enemy shelf**: which countries assign their adversaries' literature — does UA
  still list any Russian authors (post-2022 removals are documented, receipted,
  datable); does RU list Shevchenko; does anyone assign both sides of their own wars?
- **The errand**: what each admitted foreigner is FOR — the feeling a country cannot
  source domestically and imports instead (which Dickens each country picks, which
  Remarque, whose anti-war novel).
- **Window asymmetry**: A admits B's authors while B ignores A's — a directed graph of
  literary respect, computable from the tables.

## The rigor problem, solved up front

Whole novels cannot be a corpus (scale, copyright, translation). The fix:

**The unit of analysis is the LIST, not the novel.** Every school system produces an
enforceable document — the exam codifier (RU: кодификатор ЕГЭ/ОГЭ), the set-text list
(UK: GCSE exam-board specifications), the ministry program (UA: МОН list; BY; KZ), the
state anthology (CN: the 语文 textbook's fixed selections; IN: NCERT readers), the
maturità/Abitur traditions (IT, DE — where federalism itself becomes a finding), or the
absence of any national list (US — the market classroom has no ministry; district lists
and AP suggestions replace it, and THAT is a column-defining finding, same role as the
US market textbook played in book 8).

Operational definition: **a country's canon = what a 15–16-year-old can be examined on,
per the official document of a named year.** One row per work: author · title · author's
century · domestic or translated (from where) · genre · subject era (what historical
wound it touches) · memorization required? · source URL + retrieval date. The corpus is
a set of tables with receipts, exactly as auditable as book 8's page numbers.

**Two-layer corpus:**
1. `corpus/<country>.tsv` — the list-as-data (facts; committable; each row sourced).
2. The excerpt shelf — what the anthology actually PRINTS (canons teach excerpts, and
   which pages of a novel a ministry excerpts is itself an editorial act). Most core
   canon texts are 19th-century public domain; modern works quoted under normal short
   quotation. Any gathered curriculum PDFs live in `resources/` — anti-leak rules as
   book 8, never tracked, never published.

## Thesis candidates (pilot decides)

- Textbooks nationalize facts; canons nationalize *feelings*. The reading list is where
  a state decides which sorrows are load-bearing.
- The wound test: for each of book 8's events (war, famine, occupation, revolution),
  which countries assign a NOVEL about it, and whose novel. Cross-book finding: the same
  event measured in history-space (book 8) and in feeling-space (book 10).
- The convergence control (as book 8's colonial row): which works appear in MANY canons
  (Shakespeare? Antigone? — the shared shelf) vs the national-poet slot every country
  fills with exactly one non-exportable figure (Shevchenko, Pushkin, Mickiewicz, Dante,
  Goethe, Lu Xun…). Same office, never the same person — eleven ministries of feeling
  with identical org charts.

## Measurable axes (all computable from the tables)

space (share of the list) · domestic vs translated share, and WHOSE literature gets
admitted · century distribution (how old is each nation's "we") · gender of the canon ·
subject-era distribution (which wounds get literature) · the memorization mandate
(WHICH poem a nation makes children learn by heart — possibly the book's best chapter
and its strongest lander: every reader was made to memorize something at 15) ·
list-reform history (datable rupture events: UA's removals after 2022, RU codifier
changes, CN anthology revisions — curriculum reform as a receipted historical event) ·
the overlap matrix across countries.

## Landers (cup-of-tea rule inherits from AGENT.md, book 8)

The reader HAS a canon in their past — the forced book, the memorized stanza, the
summer reading list, the anthology's smell. Chapters land there by construction. Tagged
regional landers ("If your classroom made you memorize…") as in book 8.

## Method discipline (reader ruling, 2026-08-10)

**No correlation analysis on this corpus.** The tables are one-year slices of unlike
documents (codifier vs spec vs anthology TOC); statistics over them would be pseudo-
rigor. The corpus's job is proper GROUPING — period × genre × who-admits — so that a
careful reading (LLM-assisted, human-judged) can make meaningful comparisons and draw
at most one or two conclusions that survive scrutiny. Counts may be stated as plain
facts ("admitted by four of the seven programs"); no derived metrics, no significance
language, no trend claims from two data points. Same spirit as book8's rule: the
instrument proves underweighting/admission, never causes.

## Voice & rules

All book 8 rules inherit: quotes verbatim or gone (works quoted from named editions;
lists quoted from named documents with URL + date), banned registers, causal precision,
findings as human sentences with arithmetic under the floorboards, symmetric omission
grading (a work absent from one canon is a finding only against the corpus baseline).
Narrator: the twelfth-narrator stance carries over — the AI reader took no country's
literature class, memorized nobody's poem.

## Structure (reader decision 2026-08-10)

**One essay per country.** Each chapter = one nation's window: what it admits, what
errand each admitted foreigner runs, how the window changed (datable reforms). The
cross-country instruments (admission matrix / shared shelf, enemy shelf, window
asymmetry) live in connective chapters or an interlude, book8-style. Light chapters
and heavy chapters may differ in length — an essay earns its pages.

## Countries

Wave 1 (book 8's narrator set): BY RU UA CN IN DE IT UK US + KZ (+ SD if findable).
Wave 2 (reader picks, 2026-08-10): MX BO BR VN JP MN BE AU CH(Switzerland) NO —
chosen for spread: Latin America ×3, Asia ×3 (incl. post-Soviet Mongolia), and three
multilingual/federal windows (Belgium, Switzerland, Australia's state lists) that test
"one country, several windows." DE/BE/CH federalism and US no-ministry are findings,
not obstacles.

## Harness (to build as the pilot demands)

- `tools/scout_canon.sh` — agy googles the official document per country: exact name,
  issuing body, year, URL, format; notes/scout-canon.md. (First run: tonight.)
- `tools/fetch + parse` per country → `corpus/<country>.tsv` (schema above). Manual
  spot-verification against the printed document before any chapter cites a row.
- Analysis scripts over the TSVs: overlap matrix, translated share, century histogram,
  wound map. All mechanical, book8-space-matrix style.

## Status log

- 2026-08-10: folder + design seed created; rigor operationalization decided (list =
  unit, exam-codifier definition, two-layer corpus); canon-document scout launched on
  agy. No corpus rows, no chapters yet.
