#!/usr/bin/env bash
# Light assembly checks only:
#   1. private-material ignore rules appropriate to this repository
#   2. internal links (future numbered chapter links warn)
#   3. computed index/chapter count
#   4. simple HTML structural-tag balance
#   5. reader-cut provenance for every assembled chapter
#   6. reader-cut body hygiene (no blockquotes; no '(p. ' citation freight)
set -u
cd "$(dirname "$0")"
shopt -s nullglob
fail=0; warn=0
err() { echo "FAIL  $*"; fail=$((fail + 1)); }
wrn() { echo "warn  $*"; warn=$((warn + 1)); }
ok()  { echo "ok    $*"; }

chapter_files=(chapters/*.html)

# ---- 1. private material --------------------------------------------------
ignorefail=0
for d in resources/ tools/log/; do
  if ! grep -qxF "$d" .gitignore; then
    err "anti-leak: '$d' missing from .gitignore"
    ignorefail=1
  fi
done
if [ -d .git ]; then
  leaked=$(git ls-files | grep -E '^(resources|tools/log)/|\.pdf$' || true)
  if [ -n "$leaked" ]; then
    err "anti-leak: private material is tracked by git:"
    echo "$leaked" | sed 's/^/        /'
    ignorefail=1
  fi
fi
[ "$ignorefail" -eq 0 ] && ok "anti-leak (.gitignore complete$( [ -d .git ] && echo ', no tracked private files' || echo ', git not initialized' ))"

# ---- 2. internal links ----------------------------------------------------
linkfail=0
for f in index.html about.html "${chapter_files[@]}"; do
  [ -f "$f" ] || continue
  dir=$(dirname "$f")
  while IFS= read -r ref; do
    case "$ref" in
      http*|mailto:*|\#*) continue ;;
    esac
    target="$dir/${ref%%#*}"
    if [ ! -f "$target" ]; then
      if [[ "$ref" =~ (^|/)[0-9]{2}-[^/]+\.html$ ]]; then
        wrn "link: $f -> $ref (future chapter, not written yet)"
      else
        err "link: $f -> $ref (missing)"
        linkfail=1
      fi
    fi
  done < <(grep -oE '(href|src)="[^"]+"' "$f" | sed -E 's/^(href|src)="//; s/"$//')
done
[ "$linkfail" -eq 0 ] && ok "internal links (stubs to future chapters are warnings)"

# ---- 3. chapter count sync ------------------------------------------------
if [ -f index.html ]; then
  nfiles=${#chapter_files[@]}
  nlinks=$(grep -oE 'href="chapters/[^"]+\.html"' index.html | sort -u | wc -l)
  if [ "$nfiles" -ne "$nlinks" ]; then
    err "count sync: $nfiles chapter file(s) but $nlinks chapter link(s) in index.html"
  else
    ok "count sync ($nfiles chapters, $nlinks index links)"
  fi
else
  wrn "count sync: index.html has not been assembled yet"
fi

# ---- 4. HTML nesting ------------------------------------------------------
nestfail=0
for f in index.html about.html "${chapter_files[@]}"; do
  [ -f "$f" ] || continue
  for tag in div section table thead tbody tr ul ol main nav header footer; do
    o=$(grep -oE "<$tag( [^>]*)?>" "$f" | wc -l)
    c=$(grep -oF "</$tag>" "$f" | wc -l)
    if [ "$o" -ne "$c" ]; then
      err "nesting: $f <$tag> open=$o close=$c"
      nestfail=1
    fi
  done
done
[ "$nestfail" -eq 0 ] && ok "HTML nesting"

# ---- 5. reader-cut provenance --------------------------------------------
sourcefail=0
while IFS= read -r -d '' f; do
  case "$f" in
    chapters/.gitkeep) continue ;;
    *.html) ;;
    *) err "source trace: $f is not an HTML chapter page"; sourcefail=1; continue ;;
  esac
  sources=$(sed -nE 's@^[[:space:]]*<!--[[:space:]]source:[[:space:]](drafts/reader/[[:alnum:]_.-]+\.md)[[:space:]]-->[[:space:]]*$@\1@p' "$f")
  nsource=$(printf '%s\n' "$sources" | sed '/^$/d' | wc -l)
  if [ "$nsource" -ne 1 ]; then
    err "source trace: $f has $nsource source comments (want exactly 1)"
    sourcefail=1
    continue
  fi
  if [ ! -f "$sources" ]; then
    err "source trace: $f -> $sources (missing reader cut)"
    sourcefail=1
  fi
done < <(find chapters -type f -print0)
[ "$sourcefail" -eq 0 ] && ok "reader-cut provenance"

# ---- 6. chapter-body hygiene ---------------------------------------------
bodyfail=0
for f in "${chapter_files[@]}"; do
  body=$(sed -n '/<body[[:space:]>]/,/<\/body>/p' "$f")
  if printf '%s\n' "$body" | grep -Eiq '<[[:space:]]*blockquote([[:space:]>])'; then
    err "body hygiene: $f contains <blockquote>"
    bodyfail=1
  fi
  if printf '%s\n' "$body" | grep -Eiq '\(p\.[[:space:]]'; then
    err "body hygiene: $f contains parenthetical page citation freight"
    bodyfail=1
  fi
done
[ "$bodyfail" -eq 0 ] && ok "chapter-body hygiene (no blockquotes; no '(p. ' freight)"

echo
if [ "$fail" -gt 0 ]; then
  echo "verify: $fail FAILURE(S), $warn warning(s)"
  exit 1
fi
echo "verify: all checks passed, $warn warning(s)"
