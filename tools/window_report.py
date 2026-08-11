#!/usr/bin/env python3
"""The Window report: all admitted FOREIGN works across corpus/*.tsv,
grouped by literary period x genre, each entry listing admitting countries.

usage: window_report.py > notes/window-report.md
"""
import csv, glob, os, re
from collections import defaultdict

BOOK = os.path.join(os.path.dirname(__file__), "..")

def period(born_raw):
    b = born_raw.strip().lstrip("~").strip()
    bce = "BCE" in b or "до н" in b
    m = re.search(r"\d+", b)
    if not m:
        return "unknown"
    y = int(m.group(0))
    if bce:
        return "Antiquity"
    if y < 500:   return "Antiquity"
    if y < 1300:  return "Medieval"
    if y < 1600:  return "Renaissance"
    if y < 1750:  return "17th–early 18th c."
    if y < 1830:  return "Romantics (b. 1750–1830)"
    if y < 1880:  return "19th-c. realists (b. 1830–1880)"
    if y < 1930:  return "Modernists & interwar (b. 1880–1930)"
    if y < 1970:  return "Postwar (b. 1930–1970)"
    return "Contemporary (b. 1970– )"

PERIOD_ORDER = ["Antiquity", "Medieval", "Renaissance", "17th–early 18th c.",
                "Romantics (b. 1750–1830)", "19th-c. realists (b. 1830–1880)",
                "Modernists & interwar (b. 1880–1930)", "Postwar (b. 1930–1970)",
                "Contemporary (b. 1970– )", "unknown"]

# key: (author-normalized) -> {periods, genres, countries{cc: title}, source_lang}
works = defaultdict(lambda: {"genres": set(), "periods": set(),
                             "countries": {}, "langs": set(), "display": ""})

for path in sorted(glob.glob(os.path.join(BOOK, "corpus", "*.tsv"))):
    cc = os.path.basename(path).split("-")[0]
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            origin = r.get("origin", "")
            if not origin.startswith("translated"):
                continue
            author = r["author"].strip()
            # normalize on the Latin gloss in parentheses when present
            m = re.search(r"\(([^)]+)\)", author)
            key = (m.group(1) if m else author).lower()
            w = works[key]
            w["display"] = m.group(1) if m else author
            w["genres"].add(r.get("genre", "?").strip() or "?")
            w["periods"].add(period(r.get("author_born", "")))
            title = r["title"].split("(")[0].strip()
            w["countries"][cc] = title[:80]
            lang = origin.split(":", 1)[1].split(",")[0] if ":" in origin else "?"
            w["langs"].add(lang.strip())

by_period = defaultdict(lambda: defaultdict(list))
for key, w in works.items():
    p = sorted(w["periods"])[0]
    for g in sorted(w["genres"])[:1]:
        by_period[p][g].append(w)

print("# The Window — admitted foreign works, by period and genre\n")
print(f"Corpus tables: {', '.join(os.path.basename(p) for p in sorted(glob.glob(os.path.join(BOOK,'corpus','*.tsv'))))}\n")
total = len(works)
print(f"{total} distinct foreign authors/works admitted across the corpus.\n")

# admission leaderboard
board = sorted(works.values(), key=lambda w: -len(w["countries"]))[:15]
print("## Most-admitted (the de-facto world canon)\n")
for w in board:
    if len(w["countries"]) < 2:
        break
    cs = ", ".join(f"{c}: {t}" for c, t in sorted(w["countries"].items()))
    print(f"- **{w['display']}** — {len(w['countries'])} countries ({cs})")
print()

for p in PERIOD_ORDER:
    if p not in by_period:
        continue
    print(f"\n## {p}\n")
    for g in sorted(by_period[p]):
        print(f"**{g}**")
        for w in sorted(by_period[p][g], key=lambda w: (-len(w['countries']), w['display'])):
            cs = " · ".join(f"`{c}` {t}" for c, t in sorted(w["countries"].items()))
            langs = "/".join(sorted(w["langs"]))
            print(f"- {w['display']} ({langs}) — {cs}")
        print()
