#!/bin/bash
# Wave 2a: uk-aqa, br, au through the classic lane (Opus writes, sol audits, agy transchecks).
# Reader-authorized 2026-08-11; runs immediately (reader switched accounts, Opus available).
cd /home/diablo/book10 || exit 1
mkdir -p tools/log
echo "[$(date +%H:%M:%S)] wave2a start"

./tools/essay.sh uk uk-aqa-2025 "England's window is closed by the subject's own name — English Literature — and this table is the corpus's closed-window case: ZERO foreign-coded rows. The essay is about a door that opens inward. The AQA 8702 specification is ONE exam board, not a national list — say so plainly in the door paragraph and Limits, and never present board rows as England's shelf. All 73 memorize values were corrected excerpt->no in recon (closed-book exam quotation-learning is not an explicit by-heart mandate); that systemic correction belongs in Limits, not as a finding. resources/ is rich here (schemes of work, unseen-poetry guide, the Collins Worlds and Lives teacher guide) — quote teaching language verbatim where it serves. Story-spine rule is binding: find the scene; the document must not be the protagonist."

./tools/essay.sh br br-2024 "The door is the FUVEST 2024 obligatory reading list — a university entrance examination (São Paulo's vestibular), not a ministry program: a different door type from every codifier and program in the corpus so far. Be precise about whose door it is (one university system), who stands in front of it (a candidate, not a pupil in a compulsory classroom), and what force a row has. Recon was clean: all nine disputed era items resolved inside the saved manual, zero quarantines. Story-spine rule is binding: find the scene."

./tools/essay.sh au au-2024 "NSW English prescriptions 2019-2026 — ONE state standing in for a federation (same finding-shape as Germany's Länder; say so). All 141 rows are choice-list: prescriptions inside elective modules, so no single pupil meets more than a sliver of the table — never compare raw row counts as openness, and make the menu-door mechanics concrete. 21 subject_era corrections were applied in recon; the table is repaired and citable. Story-spine rule is binding: find the scene."

echo "[$(date +%H:%M:%S)] WAVE 2A DONE"
