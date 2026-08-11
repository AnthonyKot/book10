#!/bin/bash
# Rework wave 2 (restart after f775e0e): ru, kz, cn ONLY.
# ua and vn are already reworked and cleared — NEVER re-rework them (drift).
cd /home/diablo/book10 || exit 1
chmod +x tools/rework_essay.sh
./tools/rework_essay.sh ru ru-2025 "Unapplied audit (the apply step errored — treat notes/review-ru.md REQUIRED fixes as still pending) AND 4,017 words against a 2,200 cap AND predates the story-spine rule. Rework: apply the audit, find the scene (the codifier as the exam's legal text — a teenager's exam ticket, the parenthesis where the whole world lives), compress hard. The Ukraine essay (drafts/ua.md) is its published neighbor — sharpen the contrast, don't repeat its moves."
./tools/rework_essay.sh kz kz-2023 "3,621 words, predates the story-spine rule. Rework per AGENT.md: find the scene (a bilingual school's two literature classrooms? the shelf where 21 Russian works stand next to Abai?), compress toward 2,200, keep the admission-never-why discipline that the audit confirmed."
./tools/rework_essay.sh cn cn-2024 "Good length (2,310), predates the story-spine rule — check whether the document is the protagonist and fix if so; the Snow mirror is the natural scene (an American's notebook as China's chosen window on itself). Keep the Fabre quarantine in Limits."
echo "REWORK WAVE 2 DONE"
