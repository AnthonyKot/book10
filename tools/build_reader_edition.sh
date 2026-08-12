#!/bin/bash
# Build the reader-edition source file (v7+) by concatenating reader cuts in
# PLAN.md spine order. Usage: tools/build_reader_edition.sh <output.md>
# Spine: 00 → post-Soviet (ua ru; by pending testimony) → three ways (cn vn in)
# → Latin doors (bo br) → anglosphere (au us uk). Interlude + closing chapter
# join the spine when written.
set -e
cd "$(dirname "$0")/.." || exit 1
OUT="${1:?usage: build_reader_edition.sh <output.md>}"

SPINE="00-poem ua ru cn vn in bo br au us uk"

cat > "$OUT" << 'FRONT'
# The Window — a draft of the book (v7)

**Eleven chapters in reading order**, now through the polish wave: the cold sweep's
per-chapter fixes applied, the "what this chapter can't know" landers retired to the
masters, one second-person close kept in the whole book (Ukraine's), and every polished
chapter re-audited against its master for fact fidelity. Russia's chapter appears here
in its first reader cut. Belarus still waits for its witness; the Closed Windows
interlude and the closing chapter (There Is No World Canon) are next.

Order: The Poem in Your Body · Ukraine · Russia · China · Vietnam · India · Bolivia ·
Brazil · Australia · United States · England.

---

FRONT
first=1
for cc in $SPINE; do
  f="drafts/reader/${cc}.md"
  if [ ! -s "$f" ]; then
    echo "MISSING OR EMPTY: $f — refusing to build a partial edition" >&2
    exit 1
  fi
  [ $first -eq 0 ] && printf '\n\n---\n\n' >> "$OUT"
  cat "$f" >> "$OUT"
  first=0
done

echo "Built $OUT: $(wc -w < "$OUT") words, $(grep -c '^# ' "$OUT") chapters"
