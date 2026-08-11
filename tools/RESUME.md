# Book 10 — resume runbook (updated 2026-08-11 ~18:30)

## State

20/20 tables · 20/20 confirms · 17/17 recons (be/ch/no empty by design — recon loop is
FINISHED, never re-run).

**Nine essays cleared audit + transcheck and are committed:**
ua · vn · bo · ru · kz · cn · uk · br · au

**Wave 2b writing now** (Opus lane, `tools/run_wave2b.sh`): us · in · it · mn.

**Reading artifact — NEW ADDRESS as of 2026-08-11:**
https://claude.ai/code/artifact/4428face-788a-47a2-976a-c8b7001474dc
The previous artifact (19db3f88-…) died when the reader switched Claude accounts — an
artifact cannot be read or updated from a different account. Pass the URL above as the
Artifact tool's `url` parameter, and if it ever 404s again, publish fresh and record the
new address here rather than retrying.

## Rulings recorded (do not re-litigate)

- **Length**: cap 2,200; may earn to ~3,000 with the reason stated in Limits; past 3,000
  goes back for compression. In AGENT.md.
- **Writer**: Opus or Fable, either is precedented (kz, cn, and au's second apply pass
  were Fable's). sol audits, agy transchecks — those gates never move.
- **BY door** (witness answer (a)): Русская литература WAS a separate subject with its
  own hours → the BY essay is a TWO-DOORS story, not a window story. notes/witness-by.md.
- **be/ch/no** (resolved 2026-08-11, was flagged as a conflict): conclusions-draft.md's
  "do not draft Belgium, Switzerland, or Norway from the present corpus" forbids a
  SHELF-WALK essay from an empty table — it does not forbid AGENT.md's door-essay written
  from the source ledger. **BE and CH: door-essays are cleared to write**; their ledgers
  are strong (CH's carries SHA-256 hashes and page-level evidence). **NO: blocked** until
  its ledger exists — terra was tasked with authoring
  `resources/no-2024-source-ledger.txt` on 2026-08-11; check whether it landed.

## Next steps

1. **BY essay** — waits ONLY on witness answer (b): what the reader memorized by heart.
   Ask open-form, never a menu. Two findings already verified for it:
   - `resources/` holds TWO grade-9 programs, `by_bel_lit_9_2019.txt` and
     `by_rus_lit_9_2019.txt`, both under 2019 ministry order No. 123 — documentary
     corroboration of the separate-subject testimony.
   - conclusions-draft.md's old worry that "twelve Belarus rows appear imported from the
     Russian file" is RESOLVED: recon checked all 44 disputed rows against both saved
     programs, 82 rows in / 82 out, zero quarantined.
   - Caveat to handle: all 82 rows carry ONE source URL (a GEI archive bitstream) though
     two distinct programs exist. Receipts must cite the two programs separately.
   - Shape: 43 domestic + 37 translated:russian (second national shelf, own door) + a
     2-row window (1 Polish, 1 English). conclusions-draft says BY must not LEAD the
     book — ordering only, no bar on writing it.
2. **be and ch door-essays** — cleared (see ruling above); write from the ledgers.
3. **no door-essay** — after terra's ledger lands and is spot-checked.
4. **de · jp · mx** — THIN receipts, worth a terra pass before writing: de's NRW saves
   are 5 byte-identical duplicates (dedupe or refetch); jp's rows rest on publisher TOCs
   rather than the MEXT standard (4 rows already quarantined); mx has no .txt extraction
   of its PDF and its Programa names no works at all — which IS the door finding.
5. **Connective instruments** (non-Opus, sol can do it any time): admission matrix,
   shared shelf vs national-poet slot, enemy shelf, window asymmetry, memorization
   inventory. notes/window-report.md predates 7 recons and counts author keys rather than
   works — regenerate before citing it.

## Standing rules

Quotes verbatim or gone · admission never motive · every number in prose traceable to the
table · unsupported rows quarantine, never silently delete · resources/ and tools/log/
never tracked · commit per milestone with
Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>.

Engines: `claude --model claude-opus-5 -p` writes · `codex exec -s workspace-write
--model gpt-5.6-sol` audits (NEVER read-only) · `codex exec -s danger-full-access
--model gpt-5.6-terra` fetches · `agy --print-timeout 14m --model gemini-3.6-flash-high
-p` transchecks (size-check the output — zero-byte failure mode).
Lane scripts in tools/ are self-skipping EXCEPT rework_essay.sh.
