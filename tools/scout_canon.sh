#!/usr/bin/env bash
# Book10 scout: agy locates each country's enforceable canon document.
set -u
cd "$(dirname "$0")/.."
OUT="notes/scout-canon.md"
LOG="tools/log/scout-canon.log"
mkdir -p notes tools/log

PROMPT="You are scouting source documents for book10 (read CONTEXT.md in this directory first — the design: the school literature canon of ~11 countries, where the corpus unit is the enforceable LIST: exam codifiers, set-text lists, ministry programs, state anthologies).

USE YOUR GOOGLE/WEB TOOLS FREELY. For EACH of these school systems — Belarus, Russia, Ukraine, China, India (NCERT), Germany (note the Länder problem: pick one concrete example, e.g. Bavaria or NRW Abitur/Mittlere Reife lists), Italy, UK (England GCSE: pick the largest exam board, AQA, and note the others), USA (note the no-ministry finding: what fills the vacuum — AP reading lists, Common Core exemplar list Appendix B, biggest-district lists), Kazakhstan, Sudan (if findable) — locate:

1. The EXACT document that defines what a 15-16-year-old can be examined on in literature: its official name (original language + translation), issuing body, most recent year/version, and a working URL (verify the URL actually resolves; prefer official ministry/exam-board domains).
2. Format: is it a PDF list, a web page, an annex to a curriculum standard, the table of contents of a state anthology?
3. Approximate size: how many works/authors does it prescribe at this age?
4. One concrete finding you noticed while looking (e.g. a documented recent removal or addition with a news source — Ukraine's post-2022 removals, a Russian codifier change, a Chinese anthology revision, a GCSE diversity reform) with URL.
5. Feasibility grade for the corpus: EASY (clean machine-readable list) / MEDIUM (PDF needs parsing) / HARD (no single document; explain what substitutes).

Also answer two design questions with what you find: (a) which countries mandate MEMORIZATION of specific poems at this age, and where that is written down; (b) whether each list marks works as domestic vs foreign/translated (or whether we must derive it).

Write the report to $OUT as markdown, one section per country, a summary table at the top (country | document | year | size | feasibility), and end with 'Pilot recommendation: <which 2 countries to table-ize first and why>'. OUTPUT ONLY the file."

echo "[$(date +%H:%M:%S)] canon scout — agy" | tee -a "$LOG"
timeout 1000 agy --dangerously-skip-permissions --print-timeout 14m --model gemini-3.6-flash-high -p "$PROMPT" >> "$LOG" 2>&1
if [ -s "$OUT" ] && [ "$(wc -c < "$OUT")" -gt 2000 ]; then
  echo "canon-scout OK ($(wc -c < "$OUT") bytes)"
else
  echo "canon-scout RETRY" | tee -a "$LOG"
  timeout 1000 agy --dangerously-skip-permissions --print-timeout 14m --model gemini-3.6-flash-high -p "$PROMPT" >> "$LOG" 2>&1
  [ -s "$OUT" ] && echo "canon-scout OK-2 ($(wc -c < "$OUT") bytes)" || echo "canon-scout FAIL"
fi
