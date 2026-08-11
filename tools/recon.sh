#!/bin/bash
# Reconciliation lane (sol): apply blind-confirm findings to one country table.
# usage: ./tools/recon.sh <cc-tsv-basename>   e.g. ua-2024
set -u
cd "$(dirname "$0")/.."
CC="${1:?usage: recon.sh <table-basename>}"
TSV="corpus/$CC.tsv"
CONF="notes/confirm-$CC.md"
OUT="notes/recon-$CC.md"
LOG="tools/log/recon-$CC.log"
[ -s "$TSV" ] || { echo "missing $TSV"; exit 1; }
[ -s "$CONF" ] || { echo "missing $CONF"; exit 1; }
[ -s "$OUT" ] && { echo "recon-$CC SKIP (exists)"; exit 0; }
mkdir -p tools/log

PROMPT="You are the reconciliation editor for book10 (read CONTEXT.md, corpus/SCHEMA.md, and the Method discipline section first). Target: $TSV and its blind-confirm report $CONF, with the defining documents in resources/.

For each disputed item in $CONF:
1. ERA CHECKS: rule on each — reread the row, check the work's actual represented subject (not composition period, not author biography), and EDIT $TSV in place to the correct subject_era value. The rule: subject_era = what the work is about/set in.
2. MEMORIZE: apply this semantic rule everywhere — memorize = yes/excerpt ONLY if the defining document explicitly mandates learning this text (or a stated quantity of texts naizust/by heart/암기) at this level. Closed-book exams, implied quote-learning, and general recitation culture = no. Edit the column accordingly and note the systemic ruling once.
3. FLAGGED (unsupported) ROWS: grep the resources/ documents once more with transliteration variants; if genuinely absent from every saved defining document, MOVE the row out of $TSV into a quarantine section of $OUT (do not silently delete; do not keep in the table).
4. Do not touch undisputed rows. Do not add rows.

Write $OUT: a summary (rows before/after, era edits, memorize edits, quarantined rows), then one line per change (row, old -> new, reason). The table must remain valid TSV (14 columns, tabs). Print a 3-line summary."

echo "[$(date +%H:%M:%S)] recon $CC — sol" | tee -a "$LOG"
timeout 1200 codex exec --skip-git-repo-check -s workspace-write -C "$(pwd)" --model gpt-5.6-sol "$PROMPT" < /dev/null >> "$LOG" 2>&1
if [ -s "$OUT" ] && awk -F'\t' 'NR>1 && NF!=14 {exit 1}' "$TSV"; then
  echo "recon-$CC OK ($(wc -l < "$TSV") rows now)"
else
  echo "recon-$CC FAIL (out: $( [ -s "$OUT" ] && echo present || echo missing ); tsv columns: $(awk -F'\t' 'NR>1 && NF!=14' "$TSV" | wc -l) bad)"
fi
