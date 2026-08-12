#!/bin/bash
# Redo of the 5 failed grok fact sheets on sol (codex, workspace-write — local
# reads only, no network needed). Sol WRITES the sheet itself (never read-only).
cd /home/diablo/book10 || exit 1
mkdir -p tools/log/interlude-facts

run_one() {
  cc="$1"
  extra="$2"
  codex exec --skip-git-repo-check -s workspace-write --model gpt-5.6-sol "You are a fact-extraction engine for the book project in this directory. Country code: ${cc}. Build the FACT SHEET for a 300-600-word door-note in an interlude chapter about closed literary windows. Sources in authority order: corpus/${cc}*.tsv, notes/recon-${cc}*.md, notes/confirm-${cc}*.md, any resources/${cc}* source ledger.${extra} Rules: PLAIN FACTS ONLY, no essay prose, no interpretation beyond what sources literally state; never invent; if a source file is missing, write MISSING and move on. Counts as plain fractions only (e.g. '2 of 82 rows'). WRITE the sheet to tools/log/interlude-facts/${cc}.md (overwrite it — it currently holds a failed run), as markdown with exactly these sections: 1. THE DOOR - document name, issuing body, year, force type (mandate/menu/anthology/quota/open-formula/no-list). 2. THE WINDOW - which foreign works/authors are admitted, named exactly as the table names them, with the fraction; for an empty-by-design table, what the door document mandates instead. 3. QUARANTINED - rows flagged unsupported/quarantined, listed, never omitted; NONE if none. 4. THE STRANGEST CONCRETE DETAIL - the single oddest sourced fact a door-note could open on, with its source file and row/line. 5. CANNOT SAY - the confirm/recon caveats for this country, compressed." \
    < /dev/null > "tools/log/interlude-facts/${cc}.sollog" 2>&1
}

run_one be "" &
run_one ch "" &
run_one it " Also drafts/it.md exists with a REWRITE verdict: you may mine it for facts only, and only ones that carry a receipt; ignore its prose." &
run_one jp "" &
run_one kz " Also drafts/kz.md exists (a cleared full essay, demoted to door-note by the reader): you may mine it for facts only, each with a receipt; ignore its prose." &
wait

echo "=== SIZE REPORT (five redone sheets) ==="
wc -c tools/log/interlude-facts/{be,ch,it,jp,kz}.md
