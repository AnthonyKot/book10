# Book10 — chapter HTML template

Use this only to assemble a ready reader cut. Replace every `{{…}}` token, retain one
valid source comment, and remove unused optional blocks. Do not place `<blockquote>` or
parenthetical page citations such as `(p. 12)` in `<body>`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- source: drafts/reader/{{SOURCE_FILE}}.md -->
<title>{{CHAPTER_TITLE}} — {{SITE_TITLE}}</title>
<meta name="description" content="{{ONE-SENTENCE DESCRIPTION}}">
<link rel="stylesheet" href="../static/style.css">
<script src="../static/theme.js"></script>
</head>
<body>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="../index.html">{{SITE_TITLE}}</a>
    <nav class="site-nav" aria-label="Site">
      <a href="../index.html">Contents</a>
      <a href="../about.html">Method</a>
      <button class="theme-toggle" type="button">☾ Dark</button>
    </nav>
  </div>
</header>

<main class="wrap">
  <p class="kicker">{{PART OR CHAPTER LABEL}}</p>
  <h1>{{CHAPTER_TITLE}}</h1>
  <p class="lede">{{CONCRETE OPENING FROM THE READER CUT}}</p>

  <section>
    <h2>{{THE DOOR / INSTRUMENT}}</h2>
    <p>{{READER-CUT PROSE}}</p>
  </section>

  <section>
    <h2>{{WHAT THE DOCUMENT DOES}}</h2>
    <p>{{READER-CUT PROSE}}</p>
  </section>

  <section>
    <h2>{{WHAT THE SHELF / WINDOW SHOWS}}</h2>
    <p>{{READER-CUT PROSE}}</p>
    <!-- Optional: use a table for measured rows, labels, or comparisons. -->
  </section>

  <!-- Optional quotation treatment: never use a blockquote. -->
  <div class="pull" role="note">
    <p>{{SHORT QUOTATION OR DOCUMENT LINE}}</p>
    <p class="cite">{{DOCUMENT / EDITION LABEL, WITHOUT PARENTHETICAL PAGE FREIGHT}}</p>
  </div>

  <section>
    <h2>Where this stops being true</h2>
    <div class="limits">
      <p>{{LIMITS PRESERVED FROM THE READER CUT}}</p>
    </div>
  </section>

  <section>
    <h2>Receipts</h2>
    <div class="receipts">
      <ul>
        <li>{{DOCUMENT, EDITION/YEAR, AND THE NARROW CLAIM IT SUPPORTS}}</li>
      </ul>
    </div>
  </section>

  <nav class="chapter-nav" aria-label="Chapter">
    <a href="{{PREVIOUS_PAGE}}">← {{PREVIOUS_LABEL}}</a>
    <a href="{{NEXT_PAGE}}">{{NEXT_LABEL}} →</a>
  </nav>
</main>

<footer class="site-footer">
  <div class="wrap">
    <p>{{SITE_TITLE}} · {{CHAPTER_LABEL}}</p>
  </div>
</footer>

</body>
</html>
```

The source comment must name a real file directly under `drafts/reader/`, for example
`<!-- source: drafts/reader/ua.md -->`. `verify.sh` reads that exact form.
