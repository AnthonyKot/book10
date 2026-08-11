#!/usr/bin/env bash
# Translation check (agy): independently verify an essay's English renderings
# of quoted non-English passages. usage: ./tools/transcheck.sh <cc>
set -u
cd "$(dirname "$0")/.."
CC="${1:?usage: transcheck.sh <cc>}"
ESSAY="drafts/$CC.md"
OUT="notes/transcheck-$CC.md"
LOG="tools/log/transcheck-$CC.log"
[ -s "$ESSAY" ] || { echo "transcheck-$CC SKIP (no essay)"; exit 0; }
[ -s "$OUT" ] && { echo "transcheck-$CC SKIP (exists)"; exit 0; }
mkdir -p notes tools/log

PROMPT="You are a translation checker for book10, in this directory. Target: $ESSAY. Find every quoted non-English passage (Ukrainian, Russian, Belarusian, Vietnamese, Chinese, Japanese, Spanish, Portuguese, German, etc. — anything in guillemets/quotes followed by an English rendering). For each: (1) translate the original INDEPENDENTLY, without looking at the essay's rendering first; (2) then compare with the essay's rendering; (3) classify: FAITHFUL (meaning preserved; stylistic differences fine) or DIVERGENT (meaning shifted, softened, sharpened, or wrong — explain in one line what the difference does to the claim built on the quote). Also verify each quoted original against the source document in resources/ if it is cited to one (grep a fragment; line-wraps cause false misses — retry shorter fragments before flagging). Write $OUT: summary line (N passages, F faithful, D divergent, V verified-in-source, M not-found), then details ONLY for DIVERGENT or not-found items. OUTPUT ONLY the file."

echo "[$(date +%H:%M:%S)] transcheck $CC — agy" | tee -a "$LOG"
timeout 900 agy --dangerously-skip-permissions --print-timeout 14m --model gemini-3.6-flash-high -p "$PROMPT" >> "$LOG" 2>&1
if [ -s "$OUT" ]; then echo "transcheck-$CC OK: $(head -1 "$OUT" | cut -c1-100)"
else
  timeout 900 agy --dangerously-skip-permissions --print-timeout 14m --model gemini-3.6-flash-high -p "$PROMPT" >> "$LOG" 2>&1
  [ -s "$OUT" ] && echo "transcheck-$CC OK-2" || echo "transcheck-$CC FAIL"
fi
