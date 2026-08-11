#!/usr/bin/env bash
# Book10 table-izer: agy turns one country's official canon document into corpus TSV.
# usage: ./tools/build_canon.sh <country-id> <output-tsv-name>   e.g. ru ru-2025.tsv
set -u
cd "$(dirname "$0")/.."
CID="${1:?usage: build_canon.sh <country-id> <out.tsv>}"
OUTNAME="${2:?}"
OUT="corpus/$OUTNAME"
LOG="tools/log/build-$CID.log"
mkdir -p corpus resources tools/log
if [ -s "$OUT" ] && [ "$(wc -l < "$OUT")" -gt 10 ]; then
  echo "build-$CID SKIP (exists, $(wc -l < "$OUT") rows)"; exit 0
fi

SCOUT=$(cat notes/scout-canon.md notes/scout-canon2.md 2>/dev/null | awk "/^### .*\\($(echo "$CID" | tr a-z A-Z)/,/^### [0-9]/" | head -60)

PROMPT="You are building one country's corpus table for book10 (read CONTEXT.md and corpus/SCHEMA.md in this directory first — they define the project and the exact TSV schema).

COUNTRY: $CID. The scout already located the defining document:
---
$SCOUT
---

YOUR TASK:
1. Using your google/web tools, locate and download the actual defining document (the exam codifier / set-text specification named above) into resources/ (any format). If a direct file is unreachable, use the official page's own listing — but record exactly which URL each fact came from.
2. Extract the prescribed works for the 15-16-year-old exam level and write $OUT as a tab-separated table following corpus/SCHEMA.md EXACTLY (header row, all columns, tabs not spaces).
3. HARD RULE: a row exists ONLY if the document lists the work. Do not add famous works from your own knowledge. If the document names an author with 'poems (by choice)' or similar open formulas, make ONE row with title as the document's own formula.
4. subject_era codings you are unsure of get a trailing '?' (second blind pass will confirm).
5. memorize column: only 'yes'/'excerpt' if a mandate is written somewhere you can cite (note where in the note column); otherwise 'no'.
6. When done, print ONLY: the row count, the domestic/translated split, and any work you EXPECTED to find but the document does not list (that absence is data).

Anti-leak: downloaded documents stay in resources/ (never committed). The TSV is facts and is committable."

ENGINE="${ENGINE:-agy}"
run_agent() {
  if [ "$ENGINE" = "codex" ]; then
    timeout 1000 codex exec --skip-git-repo-check -s danger-full-access -C "$(pwd)" --model "${CODEX_MODEL:-gpt-5.6-terra}" "$PROMPT" < /dev/null >> "$LOG" 2>&1
  else
    timeout 1000 agy --dangerously-skip-permissions --print-timeout 14m --model gemini-3.6-flash-high -p "$PROMPT" >> "$LOG" 2>&1
  fi
}
echo "[$(date +%H:%M:%S)] build $CID — $ENGINE" | tee -a "$LOG"
run_agent
if [ -s "$OUT" ] && [ "$(head -1 "$OUT" | grep -c $'\t')" -eq 1 ] && [ "$(wc -l < "$OUT")" -gt 10 ]; then
  echo "build-$CID OK ($(wc -l < "$OUT") rows)"
else
  echo "build-$CID RETRY" | tee -a "$LOG"
  run_agent
  if [ -s "$OUT" ] && [ "$(wc -l < "$OUT")" -gt 10 ]; then echo "build-$CID OK-2 ($(wc -l < "$OUT") rows)"
  else echo "build-$CID FAIL"; fi
fi
