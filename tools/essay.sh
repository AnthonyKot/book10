#!/bin/bash
# Book10 essay lane: Opus writes -> sol audits -> Opus applies confirmed fixes.
# usage: ./tools/essay.sh <cc> <tsv-base> "<country-specific note>"
set -u
cd "$(dirname "$0")/.."
CC="${1:?}"; TSV="${2:?}"; NOTE="${3:-}"
ESSAY="drafts/$CC.md"
REVIEW="notes/review-$CC.md"
LOG="tools/log/essay-$CC.log"
mkdir -p drafts notes tools/log
[ -s "notes/recon-$TSV.md" ] || { echo "essay-$CC BLOCKED (no recon for $TSV)"; exit 1; }

BRIEF="You are the WRITE model for book 10. Write the $CC country essay to $ESSAY.
Read first, in order: CONTEXT.md (window thesis, method discipline), AGENT.md (the essay
contract — binding), corpus/$TSV.tsv (the repaired table — the ONLY citable rows),
notes/recon-$TSV.md (corrections and quarantined rows), notes/confirm-$TSV.md (caveats
for Limits), and this country's defining documents in resources/ (quote their teaching
language verbatim with location where it serves).
COUNTRY NOTE: $NOTE
Rules that are hard gates: no row counts compared as openness; admission never motive;
author identity written carefully; every number in prose traceable to the table; quotes
verbatim or gone. 1,400-2,200 words (shorter if the shelf is small), markdown, Receipts
and Limits sections per AGENT.md. The canonical voice example is drafts/ua.opus.md —
match its register, do not repeat its devices (vary the lander, vary the close).
Print a 2-line summary when done."

if [ ! -s "$ESSAY" ]; then
  echo "[$(date +%H:%M:%S)] write $CC — opus" | tee -a "$LOG"
  timeout 1500 claude --dangerously-skip-permissions --model claude-opus-5 -p "$BRIEF" >> "$LOG" 2>&1
fi
[ -s "$ESSAY" ] || { echo "essay-$CC FAIL (no draft)"; exit 1; }

if [ ! -s "$REVIEW" ]; then
  echo "[$(date +%H:%M:%S)] audit $CC — sol" | tee -a "$LOG"
  timeout 1200 codex exec --skip-git-repo-check -s workspace-write -C "$(pwd)" --model gpt-5.6-sol "You are the AUDIT model for book 10. Target essay: $ESSAY. Verify it against corpus/$TSV.tsv, notes/recon-$TSV.md, notes/confirm-$TSV.md, the defining documents in resources/, CONTEXT.md (method discipline) and AGENT.md (essay contract). Check: every number in prose against the table; every quote verbatim against the documents; every claim for motive-smuggling, openness-ranking, or wound-map overreach; Limits section honesty. Write $REVIEW: verdict line first (SHIP AS IS / FIX THEN SHIP / REWRITE), then a numbered list of REQUIRED fixes (factual errors, rule violations — each with evidence) and a separate short list of OPTIONAL suggestions. Print a 2-line summary." < /dev/null >> "$LOG" 2>&1
fi
[ -s "$REVIEW" ] || { echo "essay-$CC WARN (no review)"; exit 0; }

if grep -qi "FIX THEN SHIP\|REWRITE" "$REVIEW"; then
  echo "[$(date +%H:%M:%S)] apply $CC — opus" | tee -a "$LOG"
  timeout 1200 claude --dangerously-skip-permissions --model claude-opus-5 -p "You are the WRITE model for book 10, applying an audit. Read $REVIEW, then edit $ESSAY in place: apply every REQUIRED fix; apply OPTIONAL suggestions only where they serve the essay; never alter verbatim quotes except to correct them to the document. Keep the register. Print a 2-line summary." >> "$LOG" 2>&1
fi
./tools/transcheck.sh "$CC" >> "$LOG" 2>&1 || true
V=$(head -1 "$REVIEW" | tr -d '\n' | cut -c1-60)
echo "essay-$CC DONE ($(wc -w < "$ESSAY") words; audit: $V; transcheck: $( [ -s "notes/transcheck-$CC.md" ] && head -1 "notes/transcheck-$CC.md" | cut -c1-60 || echo pending ))"
