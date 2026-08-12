#!/usr/bin/env python3
"""Assemble chapters/*.html from drafts/reader/*.md per ASSEMBLY.md.

Deterministic, no dependencies. Each page derives from exactly one reader cut,
carries the provenance comment verify.sh checks, and keeps the cut's ## headings
as <section> boundaries. Prev/next links chain across the pages listed here, in
PLAN.md reading order. Rerunnable: overwrites chapters/ pages and index.html.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "The Window"

# (page number, slug, source stem, part label, one-sentence description)
SPINE = [
    ("00", "the-poem-in-your-body", "00-poem", "Opening",
     "The memorized poem as the book's instrument: four school systems sign named texts into children's memory, and no two face the same direction."),
    ("01", "ukraine", "ua", "The Post-Soviet Quartet",
     "A whole school subject made of nothing but the world: Foreign Literature, and the poem from Bukovina recited in Ukrainian."),
    ("02", "russia", "ru", "The Post-Soviet Quartet",
     "Five years of Europe's canon climbed step by step — and a domestic shelf that keeps all four of the by-heart texts."),
    ("04", "china", "cn", "Three Ways to Hand a Child the World",
     "Nine required books, four of them foreign — and one of the four is a foreigner's book about China itself."),
    ("05", "vietnam", "vn", "Three Ways to Hand a Child the World",
     "The state requires eight named foreign literatures and leaves every author slot for the textbook to fill."),
    ("06", "india", "in", "Three Ways to Hand a Child the World",
     "The state prints the anthology, mandates every row — and quietly subtracts the chapters the exam will not ask."),
    ("07", "bolivia", "bo", "Latin Doors",
     "One official, unsellable textbook stages world literature as a cast of names with countries stamped after them."),
    ("08", "brazil", "br", "Latin Doors",
     "Nine obligatory books guard a university door; the window opens only onto the Portuguese-speaking world."),
    ("09", "australia", "au", "The Anglosphere Paradox",
     "The widest shelf in the corpus, offered at seventeen to those who choose it — and a bureaucratic AND that forces two novels to collide."),
    ("10", "united-states", "us", "The Anglosphere Paradox",
     "No ministry, no list: an exam with a blank where the student writes in the book they brought."),
    ("11", "england", "uk", "The Anglosphere Paradox",
     "An exam board whose window is closed by the subject's own name — and a Nigerian pot that crossed the border anyway."),
    ("12", "the-closed-windows", "windows", "Interlude",
     "Eight systems that mandate reading and name, between them, five foreign writers — and one system that names everything."),
    ("13", "there-is-no-world-canon", "canon", "Closing",
     "No work reaches five of seventeen tables, the national-poet office mostly stands empty, and every ministry builds its own world."),
]

INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_ITAL = re.compile(r"\*(.+?)\*")


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = INLINE_BOLD.sub(r"<strong>\1</strong>", text)
    text = INLINE_ITAL.sub(r"<em>\1</em>", text)
    return text


def parse(md: str):
    """Return (title, intro_paras, [(heading, paras), ...])."""
    title = None
    sections = []  # (heading or None, [paras])
    current = (None, [])
    para: list[str] = []

    def flush_para():
        nonlocal para
        if para:
            current[1].append(" ".join(para))
            para = []

    for line in md.splitlines():
        line = line.rstrip()
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        elif line.startswith("## "):
            flush_para()
            sections.append(current)
            current = (line[3:].strip(), [])
        elif not line:
            flush_para()
        else:
            para.append(line.strip())
    flush_para()
    sections.append(current)
    if title is None:
        raise SystemExit("reader cut lacks a # title")
    intro = sections[0][1]
    return title, intro, sections[1:]


def render(num, slug, stem, part, desc, prev_link, next_link) -> str:
    src = ROOT / "drafts" / "reader" / f"{stem}.md"
    title, intro, sections = parse(src.read_text(encoding="utf-8"))
    lede = inline(intro[0]) if intro else ""
    out = []
    out.append("<!DOCTYPE html>")
    out.append('<html lang="en">')
    out.append("<head>")
    out.append('<meta charset="utf-8">')
    out.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    out.append(f"<!-- source: drafts/reader/{stem}.md -->")
    out.append(f"<title>{html.escape(title)} — {SITE}</title>")
    out.append(f'<meta name="description" content="{html.escape(desc, quote=True)}">')
    out.append('<link rel="stylesheet" href="../static/style.css">')
    out.append('<script src="../static/theme.js"></script>')
    out.append("</head>")
    out.append("<body>")
    out.append('<header class="site-header">')
    out.append('  <div class="wrap">')
    out.append(f'    <a class="brand" href="../index.html">The <span>Window</span></a>')
    out.append('    <nav class="site-nav" aria-label="Site">')
    out.append('      <a href="../index.html">Contents</a>')
    out.append('      <a href="../about.html">Method</a>')
    out.append('      <button class="theme-toggle" type="button">☾ Dark</button>')
    out.append("    </nav>")
    out.append("  </div>")
    out.append("</header>")
    out.append("")
    out.append('<main class="wrap">')
    out.append(f'  <p class="kicker">{html.escape(part)} · Chapter {num}</p>')
    out.append(f"  <h1>{inline(title)}</h1>")
    if lede:
        out.append(f'  <p class="lede">{lede}</p>')
    for p in intro[1:]:
        out.append(f"  <p>{inline(p)}</p>")
    for heading, paras in sections:
        out.append("  <section>")
        if heading:
            out.append(f"    <h2>{inline(heading)}</h2>")
        for p in paras:
            out.append(f"    <p>{inline(p)}</p>")
        out.append("  </section>")
    out.append('  <nav class="chapter-nav" aria-label="Chapter">')
    if prev_link:
        out.append(f'    <a href="{prev_link[0]}">← {html.escape(prev_link[1])}</a>')
    else:
        out.append('    <a href="../index.html">← Contents</a>')
    if next_link:
        out.append(f'    <a href="{next_link[0]}">{html.escape(next_link[1])} →</a>')
    else:
        out.append('    <a href="../index.html">Contents →</a>')
    out.append("  </nav>")
    out.append("</main>")
    out.append("")
    out.append('<footer class="site-footer">')
    out.append('  <div class="wrap">')
    out.append(f"    <p>{SITE} · Chapter {num}</p>")
    out.append("  </div>")
    out.append("</footer>")
    out.append("")
    out.append("</body>")
    out.append("</html>")
    return "\n".join(out) + "\n"


def main():
    pages = []
    for num, slug, stem, part, desc in SPINE:
        src = ROOT / "drafts" / "reader" / f"{stem}.md"
        if not src.is_file() or not src.stat().st_size:
            sys.exit(f"MISSING OR EMPTY: {src} — refusing a partial assembly")
        pages.append((num, slug, stem, part, desc))

    titles = {}
    for num, slug, stem, part, desc in pages:
        t, _, _ = parse((ROOT / "drafts" / "reader" / f"{stem}.md").read_text(encoding="utf-8"))
        titles[num] = t

    for i, (num, slug, stem, part, desc) in enumerate(pages):
        prev_link = next_link = None
        if i > 0:
            pn, ps = pages[i - 1][0], pages[i - 1][1]
            prev_link = (f"{pn}-{ps}.html", titles[pn])
        if i < len(pages) - 1:
            nn, ns = pages[i + 1][0], pages[i + 1][1]
            next_link = (f"{nn}-{ns}.html", titles[nn])
        page = render(num, slug, stem, part, desc, prev_link, next_link)
        out = ROOT / "chapters" / f"{num}-{slug}.html"
        out.write_text(page, encoding="utf-8")
        print(f"built chapters/{num}-{slug}.html  ({titles[num]})")

    # ---- index.html ----
    parts: list[tuple[str, list]] = []
    for entry in pages:
        if not parts or parts[-1][0] != entry[3]:
            parts.append((entry[3], []))
        parts[-1][1].append(entry)

    ix = []
    ix.append("<!DOCTYPE html>")
    ix.append('<html lang="en">')
    ix.append("<head>")
    ix.append('<meta charset="utf-8">')
    ix.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    ix.append(f"<title>{SITE} — what twenty school systems admit from the world's literature</title>")
    ix.append('<meta name="description" content="One year, twenty school systems, one question: which outsiders does each country let into its literature classroom, and what does the choice say?">')
    ix.append('<link rel="stylesheet" href="static/style.css">')
    ix.append('<script src="static/theme.js"></script>')
    ix.append("</head>")
    ix.append("<body>")
    ix.append('<header class="site-header">')
    ix.append('  <div class="wrap">')
    ix.append('    <a class="brand" href="index.html">The <span>Window</span></a>')
    ix.append('    <nav class="site-nav" aria-label="Site">')
    ix.append('      <a href="index.html">Contents</a>')
    ix.append('      <a href="about.html">Method</a>')
    ix.append('      <button class="theme-toggle" type="button">☾ Dark</button>')
    ix.append("    </nav>")
    ix.append("  </div>")
    ix.append("</header>")
    ix.append("")
    ix.append('<main class="wrap">')
    ix.append('  <p class="kicker">A book in progress</p>')
    ix.append(f"  <h1>{SITE}</h1>")
    ix.append('  <p class="lede">Every school system opens a window on the world\'s literature. '
              'This book reads the documents that do the opening — exam codifiers, ministry programs, '
              'state anthologies of twenty school systems in one recent year — and asks which outsiders '
              'each country admits into its classroom, through which door, and what each admission is there to do.</p>')
    for part, entries in parts:
        ix.append("  <section>")
        ix.append(f"    <h2>{html.escape(part)}</h2>")
        ix.append('    <ul class="toc">')
        for num, slug, stem, _, desc in entries:
            ix.append(f'      <li><a href="chapters/{num}-{slug}.html">{inline(titles[num])}</a>'
                      f'<br><span class="toc-desc">{inline(desc)}</span></li>')
            if num == "02":
                ix.append('      <li><span class="toc-pending">Belarus — the witness chapter, '
                          "awaiting its reader's testimony.</span></li>")
        ix.append("    </ul>")
        ix.append("  </section>")
    ix.append("</main>")
    ix.append("")
    ix.append('<footer class="site-footer">')
    ix.append('  <div class="wrap">')
    ix.append(f"    <p>{SITE} · drafted and audited by AI agents; read and ruled on by one human reader.</p>")
    ix.append("  </div>")
    ix.append("</footer>")
    ix.append("")
    ix.append("</body>")
    ix.append("</html>")
    (ROOT / "index.html").write_text("\n".join(ix) + "\n", encoding="utf-8")
    print("built index.html")


if __name__ == "__main__":
    main()
