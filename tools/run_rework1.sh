#!/bin/bash
# Rework wave: waits for essay wave 1 to finish, then reworks per reader verdicts.
cd /home/diablo/book10 || exit 1
for i in $(seq 1 120); do
  [ -s drafts/bo.md ] && break
  sleep 60
done
chmod +x tools/rework_essay.sh
./tools/rework_essay.sh ua ua-2024 "Solid 3 of 5 — keep structure and all discoveries; CLEAN for readability: reduce inline citation freight to Receipts, shorten overloaded sentences, cut throat-clearing. This is a polish, not a rebuild."
./tools/rework_essay.sh vn vn-2024 "Barely readable as an essay — it is a bot's reflections on reading a book list: it walks the circular clause by clause and its protagonist is the document. Full rewrite on a story spine. Candidate spines (pick the strongest, or a better one you find in the documents): (a) since the 2018 reform several competing textbook series answer the same eight-literatures quota — follow ONE quota slot (e.g. the Russian one) into the actual books pupils carry and watch different editors answer the same order differently; (b) open in the classroom where a Vietnamese teenager meets Aitmatov or Chekhov and work outward to the sentence that put the book there; (c) the shelf with eight mandatory windows as a physical scene. The three-tier force finding and the 'floor not a scale' quote are cargo — keep them, but they arrive when the story calls them."
./tools/rework_essay.sh ru ru-2025 "Unapplied audit (the apply step errored — treat notes/review-ru.md REQUIRED fixes as still pending) AND 4,017 words against a 2,200 cap AND predates the story-spine rule. Rework: apply the audit, find the scene (the codifier as the exam's legal text — a teenager's exam ticket, the parenthesis where the whole world lives), compress hard. The Ukraine essay (drafts/ua.md) is its published neighbor — sharpen the contrast, don't repeat its moves."
./tools/rework_essay.sh kz kz-2023 "3,621 words, predates the story-spine rule. Rework per AGENT.md: find the scene (a bilingual school's two literature classrooms? the shelf where 21 Russian works stand next to Abai?), compress toward 2,200, keep the admission-never-why discipline that the audit confirmed."
./tools/rework_essay.sh cn cn-2024 "Good length (2,310), predates the story-spine rule — check whether the document is the protagonist and fix if so; the Snow mirror is the natural scene (an American's notebook as China's chosen window on itself). Keep the Fabre quarantine in Limits."
echo "REWORK WAVE DONE"
