# corpus/<country>.tsv — schema (one row per prescribed work)

Columns (tab-separated, header row required):

| column | meaning |
|---|---|
| author | as the document prints it (original script), + transliteration in parentheses if non-Latin |
| title | as the document prints it (original script) + English gloss |
| author_born | year (approx ok, mark with ~) |
| author_died | year, or `living` |
| origin | `domestic` / `translated:<source-language>` — as derivable; mark `doc-marked` if the list itself labels it |
| genre | novel / novella / poem / poem-cycle / play / short-story / essay / epic |
| subject_era | the historical wound or period the work touches (e.g. `WWII-occupation`, `serfdom`, `1930s-famine`, `none/romance`, `antiquity`) |
| exam_status | `mandatory` / `choice-list` / `anthology-only` — per the document's own categories |
| memorize | `yes` / `no` / `excerpt` — is memorization mandated for this work (cite where) |
| grade | the grade/age band the document assigns it to |
| source | URL of the defining document |
| doc_year | version year of the document |
| retrieved | YYYY-MM-DD |
| note | anything the row needs (removals, additions, disputes) — keep short |

Rules:
- A row exists only if the DOCUMENT lists the work; never add "famous" works from memory.
- `subject_era` is the analyst's coding — mark uncertain codings `?` for the second-pass
  blind confirm (book8 pattern: two independent passes, CONFIRMED if they agree).
- Everything else must be literally derivable from the document or the work's standard
  bibliographic record.
- One file per country; the exam year in the filename when systems change fast:
  `ua-2024.tsv`, `ru-2025.tsv`.
