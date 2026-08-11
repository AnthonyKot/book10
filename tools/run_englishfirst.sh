#!/bin/bash
# English-first sweep: apply AGENT.md's binding 2026-08-11 rule to essays already written.
# Order = worst offenders for a reader without the language: vn (Vietnamese), cn (Chinese),
# br (Portuguese). ua/ru/kz are Russian/Ukrainian, which the reader reads — handled later.
# NOT self-skipping: each essay is rewritten once. Re-audits and re-transchecks after.
cd /home/diablo/book10 || exit 1
mkdir -p tools/log

for CC in vn cn br; do
  case "$CC" in
    vn) TSV=vn-2024; LANG_NOTE="Vietnamese" ;;
    cn) TSV=cn-2024; LANG_NOTE="Chinese" ;;
    br) TSV=br-2024; LANG_NOTE="Portuguese" ;;
  esac
  echo "[$(date +%H:%M:%S)] english-first $CC — opus" | tee -a "tools/log/ef-$CC.log"
  timeout 1500 claude --dangerously-skip-permissions --model claude-opus-5 -p "You are the WRITE model for book 10, applying ONE binding rule to an essay that is otherwise finished and reader-approved in substance. Read AGENT.md's rule 'English carries the prose' (added 2026-08-11) FIRST, then drafts/$CC.md.

The reader does not read $LANG_NOTE and told us the essays are hard to follow because the original-language text sits in the load-bearing position. Fix ONLY that, in place:
- Every quotation in the BODY becomes English. Move the verbatim $LANG_NOTE original into a Receipts block, keyed by page/location, exactly as drafts/bo.md now does — read bo.md's 'Quotations — Spanish originals' block as the model.
- Keep an original inline ONLY where its exact wording IS the finding (a subject's name, a document's term of art, a title, a country tag) and gloss it in the same breath.
- Preserve every original character-for-character when you move it, including its own quotation marks, line breaks and terminal punctuation; mark any omission with an explicit ellipsis in brackets.
- Do not change the argument, the structure, the findings, the receipts' substance, or the Limits — this is a vehicle change only. Do not re-report counts.
- Check each English rendering against its original as you move it: the translations now CARRY the argument, so a loose rendering becomes a factual error. Repair any that drift.
- Update the Limits length line to the new true count if it changes.
Print a 2-line summary." >> "tools/log/ef-$CC.log" 2>&1

  if [ -s "drafts/$CC.md" ] && [ "$(wc -w < "drafts/$CC.md")" -gt 600 ]; then
    rm -f "notes/review-$CC.md" "notes/transcheck-$CC.md"
    timeout 1200 codex exec --skip-git-repo-check -s workspace-write -C "$(pwd)" --model gpt-5.6-sol "You are the AUDIT model for book 10. Target: drafts/$CC.md, just converted to AGENT.md's 'English carries the prose' rule. The MAIN RISK SURFACE is translation: English renderings now carry the argument. Verify (a) every $LANG_NOTE original in Receipts is verbatim against the defining documents in resources/, with the document's own punctuation and marked omissions; (b) every English rendering in the body is faithful to its original and adds nothing; (c) nothing in the argument, counts, or Limits changed in the move; (d) corpus/$TSV.tsv still supports every number. Write notes/review-$CC.md: verdict line first (SHIP AS IS / FIX THEN SHIP / REWRITE), then numbered REQUIRED fixes with evidence, then a short OPTIONAL list. Print a 2-line summary." < /dev/null >> "tools/log/ef-$CC.log" 2>&1
    ./tools/transcheck.sh "$CC" >> "tools/log/ef-$CC.log" 2>&1 || true
    echo "ef-$CC DONE ($(wc -w < "drafts/$CC.md") words; audit: $(head -1 "notes/review-$CC.md" 2>/dev/null); transcheck: $(head -1 "notes/transcheck-$CC.md" 2>/dev/null))"
  else
    echo "ef-$CC FAIL"
  fi
done
echo "ENGLISH-FIRST SWEEP DONE"
