# Book 10 — resume runbook (stopped cleanly 2026-08-11 ~12:30)

State at stop (all committed, `git log` in this repo):
- 20/20 corpus tables · 20/20 confirms · 10/17 recons (7 pending, see below)
- Essays: ua ✅reworked · vn ✅reworked (4,002 words — length still hot, reader judges)
  · bo ✅new-contract · ru/kz/cn drafted but NOT yet reworked to the story-spine rule
- AGENT.md carries the binding story-spine rule (added mid-wave; ru/kz/cn predate it)

## Restart (in order; each step skips what's already done)

1. Remaining reworks — run ONLY these three (never re-rework ua/vn):
   ./tools/rework_essay.sh ru ru-2025 "<see run_rework1.sh for the ru note>"
   ./tools/rework_essay.sh kz kz-2023 "<kz note>"
   ./tools/rework_essay.sh cn cn-2024 "<cn note>"
   (or: edit run_rework1.sh to comment out the ua/vn lines and re-run it)
2. Remaining recons (self-skipping, safe to run whole list):
   for t in by-2024 in-2025 jp-2024 mx-2024 br-2024 au-2024 us-2024 uk-aqa-2025 it-2025 de-2024 mn-2024; do ./tools/recon.sh "$t"; done
3. Refresh the reading artifact with ru/kz/cn when they clear; reader questions:
   does BO/VN v2 pass the story-spine bar; is the recurring length overshoot
   (3-4k vs 2.2k cap) earned or does the cap need enforcement in essay.sh?
4. Then: BY essay (waits on reader's two witness answers — separate Russian-lit
   subject? what memorized?), then wave 2 (in, jp, mx, br, au, us, uk, it, de, mn,
   be/ch/no as door-essays).

Engines: Opus writes (claude CLI), sol audits (codex), terra fetches (codex
danger-full-access), agy transchecks (fast, quota refreshed). Commit after each
milestone; resources/ and tools/log/ stay untracked (anti-leak).
