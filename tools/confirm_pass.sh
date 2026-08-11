#!/bin/bash
# Blind second pass (sol/codex): re-code subject_era + memorize for each corpus
# table against the documents in resources/, without seeing wave-1 codings.
cd /home/diablo/book10 || exit 1
LOG=tools/log/confirm.log
mkdir -p notes tools/log
for f in corpus/*.tsv; do
  cc=$(basename "$f" .tsv)
  out="notes/confirm-$cc.md"
  [ -s "$out" ] && { echo "skip $cc" >> "$LOG"; continue; }
  PROMPT="You are running a blind verification pass for book10 (read CONTEXT.md and corpus/SCHEMA.md first). Target table: $f. The columns subject_era and memorize were coded by another model; do NOT trust them — re-derive them independently.

For EVERY row: (1) read author+title; (2) state your own subject_era coding (the historical period/wound the work is set in or about, using the schema's style) and your own memorize judgment (is memorization of this text mandated at this level — check the defining document in resources/ if it marks recitation/по памяти/学習指導要領 memorization, otherwise 'no'); (3) THEN compare with the table's value: mark CONFIRMED if equivalent, CHECK if different (give your value and one-line reason).

Also flag any row that looks like a hallucination risk: a work you cannot find in the resources/ document text for this country (grep it; account for transliteration variants before flagging).

Write $out as markdown: a summary line (N rows, X confirmed era, Y CHECK era, Z memorize disagreements, H hallucination flags), then ONLY the CHECK/flag rows in detail (confirmed rows just count). OUTPUT ONLY the file."
  echo "=== confirm-$cc $(date +%H:%M:%S)" >> "$LOG"
  timeout 900 codex exec --skip-git-repo-check -s workspace-write -C /home/diablo/book10 --model gpt-5.6-sol "$PROMPT" < /dev/null >> "$LOG" 2>&1
  if [ -s "$out" ]; then echo "confirm-$cc OK ($(wc -c < "$out") bytes)" >> "$LOG"
  else echo "confirm-$cc FAIL" >> "$LOG"; fi
done
echo "CONFIRM PASS DONE: $(grep -c 'OK' "$LOG") ok, $(grep -c 'FAIL$' "$LOG") fail"
