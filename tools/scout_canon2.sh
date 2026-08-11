#!/usr/bin/env bash
# Book10 scout, wave 2: agy locates the enforceable canon document for ten more countries.
set -u
cd "$(dirname "$0")/.."
OUT="notes/scout-canon2.md"
LOG="tools/log/scout-canon2.log"
mkdir -p notes tools/log
[ -s "$OUT" ] && { echo "canon-scout2 SKIP (exists)"; exit 0; }

PROMPT="You are scouting source documents for book10 wave 2 (read CONTEXT.md in this directory first — the design: the school literature canon, corpus unit = the enforceable LIST; the subject of the book is the FOREIGN literature each country's school admits — 'the window').

USE YOUR GOOGLE/WEB TOOLS FREELY. For EACH of these school systems — Mexico (MX: SEP, libros de texto gratuitos / secundaria), Bolivia (BO), Brazil (BR: BNCC plus the famous university vestibular reading lists, e.g. FUVEST — note which is the enforceable one), Vietnam (VN: the state Ngữ văn anthology), Japan (JP: MEXT-approved kokugo textbooks for lower secondary), Mongolia (MN), Belgium (BE: BOTH communities — Flemish leerplannen and Fédération Wallonie-Bruxelles référentiels; two windows in one country), Australia (AU: pick NSW Stage 5/6 prescribed texts as the concrete example, note other states), Switzerland (CH: cantonal plurality — pick one German-speaking and one French-speaking canton example, e.g. Zürich Lehrplan 21 and Vaud), Norway (NO: LK20 curriculum; note the 2000s national 'kanon' debate outcome) — locate:

1. The EXACT document defining what a 14-16-year-old reads/can be examined on in literature class: official name (original language + translation), issuing body, most recent year, working URL (verify it resolves; prefer official domains).
2. Format (PDF list / web page / anthology TOC / teacher-choice framework with recommended list).
3. Approximate size (works/authors at this level) and — CRITICAL for this book — how much of it is FOREIGN/translated literature and whether the document marks that distinction itself.
4. One concrete finding you noticed while looking (a reform, a removal, a canon controversy) with URL.
5. Feasibility grade: EASY / MEDIUM / HARD (explain HARD: what substitutes).

Also answer: (a) does the system mandate memorization of specific texts; (b) is there a national-literature vs world-literature subject split (like Ukraine's separate Зарубіжна література) anywhere in this set?

Write to $OUT as markdown: summary table first (country | document | year | size | foreign share | feasibility), then one section per country, ending with 'Wave-2 pilot recommendation: <which 2 to table-ize first and why>'. OUTPUT ONLY the file."

echo "[$(date +%H:%M:%S)] canon scout wave2 — agy" | tee -a "$LOG"
timeout 1200 agy --dangerously-skip-permissions --print-timeout 18m --model gemini-3.6-flash-high -p "$PROMPT" >> "$LOG" 2>&1
if [ -s "$OUT" ] && [ "$(wc -c < "$OUT")" -gt 2000 ]; then
  echo "canon-scout2 OK ($(wc -c < "$OUT") bytes)"
else
  echo "canon-scout2 RETRY" | tee -a "$LOG"
  timeout 1200 agy --dangerously-skip-permissions --print-timeout 18m --model gemini-3.6-flash-high -p "$PROMPT" >> "$LOG" 2>&1
  [ -s "$OUT" ] && echo "canon-scout2 OK-2 ($(wc -c < "$OUT") bytes)" || echo "canon-scout2 FAIL"
fi
