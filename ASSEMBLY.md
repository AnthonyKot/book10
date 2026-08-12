# ASSEMBLY — from reader cuts to the book

This is the site-assembly contract for book10. It begins only after a chapter has a
reader-approved cut in `drafts/reader/`; it does not authorize drafting, research, or
rewriting that cut.

## Authority and order

- **Chapter source:** every assembled chapter page derives from exactly one file in
  `drafts/reader/`. Record that file once in the page head as
  `<!-- source: drafts/reader/<name>.md -->`. This is provenance, not a public citation.
- **Spine:** use `PLAN.md` → **Reading order** as the sole authority for the public
  sequence. The current groups are: *The Poem in Your Body*; the post-Soviet quartet;
  *Three ways to hand a child the world*; *Latin doors*; *The anglosphere paradox*;
  *The Closed Windows* interlude; and *There Is No World Canon*.
- **Index:** when the site front door is assembled, its chapter links must express that
  order. `verify.sh` computes its chapter-count check from those links; never type a
  separate count into the page.

## Assembly pass

1. Confirm that the reader cut is ready and that its proposed place agrees with
   `PLAN.md`'s Reading order. Do not assemble a source that is still a workbench draft.
2. Copy `TEMPLATE.md` into an HTML page in `chapters/`, fill the page metadata and the
   source comment, then move the reader-cut prose into the marked sections without
   changing its claims or adding research.
3. Give the page a stable, ordered filename. Pages that are not sourced in
   `drafts/reader/` do not belong in `chapters/`; keep build notes and temporary work
   outside the public directory.
4. Add the page to the index in the PLAN order and make its previous/next links agree
   with that order once adjacent pages exist. Links to future numbered chapter pages may
   remain stubs and are warnings, not failures.
5. Run `./verify.sh` from the repository root before considering the assembly pass done.

## Page rules carried into HTML

- Preserve the reader cut's concrete opening and its stated limits. The site wrapper
  supplies navigation; it is not an excuse to add a generic introduction.
- Keep the chapter's `##` headings as the page's structural sections where possible.
  The recurring analytic movement is: opening image, the door/instrument, what the
  document permits or requires, the measured shelf, and limits/receipts.
- Put source and methodological detail in a compact receipts/limits section, not in
  parenthetical page-number freight throughout the prose. In particular, chapter bodies
  may not contain `(p. `.
- Use ordinary paragraphs, lists, tables, figures, and a styled quote container when
  needed. Do not use `<blockquote>` in a chapter body; it is reserved out of the public
  pattern so a quotation cannot become an unexamined visual authority.
- Retain the visible limits of the evidence. A reader cut's distinction between a named
  row, a required work, a menu, an exemplar, and an unknown enforcement condition is
  part of its argument.

## Checks and scope

`verify.sh` keeps book8's light approach: ignored private material, local-link checks,
computed index/chapter count, and simple structural-tag balance. It changes the book8
fixed navigation and coda checks because this book's connective pages and its PLAN order
are still being assembled. In their place it checks reader-cut provenance and the two
reader-cut body rules above. It is an assembly guard, not a fact checker or HTML parser.

`chapters/.gitkeep` is the directory sentinel, not an assembled chapter and is excluded
from provenance checks. All other regular files in `chapters/` must be HTML chapter pages
with one valid reader-source comment.
