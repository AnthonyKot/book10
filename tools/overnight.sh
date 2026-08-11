#!/bin/bash
# Overnight orchestrator: finish corpus -> verify -> grouped manual -> conclusions draft.
cd /home/diablo/book10 || exit 1
LOG=tools/log/overnight.log
log() { echo "[$(date +%H:%M:%S)] $*" >> "$LOG"; }

# 1. wait for the running codex tail (bo is last), max 2h
for i in $(seq 1 120); do
  [ -s corpus/bo-2024.tsv ] && break
  sleep 60
done
log "wait done; tables: $(ls corpus/*.tsv | wc -l)"

# 2. retry any missing wave-2 countries once on codex/terra (skip guard makes this cheap)
export ENGINE=codex
for pair in "au au-2024.tsv" "ch ch-2024.tsv" "no no-2024.tsv" "mn mn-2024.tsv" "bo bo-2024.tsv"; do
  set -- $pair
  ./tools/build_canon.sh "$1" "$2" >> "$LOG" 2>&1
done
log "retries done; tables: $(ls corpus/*.tsv | wc -l)"

# 3. India receipts fix: fetch NCERT reader TOCs into resources/
timeout 900 codex exec --skip-git-repo-check -s danger-full-access -C /home/diablo/book10 --model gpt-5.6-terra "Task: repair a receipts gap. corpus/in-2025.tsv rows were flagged because the chapter-level contents of the prescribed NCERT readers are not in resources/. Download from official sources (ncert.nic.in or its textbook portal) the tables of contents (or full PDFs) of: First Flight (class 10 English), Footprints Without Feet (class 10 supplementary), Kshitij Part 2 (class 10 Hindi A). Save under resources/ with clear names, then write resources/in-toc-ledger.txt listing each file, its source URL, and the chapter list it contains. Do not modify the TSV. Print a 2-line summary." < /dev/null >> "$LOG" 2>&1
log "IN receipts job done"

# 4. confirm pass over all tables (skips the 7 already confirmed)
./tools/confirm_pass.sh >> "$LOG" 2>&1
log "confirm pass done: $(ls notes/confirm-*.md | wc -l) confirm files"

# 5. grouped manual
python3 tools/window_report.py > notes/window-report.md 2>> "$LOG"
log "window report: $(wc -c < notes/window-report.md) bytes"

# 6. sol conclusions draft over the manual + confirms
timeout 1200 codex exec --skip-git-repo-check -s workspace-write -C /home/diablo/book10 --model gpt-5.6-sol "You are the analysis reader for book10 (read CONTEXT.md first — especially the Method discipline section: NO correlation analysis, counts as plain facts only, at most 1-2 conclusions that survive scrutiny). Read notes/window-report.md (the grouped manual of admitted foreign works by period x genre x admitting country), the corpus/*.tsv tables, and skim notes/confirm-*.md for reliability caveats. Write notes/conclusions-draft.md: (1) a short honest description of what the grouped shelf shows, organized by the book's instruments (window size, the shared shelf, the enemy shelf, the errand); (2) the 1-2 conclusions you believe survive scrutiny, each stated as a human sentence with its supporting plain facts underneath and its caveats named (data quality, one-year slices, granularity differences between systems); (3) a list of claims you REJECTED as not surviving (with why) — the rejected list is as valuable as the accepted one; (4) which country essays look richest to write first. No percentages beyond plain fractions, no trend language, no invented rows — if a fact isn't in the tables, it doesn't exist. Print a 3-line summary when done." < /dev/null >> "$LOG" 2>&1
log "conclusions draft: $( [ -s notes/conclusions-draft.md ] && wc -c < notes/conclusions-draft.md || echo MISSING )"
echo "OVERNIGHT DONE: $(ls corpus/*.tsv | wc -l) tables, $(ls notes/confirm-*.md | wc -l) confirms, manual $( [ -s notes/window-report.md ] && echo ok || echo MISSING ), conclusions $( [ -s notes/conclusions-draft.md ] && echo ok || echo MISSING )"
