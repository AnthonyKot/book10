# Book 10 — resume runbook (stopped 2026-08-11 ~13:50, Opus session limit)

State at stop (all committed):
- 20/20 corpus tables · 20/20 confirms · **17/17 recons** (be/ch/no are empty by design —
  nothing to reconcile; the recon loop is finished, do not re-run it)
- Essays: ua ✅ · vn ✅ · bo ✅ · **ru ✅ reworked** (4,017 → 2,524 words; audit applied;
  transcheck 25/25 faithful) · **kz ✗ NOT reworked** · **cn ✗ NOT reworked**

## What happened to kz (read before re-running it)

The kz rework completed its write (a 3,190-word draft) and cleared transcheck 43/43
faithful, but the Opus **apply** step hit the account session limit and never applied the
audit. The reworked draft was then destroyed by a `git checkout drafts/kz.md` during
cleanup. `drafts/kz.md` is back to the ORIGINAL pre-rework 3,621-word version, and
`notes/review-kz.md` + `notes/transcheck-kz.md` were restored to the matching pair.

**`notes/review-kz.LOST-REWORK.md` is the audit of the destroyed draft.** Its line
references are dead but its findings are real and were NOT the same as the old audit's.
Feed them into the next kz rework as known traps:
1. Not every omitted foreign work is Russian — Aitmatov's «Плаха» is `translated:kyrgyz`
   under this corpus's own convention (kz-2023.tsv rows 53, 63).
2. Row counts are rows, not works — single rows bundle works (Pushkin lyric + «Цыганы»;
   Chekhov's two teacher-choice stories). Say "rows"/"list entries", and never let
   `translated:*` imply the classroom copy is a translation.
3. Identity facts used in prose (Gundarev Russian-writing, Gogol Ukrainian-born, Asimov
   American) are not in the TSV — receipt them or cut them; Limits must not deny them.
4. **The errand close-read beat was still missing** — comparing quarter headings is not a
   close-read. Read one listed work from a named edition.
5. «типовые учебные программы» in that nominative plural form is not in the document.

## Restart (in order)

1. Reworks still owed — `tools/run_rework2.sh` has all three lines; **delete the ru line
   first** (ru is done; the script is NOT self-skipping and would redo it):
   ./tools/rework_essay.sh kz kz-2023 "<kz note + the five traps above>"
   ./tools/rework_essay.sh cn cn-2024 "<cn note from run_rework2.sh>"
   Never re-rework ua/vn/ru — drift.
2. Reading artifact — MUST be updated with the existing `url` parameter or it mints a new
   address: https://claude.ai/code/artifact/19db3f88-5cfe-43fa-a6e6-fe44bc68f0e9
   Content: ua, vn, bo + ru (ready now), then kz, cn when they clear.
3. Two questions for the reader, still unanswered (they are the BY native witness —
   the Belarus essay is blocked on both):
   (a) Was Русская литература a separate subject with its own hours? This decides the
       essay's door type: by-2024.tsv has 43 domestic vs **37 translated:russian** rows,
       and if that shelf was its own subject it is a second national shelf, not a window.
   (b) What did they memorize by heart at school? (by-2024.tsv records only 3 yes +
       3 excerpt out of 82 rows — the document is close to silent here.)
   Ask (b) WITHOUT offering options — it is witness testimony, not a menu.
4. Also for the reader's verdict: essays keep landing at 3–4k words against a 2,200 cap.
   Earned, or enforce the cap in essay.sh? Their answer calibrates wave 2.
5. Then wave 2: in jp mx br au us uk it de mn, + be/ch/no as door-essays from their
   source ledgers. All their tables are now reconciled, so all are unblocked.

## Non-Opus work available when Opus is rationed (agy/codex are separate quota)

- sol: the cross-country instruments, now that 17/17 tables are reconciled for the first
  time — admission matrix (foreign authors × countries), shared shelf vs national-poet
  slot, enemy shelf, window asymmetry. `notes/window-report.md` predates 7 of the tables.
- sol: the memorization inventory across all 20 tables (the best-chapter candidate).
- terra: fetch/rebuild any thin wave-2 defining documents in resources/.
- Method discipline holds for all of it: grouping and plain fractions, no correlation
  analysis, 1–2 conclusions max.

Engines: Opus writes (claude CLI) · sol audits (codex, workspace-write — never read-only)
· terra fetches (codex danger-full-access) · agy transchecks (size-check the output).
resources/ and tools/log/ stay untracked. Commit per milestone.
