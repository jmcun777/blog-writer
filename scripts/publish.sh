#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <draft.md> [YYYY-MM-DD]"
  exit 1
fi

DRAFT="$1"
DATE="${2:-$(date +%F)}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

python3 "$ROOT/scripts/publish.py" \
  --draft "$DRAFT" \
  --template "$ROOT/templates/post.html" \
  --dist-root "$ROOT/dist" \
  --date "$DATE"

python3 "$ROOT/scripts/build_review_table.py"

# Update root index with latest 20 posts
python3 - <<'PY'
import pathlib, re
root = pathlib.Path('/home/tz/.openclaw/workspace-dev')
d = root / 'dist'
posts = sorted([p for p in d.iterdir() if p.is_dir() and (p/'index.html').exists()], reverse=True)[:20]
items = []
for p in posts:
    label = p.name
    items.append(f'<li><a href="./dist/{label}/">{label}</a></li>')
html = f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>China Payroll Blog</title></head><body style="font-family:Arial,sans-serif;max-width:900px;margin:30px auto;padding:0 16px"><h1>China Payroll Blog</h1><p><a href="./review.html">Open Pre-Review Table</a></p><p>Latest posts:</p><ul>{''.join(items)}</ul></body></html>'''
(root/'index.html').write_text(html, encoding='utf-8')
print('updated index.html')
PY

echo "Publish artifacts generated."
