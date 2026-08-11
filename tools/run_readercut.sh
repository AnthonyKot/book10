#!/bin/bash
# Reader-cut lane: produce clean reader versions per AGENT.md's 2026-08-11 ruling
# "the essay performs its findings, not its evidence". Masters in drafts/<cc>.md keep
# full apparatus; reader cuts go to drafts/reader/<cc>.md and feed the artifact.
# Self-skipping on existing reader cuts.
cd /home/diablo/book10 || exit 1
mkdir -p drafts/reader tools/log

for CC in ua vn bo cn br au us in uk; do
  OUT="drafts/reader/$CC.md"
  [ -s "$OUT" ] && { echo "readercut-$CC SKIP"; continue; }
  echo "[$(date +%H:%M:%S)] readercut $CC — opus" | tee -a tools/log/readercut.log
  timeout 900 claude --dangerously-skip-permissions --model claude-opus-5 -p "You are the WRITE model for book 10 producing the READER CUT of one finished, audited essay. Read AGENT.md's ruling 'The essay performs its findings, not its evidence' (2026-08-11), then drafts/$CC.md (the evidenced master — every claim in it has already survived audit and transcheck).

Write drafts/reader/$CC.md: the same essay, but written as if for a book page, not an audit:
- NO blockquotes. NO page citations in prose. NO Receipts section. NO bulleted Limits.
- Quotations: at most one or two SHORT inline quotes, kept only where the exact wording is the jewel of the paragraph. Everything else the essay simply says in its own English.
- Convert quoted evidence into confident narrative prose. Where the master says 'the document states X (p. N)', the reader cut says X.
- Keep the story spine, the scenes, the findings, the lander, and the honesty: claims the master marks as the essay's own reading stay marked ('I read this as', 'on this essay's reading') in a light, natural way.
- End with ONE short closing paragraph in plain prose covering only the load-bearing caveats a general reader deserves (e.g. 'this is one exam board, not England'; 'names in an anthology, not a mandate') — three sentences maximum.
- ADD NOTHING NEW. Every sentence must be derivable from the master. Do not re-derive numbers; carry them as the master states them.
- Target 1,200–1,800 words.
Print a 1-line summary." >> tools/log/readercut.log 2>&1
  if [ -s "$OUT" ] && [ "$(wc -w < "$OUT")" -gt 500 ]; then
    echo "readercut-$CC DONE ($(wc -w < "$OUT") words)"
  else
    echo "readercut-$CC FAIL"; rm -f "$OUT"
  fi
done
echo "READER CUT LANE DONE"
