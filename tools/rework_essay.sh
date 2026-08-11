#!/bin/bash
# Rework an essay per the story-spine rule, then force fresh audit + transcheck.
# usage: ./tools/rework_essay.sh <cc> <tsv-base> "<rework instruction>"
set -u
cd "$(dirname "$0")/.."
CC="${1:?}"; TSV="${2:?}"; NOTE="${3:?}"
ESSAY="drafts/$CC.md"
LOG="tools/log/rework-$CC.log"
[ -s "$ESSAY" ] || { echo "rework-$CC FAIL (no essay)"; exit 1; }
before=$(wc -w < "$ESSAY")
echo "[$(date +%H:%M:%S)] rework $CC — opus" | tee -a "$LOG"
timeout 1500 claude --dangerously-skip-permissions --model claude-opus-5 -p "You are the WRITE model for book 10, reworking ONE essay that failed the reader's bar. Read AGENT.md FIRST — especially 'The story-spine rule', which was added after this essay was drafted and is binding. Then read the current $ESSAY, notes/review-$CC.md (audit findings, some may be unapplied), corpus/$TSV.tsv, notes/recon-$TSV.md, and the defining documents in resources/.
READER'S VERDICT ON THIS ESSAY: $NOTE
Rework $ESSAY in place. Keep every verified discovery and every verbatim quote (never alter inside quotation marks — verbatim or gone); the rework changes the VEHICLE, not the cargo. Hold the result against ~/book8/chapters/ register: scene first, documents testify inside the story, citation freight to Receipts, 1,400-2,200 words unless the material honestly earns more. Print a 2-line summary." >> "$LOG" 2>&1
if [ -s "$ESSAY" ] && [ "$(wc -w < "$ESSAY")" -gt 600 ]; then
  rm -f "notes/review-$CC.md" "notes/transcheck-$CC.md"
  ./tools/essay.sh "$CC" "$TSV" "(rework re-audit)" >> "$LOG" 2>&1
  echo "rework-$CC DONE ($before -> $(wc -w < "$ESSAY") words; re-audit: $(head -1 "notes/review-$CC.md" 2>/dev/null | cut -c1-50))"
else
  echo "rework-$CC FAIL"
fi
