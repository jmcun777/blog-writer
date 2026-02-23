#!/usr/bin/env python3
import json
import pathlib
import html
import re

ROOT = pathlib.Path('/home/tz/.openclaw/workspace-dev')
DIST = ROOT / 'dist'
OUT = ROOT / 'review.html'


def infer_tags(name: str):
    # name like YYYY-MM-DD-slug-words
    s = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', name)
    words = [w for w in s.replace('-', ' ').split() if w]
    return ', '.join(words[:6]) if words else 'china payroll, eor'


def load_prompt_preview(post_dir: pathlib.Path):
    p = post_dir / 'image_prompt.txt'
    if not p.exists():
        return '', ''
    txt = p.read_text(encoding='utf-8').strip().replace('\n', ' ')
    preview = txt[:180] + ('…' if len(txt) > 180 else '')
    return preview, './dist/' + post_dir.name + '/image_prompt.txt'


def load_tags(post_dir: pathlib.Path):
    # optional manual tags file in each dist post dir
    t = post_dir / 'tags.txt'
    if t.exists():
        return t.read_text(encoding='utf-8').strip()
    return infer_tags(post_dir.name)


def load_title(post_dir: pathlib.Path):
    idx = post_dir / 'index.html'
    if not idx.exists():
        return post_dir.name
    txt = idx.read_text(encoding='utf-8', errors='ignore')
    m = re.search(r'<h1[^>]*>(.*?)</h1>', txt, flags=re.I | re.S)
    if not m:
        return post_dir.name
    title = re.sub(r'\s+', ' ', m.group(1)).strip()
    title = re.sub(r'<[^>]+>', '', title)
    return title or post_dir.name


posts = sorted([p for p in DIST.iterdir() if p.is_dir() and (p / 'index.html').exists()], reverse=True)

rows = []
for p in posts:
    rel = f"./dist/{p.name}/"
    date = p.name[:10] if re.match(r'^\d{4}-\d{2}-\d{2}', p.name) else '-'
    title = html.escape(load_title(p))
    prompt_preview, prompt_link = load_prompt_preview(p)
    prompt_preview = html.escape(prompt_preview)
    tags = html.escape(load_tags(p))
    prompt_cell = f"<code>{prompt_preview}</code><div style='margin-top:6px'><a href=\"{prompt_link}\" target=\"_blank\">Full prompt (txt)</a></div>" if prompt_link else "-"
    rows.append(f"""
      <tr>
        <td>{date}</td>
        <td><a href=\"{rel}\" target=\"_blank\"><strong>{title}</strong></a></td>
        <td>{prompt_cell}</td>
        <td>{tags}</td>
      </tr>
    """)

page = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\" />
  <title>Editorial Pre-Review Table</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 28px auto; max-width: 1200px; padding: 0 16px; }}
    h1 {{ margin-bottom: 6px; }}
    .hint {{ color: #666; margin-bottom: 16px; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ border: 1px solid #ddd; padding: 10px; vertical-align: top; text-align: left; }}
    th {{ background: #f5f7ff; }}
    code {{ white-space: pre-wrap; word-break: break-word; background: #f6f6f6; padding: 6px; display:block; border-radius:6px; }}
    a {{ color: #0b5fff; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <h1>Editorial Pre-Review Table</h1>
  <p class=\"hint\">Daily draft entries for remote reviewer. Columns: article link, recommended image prompt, and tags/keywords.</p>
  <table>
    <thead>
      <tr>
        <th style=\"width:120px\">Date</th>
        <th style=\"width:340px\">Article Details</th>
        <th>Recommended Image Prompt</th>
        <th style=\"width:260px\">Tags / Keywords</th>
      </tr>
    </thead>
    <tbody>
      {''.join(rows) if rows else '<tr><td colspan="4">No posts yet.</td></tr>'}
    </tbody>
  </table>
</body>
</html>
"""

OUT.write_text(page, encoding='utf-8')
print(str(OUT))
