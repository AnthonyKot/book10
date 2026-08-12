#!/bin/bash
# Interlude fact-extraction lane — grok, 9 countries in parallel.
# Output: tools/log/interlude-facts/<cc>.md (stdout capture; grok's zero-byte
# failure mode means ALWAYS check the size report at the end).
cd /home/diablo/book10 || exit 1
mkdir -p tools/log/interlude-facts

run_one() {
  cc="$1"
  extra="$2"
  grok --always-approve --max-turns 25 -p "You are a fact-extraction engine for a book project in /home/diablo/book10 (your working directory). Country code: ${cc}. Build the FACT SHEET for a 300-600-word door-note in an interlude chapter about closed literary windows. Sources in authority order: corpus/${cc}*.tsv, notes/recon-${cc}*.md, notes/confirm-${cc}*.md, any resources/${cc}* source ledger.${extra} Rules: PLAIN FACTS ONLY, no essay prose, no interpretation beyond what sources literally state; never invent; if a source file is missing, write MISSING and move on. Counts as plain fractions only (e.g. '2 of 82 rows'). Output to stdout as markdown with exactly these sections: 1. THE DOOR - document name, issuing body, year, force type (mandate/menu/anthology/quota/open-formula/no-list). 2. THE WINDOW - which foreign works/authors are admitted, named exactly as the table names them, with the fraction. 3. QUARANTINED - rows flagged unsupported/quarantined, listed, never omitted. 4. THE STRANGEST CONCRETE DETAIL - the single oddest sourced fact a door-note could open on, with its source file and row/line. 5. CANNOT SAY - the confirm/recon caveats for this country, compressed." \
    > "tools/log/interlude-facts/${cc}.md" 2> "tools/log/interlude-facts/${cc}.err"
}

# kz/it/mn have essay drafts whose facts (not prose) are usable source material
run_one de "" &
run_one mx "" &
run_one mn " Also drafts/mn.md exists with a REWRITE verdict: you may mine it for facts only, and only ones that carry a receipt; ignore its prose." &
run_one jp "" &
run_one it " Also drafts/it.md exists with a REWRITE verdict: you may mine it for facts only, and only ones that carry a receipt; ignore its prose." &
run_one be "" &
run_one ch "" &
run_one no "" &
run_one kz " Also drafts/kz.md exists (a cleared full essay, demoted to door-note by the reader): you may mine it for facts only, each with a receipt; ignore its prose." &
wait

echo "=== SIZE REPORT (zero or tiny = failed run, rerun it) ==="
wc -c tools/log/interlude-facts/*.md
